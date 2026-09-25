#!/usr/bin/env python3
"""Promote partial routes when an exact cross-record full signature exists.

The promotion is deliberately evidence-layer only. It reuses an intracellular
relay and, where available, a TF/target relation from an existing full route
with the same ligand, receptor, and endpoint signature. It does not create
graph edges, causal traversals, or confidence scores.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


TARGET_FULL = "ligand>receptor>intracellular>TF>target_gene_expression"
OUTPUT_FULL = "ligand>receptor>intracellular>TF>output"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def unique_join(*values: str) -> str:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        for item in value.split(";"):
            item = item.strip()
            if item and item not in seen:
                seen.add(item)
                result.append(item)
    return "; ".join(result)


def preferred_signature(counter: Counter[tuple[str, str, str, str]]) -> tuple[str, str, str, str]:
    """Select the most frequently curated signature deterministically."""
    return sorted(counter.items(), key=lambda item: (-item[1], item[0]))[0][0]


def build_rows(bundle: Path) -> list[dict[str, str]]:
    rows = read_tsv(bundle / "mechanism_literature_expansion.tsv")
    node_labels = {row["node_id"]: row["canonical_label"] for row in read_tsv(bundle / "mechanism_nodes.tsv")}

    # Exclude the previous relay-promotion overlay as a source for this pass;
    # otherwise a generated route could recursively justify another route.
    base_rows = [
        row for row in rows
        if not row.get("expansion_id", "").startswith("M21B-LITEXP-RELAYPROMO-")
    ]
    target_signatures: dict[tuple[str, str, str], Counter[tuple[str, str, str, str]]] = defaultdict(Counter)
    output_signatures: dict[tuple[str, str, str], Counter[tuple[str, str, str, str]]] = defaultdict(Counter)
    for row in base_rows:
        path = row.get("path_expression", "")
        if path not in {TARGET_FULL, OUTPUT_FULL}:
            continue
        if not row.get("intracellular_continuation_node_id") or not row.get("transcription_factor_node_id"):
            continue
        signature = (
            row.get("intracellular_continuation_node_id", ""),
            row.get("transcription_factor_node_id", ""),
            row.get("tf_target_edge_id", ""),
            row.get("target_gene_node_id", "") or row.get("output_node_id", ""),
        )
        key = (
            row.get("ligand_label", ""),
            row.get("receptor_label", ""),
            row.get("target_gene_label", "") if path == TARGET_FULL else row.get("output_label", ""),
        )
        (target_signatures if path == TARGET_FULL else output_signatures)[key][signature] += 1

    candidates: list[tuple[dict[str, str], str, tuple[str, str, str, str]]] = []
    partial_specs = (
        ("ligand>receptor>????>????>target_gene_expression", "target"),
        ("ligand>receptor>intracellular>????>target_gene_expression", "target"),
        ("ligand>receptor>????>????>output", "output"),
        ("ligand>receptor>????>TF>output", "output"),
        ("ligand>receptor>TF>output", "output"),
        ("ligand>receptor>intracellular>????>output", "output"),
    )
    seen_source_ids: set[str] = set()
    for row in base_rows:
        if row.get("route_status") != "retained_evidence_route":
            continue
        path = row.get("path_expression", "")
        kind = next((kind for candidate_path, kind in partial_specs if candidate_path == path), None)
        if not kind or row.get("expansion_id") in seen_source_ids:
            continue
        key = (
            row.get("ligand_label", ""),
            row.get("receptor_label", ""),
            row.get("target_gene_label", "") if kind == "target" else row.get("output_label", ""),
        )
        source = target_signatures if kind == "target" else output_signatures
        if key not in source:
            continue
        signature = preferred_signature(source[key])
        candidates.append((row, kind, signature))
        seen_source_ids.add(row.get("expansion_id", ""))

    promoted_rows: list[dict[str, str]] = []
    for index, (row, kind, signature) in enumerate(candidates, start=1):
        relay_id, tf_id, tf_target_edge_id, endpoint_id = signature
        promoted = dict(row)
        final_path = TARGET_FULL if kind == "target" else OUTPUT_FULL
        original_missing = row.get("missing_layers", "")
        promoted.update(
            {
                "expansion_id": f"M21B-LITEXP-CROSSPROMO-{index:04d}",
                "source_queue_id": "",
                "path_expression": final_path,
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges" if kind == "target" else "ligand_receptor_intracellular_tf_output_missing_target_gene",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression" if kind == "target" else "ligand|receptor|intracellular_continuation|transcription_factor|output",
                "missing_layers": unique_join(
                    "receptor_to_intracellular_edge",
                    "intracellular_to_tf_edge",
                    "tf_to_target_edge" if kind == "target" else "",
                ),
                "intracellular_status": "source_supported_composed",
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": relay_id,
                "intracellular_continuation_label": node_labels.get(relay_id, row.get("intracellular_continuation_label", "")),
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": tf_id,
                "transcription_factor_label": node_labels.get(tf_id, row.get("transcription_factor_label", "")),
                "tf_target_edge_id": tf_target_edge_id if kind == "target" else "",
                "source_chain_id": f"M21B-LITEXP-CROSSPROMO-{index:04d}",
                "source_evidence_record_id": "",
                "route_linkage_status": unique_join(
                    row.get("route_linkage_status", ""),
                    "graph_linked_route_source",
                    "graph_linked_ligand_receptor_edge",
                    "cross_record_exact_ligand_receptor_endpoint_signature",
                    "matching_curated_full_route_signature",
                    "primary_layer_linked",
                    "receptor_to_intracellular_edge_not_asserted",
                    "intracellular_to_tf_edge_not_asserted",
                    "tf_to_target_edge_not_asserted" if kind == "target" else "",
                    "end_to_end_chain_not_asserted_by_single_source",
                    "evidence_route_only",
                ),
                "citation_note": unique_join(
                    row.get("citation_note", ""),
                    "The relay and endpoint signature are cross-record compositions from an existing full route with the same ligand-receptor-endpoint identity.",
                ),
                "evidence_summary": unique_join(
                    row.get("evidence_summary", ""),
                    f"The unresolved layers are filled through the existing {node_labels.get(relay_id, relay_id)} -> {node_labels.get(tf_id, tf_id)} route signature for this exact ligand-receptor endpoint.",
                ),
                "limitations": unique_join(
                    row.get("limitations", ""),
                    f"This is a cross-record composition; the original missing-layer state ({original_missing}) is retained conceptually, and no single source demonstrates every handoff. No causal traversal or confidence score is asserted.",
                ),
                "context_scope": unique_join(row.get("context_scope", ""), "exact ligand-receptor-endpoint signature composition; retain source model boundaries"),
                "primary_locator": unique_join(row.get("primary_locator", "")),
                "source_scope": "graph_linked_composite_primary_evidence",
                "curation_status": "curated_primary_route",
            }
        )
        promoted_rows.append(promoted)
    return promoted_rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = build_rows(args.bundle.resolve())
    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(args.output.resolve()),
        "rows": len(rows),
        "ligands": sorted({row["ligand_label"] for row in rows}),
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
