---
name: scaffold
description: Create a minimal Bash command project without overwriting an existing target. Use when explicitly asked to scaffold a new standalone Bash utility.
kind: utility
domain: bash
profile: scaffold
applicability: new standalone Bash utilities
requires: python
provenance: house
---

# Bash project scaffold

Creates the minimal executable structure in [structure](../../convention/structure/SKILL.md).

## Create a project

Choose the destination and command name from the user's request, then run the
shipped helper. The parent directory must exist and the project directory must
not exist, even as a symlink. It creates no production application logic.

```sh
python3 <skill-directory>/scripts/scaffold.py --destination ./projects --name report
```

The output contains `bin/report`, `.editorconfig` and `.shellcheckrc`.
The command implements help and rejects unsupported arguments. A write failure
reports the partial directory for inspection; it does not delete or retry it.

## Build and adapt

No compilation is needed. Implement only the requested behaviour, respecting the
project's declared Bash version and selected dependencies. Keep the owning
[build checks](../../convention/build/SKILL.md) with that project.

```sh
bash ./projects/report/bin/report --help
bash -n ./projects/report/bin/report
```

## Validation and publication

Check generated command behaviour and the project's static gates before delivery.
Scaffolding neither installs packages nor publishes anything.

```sh
shellcheck --shell=bash ./projects/report/bin/report
shfmt -ln bash -i 2 -d ./projects/report/bin/report
```
