class Reranker:
    def __init__(self):
        pass

    def rerank(self, matches: list[dict], query: str, active: bool = True, distance_threshold: float = 1.5) -> list[dict]:
        """Filters ChromaDB cosine similarity matches by distance boundaries.
        
        Note: Cosine distance is used in ChromaDB where 0.0 means identical 
        and values closer to 2.0 indicate high distance/dissimilarity.
        """
        if not active:
            return matches
            
        # Filter matching chunks that exceed distance thresholds
        reranked = [
            match for match in matches 
            if match.get("score", 0.0) <= distance_threshold
        ]
        
        # Sort matched chunks by similarity distance (ascending order of distance metrics)
        reranked.sort(key=lambda x: x.get("score", 0.0))
        return reranked
