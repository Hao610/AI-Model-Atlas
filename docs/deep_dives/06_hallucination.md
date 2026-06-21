← Back to [Deep Dives Directory](../DEEP_DIVES.md) | [English] | [中文 (06_hallucination_zh.md)](06_hallucination_zh.md)

---

# 06. Why Do Large Models Hallucinate?
> **Understanding the probabilistic nature of language generation and why RAG acts as an anchor.**

Large language models do not possess an internal database of facts. At their core, they are **probabilistic text completion engines**. 

```text
Text Completion Probability:
"The sky is..." ──► blue (94%) | cloudy (4%) | green (0.1%)
```

#### The Root Cause of Hallucination
When an LLM generates text, it calculates the probability distribution of the next token based on all previous tokens. It has no mechanism to verify if the statement is true; it only knows if the sentence *sounds* linguistically correct and natural based on its training distribution. 

If the model lacks information on a topic, it will still pick the most plausible-sounding next words, creating a highly convincing lie. This is **Hallucination**.

#### How RAG Prevents Hallucination
RAG acts as a physical anchor for the model. By injecting verified, factual source texts directly into the prompt context, we shift the model's task from **generation from memory** to **reading comprehension**. The model is constrained to use only the provided context, reducing hallucination rates to near zero for structured retrieval pipelines.

#### The Statistical Reality: Hallucinations Can Never Be 100% Eliminated
It is crucial to understand that no matter how advanced LLMs become (even future models like GPT-8), **hallucinations can never be completely eliminated**. 
* **Why**: LLMs are mathematical, probabilistic engines ($P(\text{word } n | \text{words } 1 \dots n-1)$). They do not reference a deterministic database of facts. 
* **The Implication**: There is always a non-zero probability that the model will select a statistically fluent but factually incorrect token combination. RAG drastically reduces the error rate, but engineers must design systems with validation checks, guardrails, and human-in-the-loop validation for critical applications.

---

To anchor our models, we give them reference text. But how much can they actually remember? Let's check in [Context Windows and the Needle in a Haystack Test](07_needle_test.md).
