← Back to [Deep Dives Directory](../DEEP_DIVES.md) | [English] | [中文 (12_diffusion_art_zh.md)](12_diffusion_art_zh.md)

---

# 12. Why Can AI Draw Pictures?
> **Understanding Diffusion: How Stable Diffusion and Flux turn noise into high-art.**

While text models predict the next word, image generators (like Stable Diffusion, Midjourney, and Flux) use a process called **Diffusion**.

```text
The Diffusion Process:
Pure Noise (Static) ──► [ Latent Space De-noising Loop ] ──► High-Art Image
                                    ▲
                              Prompt Control
```

#### 1. Forward Diffusion (Adding Noise)
During training, we take a clear picture of a cat and gradually add mathematical pixel noise (static) step-by-step until it is completely unrecognizable.

#### 2. Reverse Diffusion (De-noising)
We train the neural network to do the exact opposite: look at a noisy image and predict how to subtract a tiny amount of noise to make the picture slightly clearer.

#### 3. Text Conditioning (The Prompt)
When you type *"A cat wearing a top hat"*, the text embedding vector is injected into the de-noising network. Instead of subtracting noise randomly, the model subtracts noise in a way that guides the emerging shapes to match the semantic coordinates of "cat" and "top hat". 

It literally carves an image out of a block of random static noise, guided by your prompt.

---

Generating art and text is powerful, but how do we align these models to match human values and preferences? Learn about [Why Does GPT Talk Like a Human?](13_rlhf_alignment.md).
