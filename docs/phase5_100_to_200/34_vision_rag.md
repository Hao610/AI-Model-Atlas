# Module 34: Vision RAG & OCR

[English] | [中文 (34_vision_rag_zh.md)](34_vision_rag_zh.md)

---

Your shiny new RAG system works flawlessly on plain text documents. You ask it to summarize a company's history, and it answers perfectly. But then, you upload a corporate financial report (PDF). You ask a simple question: "What was the revenue in Q3 2024?" The system hallucinates or says it doesn't know. 

Why is it failing on corporate PDFs? Because it destroyed the tables. It's time to give your RAG system "eyes".

## The Core Insight: Tables Are Not Text, They Are Structure

Most naive document loaders and OCR tools treat pages as a flat sequence of words. When they encounter a table, they read it left-to-right, line-by-line, completely oblivious to the columns and rows that give the numbers meaning.

**Tables are the hardest part of RAG.**

### The Destruction of Structure: A Visual Demo

Imagine a simple financial table:

| Metric | Q3 2024 | Q4 2024 |
|---|---|---|
| Revenue | $150M | $200M |
| Expenses | $100M | $120M |

**How a simple chunker reads it (The Text Destruction):**
`Metric Q3 2024 Q4 2024 Revenue $150M $200M Expenses $100M $120M`

Once flattened into this string, the relationship between "Revenue", "Q3 2024", and "$150M" is gone. If a user asks "What was Q4 Expense?", the LLM sees `$200M Expenses $100M`, gets confused, and hallucinates.

**How a Vision RAG system sees it (The Structured Layout):**
A Vision RAG system preserves the bounding boxes and HTML/Markdown representation of the table.

```html
<table>
  <tr><th>Metric</th><th>Q3 2024</th><th>Q4 2024</th></tr>
  <tr><td>Revenue</td><td>$150M</td><td>$200M</td></tr>
  <tr><td>Expenses</td><td>$100M</td><td>$120M</td></tr>
</table>
```

## How to Give Your RAG System Eyes

Instead of blindly stripping text, modern Vision RAG pipelines use multi-modal models or advanced document parsing tools to understand the *layout* of the page.

1. **Layout Detection:** The system first identifies regions on the PDF: "This is a paragraph," "This is an image," "This is a table."
2. **Table Extraction:** Specialized models (like Table Transformer) extract tables and convert them into structured formats (Markdown or HTML).
3. **Multi-Modal Embeddings:** Some advanced systems embed images of the tables directly using vision-language models, preserving all visual context.
4. **Summary Augmentation:** We can pass the structured table to an LLM to write a plain-text summary of the table, and store *both* the summary and the raw table in our vector database.

By respecting the visual layout of documents, we stop destroying data before our LLM even gets a chance to read it.

---

← Prev: [33 rag evaluation](33_rag_evaluation.md) | Next: [35 graph rag](35_graph_rag.md) →
