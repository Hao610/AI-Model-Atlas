import json
import logging
from typing import List, Dict, Any
from core.llm_router import LLMRouter
from core.graph.graph_store import GraphStore

logger = logging.getLogger(__name__)

class GraphRetriever:
    def __init__(self, llm_router: LLMRouter, store: GraphStore):
        self.llm = llm_router
        self.store = store

    def retrieve(self, query: str) -> str:
        """Extracts entities from query and retrieves 1-hop graph neighbors as text context."""
        entities = self._extract_query_entities(query)
        if not entities:
            return ""
            
        context_lines = []
        for entity in entities:
            neighbors = self.store.get_neighbors(entity)
            for n in neighbors:
                # Format: Graph Knowledge: [RRF] --(fuses scores with)--> [BM25] (Evidence: rag.pdf, Chunk: chunk_438)
                line = f"Graph Knowledge: [{n['source']}] --({n['relation']})--> [{n['target']}] " \
                       f"(Evidence: {n['evidence']['source_doc']}, Chunk: {n['evidence']['chunk_id']})"
                context_lines.append(line)
                
        unique_lines = list(set(context_lines))
        return "\n".join(unique_lines)
        
    def _extract_query_entities(self, query: str) -> List[str]:
        sys_prompt = "You extract key entities from a query. Return ONLY a valid JSON list of strings."
        user_prompt = f"""
Extract the core entities/concepts from this question to search a Knowledge Graph.
Do not extract question words (what, how, why).

Question: {query}
Output Format: ["Entity1", "Entity2"]
"""
        response = self.llm.generate(sys_prompt, user_prompt)
        try:
            if "```json" in response:
                response = response.split("```json")[1].split("```")[0].strip()
            elif "```" in response:
                response = response.split("```")[1].split("```")[0].strip()
            return json.loads(response)
        except Exception:
            return []
