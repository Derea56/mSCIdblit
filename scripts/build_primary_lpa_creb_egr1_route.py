#!/usr/bin/env python3
"""Build the primary-literature LPA1-ERK-CREB-EGR1 route overlay."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def unique_join(*values: str) -> str:
    out: list[str] = []
    seen: set[str] = set()
    for value in values:
        for item in value.split(";"):
            item = item.strip()
            if item and item not in seen:
                seen.add(item)
                out.append(item)
    return "; ".join(out)


def make_row(bundle: Path) -> dict[str, str]:
    ligand_id = "NODE06482"
    receptor_id = "NODE06486"
    relay_id = "NODE06483"
    tf_id = "NODE02446"
    target_id = "NODE03139"
    lr_edge_id = "M21B-E001512"
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    required = [ligand_id, receptor_id, relay_id, tf_id, target_id]
    missing = [node_id for node_id in required if node_id not in nodes]
    if missing:
        raise ValueError(f"LPA-LPAR1-CREB-EGR1: missing nodes {missing}")
    lr = edges.get(lr_edge_id)
    if not lr or (lr["source_node_id"], lr["target_node_id"]) != (ligand_id, receptor_id):
        raise ValueError("LPA-LPAR1-CREB-EGR1: ligand-receptor edge endpoints do not match")
    expansion_id = "M21B-LITEXP-LPA-LPAR1-ERK-CREB-EGR1"
    return {
        "expansion_id": expansion_id,
        "source_queue_id": "",
        "route_status": "retained_evidence_route",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "intracellular_status": "source_supported_ligand_level",
        "ligand_node_id": ligand_id,
        "ligand_label": "LPA",
        "ligand_receptor_edge_id": lr_edge_id,
        "receptor_node_id": receptor_id,
        "receptor_label": "LPAR1/EDG2",
        "receptor_intracellular_edge_id": "",
        "intracellular_continuation_node_id": relay_id,
        "intracellular_continuation_label": "LPA-evoked ERK1/2 phosphorylation",
        "intracellular_tf_edge_id": "",
        "transcription_factor_node_id": tf_id,
        "transcription_factor_label": "CREB",
        "tf_target_edge_id": "",
        "target_gene_node_id": target_id,
        "target_gene_label": "EGR1 promoter",
        "output_node_id": target_id,
        "output_label": "EGR1 expression after LPA stimulation",
        "pathway_name": "LPA-LPAR1-PKCdelta-ERK/JNK-CREB-EGR1",
        "input_evidence_type": "primary_literature_route_expansion",
        "output_evidence_type": "primary_target_gene_expression",
        "evidence_ids": unique_join(
            lr.get("evidence_ids", ""),
            "PMID:16497989; PMID:22577133; DOI:10.1161/01.ATV.0000214980.90567.b5; DOI:10.1074/jbc.M112.363218",
        ),
        "source_chain_id": expansion_id,
        "source_evidence_record_id": "",
        "route_linkage_status": (
            "graph_linked_route_source;manual_primary_lpa_lpar1_erk_creb_egr1_route;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;evidence_route_only"
        ),
        "causal_status": "not_asserted",
        "traversal_status": "evidence_route_not_causal",
        "evidence_contract_version": "mechanism_evidence_v1",
        "evidence_polarity": "supports",
        "negative_evidence_status": "not_evaluated",
        "evidence_directness": "composite_primary_route",
        "output_class": "target_gene_expression",
        "primary_locator": "PMID:16497989; PMID:22577133; DOI:10.1161/01.ATV.0000214980.90567.b5; DOI:10.1074/jbc.M112.363218",
        "citation_note": (
            "PMID:16497989 directly reports LPA-induced CREB and SRF binding at the EGR1 promoter and "
            "suppression of maximal EGR1 induction by dominant-negative CREB; PMID:22577133 adds LPA1- and "
            "PKCdelta-dependent ERK/JNK signaling."
        ),
        "evidence_summary": (
            "Primary vascular smooth-muscle studies report LPA1-dependent PKCdelta activation with ERK1/2 "
            "and JNK signaling, LPA-induced CREB phosphorylation and CREB/SRF binding at the EGR1 promoter, "
            "and CREB-dependent EGR1 transcription. The route retains the graph-linked LPA1 receptor and "
            "ERK continuation while leaving the graph handoffs explicit."
        ),
        "limitations": (
            "The supporting studies use rat aortic smooth-muscle cells and complementary assays rather than a "
            "single uninterrupted graph chain. No causal traversal, graph edge, SCI transfer, or confidence "
            "score is inferred."
        ),
        "curation_status": "curated_primary_route",
        "species_context": "rat",
        "cell_type_context": "rat aortic vascular smooth-muscle cells",
        "compartment_context": "extracellular lipid mediator; GPCR; intracellular MAPK relay; nuclear CREB and EGR1 promoter",
        "injury_context": "no SCI transfer inferred; primary vascular smooth-muscle model context only",
        "context_scope": "primary LPA1-specific vascular smooth-muscle evidence with graph-linked receptor and relay context",
        "assay_or_perturbation": "LPA stimulation; LPA1 dependence; PKCdelta, MEK/ERK and JNK perturbation; CREB/SRF DNA binding; EGR1 promoter, RNA and protein assays",
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
