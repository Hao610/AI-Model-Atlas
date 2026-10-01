# Multimodal AI: Beyond Text 🎨🔊

> 📅 Last updated: 2026-10. AI ecosystems iterate rapidly; please refer to official documentation for the latest versions and pricing.

[English] | [中文 (10_multimodal_models_zh.md)](10_multimodal_models_zh.md)

Large Language Models (LLMs) process text. But humans interact with the world through vision, sound, and movement. **Multimodal AI** refers to models that can understand or generate multiple types of data (media) simultaneously.

Let's explore the three pillars of multimodal models: **Vision (VLM)**, **Image/Video Generation (Diffusion & Flow)**, and **Audio/Speech**.

---

## 👁️ 1. Vision-Language Models (VLMs)

* **What they do**: Read an image, diagram, UI screenshot, or video clip and answer questions about it (e.g. *"What is written on this receipt?"* or *"Analyze this architecture diagram"*).
* **How they work**: They combine a **Vision Encoder** (which translates image pixels into vectors) with a standard **LLM Decoder** (which reads those vectors as if they were text).
* **Major Models**:
  * **Closed**: GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro (native audio/video streaming).
  * **Open Weights**: **Qwen-2.5-VL (7B/72B)**, **Llama 3.2 Vision (11B/90B)**, **InternVL 2.5**.

---

## 🎨 2. Image & Video Generation (Diffusion & Flow)

Unlike VLMs which *understand* images, these models *create* them from text prompts.

```text
User Text Prompt ──► [ Diffusion Model / Denoising Process ] ──► High-Res Image
```

### Key Technologies:
* **Stable Diffusion & Flux.1 (Schnell / Dev)**: The reigning open-source image generation architectures with Flow Matching and high prompt adherence.
* **Kling 1.5, Runway Gen-3 Alpha, Sora, MiniMax Video**: Text-to-Video models. They model video frames as continuous 3D spatial-temporal patches, generating realistic movement, camera pans, and physical consistency.

---

## 🔊 3. Audio & Voice Models

These process human speech, music, or environmental sounds.

* **Automatic Speech Recognition (ASR)**: Converting spoken audio to text.
  * *Industry Standard*: **Whisper** (by OpenAI). It can transcribe dozens of languages and accents at near-human accuracy.
* **Text-to-Speech (TTS)**: Converting text into natural human voice.
  * *Industry Standard*: **ChatTTS**, **F5-TTS** (open models capable of matching emotional tones and breathing patterns).

---

Now that you understand how AI processes media, let's explore how we budget and calculate the token costs of these systems in [Token Economics & Cost Estimation](../phase3_10_to_50/16_cost_and_tokens.md).
