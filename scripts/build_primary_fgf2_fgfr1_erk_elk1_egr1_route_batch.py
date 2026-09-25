#!/usr/bin/env python3
"""Build a primary-literature FGF2/FGFR1/ERK/ELK1/EGR1 route overlay."""

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


def make_rows(bundle: Path) -> list[dict[str, str]]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    lr_edge_id = "M21B-E000203"
    tf_target_edge_id = "M22B-E000158"
    relay_node_id = "NODE03629"
    tf_node_id = "NODE03165"
    target_node_id = "NODE03139"
    lr = edges[lr_edge_id]
    tf_target = edges[tf_target_edge_id]
    ligand = nodes[lr["source_node_id"]]
    receptor = nodes[lr["target_node_id"]]
    relay = nodes[relay_node_id]
    tf = nodes[tf_node_id]
    target = nodes[target_node_id]
    expansion_id = "M21B-LITEXP-FGF2FGFR1ERKELK1-EGR1-001"
    primary_locator = "PMID:10079272; PMID:12242295; PMID:22593802; PMID:26551735"
    evidence_ids = unique_join(
        lr.get("evidence_ids", ""),
        tf_target.get("evidence_ids", ""),
        "PMID:10079272; PMID:12242295; PMID:22593802; PMID:26551735",
    )
    row = {
        "expansion_id": expansion_id,
        "source_queue_id": "",
        "route_status": "retained_evidence_route",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge",
        "intracellular_status": "source_supported_composed",
        "ligand_node_id": lr["source_node_id"],
        "ligand_label": ligand["canonical_label"],
        "ligand_receptor_edge_id": lr_edge_id,
        "receptor_node_id": lr["target_node_id"],
        "receptor_label": receptor["canonical_label"],
        "receptor_intracellular_edge_id": "",
        "intracellular_continuation_node_id": relay_node_id,
        "intracellular_continuation_label": relay["canonical_label"],
        "intracellular_tf_edge_id": "",
        "transcription_factor_node_id": tf_node_id,
        "transcription_factor_label": tf["canonical_label"],
        "tf_target_edge_id": tf_target_edge_id,
        "target_gene_node_id": target_node_id,
        "target_gene_label": target["canonical_label"],
        "target_output_form_id": "",
        "output_node_id": target_node_id,
        "output_label": "EGR1 promoter activity and EGR1 transcription",
        "output_form_id": "",
        "bridge_id": "",
        "pathway_name": "FGF2-FGFR1-MAPK-ERK-ELK1-EGR1",
        "input_evidence_type": "primary_literature_route_expansion",
        "output_evidence_type": "primary_target_gene_expression",
        "evidence_ids": evidence_ids,
        "source_chain_id": expansion_id,
        "source_evidence_record_id": "",
        "route_linkage_status": (
            "manual_primary_fgf2_fgfr1_erk_elk1_egr1_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_graph_linked;"
            "evidence_route_only"
        ),
        "causal_status": "not_asserted",
        "traversal_status": "evidence_route_not_causal",
        "evidence_contract_version": "mechanism_evidence_v1",
        "evidence_polarity": "supports",
        "negative_evidence_status": "not_evaluated",
        "evidence_directness": "composite_primary_route",
        "output_class": "target_gene_expression",
        "primary_locator": primary_locator,
        "citation_note": (
            "Primary-evidence route overlay for FGF2-FGFR1-MAPK/ERK-ELK1-EGR1. Complementary FGF2/MEK/ERK and "
            "ELK1/EGR1 promoter studies are linked without asserting an unobserved causal handoff."
        ),
        "evidence_summary": (
            "Primary FGF2 stimulation studies report paracrine FGF2 activation of an EGR1 promoter through a "
            "MEK/ERK-dependent pathway. Independent primary studies establish ERK-dependent ELK1 recruitment and "
            "activation of the EGR1 promoter, providing a source-linked TF/target layer for the FGF2 route."
        ),
        "limitations": (
            "The FGF2-to-EGR1 study and the ELK1-to-EGR1 promoter study use different experimental systems; the "
            "FGF2 paper does not by itself establish ELK1 as the required TF. Receptor-to-relay and relay-to-TF "
            "handoffs remain unresolved, and no SCI transfer, causal traversal or database confidence score is inferred."
        ),
        "curation_status": "curated_primary_route",
        "species_context": "mouse; human",
        "cell_type_context": "Primary vascular injury and prostate cancer-cell model systems with complementary FGF2/FGFR1 and ELK1/EGR1 studies",
        "compartment_context": "extracellular FGF2; plasma-membrane FGFR1; cytoplasmic and nuclear ERK/MAPK signaling; nuclear ELK1-associated EGR1 promoter output",
        "injury_context": "no SCI transfer inferred; primary model context only",
        "context_scope": "composite_primary_evidence",
        "assay_or_perturbation": "FGF2 stimulation; MEK inhibition; EGR1 promoter reporter and mRNA assays; ELK1 occupancy and perturbation assays",
        "effect_polarity": "activating",
        "source_scope": "composite_primary_evidence",
    }
    return [row]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = make_rows(args.bundle.resolve())
    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
