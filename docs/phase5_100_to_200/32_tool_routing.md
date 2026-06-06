# Module 32: Tool Routing (Agentic RAG)

[English] | [中文 (32_tool_routing_zh.md)](32_tool_routing_zh.md)

Welcome to the next level of AI engineering. You've built a basic RAG (Retrieval-Augmented Generation) pipeline, where your model fetches relevant documents to answer a question. That's a great start. But what happens when the user asks a question that requires real-time data, complex math, or writing and running code? 

A standard RAG pipeline will fail. It only knows how to search its static database. 

Now, how do you make it an orchestrated system? Enter **Agentic RAG** and **Tool Routing**.

> **Core Insight:** AI is no longer just a model, it's a system.

## Why ChatGPT Isn't Just One Model

When you interact with modern AI products like ChatGPT or Claude, you aren't just talking to a single, monolithic language model. You are interacting with an orchestrated ecosystem.

If you ask for the latest weather, it searches the web. If you ask it to plot a graph, it writes Python code and executes it in a secure sandbox. The language model isn't doing the math or the web scraping directly—it's acting as a **Router** that decides *which tool to use*.

Here is a simplified view of how this architecture works:

```text
User
  │
  ▼
[ Router (LLM) ] ──▶ (Needs current data?) ──▶ [ Search ]
  │
  ├──▶ (Needs exact math?) ──────────────────▶ [ Calc ]
  │
  └──▶ (Needs data analysis/execution?) ─────▶ [ CodeRunner ]
  │
  ▼
(Tool execution results returned)
  │
  ▼
[ LLM Synthesizes Final Answer ]
  │
  ▼
User
```

## How Tool Routing Works

In Agentic RAG, the language model is given a "toolbox" (a list of available functions or APIs) along with descriptions of what each tool does. 

When a user prompt comes in, the process is:
1. **Analyze:** The LLM reads the prompt and evaluates if it can answer directly or if it needs help from a tool.
2. **Route:** If a tool is needed, the LLM outputs a structured command (like JSON) specifying the tool name and the arguments to pass into it.
3. **Execute:** The system intercepts this command, runs the external tool (e.g., querying an API), and captures the output.
4. **Synthesize:** The tool's output is fed back into the LLM, which then reads the result and crafts a natural, accurate response for the user.

## From Pipeline to Autonomous Agent

By implementing tool routing, you graduate from building static "pipelines" to building "agents." 

Your AI is no longer a passive encyclopedia. It is an active problem solver that can plan, gather information from multiple sources, interact with external software, and synthesize complex answers. As an AI Systems Engineer, your job shifts from merely tuning prompts to designing the robust, reliable tools your agent will wield.

---

← Prev: [31 deployment](../phase4_50_to_100/31_deployment.md) | Next: [33 rag evaluation](33_rag_evaluation.md) →
