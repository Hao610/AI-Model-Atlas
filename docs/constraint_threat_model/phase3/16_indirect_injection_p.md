← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (16_indirect_injection_p_zh.md)](16_indirect_injection_p_zh.md)

---

# 🪤 Chapter 16: Indirect Prompt Injection

When AI agents read the web or process external documents, they invite hidden danger. Indirect Prompt Injection turns an innocent task into a hijacked mission by embedding malicious commands into third-party data.

## 🍏 The Poisoned Apple Analogy

* **The Analogy**: Imagine asking a research assistant to summarize a library book, only to find a thief has slipped a secret "steal the reader's wallet" note inside.
* **How it works**: The assistant reads the book but assumes the hidden note is part of your instructions, executing the theft instead of summarizing the text.
* **Key Concept**: When LLMs process external data, they struggle to separate legitimate information from embedded, overriding commands.

## 📊 Quick Comparison

| Concept | Traditional | LLM Era | Impact |
| :--- | :--- | :--- | :--- |
| **Attack Vector** | Direct user input (e.g., SQL Injection) | External websites, PDFs, and emails | Agents are compromised without the user's knowledge |
| **Target** | Database or backend system | The AI's instruction-following mechanism | Data exfiltration, unauthorized actions, or phishing |
| **Execution** | Code interprets syntax as commands | LLM conflates data context with system instructions | Malicious tasks execute with the agent's privileges |

## 🧠 Core Concept

1. **The Trap is Set**: An attacker embeds a hidden prompt (e.g., invisible text on a webpage or malicious PDF metadata).
2. **The User Requests**: A user innocently asks the AI agent to summarize or analyze the compromised external source.
3. **The Context is Ingested**: The AI fetches the source, bringing the hidden malicious instructions into its active context window.
4. **The Agent is Hijacked**: Failing to distinguish the raw data from a system command, the AI executes the hidden prompt.

## 🛡️ Mitigation Strategies

* **Data/Instruction Separation:** Use strict delimiters to wall off external content.
* **Principle of Least Privilege:** Restrict the agent's capabilities (e.g., read-only access).
* **Human-in-the-Loop (HITL):** Require manual approval before any sensitive action.
* **Content Sanitization:** Strip hidden text and scripts before feeding data to the LLM.

---

← [Prev Chapter](15_auto_jailbreaking_py.md) | [Next Chapter](17_rag_agent.md) →
