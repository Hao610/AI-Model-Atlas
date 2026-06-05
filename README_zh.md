# AI-Model-Atlas 🗺️ | AI 模型图谱

> **用一张通俗的地图，带你一省一城地丈量人工智能的世界。**

[[English] (README.md)](README.md) | [中文]

欢迎来到 **AI-Model-Atlas** (AI 模型图谱)！本项目是一个系统化、面向初学者的“字典式”科普仓库。我们的目标是：**帮助没有任何 IT、代码或算法背景的零基础小白，一路打通关，直到能够调用、本地运行、量化并微调大模型。**

无论你是对 AI 感兴趣的职场人、想要转型集成大模型的程序员，还是想要深入模型底层的算法爱好者，本图谱都会用最接地气、最少数学公式的方式为你拨云见日。

---

## 🗺️ “从 0 到 100” 学习路线图

以下是为你精心设计的进阶路径，每一阶段都为下一阶段打下坚实的基础。

```text
  0 ────────────────► 1 ────────────────► 10 ───────────────► 50 ──────────────► 100
【阶段一：认知觉醒】 【阶段二：低代码构建】  【阶段三：开发者接入】 【阶段四：硬核微调部署】
  AI 核心概念与       工作流与智能体        API 调用与本地运行    量化、LoRA 微调
  提示词艺术          (Dify / RAG)          Streamlit 界面开发   云端 GPU 算力实操
```

