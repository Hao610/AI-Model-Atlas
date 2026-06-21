# 向量表示与匹配 📊

[[English] (20_embeddings.md)](20_embeddings.md) | [中文]

计算机无法直接理解人类的字符、句子或文章。对于计算机来说，它们只认识数字。

为了打破这种隔阂，AI 工程师使用了一种叫做 **Embedding (嵌入/向量化)** 的技术。这个过程可以把人类的自然语言转换为一串很长的浮点数数组（即**向量**），从而用数学的方式精确捕捉这段文字的“深层含义”。

---

## 📍 直观理解：文本如何变成坐标

为了方便理解，假设我们只用两个维度坐标——**【快乐程度, 体型大小】**，来给动物词汇打分并画在一个网格地图上：

* **“小猫”** 的坐标可能是：`[0.9, -0.8]`（很快乐，体型很小）。
* **“老虎”** 的坐标可能是：`[0.1, 0.9]`（没那么温驯快乐，体型很大）。
* **“小狗”** 的坐标可能是：`[0.95, -0.75]`（很快乐，体型很小）。

因为“小猫”和“小狗”的坐标极其接近，计算机虽然完全不懂猫狗的生理结构，但它通过数学计算就能瞬间明白：**“小猫”和“小狗”指的是非常类似的实体概念。**

现代商业 Embedding 模型（如 OpenAI 的 `text-embedding-3-small`）可不是只有 2 个坐标，它们会将一句话映射到 **1536 维** 的超高维度坐标体系中！

---

## 📐 如何计算语义相似度：余弦相似度

把文本变成向量坐标后，我们如何计算两个句子的意思有多接近呢？我们测量这两个坐标箭头之间的夹角。这个几何学概念在 AI 领域被称为 **余弦相似度 (Cosine Similarity)**。

```text
余弦相似度数值范围：
  - 1.0 ：语义完全相同（两根向量箭头重合，夹角为 0°）。
  - 0.0 ：语义完全无关（两根向量相互垂直，夹角为 90°）。
  - -1.0：语义完全相反（两根向量方向相反，夹角为 180°）。
```

---

## 🐍 Python 代码实操：比较两个句子的相似度

以下是使用 Python 调用本地 Ollama 的 Embedding 模型来比较句子相似度的极简实例。

```python
import numpy as np
from openai import OpenAI

# 初始化本地大模型客户端
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

def get_embedding(text):
    # 调用 Embedding 模型获取文本的数字向量
    response = client.embeddings.create(
        model="nomic-embed-text",  # 本地常用的文本向量模型
        input=[text]
    )
    return response.data[0].embedding

def cosine_similarity(v1, v2):
    # 计算两个向量的余弦夹角公式
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return dot_product / (norm_v1 * norm_v2)

# 获取三个句子的向量
vec_a = get_embedding("我喜欢小狗和小猫。")
vec_b = get_embedding("犬科和猫科动物是我的最爱。")
vec_c = get_embedding("今日股市下跌了大约两个百分点。")

# 计算语义接近度
print(f"句子 A 和 B 的相似度 (猫狗 vs 动物科属): {cosine_similarity(vec_a, vec_b):.4f}")
print(f"句子 A 和 C 的相似度 (猫狗 vs 股市行情): {cosine_similarity(vec_a, vec_c):.4f}")
```

### 预期输出结果：
* **A 与 B 的相似度**：`~0.80` 左右（数值很高，因为语义上都在谈论猫狗宠物）。
* **A 与 C 的相似度**：`~0.15` 左右（数值极低，风马牛不相及）。

---

理解了语义搜索的底层数理逻辑，接下来让我们看看在工业开发中，如何通过科学手段去评测一个大模型回答的质量好坏：进入 [模型评估与测试](22_evaluation_zh.md)。
