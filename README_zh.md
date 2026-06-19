<p align="center">
  <img src="https://github.com/user-attachments/assets/a51e8bb3-b2f3-4595-aee4-2272e2323086" alt="AI Model Atlas Logo" width="250">
</p>

# 🗺️ AI Model Atlas

👉 [阅读必看：为什么需要 AI-Model-Atlas？](INTRO_zh.md)

## 开源 AI 学习地图 — 从零到 RAG、智能体与微调

> 📖 **中英双语文档** · 36 个课程模块 · 17 章深潜专题 · 可运行的 RAG 沙盒  
> 🎯 一个**面向教学的架构模拟器**——不是生产框架，也不是实时型号百科。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE-CODE)
[![CC BY 4.0](https://img.shields.io/badge/%E6%96%8B%E6%A1%A3-CC%20BY%204.0-lightgrey)](LICENSE)
[![Bilingual](https://img.shields.io/badge/lang-EN-green)](README.md)

---

> **📌 阅读说明**  
> - ✅ 适合：AI 概念入门、RAG 系统设计学习、动手实验  
> - ⚠️ 文中的模型名称与 API 价格可能已更新，请以各厂商官网为准  
> - 🚫 不适合：直接用于生产部署或作为实时价格/排行榜

---

## 🧭 从这里开始

| 我想… | 去这里 |
| :--- | :--- |
| 📚 **系统学习**（从零开始） | [CURRICULUM_zh.md](docs/CURRICULUM_zh.md) — 36 模块，Phase 1→5 |
| 🧬 **理解原理与内部机制** | [DEEP_DIVES_zh.md](docs/DEEP_DIVES_zh.md) — 17 章 |
| 📐 **查看系统架构** | [ARCHITECTURE_zh.md](docs/ARCHITECTURE_zh.md) |
| ▶️ **5 分钟跑起来** | [快速开始 ↓](#-快速开始) |
| 🗺️ **选择一条学习路径** | [入门指南](docs/GETTING_STARTED_zh.md) |

---

## 📦 内容一览

| 内容 | 数量 | 说明 |
| :--- | :---: | :--- |
| [课程](docs/CURRICULUM_zh.md) | **36 模块** | Prompt → RAG → API → 微调 → 部署 → Agent |
| [深潜专题](docs/DEEP_DIVES_zh.md) | **17 章** | Transformer, MoE, 推理模型, 对齐, 评测… |
| [RAG 沙盒](projects/rag-app/) | 1 个应用 | Streamlit 演示：缓存、重排、路由、GraphRAG |
| 语言 | 中 + 英 | 手写双语对照，非机器翻译 |

---

## 🚀 快速开始

### 路线 A：阅读课程
→ [CURRICULUM_zh.md](docs/CURRICULUM_zh.md)

### 路线 B：运行沙盒
```bash
cd projects/rag-app
pip install -r requirements.txt
streamlit run app.py
```

### 路线 C：深入专题
→ [DEEP_DIVES_zh.md](docs/DEEP_DIVES_zh.md)

---

## 🧱 项目原理

**AI Model Atlas** 是一个教学导向的 RAG 架构模拟器。它带你走完现代 RAG 系统的全链路——从语义缓存、混合检索，到智能体路由与故障恢复——全部通过可运行代码和可视化概念呈现。

```mermaid
graph LR
    A[用户提问] --> B[语义缓存]
    B --> C[查询改写]
    C --> D[混合检索]
    D --> E[重排序]
    E --> F[LLM 生成]
    F --> G[安全护栏]
    G --> H[返回结果]
```

> ⚠️ **这是一个学习沙盒，不是生产系统。** 所有性能数据均为本地开发环境测试值。

---

## 📄 许可与贡献

- 代码：[MIT](LICENSE-CODE)
- 文档：[CC BY 4.0](LICENSE)

如果这个项目对你有帮助，欢迎点一个 ⭐ star —— 让更多学习者发现这张学习地图。

---

## ✍️ 作者与维护者 (Author & Maintainer)

由 **[Loi Chiang Hao](https://github.com/hao610)** (hao610) 开发与维护。  
核心专注于**网络安全 (Cybersecurity)**、**人工智能系统 (AI Systems)**、**云基础设施 (Cloud Infrastructure)** 以及 **DevSecOps** 的交叉技术领域。

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/loi-chiang-hao) [![Portfolio](https://img.shields.io/badge/Portfolio-0A0A0A?style=for-the-badge&logo=opsgenie&logoColor=white)](https://loichianghao.vercel.app/)

