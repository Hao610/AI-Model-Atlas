# Cloud Deployment 🚀

[English] | [中文 (31_deployment_zh.md)](31_deployment_zh.md)

Once you have fine-tuned your model and verified its quality, the final step is to host it in the cloud. This allows other applications, websites, and clients to send questions to it over the internet.

For production, developers use **vLLM**, a high-performance open-source model-serving engine.

---

## ⚡ Why vLLM?

Traditional tools like Ollama are designed for single-user offline running. If 100 users hit Ollama at the same time, it will lag and freeze.

**vLLM** uses a technique called **PagedAttention** (which handles memory the way operating systems do). It allows a single GPU to serve dozens of users simultaneously at hyper-fast speeds.

---

## 🛠️ Step-by-Step Cloud Deployment (e.g. on RunPod)

Here is the blueprint for serving `Qwen2.5-7B-Instruct` on a rented cloud GPU:

### 1. Rent a GPU
1. Go to [RunPod.io](https://runpod.io) or [AutoDL.com](https://www.autodl.com).
2. Deploy a pod with **1x RTX 4090** (24GB VRAM) or **1x A10G** (24GB VRAM).
3. Select the official **PyTorch** template.
4. Launch the pod and connect to it via SSH or Jupyter Lab.

### 2. Install vLLM
In your cloud GPU terminal, run:

```bash
pip install vllm
```

### 3. Launch the Server
Start the server using vLLM's OpenAI-compatible API wrapper. vLLM will automatically download the model from Hugging Face and load it into your GPU:

```bash
python -m vllm.entrypoints.openai.api_server \
    --model Qwen/Qwen2.5-7B-Instruct \
    --port 8000 \
    --host 0.0.0.0
```

*Note: Your API server is now running on port `8000`.*

---

## 🔗 How to Connect from Your Frontend App

Now, you can edit your local Python script or Streamlit app to point to your new cloud server's public IP address:

```python
from openai import OpenAI

# Connect to your cloud GPU server IP
client = OpenAI(
    base_url="http://your-cloud-ip:8000/v1",
    api_key="not-needed-for-private-server"
)

response = client.chat.completions.create(
    model="Qwen/Qwen2.5-7B-Instruct",
    messages=[
        {"role": "user", "content": "Hello! Give me a tagline for a coffee shop."}
    ]
)

print(response.choices[0].message.content)
```

---

🎉 **Congratulations! You have completed the AI-Model-Atlas!**

You went from learning basic definitions all the way to cloud GPU deployment. You now have the full context needed to build, fine-tune, and run custom AI systems. Bookmark this atlas, and use it as your personal tech dictionary. Good luck on your AI journey!
