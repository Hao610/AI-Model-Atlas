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

1. **Pre-commit Hooks**: Developers run local scans before a commit is even created to catch hardcoded prompts immediately.
2. **Automated CI/CD Integration**: Automated pipelines inspect the diffs of every push for newly introduced prompts and secrets.
3. **Pattern Recognition**: Scanners use regex or lightweight ML to identify structures like `You are an AI assistant...` or `System:`.
4. **Blocking the Leak**: If sensitive data is found, the CI/CD pipeline fails and forces the developer to securely store the template in an environment variable.

---

← [Prev Chapter](../phase3/21_rag_pii.md) | [Next Chapter](23_prompt.md) →
