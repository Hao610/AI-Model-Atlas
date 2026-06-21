# Safety & Alignment: The Boundaries of AI 🛡️

[English] | [中文 (30_safety_alignment_zh.md)](30_safety_alignment_zh.md)

If you ask an AI model, *"How do I hotwire a car?"* or *"Tell me a joke about my boss,"* it might reply: *"I cannot fulfill this request. I am programmed to be a helpful and harmless assistant."*

Why does this happen? The model has gone through a process called **Alignment** to make sure it respects human safety boundaries.

---

## 🏗️ The Three Training Stages of LLMs

An AI model goes through three main phases of birth:

```text
[ 1. Pre-Training ] ──► Reads the whole internet. Can write anything, unfiltered.
         │
         ▼
[ 2. Instruction Tuning (SFT) ] ──► Learns to act as an assistant (answering questions).
         │
         ▼
[ 3. Alignment (Safety) ] ──► Learns what it SHOULD and SHOULD NOT say.
```

---

## 🤝 Alignment Techniques: RLHF and DPO

How do we teach a model what is good and bad? We use two main methods:

### 1. RLHF (Reinforcement Learning from Human Feedback)
* **How it works**: The model generates two different answers to the same prompt. A human evaluator reviews both and marks one as "good" (helpful, safe) and the other as "bad" (dangerous, rude).
* **The Reward**: A second "reward model" learns these human preferences. It then scores the main model's outputs, acting like a school teacher giving stars for good behavior.

### 2. DPO (Direct Preference Optimization)
* **How it works**: A newer, simpler alternative to RLHF. Instead of training a separate reward model, DPO mathematically updates the main model's weights directly using pairwise dataset logs (e.g. `[Chosen Answer, Rejected Answer]`).
* **Why it's popular**: It is much faster, uses less GPU memory, and is highly effective for fine-tuning.

---

## 🚧 Guardrails: Safety Filters in Production

Alignment changes the inner weights of the model. But to guarantee safety in production apps, companies add an external layer called **Guardrails**.

```text
User Input ──► [ Input Guardrail Filter ] ──► LLM ──► [ Output Guardrail Filter ] ──► User Output
```

* **Input Guardrail**: Scans the user's prompt *before* it reaches the LLM to detect hacking attempts (prompt injection) or prohibited topics.
* **Output Guardrail**: Scans the generated text *before* displaying it to the user to block toxic language or leaked credit card numbers.
* **Popular Tools**: **Llama Guard** (a specialized safety model by Meta), **NeMo Guardrails** (by Nvidia).

---

Now that you understand safety boundaries, let's learn how to take your model and launch it on a cloud server for public use in [Cloud Deployment](31_deployment.md).
