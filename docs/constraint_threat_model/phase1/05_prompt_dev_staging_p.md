← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (05_prompt_dev_staging_p_zh.md)](05_prompt_dev_staging_p_zh.md)

---

# 📦 Chapter 5: Prompt Version Control & Dynamic Delivery

In modern AI engineering, prompts are critical software assets, not just hardcoded text strings. Treating them like compiled binaries ensures your application stays stable, trackable, and constantly improving.

## 🍳 The Restaurant Recipe Analogy

* **The Analogy**: Deploying a new prompt is exactly like rolling out a new recipe to a global restaurant chain.
* **How it works**: The head chef creates the recipe in a test kitchen (Dev), trials it at a flagship store (Staging), and finally distributes it to all locations (Prod).
* **Key Concept**: If a recipe fails globally, you instantly swap back to the old menu without rebuilding the entire restaurant—just like dynamic prompt rollbacks.

## 📊 Quick Comparison

| Concept | Traditional | LLM Era | Impact |
| --- | --- | --- | --- |
| **Storage** | Hardcoded in source code | Centralized prompt registry | Decouples prompts from application deployments. |
| **Updates** | Requires full app redeploy | Dynamic delivery via API | Instantly push updates without downtime. |
| **Testing** | Unit tests on deterministic logic | A/B testing live traffic | Data-driven performance measurement with real-world tradeoffs. |
| **Failures** | Hotfix code & redeploy | Change a version pointer | Instant rollback in seconds. |

## 🧠 Core Concept

1. **Develop Local Prompts (Dev)**: Engineers experiment with instructions and few-shot examples against predefined test cases.
2. **Test in Staging**: The prompt integrates with app code and faces complex, production-like datasets to catch edge cases.
3. **Deploy Dynamically (Prod)**: Applications fetch the latest active prompt from a centralized system without redeploying.
4. **Monitor & Rollback**: Track outputs for errors or hallucinations, instantly reverting the version pointer if issues arise.

## 🛠️ Technical Deep Dive & Implementation

In modern LLMOps, prompts should be decoupled from application logic. Using an evaluation-driven CI/CD pipeline ensures changes are validated before hitting production.

### Evaluating Prompts in CI/CD (GitHub Actions)

This pipeline demonstrates how to automatically run evaluations on prompt changes. If the new prompt regression tests fail against baseline datasets, the build is blocked.

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
          # Evaluates the updated prompt against the staging dataset
          pf run create --flow ./prompts/customer_support --data ./datasets/staging_test_cases.jsonl --stream

      - name: Assert Evaluation Thresholds
        run: |
          # Custom script to ensure accuracy > 90% and toxicity < 1%
          python scripts/assert_metrics.py --min-accuracy 0.90
```

### Dynamic Delivery (Python Snippet)

Avoid hardcoding. Fetch prompts dynamically from a registry to allow instant rollbacks without redeploying microservices.

```python
import requests

def get_active_prompt(prompt_name: str, environment: str = "prod") -> str:
    """
    Fetches the active prompt template dynamically from a Prompt Registry.
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
        # Fallback to local cache in case of registry outage
        return load_local_fallback(prompt_name)

# Usage
customer_prompt_template = get_active_prompt("customer_support_v2")
# Execute LLM call using the dynamically retrieved template...
```

---

← [Prev Chapter](04_prompt.md) | [Next Chapter](06_system_prompt_tokens.md) →
