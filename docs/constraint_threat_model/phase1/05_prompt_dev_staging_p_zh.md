← 返回 [约束与威胁模型](../../CONSTRAINT_THREAT_MODEL_zh.md) | [English Version (05_prompt_dev_staging_p.md)](05_prompt_dev_staging_p.md)

---

# 📦 第五章：提示词版本控制与动态分发

在现代 AI 工程中，提示词不再是硬编码的文本，而是核心的软件资产。像对待编译后的二进制文件一样严谨地管理提示词，能确保系统的稳定性、可追踪与持续进化。

## 🍳 The Restaurant Recipe Analogy

* **类比**： 部署新的提示词，完全等同于向全球连锁餐厅推出一份全新菜谱。
* **原理**： 主厨在测试厨房里研发菜品（Dev），在旗舰店试营业测试反响（Staging），最终推广到所有门店（Prod）。
* **核心概念**： 如果新菜品全球翻车，直接换回老菜单而无需重建餐厅，这正是动态提示词回滚机制的精髓。

## 📊 快速对比

| 概念 | 传统方式 | LLM 时代 | 影响 |
| --- | --- | --- | --- |
| **存储方式** | 硬编码在源代码中 | 集中式提示词注册表 | 将提示词与应用程序部署解耦。 |
| **更新机制** | 需要完整的应用重新部署 | 通过 API 动态分发 | 无需停机即可瞬间推送更新。 |
| **测试验证** | 针对确定性逻辑的单元测试 | 针对真实流量的 A/B 测试 | 基于数据驱动的性能衡量。 |
| **故障处理** | 紧急修复代码并重新部署 | 更改版本指针 | 秒级实现瞬间回滚。 |

## 🧠 核心概念

1. **本地开发 (Dev)**：工程师针对预定义的测试用例尝试指令和少样本示例。
2. **预发布测试 (Staging)**：提示词与应用代码集成，面对复杂的类生产数据以捕获边缘情况。
3. **动态部署 (Prod)**：应用程序从集中式系统获取最新的活跃提示词，无需重新部署。
4. **监控与回滚 (Monitor & Rollback)**：监控输出中的错误或幻觉，如果出现问题，立即恢复版本指针。

## 🛠️ 技术深度探索与落地

在现代 LLMOps 中，提示词必须与应用程序逻辑解耦。使用基于评估的 CI/CD 流水线可确保所有的提示词变更在推送到生产环境前都经过了严格的验证。

### 在 CI/CD 中进行提示词评估 (GitHub Actions)

此流水线演示了如何自动对提示词更改运行评估。如果新的提示词在基准数据集上的回归测试失败，构建将被拦截。

```yaml
name: Prompt CI/CD Pipeline

on:
  pull_request:
    paths:
      - 'prompts/**.json'
      - 'prompts/**.yaml'

jobs:
  evaluate-prompt:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install LLMOps SDK (e.g. LangSmith, Promptflow)
        run: pip install promptflow promptflow-tools

      - name: Run Prompt Evaluation
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          # 针对 Staging 测试数据集评估更新后的提示词
          pf run create --flow ./prompts/customer_support --data ./datasets/staging_test_cases.jsonl --stream

      - name: Assert Evaluation Thresholds
        run: |
          # 运行自定义脚本确保准确率 > 90% 且有害性 < 1%
          python scripts/assert_metrics.py --min-accuracy 0.90
```

### 动态下发机制 (Python 代码片段)

避免硬编码。通过提示词注册中心（Prompt Registry）动态拉取提示词模板，可以在不重新部署微服务的情况下实现瞬间回滚。

```python
import requests

def get_active_prompt(prompt_name: str, environment: str = "prod") -> str:
    """
    从提示词注册中心动态拉取当前激活的提示词模板。
    """
    registry_url = f"https://api.promptregistry.internal/v1/prompts/{prompt_name}"
    response = requests.get(
        registry_url, 
        params={"env": environment},
        headers={"Authorization": "Bearer YOUR_REGISTRY_TOKEN"}
    )
    
    if response.status_code == 200:
        return response.json().get("template")
    else:
        # 当注册中心宕机时，回退至本地缓存
        return load_local_fallback(prompt_name)

# 使用示例
customer_prompt_template = get_active_prompt("customer_support_v2")
# 使用动态获取到的模板执行 LLM 调用...
```

---

← [上一章](04_prompt_zh.md) | [下一章](06_system_prompt_tokens_zh.md) →
