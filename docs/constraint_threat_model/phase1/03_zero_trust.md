← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (03_zero_trust_zh.md)](03_zero_trust_zh.md)

---

# 🛡️ Chapter 3: Zero Trust Architecture for LLMs

Never trust, always verify. In an LLM-driven system, treating any component, user, or data source as inherently safe is a recipe for disaster.

## 🏛️ The Embassy Analogy

* **The Analogy**: An LLM is like a brilliant but extremely gullible foreign diplomat operating in a high-security embassy.
* **How it works**: Every visitor (user input) and package (database retrieval) is heavily vetted before reaching the diplomat's desk. The diplomat cannot directly open the vault, but must request actions through guarded channels.
* **Key Concept**: The LLM cannot secure itself; the surrounding system architecture must act as the unbreachable security perimeter.

## 📊 Quick Comparison

| Concept | Traditional | LLM Era | Impact |
| --- | --- | --- | --- |
| **Execution** | Deterministic logic paths | Probabilistic text generation | Cannot reliably self-police actions |
| **Instructions vs Data** | Strict structural separation | Mixed together in natural language | Highly vulnerable to Prompt Injection |
| **Privilege** | Granted to specific users/roles | Granted to autonomous AI agents | Major risk of the Confused Deputy problem |
| **Errors** | Predictable bug crashes | Confident but false hallucinations | Requires strict output validation |

## 🧠 Core Concept

To implement Zero Trust in an LLM ecosystem, you must build strict boundaries and treat every data flow as potentially hostile.

1. **Isolate and Verify Every Input**: Treat all incoming data—including user inputs, RAG database retrieves, and tool outputs—as untrusted payloads that must be sanitized before reaching the model.
2. **Enforce Boundary Controls**: Clearly separate system commands from user data using strict delimiters or structured formats (like JSON) so the model knows what is an instruction versus what is data.
3. **Apply Least Privilege Tooling**: Grant the absolute minimum permissions (e.g., read-only access) to the LLM and require Human-in-the-Loop authorization for any destructive actions.
4. **Validate All Outputs**: Never stream raw outputs blindly to critical systems or users; always use secondary models or deterministic validators to ensure structural integrity and safety.

---

← [Prev Chapter](02_chapter_2.md) | [Next Chapter](04_prompt.md) →
