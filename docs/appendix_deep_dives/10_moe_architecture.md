← Back to [Deep Dives Directory](../../DEEP_DIVES.md) | [English] | [中文 (10_moe_architecture_zh.md)](10_moe_architecture_zh.md)

---

# 10. Why MoE Makes Scale Affordable
> **Understanding Mixture of Experts: How sparse routing enables giant models at tiny costs.**

Traditionally, when a model like GPT-4 runs inference, every single parameter in the neural network is activated to predict the next word. This is a **Dense Model**. Scaling dense models requires massive compute power, driving up API costs.

**Mixture of Experts (MoE)** converts the network into a **Sparse Model**.

```text
MoE Sparse Routing:
Input Prompt ──► [ Router Network ] ──► Expert 2 (Translation) ──┐
                                    ──► Expert 8 (Coding)      ──┼──► Output
                                    ──► [ Experts 1,3,4... Idle ]┘
```

#### How MoE Works
Instead of one massive neural network, the model is split into multiple smaller sub-networks called **Experts** (e.g., 64 distinct experts, each specializing in coding, math, translation, or creative writing).
1. **The Router**: A lightweight network reads the incoming prompt and determines which experts are best suited to handle it.
2. **Sparse Activation**: The router only activates a small subset (e.g., 2 out of 64 experts) for that specific token.
3. **The Savings**: You get the intelligence of a massive, multi-hundred-billion parameter model, but only pay the compute cost of running a tiny fraction of it. This sparse routing architecture is the core technology behind DeepSeek's high-efficiency pricing model.

---

While MoE makes big models cheaper to run, how do models take the time to reason logically before answering? Explore [How Do Reasoning Models Think?](11_reasoning_models.md).
