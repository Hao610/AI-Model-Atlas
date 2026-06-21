<p align="center">
  <img src="https://github.com/user-attachments/assets/a51e8bb3-b2f3-4595-aee4-2272e2323086" alt="AI Model Atlas Logo" width="100">
</p>

# 🛡️ 安全与韧性 AI 运行时约束与威胁模型
> 构建生产级 AI 安全参考架构。
← 返回 [中文首页](../README_zh.md) | [English Version](CONSTRAINT_THREAT_MODEL.md)
## 课程大纲

### 🛡️ Phase 1: 核心基础与新型资产管理 (Foundations & Asset Management)
> **本阶段确立 LLM 安全的基础概念，从传统的应用安全理念过渡到全新的非结构化防御体系。**

#### Module 1: LLM 时代的供应链安全与零信任架构
| 章节 | 描述 | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **1. LLM 时代的 OWASP Top 10** | 传统网络安全在 AI 时代的全面失效与平移。 | [01_owasp_top_10_llm.md](constraint_threat_model/phase1/01_owasp_top_10_llm.md) | [01_owasp_top_10_llm_zh.md](constraint_threat_model/phase1/01_owasp_top_10_llm_zh.md) |
| **2. 非结构化攻击面** | 拆解大模型特有的攻击面：模型权重、中间件与数据流。 | [02_chapter_2.md](constraint_threat_model/phase1/02_chapter_2.md) | [02_chapter_2_zh.md](constraint_threat_model/phase1/02_chapter_2_zh.md) |
| **3. 零信任架构原则** | 如何对大模型的每一次输入/输出进行身份与安全边界隔离。 | [03_zero_trust.md](constraint_threat_model/phase1/03_zero_trust.md) | [03_zero_trust_zh.md](constraint_threat_model/phase1/03_zero_trust_zh.md) |

#### Module 2: 提示词资产化管理（Prompt as Code）
| 章节 | 描述 | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **4. 拒绝硬编码** | 在全栈项目中实现 Prompt 与代码解耦的工程规范。 | [04_prompt.md](constraint_threat_model/phase1/04_prompt.md) | [04_prompt_zh.md](constraint_threat_model/phase1/04_prompt_zh.md) |
| **5. Prompt 版本控制** | 提示词的多环境（Dev/Staging/Prod）动态灰度交付流。 | [05_prompt_dev_staging_p.md](constraint_threat_model/phase1/05_prompt_dev_staging_p.md) | [05_prompt_dev_staging_p_zh.md](constraint_threat_model/phase1/05_prompt_dev_staging_p_zh.md) |
| **6. Token 成本优化** | 高压缩率系统提示词的分词优化与成本熔断设计。 | [06_system_prompt_tokens.md](constraint_threat_model/phase1/06_system_prompt_tokens.md) | [06_system_prompt_tokens_zh.md](constraint_threat_model/phase1/06_system_prompt_tokens_zh.md) |

---

### 🧠 Phase 2: 高阶生产级提示词工程 (Advanced Production Prompting)
> **本阶段聚焦于构建高鲁棒性的提示词，确保输出的确定性，并防止逻辑退化。**

#### Module 3: 确定性控制流与动态少样本工程
| 章节 | 描述 | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **7. 动态少样本提示** | 利用向量数据库实时召回关联性最强的安全示例。 | [07_dynamic_few_shot.md](constraint_threat_model/phase2/07_dynamic_few_shot.md) | [07_dynamic_few_shot_zh.md](constraint_threat_model/phase2/07_dynamic_few_shot_zh.md) |
| **8. CoT 与 ToT 优化** | 复杂业务逻辑的思维链分步路由与思维树剪枝优化。 | [08_cot_tot.md](constraint_threat_model/phase2/08_cot_tot.md) | [08_cot_tot_zh.md](constraint_threat_model/phase2/08_cot_tot_zh.md) |
| **9. 角色对齐技术** | 防止在多智能体协同系统中出现角色塌陷与指令混乱。 | [09_role_alignment_agent.md](constraint_threat_model/phase2/09_role_alignment_agent.md) | [09_role_alignment_agent_zh.md](constraint_threat_model/phase2/09_role_alignment_agent_zh.md) |

