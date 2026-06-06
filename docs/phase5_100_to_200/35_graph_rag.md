# Module 35: GraphRAG (Advanced)

Welcome to Module 35! In this module, we will explore **GraphRAG**, an advanced Retrieval-Augmented Generation approach that leverages Knowledge Graphs to provide more comprehensive answers, especially for complex, globally-oriented queries.

> [!IMPORTANT]
> **Please Read Before Panicking!**
> GraphRAG is designed for **HIGHLY relational data** (such as legal case files, medical research, or complex financial networks). It is **NOT** required for most standard RAG systems (like customer support bots or personal knowledge bases). Don't worry if this sounds extremely complex—standard vector RAG is more than enough for 95% of use cases!

## What is a Knowledge Graph?

A Knowledge Graph represents data as a network rather than isolated text chunks. It consists of two main components:
- **Nodes:** Entities (e.g., people, places, concepts, organizations).
- **Edges:** The relationships between these entities (e.g., "works for", "is located in", "treats").

By structuring data this way, we can explicitly capture the connections that might be lost when text is simply chopped into vector chunks.

## Why Do Knowledge Graphs Help with Global Summaries?

Standard vector RAG excels at **local queries**—finding a specific fact within a specific document. However, it often struggles with **global queries**, such as "What are the main themes across this entire dataset?" or "Summarize the major conflicts in this universe."

GraphRAG solves this by grouping nodes into hierarchical communities. When asked a global question, the system can summarize these communities bottom-up, allowing the LLM to understand the overarching narrative of the entire dataset rather than just piecing together a few top-k semantic matches.

## The Two-Stage Extraction Process

GraphRAG typically involves a complex pipeline to turn raw text into a usable graph, often referred to as a two-stage extraction process:

1. **Entity and Relationship Extraction:**
   The raw text is broken into chunks, and an LLM is used to identify all entities (Nodes) and the relationships between them (Edges). This stage transforms unstructured text into structured graph data.
   
2. **Community Detection and Summarization:**
   Algorithms (like Leiden) group closely connected nodes into "communities." The LLM then generates summaries for each of these communities. During retrieval, these community summaries are used to generate comprehensive answers that span the entire dataset.

---

← Prev: [34 vision rag.md](./34_vision_rag.md) | Next: [36 ai safety.md](36_ai_safety.md) →
