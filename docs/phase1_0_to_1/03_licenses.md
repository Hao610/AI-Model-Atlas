# Open Source Licenses Demystified 📜

[English] | [中文 (03_licenses_zh.md)](03_licenses_zh.md)

In the AI ecosystem, developers release models and code under different rules. Knowing these rules is crucial: using a model with the wrong license for a commercial product could result in a massive lawsuit.

Here is a simple dictionary of the most common open-source software and open-weights model licenses.

---

## 🏛️ The Software License Scale (Code & Libraries)

These licenses apply to software code (like RAG tools or web search wrappers).

```text
Permissive (Do whatever you want) ──────────────────────────► Copyleft (Share back)
       MIT                  Apache 2.0                            GPL v3
```

| License | Can I use it commercially? | Can I close the source of my changes? | Special Conditions |
| :--- | :--- | :--- | :--- |
| **MIT** | ✅ Yes | ✅ Yes | Extremely permissive. Just include the original copyright notice. |
| **Apache 2.0** | ✅ Yes | ✅ Yes | Highly permissive. Also includes a **patent grant** (protects you from patent lawsuits by contributors). |
| **GPL v3** | ✅ Yes | ❌ No | **Viral license**. If you modify GPL code and distribute it, your entire project *must* become open-source under GPL. |

---

## 🤖 The Model Weights License Scale

Models are not traditional code; they are huge files of numbers (weights). Creators often write custom licenses for them.

### 1. Fully Open Source (OSI-Approved)
Models like **Gemma 2** or **Llama** are often called "open source," but technically, some have custom restriction clauses. Genuine OSI-approved open models allow unconditional commercial and research use.

### 2. "Open Weights" (With Restrictions)
Many modern model creators restrict usage to protect their business:

* **Meta Llama License (e.g., Llama 3)**:
  * **Commercial Use**: Free to use commercially *unless* your app reaches **700 million monthly active users** (at which point you must request a license from Meta).
  * **Derivative work rule**: You cannot use Llama outputs to train competing language models.
* **Qwen License (Alibaba)**:
  * Similar to Llama, but has user-count thresholds (typically free up to 100 million monthly active users depending on the model version).
* **DeepSeek License (DeepSeek-APGL-like / Custom)**:
  * Permits commercial usage, but forbids using model outputs to improve other competing models.

---

## 💡 Summary Checklist for Beginners

1. **If you are building a commercial startup**: Stick to **MIT** or **Apache 2.0** libraries, and check if your model (like Llama/Qwen) has monthly active user (MAU) restrictions that you might cross.
2. **If you are training a model**: NEVER use outputs from OpenAI (GPT) or Anthropic (Claude) to train your open weights model; their Terms of Service strictly forbid creating competing models using their generation.

---

Now that you know the legal playground, let's look at the actual apps you can play with today in the [AI Tools Guide](04_ai_tools.md).
