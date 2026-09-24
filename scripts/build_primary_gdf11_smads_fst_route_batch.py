#!/usr/bin/env python3
"""Build the source-linked GDF11 -> SMAD2/3 -> FST route annotation."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


LR_EDGE_ID = "M21B-E003235"
INTRACELLULAR_SUPPORT_EDGE_ID = "M22B-E000379"
TF_TARGET_EDGE_ID = "M22B-E000378"
LIGAND_ID = "NODE04029"
RECEPTOR_ID = "NODE00215"
INTRACELLULAR_ID = "NODE10436"
TF_ID = "NODE10455"
TARGET_ID = "NODE03837"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def stable_locators(rows: list[dict[str, str]]) -> str:
    result: list[str] = []
    seen: set[str] = set()
    for row in rows:
        for value in row.get("source_locator", "").split(";"):
            value = value.strip()
            if not value or "?term=" in value or value in seen:
                continue
            seen.add(value)
            result.append(value)
    return "; ".join(result)


def make_row(bundle: Path) -> dict[str, str]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    sources: dict[str, list[dict[str, str]]] = {}
    for row in read_tsv(bundle / "mechanism_edge_sources.tsv"):
        sources.setdefault(row["edge_id"], []).append(row)
    required_nodes = {LIGAND_ID, RECEPTOR_ID, INTRACELLULAR_ID, TF_ID, TARGET_ID}
    required_edges = {LR_EDGE_ID, INTRACELLULAR_SUPPORT_EDGE_ID, TF_TARGET_EDGE_ID}
    if missing := sorted(required_nodes - nodes.keys()):
        raise ValueError(f"GDF11 route requires missing nodes: {missing}")
    if missing := sorted(required_edges - edges.keys()):
        raise ValueError(f"GDF11 route requires missing edges: {missing}")
    if (edges[LR_EDGE_ID]["source_node_id"], edges[LR_EDGE_ID]["target_node_id"]) != (LIGAND_ID, RECEPTOR_ID):
        raise ValueError("Unexpected GDF11 ligand/receptor endpoints")
    if (edges[TF_TARGET_EDGE_ID]["source_node_id"], edges[TF_TARGET_EDGE_ID]["target_node_id"]) != (TF_ID, TARGET_ID):
        raise ValueError("Unexpected GDF11 SMAD2/3/FST endpoints")

    locators = stable_locators(
        sources[LR_EDGE_ID] + sources[INTRACELLULAR_SUPPORT_EDGE_ID] + sources[TF_TARGET_EDGE_ID]
    )
    evidence_ids = "; ".join(
        [
            LR_EDGE_ID,
            edges[LR_EDGE_ID]["evidence_ids"],
            INTRACELLULAR_SUPPORT_EDGE_ID,
            edges[INTRACELLULAR_SUPPORT_EDGE_ID]["evidence_ids"],
            TF_TARGET_EDGE_ID,
            edges[TF_TARGET_EDGE_ID]["evidence_ids"],
            locators,
        ]
    )
    return {
        "expansion_id": "M21B-LITEXP-GDF11-SMAD2-3-FST",
        "source_queue_id": "",
        "route_status": "retained_evidence_route",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge",
        "intracellular_status": "source_supported_composed",
        "ligand_node_id": LIGAND_ID,
        "ligand_label": "GDF11",
        "ligand_receptor_edge_id": LR_EDGE_ID,
        "receptor_node_id": RECEPTOR_ID,
        "receptor_label": nodes[RECEPTOR_ID]["canonical_label"],
        "receptor_intracellular_edge_id": "",
        "intracellular_continuation_node_id": INTRACELLULAR_ID,
        "intracellular_continuation_label": nodes[INTRACELLULAR_ID]["canonical_label"],
        "intracellular_tf_edge_id": "",
        "transcription_factor_node_id": TF_ID,
        "transcription_factor_label": nodes[TF_ID]["canonical_label"],
        "tf_target_edge_id": TF_TARGET_EDGE_ID,
        "target_gene_node_id": TARGET_ID,
        "target_gene_label": nodes[TARGET_ID]["canonical_label"],
        "target_output_form_id": "",
        "output_node_id": TARGET_ID,
        "output_label": "FST gene expression",
        "output_form_id": "",
        "bridge_id": "",
        "pathway_name": "GDF11-ACVR2B-ALK5-SMAD2-3-FST",
        "input_evidence_type": "primary_literature_route_expansion",
        "output_evidence_type": "primary_smads_fst_target_gene_expression",
        "evidence_ids": evidence_ids,
        "source_evidence_record_id": "",
        "route_linkage_status": (
            "graph_linked_route_source;manual_primary_gdf11_smads_route;"
            "direct_gdf11_receptor_edge;smad_program_source_supported;"
            "receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;"
            "tf_to_target_edge_asserted_graph_evidence;evidence_route_only"
        ),
        "causal_status": "not_asserted",
        "traversal_status": "evidence_route_not_causal",
        "evidence_contract_version": "mechanism_evidence_v1",
        "evidence_polarity": "supports",
        "negative_evidence_status": "not_evaluated",
        "evidence_directness": "composite_primary_route",
        "output_class": "gene_expression_or_transcription",
        "primary_locator": locators,
        "citation_note": "Composite primary route annotation. GDF11/ACVR2B:ALK5 binding, a SMAD2/3-associated transcriptional program, and the exported SMAD2/3-to-FST target edge are joined without asserting the missing receptor-to-SMAD or SMAD-program-to-TF handoffs.",
        "evidence_summary": "Primary studies support GDF11 engagement of the ACVR2B/ALK5 receptor complex and SMAD2/3-associated signaling; the graph retains a source-linked SMAD2/3-to-FST target-gene edge. The route is therefore available to mSCS as a layered plausibility route rather than a causal chain.",
        "limitations": "The receptor, intracellular program, TF, and FST observations are complementary and do not establish a single end-to-end experiment in one cell system. Preserve the GDF11 receptor-complex and SMAD2/3 target-gene contexts; no SCI transfer, causal traversal, or confidence score is inferred.",
        "curation_status": "curated_primary_route",
        "species_context": "human; mouse developmental comparator systems as stated in primary studies",
        "cell_type_context": "Receptor-reconstitution and GDF11-responsive systems represented by the source records.",
        "compartment_context": "extracellular GDF11; ACVR2B/ALK5 receptor complex; cytoplasmic SMAD2/3 relay; nuclear FST regulation",
        "injury_context": "no SCI transfer inferred; primary GDF11 signaling contexts only",
        "context_scope": "composite primary evidence; receptor and target-gene boundaries retained",
        "assay_or_perturbation": "receptor-complex structural or binding assays, luciferase signaling, SMAD2/3 pathway readouts, and target-gene promoter or expression evidence",
        "effect_polarity": "activating",
        "source_scope": "composite_primary_evidence",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    row = make_row(args.bundle.resolve())
    args.output.resolve().write_text(json.dumps([row], indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output.resolve()), "rows": 1}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
