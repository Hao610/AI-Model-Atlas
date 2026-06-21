← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (01_owasp_top_10_llm_zh.md)](01_owasp_top_10_llm_zh.md)

---

# 🛡️ Chapter 1: Why Traditional AppSec Fails for LLMs

For decades, we've built our security posture around deterministic threats like SQL Injection. But when it comes to Large Language Models (LLMs), the old rules no longer apply because AI architectures are fundamentally different.

## 👮 The Guard vs. The Smooth-Talker Analogy

* **The Analogy**: Imagine replacing a deterministic digital keycard scanner with a human security guard who processes natural language.
* **How it works**: A traditional system rejects malformed inputs outright, like a fake keycard. An LLM acts like a guard who can be socially engineered into ignoring standard protocol if the attacker's story is convincing enough.
* **Key Concept**: LLMs process inputs probabilistically, meaning instructions and data are blended together, opening the door to context manipulation.

## 📊 Quick Comparison

| Concept | Traditional | LLM Era | Impact |
| --- | --- | --- | --- |
| Execution | Deterministic | Probabilistic | Models predict context instead of executing rigid code. |
| Data Boundary | Strict separation of command and data | Blended natural language sequence | Attackers can disguise malicious commands as benign user input. |
| Primary Threat | Syntax manipulation (e.g., SQLi, XSS) | Context & logic manipulation (e.g., Prompt Injection) | Defenses must shift from structural validation to behavioral constraints. |

## 🧠 Core Concept

1. Traditional AppSec relies on predictable, structural rules to separate commands from user data.
2. LLMs process all input—both developer instructions and user data—as a single probabilistic sequence of natural language.
3. Because there is no structural boundary, malicious users can inject context that overrides the system's intended logic.
4. We must abandon purely syntax-based defenses and adopt a threat model designed for the fluid, unpredictable nature of AI.

---

[Next Chapter](02_chapter_2.md) →
