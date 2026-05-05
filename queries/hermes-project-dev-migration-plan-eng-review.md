---
title: Hermes Project Development Migration Plan Eng Review
created: 2026-04-24
updated: 2026-04-24
type: query
tags: [hermes, gstack, eng-review, migration, project-development]
sources: [filesystem:~/.hermes, filesystem:~/wiki, review:hermes-project-dev-office-hours-review]
status: draft
---

# Hermes Project Development Migration Plan Eng Review

## Summary
这是一份把前一轮 office-hours 审查压成可执行迁移计划的 eng review。结论先说：现在最小、最稳、最确定的方案，不是继续在 `~/.hermes/scripts/` 上做局部清理，而是把已经具备独立业务边界的内容升级成独立项目目录，并让 Hermes 只保留 runtime、config、cron、skills、memory 这些宿主职责。

推荐执行顺序也很明确：
1. 先收敛 `investment-watch`
2. 再收敛 `project-kickoff`
3. 最后才回头整理 `~/.hermes/scripts/README.md` 和剩余 quick command 资产

这能在最小 diff 下，把确定性、测试入口、项目级 AGENTS、文件即操作系统这四件事一起拉回来。

## Step 0: Scope Challenge

### 0.1 What already exists
已经存在、可以直接复用的东西：
- `~/.hermes/investment-watch/`
  - 已经是半个项目根目录，里面有 `fund_rules.json`、`fund_state.json`、`trade_log.json`、`README.md`、`backups/`
- `~/.hermes/scripts/market_watch.py`
- `~/.hermes/scripts/review_trades.py`
- `~/.hermes/scripts/log_trade_action.py`
- `~/.hermes/scripts/update_fund_state.py`
- `~/.hermes/scripts/project_kickoff.py`
- 4 个基金 cron job 已存在，说明调度需求不是待验证假设，而是已经在线运行
- `~/.hermes/hermes-agent/` 本身已经给出了一个标准项目模板：`AGENTS.md` + `pyproject.toml` + `tests/`

结论：
- 不需要新造一套项目体系
- 也不需要改 Hermes 本体
- 只需要把已有零散资产重组到正确目录边界里

### 0.2 Minimum set of changes
最小可行变更应该只做这些：
- 给 `investment-watch` 建立真正的项目根
- 给 `project-kickoff` 建立真正的项目根
- 把硬编码旧路径的 cron / README / 脚本互调引用改到新路径
- 补最小 `AGENTS.md`、`pyproject.toml`、`tests/`

不应该在这一轮一起做的事：
- 不做 monorepo 大重构
- 不做统一包管理器迁移
- 不做 Hermes 插件化改造
- 不做 CI/CD
- 不做自动注册项目发现机制

### 0.3 Complexity check
如果这次迁移：
- 同时动超过 8 类资产
- 同时新建超过 2 个抽象层
- 同时处理所有散落脚本

那就过头了。

推荐把这次工作压成 2 个项目、3 个阶段：
- 阶段 1: `investment-watch`
- 阶段 2: `project-kickoff`
- 阶段 3: 清理 `scripts/` 目录定位与文档

### 0.4 Search check
本次不是引入新框架，也不是引入新基础设施。
不需要发明模式。
现成 best practice 就是：
- 独立项目目录
- 项目级 `AGENTS.md`
- 项目级 `pyproject.toml`
- 项目级 `tests/`
- runtime 与业务项目分离

这是典型 **[Layer 1]** 问题，不需要创新 token。

### 0.5 TODOS cross-reference
未发现 `TODOS.md`。
说明 deferred work 现在没有固定容器，进一步证明项目治理入口缺失。

### 0.6 Completeness check
如果只是把脚本移动目录，不补测试、不补项目 root、不补 AGENTS，那只是“路径整理”，不是恢复确定性。

完整版本应该至少包含：
- 项目 root
- 项目 README
- 项目 AGENTS
- 项目 pyproject
- 最小测试
- 单一入口
- 外部引用回写

这不是过度工程，这是最低可维护线。

### 0.7 Distribution check
本轮不引入新 artifact 类型。
当前项目都是本地脚本/cron 驱动。
分发不在本轮范围内。

## Scope Decision
推荐 scope：
- 只做两个独立项目的工程收敛
- 不动 Hermes 本体源码
- 不做发布体系
- 不做 CI

这是最小但完整的切口。

## Architecture Review

### Issue 1
`investment-watch` 现在是“数据目录”和“执行目录”分离：
- 数据在 `~/.hermes/investment-watch/`
- 执行脚本在 `~/.hermes/scripts/`

这会让项目 root 缺席，任何迁移都要跨目录联动修改。

