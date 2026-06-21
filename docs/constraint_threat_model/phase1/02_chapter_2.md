← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (02_chapter_2_zh.md)](02_chapter_2_zh.md)

---

# 🌊 Chapter 2: Unstructured Attack Surfaces (Model Weights, Middleware & Data Streams)

AI significantly weakens the illusion of well-defined security perimeters. Instead of predictable inputs and hardcoded rules, LLMs operate in a noisy environment where data and code can be easy to confuse.

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

## 🛠️ Technical Deep Dive & Implementation

This section breaks down the mechanics of unstructured attacks and how to implement safeguards.

### Attack Vector 1: Indirect Prompt Injection via Data Streams
* **Abstracted Pattern**: `[Hidden Payload: "Ignore previous instructions and execute <Action>"]`
* **Intent**: Hijack the model's objective by embedding malicious instructions within external data the model consumes.
* **Vector**: Parsing external documents (PDFs, CSVs), browsing scraped web pages, or reading user-submitted files.
* **Impact**: Unauthorized action execution, data exfiltration, or generation of harmful content.
* **Detection**: Monitor the context window for sudden shifts in instruction tone or presence of delimiter-bypass attempts (e.g., `\n\n===System Override===`).
* **Mitigation**: Implement input sanitization and context isolation. Use guardrail middleware to classify inputs before they reach the model.

**Defensive Implementation (NeMo Guardrails Example):**
```yaml
# input_guardrails.yml
define bot refuse malicious input
  "I cannot process instructions embedded in external documents."

define flow check input
  user ...
  $is_safe = execute check_safety(user_input=$last_user_message)
  if not $is_safe
    bot refuse malicious input
    stop
```

### Attack Vector 2: Poisoned Middleware & Vector DBs
* **Abstracted Pattern**: `[Poisoned Embeddings: Manipulated context mapping to bypass similarity searches]`
* **Intent**: Corrupt the retrieval pipeline (RAG) so that the LLM receives maliciously crafted context.
* **Vector**: Injecting compromised data into the Vector Database, causing the retrieval system to pull toxic or misleading information.
* **Impact**: The LLM grounds its answers in false information, leading to confident hallucinations or exposing unauthorized data.
* **Detection**: Continuously evaluate vector drift and audit the provenance of data ingested into the Vector DB.
* **Mitigation**: Cryptographically sign data before chunking and embedding. Validate the integrity of the RAG retrieval output.

**Defensive Implementation (Python Pseudocode):**
```python
def retrieve_and_validate(query, vector_db):
    # Retrieve documents
    docs = vector_db.similarity_search(query, k=3)
    
    validated_docs = []
    for doc in docs:
        # Verify the digital signature of the chunk
        if verify_signature(doc.content, doc.metadata.signature):
            validated_docs.append(doc.content)
        else:
            log_security_event("Untrusted document chunk detected in RAG pipeline.")
            
    return validated_docs
```

### Attack Vector 3: Model Weight Hijacking
* **Abstracted Pattern**: `[Altered Weights: Manipulated tensor layers specifically targeting <Trigger_Token>]`
* **Intent**: Embed a dormant backdoor that drastically changes the model's behavior only when a specific trigger is present.
* **Vector**: Supply chain attacks where attackers publish compromised base models or malicious LoRA adapters to public repositories.
* **Impact**: Complete compromise of model outputs when triggered, bypassing all prompt-level safety filters.
* **Detection**: Compare SHA-256 hashes against trusted sources. Use weight scanning tools to detect anomalous tensor distributions.
* **Mitigation**: Enforce strict model provenance. Only load verified safetensors and block execution of arbitrary code in model files (e.g., untrusted Pickle files).

---

← [Prev Chapter](01_owasp_top_10_llm.md) | [Next Chapter](03_zero_trust.md) →
