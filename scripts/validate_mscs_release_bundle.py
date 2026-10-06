#!/usr/bin/env python3
"""Validate checksums and required contents of an mSCS release bundle.

Current releases are self-contained: route connectors are the canonical
route-planning interface and any NicheNet evidence is already represented in
the release graph with source annotations.  Older releases may still declare
the separate dense NicheNet companion contract; that contract remains
supported when explicitly requested by the release manifest.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

from nichenet_release_contract import CONTRACT_RELATIVE, validate_contract


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BUNDLE = ROOT / "data" / "processed" / "mscs_release_bundle_v1_6_0_nichenet_prior_v1"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument(
        "--nichenet-artifact-root",
        type=Path,
        help=(
            "Optional legacy companion root containing "
            "nichenet_neutral_v1/ligand_target_matrix.f64le.bin. Required only "
            "when the release manifest declares the legacy NicheNet contract."
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    bundle = args.bundle_dir.resolve()
    companion_root = (
        args.nichenet_artifact_root.resolve()
        if args.nichenet_artifact_root is not None
        else None
    )
    manifest_path = bundle / "release_manifest.json"
    if not manifest_path.is_file():
        raise SystemExit(f"Missing release manifest: {manifest_path}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    legacy_nichenet_contract = manifest.get("nichenet_ligand_target_prior_manifest")
    current_route_connector_release = bool(manifest.get("route_connector_manifest_path"))
    if legacy_nichenet_contract and legacy_nichenet_contract != CONTRACT_RELATIVE.as_posix():
        raise SystemExit(
            "Release manifest points to an unsupported legacy NicheNet prior contract: "
            f"{legacy_nichenet_contract}"
        )
    if not legacy_nichenet_contract and not current_route_connector_release:
        raise SystemExit(
            "Release manifest declares neither the legacy NicheNet prior contract "
            "nor the current route connector contract"
        )
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
        "method_resources/method_resource_numeric_artifacts.tsv",
        "method_resources/method_native/nichenet_neutral_v1/neutral_model_manifest.json",
        "mechanism_graph/mechanism_output_bridges_validated.tsv",
    ]
    missing = [relative for relative in required if not (bundle / relative).is_file()]
    if missing:
        raise SystemExit("Release bundle is missing required files: " + ", ".join(missing))
    candidate_relative = manifest.get("candidate_universe_path")
    if candidate_relative:
        candidate_path = bundle / str(candidate_relative)
        if not candidate_path.is_file():
            raise SystemExit(f"Release bundle is missing candidate universe: {candidate_path}")
        csv.field_size_limit(max(csv.field_size_limit(), 10_000_000))
        with candidate_path.open(newline="", encoding="utf-8") as handle:
            candidate_rows = list(csv.DictReader(handle, delimiter="\t"))
        expected_count = manifest.get("counts", {}).get("candidate_universe_records")
        if expected_count is not None and len(candidate_rows) != expected_count:
            raise SystemExit(
                f"Candidate universe row count mismatch: {len(candidate_rows)} != {expected_count}"
            )
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
    connector_summary = None
    connector_relative = manifest.get("route_connector_manifest_path")
    if connector_relative:
        connector_manifest_path = bundle / str(connector_relative)
        if not connector_manifest_path.is_file():
            raise SystemExit(f"Release bundle is missing route connector manifest: {connector_manifest_path}")
        connector = json.loads(connector_manifest_path.read_text(encoding="utf-8"))
        if connector.get("schema_version") != "mscs_route_connectors_v1":
            raise SystemExit("Route connector manifest schema is unsupported")
        table = connector.get("connector_table", {})
        table_path = connector_manifest_path.parent / str(table.get("relative_path", ""))
        if not table_path.is_file() or sha256(table_path) != table.get("sha256"):
            raise SystemExit("Route connector table checksum validation failed")
        if connector.get("source_release", {}).get("release_id") != manifest.get("release_id"):
            raise SystemExit("Route connector release_id disagrees with release manifest")
        connector_summary = {
            "manifest_path": str(connector_manifest_path),
            "table_path": str(table_path),
            "route_connector_count": connector.get("counts", {}).get("route_connectors"),
        }
    if legacy_nichenet_contract and not current_route_connector_release:
        if companion_root is None:
            raise SystemExit(
                "This legacy release requires --nichenet-artifact-root for its "
                "separate dense NicheNet companion contract"
            )
        try:
            nichenet_summary = validate_contract(
                bundle=bundle, companion_artifact_root=companion_root
            )
        except ValueError as exc:
            raise SystemExit(f"NicheNet release contract validation failed: {exc}") from exc
    else:
        nichenet_summary = {
            "status": (
                "not_required_for_current_route_connector_release"
                if current_route_connector_release
                else "validated_legacy_contract"
            ),
            "evidence_integrated_in_release_graph": True,
            "legacy_manifest_retained_for_compatibility": bool(legacy_nichenet_contract),
        }
    print(json.dumps({
        "status": "PASS combined mSCS release bundle validation",
        "release_id": manifest.get("release_id"),
        "manifest_files_checked": len(manifest.get("files", {})),
        "migration_gaps": len(manifest.get("migration_gaps", [])),
        "candidate_universe_records": manifest.get("counts", {}).get("candidate_universe_records"),
        "original_mscs_resources_preserved": manifest.get("original_mscs_resources_preserved"),
        "nichenet": nichenet_summary,
        "route_connectors": connector_summary,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
