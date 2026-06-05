← 返回 [深潜专题目录](../../DEEP_DIVES_zh.md) | [[English] (08_mcp_protocol.md)](08_mcp_protocol.md) | [中文]

---

# 08. MCP —— AI 世界的 USB-C
> **终结 N x M 适配噩梦：Model Context Protocol 是如何统一大模型数据总线的。**

随着大模型开始接管各类工具（如读取 Notion、读写本地文件、自动操作 GitHub），工程师们遇到了一场极其痛苦的 **$N \times M$ 接口适配灾难**。

```text
没有统一标准时 (所有模型都得为所有工具开发专属驱动):
Claude ──► Notion 驱动 | GPT ──► Notion 驱动 | Llama ──► Notion 驱动
Claude ──► GitHub 驱动 | GPT ──► GitHub 驱动 | Llama ──► GitHub 驱动
```

如果你有 $N$ 个大模型，外接 $M$ 个工具，开发者就不得不编写 $N \times M$ 个专属的连接器代码。

#### MCP 协议的诞生（大模型接口标准化）
Anthropic 联合社区推出了 **Model Context Protocol (模型上下文协议)**。它提供了一套标准化的中间适配协议。

```text
MCP 统一标准模式 (USB-C 接口):
Claude ──┐             ┌──► GitHub 适配服务
GPT    ──┼─► [ MCP ] ──┼──► Notion 适配服务
Llama  ──┘             └──► 本地文件系统适配服务
```

它就像是 AI 世界的 **USB-C 接口**。以前每个手机、相机都有自己的充电孔，现在统一用 USB-C。大模型（Client）和外部工具（Server）现在只需要遵循 MCP 规范编写，任何支持 MCP 的模型就可以零门槛、即插即用地调用任何支持 MCP 的外部数据源与工具。

#### 概念辨析：Function Calling vs. MCP vs. Agent
这三个概念非常容易被初学者混淆。它们在大模型应用架构中其实处于完全不同的层级：

```text
应用层 (Application Layer) ──► Agent (具备规划、记忆与持续循环控制的智能体系统)
       │
协议层 (Protocol Layer)    ──► MCP (大模型与工具/数据源交互的标准通信协议，即 USB-C)
       │
执行层 (Execution Layer)   ──► Function Calling (大模型输出结构化 JSON 参数的单次工具调用机制)
```

* **Function Calling (函数调用)**：最底层的**执行机制**。它是单次、原子的。大模型根据输入判定：“我需要调用 `get_weather(city='北京')`”，并返回标准的 JSON 参数。它本身并不真正运行工具，也不负责网络连接的管理。
* **MCP (Model Context Protocol)**：中间的**通信标准协议**。它是 AI 世界的 **USB-C 接口**。它统一规范了外部工具如何向模型声明自己拥有的功能，以及数据如何在模型与本地/云端工具之间安全传输。
* **Agent (智能体)**：最上层的**应用形态**。它是一个闭环的控制系统，包裹了大模型的大脑与 MCP 协议，通过规划、记忆、自我反思等机制，驱动一个持续运行的循环，直到完成复杂的长期目标。

---

MCP 标准化了模型可以使用的工具，但我们如何构建能够自主规划和执行动作的系统？在 [Agent 为什么不是 Prompt](09_agent_mechanics.md) 中了解更多。
