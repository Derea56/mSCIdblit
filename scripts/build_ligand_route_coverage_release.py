#!/usr/bin/env python3
"""Create a release bundle with the all-ligand route-coverage index.

This is used when a release adds no new literature rows but needs to expose a
new derived index over an existing immutable graph snapshot. The copied graph,
edges, evidence, and route annotations are not rewritten.
"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from build_all_ligand_route_coverage import build, write_tsv_gz


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-bundle", type=Path, required=True)
    parser.add_argument("--output-bundle", type=Path, required=True)
    parser.add_argument("--release-id", required=True)
    args = parser.parse_args()

    source = args.source_bundle.resolve()
    output = args.output_bundle.resolve()
    if output.exists():
        raise FileExistsError(f"Output bundle already exists: {output}")
    shutil.copytree(source, output)

    coverage_rows, coverage_summary = build(output)
    write_tsv_gz(output / "mechanism_ligand_route_coverage.tsv.gz", coverage_rows)
    (output / "ligand_route_coverage_summary.json").write_text(
        json.dumps(coverage_summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    metadata_path = output / "bundle_metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["release_id"] = args.release_id
    metadata.setdefault("files", {})["ligand_route_coverage"] = "mechanism_ligand_route_coverage.tsv.gz"
    metadata.setdefault("counts", {})["ligand_route_coverage"] = len(coverage_rows)
    statement = (
        "The all-ligand route-coverage index is a derived evidence-layer summary; it does not assign confidence, "
        "authorize causal traversal, or create graph edges."
    )
    if statement not in metadata.setdefault("accuracy_contract", []):
        metadata["accuracy_contract"].append(statement)
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    summary = {
        "source_bundle": str(source),
        "output_bundle": str(output),
        "release_id": args.release_id,
        "coverage": coverage_summary,
        "graph_edges_changed": False,
        "literature_expansion_rows_changed": False,
        "confidence_scores_created": False,
    }
    (output / "ligand_route_coverage_release_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
