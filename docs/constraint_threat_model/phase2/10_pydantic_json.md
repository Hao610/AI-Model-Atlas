← Back to [Constraint & Threat Model](../../CONSTRAINT_THREAT_MODEL.md) | [中文版 (10_pydantic_json_zh.md)](10_pydantic_json_zh.md)

---

# 🧱 Chapter 10: Strict Output Constraints with Pydantic

When building applications that rely on Large Language Models, unstructured text responses are a liability. You need predictable, structured data that your code can reliably parse, making Pydantic the ultimate enforcer for strict output constraints.

## 🏢 The DMV Analogy

* **The Analogy**: Parsing LLM outputs is like processing paperwork at the Department of Motor Vehicles (DMV).
* **How it works**: Giving an applicant blank paper yields a chaotic mix of formats and missing info. Instead, the DMV uses strict forms where "last Tuesday" for a birthdate results in an instant rejection.
* **Key Concept**: Pydantic acts as that unforgiving, strict form for LLMs—if the output doesn't match your exact schema, it throws an immediate validation error.

## 📊 Quick Comparison

| Concept | Traditional | LLM Era | Impact |
|---------|-------------|---------|--------|
| **Data Formatting** | Simple prompt: "Return as JSON" | Pydantic classes defining exact schemas | Eliminates conversational filler and missing fields. |
| **Type Checking** | Manual regex and string parsing | Native Python type hints (`int`, `bool`) | Helps the application receive usable data types. |
| **Error Recovery** | Application crashes on bad output | Auto-retry by feeding errors back to the LLM | Transforms brittle integrations into self-healing pipelines. |

## 🧠 Core Concept

1. **Define the Schema**: Create a Pydantic `BaseModel` detailing the exact fields, types, and semantic descriptions of your expected data.
2. **Inject the Schema**: Modern frameworks translate your Pydantic model into a JSON Schema and pass it directly to the LLM API.
3. **Generate the Output**: Some providers and frameworks can steer the LLM toward JSON that conforms to the requested schema, but this still depends on the model and integration.
4. **Validate and Parse**: The raw JSON is loaded back into your Pydantic model, failing fast if it violates the expected constraints.

```python
from pydantic import BaseModel, Field

class UserProfile(BaseModel):
    name: str = Field(description="The user's full name")
    age: int = Field(description="The user's age in years")
    is_active: bool = Field(description="Whether the user account is active")
    tags: list[str] = Field(description="A list of interests or tags")
```

## 🛠️ Technical Deep Dive & Implementation

In modern LLM applications, simply asking the model to "output JSON" is insufficient. Advanced implementations leverage **Structured Outputs** (like OpenAI's `response_format` or the Instructor library) combined with Pydantic to strongly encourage schema compliance and catch invalid outputs early.

### 1. Instructor Integration (Defense Snippet)
Using the `instructor` library patches the LLM client to enforce Pydantic validation and automatically handle retries on failure.

```python
import instructor
from openai import OpenAI
from pydantic import BaseModel, Field

# Patch the OpenAI client
client = instructor.from_openai(OpenAI())

class SecurityReport(BaseModel):
    threat_level: str = Field(pattern=r"^(Low|Medium|High|Critical)$")
    vulnerabilities_found: int = Field(ge=0)
    action_items: list[str] = Field(max_length=5)

# The client will automatically retry if the LLM output violates the Pydantic schema
report = client.chat.completions.create(
    model="gpt-4o",
    response_model=SecurityReport,
    max_retries=3, # Auto-retry on validation failure
    messages=[
        {"role": "user", "content": "Analyze this log for threats: [LOG_DATA]"}
    ]
)
print(report.model_dump_json(indent=2))
```

### 2. Guardrails Configuration (NeMo YAML)
You can also enforce JSON schema constraints at the proxy/guardrail layer to drop or flag non-compliant payloads before they reach the application logic.

```yaml
models:
  - type: main
    engine: openai
    model: gpt-4
    
rails:
  output:
    flows:
      - check output schema

prompts:
  - task: generate_json
    content: |
      Generate a response conforming exactly to the following JSON schema:
      {{ expected_schema }}
```

---

← [Prev Chapter](09_role_alignment_agent.md) | [Next Chapter](11_automated_self_corre.md) →
