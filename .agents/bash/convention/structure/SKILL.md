---
name: structure
description: Bash executable, library and caller-environment boundaries. Use when placing code or changing sourced libraries and startup fragments.
kind: convention
domain: bash
profile: core
applicability: Bash scripts and sourced Bash libraries
requires: bash
provenance: house
---

# Bash structure

Owns executable, library and caller-environment boundaries.

```text
report/
├── bin/report
├── lib/report/output.bash
└── tests/
```

```bash
# lib/report/output.bash
# shellcheck shell=bash
report_write_result() {
  printf '%s\n' "$1"
}
```

```bash
#!/usr/bin/env bash
# bin/report
script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P) || exit 1
# shellcheck source-path=SCRIPTDIR
source "$script_dir/../lib/report/output.bash" || exit 1
report_write_result "Report ready"
```

## File structure

For new standalone Bash projects, put commands in `bin/<command>`, reusable
sourced functions in `lib/<project-or-library>/<responsibility>.bash`, and tests
in `tests/`. In a mixed-language repository, use this layout under the component
that owns the Bash code. Preserve established repository layouts.

Keep a small script in one file until behaviour needs reuse; create directories
only when they hold real code or tests. Share one implementation through a sourced
library when callers need shell functions, or a reusable executable when a command
interface fits. Group libraries by responsibility rather than collecting unrelated
code in `modules` or `helpers`; line count alone does not justify extraction.

Sourcing defines functions in the caller's shell; directories do not create a
Python-style namespace. Prefix public function names with their project or library
owner, as in `report_write_result`, to avoid collisions between sourced libraries.

An executable owns its process-wide options, traps and working directory.
A sourced library or startup fragment preserves its caller's options, traps,
positional parameters, working directory and shell lifetime unless changing one
is its documented purpose. Use `return` in libraries; `exit` ends the caller.

Source trusted code from an explicit location. User configuration is data unless
its interface deliberately accepts executable Bash. Resolve resources relative
to the script where appropriate rather than assuming a working directory.
Use `BASH_SOURCE[0]` for the current file, decide how symlinks are handled, and
check a directory change before any dependent operation.

Use a subshell for a temporary directory change when isolation is intended.
Pipeline stages normally run in subshells; their variable updates do not reliably
reach the parent. Redirect a loop's input for state needed afterward.
Failures in a process-substitution producer still need explicit observation.

Sources: [GNU execution environment](https://www.gnu.org/software/bash/manual/html_node/Command-Execution-Environment.html),
[GNU shell functions](https://www.gnu.org/software/bash/manual/html_node/Shell-Functions.html),
[GNU pipelines](https://www.gnu.org/software/bash/manual/html_node/Pipelines.html).
