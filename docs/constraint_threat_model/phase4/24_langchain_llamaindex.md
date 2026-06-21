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
3. **Patch Rapidly**: When a vulnerability is disclosed in an AI tool, assess the impact and upgrade to the patched version immediately.
4. **Minimal Dependency Principle**: Only include the frameworks you absolutely need. If you only require one function, consider implementing it yourself rather than importing a massive library.

---

← [Prev Chapter](23_prompt.md) | [Next Chapter](25_dspy_textgrad_prompt.md) →