#### Module 4: 强鲁棒性输出与退化控制
| 章节 | 描述 | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **10. 严格输出约束** | Pydantic 深度整合，尽可能约束模型输出为结构化 JSON。 | [10_pydantic_json.md](constraint_threat_model/phase2/10_pydantic_json.md) | [10_pydantic_json_zh.md](constraint_threat_model/phase2/10_pydantic_json_zh.md) |
| **11. 自愈与降级机制** | 应对上下文截断、输入噪声与结构化塌陷的运行时自动修补。 | [11_automated_self_corre.md](constraint_threat_model/phase2/11_automated_self_corre.md) | [11_automated_self_corre_zh.md](constraint_threat_model/phase2/11_automated_self_corre_zh.md) |
| **12. 动态超参数调优** | 基于实时幻觉率动态调整 Temperature 与 Top-p。 | [12_temperature_top_p.md](constraint_threat_model/phase2/12_temperature_top_p.md) | [12_temperature_top_p_zh.md](constraint_threat_model/phase2/12_temperature_top_p_zh.md) |

---

### 🥷 Phase 3: 对抗性黑客红队攻防 (Adversarial Red Teaming)
> **本阶段深入红队攻防测试，模拟提示词注入和 RAG 劫持等攻击以加固系统。**

#### Module 5: 提示词注入与新型越狱攻击
| 章节 | 描述 | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **13. 直接提示词注入** | 字符绕过、角色扮演与逻辑悖论攻击原理。 | [13_direct_prompt_inject.md](constraint_threat_model/phase3/13_direct_prompt_inject.md) | [13_direct_prompt_inject_zh.md](constraint_threat_model/phase3/13_direct_prompt_inject_zh.md) |
| **14. 多语言与编码注入** | 利用小众语种弱点突破系统提示词限制。 | [14_base64.md](constraint_threat_model/phase3/14_base64.md) | [14_base64_zh.md](constraint_threat_model/phase3/14_base64_zh.md) |
| **15. 越狱自动化** | 编写 Python 脚本自动寻找模型的死角。 | [15_auto_jailbreaking_py.md](constraint_threat_model/phase3/15_auto_jailbreaking_py.md) | [15_auto_jailbreaking_py_zh.md](constraint_threat_model/phase3/15_auto_jailbreaking_py_zh.md) |

#### Module 6: 间接注入与新型 RAG 漏洞
| 章节 | 描述 | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **16. 间接提示词注入** | 黑客在外部网页或 PDF 中埋藏的隐形恶意指令。 | [16_indirect_injection_p.md](constraint_threat_model/phase3/16_indirect_injection_p.md) | [16_indirect_injection_p_zh.md](constraint_threat_model/phase3/16_indirect_injection_p_zh.md) |
| **17. RAG 知识库劫持** | 智能体联网时，系统权限如何被恶意接管。 | [17_rag_agent.md](constraint_threat_model/phase3/17_rag_agent.md) | [17_rag_agent_zh.md](constraint_threat_model/phase3/17_rag_agent_zh.md) |
| **18. 视觉多模态攻击** | 利用视觉解析盲区实施渗透的越狱攻击。 | [18_visual_injection.md](constraint_threat_model/phase3/18_visual_injection.md) | [18_visual_injection_zh.md](constraint_threat_model/phase3/18_visual_injection_zh.md) |

#### Module 7: 知识防盗与隐私泄露防御
| 章节 | 描述 | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **19. 提示词泄露防范** | 破解提示词套取 (Prompt Leaking) 的社工套路。 | [19_prompt_leaking.md](constraint_threat_model/phase3/19_prompt_leaking.md) | [19_prompt_leaking_zh.md](constraint_threat_model/phase3/19_prompt_leaking_zh.md) |
| **20. 防御性元提示词** | 编写抗篡改的强鲁棒性“防御性 Meta-Prompts”。 | [20_meta_prompts.md](constraint_threat_model/phase3/20_meta_prompts.md) | [20_meta_prompts_zh.md](constraint_threat_model/phase3/20_meta_prompts_zh.md) |
| **21. PII 数据泄露防御** | 防止黑客套出底层向量库的个人隐私数据。 | [21_rag_pii.md](constraint_threat_model/phase3/21_rag_pii.md) | [21_rag_pii_zh.md](constraint_threat_model/phase3/21_rag_pii_zh.md) |