Recommendation:
- 直接把 `investment-watch` 升级成真正项目根，代码和数据同域

#### Recommendation details
- 新 root：`~/.hermes/projects/investment-watch/`
- 其中包含：
  - `AGENTS.md`
  - `README.md`
  - `pyproject.toml`
  - `tests/`
  - `src/investment_watch/` 或 `scripts/`
  - `data/`（放 `fund_rules.json` / `fund_state.json` / `trade_log.json`）
  - `backups/`

我的建议：优先 `src/investment_watch/`，不要继续用根目录散脚本。

原因：
- 更接近标准 Python 项目
- 测试与导入更自然
- 后续要扩成 CLI 也顺手

### Issue 2
`project_kickoff.py` 现在放在 `~/.hermes/scripts/`，但它不是 quick command 库的一部分，而是一个独立项目生成器。

Recommendation:
- 把它从 `scripts/` 提升为独立小项目

#### Recommendation details
可选落点里，最稳的是：
- `~/.hermes/projects/project-kickoff/`

不建议直接继续塞回 `~/wiki`，因为：
- 它服务 wiki，但它本身是代码项目
- 把代码和知识库内容混放，会把“文档内容”与“生成器实现”再一次缠住

### Architecture Verdict
推荐架构：

```text
~/.hermes/
├── config.yaml
├── AGENTS.md                      # 全局运行规则
├── scripts/                       # 只保留 quick command / runtime helper
├── projects/
│   ├── investment-watch/
│   │   ├── AGENTS.md
│   │   ├── README.md
│   │   ├── pyproject.toml
│   │   ├── src/investment_watch/
│   │   ├── tests/
│   │   ├── data/
│   │   └── backups/
│   └── project-kickoff/
│       ├── AGENTS.md
│       ├── README.md
│       ├── pyproject.toml
│       ├── src/project_kickoff/
│       └── tests/
└── investment-watch/              # 迁移后删除或转为兼容壳，最终移除
```

这个结构的关键点：
- Hermes runtime 和业务项目分层
- 每个项目有自己的治理边界
- 文件树本身表达系统结构

## Code Quality Review

### Issue 1
当前 `market_watch.py`、`review_trades.py`、`log_trade_action.py`、`update_fund_state.py` 通过绝对路径互相引用。

已验证：
- `market_watch.py` 直接调用 `/home/lin/.hermes/scripts/review_trades.py`
- 多个脚本直接写死 `Path('/home/lin/.hermes/investment-watch/...')`

这属于典型“路径即实现”的坏味道。

Recommendation:
- 把路径解析改成“相对项目根”

建议实现：
```text
project_root = Path(__file__).resolve().parents[2]
data_dir = project_root / "data"
```
或统一放到一个 `paths.py`。

### Issue 2
`~/.hermes/scripts/README.md` 仍宣称该目录是 quick command 脚本库，但现实已经混入项目脚本。

这会让文档误导后续决策。

Recommendation:
- 在迁移完成后，重写 `scripts/README.md`
- 明确：这里只放 runtime helper / quick commands，不放独立项目代码

### Issue 3
当前没有项目级 `AGENTS.md`，导致所有开发约束只能挂在全局 `~/.hermes/AGENTS.md`。

这会让项目约束不够具体。

Recommendation:
- 两个项目都补最小项目级 `AGENTS.md`

最小内容应该包括：
- 项目目标与边界
- 数据文件位置
- 测试命令
- 不允许继续把新业务脚本丢回 `~/.hermes/scripts/`

## Test Review

### 目标
100% 不是指集成全覆盖，而是这轮迁移涉及的每条新代码路径都要有对应测试或 smoke check。

### Test Framework Recommendation
用户长期偏好已经明确：
- `uv + Python 3.12 + Ruff + Ty + pytest`

所以两个项目都按这个最小模板建。

### Coverage Diagram

