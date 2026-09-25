#!/usr/bin/env python3
"""Compose separate receptor-level relay and TF evidence into route records.

The endpoint remains ligand-specific, but the intracellular relay and TF are
drawn from separate source-linked records at the same receptor. This is an
evidence-route composition only: no handoff or causal graph edge is asserted.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


TARGET_FULL = "ligand>receptor>intracellular>TF>target_gene_expression"
OUTPUT_FULL = "ligand>receptor>intracellular>TF>output"
RELAY_PATHS = {
    "ligand>receptor>intracellular>????>output",
    "ligand>receptor>intracellular>????>target_gene_expression",
    "ligand>receptor>intracellular>????",
}
TF_PATHS = {
    "ligand>receptor>????>TF>output",
    "ligand>receptor>????>TF>target_gene_expression",
    "ligand>receptor>TF>output",
}
PARTIAL_SPECS = {
    "ligand>receptor>????>????>target_gene_expression": "target",
    "ligand>receptor>intracellular>????>target_gene_expression": "target",
    "ligand>receptor>????>????>output": "output",
    "ligand>receptor>????>TF>output": "output",
    "ligand>receptor>TF>output": "output",
    "ligand>receptor>intracellular>????>output": "output",
    "ligand>receptor>output": "output",
}


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


def source_rank(row: dict[str, str]) -> tuple[int, int, str]:
    expansion_id = row.get("expansion_id", "")
    generated_markers = (
        "PROMO",
        "GAP",
        "SHARED",
        "FULLSEQ",
        "PAIR",
        "ALIAS",
        "RELAY",
        "COMPONENT",
        "TARGET",
        "SOURCE",
        "CATALOG",
    )
    generated = int(any(marker in expansion_id for marker in generated_markers))
    composite = int("composite" in row.get("source_scope", "").lower())
    return generated, composite, expansion_id


def build_rows(bundle: Path) -> list[dict[str, str]]:
    rows = read_tsv(bundle / "mechanism_literature_expansion.tsv")
    node_labels = {
        row["node_id"]: row["canonical_label"]
        for row in read_tsv(bundle / "mechanism_nodes.tsv")
    }

    # The receptor-shared overlay is not a source for this component pass;
    # otherwise the two overlays could recursively justify one another.
    source_rows = [
        row
        for row in rows
        if not row.get("expansion_id", "").startswith("M21B-LITEXP-RECSHARED-")
        and not row.get("expansion_id", "").startswith("M21B-LITEXP-COMPONENTSHARED-")
    ]

    relay_sources: dict[str, dict[str, dict[str, str]]] = defaultdict(dict)
    tf_sources: dict[str, dict[str, dict[str, str]]] = defaultdict(dict)
    for row in source_rows:
        receptor = row.get("receptor_label", "")
        if not receptor:
            continue
        relay = row.get("intracellular_continuation_node_id", "")
        tf = row.get("transcription_factor_node_id", "")
        if row.get("path_expression") in RELAY_PATHS and relay:
            prior = relay_sources[receptor].get(relay)
            if prior is None or source_rank(row) < source_rank(prior):
                relay_sources[receptor][relay] = row
        if row.get("path_expression") in TF_PATHS and tf:
            prior = tf_sources[receptor].get(tf)
            if prior is None or source_rank(row) < source_rank(prior):
                tf_sources[receptor][tf] = row

    # Include already materialized route signatures in the duplicate guard,
    # including the prior receptor-shared overlay.
    existing_signatures = {
        (
            row.get("ligand_label", ""),
            row.get("receptor_label", ""),
            row.get("intracellular_continuation_node_id", ""),
            row.get("transcription_factor_node_id", ""),
        )
        for row in rows
        if row.get("ligand_label")
        and row.get("receptor_label")
        and row.get("intracellular_continuation_node_id")
        and row.get("transcription_factor_node_id")
    }

    candidates: list[tuple[dict[str, str], str, dict[str, str], dict[str, str]]] = []
    seen_candidates: set[tuple[str, str, str, str, str, str]] = set()
    for row in rows:
        path = row.get("path_expression", "")
        kind = PARTIAL_SPECS.get(path)
        if not kind or row.get("route_status") != "retained_evidence_route":
            continue
        ligand = row.get("ligand_label", "")
        receptor = row.get("receptor_label", "")
        endpoint = row.get("target_gene_label", "") if kind == "target" else row.get("output_label", "")
        if not ligand or not receptor or not endpoint:
            continue
        for relay, relay_row in sorted(relay_sources.get(receptor, {}).items()):
            for tf, tf_row in sorted(tf_sources.get(receptor, {}).items()):
                signature = (ligand, receptor, relay, tf)
                if signature in existing_signatures:
                    continue
                candidate_key = (row.get("expansion_id", ""), kind, relay, tf, endpoint, path)
                if candidate_key in seen_candidates:
                    continue
                seen_candidates.add(candidate_key)
                candidates.append((row, kind, relay_row, tf_row))

    promoted_rows: list[dict[str, str]] = []
    for index, (row, kind, relay_row, tf_row) in enumerate(candidates, start=1):
        relay_id = relay_row["intracellular_continuation_node_id"]
        tf_id = tf_row["transcription_factor_node_id"]
        final_path = TARGET_FULL if kind == "target" else OUTPUT_FULL
        relay_ligand = relay_row.get("ligand_label", "")
        tf_ligand = tf_row.get("ligand_label", "")
        promoted = dict(row)
        promoted.update(
            {
                "expansion_id": f"M21B-LITEXP-COMPONENTSHARED-{index:04d}",
                "source_queue_id": "",
                "path_expression": final_path,
                "route_tier": (
                    "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges"
                    if kind == "target"
                    else "ligand_receptor_intracellular_tf_output_missing_target_gene"
                ),
                "known_layers": (
                    "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression"
                    if kind == "target"
                    else "ligand|receptor|intracellular_continuation|transcription_factor|output"
                ),
                "missing_layers": unique_join(
                    "receptor_to_intracellular_edge",
                    "intracellular_to_tf_edge",
                    "tf_to_target_edge" if kind == "target" else "",
                ),
                "intracellular_status": "receptor_component_source_supported_composed",
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": relay_id,
                "intracellular_continuation_label": node_labels.get(
                    relay_id, relay_row.get("intracellular_continuation_label", "")
                ),
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": tf_id,
                "transcription_factor_label": node_labels.get(
                    tf_id, tf_row.get("transcription_factor_label", "")
                ),
                "tf_target_edge_id": "",
                "source_chain_id": (
                    f"receptor_component_shared_route:{row.get('expansion_id', '')}:"
                    f"{relay_row.get('expansion_id', '')}:{tf_row.get('expansion_id', '')}"
                ),
                "source_evidence_record_id": "",
                "evidence_ids": unique_join(
                    row.get("evidence_ids", ""),
                    relay_row.get("evidence_ids", ""),
                    tf_row.get("evidence_ids", ""),
                ),
                "route_linkage_status": unique_join(
                    row.get("route_linkage_status", ""),
                    "receptor_shared_component_signature",
                    "cross_record_receptor_component_composition",
                    "separate_relay_and_tf_source_records",
                    "matching_curated_receptor_relay_and_tf_layers",
                    "graph_linked_route_source",
                    "ligand_specific_downstream_handoff_not_asserted",
                    "receptor_to_intracellular_edge_not_asserted",
                    "intracellular_to_tf_edge_not_asserted",
                    "tf_to_target_edge_not_asserted" if kind == "target" else "",
                    "end_to_end_chain_not_asserted_by_single_source",
                    "evidence_route_only",
                ),
                "citation_note": unique_join(
                    row.get("citation_note", ""),
                    f"The relay component is sourced from the {relay_ligand} route and the TF component from the {tf_ligand} route at the same receptor; neither component is asserted as ligand-specific.",
                ),
                "evidence_summary": unique_join(
                    row.get("evidence_summary", ""),
                    f"Separate primary-evidence records at this receptor support the {node_labels.get(relay_id, relay_id)} relay ({relay_ligand}) and {node_labels.get(tf_id, tf_id)} layer ({tf_ligand}); the ligand-specific endpoint evidence is retained from the source partial route.",
                ),
                "limitations": unique_join(
                    row.get("limitations", ""),
                    f"This is a two-source receptor component composition: the relay was observed with {relay_ligand} and the TF layer with {tf_ligand}, not necessarily with {row.get('ligand_label', '')}. The receptor-to-relay, relay-to-TF, and endpoint handoffs remain unasserted, and receptor sharing does not guarantee identical cell-context signaling. No causal traversal or confidence score is asserted.",
                ),
                "context_scope": unique_join(
                    row.get("context_scope", ""),
                    "receptor-shared relay and TF component composition; retain all source model boundaries",
                ),
                "primary_locator": unique_join(
                    row.get("primary_locator", ""),
                    relay_row.get("primary_locator", ""),
                    tf_row.get("primary_locator", ""),
                ),
                "source_scope": "receptor_component_composite_primary_evidence",
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
    print(
        json.dumps(
            {
                "output": str(args.output.resolve()),
                "rows": len(rows),
                "ligands": len({row["ligand_label"] for row in rows}),
                "signatures": len(
                    {
                        (
                            row["ligand_label"],
                            row["receptor_label"],
                            row["intracellular_continuation_node_id"],
                            row["transcription_factor_node_id"],
                        )
                        for row in rows
                    }
                ),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
