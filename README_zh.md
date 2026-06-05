# AI-Model-Atlas 🗺️ | AI 模型图谱

> **零基础到生产部署的系统化 AI 工程实战路线图。**

[[English] (README.md)](README.md) | [中文]

欢迎来到 **AI-Model-Atlas** (AI 模型图谱)！本项目是一个系统化、面向初学者的“字典式”实战指南。我们的目标是：**帮助没有任何 IT、代码或算法背景的零基础学习者，一路打通关，直到能够调用、本地运行、量化并微调大模型。**

---

## 🎯 本项目适合谁？

* 🧭 **零基础小白** → 通过通俗比喻和无数学公式的解构，轻松跨越 AI 概念门槛。
* 💻 **应用层开发者** → 掌握 API 接入、本地大模型运行以及快速 Web 界面开发。
* 🏗️ **AI 系统架构师** → 学习工业级 RAG 架构设计、多 Agent 协同流编排及向量数据库检索优化。
* 🚀 **硬核研究与极客** → 深入模型微调（LoRA）、量化压缩原理、算力选型及云端 GPU 高并发部署。

---

## 📍 快速开始 → 学习路径导航

为了让你更清晰地根据个人目标进行针对性学习，建议选择以下量身定制的通关路线：

```mermaid
flowchart TD
    Start([🚀 起点: 00_learning_map]) --> PathA[零代码速成路线]
    Start --> PathB[低代码/无代码路线]
    Start --> PathC[全栈 AI 工程师路线]
    
    PathA --> P1[阶段一：AI 核心概念、提示词艺术与办公工具]
    PathB --> P2[阶段二：工作流设计、Dify 搭建与无代码 Agent]
    PathC --> P3[阶段三：API 编写、Python 开发、Embeddings 与 RAG 设计]
    PathC --> P4[阶段四：LoRA 微调实操、模型量化压缩与云端算力服务部署]

    classDef default fill:#1f2937,stroke:#374151,stroke-width:1px,color:#f9fafb;
    classDef highlight fill:#3b82f6,stroke:#1d4ed8,stroke-width:2px,color:#fff;
    class Start highlight;
```

---

## 🗺️ “从 0 到 100” 学习路线图

以下是为你精心设计的进阶路径，每一阶段都为下一阶段打下坚实的基础。

| | 31. 云端 GPU 算力部署 | 租用 AutoDL / RunPod 显卡，并完成开源模型的私有化服务上线。 | [31_deployment.md](docs/phase4_50_to_100/31_deployment.md) | [31_deployment_zh.md](docs/phase4_50_to_100/31_deployment_zh.md) |

---

## 💡 本仓库设计原则

1. **文字第一，免于维护**：我们坚决不用界面截图。因为 AI 平台和工具的 UI 变化极快，截图极易失效。我们通过手绘 Markdown 图表、表格对比和文字解构来传达永不过时的原理。
2. **拒绝生硬机翻，真双语并行**：英文版 and 中文版均是由算法开发人员人工编写与校验，用词贴近中西方开发者日常习惯，杜绝死板晦涩的机器直译。
3. **闭环式实操**：不搞纯空洞理论。每一阶段的最后，读者都能得到完整的“配置清单”或“一键启动代码”，确保知识能够真正落地。

---

## 🔗 使用与共建

你可以将它加入收藏夹，或直接 `git clone` 到本地作为你的 **“AI 知识外脑”** 随时查阅。如果您觉得这些整理对您有启发，欢迎在 GitHub 点亮 **Star ⭐**！

---

## 📄 开源协议 (License)

AI-Model-Atlas 遵循 Creative Commons Attribution 4.0 International License (CC BY 4.0) 开源知识共享协议。详细中文说明请参考 [LICENSE_zh](LICENSE_zh)。

只要您遵守署名等基本协议条款，即可自由分享、传播以及进行商业化利用。

Copyright (c) 2026 AI-Model-Atlas

Created and maintained by Loi Chiang Hao.