```text
MIGRATION PLAN PATHS

[+] investment-watch migration
  ├── create project root
  │   ├── [GAP] root exists and expected dirs created
  │   └── [GAP] README / AGENTS / pyproject present
  ├── move code files
  │   ├── [GAP] old scripts relocated to src/ or scripts/
  │   └── [GAP] module imports still resolve
  ├── move data files
  │   ├── [GAP] rules/state/trade_log readable from new data/
  │   └── [GAP] backups path preserved
  ├── rewrite internal paths
  │   ├── [GAP] market_watch finds review_trades via project-local path
  │   ├── [GAP] log_trade_action finds state/log via project-local path
  │   └── [GAP] update_fund_state finds state via project-local path
  ├── update external callers
  │   ├── [GAP] cron jobs point to new command
  │   ├── [GAP] README examples point to new command
  │   └── [GAP] no remaining hardcoded old path references
  └── smoke execution
      ├── [GAP] morning mode runs
      ├── [GAP] decision mode runs
      └── [GAP] review_trades runs

[+] project-kickoff migration
  ├── create project root
  │   ├── [GAP] root exists and expected dirs created
  │   └── [GAP] README / AGENTS / pyproject present
  ├── move code file
  │   ├── [GAP] CLI still accepts --idea / --slug / --title
  │   └── [GAP] wiki output path still correct
  ├── add tests
  │   ├── [GAP] slug validation test
  │   ├── [GAP] existing-file refusal test
  │   └── [GAP] content generation smoke test
  └── update references
      └── [GAP] no remaining old path references

COVERAGE: 0/20 paths explicitly tested today
QUALITY: no project-level migration tests yet
```

### Required Tests to Add

#### investment-watch
建议最少补这 6 类测试：
1. `tests/test_paths.py`
   - 断言项目能从自身 root 正确解析 `data/`
2. `tests/test_market_watch_paths.py`
   - 断言 `market_watch` 调用本项目内 `review_trades`
3. `tests/test_update_fund_state.py`
   - 临时 state 文件写入后，字段更新正确
4. `tests/test_log_trade_action.py`
   - 记录 trade 后，state 同步回写正确
5. `tests/test_review_trades.py`
   - 对样例 `trade_log.json` 输出摘要正确
6. smoke tests
   - `market_watch.py --mode morning`
   - `market_watch.py --mode decision`

#### project-kickoff
建议最少补这 4 类测试：
1. `tests/test_slug_validation.py`
2. `tests/test_title_and_idea_normalization.py`
3. `tests/test_existing_file_refusal.py`
4. `tests/test_generate_output_smoke.py`

### Failure Modes

| Codepath | Realistic failure | Test covers? | Error handling? | User-visible? | Critical gap |
|---|---|---:|---:|---:|---:|
| investment-watch path migration | cron 仍指向旧路径导致定时任务失效 | 否 | 否 | 可能静默失败 | 是 |
| internal script calls | `market_watch` 找不到 `review_trades` | 否 | 部分 | 用户只看到执行失败 | 是 |
| data path rewrite | state/log/rules 文件路径错 | 否 | 部分 | 直接报错 | 否 |
| project-kickoff migration | 新路径下 CLI 参数 contract 被破坏 | 否 | 部分 | 用户命令失败 | 否 |
| scripts cleanup | README 继续误导新项目落点 | 否 | 否 | 静默造成后续错用 | 否 |

最关键的两个 critical gap：
- cron 指向旧路径
- 项目内互调仍残留旧路径

## Performance Review

这一轮不是性能优化项目。
但有两个轻量点值得记：

1. 不要在迁移时把 `investment-watch` 再拆成太多服务层
   - 现在主要问题是边界，不是吞吐
2. 对 `market_watch` 保持单进程脚本模型
   - 先稳住路径、测试、项目 root
   - 不要趁机做“模块化大升级”把 diff 膨胀

Performance verdict:
- 无新的性能阻塞问题
- 当前更大的风险是结构漂移，不是运行效率

## Recommended Implementation Plan

### Phase 1: investment-watch

#### Deliverables
- `~/.hermes/projects/investment-watch/`
- 项目级 `AGENTS.md`
- `README.md`
- `pyproject.toml`
- `src/investment_watch/` 或 `scripts/`
- `tests/`
- `data/`
- 兼容期路径迁移方案

#### Exact change set
1. 建目录骨架
2. 移动 4 个 Python 脚本进项目目录
3. 移动 3 个数据文件进 `data/`
4. 改写脚本内部路径解析
5. 改写 README 示例命令
6. 改写 4 个 cron job 指向新入口
7. 补最小 pytest
8. 运行 smoke + pytest
9. 最后删除旧路径或保留短期 shim

#### Recommended entrypoint
建议提供：
- `python -m investment_watch.market_watch --mode morning`
或
- `uv run python -m investment_watch.market_watch --mode morning`

不要继续把 cron 绑死到裸脚本路径。

### Phase 2: project-kickoff

#### Deliverables
- `~/.hermes/projects/project-kickoff/`
- 项目级 `AGENTS.md`
- `README.md`
- `pyproject.toml`
- `src/project_kickoff/`
- `tests/`

#### Exact change set
1. 建目录骨架
2. 移动 `project_kickoff.py`
3. 改成模块化入口
4. 补 4 个最小测试
5. 跑样例生成验证
6. 搜全局引用，确认旧路径清空

### Phase 3: scripts/ cleanup

