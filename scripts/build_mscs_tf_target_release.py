#!/usr/bin/env python3
"""Build an additive immutable mSCS release with a genome-scale TF-target prior."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from typing import Any

from tf_target_prior_contract import PRIOR_MANIFEST, validate_prior_manifest


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASE = ROOT / "data/processed/mscs_release_bundle_v1_6_0_nichenet_prior_v1_candidate_universe_v2"
DEFAULT_PRIOR = ROOT / "data/processed/tf_target_prior_trrust_mouse_v1"
DEFAULT_OUTPUT = ROOT / "data/processed/mscs_release_bundle_v1_7_0_nichenet_tf_prior_v1"
DEFAULT_RELEASE_ID = "mscs_release_bundle:2026-10-01-nichenet-tf-target-prior-v1"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-release-dir", type=Path, default=DEFAULT_BASE)
    parser.add_argument("--tf-prior-dir", type=Path, default=DEFAULT_PRIOR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--release-id", default=DEFAULT_RELEASE_ID)
    return parser.parse_args()


def _load_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise SystemExit(f"Missing JSON input: {path}")
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise SystemExit(f"Expected JSON object: {path}")
    return value


def main() -> int:
    args = parse_args()
    base = args.base_release_dir.resolve()
    prior = args.tf_prior_dir.resolve()
    output = args.output_dir.resolve()
    if output.exists():
        raise SystemExit(f"Refusing to overwrite existing release output: {output}")
    base_manifest_path = base / "release_manifest.json"
    base_manifest = _load_json(base_manifest_path)
    prior_manifest_path = prior / PRIOR_MANIFEST
    prior_manifest = _load_json(prior_manifest_path)
    if not base.is_dir():
        raise SystemExit(f"Missing base release directory: {base}")
    validate_prior_manifest(prior)

    shutil.copytree(base, output)
    shutil.copytree(prior / "tf_target_prior", output / "tf_target_prior")

    manifest = dict(base_manifest)
    manifest["release_id"] = args.release_id
    manifest["parent_release_id"] = base_manifest.get("release_id")
    manifest["tf_target_prior_manifest"] = PRIOR_MANIFEST.as_posix()
    manifest["tf_target_prior"] = prior_manifest
    manifest["counts"] = dict(base_manifest.get("counts", {}))
    manifest["counts"].update({
        "tf_target_prior_source_records": prior_manifest["counts"]["source_record_count"],
        "tf_target_prior_pairs": prior_manifest["counts"]["pair_count"],
        "tf_target_prior_tf_count": prior_manifest["counts"]["tf_count"],
        "tf_target_prior_target_count": prior_manifest["counts"]["target_count"],
        "tf_target_prior_direct_graph_edge_count": prior_manifest["counts"]["direct_graph_edge_count"],
    })
    manifest["tf_target_prior_contract"] = {
        "causal_assertions_created": False,
        "graph_edges_created": False,
        "observed_response_used": False,
        "direct_graph_tier_preserved": True,
        "weights_status": "not_supplied",
        "ranks_status": "not_supplied",
    }
    manifest["original_mscs_resources_preserved"] = True
    manifest["migration_gaps"] = list(base_manifest.get("migration_gaps", [])) + [
        "The genome-scale TF-target prior is a separate broad response-independent resource and does not create mechanism-graph edges.",
        "The TRRUST raw snapshot is not redistributed; exact source and record checksums are retained for reproducibility.",
    ]
    files = dict(base_manifest.get("files", {}))
    for relative, metadata in prior_manifest["files"].items():
        files[relative] = metadata
    manifest["files"] = files
    (output / "release_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "output_dir": str(output),
        "release_id": args.release_id,
        "parent_release_id": base_manifest.get("release_id"),
        "tf_target_prior_pairs": prior_manifest["counts"]["pair_count"],
        "direct_graph_edge_count": prior_manifest["counts"]["direct_graph_edge_count"],
        "manifest_files": len(files),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
