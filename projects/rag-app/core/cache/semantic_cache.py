import numpy as np

def cosine_similarity(v1: list[float], v2: list[float]) -> float:
    a = np.array(v1)
    b = np.array(v2)
    dot = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(dot / (norm_a * norm_b))

class SemanticCache:
    def __init__(self, embedding_manager):
        self.embeddings = embedding_manager
        # In-memory storage list containing dict objects: 
        # {"query": str, "embedding": list[float], "response": str, "intent_len": int}
        self.store = []

    def check(self, query: str, threshold: float = 0.9) -> str | None:
        """Finds cached answers by measuring embedding distance similarity."""
        if not self.store:
            return None
            
        query_vector = self.embeddings.embed_query(query)
        best_similarity = -1.0
        best_match = None
        
        for entry in self.store:
            similarity = cosine_similarity(query_vector, entry["embedding"])
            # Fallback constraint safeguard: Verify similarity and response length variance
            if similarity > threshold:
                if similarity > best_similarity:
                    # Guard logic: Ensure query length ratio similarity to avoid semantic false positives
                    length_ratio = min(len(query), len(entry["query"])) / max(len(query), len(entry["query"]))
                    if length_ratio > 0.4:
                        best_similarity = similarity
                        best_match = entry
                        
        if best_match:
            return best_match["response"]
        return None

    def put(self, query: str, response: str):
        """Saves a query vector pair to the semantic cache database."""
        query_vector = self.embeddings.embed_query(query)
        self.store.append({
            "query": query,
            "embedding": query_vector,
            "response": response,
            "intent_len": len(query)
        })

    def clear(self):
        self.store.clear()
