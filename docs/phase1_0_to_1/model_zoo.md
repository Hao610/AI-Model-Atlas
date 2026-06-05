# Model Zoo Overview 🦁

[English] | [中文 (model_zoo_zh.md)](model_zoo_zh.md)

In the AI community, a collection of pre-trained models is affectionately called a **"Model Zoo"**. With dozens of companies building models, it can be overwhelming to track them.

Here is your quick-reference directory comparing the major "families" of modern Large Language Models (LLMs).

---

## 🗺️ The Core LLM Map

| Model Family | Creator | Access Type | Strengths | Weaknesses | Best Used For |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GPT** *(e.g. GPT-4o, o1)* | OpenAI | ❌ Closed Source (API only) | Industry pioneer. Extremely balanced. Reasoning models (o1/o3) solve hard STEM problems. | Expensive; data privacy concerns. | Premium general coding, advanced math. |
| **Claude** *(e.g. Claude 3.5 Sonnet)* | Anthropic | ❌ Closed Source (API only) | Outstanding coding performance. Has an analytical, empathetic, and natural writing style. | Occasional strict safety refusal. | Software engineering, copywriting, academic review. |
| **Gemini** *(e.g. Gemini 1.5 Pro)* | Google | ❌ Closed Source (API only) | Massive **Context Window** (can read 2M tokens). Excellent native multimodal capabilities (video, audio). | Quality can sometimes be inconsistent on short inputs. | Analyzing long PDFs, books, or entire code repos. |
| **Llama** *(e.g. Llama 3.1 70B/405B)* | Meta | ✅ Open Weights (Local Deploy) | The gold standard for open models. Massive ecosystem, easy to fine-tune. | Requires decent hardware (GPUs) to run locally at high speeds. | Privacy-first enterprise apps, custom fine-tuning. |
| **DeepSeek** *(e.g. DeepSeek-V3, R1)* | DeepSeek | ✅ Open Weights (Local Deploy) | Incredible reasoning power, fraction of the price of competitors. Excellent at coding/math. | High traffic on web portal. | Budget-conscious projects, local reasoning tasks. |
| **Qwen** *(e.g. Qwen2.5)* | Alibaba | ✅ Open Weights (Local Deploy) | Superb bilingual (English/Chinese) performance. Excels in structured JSON outputs. | Context window size can be smaller on legacy variants. | Multi-lingual tasks, structured data extraction. |

---

## 💡 Terminology: Closed vs. Open Weights

* **Closed Weights (Proprietary)**: The model is hosted by the company. You cannot download the file. You pay them a small fee every time you ask a question (via API keys).
* **Open Weights (Often called Open Source)**: The model creator releases the final weights (the parameters). You can download this file for free, run it on your own computer, and modify it without telling anyone.

Now that you have visited the zoo, let's learn the fundamental vocabulary you need to speak like an AI engineer in the [Glossary](glossary.md).
