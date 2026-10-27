"""Data-root resolution for mSCIdblit (SCI D-006 / D-010, 2026-10-27).

One setting, ``MSCIDBLIT_DATA_ROOT``, names a directory laid out like this
repository's ``data/`` (``processed/``, ``raw/``). It defaults to the checkout's own
``data/``. Files that were untracked and moved to Biowulf
(``/data/derea/SCI-data/mSCIdblit/data``; superseded mechanism-graph snapshots and
every file of 50 MB or more) resolve through ``resolve()``: the local copy wins when
present, otherwise the path under ``MSCIDBLIT_DATA_ROOT``. See ``data/README.md`` and
``data/MANIFEST.tsv``.
"""

from __future__ import annotations

import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def data_root() -> Path:
    """Return the data root: ``MSCIDBLIT_DATA_ROOT`` (``~`` expanded, resolved to an
    absolute path) or ``<repo>/data`` when unset or empty."""

    value = os.environ.get("MSCIDBLIT_DATA_ROOT", "").strip()
    if not value:
        return REPO_ROOT / "data"
    return Path(value).expanduser().resolve()


def resolve(relative_to_data: str | os.PathLike[str]) -> Path:
    """Return the local ``data/<path>`` when it exists, else the same path under the root."""

    relative = Path(relative_to_data)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError(f"resolve() takes a path relative to data/, got {relative_to_data!r}")
    local = REPO_ROOT / "data" / relative
    if local.exists():
        return local
    return data_root() / relative
