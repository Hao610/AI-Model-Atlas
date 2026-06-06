# Module 33: RAG Evaluation
[English] | [中文 (33_rag_evaluation_zh.md)](33_rag_evaluation_zh.md)

You've built your RAG pipeline. You type in a few test questions, the answers look pretty good, and you deploy it. But how do you know if it's actually getting better when you tweak the chunk size? How do you know an upgrade didn't break something else? 

Are you relying on "vibes" to know if your system is improving?

**Core Insight:** Without metrics, there is no progress.

## Play the Judge

Before we look at the metrics, let's play a game. You are the judge. 

**Context Document:** "Reciprocal Rank Fusion (RRF) is a method for combining multiple search result lists. It was developed by Gordon Cormack, Charles Clarke, and Stefan Buettcher in 2009."

**Question:** "Who invented RRF?"

Which of these is the "best" answer?

*   **Answer A:** "RRF, which stands for Reciprocal Rank Fusion, is a method utilized to combine multiple search result lists. According to the provided documentation, this technique was developed and formally introduced to the world in the year 2009 by a collaborative team of researchers consisting of Gordon Cormack, Charles Clarke, and Stefan Buettcher."
*   **Answer B:** "Gordon Cormack, Charles Clarke, and Stefan Buettcher."
*   **Answer C:** "RRF was invented by Google in 2015 to improve PageRank."

Think about it for a second.

*   **Answer A** is correct, but extremely long and wordy.
*   **Answer B** is concise but missing source evidence.
*   **Answer C** is completely hallucinated. 

To teach a machine to evaluate these answers, we break down what makes an answer "good" into specific, measurable categories: Faithfulness, Relevancy, and Precision.

## The RAG Evaluation Triad

Instead of a single "goodness" score, modern RAG evaluation usually measures three independent dimensions:

### 1. Faithfulness
Does the generated answer actually come from the retrieved context? 
*   **Answer A** and **Answer B** are faithful to the source document.
*   **Answer C** fails completely here (hallucination).

### 2. Answer Relevancy
Does the generated answer directly address the user's question without adding unnecessary fluff?
*   **Answer B** has high relevancy.
*   **Answer A** has lower relevancy because it is so wordy and includes details the user didn't ask for.

### 3. Context Precision
Did your retriever pull up useful information, or just garbage? 
Even if the LLM generates a great answer, if the *retrieved context* is irrelevant, the RAG system as a whole isn't working well. Context Precision measures if the retrieved documents are actually useful for answering the user's question.

## LLM-as-a-Judge

You might be wondering: "How do we score these automatically without hiring 100 humans to read every output?"

The secret is **LLM-as-a-Judge**. We use a strong LLM (like GPT-4) to grade our RAG pipeline's output. We give the Judge LLM the Question, the Context, and the Answer, and ask it to output a score from 1 to 5 for metrics like Faithfulness and Relevancy.

It turns out, strong LLMs are surprisingly good at grading other LLMs! By running your test dataset through an LLM Judge, you can get hard numbers to track your progress and stop relying purely on vibes.

---
← Prev: [32 tool routing](32_tool_routing.md) | Next: [34 vision rag](34_vision_rag.md) →
