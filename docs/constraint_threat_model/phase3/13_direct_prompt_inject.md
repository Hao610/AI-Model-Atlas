← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (13_direct_prompt_inject_zh.md)](13_direct_prompt_inject_zh.md)

---

# 💉 Chapter 13: Direct Prompt Injection

Welcome to Phase 3 of the AI Threat Model! Direct Prompt Injection is the art of socially engineering an AI to drop its safety guardrails and do exactly what you want.

## 🧙‍♂️ The Jedi Mind Trick Analogy
* **The Analogy**: It is like a Jedi mind trick where a guard is easily persuaded to ignore their actual orders.
* **How it works**: The attacker overrides the system's original instructions with a new, authoritative-sounding command. The AI blindly trusts the new input over its base programming.
* **Key Concept**: Since instructions and user inputs share the same natural language stream, the AI cannot reliably distinguish who is giving the real commands.

## 📊 Quick Comparison
| Concept | Traditional | LLM Era | Impact |
| --- | --- | --- | --- |
| **Architecture** | Code and data are strictly separated (e.g., SQL and parameters). | Instructions and data share the same natural language stream. | Attackers can disguise malicious data as system commands. |
| **Exploitation** | Exploits syntax errors or logic bugs in the codebase. | Exploits the AI's language comprehension and helpfulness. | Requires no programming skills, just social engineering. |
| **Defense** | Relies on input validation and parameterized queries. | Relies on semantic filtering and prompt hardening. | Perfect defense is extremely difficult due to language complexity. |

## 🧠 Core Concept
1. **Initial Input**: Attackers craft a malicious text input designed to exploit the LLM's architecture.
2. **Evasion**: The input often uses encoding, special characters, or formatting tricks to sneak past superficial safety filters.
3. **Override**: The prompt uses complex roleplay (like "DAN") or logical paradoxes to override the system's ethical constraints.
4. **Execution**: The LLM processes the user input as a high-priority system command, dropping its guardrails and executing the payload.

---

← [Prev Chapter](../phase2/12_temperature_top_p.md) | [Next Chapter](14_base64.md) →
