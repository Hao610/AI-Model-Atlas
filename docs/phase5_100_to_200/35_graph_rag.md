# Module 35: GraphRAG (Advanced)

[English] | [中文 (35_graph_rag_zh.md)](35_graph_rag_zh.md)

Imagine you are investigating a complex corporate fraud case or researching a rare disease across thousands of medical journals. In these scenarios, matching paragraphs of text isn't enough. You need to know that "Company A" owns "Subsidiary B", which transferred funds to "Executive C". You are dealing with a massive web of legal or medical data where finding connections between entities is more important than matching text.

This is where GraphRAG (Retrieval-Augmented Generation with Knowledge Graphs) comes in. The core insight here is simple but profound: **"Relationships are more important than content."**

## What is GraphRAG?

Traditional RAG systems slice documents into chunks and retrieve them based on semantic similarity. They are great at answering "What does the manual say about X?" but terrible at answering "How are X, Y, and Z connected across our entire company history?"

GraphRAG builds a Knowledge Graph—a web of nodes (entities) and edges (relationships)—from your data. When a user asks a question, the system traverses this graph to retrieve connected facts, providing the LLM with structured context rather than just a list of text chunks.

## When Do You Actually Need It?

> [!WARNING]
> **GraphRAG Is Not Magic**
> 
> GraphRAG solves structure problems, not knowledge problems. It is highly effective for specific domains like legal case law, medical research, or complex supply chain analysis where relationships dictate the answer. However, the industry hype claiming "GraphRAG = Next Gen RAG" that replaces everything is false. For 90% of normal document retrieval tasks, Hybrid Search + RRF (Reciprocal Rank Fusion) is usually enough, much cheaper, and easier to maintain.

Use GraphRAG when your questions look like:
*   "What are the indirect connections between Patient 0 and the new outbreak?"
*   "Who are all the board members of companies associated with this legal dispute?"

Do **not** use GraphRAG for:
*   "Summarize this PDF."
*   "How do I reset my password?"

## How It Works (The Simplified Version)

1.  **Entity Extraction:** An LLM reads your raw documents and extracts entities (People, Organizations, Diseases, Locations).
2.  **Relationship Mapping:** The LLM identifies how these entities are connected (e.g., "Person A" *is CEO of* "Organization B").
3.  **Graph Construction:** These entities and relationships are stored in a Graph Database (like Neo4j).
4.  **Graph Retrieval:** When a query is asked, the system finds the relevant starting entities and traverses their connections to build a comprehensive context window.
5.  **Generation:** The LLM uses this mapped-out network to answer the question.

GraphRAG is powerful, but it requires significant engineering effort to build and maintain the knowledge graph. Choose it only when the relationships between your data points hold the true value of your information.

---
← Prev: [34 vision rag](34_vision_rag.md) | Next: [36 ai safety](36_ai_safety.md) →
