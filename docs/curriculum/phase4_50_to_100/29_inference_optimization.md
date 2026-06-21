# Inference Optimization 🏎️

[English] | [中文 (29_inference_optimization_zh.md)](29_inference_optimization_zh.md)

Running Large Language Models in production is not just about loading them onto a GPU. If you have 100 concurrent users hitting your API, you need to optimize how the GPU processes these requests. 

This guide covers the three pillars of **LLM Inference Optimization**: **KV Caching**, **Continuous Batching**, and **Streaming**.

---

## 💾 1. KV Caching (Key-Value Caching)

During inference, an LLM generates text one token at a time. To generate token #5, it must read tokens #1, #2, #3, and #4. Without optimization, the model would recompute the mathematical keys and values of the previous tokens *every single time* it generates a new word. This causes an $O(N^2)$ slowdown.

**KV Caching** solves this:
* As the model reads and generates tokens, it stores the computed keys and values of past tokens in GPU memory.
* For the next token, it only computes the math for the new token and fetches the past states from the cache.

*Tradeoff: KV Cache dramatically speeds up generation but consumes massive amounts of VRAM, limiting your batch size.*

---

## 📦 2. Continuous Batching

In traditional deep learning, you batch requests together. However, LLMs generate text dynamically. If User A asks for a 1-word answer, and User B asks for a 500-word essay, traditional batching would hold User A's GPU cores hostage until User B's essay is completely finished.

**Continuous Batching** (pioneered by engines like vLLM) resolves this:
* It operates at the **token level** rather than the request level.
* As soon as User A's 1-word answer is finished, that slot in the batch is immediately freed up and given to User C, even while User B's generation is still running.

```text
Traditional Batching:  [ User A (1 word)  ][ User B (500 words) ] ──► GPU waits for both
Continuous Batching:   [ User A (Done) -> User C starts         ] ──► GPU stays at 100%
```

---

## ⚡ 3. Streaming Output

To the user, the most important metric is **Time-To-First-Token (TTFT)** (how fast the first word appears on the screen).

* **Standard JSON Output**: The server waits for the model to finish generating the entire 500-word paragraph, then sends the whole payload over network HTTP. The user stares at a loading spinner for 10 seconds.
* **Streaming Output**: Using **Server-Sent Events (SSE)**, the server pushes each token to the client's browser *the microsecond* it is generated. The user sees the AI start "typing" instantly, creating a premium user experience even if the total generation takes time.

---

## 📊 Summary: Latency vs. Throughput

* **Latency**: How fast a single request is answered (optimized by KV Cache and streaming).
* **Throughput**: How many total requests the system can handle per minute (optimized by continuous batching and quantization).

---

🎉 **You have completed the optimization map!** You now have the full architectural picture of how to deploy and scale production AI systems.
