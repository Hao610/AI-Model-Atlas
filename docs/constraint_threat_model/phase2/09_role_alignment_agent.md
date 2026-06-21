← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (09_role_alignment_agent_zh.md)](09_role_alignment_agent_zh.md)

---

# 🎭 Chapter 9: Role Alignment

Role alignment ensures multi-agent systems don't descend into chaos. Without strict boundaries, agents suffer from **role collapse**—losing their assigned personas and drifting into generic or out-of-scope behaviors.

## 🎭 The Theatrical Play Analogy

* **The Analogy**: A multi-agent system is like a stage play where every actor has a distinct script and character motivation.
* **How it works**: If an actor breaks character and starts reciting someone else's lines, the narrative falls apart and the production stalls.
* **Key Concept**: Continuous context anchoring prevents LLMs from reverting to their default "helpful generalist" persona, forcing them to stick to their strict job description.

## 📊 Quick Comparison

| Concept | Traditional | LLM Era | Impact |
| :--- | :--- | :--- | :--- |
| **Persona** | Hardcoded logic constraints and permissions. | Prompt-driven behavioral guardrails. | Highly flexible but prone to semantic drift. |
| **Boundaries** | Fixed API endpoints and strict typing. | Interaction protocols and output schemas. | Requires active and continuous enforcement. |
| **Failure Mode** | Type errors or access denied exceptions. | "Role Collapse" (agent forgets its job). | Unpredictable and hard-to-debug pipeline failures. |

## 🧠 Core Concept

1. **Define the Script**: Inject a highly detailed system prompt for each agent, strictly defining allowed actions, tone, and goals.
2. **Anchor the Context**: Periodically inject reminder prompts or pin the core persona definition so it isn't pushed out of the context window over long tasks.
3. **Enforce Protocols**: Use structured outputs (like JSON) instead of free-flowing dialogue to prevent cross-agent "persona bleeding".
4. **Deploy a Stage Manager**: Use a lightweight evaluator agent to intercept outputs, validating that the agent hasn't broken character before passing data downstream.

---

← [Prev Chapter](08_cot_tot.md) | [Next Chapter](10_pydantic_json.md) →
