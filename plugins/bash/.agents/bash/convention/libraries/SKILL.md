---
name: libraries
description: Bash command and library dependencies. Use when adding executables, sourcing code or selecting data parsers.
kind: convention
domain: bash
profile: core
applicability: Bash scripts and sourced Bash libraries
requires: bash
provenance: house
---

# Bash libraries and dependencies

Owns selection and declaration of external commands and sourced dependencies.

```bash
if ! command -v jq >/dev/null 2>&1; then
  printf '%s\n' 'This command requires jq.' >&2
  exit 1
fi
jq -er '.name | strings' -- "$config_file"
```

Use builtins when they express the operation clearly; use a structured parser for
structured data, such as jq for JSON. Declare command versions and platform variants:
Bash availability establishes neither GNU utilities nor a particular PATH.

Reuse maintained selected dependencies before growing a shell framework.
A sourced library executes in the caller: use trusted code at an explicit location
and version. Sourcing a data file or downloaded text is not ordinary parsing.
Use the project's dependency/provenance mechanism; no particular package manager,
publisher or administrator-authentication tool is imposed by Bash.

Keep caller-environment contracts in [structure](../structure/SKILL.md).
Command doubles can exercise failures but do not replace actual dependency checks.

Sources: [GNU command search](https://www.gnu.org/software/bash/manual/html_node/Command-Search-and-Execution.html),
[jq manual](https://jqlang.org/manual/).
