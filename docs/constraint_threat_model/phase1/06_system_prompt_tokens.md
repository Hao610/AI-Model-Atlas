← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (06_system_prompt_tokens_zh.md)](06_system_prompt_tokens_zh.md)

---

# 💸 Chapter 6: System Prompt Compression & Token Cost Breakers

Tokenomics are the reality of working with LLMs—every character you send to an API costs you money. Bloated system prompts act like massive tax deductions on every request, while sudden traffic spikes can drain your budget overnight.

## 📦 The Telegram Analogy
* **The Analogy**: Sending a system prompt is like paying for a telegram by the word.
* **How it works**: A massive system prompt forces you to pay overhead costs on *every single interaction* before the user even types a query.
* **Key Concept**: Trim the fat out of your instructions, and install circuit breakers to stop budget bleeds during uncontrolled loops or spikes.

## 📊 Quick Comparison
| Concept | Traditional | LLM Era | Impact |
| :--- | :--- | :--- | :--- |
| **Instruction Size** | Long and overly polite instructions. | Terse, compressed, and direct. | Cheaper, faster inferences. |
| **Example Loading** | All examples loaded statically in the prompt. | RAG-injected or dynamic few-shot examples. | Massive token reduction and better focus. |
| **Usage Limits** | Hardcoded API quotas at the platform level. | Dynamic, application-layer Cost Breakers. | Granular control and graceful degradation. |

## 🧠 Core Concept
1. **Refactor and Distill**: Strip out conversational filler. Replace "Please ensure you always respond in JSON format, thank you" with "Output JSON."
2. **Optimize Examples**: Shrink few-shot examples or move them entirely into dynamic RAG injection so they only load when strictly necessary.
3. **Use Algorithmic Compression**: Utilize tools like LLMLingua to mathematically prune non-essential tokens from your prompt without destroying its semantic meaning.
4. **Implement Cost Breakers**: Track `usage` metadata on every API response to monitor rolling budgets. 
5. **Trip the Breaker**: If consumption reaches the threshold, block outbound LLM API requests and fall back to a smaller local model or a static error message to protect your wallet.

### Cost Breaker Architecture Example

```mermaid
flowchart TD
    User([User Request]) --> Gateway[API Gateway]
    Gateway --> BudgetCheck{Cost Breaker\nThreshold Reached?}
    
    BudgetCheck -- Yes --> Reject[Reject Request / Fallback]
    BudgetCheck -- No --> API[LLM API Call]
    
    API --> TokenLogger[Log Token Usage]
    TokenLogger --> Aggregator[(Redis / Metrics DB)]
    Aggregator -. Update metrics .-> BudgetCheck
```

## 🛠️ Technical Deep Dive & Implementation

To prevent Denial of Wallet (DoW) attacks and optimize token usage, implement programmatic budget enforcement at the API gateway layer, paired with prompt compression techniques.

**1. Redis-Based Token Cost Breaker (Python)**
Using a leaky bucket or token bucket approach to track and limit token expenditures per user/tenant.

```python
import redis
import time
from fastapi import HTTPException

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def check_and_deduct_budget(user_id: str, estimated_tokens: int, max_daily_tokens: int = 50000):
    """
    Evaluates if the user has enough budget for the request and updates usage.
    """
    today = time.strftime("%Y-%m-%d")
    key = f"token_usage:{user_id}:{today}"
    
    # Get current usage
    current_usage = redis_client.get(key)
    current_usage = int(current_usage) if current_usage else 0
    
    if current_usage + estimated_tokens > max_daily_tokens:
        # Trip the breaker
        raise HTTPException(
            status_code=429, 
            detail="Cost breaker tripped: Daily token budget exceeded."
        )
    
    # Increment usage (in production, update this AFTER the API response with actual tokens)
    redis_client.incrby(key, estimated_tokens)
    redis_client.expire(key, 86400) # Expire in 24 hours
    
    return True
```

**2. Algorithmic Prompt Compression (LLMLingua)**
Use lightweight models to compress system prompts before passing them to expensive frontier models.

```python
# Pseudocode for algorithmic prompt compression
from llmlingua import PromptCompressor

# Initialize compressor with a smaller, local model
compressor = PromptCompressor(model_name="microsoft/phi-2", device_map="cpu")

def compress_system_prompt(original_prompt: str, target_ratio: float = 0.5) -> str:
    """
    Compresses the prompt to reduce token size while preserving semantic instructions.
    """
    compressed = compressor.compress_prompt(
        original_prompt,
        instruction="",
        question="",
        target_token_ratio=target_ratio
    )
    return compressed['compressed_prompt']
```

---

← [Prev Chapter](05_prompt_dev_staging_p.md) | [Next Chapter](../phase2/07_dynamic_few_shot.md) →
