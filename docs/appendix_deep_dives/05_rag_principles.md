← Back to [Deep Dives Directory](../../DEEP_DIVES.md) | [English] | [中文 (05_rag_principles_zh.md)](05_rag_principles_zh.md)

---

# 05. Why is RAG so Effective?
> **Open-book vs. closed-book exams: Bridging the gap between static knowledge and dynamic lookup.**

Without RAG, large language models operate in **Closed-Book Mode**. All their knowledge is permanently baked into their parameters during training.

```text
Closed-Book Model (Static Params):
User Query ──► [ LLM (Frozen parameters) ] ──► Response (May hallucinate if outdated)
```

#### The Limits of Parameters
1. **Outdated**: A model trained in 2024 does not know what happened in 2025.
2. **Blind Spot**: A model has never seen your company's private internal wiki or invoice PDFs.
3. **Expensive**: Retraining a model to teach it new information costs millions of dollars in compute.

#### The RAG Solution (Open-Book Mode)
**Retrieval-Augmented Generation (RAG)** turns the process into an **Open-Book Exam**.

```text
Open-Book Model (RAG Workflow):
User Query ──► [ Retrieve relevant text from DB ] ──► [ Paste into Prompt ] ──► [ LLM reads & writes answer ]
```

RAG keeps the model frozen and updates the database instead. When a user asks a question, the system retrieves the most relevant paragraphs from the database, pastes them into the prompt template as reference context, and asks the model to read them and write an answer. This guarantees fresh information, zero retraining costs, and highly auditable citations.

---

RAG anchors models with facts, but why do they lie when they don't have them? Find out in [Why Do Large Models Hallucinate?](06_hallucination.md).
