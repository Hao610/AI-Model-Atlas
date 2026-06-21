<p align="center">
  <img src="https://github.com/user-attachments/assets/a51e8bb3-b2f3-4595-aee4-2272e2323086" alt="AI Model Atlas Logo" width="100">
</p>

# 🛡️ Secure & Resilient AI Runtime Constraint & Threat Model
> Engineering a Production-Grade AI Security Reference Architecture.
← Back to [README](../README.md) | [中文版](CONSTRAINT_THREAT_MODEL_zh.md)
## Curriculum

### 🛡️ Phase 1: Foundations & Asset Management
> **This phase establishes the foundational concepts of LLM security, moving away from traditional AppSec into the new unstructured paradigm.**

#### Module 1: Supply Chain Security & Zero Trust
| Chapter | Description | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **1. OWASP Top 10 for LLMs** | Why traditional AppSec fails in the LLM era. | [01_owasp_top_10_llm.md](constraint_threat_model/phase1/01_owasp_top_10_llm.md) | [01_owasp_top_10_llm_zh.md](constraint_threat_model/phase1/01_owasp_top_10_llm_zh.md) |
| **2. Unstructured Attack Surfaces** | Dissecting model weights, middleware, and data streams. | [02_chapter_2.md](constraint_threat_model/phase1/02_chapter_2.md) | [02_chapter_2_zh.md](constraint_threat_model/phase1/02_chapter_2_zh.md) |
| **3. Zero Trust Architecture** | Identity and security boundaries for every input/output. | [03_zero_trust.md](constraint_threat_model/phase1/03_zero_trust.md) | [03_zero_trust_zh.md](constraint_threat_model/phase1/03_zero_trust_zh.md) |

#### Module 2: Prompt as Code (Asset Management)
| Chapter | Description | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **4. Rejecting Hardcoding** | Engineering standards for decoupling prompts from code. | [04_prompt.md](constraint_threat_model/phase1/04_prompt.md) | [04_prompt_zh.md](constraint_threat_model/phase1/04_prompt_zh.md) |
| **5. Prompt Version Control** | Dynamic CI/CD delivery flows across environments. | [05_prompt_dev_staging_p.md](constraint_threat_model/phase1/05_prompt_dev_staging_p.md) | [05_prompt_dev_staging_p_zh.md](constraint_threat_model/phase1/05_prompt_dev_staging_p_zh.md) |
| **6. Token Optimization** | System prompt compression and cost circuit breakers. | [06_system_prompt_tokens.md](constraint_threat_model/phase1/06_system_prompt_tokens.md) | [06_system_prompt_tokens_zh.md](constraint_threat_model/phase1/06_system_prompt_tokens_zh.md) |

---

### 🧠 Phase 2: Advanced Production Prompting
> **This phase focuses on engineering robust prompts that aim to improve output consistency and reduce logical degradation.**

#### Module 3: Deterministic Control Flow
| Chapter | Description | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **7. Dynamic Few-Shot** | Using Vector DBs to inject real-time security examples. | [07_dynamic_few_shot.md](constraint_threat_model/phase2/07_dynamic_few_shot.md) | [07_dynamic_few_shot_zh.md](constraint_threat_model/phase2/07_dynamic_few_shot_zh.md) |
| **8. CoT & ToT Optimization** | Step-by-step routing and tree-of-thought pruning. | [08_cot_tot.md](constraint_threat_model/phase2/08_cot_tot.md) | [08_cot_tot_zh.md](constraint_threat_model/phase2/08_cot_tot_zh.md) |
| **9. Role Alignment** | Preventing role collapse in multi-agent environments. | [09_role_alignment_agent.md](constraint_threat_model/phase2/09_role_alignment_agent.md) | [09_role_alignment_agent_zh.md](constraint_threat_model/phase2/09_role_alignment_agent_zh.md) |

