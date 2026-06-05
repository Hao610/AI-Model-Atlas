# LoRA Explained 🎨

[English] | [中文 (25_lora_explained_zh.md)](25_lora_explained_zh.md)

Fine-tuning a Large Language Model used to require modifying all of its billions of parameters. This is called **Full Fine-Tuning**, and it requires supercomputer clusters and millions of dollars.

To make fine-tuning accessible to everyone, researchers created **LoRA (Low-Rank Adaptation)**.

---

## 🖼️ The Photoshop Analogy: The Filter Layer

Imagine you have a beautiful high-resolution photograph (the **Base Model**). You want to adjust the colors to make it look like a vintage film photo (your **Fine-tuned style**).

* **Full Fine-Tuning**: You go into the photo and manually change the color code of every single pixel in the image. The original photo is overwritten, the file size remains huge, and it takes hours of manual work.
* **LoRA (Low-Rank Adaptation)**: Instead of touching the photo, you create a transparent **Filter Layer** (a layer mask) on top of the photo. You only paint your color changes on this thin layer. The original photo underneath is untouched. When you export, you combine the two.

```text
  [ Transparent Filter Layer (LoRA Adapter: 20MB) ]  <-- We only train this!
                      │
                      ▼ (Combined during use)
  [ Original High-Res Photo (Base Model Llama: 16GB) ] <-- Remains frozen!
```

---

## ⚡ Why LoRA is a Game-Changer

Because we freeze the base model and only train the thin adapter layer, we get massive benefits:

1. **Massive Hardware Savings**: Instead of needing 8 enterprise A100 GPUs, you can train a LoRA on a single consumer graphics card (like an RTX 3090 or 4090).
2. **Tiny File Sizes**: A full model file is usually **15GB to 140GB**. A LoRA adapter file is usually only **10MB to 100MB**.
3. **Instant Swapping**: Since the base model remains frozen, you can load Llama 3 once in memory, and swap different LoRAs instantly:
   * Load Llama 3 + *Marketing LoRA* (10MB) -> Writes emails.
   * Swap out and load Llama 3 + *Coder LoRA* (15MB) -> Writes code.
   * Swap out and load Llama 3 + *Legal LoRA* (20MB) -> Analyzes contracts.

---

## 📏 What is "Rank" (r)?

When configuring a LoRA, you will see a setting called **Rank (r)** (usually set to `8`, `16`, or `64`).
* **Rank** controls the width (complexity) of the adapter layer.
* A **lower rank (e.g., 8)** means the layer is very thin. It uses less VRAM memory, trains faster, but can only capture simple style adjustments.
* A **higher rank (e.g., 64)** means the layer is wider. It can capture more complex logic, but takes longer to train and uses more GPU memory.

---

Now that you know how LoRA works under the hood, let's look at the visual tool we use to train it without writing PyTorch code: [LLaMA-Factory Guide](26_llama_factory.md).
