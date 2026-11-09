---
name: domain-design
description: Bash command interfaces and suitability. Use when designing utility arguments, streams, statuses or implementation boundaries.
kind: convention
domain: bash
profile: core
applicability: Bash scripts and sourced Bash libraries
requires: bash
provenance: house
---

# Bash command design

Owns command arguments, stream and status interfaces and shell's orchestration boundary.

```bash
case "${1-}" in
  --help) printf '%s\n' 'Usage: report INPUT'; exit 0 ;;
esac
if (( $# != 1 )); then
  printf '%s\n' 'Usage: report INPUT' >&2
  exit 2
fi
input=$1
```

Use Bash for command orchestration and simple stream processing. Prefer an
existing structured language for complex state, binary data, structured-document
editing or concurrency protocols.

Check argument counts before required positional parameters. Define unknown-option
and end-of-options behaviour; use `getopts` where short options fit the interface.
Keep command argument lists as arrays.

Document stdout's data contract; diagnostics and progress that would corrupt it
go to stderr. Deliberately distinguish an expected negative result, such as no
matches, from a command failure.

Prefer structured command output over parsing display tables or `ls`.
Bash variables cannot contain NUL and command substitution removes trailing
newlines. Use files, descriptors or another language when those bytes matter.
Declare external command versions and GNU/BSD requirements separately from Bash.

Sources: [GNU special parameters](https://www.gnu.org/software/bash/manual/html_node/Special-Parameters.html),
[GNU command substitution](https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html),
[Google shell suitability](https://google.github.io/styleguide/shellguide.html#when-to-use-shell).
