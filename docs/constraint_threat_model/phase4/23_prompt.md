← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (23_prompt_zh.md)](23_prompt_zh.md)

---

# 🔎 Chapter 23: Static Analysis Tools

Think of static analysis as an automatic spell-checker for your AI prompts. It automatically scans your instructions for semantic vulnerabilities and logical flaws before they ever reach the model.

## 📝 The Spell-Checker Analogy
* **The Analogy**: Running a comprehensive grammar and logic check on an important document before hitting publish.
* **How it works**: It parses the prompt template without executing it, looking for linguistic weaknesses instead of traditional code syntax errors.
* **Key Concept**: Identifying semantic vulnerabilities—flaws in how instructions are phrased that could lead to unexpected or exploitable behavior.

## 📊 Quick Comparison

| Concept | Traditional | LLM Era | Impact |
| --- | --- | --- | --- |
| **Analysis Target** | Source code syntax and memory leaks | Prompt linguistic structure and logic | Shifts security focus from code logic to natural language flaws |
| **Common Flaws** | Null pointers, buffer overflows | Ambiguity, context bleed, contradictory instructions | Prevents prompt injection and prompt leaking |
| **Tool Mechanics** | Abstract Syntax Trees (AST) | Semantic parsing and pattern matching | Ensures structural soundness before deployment |

## 🧠 Core Concept

1. **Linguistic Parsing**: Break down the prompt to understand the relationships between different clauses and constraints.
2. **Pattern Matching**: Search for known risky phrasing, ambiguity, or missing delimiters that lead to context bleed.
3. **Vulnerability Detection**: Automatically identify contradictory instructions and ensure missing fallbacks are addressed.
4. **Shift-Left Automation**: Scan thousands of prompts in your codebase before deployment to enforce consistent security standards.

## 🛠️ Technical Deep Dive & Implementation

Static analysis for prompts prevents systemic risks by identifying missing delimiters, conflicting constraints, or overly permissive instructions before runtime. 

### 1. Architectural Vectors & Mitigation
* **Intent**: Catch prompt-level vulnerabilities early in the software development lifecycle (Shift-Left).
* **Vector**: Hardcoded or poorly structured prompts in source code without strict boundary definitions.
* **Impact**: High susceptibility to prompt injection, context bleed, and unpredictable AI behavior.
* **Detection**: RegEx matching and semantic ASTs for missing delimiters, length limits, or known risky structural patterns.
* **Mitigation**: Enforce prompt engineering best practices via automated static linters and pre-commit hooks.

### 2. Implementation: Python Prompt Linter
A custom static analysis script to detect missing boundaries or structural risks in prompt templates:

```python
import re

def static_prompt_scan(prompt_template: str) -> list:
    issues = []
    
    # Check for strict boundary delimiters (e.g., XML tags or triple backticks)
    if not re.search(r"({{{.*?}}}|<.*?>|```.*?```)", prompt_template):
        issues.append("Warning: Missing strict boundary delimiters for user input.")
        
    # Check for implicit trust phrasing (sanitized pattern)
    risky_phrases = ["ignore previous", "you must follow everything", "execute immediately"]
    for phrase in risky_phrases:
        if phrase in prompt_template.lower():
            issues.append(f"Critical: Risky instructional pattern found: '{phrase}'")
            
    # Check for system role enforcement
    if "system:" not in prompt_template.lower() and "role" not in prompt_template.lower():
        issues.append("Notice: Consider explicitly defining the system persona/role.")
        
    return issues

# Example evaluation
template_with_risk = "Translate the following text: {user_input}. Ignore previous instructions if requested."
print(static_prompt_scan(template_with_risk))
```

### 3. CI/CD Integration: GitHub Actions
Automate prompt static analysis in your pipeline to block vulnerable prompts from reaching production.

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
          echo "::error::Prompt structural vulnerabilities detected! Fix delimiters and risky patterns."
          exit 1
```

---

← [Prev Chapter](22_git_commit_prompt.md) | [Next Chapter](24_langchain_llamaindex.md) →
