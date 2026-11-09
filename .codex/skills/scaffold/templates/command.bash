#!/usr/bin/env bash

main() {
  if (($# == 0)) || [[ $1 == --help && $# == 1 ]]; then
    printf '%s\n' 'Usage: @COMMAND@ [--help]'
    return 0
  fi
  printf '%s\n' 'Usage: @COMMAND@ [--help]' >&2
  return 2
}

main "$@"
