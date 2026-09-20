#!/usr/bin/env python3
"""Shared root resolution for wiki maintenance scripts."""

from __future__ import annotations

import os
from collections.abc import Mapping
from pathlib import Path

ENV_ROOT = "OBSIDIAN_VAULT_PATH"


def repository_root(script_file: str | Path = __file__) -> Path:
    return Path(script_file).resolve().parents[2]


def resolve_root(
    explicit: str | Path | None = None,
    *,
    environ: Mapping[str, str] = os.environ,
    script_file: str | Path = __file__,
) -> Path:
    """Resolve explicit --root, then the existing env var, then this repository."""
    selected = explicit if explicit is not None else environ.get(ENV_ROOT)
    return Path(selected).expanduser().resolve() if selected else repository_root(script_file)
