import os
from pypdf import PdfReader
from core.embeddings import EmbeddingsManager
from core.chunking import recursive_character_chunking
from core.vectorstore import VectorStoreManager
from core.llm_router import LLMRouter
from config.settings import settings

class RAGPipeline:
    def __init__(self):
        self.embeddings = EmbeddingsManager()
        self.vectorstore = VectorStoreManager(self.embeddings)
        self.router = LLMRouter()
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
        
    def execute_query(self, query: str, system_prompt: str = None, max_results: int = 4):
        """Retrieves contexts, builds prompt structure, and yields response streams."""
        # Retrieve matched contexts
        matches = self.vectorstore.query(
            collection_name=self.collection_name,
            query_text=query,
            n_results=max_results
        )
        
        context_str = ""
        sources = []
        for match in matches:
            context_str += f"\n[Source: {match['metadata'].get('source', 'Unknown')}]\n{match['content']}\n"
            sources.append(match)
            
        if not system_prompt:
            system_prompt = (
                "You are a helpful AI assistant representing the AI-Model-Atlas RAG pipeline.\n"
                "Answer the user's questions truthfully and accurately based strictly on the provided context.\n"
                "If the context does not contain the answer, state that you do not know."
            )
            
        user_prompt = (
            f"Context Information:\n{context_str}\n\n"
            f"User Question: {query}\n\n"
            f"Provide an answer utilizing the context above."
        )
        
        # Stream response
        stream = self.router.generate_stream(system_prompt, user_prompt)
        
        return stream, sources
