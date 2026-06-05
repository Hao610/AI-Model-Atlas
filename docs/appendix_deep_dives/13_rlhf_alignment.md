← Back to [Deep Dives Directory](../../DEEP_DIVES.md) | [English] | [中文 (13_rlhf_alignment_zh.md)](13_rlhf_alignment_zh.md)

---

# 13. Why Does GPT Talk Like a Human?
> **RLHF and DPO: The mechanics of alignment and how safety boundaries are established.**

A raw base LLM trained on the internet is wild and uncontrollable. If you prompt it: *"How do I write a cover letter?"*, it might autocomplete the prompt with: *"How do I write a cover letter for a job I hate? Here is a thread from Reddit..."* It has no concept of helpfulness, safety, or conversational structure.

To turn a base model into a helpful assistant, we use **Alignment** techniques.

```text
Model Alignment Pipeline:
[ Base LLM ] ──► [ Supervised Fine-Tuning ] ──► [ RLHF / DPO ] ──► [ Safe Assistant ]
```

#### 1. RLHF (Reinforcement Learning from Human Feedback)
1. **Labeling**: Humans are presented with two model outputs and asked to grade which one is more helpful and safe.
2. **Reward Model**: We train a second neural network (the Reward Model) to predict what score a human would give to any model output.
3. **PPO Optimization**: We run reinforcement learning on the base LLM, rewarding it when it generates text that scores highly on the Reward Model.

#### 2. DPO (Direct Preference Optimization)
A newer, simpler alternative to RLHF. Instead of training a separate complex Reward Model, DPO mathematically optimizes the LLM directly on pairwise preference datasets (Dataset: `[Prompt, Winning Answer, Losing Answer]`), shifting the model's output probabilities toward the preferred answers in a single step.

Alignment is what forces the model to talk politely, refuse instructions on how to build weapons, and maintain a consistent, helpful conversational persona.

---

Now that you know how we align models to human values, let's learn how we measure model progress in [AI Evaluation: How Do We Know a Model is Strong?](14_ai_evaluation.md).
