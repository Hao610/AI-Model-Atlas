# Embeddings Deep Dive 📊

[English] | [中文 (20_embeddings_zh.md)](20_embeddings_zh.md)

Computers do not understand words, sentences, or books. They only understand numbers.

To bridge this gap, we use **Embeddings**. An embedding is a process that translates human text into a long list of numbers (a **Vector**) that captures the mathematical meaning of the text.

---

## 📍 Understanding Text Vectors

Imagine we represent words on a simple grid with two coordinates: **[Happiness, Size]**.

* **"Kitten"** might be represented as: `[0.9, -0.8]` (High happiness, small size).
* **"Tiger"** might be represented as: `[0.1, 0.9]` (Low happiness, large size).
* **"Puppy"** might be represented as: `[0.95, -0.75]` (High happiness, small size).

Because `"Kitten"` and `"Puppy"` have very similar coordinates, a computer instantly knows they are similar concepts, even if they share zero matching letters.

Modern embedding models (like OpenAI's `text-embedding-3-small`) do not use just 2 coordinates. They map text into **1,536 dimensions** (1,536 floating-point coordinates)!

---

## 📐 Measuring Similarity: Cosine Similarity

Once we have vectors, how do we calculate how similar two sentences are? We measure the angle between the two coordinate arrows (vectors). This math concept is called **Cosine Similarity**.

```text
Cosine Similarity Range:
  - 1.0 : Perfectly identical meaning (pointing in the exact same direction).
  - 0.0 : Completely unrelated (orthogonal).
  - -1.0 : Opposite meanings (pointing in opposite directions).
```

---

## 🐍 Python Code: Compare Two Sentences

Here is how you can use OpenAI or Ollama embeddings to calculate the similarity between sentences in Python.

```python
import numpy as np
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

def get_embedding(text):
    response = client.embeddings.create(
        model="nomic-embed-text",  # A popular local embedding model
        input=[text]
    )
    return response.data[0].embedding

def cosine_similarity(v1, v2):
    # Standard formula to measure the angle between two vectors
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return dot_product / (norm_v1 * norm_v2)

# Get vectors for three sentences
vec_a = get_embedding("I love puppies and dogs.")
vec_b = get_embedding("Canines are my favorite animals.")
vec_c = get_embedding("The stock market fell by two percent today.")

# Calculate similarity
print(f"Similarity A & B (Dog vs Canine): {cosine_similarity(vec_a, vec_b):.4f}")
print(f"Similarity A & C (Dog vs Stock Market): {cosine_similarity(vec_a, vec_c):.4f}")
```

### Expected Output:
* **Similarity A & B**: `~0.82` (Very high similarity, because "dogs" and "canines" share the same semantic concept).
* **Similarity A & C**: `~0.15` (Very low similarity).

---

Now that you know how semantic search operates, let's learn how we scientifically test and evaluate these models in [Model Evaluation](22_evaluation.md).
