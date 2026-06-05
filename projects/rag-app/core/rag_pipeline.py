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
        self.collection_name = "default_rag"
        
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
                return cached_stream(), []
            else:
                self.controller.log("Cache Miss. Continuing vector retrieval workflow.")
                self.metrics.record_miss()

        # 2. Query Rewriting optimization
        optimized_query = self.rewriter.rewrite(query, active=rewrite_active)
        self.controller.log(f"Original Query: '{query}' | Rewritten to: '{optimized_query}'")
        
        # 3. Retrieve matched contexts
        matches = self.vectorstore.query(
            collection_name=self.collection_name,
            query_text=optimized_query,
            n_results=max_results
        )
        
        # 4. Relevance Reranking
        filtered_matches = self.reranker.rerank(
            matches, 
            query=optimized_query, 
            active=rerank_active, 
            distance_threshold=rerank_threshold
        )
        self.controller.log(f"Vector search matched {len(matches)} chunks. Rerank filter retained {len(filtered_matches)} chunks.")
        
        context_str = ""
        sources = []
        for match in filtered_matches:
            context_str += f"\n[Source: {match['metadata'].get('source', 'Unknown')}]\n{match['content']}\n"
            sources.append(match)
            
        # Dispatch execution and return control flows
        stream = self.controller.execute(
            query=query,
            context_str=context_str,
            system_prompt=system_prompt
        )
        
        # Wrap stream to cache the generated output on completion
        def stream_cacher():
            collected_response = ""
            for chunk in stream:
                collected_response += chunk
                yield chunk
            if cache_active and collected_response and "⚠️" not in collected_response:
                self.cache.put(query, collected_response)
                self.controller.log("Successfully cached response mapping in Semantic Cache memory.")
                
        return stream_cacher(), sources
