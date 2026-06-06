# 🗺️ AI Model Atlas

## A Learning-Focused RAG Architecture Simulator

AI Model Atlas is a **learning-focused system design simulator** for understanding how production RAG systems actually work, and why most tutorial-level implementations fail in real-world scenarios.

This project is **not a production framework or deployment system**. It is an educational system for studying real-world AI architecture patterns.

[English] | [中文 (README_zh.md)](README_zh.md)

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg?style=for-the-badge)](LICENSE)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE-CODE)
[![Run Locally](https://img.shields.io/badge/▶_Local_Sandbox_App-10b981?style=for-the-badge&logo=play)](#route-a-local-sandbox-interactive-ui-recommended)
[![Colab Playground](https://img.shields.io/badge/▶_Colab_Playground_(Optional)-orange?style=for-the-badge&logo=googlecolab)](https://colab.research.google.com/github/Hao610/AI-Model-Atlas/blob/main/projects/rag-app/quickstart.ipynb)

---

## 📌 What this project is

AI Model Atlas breaks down how modern RAG systems behave under real-world complexity.

It helps you understand:
* How production RAG systems are structured
* Why simple “vector search ➔ LLM” pipelines break
* Where routing, caching, and orchestration become necessary
* How system design changes from demo ➔ production scale

---

## ⚠️ The problem with most RAG tutorials

Most RAG systems look like this:
> User ➔ Embedding Search ➔ LLM

This is simple, but incomplete. In real-world systems, this design fails because:
* No routing between tools (everything goes to vector search)
* No caching layer (every request hits the LLM)
* No evaluation or feedback loop
* No failure recovery or retry logic
* No hybrid retrieval (BM25 + dense + fusion)
* No system-level orchestration or control flow

👉 This project exists to make these missing layers visible.

---

## 🧱 System design (conceptual)

This is not a chatbot. It is a **decomposition of a full RAG system architecture**:

### 🧠 Intelligence Layer
* Query routing (tool selection logic)

### 🔍 Retrieval Layer
* Hybrid retrieval (BM25 + dense + RRF fusion)
* Graph-based reasoning concepts (GraphRAG)

### ⚡ Optimization Layer
* Semantic caching (fast-path execution simulation)

### 🛡️ Reliability Layer
* Evaluation concepts (LLM-as-a-judge)
* Execution control (retry / fallback / timeout logic)

---

## 🧩 What makes this different

Instead of building another demo application, this project focuses on:
> How real AI systems behave under failure, scale, and system complexity.

It is designed as:
* A structured learning system (36 modules)
* A reference architecture for RAG system design
* A conceptual simulation of production AI pipelines

---

## ⚡ Example behavior (conceptual)

User: “What is Llama 3 license?”
➔ **Routing selected** (vector + web tools)
➔ **Hybrid retrieval executed**
➔ **No cache hit** ➔ LLM response generated
➔ **Evaluation step triggered**

Repeat query:
➔ **Cache hit detected**
➔ Retrieval + LLM skipped
➔ **Instant response** (~0.0001s simulated)

---

## 🎯 What you will learn

* Why naive RAG architectures fail in production
* Why routing is required beyond vector search
* Why caching is critical for cost and latency control
* How hybrid retrieval improves grounding quality
* Why evaluation layers are necessary in real systems
* How production AI systems are structured end-to-end

---

## 🚀 Who this is for

* Developers learning RAG system design
* Engineers moving from demos ➔ production thinking
* AI learners studying system-level architecture
* Anyone building agent-based or tool-using LLM systems

---

## ⭐ Note

This project is intended for **learning and system design exploration only**, not production deployment.

## 🧭 System Architecture Poster

```mermaid
flowchart LR
    Query([User Query]) --> Pre[1. Preprocess & Rewrite]
    Pre --> Cache{2. Semantic Cache?}
    
    Cache -->|Hit| CacheHit[Fast Cache Output 0.00s]
    Cache -->|Miss| RAG[3. Vector Search & Rerank]
    
    RAG --> Controller[4. Execution Controller]
    Controller --> LLM[5. Hybrid LLM Route]
    
    CacheHit --> Output([Final Output])
    LLM --> Output

    classDef default fill:#111827,stroke:#374151,stroke-width:1px,color:#f9fafb;
    classDef highlight fill:#10b981,stroke:#047857,stroke-width:2px,color:#fff;
    classDef title fill:#1f2937,stroke:#4b5563,stroke-width:1px,color:#f3f4f6;

    class CacheHit highlight;
```

---

## 🚀 Quick Start (Run Path Selector)

Select your preferred route to experience `AI Model Atlas` in under 60 seconds:

### Route A: Local Sandbox Interactive UI (Recommended)
Run the Streamlit observability app locally with semantic cache, reranking, and self-healing:
1. **Clone the repository and navigate to the project directory:**
   ```bash
   git clone https://github.com/Hao610/AI-Model-Atlas.git
   cd AI-Model-Atlas/projects/rag-app
   ```
2. **Install core dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Launch the application dashboard:**
   ```bash
   python app.py
   ```
   *Note: Ensure Ollama is running locally if you want offline model execution.*

### Route B: Run the Streamlit App Directly
Enter the runnable example project and start the dashboard from your terminal:
```bash
cd projects/rag-app
streamlit run app.py
```

### Route C: Guided Conceptual Onboarding
If you want to read the step-by-step guides instead of running code, start here:
👉 **[00_learning_map.md](docs/phase1_0_to_1/00_learning_map.md)**

> **ℹ️ About Colab Playground**: Colab is provided as an optional fallback runtime. For a more reliable demo experience, we recommend running the local sandbox (Route A). Colab availability depends on Google's free backend capacity and may fail during peak usage.

---

### 🧩 What will I see in 30 seconds?

Here is the raw telemetry output from a typical cache-miss and cache-hit sequence:

```text
[🔄 Rewrite] Query normalized: "Tell me about Llama 3 license" -> "llama 3 license parameters"
[⚡ Cache]   Miss! ❌ Routing to retrieval & hybrid LLM.
[🎯 Rerank]  Passed Margin Filter (Cosine similarity: 0.89).
[Response]  "Llama 3 is licensed under..." (Latency: 1.25s)

--- Ask again: "Tell me about Llama 3 license" ---
[🔄 Rewrite] Query normalized: "Tell me about Llama 3 license" -> "llama 3 license parameters"
[⚡ Cache]   Hit! ✅ Bypassing vector search and LLM invocation.
[Response]  "Llama 3 is licensed under..." (Latency: 0.0001s)
```

---

## 💡 Why This Repository Exists

Most RAG tutorials stop at embeddings or naïve retrieval demos. `AI Model Atlas` goes further, providing a real-world, engineer-grade cognitive RAG reference architecture. By integrating Semantic Cache, Query Rewriting, Relevance Reranking, and an Execution Controller, it bridges the gap between toy demos and production-ready systems.

---

## 🚀 What This Project Offers

- **🚦 Retrieval Orchestration Layer**: A deterministic regex-based router dispatching queries to Calculator, Web Search, Graph, or Vector tools.
- **📊 Lightweight Evaluation Framework**: A native LLM-as-a-judge engine designed to evaluate routing accuracy, faithfulness, and groundedness.
- **👁️ Vision RAG & Structural Parsing**: Transparent, multi-engine extraction (`pdfplumber` + `PyMuPDF`) that preserves explicit table boundaries and natively filters structural images.
- **📦 Table-Aware Chunking**: Dynamic atomic vector blocks to guarantee tabular integrity during LLM retrieval.
- **🕸️ GraphRAG Knowledge Network**: A native, lightweight Knowledge Graph extractor using NetworkX with two-stage relation extraction and 1-hop traversal routing.
- **🧠 Cognitive Query Rewriting**: Dynamic regex and prompt filters to normalize user intents before retrieval.
- **🎯 Relevance Reranking**: Reciprocal Rank Fusion (RRF) combining Dense and Sparse (BM25) search scores.
- **🛡️ Execution Controller**: Orchestrated request center with fallback routing, exponential backoffs, and timeouts.
- **🌐 Hybrid LLM Core**: Dynamic routing between local Ollama installations and commercial OpenAI/DeepSeek API endpoints.
- **⚡ Semantic Cache**: Lightweight vector embedding dictionary checks for extreme latency reduction.

---

## 🎯 Who is this for?

* 🧭 **Beginners** → Learn fundamental AI concepts with zero mathematical barrier and clear analogies.
* 💻 **Developers** → Master API integration, local model execution, and rapid UI prototyping.
* 🏗️ **Engineers & Architects** → Deploy production-ready RAG architectures, scale agent workflows, and optimize inference.
* 🚀 **Pioneers** → Dive deep into fine-tuning (LoRA), quantization, GPU selection, and cloud serving infrastructure.

---

## 🧭 Choose Your Goal

| Your Goal | Where to Go |
| :--- | :--- |
| 🚀 **Run the system now** | ↑ [Quick Start](#-quick-start-run-path-selector) |
| 🧠 **Understand the architecture** | 📐 [ARCHITECTURE.md](docs/ARCHITECTURE.md) — Benchmarks, failure recovery, state machine |
| 📚 **Learn AI from scratch** | 📚 [CURRICULUM.md](docs/CURRICULUM.md) — 36-module "0 to 200" learning roadmap |
| 🧬 **Deep dive into algorithms** | 🧬 [DEEP_DIVES.md](docs/DEEP_DIVES.md) — The 17-chapter epic tech documentary |

---

## 💡 Repository Design Philosophy

1. **Text-First & Zero-Bloat**: No heavy image files that get outdated when software UI changes. We use elegant Markdown layout, detailed tables, flow charts, and structured lists.
2. **Double Portal, Localized Content**: The English and Chinese versions of the documents are written by hand (no raw robotic translations) ensuring idiomatic, easy-to-understand explanations for developers in both regions.
3. **From Scratch to Cloud**: The guide doesn't stop at "Prompting". It goes all the way to cloud GPU fine-tuning, explaining the full engineering lifecycle of model operation.

---

## 🌍 Built something useful?

If this project helped you learn, build, or deploy Cognitive RAG systems, we invite you to join our growing community:

* **Star & Fork** ⭐: Star the repository to show support and bookmark it for quick access.
* **Share the Journey** 📢: Share the learning path or your own RAG implementation with other developers.
* **Contribute** 🤝: Submit pull requests, report issues, or suggest new modules. Check out our [Contribution Guidelines](.github/CONTRIBUTING.md) for details.
* **Community Rules** 🧭: Read our [Code of Conduct](.github/CODE_OF_CONDUCT.md) and [Security Policy](.github/SECURITY.md) before contributing.

🚀 **Spread the word:**

> Built a production-grade Cognitive RAG system with Semantic Cache, Query Rewriting, Reranking, and Failure Recovery — from learning to deployment. Check out the AI Model Atlas!
> 👉 https://github.com/Hao610/AI-Model-Atlas

## 📄 License

AI Model Atlas uses a dual-license model:

- **Documentation, curriculum, diagrams, and educational materials**: Creative Commons Attribution 4.0 International (see [`/LICENSE`](LICENSE))
- **Source code & runnable examples**: MIT License (see [`/LICENSE-CODE`](LICENSE-CODE))

> This repository distinguishes between software and educational content licensing to ensure clear reuse rights. It is continuously updated, and all new content follows the same licensing model unless explicitly stated otherwise.

Copyright (c) 2026 Loi Chiang Hao.
