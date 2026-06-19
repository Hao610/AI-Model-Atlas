<p align="center">
  <img src="https://github.com/user-attachments/assets/a51e8bb3-b2f3-4595-aee4-2272e2323086" alt="AI Model Atlas Logo" width="200">
</p>

# 📐 AI Model Atlas — System Architecture

> Engineering-grade deep dive into the Cognitive RAG system internals: benchmarks, failure recovery, and execution control.

← Back to [README](../README.md) | [中文架构文档 (ARCHITECTURE_zh.md)](ARCHITECTURE_zh.md)

---

## 🧭 System Architecture Poster

```mermaid
flowchart LR
    Query([User Query]) --> Pre[1. Preprocess & Rewrite]
    Pre --> Cache{2. Semantic Cache?}
    
    Cache -->|Hit| CacheHit[Fast Cache Output 0.00s]
    Cache -->|Miss| Router[3. Tool Router]
    
    Router -->|Math / Web| ExternalTool[Calculator / Web Search]
    Router -->|Graph| GraphRAG[GraphRAG 1-Hop Context]
    Router -->|Vector| RAG[Vector Search & Rerank]
    
    ExternalTool --> Output([Final Output])
    GraphRAG --> Controller[4. Execution Controller]
    RAG --> Controller
    
    Controller --> LLM[5. Hybrid LLM Route]
    
    CacheHit --> Output
    LLM --> Output

    classDef default fill:#111827,stroke:#374151,stroke-width:1px,color:#f9fafb;
    classDef highlight fill:#10b981,stroke:#047857,stroke-width:2px,color:#fff;
    classDef title fill:#1f2937,stroke:#4b5563,stroke-width:1px,color:#f3f4f6;

    class CacheHit highlight;
```

---

## 🚀 Key Features (with Code References)

- **🧠 Cognitive RAG Architecture**: Complete pipeline integration orchestrating the application flow. 
  - *Source:* [`rag_pipeline.py`](../projects/rag-app/core/rag_pipeline.py)
- **⚡ Persistent Semantic Cache**: Lightweight vector embedding dictionary checks for extreme latency reduction. State is persisted in JSON.
  - *Source:* [`cache/semantic_cache.py`](../projects/rag-app/core/cache/semantic_cache.py)
- **🔄 Query Rewriting**: Dynamic regex and prompt filters to normalize user intents before retrieval.
  - *Source:* [`intelligence/query_rewriter.py`](../projects/rag-app/core/intelligence/query_rewriter.py)
- **🎯 Hybrid Retrieval & RRF Reranking**: Combines Dense (ChromaDB) and Sparse (BM25) search, then fuses scores via Reciprocal Rank Fusion.
  - *Source:* [`intelligence/reranker.py`](../projects/rag-app/core/intelligence/reranker.py) | [`vectorstore.py`](../projects/rag-app/core/vectorstore.py)
- **🛡️ Execution Controller**: Orchestrated request center with fallback routing, exponential backoffs, and timeouts.
  - *Source:* [`execution_controller.py`](../projects/rag-app/core/execution_controller.py)
- **🌐 Hybrid LLM Core**: Dynamic routing between local Ollama installations and commercial OpenAI/DeepSeek API endpoints.
  - *Source:* [`llm_router.py`](../projects/rag-app/core/llm_router.py)
- **👁️ Structural Parsing & Table-Aware Chunking (Vision RAG)**: Complete atomic chunking for Markdown tables and PyMuPDF image extractions to prevent data fragmentation.
  - *Source:* [`parsing/pdf_parser.py`](../projects/rag-app/core/parsing/pdf_parser.py) | [`chunking/element_chunker.py`](../projects/rag-app/core/chunking/element_chunker.py)
- **🕸️ Lightweight Native GraphRAG**: Memory-based NetworkX Knowledge Graph running on a two-stage LLM entity/relation extraction architecture with 1-Hop traversal routing.
  - *Source:* [`graph/graph_store.py`](../projects/rag-app/core/graph/graph_store.py) | [`graph/graph_search_tool.py`](../projects/rag-app/core/graph/graph_search_tool.py)

---

## 🧠 System Runtime Model

### ⚡ Speed (What you feel)

*Disclaimer: Benchmarks are measured under local development test environments (single GPU / CPU fallback mode) and may vary under production load.*

| Configuration | Cache | Rerank | Backend | Latency (avg) | TTFT |
| :--- | :---: | :---: | :--- | :--- | :--- |
| **Local Ollama** | ❌ | ❌ | Ollama (Llama 3) | ~2.8s | 1.4s |
| **Local Ollama** | ✅ | ❌ | Ollama (Llama 3) | **~0.2s** | **0.05s** (Cache Hit) |
| **Hybrid Mode** | ✅ | ✅ | OpenAI API | ~0.8s | 0.3s |
| **Hybrid Mode** | ❌ | ✅ | OpenAI API | ~2.1s | 0.9s |

### 🛡️ Stability (When things break)

The system is designed to gracefully degrade under backend failure conditions to preserve service uptime:

#### Scenario: Local Ollama backend goes offline
1. **ExecutionController** detects connection timeout or handshake failures.
2. **Exponential Backoff Retry** mechanism triggers (automatic delays: 200ms -> 500ms -> 1s).
3. **Graceful Fallback Routing** active: switches the query endpoint automatically to the configured cloud API (OpenAI/DeepSeek).
4. **Degraded State Visualization**: system logs warnings and state shifts to the Streamlit observability console.

*Result: System continues responding to user queries without throwing unhandled terminal crashes.*

### 🧭 Logic (How choices are made)

The workflow logic operates on a strict request control state machine. You can trace this logic flow directly inside [`rag_pipeline.py`](../projects/rag-app/core/rag_pipeline.py).

```mermaid
stateDiagram-v2
    [*] --> ReceiveQuery
    ReceiveQuery --> QueryRewrite
    QueryRewrite --> CacheCheck

    CacheCheck --> CacheHit: match
    CacheCheck --> VectorSearch: miss

    VectorSearch --> Rerank
    Rerank --> ExecutionController

    ExecutionController --> Ollama
    ExecutionController --> CloudAPI

    Ollama --> Success
    Ollama --> Fail

    Fail --> RetryBackoff
    RetryBackoff --> CloudAPI

    CloudAPI --> Success
    Success --> [*]
```

---

## 📄 License

This document is part of [AI Model Atlas](../README.md), licensed under [CC BY 4.0](../LICENSE).
