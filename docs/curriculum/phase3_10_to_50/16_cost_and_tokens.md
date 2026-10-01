# Tokenomics & Cost Estimation 💳

> 📅 Last updated: 2026-10. AI ecosystems iterate rapidly; please refer to official documentation for the latest versions and pricing.

[English] | [中文 (16_cost_and_tokens_zh.md)](16_cost_and_tokens_zh.md)

When building an AI application, developers often ask: *"How much will this cost me?"* Unlike traditional cloud services where you pay for servers by the hour, commercial AI models charge you by the **Token** count.

Let's demystify Token calculations and how to estimate your budget in modern 2026 production architectures.

---

## 🪙 1. How Model Billing Works

Commercial APIs split your costs into three distinct dimensions:

1. **Uncached Input Tokens (Prompt)**: The words you send to the model + your system instructions + your RAG documents.
2. **Cached Input Tokens (Prompt Caching)**: When consecutive requests share identical prefixes (such as system prompts or document context), KV-caches allow providers to bill at **50% to 90% discount**.
3. **Output Tokens (Completion + Reasoning)**: The words the model writes back to you. For reasoning models (o1, DeepSeek-R1), *internal "thinking" tokens are billed at full output token rates*.

---

## 📈 2. Cost Comparison (Per 1 Million Tokens — 2026.10 Rates)

Here is a comparison of typical market rates (approximate USD rates per 1,000,000 tokens):

| Model (2026.10 Snapshot) | Input Price (per 1M) | Cached Input (per 1M) | Output Price (per 1M) | Architectural Notes |
| :--- | :--- | :--- | :--- | :--- |
| **GPT-4o** (Flagship Multimodal) | $2.50 | $1.25 (50% off) | $10.00 | Multimodal, reliable standard |
| **OpenAI o1 / o3-mini** (Reasoning) | $1.10 - $15.00 | $0.55 - $7.50 | $4.40 - $60.00 | Deep CoT; reasoning tokens billed as output |
| **Claude 3.5 Sonnet** (Anthropic) | $3.00 | $0.30 (90% off) | $15.00 | Industry leader in coding & tool agents |
| **Claude 3.5 Haiku** | $0.80 | $0.08 (90% off) | $4.00 | Ultra-fast lightweight API |
| **Gemini 1.5 Pro** (Google) | $1.25 | $0.31 (75% off) | $5.00 | 2M context window, native multimodal |
| **DeepSeek-V3** | $0.14 | $0.014 (90% off) | $0.28 | MLA MoE architecture, extreme cost efficiency |
| **DeepSeek-R1** (Reasoning) | $0.55 | $0.14 (75% off) | $2.19 | Open frontier reasoning model |
| **TypeSafe Jev** (System One) | ~$0.05 / 1k calls | N/A (Stateful) | $0.00 (Zero-text) | Sub-100ms typed primitives (`Noul`, `Choice`) |

---

## ⚡ 3. Modern 2026 Cost Mechanics

### A. Prompt Caching Economics
In production RAG or multi-agent pipelines, 80%+ of the input prompt consists of repetitive instructions, tool JSON schemas, and static context. Leveraging **KV Cache retention** drops recurring RAG input costs by up to 90% (e.g., DeepSeek-V3 cached input is just \$0.014 / 1M tokens).

### B. The Hidden Cost of Reasoning Tokens
Reasoning models like OpenAI o1 or DeepSeek-R1 generate hundreds or thousands of intermediate "thinking" tokens. While invisible in standard chat UI, these thinking tokens count against your output quota. A 30-word response may incur 1,500 reasoning tokens ($1,500 \times \$60.00 / 1\text{M} = \$0.09$ per query).

### C. System One Cascading (TypeSafe Jev)
Instead of invoking heavy LLMs for every input screening, routing, and guardrail check:
$$\text{Cost}_{\text{Cascaded}} = P(\text{simple}) \times \text{Cost}_{\text{Jev}} + (1 - P(\text{simple})) \times \text{Cost}_{\text{LLM}}$$
Because 70–85% of queries can be fast-passed or fast-blocked in sub-100ms by Jev, pipeline operational costs drop by 60–80% overall.

---

### 🧮 Practical Example: The Math
Imagine you run a RAG Customer Support Bot that answers 1,000 tickets a day.
* Each ticket sends a **1,500-token prompt** (FAQ documents + history + user question).
* The AI replies with a short **200-token answer**.

Using **GPT-4o**:
$$\text{Input: } 1000 \times 1500 \text{ tokens} = 1.5\text{M tokens} \times \$2.50 = \$3.75$$
$$\text{Output: } 1000 \times 200 \text{ tokens} = 0.2\text{M tokens} \times \$10.00 = \$2.00$$
$$\text{Total Daily Cost} = \$5.75 \text{ (\$172.50 per month)}$$

Using **DeepSeek-V3** (with 80% prompt cache hit rate):
$$\text{Uncached Input: } 0.3\text{M tokens} \times \$0.14 = \$0.042$$
$$\text{Cached Input: } 1.2\text{M tokens} \times \$0.014 = \$0.0168$$
$$\text{Output: } 0.2\text{M tokens} \times \$0.28 = \$0.056$$
$$\text{Total Daily Cost} \approx \$0.115 \text{ (\$3.45 per month)}$$

*A 98% operational cost reduction compared to naive un-cached flagship calls.*

---

## 🖥️ 4. GPU Renting vs. API Keys vs. Local Hardware

If you decide to run open models, how do the hardware hosting costs compare to paying for API keys?

| Hosting Mode | Financial Profile | Best Used For |
| :--- | :--- | :--- |
| **Pay-As-You-Go APIs** | Variable cost. You only pay when a user chats. | **Early stages / Low traffic**: If you have 10 users, this is always the cheapest option. |
| **Cloud GPU Renting** (vLLM / SGLang) | Fixed hourly cost (e.g. \$1.50/hr for an A100/L40S). | **High traffic**: When sustained queries exceed 50+ QPS, dedicated GPU serving beats API token fees. |
| **Buying Local Hardware** | Large upfront capital expense (\$1,600+ for an RTX 4090). | **Offline usage / Privacy**: 100% free forever after purchase, completely private. |

---

Now that you can calculate your costs, let's learn how to prep and clean your training data before starting a fine-tuning run in [Data Preparation](../phase4_50_to_100/23_data_preparation.md).
