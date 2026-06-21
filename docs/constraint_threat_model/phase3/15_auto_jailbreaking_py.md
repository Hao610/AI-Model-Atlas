← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (15_auto_jailbreaking_py_zh.md)](15_auto_jailbreaking_py_zh.md)

---

# 🤖 Chapter 15: Auto-Jailbreaking and Automated Red Teaming

Automated red teaming, colloquially known as "auto-jailbreaking," unleashes scripts to systematically hammer an AI model's safety filters. It replaces slow human intuition with rapid, programmatic prompt experimentation.

## 🔐 The Lock-Picking Robot Analogy

* **The Analogy**: Imagine a robotic lock-picker designed to systematically try millions of key combinations at superhuman speeds until the lock finally clicks open.
* **How it works**: Instead of a human manually typing complex prompts to test safety boundaries, a script programmatically generates, mutates, and submits thousands of prompt variations in seconds.
* **Key Concept**: Automation scales up constraint probing far beyond human capacity to expose hidden model blind spots.

## 📊 Quick Comparison

| Concept | Traditional | LLM Era | Impact |
|---------|-------------|---------|--------|
| **Red Teaming** | Manual, slow penetration testing | Automated Python script probes | Massive scale and speed of testing |
| **Fuzzing** | Hand-crafted code edge cases | LLM prompt mutation and variation | Uncovers unexpected semantic blind spots |
| **Evaluation** | Human reading output logs | Secondary AI scoring the target AI | Enables closed-loop, real-time optimization |

## 🧠 Core Concept

1. **Fuzzing and Mutation**: The script starts with "seed" prompts and automatically mutates them by swapping synonyms, changing languages, or adding hypothetical scenarios.
2. **Batch Execution**: The automated system fires thousands of these modified prompts at the target model simultaneously.
3. **Heuristic Evaluation**: A secondary "evaluator" AI model instantly scores the target's output (low score for refusal, high score for restricted behavior).
4. **Iterative Optimization**: Using search algorithms, the script grabs the highest-scoring prompts, mutates them further, and launches the next wave to gradually break the model.

```python
def run_automated_probe(target_ai, evaluator_ai, objective):
    current_prompts = generate_initial_seeds(objective)

    for iteration in range(MAX_ITERATIONS):
        responses = target_ai.query_batch(current_prompts)
        scores = evaluator_ai.score_batch(responses, objective)

        if max(scores) >= SUCCESS_THRESHOLD:
            print("Vulnerability or blind spot discovered!")
            break

        current_prompts = mutate_prompts(current_prompts, scores)
```

---

← [Prev Chapter](14_base64.md) | [Next Chapter](16_indirect_injection_p.md) →
