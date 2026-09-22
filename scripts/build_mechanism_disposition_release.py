#!/usr/bin/env python3
"""Create an evidence-preserving release that adds the downstream disposition ledger."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from build_downstream_manual_disposition_ledger import main as build_ledger


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-bundle", type=Path, required=True)
    parser.add_argument("--output-bundle", type=Path, required=True)
    parser.add_argument("--release-id", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = args.source_bundle.resolve()
    output = args.output_bundle.resolve()
    if output.exists():
        raise FileExistsError(f"Output bundle already exists: {output}")
    shutil.copytree(source, output)

    ledger_path = output / "mechanism_downstream_manual_disposition.tsv"
    build_ledger_args = [
        "--bundle-dir",
        str(output),
        "--output",
        str(ledger_path),
    ]
    import sys

    previous_argv = sys.argv
    try:
        sys.argv = ["build_downstream_manual_disposition_ledger.py", *build_ledger_args]
        build_ledger()
    finally:
        sys.argv = previous_argv

    metadata_path = output / "bundle_metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["release_id"] = args.release_id
    metadata.setdefault("files", {})["downstream_manual_disposition"] = "mechanism_downstream_manual_disposition.tsv"
    metadata.setdefault("counts", {})["downstream_manual_disposition"] = sum(
        1 for _ in ledger_path.open(encoding="utf-8")
    ) - 1
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "source_bundle": str(source),
                "output_bundle": str(output),
                "release_id": args.release_id,
                "downstream_manual_disposition": metadata["counts"]["downstream_manual_disposition"],
                "graph_edges_changed": False,
                "causal_edges_created": False,
                "confidence_scores_created": False,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