#### Deliverables
- 重写 `~/.hermes/scripts/README.md`
- 明确目录职责
- 清理不再属于 quick command 库的残留引用

#### Rule after migration
`~/.hermes/scripts/` 只允许：
- quick command helpers
- runtime helpers
- 纯宿主层脚本

不允许再放：
- 独立业务项目主代码
- 带独立状态文件的项目脚本
- 需要项目级测试与 AGENTS 的代码

## NOT in Scope
- 不改 Hermes 本体源码
- 不引入 CI/CD
- 不把两个项目合成一个 monorepo 包
- 不统一改造所有现存 shell quick command
- 不在本轮解决所有历史散落文件
- 不做自动项目发现/注册机制
- 不做跨项目共享工具库抽象

## Parallelization Strategy

### Dependency Table

| Step | Modules touched | Depends on |
|------|----------------|------------|
| investment-watch directory scaffold | projects/investment-watch/ | — |
| investment-watch path rewrite | projects/investment-watch/src, data, cron | scaffold |
| investment-watch tests | projects/investment-watch/tests | path rewrite |
| project-kickoff scaffold | projects/project-kickoff/ | — |
| project-kickoff migration | projects/project-kickoff/src | scaffold |
| project-kickoff tests | projects/project-kickoff/tests | migration |
| scripts README cleanup | ~/.hermes/scripts/README.md | both migrations |

### Parallel lanes
- Lane A: `investment-watch` scaffold → path rewrite → tests
- Lane B: `project-kickoff` scaffold → migration → tests
- Lane C: `scripts/README.md` cleanup

### Execution order
- 先并行启动 Lane A + Lane B
- 两边都完成并验证后，再做 Lane C

### Conflict flags
- Lane A 和 Lane B 基本独立
- Lane C 必须最后做，因为它依赖前两个项目迁移后的真实落点

## What already exists
- `investment-watch` 已有数据目录和 README
- 基金 cron 已存在，可直接作为迁移后回归验证对象
- `project_kickoff.py` 已有可运行 CLI contract
- `hermes-agent` 已提供标准项目形态参考

结论：
- 这是重组，不是从零开始
- 最大价值来自边界收敛，不来自新功能

## Recommended File Layouts

### investment-watch
```text
~/.hermes/projects/investment-watch/
├── AGENTS.md
├── README.md
├── pyproject.toml
├── src/investment_watch/
│   ├── __init__.py
│   ├── paths.py
│   ├── market_watch.py
│   ├── review_trades.py
│   ├── log_trade_action.py
│   └── update_fund_state.py
├── tests/
│   ├── test_paths.py
│   ├── test_market_watch_paths.py
│   ├── test_update_fund_state.py
│   ├── test_log_trade_action.py
│   └── test_review_trades.py
├── data/
│   ├── fund_rules.json
│   ├── fund_state.json
│   └── trade_log.json
└── backups/
```

### project-kickoff
```text
~/.hermes/projects/project-kickoff/
├── AGENTS.md
├── README.md
├── pyproject.toml
├── src/project_kickoff/
│   ├── __init__.py
│   └── cli.py
└── tests/
    ├── test_slug_validation.py
    ├── test_title_and_idea_normalization.py
    ├── test_existing_file_refusal.py
    └── test_generate_output_smoke.py
```

## Completion Summary
- Step 0: Scope Challenge — scope reduced to 2 projects + 1 cleanup phase
- Architecture Review: 2 core issues found
- Code Quality Review: 3 core issues found
- Test Review: diagram produced, 20 migration/test gaps identified
- Performance Review: 0 blocking issues found
- NOT in scope: written
- What already exists: written
- TODOS.md updates: 0, because no `TODOS.md` exists yet
- Failure modes: 2 critical gaps flagged
- Outside voice: skipped
- Parallelization: 3 lanes, 2 parallel / 1 sequential
- Lake Score: 3/3 recommendations chose complete option

## Final Verdict
DONE_WITH_CONCERNS

### Why
计划已经够清楚，可以直接进入实施。
但有两个前置 concern 不能省：
1. 迁移时必须先处理 cron 和内部硬编码路径
2. 必须在迁移同一轮补最小测试，不然还是会回到“整理了目录，但没恢复确定性”

## Next Step
最合理的下一步不是继续讨论，而是直接开做 Phase 1：
- 先把 `investment-watch` 迁成独立项目
- 迁移时做备份
- 同步改 cron / README / 内部路径
- 补最小 pytest
- 跑 smoke 验证

## Related
- [[hermes-project-dev-office-hours-review]]
- [[gstack-project-execution-lane-validation-case]]
- [[hermes-agent-workflow-layering-and-adoption-order]]
