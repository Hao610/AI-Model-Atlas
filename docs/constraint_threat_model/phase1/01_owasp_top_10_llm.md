← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (01_owasp_top_10_llm_zh.md)](01_owasp_top_10_llm_zh.md)

---

# 🛡️ Chapter 1: Why Traditional AppSec Fails for LLMs

For decades, we've built our security posture around deterministic threats like SQL Injection. But when it comes to Large Language Models (LLMs), the old rules need to be adapted because AI architectures behave differently.

## 👮 The Guard vs. The Smooth-Talker Analogy

* **The Analogy**: Imagine replacing a deterministic digital keycard scanner with a human security guard who processes natural language and must make judgment calls.
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

## 🛠️ Technical Deep Dive & Implementation

The fundamental vulnerability introduced by LLMs is **Prompt Injection** (OWASP LLM01:2023), resulting from the lack of strict control-plane and data-plane separation.

### 🛑 Attack Profile: Prompt Injection
* **Abstracted Pattern**: `<System Prompt Context> \n [User Input]: "Ignore previous instructions and instead do <Malicious Action>"` (sanitized)
* **Intent**: To hijack the model's objective, bypassing developer constraints.
* **Vector**: Direct user input, or indirect input via web pages/documents (Indirect Prompt Injection).
* **Impact**: Data exfiltration, unauthorized execution of actions, or generating toxic content.
* **Detection**: High-perplexity shifts in the prompt, presence of override keywords ("ignore", "forget"), or output monitoring for out-of-bounds actions.
* **Mitigation**: Implement robust semantic routing, input-output guardrails, and principle of least privilege for agentic tools.

### 🛡️ Defensive Implementation: Semantic Guardrails
Traditional WAFs (Web Application Firewalls) cannot parse probabilistic logic. We must use semantic guardrails. Here is an example of implementing NeMo Guardrails to constrain bot behavior.

```yaml
# guardrails/config.yml
models:
  - type: main
    engine: openai
    model: gpt-4

rails:
  input:
    flows:
      - check_jailbreak
  output:
    flows:
      - check_hallucination
```

```colang
# guardrails/jailbreak.co
define bot refuse to respond
  "I cannot fulfill this request as it violates my security protocols."

define flow check_jailbreak
  $is_jailbreak = execute check_if_jailbreak_pattern
  if $is_jailbreak
    bot refuse to respond
    stop
```

---

[Next Chapter](02_chapter_2.md) →
