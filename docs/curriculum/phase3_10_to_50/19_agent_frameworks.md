# Agent Frameworks: Building Teams of AI 👥

> 📅 Last updated: 2026-10. AI ecosystems iterate rapidly; please refer to official documentation for the latest versions and pricing.

[English] | [中文 (19_agent_frameworks_zh.md)](19_agent_frameworks_zh.md)

What happens when a single AI prompt isn't enough to solve a complex business problem? The answer is **Multi-Agent Collaboration**.

Instead of asking one general AI to do everything, you create a **team of specialized AI agents** (e.g., a Researcher, a Writer, and a Critic) and let them talk to each other to complete a task.

To build these teams in Python, developers use specialized **Agent Frameworks** alongside standardized protocols like **MCP (Model Context Protocol)**.

---

## 🆚 Comparing the Major Frameworks

| Framework / Tool | Complexity | Architecture Style | Best Used For |
| :--- | :--- | :--- | :--- |
| **Dify / Coze** | ★ | Visual Drag & Drop | Quick prototypes, basic pipelines. |
| **CrewAI** | ★★ | Role-Play / Sequential | Writing blogs, market research, structured reports (Agent A -> Agent B). |
| **AutoGen** (by Microsoft) | ★★★ | Conversation-Driven | Multi-agent debates, brainstorming, autonomous coding games. |
| **LangGraph** (by LangChain) | ★★★★★ | Graph (Nodes & Edges) | Production-grade cyclical workflows with loops, state persistence, and human-in-the-loop. |
| **MCP (Model Context Protocol)** | ★★ | Protocol Standard | Universal standard for connecting agents to external databases, files, and tools. |
| **TypeSafe Jev Gateway** | ★ | System One Decision Gate | Sub-100ms deterministic gating for tool approvals and safety guards before expensive agent runs. |

---

## 🏛️ Framework Spotlights

### 1. CrewAI (The Practical Multi-Agent Team)
CrewAI treats agents like a corporate team. You define:
* **Agents**: "Researcher" (has internet tool), "Writer" (no tools, just writes).
* **Tasks**: Task 1: *"Research the top 3 AI trends of 2026."* Task 2: *"Write an engaging blog post about these trends."*
* **Crew**: Combines the agents and tasks, executing them sequentially or hierarchically.

### 2. AutoGen (The Conversational Playground)
Developed by Microsoft, AutoGen is built around **conversation**. You create agents (like a coder and a code reviewer) and they chat with each other in an infinite loop until the task is marked as complete. One agent writes the code, the other runs it in a safe environment, checks for errors, and gives feedback.

### 3. LangGraph (The Graph-Based Engine)
When your workflows are not linear (e.g. if the user says "No", go back to Step 2; if the user says "Yes", proceed to Step 4), you need LangGraph. It models agent states as a **Graph** containing:
* **Nodes**: The actions or agents (e.g., "Draft Email").
* **Edges**: The conditional paths (e.g., "If email is approved -> Send; else -> Rewrite").

---

## 🛡️ LangChain Security Overview

LangChain is the most widely adopted framework in enterprise agent ecosystems, but its flexible tool-execution pipeline makes it a primary surface for adversarial attacks:

* **PromptTemplate Injection**: Untrusted user variables breaking out of template formatting delimiters to hijack agent intent.
* **Tool Description Poisoning**: Malicious semantic overrides within tool `description` fields tricking LLMs into unauthorized tool calls.
* **Memory Buffer Hijacking**: Poisoning conversation history buffers to manipulate downstream multi-turn agent decisions.
* **OutputParser Manipulation**: Coercing output parsers into triggering unintended fallback actions or raw code execution.

> 📖 **Deep Dive Available**: For a full trust-boundary dissection, attack vector taxonomy, and runtime defense implementation with `ContextGuard` and `SafetyJudge`, see **[Module 37: LangChain Security Deep Dive](../phase5_100_to_200/37_langchain_security.md)**.

---

## 🔍 How to Start?

1. **If you want to build a content writing or marketing pipeline**: Use **CrewAI**. It is highly intuitive and gets multi-agent systems running in minutes.
2. **If you need complex logic loops, human-in-the-loop approvals, and precise control**: Invest the time to learn **LangGraph**. It is a strong choice for production-grade AI workflows where explicit state management matters.

---

Now that you know how to build teams, let's explore how computers understand the meaning of human text behind the scenes in [Embeddings Deep Dive](20_embeddings.md).
