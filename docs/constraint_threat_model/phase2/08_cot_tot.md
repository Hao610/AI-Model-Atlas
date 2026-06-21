← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (08_cot_tot_zh.md)](08_cot_tot_zh.md)

---

# 🌳 Chapter 8: CoT & ToT Optimization

As LLMs tackle harder logic puzzles, standard prompting hits a wall. **Chain-of-Thought (CoT)** and **Tree-of-Thought (ToT)** force models to slow down, plan, and evaluate their own logic before outputting a final answer.

## 🕵️‍♂️ The Detective Analogy

* **The Analogy**: A detective doesn't just guess the murderer instantly; they build a timeline and test different theories.
* **How it works**: CoT forces a linear step-by-step deduction path. ToT goes further by exploring multiple timelines at once, backtracking when a clue hits a dead end.
* **Key Concept**: By revealing intermediate reasoning, we dramatically reduce hallucination and logic errors.

## 📊 Quick Comparison

| Concept | Traditional | LLM Era | Impact |
| :--- | :--- | :--- | :--- |
| **Logic Path** | Immediate "Input -> Output" mapping | "Input -> Reasoning -> Output" | Drops hallucination rate |
| **Exploration** | Single, linear response attempt | Branching paths evaluated in parallel | Solves complex, multi-step tasks |
| **Correction** | Fails entirely if one step is wrong | Prunes bad paths and backtracks | Massive boost in reasoning reliability |

## 🧠 Core Concept

**Chain-of-Thought (CoT)** is a linear reasoning process, while **Tree-of-Thought (ToT)** expands this into an evaluative branching structure.

1. **Prompt for Steps**: Instruct the model to "think step by step" to generate intermediate logical states.
2. **Generate Candidates**: For ToT, the model brainstorms several possible next steps (branches) instead of just one.
3. **Evaluate States**: The model acts as its own critic, assessing how close each branch brings it to the correct solution.
4. **Search & Prune**: Promising paths are explored further, while dead-end logic paths are pruned away before generating the final answer.

---

← [Prev Chapter](07_dynamic_few_shot.md) | [Next Chapter](09_role_alignment_agent.md) →
