← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (04_prompt_zh.md)](04_prompt_zh.md)

---

# 🧩 Chapter 4: Prompt as Code (Decoupling Prompts)

Hardcoding prompts into your application logic is the ultimate anti-pattern in the LLM era. By treating prompts as versioned assets, you unlock faster iteration and empower domain experts to optimize AI behavior without touching source code.

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

---

← [Prev Chapter](03_zero_trust.md) | [Next Chapter](05_prompt_dev_staging_p.md) →
