import os
import time
from pypdf import PdfReader
from core.embeddings import EmbeddingsManager
from core.chunking import recursive_character_chunking
from core.vectorstore import VectorStoreManager
from core.llm_router import LLMRouter
from core.execution_controller import ExecutionController
from core.intelligence.query_rewriter import QueryRewriter
from core.intelligence.reranker import Reranker
from core.cache.semantic_cache import SemanticCache
from core.cache.cache_metrics import CacheMetrics
from core.tools.router import ToolRouter, ToolType
from core.tools.calculator import CalculatorTool
from core.tools.web import WebSearchTool
from config.settings import settings

class RAGPipeline:
    def __init__(self):
        self.embeddings = EmbeddingsManager()
        self.vectorstore = VectorStoreManager(self.embeddings)
        self.router = LLMRouter()
        self.controller = ExecutionController(self.router)
        self.rewriter = QueryRewriter(self.router)
        self.reranker = Reranker()
        self.cache = SemanticCache(self.embeddings)
        self.metrics = CacheMetrics()
        self.tool_router = ToolRouter()
        self.calculator = CalculatorTool()
        self.web_search = WebSearchTool()
        self.traces = [] # Stores PipelineTrace dictionaries for Stage B Evaluation
        self.collection_name = "default_rag"
        
    def reload_llm(self):
        """Reloads the LLM router and its dependents without reloading embeddings or vectorstore."""
        self.router = LLMRouter()
        self.controller.router = self.router
        self.rewriter.router = self.router
        
    def ingest_pdf(self, file_path: str, chunk_size: int = 800, chunk_overlap: int = 100) -> int:
        """Parses a PDF, chunks it recursively, embeds it, and indexes it into ChromaDB."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
            
        reader = PdfReader(file_path)
        full_text = ""
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                full_text += f"\n--- PAGE {i+1} ---\n" + text
                
        # Split text into chunks
        chunks = recursive_character_chunking(
            text=full_text,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        
        # Clear vectorstore cache for this document
        self.vectorstore.reset_collection(self.collection_name)
        
        # Ingest into vector store
        file_name = os.path.basename(file_path)
        metadatas = [{"source": file_name, "chunk_index": idx} for idx, _ in enumerate(chunks)]
        ids = [f"{file_name}_chunk_{idx}" for idx, _ in enumerate(chunks)]
        
        if chunks:
            self.vectorstore.add_documents(
                collection_name=self.collection_name,
                texts=chunks,
                metadatas=metadatas,
                ids=ids
            )
            
        return len(chunks)
        
    def execute_query(self, query: str, system_prompt: str = None, max_results: int = 4, 
                      rewrite_active: bool = True, rerank_active: bool = True, rerank_threshold: float = 1.5,
                      cache_active: bool = True, cache_threshold: float = 0.9):
        """Retrieves contexts, optimizes using intelligence modules, and yields streams."""
        start_time = time.time()
        
        # 0. Tool Routing Layer (Stage A)
        self.controller.log("Analyzing intent via ToolRouter...")
        route_decision = self.tool_router.route(query)
        
        # Initialize PipelineTrace
        trace = {
            "query": query,
            "route": route_decision.tool.value,
            "confidence": route_decision.confidence,
            "reason": route_decision.reason,
            "retrieved_docs": [],
            "answer": "",
            "latency": 0.0
        }
        
        # Handle Non-RAG Routes (Calculator / Web)
        if route_decision.tool == ToolType.CALCULATOR:
            self.controller.log("Router dispatched to CalculatorTool.")
            result = self.calculator.run(query)
            trace["answer"] = result
            trace["latency"] = time.time() - start_time
            self.traces.append(trace)
            def calc_stream():
                yield f"🧮 **Calculator Result:**\n`{result}`"
            return calc_stream(), []
            
        elif route_decision.tool == ToolType.WEB:
            self.controller.log("Router dispatched to WebSearchTool.")
            result = self.web_search.run(query)
            trace["answer"] = result
            trace["latency"] = time.time() - start_time
            self.traces.append(trace)
            def web_stream():
                yield f"🌐 **Web Search Action:**\n{result}"
            return web_stream(), []

        # 1. Semantic Cache check
        if cache_active:
            self.controller.log("Checking Semantic Cache...")
            start_cache = time.time()
            cached_response = self.cache.check(query, threshold=cache_threshold)
            duration = time.time() - start_cache
            
            if cached_response is not None:
                self.controller.log(f"Cache Hit! Retained answer from memory. Latency Saved: {duration:.4f}s")
                self.metrics.record_hit(duration)
                
                # Yield cached stream instantly
                def cached_stream():
                    yield cached_response
                    
                trace["answer"] = cached_response
                trace["latency"] = duration
                self.traces.append(trace)
                return cached_stream(), []
            else:
                self.controller.log("Cache Miss. Continuing vector retrieval workflow.")
                self.metrics.record_miss()

        # 2. Query Rewriting optimization
        optimized_query = self.rewriter.rewrite(query, active=rewrite_active)
        self.controller.log(f"Original Query: '{query}' | Rewritten to: '{optimized_query}'")
        
        # 3. Hybrid Dual Retrieval
        hybrid_results = self.vectorstore.hybrid_query(
            collection_name=self.collection_name,
            query_text=optimized_query,
            n_results=max_results * 2 # fetch more to give RRF a larger pool
        )
        dense_matches = hybrid_results["dense_matches"]
        sparse_matches = hybrid_results["sparse_matches"]
        
        self.controller.log(f"Vector Search: {len(dense_matches)} docs retrieved.")
        self.controller.log(f"BM25 Search: {len(sparse_matches)} docs retrieved.")
        
        # 4. Reciprocal Rank Fusion (RRF) Reranking
        filtered_matches = self.reranker.rerank(
            dense_matches=dense_matches,
            sparse_matches=sparse_matches,
            active=rerank_active, 
            top_k=max_results
        )
        self.controller.log(f"RRF Fusion: {len(dense_matches)} + {len(sparse_matches)} -> {len(filtered_matches)} docs.")
        
        if dense_matches:
            self.controller.log("Dense Top3: " + ", ".join(d["id"] for d in dense_matches[:3]))
        if sparse_matches:
            self.controller.log("Sparse Top3: " + ", ".join(d["id"] for d in sparse_matches[:3]))
        if filtered_matches:
            self.controller.log("Fused Top3: " + ", ".join(d["id"] for d in filtered_matches[:3]))
        
        context_str = ""
        sources = []
        for match in filtered_matches:
            context_str += f"\n[Source: {match['metadata'].get('source', 'Unknown')}]\n{match['content']}\n"
            sources.append(match)
            
        trace["retrieved_docs"] = [m["id"] for m in sources]
            
        # Dispatch execution and return control flows
        stream = self.controller.execute(
            query=query,
            context_str=context_str,
            system_prompt=system_prompt
        )
        
        # Wrap stream to cache the generated output on completion and log trace
        def stream_cacher():
            collected_response = ""
            for chunk in stream:
                collected_response += chunk
                yield chunk
            
            # Finalize Trace
            trace["answer"] = collected_response
            trace["latency"] = time.time() - start_time
            self.traces.append(trace)
            
            if cache_active and collected_response and "⚠️" not in collected_response:
                self.cache.put(query, collected_response)
                self.controller.log("Successfully cached response mapping in Semantic Cache memory.")
                
        return stream_cacher(), sources
