#!/usr/bin/env python3
"""Build a primary-literature TGF-beta2 target-gene route overlay."""

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
    ligand_id = "NODE11008"
    receptor_id = "NODE11016"
    relay_id = "NODE10459"
    tf_id = "NODE10462"
    target_id = "NODE02339"
    lr_edge_id = "M21B-E000341"
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    required = [ligand_id, receptor_id, relay_id, tf_id, target_id]
    missing = [node_id for node_id in required if node_id not in nodes]
    if missing:
        raise ValueError(f"TGFB2-TGFBR-SMAD23-COL1A1: missing nodes {missing}")
    lr = edges.get(lr_edge_id)
    if not lr or (lr["source_node_id"], lr["target_node_id"]) != (ligand_id, receptor_id):
        raise ValueError("TGFB2-TGFBR-SMAD23-COL1A1: ligand-receptor edge endpoints do not match")
    expansion_id = "M21B-LITEXP-TGFB2-TGFBR-SMAD23-COL1A1"
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
        "ligand_label": "Tgfb2",
        "ligand_receptor_edge_id": lr_edge_id,
        "receptor_node_id": receptor_id,
        "receptor_label": "TGFBR1-TGFBR2 receptor complex",
        "receptor_intracellular_edge_id": "",
        "intracellular_continuation_node_id": relay_id,
        "intracellular_continuation_label": "SMAD2/3-SMAD4 heteromeric complex",
        "intracellular_tf_edge_id": "",
        "transcription_factor_node_id": tf_id,
        "transcription_factor_label": "SMAD2;SMAD3",
        "tf_target_edge_id": "",
        "target_gene_node_id": target_id,
        "target_gene_label": "COL1A1 gene",
        "output_node_id": target_id,
        "output_label": "COL1A1/collagen-I expression after TGF-beta2 stimulation",
        "pathway_name": "Tgfb2-TGFBR1/2-SMAD2/3-SMAD4-COL1A1",
        "input_evidence_type": "primary_literature_route_expansion",
        "output_evidence_type": "primary_target_gene_expression",
        "evidence_ids": unique_join(lr.get("evidence_ids", ""), "PMID:24755068; DOI:10.1016/j.bbrc.2014.04.068"),
        "source_chain_id": expansion_id,
        "source_evidence_record_id": "",
        "route_linkage_status": (
            "graph_linked_route_source;manual_primary_tgfb2_smad23_col1a1_route;"
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
        "primary_locator": "PMID:24755068; DOI:10.1016/j.bbrc.2014.04.068",
        "citation_note": (
            "PMID:24755068 reports TGF-beta2-induced collagen-I expression in human lens epithelial cells "
            "and inhibition of the response by SMAD2/3 blockade; the receptor and relay layers are retained "
            "from the graph-linked TGF-beta2 record."
        ),
        "evidence_summary": (
            "A primary human lens-epithelial study reports that TGF-beta2 induces collagen-I/COL1A1 and "
            "other extracellular-matrix outputs, while blockade of SMAD2 and SMAD3 inhibits the response. "
            "The route retains the graph-linked TGFBR1/2 receptor and SMAD2/3-SMAD4 continuation without "
            "asserting every molecular handoff as a graph edge."
        ),
        "limitations": (
            "The study uses human lens epithelial cells and pharmacologic or silencing perturbations; it does "
            "not establish a single uninterrupted receptor-to-promoter chain. No causal traversal, graph edge, "
            "SCI transfer, or confidence score is inferred."
        ),
        "curation_status": "curated_primary_route",
        "species_context": "human",
        "cell_type_context": "human lens epithelial cells",
        "compartment_context": "extracellular ligand; plasma-membrane receptor; receptor-SMAD relay; nuclear transcriptional output",
        "injury_context": "no SCI transfer inferred; primary lens-epithelial model context only",
        "context_scope": "primary ligand-specific epithelial evidence with graph-linked receptor and relay context",
        "assay_or_perturbation": "TGF-beta2 stimulation; SMAD2/3 blockade or silencing; COL1A1/collagen-I and extracellular-matrix expression assays",
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