---

### ⚙️ Phase 4: CI/CD 自动化安全流水线 (Prompt DevSecOps)
> **本阶段将自动化安全扫描和模型评估集成到部署生命周期中。**

#### Module 8: 安全左移与静态扫描
| 章节 | 描述 | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **22. Git Commit 扫描** | 在代码提交阶段自动拦截 Prompt 模板泄露。 | [22_git_commit_prompt.md](constraint_threat_model/phase4/22_git_commit_prompt.md) | [22_git_commit_prompt_zh.md](constraint_threat_model/phase4/22_git_commit_prompt_zh.md) |
| **23. 静态分析工具** | 基于静态分析发现 Prompt 语义漏洞。 | [23_prompt.md](constraint_threat_model/phase4/23_prompt.md) | [23_prompt_zh.md](constraint_threat_model/phase4/23_prompt_zh.md) |
| **24. 依赖项审计** | 针对 LangChain / LlamaIndex 等框架的 CVE 监控集成。 | [24_langchain_llamaindex.md](constraint_threat_model/phase4/24_langchain_llamaindex.md) | [24_langchain_llamaindex_zh.md](constraint_threat_model/phase4/24_langchain_llamaindex_zh.md) |

#### Module 9: 自动化跑分与优化
| 章节 | 描述 | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **25. DSPy / TextGrad** | 自动进化出更安全、更聪明的 Prompt。 | [25_dspy_textgrad_prompt.md](constraint_threat_model/phase4/25_dspy_textgrad_prompt.md) | [25_dspy_textgrad_prompt_zh.md](constraint_threat_model/phase4/25_dspy_textgrad_prompt_zh.md) |
| **26. 自动化红队测试** | 在流水线中自动实施红队压力攻击。 | [26_automated_red_teamin.md](constraint_threat_model/phase4/26_automated_red_teamin.md) | [26_automated_red_teamin_zh.md](constraint_threat_model/phase4/26_automated_red_teamin_zh.md) |
| **27. 熔断阻断器配置** | 在 GitHub Actions 中实现越狱拦截。 | [27_github_actions.md](constraint_threat_model/phase4/27_github_actions.md) | [27_github_actions_zh.md](constraint_threat_model/phase4/27_github_actions_zh.md) |

#### Module 10: LLM-as-a-Judge 自动评估
| 章节 | 描述 | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **28. 安全裁判矩阵** | 构建专属的“安全裁判模型（Safety Judge）”打分矩阵。 | [28_safety_judge.md](constraint_threat_model/phase4/28_safety_judge.md) | [28_safety_judge_zh.md](constraint_threat_model/phase4/28_safety_judge_zh.md) |
| **29. 三维量化指标** | 建立幻觉率、准确率与对抗通过率的量化体系。 | [29_chapter_29.md](constraint_threat_model/phase4/29_chapter_29.md) | [29_chapter_29_zh.md](constraint_threat_model/phase4/29_chapter_29_zh.md) |
| **30. 性能追踪看板** | 长期迭代评测：建立 Prompt 资产的性能监控。 | [30_prompt.md](constraint_threat_model/phase4/30_prompt.md) | [30_prompt_zh.md](constraint_threat_model/phase4/30_prompt_zh.md) |

---

### 🛡️ Phase 5: 网关容灾与终极护栏 (Runtime Guardrails)
> **本阶段引入动态流量管理、熔断器和严格的 API 级别护栏，构建极具弹性的系统架构。**

#### Module 11: 零信任网关与分布式容灾
| 章节 | 描述 | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **31. AI 网关容灾架构** | 实现熔断器与多模型节点不可达时的防灾分流。 | [31_ai_gateway_circuit_b.md](constraint_threat_model/phase5/31_ai_gateway_circuit_b.md) | [31_ai_gateway_circuit_b_zh.md](constraint_threat_model/phase5/31_ai_gateway_circuit_b_zh.md) |
| **32. 异步一致性队列** | 应对大并发延迟、乱序处理与 AI 管道的幂等设计。 | [32_ai.md](constraint_threat_model/phase5/32_ai.md) | [32_ai_zh.md](constraint_threat_model/phase5/32_ai_zh.md) |
| **33. 生产线日志审计** | 在可观测性平台中捕获级联故障与异常流量。 | [33_observability_cascad.md](constraint_threat_model/phase5/33_observability_cascad.md) | [33_observability_cascad_zh.md](constraint_threat_model/phase5/33_observability_cascad_zh.md) |

