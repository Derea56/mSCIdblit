#!/usr/bin/env python3
"""Build one mSCS release bundle from a graph bundle and method-resource intake.

The graph bundle remains the mechanism snapshot.  The method-resource layer
adds canonical communication records, native projections, provenance manifests,
and equivalence reports without changing or deleting the original mSCS files.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_GRAPH = ROOT / "data" / "processed" / "mechanism_graph_module20_24_v2026_09_01"
DEFAULT_METHOD = ROOT / "data" / "processed" / "method_resource_migration_v1"
DEFAULT_OUTPUT = ROOT / "data" / "processed" / "mscs_release_bundle_v1_4_0_method_resources_v1"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def copy_tree(source: Path, destination: Path) -> list[Path]:
    copied: list[Path] = []
    for path in sorted(source.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(source)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        copied.append(target)
    return copied


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--graph-bundle-dir", type=Path, default=DEFAULT_GRAPH)
    parser.add_argument("--method-migration-dir", type=Path, default=DEFAULT_METHOD)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    graph = args.graph_bundle_dir.resolve()
    method = args.method_migration_dir.resolve()
    output = args.output_dir.resolve()
    required_graph = [
        "bundle_metadata.json",
        "mechanism_nodes.tsv",
        "mechanism_node_roles.tsv",
        "mechanism_edges.tsv",
        "mechanism_edge_sources.tsv",
        "mechanism_pathways.tsv",
        "mechanism_boundary_summary.tsv",
        "validation_report.json",
    ]
    required_method = [
        "method_resource_manifest.tsv",
        "source_snapshot_manifest.tsv",
        "canonical_communication_records.tsv",
        "method_resource_records.tsv",
        "method_resource_complex_components.tsv",
        "method_resource_annotations.tsv",
        "method_resource_projections.tsv",
        "method_resource_numeric_artifacts.tsv",
        "method_resource_materialization.sql",
        "method_resource_migration_report.json",
        "method_resource_equivalence_report.json",
        "method_native",
    ]
    missing = [str(graph / name) for name in required_graph if not (graph / name).exists()]
    missing.extend(str(method / name) for name in required_method if not (method / name).exists())
    if missing:
        raise SystemExit("Missing release inputs: " + ", ".join(missing))

    if output.exists():
        raise SystemExit(f"Refusing to overwrite existing release bundle: {output}")
    output.mkdir(parents=True)
    graph_files = copy_tree(graph, output / "mechanism_graph")
    method_files: list[Path] = []
    for name in required_method:
        source = method / name
        target = output / "method_resources" / name
        if source.is_dir():
            method_files.extend(copy_tree(source, target))
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
            method_files.append(target)

    graph_metadata = json.loads((graph / "bundle_metadata.json").read_text(encoding="utf-8"))
    method_report = json.loads((method / "method_resource_migration_report.json").read_text(encoding="utf-8"))
    file_manifest: dict[str, dict[str, Any]] = {}
    for path in sorted(graph_files + method_files):
        file_manifest[str(path.relative_to(output))] = {
            "sha256": sha256(path),
            "bytes": path.stat().st_size,
        }
    manifest = {
        "schema_version": "mscs_release_bundle_v1",
        "release_id": "mscs_release_bundle_v1_4_0_method_resources_v1",
        "project": "mSCIdblit",
        "target_consumer": "mSCS",
        "mechanism_graph_release": graph_metadata.get("release_id", "unknown"),
        "mechanism_graph_version": graph_metadata.get("graph_version", "unknown"),
        "method_resource_schema": "method_resource_layer_v1",
        "method_resource_migration_schema": method_report.get("schema_version"),
        "database_is_source_of_truth": True,
        "original_mscs_resources_preserved": True,
        "biological_validation_created_by_resource_import": False,
        "method_resource_membership_is_not_biological_validation": True,
        "counts": {
            "mechanism_graph_files": len(graph_files),
            "method_resource_files": len(method_files),
            "canonical_communication_records": method_report.get("canonical_communication_count"),
            "method_resource_records": method_report.get("method_resource_record_count"),
            "method_resource_projections": method_report.get("projection_count"),
            "numeric_artifacts": method_report.get("numeric_artifact_count"),
        },
        "migration_gaps": method_report.get("migration_gaps", []),
        "files": file_manifest,
    }
    (output / "release_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output_dir": str(output), "file_count": len(file_manifest), "release_id": manifest["release_id"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