| 阶段 | 模块 | 核心内容简介 | 英文版指南 | 中文版指南 |
| :--- | :--- | :--- | :--- | :--- |
| **阶段一：从 0 到 1**<br>*(认知与觉醒)* | 1. 什么是 AI？ | 用大白话和生活实例解释什么是机器学习、深度学习和大模型。 | [what_is_ai.md](docs/phase1_0_to_1/what_is_ai.md) | [what_is_ai_zh.md](docs/phase1_0_to_1/what_is_ai_zh.md) |
| | 2. 提示词艺术 | 掌握 ROLE 框架、Few-Shot 样本等高效与大模型对话的公式。 | [prompt_art.md](docs/phase1_0_to_1/prompt_art.md) | [prompt_art_zh.md](docs/phase1_0_to_1/prompt_art_zh.md) |
| | 3. 开源协议指南 | MIT、Apache 2.0 到底是什么？为什么有些模型不能拿来商用？ | [licenses.md](docs/phase1_0_to_1/licenses.md) | [licenses_zh.md](docs/phase1_0_to_1/licenses_zh.md) |
| | 4. 常用 AI 工具 | 开箱即用的办公与创意工具全景图 (ChatGPT, Claude, Midjourney)。 | [ai_tools.md](docs/phase1_0_to_1/ai_tools.md) | [ai_tools_zh.md](docs/phase1_0_to_1/ai_tools_zh.md) |
| | 5. 模型动物园 | 一张表看懂 GPT, Claude, Gemini, Llama, DeepSeek, Qwen。 | [model_zoo.md](docs/phase1_0_to_1/model_zoo.md) | [model_zoo_zh.md](docs/phase1_0_to_1/model_zoo_zh.md) |
| | 6. Hugging Face 极简指南 | 玩转 AI 军火库：文件后缀解密、Python 自动下载模型。 | [huggingface_guide.md](docs/phase1_0_to_1/huggingface_guide.md) | [huggingface_guide_zh.md](docs/phase1_0_to_1/huggingface_guide_zh.md) |
| | 7. 核心词汇表 | 新手查字典：Token、Temperature、Context Window 分别代表什么。 | [glossary.md](docs/phase1_0_to_1/glossary.md) | [glossary_zh.md](docs/phase1_0_to_1/glossary_zh.md) |
| **阶段二：从 1 到 10**<br>*(低代码搭建)* | 8. 大模型全景图谱 | 探索现代闭源模型与开源权重的技术脉络与分化。 | [llm_landscape.md](docs/phase2_1_to_10/llm_landscape.md) | [llm_landscape_zh.md](docs/phase2_1_to_10/llm_landscape_zh.md) |
| | 9. 无代码 Agent 搭建 | 如何使用 Coze (扣子) 和 Dify 一步步配置属于你自己的智能体。 | [no_code_agents.md](docs/phase2_1_to_10/no_code_agents.md) | [no_code_agents_zh.md](docs/phase2_1_to_10/no_code_agents_zh.md) |
| | 10. 多模态 AI | 文字之外的世界：Stable Diffusion生图、语音Whisper、Sora视频。 | [multimodal_models.md](docs/phase2_1_to_10/multimodal_models.md) | [multimodal_models_zh.md](docs/phase2_1_to_10/multimodal_models_zh.md) |
| | 11. RAG 知识库检索 | 什么是检索增强生成？如何让 AI 在几秒内阅读完并学习本地 PDF。 | [rag_intro.md](docs/phase2_1_to_10/rag_intro.md) | [rag_intro_zh.md](docs/phase2_1_to_10/rag_intro_zh.md) |
| | 12. 向量数据库入门 | 了解 Chroma、Milvus、FAISS 和 PGVector 的定位与选择。 | [vector_db.md](docs/phase2_1_to_10/vector_db.md) | [vector_db_zh.md](docs/phase2_1_to_10/vector_db_zh.md) |
| | 13. AI 工作流架构 | 解析 用户 -> 智能体 -> RAG -> 大模型 的完整工作数据流向。 | [ai_workflows.md](docs/phase2_1_to_10/ai_workflows.md) | [ai_workflows_zh.md](docs/phase2_1_to_10/ai_workflows_zh.md) |
| | 14. 真实应用案例 | 客服机器人、企业知识库、AI翻译等实战场景配置指南。 | [use_cases.md](docs/phase2_1_to_10/use_cases.md) | [use_cases_zh.md](docs/phase2_1_to_10/use_cases_zh.md) |
| **阶段三：从 10 到 50**<br>*(开发者之路)* | 15. API 接入秘籍 | 申请 API 密钥 (Key)，并用几行最简的 Python 代码调用大模型。 | [api_guide.md](docs/phase3_10_to_50/api_guide.md) | [api_guide_zh.md](docs/phase3_10_to_50/api_guide_zh.md) |
| | 16. 计费与 Token 经济学 | Token计费原理、各大模型价格PK、GPU租用与API成本比对。 | [cost_and_tokens.md](docs/phase3_10_to_50/cost_and_tokens.md) | [cost_and_tokens_zh.md](docs/phase3_10_to_50/cost_and_tokens_zh.md) |
| | 17. 本地大模型运行 | 使用 Ollama 和 LM Studio 在普通笔记本上本地跑起百亿模型。 | [local_llm.md](docs/phase3_10_to_50/local_llm.md) | [local_llm_zh.md](docs/phase3_10_to_50/local_llm_zh.md) |
| | 18. 前端界面极速生成 | 使用 Streamlit 和 Gradio 一键为你的 AI 脚本套上好看的聊天网页。 | [ui_interfaces.md](docs/phase3_10_to_50/ui_interfaces.md) | [ui_interfaces_zh.md](docs/phase3_10_to_50/ui_interfaces_zh.md) |
| | 19. 智能体开发框架 | 对比 CrewAI、AutoGen、LangChain、LangGraph，教你如何选择。 | [agent_frameworks.md](docs/phase3_10_to_50/agent_frameworks.md) | [agent_frameworks_zh.md](docs/phase3_10_to_50/agent_frameworks_zh.md) |
| | 20. 向量表示与匹配 | 文本如何变成浮点数数组？解释余弦相似度匹配的物理意义。 | [embeddings.md](docs/phase3_10_to_50/embeddings.md) | [embeddings_zh.md](docs/phase3_10_to_50/embeddings_zh.md) |
| | 21. Model Evaluation | 如何判定大模型好坏？详解 BLEU、Human Eval 与大模型裁判。 | [evaluation.md](docs/phase3_10_to_50/evaluation.md) | [evaluation_zh.md](docs/phase3_10_to_50/evaluation_zh.md) |
| **阶段四：从 50 到 100**<br>*(硬核与超越)* | 22. 数据准备与清洗 | JSON/JSONL格式规范、去重Checklist、大模型生成合成数据。 | [data_preparation.md](docs/phase4_50_to_100/data_preparation.md) | [data_preparation_zh.md](docs/phase4_50_to_100/data_preparation_zh.md) |
| | 23. 为什么要微调？ | 为什么提示词不能解决所有问题？什么时候该训练专属模型。 | [finetuning.md](docs/phase4_50_to_100/finetuning.md) | [finetuning_zh.md](docs/phase4_50_to_100/finetuning_zh.md) |
| | 24. LoRA 极简原理解释 | 用修图软件中的“滤镜图层”通俗解释低秩适应（LoRA）原理。 | [lora_explained.md](docs/phase4_50_to_100/lora_explained.md) | [lora_explained_zh.md](docs/phase4_50_to_100/lora_explained_zh.md) |
| | 25. LLaMA-Factory 训练 | 图形化微调利器：无需手写 PyTorch 训练循环，一键点选训练。 | [llama_factory.md](docs/phase4_50_to_100/llama_factory.md) | [llama_factory_zh.md](docs/phase4_50_to_100/llama_factory_zh.md) |
| | 26. 模型量化压缩 | 什么是 GGUF/INT4？为什么量化能让 70B 模型挤进民用显卡。 | [quantization.md](docs/phase4_50_to_100/quantization.md) | [quantization_zh.md](docs/phase4_50_to_100/quantization_zh.md) |
| | 27. 显卡选型备忘录 | RTX 4090/5090 能跑什么？A100、H100 究竟贵在哪里？ | [gpu_selection.md](docs/phase4_50_to_100/gpu_selection.md) | [gpu_selection_zh.md](docs/phase4_50_to_100/gpu_selection_zh.md) |
| | 28. 对齐与安全围栏 | 解释 RLHF、DPO 以及为什么大模型会拒绝回答你的敏感问题。 | [safety_alignment.md](docs/phase4_50_to_100/safety_alignment.md) | [safety_alignment_zh.md](docs/phase4_50_to_100/safety_alignment_zh.md) |
| | 29. 云端 GPU 算力部署 | 租用 AutoDL / RunPod 显卡，并完成开源模型的私有化服务上线。 | [deployment.md](docs/phase4_50_to_100/deployment.md) | [deployment_zh.md](docs/phase4_50_to_100/deployment_zh.md) |

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
