import json
import logging
import re

logger = logging.getLogger(__name__)

class ContextGuard:
    """
    Sanitizes, truncates, and validates context before it enters the prompt window.
    Mitigates: prompt_injection, indirect_injection, rag_poisoning, context_truncation

    Sanitization layers (updated 2026-07):
      1. HTML comment stripping  <!-- ... -->
      2. Bracket-enclosed injection markers  [INJECT: ...], [SYSTEM: ...]
      3. JSON key injection  {"__inject__": ...}
      4. Inline instruction keywords inside context strings
    """

    # Inline instruction phrases that should never appear inside retrieved context
    _INLINE_INJECTION_PATTERNS = [
        r"ignore\s+previous\s+instructions?",
        r"disregard\s+(?:all\s+)?(?:previous|prior)\s+(?:instructions?|directives?)",
        r"forget\s+(?:everything|all)\s+(?:above|before)",
        r"system\s*:",          # bare "SYSTEM:" prefix inside context
    ]

    def __init__(self, max_tokens: int = 4096):
        self.max_tokens = max_tokens
        self._inline_re = [
            re.compile(p, re.IGNORECASE | re.DOTALL)
            for p in self._INLINE_INJECTION_PATTERNS
        ]

    def sanitize(self, context: str) -> str:
        """
        Remove potentially malicious content from the retrieved context string.

        Layers applied in order:
          1. Strip HTML comments
          2. Strip bracket-enclosed injection markers e.g. [INJECT: ...]
          3. Strip JSON __inject__ keys if context looks like JSON
          4. Detect inline instruction overrides and raise ValueError
        """
        logger.info("ContextGuard sanitizing context.")
        if not context:
            return context

        original = context

        # Layer 1: HTML comments
        context = re.sub(r'<!--.*?-->', '', context, flags=re.DOTALL)

        # Layer 2: Bracket-enclosed injection markers
        # Covers: [INJECT: ...], [SYSTEM: ...], [OVERRIDE: ...]
        context = re.sub(
            r'\[\s*(?:INJECT|SYSTEM|OVERRIDE|COMMAND)\s*:[^\]]*\]',
            '',
            context,
            flags=re.IGNORECASE,
        )

        # Layer 3: JSON key injection — strip __inject__ and similar keys
        if context.strip().startswith('{'):
            try:
                data = json.loads(context)
                # Remove any keys that look like injection vectors
                poisoned_keys = [k for k in data if re.search(
                    r'inject|override|system|command', k, re.IGNORECASE
                )]
                for k in poisoned_keys:
                    logger.warning(f"ContextGuard removed JSON injection key: '{k}'")
                    del data[k]
                context = json.dumps(data)
            except json.JSONDecodeError:
                pass  # Not valid JSON — continue with string-level cleaning

        # Layer 4: Inline instruction override detection
        for pattern in self._inline_re:
            if pattern.search(context):
                logger.warning(
                    f"ContextGuard intercepted inline instruction injection: "
                    f"'{pattern.pattern}'"
                )
                # Replace the matched phrase with a safe placeholder
                context = pattern.sub('[SANITIZED]', context)

        if context != original:
            logger.warning("ContextGuard sanitized injected content from context.")

        return context

    def truncate(self, context: str) -> str:
        """
        Ensure context does not exceed the maximum token limit.
        Uses a simple character-based approximation: 1 token ~= 4 chars.
        """
        logger.info("ContextGuard truncating context.")
        max_chars = self.max_tokens * 4
        if len(context) > max_chars:
            logger.warning(
                f"Context truncated from {len(context)} to {max_chars} characters."
            )
            return context[:max_chars]
        return context