#### Module 4: Robustness & Degradation Control
| Chapter | Description | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **10. Strict Output Constraints** | Pydantic integration for strongly structured JSON outputs. | [10_pydantic_json.md](constraint_threat_model/phase2/10_pydantic_json.md) | [10_pydantic_json_zh.md](constraint_threat_model/phase2/10_pydantic_json_zh.md) |
| **11. Self-Correction Mechanisms** | Graceful degradation and automated error patching. | [11_automated_self_corre.md](constraint_threat_model/phase2/11_automated_self_corre.md) | [11_automated_self_corre_zh.md](constraint_threat_model/phase2/11_automated_self_corre_zh.md) |
| **12. Dynamic Hyperparameters** | Real-time Temperature/Top-p adjustment based on hallucination rates. | [12_temperature_top_p.md](constraint_threat_model/phase2/12_temperature_top_p.md) | [12_temperature_top_p_zh.md](constraint_threat_model/phase2/12_temperature_top_p_zh.md) |

---

### 🥷 Phase 3: Adversarial Red Teaming
> **This phase covers offensive security testing, simulating attacks like prompt injection and RAG hijacking to harden defenses.**

#### Module 5: Prompt Injection & Jailbreaking
| Chapter | Description | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **13. Direct Prompt Injection** | Bypasses, roleplay, and logical paradox attacks. | [13_direct_prompt_inject.md](constraint_threat_model/phase3/13_direct_prompt_inject.md) | [13_direct_prompt_inject_zh.md](constraint_threat_model/phase3/13_direct_prompt_inject_zh.md) |
| **14. Multilingual & Base64 Injections** | Exploiting esoteric languages to bypass filters. | [14_base64.md](constraint_threat_model/phase3/14_base64.md) | [14_base64_zh.md](constraint_threat_model/phase3/14_base64_zh.md) |
| **15. Auto-Jailbreaking** | Writing Python scripts to automatically probe model blind spots. | [15_auto_jailbreaking_py.md](constraint_threat_model/phase3/15_auto_jailbreaking_py.md) | [15_auto_jailbreaking_py_zh.md](constraint_threat_model/phase3/15_auto_jailbreaking_py_zh.md) |

#### Module 6: Indirect Injection & RAG Vulnerabilities
| Chapter | Description | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **16. Indirect Prompt Injection** | Malicious instructions hidden in external web pages and PDFs. | [16_indirect_injection_p.md](constraint_threat_model/phase3/16_indirect_injection_p.md) | [16_indirect_injection_p_zh.md](constraint_threat_model/phase3/16_indirect_injection_p_zh.md) |
| **17. RAG Agent Hijacking** | System takeover via external knowledge base poisoning. | [17_rag_agent.md](constraint_threat_model/phase3/17_rag_agent.md) | [17_rag_agent_zh.md](constraint_threat_model/phase3/17_rag_agent_zh.md) |
| **18. Visual Injection** | Bypassing guardrails using image parsing blind spots. | [18_visual_injection.md](constraint_threat_model/phase3/18_visual_injection.md) | [18_visual_injection_zh.md](constraint_threat_model/phase3/18_visual_injection_zh.md) |

#### Module 7: Data Protection
| Chapter | Description | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **19. Prompt Leaking** | Social engineering attacks targeting proprietary prompts. | [19_prompt_leaking.md](constraint_threat_model/phase3/19_prompt_leaking.md) | [19_prompt_leaking_zh.md](constraint_threat_model/phase3/19_prompt_leaking_zh.md) |
| **20. Defensive Meta-Prompts** | Writing highly robust instructions that resist tampering. | [20_meta_prompts.md](constraint_threat_model/phase3/20_meta_prompts.md) | [20_meta_prompts_zh.md](constraint_threat_model/phase3/20_meta_prompts_zh.md) |
| **21. Preventing PII Exfiltration** | Stopping hackers from extracting private vector data. | [21_rag_pii.md](constraint_threat_model/phase3/21_rag_pii.md) | [21_rag_pii_zh.md](constraint_threat_model/phase3/21_rag_pii_zh.md) |

