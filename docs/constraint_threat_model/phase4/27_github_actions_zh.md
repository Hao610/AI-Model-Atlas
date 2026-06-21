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

```yaml
name: AI Security Gateway

on:
  pull_request:
    branches: [ "main" ]

jobs:
  security-check:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Run Prompt Injection Scanner
        run: python -m security_tools.prompt_scanner ./app/prompts/

      - name: Adversarial Automated Testing
        run: pytest tests/adversarial/
```

---

← [上一章](26_automated_red_teamin_zh.md) | [下一章](28_safety_judge_zh.md) →
