---
title: Automating and Optimizing Financial Signal Discovery with Multi-Agent Systems
created: 2026-05-22
updated: 2026-05-22
type: raw-source
tags: [agent, multi-agent, evaluation, workflow, finance, nvidia]
source_url: https://developer.nvidia.com/blog/automating-and-optimizing-financial-signal-discovery-with-multi-agent-systems/
source_site: NVIDIA Technical Blog
published: 2026-05-21
extracted: 2026-05-22
extraction_note: Direct HTML fetch with browser-like headers; extracted .entry-content source prose from NVIDIA Technical Blog. web_extract returned a synthesized summary and was not used as source.
summary_path: ~/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260522-195212-Automating-and-Optimizing-Financial-Signal-Discovery-with-Multi-Agent-Systems-2246843-812495160-summary.md
status: captured
---

# Automating and Optimizing Financial Signal Discovery with Multi-Agent Systems

## Provenance

- Source URL: https://developer.nvidia.com/blog/automating-and-optimizing-financial-signal-discovery-with-multi-agent-systems/
- Publisher: NVIDIA Technical Blog
- Authors: Peihan Huo, Yang Shen, Hanyue He, Ioana Boier
- Published: 2026-05-21
- Extracted: 2026-05-22
- Extraction limitation: Direct HTML extraction returned substantial source prose from `.entry-content`; the article includes formulas, configuration snippets, and backtest statistics, but not the underlying S&P 500 dataset or full backtest engine implementation.
- Gemini summary: `~/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260522-195212-Automating-and-Optimizing-Financial-Signal-Discovery-with-Multi-Agent-Systems-2246843-812495160-summary.md`

## Local summary

Source URL: https://developer.nvidia.com/blog/automating-and-optimizing-financial-signal-discovery-with-multi-agent-systems/
Source title: Automating and Optimizing Financial Signal Discovery with Multi-Agent Systems
Extraction route: direct_html
Fallback reason: web_extract_generated_summary
Source quality: full
Extraction note: Direct HTML fetch with browser-like headers; extracted .entry-content source prose from NVIDIA Technical Blog. web_extract returned a synthesized summary and was not used as source.

---

标题：使用多智能体系统自动化与优化金融信号发现

一句话结论：NVIDIA 提出了一种基于 NeMo Agent Toolkit 构建的多智能体闭环系统，通过脑暴智能体、代码翻译智能体与回测评估智能体的协同迭代，实现了量化交易信号的自主发现与优化，并在标普500数据回测中生成了统计显著的动量反转信号。

核心观点与论证：
- 观点：多智能体协同设计可将碎片化的手动量化信号研发流程转化为全自动的演进闭环。
  依据/论证：系统设计了三种专业智能体：Signal Agent（生成信号 JSON 蓝图）、Code Agent（将蓝图转译为内联 Python 代码）以及 Evaluation Agent（回测并计算 Rank IC，不合格则向 Signal Agent 反馈优化建议）。三者通过 YAML 配置驱动的 NeMo Agent Toolkit 衔接，实现无人工干预的自动循环。
- 观点：为语言模型提供限制性数学算子库是防止数学公式“幻觉”并保证代码可用性的核心机制。
  依据/论证：文章没有让大模型自由生成数学公式，而是为其提供了一个包含 66 个算子（如 Rank_Add、TS_Return、Decay_Exp 等）的结构化计算器库（calculator.json），为模型提供具备明确输入输出、签名与经济学含义的积木块，确保了生成结果的逻辑严密性与代码可转译性。
- 观点：配置驱动与实时推理链路观测是提升高延迟、高逻辑性金融智能体系统研发效率的关键。
  依据/论证：系统逻辑、模型选择、IC 阈值等参数完全在单一的 config.yml 中集中配置，使得调整实验无需改动源码；同时，引入 Arize Phoenix 追踪 NIM 驱动的智能体推理轨迹，在多步骤的高延迟回测循环中实时可视化 LLM 思考过程，从而快速定位和调试“公式成立但经济无意义”的静默失败。