---

### ⚙️ Phase 4: Prompt DevSecOps Pipeline
> **This phase integrates continuous security scanning and automated model evaluation into the deployment lifecycle.**

#### Module 8: Shift-Left Security & Static Scanning
| Chapter | Description | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **22. Git Commit Scanning** | Catching prompt template leaks in CI/CD. | [22_git_commit_prompt.md](constraint_threat_model/phase4/22_git_commit_prompt.md) | [22_git_commit_prompt_zh.md](constraint_threat_model/phase4/22_git_commit_prompt_zh.md) |
| **23. Static Analysis Tools** | Identifying semantic vulnerabilities in prompts. | [23_prompt.md](constraint_threat_model/phase4/23_prompt.md) | [23_prompt_zh.md](constraint_threat_model/phase4/23_prompt_zh.md) |
| **24. Dependency Auditing** | Monitoring CVEs for LangChain, LlamaIndex, etc. | [24_langchain_llamaindex.md](constraint_threat_model/phase4/24_langchain_llamaindex.md) | [24_langchain_llamaindex_zh.md](constraint_threat_model/phase4/24_langchain_llamaindex_zh.md) |

#### Module 9: Automated Optimization
| Chapter | Description | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **25. DSPy & TextGrad** | Auto-evolving safer and smarter prompt pipelines. | [25_dspy_textgrad_prompt.md](constraint_threat_model/phase4/25_dspy_textgrad_prompt.md) | [25_dspy_textgrad_prompt_zh.md](constraint_threat_model/phase4/25_dspy_textgrad_prompt_zh.md) |
| **26. Automated Red Teaming** | Subjecting prompts to automated CI/CD attacks. | [26_automated_red_teamin.md](constraint_threat_model/phase4/26_automated_red_teamin.md) | [26_automated_red_teamin_zh.md](constraint_threat_model/phase4/26_automated_red_teamin_zh.md) |
| **27. Gateway Interceptors** | Enforcing jailbreak blocking in GitHub Actions. | [27_github_actions.md](constraint_threat_model/phase4/27_github_actions.md) | [27_github_actions_zh.md](constraint_threat_model/phase4/27_github_actions_zh.md) |

#### Module 10: LLM-as-a-Judge
| Chapter | Description | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **28. Safety Judge Matrix** | Building custom heuristic evaluation models. | [28_safety_judge.md](constraint_threat_model/phase4/28_safety_judge.md) | [28_safety_judge_zh.md](constraint_threat_model/phase4/28_safety_judge_zh.md) |
| **29. 3D Quantification Metrics** | Tracking Hallucination, Accuracy, and Adversarial Pass Rates. | [29_chapter_29.md](constraint_threat_model/phase4/29_chapter_29.md) | [29_chapter_29_zh.md](constraint_threat_model/phase4/29_chapter_29_zh.md) |
| **30. Performance Dashboard** | Establishing long-term observability for prompt assets. | [30_prompt.md](constraint_threat_model/phase4/30_prompt.md) | [30_prompt_zh.md](constraint_threat_model/phase4/30_prompt_zh.md) |

---

### 🛡️ Phase 5: Runtime Guardrails & Resilience
> **This phase introduces dynamic traffic management, circuit breaking, and strict API-level guardrails.**

#### Module 11: Zero Trust Gateway & Distributed Resilience
| Chapter | Description | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **31. AI Gateway Resilience** | Circuit breakers and multi-model failover routing. | [31_ai_gateway_circuit_b.md](constraint_threat_model/phase5/31_ai_gateway_circuit_b.md) | [31_ai_gateway_circuit_b_zh.md](constraint_threat_model/phase5/31_ai_gateway_circuit_b_zh.md) |
| **32. Async & Queues** | Managing high concurrency, out-of-order processing, and idempotency. | [32_ai.md](constraint_threat_model/phase5/32_ai.md) | [32_ai_zh.md](constraint_threat_model/phase5/32_ai_zh.md) |
| **33. Production Observability** | Capturing cascading failures and abnormal traffic patterns. | [33_observability_cascad.md](constraint_threat_model/phase5/33_observability_cascad.md) | [33_observability_cascad_zh.md](constraint_threat_model/phase5/33_observability_cascad_zh.md) |

