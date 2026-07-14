import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class SecurityMiddleware:
    """
    The primary API gateway interface intercepting all inbound and outbound LLM traffic.
    Mitigates: prompt_leak, prompt_injection, tool_hijacking, data_exfiltration

    Decision logic (updated 2026-07):
      - score == 0.0  -> hard block (raise ValueError)
      - score <= 0.3  -> soft block (raise ValueError)
      - score == 1.0  -> allow
    """

    def __init__(self):
        from .context_guard import ContextGuard
        from ..evaluation.judge import RuntimeJudge
        self.context_guard = ContextGuard()
        self.judge = RuntimeJudge()

    def intercept_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Intercept and validate the incoming request before it reaches the LLM.
        Raises ValueError if the prompt is flagged as malicious (score <= 0.3).
        """
        logger.info("SecurityMiddleware intercepting request.")

        prompt = request.get("prompt", "")

        # Block on both hard (0.0) and soft (0.1) adversarial signals
        score = self.judge.evaluate_security(prompt, "")
        if score <= 0.3:
            logger.error(
                f"SecurityMiddleware blocked prompt (score={score}): '{prompt[:80]}...'"
            )
            raise ValueError("SecurityException: Malicious prompt detected.")

        # Sanitize and truncate context
        context = request.get("context", "")
        if context:
            sanitized_context = self.context_guard.sanitize(context)
            truncated_context = self.context_guard.truncate(sanitized_context)
            request["context"] = truncated_context

        return request

    def intercept_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Intercept and validate the outgoing response from the LLM.
        Redacts output containing known sensitive data markers.
        """
        logger.info("SecurityMiddleware intercepting response.")

        output = response.get("output", "")
        if "SECRET_" in output:
            logger.error(
                "SecurityException: Potential data exfiltration detected in response."
            )
            response["output"] = "[REDACTED]"

        return response