关键细节：
- 核心模型：信号生成使用通过 NVIDIA NIM 部署的 nemotron-3-nano-30b-a3b 开源模型。
- 评价指标：评估阶段采用 Rank IC（排名信息系数），即信号值的截面排名与后续资产收益排名的相关性。该指标相比 Pearson IC 对异常值更鲁棒。行业公认优秀的机构级信号 Rank IC 均值在 0.02 到 0.05 之间，高于 0.05 为极强信号。
- 实验配置与命令：通过执行命令 `nat run --config_file configs/config-optimization.yml --input "momentum signals"` 启动动量信号发现，系统默认配置进行 3 次迭代。
- 生成信号1（指数成交量调整动量）：公式为 `Signal_1(t) = (Close(t) - Close(t-10)) / (Close(t-10)) / EWMA_10[Volume](t)`。其背后的逻辑是：在低流动性或薄弱交易量下产生的 10 天价格收益，会被赋予更大的信号权重。
- 生成信号2（排名调整收益动量）：公式为 Signal_2(t) ∝ Rank_t(Close) · Rank_t(TS_Return(Close, 10))。利用截面分位数（值域在 0 到 1 之间）相乘，剔除中庸资产，筛选出价格和近期收益率同时处于极高位的股票。
- 回测表现：系统最终筛选出“排名调整收益动量”信号，在标普 500 指数成分股上进行了跨越 3504 个交易日的回测。结果为：Mean IC 为 -0.0134，IC 标准差为 0.1483，T 统计量为 -5.37，p-value 极度显著（p < 10^-7），正 IC 比例为 46.38%。

可信度与局限：
- 证据较强部分（高可信度）：文章给出了清晰的数学公式推导（如双重 cross-sectional 排名相乘、EWMA 分母设计）以及详尽的回测统计学数据。3504 个交易日的大样本回测，配合极具说服力的 T 统计量（-5.37）与近乎为零的 p-value，证实了该系统生成的动量信号在标普 500 历史数据中具有明确的统计显著性（表现为显著的短期反转/Underperformance 倾向）。
- 证据较弱与局限部分（主观推演与解释）：首先，该信号回测得到的 Mean IC 绝对值仅为 0.0134，实际上低于系统设定的 0.02 机构级合格阈值（文章称其为在 2 次迭代后勉强接受的“best-effort”结果），文章对该未达标信号的经济价值解释带有一定的乐观主观色彩。其次，回测仅在 S&P 500 历史数据集上完成，未考虑实盘交易中的滑点、佣金和市场冲击成本，亦未在非股票市场（如加密货币或低流动性资产）中验证其泛化能力。

来源元数据：
- Source URL: https://developer.nvidia.com/blog/automating-and-optimizing-financial-signal-discovery-with-multi-agent-systems/
- 提取质量或局限：本文档提取自 NVIDIA 官方技术博客的架构解析和 Notebook 实践说明。文章包含清晰的 YAML 配置、回测指标输出日志和完整的公式细节，但未包含底层 S&P 500 CSV 数据源和具体回测引擎的实现代码。

工程复盘启发：
- [作者观点映射] 在特定垂直领域（如量化金融或医疗），降低大模型“幻觉”的最佳策略是限制其自由度。通过为模型提供结构化、有限制的“工具箱”（如 66 个精简的数学算子定义），我们可以让模型在已知规则的积木堆中进行逻辑拼接，这远比通过 Prompt 警告模型“不要编造”更具工程实用性。
- [推论] 自动化多智能体系统的“演进闭环”能够成功运转，前提是其反馈链路必须依赖客观、可量化的评估指标。本案中系统使用 Rank IC 统计值和 P 值作为 Evaluation Agent 输出给 Signal Agent 的反馈参数，这种高度结构化的数字反馈能够给优化模型提供清晰的改进梯度，比纯代码运行报错信息更能指导智能体向正确目标逼近。

