← 返回 [约束与威胁模型](../../CONSTRAINT_THREAT_MODEL_zh.md) | [English Version (15_auto_jailbreaking_py.md)](15_auto_jailbreaking_py.md)

---

# 🤖 第15章：自动化越狱与自动化红队测试

自动化红队测试（俗称“自动化越狱”）是指释放脚本来系统性地猛攻AI模型的安全过滤器。它用快速、自动化的提示词实验取代了缓慢的人类直觉。

## 🔐 开锁机器人的比喻

* **类比**： 想象一个开锁机器人，它能以超凡速度系统地尝试数百万种钥匙组合，直到锁最终被咔哒一声打开。
* **原理**： 与人类手动输入复杂的提示词来测试安全边界不同，Python脚本可以编程自动生成、变异并提交数以千计的提示词变体。
* **核心概念**： 自动化将约束探测的规模扩展到了远超人类能力的范围，从而暴露出模型隐藏的盲区。

## 📊 快速对比

| 概念 | 传统方式 | LLM 时代 | 影响 |
|---------|-------------|---------|--------|
| **红队测试** | 手动、缓慢的渗透测试 | 自动化的Python脚本探测 | 极大提升了测试的规模和速度 |
| **模糊测试** | 手工制作代码边界用例 | LLM提示词的变异和变形 | 能够发现意想不到的语义盲区 |
| **结果评估** | 人工阅读输出日志 | 使用第二个AI模型对目标AI评分 | 实现了闭环、实时的自动化优化 |

## 🧠 核心概念

1. **模糊测试与变异**：脚本从一组“种子”提示词开始，通过替换同义词、更改语言或添加假设场景来自动使它们发生变异。
2. **批量执行**：自动化系统将成千上万个这些修改后的提示词同时发送给目标模型。
3. **启发式评估**：第二个“评估器”AI模型会立即对目标的输出进行评分（拒绝回答得低分，输出受限行为得高分）。
4. **迭代优化**：使用搜索算法，脚本提取得分最高的提示词，进一步使它们变异，然后发起下一波攻击以逐渐击破模型。

```python
def run_automated_probe(target_ai, evaluator_ai, objective):
    current_prompts = generate_initial_seeds(objective)

    for iteration in range(MAX_ITERATIONS):
        responses = target_ai.query_batch(current_prompts)
        scores = evaluator_ai.score_batch(responses, objective)

        if max(scores) >= SUCCESS_THRESHOLD:
            print("发现漏洞或盲区！")
            break

        current_prompts = mutate_prompts(current_prompts, scores)
```

---

← [上一章](14_base64_zh.md) | [下一章](16_indirect_injection_p_zh.md) →
