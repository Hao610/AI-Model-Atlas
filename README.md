# AI-Model-Atlas 🗺️

> **Mapping the world of Artificial Intelligence, one model at a time.**

[English] | [中文 (README_zh.md)](README_zh.md)

Welcome to the **AI-Model-Atlas**! This repository is a comprehensive, beginner-friendly "dictionary-style" guide designed to take anyone from zero technical background to understanding, calling, running, and even fine-tuning modern Artificial Intelligence models.

Whether you are a curious bystander, a software developer looking to integrate LLMs, or an aspiring AI practitioner, this atlas provides a clear roadmap with zero mathematical gatekeeping.

---

## 🗺️ The "0 to 100" Roadmap

Below is the structured learning path. Each phase is designed to build on the previous one.

```text
  0 ────────────────► 1 ────────────────► 10 ───────────────► 50 ──────────────► 100
[Phase 1: Learn]   [Phase 2: Build]   [Phase 3: Integrate]  [Phase 4: Train & Deploy]
  Concepts &        Low-code RAG &     APIs & Local LLMs    Fine-Tuning, Quantization
  Prompt Art        Agent Workflows    & User Interfaces    & GPU Clusters
```

| Phase | Module | Description | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 1: 0 to 1**<br>*(Learn & Awaken)* | 1. What is AI? | AI, Machine Learning, and Deep Learning explained via analogies. | [what_is_ai.md](docs/phase1_0_to_1/what_is_ai.md) | [what_is_ai_zh.md](docs/phase1_0_to_1/what_is_ai_zh.md) |
| | 2. Prompt Art | Structured frameworks (ROLE, Few-Shot) for talking to AI. | [prompt_art.md](docs/phase1_0_to_1/prompt_art.md) | [prompt_art_zh.md](docs/phase1_0_to_1/prompt_art_zh.md) |
| | 3. Open Source Licenses | MIT, Apache 2.0, and commercial limits of models (e.g. Llama 3). | [licenses.md](docs/phase1_0_to_1/licenses.md) | [licenses_zh.md](docs/phase1_0_to_1/licenses_zh.md) |
| | 4. AI Tools Guide | Web-based daily productivity tools (ChatGPT, Claude, Midjourney). | [ai_tools.md](docs/phase1_0_to_1/ai_tools.md) | [ai_tools_zh.md](docs/phase1_0_to_1/ai_tools_zh.md) |
| | 5. Model Zoo Overview | Quick table comparing GPT, Claude, Gemini, Llama, DeepSeek, Qwen. | [model_zoo.md](docs/phase1_0_to_1/model_zoo.md) | [model_zoo_zh.md](docs/phase1_0_to_1/model_zoo_zh.md) |
| | 6. Hugging Face Guide | Understanding the Hub: repository layout, safetensors, and hub API. | [huggingface_guide.md](docs/phase1_0_to_1/huggingface_guide.md) | [huggingface_guide_zh.md](docs/phase1_0_to_1/huggingface_guide_zh.md) |
| | 7. Glossary | Essential vocab sheet (Tokens, Temperature, Context Window). | [glossary.md](docs/phase1_0_to_1/glossary.md) | [glossary_zh.md](docs/phase1_0_to_1/glossary_zh.md) |
| **Phase 2: 1 to 10**<br>*(Build & Architect)* | 8. LLM Landscape | The lineage and capabilities of modern closed & open weights models. | [llm_landscape.md](docs/phase2_1_to_10/llm_landscape.md) | [llm_landscape_zh.md](docs/phase2_1_to_10/llm_landscape_zh.md) |
| | 9. No-Code Agents | Creating autonomous assistants using Dify and Coze. | [no_code_agents.md](docs/phase2_1_to_10/no_code_agents.md) | [no_code_agents_zh.md](docs/phase2_1_to_10/no_code_agents_zh.md) |
| | 10. Multimodal AI | Images (Flux, SD), voice (Whisper, TTS), and video generation. | [multimodal_models.md](docs/phase2_1_to_10/multimodal_models.md) | [multimodal_models_zh.md](docs/phase2_1_to_10/multimodal_models_zh.md) |
| | 11. RAG Introduction | Retrieval-Augmented Generation: Giving AI a custom PDF library. | [rag_intro.md](docs/phase2_1_to_10/rag_intro.md) | [rag_intro_zh.md](docs/phase2_1_to_10/rag_intro_zh.md) |
| | 12. Vector Databases | Understanding Chroma, Milvus, FAISS, and PGVector. | [vector_db.md](docs/phase2_1_to_10/vector_db.md) | [vector_db_zh.md](docs/phase2_1_to_10/vector_db_zh.md) |
| | 13. AI Workflows | Visualizing User -> Agent -> RAG -> LLM architectures. | [ai_workflows.md](docs/phase2_1_to_10/ai_workflows.md) | [ai_workflows_zh.md](docs/phase2_1_to_10/ai_workflows_zh.md) |
| | 14. Real-World Use Cases | Core templates for CS Bots, Knowledge Bases, and AI Translators. | [use_cases.md](docs/phase2_1_to_10/use_cases.md) | [use_cases_zh.md](docs/phase2_1_to_10/use_cases_zh.md) |
| **Phase 3: 10 to 50**<br>*(Integrate & Code)* | 15. API Integration | Requesting model keys and calling models via simple Python scripts. | [api_guide.md](docs/phase3_10_to_50/api_guide.md) | [api_guide_zh.md](docs/phase3_10_to_50/api_guide_zh.md) |
| | 16. Cost & Tokenomics | Calculating API expenses and GPU hosting cost metrics. | [cost_and_tokens.md](docs/phase3_10_to_50/cost_and_tokens.md) | [cost_and_tokens_zh.md](docs/phase3_10_to_50/cost_and_tokens_zh.md) |
| | 17. Local LLM Runner | Deploying models locally using Ollama and LM Studio. | [local_llm.md](docs/phase3_10_to_50/local_llm.md) | [local_llm_zh.md](docs/phase3_10_to_50/local_llm_zh.md) |
| | 18. UI Interfaces | Building clean web interfaces with Streamlit & Gradio. | [ui_interfaces.md](docs/phase3_10_to_50/ui_interfaces.md) | [ui_interfaces_zh.md](docs/phase3_10_to_50/ui_interfaces_zh.md) |
| | 19. Agent Frameworks | Comparing CrewAI, AutoGen, LangChain, and LangGraph. | [agent_frameworks.md](docs/phase3_10_to_50/agent_frameworks.md) | [agent_frameworks_zh.md](docs/phase3_10_to_50/agent_frameworks_zh.md) |
| | 20. Embeddings Deep Dive | Transforming text into vectors and measuring cosine similarity. | [embeddings.md](docs/phase3_10_to_50/embeddings.md) | [embeddings_zh.md](docs/phase3_10_to_50/embeddings_zh.md) |
| | 21. Model Evaluation | Methods: BLEU, Human Eval, Chatbot Arena, and LLM-as-a-Judge. | [evaluation.md](docs/phase3_10_to_50/evaluation.md) | [evaluation_zh.md](docs/phase3_10_to_50/evaluation_zh.md) |
| **Phase 4: 50 to 100**<br>*(Train & Deploy)* | 22. Data Preparation | Formatting JSON/JSONL datasets and synthetic data generation. | [data_preparation.md](docs/phase4_50_to_100/data_preparation.md) | [data_preparation_zh.md](docs/phase4_50_to_100/data_preparation_zh.md) |
| | 23. Why Fine-Tune? | When prompt engineering fails and model customization is needed. | [finetuning.md](docs/phase4_50_to_100/finetuning.md) | [finetuning_zh.md](docs/phase4_50_to_100/finetuning_zh.md) |
| | 24. LoRA Explained | Under the hood of Low-Rank Adaptation (the math-free version). | [lora_explained.md](docs/phase4_50_to_100/lora_explained.md) | [lora_explained_zh.md](docs/phase4_50_to_100/lora_explained_zh.md) |
| | 25. LLaMA-Factory Guide | Click-and-train GUI for fine-tuning without writing custom code. | [llama_factory.md](docs/phase4_50_to_100/llama_factory.md) | [llama_factory_zh.md](docs/phase4_50_to_100/llama_factory_zh.md) |
| | 26. Model Quantization | GGUF vs FP16, compressing 70B models down to consumer GPUs. | [quantization.md](docs/phase4_50_to_100/quantization.md) | [quantization_zh.md](docs/phase4_50_to_100/quantization_zh.md) |
| | 27. GPU Selection Guide | Finding the right hardware (RTX 4090 vs cloud GPU clusters). | [gpu_selection.md](docs/phase4_50_to_100/gpu_selection.md) | [gpu_selection_zh.md](docs/phase4_50_to_100/gpu_selection_zh.md) |
| | 28. Safety & Alignment | RLHF, DPO, Guardrails, and understanding model boundaries. | [safety_alignment.md](docs/phase4_50_to_100/safety_alignment.md) | [safety_alignment_zh.md](docs/phase4_50_to_100/safety_alignment_zh.md) |
| | 29. Cloud Deployment | Renting compute on AutoDL/RunPod and serving models to users. | [deployment.md](docs/phase4_50_to_100/deployment.md) | [deployment_zh.md](docs/phase4_50_to_100/deployment_zh.md) |

---

## 💡 Repository Design Philosophy

1. **Text-First & Zero-Bloat**: No heavy image files that get outdated when software UI changes. We use elegant Markdown layout, detailed tables, flow charts, and structured lists.
2. **Double Portal, Localized Content**: The English and Chinese versions of the documents are written by hand (no raw robotic translations) ensuring idiomatic, easy-to-understand explanations for developers in both regions.
3. **From Scratch to Cloud**: The guide doesn't stop at "Prompting". It goes all the way to cloud GPU fine-tuning, explaining the full engineering lifecycle of model operation.

---

## 🔗 Contributing & Usage

Feel free to bookmark this atlas or clone it to use as your personal reference notes ("Knowledge External Brain"). If you find it helpful, please star the repository!

---

## 📄 License

AI-Model-Atlas is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). For details, please refer to [LICENSE](LICENSE).

You are free to share, adapt, and use the contents commercially, provided that appropriate attribution is given.

Copyright (c) 2026 AI-Model-Atlas

Created and maintained by Loi Chiang Hao.
