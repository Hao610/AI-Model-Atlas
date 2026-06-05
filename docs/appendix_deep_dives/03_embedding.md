← Back to [Deep Dives Directory](../DEEP_DIVES.md) | [English] | [中文 (03_embedding_zh.md)](03_embedding_zh.md)

---

# 03. What is Embedding under the Hood?
> **From raw words to coordinate spaces: The visual geometry of vector representation.**

A computer cannot read a word; it only understands numbers. The naive solution is **One-Hot Encoding** (giving every word in the dictionary its own index: `apple = [1, 0, 0]`, `banana = [0, 1, 0]`). But this method fails to represent relationships—mathematically, `apple` is just as different from `banana` as it is from `nuclear reactor`.

An **Embedding** represents text as coordinates in a dense, high-dimensional space (often 768 or 1536 dimensions).

```text
Text Input          Embedding Model          High-Dimensional Vector
"King"     ──►    [ 1536-dim network ]   ──►    [ 0.25, -0.47, 0.89, ... ]
"Queen"    ──►    [ 1536-dim network ]   ──►    [ 0.23, -0.45, 0.91, ... ]
"Apple"    ──►    [ 1536-dim network ]   ──►    [ -0.88, 0.12, -0.34, ... ]
```

#### The Magic of Vector Arithmetic
Because these coordinates represent semantic meaning, words with similar concepts sit close to each other in this virtual space. This leads to the famous spatial relationship equation:

$$\overrightarrow{\text{King}} - \overrightarrow{\text{Man}} + \overrightarrow{\text{Woman}} \approx \overrightarrow{\text{Queen}}$$

Embeddings turn language into geometry, allowing us to compute the "meaning distance" between any two sentences.

#### Common Misconception: Embedding is NOT Compression
A common mistake for beginners is thinking that embedding acts as a text compression tool. 
* **The Misconception**: Believing that feeding a 1,000-word article to an embedding model compresses it into a "shortened summary" version.
* **The Reality**: The embedding vector (e.g., 1536 float values) represents the **address coordinates** of the text's meaning in a multi-dimensional semantic space, not the text itself. It is a coordinate card, not a compressed ZIP file. You cannot reverse-engineer or reconstruct the original 1,000 words from its coordinate vector.

---

With embeddings representing text as coordinates, let's learn how we search and retrieve them in [How Do Vector Databases Retrieve Meaning?](04_vector_db.md).
