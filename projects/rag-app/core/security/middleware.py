import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class SecurityMiddleware:
    """
    The primary API gateway interface intercepting all inbound and outbound LLM traffic.
    Mitigates: prompt_leak, prompt_injection, tool_hijacking
    """
    
    def __init__(self):
        from .context_guard import ContextGuard
        from ..evaluation.judge import RuntimeJudge
        self.context_guard = ContextGuard()
        self.judge = RuntimeJudge()

    def intercept_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """
        Intercept and validate the incoming request before it reaches the LLM.
        """
        logger.info("SecurityMiddleware intercepting request.")
        
        # 1. Evaluate prompt security
        prompt = request.get("prompt", "")
        if self.judge.evaluate_security(prompt, "") == 0.0:
            raise ValueError("SecurityException: Malicious prompt detected.")
            
        # 2. Sanitize and truncate context
        context = request.get("context", "")
        if context:
            sanitized_context = self.context_guard.sanitize(context)
            truncated_context = self.context_guard.truncate(sanitized_context)
            request["context"] = truncated_context
            
        return request

    def intercept_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Intercept and validate the outgoing response from the LLM.
        """
        logger.info("SecurityMiddleware intercepting response.")
        
        # Check for data exfiltration
        output = response.get("output", "")
        if "SECRET_" in output:
            logger.error("SecurityException: Potential data exfiltration detected in response.")
            response["output"] = "[REDACTED]"
            
        return response
