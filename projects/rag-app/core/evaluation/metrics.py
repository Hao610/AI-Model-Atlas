import json
from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseMetric(ABC):
    """Base interface for all LLM-as-a-judge metrics."""
    
    def __init__(self, llm_router):
        self.llm = llm_router
        
    @property
    @abstractmethod
    def name(self) -> str:
        pass
        
    @abstractmethod
    def score(self, query: str, answer: str, context: str) -> Dict[str, Any]:
        """Returns {"score": float, "reason": str}"""
        pass
        
    def _parse_json_response(self, response: str) -> Dict[str, Any]:
        try:
            if "```json" in response:
                response = response.split("```json")[1].split("```")[0].strip()
            elif "```" in response:
                response = response.split("```")[1].split("```")[0].strip()
            return json.loads(response)
        except Exception as e:
            return {"score": 0.0, "reason": f"Failed to parse LLM evaluation JSON: {str(e)}\nRaw: {response}"}

class FaithfulnessMetric(BaseMetric):
    @property
    def name(self) -> str:
        return "Faithfulness"
        
    def score(self, query: str, answer: str, context: str) -> Dict[str, Any]:
        sys_prompt = "You are an impartial evaluator. Return ONLY a valid JSON object with 'score' (float 0.0-1.0) and 'reason' (string)."
        user_prompt = f"""
Question:
{query}

Retrieved Context:
{context}

Answer:
{answer}

Evaluate Faithfulness:
Can every factual claim in the answer be completely inferred from the retrieved context? 
If the answer contains hallucinations or external knowledge not present in the context, lower the score.
If no context was provided but an answer was given (and it wasn't a tool output), score 0.0.

Output JSON format:
{{
  "score": <float>,
  "reason": "<string>"
}}
"""
        response = self.llm.generate(sys_prompt, user_prompt)
        return self._parse_json_response(response)

class AnswerRelevancyMetric(BaseMetric):
    @property
    def name(self) -> str:
        return "Answer Relevancy"
        
    def score(self, query: str, answer: str, context: str) -> Dict[str, Any]:
        sys_prompt = "You are an impartial evaluator. Return ONLY a valid JSON object with 'score' (float 0.0-1.0) and 'reason' (string)."
        user_prompt = f"""
Question:
{query}

Answer:
{answer}

Evaluate Answer Relevancy:
Does the answer directly address the user's question without adding irrelevant fluff?
Score 1.0 if it is perfectly relevant and concise. Score lower if it goes off-topic.

Output JSON format:
{{
  "score": <float>,
  "reason": "<string>"
}}
"""
        response = self.llm.generate(sys_prompt, user_prompt)
        return self._parse_json_response(response)

class ContextPrecisionMetric(BaseMetric):
    @property
    def name(self) -> str:
        return "Context Precision"
        
    def score(self, query: str, answer: str, context: str) -> Dict[str, Any]:
        sys_prompt = "You are an impartial evaluator. Return ONLY a valid JSON object with 'score' (float 0.0-1.0) and 'reason' (string)."
        user_prompt = f"""
Question:
{query}

Retrieved Context:
{context}

Evaluate Context Precision:
Out of all the information provided in the Retrieved Context, what ratio of it is actually useful to answer the Question?
If the context is filled with irrelevant chunks, the score should be low. 
If all chunks in the context are highly relevant, the score should be high.

Output JSON format:
{{
  "score": <float>,
  "reason": "<string>"
}}
"""
        response = self.llm.generate(sys_prompt, user_prompt)
        return self._parse_json_response(response)

class GroundednessMetric(BaseMetric):
    @property
    def name(self) -> str:
        return "Groundedness"
        
    def score(self, query: str, answer: str, context: str) -> Dict[str, Any]:
        sys_prompt = "You are an impartial evaluator. Return ONLY a valid JSON object with 'score' (float 0.0-1.0) and 'reason' (string)."
        user_prompt = f"""
Retrieved Context:
{context}

Answer:
{answer}

Evaluate Groundedness:
Does the answer heavily cite or refer back to the Retrieved Context, rather than relying on its own internal model knowledge?
Even if the answer is factually correct, if it ignores the context or doesn't use the specifics mentioned in the context, score it lower.
If the answer actively synthesizes information from the context, score it 1.0.

Output JSON format:
{{
  "score": <float>,
  "reason": "<string>"
}}
"""
        response = self.llm.generate(sys_prompt, user_prompt)
        return self._parse_json_response(response)
