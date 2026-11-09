---
name: errors
description: Bash failures, traps, file replacement and child ownership. Use when writing or reviewing failure and cleanup paths.
kind: convention
domain: bash
profile: core
applicability: Bash scripts and sourced Bash libraries
requires: bash
provenance: house
---

# Bash errors and resource lifetime

Owns failure propagation, cleanup and filesystem/process resource ownership.

```bash
copy_report() {
  local source=$1 destination=$2
  if cp -- "$source" "$destination"; then
    return 0
  else
    local status=$?
    printf 'Copy failed: %s\n' "$source" >&2
    return "$status"
  fi
}
```

Check critical commands before using results or doing dependent mutations.
Capture status immediately; `$?` in `if ! command` is the negated status.
Separate declarations from command substitutions so `local`, `export` and
`readonly` do not mask failures (SC2155).

Choose `errexit`, `nounset` and `pipefail` deliberately at the executable
boundary, not as a universal safety header. `set -e` is suppressed in conditions,
negation and parts of AND/OR lists, including functions invoked there.
It is not exception handling or rollback; explicitly guard critical operations
(SC2310).

Pipelines normally return the last command's status. With `pipefail`, a producer's
SIGPIPE after an early reader exit can cause failure. Check the intended contract;
capture `PIPESTATUS` immediately when individual statuses matter. Command
substitution and asynchronous process substitution have separate failure semantics.

Acquire temporary resources with `mktemp` and check success before use. Then install
cleanup using a named function or single-quoted trap (SC2064), preserving the
original failure status. Define INT/TERM termination and exit status rather than
swallowing signals. Cleanup touches only this invocation's resources and recorded
child PIDs; wait for owned children when completion matters. `command &` succeeding
does not prove child success or readiness. Use `exec` for pure command wrappers.

Never read and truncate the same file in one operation (SC2094). For replacement,
write and validate a temporary file in the destination filesystem before rename.
Define permissions, symlink and concurrent-writer behaviour: rename alone does not
provide locking, metadata preservation or durable rollback. A failed write leaves
the existing configuration usable.

Sources: [GNU set](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html),
[SC2155](https://www.shellcheck.net/wiki/SC2155),
[SC2310](https://www.shellcheck.net/wiki/SC2310),
[SC2064](https://www.shellcheck.net/wiki/SC2064),
[SC2094](https://www.shellcheck.net/wiki/SC2094).
