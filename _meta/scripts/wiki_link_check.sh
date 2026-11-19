#!/usr/bin/env bash
# External link liveness for formal pages and raw source URLs. See _meta/lychee.toml.
#
# Deliberately not part of wiki_health_check.py: this one needs the network,
# so its result is not reproducible from the files alone. A nonzero exit
# can indicate link failures or an error running the check.
set -euo pipefail

PATH="${HOME:+$HOME/.local/bin:}$PATH"

ROOT=""
LYCHEE_ARGS=()
while (($#)); do
  case "$1" in
    --root)
      (($# >= 2)) || { printf '%s\n' 'error: --root requires a value' >&2; exit 2; }
      ROOT=$2
      shift 2
      ;;
    --root=*)
      ROOT=${1#--root=}
      shift
      ;;
    *)
      LYCHEE_ARGS+=("$1")
      shift
      ;;
  esac
done

if [[ -z "$ROOT" ]]; then
  ROOT=${OBSIDIAN_VAULT_PATH:-}
fi
SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
if [[ -z "$ROOT" ]]; then
  ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/../.." && pwd -P)
fi
cd "$ROOT"

python3 "$SCRIPT_DIR/wiki_raw_source_urls.py" --root "$PWD" | \
lychee -c _meta/lychee.toml "${LYCHEE_ARGS[@]}" - \
  'entities/**/*.md' \
  'concepts/**/*.md' \
  'queries/**/*.md' \
  'comparisons/**/*.md' \
  'operations/**/*.md'
