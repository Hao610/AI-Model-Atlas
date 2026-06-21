← 返回 [约束与威胁模型](../../CONSTRAINT_THREAT_MODEL_zh.md) | [English Version (04_prompt.md)](04_prompt.md)

---

# 🧩 第四章：提示词即代码 (解耦提示词)

在应用逻辑中硬编码提示词是LLM时代的终极反模式。通过将提示词视为版本化的资产，你可以解锁更快的迭代速度，并赋予领域专家在不接触源代码的情况下优化AI行为的能力。

## 🤖 机器人比喻

* **类比**： 想象一下，是将日常操作规则直接焊接到机器人的物理大脑电路中，还是给它一本可随时替换的规则手册。
* **原理**： 如果硬编码规则，你需要一名拿着烙铁的硬件工程师来改变机器人的行为。如果使用规则手册，任何懂工厂规则的人都可以直接替换指令。
* **核心概念**： 应用代码应该只知道*如何*读取和执行指令，而提示词本身则应作为易于修改的外部资产独立存在。

## 📊 快速对比

| 概念 | 传统方式 | LLM 时代 | 影响 |
| :--- | :--- | :--- | :--- |
| **逻辑存储** | 直接嵌入到源代码中 | 提取到YAML/JSON文件中 | 允许非技术专家独立进行迭代 |
| **更新周期** | 需要完整的CI/CD部署流程 | 作为独立资产随时进行部署 | 大幅加快提示词更新的上市时间 |
| **版本控制** | 与应用代码的历史记录交织 | 作为独立的版本化资产管理 | 轻松实现安全回滚和A/B测试 |
| **可重用性** | 锁定在特定的底层代码路径中 | 跨多个功能模块和项目共享 | 在整个应用程序中实现标准化行为 |

## 🧠 核心概念

1. **解耦提示词**：将所有提示词指令移出Python文件，放入YAML或JSON等结构化格式中。
2. **作为资产进行版本控制**：在版本控制系统中跟踪外部提示词文件，像对待代码配置一样严谨。
3. **分离生命周期**：允许核心应用代码和提示词规则各自独立地进行更新、测试和部署。
4. **赋能专家**：让提示词工程师和领域专家能够直接修改提示词资产，而无需浏览复杂的代码库。

## 🛠️ 技术深度探索与落地

通过将提示词解耦为受版本控制的资产，我们将工程严谨性引入了提示词工程生命周期。

**1. 通过 YAML 加载提示词 (Python)**
摒弃硬编码的字符串拼接，集中管理提示词资产：
```python
import yaml
from langchain.prompts import PromptTemplate

def load_prompt_asset(file_path: str) -> PromptTemplate:
    with open(file_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return PromptTemplate(
        input_variables=data["input_variables"],
        template=data["template"]
    )
```

**2. 自动化提示词验证 (GitHub Actions)**
CI/CD 流水线可确保提示词的更改在部署前不会破坏下游逻辑或超出 Token 限制：
```yaml
name: Validate Prompts
on:
  pull_request:
    paths:
      - 'prompts/**/*.yaml'

jobs:
  evaluate_prompts:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Run Evaluator
        run: |
          pip install -r requirements-dev.txt
          python scripts/eval_prompts.py \
            --prompts_dir ./prompts \
            --test_dataset ./data/eval_cases.json
```

---

← [上一章](03_zero_trust_zh.md) | [下一章](05_prompt_dev_staging_p_zh.md) →
