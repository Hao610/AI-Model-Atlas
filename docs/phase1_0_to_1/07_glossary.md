# AI Vocabulary Glossary 📖

[English] | [中文 (07_glossary_zh.md)](07_glossary_zh.md)

Entering the AI field means learning a lot of jargon. Below is a beginner-friendly dictionary of the most critical terms you will encounter daily.

---

## 🔑 Key Vocabulary

### 1. Token
* **What it is**: The basic unit of data processed by LLMs. 
* **Analogy**: A token is not necessarily a full word. It is a "chunk" of characters. For example, the word `"preheating"` might be split into three tokens: `"pre"`, `"heat"`, and `"ing"`.
* **Rule of thumb**: In English, **100 tokens** is roughly equal to **75 words**. 

### 2. Context Window
* **What it is**: The maximum memory of the model in a single chat session.
* **Analogy**: Imagine a desk workspace. If a model has a 128k token context window, it can read and remember about 90,000 words (like a thick textbook) on its desk at once. If you feed it more than that, it will start forgetting the oldest messages.

### 3. Temperature
* **What it is**: A settings knob that controls the randomness/creativity of the model's output.
* **Range**: Usually between `0` and `2` (default is around `0.7`).
  * **Low Temperature (`0` to `0.2`)**: The model is highly analytical, conservative, and predictable. (Best for writing code, math, factual lookup).
  * **High Temperature (`0.9` to `1.5`)**: The model is creative, erratic, and unpredictable. (Best for brainstorming, creative writing, poetry).

### 4. Hallucination
* **What it is**: When an AI states a completely false claim with absolute confidence.
* **Analogy**: A confident student making up a history fact on a test to sound smart. Large Language Models generate text by predicting the *next most likely word*, which means they have no actual concept of "truth."

### 5. Parameters
* **What it is**: The size of the model's "brain." Usually represented with a **B** (e.g., Llama-3-8B has 8 Billion parameters).
* **Analogy**: The number of synpatic connections in the AI's virtual brain. Larger models (e.g., 70B, 405B) are much smarter and understand complex logic, but require massively expensive GPUs to run. Smaller models (e.g., 8B, 3B) are fast and can run on your laptop.

### 6. Inference vs. Training
* **Training**: The process of *teaching* the model using huge compute systems (like supercomputers). This costs millions of dollars.
* **Inference**: The process of *running* the model to get answers. When you ask ChatGPT a question and it types a reply, that is inference. This requires very little power compared to training.

---

Congratulations! You have completed **Phase 1 (0 to 1)**! You now speak the language of AI. 

Next, let's step into **Phase 2 (1 to 10)** and learn how models scale in [LLM Landscape](../phase2_1_to_10/08_llm_landscape.md).
