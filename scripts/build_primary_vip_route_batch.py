#!/usr/bin/env python3
"""Build bounded VIP/VPAC2 evidence routes from primary source layers."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


TARGETS = [
    {
        "target_node_id": "NODE08901",
        "target_label": "Per1",
        "output_label": "Per1 expression",
        "locators": "PMID:7733904; PMCID:PMC6358603; DOI:10.1016/S0092-8674(02)00736-5",
        "summary": "Primary evidence supports VIP binding and cAMP activation through VPAC2, VIP/VPAC2-dependent circadian Per1 output, and CRE-mediated transcriptional convergence in the SCN.",
        "context": "Human VPAC2 receptor-expressing cells and mouse suprachiasmatic-nucleus/circadian models, with VIP-induced Per1 output and receptor-loss comparisons.",
        "limitation": "The receptor/cAMP, circadian output, and CREB/CRE transcription observations are source-linked layers from bounded models; the exact GNAS-to-CREB relay and direct CREB occupancy at Per1 remain unasserted, and no SCI transfer is inferred.",
    },
    {
        "target_node_id": "NODE05511",
        "target_label": "IL6 gene",
        "output_label": "IL6 gene expression",
        "locators": "PMID:7733904; PMID:16085472",
        "summary": "Primary evidence supports VIP/VPAC2-associated cAMP signaling and VIP-stimulated IL6 expression through a CREB-linked pathway in osteoblasts.",
        "context": "Recombinant human VPAC2 receptor-expressing cells and mouse calvarial osteoblast cultures stimulated with VIP.",
        "limitation": "The VIP/VPAC2 receptor and cAMP layer is combined with the osteoblast IL6/CREB output study; the exact GNAS-to-CREB relay and direct CREB-to-IL6 promoter handoff remain unasserted, and the osteoblast context is not an SCI receiver-cell assertion.",
    },
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def unique_join(values: list[str]) -> str:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        for item in value.split(";"):
            item = item.strip()
            if item and item not in seen:
                seen.add(item)
                result.append(item)
    return "; ".join(result)


def make_rows(bundle: Path) -> list[dict[str, str]]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    for node_id in ("NODE11764", "NODE11773", "NODE04295", "NODE02446"):
        if node_id not in nodes:
            raise ValueError(f"VIP route requires missing node {node_id}")
    lr_edge = edges["M21B-E001262"]
    receptor_intracellular_edge = edges["M21B-E001896"]
    if (lr_edge["source_node_id"], lr_edge["target_node_id"]) != ("NODE11764", "NODE11773"):
        raise ValueError("VIP/VPAC2 edge endpoints changed")
    if (receptor_intracellular_edge["source_node_id"], receptor_intracellular_edge["target_node_id"]) != ("NODE11773", "NODE04295"):
        raise ValueError("VPAC2/GNAS edge endpoints changed")

    rows: list[dict[str, str]] = []
    for index, target in enumerate(TARGETS, start=1):
        if target["target_node_id"] not in nodes:
            raise ValueError(f"VIP route requires missing target node {target['target_node_id']}")
        expansion_id = f"M21B-LITEXP-VIP-{index:03d}"
        evidence_ids = unique_join(
            [
                "M21B-E001262",
                "M21B-E001896",
                "PMID:7733904",
                target["locators"],
            ]
        )
        rows.append(
            {
                "expansion_id": expansion_id,
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "intracellular_to_tf_edge|tf_to_target_edge",
                "intracellular_status": "source_supported",
                "ligand_node_id": "NODE11764",
                "ligand_label": "VIP/Vasoactive intestinal peptide",
                "ligand_receptor_edge_id": "M21B-E001262",
                "receptor_node_id": "NODE11773",
                "receptor_label": "VIPR2/VPAC2",
                "receptor_intracellular_edge_id": "M21B-E001896",
                "intracellular_continuation_node_id": "NODE04295",
                "intracellular_continuation_label": "GNAS",
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": "NODE02446",
                "transcription_factor_label": "CREB",
                "tf_target_edge_id": "",
                "target_gene_node_id": target["target_node_id"],
                "target_gene_label": target["target_label"],
                "output_node_id": target["target_node_id"],
                "output_label": target["output_label"],
                "pathway_name": f"VIP-VPAC2-GNAS-CREB-{target['target_label']}",
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_vip_transcriptional_output",
                "evidence_ids": evidence_ids,
                "source_chain_id": expansion_id,
                "source_evidence_record_id": "",
                "route_linkage_status": "graph_linked_route_source;manual_primary_vip_route;receptor_proximal_and_tf_output_evidence_composed;intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;evidence_route_only",
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression",
                "primary_locator": target["locators"],
                "citation_note": "Composite primary route annotation: VIP/VPAC2 receptor and cAMP evidence, GNAS coupling, CREB-linked transcription, and target output are retained as separate source-linked layers.",
                "evidence_summary": target["summary"],
                "limitations": target["limitation"],
                "curation_status": "curated_primary_route",
                "species_context": "human; mouse; rat as stated in primary model/assay",
                "cell_type_context": target["context"],
                "compartment_context": "extracellular ligand; plasma membrane; cytoplasm; nucleus; target-gene regulatory locus",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary evidence; route layers retain source-specific models",
                "assay_or_perturbation": "VIP binding and cAMP assays, VPAC2 receptor-loss or receptor-expression comparisons, and target-output transcription assays as described by the cited primary sources.",
                "effect_polarity": "activating",
                "source_scope": "composite_primary_evidence",
            }
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = make_rows(args.bundle.resolve())
    args.output.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
