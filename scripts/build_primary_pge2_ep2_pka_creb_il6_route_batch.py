#!/usr/bin/env python3
"""Build a primary-literature PGE2/EP2/PKA/CREB/IL6 route overlay."""

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

    ligand_id = "NODE08947"
    receptor_id = "NODE09435"
    relay_id = "NODE09272"
    tf_id = "NODE02446"
    target_id = "NODE05511"
    lr_edge_id = "M21B-E001268"
    required_nodes = [ligand_id, receptor_id, relay_id, tf_id, target_id]
    missing = [node_id for node_id in required_nodes if node_id not in nodes]
    if missing:
        raise ValueError(f"PGE2-EP2-PKA-CREB-IL6: missing nodes {missing}")
    lr = edges.get(lr_edge_id)
    if not lr or (lr["source_node_id"], lr["target_node_id"]) != (ligand_id, receptor_id):
        raise ValueError("PGE2-EP2-PKA-CREB-IL6: ligand-receptor edge endpoints do not match")

    expansion_id = "M21B-LITEXP-PGE2-EP2-PKA-CREB-IL6-001"
    primary_locator = "PMID:21209948; PMID:15855407; PMID:15121014"
    return {
        "expansion_id": expansion_id,
        "source_queue_id": "",
        "route_status": "retained_evidence_route",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "intracellular_status": "source_supported_composed",
        "ligand_node_id": ligand_id,
        "ligand_label": nodes[ligand_id]["canonical_label"],
        "ligand_receptor_edge_id": lr_edge_id,
        "receptor_node_id": receptor_id,
        "receptor_label": nodes[receptor_id]["canonical_label"],
        "receptor_intracellular_edge_id": "",
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
        "output_label": "IL6 gene expression",
        "output_form_id": "",
        "bridge_id": "",
        "pathway_name": "PGE2-EP2-cAMP-PKA-CREB-IL6",
        "input_evidence_type": "primary_literature_route_expansion",
        "output_evidence_type": "primary_target_gene_expression",
        "evidence_ids": unique_join(lr.get("evidence_ids", ""), primary_locator),
        "source_chain_id": expansion_id,
        "source_evidence_record_id": "",
        "route_linkage_status": (
            "manual_primary_pge2_ep2_pka_creb_il6_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;"
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
            "PMID:21209948 reports PGE2-induced IL6 gene expression through EP2/cAMP/PKA and CREB/CBP-dependent "
            "transcriptional regulation in orbital fibroblasts; PMID:15855407 supports EP2-linked CREB phosphorylation; "
            "PMID:15121014 provides complementary EP2/EP4-cAMP-PKA-COX2 transcription evidence."
        ),
        "evidence_summary": (
            "Primary orbital-fibroblast experiments support PGE2-induced IL6 expression, EP2 dependence, cAMP/PKA "
            "involvement, and CREB/CBP-dependent transcription. Independent primary receptor studies support EP2-linked "
            "CREB phosphorylation through PKA. The graph-linked PGE2-to-EP2 edge and existing PKA, CREB, and IL6 nodes "
            "therefore retain a traversable evidence route while keeping unasserted graph handoffs explicit."
        ),
        "limitations": (
            "The cited studies use orbital fibroblast and receptor-expression models rather than an SCI receiver-cell "
            "system. The route is a composed primary-evidence overlay; no new graph edges, causal traversal, SCI transfer, "
            "or database confidence score is inferred. EP2-to-PKA and CREB-to-IL6 promoter handoffs remain source-supported "
            "route evidence rather than asserted mechanism-graph edges."
        ),
        "curation_status": "curated_primary_route",
        "species_context": "human; rat; mouse",
        "cell_type_context": "Human orbital fibroblasts and heterologous EP2/EP4 receptor-expression systems",
        "compartment_context": "extracellular PGE2; plasma-membrane EP2; cytoplasmic cAMP/PKA; nuclear CREB/CBP and IL6 regulatory locus",
        "injury_context": "no SCI transfer inferred; primary receptor and fibroblast model contexts only",
        "context_scope": "composite_primary_evidence",
        "assay_or_perturbation": "PGE2 stimulation; EP2/EP4 subtype pharmacology; cAMP and PKA perturbation; CREB/CBP loss-of-function; IL6 mRNA/promoter assays",
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
