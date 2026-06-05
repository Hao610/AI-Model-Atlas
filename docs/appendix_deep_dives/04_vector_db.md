← Back to [Deep Dives Directory](../../DEEP_DIVES.md) | [English] | [中文 (04_vector_db_zh.md)](04_vector_db_zh.md)

---

# 04. How Do Vector Databases Retrieve Meaning?
> **Moving beyond string matches: Nearest neighbor algorithms and the mechanics of HNSW.**

A traditional SQL database searches for exact string matches (`WHERE description = 'iPhone'`). If a user searches for `"Apple smartphone"`, the query returns empty because the characters do not match.

A **Vector Database** solves this by storing the Embedding coordinates of text blocks and searching for the mathematically closest vectors.

#### 1. Calculating Distance
* **Cosine Similarity**: Measures the angle between two vectors. If they point in the same direction, the score is close to $1.0$, regardless of sentence length.
* **Euclidean Distance**: Measures the straight-line distance between two points in space.

#### 2. Scaling the Search (Approximate Nearest Neighbors - ANN)
If your database has 10 million documents, calculating the cosine similarity for all of them for every search query is too slow. Vector databases use **HNSW (Hierarchical Navigable Small World)** graphs.

```text
HNSW Multi-Layer Highway Graph:
Layer 2 (Express) ──►  [Point A] ──────────────────────────► [Point F]
Layer 1 (Local)   ──►  [Point A] ──► [Point C] ────────────► [Point F]
Layer 0 (All)     ──►  [Point A] ──► [Point B] ──► [Point C] ──► [Point F]
```

HNSW builds a multi-layered network of vectors, similar to an express highway system. The search starts at the top layer (skipping far-away clusters quickly) and drops down to lower layers for high-precision local routing. This reduces search time from $O(N)$ to $O(\log N)$.

#### The Critical Bridge: Chunking
In real production systems, you cannot feed an entire 500-page book to an embedding model all at once (due to model input limits and semantic dilution). Instead, developers implement a pipeline:
`Document ──► Chunking ──► Embedding ──► Vector Database`

**Chunking** is the process of breaking long documents into smaller, coherent text segments. Getting the chunk size right is a crucial engineering trade-off:
* **Chunk too large (e.g., 2000 tokens)**: Semantic coordinates get diluted. If a single sentence of high importance is buried in 2,000 words of background details, the overall embedding vector will represent the average background topic, making the specific key sentence hard to retrieve.
* **Chunk too small (e.g., 50 tokens)**: The query retrieves the exact sentence, but surrounding context is completely lost. When the sentence is passed to the LLM, the model cannot understand pronouns, references, or the overall intent, leading to poor answers.

---

Now that you know how vector databases retrieve semantic coordinates, let's explore how we use them to feed external context to models in [Why is RAG so Effective?](05_rag_principles.md).
