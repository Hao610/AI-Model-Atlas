← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (27_github_actions_zh.md)](27_github_actions_zh.md)

---

# 🛑 Chapter 27: Gateway Interceptors (GitHub Actions)

Stop prompt injections and jailbreaks before they ever reach production. Welcome to CI/CD for AI security.

## 🛂 The Airport Security Analogy
* **The Analogy**: CI/CD Gateway Interceptors are like airport passport control and security scanners.
* **How it works**: Before your code can "board the flight" to production, it must pass through automated checks that scan for contraband (vulnerabilities).
* **Key Concept**: You catch weak system prompts and missing safeguards during the build phase, preventing proactive threats altogether.

## 📊 Quick Comparison

| Concept | Traditional | LLM Era | Impact |
| --- | --- | --- | --- |
| **Linting** | Syntax checks, unused variables. | Prompt scanning, safeguard validation. | Catches risky instructions. |
| **Testing** | Unit testing logic. | Automated adversarial testing (red teaming). | Blocks known jailbreaks. |
| **Fail State** | Fails on broken code. | Fails on insecure prompt configurations. | Prevents vulnerable deployments. |

## 🧠 Core Concept

1. **Shift-Left Security:** Integrate prompt vulnerability scanners directly into your Pull Request workflows.
2. **Automated Enforcement:** CI/CD pipelines automatically evaluate system prompts and model parameters.
3. **Adversarial Testing:** Run automated suites that attempt to jailbreak the local staging models.
4. **Auditability:** Generate security logs for every build, proving that safeguards were checked and passed.

## 🛠️ Technical Deep Dive & Implementation

To build an effective AI Security Gateway, you need a multi-layered automated defense mechanism inside your CI pipeline. We validate static prompts (Prompt Linting) and dynamically test the application via synthetic adversarial evaluation.

### GitHub Actions: The AI DevSecOps Pipeline

The following workflow demonstrates how to integrate static analysis and dynamic adversarial testing via Promptfoo or pytest into your CI/CD process.

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

      - name: 🛡️ Step 1 - Static Prompt Analysis
        # Checks for hardcoded API keys or dangerously broad system prompts
        run: |
          detect-secrets scan ./app/prompts/ > secrets_report.json
          python scripts/lint_prompts.py ./app/prompts/

      - name: 🧪 Step 2 - Dynamic Adversarial Testing (Local Staging)
        # Evaluates the LLM endpoints using predefined sanitized payloads
        # e.g., Pattern: "Ignore previous instructions..." (sanitized)
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          STAGING_ENDPOINT: "http://localhost:8000/v1/chat"
        run: |
          # Example: using promptfoo for evaluation
          promptfoo eval -c tests/adversarial/promptfoo.yaml --output eval_results.json
          
      - name: 🚦 Step 3 - Gatekeeper Policy Enforcement
        # Fail the build if the pass rate is below the 95% threshold
        run: |
          python scripts/enforce_threshold.py eval_results.json --min-pass-rate 0.95
```

### Evaluation Script Snippet (`enforce_threshold.py`)

A simple script to parse the evaluation outputs and block merging if security regressions are detected.

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
        print("❌ No adversarial tests were executed. Failing the build.")
        sys.exit(1)
        
    pass_rate = passed_tests / total_tests
    print(f"📊 LLM Security Pass Rate: {pass_rate*100:.2f}%")
    
    if pass_rate < min_pass_rate:
        print(f"❌ Security Threshold Failed. Required: {min_pass_rate*100}%, Actual: {pass_rate*100:.2f}%")
        print("⚠️ Possible prompt injection vulnerabilities detected. Review evaluation logs.")
        sys.exit(1)
        
    print("✅ All LLM security checks passed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('results', help='Path to evaluation results JSON')
    parser.add_argument('--min-pass-rate', type=float, default=0.95)
    args = parser.parse_args()
    
    enforce_security_threshold(args.results, args.min_pass_rate)
```

---

← [Prev Chapter](26_automated_red_teamin.md) | [Next Chapter](28_safety_judge.md) →
