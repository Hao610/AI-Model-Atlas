# Vector Databases 🗄️

[English] | [中文 (vector_db_zh.md)](vector_db_zh.md)

In traditional databases (like MySQL or Excel sheets), you look up data by exact matches (e.g., search for the ID `105` or the exact word `"apple"`).

But in AI, we search by **meaning (semantics)**. If you search for *"kitten"*, the system should find documents containing *"small cat"* or *"cute meow"*, even if the word *"kitten"* is never mentioned.

To do this, we convert text into mathematical coordinates (vectors) and store them in a **Vector Database**.

---

## 📍 The Analogy: The Semantic Map

Imagine a massive 3D map where words are placed based on what they mean:

* **"King"** and **"Queen"** are floating close to each other.
* **"Apple"** and **"Banana"** are in a different corner.
* **"Computer"** and **"Laptop"** are in another.

A Vector Database doesn't search for text spelling. It calculates the physical distance between coordinates. When you search for *"phone"*, it looks at the coordinate of *"phone"* and grabs the closest items on the map, such as *"smartphone"* or *"mobile device"*.

---

## 🏆 The Big Four Vector Databases

When choosing a vector database for your RAG system, you will generally pick one of these four:

| Database | Complexity | Scalability | Best Used For |
| :--- | :--- | :--- | :--- |
| **Chroma** | ★ | ★★ | **Beginners / Prototyping**: Runs completely inside your Python script with zero setup. Great for local apps. |
| **FAISS** (by Meta) | ★★ | ★★★ | **High-speed local search**: A raw library (not a full DB) designed for hyper-fast mathematical lookups on your machine. |
| **Milvus / Qdrant** | ★★★★ | ★★★★★ | **Enterprise scale**: Distributed databases designed to handle billions of vector coordinates across cluster nodes. |
| **PGVector** | ★★★ | ★★★★ | **Relational hybrid**: An extension for PostgreSQL. Excellent if you want to store your standard tables and vectors in the same DB. |

---

## 🔍 How to Choose?

1. **If you are starting out today**: Use **Chroma**. It takes 1 line of Python code to start, and you don't need to install any external database software.
2. **If you already use PostgreSQL**: Just install the `pgvector` extension. This keeps your architecture simple and avoids setting up a secondary database.
3. **If you are building a massive enterprise system**: Deploy **Milvus** or **Qdrant** in the cloud to handle scale.

---

Now that you know where vectors are stored, let's look at the flow of data in a complete system in [AI Workflows](ai_workflows.md).
