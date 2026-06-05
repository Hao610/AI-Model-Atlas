# 前端界面极速生成 🎨

[[English] (18_ui_interfaces.md)](18_ui_interfaces.md) | [中文]

在终端黑框里运行代码对于开发者来说很亲切，但普通用户需要一个美观的网页聊天框来使用你的模型。

在 Python 生态中，你完全不需要掌握复杂的 HTML、CSS 或 JavaScript，就能在几分钟内搭建出一个精美的网页前端。这要归功于 **Streamlit**。

---

## 🛠️ 第一步：安装 Streamlit 框架

打开命令行，输入以下命令安装：

```bash
pip install streamlit openai
```

---

## 🐍 第二步：编写 Streamlit 聊天网页代码

新建一个名为 `app.py` 的文件，写入以下代码：

```python
import streamlit as st
from openai import OpenAI

# 设置网页标签与标题
st.set_page_config(page_title="AI聊天助手", page_icon="🤖")
st.title("🤖 专属 AI 聊天助理")

# 在系统会话状态中初始化历史聊天记录
if "messages" not in st.session_state:
    st.session_state.messages = []

# 循环渲染历史对话内容
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 捕获用户在输入框的文字输入
if user_input := st.chat_input("说点什么吧..."):
    # 将用户提问存入历史记录并渲染
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 初始化本地大模型客户端（以本地 Ollama 为例）
    client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
    
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # 启用流式传输 (Stream) 获取打字机效果的回复
        response = client.chat.completions.create(
            model="llama3.2:3b",
            messages=st.session_state.messages,
            stream=True
        )
        
        for chunk in response:
            if chunk.choices[0].delta.content:
                full_response += chunk.choices[0].delta.content
                message_placeholder.markdown(full_response + "▌") # 模拟光标
        
        message_placeholder.markdown(full_response) # 渲染最终完整文本
        
    # 将 AI 的回复存入历史记录
    st.session_state.messages.append({"role": "assistant", "content": full_response})
```

---

## 🚀 第三步：启动你的网页应用

在命令行中输入以下命令运行（**特别注意**：请使用 `streamlit run`，而不是 `python app.py`）：

```bash
streamlit run app.py
```

系统会瞬间自动在你的浏览器中弹出一个新标签页（地址通常为 `http://localhost:8501`），展示你刚才写好的具备打字机效果的私人聊天网页！

---

## 🆚 Streamlit vs. Gradio

在 Python AI 界，除了 Streamlit，另一个极其有名的前端框架是 **Gradio**。

| 维度 | Streamlit | Gradio |
| :--- | :--- | :--- |
| **最适合的场景** | 完整的仪表盘看板、多页面客服系统、数据分析应用。 | 机器学习模型的快速 Demo 演示（如一键上传图片分类、音频去噪）。 |
| **页面布局** | 偏向于经典的网页布局，文字渲染美观，排版极其灵活。 | 支持左右分栏（左侧输入参数，右侧显示结果），设计直观。 |
| **生态背景** | 拥有数百个社区插件（图表、地图、进度条）。 | 获得 Hugging Face 的官方支持，能一键托管到 Hugging Face Spaces。 |

---

拥有了前端界面，接下来让我们去了解如何使用代码开发复杂的“多智能体协同系统”：进入 [智能体开发框架](19_agent_frameworks_zh.md)。
