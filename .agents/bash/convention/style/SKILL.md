---
name: style
description: Bash syntax, quoting, arguments, naming and formatting. Use when writing or reviewing Bash scripts and sourced libraries.
kind: convention
domain: bash
profile: core
applicability: Bash scripts and sourced Bash libraries
requires: bash
provenance: house
---

# Bash style

Owns Bash syntax, data expansion, argument construction, names and formatting.

```bash
files=('quarter one.txt' '*.txt')
args=(--output "$output_dir")
processor "${args[@]}" -- "${files[@]}"
```

- Executables declare Bash with a Bash shebang; invoke them directly or with Bash,
  never `sh`. Sourced files can declare `# shellcheck shell=bash`.
  Declare a minimum Bash version before using version-specific features.
- Quote data expansions and forward lists with `"$@"` or `"${items[@]}"`
  (ShellCheck SC2086/SC2068). Build optional arguments as arrays rather than
  strings reparsed by `eval` or `bash -c`.
- Prefer `$(command)`, `[[ ... ]]` tests and `(( ... ))` arithmetic.
  Quote the right side of `==` for literal comparison; leave an intended glob
  unquoted. Validate numeric input before arithmetic: expressions and array
  subscripts can evaluate more than plain digits.
- Print arbitrary text with `printf '%s\n' "$value"`; keep format strings
  literal. Use `--` before arbitrary operands where that command supports it.
- Read literal lines with `IFS= read -r line` (SC2162). For arbitrary filename
  lists use NUL-delimited input, such as `find ... -print0` with `read -r -d ''`,
  rather than splitting command output on whitespace or newlines.
- Use `snake_case` for functions and local variables; uppercase for exported
  configuration and constants. Avoid reusing special names such as PATH or HOME.
- Preserve existing formatting. For new files default to two spaces,
  `name() { ...; }` and `then`/`do` on the condition line; the adopting
  repository's formatter configuration owns deviations.

Sources: [Google shell style](https://google.github.io/styleguide/shellguide.html),
[SC2086](https://www.shellcheck.net/wiki/SC2086),
[SC2068](https://www.shellcheck.net/wiki/SC2068),
[SC2162](https://www.shellcheck.net/wiki/SC2162),
[GNU conditional expressions](https://www.gnu.org/software/bash/manual/html_node/Bash-Conditional-Expressions.html).
