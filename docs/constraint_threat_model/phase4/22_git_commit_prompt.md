← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (22_git_commit_prompt_zh.md)](22_git_commit_prompt_zh.md)

---

# 🛡️ Chapter 22: Git Commit Scanning

Hardcoded prompt templates and API keys are ticking time bombs in your codebase. Stop intellectual property leaks at the source by inspecting your commits before they ever reach version control.

## 💂 The Security Guard Analogy

* **The Analogy**: Before you leave a top-secret facility, a security guard checks your backpack to make sure you aren't walking out with sensitive company documents.
* **How it works**: Git commit scanning acts as the security guard for your codebase, automatically inspecting outgoing changes to prevent accidental exposure of your secrets.
* **Key Concept**: Catching hardcoded prompt templates and AI keys early prevents proprietary logic leaks and mitigates prompt injection vulnerabilities.

## 📊 Quick Comparison

| Concept | Traditional | LLM Era | Impact |
| --- | --- | --- | --- |
| **Secrets in Code** | Passwords and database credentials | AI API keys and system prompt instructions | Hardcoded prompts expose core constraints and proprietary logic. |
| **Leak Prevention** | Basic regex for API keys | Semantic scanning for LLM template structures | Prevents prompt injection blueprints from falling into attacker hands. |
| **Security Checkpoint** | Reactive security audits | Automated Pre-commit hooks & CI/CD checks | Blocks sensitive AI data before it even enters version control. |

## 🧠 Core Concept

1. **Pre-commit Hooks**: Developers run local scans before a commit is created to catch hardcoded prompts early.
2. **Automated CI/CD Integration**: Automated pipelines inspect the diffs of every push for newly introduced prompts and secrets.
3. **Pattern Recognition**: Scanners use regex or lightweight ML to identify structures like `You are an AI assistant...` or `System:`.
4. **Blocking the Leak**: If sensitive data is found, the CI/CD pipeline fails and forces the developer to securely store the template in an environment variable.

## 🛠️ Technical Deep Dive & Implementation

Securing the supply chain of AI applications requires robust operational (Ops/CI) guardrails. Hardcoded system prompts act as a blueprint for attackers to reverse-engineer your defenses.

### 1. Custom Pre-commit Hook for Prompt Detection

You can use custom regular expressions in a pre-commit hook or secrets scanning tool to identify potentially hardcoded prompt instructions.

**`.pre-commit-config.yaml` Snippet:**
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
        entry: bash -c 'git grep -E -i "(You are an AI|System Prompt:|Answer as a helpful assistant)" --cached && echo "🚨 Hardcoded prompts detected!" && exit 1 || exit 0'
        language: system
        pass_filenames: false
```

### 2. Automated Secret and Prompt Scanning in CI/CD

Integrate tools like [TruffleHog](https://github.com/trufflesecurity/trufflehog) or [Gitleaks](https://github.com/gitleaks/gitleaks) directly into your CI pipeline. You can extend their default rule sets to detect proprietary LLM framework patterns (e.g., LangChain template strings).

**GitHub Actions Pipeline (`.github/workflows/ai-security-scan.yml`):**
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
          echo "Scanning diffs for hardcoded LangChain/LlamaIndex system templates..."
          # Sanitized pattern matching for prompt leaks
          if git diff origin/main..HEAD | grep -iE 'PromptTemplate|SystemMessage|ChatPromptTemplate\.from_messages'; then
            echo "⚠️  WARNING: Prompt templates found in commit diff. Ensure proprietary instructions are stored securely (e.g., AWS Parameter Store, HashiCorp Vault) and not hardcoded."
            # Uncomment to block build: exit 1
          fi
```

### 3. Mitigation Strategy
- **Externalize Prompts:** Store system prompts in centralized configuration management (e.g., Azure App Configuration, AWS Systems Manager) or a dedicated database.
- **Use Identifiers:** In your codebase, reference prompts by an ID rather than hardcoding the raw string.
- **Sanitize Logs:** Ensure CI/CD pipelines strip out the actual prompt text if a failure occurs during template evaluation.

---

← [Prev Chapter](../phase3/21_rag_pii.md) | [Next Chapter](23_prompt.md) →
