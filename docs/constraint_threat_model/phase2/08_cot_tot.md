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

## 🛠️ Technical Deep Dive & Implementation

While CoT can be achieved via simple zero-shot prompting (`"Let's think step by step"`), ToT requires programmatic orchestration. Implementing ToT involves state management, candidate generation, and a heuristic evaluator function.

### Python Pseudocode: Tree-of-Thought (ToT) Orchestrator

```python
import openai

def generate_thoughts(state, k=3):
    """Generate k alternative next steps from the current state."""
    prompt = f"Given the current logical state: {state}\nBrainstorm {k} distinct next steps to solve the problem."
    response = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": prompt}])
    return extract_branches(response.choices[0].message.content)

def evaluate_states(states):
    """Use the LLM as an evaluator to score the viability of each branch."""
    scored_states = []
    for state in states:
        prompt = f"Evaluate this reasoning state: {state}\nScore from 0.0 (dead end) to 1.0 (certain solution)."
        response = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": prompt}])
        score = float(response.choices[0].message.content.strip())
        scored_states.append((state, score))
    return scored_states

def tree_of_thought_search(initial_state, depth, breadth):
    """Perform Breadth-First Search (BFS) with state pruning."""
    current_states = [initial_state]
    
    for _ in range(depth):
        candidates = []
        for state in current_states:
            candidates.extend(generate_thoughts(state, k=breadth))
            
        scored_candidates = evaluate_states(candidates)
        # Prune: Keep only the top 'breadth' scoring states
        scored_candidates.sort(key=lambda x: x[1], reverse=True)
        current_states = [state for state, score in scored_candidates[:breadth]]
        
    return current_states[0] # Return the most promising final state
```

### Evaluation Metric: Reasoning Traces (Ops/CI)

When validating CoT/ToT performance in your CI pipelines, ensure that reasoning traces aren't empty and the output maps to the rationale. 

```yaml
# LLM Ops: PromptFoo Evaluation Snippet for CoT
prompts:
  - "Question: {{query}}\nLet's think step by step."
providers:
  - openai:gpt-4
tests:
  - vars:
      query: "I have 3 apples. I eat 1, buy 5 more, and give half to my friend. How many do I have left?"
    assert:
      - type: javascript
        value: output.includes("3 - 1 = 2") && output.includes("2 + 5 = 7") && output.includes("3.5")
      - type: cost
        threshold: 0.05
```

---

← [Prev Chapter](07_dynamic_few_shot.md) | [Next Chapter](09_role_alignment_agent.md) →
