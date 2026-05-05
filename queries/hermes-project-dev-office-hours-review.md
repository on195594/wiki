---
title: Hermes Project Development Office Hours Review
created: 2026-04-24
updated: 2026-04-24
type: query
tags: [hermes, gstack, office-hours, workflow, project-development]
sources: [filesystem:~/.hermes, filesystem:~/wiki, session:telegram-2026-04-24]
status: draft
---

# Hermes Project Development Office Hours Review

## Summary
这页用 gstack office-hours 的 forcing questions 审查当前把 Hermes 当项目开发环境时暴露出的结构问题。结论很明确：现在的主要问题不是“还差几个脚本或 skill”，而是缺少一个稳定的项目级执行单元。结果是项目代码、运行脚本、状态文件、cron、文档、记忆和 quick commands 混在 `~/.hermes` 里，形成“能继续堆功能，但越来越难维护、难验证、难复盘”的局面。当前最该做的不是继续加功能，而是恢复项目边界与确定性。

## Grounded Observations
### 当前已验证的事实
- `~/.hermes/scripts/` 根目录散落至少两组项目脚本：
  - `project_kickoff.py`
  - `market_watch.py` / `review_trades.py` / `log_trade_action.py` / `update_fund_state.py`
- `~/.hermes/scripts/` 下没有项目级 `tests/` 目录，也没有对应 `pyproject.toml`
- `~/.hermes` 只有全局 `AGENTS.md`，`~/.hermes/scripts/` 和 `~/.hermes/investment-watch/` 没有自己的项目级 `AGENTS.md`
- 基金监控项目的数据文件在 `~/.hermes/investment-watch/`，但执行脚本在 `~/.hermes/scripts/`，项目边界被拆开
- 基金监控相关 cron job 直接调用 `/home/lin/.hermes/scripts/market_watch.py`
- `market_watch.py` 内部继续硬编码调用 `/home/lin/.hermes/scripts/review_trades.py`
- `~/.hermes/scripts/README.md` 仍把该目录定义为 quick command 脚本库，但里面已经混入独立项目脚本，文档与现实不一致
- `~/.hermes/hermes-agent/` 是标准项目形态：有自己的 `AGENTS.md`、`pyproject.toml`、`tests/`

## Office Hours Question 1: Demand Reality
### 真实要解决的问题是什么？
不是“怎么继续在 Hermes 里写脚本更快”，而是：
- 怎么让 Hermes 支撑的小项目开发保持可维护、可验证、可迁移
- 怎么让一个项目的代码、规则、状态、测试、文档、运行入口保持同域
- 怎么避免继续把 `~/.hermes` 变成混合运行时 + 数据目录 + 临时代码目录 + 项目目录的总垃圾场

### 为什么这是刚需？
因为你已经进入“同一个环境里同时存在多个小项目”的阶段：
- wiki kickoff 生成器
- investment-watch 基金监控
- quick command 脚本库

这说明问题不是理论风险，而是已经开始影响维护成本。

## Office Hours Question 2: Status Quo
### 当前你是怎么在解决它的？
当前做法本质上是：
- 把新能力先写进 `~/.hermes/scripts/`
- 把状态文件留在别的目录，比如 `~/.hermes/investment-watch/`
- 用 README、cron、memory、config 去补引用关系
- 依赖聊天上下文和人工记忆维持“这个脚本属于哪个项目”

### 这套 status quo 为什么会失败？
1. 边界靠记忆，不靠目录
2. 运行入口靠硬编码绝对路径，不靠项目 root
3. 验证靠手工运行，不靠测试
4. 约束靠全局 AGENTS，不靠项目 AGENTS
5. 产物散落在不同目录，违反 file-based operating model
6. 项目一多，任何重构都会变成全局搜改

## Office Hours Question 3: Desperate Specificity
### 当前最痛的具体场景是什么？
最具体的问题不是“目录不好看”，而是下面这些会持续发生的事：
- 你想移动一个脚本时，不确定 cron、README、memory、脚本内部互调、config 里谁会一起坏
- 你想给 investment-watch 加测试时，没有项目 root，也没有自然的测试入口
- 你想给某个项目加 AGENTS 约束时，没有一个明确子树可挂载
- 你想把某个项目迁出 `~/.hermes` 独立演化时，会发现代码、数据、调度、文档已经深度耦合
- 你很难区分“这是 Hermes runtime 资产”还是“这是某个业务项目资产”

