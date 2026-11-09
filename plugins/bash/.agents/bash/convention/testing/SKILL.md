---
name: testing
description: Bash behavioural testing and evidence limits. Use when selecting or reviewing tests for changed shell behaviour.
kind: convention
domain: bash
profile: core
applicability: Bash scripts and sourced Bash libraries
requires: bash
provenance: house
---

# Bash testing

Owns observable Bash behaviour tests and selection of a suitable test harness.

```bats
@test "missing input fails without writing output" {
  run --separate-stderr ./bin/report "$BATS_TEST_TMPDIR/missing"
  [ "$status" -ne 0 ]
  [ -n "$stderr" ]
  [ ! -e "$BATS_TEST_TMPDIR/report.txt" ]
}
```

Keep the existing harness. Bats is an option when a Bash-focused harness adds value,
not a required dependency for every script. Use temporary roots and controlled
command doubles for mutating paths.

Test changed behaviour: exact arguments with spaces, empty values, wildcards and
leading dashes; missing inputs; failures of critical commands; streams and status;
cleanup and the state left after failure. Assert absence of unintended writes.
Installers also test unrelated-setting preservation and repeatability when promised.

Source libraries in disposable shells and observe the caller state they promise
to preserve. Check declared Bash versions and command environments; current Linux
alone does not establish macOS, MSYS or older-Bash support.

When process behaviour changes, cover cancellation, readiness and owned-child
cleanup. Stubs prove the caller's protocol, not actual desktop or service behaviour.
Syntax, formatter and linter passes do not establish behavioural acceptance.

Bats `run` returns success to allow assertions; assert `$status` explicitly.
It runs in a subshell, so parent-shell variable changes do not persist.
Use `--separate-stderr` for stream contracts and Bats pipeline facilities rather
than piping `run` itself.

Source: [Bats semantics](https://bats-core.readthedocs.io/en/stable/writing-tests.html).
