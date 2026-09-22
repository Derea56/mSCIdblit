#!/usr/bin/env python3
"""Create a checksum manifest for importing a graph release into mSCS."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BUNDLE = ROOT / "data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion262"
REQUIRED = ("mechanism_nodes.tsv", "mechanism_edges.tsv", "mechanism_edge_sources.tsv")
OPTIONAL = (
    "mechanism_node_roles.tsv", "mechanism_possible_signaling_paths.tsv",
    "mechanism_signaling_route_evidence.tsv", "mechanism_downstream_curation_queue.tsv",
    "mechanism_downstream_evidence_records.tsv", "mechanism_literature_expansion.tsv",
)


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
    metadata = json.loads((bundle / "bundle_metadata.json").read_text(encoding="utf-8"))
    missing = [name for name in REQUIRED if not (bundle / name).exists()]
    if missing:
        raise SystemExit("Missing required mSCS import files: " + ", ".join(missing))
    files = {}
    for name in REQUIRED + OPTIONAL:
        path = bundle / name
        if path.exists():
            files[name] = {"bytes": path.stat().st_size, "sha256": sha256(path)}
    manifest = {
        "manifest_schema": "mscs_import_manifest_v1",
        "target_consumer": "mSCS",
        "source_project": "mSCIdblit",
        "release_id": metadata.get("release_id", "unknown"),
        "bundle_dir": str(bundle),
        "import_command": "python3 mSCS/src/mscs/import_mechanism_bundle.py <bundle> --mechanism-dir <active_release> --export-tsv",
        "required_files": list(REQUIRED),
        "optional_files_present": [name for name in OPTIONAL if (bundle / name).exists()],
        "files": files,
        "counts": metadata.get("counts", {}),
        "route_evidence_is_non_causal": True,
        "confidence_scores_created": False,
        "graph_edges_created_by_public_lr_overlay": 0,
        "original_graph_bundle_preserved": True,
    }
    output = bundle / "mscs_import_manifest.json"
    output.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"manifest": str(output), "files": len(files), "release_id": manifest["release_id"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
