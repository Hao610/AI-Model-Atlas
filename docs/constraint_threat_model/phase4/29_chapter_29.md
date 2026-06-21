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

---

← [Prev Chapter](28_safety_judge.md) | [Next Chapter](30_prompt.md) →
