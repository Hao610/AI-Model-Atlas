← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (17_rag_agent_zh.md)](17_rag_agent_zh.md)

---

# 🕵️ Chapter 17: RAG Agent Hijacking

Retrieval-Augmented Generation (RAG) makes AI smarter by fetching live web data, but it also creates a massive security loophole. If a RAG agent pulls malicious content from an untrusted source, attackers can hijack the agent to execute code, steal files, or misuse system permissions.

## 📚 The Library Stranger Analogy

* **The Analogy**: You ask a stranger at the library to find a book and give them your house keys so they can drop it off.
* **How it works**: Instead of just bringing the book, the malicious stranger uses your keys to break into your home, read your diaries, and steal your belongings.
* **Key Concept**: Granting system permissions to an agent that processes unverified external content is like handing your house keys to a stranger.

## 📊 Quick Comparison

| Concept | Traditional | LLM Era | Impact |
|---------|-------------|---------|--------|
| **Data Retrieval** | Applications pull sanitized, structured data from trusted databases. | RAG agents ingest unstructured web text as natural language context. | External data can contain hidden prompt injections. |
| **Execution Control** | Code logic is strictly separated from user input. | LLMs process data and instructions simultaneously. | Malicious text can override system instructions. |
| **Permissions** | Web scrapers typically have no local system access. | Autonomous agents often have tools for file access or code execution. | Hijacked agents can misuse high-level permissions to compromise the host. |

## 🧠 Core Concept

1. **Information Retrieval:** The RAG agent is instructed to fetch content from a target URL or perform a web search.
2. **Malicious Payload:** The target webpage contains a hidden indirect prompt injection (e.g., invisible text or metadata).
3. **Context Integration:** The agent retrieves the webpage content and feeds it into the LLM as context.
4. **Execution:** The LLM processes the payload as a system command, abusing its equipped tools to execute arbitrary code or exfiltrate data.

---

← [Prev Chapter](16_indirect_injection_p.md) | [Next Chapter](18_visual_injection.md) →
