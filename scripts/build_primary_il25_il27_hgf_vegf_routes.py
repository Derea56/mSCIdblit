#!/usr/bin/env python3
"""Build primary-literature route overlays for four canonical ligand gaps."""

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


def make_rows(bundle: Path) -> list[dict[str, str]]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    specs = [
        {
            "expansion_id": "M21B-LITEXP-IL25-IL17RB-ACT1-NFKB-IL13",
            "ligand_node_id": "NODE05435",
            "ligand_label": "IL25/IL17E",
            "lr_edge_id": "M21B-E000748",
            "receptor_node_id": "NODE05341",
            "receptor_label": "IL17RA:IL17RB receptor complex",
            "relay_node_id": "NODE00152",
            "relay_label": "ACT1/CIKS",
            "tf_node_id": "NODE07984",
            "tf_label": "NF-kB",
            "target_node_id": "",
            "target_label": "",
            "pathway_name": "IL25-IL17RA-IL17RB-ACT1-NF-kB-IL13-output",
            "primary_locator": "PMID:22045852; PMID:19155512",
            "evidence_summary": (
                "Primary studies show that IL-25 signals through the IL-17RA/IL-17RB receptor system and recruits "
                "the SEFIR adaptor Act1. Act1 loss or disruption suppresses IL-25-induced Il13 mRNA and pulmonary "
                "type-2 cytokine output, while the route retains NF-kB as the downstream transcriptional family layer."
            ),
            "limitations": (
                "The studies resolve receptor–Act1 dependence and IL-13 output but do not establish a single direct "
                "Act1-to-NF-kB-to-IL13 molecular chain. The terminal target locus and exact kinase/adaptor ordering "
                "remain unasserted; no SCI transfer is inferred."
            ),
            "cell_type_context": "Act1-deficient MEFs expressing IL17RB; mouse lung and airway epithelium",
            "assay_or_perturbation": "IL-25 stimulation; Act1 deletion/reconstitution; SEFIR-domain perturbation; Il13/Cxcl1 mRNA; pulmonary cytokine and eosinophil readouts",
            "species_context": "mouse; engineered mammalian cell systems",
        },
        {
            "expansion_id": "M21B-LITEXP-IL27-IL27R-JAK-TYK2-STAT1-TBX21",
            "ligand_node_id": "NODE05437",
            "ligand_label": "IL27",
            "lr_edge_id": "M21B-E000124",
            "receptor_node_id": "NODE05442",
            "receptor_label": "IL27RA/WSX-1:gp130 receptor complex",
            "relay_node_id": "NODE06023",
            "relay_label": "JAK1/JAK2/TYK2",
            "tf_node_id": "NODE10705",
            "tf_label": "STAT1",
            "target_node_id": "NODE10908",
            "target_label": "TBX21 gene",
            "tf_target_edge_id": "M21B-E008248",
            "pathway_name": "IL27-IL27RA-gp130-JAK-STAT1-TBX21",
            "primary_locator": "PMID:14565860; PMID:15356135; PMID:23452095",
            "evidence_summary": (
                "Primary studies report IL-27 receptor-dependent phosphorylation of STAT1 and STAT3, activation of "
                "JAK1/JAK2/TYK2-associated signaling, and STAT1-dependent induction of T-bet/TBX21 in human and mouse "
                "T-cell systems. An independent primary endothelial study also links IL-27 to JAK-dependent STAT1/3 "
                "activation and STAT1-dependent chemokine transcription."
            ),
            "limitations": (
                "The cited studies use complementary T-cell and endothelial models and do not establish one uninterrupted "
                "IL27-to-TBX21 experiment with every receptor-to-kinase handoff. The graph-linked STAT1-to-TBX21 edge is "
                "retained as an evidence component, while receptor-to-JAK and JAK-to-STAT1 transitions remain composed."
            ),
            "cell_type_context": "primary human T cells; mouse naive CD4 T cells; human lymphatic endothelial cells",
            "assay_or_perturbation": "IL-27 stimulation; JAK/STAT phosphorylation; STAT1-deficient T cells; T-bet/TBX21 and IL12RB2 expression; STAT1 knockdown and chemokine assays",
            "species_context": "human; mouse",
        },
        {
            "expansion_id": "M21B-LITEXP-HGF-MET-MAPK-EGR1-SNAIL",
            "ligand_node_id": "NODE04679",
            "ligand_label": "HGF (cleaved two-chain form)",
            "lr_edge_id": "M21B-E000167",
            "receptor_node_id": "NODE06947",
            "receptor_label": "MET receptor",
            "relay_node_id": "NODE04680",
            "relay_label": "HGF-MET-GAB1/GRB2-MAPK/PI3K relay",
            "tf_node_id": "NODE03137",
            "tf_label": "EGR1",
            "target_node_id": "",
            "target_label": "",
            "pathway_name": "HGF-MET-MAPK-EGR1-SNAIL-motility-output",
            "primary_locator": "PMID:16858414; PMID:20357818",
            "evidence_summary": (
                "Primary studies report HGF/MET-dependent MAPK signaling, EGR-1 requirement for HGF-induced Snail "
                "transcription, and HGF-dependent CD44v6 transcription and motility in primary human melanocytes. "
                "The route retains the graph-linked HGF-MET input and the existing HGF-MET-MAPK relay annotation."
            ),
            "limitations": (
                "The cited studies use epithelial and primary melanocyte systems and report complementary HGF/MET, "
                "MAPK/EGR-1, and CD44v6 or Snail outputs. The exact MET-to-relay and EGR-1-to-terminal-gene handoffs "
                "remain unasserted, and no SCI transfer is inferred."
            ),
            "cell_type_context": "human epithelial cells and primary human melanocytes",
            "assay_or_perturbation": "HGF stimulation; MET or MAPK perturbation; EGR-1 depletion; Snail transcription; CD44v6 promoter/expression and motility assays",
            "species_context": "human; mammalian cell systems",
        },
        {
            "expansion_id": "M21B-LITEXP-VEGFA165-NRP1KDR-ERK-AP1-JUNB",
            "ligand_node_id": "NODE11720",
            "ligand_label": "VEGF165/VEGFA isoform",
            "lr_edge_id": "M21B-E000185",
            "receptor_node_id": "NODE08326",
            "receptor_label": "NRP1:KDR receptor complex",
            "relay_node_id": "NODE03370",
            "relay_label": "ERK1/2/MAPK1/3",
            "tf_node_id": "NODE00609",
            "tf_label": "AP-1",
            "target_node_id": "NODE06057",
            "target_label": "JUNB gene",
            "pathway_name": "VEGF165-VEGFR2-ERK-AP1-JUNB-endothelial-output",
            "primary_locator": "PMID:26860974; PMID:17549302; PMID:22828632",
            "evidence_summary": (
                "Primary endothelial studies report VEGF receptor activation with ERK phosphorylation, VEGF-induced "
                "AP-1 family transcription—especially JunB—and AP-1-dependent endothelial migration/proliferation. "
                "A complementary primary study identifies VEGF-dependent NFAT/EGR-1 cooperation at a tissue-factor "
                "promoter, supporting the broader transcriptional-output layer."
            ),
            "limitations": (
                "The studies use complementary receptor, ERK, AP-1, NFAT/EGR-1, and endothelial-output experiments. "
                "They do not establish one uninterrupted NRP1:KDR-to-ERK-to-AP-1-to-JUNB chain, so receptor-to-relay, "
                "relay-to-TF, and TF-to-target edges remain unasserted."
            ),
            "cell_type_context": "primary human endothelial cells and HUVECs",
            "assay_or_perturbation": "VEGF stimulation; VEGFR1/2 activation; ERK phosphorylation; AP-1 dominant-negative c-Fos; JunB knockdown; promoter/reporter and migration/proliferation assays",
            "species_context": "human; mouse vascular models",
        },
    ]

    rows: list[dict[str, str]] = []
    for spec in specs:
        required_nodes = [
            spec["ligand_node_id"], spec["receptor_node_id"], spec["relay_node_id"], spec["tf_node_id"]
        ]
        if spec.get("target_node_id"):
            required_nodes.append(spec["target_node_id"])
        missing = [node_id for node_id in required_nodes if node_id not in nodes]
        if missing:
            raise ValueError(f"{spec['expansion_id']}: missing nodes {missing}")
        lr = edges.get(spec["lr_edge_id"])
        if not lr or (lr["source_node_id"], lr["target_node_id"]) != (
            spec["ligand_node_id"], spec["receptor_node_id"]
        ):
            raise ValueError(f"{spec['expansion_id']}: ligand-receptor edge endpoints do not match")
        tf_edge_id = spec.get("tf_target_edge_id", "")
        if tf_edge_id:
            tf_edge = edges.get(tf_edge_id)
            if not tf_edge or (tf_edge["source_node_id"], tf_edge["target_node_id"]) != (
                spec["tf_node_id"], spec["target_node_id"]
            ):
                raise ValueError(f"{spec['expansion_id']}: TF-target edge endpoints do not match")
        has_target = bool(spec.get("target_node_id"))
        missing_layers = ["receptor_to_intracellular_edge", "intracellular_to_tf_edge"]
        if not has_target:
            missing_layers.append("target_gene_expression")
        route_linkage = (
            "graph_linked_route_source;manual_primary_route_expansion;primary_layer_linked;"
            "receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;"
            + (
                "tf_to_target_edge_asserted_as_graph_edge;"
                if tf_edge_id
                else ("tf_to_target_edge_not_asserted;" if has_target else "")
            )
            + "end_to_end_chain_not_asserted_by_single_source;evidence_route_only"
        )
        rows.append(
            {
                "expansion_id": spec["expansion_id"],
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression" if has_target else "ligand>receptor>intracellular>TF>output",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges" if has_target else "ligand_receptor_intracellular_tf_output_missing_target_gene",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression" if has_target else "ligand|receptor|intracellular_continuation|transcription_factor|output",
                "missing_layers": "|".join(missing_layers),
                "intracellular_status": "source_supported_composed",
                "ligand_node_id": spec["ligand_node_id"],
                "ligand_label": spec["ligand_label"],
                "ligand_receptor_edge_id": spec["lr_edge_id"],
                "receptor_node_id": spec["receptor_node_id"],
                "receptor_label": spec["receptor_label"],
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": spec["relay_node_id"],
                "intracellular_continuation_label": spec["relay_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": spec["tf_node_id"],
                "transcription_factor_label": spec["tf_label"],
                "tf_target_edge_id": tf_edge_id,
                "target_gene_node_id": spec.get("target_node_id", ""),
                "target_gene_label": spec.get("target_label", ""),
                "target_output_form_id": "",
                "output_node_id": "",
                "output_label": spec.get("target_label", "") if has_target else spec["pathway_name"].split("-")[-1] + " functional output",
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": spec["pathway_name"],
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression" if has_target else "primary_composed_downstream_output",
                "evidence_ids": unique_join(lr.get("evidence_ids", ""), edges.get(tf_edge_id, {}).get("evidence_ids", ""), spec["primary_locator"]),
                "source_chain_id": spec["expansion_id"],
                "source_evidence_record_id": "",
                "route_linkage_status": route_linkage,
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression" if has_target else "generic_functional_readout",
                "primary_locator": spec["primary_locator"],
                "citation_note": "Primary literature supports the listed route layers; unresolved handoffs remain explicitly bounded and no confidence score is assigned.",
                "evidence_summary": spec["evidence_summary"],
                "limitations": spec["limitations"],
                "curation_status": "curated_primary_route",
                "species_context": spec["species_context"],
                "cell_type_context": spec["cell_type_context"],
                "compartment_context": "extracellular ligand; plasma-membrane receptor; intracellular relay; nuclear transcriptional/output layer",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary evidence with graph-linked ligand-receptor identity",
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
