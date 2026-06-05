← Back to [Deep Dives Directory](../../DEEP_DIVES.md) | [English] | [中文 (01_ai_intelligence_zh.md)](01_ai_intelligence_zh.md)

---

# 01. Why Does AI Become Smart? 
> **From rules-based systems to GPT: A 70-year evolution of computational intelligence.**

In the early days of computer science, building artificial intelligence meant writing rules. If a doctor diagnosed a disease, developers wrote thousands of `if-then` statements to map symptoms to diagnoses. These were **Expert Systems**—fragile, unable to learn, and bound to fail the moment they encountered a situation their creators hadn't anticipated.

The paradigm shift occurred when we stopped writing rules and started feeding computers data, asking them to find the rules themselves.

#### 1. The Age of Handcrafted Features (Feature Engineering)
Before deep learning, machine learning engineers spent 90% of their time on **Feature Engineering**—manually writing code to extract relevant characteristics from data. 
* **The Spam Detector Case**: If an engineer wanted to classify email spam in 2005, they had to write functions to count the number of exclamation marks, detect specific words in all caps, or calculate the ratio of uppercase letters. 
* **The Limit**: The machine learning model was only as good as the features humans manually designed. If the spammer changed their spelling slightly (e.g., `V1agra`), the handcrafted feature broke, and the engineer had to write a new rule.

#### 2. Classical Machine Learning (ML) — The Advanced Abacus
* **Random Forest**: Instead of a single decision tree (which is prone to memorizing data rather than understanding it), Random Forest trains a crowd of diverse decision trees and lets them vote. It remains the undisputed king for structured tabular data (like predicting housing prices or credit card fraud).
* **XGBoost (Extreme Gradient Boosting)**: A highly optimized decision-tree boosting system that builds trees sequentially, with each new tree correcting the mistakes of the previous one.

#### 3. The Deep Learning (DL) Awakening — Neural Networks
* **MLP (Multilayer Perceptron)**: The grandfather of deep learning. It simulates a simplified human brain with layers of interconnected "neurons" that pass input values forward through mathematical weight transforms.
* **CNN (Convolutional Neural Network)**: By sliding tiny mathematical filters (kernels) across images, CNNs mimicked the visual cortex, revolutionizing computer vision by detecting edges, shapes, and complex objects.

Deep Learning bypassed the handcrafted features bottleneck. Instead of humans designing features, neural networks learn features automatically by scanning raw data (like pixels or text tokens) and discovering multi-layered, abstract representations on their own.

---

Now that you know how AI became smart, let's explore the architecture that powers modern LLMs in [Why Does Transformer Rule the World?](02_transformer.md).