可执行建议：
- 本文有方法启发，但暂无直接可执行建议。

## Extracted source

Source URL: https://developer.nvidia.com/blog/automating-and-optimizing-financial-signal-discovery-with-multi-agent-systems/
Title: Automating and Optimizing Financial Signal Discovery with Multi-Agent Systems
Extraction note: Direct HTML fetch with browser-like headers; extracted .entry-content source prose from NVIDIA Technical Blog. web_extract returned a synthesized summary and was not used as source.

In quantitative finance, researchers build algorithms to trade assets, derivatives, and other financial instruments. A key part of that work is finding signals: patterns in messy market data that may help predict future returns. These signals can come from price and volume data, economic indicators, fundamentals, or alternative sources like news sentiment.
For years, quant firms have uncovered and tested signals largely by hand. Traditionally, quantitative researchers have to manually hypothesize, code, backtest, and refine hundreds of potential signals. The workflow is often fragmented, moving between data scientists, developers, and analysts, which creates significant lag in a market that moves in milliseconds. Now, AI can help automate parts of this workflow and speed up the research cycle. The
quantitative signal discovery agent developer example
from NVIDIA shows how to automate signal discovery using agentic architecture built with the
NVIDIA Nemotron
family of open models and the
NVIDIA NeMo Agent Toolkit
open-source library.
In this blog post, we walk you through a complete example of building an agentic system for signal discovery using the NeMo Agent Toolkit.
Agentic systems for signal discovery
Agentic AI is bridging the gap between human expertise and automated efficiency. We designed a system of signal-discovery agents using NeMo Agent Toolkit to change signal discovery from a manual grind into a self-evolving, autonomous loop. The result is a painless process for designing, testing, and optimizing the agentic system.
The system coordinates three specialized agents:
Signal agent: Identifies potential alpha signals from market data.
Code agent: Translates signal descriptions into executable Python code.
Evaluation agent: Runs backtests, applies logical evaluation, and iteratively refines signal suggestions.
NeMo Agent Toolkit multi-agent signal discovery loop
The NeMo Agent Toolkit provides the orchestration layer to build intelligent agents that plan complex research tasks, use tools to execute Python code, and reflect on backtesting results to refine their own hypotheses. Our proposed system consists of three specialized agents that interact in a continuous cycle of creation, execution, and refinement. The NeMo Agent Toolkit manages the “handoffs” between these agents, ensuring that context (such as signal definitions or backtest results) is preserved across the workflow.
Figure 1. Architecture of the quantitative signal discovery agent developer example
The signal generator
This agent acts as the creative brain, using
nemotron-3-nano-30b-a3b
through NVIDIA NIM to hypothesize new signal expressions. We designed the following system prompt: “You are a senior quantitative researcher at a top hedge fund. Generate
{config.num_signals}
unique stock selection signals based on the request” to define the core objective of the agent.
To ensure it produced logically sound results rather than “hallucinating” math, we provided it with a structured library of mathematical calculators as building blocks. Each calculator is a dictionary containing a name, signature, and meaning. In our example, there are 66 different operators covering operations from arithmetic, math (abs, clip, power), rank, and time series (log return, momentum, delta). For example,
Rank_Add,
normalizes two different sets of data (like price and volume) into a shared 0-to-1 percentile scale and sums them together. We provide the interpretation and the Python code, enabling the agent to combine different market signals into a single, balanced score.
{
  "name": "Rank_Add",
  "signature": "Rank_Add(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame",
  "meanings": "Return the sum of the quantiles of the elements in DataFrame x and the corresponding elements in DataFrame y.",
  "code": "def Rank_Add(x, y):\n    rank_x = x.T.rank() / (len(x.T) + 1)\n    rank_y = y.T.rank() / (len(y.T) + 1)\n    return (rank_x + rank_y).T\n"
}
By supplying these reference operators, the agent can reason through its “toolbox” to select the best combination of operators to measure market trends, ensuring the resulting signal is both high-quality and theoretically sound.
The signal generator outputs the “blueprint” as directed by the following prompt:
Return each signal as a JSON object with these fields:
- name: Signal name (descriptive)
- formula: Formula using ONLY the operators listed above
- meaning: Economic intuition (what alpha it captures)
- category: One of [momentum, volatility, volume, reversal, quality, other]
- data_fields_used: List of data fields used (Open, Close, High, Low, Volume)
- operators_used: List of operators used
- lookback_periods: List of lookback days used
By asking the agent to output all the details, we ensure the interpretability and reproducibility of the signals generated by the agent; also, tracking this information will also facilitate the evaluation step further down the loop.
The code agent
Once a hypothesis is formed, the code agent transforms natural language ideas into executable Python code. In the NeMo Agent Toolkit ecosystem, this agent is specifically tuned for tool-calling and code generation. It takes the blueprint from the signal agent and produces Python code that calculates the signal against historical price-volume data—with the operator implementations from
calculator.json
inlined automatically so the resulting module is self-contained and portable.
The evaluation agent
This agent processes the raw data from the code agent to calculate the Information Coefficient (IC) and Rank IC metrics that quantify how well the signal predicts price movement. In quantitative research, Rank IC is the correlation between the ranks of your signal values and the ranks of subsequent asset returns.
Unlike the standard Pearson IC, Rank IC is more robust against outliers and focuses on the relative ordering of assets—an essential feature for building ranking-based trading strategies.
Usually, a “good” institutional-grade signal maintains a mean Rank IC between 0.02 and 0.05. Anything consistently above 0.05 is considered a very strong signal, often found in high-frequency or niche momentum strategies.
The user can define an acceptance threshold for the evaluation agent to decide when to accept a generated signal. If a signal has suboptimal performance in backtesting, the evaluation agent generates optimization suggestions that are fed back into the Signal Agent’s next iteration. This creates a self-improving loop where each subsequent generation of signals is more refined than the last.
Why NeMo Agent Toolkit for automating signal discovery?
Using the toolkit for this specific use case provides multiple benefits:
Config-driven workflows
The toolkit helps shift the project from a rigid script to a flexible research platform. Instead of hard-coding the interactions between agents, you define the system’s logic—including personas, tools, and constraints—entirely within a YAML configuration. This modularity makes it trivial to swap models for different tasks. For example, you can assign a high-reasoning model to handle hypothesis generation while using a faster, more cost-effective model for the code agent without modifying the underlying source code.
In our implementation, the
config.yml
acts as the single source of truth for the entire signal discovery experiment. It centralizes every critical parameter, from the IC thresholds to the depth of the optimization loop. This enables quantitative researchers to iterate at high velocity—adjusting the forward-returns period or tightening the IC requirements—simply by editing a YAML file.
llms:
  signal_generator:
    _type: nim
    model_name: nvidia/nemotron-3-nano-30b-a3b
    base_url: "https://integrate.api.nvidia.com/v1/"
    temperature: 0.8
    max_tokens: 3000

  code_generator:
    _type: nim
    model_name: nvidia/nemotron-3-nano-30b-a3b
    base_url: "https://integrate.api.nvidia.com/v1/"
    temperature: 0.0
    max_tokens: 2000

  optimization_advisor:
    _type: nim
    model_name: nvidia/nemotron-3-nano-30b-a3b
    base_url: "https://integrate.api.nvidia.com/v1/"
    temperature: 0.5
    max_tokens: 1000

