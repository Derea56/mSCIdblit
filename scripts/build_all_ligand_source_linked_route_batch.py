#!/usr/bin/env python3
"""Collect historical source-linked routes for all known ligand-receptor pairs.

Historical Module 21B batches contain curated evidence routes at several
levels of completeness.  This overlay exposes the known-ligand/known-receptor
records to the current release while preserving unknown intermediate, TF, and
target layers as explicit ``????`` fields.  It is an evidence-layer import:
it does not create graph edges, causal assertions, or confidence scores.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def historical_rows(root: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    seen: set[str] = set()
    for path in sorted((root / "work/module_b_consolidation/module21b").glob("module21b_literature_expansion_batch*.json")):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(payload, list):
            continue
        for value in payload:
            if not isinstance(value, dict):
                continue
            row = {str(key): "" if item is None else str(item) for key, item in value.items()}
            expansion_id = row.get("expansion_id", "")
            if not expansion_id or expansion_id in seen:
                continue
            seen.add(expansion_id)
            rows.append(row)
    return rows


def read_tsv(path: Path) -> list[dict[str, str]]:
    import csv

    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def split_values(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()]


def reconcile_edge_endpoints(row: dict[str, str], edges: dict[str, tuple[str, str]]) -> None:
    """Use current edge endpoints when historical node IDs were reindexed."""

    lr_edge = edges.get(row.get("ligand_receptor_edge_id", ""))
    if lr_edge:
        row["ligand_node_id"], row["receptor_node_id"] = lr_edge
    tf_edge = edges.get(row.get("tf_target_edge_id", ""))
    if tf_edge:
        row["transcription_factor_node_id"], row["target_gene_node_id"] = tf_edge


def append_unique(value: str, *additions: str) -> str:
    result: list[str] = []
    seen: set[str] = set()
    for item in split_values(value) + [part.strip() for addition in additions for part in addition.split(";")]:
        if item and item not in seen:
            seen.add(item)
            result.append(item)
    return ";".join(result)


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    bundle = args.bundle.resolve()

    current_expansions = read_tsv(bundle / "mechanism_literature_expansion.tsv")
    current_ids = {row.get("expansion_id", "") for row in current_expansions}
    node_ids = {row["node_id"] for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {
        row["edge_id"]: (row["source_node_id"], row["target_node_id"])
        for row in read_tsv(bundle / "mechanism_edges.tsv")
    }
    queue_ids = {row["queue_id"] for row in read_tsv(bundle / "mechanism_downstream_curation_queue.tsv")}
    evidence_ids = {row["record_id"] for row in read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")}

    candidates: list[dict[str, str]] = []
    skipped = {
        "already_current": 0,
        "missing_ligand_or_receptor": 0,
        "missing_graph_reference": 0,
        "missing_source_link": 0,
        "missing_primary_locator": 0,
    }
    for row in historical_rows(root):
        if row["expansion_id"] in current_ids:
            skipped["already_current"] += 1
            continue
        if not row.get("ligand_label") or not row.get("receptor_label"):
            skipped["missing_ligand_or_receptor"] += 1
            continue
        if any(
            row.get(field, "") and row[field] not in node_ids
            for field in (
                "ligand_node_id",
                "receptor_node_id",
                "intracellular_continuation_node_id",
                "transcription_factor_node_id",
                "target_gene_node_id",
                "output_node_id",
            )
        ) or any(
            row.get(field, "") and row[field] not in edges
            for field in (
                "ligand_receptor_edge_id",
                "receptor_intracellular_edge_id",
                "intracellular_tf_edge_id",
                "tf_target_edge_id",
            )
        ):
            skipped["missing_graph_reference"] += 1
            continue
        if (
            not row.get("source_queue_id")
            or row["source_queue_id"] not in queue_ids
            or not row.get("source_evidence_record_id")
            or row["source_evidence_record_id"] not in evidence_ids
        ):
            skipped["missing_source_link"] += 1
            continue
        if not row.get("primary_locator"):
            skipped["missing_primary_locator"] += 1
            continue

        reconcile_edge_endpoints(row, edges)
        row["route_linkage_status"] = append_unique(
            row.get("route_linkage_status", ""),
            "literature_expansion:all_ligand_source_linked_route",
            "known_ligand_receptor",
            "end_to_end_chain_not_asserted_by_single_source",
        )
        row["limitations"] = append_unique(
            row.get("limitations", ""),
            "This all-ligand import preserves unresolved intermediate, TF, and target layers as explicit gaps; it does not infer them from the ligand-receptor pair.",
        )
        row["source_scope"] = append_unique(
            row.get("source_scope", ""),
            "historical_primary_source_linked_all_ligand_batch",
        )
        candidates.append(row)

    candidates.sort(key=lambda row: row["expansion_id"])
    expansion_ids = [row["expansion_id"] for row in candidates]
    if len(expansion_ids) != len(set(expansion_ids)):
        raise ValueError("historical route overlay contains duplicate expansion IDs")
    args.output.resolve().write_text(json.dumps(candidates, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "rows": len(candidates),
                "ligands": len({row["ligand_label"] for row in candidates}),
                "known_ligand_receptor_edges": len({row["ligand_receptor_edge_id"] for row in candidates}),
                "skipped": skipped,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
