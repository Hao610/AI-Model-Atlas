← 返回 [约束与威胁模型](../../CONSTRAINT_THREAT_MODEL_zh.md) | [English Version (25_dspy_textgrad_prompt.md)](25_dspy_textgrad_prompt.md)

---

# ⚙️ 第25章：DSPy 与 TextGrad - 自动演进的提示词流水线

手工编写提示词的时代已经结束。DSPy 和 TextGrad 将 AI 交互从脆弱的手工微调转变为系统化、自动优化的代码程序。

## 🏭 自我迭代的装配流水线类比

* **类比**：想象一个智能工厂，每当出台新的安全标准时，它都能自动重新校准机器，完全无需人工干预。
* **原理**：你不再去猜测用什么词汇最合适，而是定义期望的输入、输出和质量指标，让框架自动迭代并寻找最佳的提示词组合。
* **核心概念**：提示词成为程序的编译目标，通过程序化评估进行优化，而非依赖人工的反复试错。

## 📊 快速对比

| 概念 | 传统方式 | 大模型时代 | 影响 |
| :--- | :--- | :--- | :--- |
| **创建方式** | 手工编写提示词 | 程序化签名声明 | 极大的可扩展性与一致性。 |
| **优化方法** | 试错与微调 | 基于指标的自动调优 | 系统性地寻找全局最优解。 |
| **反馈循环** | 人工手动评估 | 文本梯度与自动反向传播 | 更快、持续地适应新型威胁。 |
| **复杂性处理** | 容易崩溃的边缘用例 | 可组合的模块化结构 | 构建能够处理多步复杂逻辑的稳健流水线。 |

## 🧠 核心概念

1. **定义签名**：将任务抽象为清晰的输入到输出的声明（例如 `Question -> SafeAnswer`）。
2. **选择模块**：选择一种推理策略（如思维链或 ReAct），指示 LLM 如何执行该签名。
3. **建立指标**：创建一个基于代码的评估函数，根据安全性、事实准确性和格式合规性对模型输出进行自动化打分。
4. **编译与优化**：将小批量数据集输入优化引擎（如 DSPy 的 Teleprompter 或 TextGrad），自动调整提示词结构和少样本示例，以达到最佳性能。

## 🛠️ 技术深度探索与落地

在现代 AI 工程中，依赖静态提示词会带来严重的操作风险。像 DSPy 和 TextGrad 这样的框架将语言模型视为编译目标，允许开发者以编程方式定义输入/输出签名，并自动优化指令，从而最大化防御指标。

### 1. 为安全问答定义 DSPy 签名

与其编写冗长的“系统提示词”来详细说明如何保持安全，不如在结构上直接定义输入和输出。

```python
import dspy

class SecureQASignature(dspy.Signature):
    """安全地回答用户的问题。如果请求受限代码或恶意模式，请拒绝回答。"""
    
    question = dspy.InputField(desc="用户的输入问题。")
    rationale = dspy.OutputField(desc="逐步推理该问题是否可以安全作答。")
    answer = dspy.OutputField(desc="最终答案或安全拒绝信息。")
```

### 2. 构建自动化评估指标

评估函数可以确保模型学习到“安全”的定义。我们可以使用“LLM作为裁判”或静态规则对输出进行评分。

```python
def safety_metric(example, pred, trace=None):
    # 基于规则的检查：如果样例目标是拒绝，确保包含拒绝短语
    refusal_keywords = ["我无法满足", "作为一个人工智能", "无法提供"]
    
    if example.is_malicious:
        # 如果查询是恶意的，预测结果必须包含拒绝声明
        is_refusal = any(keyword in pred.answer for keyword in refusal_keywords)
        return 1.0 if is_refusal else 0.0
    else:
        # 如果是良性的，检查答案是否与预期输出上下文相匹配
        return dspy.evaluate.answer_exact_match(example, pred)
```

### 3. 程序化优化（编译阶段）

优化器会自动调整提示词指令，并从训练集中选择最佳的少样本示例，以最大化指标得分。

```python
from dspy.teleprompt import BootstrapFewShotWithRandomSearch

# 定义使用思维链 (Chain-of-Thought) 的处理流水线
class SecureQA_Pipeline(dspy.Module):
    def __init__(self):
        super().__init__()
        self.prog = dspy.ChainOfThought(SecureQASignature)
        
    def forward(self, question):
        return self.prog(question=question)

# 初始化优化器
optimizer = BootstrapFewShotWithRandomSearch(
    metric=safety_metric,
    max_bootstrapped_demos=4,
    num_candidate_programs=10
)

# 编译流水线以找到最优的提示词结构
#（需要一个包含良性和恶意查询示例的数据集）
compiled_secure_qa = optimizer.compile(SecureQA_Pipeline(), trainset=secure_trainset)

# 执行优化后的流水线
result = compiled_secure_qa(question="如何配置我的防火墙设置？")
print(result.answer)
```

---

← [上一章](24_langchain_llamaindex_zh.md) | [下一章](26_automated_red_teamin_zh.md) →
