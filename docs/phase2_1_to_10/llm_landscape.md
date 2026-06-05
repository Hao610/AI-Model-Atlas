# LLM Landscape 🌐

[English] | [中文 (llm_landscape_zh.md)](llm_landscape_zh.md)

Large Language Models (LLMs) did not appear overnight. They are the result of a massive shift in how computers process human language. Let's explore the current landscape, key players, and how to choose the right model.

---

## 🌳 The Evolutionary Tree of LLMs

The modern era of AI began in **2017** with a research paper from Google titled *"Attention Is All You Need"*, which introduced the **Transformer** architecture.

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
ChatGPT     DeepSeek, Qwen
```

---

## 🆚 Closed-Source (API) vs. Open-Weights

When building an AI application, the first major architectural decision you will make is: **Do we use a cloud API or deploy our own model?**

| Feature | Closed-Source APIs (e.g. OpenAI, Claude) | Open-Weights Models (e.g. Llama, Qwen, DeepSeek) |
| :--- | :--- | :--- |
| **Ease of Setup** | ⚡ **Instant**: Get a key, write 3 lines of code. | 🛠️ **Moderate**: Requires hardware, software libraries (Ollama/vLLM). |
| **Data Privacy** | ⚠️ **Risk**: Your data is sent over the internet to a third party. | 🔒 **Secure**: Run it on your local server. Data never leaves your network. |
| **Customization** | ⚠️ **Limited**: Only prompt tuning and basic cloud fine-tuning. | 🎯 **Full Control**: Deep fine-tuning, customize model weights. |
| **Cost Structure** | 💳 **Pay-per-use**: Costs scale with user traffic (tokens). | 🖥️ **Capital expense**: Pay for the server/GPU once, run it infinitely. |

---

## 📏 Understanding Model Sizes (Parameters)

Open-weights models are usually named with a number indicating their parameter count (e.g., `Llama-3-8B`, `Qwen-72B`). Here is how to understand these sizes:

### 1. Small Models (1B to 9B Parameters)
* **Examples**: `Llama-3-8B`, `Qwen-2.5-7B`, `Gemma-2-9B`.
* **Hardware required**: Standard laptop, mobile phone, or cheap cloud hosting.
* **Capabilities**: Excellent for basic text classification, summarizing single articles, simple chatbots, and parsing unstructured text into JSON.

### 2. Medium Models (14B to 32B Parameters)
* **Examples**: `Qwen-2.5-14B`, `DeepSeek-Lite-16B`.
* **Hardware required**: High-end gaming PC (RTX 3090/4090) or mid-range cloud server.
* **Capabilities**: A great sweet-spot. Decent coding abilities, complex logical reasoning, and basic translation.

### 3. Large Models (70B+ Parameters)
* **Examples**: `Llama-3-70B`, `Qwen-2.5-72B`, `DeepSeek-V3` (671B MoE).
* **Hardware required**: Enterprise GPU servers (Mac Studio with 192GB Unified Memory, or multiple A100/H100 cards).
* **Capabilities**: Near-human level reasoning, advanced code generation, multi-step planning, and complex agent workflows.

---

Now that you understand the models, let's learn how to orchestrate them without code in [No-Code Agents](no_code_agents.md).
