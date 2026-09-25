#!/usr/bin/env python3
"""Build a primary-evidence TGFB1/SMAD3/4/SMAD7 feedback route."""

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
    ligand_id = "NODE10998"
    receptor_id = "NODE11016"
    relay_id = "NODE10463"
    tf_id = "NODE10470"
    target_id = "NODE10475"
    lr_edge_id = "M21B-E000335"
    receptor_relay_edge_id = "M21B-E000035"
    feedback_edge_id = "M21B-E008384"
    required = [ligand_id, receptor_id, relay_id, tf_id, target_id]
    missing = [node_id for node_id in required if node_id not in nodes]
    if missing:
        raise ValueError(f"TGFB1-SMAD7-feedback: missing nodes {missing}")
    lr = edges.get(lr_edge_id)
    relay_edge = edges.get(receptor_relay_edge_id)
    feedback_edge = edges.get(feedback_edge_id)
    if not lr or (lr["source_node_id"], lr["target_node_id"]) != (ligand_id, receptor_id):
        raise ValueError("TGFB1-SMAD7-feedback: ligand-receptor endpoints do not match")
    if not relay_edge or (relay_edge["source_node_id"], relay_edge["target_node_id"]) != (receptor_id, relay_id):
        raise ValueError("TGFB1-SMAD7-feedback: receptor-relay endpoints do not match")
    if not feedback_edge or (feedback_edge["source_node_id"], feedback_edge["target_node_id"]) != ("NODE10467", target_id):
        raise ValueError("TGFB1-SMAD7-feedback: feedback evidence edge endpoints do not match")
    expansion_id = "M21B-LITEXP-TGFB1-SMAD3-SMAD4-SMAD7-001"
    locators = "PMID:20207738; PMCID:PMC1170167; PMID:9311995; PMID:10559222; PMCID:PMC18614; DOI:10.1074/jbc.274.47.33412"
    return {
        "expansion_id": expansion_id,
        "source_queue_id": "",
        "route_status": "retained_evidence_route",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "intracellular_to_tf_edge|tf_to_target_edge",
        "intracellular_status": "source_supported_composed",
        "ligand_node_id": ligand_id,
        "ligand_label": nodes[ligand_id]["canonical_label"],
        "ligand_receptor_edge_id": lr_edge_id,
        "receptor_node_id": receptor_id,
        "receptor_label": nodes[receptor_id]["canonical_label"],
        "receptor_intracellular_edge_id": receptor_relay_edge_id,
        "intracellular_continuation_node_id": relay_id,
        "intracellular_continuation_label": nodes[relay_id]["canonical_label"],
        "intracellular_tf_edge_id": "",
        "transcription_factor_node_id": tf_id,
        "transcription_factor_label": nodes[tf_id]["canonical_label"],
        "tf_target_edge_id": "",
        "target_gene_node_id": target_id,
        "target_gene_label": nodes[target_id]["canonical_label"],
        "target_output_form_id": "",
        "output_node_id": target_id,
        "output_label": "SMAD7 gene transcription and inhibitory-feedback induction",
        "output_form_id": "",
        "bridge_id": "",
        "pathway_name": "TGFB1-TGFBR-SMAD3-SMAD4-SMAD7-negative-feedback",
        "input_evidence_type": "primary_literature_route_expansion",
        "output_evidence_type": "primary_target_gene_expression",
        "evidence_ids": unique_join(lr.get("evidence_ids", ""), relay_edge.get("evidence_ids", ""), feedback_edge.get("evidence_ids", ""), locators),
        "source_chain_id": expansion_id,
        "source_evidence_record_id": "",
        "route_linkage_status": (
            "manual_primary_tgfb1_smad7_feedback_route;graph_linked_route_source;primary_layer_linked;"
            "receptor_to_intracellular_edge_graph_linked;intracellular_to_tf_edge_not_asserted;"
            "tf_to_target_edge_not_asserted;smad3_smad4_complex_target_edge_source_linked;evidence_route_only"
        ),
        "causal_status": "not_asserted",
        "traversal_status": "evidence_route_not_causal",
        "evidence_contract_version": "mechanism_evidence_v1",
        "evidence_polarity": "supports",
        "negative_evidence_status": "not_evaluated",
        "evidence_directness": "composite_primary_route",
        "output_class": "target_gene_expression",
        "primary_locator": locators,
        "citation_note": (
            "Primary receptor/SMAD studies support TGFB1-induced SMAD2/3 phosphorylation, SMAD3/4 association, and nuclear "
            "signaling; PMID:10559222 directly reports SMAD3/4 binding and activation of the SMAD7 promoter."
        ),
        "evidence_summary": (
            "Primary studies support TGFB1 engagement of the TGFBR1/TGFBR2 complex, receptor-dependent SMAD3 signaling and "
            "SMAD3/4 nuclear association, and SMAD3/4 binding to and activating the SMAD7 promoter. The route captures "
            "the canonical inhibitory-feedback target while preserving the SMAD3-to-SMAD3/4 composition as evidence rather "
            "than a newly asserted graph edge."
        ),
        "limitations": (
            "The receptor, SMAD activation, and SMAD7 promoter experiments use complementary receptor-reconstitution, "
            "mink, human, HepG2, and HEK293 systems. They do not establish a single uninterrupted TGFB1-to-SMAD7 experiment "
            "in an SCI receiver cell, and the route does not infer SMAD7 protein abundance, feedback kinetics, causal traversal, "
            "or a database confidence score."
        ),
        "curation_status": "curated_primary_route",
        "species_context": "human; mink; mouse comparator systems",
        "cell_type_context": "Human HepG2 and HEK293 cells, receptor-reconstitution systems, and mink TGF-beta reporter models",
        "compartment_context": "extracellular TGFB1; plasma-membrane TGFBR complex; cytoplasmic SMAD3; nuclear SMAD3/4 and SMAD7 promoter",
        "injury_context": "no SCI transfer inferred; primary receptor, reporter, and hepatic/epithelial model contexts only",
        "context_scope": "composite_primary_evidence",
        "assay_or_perturbation": "TGFB1 stimulation; receptor-SMAD phosphorylation and association; SMAD3/4 expression or perturbation; SMAD7 promoter reporter, EMSA, SBE mutagenesis, and transcription assays",
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
    print(json.dumps({"rows": 1, "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
