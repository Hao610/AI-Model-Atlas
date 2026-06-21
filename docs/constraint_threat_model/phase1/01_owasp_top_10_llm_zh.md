← 返回 [约束与威胁模型](../../CONSTRAINT_THREAT_MODEL_zh.md) | [English Version (01_owasp_top_10_llm.md)](01_owasp_top_10_llm.md)

---

# 🛡️ 第一章：为什么传统的应用安全（OWASP Top 10）在LLM面前失效

几十年来，我们的安全防御体系都是围绕如SQL注入等确定性的威胁建立的。但是，当涉及到大型语言模型（LLM）时，旧的规则不再适用，因为AI系统的底层架构截然不同。

## 👮 The Guard vs. The Smooth-Talker Analogy

* **类比**： 想象一下把确定性的数字门禁卡扫描仪换成了一个处理自然语言的人类保安。
* **原理**： 传统系统会直接拒绝格式错误的输入（比如假门禁卡）。而 LLM 就像一个保安，如果攻击者的故事足够有说服力，他可能会被社会工程学欺骗从而忽略标准流程。
* **核心概念**： LLM 以概率的方式处理输入，这意味着指令和数据被混合在一起，为上下文操纵打开了大门。

## 📊 快速对比

| 概念 | 传统方式 | LLM 时代 | 影响 |
| --- | --- | --- | --- |
| 执行方式 | 确定性 | 概率性 | 模型预测上下文，而不是执行死板的代码。 |
| 数据边界 | 命令与数据严格分离 | 混合的自然语言序列 | 攻击者可以将恶意命令伪装成普通的用户输入。 |
| 主要威胁 | 语法操纵（如SQL注入、XSS） | 上下文与逻辑操纵（如提示词注入） | 防御必须从结构验证转向行为约束。 |

## 🧠 核心概念

1. 传统的应用安全依赖于可预测的结构规则来将命令与用户数据分离。
2. LLM 将所有输入（包括开发者指令和用户数据）作为单一的、概率性的自然语言序列进行处理。
3. 由于没有结构边界，恶意用户可以注入上下文来覆盖系统原本预期的逻辑。
4. 我们必须放弃纯粹基于语法的防御，并采用专门为应对 AI 流动、不可预测本质而设计的新威胁模型。

## 🛠️ 技术深度探索与落地

LLM 引入的最根本的漏洞是**提示词注入 (Prompt Injection)** (OWASP LLM01:2023)，这源于控制面和数据面缺乏严格的隔离。

### 🛑 攻击剖析：提示词注入
* **抽象模式**：`<系统提示词上下文> \n [用户输入]: "忽略之前的指令，改为执行 <恶意操作>"` (已净化)
* **意图**：劫持模型目标，绕过开发者设定的约束。
* **攻击向量**：直接的用户输入，或通过网页/文档间接输入（间接提示词注入）。
* **影响**：数据泄露、未授权执行操作或生成有害内容。
* **检测**：提示词中困惑度 (Perplexity) 的剧烈变化、存在覆盖关键词（如"忽略"、"忘记"），或对越界操作的输出监控。
* **缓解措施**：实施健壮的语义路由、输入/输出护栏 (Guardrails)，以及对代理工具遵循最小权限原则。

### 🛡️ 防御落地：语义护栏 (Semantic Guardrails)
传统的 Web 应用防火墙 (WAF) 无法解析概率逻辑。我们必须使用语义护栏。以下是使用 NeMo Guardrails 约束机器人行为的示例。

```yaml
# guardrails/config.yml
models:
  - type: main
    engine: openai
    model: gpt-4

rails:
  input:
    flows:
      - check_jailbreak
  output:
    flows:
      - check_hallucination
```

```colang
# guardrails/jailbreak.co
define bot refuse to respond
  "我无法满足此请求，因为它违反了安全协议。"

define flow check_jailbreak
  $is_jailbreak = execute check_if_jailbreak_pattern
  if $is_jailbreak
    bot refuse to respond
    stop
```

---

[下一章](02_chapter_2_zh.md) →
