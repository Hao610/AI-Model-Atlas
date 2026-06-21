← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (21_rag_pii_zh.md)](21_rag_pii_zh.md)

---

# 🛡️ Chapter 21: Preventing PII Exfiltration

In RAG systems, your vector database can easily become a goldmine for hackers seeking Personally Identifiable Information (PII). A clever prompt injection attack can trick the LLM into spitting out sensitive private data unless strict safeguards are in place.

## 🕵️ The Censorious Librarian Analogy

* **The Analogy**: A vigilant librarian redacts names and private details from records *before* handing them to patrons.
* **How it works**: By actively scanning for and blacking out sensitive information, the librarian ensures that even if a malicious patron asks a tricky question, the secrets simply aren't there to be revealed.
* **Key Concept**: Sanitizing data before it reaches the LLM is the ultimate defense against data leakage.

## 📊 Quick Comparison

| Concept | Traditional | LLM Era | Impact |
| :--- | :--- | :--- | :--- |
| **Data Protection** | Database permissions | Multi-layered RAG sanitization | Prevents direct PII extraction |
| **Search Restrictions** | SQL row-level security | Vector metadata filtering | Isolates private user data chunks |
| **Output Control** | Static API gateways | Post-generation DLP scanning | Catches rogue LLM data leaks |

## 🧠 Core Concept

1. **Sanitize Before Indexing:** Use NER models or regex to automatically mask PII (e.g., replacing names with `[REDACTED]`) before chunking and embedding documents.
2. **Minimize Indexed Data:** Strictly limit your vector database to only hold the information necessary for the application's function.
3. **Enforce Metadata RBAC:** Attach access-level metadata to every vector chunk so that retrieval is rigidly filtered based on the user's authorization.
4. **Filter the Final Output:** Run the LLM's generated response through a Data Loss Prevention (DLP) tool to catch and block any PII before it reaches the user.

---

← [Prev Chapter](20_meta_prompts.md) | [Next Chapter](../phase4/22_git_commit_prompt.md) →
