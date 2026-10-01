# API Integration Guide 🔑

> 📅 Last updated: 2026-10. AI ecosystems iterate rapidly; please refer to official documentation for the latest versions and pricing.

[English] | [中文 (15_api_guide_zh.md)](15_api_guide_zh.md)

An **API (Application Programming Interface)** is a bridge that lets your software talk directly to an LLM provider. Instead of using a web chat interface, your code sends a structured request and gets back a structured response.

This guide will show you how to set up and run your first Python script to call a model, plus how to incorporate System One decision gating.

---

## 🛠️ Step 1: Install Python & Libraries

Make sure you have Python installed. Then, open your terminal/command prompt and install the official OpenAI SDK (which is also used by DeepSeek and Qwen):

```bash
pip install openai pydantic
```

---

## 🔑 Step 2: Get Your API Key

1. Go to an LLM provider's developer console:
   * **OpenAI**: [platform.openai.com](https://platform.openai.com)
   * **DeepSeek**: [platform.deepseek.com](https://platform.deepseek.com)
2. Create an account, add credit, and generate a new **Secret Key** (looks like `sk-...`).
3. **Important**: Store this key securely in environment variables. Never upload it to GitHub!

---

## 🐍 Step 3: Write Your First Python script

Create a file named `chat.py` and write the following code:

```python
import os
from openai import OpenAI

# Initialize the client.
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY", "your_api_key_here")
)

# Call the model
response = client.chat.completions.create(
    model="gpt-4o-mini",  # For DeepSeek, use "deepseek-chat"
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain what an API key is in one sentence."}
    ],
    temperature=0.7
)

# Print the model's reply
print("AI Reply:")
print(response.choices[0].message.content)
```

---

## 🌐 How to Switch to DeepSeek API

The OpenAI SDK has become the industry standard. Most providers use the exact same formatting. To switch from OpenAI to DeepSeek, you only need to change the **API Key**, the **Base URL**, and the **Model Name**:

```python
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY", "your_deepseek_key_here"),
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-chat",  # DeepSeek-V3
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)
print(response.choices[0].message.content)
```

---

## ⚡ Modern 2026 Pattern: System One Decision Gating

In production, calling heavy LLMs for simple classification or safety checks wastes latency and budget. Modern architectures prepend a **System One decision gate** (like TypeSafe Jev) before calling generation APIs:

```python
from pydantic import BaseModel

# 1. Sub-100ms deterministic decision check (e.g. TypeSafe Jev or lightweight router)
# Only if query is classified as safe and requires generative reasoning:
# 2. Forward to deep LLM (OpenAI o1 / Claude 3.5 / DeepSeek-V3)
```

---

Now that you can call models in the cloud, let's learn how to run them for free on your own computer in [Local LLMs](17_local_llm.md).
