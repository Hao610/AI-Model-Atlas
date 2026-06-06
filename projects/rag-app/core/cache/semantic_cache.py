import os
import json
import numpy as np
from config.settings import settings

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
        self.cache_file = settings.CACHE_FILE
        self.store = []
        self._load_cache()

    def _load_cache(self):
        """Loads semantic cache from persistent JSON file."""
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, "r", encoding="utf-8") as f:
                    self.store = json.load(f)
            except Exception:
                self.store = []

    def _save_cache(self):
        """Saves semantic cache to persistent JSON file."""
        os.makedirs(os.path.dirname(self.cache_file), exist_ok=True)
        try:
            with open(self.cache_file, "w", encoding="utf-8") as f:
                json.dump(self.store, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Failed to save semantic cache: {e}")

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
        # Ensure embedding is a list of floats for JSON serialization
        if isinstance(query_vector, np.ndarray):
            query_vector = query_vector.tolist()
            
        self.store.append({
            "query": query,
            "embedding": query_vector,
            "response": response,
            "intent_len": len(query)
        })
        self._save_cache()

    def clear(self):
        self.store.clear()
        self._save_cache()
