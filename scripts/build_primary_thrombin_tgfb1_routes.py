#!/usr/bin/env python3
"""Build primary-literature route overlays for thrombin and TGF-beta1."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "THROMBIN-PAR1-ERK-ELK1-EGR1",
        "ligand_node_id": "NODE11065",
        "ligand_label": "Thrombin",
        "lr_edge_id": "M21B-E001309",
        "receptor_node_id": "NODE03454",
        "receptor_label": "F2R/PAR1",
        "intracellular_node_id": "NODE06776",
        "intracellular_label": "MAPK1/MAPK3",
        "tf_node_id": "NODE03164",
        "tf_label": "Elk-1",
        "target_node_id": "NODE03139",
        "target_label": "EGR1 promoter",
        "output_node_id": "NODE03139",
        "output_label": "EGR1 expression after thrombin stimulation",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "locators": "PMID:19432968; PMID:12393577; DOI:10.1186/1471-2199-10-40; DOI:10.1182/blood-2002-02-0415",
        "pathway_name": "Thrombin-PAR1-ERK1/2-Elk1-EGR1",
        "evidence_summary": (
            "Primary thrombin-stimulation work reports Ca2+- and PKC-dependent ERK activation, Elk-1 "
            "phosphorylation and Elk-1-dependent EGR1 induction in fibroblasts. Independent primary "
            "endothelial-cell work reports thrombin-induced EGR1 transcription and inhibition by MEK/ERK "
            "blockade. The thrombin-PAR1 input is retained from the graph-linked receptor record."
        ),
        "citation_note": (
            "PMID:19432968 directly links thrombin stimulation to ERK, Elk-1 and EGR1 in fibroblasts; "
            "PMID:12393577 provides complementary thrombin-induced EGR1/MEK-ERK evidence in primary "
            "human endothelial cells."
        ),
        "species_context": "human endothelial cells; mouse lung fibroblast model",
        "cell_type_context": "primary human endothelial cells and 39M1-81 lung fibroblasts",
        "assay_or_perturbation": "thrombin stimulation; MEK/ERK inhibition; Elk-1 phosphorylation and dominant-negative Elk-1; EGR1 promoter, RNA and protein assays",
        "route_linkage_status": (
            "graph_linked_route_source;manual_primary_thrombin_par1_erk_elk1_egr1_route;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;evidence_route_only"
        ),
    },
    {
        "name": "TGFB1-TGFBR-ERK-ELK1-EGR1",
        "ligand_node_id": "NODE10998",
        "ligand_label": "Tgfb1",
        "lr_edge_id": "M21B-E000335",
        "receptor_node_id": "NODE11016",
        "receptor_label": "TGFBR1-TGFBR2 receptor complex",
        "intracellular_node_id": "NODE06776",
        "intracellular_label": "MAPK1/MAPK3",
        "tf_node_id": "NODE03164",
        "tf_label": "Elk-1",
        "target_node_id": "NODE03139",
        "target_label": "EGR1 promoter",
        "output_node_id": "NODE03139",
        "output_label": "EGR1 expression after TGF-beta stimulation",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "locators": "PMID:18772333; DOI:10.1007/s00125-008-1121-7",
        "pathway_name": "Tgfb1-TGFBR1/2-ERK1/2-Elk1-EGR1",
        "evidence_summary": (
            "Primary fibroblast work reports TGF-beta-induced EGR1 mRNA and protein, increased EGR1 "
            "transcription through serum-response elements, and enhanced Elk-1 activity through the "
            "MEK-ERK1/2 pathway. The Tgfb1-TGFBR1/2 input is retained from the graph-linked receptor record."
        ),
        "citation_note": "PMID:18772333 reports TGF-beta-induced EGR1 transcription and MEK-ERK1/2-dependent Elk-1 activation in fibroblasts.",
        "species_context": "human",
        "cell_type_context": "normal human fibroblasts and scleroderma fibroblasts",
        "assay_or_perturbation": "TGF-beta stimulation; MEK/ERK inhibition; EGR1 mRNA/protein and promoter/SRE transcription assays; Elk-1 activity assays",
        "route_linkage_status": (
            "graph_linked_route_source;manual_primary_tgfb1_tgfbr_erk_elk1_egr1_route;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;evidence_route_only"
        ),
    },
    {
        "name": "THROMBIN-PAR1-ERK-CXCL8",
        "ligand_node_id": "NODE11065",
        "ligand_label": "Thrombin",
        "lr_edge_id": "M21B-E001309",
        "receptor_node_id": "NODE03454",
        "receptor_label": "F2R/PAR1",
        "intracellular_node_id": "NODE06776",
        "intracellular_label": "MAPK1/MAPK3",
        "tf_node_id": "",
        "tf_label": "",
        "target_node_id": "",
        "target_label": "",
        "output_node_id": "NODE02693",
        "output_label": "CXCL8/IL-8 secretion",
        "path_expression": "ligand>receptor>intracellular>????>output",
        "route_tier": "ligand_receptor_intracellular_output_missing_tf",
        "known_layers": "ligand|receptor|intracellular_continuation|output",
        "missing_layers": "receptor_to_intracellular_edge|transcription_factor|intracellular_to_tf_edge|target_gene_expression",
        "locators": "PMID:16697690; DOI:10.1016/j.biocel.2006.03.016",
        "pathway_name": "Thrombin-PAR1-ERK-CXCL8-output",
        "evidence_summary": (
            "Primary human dermal-fibroblast work reports thrombin-induced CXCL8/IL-8 secretion through "
            "PAR1, with ERK inhibition blocking both ERK1/2 phosphorylation and IL-8 secretion. The study "
            "also reports JAK/STAT3 activation, but does not establish a terminal TF-to-CXCL8 edge, so the "
            "route is retained as a functional-output route."
        ),
        "citation_note": "PMID:16697690 reports PAR1-dependent thrombin-induced IL-8 secretion and ERK-pathway dependence in primary human dermal fibroblasts.",
        "species_context": "human",
        "cell_type_context": "primary human dermal fibroblasts",
        "assay_or_perturbation": "thrombin stimulation; PAR1 blockade; MEK/ERK and p38 inhibition; CXCL8/IL-8 secretion assays",
        "route_linkage_status": (
            "graph_linked_route_source;manual_primary_thrombin_par1_erk_cxcl8_output_route;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "transcription_factor_unresolved;target_gene_expression_unresolved;evidence_route_only"
        ),
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
        required = [spec["ligand_node_id"], spec["receptor_node_id"], spec["intracellular_node_id"], spec["output_node_id"]]
        if spec["tf_node_id"]:
            required.append(spec["tf_node_id"])
        if spec["target_node_id"]:
            required.append(spec["target_node_id"])
        missing = [node_id for node_id in required if node_id not in nodes]
        if missing:
            raise ValueError(f"{spec['name']}: missing nodes {missing}")
        lr = edges.get(spec["lr_edge_id"])
        if not lr or (lr["source_node_id"], lr["target_node_id"]) != (spec["ligand_node_id"], spec["receptor_node_id"]):
            raise ValueError(f"{spec['name']}: ligand-receptor edge endpoints do not match")
        expansion_id = f"M21B-LITEXP-{spec['name']}"
        rows.append({
            "expansion_id": expansion_id,
            "source_queue_id": "",
            "route_status": "retained_evidence_route",
            "path_expression": spec["path_expression"],
            "route_tier": spec["route_tier"],
            "known_layers": spec["known_layers"],
            "missing_layers": spec["missing_layers"],
            "intracellular_status": "source_supported_ligand_level",
            "ligand_node_id": spec["ligand_node_id"],
            "ligand_label": spec["ligand_label"],
            "ligand_receptor_edge_id": spec["lr_edge_id"],
            "receptor_node_id": spec["receptor_node_id"],
            "receptor_label": spec["receptor_label"],
            "receptor_intracellular_edge_id": "",
            "intracellular_continuation_node_id": spec["intracellular_node_id"],
            "intracellular_continuation_label": spec["intracellular_label"],
            "intracellular_tf_edge_id": "",
            "transcription_factor_node_id": spec["tf_node_id"],
            "transcription_factor_label": spec["tf_label"],
            "tf_target_edge_id": "",
            "target_gene_node_id": spec["target_node_id"],
            "target_gene_label": spec["target_label"],
            "output_node_id": spec["output_node_id"],
            "output_label": spec["output_label"],
            "pathway_name": spec["pathway_name"],
            "input_evidence_type": "primary_literature_route_expansion",
            "output_evidence_type": "primary_target_gene_expression" if spec["target_node_id"] else "primary_functional_output",
            "evidence_ids": unique_join(lr.get("evidence_ids", ""), spec["locators"]),
            "source_chain_id": expansion_id,
            "source_evidence_record_id": "",
            "route_linkage_status": spec["route_linkage_status"],
            "causal_status": "not_asserted",
            "traversal_status": "evidence_route_not_causal",
            "evidence_contract_version": "mechanism_evidence_v1",
            "evidence_polarity": "supports",
            "negative_evidence_status": "not_evaluated",
            "evidence_directness": "composite_primary_route",
            "output_class": "target_gene_expression" if spec["target_node_id"] else "generic_functional_readout",
            "primary_locator": spec["locators"],
            "citation_note": spec["citation_note"],
            "evidence_summary": spec["evidence_summary"],
            "limitations": (
                "The cited studies establish complementary receptor, intracellular, TF-activity and output layers "
                "rather than a single asserted end-to-end graph sequence. Receptor-to-intermediate and downstream "
                "handoffs remain unasserted; no causal traversal or confidence score is inferred."
            ),
            "curation_status": "curated_primary_route",
            "species_context": spec["species_context"],
            "cell_type_context": spec["cell_type_context"],
            "compartment_context": "extracellular ligand; plasma-membrane receptor; intracellular signaling relay; nuclear TF or functional output context",
            "injury_context": "no SCI transfer inferred; primary model context only",
            "context_scope": "composite primary evidence; source-specific receptor and output context retained",
            "assay_or_perturbation": spec["assay_or_perturbation"],
            "effect_polarity": "activating",
            "source_scope": "composite_primary_evidence",
        })
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
