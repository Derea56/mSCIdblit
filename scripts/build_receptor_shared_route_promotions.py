#!/usr/bin/env python3
"""Promote partial routes using a downstream signature shared by the receptor.

This is deliberately an evidence-layer composition.  A partial ligand-receptor
route supplies the ligand-specific endpoint evidence, while a full route at
the same receptor supplies an intracellular-continuation/transcription-factor
signature.  The generated record keeps every missing handoff unasserted and
marks the receptor-shared composition so mSCS can evaluate it separately from
ligand-specific routes.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


TARGET_FULL = "ligand>receptor>intracellular>TF>target_gene_expression"
OUTPUT_FULL = "ligand>receptor>intracellular>TF>output"
FULL_PATHS = {TARGET_FULL, OUTPUT_FULL}
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
    """Prefer non-generated rows, then direct-looking source scopes."""
    expansion_id = row.get("expansion_id", "")
    generated_markers = (
        "CROSSPROMO",
        "RELAYPROMO",
        "COMPONENTPROMO",
        "TARGETPROMO",
        "SHAREDROUTE",
        "SRCSHARED",
        "FULLSEQ",
        "OUTPROMO",
        "TFPROMO",
        "PAIRWISE",
        "PAIRFULLOUT",
        "FULLOUT",
        "SPLITPROMO",
        "ALIASFULL",
        "GAPFULL",
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

    # Do not recursively consume this overlay or the exact endpoint overlay
    # that preceded it. Earlier source-linked compositions remain available as
    # evidence, because their citation and limitation fields are retained.
    base_rows = [
        row
        for row in rows
        if not row.get("expansion_id", "").startswith("M21B-LITEXP-RECSHARED-")
        and not row.get("expansion_id", "").startswith("M21B-LITEXP-CROSSPROMO-")
    ]

    # Keep one deterministic source row for each receptor-level relay/TF
    # signature. The source row is used only for provenance and citations.
    receptor_signatures: dict[
        str, dict[tuple[str, str], dict[str, str]]
    ] = defaultdict(dict)
    for row in base_rows:
        if row.get("path_expression") not in FULL_PATHS:
            continue
        receptor = row.get("receptor_label", "")
        relay = row.get("intracellular_continuation_node_id", "")
        tf = row.get("transcription_factor_node_id", "")
        if not receptor or not relay or not tf:
            continue
        key = (relay, tf)
        prior = receptor_signatures[receptor].get(key)
        if prior is None or source_rank(row) < source_rank(prior):
            receptor_signatures[receptor][key] = row

    existing_signatures = {
        (
            row.get("ligand_label", ""),
            row.get("receptor_label", ""),
            row.get("intracellular_continuation_node_id", ""),
            row.get("transcription_factor_node_id", ""),
        )
        for row in base_rows
        if row.get("ligand_label")
        and row.get("receptor_label")
        and row.get("intracellular_continuation_node_id")
        and row.get("transcription_factor_node_id")
    }

    candidates: list[tuple[dict[str, str], str, dict[str, str]]] = []
    seen_candidates: set[tuple[str, str, str, str, str, str]] = set()
    for row in base_rows:
        path = row.get("path_expression", "")
        kind = PARTIAL_SPECS.get(path)
        if not kind or row.get("route_status") != "retained_evidence_route":
            continue
        ligand = row.get("ligand_label", "")
        receptor = row.get("receptor_label", "")
        endpoint = row.get("target_gene_label", "") if kind == "target" else row.get("output_label", "")
        if not ligand or not receptor or not endpoint:
            continue
        for (relay, tf), source_row in sorted(receptor_signatures.get(receptor, {}).items()):
            signature = (ligand, receptor, relay, tf)
            if signature in existing_signatures:
                continue
            candidate_key = (row.get("expansion_id", ""), kind, relay, tf, endpoint, path)
            if candidate_key in seen_candidates:
                continue
            seen_candidates.add(candidate_key)
            candidates.append((row, kind, source_row))

    promoted_rows: list[dict[str, str]] = []
    for index, (row, kind, source_row) in enumerate(candidates, start=1):
        relay_id = source_row["intracellular_continuation_node_id"]
        tf_id = source_row["transcription_factor_node_id"]
        final_path = TARGET_FULL if kind == "target" else OUTPUT_FULL
        original_missing = row.get("missing_layers", "")
        source_ligand = source_row.get("ligand_label", "")
        promoted = dict(row)
        promoted.update(
            {
                "expansion_id": f"M21B-LITEXP-RECSHARED-{index:04d}",
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
                "intracellular_status": "receptor_shared_source_supported_composed",
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": relay_id,
                "intracellular_continuation_label": node_labels.get(
                    relay_id, source_row.get("intracellular_continuation_label", "")
                ),
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": tf_id,
                "transcription_factor_label": node_labels.get(
                    tf_id, source_row.get("transcription_factor_label", "")
                ),
                # A TF-to-target edge from a different endpoint is not
                # transferable. Keep this blank even for target-gene routes.
                "tf_target_edge_id": "",
                "source_chain_id": (
                    f"receptor_shared_route:{row.get('expansion_id', '')}:"
                    f"{source_row.get('expansion_id', '')}"
                ),
                "source_evidence_record_id": "",
                "evidence_ids": unique_join(
                    row.get("evidence_ids", ""), source_row.get("evidence_ids", "")
                ),
                "route_linkage_status": unique_join(
                    row.get("route_linkage_status", ""),
                    "receptor_shared_downstream_signature",
                    "cross_record_receptor_signature_composition",
                    "matching_curated_receptor_route_signature",
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
                    f"The receptor-shared relay/TF signature is sourced from the {source_ligand} route at the same receptor; it is not asserted as ligand-specific.",
                ),
                "evidence_summary": unique_join(
                    row.get("evidence_summary", ""),
                    f"A primary-evidence route for {source_ligand} at the same receptor supports the {node_labels.get(relay_id, relay_id)} -> {node_labels.get(tf_id, tf_id)} downstream signature; the ligand-specific endpoint evidence is retained from the source partial route.",
                ),
                "limitations": unique_join(
                    row.get("limitations", ""),
                    f"This is a receptor-shared composition: the downstream relay/TF signature was observed with {source_ligand}, not necessarily with {row.get('ligand_label', '')}. The ligand-specific receptor-to-relay, relay-to-TF, and endpoint handoffs remain unasserted; receptor sharing does not guarantee identical cell-context signaling. No causal traversal or confidence score is asserted.",
                ),
                "context_scope": unique_join(
                    row.get("context_scope", ""),
                    "receptor-shared downstream signature composition; retain ligand and source model boundaries",
                ),
                "primary_locator": unique_join(
                    row.get("primary_locator", ""), source_row.get("primary_locator", "")
                ),
                "source_scope": "receptor_shared_composite_primary_evidence",
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
