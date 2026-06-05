import os
import chromadb
from chromadb.config import Settings as ChromaSettings
from config.settings import settings

class VectorStoreManager:
    def __init__(self, embedding_manager):
        self.embeddings = embedding_manager
        
        # Ensure persistence directory exists
        os.makedirs(settings.DB_DIR, exist_ok=True)
        
        self.chroma_client = chromadb.PersistentClient(path=settings.DB_DIR)
        
        # Custom embedding function adapter for ChromaDB
        class ChromaEmbeddingAdapter:
            def __init__(self, embedder):
                self.embedder = embedder
            def __call__(self, input):
                return self.embedder.embed_documents(input)
                
        self.embedding_fn = ChromaEmbeddingAdapter(self.embeddings)
        
    def get_or_create_collection(self, collection_name: str = "rag_collection"):
        return self.chroma_client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embedding_fn
        )
        
    def add_documents(self, collection_name: str, texts: list[str], metadatas: list[dict], ids: list[str]):
        collection = self.get_or_create_collection(collection_name)
        collection.add(
            documents=texts,
            metadatas=metadatas,
            ids=ids
        )
        
    def query(self, collection_name: str, query_text: str, n_results: int = 4) -> list[dict]:
        """Queries the vector store and returns matching documents with scores."""
        collection = self.get_or_create_collection(collection_name)
        results = collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        
        formatted_results = []
        if results and "documents" in results and results["documents"]:
            docs = results["documents"][0]
            metas = results["metadatas"][0] if "metadatas" in results else [{}]*len(docs)
            distances = results["distances"][0] if "distances" in results else [0.0]*len(docs)
            ids = results["ids"][0]
            
            for doc, meta, dist, doc_id in zip(docs, metas, distances, ids):
                formatted_results.append({
                    "id": doc_id,
                    "content": doc,
                    "metadata": meta,
                    "score": float(dist) # distance metric
                })
        return formatted_results

    def reset_collection(self, collection_name: str):
        try:
            self.chroma_client.delete_collection(name=collection_name)
        except Exception:
            pass
        self.get_or_create_collection(collection_name)
