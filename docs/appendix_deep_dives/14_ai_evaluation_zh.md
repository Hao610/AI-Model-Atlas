← 返回 [深潜专题目录](../DEEP_DIVES_zh.md) | [[English] (14_ai_evaluation.md)](14_ai_evaluation.md) | [中文]

---

# 14. AI 系统评测理论：我们如何度量智能？
> **关于人工智能度量的极限、投影与优化闭环的正式理论框架。**

随着大型语言模型从静态问答引擎过渡到自主认知系统，传统的静态跑分榜单（Leaderboards）正在丧失其诊断价值。本章构建了一个统一的数学与系统工程框架——**AI 智能度量理论 (AIMT)**。在该框架中，评测不再是一系列静态测试题目的集合，而是隐式执行流形（Latent Execution Manifold）的有损投影。

---

## 🌐 AI 评测栈（观测算子层级）

在形式化评测指标之前，我们根据观测算子的数学类型，将 AI 评测的观测边界划分为四层体系：

```text
  LEVEL 4: 分布偏移评测 [O_L4] (AGI 边界，分布外泛化与稳定性度量)
      ▲
      │
  LEVEL 3: 轨迹评测 [O_L3] (智能体闭环，POMDP 执行流，RAG 系统级测试)
      ▲
      │
  LEVEL 2: 链式评测 [O_L2] (思考链轨迹，CoT 步骤级逻辑校验)
      ▲
      │
  LEVEL 1: 单点评测 [O_L1] (静态问答，单步输入到输出的映射)
```

### 🗺️ AI 评测体系演进脉络

```text
                       AI Evaluation Evolution

                 GLUE (2018)：基础 NLP 单点分类任务
                       │
                       ▼
                 SuperGLUE (2019)：高难度 NLP 上下文任务
                       │
                       ▼
                 MMLU (2021)：单点多学科综合知识选择题
                       │
                       ▼
                 HumanEval (2021)：基础单点代码生成测试
                       │
                       ▼
                 MATH (2021)：多步链式数学推理评测
                       │
                       ▼
                 GPQA (2023)：高难度博士级链式推理
                       │
                       ▼
                 SWE-bench (2024)：多文件软件工程实战轨迹测试
                       │
                       ▼
                 AgentBench / GAIA (2025+)：动态智能体多轮沙盒交互
                       │
                       ▼
                 BrowseComp (2025+)：网页浏览与动态执行控制流闭环
```

---

## 🧬 核心公理系统

我们将评测形式化为：将模型参数、系统工程脚手架以及任务环境分布，映射为一个标量效用值的泛函。

### Definition 14.1 (统一评测系统)
设 $M$ 为模型参数流形（神经网络权重），$S$ 为系统算子（包含 Prompt 脚手架、检索器、外部工具等），$\mathcal{D}$ 为任务环境分布。系统的评测值定义为在任务环境分布下，系统运行轨迹 $\tau$ 在特定观测算子下的效用期望：

$$\mathcal{E}(M, S, \mathcal{D}, \mathcal{O}_i) = \mathbb{E}_{\tau \sim \mathcal{D}} \left[ \mathcal{O}_i(M, S, \tau) \right]$$

### Definition 14.2 (观测空间)
形式化观测空间 $\mathcal{O}$ 定义为一族投影算子的集合，它负责将高维的隐式执行流形投影为可度量的标量分数：

$$\mathcal{O} = \{ \mathcal{O}_{\text{acc}}, \mathcal{O}_{\text{reason}}, \mathcal{O}_{\text{pref}}, \mathcal{O}_{\text{traj}} \}$$

其中：
* $\mathcal{O}_{\text{acc}}$ 代表静态单点问答的准确率度量。
* $\mathcal{O}_{\text{reason}}$ 代表多步推理链的中间步骤校验度量。
* $\mathcal{O}_{\text{pref}}$ 代表随机人类偏好估计。
* $\mathcal{O}_{\text{traj}}$ 代表顺序执行轨迹下的成功/失败状态度量。