### 对应你的 6 个观察，实质分别是什么？
1. 文件目录散落
   - 本质是项目边界缺失
2. 没有独立项目目录
   - 本质是没有最小治理单元
3. 没有写测试
   - 本质是没有可重复验证机制
4. 没有项目级 AGENTS.md
   - 本质是约束只能停留在全局层
5. 违背文件即操作系统
   - 本质是文件系统没有表达真实结构，真实结构藏在脑子里和聊天里
6. 偏离确定性
   - 本质是输入、输出、约束、验证都不在一个固定项目容器里

## Office Hours Question 4: Narrowest Wedge
### 最小可行切口是什么？
不要先大修整个 Hermes。最小切口是：

把每一个“已经有独立业务意图、独立数据、独立运行入口”的东西，从 `~/.hermes/scripts/` 升级成独立项目目录。

### 第一优先级只做 2 个项目切分
1. `project-kickoff`
2. `investment-watch`

### 每个项目先只补这 6 件东西
- 独立目录
- 项目级 `AGENTS.md`
- `README.md`
- `pyproject.toml`
- `tests/`
- 单一入口（CLI 或 main script）

### 不该先做的事
- 不要先搞统一大框架
- 不要先做自动项目注册中心
- 不要先做复杂插件系统
- 不要先动 Hermes 本体源码来补这个缺口

## Office Hours Question 5: Unique Observation
### 你现在看到而别人可能没看到的信号是什么？
最关键的观察是：

`~/.hermes/hermes-agent/` 自己就是一个“像样项目”的例子，但你新增的小项目没有沿用同样的工程边界。

也就是说，不是你不知道正确结构，而是当前新增项目默认落点错了：
- Hermes runtime 目录被当成了项目孵化区
- quick command 脚本目录被当成了通用项目代码目录
- 项目治理没有在项目创建时被强制建立

这会造成一个很典型的偏差：
- Hermes 本体是工程化的
- Hermes 上长出来的小项目却是 prompt-driven bricolage

这就是“严重偏离项目确定性”的根因。

## Office Hours Question 6: Future Fit
### 如果继续沿着当前方式做 3 个月，会发生什么？
- `~/.hermes/scripts/` 会继续变成事实上的 misc 项目堆场
- 每新增一个 cron / skill / wiki / memory 绑定，迁移成本进一步升高
- 测试债、路径债、文档债一起累积
- 你会越来越不愿意重构，因为每次改动都像拆雷
- 最终 Hermes 会变成“很能做事，但很难可靠地持续做事”

### 如果按正确方向收敛，会得到什么？
- 每个项目都有自己的代码/数据/文档/测试/规则边界
- Hermes 只负责 orchestration，不再兼任项目垃圾桶
- file tree 可以直接表达系统结构
- AGENTS.md 可以沉到项目层，减少全局规则污染
- 迁移、备份、测试、review、归档都会简单很多

## Verdict
### 结论一句话
你现在的问题不是“开发规范还不够完整”，而是“项目还没被当成项目在管理”。

### 严重度排序
1. 没有独立项目目录
2. 没有项目级测试与验证入口
3. 文件系统不能表达真实项目边界
4. 运行时目录与项目目录混用
5. 缺少项目级 AGENTS.md
6. 文档与实际目录漂移

## Recommended Next Step
### 最小下一步
先不要重构全部内容，只做一个两阶段修复：

#### Phase 1
把 `investment-watch` 收敛成独立项目目录，至少形成：
- `project root`
- `AGENTS.md`
- `README.md`
- `tests/`
- `src or scripts`
- 明确的命令入口

#### Phase 2
把 `project_kickoff.py` 从 `~/.hermes/scripts/` 提升为单独项目或明确归入 `~/wiki` 相关项目目录。

### Done 的标准
- 从文件树本身就能看出每个项目归属
- 从项目根目录就能跑最小测试
- 项目约束不再只依赖全局 `AGENTS.md`
- cron / config / docs 不再跨多个无关目录硬编码引用

## Anti-Goals
- 不是要把所有东西都做成大型仓库
- 不是要把 Hermes 本体改成项目管理器
- 不是要先上 CI/CD
- 不是先追求工具链完整，而是先恢复项目边界和确定性

## Related
- [[gstack-project-execution-lane-validation-case]]
- [[hermes-memory-skills-wiki-boundaries]]
- [[hermes-agent-workflow-layering-and-adoption-order]]
