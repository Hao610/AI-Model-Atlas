← 返回 [约束与威胁模型](../../CONSTRAINT_THREAT_MODEL_zh.md) | [English Version (32_ai.md)](32_ai.md)

---

# ⏳ 第 32 章：异步与队列

在扩展 AI 系统时，同步执行很快就会成为瓶颈。采用异步处理和消息队列对于防止在高负载下出现超时、浪费 GPU 资源和糟糕的用户体验至关重要。

## 🍳 The 餐厅厨房 Analogy

* **类比**： 餐厅采用订单架系统，而不是让服务员站在厨房里等菜做好。
* **原理**： 服务员将订单贴在订单架（消息队列）上，然后立刻回去接更多订单。厨师一有空就处理订单，这意味着后点的快手沙拉可能会比先点的全熟牛排更早做好。
* **核心概念**： 将请求接收与繁重的处理过程解耦，能够在不阻塞服务器的情况下实现大规模并发。

## 📊 快速对比

| 概念 | 传统方式 | LLM 时代 | 影响 |
| --- | --- | --- | --- |
| **执行方式** | 同步执行（等待响应） | 异步执行（即发即弃） | 防止 API 在缓慢的生成过程中超时。 |
| **系统扩展** | 扩展 Web 服务器 | 独立扩展工作节点池 | 优化昂贵的 GPU 资源使用率。 |
| **处理顺序** | 严格的先进先出 (FIFO) | 优先级队列与乱序处理 | 高优先级或简单的请求能更快完成。 |
| **重试机制** | 简单的 API 调用 | 幂等性生成 | 防止重复且昂贵的 AI 计算。 |

## 🧠 核心概念

1. **解耦请求接收**：客户端提交请求并立即收到一个 `Job ID`，同时该任务进入消息队列（如 Kafka、Redis）。
2. **管理并发**：独立的工作节点池根据其当前的可用性和 GPU 容量，从队列中拉取任务。
3. **处理乱序执行**：实现优先级队列和健壮的状态管理（`等待中`、`处理中`、`已完成`），以原生方式处理不同的延迟情况。
4. **强制幂等性**：要求每个请求具有唯一的“幂等键”，确保网络重试绝不会触发重复且昂贵的 LLM 生成过程。

## 🛠️ 技术深度探索与落地

在高并发的大语言模型（LLM）环境中，同步等待 API 响应会耗尽工作线程并导致级联故障。使用队列（如 Redis、RabbitMQ）将请求接收与执行解耦，并强制执行幂等性，可以防止资源耗尽和重复计费。

### 带有幂等性的异步队列实现（FastAPI + Celery/Redis）

```python
from fastapi import FastAPI, Header, HTTPException, BackgroundTasks
from celery import Celery
import redis
import json

app = FastAPI()
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# 配置 Celery 工作节点池
celery_app = Celery('llm_tasks', broker='redis://localhost:6379/0')

@celery_app.task(bind=True)
def process_llm_generation(self, prompt: str, idempotency_key: str):
    # 抽象的 LLM 执行逻辑
    response = f"Generated response for: {prompt[:10]}..."
    
    # 存储结果并设置 TTL，防止无限期存储
    redis_client.setex(
        f"result:{idempotency_key}", 
        3600, 
        json.dumps({"status": "completed", "output": response})
    )
    return response

@app.post("/generate")
async def generate_text(prompt: str, idempotency_key: str = Header(...)):
    # 1. 检查请求是否已经处理或正在处理中
    existing_job = redis_client.get(f"result:{idempotency_key}")
    if existing_job:
        return json.loads(existing_job)
    
    if redis_client.get(f"lock:{idempotency_key}"):
        return {"status": "processing", "message": "任务正在处理中"}

    # 2. 获取锁以防止重试时的竞态条件
    redis_client.setex(f"lock:{idempotency_key}", 300, "locked")
    
    # 3. 分发到工作队列
    process_llm_generation.delay(prompt, idempotency_key)
    
    # 4. 立即返回 Job ID (即发即弃)
    return {"status": "accepted", "job_id": idempotency_key, "message": "请稍后查询结果"}
```

### 应对队列耗尽的缓解策略

* **死信队列 (DLQ)**: 在重试特定次数后，将失败或永久挂起的 LLM 任务路由到 DLQ，以防止队列阻塞。
* **超时与 TTL**: 对队列项强制设置严格的生存时间 (TTL)，以便在用户已经放弃请求时，丢弃过期的任务而不是继续执行。
* **基于租户的速率限制**: 为每个用户/租户应用独立的队列限制，防止“吵闹的邻居”攻击独占 GPU 工作节点池。

---

← [上一章](31_ai_gateway_circuit_b_zh.md) | [下一章](33_observability_cascad_zh.md) →
