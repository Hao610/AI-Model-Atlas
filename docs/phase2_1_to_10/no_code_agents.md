# No-Code Agents Guide 🛠️

[English] | [中文 (no_code_agents_zh.md)](no_code_agents_zh.md)

You don't need to write code to build complex AI applications. Modern visual platforms like **Dify** and **Coze** (by ByteDance) allow you to build fully autonomous **AI Agents** using a visual interface. 

Let's break down the anatomy of a No-Code Agent.

---

## 🧩 The Anatomy of an Agent

An Agent is more than just a chatbot. It is a model equipped with three key additions:

```text
               ┌──────────────────────┐
               │    Large Language    │
               │     Model (LLM)      │
               └──────────┬───────────┘
                          │
         ┌────────────────┼────────────────┐
         ▼                ▼                ▼
     [Memory]          [Tools]         [Knowledge]
 (Chat history)     (Google, APIs)    (Uploaded PDFs)
```

1. **System Prompt (The Soul)**: Instructions that set its behavior, role, and boundaries.
2. **Tools (The Hands)**: Plugins that allow the model to interact with the real world (e.g., search Google, send an email, check the weather).
3. **Memory (The Brain)**: Storing past interactions so the agent remembers you across sessions.
4. **Knowledge (The Library)**: Static files or database records the agent can query to answer factual questions.

---

## 🆚 Dify vs. Coze

If you are looking to build a no-code agent, these are the two best platforms:

| Feature | Dify | Coze |
| :--- | :--- | :--- |
| **Hosting** | Open Source (Self-hostable or Cloud). | Fully Managed Cloud (hosted by ByteDance). |
| **Best Used For** | Enterprise internal pipelines, connecting to local databases. | Creating social media bots (Telegram, Discord, WeChat), public APIs. |
| **Plugin Ecosystem** | Good, focuses on developer tools. | Massive, hundreds of ready-to-use search and multimedia plugins. |
| **Workflow Engine** | Highly structured, excellent visual graph designer. | Very user-friendly, has integrated code sandboxes. |

---

## 📝 Step-by-Step: How to Build a Simple Support Agent

Here is the blueprint for creating a customer support assistant on Dify:

1. **Create an App**: Choose **Chatflow** (for structured pipelines) or **Agent** (for flexible tool usage).
2. **Define the Prompt**:
   > *"You are a helpful customer support agent for 'CoolShoes Inc.' Answer user questions politely using the uploaded Knowledge library. If you do not know the answer, do not make it up; instead, trigger the Email Tool to forward the query to a human operator."*
3. **Connect Knowledge**: Upload your company FAQ PDF. Dify will automatically slice the document (chunking) and set it up for search.
4. **Add Tools**: Add the Google Search tool and a simple email-sending block.
5. **Publish**: Dify gives you a clean web link. You can send this link to anyone to try your bot instantly.

---

No-code platforms handle the indexing automatically, but what happens under the hood when the agent reads your files? Let's discover in [RAG Introduction](rag_intro.md).
