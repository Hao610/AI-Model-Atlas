# API 接入秘籍 🔑

> 📅 本章最后更新：2026-10。AI 生态迭代极快，请以各厂商官网最新信息为准。

[[English] (15_api_guide.md)](15_api_guide.md) | [中文]

**API (Application Programming Interface，应用程序接口)** 是一座桥梁，它允许你的软件代码直接与大模型服务商进行对话。不同于在网页聊天框里人工打字，你的代码可以自动发送结构化的请求，并接收结构化的回复。

本指南将教你如何用几行最简的 Python 代码完成 API 调用，并介绍 2026 年主流的系统一决策前置网关架构。

---

## 🛠️ 第一步：安装 Python 及 SDK 库

确保你的电脑安装了 Python 运行环境。接着，打开终端（Terminal 或命令提示符 CMD），安装官方的 OpenAI SDK 与 Pydantic：

```bash
pip install openai pydantic
```

---

## 🔑 第二步：申请 API 密钥 (Key)

1. 前往大模型厂商的开发者控制台注册账号：
   * **OpenAI 平台**：[platform.openai.com](https://platform.openai.com)
   * **DeepSeek 平台**：[platform.deepseek.com](https://platform.deepseek.com)
2. 充值微量金额（通常几元钱即可用很久），在后台生成一个新的 **API Key**（通常格式为 `sk-...`）。
3. **特别警告**：保护好你的 Key，推荐作为环境变量读取，千万不要把它直接提交到 GitHub 公开仓库中！

---

## 🐍 第三步：编写你的第一段 Python 脚本

在你的文件夹下，新建一个名为 `chat.py` 的文件，写入以下代码：

```python
import os
from openai import OpenAI

# 初始化客户端（推荐通过环境变量读取 Key）
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY", "在此处填写你申请到的Key")
)

# 向大模型发起对话请求
response = client.chat.completions.create(
    model="gpt-4o-mini",  # 对应低延迟主力轻量模型
    messages=[
        {"role": "system", "content": "你是一个严谨的助手。"},
        {"role": "user", "content": "用一句话解释什么是 API 密钥。"}
    ],
    temperature=0.7
)

# 打印模型返回的文本内容
print("AI 回复：")
print(response.choices[0].message.content)
```

---

## 🌐 如何无缝切换到 DeepSeek API

OpenAI 官方编写的 SDK 已经成为事实上的行业协议标准。这意味着，你只需要修改**三个参数**（API Key、Base URL 以及模型名称），就能把你的整套程序零门槛切换到 DeepSeek：

```python
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY", "在此处填写你的DeepSeek_Key"),
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-chat",  # 对应 DeepSeek-V3 接口
    messages=[
        {"role": "user", "content": "你好！"}
    ]
)
print(response.choices[0].message.content)
```

---

## ⚡ 现代 2026 工程范式：系统一 (System One) 前置决策网关

在真实生产中，如果将所有安全过滤、路由分流都交给耗时数秒的昂贵大模型，不仅延迟飙升，成本也将难以维系。现代工业界普遍引入 **系统一极速决策网关**（如 TypeSafe Jev）：

```python
# 1. 前置 100ms 极速类型化检查 (如 TypeSafe Jev 的 Noul/Choice 判断)
# 2. 若直接命中违规恶意请求 -> 毫秒级阻断 (零 Token 浪费)
# 3. 若为纯良性常规指令 -> 快速放行或由轻量模型直答
# 4. 仅对于边缘模糊/高价值复杂任务 -> 级联唤起 DeepSeek-R1 / o1 / Claude 深度思考
```

---

学会了调用云端模型，你想不想在自己电脑上不花一分钱，本地跑一个模型呢？让我们进入下一章：[本地大模型运行](17_local_llm_zh.md)。
