#!/usr/bin/env python3
"""Build a response-independent mouse TF-target prior from retained source rows."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

from tf_target_prior_contract import (
    DIRECT_GRAPH_TIER,
    PRIOR_DIR,
    PRIOR_MANIFEST,
    PRIOR_TABLE,
    SOURCE_RECORDS,
    SOURCE_REGISTRY,
    TARGET_AXIS,
    TF_AXIS,
    aggregate_pairs,
    read_tsv,
    sha256,
    write_tsv,
)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PAIR_RECORDS = ROOT / "data/processed/public_tf_union_expansion_v1/tf_pair_records.tsv"
DEFAULT_SOURCE_REGISTRY = ROOT / "data/processed/public_tf_union_expansion_v1/source_registry.tsv"
DEFAULT_GRAPH = ROOT / "data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion627"
DEFAULT_OUTPUT = ROOT / "data/processed/tf_target_prior_trrust_mouse_v1"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pair-records", type=Path, default=DEFAULT_PAIR_RECORDS)
    parser.add_argument("--source-registry", type=Path, default=DEFAULT_SOURCE_REGISTRY)
    parser.add_argument("--graph-bundle-dir", type=Path, default=DEFAULT_GRAPH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def build_direct_graph_tier(graph_dir: Path) -> list[dict[str, str]]:
    edges = read_tsv(graph_dir / "mechanism_edges.tsv")
    roles = read_tsv(graph_dir / "mechanism_node_roles.tsv")
    role_by_node: dict[str, set[str]] = {}
    for row in roles:
        role_by_node.setdefault(row.get("node_id", ""), set()).add(row.get("role", ""))
    rows: list[dict[str, str]] = []
    for edge in edges:
        if edge.get("exportable") != "true":
            continue
        if "transcription_factor" not in role_by_node.get(edge.get("source_node_id", ""), set()):
            continue
        if "target_gene" not in role_by_node.get(edge.get("target_node_id", ""), set()):
            continue
        rows.append({
            "tier": "direct_graph_evidence",
            "edge_id": edge.get("edge_id", ""),
            "source_node_id": edge.get("source_node_id", ""),
            "target_node_id": edge.get("target_node_id", ""),
            "source_label": edge.get("source_label", ""),
            "target_label": edge.get("target_label", ""),
            "relation_type": edge.get("relation_type", ""),
            "effect_polarity": edge.get("effect_polarity", ""),
            "species_context": edge.get("species_context", ""),
            "evidence_status": edge.get("evidence_status", ""),
            "export_priority": edge.get("export_priority", ""),
            "evidence_layer": edge.get("evidence_layer", ""),
            "confidence_tier": edge.get("confidence_tier", ""),
            "evidence_ids": edge.get("evidence_ids", ""),
            "source_locator_count": edge.get("source_locator_count", ""),
            "graph_source": str(graph_dir.relative_to(ROOT)),
        })
    return sorted(rows, key=lambda row: row["edge_id"])


def main() -> int:
    args = parse_args()
    pair_path = args.pair_records.resolve()
    registry_path = args.source_registry.resolve()
    graph_dir = args.graph_bundle_dir.resolve()
    output = args.output_dir.resolve()
    if output.exists():
        raise SystemExit(f"Refusing to overwrite existing TF-target prior output: {output}")

    pair_rows = read_tsv(pair_path)
    registry_rows = read_tsv(registry_path)
    registry = [
        row for row in registry_rows
        if row.get("source_registry") == "TRRUST" and row.get("species_scope") == "mouse"
    ]
    if len(registry) != 1:
        raise SystemExit("Expected exactly one TRRUST mouse source-registry row")
    source = registry[0]
    if source.get("resource_class") != "tf_regulon":
        raise SystemExit("TRRUST mouse source is not classified as a TF regulon resource")
    source_rows = [
        row for row in pair_rows
        if row.get("source_registry") == "TRRUST" and row.get("species_scope") == "mouse"
    ]
    if not source_rows:
        raise SystemExit("No retained TRRUST mouse TF-target source rows")
    if any(not row.get("source_record_id") or not row.get("raw_record_sha256") or not row.get("source_locator") for row in source_rows):
        raise SystemExit("A retained TRRUST source row lacks exact record provenance")
    prior_rows = aggregate_pairs(source_rows)
    direct_rows = build_direct_graph_tier(graph_dir)
    tf_rows = [{"tf_id": row["tf_id"], "tf_symbol": row["tf_symbol"], "species": "mouse", "identifier_namespace": "mouse_gene_symbol"}
               for row in sorted({row["tf_id"]: row for row in prior_rows}.values(), key=lambda row: row["tf_id"])]
    target_rows = [{"target_id": row["target_id"], "target_symbol": row["target_symbol"], "species": "mouse", "identifier_namespace": "mouse_gene_symbol"}
                   for row in sorted({row["target_id"]: row for row in prior_rows}.values(), key=lambda row: row["target_id"])]

    output.mkdir(parents=True)
    write_tsv(output / SOURCE_RECORDS, list(source_rows[0]), source_rows)
    write_tsv(output / PRIOR_TABLE, list(prior_rows[0]), prior_rows)
    write_tsv(output / TF_AXIS, ["tf_id", "tf_symbol", "species", "identifier_namespace"], tf_rows)
    write_tsv(output / TARGET_AXIS, ["target_id", "target_symbol", "species", "identifier_namespace"], target_rows)
    write_tsv(output / DIRECT_GRAPH_TIER, list(direct_rows[0]) if direct_rows else ["tier", "edge_id"], direct_rows)

    source_registry_row = dict(source)
    source_registry_row.update({
        "license_name": "Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)",
        "license_url": "https://creativecommons.org/licenses/by-sa/4.0/",
        "license_basis_locator": "https://www.grnpedia.org/trrust/",
        "usage_scope": "non_commercial_research",
        "raw_snapshot_distribution_status": "not_distributed; source checksum and record hashes retained",
    })
    write_tsv(output / SOURCE_REGISTRY, list(source_registry_row), [source_registry_row])

    files: dict[str, dict[str, Any]] = {}
    for relative in (PRIOR_TABLE, SOURCE_RECORDS, TF_AXIS, TARGET_AXIS, DIRECT_GRAPH_TIER, SOURCE_REGISTRY):
        path = output / relative
        files[relative.as_posix()] = {"sha256": sha256(path), "bytes": path.stat().st_size}
    manifest = {
        "schema_version": "tf_target_prior_v1",
        "prior_kind": "response_independent_mouse_tf_target_prior",
        "species": "mouse",
        "identifier_namespace": "mouse_gene_symbol",
        "response_selection": "none",
        "observed_response_used": False,
        "orthology_inference_used": False,
        "storage": {"format": "tsv", "dtype": None, "layout": None, "numeric_artifact": False},
        "weights": {"status": "not_supplied", "column": "association_weight"},
        "ranks": {"status": "not_supplied", "column": "association_rank"},
        "sign_policy": "retain source-supported activation/repression; conflicting or unknown source signs remain unknown",
        "source": {
            "source_registry": source["source_registry"],
            "source_version": source["source_version"],
            "source_locator": "https://www.grnpedia.org/trrust/data/trrust_rawdata.mouse.tsv",
            "source_snapshot_sha256": source["snapshot_sha256"],
            "license_name": source_registry_row["license_name"],
            "license_url": source_registry_row["license_url"],
            "license_basis_locator": source_registry_row["license_basis_locator"],
            "usage_scope": source_registry_row["usage_scope"],
        },
        "input_provenance": {
            "processed_pair_records_path": str(pair_path.relative_to(ROOT)),
            "processed_pair_records_sha256": sha256(pair_path),
            "source_registry_path": str(registry_path.relative_to(ROOT)),
            "source_registry_sha256": sha256(registry_path),
            "graph_bundle_path": str(graph_dir.relative_to(ROOT)),
            "direct_graph_edges_changed": False,
            "observed_response_dataset_used": False,
        },
        "counts": {
            "source_record_count": len(source_rows),
            "pair_count": len(prior_rows),
            "tf_count": len(tf_rows),
            "target_count": len(target_rows),
            "direct_graph_edge_count": len(direct_rows),
        },
        "files": files,
        "limitations": [
            "This is a broad source prior, not a causal graph and not a TF activity state.",
            "TRRUST signs are source-supported relationship modes; unknown and conflicting signs are retained as unknown.",
            "TRRUST provides no association weights or ranks in the retained source snapshot.",
            "The raw source snapshot is not redistributed; source URL, snapshot checksum, record hashes, and locators are retained.",
        ],
    }
    (output / PRIOR_MANIFEST).write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output_dir": str(output), "pair_count": len(prior_rows), "direct_graph_edge_count": len(direct_rows)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
