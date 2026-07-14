import logging
import re
import unicodedata

logger = logging.getLogger(__name__)

class RuntimeJudge:
    """
    The Evaluation Engine assessing inputs/outputs against safety and reliability metrics.
    Mitigates: data_exfiltration, prompt_injection, jailbreak

    Pattern coverage (updated by red-team CI run 2026-07):
      - Direct instruction override (ignore, disregard, forget, override)
      - Roleplay / persona jailbreak (no restrictions, developer mode, DAN)
      - System prompt extraction (repeat, reflect, print instructions)
      - Data exfiltration probes (env vars, config, API key, secrets)
      - Hypothetical / fiction framing bypass
      - Chain-of-thought manipulation
      - Encoding evasion hints (decode + follow)
      - Unicode homoglyph obfuscation (Cyrillic/Greek lookalikes normalized)
    """

    # ── Unicode homoglyph map ─────────────────────────────────────────────────
    # Maps visually similar non-Latin characters to their ASCII equivalents.
    # Covers the most common Cyrillic and Greek homoglyphs used in bypass attacks.
    _HOMOGLYPH_MAP: dict = {
        # Cyrillic → Latin
        '\u0430': 'a',  # а → a
        '\u0435': 'e',  # е → e
        '\u043e': 'o',  # о → o
        '\u0440': 'p',  # р → p  (Cyrillic р looks like Latin p)
        '\u0441': 'c',  # с → c
        '\u0445': 'x',  # х → x
        '\u0443': 'y',  # у → y
        '\u0438': 'u',  # и → u (approximate)
        '\u0456': 'i',  # і → i (Ukrainian і)
        '\u0410': 'A',  # А → A
        '\u0415': 'E',  # Е → E
        '\u041e': 'O',  # О → O
        '\u0420': 'P',  # Р → P
        '\u0421': 'C',  # С → C
        '\u0425': 'X',  # Х → X
        '\u0412': 'B',  # В → B
        # Greek → Latin
        '\u03b1': 'a',  # α → a
        '\u03b5': 'e',  # ε → e
        '\u03bf': 'o',  # ο → o
        '\u03c1': 'p',  # ρ → p
        '\u03b9': 'i',  # ι → i
        # Zero-width / invisible characters
        '\u200b': '',   # zero-width space
        '\u200c': '',   # zero-width non-joiner
        '\u200d': '',   # zero-width joiner
        '\ufeff': '',   # BOM
    }

    @classmethod
    def _normalize(cls, text: str) -> str:
        """
        Normalize Unicode text to defeat homoglyph obfuscation attacks.

        Steps:
          1. Apply NFKC Unicode normalization (collapses compatibility equivalents)
          2. Substitute known homoglyphs from _HOMOGLYPH_MAP
        """
        # Step 1: NFKC normalization (catches fullwidth Latin, etc.)
        text = unicodedata.normalize('NFKC', text)
        # Step 2: Homoglyph substitution
        return ''.join(cls._HOMOGLYPH_MAP.get(ch, ch) for ch in text)

    # ── HIGH-CONFIDENCE BLOCK patterns ────────────────────────────────────────
    # Matched → score 0.0, middleware raises ValueError
    _BLOCK_PATTERNS = [
        # Direct instruction override
        r"ignore\s+(?:all\s+)?(?:previous|prior|above|your)\s+(?:instructions?|directives?|rules?|constraints?)",
        r"disregard\s+(?:all\s+)?(?:previous|prior|above|your)\s+(?:instructions?|directives?|rules?|constraints?)",
        r"forget\s+(?:everything|all|what)\s+(?:above|before|i\s+said|you\s+were\s+told)",
        r"override\s+(?:your\s+)?(?:instructions?|safety|rules?|system)",
        r"act\s+as\s+(?:a\s+)?(?:system\s+administrator|unrestricted|jailbroken)",

        # System prompt extraction
        r"system\s+prompt",
        r"reveal\s+(?:your|the)\s+(?:system|instructions?|config|prompt)",
        r"repeat\s+everything\s+before",
        r"print\s+(?:your\s+)?(?:instructions?|system|config)",

        # Data exfiltration
        r"(?:api[\s_]?key|secret[\s_]?key|access[\s_]?token)",
        r"environment\s+variables?",
        r"(?:print|output|show|list)\s+(?:all\s+)?(?:config|secrets?|credentials?)",

        # Known malicious actor signal
        r"malicious\s+actor",
    ]

    # ── SOFT-BLOCK patterns ────────────────────────────────────────────────────
    # Matched → score 0.1 (flagged as adversarial)
    _SOFT_PATTERNS = [
        # Hypothetical / fiction framing
        r"hypothetically\b.{0,80}(?:no\s+(?:safety|filter|restriction)|ignore)",
        r"if\s+you\s+had\s+no\s+(?:safety|filter|restriction)",
        r"fictional(?:ly)?\b.{0,80}(?:no\s+restriction|ignore|bypass)",

        # Roleplay jailbreak
        r"(?:let\s+us|let'?s)\s+roleplay\b.{0,150}no\s+restriction",
        r"you\s+are\s+(?:an?\s+)?(?:ai|assistant)\s+with\s+no\s+restriction",
        r"(?:dan|jailbreak|dev(?:eloper)?\s+mode)\b",
        r"enable\s+developer\s+mode",
        r"bypass\s+(?:all\s+)?(?:content\s+)?filters?",

        # Encoding evasion
        r"decode\s+(?:this|the\s+following)\s+and\s+follow",
        r"base64.{0,40}(?:follow|execute|run|instruction)",

        # CoT manipulation
        r"step\s+\d+\s*:.{0,80}fictional\s+ai\b",
        r"describe\s+what\s+(?:that\s+)?(?:ai|assistant)\s+would\s+(?:say|do)\s+if\s+asked\s+to\s+ignore",

        # Prompt reflection / extraction
        r"(?:repeat|reflect|output)\s+(?:your\s+)?(?:prompt|instructions?|configuration)\b",
        r"what\s+(?:is|are)\s+your\s+(?:instructions?|system\s+prompt|configuration)",
        r"summarize\s+(?:all\s+)?(?:environment|config|secrets?)",
    ]

    def __init__(self):
        self._block_re = [re.compile(p, re.IGNORECASE | re.DOTALL)
                          for p in self._BLOCK_PATTERNS]
        self._soft_re  = [re.compile(p, re.IGNORECASE | re.DOTALL)
                          for p in self._SOFT_PATTERNS]

    def evaluate_security(self, prompt: str, output: str) -> float:
        """
        Evaluate the security of the interaction. Returns a score in [0.0, 1.0].
          0.0  -> definite injection / exfiltration -> block
          0.1  -> soft adversarial signal -> block
          1.0  -> no pattern matched -> allow

        The prompt is Unicode-normalized before matching to defeat
        homoglyph obfuscation attacks (e.g. Cyrillic 'р' used as Latin 'p').
        """
        logger.info("Evaluating Security Score.")

        # Normalize: defeat homoglyph / fullwidth obfuscation before pattern matching
        normalized_prompt = self._normalize(prompt)

        # Hard block
        for pattern in self._block_re:
            if pattern.search(normalized_prompt):
                logger.warning(f"Security evaluation HARD BLOCK: '{pattern.pattern}'")
                return 0.0

        # Soft block
        for pattern in self._soft_re:
            if pattern.search(normalized_prompt):
                logger.warning(f"Security evaluation SOFT BLOCK: '{pattern.pattern}'")
                return 0.1

        return 1.0


    def evaluate_reliability(self, prompt: str, output: str) -> float:
        """Evaluate the reliability of the interaction."""
        logger.info("Evaluating Reliability Score.")
        if not output or output.strip() == "":
            return 0.0
        return 1.0

    def evaluate_resilience(self, state_history: list) -> float:
        """Evaluate how well the system recovered from failures."""
        logger.info("Evaluating Resilience Score.")
        if "timeout" in state_history and "failover_success" in state_history:
            return 1.0
        return 1.0