#### Module 12: 双向护栏与全约束实战闭环
| 章节 | 描述 | English Guide | 中文指南 |
| :--- | :--- | :--- | :--- |
| **34. NeMo Guardrails** | 深度实战：通过 `.co` 规则建立运行时输入/输出防御墙。 | [34_nvidia_nemo_guardrai.md](constraint_threat_model/phase5/34_nvidia_nemo_guardrai.md) | [34_nvidia_nemo_guardrai_zh.md](constraint_threat_model/phase5/34_nvidia_nemo_guardrai_zh.md) |
| **35. 本地轻量级护栏** | 部署 Llama Guard 作为流量的双向安全护栏。 | [35_llama_guard_guardrai.md](constraint_threat_model/phase5/35_llama_guard_guardrai.md) | [35_llama_guard_guardrai_zh.md](constraint_threat_model/phase5/35_llama_guard_guardrai_zh.md) |
| **36. 终极实战交付** | 在检索失效与模型崩溃的三重约束下优雅降级的企业系统。 | [36_chapter_36.md](constraint_threat_model/phase5/36_chapter_36.md) | [36_chapter_36_zh.md](constraint_threat_model/phase5/36_chapter_36_zh.md) |


## 1. 能力地图 (Capability Map)

能力地图确保项目随着扩展，新功能能够自然地归类到现有的支柱下，而不会破坏架构的完整性。我们将弹性 (Resilience) 和安全性 (Security) 视为同等重要的一等公民。

| 能力模块 | 范围与焦点 | 覆盖的威胁 / 约束 |
|---|---|---|
| **提示词安全 (Prompt Security)** | 保护用户与 LLM 之间的交互层。 | 提示词泄漏 (Prompt Leak)、提示词注入 (Prompt Injection)、越狱 (Jailbreaking) |
| **上下文安全 (Context Security)** | 保护知识检索和注入管道。 | RAG 投毒 (RAG Poisoning)、间接注入 (Indirect Injection)、数据外泄 (Data Exfiltration) |
| **运行时安全 (Runtime Security)** | 实时拦截与策略执行。 | 护栏绕过 (Guardrail Bypasses)、有害内容生成 (Harmful Content Generation) |
| **智能体安全 (Agent Security)** | 工具权限、智能体身份、智能体隔离、多智能体协调、工作流授权。 | 工具劫持 (Tool Hijacking)、提权 (Privilege Escalation)、未授权工作流执行 |
| **弹性与可靠性 (Resilience & Reliability)** | 熔断器、故障转移、优雅降级、队列恢复、重试策略、幂等性、背压、限流。 | 检索崩溃 (Retrieval Collapse)、模型宕机 (Model Outage)、级联故障 (Cascading Failure)、队列饱和 (Queue Saturation)、上下文截断 (Context Truncation)、智能体死锁 (Agent Deadlock) |
| **安全运营 (Security Operations)** | 可见性、监控和审计跟踪。 | 缺乏可追溯性、未检测到的攻击 |
| **安全治理 (Security Governance)** | 标准化风险评估与策略管理。 | 未量化的风险、临时的策略执行 |
| **DevSecOps** | CI/CD 管道中的持续安全验证。 | 回归漏洞、不安全的依赖 |

---

## 2. 受保护的资产 (Protected Assets)

在对威胁进行建模之前，我们必须识别架构中需要保护的关键资产。威胁以资产为目标；控制措施保护资产。

- **`prompt`**: 控制 AI 行为和约束的基础指令 (`system_prompt`)。
- **`context`**: 从向量数据库中检索出并注入到提示词中的知识块。
- **`memory`**: 对话历史、会话状态和特定于用户的上下文。
- **`tool`**: 智能体可以调用的外部 API、数据库和执行环境。
- **`model`**: 底层 LLM 本身 (权重、推理端点、Token 使用量)。
- **`workflow`**: 编排逻辑、执行状态和多智能体协调管道。

