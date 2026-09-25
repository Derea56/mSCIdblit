#!/usr/bin/env python3
"""Build a norepinephrine/ADRB2/CREB BDNF promoter-IV route overlay."""

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
    ligand_id = "NODE08183"
    receptor_id = "NODE00347"
    relay_id = "NODE04295"
    tf_id = "NODE02454"
    target_id = "NODE01191"
    lr_edge_id = "M21B-E001464"
    relay_edge_id = "M21B-E001833"
    required = [ligand_id, receptor_id, relay_id, tf_id, target_id]
    missing = [node_id for node_id in required if node_id not in nodes]
    if missing:
        raise ValueError(f"Norepinephrine-ADRB2-CREB-BDNF-IV: missing nodes {missing}")
    lr = edges.get(lr_edge_id)
    relay_edge = edges.get(relay_edge_id)
    if not lr or (lr["source_node_id"], lr["target_node_id"]) != (ligand_id, receptor_id):
        raise ValueError("Norepinephrine-ADRB2-CREB-BDNF-IV: ligand-receptor endpoints do not match")
    if not relay_edge or (relay_edge["source_node_id"], relay_edge["target_node_id"]) != (receptor_id, relay_id):
        raise ValueError("Norepinephrine-ADRB2-CREB-BDNF-IV: receptor-relay endpoints do not match")
    expansion_id = "M21B-LITEXP-NOREPIADRB2-CREB-BDNFIV-001"
    locators = "PMID:28983964; PMID:22593004; PMID:17681645; PMID:15056290"
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
        "receptor_intracellular_edge_id": relay_edge_id,
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
        "output_label": "BDNF promoter IV activity and exon IV transcription",
        "output_form_id": "",
        "bridge_id": "",
        "pathway_name": "norepinephrine-ADRB2-GNAS-PKA-CREB-BDNF-promoter-IV",
        "input_evidence_type": "primary_literature_route_expansion",
        "output_evidence_type": "primary_target_gene_expression",
        "evidence_ids": unique_join(lr.get("evidence_ids", ""), relay_edge.get("evidence_ids", ""), locators),
        "source_chain_id": expansion_id,
        "source_evidence_record_id": "",
        "route_linkage_status": (
            "manual_primary_norepinephrine_adrb2_creb_bdnf_promoter_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_graph_linked;"
            "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;"
            "beta2_contribution_not_exclusive;evidence_route_only"
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
            "Primary norepinephrine/adrenergic astrocyte studies support BDNF exon-IV transcription and CREB-associated "
            "promoter regulation; the route retains the graph-linked ADRB2-to-GNAS layer without asserting direct "
            "GNAS-to-CREB or CREB-to-promoter graph edges."
        ),
        "evidence_summary": (
            "Primary cortical-astrocyte studies report norepinephrine-induced BDNF exon-IV transcription and CREB-linked "
            "responses. Separate beta-adrenergic pharmacology supports ADRB2 participation in the norepinephrine/cAMP "
            "response, while related CREB/BDNF promoter studies support the terminal promoter-IV layer. The route keeps "
            "the promoter output distinct from exon-specific transcript rows."
        ),
        "limitations": (
            "The cited studies use related but distinct astrocyte systems and receptor/pharmacologic perturbations; they "
            "do not establish a single ADRB2-to-GNAS-to-CREB-to-BDNF promoter-IV experiment, and ADRB2 is not claimed "
            "to be exclusive. No SCI transfer, causal traversal, or database confidence score is inferred."
        ),
        "curation_status": "curated_primary_route",
        "species_context": "rat; human",
        "cell_type_context": "Cultured rat cortical astrocytes and related adrenergic/BDNF model systems",
        "compartment_context": "extracellular norepinephrine; plasma-membrane ADRB2; GNAS/cAMP intracellular signaling; nuclear CREB-associated BDNF promoter IV",
        "injury_context": "no SCI transfer inferred; primary neural and astrocyte model contexts only",
        "context_scope": "composite_primary_evidence; beta2 contribution not exclusive",
        "assay_or_perturbation": "norepinephrine stimulation; beta- and alpha-adrenergic pharmacology; cAMP/PKA and CREB perturbation; BDNF promoter-IV and exon-IV transcript assays",
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
