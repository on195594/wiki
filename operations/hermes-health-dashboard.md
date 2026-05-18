---
title: Hermes Health Dashboard
created: 2026-04-22
updated: 2026-04-22
type: concept
tags: [hermes, operations, health, cron, monitoring]
sources: []
status: active
---

# Hermes Health Dashboard

## Summary
这页定义 Hermes 周度治理线的最小运行面板：用一个固定 skill + 一个每周 cron，把 Hermes 当前运行面的关键健康状态压成一页可快速查看的运维基线。

## Current baseline
### Runtime
- Hermes version: `v0.10.0 (2026.4.16)`
- Update status: `1 commit behind`
- Python: `3.11.15`
- Gateway/service: running

### Cron
- Active job: `晨报` — `0 7 * * *`
- Active job: `hermes-weekly-health-check` — `30 8 * * 1`
- New weekly health cron job id: `7cb813eb5431`
- Delivery: `origin`

### Memory
- `MEMORY.md`: `931 chars`
- `USER.md`: `789 chars`
- Current status: healthy after cleanup

### Browser
- Runtime status: basic local browsing works
- Doctor status: false negative / still reported as unavailable at toolset level
- Evidence: local `agent-browser` and Chromium are installed; `browser_navigate`, `browser_snapshot`, and `browser_console` succeeded against public sites; `hermes doctor` still marks `browser` unavailable because the `browser` toolset availability is currently gated by `browser_cdp`, which requires a CDP override
- Operational meaning: public pages and basic interactions are usable now, but browser-heavy automation should still be treated as degraded until site-specific validation is done

### Known risks
- `agent-browser` still has one high-severity npm vulnerability warning
- `hermes doctor` currently misreports browser availability because of toolset-level gating by `browser_cdp`
- Login-required / strong anti-bot / complex dynamic sites are not yet validated and should still be treated as degraded
- WhatsApp bridge has critical dependency warnings, though it is irrelevant to the current Telegram-only setup
- OpenRouter is not configured
- `tinker-atropos` submodule is missing

## Weekly governance pipeline
- Skill: `hermes-weekly-health-check`
- Cron: `hermes-weekly-health-check`
- Schedule: `30 8 * * 1`
- Deliver: `origin`
- Goal: generate one short decision-oriented weekly runtime health report

## Report contract
The weekly report should always answer:
1. Is Hermes behind on updates?
2. Are cron jobs healthy and still meaningful?
3. Is memory capacity still healthy?
4. Is browser usable, degraded, or unavailable?
5. What are the top next actions?

## Interpretation policy
### Healthy
- Update lag is small or none
- Cron jobs are active and not obviously stale
- Memory stays well under pressure thresholds
- Browser status is at least usable or degraded with known scope

### Degraded
- Update lag exists
- Browser warnings exist
- One or more integrations are partially unhealthy
- Action is needed, but the system is still usable for current workflows

### Unhealthy
- Core cron delivery breaks
- Memory is near cap again
- Browser or key tools are unusable for required workflows
- Version drift or dependency issues materially reduce trust in Hermes output

## Next actions
- Run `hermes update`
- If you want doctor output to match reality, patch the browser toolset availability bug so `browser_cdp` does not hide the working local browser tools
- Treat login-required or strong anti-bot sites as opt-in validation targets, not default browser workloads
- For low-risk login forms with unstable refs, use the `browser-login-form-fallback` skill pattern: DOM inspection → controlled form submission → explicit login/session verification
- Periodically review whether existing cron jobs still deserve to stay active

## Related
- [[hermes-memory-governance-notes]]
- [[hermes-layer-routing-decision-checklist]]
- Skill: `browser-login-form-fallback`
- [[index]]
- [[log]]
