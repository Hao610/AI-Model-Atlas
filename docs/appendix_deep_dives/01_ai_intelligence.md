← Back to [Deep Dives Directory](../../DEEP_DIVES.md) | [English] | [中文 (01_ai_intelligence_zh.md)](01_ai_intelligence_zh.md)

---

# 01. Why Does AI Become Smart? 
> **From rules-based systems to GPT: A 70-year evolution of computational intelligence.**

In the early days of computer science, building artificial intelligence meant writing rules. If a doctor diagnosed a disease, developers wrote thousands of `if-then` statements to map symptoms to diagnoses. These were **Expert Systems**—fragile, unable to learn, and bound to fail the moment they encountered a situation their creators hadn't anticipated.

The paradigm shift occurred when we stopped writing rules and started feeding computers data, asking them to find the rules themselves.

#### 1. Classical Machine Learning (ML) — The Advanced Abacus
* **Random Forest**: Instead of a single decision tree (which is prone to memorizing data rather than understanding it), Random Forest trains a crowd of diverse decision trees and lets them vote. It remains the undisputed king for structured tabular data (like predicting housing prices or credit card fraud).
* **XGBoost (Extreme Gradient Boosting)**: A highly optimized decision-tree boosting system that builds trees sequentially, with each new tree correcting the mistakes of the previous one.

#### 2. The Deep Learning (DL) Awakening — Neural Networks
* **MLP (Multilayer Perceptron)**: The grandfather of deep learning. It simulates a simplified human brain with layers of interconnected "neurons" that pass input values forward through mathematical weight transforms.
* **CNN (Convolutional Neural Network)**: By sliding tiny mathematical filters (kernels) across images, CNNs mimicked the visual cortex, revolutionizing computer vision by detecting edges, shapes, and complex objects.

---

Now that you know how AI became smart, let's explore the architecture that powers modern LLMs in [Why Does Transformer Rule the World?](02_transformer.md).
