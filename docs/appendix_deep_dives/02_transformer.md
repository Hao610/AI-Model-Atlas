← Back to [Deep Dives Directory](../../DEEP_DIVES.md) | [English] | [中文 (02_transformer_zh.md)](02_transformer_zh.md)

---

# 02. Why Does Transformer Rule the World?
> **How Attention ended the sequential bottleneck of RNNs and ushered in the LLM revolution.**

Before 2017, natural language processing was dominated by **Recurrent Neural Networks (RNNs)** and **Long Short-Term Memory (LSTM)** networks. They read text the way humans do: word-by-word, sequentially from left to right.

```text
Sequential Reading (RNN/LSTM):
"The" ──► "quick" ──► "brown" ──► "fox" ──► "jumps" ...
```

#### The Sequential Bottleneck
Because RNNs had to process word $t$ before they could look at word $t+1$, they had two fatal flaws:
1. **Forgetfulness**: By the time an RNN read page 10 of a document, it had mathematically forgotten the details from page 1.
2. **Hardware Lock**: GPUs (which excel at doing thousands of mathematical operations at the exact same time) sat mostly idle because the network had to wait for the previous word to finish processing.

#### The Transformer Breakthrough (Attention Is All You Need)
In 2017, Google researchers proposed the **Transformer** architecture. Its core innovation was **Self-Attention**: instead of reading word-by-word, the Transformer reads the entire text block simultaneously.

```text
Parallel Attention (Transformer):
[ "The", "quick", "brown", "fox", "jumps" ] ──► Processed all at once!
```

Every word looks at every other word in the sentence at the exact same time, calculating a mathematical relationship score.
* **Why it changed history**: 
  1. It resolved the forgetfulness problem because long-distance relationships were computed in a single step.
  2. It allowed massive GPU parallelization. Training speeds skyrocketed, allowing models to be fed the entire public internet.
* **The Split Brain**:
  * **BERT (Encoder-only)**: Excels at understanding context by looking both left and right simultaneously. Perfect for classification and extraction.
  * **GPT (Decoder-only)**: Excels at "text auto-complete" by predicting the next most likely word. This became the foundation for modern conversational generative AI.

---

Now that you understand the Transformer, let's dive into how it turns text into coordinates in [What is Embedding under the Hood?](03_embedding.md).
