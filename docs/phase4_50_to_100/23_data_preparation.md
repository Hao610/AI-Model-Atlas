# Data Preparation & Synthetic Data 📂

[English] | [中文 (23_data_preparation_zh.md)](23_data_preparation_zh.md)

In machine learning, there is a golden rule: **"Garbage In, Garbage Out."** No matter how advanced your GPU is or how high your learning rate is, if you feed your model messy, repetitive, or incorrect data, the fine-tuned model will perform poorly.

This guide explains how to prepare, clean, and format your datasets, and how to use larger models to generate synthetic training data.

---

## 📄 1. The Standard Formats: JSON vs. JSONL

For language models, training data is typically structured as a list of conversation turns.

### JSON Format
An array of objects (best for small datasets under 1,000 samples).
```json
[
  {"instruction": "Q1", "input": "", "output": "A1"},
  {"instruction": "Q2", "input": "", "output": "A2"}
]
```

### JSONL Format (JSON Lines)
Each line of the file is a separate, valid JSON object (best for large datasets). It is memory efficient because loaders can read the file line-by-line without loading the entire gigabyte-sized file into memory.
```jsonl
{"instruction": "Q1", "input": "", "output": "A1"}
{"instruction": "Q2", "input": "", "output": "A2"}
```

---

## 🧼 2. The Data Cleaning Checklist

Before starting LLaMA-Factory, pass your text documents through this checklist:

1. **Remove Duplicates**: If your dataset has identical QA pairs, the model will overfit (memorize them too rigidly).
2. **Standardize Layouts**: Ensure bullet points, punctuation, and system prompts are identical across all samples.
3. **Filter Out Bad Outputs**: Manually review and delete samples where the output is vague (e.g. *"I don't know,"* *"Please check the manual"*), otherwise your model will learn to avoid answering.
4. **Token Length Control**: Ensure your samples do not exceed the model's target context length (e.g. keep samples under 2,000 tokens) to prevent out-of-memory errors on your GPU.

---

## 🧬 3. Generating Synthetic Data (LLM-as-a-Creator)

What if you have a 100-page company manual, but zero QA pairs to train your model? You can use a stronger model (like GPT-4o or Claude) to read the manual and generate 1,000 synthetic questions and answers.

Here is the prompt template to generate synthetic data:

> *"Act as an expert data annotator. Read the following page from our manual and generate 5 realistic user questions and Standard Operating Procedure answers. Output the results strictly in the following JSON format:*
>
> `[{"instruction": "user question", "input": "", "output": "detailed standard answer"}]`
>
> *Manual page content: [Paste manual text here]"*

By looping this prompt across all 100 pages of your manual using a Python script, you can build a high-quality dataset of 500 samples in a few minutes for a few dollars.

---

Now that your training data is ready, you can feed it into your model in [Why Fine-Tune?](24_finetuning.md).
