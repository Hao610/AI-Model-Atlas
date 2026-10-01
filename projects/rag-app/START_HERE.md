# 🚀 Start Here: 1-Minute Quickstart Guide

Welcome to the **Hybrid Cognitive RAG System**! Follow this quick, 7-step guide to run and experience all 4 core interactive modules of the system in action.

---

## 🏃‍♂️ Step 1: Install Dependencies
Ensure you have Python 3.9+ installed, then install the package requirements:
```bash
pip install -r requirements.txt
```

---

## 💻 Step 2: Start Local Models (Default Mode)
If you want to run completely locally and for free, launch Ollama in your background terminal and pull Llama 3:
```bash
ollama pull llama3
```
*(Alternatively, you can switch to cloud API mode in the sidebar at runtime by entering your OpenAI, DeepSeek, or Groq API key).*

---

## 🌐 Step 3: Run the Application
Launch the interactive Streamlit user control panel:
```bash
python app.py
```
This will automatically open your web browser pointing to: `http://localhost:8501`.

> 🎨 **Theme Customization (Obsidian Titanium & Light Precision)**:
> In the top-right corner of the Streamlit interface, click `⋮` -> `Settings` -> `Theme` to toggle between **Dark (Obsidian Titanium)** and **Light (Titanium Precision)**. All panels, charts, metrics, and tactile buttons dynamically adapt to both environments.

---

## 📂 Step 4: Digest a Document
1. Locate the **"📂 Document Context Ingestion"** section on the right side of the page.
2. Drag and drop any PDF file.
3. Watch the system segment, chunk, embed, and index your document into the persistent database.

---

## 💬 Step 5: Test the Interactive RAG Assistant (Tab 1)
1. Locate **Tab 1: 💬 Interactive RAG Assistant** in the centered navigation bar.
2. Type a question in the chat bar and hit send.
3. **Observe Latency**: Notice the token generation speed and the first-token latency (TTFT) metrics logged in the traces.
4. **Trigger Cache Hit**: Re-send the exact same question (or a semantically similar one). You will notice the response outputs **instantly** (0.00s delay) via the **Semantic Cache**.
5. **Tune Settings**: Toggle Reranking or adjust the Similarity Cutoff in the sidebar to see how the system adapts context retrieval in real-time.

---

## ⚡ Step 6: Test TypeSafe Jev System One Decision Gate (Tab 3)
1. In the centered navigation bar, click **Tab 3: ⚡ TypeSafe Jev (System One Gate)**.
2. Select an adversarial or benign preset from the dropdown (or input a custom prompt).
3. Adjust the **Fast-Block (τ_strict)** and **Fast-Pass (τ_safe)** sliders.
4. Click **"Execute Jev System One Screening"** to watch sub-100ms decision primitives (`Noul`, `Choice`, `Score`) triage the request into `FAST_BLOCK`, `FAST_PASS`, or `ESCALATE`.
5. Switch to the **Benchmark Batch Inspector** radio option to evaluate the entire adversarial test dataset against Jev, measuring triage distribution and ~80%+ token cost savings.

---

## ⚖️ Step 7: Run Tool Routing Benchmarks & LLM Quality Judge (Tab 4)
1. In the centered navigation bar, click **Tab 4: ⚖️ Benchmark Evaluation & LLM-as-a-Judge**.
2. **Tool Routing Benchmark Suite**: Click **"🚀 Run Routing Benchmark Suite"** to test deterministic intent classification across math calculation, web freshness, graph relations, and vector lookup with 0 token consumption.
3. **Live RAG Triad Quality Scorer**: Under the single-QA evaluation section, review the query, retrieved context, and generated answer, then click **"⚖️ Execute RAG Triad Evaluation"** to compute quantitative **Faithfulness** (factual consistency) and **Answer Relevancy** scores via an LLM judge.
