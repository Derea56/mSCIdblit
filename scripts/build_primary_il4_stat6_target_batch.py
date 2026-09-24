#!/usr/bin/env python3
"""Build primary-literature IL-4/JAK/STAT6 target-gene routes."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "IL4-IL4R-JAK1JAK3-STAT6-ARG1",
        "target_node_id": "NODE00751",
        "primary_locator": "PMID:11160269",
        "output_label": "ARG1 gene expression",
        "pathway_name": "IL4-IL4R-JAK1JAK3-STAT6-ARG1",
        "assay_or_perturbation": "IL-4 or IL-13 stimulation of murine macrophages; Stat6-dependent arginase I induction; nitric-oxide substrate depletion and exogenous arginine rescue",
    },
    {
        "name": "IL4-IL4R-JAK1JAK3-STAT6-CCL17",
        "target_node_id": "NODE01656",
        "primary_locator": "PMID:16810739",
        "output_label": "CCL17/TARC gene expression",
        "pathway_name": "IL4-IL4R-JAK1JAK3-STAT6-CCL17",
        "assay_or_perturbation": "IL-4 stimulation of human T cells; STAT6 electrophoretic mobility shift and chromatin immunoprecipitation; CCL17 promoter reporter assays with STAT6-site mutation",
    },
    {
        "name": "IL4-IL4R-JAK1JAK3-STAT6-GATA3",
        "target_node_id": "NODE03996",
        "primary_locator": "PMID:11283251",
        "output_label": "GATA3 gene expression",
        "pathway_name": "IL4-IL4R-JAK1JAK3-STAT6-GATA3",
        "assay_or_perturbation": "Primary CD4 T-cell activation under Th2 conditions; IL-4/STAT6-dependent GATA3 induction; Stat6-deficient T-cell comparison and retroviral transcription-factor perturbation",
    },
    {
        "name": "IL4-IL4R-JAK1JAK3-STAT6-CHIL3",
        "target_node_id": "NODE02113",
        "primary_locator": "PMID:19567879",
        "output_label": "CHIL3/Ym1 gene expression",
        "pathway_name": "IL4-IL4R-JAK1JAK3-STAT6-CHIL3",
        "assay_or_perturbation": "IL-4-induced alternative activation of bone-marrow-derived macrophages; wild-type versus Stat6-deficient expression of Jmjd3, Chi3l3/Ym1, Retnla, and Arg1; chromatin-mark and recruitment assays",
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
    lr_edge_id = "M21B-E001754"
    lr = edges[lr_edge_id]
    ligand = nodes[lr["source_node_id"]]
    receptor = nodes[lr["target_node_id"]]
    relay = nodes["NODE06024"]
    tf = nodes["NODE10761"]
    rows: list[dict[str, str]] = []
    for index, spec in enumerate(SPECS, start=1):
        target = nodes[spec["target_node_id"]]
        expansion_id = f"M21B-LITEXP-IL4GAP-{index:03d}"
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
                "transcription_factor_node_id": "NODE10761",
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
                    f"Primary-evidence route overlay for {spec['name']}. IL-4 receptor/JAK/STAT6 and target-gene layers are retained "
                    "while unresolved graph handoffs remain explicit; no causal edge or confidence score is created."
                ),
                "evidence_summary": (
                    "Primary IL-4 studies support IL-4 receptor-associated JAK/STAT6 activation and the "
                    f"{spec['output_label']} readout, including STAT6-dependent or promoter/enhancer evidence. The route maps those "
                    "observations onto the existing IL-4 receptor, JAK1/JAK3, STAT6, and target-gene nodes."
                ),
                "limitations": (
                    "The source systems differ across human T cells, primary macrophages, and genetically perturbed models. Direct "
                    "receptor-to-JAK, JAK-to-STAT6, and STAT6-to-target graph handoffs remain evidence-layer links; no SCI transfer "
                    "or causal graph edge is inferred."
                ),
                "curation_status": "curated_primary_route",
                "species_context": "human and mouse cell systems",
                "cell_type_context": "primary human T-cell or murine macrophage systems and cytokine-receptor signaling models",
                "compartment_context": "extracellular IL-4; plasma-membrane IL-4 receptor complex; intracellular JAK1/JAK3 signaling; nuclear STAT6 target-gene output",
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
