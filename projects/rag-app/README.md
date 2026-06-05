# 🧠 Cognitive RAG System with Execution Control & Semantic Cache

> **A production-grade, hybrid RAG reference architecture designed for extreme reliability, cognitive intelligence, and semantic acceleration.**

[English] | [中文 (README_zh.md)](README_zh.md)

This project showcases a complete **Cognitive RAG System** demonstrating how to transition an AI application from a simple proof-of-concept into a resilient, production-ready system. It features a dual-inference backend allowing seamless runtime switching between local models (Ollama) and cloud APIs (OpenAI/DeepSeek).

---

## 🗺️ System Data Flow & Architecture

```mermaid
flowchart TD
    UserQuery[User Question] --> QueryRewriter[Query Rewriter]
    QueryRewriter --> SemanticCacheCheck{Semantic Cache Hit?}
    
    SemanticCacheCheck -->|Yes| InstantReturn[Return Cached Response]
    SemanticCacheCheck -->|No| VectorSearch[ChromaDB Vector Retrieval]
    
    VectorSearch --> Reranker[Relevance Reranker]
    Reranker --> ExecutionController[Execution Controller]
    
    ExecutionController -->|Retry / Fallback| LLMRouter[LLM Router Engine]
    LLMRouter -->|local| Ollama[Ollama Local LLM]
    LLMRouter -->|cloud| CloudAPI[DeepSeek / OpenAI API]
    
    Ollama --> StreamOutput[Stream to UI & Cache Store]
    CloudAPI --> StreamOutput
```

---

## ⚡ Key Highlights

* **🧠 Cognitive Query Rewriting**: Standardizes and optimizes conversational queries by removing grammatical noise and syntax prefixes before vector search, improving retrieval accuracy.
* **🛡️ Execution Control Plane**: Orchestrates all request lifetimes. Handles exponential backoff retries, connection timeouts, and automatic graceful degradation (seamlessly falling back from local Ollama to cloud API if local nodes go offline).
* **⚡ Semantic Cache Layer**: Prevents redundant model execution. Repeated or semantically matching queries are bypassed and returned instantly with cosine similarity checks and length ratio boundaries.
* **🔍 Deep Observability Dashboard**: Streamlit interface containing dynamic threshold parameters, pre-vs-post rerank document context diagnostics, and live system latency metrics (TTFT, throughput tokens/sec).

---

## 📂 System Packages Directory

```text
rag-app/
├── app.py                # Subprocess runner launcher
├── requirements.txt      # Module dependencies (Streamlit, ChromaDB, pypdf)
├── START_HERE.md         # 1-minute quickstart guide
│
├── config/
│   └── settings.py       # Centralized runtime configuration state
│
└── core/
    ├── execution_controller.py  # Orchestrates retries, timeouts, and API fallbacks
    ├── prompt_templates.py      # Centralized prompts and fallback boundaries
    ├── llm_router.py            # Adapts output streaming for Ollama/Cloud API
    ├── embeddings.py            # Local SentenceTransformers / OpenAI embeddings interface
    ├── chunking.py              # Recursive character paragraph splitter
    ├── vectorstore.py           # Persistent ChromaDB collection managers
    └── intelligence/
        ├── query_rewriter.py    # Removes prefix noise and conversational grammar
        └── reranker.py          # Prunes context chunks using similarity metrics
```

---

## 🏃‍♂️ 1-Minute Setup & Launch

To run the system locally, make sure you have python 3.9+ and Ollama running locally.

```bash
# Install dependencies
pip install -r requirements.txt

# Start Ollama local model
ollama pull llama3

# Launch the dashboard
python app.py
```
For detailed workflow walkthroughs, read **[START_HERE.md](START_HERE.md)**.

---

## 📄 License

This example project is part of [AI-Model-Atlas](../../README.md). Source code is licensed under the [MIT License](../../LICENSE-CODE), while documentation content is licensed under [CC BY 4.0](../../LICENSE).