### Theorem 14.0 (AI 评测等价性定理)
*所有 AI 评测方法均为统一评测泛函 $\mathcal{E}(M, S, \mathcal{D}, \mathcal{O}_i)$ 在特定观测约束下的局部有损投影。*

### Theorem 14.1 (观测损耗原理 / 没有免费的评测定理)
*一切评测皆为信息压缩，不存在无损的智能测量算子。*

$$\forall S, \quad \nexists \mathcal{O}_i \in \mathcal{O} \quad \text{s.t.} \quad \mathcal{O}_i(S) = S$$

### 评测投影交换图

该图展示了各种不同的评测范式，如何在不同的观测算子下，作为隐式执行流形 $\mathcal{E}^*$ 的有损投影存在：

```text
                           隐式执行流形 E*
                                  │
                                  ▼
                     E(M, S, D, O_i) [Theorem 14.0]
                                  │
       ┌──────────────────────────┼──────────────────────────┐
       │                          │                          │
     O_acc                     O_pref                     O_traj
 (基准测试: L1/L2)          (盲测竞技场: L3)            (智能体: L3)
       │                          │                          │
       └──────────────────────────┼──────────────────────────┘
                                  │
                                  ▼
                            分布不变性 (L4)
                           [Definition 14.5]
                                  │
                                  ▼
                            评测控制闭环 (RL)
```

### 🧠 算子操作解释层 (Operational Interpretation Layer)
尽管所有评测方法都是隐式执行流形的投影，但每个观测算子实际上对应着不同的**工程约束边界**：
* $\mathcal{O}_{\text{acc}}$：受限于记忆容量的符号压缩度量（静态题库，考查事实性记忆与检索）。
* $\mathcal{O}_{\text{pref}}$：人类偏好对齐下的随机选择度量（考查“看起来聪明”的回复风格与主观偏好）。
* $\mathcal{O}_{\text{traj}}$：部分可观测环境下的顺序决策控制度量（考查多轮动态交互与纠错能力）。

---

## 1. 静态基准测试与跑分坍缩 (L1/L2)

传统的基准测试（如 MMLU、GPQA）专注于静态事实库检索或单步计算。

### Corollary 14.1 (静态基准测试投影 / 跑分坍缩)
设 $x$ 为静态输入问题，$y$ 为标准答案。在静态单点评测（Level 1 和 Level 2）下，观测算子将高维轨迹空间坍缩为单步损失函数的估计：

$$\mathcal{O}_{\text{acc}}(M, S, \tau) \approx \mathbb{I}[f_M(x) = y]$$

这种坍缩导致了以下三个核心工程缺陷：
1. **数据污染 (作弊与漏题)**：由于评测集是静态的，测试样本极易泄漏进训练分布 $\mathcal{D}_{\text{train}}$，这使得原本考查推理能力的测试坍缩为模型的**事实背诵**。
2. **榜单过拟合 (Leaderboard Overfitting)**：厂商针对特定跑分集风格进行靶向微调，最大化了单点指标，却损害了分布外的真实泛化能力。
3. **考试与工作的断层**：选择题拿高分不等于能做软件开发。一个在 MMLU 上拿到 $90\%$ 分数的模型，在真实的多文件代码修改与 Debug 任务中依然可能频繁报错。

---

## 2. 随机偏好投影 (L3 - LMSYS 竞技场)

为了摆脱静态题库的局限，行业广泛采用双盲众包的 LMSYS Chatbot Arena。

### Definition 14.3 (人类偏好估计器)
竞技场通过将两台模型的输出（$A$ 和 $B$）呈现给从用户分布 $\mathcal{D}_{\text{user}}$ 中采样的真实人类，并利用 Logistic 函数计算胜率从而估计 Elo 分数：

$$P(A \succ B) = \frac{1}{1 + 10^{(R_B - R_A)/400}}$$

### Corollary 14.2 (偏好对齐失真 / 偏好投影)
竞技场输出的 Elo 排名是人类偏好分布的随机投影，而非模型绝对正确性的度量：

