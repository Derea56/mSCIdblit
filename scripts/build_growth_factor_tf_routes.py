#!/usr/bin/env python3
"""Build bounded primary-literature routes for canonical growth factors."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROUTES = (
    {
        "name": "GCSF-STAT3-MMP2",
        "ligand_node_id": "NODE03898",
        "ligand_label": "G-CSF",
        "lr_edge_id": "M21B-E001008",
        "receptor_node_id": "NODE02538",
        "receptor_label": "CSF3R homodimer",
        "intracellular_node_id": "NODE06026",
        "intracellular_label": "JAK2",
        "tf_node_id": "NODE10726",
        "tf_label": "STAT3",
        "target_node_id": "NODE07455",
        "target_label": "MMP2 gene",
        "target_short": "MMP2",
        "output_label": "MMP2 expression in G-CSF-stimulated TNBC cells",
        "locators": "PMID:7521688; PMID:25908586; PMID:32242230",
        "pathway_name": "GCSF-CSF3R-JAK2-STAT3-MMP2",
        "citation_note": "Primary G-CSF studies support CSF3R-linked JAK/STAT3 activation and G-CSF/STAT3-dependent MMP2 expression; unresolved handoffs remain explicit.",
        "evidence_summary": "G-CSF induces JAK1/JAK2 and STAT3 activation, while a primary TNBC study identifies MMP2 as a G-CSF/STAT3-dependent target output.",
        "species_context": "human; mouse comparator in the G-CSF neuroblastoma study",
        "cell_type_context": "human neuroblastoma and triple-negative breast-cancer cells; source-specific context retained",
        "assay_or_perturbation": "G-CSF stimulation; JAK/STAT3 phosphorylation; STAT3 inhibition; MMP2/MMP9 expression assays",
    },
    {
        "name": "GCSF-STAT3-MMP9",
        "ligand_node_id": "NODE03898",
        "ligand_label": "G-CSF",
        "lr_edge_id": "M21B-E001008",
        "receptor_node_id": "NODE02538",
        "receptor_label": "CSF3R homodimer",
        "intracellular_node_id": "NODE06026",
        "intracellular_label": "JAK2",
        "tf_node_id": "NODE10726",
        "tf_label": "STAT3",
        "target_node_id": "NODE07461",
        "target_label": "MMP9 gene",
        "target_short": "MMP9",
        "output_label": "MMP9 expression in G-CSF-stimulated TNBC cells",
        "locators": "PMID:7521688; PMID:25908586; PMID:32242230",
        "pathway_name": "GCSF-CSF3R-JAK2-STAT3-MMP9",
        "citation_note": "Primary G-CSF studies support CSF3R-linked JAK/STAT3 activation and G-CSF/STAT3-dependent MMP9 expression; unresolved handoffs remain explicit.",
        "evidence_summary": "G-CSF induces JAK1/JAK2 and STAT3 activation, while a primary TNBC study identifies MMP9 as a G-CSF/STAT3-dependent target output.",
        "species_context": "human; mouse comparator in the G-CSF neuroblastoma study",
        "cell_type_context": "human neuroblastoma and triple-negative breast-cancer cells; source-specific context retained",
        "assay_or_perturbation": "G-CSF stimulation; JAK/STAT3 phosphorylation; STAT3 inhibition; MMP2/MMP9 expression assays",
    },
    {
        "name": "VEGFA-STAT3-MYC",
        "ligand_node_id": "NODE11726",
        "ligand_label": "VEGFA/VEGF-A",
        "lr_edge_id": "M21B-E000183",
        "receptor_node_id": "NODE06103",
        "receptor_label": "KDR/VEGFR2 receptor dimer",
        "intracellular_node_id": "NODE06026",
        "intracellular_label": "JAK2",
        "tf_node_id": "NODE10726",
        "tf_label": "STAT3",
        "target_node_id": "NODE07604",
        "target_label": "MYC gene",
        "target_short": "MYC",
        "output_label": "MYC expression in VEGF-stimulated breast and lung cancer stem cells",
        "locators": "PMID:10961983; PMID:25151964; DOI:10.1074/jbc.C000318200; DOI:10.1038/onc.2014.257",
        "pathway_name": "VEGFA-KDR-JAK2-STAT3-MYC",
        "citation_note": "Primary VEGF studies support VEGFR2-associated STAT activation and VEGF/VEGFR2/STAT3-dependent MYC induction; unresolved handoffs remain explicit.",
        "evidence_summary": "VEGF activates STAT signaling through VEGFR2, and a primary study reports VEGFR2/JAK2/STAT3 binding, STAT3 promoter occupancy, and MYC induction after VEGF exposure.",
        "species_context": "human; bovine endothelial comparator in the VEGFR2/STAT study",
        "cell_type_context": "human breast and lung cancer stem-cell models; endothelial comparator context retained",
        "assay_or_perturbation": "VEGF stimulation; VEGFR2 knockdown/inhibition; JAK2/STAT3 activation; STAT3 binding and MYC expression assays",
    },
    {
        "name": "VEGFA-STAT3-SOX2",
        "ligand_node_id": "NODE11726",
        "ligand_label": "VEGFA/VEGF-A",
        "lr_edge_id": "M21B-E000183",
        "receptor_node_id": "NODE06103",
        "receptor_label": "KDR/VEGFR2 receptor dimer",
        "intracellular_node_id": "NODE06026",
        "intracellular_label": "JAK2",
        "tf_node_id": "NODE10726",
        "tf_label": "STAT3",
        "target_node_id": "NODE10536",
        "target_label": "SOX2 gene",
        "target_short": "SOX2",
        "output_label": "SOX2 expression in VEGF-stimulated breast and lung cancer stem cells",
        "locators": "PMID:10961983; PMID:25151964; DOI:10.1074/jbc.C000318200; DOI:10.1038/onc.2014.257",
        "pathway_name": "VEGFA-KDR-JAK2-STAT3-SOX2",
        "citation_note": "Primary VEGF studies support VEGFR2-associated STAT activation and VEGF/VEGFR2/STAT3-dependent SOX2 induction; unresolved handoffs remain explicit.",
        "evidence_summary": "VEGF activates STAT signaling through VEGFR2, and a primary study reports VEGFR2/JAK2/STAT3 binding, STAT3 promoter occupancy, and SOX2 induction after VEGF exposure.",
        "species_context": "human; bovine endothelial comparator in the VEGFR2/STAT study",
        "cell_type_context": "human breast and lung cancer stem-cell models; endothelial comparator context retained",
        "assay_or_perturbation": "VEGF stimulation; VEGFR2 knockdown/inhibition; JAK2/STAT3 activation; STAT3 binding and SOX2 expression assays",
    },
    {
        "name": "PGE2-ERK-CREB-EGR1",
        "ligand_node_id": "NODE08947",
        "ligand_label": "PGE2/prostaglandin E2",
        "lr_edge_id": "M21B-E001537",
        "receptor_node_id": "NODE09440",
        "receptor_label": "PTGER4/EP4 prostaglandin E receptor",
        "intracellular_node_id": "NODE06776",
        "intracellular_label": "MAPK1/MAPK3 (ERK1/2)",
        "tf_node_id": "NODE02446",
        "tf_label": "CREB",
        "target_node_id": "NODE03139",
        "target_label": "EGR1 promoter",
        "target_short": "EGR1",
        "output_label": "EGR1 expression in PGE2-stimulated HCA-7 cells",
        "locators": "PMID:17631291; DOI:10.1016/j.yexcr.2007.06.004",
        "pathway_name": "PGE2-EP4-ERK1/2-CREB-EGR1",
        "citation_note": "The primary EP4 study directly reports ERK1/2 activation, CREB phosphorylation and CREB-dependent EGR1 transcription; graph handoffs remain explicit.",
        "evidence_summary": "PGE2-induced ERK1/2 activation is blocked by EP4 antagonism, CREB is phosphorylated, and dominant-negative CREB suppresses PGE2-driven EGR1 promoter activity and expression.",
        "species_context": "human",
        "cell_type_context": "HCA-7 human colon epithelial cancer cells",
        "assay_or_perturbation": "PGE2 stimulation; EP4 antagonism; ERK inhibition; CREB phosphorylation, reporter, promoter and EGR1 expression assays",
    },
    {
        "name": "PDGFB-ERK-ELK1-EGR1",
        "ligand_node_id": "NODE08843",
        "ligand_label": "PDGFB",
        "lr_edge_id": "M21B-E011671",
        "receptor_node_id": "NODE08853",
        "receptor_label": "PDGFRA+PDGFRB",
        "intracellular_node_id": "NODE06776",
        "intracellular_label": "MAPK1/MAPK3 (ERK1/2)",
        "tf_node_id": "NODE03164",
        "tf_label": "Elk-1",
        "target_node_id": "NODE03139",
        "target_label": "EGR1 promoter",
        "target_short": "EGR1",
        "output_label": "EGR1 expression after PDGF-BB stimulation",
        "locators": "PMID:15003938; PMID:15492129; DOI:10.1152/ajplung.00190.2003",
        "pathway_name": "PDGFB-PDGFR-ERK1/2-Elk1-EGR1",
        "citation_note": "Primary PDGF studies support PDGF receptor-linked ERK1/2 and Elk-1 activation with EGR1 promoter/output induction; unresolved handoffs remain explicit.",
        "evidence_summary": "PDGF induces ERK1/2 and Elk-1 phosphorylation, EGR1 promoter activity and EGR1 expression; PDGF-BB-induced EGR1 and tissue-factor transcription are reduced by ERK/Src pathway inhibition.",
        "species_context": "human; rat comparator in the PDGF-BB vascular smooth-muscle study",
        "cell_type_context": "human airway smooth muscle and rat vascular smooth muscle cells",
        "assay_or_perturbation": "PDGF or PDGF-BB stimulation; ERK/Src inhibition; ERK and Elk-1 phosphorylation; EGR1 promoter, RNA and protein assays",
    },
)


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


def make_rows(bundle: Path) -> list[dict[str, str]]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    rows: list[dict[str, str]] = []
    for spec in ROUTES:
        required_nodes = [
            spec["ligand_node_id"], spec["receptor_node_id"], spec["intracellular_node_id"],
            spec["tf_node_id"], spec["target_node_id"],
        ]
        missing_nodes = [node_id for node_id in required_nodes if node_id not in nodes]
        if missing_nodes:
            raise ValueError(f"{spec['name']}: missing nodes {missing_nodes}")
        if spec["lr_edge_id"] not in edges:
            raise ValueError(f"{spec['name']}: missing ligand-receptor edge {spec['lr_edge_id']}")
        lr = edges[spec["lr_edge_id"]]
        if (lr["source_node_id"], lr["target_node_id"]) != (spec["ligand_node_id"], spec["receptor_node_id"]):
            raise ValueError(f"{spec['name']}: ligand-receptor endpoints do not match")

        expansion_id = f"M21B-LITEXP-{spec['name']}"
        rows.append({
            "expansion_id": expansion_id,
            "source_queue_id": "",
            "route_status": "retained_evidence_route",
            "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
            "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
            "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
            "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
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
            "output_node_id": spec["target_node_id"],
            "output_label": spec["output_label"],
            "pathway_name": spec["pathway_name"],
            "input_evidence_type": "primary_literature_route_expansion",
            "output_evidence_type": "primary_target_gene_expression",
            "evidence_ids": unique_join(lr.get("evidence_ids", ""), spec["locators"]),
            "source_chain_id": expansion_id,
            "source_evidence_record_id": "",
            "route_linkage_status": (
                "graph_linked_route_source;manual_primary_growth_factor_tf_route;primary_layer_linked;"
                "receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;"
                "tf_to_target_edge_not_asserted;evidence_route_only"
            ),
            "causal_status": "not_asserted",
            "traversal_status": "evidence_route_not_causal",
            "evidence_contract_version": "mechanism_evidence_v1",
            "evidence_polarity": "supports",
            "negative_evidence_status": "not_evaluated",
            "evidence_directness": "composite_primary_route",
            "output_class": "target_gene_expression",
            "primary_locator": spec["locators"],
            "citation_note": spec["citation_note"],
            "evidence_summary": spec["evidence_summary"],
            "limitations": (
                "The cited studies establish complementary receptor, intracellular, TF-activity and expression layers "
                "rather than a single asserted end-to-end edge sequence. Receptor-to-intermediate, intermediate-to-TF "
                "and TF-to-target handoffs are not created as graph edges; no SCI transfer, causal traversal, or "
                "confidence score is inferred."
            ),
            "curation_status": "curated_primary_route",
            "species_context": spec["species_context"],
            "cell_type_context": spec["cell_type_context"],
            "compartment_context": "extracellular ligand; plasma-membrane receptor; intracellular signaling relay; nuclear TF and target-gene locus",
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
    args.output.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
