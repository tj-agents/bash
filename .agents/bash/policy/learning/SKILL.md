---
name: learning
description: Teach Bash while preserving the requested task. Use for lessons, explanations or learner-record updates.
kind: policy
domain: bash
profile: knowledge
applicability: Bash scripts and sourced Bash libraries
requires: bash
provenance: house
---

# Bash learning

## Two modes

Follow the requested task. In lessons, explain and review while the learner
practises. In delivery work, implement the requested change and explain relevant
mechanisms. Bash adoption does not convert all work into lessons.

```bash
printf '%s\n' "$@"  # Preserve each input argument.
```

## Calibrate to `bash:knowledge`

Locate a project-owned record through [knowledge](../../knowledge/knowledge/SKILL.md).
Ask a focused question when prior understanding matters and is not recorded.

## Working rules

Explain unfamiliar expansion, status and process boundaries in chat with a small
example. Production code keeps normal comments. Follow the project's instructions
for who writes code.

## Progress

Update the learner's own record only after demonstrated understanding and their
agreement. Never store personal progress in this shared package.

## Agreeing a convention

Use the documented baseline in adopting projects. Explain new choices with primary
sources and distinguish language constraints from preferences. Keep project-specific
decisions there; shared changes need a reusable reason, example and validation.