#### Module 12: Bi-Directional Guardrails
| Chapter | Description | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **34. NVIDIA NeMo Guardrails** | Enforcing strict I/O walls using `.co` rules. | [34_nvidia_nemo_guardrai.md](constraint_threat_model/phase5/34_nvidia_nemo_guardrai.md) | [34_nvidia_nemo_guardrai_zh.md](constraint_threat_model/phase5/34_nvidia_nemo_guardrai_zh.md) |
| **35. Local Guard Models** | Deploying Llama Guard as a lightweight safety interceptor. | [35_llama_guard_guardrai.md](constraint_threat_model/phase5/35_llama_guard_guardrai.md) | [35_llama_guard_guardrai_zh.md](constraint_threat_model/phase5/35_llama_guard_guardrai_zh.md) |
| **36. The Ultimate Capstone** | Delivering an Enterprise RAG that survives extreme constraints. | [36_chapter_36.md](constraint_threat_model/phase5/36_chapter_36.md) | [36_chapter_36_zh.md](constraint_threat_model/phase5/36_chapter_36_zh.md) |


## 1. Capability Map

The Capability Map ensures that as the project grows, new features naturally align under existing pillars without fracturing the architecture. We treat Resilience and Security as co-equal first-class citizens.

| Capability | Scope & Focus | Covered Threats / Constraints |
|---|---|---|
| **Prompt Security** | Securing the interaction layer between user and LLM. | Prompt Leak, Prompt Injection, Jailbreaking |
| **Context Security** | Securing the knowledge retrieval and injection pipeline. | RAG Poisoning, Indirect Injection, Data Exfiltration |
| **Runtime Security** | Real-time interception and policy enforcement. | Guardrail Bypasses, Harmful Content Generation |
| **Agent Security** | Tool Permission, Agent Identity, Agent Isolation, Multi-Agent Coordination, Workflow Authorization. | Tool Hijacking, Privilege Escalation, Unauthorized Workflow Execution |
| **Resilience & Reliability** | Circuit Breaker, Failover, Graceful Degradation, Queue Recovery, Retry Strategy, Idempotency, Backpressure, Rate Limiting. | Retrieval Collapse, Model Outage, Cascading Failure, Queue Saturation, Context Truncation, Agent Deadlock |
| **Security Operations** | Visibility, monitoring, and audit trails. | Lack of Traceability, Undetected Attacks |
| **Security Governance** | Standardized risk assessment and policy management. | Unquantified Risk, Ad-hoc Policy Enforcement |
| **DevSecOps** | Continuous security validation in the CI/CD pipeline. | Regression Vulnerabilities, Unsafe Dependencies |

---

## 2. Protected Assets

Before modeling threats, we must identify the critical assets within the architecture that require protection. Threats target assets; controls protect them.

- **`prompt`**: The foundational instructions (`system_prompt`) governing the AI's behavior and constraints.
- **`context`**: The retrieved knowledge chunks from the vector database injected into the prompt.
- **`memory`**: The conversational history, session state, and user-specific context.
- **`tool`**: External APIs, databases, and execution environments the agent can invoke.
- **`model`**: The underlying LLM itself (weights, inference endpoints, token usage).
- **`workflow`**: The orchestration logic, execution state, and multi-agent coordination pipelines.

---

## 3. Constraint & Threat Model

Our model formally identifies the critical constraints and attack vectors targeting our assets. 

### 🛡️ Class A: Adversarial Threats (Security)

Malicious attacks attempting to compromise system assets.

