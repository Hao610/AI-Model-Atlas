# Hugging Face Guide 🤗

[English] | [中文 (huggingface_guide_zh.md)](huggingface_guide_zh.md)

If GitHub is the home for code, **Hugging Face** is the absolute home for Artificial Intelligence. It is where researchers, developers, and organizations host datasets, share model weights, and build interactive demos.

Understanding how to navigate Hugging Face is the first step to becoming an open-source AI practitioner.

---

## 🏛️ Key Concepts of Hugging Face

When you open [huggingface.co](https://huggingface.co), you will see three core categories:

1. **Models**: The actual files containing the trained synaptic weights of AI models (e.g. `meta-llama/Llama-3-8b-Instruct`).
2. **Datasets**: Collections of texts, images, or audio samples used to train or evaluate models.
3. **Spaces**: Interactive web applications hosted for free, allowing users to test models instantly on their browsers.

---

## 🆚 Understanding File Formats: Safetensors vs. GGUF vs. BIN

When downloading model weights from the **Files and versions** tab of a Hugging Face repo, you will see different file extensions. Here is what they mean:

| Extension | Format Name | Best Used For | Safety Level |
| :--- | :--- | :--- | :--- |
| **`.safetensors`** | Safetensors | Modern standard for PyTorch/GPU running. | 🔒 **High**: Stores only raw tensors. Zero risk of malicious code execution. |
| **`.gguf`** | GGUF (llama.cpp) | Running locally on CPU / consumer Macs. | 🔒 **High**: Optimized single-file format containing both weights and configuration. |
| **`.bin` / `.pt`** | Pickle (Legacy) | Older PyTorch models. | ⚠️ **Risk**: Can contain executable Python code. Never download `.bin` files from untrusted sources. |

---

## 📥 How to Download Models in Python

Instead of downloading huge gigabyte files manually on your browser, you can use the official `huggingface_hub` Python library to download models automatically:

```bash
pip install huggingface_hub
```

Here is a short script to download a model repository to your local cache:

```python
from huggingface_hub import snapshot_download

# Download the lightweight Qwen 0.5B model from Alibaba
model_path = snapshot_download(
    repo_id="Qwen/Qwen2.5-0.5B-Instruct",
    local_dir="./my_qwen_model"
)

print(f"Model downloaded successfully to: {model_path}")
```

---

Now that you can navigate the open-source registry, let's explore multimodal models that process images, audio, and video in [Multimodal AI](../phase2_1_to_10/multimodal_models.md).
