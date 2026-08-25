#!/usr/bin/env python3
"""Validate a Module 20B–24B mechanism graph release bundle."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BUNDLE = ROOT / "data" / "processed" / "mechanism_graph_module20_24_v2026_08_25"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument(
        "--report",
        type=Path,
        default=None,
        help="Optional report path. Defaults to bundle_dir/validation_report.json.",
    )
    return parser.parse_args()


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        rows = list(reader)
        return reader.fieldnames or [], rows


def duplicates(values: list[str]) -> list[str]:
    return sorted(value for value, count in Counter(values).items() if count > 1)


def validate(bundle_dir: Path) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []
    required = [
        "mechanism_nodes.tsv",
        "mechanism_edges.tsv",
        "mechanism_edge_sources.tsv",
        "mechanism_pathways.tsv",
        "mechanism_boundary_summary.tsv",
        "bundle_metadata.json",
    ]
    missing = [name for name in required if not (bundle_dir / name).exists()]
    errors.extend(f"missing file: {name}" for name in missing)
    if errors:
        return {"status": "fail", "errors": errors, "warnings": warnings}

    node_fields, nodes = read_tsv(bundle_dir / "mechanism_nodes.tsv")
    edge_fields, edges = read_tsv(bundle_dir / "mechanism_edges.tsv")
    source_fields, sources = read_tsv(bundle_dir / "mechanism_edge_sources.tsv")
    pathway_fields, pathways = read_tsv(bundle_dir / "mechanism_pathways.tsv")
    boundary_fields, boundaries = read_tsv(bundle_dir / "mechanism_boundary_summary.tsv")
    metadata = json.loads((bundle_dir / "bundle_metadata.json").read_text())

    expected_fields = {
        "nodes": ["node_id", "canonical_label", "label_variants", "modules", "pathways", "exportable_edge_count"],
        "edges": [
            "edge_id", "module", "source_node_id", "target_node_id", "source_label",
            "relation_type", "target_label", "pathway_name", "evidence_layer", "edge_status",
            "context_scope", "cell_type_context", "compartment_context", "species_context",
            "injury_context", "confidence_tier", "export_priority", "evidence_ids",
            "evidence_count", "source_locator_count", "exportable", "consolidation_note",
        ],
        "sources": [
            "source_id", "edge_id", "module", "evidence_id", "source_kind", "source_locator",
            "source_locator_status", "support_kind", "species_support", "source_scope", "confidence_tier", "citation_note",
            "evidence_summary", "limitations", "evidence_layer", "evidence_exportable",
            "consolidation_note",
        ],
        "pathways": ["module", "pathway_name", "edge_count", "node_count", "evidence_count"],
        "boundaries": [
            "module", "pathway_name", "evidence_layer", "edge_status", "export_priority",
            "nonexportable_edge_count",
        ],
    }
    for label, actual, expected in (
        ("nodes", node_fields, expected_fields["nodes"]),
        ("edges", edge_fields, expected_fields["edges"]),
        ("sources", source_fields, expected_fields["sources"]),
        ("pathways", pathway_fields, expected_fields["pathways"]),
        ("boundaries", boundary_fields, expected_fields["boundaries"]),
    ):
        if actual != expected:
            errors.append(f"{label} header mismatch: expected {expected}, got {actual}")

    node_ids = [row["node_id"] for row in nodes]
    edge_ids = [row["edge_id"] for row in edges]
    source_ids = [row["source_id"] for row in sources]
    if duplicates(node_ids):
        errors.append(f"duplicate node IDs: {duplicates(node_ids)[:5]}")
    if duplicates(edge_ids):
        errors.append(f"duplicate edge IDs: {duplicates(edge_ids)[:5]}")
    if duplicates(source_ids):
        errors.append(f"duplicate source IDs: {duplicates(source_ids)[:5]}")

    node_id_set = set(node_ids)
    edge_id_set = set(edge_ids)
    missing_nodes = sorted(
        {
            node_id
            for row in edges
            for node_id in (row["source_node_id"], row["target_node_id"])
            if node_id not in node_id_set
        }
    )
    if missing_nodes:
        errors.append(f"edges reference missing nodes: {missing_nodes[:5]}")

    missing_source_edges = sorted({row["edge_id"] for row in sources if row["edge_id"] not in edge_id_set})
    if missing_source_edges:
        errors.append(f"sources reference missing edges: {missing_source_edges[:5]}")

    nonexportable_edges = [row["edge_id"] for row in edges if row["exportable"] != "true"]
    if nonexportable_edges:
        errors.append(f"non-exportable rows present in graph edge file: {nonexportable_edges[:5]}")

    sources_by_edge: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in sources:
        sources_by_edge[row["edge_id"]].append(row)
    no_sources = sorted(edge_id_set - set(sources_by_edge))
    if no_sources:
        errors.append(f"exported edges without evidence sources: {no_sources[:5]}")

    for row in edges:
        actual_count = len(sources_by_edge.get(row["edge_id"], []))
        if int(row["evidence_count"]) != actual_count:
            errors.append(
                f"evidence count mismatch for {row['edge_id']}: "
                f"edge={row['evidence_count']} sources={actual_count}"
            )
        actual_locators = sum(bool(source["source_locator"].strip()) for source in sources_by_edge.get(row["edge_id"], []))
        if int(row["source_locator_count"]) != actual_locators:
            errors.append(
                f"locator count mismatch for {row['edge_id']}: "
                f"edge={row['source_locator_count']} sources={actual_locators}"
            )

    pathway_keys = {(row["module"], row["pathway_name"]) for row in pathways}
    missing_pathways = sorted(
        {(row["module"], row["pathway_name"]) for row in edges} - pathway_keys
    )
    if missing_pathways:
        errors.append(f"edges missing pathway summary rows: {missing_pathways[:5]}")

    for row in pathways:
        key = (row["module"], row["pathway_name"])
        pathway_edges = [edge for edge in edges if (edge["module"], edge["pathway_name"]) == key]
        pathway_nodes = {
            node_id
            for edge in pathway_edges
            for node_id in (edge["source_node_id"], edge["target_node_id"])
        }
        pathway_evidence = {
            source["evidence_id"]
            for edge in pathway_edges
            for source in sources_by_edge.get(edge["edge_id"], [])
        }
        if int(row["edge_count"]) != len(pathway_edges):
            errors.append(f"pathway edge count mismatch: {key}")
        if int(row["node_count"]) != len(pathway_nodes):
            errors.append(f"pathway node count mismatch: {key}")
        if int(row["evidence_count"]) != len(pathway_evidence):
            errors.append(f"pathway evidence count mismatch: {key}")

    metadata_counts = metadata.get("counts", {})
    actual_counts = {
        "nodes": len(nodes),
        "edges": len(edges),
        "edge_sources": len(sources),
        "pathways": len(pathways),
        "boundary_groups": len(boundaries),
    }
    for key, actual in actual_counts.items():
        if metadata_counts.get(key) != actual:
            errors.append(f"metadata count mismatch for {key}: metadata={metadata_counts.get(key)} actual={actual}")

    if any(not row["source_locator"].strip() for row in sources):
        warnings.append("some evidence sources have no stable locator; inspect evidence_exportable and limitations")

    report = {
        "status": "pass" if not errors else "fail",
        "bundle_dir": str(bundle_dir),
        "errors": errors,
        "warnings": warnings,
        "counts": actual_counts,
        "checks": {
            "unique_node_ids": not duplicates(node_ids),
            "unique_edge_ids": not duplicates(edge_ids),
            "unique_source_ids": not duplicates(source_ids),
            "edge_node_references_resolve": not missing_nodes,
            "source_edge_references_resolve": not missing_source_edges,
            "all_graph_edges_exportable": not nonexportable_edges,
            "all_graph_edges_have_evidence": not no_sources,
            "pathway_summaries_resolve": not missing_pathways,
            "metadata_counts_match": not any("metadata count mismatch" in error for error in errors),
        },
    }
    return report


def main() -> None:
    args = parse_args()
    bundle_dir = args.bundle_dir.resolve()
    report = validate(bundle_dir)
    report_path = (args.report or bundle_dir / "validation_report.json").resolve()
    report_path.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, sort_keys=True))
    raise SystemExit(0 if report["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
