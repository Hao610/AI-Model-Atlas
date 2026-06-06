from collections import defaultdict

class Reranker:
    def __init__(self):
        pass

    def rerank(self, dense_matches: list[dict], sparse_matches: list[dict], active: bool = True, top_k: int = 5) -> list[dict]:
        """Fuses Dense and Sparse results using Reciprocal Rank Fusion (RRF)."""
        if not active:
            # If inactive, just return the dense matches as a fallback
            return dense_matches[:top_k]
            
        rrf_scores = defaultdict(float)
        doc_lookup = {}
        
        # 1. Dense Contribution
        for rank, doc in enumerate(dense_matches, start=1):
            doc_id = doc["id"]
            if doc_id not in doc_lookup:
                doc_lookup[doc_id] = doc
            rrf_scores[doc_id] += 1.0 / (60 + rank)
            
        # 2. Sparse (BM25) Contribution
        for rank, doc in enumerate(sparse_matches, start=1):
            doc_id = doc["id"]
            if doc_id not in doc_lookup:
                doc_lookup[doc_id] = doc
            rrf_scores[doc_id] += 1.0 / (60 + rank)
            
        # 3. Fuse and sort
        fused_docs = []
        for doc_id, score in rrf_scores.items():
            item = doc_lookup[doc_id].copy()
            item["rrf_score"] = score
            fused_docs.append(item)
            
        # Sort by RRF score descending
        fused_docs.sort(key=lambda x: x["rrf_score"], reverse=True)
        
        return fused_docs[:top_k]
