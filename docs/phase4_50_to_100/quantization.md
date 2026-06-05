# Model Quantization 📉

[English] | [中文 (quantization_zh.md)](quantization_zh.md)

Deploying Large Language Models in production is expensive. A model with 70 billion parameters (like `Llama-3-70B`) is stored in high-precision floats (16-bit floating-point numbers, or **FP16**). 

Running this model raw requires **140 gigabytes of Video RAM (VRAM)**. This means you would need to rent or buy two massive enterprise A100 GPUs just to load the model.

To solve this, we use **Model Quantization**.

---

## 🧠 What is Quantization?

Quantization is the process of compressing a model by lowering the mathematical precision of its weight coordinates.

Think of it like digital audio or images:
* **FP16 (High Resolution)**: A lossless, raw audio file (FLAC/WAV). Sounds perfect, but takes up massive disk space.
* **INT4 (Compressed)**: A high-quality MP3 file. The human ear can barely tell the difference, but the file size is **75% smaller**.

```text
    FP16 Precision (16-bit) ──► INT8 (8-bit) ──► INT4 (4-bit)
    [ 140GB VRAM Needed ]        [ 70GB VRAM ]    [ 40GB VRAM ]
```

By converting the model weights from 16-bit decimal numbers (`FP16`) to simple 4-bit integers (`INT4`), we compress the memory footprint by 4 times, with only a negligible loss in logical reasoning capability!

---

## 📦 Common Quantization Formats

When downloading local open weights models, you will encounter these main formats:

### 1. GGUF (Great for CPU / Local Running)
* **What it is**: Designed by the open-source community for CPU running.
* **Pros**: Allows "VRAM Offloading". If you have a model that needs 20GB of memory, but your GPU only has 8GB, GGUF can split the model, running 8GB on your graphics card and offloading the remaining 12GB to your computer's standard system RAM (CPU).
* **Best Used For**: Running models locally on consumer Macbooks, laptops, and PCs using **Ollama** or **LM Studio**.

### 2. AWQ / GPTQ (Great for GPU / Production Serving)
* **What it is**: Specialized formats optimized for hyper-fast inference on dedicated graphics cards (GPUs).
* **Pros**: Incredible execution speed.
* **Cons**: Does not support offloading to CPU RAM. The model must fit entirely inside your GPU memory.
* **Best Used For**: Production hosting servers running engines like **vLLM** or **TGI**.

---

## 📊 VRAM Estimation Rule of Thumb

How much memory do you need to run a quantized model? Use this simple mental formula:

$$\text{Required VRAM (in GB)} = (\text{Parameter Count in Billions}) \times \frac{\text{Quantization Bits}}{8} \times 1.2$$

*The $1.2$ factor adds a 20% safety buffer for the model's chat history memory (KV Cache).*

### Example: Running a 70B model at 4-bit quantization (INT4)
$$70 \times \frac{4}{8} \times 1.2 = 42\text{ GB of VRAM}$$

Instead of needing $140\text{ GB}$ of enterprise VRAM, you can run this model on two consumer **RTX 3090/4090** GPUs ($24\text{ GB} \times 2 = 48\text{ GB}$)!

---

Now that you know how to compress models to fit on consumer hardware, let's explore how to select the right GPU for your budget and goals in [GPU Selection Guide](gpu_selection.md).
