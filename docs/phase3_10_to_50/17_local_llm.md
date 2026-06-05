# Local LLM Runner 🖥️

[English] | [中文 (17_local_llm_zh.md)](17_local_llm_zh.md)

What if you have no internet access, want 100% data privacy, or don't want to pay API fees? You can run Large Language Models directly on your own computer.

Thanks to modern open-weights software, running models locally is now as easy as double-clicking an installer.

---

## 🏎️ Tool 1: Ollama (Command Line Champion)

**Ollama** is the most popular tool to run models locally. It runs as a light background service and exposes a local API server.

### 1. Installation & First Run
1. Download Ollama from [ollama.com](https://ollama.com) and install it.
2. Open your terminal/command prompt and run:
   ```bash
   ollama run llama3.2:3b
   ```
3. Ollama will download the model file (about 2GB) and start an interactive chat session inside your terminal.

### 2. Common Ollama Commands

| Command | Action |
| :--- | :--- |
| `ollama run <model>` | Pull and start chatting with a model. |
| `ollama pull <model>` | Download a model without running it. |
| `ollama list` | List all models installed on your machine. |
| `ollama rm <model>` | Delete a model to free up disk space. |

---

## 🎨 Tool 2: LM Studio (Visual & GUI Native)

If you hate command lines and want a beautiful, ChatGPT-like interface that runs locally, **LM Studio** is your best choice.

1. Download and install it from [lmstudio.ai](https://lmstudio.ai).
2. Open the app, search for **"Llama 3.2"** or **"DeepSeek-R1-Distill"** in the built-in store, and click **Download**.
3. Go to the Chat panel, select your downloaded model from the dropdown at the top, and start chatting!
4. **Local Server Mode**: You can toggle a switch in LM Studio to start a local server at `http://localhost:1234`. This server is 100% compatible with the OpenAI API format!

---

## 🐍 Connecting Python Code to Local Models

If you run Ollama, it automatically hosts a local API at `http://localhost:11434/v1`. You can redirect your Python code to query your own computer instead of OpenAI's servers:

```python
from openai import OpenAI

# Point client to your local Ollama server
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # Ollama doesn't require a real key
)

response = client.chat.completions.create(
    model="llama3.2:3b",
    messages=[
        {"role": "user", "content": "Why is the sky blue?"}
    ]
)

print(response.choices[0].message.content)
```

---

Now that you have your backend running locally or in the cloud, let's build a beautiful web UI for it in [UI Interfaces](18_ui_interfaces.md).
