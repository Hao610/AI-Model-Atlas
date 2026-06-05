# RAG System Design 🏗️

[English] | [中文 (21_rag_system_design_zh.md)](21_rag_system_design_zh.md)

Building a basic RAG system that reads a PDF and answers questions is easy. But building a **production-grade** RAG system that is accurate, handles thousands of documents, and has low latency is highly complex.

This guide explains the architectural bridge from a prototype RAG to a production system.

---

## 🗺️ The Production RAG Pipeline

In a production system, we add **Preprocessing** and **Post-Retrieval** steps to make sure the AI gets the absolute best context:

```text
User Query ──► [ Query Rewriting ] ──► [ Vector DB Search ] ──► [ Reranker (Filter) ] ──► LLM
```

---

## ⚡ 1. Advanced Chunking Strategies

Standard RAG slices text by character limits (e.g. every 500 characters). This can cut sentences in half, destroying their meaning. Production systems use smarter strategies:

* **Sliding Window (Overlap)**: Slicing text into paragraphs but leaving an overlap (e.g. 500-character chunks with 100 characters of overlap). This ensures context from the end of one chunk is carried over to the start of the next.
* **Semantic Chunking**: Slicing text only when the semantic meaning changes (e.g., detecting paragraph breaks or using an embedding model to split when the distance coordinate jumps).

---

## 🔄 2. The Power of Reranking

When you search a vector database, it returns the top 10 chunks based on vector distance. However, vector distance can be imprecise for complex reasoning.

To solve this, we add a **Reranker** (using a Cross-Encoder model like `cohere-rerank` or `bge-reranker`):

1. **Step 1 (Fast Retrieval)**: The Vector DB runs a fast, cheap search and fetches the top 50 candidates.
2. **Step 2 (Reranking)**: The Reranker model reads the user query and the 50 candidates, analyzing them deeply to re-sort them.
3. **Step 3 (Selection)**: We feed only the top 3 reranked, high-accuracy chunks to the LLM.

*This two-stage system gives you the speed of vector search combined with the analytical accuracy of a deep neural network.*

---

## ⏱️ 3. Latency Optimization

Retrieval adds latency. To keep your app fast:

* **Embedding Caching**: Store vectors of frequently searched queries.
* **Metadata Filtering**: Restrict your search *before* calculating vector distances. For example, if you know the user is asking about "2026", filter out all documents that aren't tagged with "2026" in the DB.

---

Now that you know how to architect search, let's explore inference optimizations to make the model run faster on your GPU in [Inference Optimization](../phase4_50_to_100/29_inference_optimization.md).
