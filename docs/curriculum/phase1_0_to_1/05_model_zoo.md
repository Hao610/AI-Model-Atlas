# Model Zoo Overview 🦁

> 📅 Last updated: 2026-10. AI ecosystems iterate rapidly; please refer to official documentation for the latest versions and pricing.

[English] | [中文 (05_model_zoo_zh.md)](05_model_zoo_zh.md)

In the AI community, a collection of pre-trained models is affectionately called a **"Model Zoo"**. With dozens of companies building models, it can be overwhelming to track them.

Here is your quick-reference directory comparing the major "families" of modern Large Language Models (LLMs) and System One decision primitives.

---

## 🗺️ The Core LLM Map

| Model Family | Creator | Access Type | Strengths | Weaknesses | Best Used For |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GPT** *(e.g. GPT-4o, o1, o3-mini)* | OpenAI | ❌ Closed Source (API only) | Industry pioneer. Extremely balanced. Reasoning models (o1/o3-mini) excel at competitive STEM/coding. | Expensive tier pricing; data privacy constraints. | Premium enterprise coding, advanced scientific reasoning. |
| **Claude** *(e.g. Claude 3.5 Sonnet, 3.5 Haiku)* | Anthropic | ❌ Closed Source (API only) | Industry-leading coding and agentic workflows. Analytical, nuanced, empathetic prose. | Strict safety refusals on ambiguous prompts. | Production software engineering, complex tool orchestration. |
| **Gemini** *(e.g. Gemini 1.5 Pro, 1.5 Flash)* | Google | ❌ Closed Source (API only) | Massive **Context Window** (up to 2M tokens). Native audio/video multimodal processing and speed. | Occasional inconsistency on short single-turn completions. | Mega-context repo analysis, multimodal document parsing. |
| **Llama** *(e.g. Llama 3.3 70B, Llama 3.1 405B)* | Meta | ✅ Open Weights (Local Deploy) | Gold standard for open enterprise architectures. Llama 3.3 70B matches previous 405B quality. | Requires multi-GPU infrastructure for high concurrency. | Self-hosted enterprise deployments, fine-tuning. |
| **DeepSeek** *(e.g. DeepSeek-V3, DeepSeek-R1)* | DeepSeek | ✅ Open Weights (Local Deploy) | Top-tier multi-head latent attention (MLA) and open reasoning (R1) at ultra-low token costs. | High web endpoint traffic during peak Asian hours. | Cost-effective frontier reasoning, local open weights. |
| **Qwen** *(e.g. Qwen 2.5, Qwen2.5-Coder)* | Alibaba | ✅ Open Weights (Local Deploy) | Exceptional multilingual fluency, state-of-the-art open coding (Qwen2.5-Coder), structured JSON. | Compute-heavy at 72B parameter tier. | Structured data extraction, coding agents, bilingual apps. |
| **Jev** *(System One Decision Primitive)* | TypeSafe AI | ⚡ Fast Decision Engine (API) | Sub-100ms deterministic execution. Typed primitives (`Noul`, `Choice`, `Score`). 0% syntax formatting errors. | Does not produce free text; strictly bound to narrow closed-set questions. | Agent guardrails, high-frequency RAG routing, triage filters. |

---

## 💡 Terminology: Closed vs. Open Weights

* **Closed Weights (Proprietary)**: The model is hosted by the company. You cannot download the file. You pay them a small fee every time you ask a question (via API keys).
* **Open Weights (Often called Open Source)**: The model creator releases the final weights (the parameters). You can download this file for free, run it on your own computer, and modify it without telling anyone.

Now that you have visited the zoo, let's learn the fundamental vocabulary you need to speak like an AI engineer in the [Glossary](07_glossary.md).
