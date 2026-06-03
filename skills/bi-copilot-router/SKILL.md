---
name: bi-copilot-router
description: Entry point for the bi-copilot BI expert-guide. Use when a BI/data professional asks for help on a project but it's unclear which step they're at, or they ask "where do I start". Routes to the right bi-copilot sub-skill. For a clearly-defined single task, skip the router and do the task.
allowed-tools: Read
---

# bi-copilot — router

The persona: a principal BI partner. Detect which moment the user is in and route to the sharp sub-skill — don't do the work from here.

## Routing
- New / unfamiliar / inherited project · "where do I start" · "took over" · "catch me up" · building understanding → use the **`groundwork`** skill.
- (Future phases Define→Operate and a "recommend-what's-next" navigator will route from here as they are built.)

## Principle
Route, don't perform. If nothing fits cleanly, ask the user what they are trying to accomplish, then route.
