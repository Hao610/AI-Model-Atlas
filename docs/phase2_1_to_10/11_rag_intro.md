# RAG: Retrieval-Augmented Generation 📚

[English] | [中文 (11_rag_intro_zh.md)](11_rag_intro_zh.md)

If you ask an AI about your company’s internal product roadmap or your private daily schedule, it will either hallucinate or tell you it doesn't know. This is because models are only trained on public internet data.

How do we give the AI access to private data without retraining it? The answer is **RAG (Retrieval-Augmented Generation)**.

---

## 📖 The Analogy: Closed-Book vs. Open-Book Exam

Think of how you would answer a complex history exam:

* **Traditional LLM (Closed-Book Exam)**: You sit in a room with no internet and no books. You must rely purely on what you memorized during your training. If you get asked a highly specific question, you might guess or get confused.
* **RAG LLM (Open-Book Exam)**: You sit in a room, and someone hands you a question. Before you answer, a fast librarian runs into a private library, pulls out the exact 3 pages containing the answer, and places them on your desk. You read those pages and write a perfect, factual answer.

```text
User Question
     │
     ▼
[ Search System ] ──► Queries Private Library ──► Retrieves Relevant Pages (Context)
     │
     ▼
[ Combined Prompt ] (Question + Retrieved Pages) ──► LLM ──► Factual Answer
```

---

## ⚙️ How RAG Works: Step-by-Step

RAG operates in two main phases: **Preparation** and **Retrieval**.

### Phase 1: Preparing the Library (Ingestion)
1. **Document Loading**: You feed your PDFs, Word files, or website links into the RAG system.
2. **Chunking**: The system cuts long documents into small, bite-sized paragraphs (e.g., 500 characters each). This prevents the AI's desk (Context Window) from getting cluttered.
3. **Embedding**: The system converts these text paragraphs into mathematical coordinates (vectors).
4. **Vector Database**: These coordinates are stored in a specialized database.

### Phase 2: Answering a Question (Retrieval & Generation)
1. **The Query**: User asks: *"What is our company's refund policy for damaged goods?"*
2. **Retrieval**: The system converts the query into coordinates, searches the Vector DB, and instantly pulls out the top 3 most similar paragraphs.
3. **Prompt Packing**: The system constructs a super-prompt for the LLM:
   > *"Answer the user question using only the following context. Context: [Inserts the 3 retrieved paragraphs]. Question: What is our company's refund policy for damaged goods?"*
4. **Generation**: The LLM reads the context and writes a highly accurate answer.

---

## ⚖️ RAG vs. Fine-Tuning

Beginners often get confused between RAG and Fine-Tuning. Here is how they compare:

| Feature | RAG (Open-Book) | Fine-Tuning (Brain Surgery) |
| :--- | :--- | :--- |
| **Primary Goal** | Accessing new/private **factual information**. | Customizing the **style, tone, or format** of the model. |
| **Setup Cost** | Very low. | High (requires high-end GPUs). |
| **Updating Knowledge**| Instant (just upload or delete a file in the DB). | Slow (requires running a new training job). |
| **Factuality** | Extremely high (less hallucination). | Moderate (still prone to making things up). |

---

Now that you know the theory of RAG, let's look at where we store these mathematical text coordinates in [Vector Databases](12_vector_db.md).
