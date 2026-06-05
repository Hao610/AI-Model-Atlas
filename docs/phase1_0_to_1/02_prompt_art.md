# Prompt Art 🎨

[English] | [中文 (02_prompt_art_zh.md)](02_prompt_art_zh.md)

Talking to an AI is not like searching on Google. On Google, you search for keywords. With AI, you are directing an intelligent assistant. 

A **Prompt** is simply the text instruction you give to the AI. Writing good prompts is called **Prompt Engineering**.

---

## 🏛️ The R.O.L.E. Framework

If you write a vague question, you will get a vague answer. To get high-quality outputs, use the **ROLE** formula:

| Element | Description | Example |
| :--- | :--- | :--- |
| **R**ole (Who?) | Give the AI a clear persona or profession. | *"Act as an expert English teacher."* |
| **O**bjective (What?) | State the exact task you want to accomplish. | *"Explain the difference between 'affect' and 'effect'."* |
| **L**imitations (How?) | Define boundaries, constraints, or tone. | *"Use simple words. Keep it under 100 words. No technical jargon."* |
| **E**xample (Format?) | Show the AI what the desired output looks like. | *Provide a short sample output layout.* |

---

## 🎯 Bad Prompt vs. Great Prompt

Let's look at the difference in results:

### Scenario: Writing an Email to a Boss

| Bad Prompt | Great Prompt (ROLE Framework) |
| :--- | :--- |
| *Write an email to my boss saying I'm sick.* | *Act as a professional corporate assistant (Role). Write a polite email to my boss explaining that I cannot come to work today due to a sudden fever (Objective). Keep the tone professional, respectful, and brief (Limitations). Format it with Subject, Salutation, Body, and Sign-off (Example).* |
| **Result**: A generic, sometimes overly casual email that might not fit your company culture. | **Result**: A perfectly polished, respectful email ready to send with zero editing required. |

---

## ⚡ Key Techniques

### 1. Zero-Shot vs. Few-Shot Prompting
* **Zero-Shot**: You ask the AI to do something without giving it any examples.
  * *Example*: *"Translate this sentence to French: Hello, how are you?"*
* **Few-Shot**: You give the AI 1 or 2 examples of how it should answer before asking your question. This is incredibly powerful for complex formatting or style mirroring.
  * *Example*:
    ```text
    Input: Happy -> Output: 😊
    Input: Sad -> Output: 😢
    Input: Excited -> Output:
    ```
    *(The AI will instantly output 😆 because it sees the pattern)*.

### 2. Chain of Thought (CoT)
If you ask AI to solve a hard math riddle or logic puzzle, it might rush to a wrong answer. To fix this, tell the AI to:
> *"Think step-by-step before answering."*

This forces the model to write out its reasoning steps first, which dramatically increases accuracy.

---

Now that you can talk to AI like a pro, let's understand the rules of the playground in [Open Source Licenses](03_licenses.md).
