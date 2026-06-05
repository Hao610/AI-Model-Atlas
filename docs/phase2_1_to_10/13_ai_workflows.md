# AI Workflows 🔄

[English] | [中文 (13_ai_workflows_zh.md)](13_ai_workflows_zh.md)

Building a real AI application is not just about sending a prompt to an LLM. It is about setting up a structured **workflow** where the LLM is just one of many steps.

Let's visualize the architecture of a complete RAG-enabled Agent system.

---

## 🗺️ The Complete Architecture Workflow

Below is the step-by-step diagram of how a user's question is processed in a professional AI application:

```text
[1. User Input] ──► "What are my Q3 sales targets?"
       │
       ▼
[2. The Agent Core] 
  - Analyzes the request.
  - Recognizes it needs factual documents.
       │
       ▼
[3. Retrieval (RAG)] 
  - Converts question to vector.
  - Queries Vector DB (e.g. Chroma).
  - Retrieves top matching document slices.
       │
       ▼
[4. Prompt Engineering Context Injection]
  - Combines: System instructions + Retrieved Documents + User Question.
       │
       ▼
[5. Large Language Model (LLM)]
  - Reads the packaged prompt context.
  - Formulates a factual, safe answer.
       │
       ▼
[6. Output Guardrail Filtering]
  - Checks if output contains sensitive data or code errors.
       │
       ▼
[7. User Output] ──► "Your Q3 sales target is $50,000..."
```

---

## ⚡ The Key Components Explained

1. **User Input**: The raw prompt from the chatbox.
2. **Agent Core (Orchestrator)**: The router. In advanced systems, the Agent decides: *"Do I answer this myself, query the database, or run a python script to get the answer?"*
3. **Retrieval Module**: The search engine. It translates human words to mathematical coordinates, finds similar coordinates in the vector database, and fetches the text.
4. **Context Ingestion**: Merges the retrieved facts with the user's question into one formatted block.
5. **LLM Inference**: The engine. It reads the context and produces the final natural language response.
6. **Guardrails**: Safety filters. They check the output to ensure the AI did not leak API keys, use offensive language, or hallucinate dangerous advice.

---

## 🎨 Why Workflows Matter

Without a workflow, you are simply hoping the AI remembers the facts you gave it. With a workflow:
* You control exactly what documents the AI reads.
* You restrict the AI to only talk about topics in your database.
* You save costs by only feeding the AI paragraphs that are relevant to the user's question, rather than uploading entire books for every message.

---

Now that you understand the architectural flow, let's explore real-world templates of this layout in [Real-World Use Cases](14_use_cases.md).
