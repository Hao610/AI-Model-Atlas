# Real-World AI Use Cases 💼

[English] | [中文 (use_cases_zh.md)](use_cases_zh.md)

Let's look at how the **Agent + RAG + LLM** workflow is applied to solve real business problems. Below are six core templates of the most common AI projects in the industry.

---

## 🤖 1. Customer Support Assistant

* **Goal**: Answer repetitive customer tickets automatically 24/7 without human intervention.
* **The Architecture**:
  * **Knowledge**: Company FAQ PDFs, refund policies, and shipping rules.
  * **Tools**: Order tracking API, human hand-off trigger (sends a Slack alert if the user demands a human agent).
  * **System Prompt**: *"Act as a friendly retail support agent. You are helpful, polite, and only answer questions based on the uploaded FAQ. Never guess order tracking numbers; always use the tracking tool."*

---

## 📂 2. Enterprise Knowledge Base

* **Goal**: Help internal employees find information inside hundreds of pages of engineering specs, HR policies, or legal documents.
* **The Architecture**:
  * **Knowledge**: PDF libraries containing hundreds of internal policy documents.
  * **Database**: PostgreSQL with `pgvector` extension.
  * **System Prompt**: *"You are the internal HR assistant. Cite the specific document name and section when answering employee questions (e.g. 'According to HR-Handbook-2026, Section 4.2...')."*

---

## ✍️ 3. AI Writing Assistant

* **Goal**: Co-write marketing emails, blog posts, and advertisements matching a company's specific brand voice.
* **The Architecture**:
  * **Knowledge**: Brand style guides, past successful marketing emails (few-shot samples).
  * **Workflow**: A multi-step pipeline where Step 1 generates an outline, Step 2 draft the copy, and Step 3 reviews the copy for tone.
  * **System Prompt**: *"You are a senior copywriter. Keep the tone punchy, energetic, and highly readable. Avoid using cliché buzzwords like 'synergy', 'revolutionize', or 'game-changing'."*

---

## 🌍 4. Context-Aware AI Translator

* **Goal**: Go beyond raw literal translation (like Google Translate) and translate slang, technical jargon, and idioms accurately.
* **The Architecture**:
  * **Knowledge**: Industry-specific glossaries (e.g. medical terms or software coding slang).
  * **Workflow**: Few-shot examples demonstrating context-aware translations.
  * **System Prompt**: *"Translate this software document from English to Chinese. Make sure terms like 'container' are translated as '容器' (Docker context), not '货柜' (shipping context)."*

---

## 📊 5. AI Data Analyst

* **Goal**: Allow non-technical managers to query databases using plain English.
* **The Architecture**:
  * **Knowledge**: Database schema layouts (table names, column definitions).
  * **Tools**: Python code runner execution sandbox.
  * **Workflow**: 
    1. User asks a question in English.
    2. LLM writes a SQL query or Python pandas script.
    3. The system runs the code in a secure sandbox.
    4. The LLM reads the result and formats it into a neat markdown chart.

---

Congratulations! You have completed **Phase 2 (1 to 10)**. You now understand how AI workflows and architectures solve actual business problems.

Next, let's step into **Phase 3 (10 to 50)** and write some Python code to interface directly with these models in [API Integration](../phase3_10_to_50/api_guide.md).
