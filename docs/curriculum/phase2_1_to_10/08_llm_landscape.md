# LLM Landscape 🌐

> 📅 Last updated: 2026-10. AI ecosystems iterate rapidly; please refer to official documentation for the latest versions and pricing.

[English] | [中文 (08_llm_landscape_zh.md)](08_llm_landscape_zh.md)

Large Language Models (LLMs) did not appear overnight. They are the result of a massive shift in how computers process human language and logic. Let's explore the current landscape, key architectural paradigms, and how to select the right model.

---

## 🌳 The Evolutionary Tree of LLMs

The modern era of AI began in **2017** with a research paper from Google titled *"Attention Is All You Need"*, introducing the **Transformer** architecture.

```text
               Transformer (Google, 2017)
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
    GPT-1 (OpenAI, 2018)       BERT (Google, 2018)
  (Generative / Decoders)    (Understanding / Encoders)
         │                           │
  ┌──────┴──────┐                    ▼
  ▼             ▼              Specialized NLP
GPT-3        Llama (Meta)
  │             │
  ▼             ▼
GPT-4o, o1   Llama 3.3, DeepSeek-V3/R1, Qwen 2.5
                │
                ▼
   System One Decision Primitives (TypeSafe Jev, 2026)
```

---

## 🆚 Closed-Source (API) vs. Open-Weights

When building an AI application, your first major architectural decision is: **Do we use a cloud API or deploy our own open weights?**

| Feature | Closed-Source APIs (e.g. OpenAI o1/4o, Claude 3.5 Sonnet) | Open-Weights Models (e.g. Llama 3.3, DeepSeek-V3/R1, Qwen 2.5) |
| :--- | :--- | :--- |
| **Ease of Setup** | ⚡ **Instant**: Get an API key, write 3 lines of code. | 🛠️ **Moderate**: Requires hardware, orchestration libraries (Ollama, vLLM, SGLang). |
| **Data Privacy** | ⚠️ **Risk**: Requests route over the internet to external providers. | 🔒 **Absolute**: Host on private on-prem or VPC clusters. Data never leaks. |
| **Customization** | ⚠️ **Constrained**: Prompt engineering and basic cloud fine-tuning. | 🎯 **Full Control**: Deep LoRA/Full parameter tuning, quantization, custom CUDA kernels. |
| **Cost Structure** | 💳 **Pay-per-token**: Scaled consumption; leverages Prompt Caching (50-80% off). | 🖥️ **CapEx/OpEx**: Fixed GPU capital/rental expense with unlimited generation. |

---

## 📏 Understanding Model Sizes and Paradigms

Today's ecosystem spans from micro-latency decision engines to multi-hundred-billion MoE architectures:

### 0. Micro & System One Primitives (<1B Parameters)
* **Examples**: `TypeSafe Jev`, specialized classification / guardrail heads.
* **Characteristics**: Sub-100ms latency, zero text generation overhead, outputs deterministic typed probabilities (`Noul`, `Choice`, `Score`).
* **Capabilities**: Instant security guardrail screening, RAG query routing, and agent tool execution gating before escalating to heavy LLMs.

### 1. Small Edge Models (1B to 9B Parameters)
* **Examples**: `Llama-3.2-3B`, `Llama-3.1-8B`, `Qwen-2.5-7B`, `Gemma-2-9B`.
* **Hardware required**: Standard laptop, Apple Silicon, edge device, or single low-cost cloud GPU.
* **Capabilities**: Fast document summarization, basic entity extraction, local synthetic data filtering, and high-throughput JSON generation.

### 2. Medium Workhorse Models (14B to 32B Parameters)
* **Examples**: `Qwen-2.5-14B/32B`, `DeepSeek-R1-Distill-Qwen-32B`.
* **Hardware required**: High-end consumer GPU (RTX 4090 / 24GB VRAM) or single cloud A10G/L4.
* **Capabilities**: Excellent cost-to-performance ratio. Capable code generation, intricate logical deductions, and bilingual translation.

### 3. Large Frontier & MoE Models (70B+ to 671B Parameters)
* **Examples**: `Llama-3.3-70B`, `Qwen-2.5-72B`, `DeepSeek-V3` / `DeepSeek-R1` (671B MoE with 37B active parameters).
* **Hardware required**: Multi-GPU clusters (e.g. 4x-8x A100/H100 or H200) or high-memory unified systems.
* **Capabilities**: Complex multi-step reasoning, automated competitive programming, autonomous agent tool pipelines, and frontier mathematics.

---

Now that you understand the models, let's learn how to orchestrate them without code in [No-Code Agents](09_no_code_agents.md).
