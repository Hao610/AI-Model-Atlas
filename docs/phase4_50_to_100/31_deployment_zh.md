# 云端 GPU 算力部署 🚀

[[English] (31_deployment.md)](31_deployment.md) | [中文]

当你微调出了自己的专属模型，并且通过评测确认了它的回答质量后，最后一步就是将它部署到云端服务器上。这样，其他人的手机 App、网页或者后台服务就能随时随地通过互联网向你的模型发起请求。

在工业界，大模型的在线服务托管通常会使用高性能推理引擎 **vLLM**。

---

## ⚡ 为什么不能用 Ollama 做线上服务？

Ollama/LM Studio 主要是为了单机个人离线使用而设计的。如果你的网站有 100 个人同时在线向 Ollama 发起提问，Ollama 就会因为显存排队而卡死。

而 **vLLM** 采用了一项名为 **PagedAttention** 的革命性技术（像操作系统管理虚拟内存一样来管理大模型的显存键值缓存）。它允许单张显卡同时并发处理数十个用户的提问，吞吐速度极大提升。

---

## 🛠️ 云端部署实操指南（以 AutoDL 为例）

以下是将 `Qwen2.5-7B-Instruct` 部署上云的完整操作指南：

### 第一步：租用云端 GPU 显卡
1. 登录国内常用的算力租用平台（如 **AutoDL.com**，国外可使用 **RunPod.io**）。
2. 选择租用一张 **RTX 4090 (24GB 显存)** 或 **RTX 3090 (24GB 显存)** 显卡。
3. 镜像选择系统预装好的 **PyTorch** 官方镜像。
4. 创建并启动容器，通过 SSH 连接或者直接打开内置的 Jupyter Lab 终端。

### 第二步：安装 vLLM 推理引擎
在容器的命令行终端中输入以下命令安装：

```bash
pip install vllm
```

### 第三步：一键启动 OpenAI 兼容接口服务
使用 vLLM 的 OpenAI 兼容接口命令启动。vLLM 会自动帮你从 Hugging Face 或 ModelScope（魔搭社区，国内极速下载）下载对应的模型文件并加载到显存中：

```bash
vllm serve Qwen/Qwen2.5-7B-Instruct \
    --port 8000 \
    --host 0.0.0.0
```

*看到终端输出服务监听在 `0.0.0.0:8000`，说明接口服务已经启动。较旧版本的 vLLM 可能仍使用 `python -m vllm.entrypoints.openai.api_server`，如命令不一致，请以你安装的 vLLM 版本文档为准。*

**安全提醒：** `--host 0.0.0.0` 会让服务监听所有网卡。不要在没有鉴权、防火墙、限流和访问控制的情况下，把这个端口直接暴露到公网。

---

## 🔗 在你的前端网页或 App 中调用云端模型

现在，你可以回到 Streamlit 网页代码或 Python 脚本中，修改 API 客户端的连接地址为你租用的云服务器地址。如果要公网访问，建议先通过带鉴权的网关或反向代理转发，不要直接调用裸露的 vLLM 端口：

```python
from openai import OpenAI

# 将 base_url 指向你云端 GPU 服务器的公网 IP 和端口
client = OpenAI(
    base_url="http://您的服务器公网IP:8000/v1",
    api_key="请使用真实密钥或受保护的网关凭据"
)

response = client.chat.completions.create(
    model="Qwen/Qwen2.5-7B-Instruct",
    messages=[
        {"role": "user", "content": "你好！请给一家精品咖啡店起一个吸引人的标语。"}
    ]
)
---

🎉 **恭喜！你已经完成了阶段四 (从 50 到 100) 的学习！**

你从最基础的定义一路通关到了云端 GPU 的部署上线。接下来，让我们踏入真正的“无人区”。

请进入 **阶段五：前沿架构与智能体 (从 100 到 200)**，去构建你的第一个能思考的工作流吧：[Tool Routing (智能体路由)](../phase5_100_to_200/32_tool_routing_zh.md)。
