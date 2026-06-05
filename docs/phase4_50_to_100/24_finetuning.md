# Why Fine-Tune? 🎯

[English] | [中文 (24_finetuning_zh.md)](24_finetuning_zh.md)

So far, you have used pre-trained models by giving them instructions (Prompt Engineering) or uploading documents (RAG). 

But sometimes, these methods fail. The model might keep forgetting your formatting rules, struggle to learn your specific coding language, or cost too much because your prompts are thousands of words long.

This is when you need **Fine-Tuning**.

---

## 🧠 What is Fine-Tuning?

Fine-tuning is the process of taking an existing pre-trained model (like Llama 3) and training it further on a smaller, highly specialized dataset to customize its behavior, tone, or knowledge.

```text
[ Pre-trained Model (e.g. Llama 3) ] ──► Knows grammar, facts, general reasoning.
                    │
                    ▼  + [ Your Specialized Dataset ] (e.g. 5,000 corporate chat logs)
[ Fine-Tuned Model ] ──────────────────► Master of your specific style/format.
```

---

## 🆚 Prompt Engineering vs. RAG vs. Fine-Tuning

| Dimension | Prompt Engineering | RAG (Search & Ingest) | Fine-Tuning (Brain Surgery) |
| :--- | :--- | :--- | :--- |
| **Model weights** | ❌ Unchanged | ❌ Unchanged | ✅ Modified |
| **New Knowledge** | ⚠️ Limited (Context window) | ✅ Excellent (Dynamic lookup) | ⚠️ Hard to update facts |
| **Form/Style Control**| ⚠️ Moderate (Can drift) | ⚠️ Moderate | ✅ Perfect (Reads thousands of samples) |
| **Latent Latency** | ⚡ Instant | ⏱️ Added search overhead | ⚡ Extremely fast |
| **Compute Cost** | Low | Low | High (requires training runs) |

---

## 🚦 When to Fine-Tune: The Decision Matrix

Only fine-tune if you meet one of the following scenarios:

### 1. You need extreme format consistency
* *Example*: You need the model to output a very complex JSON structure *every single time* without fail. Prompts can fail 1% of the time. Fine-tuning reduces this error rate to near 0%.

### 2. You want to mimic a highly specific style or voice
* *Example*: Training a model to write exactly like a specific historical figure, or matching your brand's unique copywriting style using 10,000 past articles.

### 3. You need to teach the model a new syntax or skill
* *Example*: Teaching a model to write code in a proprietary programming language used only inside your company.

### 4. You want to save API costs
* If your prompt contains 5,000 words of instructions and examples for every request, you are paying for those tokens every single time. Fine-tuning bakes those instructions *into* the model's brain. You can then use short prompts (e.g. 10 words) and get the same result, saving up to 90% in token fees.

---

Now that you know why we fine-tune, let's learn about the most popular and cost-effective technique to do it in [LoRA Explained](25_lora_explained.md).
