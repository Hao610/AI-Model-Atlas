← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (04_prompt_zh.md)](04_prompt_zh.md)

---

# 🧩 Chapter 4: Prompt as Code (Decoupling Prompts)

Hardcoding prompts into your application logic is a poor fit for the LLM era. By treating prompts as versioned assets, you can improve iteration speed and let domain experts tune AI behavior without touching source code.

## 🤖 The Robot Analogy

* **The Analogy**: Imagine wiring day-to-day operational rules directly into a robot's physical brain circuits versus handing it a swappable rulebook.
* **How it works**: If you hardcode rules, you need a hardware engineer with a soldering iron to change behaviors. If you use a rulebook, anyone who understands the factory rules can swap out the instructions instantly.
* **Key Concept**: Application code should only know *how* to read and execute instructions, while the prompts themselves live externally as easily modified assets.

## 📊 Quick Comparison

| Concept | Traditional | LLM Era | Impact |
| :--- | :--- | :--- | :--- |
| **Logic Storage** | Embedded directly in source code | Extracted into YAML/JSON files | Enables non-technical experts to iterate |
| **Update Cycle** | Requires full CI/CD deployment | Deployed independently as assets | Faster time-to-market for prompt updates |
| **Versioning** | Tangled with application code history | Managed as distinct versioned assets | Easy rollbacks and A/B testing |
| **Reusability** | Locked into specific code paths | Shareable across multiple features | Standardized behavior across the app |

## 🧠 Core Concept

1. **Decouple Prompts**: Move all prompt instructions out of Python files and into structured formats like YAML or JSON.
2. **Version as Assets**: Track your external prompt files in version control, treating them with the same rigor as code configurations.
3. **Separate Lifecycles**: Allow your core application code and your prompt rules to be updated, tested, and deployed independently.
4. **Empower Experts**: Give prompt engineers and subject matter experts direct access to modify prompt assets without navigating complex codebases.

## 🛠️ Technical Deep Dive & Implementation

By decoupling prompts into version-controlled assets, we introduce rigor into the Prompt Engineering lifecycle.

**1. Loading Prompts via YAML (Python)**
Instead of inline string concatenation, manage prompts centrally using YAML.
```python
import yaml
from langchain.prompts import PromptTemplate

def load_prompt_asset(file_path: str) -> PromptTemplate:
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)
    return PromptTemplate(
        input_variables=data["input_variables"],
        template=data["template"]
    )
```

**2. Automated Prompt Validation (GitHub Actions)**
A CI/CD pipeline ensures prompt changes don't break downstream logic or exceed token limits before deployment.
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

← [Prev Chapter](03_zero_trust.md) | [Next Chapter](05_prompt_dev_staging_p.md) →
