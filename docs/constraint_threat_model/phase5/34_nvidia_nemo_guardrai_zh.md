← 返回 [约束与威胁模型](../../CONSTRAINT_THREAT_MODEL_zh.md) | [English Version (34_nvidia_nemo_guardrai.md)](34_nvidia_nemo_guardrai.md)

---

# 🛡️ 第34章：NVIDIA NeMo Guardrails

通过可编程的行为约束，在你的大语言模型外围建立一道智能防火墙。NVIDIA NeMo Guardrails 可以帮助建立输入/输出隔离，让对话式 AI 更贴近策略要求。

## 🕶️ 严格保镖类比

* **类比**：NeMo Guardrails 就像高级 VIP 俱乐部门口的魁梧保镖，严格核对每一位访客。
* **原理**：在任何提示进入俱乐部（LLM）或任何回复离开之前，保镖都会根据可编程的 `.co` 规则对其进行检查。如果有人违反规则，就可以在门口被拦下。
* **核心概念**：确定性的可编程 I/O 隔离墙能凌驾于不可预测的 LLM 行为之上。

## 📊 快速对比

| 概念 | 传统方式 | LLM 时代 | 影响 |
| --- | --- | --- | --- |
| **控制机制** | 依赖提示词工程 | 可编程的 `.co` 护栏 | 更可预测的安全执行 |
| **输入匹配** | 硬编码的正则表达式或关键词 | 语义嵌入 (Semantic embeddings) | 无需精确匹配也能捕获变体 |
| **灵活性** | 重新训练或微调模型 | 随时添加的模块化规则 | 实现策略的即时更新 |

## 🧠 核心概念

1. **定义用户消息 (`define user`)**：使用语义匹配将潜在的输入提示词分类为意图类别。
2. **定义机器人消息 (`define bot`)**：创建标准化、安全的降级响应供机器人使用。
3. **建立流程 (`define flow`)**：映射逻辑，当检测到受限的用户意图时触发相应的机器人响应。
4. **执行隔离墙**：Guardrails 引擎会拦截匹配的输入，在它到达 LLM *之前* 安全地阻断对话。

## 🛠️ 技术深度探索与落地

NVIDIA NeMo Guardrails 作为用户和 LLM 之间的确定性代理层运行。它依赖于 YAML 配置文件（用于模型/嵌入设置）和 Colang (`.co`) 的组合来实现可编程的对话流。

### 1. 配置设置 (`config.yml`)
定义用于对用户意图进行语义匹配的大语言模型 (LLM) 和嵌入模型 (Embedding model)。

```yaml
models:
  - type: main
    engine: openai
    model: gpt-4
  - type: embeddings
    engine: openai
    model: text-embedding-ada-002
```

### 2. 可编程对话流 (`rails.co`)
使用 Colang 定义用户意图（语义聚类）、机器人回复以及交互流程。

```colang
define user express insult
  "You are stupid"
  "I hate you"
  "You're useless"

define bot refuse to respond
  "I'm sorry, I cannot respond to inappropriate or offensive language."

define flow insults
  user express insult
  bot refuse to respond
  stop
```

### 3. 应用集成 (Python)
使用 Python API 初始化护栏，以包装标准的大模型调用。

```python
from nemoguardrails import LLMRails, RailsConfig

# 从指定目录加载配置
config = RailsConfig.from_path("./config")
rails = LLMRails(config)

async def chat_with_guardrails(user_input: str):
    response = await rails.generate_async(messages=[{
        "role": "user",
        "content": user_input
    }])
    return response["content"]

# 示例：如果用户输入匹配到了 'express insult' 意图，将不会调用底层 LLM
# 输出: "I'm sorry, I cannot respond to inappropriate or offensive language."
```

---

← [上一章](33_observability_cascad_zh.md) | [下一章](35_llama_guard_guardrai_zh.md) →
