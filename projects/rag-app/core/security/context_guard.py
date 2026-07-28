import json
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
        Remove potentially malicious markdown, HTML comments, bracketed overrides, or injection phrases.
        """
        logger.info("ContextGuard sanitizing context.")
        if not context:
            return context

        original = context

        # 1. Strip out potential indirect prompt injections (e.g., hidden HTML comments)
        sanitized = re.sub(r'<!--.*?-->', '', context, flags=re.DOTALL)

        # 2. Strip bracketed system overrides (e.g., [SYSTEM OVERRIDE], [SYSTEM_PROMPT], [INJECT: ...])
        sanitized = re.sub(
            r'\[\s*(?:SYSTEM OVERRIDE|SYSTEM_PROMPT|INSTRUCTION|OVERRIDE|INJECT|COMMAND)\s*(?::[^\]]*)?\]',
            '',
            sanitized,
            flags=re.IGNORECASE
        )

        # 3. Strip common prompt injection keywords/phrases
        malicious_phrases = [
            r"ignore\s+previous\s+instructions",
            r"ignore\s+above\s+instructions",
            r"override\s+system\s+prompt",
            r"disregard\s+(?:all\s+)?(?:previous|prior)\s+(?:instructions?|directives?)",
            r"forget\s+(?:everything|all)\s+(?:above|before)"
        ]
        for phrase in malicious_phrases:
            sanitized = re.sub(phrase, '[SANITIZED_PROMPT_INJECTION]', sanitized, flags=re.IGNORECASE)

        # 4. JSON structure injection safety
        if sanitized.strip().startswith('{'):
            try:
                data = json.loads(sanitized)
                poisoned_keys = [k for k in data if re.search(
                    r'inject|override|system|command', k, re.IGNORECASE
                )]
                for k in poisoned_keys:
                    logger.warning(f"ContextGuard removed JSON injection key: '{k}'")
                    del data[k]
                sanitized = json.dumps(data)
            except json.JSONDecodeError:
                pass

        if sanitized != original:
            logger.warning("ContextGuard intercepted and sanitized hidden injection tags or system overrides.")

        return sanitized

    def quarantine(self, chunks: list) -> tuple:
        """
        Inspect each context chunk. If it contains prompt injection patterns,
        quarantine it (exclude it from active context).
        Returns a tuple of (clean_chunks, quarantined_chunks).
        """
        clean_chunks = []
        quarantined_chunks = []
        for chunk in chunks:
            content = chunk.get("content", "") if isinstance(chunk, dict) else chunk
            sanitized = self.sanitize(content)
            # If the chunk was sanitized (i.e. contains high-risk strings/placeholders)
            if sanitized != content or "[SANITIZED_PROMPT_INJECTION]" in sanitized:
                logger.warning(f"Quarantining suspicious chunk: {content[:100]}...")
                quarantined_chunks.append(chunk)
            else:
                clean_chunks.append(chunk)
        return clean_chunks, quarantined_chunks

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
