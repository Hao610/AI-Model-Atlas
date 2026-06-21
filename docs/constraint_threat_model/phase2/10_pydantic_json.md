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

---

← [Prev Chapter](09_role_alignment_agent.md) | [Next Chapter](11_automated_self_corre.md) →
