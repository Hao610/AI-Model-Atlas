← 返回 [约束与威胁模型](../../CONSTRAINT_THREAT_MODEL_zh.md) | [English Version (22_git_commit_prompt.md)](22_git_commit_prompt.md)

---

# 🛡️ 第22章：Git 提交扫描 (Git Commit Scanning)

硬编码的提示词模板和 AI 密钥是代码库中的定时炸弹。通过在提交到达版本控制之前进行拦截，从源头上阻止知识产权的泄露。

## 💂 “保安”的类比

* **类比**： 在你离开高度机密的设施前，保安会检查你的背包，以防你带走敏感的公司文件。
* **原理**： Git 提交扫描充当代码库的保安，自动检查即将推送的代码更改，防止核心信息意外曝光。
* **核心概念**： 尽早捕获硬编码的提示词模板和 API 密钥，能够有效防止专有逻辑泄露并阻断提示词注入攻击。

## 📊 快速对比

| 概念 | 传统方式 | LLM 时代 | 影响 |
| --- | --- | --- | --- |
| **代码中的机密** | 密码和数据库凭证 | AI API 密钥和系统提示词指令 | 硬编码的提示词会暴露核心约束和专有逻辑。 |
| **防泄漏机制** | 针对 API 密钥的基础正则匹配 | 针对 LLM 模板结构的语义扫描 | 防止提示词注入攻击的蓝图落入攻击者手中。 |
| **安全检查点** | 滞后的安全审计 | 自动化的 Pre-commit 钩子与 CI/CD 检查 | 在敏感的 AI 数据进入版本控制系统之前进行拦截。 |

## 🧠 核心概念

1. **Pre-commit 钩子 (Hooks)**：开发者在创建提交前运行本地扫描，尽早捕获硬编码的提示词。
2. **自动化 CI/CD 集成**：自动化的流水线会检查每次代码推送的差异，寻找新引入的提示词和机密信息。
3. **模式识别**：扫描器使用正则表达式或轻量级机器学习，识别诸如 `You are an AI assistant...` 或 `System:` 等提示词结构。
4. **拦截泄露**：如果发现敏感数据，CI/CD 流水线将失败，并强制要求开发者将模板安全地存储到环境变量中。

## 🛠️ 技术深度探索与落地

保障 AI 应用的供应链安全需要健壮的运维（Ops/CI）护栏。硬编码的系统提示词等同于给攻击者提供了逆向工程你的防御机制的蓝图。

### 1. 针对提示词检测的自定义 Pre-commit 钩子

你可以利用 pre-commit 钩子或机密扫描工具中的自定义正则表达式，来识别可能被硬编码的提示词指令。

**`.pre-commit-config.yaml` 片段：**
```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: check-added-large-files
  - repo: local
    hooks:
      - id: scan-hardcoded-prompts
        name: Scan for Hardcoded System Prompts
        entry: bash -c 'git grep -E -i "(You are an AI|System Prompt:|Answer as a helpful assistant)" --cached && echo "🚨 警告：检测到硬编码的系统提示词！" && exit 1 || exit 0'
        language: system
        pass_filenames: false
```

### 2. CI/CD 中的自动化机密与提示词扫描

将诸如 [TruffleHog](https://github.com/trufflesecurity/trufflehog) 或 [Gitleaks](https://github.com/gitleaks/gitleaks) 之类的工具直接集成到你的 CI 流水线中。你可以扩展它们的默认规则集，以检测专有的 LLM 框架模式（例如，LangChain 模板字符串）。

**GitHub Actions 流水线 (`.github/workflows/ai-security-scan.yml`)：**
```yaml
name: AI Security Commit Scan
on: [push, pull_request]

jobs:
  secret_and_prompt_scan:
    name: Scan for LLM Secrets and Prompts
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Run Gitleaks
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          
      - name: Scan for Proprietary Prompt Templates
        run: |
          echo "正在扫描差异代码中是否存在硬编码的 LangChain/LlamaIndex 系统模板..."
          # 针对提示词泄露的抽象模式匹配
          if git diff origin/main..HEAD | grep -iE 'PromptTemplate|SystemMessage|ChatPromptTemplate\.from_messages'; then
            echo "⚠️  警告：在提交差异中发现提示词模板。请确保专有指令安全存储（如 AWS Parameter Store, HashiCorp Vault），避免硬编码。"
            # 取消注释以拦截构建：exit 1
          fi
```

### 3. 缓解策略
- **外部化提示词：** 将系统提示词存储在集中式配置管理工具（如 Azure App Configuration，AWS Systems Manager）或专用的数据库中。
- **使用标识符：** 在代码库中，通过 ID 来引用提示词，而不是硬编码原始字符串。
- **脱敏日志：** 确保如果在模板评估期间发生构建失败，CI/CD 流水线会自动剥离实际的提示词文本。

---

← [上一章](../phase3/21_rag_pii_zh.md) | [下一章](23_prompt_zh.md) →
