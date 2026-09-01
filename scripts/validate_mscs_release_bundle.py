#!/usr/bin/env python3
"""Validate checksums and required contents of a combined mSCS release bundle."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BUNDLE = ROOT / "data" / "processed" / "mscs_release_bundle_v1_4_0_method_resources_v1"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    bundle = args.bundle_dir.resolve()
    manifest_path = bundle / "release_manifest.json"
    if not manifest_path.is_file():
        raise SystemExit(f"Missing release manifest: {manifest_path}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    required = [
        "mechanism_graph/mechanism_nodes.tsv",
        "mechanism_graph/mechanism_node_roles.tsv",
        "mechanism_graph/mechanism_edges.tsv",
        "mechanism_graph/mechanism_edge_sources.tsv",
        "mechanism_graph/mechanism_pathways.tsv",
        "method_resources/method_resource_manifest.tsv",
        "method_resources/source_snapshot_manifest.tsv",
        "method_resources/canonical_communication_records.tsv",
        "method_resources/method_resource_records.tsv",
        "method_resources/method_resource_projections.tsv",
        "method_resources/method_resource_materialization.sql",
    ]
    missing = [relative for relative in required if not (bundle / relative).is_file()]
    if missing:
        raise SystemExit("Release bundle is missing required files: " + ", ".join(missing))
    mismatches: list[str] = []
    for relative, expected in manifest.get("files", {}).items():
        path = bundle / relative
        if not path.is_file():
            mismatches.append(f"missing manifest file: {relative}")
            continue
        actual = sha256(path)
        if actual != expected.get("sha256") or path.stat().st_size != expected.get("bytes"):
            mismatches.append(f"checksum/size mismatch: {relative}")
    if mismatches:
        raise SystemExit("Release bundle validation failed: " + "; ".join(mismatches))
    print(json.dumps({
        "status": "PASS combined mSCS release bundle validation",
        "release_id": manifest.get("release_id"),
        "manifest_files_checked": len(manifest.get("files", {})),
        "migration_gaps": len(manifest.get("migration_gaps", [])),
        "original_mscs_resources_preserved": manifest.get("original_mscs_resources_preserved"),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
