← 返回 [约束与威胁模型](../../CONSTRAINT_THREAT_MODEL_zh.md) | [English Version (08_cot_tot.md)](08_cot_tot.md)

---

# 🌳 第八章：CoT 与 ToT 优化

当大语言模型处理复杂的逻辑难题时，标准的提示方法往往会碰壁。**思维链 (CoT)** 和 **思维树 (ToT)** 迫使模型放慢速度，在输出最终答案前先进行规划和自我评估。

## 🕵️‍♂️ 侦探类比

* **类比**： 侦探绝不会立刻瞎猜凶手，而是建立时间线并测试不同的推论。
* **原理**： CoT 强制执行线性的逐步推导。ToT 则更进一步，同时探索多个时间线，并在某条线索走进死胡同时进行回溯。
* **核心概念**： 通过展现中间的推理步骤，我们能够大幅降低幻觉和逻辑错误。

## 📊 快速对比

| 概念 | 传统方式 | LLM 时代 | 影响 |
| :--- | :--- | :--- | :--- |
| **逻辑路径** | 直接的“输入 -> 输出”映射 | “输入 -> 推理 -> 输出” | 显著降低幻觉率 |
| **路径探索** | 单一、线性的尝试 | 并行评估的树状分支 | 攻克复杂的多步骤任务 |
| **纠错能力** | 一步错，步步错 | 修剪错误路径并回溯 | 推理可靠性的巨大飞跃 |

## 🧠 核心概念

**思维链 (CoT)** 是一种线性的推理过程，而 **思维树 (ToT)** 将其扩展为具有评估机制的分支结构。

1. **提示步骤**: 指示模型“一步步思考”，生成中间的逻辑状态。
2. **生成候选**: 在 ToT 中，模型不只生成一个分支，而是头脑风暴出多个可能的下一步骤。
3. **评估状态**: 模型充当自身的评论家，评估每条分支能在多大程度上接近正确答案。
4. **搜索与修剪**: 继续深入探索有希望的路径，并在生成最终答案前修剪掉死胡同的逻辑分支。

## 🛠️ 技术深度探索与落地

虽然通过简单的零样本提示（`“让我们一步步思考”`）即可实现思维链（CoT），但思维树（ToT）通常需要代码层面的编排调度。实现 ToT 涉及状态管理、候选分支生成以及启发式评估函数。

### Python 伪代码：思维树 (ToT) 调度器

```python
import openai

def generate_thoughts(state, k=3):
    """根据当前状态，生成 k 个可能的下一步骤。"""
    prompt = f"基于当前的逻辑状态：{state}\n请头脑风暴 {k} 种不同的下一步解决方案。"
    response = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": prompt}])
    return extract_branches(response.choices[0].message.content)

def evaluate_states(states):
    """让 LLM 作为评估者对每个分支的可行性进行打分。"""
    scored_states = []
    for state in states:
        prompt = f"请评估此推理状态：{state}\n打分范围从 0.0 (死胡同) 到 1.0 (确定能解决问题)。"
        response = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": prompt}])
        score = float(response.choices[0].message.content.strip())
        scored_states.append((state, score))
    return scored_states

def tree_of_thought_search(initial_state, depth, breadth):
    """通过广度优先搜索 (BFS) 与状态剪枝寻找答案。"""
    current_states = [initial_state]
    
    for _ in range(depth):
        candidates = []
        for state in current_states:
            candidates.extend(generate_thoughts(state, k=breadth))
            
        scored_candidates = evaluate_states(candidates)
        # 剪枝：仅保留得分最高的前 'breadth' 个状态
        scored_candidates.sort(key=lambda x: x[1], reverse=True)
        current_states = [state for state, score in scored_candidates[:breadth]]
        
    return current_states[0] # 返回最有希望的最终推理状态
```

### 评估指标：推理轨迹 (Ops/CI)

在 CI 流水线中验证 CoT/ToT 性能时，需要确保推理轨迹（Reasoning traces）不为空，并且输出结果与推导逻辑一致。

```yaml
# LLM Ops: 用于评估 CoT 的 PromptFoo 配置片段
prompts:
  - "问题：{{query}}\n请一步步进行思考与推导。"
providers:
  - openai:gpt-4
tests:
  - vars:
      query: "我有3个苹果。我吃了1个，又买了5个，然后把一半给朋友。我还剩几个？"
    assert:
      - type: javascript
        value: output.includes("3 - 1 = 2") && output.includes("2 + 5 = 7") && output.includes("3.5")
      - type: cost
        threshold: 0.05
```

---

← [上一章](07_dynamic_few_shot_zh.md) | [下一章](09_role_alignment_agent_zh.md) →
