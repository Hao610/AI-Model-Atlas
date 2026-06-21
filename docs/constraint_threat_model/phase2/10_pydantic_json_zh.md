← 返回 [约束与威胁模型](../../CONSTRAINT_THREAT_MODEL_zh.md) | [English Version (10_pydantic_json.md)](10_pydantic_json.md)

---

# 🧱 第 10 章：使用 Pydantic 实现严格的输出约束

在构建依赖大型语言模型 (LLM) 的应用程序时，非结构化的文本响应往往是一个隐患。您需要代码能够可靠解析的、可预测的结构化数据，而 Pydantic 正是实现严格输出约束的终极执行者。

## 🏢 DMV (车管所) 类比

* **类比**： 解析 LLM 的输出就像在车管所 (DMV) 处理申请表格。
* **原理**： 如果给申请人一张白纸，只会得到格式混乱、信息缺失的申请。相反，车管所使用严格的表格，任何格式错误（如日期填了“上周二”）都会导致立刻拒收。
* **核心概念**： Pydantic 就像是对 LLM 极其严苛的表格——如果输出不能完美匹配您的数据模式，它会立刻抛出验证错误。

## 📊 快速对比

| 概念 | 传统方式 | LLM 时代 | 影响 |
|---------|-------------|---------|--------|
| **数据格式化** | 简单的提示词要求返回 JSON | 使用 Pydantic 类定义精确的模式 | 彻底消除对话式的填充词和字段遗漏。 |
| **类型检查** | 容易出错的字符串解析 | 原生的 Python 类型提示 (`int`, `bool`) | 帮助应用程序收到可用的数据类型。 |
| **错误处理** | 由于输出格式错误导致应用崩溃 | 将验证错误反馈给 LLM 并自动重试 | 将脆弱的 AI 集成转变为具备自愈能力的流水线。 |

## 🧠 核心概念

1. **定义模式**：创建一个 Pydantic `BaseModel`，详细说明所需数据的确切字段、类型和语义描述。
2. **注入模式**：该模式将被转换为 JSON Schema，并在请求时直接传递给 LLM API。
3. **强制输出**：部分提供商和框架可以引导 LLM 输出更符合模式的 JSON，但最终仍取决于模型和集成方式。
4. **验证与解析**：模型响应会被直接解析回您的 Python 对象，如有任何不合规就会快速报错拦截。

```python
from pydantic import BaseModel, Field

class UserProfile(BaseModel):
    name: str = Field(description="用户的全名")
    age: int = Field(description="用户的年龄（岁）")
    is_active: bool = Field(description="用户帐户是否处于活动状态")
    tags: list[str] = Field(description="与用户相关的兴趣或标签列表")
```

---

← [上一章](09_role_alignment_agent_zh.md) | [下一章](11_automated_self_corre_zh.md) →