workflow:
  _type: signal_optimizer
  signal_generator_llm: signal_generator
  code_generator_llm: code_generator
  optimization_advisor_llm: optimization_advisor
  ic_threshold: 0.02
  p_value_threshold: 0.05
  max_iterations: 3
  num_signals: 2
  forward_periods: 5
Built-in observability
Arize Phoenix tracing adds observability to NIM-powered signal discovery agents in long-running quantitative workflows. Since signal discovery involves high-latency loops—generating complex price-volume formulas, running vectorized backtests, and performing fitness evaluations—Phoenix enables us to visualize the reasoning traces of the LLM in real time.
Figure 2. NeMo Agent Toolkit Tracing provides a visual trace of the LLM agent’s reasoning across the signal discovery workflow
By tracking reasoning traces and token usage across the
ChatNVIDIA()
calls, we can pinpoint whether a bottleneck lies in the model’s logic generation and gain deeper insights into the agent’s thinking process at each step. This transparency is essential for debugging “silent failures” where an agent might produce a mathematically valid but economically meaningless signal, enabling optimization for both the prompt strategy and the computational costs of the discovery cycle.
End-to-end example: Mining momentum-based signals
Momentum-based signals are one of the most commonly used in trading. They are based on the empirical observation that assets that have performed well recently tend to continue their upward trajectory, while those performing poorly often continue to decline. Let’s run the workflow against this prompt:
nat run --config_file configs/config-optimization.yml --input "momentum signals"
The
nat run
command spins up the workflow based on the YAML config to perform the generation and optimization loop:
026-04-24 14:34:02 - INFO     - signal_discovery_workflow.signal_discovery_optimization_workflow:353 - === Iteration 1/3 ===
2026-04-24 14:34:02 - INFO     - signal_discovery_workflow.signal_discovery_optimization_workflow:355 - Generating signals...
2026-04-24 14:34:10 - INFO     - signal_discovery_workflow.signal_discovery_optimization_workflow:360 - Generating code...
2026-04-24 14:34:13 - INFO     - signal_discovery_workflow.signal_discovery_optimization_workflow:366 - Evaluating IC...
2026-04-24 14:34:13 - INFO     - signal_discovery_workflow.signal_evaluator:391 - Found 2 signal function(s): ['signal_volume_adjusted_momentum', 'signal_20_day_price_rank_momentum']
2026-04-24 14:34:15 - INFO     - signal_discovery_workflow.signal_evaluator:457 -   signal_volume_adjusted_momentum: |IC| = 0.0103
2026-04-24 14:34:18 - INFO     - signal_discovery_workflow.signal_evaluator:457 -   signal_20_day_price_rank_momentum: |IC| = 0.0138
2026-04-24 14:34:18 - INFO     - signal_discovery_workflow.signal_evaluator:472 - Selected best signal: signal_20_day_price_rank_momentum with |IC| = 0.0138
2026-04-24 14:34:19 - INFO     - signal_discovery_workflow.signal_discovery_optimization_workflow:371 - Mean IC: -0.0138, p-value: 7.202971903375044e-07
2026-04-24 14:34:19 - INFO     - signal_discovery_workflow.signal_discovery_optimization_workflow:413 - Generating optimization feedback...
signal_discovery_workflow.signal_discovery_optimization_workflow:353 - === Iteration 2/3 ===
...
signal_discovery_workflow.signal_discovery_optimization_workflow:353 - === Iteration 3/3 ===
...
After three optimization iterations, we get the following generated signals:
Signal 1: ExpVolume-Adjusted Momentum
    Formula:    Div(TS_Return(Close, 10), Decay_Exp(Volume, 10))
    Meaning:    10‑day price return scaled by exponentially weighted volume, isolating momentum that is amplified when trading activity is sustained
    Category:   momentum
    Data fields: Close, Volume
    Operators:   Div, TS_Return, Decay_Exp
    Lookback:    [10]

  Signal 2: Rank-Adjusted Return Momentum << SELECTED
    Formula:    Rank_Mul(Rank(Close), Rank(TS_Return(Close, 10)))
    Meaning:    Combines the relative standing of price with the relative strength of recent returns, highlighting stocks that are both highly ranked in price and showing strong upward momentum
    Category:   momentum
    Data fields: Close

