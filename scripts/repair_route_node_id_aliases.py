#!/usr/bin/env python3
"""Repair uniquely resolvable node-ID/label mismatches in route overlays.

Older evidence-layer rows sometimes retained a node ID from a different
canonical-label record.  This repair is deliberately conservative: a label
must map to one node (case-insensitively), and any explicit edge endpoint for
the field must agree with the replacement.  Ambiguous or edge-conflicting
rows remain unchanged and are recorded in a release report.

The repair changes evidence-layer references only.  It does not alter graph
nodes, graph edges, causal status, confidence, or route semantics.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
from collections import Counter
from pathlib import Path

try:
    from .build_all_ligand_route_coverage import build as build_ligand_route_coverage
    from .build_all_ligand_route_coverage import write_tsv_gz as write_ligand_route_coverage
    from .route_artifacts import write_normalized_route_artifacts
except ImportError:  # pragma: no cover - direct script execution
    from build_all_ligand_route_coverage import build as build_ligand_route_coverage
    from build_all_ligand_route_coverage import write_tsv_gz as write_ligand_route_coverage
    from route_artifacts import write_normalized_route_artifacts


NODE_LABEL_FIELDS = {
    "ligand_node_id": "ligand_label",
    "receptor_node_id": "receptor_label",
    "intracellular_continuation_node_id": "intracellular_continuation_label",
    "transcription_factor_node_id": "transcription_factor_label",
    "target_gene_node_id": "target_gene_label",
    "output_node_id": "output_label",
}

EDGE_BINDINGS = {
    "ligand_node_id": ("ligand_receptor_edge_id", "source_node_id"),
    "receptor_node_id": ("ligand_receptor_edge_id", "target_node_id"),
    "intracellular_continuation_node_id": ("receptor_intracellular_edge_id", "target_node_id"),
    "transcription_factor_node_id": ("intracellular_tf_edge_id", "target_node_id"),
    "target_gene_node_id": ("tf_target_edge_id", "target_node_id"),
}


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", newline="", encoding="utf-8", errors="replace") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    if path.suffix == ".gz":
        with gzip.open(path, "wt", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows({field: row.get(field, "") for field in fields} for row in rows)
    else:
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


def node_label(row: dict[str, str]) -> str:
    return row.get("canonical_label", "") or row.get("canonical_name", "")


def label_key(value: str) -> str:
    return " ".join(str(value).split()).casefold()


def build_replacements(nodes: list[dict[str, str]]) -> dict[str, list[str]]:
    by_label: dict[str, list[str]] = {}
    for row in nodes:
        label = node_label(row)
        if not label:
            continue
        by_label.setdefault(label_key(label), []).append(row["node_id"])
    return {key: sorted(set(value)) for key, value in by_label.items()}


def repair_rows(
    rows: list[dict[str, str]],
    nodes_by_id: dict[str, dict[str, str]],
    edges_by_id: dict[str, dict[str, str]],
    candidates_by_label: dict[str, list[str]],
) -> tuple[Counter, Counter, list[dict[str, str]]]:
    repaired = Counter()
    skipped = Counter()
    examples: list[dict[str, str]] = []
    for row in rows:
        row_id = row.get("expansion_id") or row.get("route_evidence_id") or "unknown"
        for id_field, label_field in NODE_LABEL_FIELDS.items():
            current_id = row.get(id_field, "")
            label = row.get(label_field, "")
            if not current_id or not label or current_id not in nodes_by_id:
                continue
            current_label = node_label(nodes_by_id[current_id])
            if label_key(current_label) == label_key(label):
                continue
            candidates = candidates_by_label.get(label_key(label), [])
            if len(candidates) != 1:
                skipped["ambiguous_or_unmapped"] += 1
                continue
            replacement = candidates[0]
            if replacement == current_id:
                continue
            edge_field, endpoint_field = EDGE_BINDINGS.get(id_field, ("", ""))
            edge_id = row.get(edge_field, "") if edge_field else ""
            if edge_id:
                edge = edges_by_id.get(edge_id)
                if not edge or edge.get(endpoint_field) != replacement:
                    skipped["edge_conflict"] += 1
                    if len(examples) < 100:
                        examples.append(
                            {
                                "row_id": row_id,
                                "field": id_field,
                                "current_node_id": current_id,
                                "stored_label": label,
                                "current_node_label": current_label,
                                "candidate_node_id": replacement,
                                "edge_id": edge_id,
                                "edge_endpoint": edge.get(endpoint_field, "") if edge else "missing_edge",
                            }
                        )
                    continue
            row[id_field] = replacement
            repaired[f"{id_field}:{current_id}->{replacement}"] += 1
            if len(examples) < 100:
                examples.append(
                    {
                        "row_id": row_id,
                        "field": id_field,
                        "current_node_id": current_id,
                        "stored_label": label,
                        "current_node_label": current_label,
                        "replacement_node_id": replacement,
                        "status": "repaired",
                    }
                )
    return repaired, skipped, examples


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, required=True)
    args = parser.parse_args()
    bundle = args.bundle.resolve()

    nodes_fields, nodes = read_tsv(bundle / "mechanism_nodes.tsv")
    nodes_by_id = {row["node_id"]: row for row in nodes}
    edge_fields, edges = read_tsv(bundle / "mechanism_edges.tsv")
    edges_by_id = {row["edge_id"]: row for row in edges}
    candidates_by_label = build_replacements(nodes)

    repair_totals = Counter()
    skipped_totals = Counter()
    examples: list[dict[str, str]] = []
    file_reports: dict[str, dict[str, object]] = {}

    expansion_path = bundle / "mechanism_literature_expansion.tsv"
    expansion_fields, expansion_rows = read_tsv(expansion_path)
    repaired, skipped, file_examples = repair_rows(expansion_rows, nodes_by_id, edges_by_id, candidates_by_label)
    write_tsv(expansion_path, expansion_fields, expansion_rows)
    repair_totals.update(repaired)
    skipped_totals.update(skipped)
    examples.extend(file_examples)
    file_reports[expansion_path.name] = {
        "rows": len(expansion_rows),
        "repaired_cells": sum(repaired.values()),
        "repaired_patterns": len(repaired),
        "skipped_cells": sum(skipped.values()),
    }

    route_path = bundle / "mechanism_signaling_route_evidence.tsv.gz"
    route_fields, route_rows = read_tsv(route_path)
    repaired, skipped, file_examples = repair_rows(route_rows, nodes_by_id, edges_by_id, candidates_by_label)
    write_tsv(route_path, route_fields, route_rows)
    repair_totals.update(repaired)
    skipped_totals.update(skipped)
    examples.extend(file_examples)
    file_reports[route_path.name] = {
        "rows": len(route_rows),
        "repaired_cells": sum(repaired.values()),
        "repaired_patterns": len(repaired),
        "skipped_cells": sum(skipped.values()),
    }

    edge_sources_fields, edge_sources = read_tsv(bundle / "mechanism_edge_sources.tsv")
    normalized_counts = write_normalized_route_artifacts(bundle, route_rows, nodes, edges, edge_sources)
    coverage_rows, coverage_summary = build_ligand_route_coverage(bundle)
    write_ligand_route_coverage(bundle / "mechanism_ligand_route_coverage.tsv.gz", coverage_rows)
    (bundle / "ligand_route_coverage_summary.json").write_text(
        json.dumps(coverage_summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    report = {
        "bundle": str(bundle),
        "policy": "unique_label_and_explicit_edge_endpoint_only",
        "files": file_reports,
        "repaired_cell_count": sum(repair_totals.values()),
        "repaired_pattern_count": len(repair_totals),
        "repaired_patterns": dict(sorted(repair_totals.items())),
        "skipped_cell_count": sum(skipped_totals.values()),
        "skipped_reasons": dict(sorted(skipped_totals.items())),
        "examples": examples[:100],
        "normalized_route_artifacts": normalized_counts,
        "ligand_route_coverage": coverage_summary,
    }
    (bundle / "route_node_id_repair_summary.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    metadata_path = bundle / "bundle_metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata.setdefault("files", {})["route_node_id_repair_summary"] = "route_node_id_repair_summary.json"
    metadata.setdefault("counts", {})["ligand_route_coverage"] = len(coverage_rows)
    metadata.setdefault("graph_policy", {})["route_node_id_repairs_are_evidence_layer_only"] = True
    statement = (
        "Route node-ID repairs are applied only for uniquely label-resolved nodes with matching explicit edge endpoints; "
        "ambiguous and conflicting rows remain unchanged and are reported."
    )
    if statement not in metadata.setdefault("accuracy_contract", []):
        metadata["accuracy_contract"].append(statement)
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    expansion_summary_path = bundle / "mechanism_literature_expansion_summary.json"
    if expansion_summary_path.exists():
        expansion_summary = json.loads(expansion_summary_path.read_text(encoding="utf-8"))
        expansion_summary["literature_expansion_rows"] = len(expansion_rows)
        expansion_summary["route_evidence_rows_after"] = len(route_rows)
        expansion_summary["route_nodes"] = normalized_counts["route_nodes"]
        expansion_summary["route_edges"] = normalized_counts["route_edges"]
        expansion_summary["ligand_route_coverage"] = coverage_summary
        expansion_summary["route_node_id_repairs"] = {
            "repaired_cell_count": report["repaired_cell_count"],
            "skipped_cell_count": report["skipped_cell_count"],
            "policy": report["policy"],
        }
        expansion_summary_path.write_text(
            json.dumps(expansion_summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )

    coverage_release_summary = {
        "release_id": metadata.get("release_id", ""),
        "source_bundle": metadata.get("source_bundle", ""),
        "output_bundle": str(bundle),
        "coverage": coverage_summary,
        "graph_edges_changed": False,
        "confidence_scores_created": False,
        "literature_expansion_rows_changed": bool(report["repaired_cell_count"]),
        "route_node_id_repairs": {
            "repaired_cell_count": report["repaired_cell_count"],
            "skipped_cell_count": report["skipped_cell_count"],
            "policy": report["policy"],
        },
    }
    (bundle / "ligand_route_coverage_release_summary.json").write_text(
        json.dumps(coverage_release_summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
