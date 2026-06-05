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

---

Reasoning models excel at logical text generation. But how do generative models create visual art? Let's dive into [Why Can AI Draw Pictures?](12_diffusion_art.md).