Evaluation Metrics (on: signal_rank_adjusted_return_momentum):
----------------------------------------
  Mean IC: -0.0134
  IC Std: 0.1483
  IC IR: -0.0906
  T-stat: -5.3655
  P-value: 0.000000
  Num Periods: 3504
  Positive IC Ratio: 46.38%
In this demonstration, the signal agent generated two momentum-based stock-selection signals using the structured library of mathematical operators we provided.
The first, ExpVolume-Adjusted Momentum, computes each stock’s 10-day price return and divides it by an exponentially weighted moving average of trading volume over the same span:

`\text{Signal}_1(t) = \frac{ \frac{\text{Close}(t) – \text{Close}(t-10)}{\text{Close}(t-10)} }{ \mathrm{EWMA}_{\alpha}\bigl[\text{Volume}\bigr](t) }`

The denominator is the recursive exponentially-weighted average with span 10:

`\mathrm{EWMA}_{\alpha}\bigl[\text{Volume}\bigr](t) = \alpha \cdot \text{Volume}(t) + (1-\alpha)\cdot \mathrm{EWMA}_{\alpha}\bigl[\text{Volume}\bigr](t-1)`

The intuition is that a 10-day price return carries more weight when it occurs on low liquidity or thin trading activity. Given two stocks with identical price returns, the one with weaker, fading EWMA volume will receive a larger signal magnitude.
The second, Rank-Adjusted Return Momentum, composes two cross-sectional ranks: each stock’s price rank and the rank of its 10-day return, multiplied together so the signal is large only when both are high simultaneously:

