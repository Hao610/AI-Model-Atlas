# 🚀 Start Here: 1-Minute Quickstart Guide

Welcome to the **Hybrid Cognitive RAG System**! Follow this quick, 5-step guide to run and experience the system in action.

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
*(Alternatively, you can switch to cloud API mode in the sidebar at runtime by entering your OpenAI or DeepSeek API key).*

---

## 🌐 Step 3: Run the Application
Launch the interactive Streamlit user control panel:
```bash
python app.py
```
This will automatically open your web browser pointing to: `http://localhost:8501`.

---

## 📂 Step 4: Digest a Document
1. Locate the **"📂 Document Context Ingestion"** section on the right side of the page.
2. Drag and drop any PDF file.
3. Watch the system segment, chunk, embed, and index your document into the persistent database.

---

## 💬 Step 5: Test the Intelligence & Performance
1. Type a question in the chat bar and hit send.
2. **Observe Latency**: Notice the token generation speed and the first-token latency (TTFT) metrics logged in the traces.
3. **Trigger Cache Hit**: Re-send the exact same question (or a semantically similar one). You will notice the response outputs **instantly** (0.00s delay) via the **Semantic Cache**.
4. **Tune Settings**: Toggle Reranking or adjust the Similarity Cutoff in the sidebar to see how the system adapts context retrieval in real-time.
