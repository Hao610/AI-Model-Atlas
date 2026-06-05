import re

class QueryRewriter:
    def __init__(self, llm_router=None):
        self.router = llm_router

    def rewrite(self, query: str, active: bool = True) -> str:
        """Optimizes conversational user search terms for vector database search queries."""
        if not active:
            return query
            
        # Strip common conversational prefixes (English & Chinese)
        clean_query = query.strip()
        conversational_patterns = [
            r"^(please tell me|can you explain|what is|how do i|tell me about)\s+",
            r"^(请问|我想知道|你能解释一下|什么是|怎么|关于|介绍一下)\s*"
        ]
        
        for pattern in conversational_patterns:
            clean_query = re.sub(pattern, "", clean_query, flags=re.IGNORECASE)
            
        # Clean question marks and ending punctuation
        clean_query = re.sub(r"[?？.!。!！]+$", "", clean_query)
        
        # Simple heuristics: keyword expansion fallback
        if not clean_query.strip():
            return query
            
        return clean_query.strip()