`\text{Signal}_2(t) \propto \mathrm{Rank}_t\bigl(\text{Close}\bigr) \cdot \mathrm{Rank}_t\bigl(\text{TS\_Return}(\text{Close}, 10)\bigr)`

The cross-sectional rank on day \(t\) is the within-day quantile across the \(N\) S&P 500 names:

`\mathrm{Rank}_t(x) = \frac{\mathrm{rank}\bigl(x_t\bigr)}{N+1} \in (0, 1)`

This isolates stocks that are simultaneously highly priced and showing strong recent momentum—the product sharpens the signal versus either rank in isolation, since middle-of-the-pack names on either dimension are damped multiplicatively.
The evaluator backtested both signals against S&P 500 forward returns and selected Rank-Adjusted Return Momentum as the stronger candidate, achieving a mean IC of -0.0134 (IC standard deviation 0.1483, information ratio -0.091) with a \(t\)-statistic of -5.37, a vanishingly small \(p\)-value (\(p < 10^{-7}\)) over 3,504 trading days.
The positive-IC ratio of 46.4% confirms the signal leans negative more often than not. While $|IC|$ sits just below the 0.02 acceptance threshold (hence the “best-effort” outcome after two iterations), the highly significant negative sign means the signal carries consistent predictive information—high-priced, high-momentum stocks systematically underperform forward, the textbook short-momentum / reversal pattern.
Quantitative signal discovery agent developer example
We finish walking through an example of how to build a highly scalable, flexible, and powerful engine for uncovering new sources of alpha. The quantitative signal discovery agent developer example is easily extensible:
Try different signal categories by changing the –input string, such as “volatility signals”, “mean reversion signals”, or “volume-price divergence signals”.
Mix model sizes per agent. Assign a higher-capability reasoning model like nemotron-3-super-120b-a12b to the signal agent for richer ideation while keeping the smaller nemotron-3-nano-30b-a3b for the code agent and advisor, only a one-line change in YAML.
Add your own operators by editing template/calculator.json. Drop in your firm’s proprietary technical indicators or alternative-data transforms; the signal agent will discover them automatically on the next run.
Plug in your own data. Replace the included S&P 500 CSVs with your own universe (Asian equities, crypto, ETFs) or add new data fields like fundamentals or sentiment.
Tune the optimization criteria—such as ic_threshold, max_iterations, and forward_periods—to match your investment style.
Get started
Visit
build.nvidia.com
to deploy the notebook in a GPU-accelerated environment with either
NVIDIA Brev
or your own cloud infrastructure using the
quantitative signal discovery agent notebook
on GitHub.