$$P(\text{Win}) = \pi_{\text{pref}}(\text{Output} \mid \mathcal{D}_{\text{user}}) \neq P(\text{Correctness} \mid \tau)$$

这种偏好投影引入了明显的统计偏差：
* **感官智能 vs. 真实能力**：竞技场天然偏好“看起来很聪明”的特征（如长回答、结构化排版、礼貌温和的人设），而非数理逻辑或代码运行的绝对正确性。
* **RLHF/DPO 的合谋**：经过高度偏好对齐（参见[第 13 章](13_rlhf_alignment_zh.md)）的模型，学会了迎合人类的感官偏好来刷高胜率，但这并未提升其底层推理上限。

---

## 3. 轨迹投影与 POMDP 智能体评测 (L3 - Agents)

当 AI 系统向自主智能体（参见[第 9 章](09_agent_mechanics_zh.md)）演进时，它必须与外部环境和工具进行交互。

### Definition 14.4 (智能体 POMDP 环境)
智能体的运行环境被形式化为一个部分可观测马尔可夫决策过程：

$$\text{Agent Environment} = \langle S_P, A_P, T_P, R_P, \Omega, O_P \rangle$$

其中 $S_P$ 为环境状态空间，$A_P$ 为智能体动作空间，$T_P: S_P \times A_P \rightarrow \mathcal{P}(S_P)$ 为状态转移概率，$R_P$ 为即时奖惩，$\Omega$ 为观测空间，$O_P: S_P \times A_P \rightarrow \mathcal{P}(\Omega)$ 为观测概率。

### Corollary 14.3 (轨迹投影)
评估智能体性能的本质是评估状态-动作序列构成的运行轨迹 $\tau = (s_0, a_0, o_1, r_1, \dots, s_n)$，而非单步输出：

$$\text{Eval}(\text{Agent}) = f(\tau)$$

#### ✈️ 案例研究：订票智能体
考虑目标：*“帮我购买明天飞往上海最便宜的机票”*
* 静态基准测试完全无法评估这一任务。
* 智能体必须执行搜索动作 ($a_0$)，观测返回的价格列表 ($o_1$)，理解页面布局 ($s_1$)，处理网络超时的 API 报错 ($a_1$)，填写表单并确认交易。
* 评测算子 $\mathcal{O}_{\text{traj}}$ 评估的是这串多轮控制序列在特定工程约束下的成功概率。这也是 **AgentBench**、**GAIA** 和 **BrowseComp** 等动态评测集的核心逻辑。

---

## 4. 系统不可约性与系统分解定理

工程师经常混淆“模型评测”与“系统评测”。

### Theorem 14.2 (系统分解定理 / 系统不可约性)
系统效用是模型算子 $M$ 与交互算子 $I$（代表 RAG 检索、MCP 工具总线、上下文窗口及硬件延迟约束）的复合函数：

$$S = M \circ I$$

### Corollary 14.4 (系统不可约性)
*系统整体性能无法等价还原为模型单体性能 ($S \neq M$)。*

高分模型不等于高分系统：
* 在 RAG 系统中（参见[第 5 章](05_rag_principles_zh.md)），如果检索器（Retriever）召回了垃圾片段（例如由于[第 4 章](04_vector_db_zh.md)中的不良分块设计），即便大模型单体 GPQA 跑分高达 $90\%$，系统最终也会输出幻觉。
* 在智能体系统中（参见[第 9 章](09_agent_mechanics_zh.md)），如果外部工具的 API 崩溃，或者上下文窗口管理机制失效导致关键记忆丢失（参见[第 7 章](07_needle_test_zh.md)），无论模型自身参数规模有多大，系统都会瞬间崩溃。

---

## 5. 多目标推理评测与帕累托前沿 (L2)

推理模型（如[第 11 章](11_reasoning_models_zh.md)中的 DeepSeek-R1 或 OpenAI o1）引入了生成时算力（Test-Time Compute）。

### Corollary 14.5 (帕累托推理前沿)
推理能力的评估是一个多目标优化问题，不能用单一的标量准确率概括：

$$\text{Score} = f(\text{Correctness}, \text{Tokens}_{\text{think}}, \text{Time}, \text{Stability})$$

