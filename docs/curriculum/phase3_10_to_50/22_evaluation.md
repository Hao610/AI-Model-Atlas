# Model Evaluation: How Good is my AI? 📏

[English] | [中文 (22_evaluation_zh.md)](22_evaluation_zh.md)

If you modify a prompt, swap a database, or fine-tune a model, how do you know if the AI's answers actually got better or worse?

Unlike traditional software where code passes or fails unit tests, AI outputs are subjective. To measure them, we use specialized **Evaluation Methods**.

---

## 🏆 The Core Evaluation Methods

| Method | How it works | Best Used For | Pros & Cons |
| :--- | :--- | :--- | :--- |
| **BLEU / ROUGE** | Counts how many exact words in the AI output match a human reference answer. | Translation, summarization. | ⚡ **Pros**: Instant, free.<br>⚠️ **Cons**: Fails if the AI uses synonyms (e.g. "happy" instead of "glad"). |
| **Human Eval** | Real humans grade the AI output based on a scorecard. | High-risk medical, legal, or premium UX apps. | ⚡ **Pros**: Extremely accurate.<br>⚠️ **Cons**: Very expensive, slow, hard to scale. |
| **Chatbot Arena** *(Elo Rating)* | Blinds two models (Model A vs Model B) on the same prompt. Humans vote on the best reply. | General model benchmarking. | ⚡ **Pros**: Unbiased, reflects human preference.<br>⚠️ **Cons**: Not suitable for private data. |
| **LLM-as-a-Judge** | A larger model (like GPT-4o) reads the prompt, the student model's reply, and grades it from 1 to 10. | RAG systems, customer support automation. | ⚡ **Pros**: Fast, automated, cheap, highly scalable.<br>⚠️ **Cons**: Judge models can have a bias towards their own style. |

---

## 🤖 Deep Dive: LLM-as-a-Judge Workflow

This is the industry-standard method for evaluating RAG applications (e.g., using frameworks like **Ragas**).

```text
       [ User Query ] + [ Retrieved Documents ]
                         │
                         ▼
                [ Student AI Answer ]
                         │
                         ▼
        ┌──────────────────────────────────┐
        │        Judge LLM (GPT-4o)        │
        │ - Reads Query & Documents.       │
        │ - Grades Student Answer on:      │
        │   1. Faithfulness (factual?)     │
        │   2. Answer Relevance.           │
        │   3. Hallucination detection.   │
        └────────────────┬─────────────────┘
                         │
                         ▼
                 [ Score Card (1-10) ]
```

By running this automated test suite across 100 historical customer questions before pushing changes to production, you can prevent your AI from deploying bad advice.

---

Congratulations! You have completed **Phase 3 (10 to 50)**! You can now call APIs, run local models, construct web interfaces, deploy multi-agent squads, and run evaluations.

Next, let's enter the elite tier: **Phase 4 (50 to 100)**. Let's learn about model fine-tuning in [Why Fine-Tune?](../phase4_50_to_100/24_finetuning.md).
