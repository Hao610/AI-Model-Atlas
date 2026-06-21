← 返回 [约束与威胁模型](../../CONSTRAINT_THREAT_MODEL_zh.md) | [English Version (33_observability_cascad.md)](33_observability_cascad.md)

---

# 🔭 第 33 章：生产环境可观测性

在复杂的 AI 部署中，仅知道哪里坏了是不够的；您必须知道*为什么*。生产环境可观测性提供了至关重要的透视能力，用于解开级联故障和发现隐藏的系统异常。

## ✈️ 飞机黑匣子类比 (The Black Box Flight Recorder Analogy)

* **类比**： 就像飞机的黑匣子一样，可观测性工具捕捉高保真参数，以重构系统崩溃前的精确时刻。
* **原理**： 分布式遥测系统持续记录跨越所有服务的追踪、指标和状态数据。当事件发生时，工程师可以“倒带”到故障产生的精确微秒。
* **核心概念**： 全面的追踪让原本不可见、复杂的系统行为更容易被检查和理解。

## 📊 快速对比

| 概念 | 传统方式 | LLM 时代 | 影响 |
| :--- | :--- | :--- | :--- |

## 📊 快速对比

| 概念 | 传统方式 | LLM 时代 | 影响 |
| :--- | :--- | :--- | :--- |
| **监控 (Monitoring)** | 孤立的服务器日志和硬件指标 | 分布式、感知上下文的语义追踪 | 实现跨边界的快速根本原因分析 |
| **故障 (Failures)** | 在崩溃点发出的孤立错误警报 | 跨服务的级联故障映射图 | 修复实际的源头瓶颈，而不仅仅是表面症状 |
| **流量 (Traffic)** | 追踪基础的流量激增 | 深入的提示词负载和延迟分析 | 检测细微的模型滥用和资源耗尽 |

## 🧠 核心概念

1. **全面插桩**: 在您的整个技术栈中（从微服务到 LLM API）嵌入标准遥测技术（如 OpenTelemetry）。
2. **注入关联 ID**: 为每一个用户请求标记唯一的标识符，以追踪它在各个依赖项之间的流转路径。
3. **映射级联故障**: 可视化服务依赖关系，瞬间发现下游模型超时是如何引发上游 API 大规模故障的。
4. **建立基准线**: 收集颗粒化指标以定义“正常”行为，从而在异常流量模式或 DDoS 尝试发生时立即发出警报。

## 🛠️ 技术深度探索与落地

在现代 LLM 基础设施中，标准的 APM（应用性能监控）已经不足以应对，因为模型输出具有非确定性，且 token 生成具有高延迟。一个完整的可观测性技术栈必须追踪 token 消耗量、语义相似度漂移、首字延迟（TTFT）以及安全护栏的拦截率。

### 1. 针对 LLM 的 OpenTelemetry (Python 代码片段)
使用标准 OpenTelemetry 实现分布式追踪，并将追踪 ID 与 LLM 上下文关联。

```python
from opentelemetry import trace
from opentelemetry.instrumentation.requests import RequestsInstrumentor
import openai
import os

# 初始化追踪
tracer = trace.get_tracer(__name__)
RequestsInstrumentor().instrument()

def process_user_query(query: str, user_id: str):
    with tracer.start_as_current_span("process_llm_chain") as span:
        span.set_attribute("user.id", user_id)
        span.set_attribute("llm.provider", "openai")
        span.set_attribute("llm.model", "gpt-4-turbo")
        
        try:
            # 提取 trace_id 用于全链路日志聚合
            trace_id = span.get_span_context().trace_id
            formatted_trace_id = f"{trace_id:032x}"
            
            response = openai.ChatCompletion.create(
                model="gpt-4-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": query}
                ],
                user=user_id # 向服务商透传 ID 以监控滥用行为
            )
            
            # 记录 Token 指标数据
            usage = response.get("usage", {})
            span.set_attribute("llm.usage.prompt_tokens", usage.get("prompt_tokens", 0))
            span.set_attribute("llm.usage.completion_tokens", usage.get("completion_tokens", 0))
            
            return response.choices[0].message.content
            
        except Exception as e:
            span.record_exception(e)
            span.set_status(trace.StatusCode.ERROR, str(e))
            raise
```

### 2. AI 网关的 Prometheus 指标 (YAML/配置)
为了追踪级联故障，需要在 API 网关层（如 Kong、Envoy 或专用 AI 网关）配置特定的 LLM 监控指标。

```yaml
# AI 网关的 Prometheus 抓取配置示例
scrape_configs:
  - job_name: 'ai_gateway_metrics'
    static_configs:
      - targets: ['api-gateway:9090']
    metrics_path: '/metrics'
    # 监控级联故障的关键指标：
    # - ai_gateway_llm_latency_seconds_bucket (首字响应延迟 / TTFT)
    # - ai_gateway_rate_limit_hits_total (资源耗尽和限流预警)
    # - ai_gateway_guardrail_blocks_total (触发的安全护栏拦截次数)
    # - ai_gateway_active_streaming_connections (连接数/Socket耗尽风险)
```

### 3. CI/CD 可观测性自动化验证 (GitHub Actions)
确保在持续部署过程中，追踪上下文的传递和日志格式不会被破坏。

```yaml
name: Observability Telemetry Validation

on:
  pull_request:
    paths:
      - 'src/llm_pipeline/**'

jobs:
  validate-telemetry:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          
      - name: Install dependencies
        run: pip install -r requirements.txt opentelemetry-sdk pytest
        
      - name: Run Telemetry Mock Tests
        run: |
          # 验证链路跨度是否缺少关键属性（如 user_id, token_count）
          pytest tests/test_telemetry.py --maxfail=1
          
      - name: Check Log Formatting
        run: |
          # 验证日志输出格式是否为 JSON 且包含必需的 trace_id 字段
          python scripts/validate_json_logs.py
```

---

← [上一章](32_ai_zh.md) | [下一章](34_nvidia_nemo_guardrai_zh.md) →
