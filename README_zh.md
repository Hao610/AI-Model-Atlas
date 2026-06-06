# 🗺️ AI Model Atlas | AI 模型图谱

## 聚焦教学的 RAG 系统架构演练沙盒

AI Model Atlas 是一个**专注于系统设计与教学的模拟演练系统**，旨在帮助学习者理解生产级 RAG 系统是如何设计的，以及为什么绝大多数“教程级”的简单实现方案在真实生产环境中都会崩溃。

本项目**并非生产框架或部署系统**。它是一个针对真实 RAG 架构设计模式的概念性教学模拟沙盒。

[[English] (README.md)](README.md) | [中文]

👉 **第一次来到本项目？推荐从我们的 [🧭 快速入门指南](docs/GETTING_STARTED_zh.md) 开始，选择最适合您的学习路径！**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg?style=for-the-badge)](LICENSE)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE-CODE)
[![本地沙盒 UI](https://img.shields.io/badge/▶_本地沙盒应用-10b981?style=for-the-badge&logo=play)](#%E8%B7%AF%E5%BE%84-a%E6%9C%AC%E5%9C%B0%E6%B2%99%E7%9B%92%E4%BA%A4%E4%BA%92%E5%BC%8F-ui-%E6%8E%A8%E8%8D%90)
[![Colab 在线体验](https://img.shields.io/badge/▶_Colab_在线玩转_(可选)-orange?style=for-the-badge&logo=googlecolab)](https://colab.research.google.com/github/Hao610/AI-Model-Atlas/blob/main/projects/rag-app/quickstart.ipynb)

---

## 📌 本项目是什么

AI Model Atlas 深入剖析了现代 RAG 系统在面对真实世界复杂业务场景时的运转逻辑。

它将帮助你理解：
* 真实的 RAG 系统在生产中是如何进行架构设计的
* 为什么迈出第一步的“向量检索 ➔ 大模型”管道会轻易失效
* 路由、缓存和工作流编排在什么阶段是必需的
* 系统从原型 Demo 演进到真实业务规模时，系统设计会有哪些改变

---

## ⚠️ 绝大多数 RAG 教程存在的问题

大多数 RAG 教程的运行逻辑都非常简单：
> 用户 ➔ 向量检索 ➔ 大模型

这种设计很简单，但并不完整。在真实业务系统中，这种简易设计会崩溃，因为：
* 工具之间缺乏路由（一切查询都粗暴地塞给向量检索）
* 缺少缓存层（每一次查询都会去调用大模型，成本高昂）
* 没有任何质量评测与反馈闭环
* 缺少任何故障自愈与重试逻辑
* 没有混合检索策略（BM25 + 密集向量 + RRF 融合）
* 系统层缺乏组件间的状态控制或工作流编排

👉 本项目存在的目标，就是为了让这些隐蔽的系统架构设计层变得清晰可见。

---

## 🧱 系统设计（概念性）

本系统不是一个简单的聊天机器人，而是一个 RAG 架构的解耦呈现：
* 🧠 查询智能路由 (工具选择逻辑)
* 🔍 混合检索 (BM25 + 密集向量 + RRF 融合重排)
* ⚡ 语义缓存 (快速执行通道模拟)
* 🛡️ 量化评测概念 (LLM-as-a-judge 裁判引擎)
* 🔁 执行控制器 (重试 / 降级兜底 / 超时控制逻辑)

---

## 🧩 本项目的独特之处

我们不只是做了一个简单的聊天机器人 Demo，我们关注的是：
> 🧠 **理解真实的 AI 系统在面对故障、规模化以及系统复杂性时是如何运行的。**

它的定位是：
* 一个系统化课程 (36 模块)
* 一个 RAG 系统架构设计模式的参考指南
* 一个 RAG 生产级系统概念的模拟沙盒

---

## ⚡ 系统行为演示 (模拟概念流)

用户: "Llama 3 遵循什么开源协议？"
➔ **路由分发** (选中向量检索与网页搜索工具)
➔ **检索执行** (混合检索搜索)
➔ **未命中缓存** ➔ 大模型回答生成
➔ **触发自动评测步骤**

重复相同查询:
➔ **检测到缓存命中**
➔ 绕过检索与大模型调用
➔ **毫秒级极速响应模拟** (~0.0001s)

---

## 🎯 你将从中获得什么

* 明白为什么初级 RAG 系统在生产中会失效
* 理解为什么除了向量检索之外，路由分发也是必需的
* 掌握为什么缓存对控制 API 成本和延迟至关重要
* 学习混合检索如何有效提升检索的精准度
* 明白为什么在真实系统中必须配置自动化评测层
* 概念性地掌握真实的 AI 系统从头到尾应该如何架构

---

## 🚀 目标读者

* 正在学习 RAG 系统设计的开发者
* 正在从写 Demo 转向构建系统性架构思维的工程师
* 希望从系统级理解 AI 运作的自学者
* 任何构建智能体或使用外部工具系统的开发者

---

## ⭐ 注意

本仓库仅用于**教学和系统设计概念探索**，并非用于生产部署。

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
