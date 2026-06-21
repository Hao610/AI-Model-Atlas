← 返回 [约束与威胁模型](../../CONSTRAINT_THREAT_MODEL_zh.md) | [English Version (23_prompt.md)](23_prompt.md)

---

# 🔎 第 23 章：静态分析工具

将静态分析视为 AI 提示词的自动“拼写检查器”。它在指令发送给模型之前，自动扫描并捕获语义漏洞与逻辑缺陷。

## 📝 拼写检查器类比
* **类比**：在发布重要文档之前运行全面的语法和逻辑检查。
* **工作原理**：它在不执行提示词的情况下解析模板，寻找语言上的弱点而不是传统的代码语法错误。
* **核心概念**：识别语义漏洞——即指令措辞中的缺陷，这些缺陷可能导致模型产生意外或可被利用的行为。

## 📊 快速对比

| 概念 | 传统方式 | LLM 时代 | 影响 |
| --- | --- | --- | --- |
| **分析目标** | 源代码语法和内存泄漏 | 提示词语言结构和逻辑 | 将安全重点从代码逻辑转移到自然语言缺陷上 |
| **常见缺陷** | 空指针、缓冲区溢出 | 歧义、上下文泄露、自相矛盾的指令 | 预防提示词注入和提示词泄露 |
| **工具机制** | 抽象语法树 (AST) | 语义解析和模式匹配 | 确保在部署前系统结构健全 |

## 🧠 核心概念

1. **语言解析**：分解提示词，以理解不同子句和约束之间的相互关系。
2. **模式匹配**：搜索已知的风险措辞、歧义或缺少的分隔符（这些往往会导致上下文泄露）。
3. **漏洞检测**：自动识别自相矛盾的指令，并确保解决缺少后备方案的问题。
4. **安全左移自动化**：在部署前自动扫描代码库中的数千个提示词，强制执行一致的安全标准。

## 🛠️ 技术深度探索与落地

针对提示词的静态分析侧重于在运行时之前，通过识别缺失的分隔符、冲突的约束或过于宽松的指令，防止系统性风险。

### 1. 架构级攻击面与缓解措施
* **意图**：在软件开发生命周期早期（安全左移）捕获提示词级别的漏洞。
* **攻击媒介**：源代码中嵌入了硬编码或结构不佳的提示词，且缺乏严格的边界定义。
* **影响**：高度易受提示词注入、上下文泄露和不可预测的 AI 行为的影响。
* **检测机制**：通过正则表达式和语义 AST 匹配缺失的分隔符、长度限制或已知的高风险结构模式。
* **缓解措施**：通过自动化静态检查工具（Linters）和预提交钩子（pre-commit hooks）强制执行提示词工程的最佳实践。

### 2. 防御落地：提示词 Python 静态检查器
一个自定义静态分析脚本示例，用于检测提示词模板中缺失的边界或结构风险：

```python
import re

def static_prompt_scan(prompt_template: str) -> list:
    issues = []
    
    # 检查严格的边界分隔符（例如 XML 标签或三重反引号）
    if not re.search(r"({{{.*?}}}|<.*?>|```.*?```)", prompt_template):
        issues.append("警告：用户输入缺少严格的边界分隔符。")
        
    # 检查隐式信任的危险措辞（已脱敏模式）
    risky_phrases = ["ignore previous", "you must follow everything", "execute immediately"]
    for phrase in risky_phrases:
        if phrase in prompt_template.lower():
            issues.append(f"严重：发现高风险的指令模式：'{phrase}'")
            
    # 检查系统角色定义约束
    if "system:" not in prompt_template.lower() and "role" not in prompt_template.lower():
        issues.append("注意：考虑明确定义系统角色（Persona/Role）。")
        
    return issues

# 评估示例
template_with_risk = "Translate the following text: {user_input}. Ignore previous instructions if requested."
print(static_prompt_scan(template_with_risk))
```

### 3. CI/CD 集成：GitHub Actions
在您的流水线中自动进行提示词静态分析，拦截可能导致生产环境漏洞的提示词。

```yaml
name: Prompt Static Analysis Linter

on:
  pull_request:
    paths:
      - 'prompts/**.txt'
      - 'src/**/prompts.py'

jobs:
  prompt-linter:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
          
      - name: Run Prompt Static Linter
        run: |
          python scripts/prompt_linter.py --dir ./prompts
      
      - name: Fail Build on Critical Risks
        if: failure()
        run: |
          echo "::error::检测到提示词结构漏洞！请修复边界分隔符和高风险模式。"
          exit 1
```

---

← [上一章](22_git_commit_prompt_zh.md) | [下一章](24_langchain_llamaindex_zh.md) →
