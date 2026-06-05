← Back to [Deep Dives Directory](../../DEEP_DIVES.md) | [English] | [中文 (09_agent_mechanics_zh.md)](09_agent_mechanics_zh.md)

---

# 09. Why an Agent is More Than a Prompt
> **The cybernetic feedback loop: Orchestrating memory, tools, planning, and execution.**

A standard LLM call is a **linear pipeline**: input goes in, output comes out, and the process stops. A simple system prompt (e.g., *"You are a helpful assistant"*) does not make it an Agent.

An **Autonomous Agent** is a dynamic feedback loop that wraps around an LLM to coordinate five components:

```text
                  ┌────────────────────────┐
                  ▼                        │
User Goal ──► [ Planning ] ──► [ Execution / Tools ] ──► [ Environment ]
                  ▲                        │
                  └─────── [ Memory ] ◄────┘
```

#### The Five Pillars of Agentic Architecture
1. **The Brain (LLM)**: Provides core logic, text comprehension, and decision making.
2. **Planning (Self-Reflection)**: The agent breaks down a complex goal (*"Book a flight and hotel for my trip"*) into discrete sub-tasks, evaluates its own intermediate results, and corrects course if a tool fails.
3. **Memory**:
   * *Short-Term Memory*: Tracks the current execution steps.
   * *Long-Term Memory*: Retains information across sessions (storing user preferences in a vector database).
4. **Tools**: External APIs (web search, databases, terminal access) that allow the agent to affect the real world.
5. **Execution**: Running loop controllers (like LangGraph) that keep the agent active until the goal is verified as completed.

---

Agents require intelligence and speed. Let's see how modern architectures keep costs down while scaling up parameters in [Why MoE Makes Scale Affordable](10_moe_architecture.md).
