#!/usr/bin/env python3
"""Combine the validated ligand-specific primary route overlays once."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from .build_primary_il13_stat6_output_route_batch import make_rows as make_il13_rows
    from .build_primary_output_linked_route_batch import make_rows as make_linked_rows
except ImportError:  # pragma: no cover - direct script execution
    from build_primary_il13_stat6_output_route_batch import make_rows as make_il13_rows
    from build_primary_output_linked_route_batch import make_rows as make_linked_rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = make_il13_rows(args.bundle.resolve()) + make_linked_rows(args.bundle.resolve())
    expansion_ids = [row["expansion_id"] for row in rows]
    if len(expansion_ids) != len(set(expansion_ids)):
        raise ValueError("combined route overlay contains duplicate expansion IDs")
    args.output.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
