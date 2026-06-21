← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (18_visual_injection_zh.md)](18_visual_injection_zh.md)

---

# 👁️ Chapter 18: Visual Injection

Visual Injection is a technique where malicious instructions are hidden inside images to bypass text-based security filters. As AI models process both text and visual data, attackers exploit this blind spot to hijack multi-modal systems.

## 🖼️ The Smuggler's Painting Analogy

* **The Analogy**: A smuggler hides contraband inside a beautiful landscape painting to bypass border guards who only check luggage.
* **How it works**: The text-based security filters (the "guards") only scan standard text inputs and let the image pass through. Once inside, the AI's vision systems extract and execute the hidden instructions.
* **Key Concept**: Security guardrails applied exclusively to text cannot protect against malicious payloads embedded in visual inputs.

## 📊 Quick Comparison

| Concept | Traditional | LLM Era | Impact |
| :--- | :--- | :--- | :--- |
| **Input Medium** | Text strings and code. | Images, audio, and complex multi-modal inputs. | Attack surface expands beyond standard text parsing. |
| **Security Focus** | Filtering known bad text patterns. | Must scan and interpret visual data for hidden prompts. | Text-only filters are entirely bypassed by visual payloads. |
| **Execution** | Code executes directly. | Vision encoders transcribe text from images into the context window. | AI unknowingly reads and follows malicious visual instructions. |

## 🧠 Core Concept

1. **Craft the Image**: The attacker embeds malicious instructions (like "Ignore previous instructions") into an image using typography, hidden text, or optical illusions.
2. **Submit the Payload**: The image is uploaded to the multi-modal AI system.
3. **Bypass Filters**: Standard text-based security guardrails scan the text prompt but ignore the image content.
4. **Visual Processing**: The model's vision encoder (or OCR) parses the image and extracts the hidden text directly into the AI's processing context.
5. **Hijack Execution**: The AI reads the extracted text as a valid command and alters its behavior accordingly.

---

← [Prev Chapter](17_rag_agent.md) | [Next Chapter](19_prompt_leaking.md) →
