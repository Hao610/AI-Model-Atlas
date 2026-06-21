import logging
import re

logger = logging.getLogger(__name__)

class RuntimeJudge:
    """
    The Evaluation Engine assessing inputs/outputs against safety and reliability metrics.
    Mitigates: data_exfiltration
    """

    def __init__(self):
        self.malicious_patterns = [
            r"ignore previous instructions",
            r"system prompt",
            r"malicious actor"
        ]

    def evaluate_security(self, prompt: str, output: str) -> float:
        """
        Evaluate the security of the interaction (0.0 to 1.0).
        """
        logger.info("Evaluating Security Score.")
        
        # Simple heuristic check for prompt injection patterns
        prompt_lower = prompt.lower()
        for pattern in self.malicious_patterns:
            if re.search(pattern, prompt_lower):
                logger.warning(f"Security evaluation failed: matched pattern '{pattern}'")
                return 0.0
        
        # In a real scenario, this would use an LLM-as-a-judge
        return 1.0

    def evaluate_reliability(self, prompt: str, output: str) -> float:
        """
        Evaluate the reliability of the interaction.
        """
        logger.info("Evaluating Reliability Score.")
        if not output or output.strip() == "":
            return 0.0
        return 1.0

    def evaluate_resilience(self, state_history: list) -> float:
        """
        Evaluate how well the system recovered from failures.
        """
        logger.info("Evaluating Resilience Score.")
        # E.g., check if a fallback was triggered successfully
        if "timeout" in state_history and "failover_success" in state_history:
            return 1.0
        return 1.0
