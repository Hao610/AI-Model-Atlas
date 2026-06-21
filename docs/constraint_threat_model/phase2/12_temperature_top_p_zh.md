← 返回 [约束与威胁模型](../../CONSTRAINT_THREAT_MODEL_zh.md) | [English Version (12_temperature_top_p.md)](12_temperature_top_p.md)

---

# 🎛️ 第12章：动态超参数

静态生成设置在某些工作流里可能比较脆弱。动态超参数会根据不断变化的置信度和安全得分，实时调节 Temperature（温度）和 Top-p。

## 🍳 炉灶比喻

* **The Analogy（比喻）**：当水开始沸腾溢出时，立即调低炉灶的火力。
* **How it works（运作方式）**：当模型的创造性输出开始变得不稳定或荒谬（沸腾溢出）时，系统会自动“调低旋钮”（降低 Temperature 和 Top-p）以稳定输出。
* **Key Concept（核心概念）**：当幻觉风险激增时，安全系统可以动态限制参数，以帮助生成更受约束的输出。

## 📊 快速对比


## 📊 快速对比

| 概念 | 传统方式 | 大模型时代 | 影响 |
| :--- | :--- | :--- | :--- |
| **参数调节** | 每次模型运行使用硬编码配置。 | 每次对话或每个词元的实时调节。 | 平衡了安全性与创造的灵活性。 |
| **故障响应** | 生成后的过滤或拦截。 | 生成过程中的确定性降级。 | 主动防止级联幻觉。 |
| **上下文适应** | 无视提示词复杂度，设置僵化。 | 适应输出置信度的流动设置。 | 针对不同任务优化输出质量。 |

## 🧠 核心概念

实施动态超参数调整需要一个闭环反馈机制：

1. **监控 (Monitor)**：在生成输出期间，持续评估置信度得分、幻觉信号和安全指标。
2. **评估 (Evaluate)**：将实时跟踪指标与预定义的风险阈值进行比较。
3. **调整 (Adjust)**：如果突破安全限制，就降低 Temperature 和 Top-p，帮助模型朝更确定的方向输出。
4. **恢复 (Restore)**：一旦输出稳定并重新获得置信度，逐渐将超参数恢复到基线水平。

## 🛠️ 技术深度探索与落地

在实际应用中，标准的 LLM API（如 OpenAI）不允许在生成中途调整参数。这种策略通常通过**自适应重试**（当安全分类器拦截输出时，使用 `temperature=0.0` 重新请求）来实现，或者在自托管模型中通过自定义 **LogitsProcessor** 原生实现。

### 基于 LogitsProcessor 的动态温度调节 (PyTorch)
在本地运行模型时（例如使用 Hugging Face `transformers`），可以拦截 Logits 生成步骤，在不确定性（信息熵）激增时动态限制温度。

```python
import torch
from transformers import LogitsProcessor

class DynamicTempLogitsProcessor(LogitsProcessor):
    def __init__(self, base_temp=0.8, entropy_threshold=2.5):
        self.base_temp = base_temp
        self.entropy_threshold = entropy_threshold
        self.current_temp = base_temp

    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor:
        # 1. 计算预测不确定性 (信息熵)
        probs = torch.nn.functional.softmax(scores, dim=-1)
        entropy = -torch.sum(probs * torch.log(probs + 1e-9), dim=-1).mean().item()
        
        # 2. 根据实时风险调整温度
        if entropy > self.entropy_threshold:
            # 不确定性激增：下调温度以趋于确定性
            self.current_temp = max(0.1, self.current_temp - 0.3)
        else:
            # 预测稳定：逐渐恢复创造性基准
            self.current_temp = min(self.base_temp, self.current_temp + 0.05)
            
        # 3. 应用动态温度缩放
        return scores / self.current_temp
```

### 检测与缓解策略

* **检测**：监控词元概率和序列困惑度（Perplexity）。信息熵的突然激增通常是幻觉或有害偏离的前兆。
* **缓解**：将动态超参数调整与语义护栏结合使用。如果降低温度仍不能解决风险指标问题，则彻底中断生成。

---

← [上一章](11_automated_self_corre_zh.md) | [下一章](../phase3/13_direct_prompt_inject_zh.md) →
