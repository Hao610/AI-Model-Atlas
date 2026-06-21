← 返回 [约束与威胁模型](../../CONSTRAINT_THREAT_MODEL_zh.md) | [English Version (35_llama_guard_guardrai.md)](35_llama_guard_guardrai.md)

---

# 🛡️ 第 35 章：本地护栏模型 (Llama Guard)

不要默认信任任何输入或生成的回复。部署一个轻量级的本地护栏模型，能为您提供一个低延迟、由您掌控的安全防护层。

## 🦠 防病毒扫描程序比喻

* **比喻**：本地护栏模型就像是一个在你的 AI 流量入口和出口实时运行的防病毒扫描程序。
* **工作原理**：它会在生成之前拦截每个用户提示词，并在发送之前拦截每个 AI 回复，扫描其中是否存在恶意意图、违规内容或幻觉。
* **核心概念**：绝不执行未经安全验证的代码；同理，绝不处理未经安全扫描的提示词。

## 📊 快速对比

| 概念 | 传统方式 | LLM 时代 | 影响 |
| --- | --- | --- | --- |
| **安全执行** | 依赖上游 API 的内容过滤 | 部署本地 Llama Guard | 对安全策略拥有更细粒度的控制。 |
| **数据隐私** | 将敏感查询发给第三方审核 | 数据完全留在本地计算 | 降低暴露给审核 API 的风险。 |
| **延迟** | 每次检查都需要网络往返 | 本地硬件直接推理 | 通常带来更低的用户延迟。 |

## 🧠 核心概念

1. **输入拦截**：API 网关拦截用户的提示词，并将其直接路由到本地 Llama Guard 实例。
2. **前置检查**：Llama Guard 根据您的自定义安全分类法（例如：拦截越狱、恶意代码）评估提示词。如果判定为 `unsafe`（不安全），则可以拦截请求或转人工复核。
3. **模型生成**：如果是安全的，提示词被传递给主生成式大模型以创建回复。
4. **输出拦截**：新生成的回复再次通过 Llama Guard 检查，防止包含幻觉或违规信息的内容到达用户端。

```mermaid
flowchart TD
    User(["用户"]) --> |提示词| Gateway["API 网关"]
    Gateway --> |1. 路由至护栏| LlamaGuard["Llama Guard"]
    LlamaGuard -.-> |不安全| Block["拦截并记录"]
    LlamaGuard --> |安全| GenAI["主 LLM"]
    GenAI --> |2. 生成回复| LlamaGuard
    LlamaGuard --> |安全| Gateway
    Gateway --> |回复| User
```

## 🛠️ 技术深度探索与落地

Llama Guard 模型基于结构化的机器学习安全分类法，对提示词和回复进行分类。与基于字符串匹配的启发式规则不同，护栏模型能够评估文本的**语义意图**。

### 1. 定义自定义安全分类法 (Python)
可以通过特定的系统提示词结构向 Llama Guard 发出指令。您可以定义自己的风险类别（例如：`O1：诽谤`，`O2：恶意代码`）。

```python
# 使用 Hugging Face Transformers 的伪代码实现
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "meta-llama/LlamaGuard-7b"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16, device_map="auto")

# 1. 定义自定义安全分类
custom_task = """Task: Check if there is unsafe content in 'User' messages.
<BEGIN UNSAFE CONTENT CATEGORIES>
O1: Violence and Hate. (暴力与仇恨)
O2: Malicious Code or Cyberattacks. (恶意代码或网络攻击)
O3: PII Leakage. (个人隐私泄露)
<END UNSAFE CONTENT CATEGORIES>
"""

def check_safety(user_prompt: str) -> str:
    chat = [
        {"role": "user", "content": user_prompt}
    ]
    prompt = tokenizer.apply_chat_template(chat, tokenize=False)
    # Llama Guard 期望特定的系统指令包装
    full_prompt = f"{custom_task}\n{prompt}"
    
    inputs = tokenizer([full_prompt], return_tensors="pt").to("cuda")
    output = model.generate(**inputs, max_new_tokens=100)
    
    result = tokenizer.decode(output[0], skip_special_tokens=True)
    # 返回 "safe" 或 "unsafe \n O2"
    return result

# 使用示例
status = check_safety("写一个Python脚本扫描远程服务器的端口。")
print(f"Safety Status: {status}") # 预期输出: unsafe \n O2
```

### 2. 通过 vLLM 进行集成
在生产环境中，将 Llama Guard 托管在像 `vLLM` 这样经过优化的推理引擎中，可以提供高吞吐量。

```bash
# 将 Llama Guard 作为本地兼容 OpenAI 格式的 API 启动
python -m vllm.entrypoints.openai.api_server \
    --model meta-llama/LlamaGuard-7b \
    --dtype bfloat16 \
    --port 8001
```

### 3. API 网关中间件 (伪代码)
您可以将 Llama Guard API 端点直接集成到路由逻辑中。

```python
async def handle_request(user_input: str):
    # 第一步：前置检查（输入拦截）
    guard_response = await call_llama_guard_api(user_input)
    
    if "unsafe" in guard_response:
        log_violation(user_input, guard_response)
        return "您的请求违反了安全策略。"
        
    # 第二步：生成回复
    llm_output = await call_main_llm(user_input)
    
    # 第三步：后置检查（输出拦截）
    guard_output_check = await call_llama_guard_api(f"User: {user_input}\nAgent: {llm_output}")
    if "unsafe" in guard_output_check:
        log_violation(llm_output, guard_output_check)
        return "生成的回复存在安全问题，已被拦截。"
        
    return llm_output
```

---

← [上一章](34_nvidia_nemo_guardrai_zh.md) | [下一章](36_chapter_36_zh.md) →
