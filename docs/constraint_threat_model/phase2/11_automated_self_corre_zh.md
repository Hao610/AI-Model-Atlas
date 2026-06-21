← 返回 [约束与威胁模型](../../CONSTRAINT_THREAT_MODEL_zh.md) | [English Version (11_automated_self_corre.md)](11_automated_self_corre.md)

---

# 🧰 第 11 章：自我纠错机制

不要再让 AI 的幻觉导致你的系统崩溃了。自我纠错与优雅降级机制构成了自动化的安全网，能在无需人工干预的情况下确保系统稳健运行。

## ✍️ The Editor and Writer Analogy

* **类比**： 将 AI 模型视为**作家**，将你的应用系统视为**编辑**。
* **原理**： 当作家提交了带有错误的草稿时，编辑不会直接扔掉或让系统崩溃。相反，编辑会将草稿连同具体的反馈一起退回，让作家自己修改错误。
* **核心概念**： 实现一个验证循环，在最终用户看到错误之前，拦截故障并提示 AI 进行自我纠正。

## 📊 快速对比

| 概念 | 传统方式 | LLM 时代 | 影响 |
| --- | --- | --- | --- |
| **错误处理** | 硬编码的 `try/catch` 和系统直接崩溃。 | 迭代式的反馈循环，让模型自行修复输出。 | **减少停机时间**。能够动态地从格式错误的输出中恢复。 |
| **验证方式** | 严格的正则表达式和类型规则。 | 模式验证结合自动提示纠错。 | **高弹性**。避免数据管道因损坏的 JSON 结构而中断。 |
| **系统故障** | 整个应用直接下线或抛出 500 错误状态。 | 优雅降级至使用缓存或简单的启发式模型。 | **高可用性**。为用户提供降级但依然可用的体验。 |

## 🧠 核心概念

1. **生成 (Generation):** LLM 尝试生成一个 JSON 响应，但可能忘记了闭合的右括号。
2. **验证 (Validation):** 应用程序的 JSON 解析器捕获到格式错误，并抛出 `SyntaxError`。
3. **纠错循环 (Correction Loop):** 系统拦截崩溃，提取解析器的错误消息，并附加提示词发送回 LLM（如：“之前的 JSON 无效，以下是错误提示，请修复 JSON。”）。
4. **解决 (Resolution):** LLM 纠正语法并返回有效的 JSON 对象，允许整个流程正常继续。
5. **优雅降级 (Graceful Degradation):** 如果模型在多次重试后仍然失败，系统将回退到较小的本地模型或使用缓存的响应，而不是彻底崩溃。

## 🛠️ 技术深度探索与落地

**防御模式：强大的验证与自我纠错循环 (Robust Validation & Self-Correction Loop)**

自我纠错机制通过捕获解析异常或验证失败（例如，使用 Pydantic），将具体的错误信息或堆栈跟踪作为提示词重新发送给模型，从而避免数据管道中断。

**落地示例 (Python 通用接口实现)：**

```python
import json
import logging

def robust_json_generator(initial_prompt: str, max_retries: int = 3) -> dict:
    current_prompt = initial_prompt
    
    for attempt in range(max_retries):
        # 1. 执行 LLM 生成
        raw_output = llm_client.generate(current_prompt)
        
        try:
            # 2. 严格的验证检查
            parsed_data = json.loads(raw_output)
            # 可选: 此处可添加严格的 Schema 验证（例如 Pydantic）
            return parsed_data
            
        except json.JSONDecodeError as e:
            logging.warning(f"第 {attempt + 1} 次验证失败: {e}")
            
            # 3. 构建自我纠错反馈循环
            current_prompt = (
                f"你之前的输出未通过验证。\n"
                f"错误详情: {str(e)}\n"
                f"格式错误的输出: {raw_output}\n"
                f"规则: 请修复格式错误，并且只返回有效的 JSON 格式。"
            )
            
    # 4. 优雅降级：重试耗尽后的安全回退
    logging.error("自我纠错次数耗尽，触发安全回退机制。")
    return _safe_fallback_handler()

def _safe_fallback_handler() -> dict:
    # 返回一个经过净化的默认数据结构，防止上游服务崩溃
    return {"status": "degraded", "data": None}
```

---

← [上一章](10_pydantic_json_zh.md) | [下一章](12_temperature_top_p_zh.md) →
