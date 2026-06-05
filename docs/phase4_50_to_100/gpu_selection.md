# GPU Selection Guide 🖥️

[English] | [中文 (gpu_selection_zh.md)](gpu_selection_zh.md)

When running, serving, or fine-tuning local models, the most critical piece of hardware is the **GPU (Graphics Processing Unit)**. Specifically, we care about **VRAM (Video RAM)**, which is the physical memory inside the GPU that holds the model.

If your model is bigger than your VRAM, it will either crash or run painfully slow on your CPU.

Here is your hardware guide for choosing the right card for your goals and budget.

---

## 🆚 GPU Directory: Consumer vs. Enterprise

| GPU Model | Class | VRAM Size | Best Used For | VRAM Speed | Approx. Value |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **RTX 4060 Ti (16GB)** | Consumer | 16 GB | **Budget local running**: Best price-to-VRAM ratio for hobbyists starting out. | Slow (128-bit bus) | Low |
| **RTX 3090 / 4090** | Consumer | 24 GB | **Developer Sweet-Spot**: Running 8B/14B models at full speed, LoRA training. | Fast | Mid-High |
| **RTX 5090** | Consumer | 32 GB | **Next-Gen Powerhouse**: Running 32B models locally or complex multi-LoRA pipelines. | Very Fast | High |
| **Mac Studio (M2/M3 Ultra)** | Unified Memory | Up to 192 GB | **Ultra-large inference**: Running massive 70B/405B models locally on a single desktop (acts as system+GPU RAM). | Medium (Shared memory) | High |
| **Nvidia A100 / H100** | Enterprise | 80 GB | **Heavy cloud fine-tuning & pre-training**: Renting on clusters to train multi-billion parameter models. | Hyper-Fast (HBM3) | Extreme |

---

## 🚦 Hardware Decision Guide

### Scenario 1: "I want a cheap local playground on my desktop"
* **Recommendation**: Buy a used **RTX 3090 (24GB)** or a new **RTX 4060 Ti (16GB)**.
* **Why**: The RTX 3090 has the same 24GB VRAM capacity as the newer 4090 but costs a fraction of the price. 24GB allows you to run `Llama-3-8B` at 16-bit precision, or `Qwen-2.5-32B` at 4-bit quantization.

### Scenario 2: "I want to fine-tune a model on my custom dataset"
* **Recommendation**: Rent GPUs on the cloud (e.g. **AutoDL** or **RunPod**).
* **Why**: Buying H100 or A100 cards costs tens of thousands of dollars. Renting a single **A100 (80GB)** costs around $1.50 to $2.00 per hour. You can upload your data, run your training run in 4 hours, pay $8, and download your finished 20MB LoRA adapter.

### Scenario 3: "I need to serve a model to thousands of active users"
* **Recommendation**: Set up a cloud instance running **A10G (24GB)** or **L4 (24GB)** cards.
* **Why**: These are server-grade cards designed to run 24/7 in data centers, making them highly reliable for hosting API engines like vLLM.

---

Now that you know how to choose your hardware, let's explore why models refuse to answer certain prompts and how safety systems are built in [Safety & Alignment](safety_alignment.md).
