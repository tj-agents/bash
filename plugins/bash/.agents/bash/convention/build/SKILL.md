---
name: build
description: Bash syntax, ShellCheck and shfmt gates. Use when configuring or running static verification, including extensionless files.
kind: convention
domain: bash
profile: core
applicability: Bash scripts and sourced Bash libraries
requires: bash
provenance: house
---

# Bash build and checks

Owns syntax, static analysis, formatting and tool/interpreter-version declarations.

```bash
bash -n -- bin/report
bash -n -- lib/output.bash
shellcheck --shell=bash bin/report lib/output.bash
shfmt -ln bash -i 2 -d bin/report lib/output.bash
```

Check the explicit file set with the supported Bash interpreter, ShellCheck and
the repository's shfmt configuration. Bash reads one script per `bash -n`
invocation; remaining filenames would be script arguments. A missing required
checker is an incomplete gate.

Include extensionless executables, `.bash` libraries and sourced fragments.
Identify Bash by interpreter and project ownership: `.sh` alone is ambiguous.
Exclude vendored/generated code according to the owning repository.

Resolve sourced libraries for ShellCheck. Narrow diagnostic suppressions need a
reason; do not suppress whole categories to make CI green. Consider optional
`check-set-e-suppressed` and `check-extra-masked-returns` checks for failure paths.
Explicit shfmt printer/parser flags override EditorConfig formatting options.

Check the minimum supported Bash version for newer syntax and builtins; record
tool versions using the repository's dependency mechanism.
[Behaviour tests](../testing/SKILL.md) are a separate gate.

Sources: [ShellCheck optional checks](https://www.shellcheck.net/wiki/Optional),
[shfmt manual](https://github.com/mvdan/sh/blob/master/cmd/shfmt/shfmt.1.scd).
