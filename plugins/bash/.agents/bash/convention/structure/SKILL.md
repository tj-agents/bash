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

```bash
# lib/output.bash
# shellcheck shell=bash
write_result() {
  printf '%s\n' "$1"
}
```

## File structure

Keep a small script in one file. A standalone project needing shared functions
can use `bin/<command>`, `lib/*.bash` and `tests/`. Existing repositories keep
their layout; extraction needs shared behaviour, not a line-count threshold.

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
[GNU pipelines](https://www.gnu.org/software/bash/manual/html_node/Pipelines.html).
