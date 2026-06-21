← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (31_ai_gateway_circuit_b_zh.md)](31_ai_gateway_circuit_b_zh.md)

---

# 🛡️ Chapter 31: AI Gateway Resilience

AI models can fail, spike in latency, or hit rate limits at any moment. **Circuit Breakers** and **Multi-Model Failover Routing** are the dual shields that keep your AI gateway running when providers go down.

## ⚡ The Electrical Circuit Breaker Analogy

* **The Analogy**: Your AI gateway is a smart home electrical panel equipped with backup generators.
* **How it works**: When a power surge (model failure) occurs, a circuit breaker trips to cut the current. A backup generator (failover model) can take over to keep the service available.
* **Key Concept**: Fail fast to reduce the blast radius of failures, then route traffic to backup models to improve availability.

## 📊 Quick Comparison

| Concept | Traditional | LLM Era | Impact |
| :--- | :--- | :--- | :--- |
| **Error Handling** | Retries and timeouts against a single database or API. | Dynamic routing across completely different AI providers. | Avoids vendor lock-in and protects against single points of failure. |
| **Outage Mitigation** | Show a "Service Unavailable" error page. | Fall back to a smaller, cheaper, or local model when possible. | Users may see a brief degradation instead of a hard outage. |
| **Trust Model** | Assuming first-party APIs are generally reliable. | "Zero Trust" gateway assuming third-party LLMs will frequently fail. | Drastically improves application stability. |

## 🧠 Core Concept

1. **Monitor & Measure**: The gateway continuously tracks latency, error rates, and API limits for your primary model.
2. **Trip the Breaker**: If failure thresholds are crossed, the circuit "opens" to instantly block traffic and prevent resource exhaustion.
3. **Execute Failover**: Traffic can be rerouted to a secondary model (e.g., Claude 3 or local Llama 3) to support graceful degradation.
4. **Test & Recover**: The gateway periodically tests the primary model; once recovered, the breaker "closes" to restore normal traffic flow.

## 🛠️ Technical Deep Dive & Implementation

In modern AI gateways (like LiteLLM, Kong AI Gateway, or LangChain), circuit breaking and failover are implemented to ensure high availability. When a primary provider (e.g., OpenAI) times out or hits rate limits (HTTP 429), the gateway can fallback to a secondary provider (e.g., Azure OpenAI or Anthropic) rather than failing the user request.

### Implementation: Python LiteLLM Failover Snippet

Below is a Python example using `litellm` to configure model fallbacks. If the primary model fails or times out, it automatically attempts the next model in the list.

```python
import litellm
import os

os.environ["OPENAI_API_KEY"] = "sk-primary-..."
os.environ["ANTHROPIC_API_KEY"] = "sk-ant-..."
os.environ["AZURE_API_KEY"] = "sk-azure-..."

# Define the failover list (Primary -> Secondary -> Fallback)
fallback_models = [
    "gpt-4o",                     # Primary (OpenAI)
    "claude-3-5-sonnet-20240620", # Secondary (Anthropic)
    "azure/gpt-4o"                # Fallback (Azure)
]

def resilient_llm_call(prompt: str):
    try:
        response = litellm.completion(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            fallbacks=fallback_models,
            timeout=5.0,        # Fast timeout to trigger failover quickly
            num_retries=1       # Minimal retries to avoid hanging
        )
        return response.choices[0].message.content
    except Exception as e:
        # Catch all exceptions after fallbacks are exhausted
        return f"Gateway Error: All models failed. {str(e)}"

# Example Usage
print(resilient_llm_call("Analyze this log file..."))
```

### Key Considerations for Circuit Breakers
- **Timeouts**: Keep primary model timeouts relatively short (e.g., 5-10 seconds) to reduce the chance of a long wait during a failover cascade.
- **Stateful Breakers**: For production, use a distributed cache (like Redis) to count consecutive failures across all gateway instances. If failures cross a threshold, "open" the circuit globally and instantly route all requests to the secondary model for a cooldown period (e.g., 60 seconds) without waiting for timeouts.
- **Cost & Context Windows**: Ensure your fallback models support equivalent context window sizes and account for potential pricing differences during fallback routing.

---

← [Prev Chapter](../phase4/30_prompt.md) | [Next Chapter](32_ai.md) →
