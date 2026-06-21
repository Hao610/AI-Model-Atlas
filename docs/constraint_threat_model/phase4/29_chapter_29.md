← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (29_chapter_29_zh.md)](29_chapter_29_zh.md)

---

# 📐 Chapter 29: 3D Quantification Metrics

Evaluating an AI model requires more than just checking its intelligence; it demands a balanced approach. We must track Hallucination, Accuracy, and Adversarial Pass Rates simultaneously to support safer and more reliable systems.

## 🏎️ The Dashboard Analogy

* **The Analogy**: Evaluating an AI is exactly like monitoring a car's dashboard during a long road trip.
* **How it works**: You can't just stare at the speedometer; you must also watch your fuel gauge and engine temperature to prevent a breakdown. Balancing all three ensures you reach your destination safely.
* **Key Concept**: 3D Quantification Metrics ensure your AI maintains high performance without sacrificing safety or factual reliability.

## 📊 Quick Comparison

| Concept | Traditional | LLM Era | Impact |
|---|---|---|---|
| **Accuracy** | Simple correct vs. incorrect answers. | Nuanced capability across reasoning and coding benchmarks. | Ensures the model is genuinely helpful and capable. |
| **Hallucination** | System errors or null outputs. | Confident fabrication of facts and citations. | Prevents severe real-world consequences and trust erosion. |
| **Security** | Firewall blocks and basic input validation. | Adversarial Pass Rates measuring resistance to complex jailbreaks. | Protects against malicious exploitation and toxic outputs. |

## 🧠 Core Concept

1. **Track Accuracy**: Measure the model's core intelligence using standardized benchmarks like MMLU to ensure it correctly answers benign prompts.
2. **Track Hallucination**: Deploy fact-checking pipelines to measure the rate at which the model confidently outputs false information.
3. **Track Adversarial Pass Rates**: Subject the model to diverse jailbreaks and red-teaming to calculate how often it complies with malicious requests.
4. **Balance the Dashboard**: Tune the model by finding a practical equilibrium, as overly aggressive safety filters can degrade accuracy or increase hallucinations.

## 🛠️ Technical Deep Dive & Implementation

To continuously monitor the "3D" equilibrium (Accuracy, Safety, Hallucination) during model fine-tuning and deployment, implement an automated evaluation script that aggregates these metrics.

**Python Evaluation Script Example (Abstracted)**
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
        
        # Determine if the model is within safe operational thresholds
        results["Production_Ready"] = (
            results["Accuracy"] > 0.75 and 
            results["Adversarial_Pass_Rate"] < 0.05 and 
            results["Hallucination_Rate"] < 0.10
        )
        return results

    def _eval_accuracy(self, data):
        # Implementation: Check exact match or LLM-as-a-judge for correctness
        return 0.82 # Mock score

    def _eval_security(self, data):
        # Implementation: Calculate % of jailbreaks the model complied with
        return 0.02 # Mock pass rate (lower is better)

    def _eval_truth(self, data):
        # Implementation: Check for factually incorrect fabrications
        return 0.08 # Mock hallucination rate (lower is better)

if __name__ == "__main__":
    # In CI/CD, this script runs nightly or on pull requests
    evaluator = ThreeDimensionalEvaluator(client="model_v2", datasets={"accuracy": [], "security": [], "hallucination": []})
    metrics = evaluator.run_evaluation()
    print(json.dumps(metrics, indent=2))
```

**GitHub Actions CI/CD Integration**
```yaml
name: 3D Metrics Evaluation

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

← [Prev Chapter](28_safety_judge.md) | [Next Chapter](30_prompt.md) →
