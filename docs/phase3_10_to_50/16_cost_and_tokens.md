# Tokenomics & Cost Estimation 💳

[English] | [中文 (16_cost_and_tokens_zh.md)](16_cost_and_tokens_zh.md)

When building an AI application, developers often ask: *"How much will this cost me?"* Unlike traditional cloud services where you pay for servers by the hour, commercial AI models charge you by the **Token** count.

Let's demystify Token calculations and how to estimate your budget.

---

## 🪙 1. How Model Billing Works

Commercial APIs (like OpenAI or DeepSeek) split your costs into two columns:

1. **Input Tokens (Prompt)**: The words you send to the model + your system instructions + your RAG documents.
2. **Output Tokens (Completion)**: The words the model writes back to you.

*Note: Input tokens are always cheaper than output tokens because outputting tokens requires active GPU computation step-by-step.*

---

## 📈 2. Cost Comparison (Per 1 Million Tokens)

To give you a real sense of pricing, here is a comparison of typical market rates (approximate USD rates per 1,000,000 tokens):

| Model | Input Cost (per 1M) | Output Cost (per 1M) | Relative Price Level |
| :--- | :--- | :--- | :--- |
| **GPT-4o** | \$2.50 | \$10.00 | 🟥 Premium |
| **Claude 3.5 Sonnet** | \$3.00 | \$15.00 | 🟥 Premium |
| **GPT-4o-mini** | \$0.150 | \$0.600 | 🟨 Budget Friendly |
| **DeepSeek V3 / R1** | \$0.14 | \$0.28 | 🟩 Ultra Cheap |

### 🧮 Practical Example: The Math
Imagine you run a RAG Customer Support Bot that answers 1,000 tickets a day.
* Each ticket sends a **1,500-token prompt** (FAQ documents + history + user question).
* The AI replies with a short **200-token answer**.

Using **GPT-4o**:
$$\text{Input: } 1000 \times 1500 \text{ tokens} = 1.5\text{M tokens} \times \$2.50 = \$3.75$$
$$\text{Output: } 1000 \times 200 \text{ tokens} = 0.2\text{M tokens} \times \$10.00 = \$2.00$$
$$\text{Total Daily Cost} = \$5.75 \text{ (\$172.50 per month)}$$

Using **DeepSeek V3**:
$$\text{Input: } 1.5\text{M tokens} \times \$0.14 = \$0.21$$
$$\text{Output: } 0.2\text{M tokens} \times \$0.28 = \$0.056$$
$$\text{Total Daily Cost} = \$0.266 \text{ (\$7.98 per month)}$$

*This 95% price reduction explains why choosing the right model architecture is critical for business viability.*

---

## 🖥️ 3. GPU Renting vs. API Keys vs. Local Hardware

If you decide to run open models, how do the hardware hosting costs compare to paying for API keys?

| Hosting Mode | Financial Profile | Best Used For |
| :--- | :--- | :--- |
| **Pay-As-You-Go APIs** | Variable cost. You only pay when a user chats. | **Early stages / Low traffic**: If you have 10 users, this is always the cheapest option. |
| **Cloud GPU Renting** (vLLM) | Fixed hourly cost (e.g. \$1.50/hr for an A100). | **High traffic**: If you have thousands of users queries per minute, a dedicated GPU server is cheaper than paying API fees per token. |
| **Buying Local Hardware** | Large upfront capital expense (\$1,600+ for an RTX 4090). | **Offline usage / Privacy**: 100% free forever after the purchase, completely private. |

---

Now that you can calculate your costs, let's learn how to prep and clean your training data before starting a fine-tuning run in [Data Preparation](../phase4_50_to_100/23_data_preparation.md).
