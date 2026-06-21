← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (24_langchain_llamaindex_zh.md)](24_langchain_llamaindex_zh.md)

---

# 📦 Chapter 24: Dependency Auditing

Your application logic might be flawless, but an outdated AI framework can instantly compromise your entire system. Dependency auditing is the continuous process of securing your software supply chain before known vulnerabilities taint your app.

## 🥛 The "Expired Ingredients" Analogy

* **The Analogy**: Cooking a gourmet meal with a master recipe but using spoiled milk ruins the dish.
* **How it works**: In AI development, your "ingredients" are third-party frameworks like LangChain, LlamaIndex, or vector DB clients. Even if your LLM is secure, a vulnerability in these fast-moving dependencies introduces direct risk.
* **Key Concept**: You must continuously check the "expiration dates" (CVEs) of your software supply chain before deploying.

## 📊 Quick Comparison

| Concept | Traditional | LLM Era | Impact |
| :--- | :--- | :--- | :--- |
| **Release Speed** | Stable, slow-moving library updates. | Breakneck, daily/weekly framework releases. | Rapid iteration frequently introduces security oversights. |
| **Attack Surface** | Self-contained utilities with predictable scope. | Massive integrations with external APIs, parsers, and DBs. | A single vulnerable parser can compromise the entire agent. |
| **Injection Risks** | Standard SQL/XSS prevention libraries. | Frameworks handle LLM input parsing and escaping. | Poor input handling in frameworks opens doors to indirect prompt injections. |

## 🧠 Core Concept

1. **Maintain an Accurate SBOM**: Generate a Software Bill of Materials (SBOM) during your build process—you can't secure what you don't know you have.
2. **Monitor CVE Databases**: Use automated tools (Dependabot, Snyk) to continuously scan your repository against Common Vulnerabilities and Exposures (CVE) databases.
3. **Patch Promptly**: When a vulnerability is disclosed in an AI tool, assess the impact and upgrade to the patched version as soon as practical.
4. **Minimal Dependency Principle**: Only include the frameworks you absolutely need. If you only require one function, consider implementing it yourself rather than importing a massive library.

## 🛠️ Technical Deep Dive & Implementation

AI frameworks like LangChain and LlamaIndex have massive dependency trees. A vulnerability deep in a secondary package (like an unpatched PDF parser or an outdated API wrapper) can easily expose your application to remote code execution (RCE) or sensitive data leaks.

### 1. Automated SBOM Generation and Vulnerability Scanning
Integrate dependency auditing directly into your CI/CD pipeline. Use tools like Syft (for SBOM generation) and Grype or Snyk (for vulnerability scanning) to ensure every build is audited.

**GitHub Actions YAML (`.github/workflows/ai-dep-audit.yml`):**
```yaml
name: AI Dependency Security Audit

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
  schedule:
    - cron: '0 2 * * *' # Daily at 2 AM

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
          echo "SBOM generated successfully."

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

### 2. Pinning and Isolating AI Frameworks
Never use `langchain` or `llama-index` without pinning exact versions. Furthermore, strip out unused integrations by explicitly installing only what you need (e.g., `langchain-core` and `langchain-openai` instead of the monolithic `langchain` package).

**Example `requirements.txt` Best Practices:**
```text
# ❌ BAD: Pulls in hundreds of unverified integrations
# langchain>=0.1.0
# llama-index

# ✅ GOOD: Pinned, modular packages
langchain-core==0.1.52
langchain-openai==0.1.3
llama-index-core==0.10.30
llama-index-vector-stores-pinecone==0.1.4

# Pinned security tools
safety==3.1.0
```

### 3. CI/CD Governance Guardrails
Enforce strict rules on dependency updates. Require human review or automated evaluation for any update involving AI core frameworks to prevent supply chain attacks (e.g., typosquatting or compromised package maintainers).

* **Require Signed Commits**: Ensure package updates come from trusted sources.
* **Monitor Package Registries**: Use tools that flag sudden changes in repository ownership or highly unusual release patterns for your AI tools.

---

← [Prev Chapter](23_prompt.md) | [Next Chapter](25_dspy_textgrad_prompt.md) →
