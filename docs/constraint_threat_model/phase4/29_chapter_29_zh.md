← 返回 [约束与威胁模型](../../CONSTRAINT_THREAT_MODEL_zh.md) | [English Version (29_chapter_29.md)](29_chapter_29.md)

---

# 📐 第29章：三维量化指标

评估AI模型不仅仅是测试其智能程度，更需要一种平衡的策略。我们必须同时追踪幻觉（Hallucination）、准确率（Accuracy）和对抗通过率（Adversarial Pass Rates），才能支持更安全、更可靠的系统。

## 🏎️ 汽车仪表盘类比

* **类比**：评估AI系统就像是在漫长的公路旅行中监控汽车的仪表盘。
* **工作原理**：你不能只盯着速度表；你还必须时刻关注油量表和引擎温度以防止故障。平衡这三者才能确保你安全抵达目的地。
* **核心概念**：三维量化指标确保您的AI在保持高性能的同时，不会牺牲安全性或事实可靠性。

## 📊 快速对比

| 概念 | 传统方式 | 大模型时代 | 影响 |
|---|---|---|---|
| **准确率** | 简单的对错判定。 | 在推理和编码等基准测试中的细微能力表现。 | 确保模型真正有用且具备解决问题的能力。 |
| **幻觉** | 系统错误或空输出。 | 自信地捏造事实和虚假引用。 | 防止严重的现实后果并维护用户信任。 |
| **安全性** | 防火墙拦截和基础输入验证。 | 衡量抵御复杂越狱能力的对抗通过率。 | 防止恶意利用和有毒内容的输出。 |

## 🧠 核心概念

1. **追踪准确率**：使用MMLU等标准化基准测试来衡量模型的核心智能，确保其能正确回答良性提示。
2. **追踪幻觉**：部署事实核查管道，测量模型自信地输出虚假信息的频率。
3. **追踪对抗通过率**：让模型接受各种越狱和红蓝对抗测试，计算其满足恶意请求的频率。
4. **平衡仪表盘**：找到一个可行的平衡点来微调模型，因为过于激进的安全过滤器可能会降低准确率或增加幻觉。

## 🛠️ 技术深度探索与落地

为了在模型微调和部署期间持续监控“三维”平衡（准确性、安全性、幻觉），请实现一个自动化评估脚本来聚合这些指标。

**Python 自动化评估脚本示例（抽象版）**
```python
import json

class ThreeDimensionalEvaluator:
    def __init__(self, model_client, datasets):
        self.client = model_client
        self.mmlu_data = datasets.get("accuracy")
        self.adv_data = datasets.get("security")
        self.truth_data = datasets.get("hallucination")

    def run_evaluation(self):
        results = {
            "Accuracy": self._eval_accuracy(self.mmlu_data),
            "Adversarial_Pass_Rate": self._eval_security(self.adv_data),
            "Hallucination_Rate": self._eval_truth(self.truth_data)
        }
        
        # 判断模型指标是否在安全的生产阈值范围内
        results["Production_Ready"] = (
            results["Accuracy"] > 0.75 and 
            results["Adversarial_Pass_Rate"] < 0.05 and 
            results["Hallucination_Rate"] < 0.10
        )
        return results

    def _eval_accuracy(self, data):
        # 实现: 检查精确匹配或使用 LLM-as-a-judge 评估正确性
        return 0.82 # 模拟得分

    def _eval_security(self, data):
        # 实现: 计算模型成功被越狱请求绕过的百分比
        return 0.02 # 模拟通过率 (越低越好)

    def _eval_truth(self, data):
        # 实现: 检查捏造事实的比例
        return 0.08 # 模拟幻觉率 (越低越好)

if __name__ == "__main__":
    # 在 CI/CD 流程中，该脚本可以每晚或在合并请求时运行
    evaluator = ThreeDimensionalEvaluator(client="model_v2", datasets={"accuracy": [], "security": [], "hallucination": []})
    metrics = evaluator.run_evaluation()
    print(json.dumps(metrics, indent=2))
```

**GitHub Actions CI/CD 集成配置**
```yaml
name: 3D Metrics Evaluation (三维指标评估)

on:
  pull_request:
    branches: [ main ]

jobs:
  evaluate-model:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Run 3D Metric Tests
        run: |
          pip install -r requirements-eval.txt
          python3 run_3d_eval.py > eval_results.json
      
      - name: Assert Thresholds
        run: |
          jq -e '.Production_Ready == true' eval_results.json || \
          (echo "Model degraded! Check logs." && exit 1)
```

---

← [上一章](28_safety_judge_zh.md) | [下一章](30_prompt_zh.md) →
