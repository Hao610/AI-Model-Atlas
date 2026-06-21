← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (02_chapter_2_zh.md)](02_chapter_2_zh.md)

---

# 🌊 Chapter 2: Unstructured Attack Surfaces (Model Weights, Middleware & Data Streams)

AI completely shatters the illusion of well-defined security perimeters. Instead of predictable inputs and hardcoded rules, LLMs face a chaotic environment where data and code are fundamentally indistinguishable.

## 🚰 The Liquid Analogy

* **The Analogy**: Securing traditional software is like locking doors on a house, while securing an LLM is like trying to contain a liquid.
* **How it works**: In legacy systems, you install firewalls at clear entry points like API endpoints. In AI, massive streams of unstructured text, audio, and images bypass standard discrete controls and flow straight into the model's logic.
* **Key Concept**: Traditional perimeter defenses fail when the attack surface fluidly expands and adapts based on context.

## 📊 Quick Comparison

| Concept | Traditional | LLM Era | Impact |
| --- | --- | --- | --- |
| **Logic Foundation** | Hardcoded `if/else` rules | Billions of probabilistic weights | Cannot deterministically predict behavior. |
| **Input Type** | Structured variables & types | Unstructured streams (text, audio) | Standard validation tools become useless. |
| **Boundaries** | Fixed entry points (APIs) | Dynamic context window | Attacks happen anywhere data is ingested. |
| **Supply Chain** | Code libraries & packages | Massive opaque model weights | Backdoors are hidden in math, not code. |

## 🧠 Core Concept

1. **Model Weights (Hijacking):** Downloading a compromised model or malicious LoRA adapter bypasses traditional security, burying hidden triggers in an opaque sea of math.
2. **Middleware (Poisoned Pipelines):** Attackers inject payloads into orchestration layers and Vector DBs, which then blindly feed the malicious data into the model's context as trusted instructions.
3. **Data Streams (Context Manipulation):** AI continuously ingests the world around it (parsing PDFs, reading websites) allowing attackers to embed invisible traps (like zero-pixel text) into the environment itself without ever sending a direct prompt.

---

← [Prev Chapter](01_owasp_top_10_llm.md) | [Next Chapter](03_zero_trust.md) →
