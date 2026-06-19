<p align="center">
  <img src="https://github.com/user-attachments/assets/a51e8bb3-b2f3-4595-aee4-2272e2323086" alt="AI Model Atlas Logo" width="150">
</p>

# 🗺️ AI Model Atlas

👉 [Read This First: Why AI-Model-Atlas Exists?](INTRO.md)

## Open-Source AI Learning Map — From Zero to RAG, Agents & Fine-Tuning

> 📖 **Bilingual docs (EN/ZH)** · 36 curriculum modules · 17 deep-dive chapters · Runnable RAG sandbox  
> 🎯 A **learning-focused architecture simulator** — not a production framework, not a live model catalog.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE-CODE)
[![CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-lightgrey)](LICENSE)
[![Bilingual](https://img.shields.io/badge/lang-ZH-green)](README_zh.md)

---

> **📌 Reading guide**  
> - ✅ Great for: learning AI concepts, RAG system design, and hands-on experimentation  
> - ⚠️ Model names & API prices may change — always verify against official docs  
> - 🚫 Not intended for: production deployment or real-time benchmarking

---

## 🧭 Start Here

| I want to… | Go to |
| :--- | :--- |
| 📚 **Learn from scratch** (step-by-step) | [CURRICULUM.md](docs/CURRICULUM.md) — 36 modules, Phase 1→5 |
| 🧬 **Understand the math & internals** | [DEEP_DIVES.md](docs/DEEP_DIVES.md) — 17 chapters |
| 📐 **See the system architecture** | [ARCHITECTURE.md](docs/ARCHITECTURE.md) |
| ▶️ **Run the demo in 5 min** | [Quick Start ↓](#-quick-start) |
| 🗺️ **Pick a learning track** | [Getting Started Guide](docs/GETTING_STARTED.md) |

---

## 📦 What's Inside

| Content | Count | Description |
| :--- | :---: | :--- |
| [Curriculum](docs/CURRICULUM.md) | **36 modules** | Prompt → RAG → API → Fine-tune → Deploy → Agent |
| [Deep Dives](docs/DEEP_DIVES.md) | **17 chapters** | Transformer, MoE, Reasoning, Alignment, Evaluation… |
| [RAG Sandbox](projects/rag-app/README.md) | 1 app | Streamlit demo: cache, rerank, routing, GraphRAG |
| Languages | EN + ZH | Hand-written bilingual docs (not machine-translated) |

---

## 🚀 Quick Start

### Route A: Read the curriculum
→ [CURRICULUM.md](docs/CURRICULUM.md)

### Route B: Run the sandbox
```bash
cd projects/rag-app
pip install -r requirements.txt
streamlit run app.py
```

### Route C: Dive deep
→ [DEEP_DIVES.md](docs/DEEP_DIVES.md)

---

## 🧱 How It Works

**AI Model Atlas** is a teaching-focused RAG architecture simulator. It walks you through the full stack of a modern RAG system — from semantic caching and hybrid retrieval to agent routing and fault recovery — all through runnable code and illustrated concepts.

```mermaid
graph LR
    A[User Query] --> B[Semantic Cache]
    B --> C[Query Rewrite]
    C --> D[Hybrid Retrieval]
    D --> E[Rerank]
    E --> F[LLM Generation]
    F --> G[Guardrails]
    G --> H[Response]
```

> ⚠️ **This is a learning sandbox, not a production system.** All performance numbers are local development estimates.

---

## 📄 License & Contributing

- Code: [MIT](LICENSE-CODE)
- Documentation: [CC BY 4.0](LICENSE)

If you find this project helpful, please consider giving it a ⭐ star — it helps more people discover the roadmap.

---

## ✍️ Author & Maintainer

Developed and maintained by **[Loi Chiang Hao](https://github.com/hao610)** (hao610).  
Focusing on the intersection of Cybersecurity, AI Systems, Cloud Infrastructure, and DevSecOps.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/loi-chiang-hao) [![Portfolio](https://img.shields.io/badge/Portfolio-0A0A0A?style=for-the-badge&logo=opsgenie&logoColor=white)](https://loichianghao.vercel.app/)
