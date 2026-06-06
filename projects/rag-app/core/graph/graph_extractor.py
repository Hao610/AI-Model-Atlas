import json
import logging
from typing import List, Dict, Any
from core.llm_router import LLMRouter

logger = logging.getLogger(__name__)

class GraphExtractor:
    def __init__(self, llm_router: LLMRouter):
        self.llm = llm_router

    def extract(self, text_chunk: str) -> Dict[str, Any]:
        """
        Two-stage extraction to reduce hallucinated relations.
        Returns: {"entities": [...], "relations": [...]}
        """
        # Stage 1: Extract Entities
        entities = self._extract_entities(text_chunk)
        
        # Stage 2: Extract Relations
        relations = []
        if entities:
            relations = self._extract_relations(text_chunk, entities)
            
        return {
            "entities": entities,
            "relations": relations
        }

    def _extract_entities(self, text: str) -> List[Dict[str, str]]:
        sys_prompt = "You are an expert Knowledge Graph extractor. Return ONLY a valid JSON list of entities."
        user_prompt = f"""
Extract all key entities (Concepts, Algorithms, Technologies, People, Organizations) from the text.
Output Format:
[
  {{"entity": "RRF", "type": "Algorithm"}},
  {{"entity": "OpenAI", "type": "Organization"}}
]

Text:
{text}
"""
        response = self.llm.generate(sys_prompt, user_prompt)
        return self._parse_json(response, default_return=[])

    def _extract_relations(self, text: str, entities: List[Dict[str, str]]) -> List[Dict[str, str]]:
        sys_prompt = "You are an expert Knowledge Graph extractor. Return ONLY a valid JSON list of relations."
        entity_names = [e["entity"] for e in entities]
        user_prompt = f"""
Given the following entities: {entity_names}
Extract relationships between these specific entities based ONLY on the text provided.
Do NOT hallucinate relations not explicitly stated.

Output Format:
[
  {{"source": "Entity1", "target": "Entity2", "relation": "is used by"}}
]

Text:
{text}
"""
        response = self.llm.generate(sys_prompt, user_prompt)
        return self._parse_json(response, default_return=[])

    def _parse_json(self, response: str, default_return: Any) -> Any:
        try:
            if "```json" in response:
                response = response.split("```json")[1].split("```")[0].strip()
            elif "```" in response:
                response = response.split("```")[1].split("```")[0].strip()
            return json.loads(response)
        except Exception as e:
            logger.error(f"GraphExtractor JSON parse error: {e}\nRaw: {response}")
            return default_return
