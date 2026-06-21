← 返回 [约束与威胁模型](../../CONSTRAINT_THREAT_MODEL_zh.md) | [English Version (36_chapter_36.md)](36_chapter_36.md)

---

# ?? ? 36 ?????? - ?????????? RAG

在真实世界中构建企业级 RAG 系统，就像建造一座防护完善的设施。你不能随意堆砌石头，而是必须规划护城河、加固城墙并保卫主楼，以在资源受限、动态数据和流量激增的条件下稳定运行。

## 🏰 堡垒 (Fortress) 类比

*   **??**??????????? RAG ??????????????????????
*   **它的工作原理**：你需要打下坚实的基石（资源优化），挖掘深邃的护城河（安全），保障补给线（数据管道），并守卫核心的主楼（LLM 引擎）。
*   **????**???? RAG ???????? API ??????????????????????????????????????????

## 📊 快速对比

| 概念 | 传统方式 | LLM 时代 | 影响 |
| :--- | :--- | :--- | :--- |
| **基石 (Foundation)** | 堆砌更多内存 | 量化与 PagedAttention | 适应受限的显存 (VRAM) |
| **安全 (Security)** | 基础防火墙 | 提示词注入防御与 RBAC | 抵御 AI 专属攻击 |
| **检索 (Retrieval)** | 静态密集型嵌入 | 混合检索与自适应分块 | 处理复杂的企业级数据 |
| **合成 (Synthesis)** | 把所有内容扔给大模型 | 重排与上下文窗口管理 | 防止上下文膨胀与幻觉 |

## 🧠 核心概念

1. **优化基石 (Optimize the Bedrock)**：使用 INT4 量化和模型蒸馏将模型压缩到稀缺的显存中。利用 PagedAttention 和语义缓存来防止内存碎片并绕过昂贵的计算。
2. **挖掘护城河 (Build the Moat)**：实施强大的提示词注入防御、严格的意图过滤和数据隔离 (RBAC)。在上下文到达 LLM 之前，积极消除个人身份信息 (PII)。
3. **保障补给线 (Secure the Supply Lines)**：超越静态分块。使用混合检索 (密集向量 + BM25)，并确保异步管道完美处理实时更新和软删除。
4. **守卫主楼 (Defend the Keep)**：使用交叉编码器 (Cross-encoder) 重排以防止上下文膨胀。实施严格的回退机制，在不确定时优雅降级，而不是产生幻觉。
5. **在围攻中生存 (Survive the Siege)**：部署混沌工程，模拟节点宕机和流量激增。利用 RAGAS 进行持续评估，并实现深度可观测性以获取即时的瓶颈警报。

## 🛠️ 技术深度探索与落地

**企业级 RAG 降级与约束管道**

?????????? RAG ???????????????????????????? Python ????? RAG ??????

```python
import asyncio
from typing import Optional

async def execute_rag_pipeline(query: str, user_role: str) -> str:
    """
    ????????? RAG ???
    特性：RBAC（基于角色的访问控制）、语义缓存、超时降级与安全护栏。
    """
    # 1. 检查语义缓存 (快速路径)
    cached_response = check_semantic_cache(query)
    if cached_response:
        return f"[缓存命中] {cached_response}"

    # 2. RBAC 与安全护栏 (安全防御)
    if not is_safe_query(query):
        return "查询被安全护栏拦截。Pattern: 'Ignore previous instructions...' (sanitized)。"
    
    # 3. 约束检索 (资源管理)
    try:
        # 对向量数据库强制执行 500 毫秒超时
        context = await asyncio.wait_for(
            retrieve_with_rbac(query, role=user_role), 
            timeout=0.5
        )
    except asyncio.TimeoutError:
        return "知识库当前负载过高，请稍后再试。"
    
    # 4. 带有回退机制的 LLM 生成 (内容合成)
    try:
        # 尝试使用主节点的大模型
        response = await generate_with_llm(query, context, model="llama-3-70b", timeout=2.0)
    except Exception as e:
        # 降级到边缘侧/CPU 上运行的量化小模型
        response = await generate_with_llm(query, context, model="phi-3-mini-int4", timeout=1.0)
        response += " (通过回退模型生成)"
    
    # 5. 输出护栏与缓存更新
    if not passes_output_check(response, context):
        return "我无法在提供的文档中找到经过验证的答案。"
        
    update_semantic_cache(query, response)
    return response

# 抽象的模拟函数
def check_semantic_cache(q): return None
def is_safe_query(q): return True
async def retrieve_with_rbac(q, role): return ["文档 A", "文档 B"]
async def generate_with_llm(q, ctx, model, timeout): return "基于上下文的回答。"
def passes_output_check(r, ctx): return True
def update_semantic_cache(q, r): pass
```

---

← [上一章](35_llama_guard_guardrai_zh.md)
