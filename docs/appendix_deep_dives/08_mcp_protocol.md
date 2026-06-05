← Back to [Deep Dives Directory](../../DEEP_DIVES.md) | [English] | [中文 (08_mcp_protocol_zh.md)](08_mcp_protocol_zh.md)

---

# 08. Model Context Protocol (MCP) — The USB-C of AI
> **Solving the N x M integration problem: How a unified protocol standardizes AI tools.**

As AI models began calling external tools (reading Notion, querying databases, searching GitHub), engineers faced a scaling nightmare: the **$N \times M$ integration problem**.

```text
Without MCP (Proprietary Integrations):
Claude  ──►  Notion Driver  |  GPT  ──►  Notion Driver  |  Llama  ──►  Notion Driver
Claude  ──►  GitHub Driver  |  GPT  ──►  GitHub Driver  |  Llama  ──►  GitHub Driver
```

If you had $N$ models and $M$ tools, developers had to write custom API connectors for every single pair.

#### The USB-C of AI
The **Model Context Protocol (MCP)**, introduced by Anthropic, acts as a universal adapter. It defines a standard communication protocol between models (clients) and data sources (servers).

```text
With MCP (Universal Standard):
Claude ──┐             ┌──► GitHub Server
GPT    ──┼─► [ MCP ] ──┼──► Notion Server
Llama  ──┘             └──► Local Filesystem
```

Now, developers only write one MCP connector for their tool, and any MCP-compliant model can immediately query, write, and interact with it. It standardizes how AI reads contexts, executes actions, and prompts local environments.

---

MCP standardizes the tools our models can use, but how do we build systems that plan and execute actions autonomously? Learn more in [Why an Agent is More Than a Prompt](09_agent_mechanics.md).
