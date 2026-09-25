#!/usr/bin/env python3
"""Fill endpoint-specific route records from receptor-shared downstream routes.

The source partial record contributes the ligand, receptor, and endpoint. A
curated full route at the same receptor contributes the intracellular relay and
TF signature. The resulting record is evidence-only and keeps all handoffs
unasserted so mSCS can distinguish it from a ligand-specific chain.
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


def eligible_full_source(row: dict[str, str]) -> bool:
    """Exclude broad promotion overlays from the receptor signature index."""
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
        "CROSS",
    )
    return not any(marker in expansion_id for marker in generated_markers)


def merge_endpoint_rows(rows: list[dict[str, str]]) -> dict[str, str]:
    """Retain a deterministic representative while preserving evidence locators."""
    representative = min(rows, key=source_rank)
    merged = dict(representative)
    for field in (
        "evidence_ids",
        "primary_locator",
        "citation_note",
        "evidence_summary",
        "limitations",
        "route_linkage_status",
        "context_scope",
    ):
        merged[field] = unique_join(*(row.get(field, "") for row in rows))
    return merged


def build_rows(bundle: Path) -> list[dict[str, str]]:
    rows = read_tsv(bundle / "mechanism_literature_expansion.tsv")
    node_labels = {
        row["node_id"]: row["canonical_label"]
        for row in read_tsv(bundle / "mechanism_nodes.tsv")
    }

    overlay_prefixes = (
        "M21B-LITEXP-RECSHARED-",
        "M21B-LITEXP-COMPONENTSHARED-",
        "M21B-LITEXP-RECENDPOINT-",
    )
    source_rows = [
        row for row in rows if not row.get("expansion_id", "").startswith(overlay_prefixes)
    ]

    # One representative full route per receptor-level relay/TF signature.
    receptor_signatures: dict[
        str, dict[tuple[str, str], dict[str, str]]
    ] = defaultdict(dict)
    for row in source_rows:
        if row.get("path_expression") not in FULL_PATHS:
            continue
        if not eligible_full_source(row):
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

    # Aggregate endpoint evidence before composition so repeated source-linked
    # rows do not create duplicate route records or discard their locators.
    endpoint_groups: dict[tuple[str, str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in source_rows:
        path = row.get("path_expression", "")
        kind = PARTIAL_SPECS.get(path)
        if not kind or row.get("route_status") != "retained_evidence_route":
            continue
        ligand = row.get("ligand_label", "")
        receptor = row.get("receptor_label", "")
        endpoint = row.get("target_gene_label", "") if kind == "target" else row.get("output_label", "")
        if ligand and receptor and endpoint:
            endpoint_groups[(ligand, receptor, endpoint, path)].append(row)

    # Do not duplicate a route that already has this exact endpoint and
    # relay/TF signature, including signatures added by prior overlays.
    existing_endpoint_signatures = {
        (
            row.get("ligand_label", ""),
            row.get("receptor_label", ""),
            row.get("target_gene_label", "") or row.get("output_label", ""),
            row.get("path_expression", ""),
            row.get("intracellular_continuation_node_id", ""),
            row.get("transcription_factor_node_id", ""),
        )
        for row in rows
        if row.get("path_expression") in FULL_PATHS
    }

    candidates: list[tuple[dict[str, str], str, dict[str, str]]] = []
    for (ligand, receptor, endpoint, partial_path), partial_rows in sorted(endpoint_groups.items()):
        kind = PARTIAL_SPECS[partial_path]
        endpoint_row = merge_endpoint_rows(partial_rows)
        for (relay, tf), source_row in sorted(receptor_signatures.get(receptor, {}).items()):
            full_path = TARGET_FULL if kind == "target" else OUTPUT_FULL
            key = (ligand, receptor, endpoint, full_path, relay, tf)
            if key not in existing_endpoint_signatures:
                candidates.append((endpoint_row, kind, source_row))

    promoted_rows: list[dict[str, str]] = []
    for index, (row, kind, source_row) in enumerate(candidates, start=1):
        relay_id = source_row["intracellular_continuation_node_id"]
        tf_id = source_row["transcription_factor_node_id"]
        full_path = TARGET_FULL if kind == "target" else OUTPUT_FULL
        source_ligand = source_row.get("ligand_label", "")
        same_ligand = source_ligand == row.get("ligand_label", "")
        source_relation = (
            "same_ligand_receptor_downstream_signature"
            if same_ligand
            else "receptor_shared_downstream_signature"
        )
        promoted = dict(row)
        promoted.update(
            {
                "expansion_id": f"M21B-LITEXP-RECENDPOINT-{index:05d}",
                "source_queue_id": "",
                "path_expression": full_path,
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
                "intracellular_status": "receptor_shared_endpoint_source_supported_composed",
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
                # A TF-target edge from a different endpoint is not
                # transferable to this endpoint.
                "tf_target_edge_id": "",
                "source_chain_id": (
                    f"receptor_endpoint_route:{row.get('expansion_id', '')}:"
                    f"{source_row.get('expansion_id', '')}"
                ),
                "source_evidence_record_id": "",
                "evidence_ids": unique_join(
                    row.get("evidence_ids", ""), source_row.get("evidence_ids", "")
                ),
                "route_linkage_status": unique_join(
                    row.get("route_linkage_status", ""),
                    source_relation,
                    "cross_record_receptor_endpoint_signature_composition",
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
                    f"The receptor-level {node_labels.get(relay_id, relay_id)} -> {node_labels.get(tf_id, tf_id)} signature is sourced from the {source_ligand} route at the same receptor; it is not asserted as a complete ligand-specific chain.",
                ),
                "evidence_summary": unique_join(
                    row.get("evidence_summary", ""),
                    f"A primary-evidence route at this receptor supports the {node_labels.get(relay_id, relay_id)} -> {node_labels.get(tf_id, tf_id)} downstream signature; the ligand-specific endpoint evidence is retained from the aggregated partial route sources.",
                ),
                "limitations": unique_join(
                    row.get("limitations", ""),
                    f"This is a receptor-shared endpoint composition: the downstream signature was observed with {source_ligand}, not necessarily with {row.get('ligand_label', '')}. The ligand-specific receptor-to-relay, relay-to-TF, and endpoint handoffs remain unasserted; receptor sharing does not guarantee identical cell-context signaling. No causal traversal or confidence score is asserted.",
                ),
                "context_scope": unique_join(
                    row.get("context_scope", ""),
                    "receptor-shared downstream endpoint composition; retain ligand and source model boundaries",
                ),
                "primary_locator": unique_join(
                    row.get("primary_locator", ""), source_row.get("primary_locator", "")
                ),
                "source_scope": "receptor_shared_endpoint_composite_primary_evidence",
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
