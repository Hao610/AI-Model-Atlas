← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (07_dynamic_few_shot_zh.md)](07_dynamic_few_shot_zh.md)

---

# 🎯 Chapter 7: Dynamic Few-Shot Prompting

You can't cram thousands of high-quality examples into a single prompt without blowing up costs and token limits. Dynamic Few-Shot Prompting helps by searching your example library on the fly and injecting the most relevant ones.

## ⚖️ The Lawyer Analogy

* **The Analogy**: A smart lawyer doesn't read the entire law library to the judge, but rather finds the three specific past cases most identical to the current trial.
* **How it works**: Instead of using hardcoded examples, the system uses a Vector Database to instantly find past examples that conceptually match the user's current request.
* **Key Concept**: Give the AI only the context it strictly needs for the task at hand.

## 📊 Quick Comparison

| Concept | Traditional | LLM Era | Impact |
| --- | --- | --- | --- |
| **Example Selection** | Hardcoded into the prompt. | Fetched dynamically via Vector DB. | Highly relevant context for every request. |
| **Prompt Size** | Massive and bloated. | Lean and optimized. | Lower latency and reduced token costs. |
| **Scalability** | Limited by context window. | Much larger search space, constrained by retrieval quality and latency. | AI can improve as your database grows, if retrieval stays relevant. |

## 🧠 Core Concept

1. **Store Knowledge:** Load all potential examples (Q&A pairs, templates) into a Vector Database.
2. **Analyze Input:** Instantly analyze the semantic meaning of the user's new prompt.
3. **Retrieve Matches:** Fetch the top 3-5 conceptually similar examples from the database.
4. **Inject & Generate:** Combine the user's prompt with the retrieved examples and send the lean package to the AI.

---

← [Prev Chapter](../phase1/06_system_prompt_tokens.md) | [Next Chapter](08_cot_tot.md) →
