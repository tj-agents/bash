---
name: direction
description: Bash learning sequence and primary references. Use when sourcing guidance or planning lessons.
kind: knowledge
domain: bash
profile: knowledge
applicability: Bash scripts and sourced Bash libraries
requires: bash
provenance: house
---

# Bash direction

## The goal

Write small utilities with predictable arguments, status and side effects.

```bash
values=('two words' '*')
printf '<%s>\n' "${values[@]}"
```

## The skill tree

Learn in task order: quoting and arguments; arrays and expansion; conditions and
statuses; functions and scope; redirection; pipelines and subshells; traps and
child lifetimes; static analysis and behaviour tests. The adopting project owns
the learner's goals and progress.

## References

- [GNU Bash manual](https://www.gnu.org/software/bash/manual/bash.html): semantics;
  an installed matching-version manual is also authoritative.
- [Google shell style](https://google.github.io/styleguide/shellguide.html): idioms
  and preferences, not mandatory product or operating-system policy.
- [ShellCheck wiki](https://www.shellcheck.net/wiki/): diagnostics.
- [shfmt manual](https://github.com/mvdan/sh/blob/master/cmd/shfmt/shfmt.1.scd): formatting.
- [Bats](https://bats-core.readthedocs.io/en/stable/writing-tests.html): optional tests.

Distinguish language correctness from explicit project conventions.
