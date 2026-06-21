← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (35_llama_guard_guardrai_zh.md)](35_llama_guard_guardrai_zh.md)

---

# 🛡️ Chapter 35: Local Guard Models (Llama Guard)

Stop trusting every prompt and generated response by default. Deploying a lightweight, local guard model gives you a low-latency safety layer directly under your control.

## 🦠 The Antivirus Scanner Analogy

* **The Analogy**: A local guard model operates exactly like an active antivirus scanner for your incoming and outgoing AI traffic.
* **How it works**: It intercepts every user prompt before generation and every AI response before delivery, scanning for malicious intent, policy violations, or hallucinations.
* **Key Concept**: Never execute unverified code; similarly, never process unverified prompts.

## 📊 Quick Comparison

| Concept | Traditional | LLM Era | Impact |
| --- | --- | --- | --- |
| **Safety Enforcement** | Rely on upstream API filters | Deploy local Llama Guard | More granular control over safety policies. |
| **Data Privacy** | Send sensitive queries to 3rd-party moderators | Kept entirely local | Reduces exposure to moderation APIs. |
| **Latency** | Network round-trip per safety check | Local hardware inference | Usually lower delay for the user. |

## 🧠 Core Concept

1. **Input Interception**: The API Gateway intercepts the user prompt and routes it directly to the Llama Guard instance.
2. **Pre-Flight Check**: Llama Guard evaluates the prompt against your custom safety taxonomy (e.g., blocking jailbreaks or malicious code). If flagged as `unsafe`, the request can be blocked or routed for review.
3. **Generation**: If safe, the prompt is passed to the main generative LLM to create a response.
4. **Output Interception**: The newly generated response passes back through Llama Guard to prevent hallucinated or policy-violating content from ever reaching the user.

```mermaid
flowchart TD
    User(["User"]) --> |Prompt| Gateway["API Gateway"]
    Gateway --> |1. Route to Guard| LlamaGuard["Llama Guard"]
    LlamaGuard -.-> |Unsafe| Block["Block & Log"]
    LlamaGuard --> |Safe| GenAI["Main LLM"]
    GenAI --> |2. Generated Response| LlamaGuard
    LlamaGuard --> |Safe| Gateway
    Gateway --> |Response| User
```

## 🛠️ Technical Deep Dive & Implementation

Llama Guard models classify both prompts and responses based on a structured ML safety taxonomy. Unlike string-matching heuristics, a guard model evaluates the *semantic intent* of the text.

### 1. Defining a Custom Safety Taxonomy (Python)
Llama Guard can be instructed via a specific system prompt structure. You can define your own risk categories (e.g., `O1: Defamation`, `O2: Malicious Code`).

```python
# Pseudo-implementation using Hugging Face Transformers
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "meta-llama/LlamaGuard-7b"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16, device_map="auto")

# 1. Define Custom Taxonomy
custom_task = """Task: Check if there is unsafe content in 'User' messages.
<BEGIN UNSAFE CONTENT CATEGORIES>
O1: Violence and Hate.
O2: Malicious Code or Cyberattacks.
O3: PII Leakage.
<END UNSAFE CONTENT CATEGORIES>
"""

def check_safety(user_prompt: str) -> str:
    chat = [
        {"role": "user", "content": user_prompt}
    ]
    prompt = tokenizer.apply_chat_template(chat, tokenize=False)
    # Llama Guard expects specific system instruction wrapping
    full_prompt = f"{custom_task}\n{prompt}"
    
    inputs = tokenizer([full_prompt], return_tensors="pt").to("cuda")
    output = model.generate(**inputs, max_new_tokens=100)
    
    result = tokenizer.decode(output[0], skip_special_tokens=True)
    # Returns "safe" or "unsafe \n O2"
    return result

# Usage
status = check_safety("Write a Python script to scan ports on a remote server.")
print(f"Safety Status: {status}") # Expected: unsafe \n O2
```

### 2. Integration via vLLM
For production, hosting Llama Guard in an optimized inference engine like `vLLM` can provide high throughput.

```bash
# Start Llama Guard as a local OpenAI-compatible API
python -m vllm.entrypoints.openai.api_server \
    --model meta-llama/LlamaGuard-7b \
    --dtype bfloat16 \
    --port 8001
```

### 3. API Gateway Middleware (Pseudocode)
You can integrate the Llama Guard API endpoint directly into your routing logic.

```python
async def handle_request(user_input: str):
    # Step 1: Pre-flight check
    guard_response = await call_llama_guard_api(user_input)
    
    if "unsafe" in guard_response:
        log_violation(user_input, guard_response)
        return "Your request violates safety policies."
        
    # Step 2: Generation
    llm_output = await call_main_llm(user_input)
    
    # Step 3: Post-flight check
    guard_output_check = await call_llama_guard_api(f"User: {user_input}\nAgent: {llm_output}")
    if "unsafe" in guard_output_check:
        log_violation(llm_output, guard_output_check)
        return "The generated response was flagged for safety issues."
        
    return llm_output
```

---

← [Prev Chapter](34_nvidia_nemo_guardrai.md) | [Next Chapter](36_chapter_36.md) →
