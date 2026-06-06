# 📐 AI-Model-Atlas — 系统架构文档

> 认知级 RAG 系统的工程深度剖析：性能指标、容灾自愈与执行控制。

← 返回 [中文首页](../README_zh.md) | [English Architecture (ARCHITECTURE.md)](ARCHITECTURE.md)

---

## 🧭 系统数据流向与架构设计

```mermaid
flowchart LR
    Query([用户问题]) --> Pre[1. 查询改写与预处理]
    Pre --> Cache{2. 语义缓存拦截?}
    
    Cache -->|命中| CacheHit[极速返回 0.00s]
    Cache -->|未命中| RAG[3. 混合向量检索与重排]
    
    RAG --> Controller[4. 执行控制中心]
    Controller --> LLM[5. 双模 LLM 路由]
    
    CacheHit --> Output([最终输出])
    LLM --> Output

    classDef default fill:#111827,stroke:#374151,stroke-width:1px,color:#f9fafb;
    classDef highlight fill:#10b981,stroke:#047857,stroke-width:2px,color:#fff;
    classDef title fill:#1f2937,stroke:#4b5563,stroke-width:1px,color:#f3f4f6;

    class CacheHit highlight;
```

---

## 🚀 核心架构与源码映射 (Code References)

- **🧠 认知级 RAG 主干**: 统一串联组件，调度系统的整体数据流转链路。
  - *源码路径:* [`rag_pipeline.py`](../projects/rag-app/core/rag_pipeline.py)
- **⚡ 持久化语义缓存**: 内存级向量比对机制，通过本地 JSON 持久化，实现 0 时延拦截高频相似问题。
  - *源码路径:* [`cache/semantic_cache.py`](../projects/rag-app/core/cache/semantic_cache.py)
- **🔄 智能查询改写**: 动态 Prompt 过滤器，在检索前剥离用户的口语化噪音。
  - *源码路径:* [`intelligence/query_rewriter.py`](../projects/rag-app/core/intelligence/query_rewriter.py)
- **🎯 混合检索与 RRF 重排**: 融合 ChromaDB 稠密向量与 BM25 稀疏检索，并通过倒数秩融合(RRF)进行双重打分排序。
  - *源码路径:* [`intelligence/reranker.py`](../projects/rag-app/core/intelligence/reranker.py) | [`vectorstore.py`](../projects/rag-app/core/vectorstore.py)
- **🛡️ 执行控制平面**: 统一接管请求生命周期，处理超时、异常、指数退避重试。
  - *源码路径:* [`execution_controller.py`](../projects/rag-app/core/execution_controller.py)
- **🌐 双模 LLM 推理层**: 动态解耦 Ollama 本地模型与商业云端 API (如 OpenAI/DeepSeek)。
  - *源码路径:* [`llm_router.py`](../projects/rag-app/core/llm_router.py)

---

## 🧠 系统运行模型 (System Runtime Model)

### ⚡ 速度与性能指标

*注：以下基准测试在单卡消费级 GPU/CPU 降级环境中进行，生产环境中并发性能可能会有所不同。*

| 配置 | 缓存 | 重排 | 后端引擎 | 总体延迟 (avg) | 首字输出延迟 (TTFT) |
| :--- | :---: | :---: | :--- | :--- | :--- |
| **纯本地模式** | ❌ | ❌ | Ollama (Llama 3) | ~2.8s | 1.4s |
| **纯本地模式** | ✅ | ❌ | Ollama (Llama 3) | **~0.2s** | **0.05s** (缓存命中) |
| **云端混合模式** | ✅ | ✅ | OpenAI API | ~0.8s | 0.3s |
| **云端混合模式** | ❌ | ✅ | OpenAI API | ~2.1s | 0.9s |

### 🛡️ 容灾与自愈机制 (当系统崩溃时)

为了保证工业级的可用性，系统采用了**优雅降级 (Graceful Degradation)** 的防御设计：

#### 场景演练：当本地 Ollama 节点宕机断电时
1. **执行控制中心 (ExecutionController)** 感知到 TCP 握手失败或连接超时。
2. **指数退避重试** 被激活 (阻断延时自动攀升: 200ms -> 500ms -> 1s)。
3. **故障降级路由** 生效：强制阻断本地请求，自动将用户提示词平滑重定向至备用云端 API (OpenAI/DeepSeek)。
4. **前端可观测性**：Streamlit UI 依然保持可用，同时日志控制台会高亮打印状态迁移告警。

*结果：用户体验零中断，完全感知不到底层服务器已经挂掉。*

### 🧭 状态机流转逻辑

整个生命周期的核心流转逻辑是一个严格的状态机。你可以在 [`rag_pipeline.py`](../projects/rag-app/core/rag_pipeline.py) 中对照查阅具体的执行逻辑：

```mermaid
stateDiagram-v2
    [*] --> ReceiveQuery
    ReceiveQuery --> QueryRewrite
    QueryRewrite --> CacheCheck

    CacheCheck --> CacheHit: 匹配成功
    CacheCheck --> VectorSearch: 匹配失败 (触发双路检索)

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

## 📄 开源协议

本文档为 [AI-Model-Atlas](../README_zh.md) 项目的一部分，遵循 [CC BY 4.0](../LICENSE_zh) 协议。