---

## 3. 约束与威胁模型 (Constraint & Threat Model)

我们的模型正式识别了针对我们资产的关键约束和攻击向量。

### 🛡️ A 类：对抗性威胁 (安全) / Class A: Adversarial Threats (Security)

试图破坏系统资产的恶意攻击。

- **`prompt_leak`**: 试图通过社会工程或边缘情况操作提取 `system_prompt` 或内部工具模式。
- **`prompt_injection`**: 直接操纵用户输入，以覆盖 `system_prompt` 并劫持 LLM 的目标。
- **`indirect_injection`**: 通过检索到的 `context` 注入恶意指令 (例如，PDF 中的隐藏文本、网站中的不可见 Markdown)。
- **`rag_poisoning`**: 破坏向量数据库，以向 LLM 返回有偏见的、有害的或恶意制作的 `context`。
- **`data_exfiltration`**: 迫使 LLM 将 `context` 或 `memory` 中的敏感信息通过编码字符串或外部 API 调用输出给外部攻击者。
- **`tool_hijacking`**: 欺骗智能体执行未经授权的 `tool` 命令 (例如，执行恶意脚本、删除数据库)。

### ⚠️ B 类：运维故障 (可靠性) / Class B: Operational Failures (Reliability)

导致系统降级的非恶意物理和环境约束。

- **`retrieval_collapse`**: RAG 管道未能找到有效内容 (返回空的、矛盾的或垃圾上下文)。
- **`context_truncation`**: 累积的提示词长度超过模型最大窗口大小而被强制截断。
- **`model_unavailable`**: 上游 LLM API 端点或本地推理节点宕机、超时或无法访问。
- **`queue_saturation`**: 突发的流量激增使异步处理队列不堪重负，导致消息堆积和极端延迟。
- **`cascading_failure`**: 单个组件的故障 (例如，缓慢的数据库查询) 占用线程池，拖垮整个执行链。
- **`agent_deadlock`**: 在多智能体环境中，智能体陷入无限等待彼此的状态，导致工作流停滞。

---

## 4. 安全控制措施 (Security Controls)

控制措施是为了减轻上述识别出的威胁和约束而设计的架构原语。这创建了一条清晰的 `资产 (Asset) -> 威胁 (Threat) -> 控制措施 (Control)` 链路。

- **`SecurityMiddleware`**: 拦截所有入站和出站 LLM 流量的主要 API 网关接口。
- **`ContextGuard`**: 在 `context` 进入提示词窗口之前对其进行清理、截断和验证 (缓解 RAG 投毒和上下文截断)。
- **`RuntimeJudge`**: 评估引擎，根据安全性和可靠性指标评估输入/输出。
- **`FailoverRouter`**: 当主模型宕机时，将流量动态路由到后备模型或本地端点 (缓解模型不可用)。
- **`CircuitBreaker`**: 当下游依赖项 (如向量数据库或智能体工具) 变得无响应时，快速使请求失败并减轻负载 (缓解级联故障)。

### 威胁到控制措施的映射 (Threat-to-Control Mapping)

| 威胁 / 约束 (Threat / Constraint) | 主要控制措施 (Primary Control) |
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

## 5. 冲刺对齐 (Sprint Alignment)

由于安全性和可靠性是统一的，我们的管道组件必须同时评估这两个维度。

*   **冲刺 A (Sprint A)** 将把这个统一模型实例化到 `security/threat_model/` (`model.yml`, `assets.yml`, `controls.yml`) 中。
*   **冲刺 B - 基准测试 (Sprint B - Benchmark)** 将生成涵盖两个维度的测试用例 (例如，`{"id": "rag_poisoning_001", "category": "security"}` 与 `{"id": "retrieval_collapse_001", "category": "reliability"}`并列)。
*   **冲刺 B - 裁判引擎 (Sprint B - Judge Engine)** 将实现 `RuntimeJudge` 作为一个全面的**评估引擎 (Evaluation Engine)**，输出多维度评分卡：
    *   `Security Score` (安全分数，由安全验证规则提供支持)
    *   `Reliability Score` (可靠性分数)
    *   `Resilience Score` (弹性分数)
    *   `Overall Runtime Score` (整体运行时分数)
