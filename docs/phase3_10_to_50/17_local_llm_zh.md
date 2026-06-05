# 本地大模型运行指南 🖥️

[[English] (17_local_llm.md)](17_local_llm.md) | [中文]

如果你的电脑无法联网、对数据隐私有 100% 的严格要求，或者单纯不想支付 API 接口费，该怎么办？你可以将大语言模型下载下来，直接跑在自己的电脑上。

得益于开源社区的迅猛发展，现在在本地运行模型就像双击安装一个普通软件一样简单。

---

## 🏎️ 工具一：Ollama (终端命令行神器)

**Ollama** 是目前最火的本地大模型运行框架。它作为轻量级后台服务运行，并且会在本地自动搭建一个兼容 OpenAI 格式的 API 服务器。

### 1. 安装与首次运行
1. 前往 [ollama.com](https://ollama.com) 下载对应你系统的安装包并安装。
2. 打开你的命令行（Terminal 或 CMD），输入以下命令并回车：
   ```bash
   ollama run llama3.2:3b
   ```
3. Ollama 会自动开始下载模型参数文件（约 2GB 大小）。下载完成后，你就能直接在终端里和它开始聊天了。

### 2. Ollama 常用命令表

| 常用命令 | 功能描述 |
| :--- | :--- |
| `ollama run <模型名称>` | 下载并运行模型，直接进入终端聊天模式。 |
| `ollama pull <模型名称>` | 仅下载模型到本地，不立即运行。 |
| `ollama list` | 列出你本地已经下载的所有模型。 |
| `ollama rm <模型名称>` | 删除某个本地模型以释放硬盘空间。 |

---

## 🎨 工具二：LM Studio (可视化图形界面首选)

如果你讨厌命令行黑框，更想要一个类似 ChatGPT 网页端那样美观、带聊天历史记录的客户端，**LM Studio** 是最佳选择。

1. 前往 [lmstudio.ai](https://lmstudio.ai) 下载并安装。
2. 打开软件，在内置的应用商店搜索栏输入 **“Llama 3.2”** 或 **“DeepSeek-R1-Distill”**，点击 **Download** 下载。
3. 进入左侧 Chat（聊天面板），在顶部下拉菜单选择你刚才下载好的模型，就能立即开始对话。
4. **一键启动 API 服务器**：在左侧 Local Server 面板，你可以开启本地服务，端口默认为 `1234`。这个本地服务的接口格式与 OpenAI 官方 API 保持 100% 一致！

---

## 🐍 用 Python 代码调用本地模型

当你运行 Ollama 时，它会在后台运行一个本地接口，地址是 `http://localhost:11434/v1`。你可以把你的 Python 代码重定向到你自己的电脑，不需要花一分钱接口费：

```python
from openai import OpenAI

# 将 client 客户端指向你本地的 Ollama 服务
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # 本地运行不需要真的Key，随便填一个占位即可
)

response = client.chat.completions.create(
    model="llama3.2:3b",  # 确保你本地已经通过 ollama pull 下载了该模型
    messages=[
        {"role": "user", "content": "为什么天空是蓝色的？"}
    ]
)

print(response.choices[0].message.content)
```

---

现在你已经可以在本地或云端调用大模型了。接下来，让我们为我们的 Python 脚本套上一个精美的网页聊天界面：进入 [前端界面极速生成](18_ui_interfaces.md)。
