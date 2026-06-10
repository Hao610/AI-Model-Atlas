import os
import chromadb
from chromadb.config import Settings as ChromaSettings
from config.settings import settings
from rank_bm25 import BM25Okapi
import jieba

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
        
        # Default collection used by the app
        self.default_collection_name = "default_rag"
        
        # BM25 State
        self.bm25_index = None
        self.bm25_corpus = []
        self.bm25_doc_map = []
        
        # Parent-Child Document Store
        self.doc_store = {}
        
        # Restore BM25 from ChromaDB on startup
        self._rebuild_bm25(self.default_collection_name)
        
    def get_or_create_collection(self, collection_name: str = "default_rag"):
        return self.chroma_client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embedding_fn
        )
        
    def _rebuild_bm25(self, collection_name: str):
        """Rebuilds the BM25 index from all existing Chroma documents."""
        collection = self.get_or_create_collection(collection_name)
        results = collection.get()
        
        documents = results.get("documents", [])
        metadatas = results.get("metadatas", [])
        ids = results.get("ids", [])
        
        if not documents:
            self.bm25_index = None
            self.bm25_corpus = []
            self.bm25_doc_map = []
            return
            
        tokenized_corpus = []
        doc_map = []
        
        for doc_id, doc_text, metadata in zip(ids, documents, metadatas):
            # Jieba handles both English splits and Chinese tokenization well
            tokens = jieba.lcut(doc_text)
            tokenized_corpus.append(tokens)
            doc_map.append({
                "id": doc_id,
                "content": doc_text,
                "metadata": metadata
            })
            self.doc_store[doc_id] = {
                "content": doc_text,
                "metadata": metadata
            }
            
        self.bm25_corpus = tokenized_corpus
        self.bm25_doc_map = doc_map
        self.bm25_index = BM25Okapi(tokenized_corpus)
        
    def add_documents(self, collection_name: str, texts: list[str], metadatas: list[dict], ids: list[str]):
        collection = self.get_or_create_collection(collection_name)
        
        # Populate parent_id for child documents and save to self.doc_store
        for doc_id, meta, text in zip(ids, metadatas, texts):
            is_child = meta.get("is_child", False)
            is_child_bool = str(is_child).lower() == "true" if is_child is not None else False
            parent_chunk_index = meta.get("parent_chunk_index", -1)
            
            if is_child_bool and parent_chunk_index != -1:
                if "_chunk_" in doc_id:
                    prefix = doc_id.rsplit("_chunk_", 1)[0]
                    parent_id = f"{prefix}_chunk_{parent_chunk_index}"
                    meta["parent_id"] = parent_id
                else:
                    meta["parent_id"] = ""
            else:
                meta["parent_id"] = ""
                
            self.doc_store[doc_id] = {
                "content": text,
                "metadata": meta
            }
            
        collection.add(
            documents=texts,
            metadatas=metadatas,
            ids=ids
        )
        # Rebuild BM25 after new documents are ingested to keep them in sync
        self._rebuild_bm25(collection_name)
        
    def hybrid_query(self, collection_name: str, query_text: str, n_results: int = 10) -> dict:
        """Executes Dual Retrieval (Dense + Sparse) and returns both match lists."""
        collection = self.get_or_create_collection(collection_name)
        
        # --- 1. Dense Search (Chroma) ---
        dense_results = collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        
        dense_matches = []
        if dense_results and "documents" in dense_results and dense_results["documents"]:
            docs = dense_results["documents"][0]
            metas = dense_results["metadatas"][0] if "metadatas" in dense_results else [{}]*len(docs)
            distances = dense_results["distances"][0] if "distances" in dense_results else [0.0]*len(docs)
            ids = dense_results["ids"][0]
            
            for doc, meta, dist, doc_id in zip(docs, metas, distances, ids):
                dense_matches.append({
                    "id": doc_id,
                    "content": doc,
                    "metadata": meta,
                    "score": float(dist) # distance metric
                })
                
        # --- 2. Sparse Search (BM25) ---
        sparse_matches = []
        if self.bm25_index:
            query_tokens = jieba.lcut(query_text)
            scores = self.bm25_index.get_scores(query_tokens)
            
            # Sort by highest BM25 score
            ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
            
            for idx, score in ranked[:n_results]:
                # Exclude zero scores
                if score <= 0.0:
                    continue
                doc = self.bm25_doc_map[idx]
                sparse_matches.append({
                    "id": doc["id"],
                    "content": doc["content"],
                    "metadata": doc["metadata"],
                    "score": float(score) # frequency metric
                })
                
        # --- Resolve Child Chunks to Parent Chunks ---
        def resolve_parents(matches):
            resolved = []
            seen = set()
            for m in matches:
                meta = m["metadata"]
                is_child = meta.get("is_child", False)
                is_child_bool = str(is_child).lower() == "true" if is_child is not None else False
                parent_id = meta.get("parent_id")
                
                if is_child_bool and parent_id:
                    if parent_id not in seen:
                        parent_chunk = self.doc_store.get(parent_id)
                        if parent_chunk:
                            resolved.append({
                                "id": parent_id,
                                "content": parent_chunk["content"],
                                "metadata": parent_chunk["metadata"],
                                "score": m["score"]
                            })
                            seen.add(parent_id)
                else:
                    doc_id = m["id"]
                    if doc_id not in seen:
                        resolved.append(m)
                        seen.add(doc_id)
            return resolved

        return {
            "dense_matches": resolve_parents(dense_matches),
            "sparse_matches": resolve_parents(sparse_matches)
        }

    def reset_collection(self, collection_name: str):
        try:
            self.chroma_client.delete_collection(name=collection_name)
        except Exception:
            pass
        self.get_or_create_collection(collection_name)
        self._rebuild_bm25(collection_name)
