# UI Interfaces with Streamlit 🎨

[English] | [中文 (ui_interfaces_zh.md)](ui_interfaces_zh.md)

Running code in the terminal is fine for developers, but users want a clean web page to chat with your model. 

In the Python ecosystem, you don't need to know HTML, CSS, or JavaScript to build a web interface. You can use **Streamlit** to create a stunning frontend in just a few lines of Python.

---

## 🛠️ Step 1: Install Streamlit

Open your terminal and run:

```bash
pip install streamlit openai
```

---

## 🐍 Step 2: Write the Streamlit App

Create a file named `app.py` and write the following code:

```python
import streamlit as st
from openai import OpenAI

# Page title
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 My Custom AI Assistant")

# Initialize chat history in session memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if user_input := st.chat_input("Ask me anything..."):
    # Add user message to state
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call LLM (using Ollama locally as an example)
    client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
    
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Get streaming response
        response = client.chat.completions.create(
            model="llama3.2:3b",
            messages=st.session_state.messages,
            stream=True
        )
        
        for chunk in response:
            if chunk.choices[0].delta.content:
                full_response += chunk.choices[0].delta.content
                message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
        
    # Save AI response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
```

---

## 🚀 Step 3: Run Your Web Interface

In your terminal, run the following command (do not use `python app.py`):

```bash
streamlit run app.py
```

A browser tab will instantly open at `http://localhost:8501` showing your custom chatbot web interface with message streaming!

---

## 🆚 Streamlit vs. Gradio

| Feature | Streamlit | Gradio |
| :--- | :--- | :--- |
| **Best Used For** | Full dashboard apps, analytical business tools, multi-page customer chatbots. | Quick machine learning model demos (image classification, audio processing). |
| **Custom Styling** | Highly structured, clean modern aesthetics out-of-the-box. | Easier to create side-by-side input/output panels. |
| **Ecosystem** | Very large, hundreds of custom plugins (charts, maps). | Officially backed by Hugging Face (great for hosting on Hugging Face Spaces). |

---

Now that you can build user interfaces, let's explore developer agent frameworks to create multi-agent systems in [Agent Frameworks](agent_frameworks.md).