这带来了评测范式的重构：
* **打破“非黑即白”的评测**：传统测试只关注最终答案是否正确（$\mathbb{I}[\text{Correct}]$）。在推理时代，我们必须将“思考成本”引入度量维度。
* **帕累托效率**：更强的推理模型，不仅是准确率更高的模型，更是能在**更低的计算预算**（思考 Token 数量、推理时间）下达到同等准确率的模型。

---

## 6. 分布偏移与 AGI 边界 (L4)

评测的终极局限是什么？它又是如何定义 AGI 的？

### Definition 14.5 (分布不变性原理)
一个 AI 系统实现通用人工智能 (AGI) 的充要条件是，其评测表现对于任意非平稳分布偏移的任务环境集均保持投影不变性：

$$\text{AGI} \iff \forall \mathcal{O}_i \in \mathcal{O}, \quad \forall \mathcal{D}' \in \mathbf{D}_{\text{shift}}, \quad \mathcal{E}(M, S, \mathcal{D}', \mathcal{O}_i) \sim \mathcal{E}(M, S, \mathcal{D}, \mathcal{O}_i)$$

### Corollary 14.6 (AGI 泛化上界)
设 $\mathcal{D}_{\text{train}}$ 为训练分布，$\mathcal{D}_{\text{test}}$ 为发生偏移的测试环境分布。泛化差距定义为这两者之间的损失期望差：

$$\text{AGI Gap} = \mathbb{E}_{\tau \sim \mathcal{D}_{\text{train}}}[\mathcal{O}_i(M, S, \tau)] - \mathbb{E}_{\tau \sim \mathcal{D}_{\text{test}}}[\mathcal{O}_i(M, S, \tau)]$$

静态基准测试只能在独立同分布 (i.i.d.) 假设下近似度量智能。真正的通用智能，由模型在任意未知环境下的**分布外泛化稳定性**所定义。

---

## 7. 隐式执行流形

我们通过最后的评测收束定理，完成 AI 系统评测理论的闭环。

### Theorem 14.3 (评测坍缩定理)
*所有评测方法（基准测试、盲测竞技场、智能体轨迹）均是单一隐式执行流形 $\mathcal{E}^*$ 的有损投影。*

$$\forall \mathcal{O}_i \in \mathcal{O}, \quad \mathcal{E}(M, S, \mathcal{D}, \mathcal{O}_i) \text{ is a projection of } \mathcal{E}^*$$

---

## 🔄 评测控制闭环（系统驱动器）

评测绝非 AI 生命周期的终点，而是驱动系统持续进化的梯度信号。

### Corollary 14.7 (评测控制闭环)
评测泛函构成了更新系统算子与调整模型参数的控制闭环：

$$E_t \xrightarrow{\text{优化更新}} S_{t+1}, M_{t+1} \xrightarrow{\text{部署发布}} E_{t+1}$$

```text
       ┌───────────────── 系统遥测指标 ─────────────────┐
       ▼                                                │
  系统评测 ──► 监督微调 SFT / DPO ──► 部署上线 ──► 再次评测
       ▲                                                │
       └────────────────── 参数强化强化 ────────────────┘
```

这个控制闭环按照如下机制循环运转：
1. **系统评测** ($E_t$) 暴露当前系统的具体缺陷（检索质量差、大模型幻觉、工具调用死循环）。
2. **优化更新** 通过调整交互算子 $I$（如重写 RAG 检索参数、优化 Tool 结构描述）和微调模型参数流形 $M$（如通过 DPO/RL 强化对齐）来升级系统。
3. **部署发布** 将新系统置入新的环境数据中运行，从而开启下一轮评测状态 ($E_{t+1}$)。

评测不是旁观的诊断指标，它是自适应智能系统演进的**梯度源泉**。

---

现在我们已经建立了系统度量与评测的底层数学逻辑，接下来让我们在 [AI 系统失效模式理论：从评测到崩溃](15_failure_modes_zh.md) 中，探究系统崩溃的物理本质。

