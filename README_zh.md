# AI Model Atlas 🗺️ | AI 模型图谱
## 从玩具级 RAG 到生产级 AI 系统

一个生产级的 **RAG 架构演练沙盒**，展示从简单的向量检索教程走向真实 AI 系统时，究竟会发生什么。

[[English] (README.md)](README.md) | [中文]

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg?style=for-the-badge)](LICENSE)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE-CODE)
[![本地沙盒 UI](https://img.shields.io/badge/▶_本地沙盒应用-10b981?style=for-the-badge&logo=play)](#%E8%B7%AF%E5%BE%84-a%E6%9C%AC%E5%9C%B0%E6%B2%99%E7%9B%92%E4%BA%A4%E4%BA%92%E5%BC%8F-ui-%E6%8E%A8%E8%8D%90)
[![Colab 在线体验](https://img.shields.io/badge/▶_Colab_在线玩转_(可选)-orange?style=for-the-badge&logo=googlecolab)](https://colab.research.google.com/github/Hao610/AI-Model-Atlas/blob/main/projects/rag-app/quickstart.ipynb)

绝大多数 RAG 演示都止步于“向量检索 + LLM”。**AI Model Atlas 走得更远 —— 深入剖析生产环境中的故障痛点：路由、缓存、评测、编排与自愈。**

---

## ⚠️ 为什么存在本项目

大多数 RAG 教程的运行逻辑都是这样的：
> 用户 ➔ 向量检索 ➔ 大模型 ➔ 生成答案

但在真实系统的生产环境中，会遇到教程中从未提及的崩溃点：
* ❌ **工具之间缺乏路由**（所有查询一律塞给向量检索）
* ❌ **缺少缓存层**（每一次相同查询都极其昂贵且缓慢）
* ❌ **缺少评测机制**或质量反馈闭环
* ❌ **缺少故障自愈**或重试重试机制
* ❌ **缺少混合检索**策略（如密集+稀疏检索融合 RFF）
* ❌ **缺少组件间的状态控制**或编排

**本项目专为暴露并解决这些工程痛点而设计。**

---

## 🧱 本系统究竟包含什么

一个高度模块化的 RAG 执行架构，包含真实的生产级组件：
* 🎯 **查询路由引擎 (Query Routing Engine)** (计算器 / 网页 / 向量 / 图谱)
* ⚡ **语义缓存层 (Semantic Cache)** (命中缓存时，绕过检索与大模型极速响应)
* 🧠 **知识图谱层 (GraphRAG)** (基于实体关系的多跳知识推理)
* 🔍 **混合检索系统 (Hybrid Retrieval)** (BM25 + 密集向量 + RRF 重排)
* 🧪 **量化评测引擎 (Evaluation Engine)** (大模型作为裁判评判生成质量与忠实度)
* 🛠️ **执行控制器 (Execution Controller)** (超时控制、降级兜底、重试机制)
* 📦 **确定性管道设计 (Stateful Pipeline)** (基于状态流转的异步任务体系)

---

## 🧩 本项目的独特之处

我们不只是做了一个简单的“聊天机器人 Demo”，我们关注的是：
> 🧠 真实的 AI 系统在面对复杂性、故障以及规模化时是如何运行的。

它的定位是：
* 一个 **系统化课程** (36 模块带你从 0 到 200)
* 一个 **参考系统架构 (Reference Architecture)**
* 一个 **RAG 生产环境模拟沙盒 (Production Simulation Environment)**

---

## ⚡ 极速演示

```
[查询]  "Llama 3 遵循什么开源协议？"

[路由] ➔ 选中向量检索与网页搜索工具
[缓存] ➔ 未命中 (MISS) ❌
[检索] ➔ 混合检索 + RRF 重排
[生成] ➔ 大模型回答生成
[评测] ➔ 自动计算 Faithfulness (忠实度) 分数
```

然后：

```
重复相同查询

[缓存] ➔ 命中 (HIT) ✅
[生成] ➔ 绕过检索与大模型
延迟   ➔ ~0.0001s
```

---

## 🎯 你将从中获得什么

* 明白为什么初级 RAG 系统在生产中会失效
* 理解路由如何显著提升系统稳定性
* 掌握为什么缓存对控制 API 成本至关重要
* 学习混合检索如何有效解决模型幻觉
* 学习评测如何防止系统悄无声息地产生低劣回答
* 掌握真实的 AI 系统应该如何架构

---

## 🚀 目标读者

* 正在开发 RAG 应用的开发者
* 正在将 AI Demo 推进到生产环境的工程师
* 希望从系统级理解 AI 运作的自学者
* 任何构建智能体或使用外部工具系统的开发者

---

## ⭐ 如果本项目帮助你理解了真实 RAG 系统
欢迎点个 Star 收藏 —— 它是你搭建生产级 AI 系统最扎实的参考架构。

---

## 🧭 系统架构图谱

```mermaid
flowchart LR
    Query([用户提问]) --> Pre[1. 意图改写与预处理]
    Pre --> Cache{2. 语义缓存拦截?}
    
    Cache -->|命中| CacheHit[毫秒级缓存响应 0.00s]
    Cache -->|未命中| RAG[3. 向量检索与重排]
    
    RAG --> Controller[4. 请求执行控制面]
    Controller --> LLM[5. 混合大模型路由]
    
    CacheHit --> Output([输出回答])
    LLM --> Output

    classDef default fill:#111827,stroke:#374151,stroke-width:1px,color:#f9fafb;
    classDef highlight fill:#10b981,stroke:#047857,stroke-width:2px,color:#fff;
    classDef title fill:#1f2937,stroke:#4b5563,stroke-width:1px,color:#f3f4f6;

    class CacheHit highlight;
```

---

## 🚀 快速开始 (运行路径选择器)

选择你最想体验 `AI Model Atlas` 的路径，在 60 秒内上手：

### 路径 A：本地沙盒交互式 UI (推荐)
在本地运行 Streamlit 可观测性面板，实时体验语义缓存、检索重排序与自愈控制：
1. **克隆仓库并进入项目目录：**
   ```bash
   git clone https://github.com/Hao610/AI-Model-Atlas.git
   cd AI-Model-Atlas/projects/rag-app
   ```
2. **安装核心依赖：**
   ```bash
   pip install -r requirements.txt
   ```
3. **启动应用面板：**
   ```bash
   python app.py
   ```
   *提示：如果需要本地离线大模型支持，请确保 Ollama 服务已在后台运行。*

### 路径 B：直接启动 Streamlit 应用
进入可运行示例项目，并从终端启动交互式应用面板：
```bash
cd projects/rag-app
streamlit run app.py
```

### 路径 C：概念与学习路线图
如果你当前无法运行代码，可以从手把手教程入口开始阅读：
👉 **[00_learning_map_zh.md](docs/phase1_0_to_1/00_learning_map_zh.md)**

> **ℹ️ 关于 Colab 在线体验**：Colab 仅作为可选的备用运行环境。如需更稳定的体验，建议使用本地沙盒（路径 A）。Colab 的可用性取决于 Google 免费后端算力资源池，高峰期可能出现分配失败。

---

### 🧩 运行后我能看到什么？

以下是系统在"缓存未命中"与"缓存命中"状态下的典型终端/看板输出日志：

```text
[🔄 查询改写] 意图归一化: "帮我查一下 Llama 3 开源协议" -> "llama 3 license parameters"
[⚡ 语义缓存] 未命中! ❌ 正在路由至向量库检索与大模型调用。
[🎯 相关重排] 成功通过相似度阈值过滤 (余弦距离评分: 0.89)。
[回复内容]   "Llama 3 遵循 LLAMA 3 社区许可协议..." (响应时延: 1.25秒)

--- 再次输入相同提问: "帮我查一下 Llama 3 开源协议" ---
[🔄 查询改写] 意图归一化: "帮我查一下 Llama 3 开源协议" -> "llama 3 license parameters"
[⚡ 语义缓存] 命中! ✅ 成功拦截，直接绕过向量检索与大模型推理。
[回复内容]   "Llama 3 遵循 LLAMA 3 社区许可协议..." (响应时延: 0.0001秒)
```

---

## 💡 为什么发起本项目？

市面上的 RAG 教程大多停留在 Embeddings 或简单检索演示。`AI Model Atlas` 更进一步，提供面向生产落地的工业级认知 RAG 系统参考架构。通过整合语义缓存、查询改写、检索重排与执行控制器，打通从 Demo 到生产级系统之间的最后一步。

---

## 🚀 本项目提供什么 (Key Features)

- **🚦 检索编排与路由层 (Retrieval Orchestration Layer)**：基于确定性正则的意图路由器，支持计算器、联网搜索、混合向量检索等独立处理分支。
- **📊 轻量级量化评测体系 (Lightweight Evaluation Framework)**：纯原生手工实现的 LLM-as-a-judge 裁判引擎，支持路由准确率、忠实度与扎实度等硬核评估。
- **👁️ 结构化解析引擎 (Structural Parsing)**：完全透明可控地精准提取 PDF 表格边界，输出原生 Markdown，并过滤掉无用图片与图表 (`pdfplumber` + `PyMuPDF`)。
- **📦 原子化表格切片 (Table-Aware Chunking)**：抛弃传统的暴力文本切片机制，确保全量 Markdown 表格被完整灌入向量库，避免数据被截断导致幻觉。
- **🕸️ 图检索增强引擎 (GraphRAG Knowledge Network)**：基于 NetworkX 构建两阶段关系抽取逻辑的轻量级原生知识图谱引擎，并通过 1-Hop 关系检索作为补充上下文。
- **🧠 认知查询改写 (Cognitive Query Rewriting)**：内置智能正则和提示词过滤器，去除口语噪音，精准提取检索意图。
- **🎯 检索相关性重排 (Relevance Reranking)**：支持 RRF 倒数秩融合稠密与稀疏结果，并结合余弦阈值过滤无效噪声片段。
- **🛡️ 强大的请求控制面 (Execution Controller)**：统一接管请求生命周期，支持指数级退避重试、连接超时控制。
- **🌐 混合大模型推理后端 (Hybrid LLM Core)**：支持在本地 Ollama (Llama 3/DeepSeek) 与商业云端 API (如 OpenAI) 之间进行自动热切换。
- **⚡ 语义缓存加速 (Semantic Cache)**：通过向量相似度匹配与长度比例控制拦截重复请求，实现毫秒级响应。

---

## 🎯 本项目适合谁？

* 🧭 **零基础小白** → 通过通俗比喻和无数学公式的解构，轻松跨越 AI 概念门槛。
* 💻 **应用层开发者** → 掌握 API 接入、本地大模型运行以及快速 Web 界面开发。
* 🏗️ **AI 系统架构师** → 学习工业级 RAG 架构设计、多 Agent 协同流编排及向量数据库检索优化。
* 🚀 **硬核研究与极客** → 深入模型微调（LoRA）、量化压缩原理、算力选型及云端 GPU 高并发部署。

---

## 🧭 选择你的目标

| 你的目标 | 前往 |
| :--- | :--- |
| 🚀 **立刻运行系统** | ↑ [快速开始](#-快速开始-运行路径选择器) |
| 🧠 **理解系统架构** | 📐 [ARCHITECTURE_zh.md](docs/ARCHITECTURE_zh.md) — 性能指标、容灾自愈、状态机 |
| 📚 **从零学习 AI** | 📚 [CURRICULUM_zh.md](docs/CURRICULUM_zh.md) — 36 模块 "从 0 到 200" 学习路线图 |
| 🧬 **深潜算法原理** | 🧬 [DEEP_DIVES_zh.md](docs/DEEP_DIVES_zh.md) — 17 篇 AI 底层算法与大模型技术纪录片 |

---

## 💡 本仓库设计原则

1. **文字第一，免于维护**：我们坚决不用界面截图。因为 AI 平台和工具的 UI 变化极快，截图极易失效。我们通过手绘 Markdown 图表、表格对比和文字解构来传达永不过时的原理。
2. **拒绝生硬机翻，真双语并行**：英文版 and 中文版均是由算法开发人员人工编写与校验，用词贴近中西方开发者日常习惯，杜绝死板晦涩的机器直译。
3. **闭环式实操**：不搞纯空洞理论。每一阶段的最后，读者都能得到完整的"配置清单"或"一键启动代码"，确保知识能够真正落地。

---

## 🌍 创造了有价值的工具？

如果本项目帮助你学习、构建或部署了认知级 RAG 系统，我们诚挚地邀请你加入我们的共建社区：

* **点亮 Star & Fork** ⭐：点亮 Star 以示支持，并 Fork 项目以便快速检索。
* **分享学习旅程** 📢：将本图谱或你自己的 RAG 实战成果分享给更多开发者。
* **参与共建** 🤝：提交 Pull Request、反馈 Bug 或提出新模块建议。详情请参阅我们的[贡献指南](.github/CONTRIBUTING_zh.md)。
* **社区规范** 🧭：参与前请先阅读我们的[行为准则](.github/CODE_OF_CONDUCT_zh.md)与[安全政策](.github/SECURITY_zh.md)。

🚀 **一键分享：**

> 我使用 Python 搭建了一个具备语义缓存、查询改写、重排与故障自愈的工业级认知 RAG系统！推荐正在学习和构建 AI 应用的开发者看看 AI Model Atlas。
> 👉 https://github.com/Hao610/AI-Model-Atlas

---

## 📄 开源协议 (License)

AI Model Atlas 采用双协议模式（Dual-License Model）：

- **文档、课程体系、图示与教学内容**：Creative Commons Attribution 4.0 International (详见 [`/LICENSE`](LICENSE))
- **源代码与可运行示例项目**：MIT License (详见 [`/LICENSE-CODE`](LICENSE-CODE))

> 本项目将软件代码许可与内容创作许可进行了严格分离，以确保清晰度与商业复用的安全性。本项目将持续更新，所有新增内容均默认遵循上述双协议模式，除非另有特别说明。

Copyright (c) 2026 Loi Chiang Hao.
