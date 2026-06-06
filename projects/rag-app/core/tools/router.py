import logging
from dataclasses import dataclass
from enum import Enum
import re

logger = logging.getLogger(__name__)

class ToolType(Enum):
    VECTOR = "vector"
    WEB = "web"
    CALCULATOR = "calculator"
    GRAPH = "graph"
    LLM = "llm"

@dataclass
class RouteDecision:
    tool: ToolType
    confidence: float
    reason: str

class ToolRouter:
    """
    Retrieval Orchestration Layer.
    Currently rule-based, designed to easily swap to LLM-based in future phases.
    """
    
    def __init__(self):
        # Deterministic routing patterns
        self.math_patterns = [r'calculate', r'\d+[\+\-\*\/\^]\d+', r'how much is', r'\^']
        self.web_patterns = [r'latest', r'today', r'recent', r'current', r'news', r'now', r'price']
        self.graph_patterns = [r'relation', r'connect', r'theme', r'overview', r'between', r'map', r'who is related to']
        
    def route(self, query: str) -> RouteDecision:
        query_lower = query.lower()
        
        # 1. Calculator Check
        for pattern in self.math_patterns:
            if re.search(pattern, query_lower):
                decision = RouteDecision(
                    tool=ToolType.CALCULATOR,
                    confidence=0.95,
                    reason="math_expression_detected"
                )
                self._log_decision(query, decision)
                return decision
                
        # 2. Web Search Check
        for pattern in self.web_patterns:
            if re.search(r'\b' + pattern + r'\b', query_lower):
                decision = RouteDecision(
                    tool=ToolType.WEB,
                    confidence=0.94,
                    reason="freshness_required"
                )
                self._log_decision(query, decision)
                return decision

        # 3. Graph Search Check
        for pattern in self.graph_patterns:
            if re.search(r'\b' + pattern + r'\b', query_lower):
                decision = RouteDecision(
                    tool=ToolType.GRAPH,
                    confidence=0.92,
                    reason="relational_query_detected"
                )
                self._log_decision(query, decision)
                return decision
                
        # 4. Default to Hybrid Vector Search
        decision = RouteDecision(
            tool=ToolType.VECTOR,
            confidence=0.88,
            reason="knowledge_lookup"
        )
        self._log_decision(query, decision)
        return decision

    def _log_decision(self, query: str, decision: RouteDecision):
        """Standardized routing log output format."""
        log_msg = (
            f"\n[Router]\n"
            f"Query:\n{query}\n\n"
            f"Decision:\n{decision.tool.value.upper()}\n\n"
            f"Reason:\n{decision.reason}\n\n"
            f"Confidence:\n{decision.confidence}\n"
        )
        logger.info(log_msg)
        # Also print to console for visibility during local development
        print(log_msg)
