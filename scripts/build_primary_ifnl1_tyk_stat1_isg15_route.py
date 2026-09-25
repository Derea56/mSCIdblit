#!/usr/bin/env python3
"""Build a primary-evidence IFN-lambda1/ISGF3/ISG15 route overlay."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


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


def make_row(bundle: Path) -> dict[str, str]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    lr = edges["M21B-E008849"]
    relay_edge = edges["M21B-E000062"]
    target_edge = edges["M21B-E008209"]
    required_nodes = {"NODE04987", "NODE05018", "NODE11528", "NODE05712", "NODE05709"}
    missing = sorted(required_nodes - nodes.keys())
    if missing:
        raise ValueError(f"IFN-lambda1 route requires missing nodes: {missing}")
    if lr["source_node_id"] != "NODE04987" or lr["target_node_id"] != "NODE05018":
        raise ValueError("Unexpected IFN-lambda1 ligand-receptor endpoints")
    if relay_edge["target_node_id"] != "NODE11528" or target_edge["source_node_id"] != "NODE05712":
        raise ValueError("Unexpected type-III interferon relay or target edge")

    expansion_id = "M21B-LITEXP-IFNL1-ISGF3-ISG15-001"
    locators = "PMID:34706932; PMCID:PMC8612983; DOI:10.4049/jimmunol.2100339"
    return {
        "expansion_id": expansion_id,
        "source_queue_id": "",
        "route_status": "retained_evidence_route",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge",
        "intracellular_status": "source_supported_composed",
        "ligand_node_id": "NODE04987",
        "ligand_label": nodes["NODE04987"]["canonical_label"],
        "ligand_receptor_edge_id": lr["edge_id"],
        "receptor_node_id": "NODE05018",
        "receptor_label": nodes["NODE05018"]["canonical_label"],
        "receptor_intracellular_edge_id": "",
        "intracellular_continuation_node_id": "NODE11528",
        "intracellular_continuation_label": nodes["NODE11528"]["canonical_label"],
        "intracellular_tf_edge_id": "",
        "transcription_factor_node_id": "NODE05712",
        "transcription_factor_label": nodes["NODE05712"]["canonical_label"],
        "tf_target_edge_id": target_edge["edge_id"],
        "target_gene_node_id": "NODE05709",
        "target_gene_label": nodes["NODE05709"]["canonical_label"],
        "target_output_form_id": "",
        "output_node_id": "NODE05709",
        "output_label": "ISG15 gene expression",
        "output_form_id": "",
        "bridge_id": "",
        "pathway_name": "IFNL1-IFNLR1-IL10RB-TYK2-STAT1-STAT2-IRF9-ISG15",
        "input_evidence_type": "primary_literature_route_expansion",
        "output_evidence_type": "primary_target_gene_expression",
        "evidence_ids": unique_join(lr.get("evidence_ids", ""), relay_edge.get("evidence_ids", ""), target_edge.get("evidence_ids", ""), locators),
        "source_chain_id": expansion_id,
        "source_evidence_record_id": "",
        "route_linkage_status": (
            "manual_primary_ifnl1_isgf3_isg15_route;graph_linked_route_source;primary_layer_linked;"
            "receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;"
            "tf_to_target_edge_asserted_as_graph_evidence;evidence_route_only"
        ),
        "causal_status": "not_asserted",
        "traversal_status": "evidence_route_not_causal",
        "evidence_contract_version": "mechanism_evidence_v1",
        "evidence_polarity": "supports",
        "negative_evidence_status": "not_evaluated",
        "evidence_directness": "composite_primary_route",
        "output_class": "gene_expression_or_transcription",
        "primary_locator": locators,
        "citation_note": "The primary study directly tests IFN-lambda1 responses in human B cells, including IFNLR1-dependent signaling, STAT1 phosphorylation, and ISG15 induction; shared type-III interferon relay and ISGF3 target layers are retained as bounded evidence components.",
        "evidence_summary": "A primary human B-cell study reports IFN-lambda1-induced STAT1 phosphorylation and induction of ISG15 and other interferon-stimulated genes, with IFNLR1 neutralization supporting type-III interferon receptor specificity. The route joins that ligand-specific evidence to the exported TYK2-dependent STAT and ISGF3/ISG15 layers.",
        "limitations": "The primary study uses human B-cell subsets and TLR/BCR co-stimulation contexts; it does not establish a single exported IFNLR1-to-TYK2-to-ISGF3 chain or direct ISGF3 occupancy at the ISG15 locus for every condition. No SCI transfer, causal graph edge, traversal permission, or confidence score is inferred.",
        "curation_status": "curated_primary_route",
        "species_context": "human",
        "cell_type_context": "primary human B-cell subsets from healthy donors and systemic-lupus-erythematosus samples",
        "compartment_context": "extracellular IFN-lambda1; plasma-membrane IFNLR1/IL10RB receptor system; cytoplasmic JAK/STAT relay; nuclear ISGF3 and ISG15 regulation",
        "injury_context": "no SCI transfer inferred; antiviral and autoimmune comparator context only",
        "context_scope": "composite primary evidence; ligand-specific and shared type-III interferon layers bounded",
        "assay_or_perturbation": "IFN-lambda1 stimulation; IFNLR1 neutralization; STAT1 phosphorylation flow cytometry; ISG15 mRNA expression; human B-cell activation and differentiation assays",
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
    print(json.dumps({"rows": 1, "output": str(args.output.resolve())}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
