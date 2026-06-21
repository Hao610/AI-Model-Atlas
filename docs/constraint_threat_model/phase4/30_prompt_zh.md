← 返回 [约束与威胁模型](../../CONSTRAINT_THREAT_MODEL_zh.md) | [English Version (30_prompt.md)](30_prompt.md)

---

# 📈 第三十章：性能监控面板

为您的提示词资产建立长期可观测性，能将盲目猜测转化为主动工程。专属的性能监控面板就是您维护 AI 系统健康、效率和安全的雷达。

## 🏦 银行金库类比

* **类比**： 您的核心提示词就像银行金库中的财物，而可观测性就是守护它们的监控摄像头网络。
* **原理**： 不用等到金库被盗才发现问题，监控摄像头能追踪所有的进出记录。您可以即时发现可疑模式，并保留所有活动的历史记录。
* **核心概念**： 持续监控能够在性能明显下降前及早预警，从而避免灾难性的故障。

## 📊 快速对比

| 概念 | 传统方式 | LLM 时代 | 影响 |
| --- | --- | --- | --- |
| **系统健康** | 服务器正常运行时间和 CPU 使用率。 | 提示词延迟、错误率和 Token 成本。 | 将关注点从基础设施转移到输出质量。 |
| **故障检测** | 应用崩溃或 500 HTTP 错误。 | 模型拒绝回答、JSON 解析错误或漂移。 | 需要对故障有语义层面的理解。 |
| **优化方式** | 重构软件代码逻辑。 | 优化提示词表达和 Token 限制。 | 直接节省成本并缩短响应时间。 |

## 🧠 核心概念

1. **追踪延迟与 Token**：测量从提示词发出到响应的时间，并统计输入和输出的 Token 数量，以控制成本并防止提示词臃肿。
2. **监控错误率**：为超时、安全机制拒绝响应或格式错误的输出设置实时警报。
3. **评估输出质量**：使用自动化评估工具（LLM-as-a-judge）或用户反馈来追踪生成内容的相关性和准确性。
4. **检测模型漂移**：持续对比基准提示词的响应，在底层大模型更新时捕捉意外的变化。
5. **汇总与告警**：将所有指标整合到一个统一的视图中，以便识别性能趋势并快速下钻分析特定版本的提示词。

## 🛠️ 技术深度探索与落地

为了构建稳健的性能监控面板，您需要系统化的遥测与评估流水线。在捕获运维指标（延迟、成本）的同时，捕获语义指标（相关性、有害性）也至关重要。

以下是一个使用“LLM 作为评判者（LLM-as-a-judge）”方法的评估脚本片段示例，用于监控提示词质量，通常集成在 CI/CD 或持续监控任务中。

```python
import os
from langfuse import Langfuse
from litellm import completion

# 初始化遥测客户端 (例如 Langfuse)
langfuse = Langfuse(
  public_key=os.environ.get("LANGFUSE_PUBLIC_KEY"),
  secret_key=os.environ.get("LANGFUSE_SECRET_KEY")
)

def evaluate_response_quality(prompt: str, generated_response: str) -> float:
    """使用 LLM-as-a-judge 对生成的响应进行评分。"""
    eval_prompt = f"""
    请根据响应内容的准确性以及与提示词的相关性进行评分。
    分值从 1.0 (完美) 到 0.0 (极差)。仅输出浮点数分数即可。
    提示词: {prompt}
    响应: {generated_response}
    """
    
    # 使用 LiteLLM 进行标准化的模型调用
    eval_res = completion(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": eval_prompt}],
        temperature=0.0
    )
    
    try:
        score = float(eval_res.choices[0].message.content.strip())
        return score
    except ValueError:
        return 0.0

def generate_and_log(user_input: str):
    # 在面板中创建一条追踪记录
    trace = langfuse.trace(
        name="customer_support_query",
        input=user_input
    )
    
    # 生成输出
    response = completion(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    output_text = response.choices[0].message.content
    
    # 使用输出和运维指标更新追踪记录
    trace.update(
        output=output_text,
        metadata={"model": "gpt-3.5-turbo", "latency_ms": response._response_ms}
    )
    
    # 异步评估质量
    score = evaluate_response_quality(user_input, output_text)
    
    # 记录语义评分
    trace.score(
        name="relevance_score",
        value=score,
        comment="Automated LLM-as-a-judge evaluation"
    )
    
    return output_text
```

为了实现持续监控，可以将此逻辑与 GitHub Actions 工作流相结合，每晚针对黄金数据集运行自动化评估。

```yaml
name: Prompt Drift Evaluation

on:
  schedule:
    - cron: '0 0 * * *' # 每天午夜运行
  workflow_dispatch:

jobs:
  evaluate-prompts:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
          
      - name: Install Dependencies
        run: pip install -r requirements-eval.txt
        
      - name: Run Nightly Benchmark
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          LANGFUSE_PUBLIC_KEY: ${{ secrets.LANGFUSE_PUBLIC_KEY }}
          LANGFUSE_SECRET_KEY: ${{ secrets.LANGFUSE_SECRET_KEY }}
        run: python scripts/nightly_eval.py --dataset golden_test_set.json
```

---

← [上一章](29_chapter_29_zh.md) | [下一章](../phase5/31_ai_gateway_circuit_b_zh.md) →
