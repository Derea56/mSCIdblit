#!/usr/bin/env python3
"""Build primary-literature route overlays for three signaling gaps."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "IL34-CSF1R-JNK-AP1-CFOS",
        "lr_edge_id": "M21B-E000121",
        "relay_node_id": "NODE06801",
        "tf_node_id": "NODE00609",
        "target_node_id": "NODE02087",
        "primary_locator": "PMID:33800170",
        "pathway_name": "IL34-CSF1R-JNK-cJUN-AP1-CFOS",
        "route_linkage_status": (
            "manual_primary_il34_csf1r_jnk_ap1_cfos_route;graph_linked_route_source;"
            "primary_layers_source_linked;receptor_to_intracellular_edge_not_asserted;"
            "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;"
            "end_to_end_chain_not_asserted_by_single_source;evidence_route_only"
        ),
        "evidence_summary": (
            "A primary mouse JB6 epidermal-cell and human MCF7-cell study reports that IL-34 activates CSF1R, "
            "increases JNK1/2 and c-Jun phosphorylation, and increases c-Fos and c-Jun promoter activity with AP-1 "
            "transactivation. The route retains this distinct JNK/AP-1 branch alongside the existing IL-34 ERK/Elk-1 evidence."
        ),
        "limitations": (
            "The source uses transformed epithelial and breast-cancer cell models and reports pathway activation and "
            "promoter activity rather than a single purified receptor-to-target experiment. The graph handoffs remain "
            "unasserted and no SCI transfer is inferred."
        ),
        "species_context": "mouse and human",
        "cell_type_context": "mouse JB6 C141 epidermal cells and human MCF7 breast-cancer cells",
        "assay_or_perturbation": "IL-34 stimulation; CSF1R dependence; MEK/ERK and JNK/c-Jun phosphorylation; c-Fos and c-Jun promoter assays; AP-1 transactivation",
        "source_chain_id": "manual_primary_il34_csf1r_jnk_ap1_cfos",
    },
    {
        "name": "IL9-IL9R-JAK-STAT5-BCL3",
        "lr_edge_id": "M21B-E000325",
        "relay_node_id": "NODE06024",
        "tf_node_id": "NODE10752",
        "target_node_id": "NODE01167",
        "primary_locator": "PMID:10361130; PMID:10919676; PMID:16763206",
        "pathway_name": "IL9-IL9R-JAK1JAK3-STAT5-BCL3",
        "route_linkage_status": (
            "manual_primary_il9_il9r_jak_stat5_bcl3_route;graph_linked_route_source;"
            "primary_layers_source_linked;receptor_to_intracellular_edge_not_asserted;"
            "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;"
            "end_to_end_chain_not_asserted_by_single_source;evidence_route_only"
        ),
        "evidence_summary": (
            "A primary T-cell and mast-cell study reports IL-9-dependent transcriptional upregulation of BCL3 and "
            "attributes the response to Jak/STAT signaling. Complementary primary studies link IL-9 receptor signaling "
            "to JAK3/STAT activation and show IL-9-dependent STAT5 activation associated with PIM1 expression, supporting "
            "the retained JAK1/JAK3-to-STAT5 intermediate context."
        ),
        "limitations": (
            "The route composes complementary immune-cell and lymphoma-model studies, and the cited experiments do not "
            "establish every receptor-to-JAK, JAK-to-STAT5, and STAT5-to-BCL3 handoff in one system. No causal graph edge "
            "or SCI transfer is inferred."
        ),
        "species_context": "human and mouse",
        "cell_type_context": "primary T-cell and mast-cell systems, IL-9-dependent lymphoid cells, and ALK-positive lymphoma models",
        "assay_or_perturbation": "IL-9 stimulation; BCL3 transcription; Jak/STAT dependence; IL-9 receptor blockade; JAK3 and STAT5 activation; PIM1 expression",
        "source_chain_id": "manual_primary_il9_il9r_jak_stat5_bcl3",
    },
    {
        "name": "PDGFB-PDGFRB-PLCG1-ELK1-CFOS",
        "lr_edge_id": "M21B-E000182",
        "relay_node_id": "NODE09092",
        "tf_node_id": "NODE03164",
        "target_node_id": "NODE02087",
        "primary_locator": "PMID:21285289; PMID:1310326; PMID:9299466",
        "pathway_name": "PDGFB-PDGFRB-PLCG1-ERK-Elk1-CFOS",
        "route_linkage_status": (
            "manual_primary_pdgfb_pdgfrb_plcg1_elk1_cfos_route;graph_linked_route_source;"
            "primary_layers_source_linked;receptor_to_intracellular_edge_not_asserted;"
            "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;"
            "end_to_end_chain_not_asserted_by_single_source;evidence_route_only"
        ),
        "evidence_summary": (
            "A primary human vascular-smooth-muscle study reports PDGF-BB-induced PLCgamma1-dependent ERK1/2 and "
            "Elk-1 activation together with c-fos induction. A primary receptor-promoter study shows PDGF-BB activation "
            "of the c-fos promoter through PDGF receptor-mediated signaling, and a primary osteoblast/stromal-cell study "
            "confirms PDGF-BB activation of ERK1/2."
        ),
        "limitations": (
            "The route composes primary vascular-smooth-muscle, fibroblast, and osteoblast/stromal-cell evidence. PLCgamma1, "
            "ERK1/2, Elk-1, and c-fos were not all measured as one uninterrupted chain in one source; missing graph handoffs "
            "remain explicit and no SCI transfer is inferred."
        ),
        "species_context": "human, rat, and mouse",
        "cell_type_context": "human vascular smooth-muscle cells, BALB/c-3T3 fibroblasts, and primary osteoblast/bone-marrow stromal cells",
        "assay_or_perturbation": "PDGF-BB stimulation; PLCgamma1 perturbation; ERK1/2 phosphorylation; Elk-1 phosphorylation; c-fos promoter and expression assays",
        "source_chain_id": "manual_primary_pdgfb_pdgfrb_plcg1_elk1_cfos",
    },
)


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
    rows: list[dict[str, str]] = []
    for spec in SPECS:
        lr = edges[spec["lr_edge_id"]]
        ligand = nodes[lr["source_node_id"]]
        receptor = nodes[lr["target_node_id"]]
        relay = nodes[spec["relay_node_id"]]
        tf = nodes[spec["tf_node_id"]]
        target = nodes[spec["target_node_id"]]
        rows.append(
            {
                "expansion_id": f"M21B-LITEXP-NEXT-{spec['name']}-001",
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
                "intracellular_status": "source_supported_composed",
                "ligand_node_id": lr["source_node_id"],
                "ligand_label": ligand["canonical_label"],
                "ligand_receptor_edge_id": spec["lr_edge_id"],
                "receptor_node_id": lr["target_node_id"],
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": spec["relay_node_id"],
                "intracellular_continuation_label": relay["canonical_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": spec["tf_node_id"],
                "transcription_factor_label": tf["canonical_label"],
                "tf_target_edge_id": "",
                "target_gene_node_id": spec["target_node_id"],
                "target_gene_label": target["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": "",
                "output_label": f"{target['canonical_label']} gene expression",
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": spec["pathway_name"],
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": unique_join(lr.get("evidence_ids", ""), spec["primary_locator"]),
                "source_chain_id": spec["source_chain_id"],
                "source_evidence_record_id": "",
                "route_linkage_status": spec["route_linkage_status"],
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression",
                "primary_locator": spec["primary_locator"],
                "citation_note": (
                    f"Primary-evidence route overlay for {spec['name']}. Unresolved handoffs and model limitations "
                    "remain explicit; no graph edge, causal assertion, or confidence score is created."
                ),
                "evidence_summary": spec["evidence_summary"],
                "limitations": spec["limitations"],
                "curation_status": "curated_primary_route",
                "species_context": spec["species_context"],
                "cell_type_context": spec["cell_type_context"],
                "compartment_context": "extracellular ligand; plasma-membrane receptor; intracellular signaling; nuclear gene-expression context",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary evidence; route layers retain source-specific models",
                "assay_or_perturbation": spec["assay_or_perturbation"],
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
    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
