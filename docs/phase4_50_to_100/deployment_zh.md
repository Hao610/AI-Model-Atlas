# 云端 GPU 算力部署 🚀

[[English] (deployment.md)](deployment.md) | [中文]

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
使用 vLLM 的 OpenAI 包装器接口命令启动。vLLM 会自动帮你从 Hugging Face 或 ModelScope（魔搭社区，国内极速下载）下载对应的模型文件并加载到显存中：

```bash
python -m vllm.entrypoints.openai.api_server \
    --model Qwen/Qwen2.5-7B-Instruct \
    --port 8000 \
    --host 0.0.0.0
```

*看到终端输出 `Uvicorn running on http://0.0.0.0:8000`，说明你的接口服务已经上线成功！*

---

## 🔗 在你的前端网页或 App 中调用云端模型

现在，你只需要回到你的 Streamlit 网页代码或 Python 脚本中，修改 API 客户端的连接地址为你租用的云服务器的公网 IP 即可：

```python
from openai import OpenAI

# 将 base_url 指向你云端 GPU 服务器的公网 IP 和端口
client = OpenAI(
    base_url="http://您的服务器公网IP:8000/v1",
    api_key="vllm-server"  # 私有服务器不需要Key，填占位符即可
)

response = client.chat.completions.create(
    model="Qwen/Qwen2.5-7B-Instruct",
    messages=[
        {"role": "user", "content": "你好！请给一家精品咖啡店起一个吸引人的标语。"}
    ]
)

print(response.choices[0].message.content)
```

---

🎉 **恭喜你！你已经通关了 AI-Model-Atlas 的全部内容！**

你从最基础的概念比喻、提示词编写开始，一路上山，最终学会了本地运行、向量库搭建、多智能体协同、LoRA 微调，甚至完成了云端 GPU 推理服务部署。你现在已经完全具备了独立搭建、维护和迭代一套垂直领域 AI 应用的底座知识。

建议将本仓库加入收藏夹，作为你的“私人 AI 知识外脑”随时查阅。祝你在人工智能的新世界里乘风破浪！
