← Back to [Deep Dives Directory](../../DEEP_DIVES.md) | [English] | [中文 (11_reasoning_models_zh.md)](11_reasoning_models_zh.md)

---

# 11. How Do Reasoning Models Think?
> **DeepSeek-R1 and o1: The transition from fast intuition to systematic computation.**

Traditional LLMs operate on **System 1 Thinking** (fast, intuitive, immediate). They generate the next word instantly, without a pause to plan. If they make a logical error in the first sentence of an explanation, they are forced to continue writing to justify the mistake, resulting in logical failure.

Modern **Reasoning Models** (like DeepSeek-R1 and OpenAI's o1) introduce **System 2 Thinking** (slow, deliberate, analytical).

```text
Reasoning Model Workflow (Test-Time Compute):
User Query ──► [ Silent Chain of Thought / Verification Loop ] ──► Final Answer
```

#### 1. Chain of Thought (CoT) & Test-Time Compute
Before outputting a single word to the user, the model enters a hidden reasoning phase. It writes out its thinking steps, checks its math, identifies logical fallacies, and corrects itself. The system trades **compute time during generation** (Test-Time Compute) for higher correctness.

#### 2. Reinforcement Learning (RL)
These models are trained using large-scale Reinforcement Learning. The model is given a complex puzzle and rewarded when it finds the correct answer. Through millions of self-play iterations, the model learns strategies like:
* Double-checking assumptions.
* Breaking complex math into smaller equations.
* Backtracking when a chosen logic path hits a dead end.

This shifts AI from a simple text-generation autocomplete box into a systematic cognitive processor.

#### The Draft Paper Analogy: GPT vs. Reasoning Models
To understand the difference between standard LLMs (like GPT-4o) and Reasoning Models (like DeepSeek-R1 or o1), use this analogy:
* **Standard LLM (Intuition)**: The model is in a game show. The moment it sees the question, it must blurt out the answer immediately, word-by-word, without pausing to think. If it starts the sentence with a wrong assumption, it is trapped and must hallucinate a justification to keep the sentence fluent.
* **Reasoning Model (Deliberation)**: The model is given a draft paper. When asked a hard puzzle, it sits in silence, writes out calculations on the draft paper, double-checks its arithmetic, identifies its own mistakes, crosses out wrong paths, and *only* writes down the final clean answer once it is confident.

#### The Cost of Logic & The Inference Scaling Law
This shift in thinking introduces a new paradigm in AI economics and scaling:

1. **Why Reasoning Models Are More Expensive**
In standard models, the token budget is simple: you only pay for the words you see. In reasoning models, you must pay for both **Thinking Tokens** (the draft paper steps generated silently in the background) and **Answer Tokens** (the final visible output). Even a 5-word final answer could require 2,000 thinking tokens of intense computation, making logic highly resource-intensive.

```text
Standard LLM Token Budget:
[ User Query ] ──► [ Answer Tokens ]

Reasoning Model Token Budget:
[ User Query ] ──► [ Thinking Tokens (Hidden draft) + Answer Tokens ]
```

2. **The Inference Scaling Law**
Historically, the only way to make AI smarter was to scale **Training Compute** (feeding larger models more data during training). Reasoning models unlock a second dimension: **Inference Scaling (Test-Time Compute)**. By allowing the model to generate more thinking tokens (i.e., think longer and explore more logical branches), we can scale its performance on complex math, coding, and scientific reasoning tasks without retraining the base model.

---

Reasoning models excel at logical text generation. But how do generative models create visual art? Let's dive into [Why Can AI Draw Pictures?](12_diffusion_art.md).
