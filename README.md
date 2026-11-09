# Bash

Reusable Bash scripting standards for Codex and Claude, published as
`bash@tj-agents` through [the shared marketplace](https://github.com/tj-agents/marketplace).

Select this stack for Bash executables and sourced Bash libraries. It does not
claim POSIX `sh`, Fish or PowerShell compatibility. The adopting repository owns
its supported Bash version, operating systems, privilege mechanism and product
behaviour. Personal settings and learner progress stay in that repository.

## Topic ownership

| Concern | Canonical skill |
|---|---|
| Syntax, quoting, arrays, names, formatting | [style](.agents/bash/convention/style/SKILL.md) |
| Executables, libraries and caller state | [structure](.agents/bash/convention/structure/SKILL.md) |
| CLI contracts and suitability | [domain-design](.agents/bash/convention/domain-design/SKILL.md) |
| Statuses, pipelines, traps, files and children | [errors](.agents/bash/convention/errors/SKILL.md) |
| Observable behaviour and test harnesses | [testing](.agents/bash/convention/testing/SKILL.md) |
| Syntax, ShellCheck and shfmt gates | [build](.agents/bash/convention/build/SKILL.md) |
| Executable and sourced dependencies | [libraries](.agents/bash/convention/libraries/SKILL.md) |
| Minimal new project | [scaffold](.agents/bash/utility/scaffold/SKILL.md) |
| Teaching and project-owned progress | [learning](.agents/bash/policy/learning/SKILL.md), [knowledge](.agents/bash/knowledge/knowledge/SKILL.md) |
| Learning sequence and primary sources | [direction](.agents/bash/knowledge/direction/SKILL.md) |

These are source-backed conventions, with project-overridable formatting choices.
They do not install checks into consumers or prove native host loading by themselves.
Tier detection includes Bash shebangs in extensionless scripts; `.sh` alone is not
classified as Bash.

## Authoring and verification

```sh
pwsh .agents/sync-generated.ps1
pwsh .agents/sync-generated.ps1 -Check
python3 -m unittest discover -s .agents/tests -v
```

Layout, generated host projections and shared CI come from
[Template](https://github.com/tj-agents/template). Author skills once under
`.agents/bash/`; generated payloads are distribution artifacts.
