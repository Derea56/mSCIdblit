#!/usr/bin/env python3
"""Build primary-literature IL-2/JAK/STAT5 target-gene routes."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "IL2-IL2R-JAK1JAK3-STAT5-CISH",
        "target_node_id": "NODE02198",
        "primary_locator": "PMID:9129017",
        "output_label": "CISH gene expression",
        "pathway_name": "IL2-IL2R-JAK1JAK3-STAT5-CISH",
        "assay_or_perturbation": "IL-2 stimulation; IL-2 receptor mutant comparison; STAT5 phosphorylation/DNA binding; CISH promoter mapping and luciferase; CISH mRNA induction",
    },
    {
        "name": "IL2-IL2R-JAK1JAK3-STAT5-FRA2",
        "target_node_id": "NODE03776",
        "primary_locator": "PMID:24587342",
        "output_label": "FOSL2/FRA2 gene expression",
        "pathway_name": "IL2-IL2R-JAK1JAK3-STAT5-FRA2",
        "assay_or_perturbation": "IL-2 and T-cell-receptor stimulation; STAT5 ChIP at the FRA2 intron; GAS reporter mutagenesis; JAK3 inhibitor; daclizumab; FOSL2/FRA2 transcriptional readouts",
    },
    {
        "name": "IL2-IL2R-JAK1JAK3-STAT5-IFNG",
        "target_node_id": "NODE05005",
        "primary_locator": "PMID:15271977",
        "output_label": "IFNG gene expression",
        "pathway_name": "IL2-IL2R-JAK1JAK3-STAT5-IFNG",
        "assay_or_perturbation": "IL-2 treatment of primary human NK cells and Th1 cells; IFNG-locus chromatin acetylation; STAT5A/STAT5B ChIP; GAS-motif disruption; IFNG reporter transcription",
    },
    {
        "name": "IL2-IL2R-JAK1JAK3-STAT5-MYC",
        "target_node_id": "NODE07604",
        "primary_locator": "PMID:10679091",
        "output_label": "MYC gene expression",
        "pathway_name": "IL2-IL2R-JAK1JAK3-STAT5-MYC",
        "assay_or_perturbation": "IL-2 receptor-beta tyrosine-mutant systems; STAT5 transactivation-domain perturbation; MYC expression; CTLL-2 and BA/F3 lymphocyte growth assays",
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
    lr_edge_id = "M21B-E000236"
    lr = edges[lr_edge_id]
    ligand = nodes[lr["source_node_id"]]
    receptor = nodes[lr["target_node_id"]]
    relay = nodes["NODE06024"]
    tf = nodes["NODE10759"]
    rows: list[dict[str, str]] = []
    for index, spec in enumerate(SPECS, start=1):
        target = nodes[spec["target_node_id"]]
        expansion_id = f"M21B-LITEXP-IL2GAP-{index:03d}"
        rows.append(
            {
                "expansion_id": expansion_id,
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
                "intracellular_status": "source_supported_composed",
                "ligand_node_id": lr["source_node_id"],
                "ligand_label": ligand["canonical_label"],
                "ligand_receptor_edge_id": lr_edge_id,
                "receptor_node_id": lr["target_node_id"],
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": "NODE06024",
                "intracellular_continuation_label": relay["canonical_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": "NODE10759",
                "transcription_factor_label": tf["canonical_label"],
                "tf_target_edge_id": "",
                "target_gene_node_id": spec["target_node_id"],
                "target_gene_label": target["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": "",
                "output_label": spec["output_label"],
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": spec["pathway_name"],
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": unique_join(lr.get("evidence_ids", ""), spec["primary_locator"]),
                "source_chain_id": expansion_id,
                "source_evidence_record_id": "",
                "route_linkage_status": (
                    f"manual_primary_{spec['name'].lower().replace('-', '_')}_route;graph_linked_route_source;"
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
                "primary_locator": spec["primary_locator"],
                "citation_note": (
                    f"Primary-evidence route overlay for {spec['name']}. IL-2 receptor/JAK/STAT5 and target-gene layers are retained "
                    "while unresolved graph handoffs remain explicit; no causal edge or confidence score is created."
                ),
                "evidence_summary": (
                    "Primary IL-2 studies support IL-2 receptor-associated JAK/STAT5 activation and the "
                    f"{spec['output_label']} readout, including STAT5 DNA binding or promoter/enhancer evidence. The route maps those "
                    "observations onto the existing IL-2 receptor, JAK1/JAK3, STAT5-family, and target-gene nodes."
                ),
                "limitations": (
                    "The source systems differ across receptor reconstitution, lymphocyte, NK-cell, and T-cell models. Direct "
                    "receptor-to-JAK, JAK-to-STAT5, and STAT5-to-target graph handoffs remain evidence-layer links; no SCI transfer "
                    "or causal graph edge is inferred."
                ),
                "curation_status": "curated_primary_route",
                "species_context": "human and mammalian cell systems",
                "cell_type_context": "primary human NK/Th1 or T-cell systems and cytokine-receptor reconstitution models",
                "compartment_context": "extracellular IL-2; plasma-membrane IL-2 receptor complex; intracellular JAK1/JAK3 signaling; nuclear STAT5 target-gene output",
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
