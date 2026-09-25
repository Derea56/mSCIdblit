#!/usr/bin/env python3
"""Promote partial primary-evidence routes when a compatible relay is curated.

This creates evidence-layer route annotations only. It does not create graph
edges, causal traversals, or confidence scores. The source bundle already
contains the ligand/receptor/TF/target records; this pass fills a missing
intracellular continuation from an explicitly curated receptor-family relay
policy and retains the handoffs as unasserted evidence composition.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


RELAY_BY_KEY = {
    ("IL21", "STAT3"): "NODE06024",
    ("IL21", "STAT5"): "NODE06024",
    ("IL26", "STAT3"): "NODE06023",
    ("CNTF", "STAT3"): "NODE06016",
    ("IL-6", "STAT3"): "NODE06016",
    ("IL12B/IL23A", "STAT3"): "NODE06026",
    ("IL13", "STAT3"): "NODE06023",
    ("IL20", "STAT3"): "NODE06016",
    ("IL22", "STAT3"): "NODE06016",
    ("IL31", "STAT3"): "NODE06016",
    ("Il11", "STAT3"): "NODE06016",
    ("Il15", "STAT3"): "NODE06024",
    ("Il15", "STAT5"): "NODE06024",
    ("Il2", "STAT3"): "NODE06024",
    ("Il2", "STAT5"): "NODE06024",
    ("Il3", "STAT5"): "NODE06026",
    ("Il5", "STAT5"): "NODE06026",
    ("Il9", "STAT3"): "NODE06024",
    ("Il9", "STAT5"): "NODE06024",
    ("Epo", "STAT5"): "NODE06026",
    ("Thpo", "STAT5"): "NODE06026",
    ("IL4", "STAT6"): "NODE06024",
    ("IFNL3", "STAT1"): "NODE11528",
    ("IFNL4/interferon-lambda-4", "STAT1"): "NODE11528",
    ("IL36A", "NFKB p65/p50 complex"): "NODE07613",
    ("IL36B", "NFKB p65/p50 complex"): "NODE07613",
    ("IL36G", "NFKB p65/p50 complex"): "NODE07613",
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


def build_rows(bundle: Path) -> list[dict[str, str]]:
    rows = read_tsv(bundle / "mechanism_literature_expansion.tsv")
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    output: list[dict[str, str]] = []
    for row in rows:
        if row.get("route_status") != "retained_evidence_route":
            continue
        if row.get("path_expression") != "ligand>receptor>????>TF>target_gene_expression":
            continue
        key = (row.get("ligand_label", ""), row.get("transcription_factor_label", ""))
        relay_id = RELAY_BY_KEY.get(key)
        if not relay_id or not row.get("target_gene_node_id") or not row.get("tf_target_edge_id"):
            continue
        if relay_id not in nodes:
            raise ValueError(f"Missing relay node {relay_id} for {row['expansion_id']}")
        relay = nodes[relay_id]
        index = len(output) + 1
        promoted = dict(row)
        promoted.update(
            {
                "expansion_id": f"M21B-LITEXP-RELAYPROMO-{index:04d}",
                "source_queue_id": "",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
                "intracellular_status": "source_supported_composed",
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": relay_id,
                "intracellular_continuation_label": relay["canonical_label"],
                "intracellular_tf_edge_id": "",
                "source_chain_id": f"M21B-LITEXP-RELAYPROMO-{index:04d}",
                "source_evidence_record_id": "",
                "route_linkage_status": unique_join(
                    row.get("route_linkage_status", ""),
                    "graph_linked_route_source",
                    "graph_linked_ligand_receptor_edge",
                    "matching_curated_relay_layer",
                    "primary_layer_linked",
                    "receptor_to_intracellular_edge_not_asserted",
                    "intracellular_to_tf_edge_not_asserted",
                    "tf_to_target_edge_not_asserted",
                    "end_to_end_chain_not_asserted_by_single_source",
                    "evidence_route_only",
                ),
                "citation_note": (
                    row.get("citation_note", "")
                    + " Relay promotion uses the explicitly curated receptor-family intracellular continuation "
                    + f"{relay['canonical_label']} from the existing graph-linked evidence layer."
                ).strip(),
                "evidence_summary": (
                    row.get("evidence_summary", "")
                    + " The missing intracellular slot is filled as a plausible evidence-layer continuation "
                    + f"through {relay['canonical_label']}; this is a route composition, not a new causal edge."
                ).strip(),
                "limitations": (
                    row.get("limitations", "")
                    + " The receptor-to-relay and relay-to-TF handoffs remain unasserted, and the route is not "
                    + "authorized for causal graph traversal or database confidence scoring."
                ).strip(),
                "context_scope": unique_join(
                    row.get("context_scope", ""),
                    "receptor-family relay composition; preserve source cell and species context",
                ),
                "source_scope": "graph_linked_composite_primary_evidence",
                "curation_status": "curated_primary_route",
            }
        )
        output.append(promoted)
    return output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = build_rows(args.bundle.resolve())
    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    ligands = sorted({row["ligand_label"] for row in rows})
    print(json.dumps({"output": str(args.output.resolve()), "rows": len(rows), "ligands": ligands}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
