# 模块 33: 量化评测 (RAG Evaluation)
[[English] (33_rag_evaluation.md)](33_rag_evaluation.md) | [中文]

你已经构建好了你的 RAG 流水线。你输入了几个测试问题，答案看起来相当不错，然后你把它部署了。但是，当你调整文本块大小（chunk size）时，你怎么知道它是否真的变得更好了？你怎么知道一次升级没有破坏其他功能？

你是不是在依靠“感觉”来判断你的系统是否在进步？

**核心洞察 (Core Insight)：** 没有指标，就没有进步。

## 来当一次裁判吧 (Play the Judge)

在看具体指标之前，我们先玩个游戏。现在你是裁判。

**上下文文档：** "Reciprocal Rank Fusion (RRF) 是一种用于组合多个搜索结果列表的方法。它由 Gordon Cormack、Charles Clarke 和 Stefan Buettcher 于 2009 年开发。"

**用户提问：** "是谁发明了 RRF？"

下面哪一个是“最好”的答案？

*   **答案 A：** "RRF，全称为倒数排名融合（Reciprocal Rank Fusion），是一种用于合并多个搜索结果列表的方法。根据提供的文档内容，这项技术最初是由 Gordon Cormack、Charles Clarke 和 Stefan Buettcher 组成的一个合作研究团队在 2009 年开发并正式推出的。"
*   **答案 B：** "Gordon Cormack、Charles Clarke 和 Stefan Buettcher。"
*   **答案 C：** "RRF 是由 Google 在 2015 年发明的，旨在改进 PageRank。"

想一想。

*   **答案 A** 是正确的，但是极其冗长和啰嗦。
*   **答案 B** 非常简洁，但缺乏来源证据。
*   **答案 C** 完全是幻觉产生的。

为了教机器评估这些答案，我们把什么是“好答案”拆解成了具体、可衡量的维度：忠实度 (Faithfulness)、相关性 (Relevancy) 和精度 (Precision)。

## RAG 评测三要素 (The RAG Evaluation Triad)

现代 RAG 评测通常不使用单一的“好坏”评分，而是衡量三个独立的维度：

### 1. 忠实度 (Faithfulness)
生成的答案真的来自检索到的上下文吗？
*   **答案 A** 和 **答案 B** 都忠实于源文档。
*   **答案 C** 在这里完全不及格（幻觉）。

### 2. 回答相关性 (Answer Relevancy)
生成的答案是否直接回答了用户的问题，而没有添加不必要的废话？
*   **答案 B** 的相关性很高。
*   **答案 A** 的相关性较低，因为它太啰嗦，包含了用户没有询问的细节。

### 3. 上下文精度 (Context Precision)
你的检索器提取了有用的信息，还是只是垃圾？
即使 LLM 生成了一个很好的答案，如果*检索到的上下文*是不相关的，那么整个 RAG 系统的表现依然是不佳的。上下文精度衡量的是检索到的文档对于回答用户问题是否真的有用。

## LLM 作为裁判 (LLM-as-a-Judge)

你可能会问：“如果不雇佣 100 个人来阅读每一个输出，我们如何自动给这些结果打分？”

秘诀就是 **LLM-as-a-Judge**。我们使用一个强大的 LLM（比如 GPT-4）来给我们的 RAG 流水线的输出打分。我们把问题、上下文和答案交给裁判 LLM，并让它在忠实度和相关性等指标上输出 1 到 5 的评分。

事实证明，强大的 LLM 在给其他 LLM 打分方面出奇地好！通过让你的测试数据集经过 LLM 裁判的评判，你可以获得具体的数据指标来跟踪你的进步，而不再仅仅依靠感觉。

---
← 上一章: [32 tool routing](32_tool_routing_zh.md) | 下一章: [34 vision rag](34_vision_rag_zh.md) →
