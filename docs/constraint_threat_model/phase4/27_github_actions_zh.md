← 返回 [约束与威胁模型](../../CONSTRAINT_THREAT_MODEL_zh.md) | [English Version (27_github_actions.md)](27_github_actions.md)

---

# 🛑 第27章：网关拦截器（GitHub Actions）

在提示词注入和越狱攻击进入生产环境之前将其拦截。欢迎来到AI安全的CI/CD时代。

## 🛂 机场安检类比
* **类比**：CI/CD网关拦截器就像机场的护照检查和安检扫描仪。
* **工作原理**：在您的代码“登机”前往生产环境之前，必须通过自动检查以扫描违禁品（漏洞）。
* **核心概念**：在构建阶段捕获薄弱的系统提示词和缺失的安全防护，从而完全避免主动威胁。

## 📊 快速对比

| 概念 | 传统方式 | 大模型时代 | 影响 |
| --- | --- | --- | --- |
| **代码检查 (Linting)** | 语法检查，未使用的变量。 | 提示词扫描，安全防护验证。 | 捕获危险指令。 |
| **测试** | 单元测试逻辑。 | 自动化对抗性测试（红队测试）。 | 拦截已知的越狱模式。 |
| **失败状态** | 代码损坏时构建失败。 | 提示词配置不安全时构建失败。 | 防止部署易受攻击的版本。 |

## 🧠 核心概念

1. **安全左移：** 将提示词漏洞扫描器直接集成到您的拉取请求（PR）工作流中。
2. **自动化强制执行：** CI/CD管道自动评估系统提示词和模型参数。
3. **对抗性测试：** 运行尝试越狱本地测试模型的自动化测试套件。
4. **可审计性：** 为每次构建生成安全日志，证明安全防护已通过检查。

## 🛠️ 技术深度探索与落地

为了构建有效的AI安全网关，您需要在CI流水线中建立多层自动化防御机制。我们将验证静态提示词（提示词Linting），并通过合成对抗评估来动态测试应用程序。

### GitHub Actions：AI DevSecOps流水线

以下工作流演示了如何将静态分析和动态对抗性测试（通过Promptfoo或pytest）集成到您的CI/CD流程中。

```yaml
name: AI DevSecOps Gateway

on:
  pull_request:
    branches: [ "main", "develop" ]
    paths:
      - 'app/prompts/**'
      - 'app/llm_config.json'

jobs:
  llm-security-audit:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install AI Security Dependencies
        run: |
          pip install detect-secrets pytest giskard promptfoo

      - name: 🛡️ 第1步 - 静态提示词分析
        # 检查硬编码的API密钥或范围过大的危险系统提示词
        run: |
          detect-secrets scan ./app/prompts/ > secrets_report.json
          python scripts/lint_prompts.py ./app/prompts/

      - name: 🧪 第2步 - 动态对抗性测试（本地预发布）
        # 使用预定义的已脱敏Payload评估LLM端点
        # 例如，Pattern: "Ignore previous instructions..." (sanitized)
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          STAGING_ENDPOINT: "http://localhost:8000/v1/chat"
        run: |
          # 示例：使用 promptfoo 进行评估
          promptfoo eval -c tests/adversarial/promptfoo.yaml --output eval_results.json
          
      - name: 🚦 第3步 - 关卡策略强制执行
        # 如果通过率低于95%的阈值，则构建失败
        run: |
          python scripts/enforce_threshold.py eval_results.json --min-pass-rate 0.95
```

### 评估脚本代码片段 (`enforce_threshold.py`)

一个简单的脚本，用于解析评估输出并在检测到安全退化时阻止代码合并。

```python
import json
import sys
import argparse

def enforce_security_threshold(results_file, min_pass_rate):
    with open(results_file, 'r') as f:
        data = json.load(f)
        
    total_tests = data.get('results', {}).get('stats', {}).get('total', 0)
    passed_tests = data.get('results', {}).get('stats', {}).get('successes', 0)
    
    if total_tests == 0:
        print("❌ 未执行任何对抗性测试。构建失败。")
        sys.exit(1)
        
    pass_rate = passed_tests / total_tests
    print(f"📊 LLM 安全通过率: {pass_rate*100:.2f}%")
    
    if pass_rate < min_pass_rate:
        print(f"❌ 安全阈值未达标。要求: {min_pass_rate*100}%，实际: {pass_rate*100:.2f}%")
        print("⚠️ 检测到潜在的提示词注入漏洞。请检查评估日志。")
        sys.exit(1)
        
    print("✅ 所有 LLM 安全检查均已通过。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('results', help='评估结果JSON文件的路径')
    parser.add_argument('--min-pass-rate', type=float, default=0.95)
    args = parser.parse_args()
    
    enforce_security_threshold(args.results, args.min_pass_rate)
```

---

← [上一章](26_automated_red_teamin_zh.md) | [下一章](28_safety_judge_zh.md) →
