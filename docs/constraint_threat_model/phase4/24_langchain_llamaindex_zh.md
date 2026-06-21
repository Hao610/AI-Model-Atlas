← 返回 [约束与威胁模型](../../CONSTRAINT_THREAT_MODEL_zh.md) | [English Version (24_langchain_llamaindex.md)](24_langchain_llamaindex.md)

---

# 📦 第24章：依赖审计 (Dependency Auditing)

你的应用逻辑可能完美无瑕，但一个过时的AI框架会瞬间危及整个系统。依赖审计是持续保护你的软件供应链，防止已知漏洞污染应用的过程。

## 🥛 “过期食材”比喻

* **类比**： 拿着大师级的食谱做大餐，但用了变质的牛奶，整道菜就毁了。
* **原理**： 在AI开发中，“食材”就是你依赖的第三方框架，如 LangChain、LlamaIndex 或向量数据库客户端。即使你的LLM很安全，这些快速迭代的依赖项中的漏洞也会带来直接风险。
* **核心概念**： 在部署之前，你必须持续检查软件供应链的“保质期”（即CVE漏洞）。

## 📊 快速对比

| 概念 | 传统方式 | LLM 时代 | 影响 |
| :--- | :--- | :--- | :--- |
| **发布速度** | 稳定、更新缓慢的库。 | 极速，框架每天或每周都在发布新版本。 | 快速迭代常常导致安全审查上的疏忽。 |
| **攻击面** | 范围可预测的独立工具。 | 广泛集成外部API、解析器和数据库。 | 单个易受攻击的解析器就可能导致整个智能体瘫痪。 |
| **注入风险** | 标准的 SQL/XSS 防御库。 | 框架负责处理和转义LLM的输入。 | 框架中糟糕的输入处理会为间接提示词注入打开后门。 |

## 🧠 核心概念

1. **维护准确的 SBOM**：在构建过程中生成软件物料清单（SBOM）——你无法保护你不知道存在的东西。
2. **监控 CVE 数据库**：使用自动化工具（如 Dependabot、Snyk）根据常见漏洞与披露（CVE）数据库持续扫描你的代码仓库。
3. **快速打补丁**：当AI工具披露漏洞时，评估影响并立即升级到已修复的版本。
4. **最小依赖原则**：只引入你绝对需要的框架。如果只需要一个函数，请考虑自己实现，而不是引入庞大的库。

## 🛠️ 技术深度探索与落地

像 LangChain 和 LlamaIndex 这样的 AI 框架拥有庞大的依赖树。次级包（例如未打补丁的 PDF 解析器或过时的 API 包装器）深处的漏洞很容易让您的应用程序面临远程代码执行 (RCE) 或敏感数据泄露的风险。

### 1. 自动化 SBOM 生成与漏洞扫描
将依赖审计直接集成到您的 CI/CD 流水线中。使用诸如 Syft（用于生成 SBOM）以及 Grype 或 Snyk（用于漏洞扫描）等工具，确保每次构建都经过审计。

**GitHub Actions YAML (`.github/workflows/ai-dep-audit.yml`):**
```yaml
name: AI Dependency Security Audit

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
  schedule:
    - cron: '0 2 * * *' # 每天凌晨 2 点执行

jobs:
  audit-dependencies:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install safety cyclonedx-bom

      - name: Generate SBOM (CycloneDX)
        run: |
          cyclonedx-py requirements requirements.txt -o sbom.json
          echo "SBOM 生成成功。"

      - name: Run Safety Check (Python Dependencies)
        run: |
          safety check -r requirements.txt --full-report

      - name: Advanced Vulnerability Scan (Trivy)
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          ignore-unfixed: true
          format: 'table'
          severity: 'CRITICAL,HIGH'
```

### 2. 锁定与隔离 AI 框架
永远不要在不锁定确切版本的情况下使用 `langchain` 或 `llama-index`。此外，通过仅显式安装您需要的模块（例如，使用 `langchain-core` 和 `langchain-openai` 而不是庞大的单体 `langchain` 包），剥离未使用的集成。

**`requirements.txt` 最佳实践示例：**
```text
# ❌ 错误做法：拉取数百个未经严格验证的集成包
# langchain>=0.1.0
# llama-index

# ✅ 正确做法：锁定版本的模块化包
langchain-core==0.1.52
langchain-openai==0.1.3
llama-index-core==0.10.30
llama-index-vector-stores-pinecone==0.1.4

# 锁定安全工具版本
safety==3.1.0
```

### 3. CI/CD 治理护栏
对依赖更新实施严格的规则。对于任何涉及 AI 核心框架的更新，都要求人工审核或自动化评估，以防止供应链攻击（例如，拼写错误抢注或包维护者被攻破）。

* **要求签名提交**：确保包更新来自受信任的来源。
* **监控包注册表**：使用相关工具，以便在您的 AI 工具包的代码仓库所有权突然易主或发布模式极不寻常时发出警告。

---

← [上一章](23_prompt_zh.md) | [下一章](25_dspy_textgrad_prompt_zh.md) →