- **`prompt_leak`**: Attempts to extract the `system_prompt` or internal tool schemas via social engineering or edge-case manipulation.
- **`prompt_injection`**: Direct manipulation of the user input to override the `system_prompt` and hijack the LLM's goal.
- **`indirect_injection`**: Injecting malicious instructions via retrieved `context` (e.g., hidden text in a PDF, invisible markdown in a website).
- **`rag_poisoning`**: Compromising the vector database to return biased, harmful, or maliciously crafted `context` to the LLM.
- **`data_exfiltration`**: Forcing the LLM to output sensitive information from `context` or `memory` to an external attacker via encoded strings or external API calls.
- **`tool_hijacking`**: Tricking the agent into executing unauthorized `tool` commands (e.g., executing a malicious script, deleting a database).

### ⚠️ Class B: Operational Failures (Reliability)

Non-malicious physical and environmental constraints that cause system degradation.

- **`retrieval_collapse`**: The RAG pipeline fails to find valid content (returning empty, contradictory, or garbage context).
- **`context_truncation`**: The accumulated prompt length exceeds the model's maximum window size and is truncated by the runtime or API.
- **`model_unavailable`**: The upstream LLM API endpoint or local inference node goes down, times out, or becomes unreachable.
- **`queue_saturation`**: A sudden burst of traffic overwhelms the asynchronous processing queue, causing message pileup and extreme latency.
- **`cascading_failure`**: A single component's failure (e.g., a slow database query) hogs thread pools, dragging down the entire execution chain.
- **`agent_deadlock`**: In multi-agent environments, agents get stuck waiting on each other indefinitely, causing workflow stagnation.

---

## 4. Security Controls

Controls are the architectural primitives designed to mitigate the threats and constraints identified above. This creates a clean `Asset -> Threat -> Control` lineage.

- **`SecurityMiddleware`**: The primary API gateway interface intercepting all inbound and outbound LLM traffic.
- **`ContextGuard`**: Sanitizes, truncates, and validates `context` before it enters the prompt window (mitigates RAG Poisoning & Context Truncation).
- **`RuntimeJudge`**: The Evaluation Engine assessing inputs/outputs against safety and reliability metrics.
- **`FailoverRouter`**: Dynamically routes traffic to fallback models or local endpoints when the primary model goes down (mitigates Model Unavailable).
- **`CircuitBreaker`**: Rapidly fails requests and sheds load when downstream dependencies (e.g., vector DBs or agent tools) become unresponsive (mitigates Cascading Failures).

### Threat-to-Control Mapping

| Threat / Constraint | Primary Control |
| :--- | :--- |
| `prompt_leak` | `SecurityMiddleware` |
| `prompt_injection` | `SecurityMiddleware` + `ContextGuard` |
| `indirect_injection` | `ContextGuard` |
| `rag_poisoning` | `ContextGuard` |
| `data_exfiltration` | `RuntimeJudge` |
| `tool_hijacking` | `SecurityMiddleware` |
| `model_unavailable` | `FailoverRouter` |
| `cascading_failure` | `CircuitBreaker` |
| `context_truncation` | `ContextGuard` |
| `queue_saturation` | `CircuitBreaker` |
| `agent_deadlock` | `CircuitBreaker` / `Timeout` |

---

## 5. Sprint Alignment

Because Security and Reliability are unified, our pipeline components must evaluate both dimensions simultaneously.

*   **Sprint A** will instantiate this unified model into `security/threat_model/` (`model.yml`, `assets.yml`, `controls.yml`).
*   **Sprint B (Benchmark)** will generate test cases covering both dimensions (e.g., `{"id": "rag_poisoning_001", "category": "security"}` alongside `{"id": "retrieval_collapse_001", "category": "reliability"}`).
*   **Sprint B (Judge Engine)** will implement `RuntimeJudge` as a comprehensive **Evaluation Engine**, outputting a multi-dimensional scorecard:
    *   `Security Score` (powered by Safety validation rules)
    *   `Reliability Score`
    *   `Resilience Score`
    *   `Overall Runtime Score`
