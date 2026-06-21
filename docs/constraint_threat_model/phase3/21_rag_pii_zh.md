← 返回 [约束与威胁模型](../../CONSTRAINT_THREAT_MODEL_zh.md) | [English Version (21_rag_pii.md)](21_rag_pii.md)

---

# 🛡️ 第 21 章：防止 PII 数据泄露

在检索增强生成 (RAG) 系统中，如果没有严格的安全防护，向量数据库很容易成为黑客窃取个人身份信息 (PII) 的金矿。一次巧妙的提示词注入攻击就能诱导 LLM 吐出敏感的私密数据。

## 🕵️ 负责审查的图书管理员类比

* **类比**： 一位警惕的图书管理员会在将档案交给读者*之前*，把姓名和私密细节涂黑。
* **原理**： 通过主动扫描并掩盖敏感信息，图书管理员确保即使恶意读者提出刁钻的问题，那些秘密也根本不在文本中，无法被泄露。
* **核心概念**： 在数据被索引和进入 LLM 之前进行清洗，是防止数据泄露的终极防线。

## 📊 快速对比

| 概念 | 传统方式 | LLM 时代 | 影响 |
| :--- | :--- | :--- | :--- |
| **数据保护** | 数据库权限 | 多层 RAG 清洗 | 防止直接提取 PII |
| **搜索限制** | SQL 行级安全 | 向量元数据过滤 | 隔离用户的私密数据块 |
| **输出控制** | 静态 API 网关 | 生成后的 DLP 扫描 | 拦截 LLM 违规的数据泄露 |

## 🧠 核心概念

1. **索引前的数据清洗：** 在对文档进行分块和向量化之前，使用 NER 模型或正则表达式自动屏蔽 PII（例如，将姓名替换为 `[REDACTED]`）。
2. **最小化索引数据：** 严格限制向量数据库，仅保留应用程序核心功能绝对必需的信息。
3. **强制元数据 RBAC：** 将访问级别的元数据附加到每个向量块，以便根据用户的权限对检索进行严格过滤。
4. **过滤最终输出：** 将 LLM 生成的响应通过数据防泄漏 (DLP) 工具，在任何 PII 到达用户之前对其进行捕获和拦截。

## 🛠️ 技术深度探索与落地

在防御姿态下，缓解 RAG 架构中的 PII 泄露需要采取多层防御策略：在索引前进行清洗、在检索时强制执行严格的元数据过滤，以及对 LLM 输出进行最终扫描。

### 1. 注入管道：在索引前匿名化 PII
在创建向量嵌入之前，使用 NLP 模型（如 Microsoft Presidio）或正则表达式扫描并脱敏文本中的 PII。

```python
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

def sanitize_document(text: str) -> str:
    # 扫描文本中的 PII（姓名、邮箱、电话号码等）
    results = analyzer.analyze(text=text, entities=["PERSON", "EMAIL_ADDRESS", "PHONE_NUMBER"], language='en')
    
    # 匿名化发现的敏感信息
    anonymized_result = anonymizer.anonymize(text=text, analyzer_results=results)
    return anonymized_result.text

raw_text = "John Doe's email is john.doe@example.com."
safe_text = sanitize_document(raw_text)
# 输出: "<PERSON>'s email is <EMAIL_ADDRESS>."
```

### 2. 检索过滤：基于元数据的 RBAC
在存储向量嵌入时，将基于角色的访问控制 (RBAC) 标签附加到元数据中。在检索阶段，应用严格的元数据过滤器。

```python
# 使用 Pinecone 向量数据库的示例
# 1. 插入带有元数据的向量
index.upsert(
    vectors=[
        {"id": "doc1", "values": [0.1, 0.2, ...], "metadata": {"clearance": "level_1", "user_id": "u456"}},
        {"id": "doc2", "values": [0.3, 0.4, ...], "metadata": {"clearance": "level_2", "user_id": "u789"}}
    ]
)

# 2. 带有严格元数据过滤的查询
query_response = index.query(
    vector=[0.1, 0.2, ...],
    top_k=5,
    include_metadata=True,
    filter={
        "clearance": {"$eq": "level_1"},
        "user_id": {"$eq": "u456"} # 仅检索请求者拥有的数据块
    }
)
```

### 3. 输出扫描：NeMo Guardrails 防护
在生成的响应到达用户之前，确保对其进行敏感数据检查。

```yaml
# NeMo Guardrails 的 config.yml 配置文件
define bot prevent pii leaks
  "You are a helpful assistant. You must not reveal any Personally Identifiable Information."

define flow check pii
  user ask question
  bot generate response
  $is_safe = execute check_pii_dlp(response=$bot_response)
  if not $is_safe
    bot "抱歉，由于隐私限制，我无法提供此信息。"
    stop
```

---

← [上一章](20_meta_prompts_zh.md) | [下一章](../phase4/22_git_commit_prompt_zh.md) →
