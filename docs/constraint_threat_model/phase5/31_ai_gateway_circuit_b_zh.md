← 返回 [约束与威胁模型](../../CONSTRAINT_THREAT_MODEL_zh.md) | [English Version (31_ai_gateway_circuit_b.md)](31_ai_gateway_circuit_b.md)

---

# 🛡️ 第 31 章：AI 网关的弹性设计 (AI Gateway Resilience)

在生产环境中，AI 模型随时可能发生故障、延迟激增或触及速率限制。**断路器**和**多模型故障转移路由**是确保你的 AI 网关在服务商宕机时依然平稳运行的双重护盾。

## ⚡ The Electrical Circuit Breaker Analogy

* **类比**： 你的 AI 网关就像配备了备用发电机的智能家居配电盘。
* **原理**： 当发生电涌（模型故障）时，断路器会跳闸切断电流。备用发电机（故障转移模型）随即立刻启动，维持供电。
* **核心概念**： 快速失败可以缩小故障影响面，然后将流量路由至备用模型，以提升可用性。


## 📊 快速对比

| 概念 | 传统方式 | LLM 时代 | 影响 |
| :--- | :--- | :--- | :--- |
| **错误处理** | 针对单一数据库或 API 的重试和超时机制。 | 在完全不同的 AI 供应商之间进行动态路由。 | 避免供应商锁定并防范单点故障。 |
| **故障缓解** | 显示“服务不可用”错误页面。 | 在可行时降级至较小、更便宜或本地的模型。 | 用户可能看到短暂降级，而不是完全不可用。 |
| **信任模型** | 假定第一方 API 通常是可靠的。 | 假定第三方大模型会频繁失败的“零信任”网关。 | 极大提升了应用程序的稳定性。 |

## 🧠 核心概念

1. **监控与测量**：网关持续跟踪主模型的延迟、错误率和 API 限制。
2. **断路器跳闸**：如果超过失败阈值，电路“断开 (Open)”，立即阻止流向故障模型的流量以防止资源耗尽。
3. **执行故障转移**：流量可以重新路由至辅助模型（例如 Claude 3 或本地 Llama 3），以支持优雅降级。
4. **测试与恢复**：网关定期测试主模型；一旦确认其恢复，断路器“闭合 (Closed)”并恢复正常流量。

## 🛠️ 技术深度探索与落地

在现代 AI 网关（如 LiteLLM、Kong AI Gateway 或 LangChain）中，断路器和故障转移是确保高可用性的关键。当主要供应商（例如 OpenAI）超时或触发速率限制（HTTP 429）时，网关应立即回退（Fallback）到备用供应商（例如 Azure OpenAI 或 Anthropic），而不是直接向用户返回错误。

### 落地实践：使用 Python LiteLLM 实现故障转移

以下是一个使用 `litellm` 配置模型回退的 Python 示例。如果主模型失败或超时，它会自动尝试列表中的下一个模型。

```python
import litellm
import os

os.environ["OPENAI_API_KEY"] = "sk-primary-..."
os.environ["ANTHROPIC_API_KEY"] = "sk-ant-..."
os.environ["AZURE_API_KEY"] = "sk-azure-..."

# 定义故障转移列表 (主模型 -> 备用模型 -> 最终回退)
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
            timeout=5.0,        # 设置较短超时时间以快速触发故障转移
            num_retries=1       # 最小化重试次数以避免请求挂起
        )
        return response.choices[0].message.content
    except Exception as e:
        # 当所有备用模型都耗尽后捕获异常
        return f"Gateway Error: 所有模型均已失败。{str(e)}"

# 使用示例
print(resilient_llm_call("请分析这份日志文件..."))
```

### 断路器的关键考量
- **超时设置 (Timeouts)**：保持主模型的超时时间尽可能短（例如 5-10 秒），以防止用户在级联故障转移过程中等待过久。
- **状态断路器 (Stateful Breakers)**：在生产环境中，使用分布式缓存（如 Redis）来统计所有网关实例的连续失败次数。如果失败次数超过阈值，则全局“断开 (Open)”电路，并立即将所有请求路由到备用模型，维持一个冷却期（例如 60 秒），无需再等待主模型的超时。
- **成本与上下文窗口**：确保你的备用模型支持等效的上下文窗口大小，并在故障转移路由期间考虑到潜在的成本变化。

---

← [上一章](../phase4/30_prompt_zh.md) | [下一章](32_ai_zh.md) →
