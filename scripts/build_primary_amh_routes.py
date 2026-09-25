#!/usr/bin/env python3
"""Build the primary AMH receptor-to-output evidence route.

The source study supports AMH/AMHR2-associated SMAD1/5/8 activation and
Fshb/Inhbb expression in gonadotrope models.  It does not establish a named
terminal TF or a direct promoter handoff, so this remains an evidence-layer
route rather than a full causal chain.
"""

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
    ligand_id = "NODE00511"
    receptor_id = "NODE00512"
    relay_id = "NODE10440"
    output_id = "NODE00509"
    lr_edge_id = "M21B-E003273"
    lr_edge = edges.get(lr_edge_id)
    if not lr_edge or (lr_edge["source_node_id"], lr_edge["target_node_id"]) != (ligand_id, receptor_id):
        raise ValueError("AMH ligand-receptor edge endpoints do not match")
    for node_id in (ligand_id, receptor_id, relay_id, output_id):
        if node_id not in nodes:
            raise ValueError(f"AMH route is missing node {node_id}")

    return {
        "expansion_id": "M21B-LITEXP-AMH-AMHR2-SMAD1-5-8-FSHB-INHBB-001",
        "source_queue_id": "",
        "route_status": "retained_evidence_route",
        "path_expression": "ligand>receptor>intracellular>output",
        "route_tier": "ligand_receptor_intracellular_output_missing_tf",
        "known_layers": "ligand|receptor|intracellular_continuation|output",
        "missing_layers": "receptor_to_intracellular_edge|transcription_factor|target_gene_expression",
        "intracellular_status": "source_supported_composed",
        "ligand_node_id": ligand_id,
        "ligand_label": "AMH/anti-Müllerian hormone",
        "ligand_receptor_edge_id": lr_edge_id,
        "receptor_node_id": receptor_id,
        "receptor_label": "AMHR2",
        "receptor_intracellular_edge_id": "",
        "intracellular_continuation_node_id": relay_id,
        "intracellular_continuation_label": "SMAD1/5/8",
        "intracellular_tf_edge_id": "",
        "transcription_factor_node_id": "",
        "transcription_factor_label": "",
        "tf_target_edge_id": "",
        "target_gene_node_id": "",
        "target_gene_label": "",
        "target_output_form_id": "",
        "output_node_id": output_id,
        "output_label": "Fshb and Inhbb expression in gonadotrope cells",
        "output_form_id": "",
        "bridge_id": "",
        "pathway_name": "AMH-AMHR2-SMAD1/5/8-gonadotrope-expression",
        "input_evidence_type": "primary_literature_route_expansion",
        "output_evidence_type": "primary_gene_expression_output",
        "evidence_ids": unique_join(
            lr_edge.get("evidence_ids", ""),
            "M21B-EVID-003755",
            "M22B-EVID-000085",
            "PMID:27030385",
            "PMCID:PMC4815011",
        ),
        "source_chain_id": "M21B-LITEXP-AMH-AMHR2-SMAD1-5-8-FSHB-INHBB-001",
        "source_evidence_record_id": "",
        "route_linkage_status": (
            "graph_linked_route_source;manual_primary_amh_route;primary_layer_linked;"
            "receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;"
            "transcription_factor_not_asserted;target_gene_expression_not_asserted;"
            "end_to_end_chain_not_asserted_by_single_source;evidence_route_only"
        ),
        "causal_status": "not_asserted",
        "traversal_status": "evidence_route_not_causal",
        "evidence_contract_version": "mechanism_evidence_v1",
        "evidence_polarity": "supports",
        "negative_evidence_status": "not_evaluated",
        "evidence_directness": "composite_primary_route",
        "output_class": "gene_expression_or_transcription",
        "primary_locator": "PMID:27030385; PMCID:PMC4815011",
        "citation_note": "The primary AMH study supports AMHR2-associated SMAD1/5/8 activation and Fshb/Inhbb expression; no named terminal TF or direct promoter edge is asserted.",
        "evidence_summary": "In primary rat and LβT2 gonadotrope experiments, mature AMH and AMH precursor recruited the SMAD pathway, increased SMAD1/5/8 phosphorylation, and increased Fshb and Inhbb transcripts. The route retains the graph-linked AMH-AMHR2 input and the existing AMH/SMAD program while representing the measured gene-expression output without inventing a TF handoff.",
        "limitations": "The study is a reproductive-endocrine model rather than an SCI receiver-cell experiment. Type-I receptor usage is not uniquely resolved, the SMAD1/5/8 step is a pathway activation readout rather than a direct target-promoter claim, and no terminal TF or direct AMH-to-promoter edge is asserted; no causal traversal or confidence score is inferred.",
        "curation_status": "curated_primary_route",
        "species_context": "rat; human cell-line comparator",
        "cell_type_context": "rat pituitary and LβT2 gonadotrope cells",
        "compartment_context": "extracellular ligand; plasma-membrane AMHR2 context; intracellular SMAD relay; gene-expression output",
        "injury_context": "no SCI transfer inferred; primary model context only",
        "context_scope": "composite primary evidence with graph-linked ligand-receptor identity",
        "assay_or_perturbation": "AMH or AMH precursor stimulation; AMHR2 expression and pathway assays; phospho-SMAD1/5/8 immunoblotting; Fshb and Inhbb transcript measurements",
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
