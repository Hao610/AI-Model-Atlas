← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (21_rag_pii_zh.md)](21_rag_pii_zh.md)

---

# 🛡️ Chapter 21: Preventing PII Exfiltration

In RAG systems, your vector database can easily become a goldmine for hackers seeking Personally Identifiable Information (PII). A clever prompt injection attack can trick the LLM into spitting out sensitive private data unless strict safeguards are in place.

## 🕵️ The Censorious Librarian Analogy

* **The Analogy**: A vigilant librarian redacts names and private details from records *before* handing them to patrons.
* **How it works**: By actively scanning for and blacking out sensitive information, the librarian ensures that even if a malicious patron asks a tricky question, the secrets simply aren't there to be revealed.
* **Key Concept**: Sanitizing data before it reaches the LLM is the ultimate defense against data leakage.

## 📊 Quick Comparison

| Concept | Traditional | LLM Era | Impact |
| :--- | :--- | :--- | :--- |
| **Data Protection** | Database permissions | Multi-layered RAG sanitization | Prevents direct PII extraction |
| **Search Restrictions** | SQL row-level security | Vector metadata filtering | Isolates private user data chunks |
| **Output Control** | Static API gateways | Post-generation DLP scanning | Catches rogue LLM data leaks |

## 🧠 Core Concept

1. **Sanitize Before Indexing:** Use NER models or regex to automatically mask PII (e.g., replacing names with `[REDACTED]`) before chunking and embedding documents.
2. **Minimize Indexed Data:** Strictly limit your vector database to only hold the information necessary for the application's function.
3. **Enforce Metadata RBAC:** Attach access-level metadata to every vector chunk so that retrieval is rigidly filtered based on the user's authorization.
4. **Filter the Final Output:** Run the LLM's generated response through a Data Loss Prevention (DLP) tool to catch and block any PII before it reaches the user.

## 🛠️ Technical Deep Dive & Implementation

In a defensive posture, mitigating PII exfiltration from a RAG setup requires a multi-layered approach: sanitizing before indexing, enforcing strict retrieval-time metadata filtering, and scanning LLM outputs.

### 1. Ingestion Pipeline: Anonymizing PII Before Indexing
Before creating vector embeddings, scan the text using NLP models (like Presidio) or regex to redact PII.

```python
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

def sanitize_document(text: str) -> str:
    # Analyze text for PII (Names, Emails, Phone numbers, etc.)
    results = analyzer.analyze(text=text, entities=["PERSON", "EMAIL_ADDRESS", "PHONE_NUMBER"], language='en')
    
    # Anonymize findings
    anonymized_result = anonymizer.anonymize(text=text, analyzer_results=results)
    return anonymized_result.text

raw_text = "John Doe's email is john.doe@example.com."
safe_text = sanitize_document(raw_text)
# Output: "<PERSON>'s email is <EMAIL_ADDRESS>."
```

### 2. Retrieval Filtering: Metadata RBAC
When storing embeddings, attach role-based access control (RBAC) tags to metadata. During retrieval, apply strict metadata filters.

```python
# Example using Pinecone vector database
# 1. Insert with metadata
index.upsert(
    vectors=[
        {"id": "doc1", "values": [0.1, 0.2, ...], "metadata": {"clearance": "level_1", "user_id": "u456"}},
        {"id": "doc2", "values": [0.3, 0.4, ...], "metadata": {"clearance": "level_2", "user_id": "u789"}}
    ]
)

# 2. Query with strict metadata filtering
query_response = index.query(
    vector=[0.1, 0.2, ...],
    top_k=5,
    include_metadata=True,
    filter={
        "clearance": {"$eq": "level_1"},
        "user_id": {"$eq": "u456"} # Only retrieve chunks owned by the requester
    }
)
```

### 3. Output Scanning: NeMo Guardrails
Ensure the generated response is checked for sensitive data before it reaches the user.

```yaml
# config.yml for NeMo Guardrails
define bot prevent pii leaks
  "You are a helpful assistant. You must not reveal any Personally Identifiable Information."

define flow check pii
  user ask question
  bot generate response
  $is_safe = execute check_pii_dlp(response=$bot_response)
  if not $is_safe
    bot "I'm sorry, I cannot provide this information due to privacy constraints."
    stop
```

---

← [Prev Chapter](20_meta_prompts.md) | [Next Chapter](../phase4/22_git_commit_prompt.md) →
