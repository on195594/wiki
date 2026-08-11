#!/usr/bin/env bash
# External link liveness check for formal wiki pages. See _meta/lychee.toml.
#
# Deliberately not part of wiki_health_check.py: this one needs the network,
# so its result is not reproducible from the files alone. Exit code is
# lychee's, so a nonzero exit means dead links, not "the script broke".
set -euo pipefail

ROOT="${OBSIDIAN_VAULT_PATH:-/home/lin/wiki}"
cd "$ROOT"

exec lychee -c _meta/lychee.toml "$@" \
  'concepts/**/*.md' \
  'queries/**/*.md' \
  'comparisons/**/*.md' \
  'operations/**/*.md'
