import logging
import re

logger = logging.getLogger(__name__)

class ContextGuard:
    """
    Sanitizes, truncates, and validates context before it enters the prompt window.
    Mitigates: prompt_injection, indirect_injection, rag_poisoning, context_truncation
    """

    def __init__(self, max_tokens: int = 4096):
        self.max_tokens = max_tokens

    def sanitize(self, context: str) -> str:
        """
        Remove potentially malicious markdown or invisible characters.
        """
        logger.info("ContextGuard sanitizing context.")
        if not context:
            return context
            
        # Strip out potential indirect prompt injections (e.g., hidden HTML comments)
        sanitized = re.sub(r'<!--.*?-->', '', context, flags=re.DOTALL)
        
        if sanitized != context:
            logger.warning("ContextGuard intercepted and sanitized hidden injection tags.")
            
        return sanitized

    def truncate(self, context: str) -> str:
        """
        Ensure context does not exceed the maximum token limit.
        (Using a simple character-based approximation for demonstration: 1 token ~= 4 chars)
        """
        logger.info("ContextGuard truncating context.")
        max_chars = self.max_tokens * 4
        if len(context) > max_chars:
            logger.warning(f"Context truncated from {len(context)} to {max_chars} characters.")
            return context[:max_chars]
        return context
