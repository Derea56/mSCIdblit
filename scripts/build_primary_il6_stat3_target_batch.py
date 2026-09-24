#!/usr/bin/env python3
"""Build primary-literature IL-6/JAK1/STAT3 target-gene routes."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "IL6-IL6Rgp130-JAK1-STAT3-CRP",
        "target_node_id": "NODE02493",
        "primary_locator": "PMID:35430542; PMID:17595889",
        "output_label": "CRP gene expression",
        "pathway_name": "IL6-IL6Rgp130-JAK1-STAT3-CRP",
        "assay_or_perturbation": "IL-6 stimulation of human hepatoma cells and primary human hepatocytes; STAT3 activity assays; CRP promoter-site analysis and CRP RNA/protein readouts",
    },
    {
        "name": "IL6-IL6Rgp130-JAK1-STAT3-HAMP",
        "target_node_id": "NODE04598",
        "primary_locator": "PMID:16835372",
        "output_label": "HAMP/hepcidin gene expression",
        "pathway_name": "IL6-IL6Rgp130-JAK1-STAT3-HAMP",
        "assay_or_perturbation": "IL-6 treatment of HepG2/2.2.1 cells; hepcidin promoter reporter and STAT3 chromatin immunoprecipitation; dominant-negative or siRNA STAT3 perturbation",
    },
    {
        "name": "IL6-IL6Rgp130-JAK1-STAT3-CEBPD",
        "target_node_id": "NODE02060",
        "primary_locator": "PMID:9528783",
        "output_label": "CEBPD gene expression",
        "pathway_name": "IL6-IL6Rgp130-JAK1-STAT3-CEBPD",
        "assay_or_perturbation": "IL-6 treatment of HepG2/Hep3B hepatoma cells; CEBPD promoter deletion and reporter assays; STAT3 DNA-binding and transactivation analysis",
    },
    {
        "name": "IL6-IL6Rgp130-JAK1-STAT3-SOCS3",
        "target_node_id": "NODE10509",
        "primary_locator": "PMID:16718380; PMID:12560330",
        "output_label": "SOCS3 gene expression",
        "pathway_name": "IL6-IL6Rgp130-JAK1-STAT3-SOCS3",
        "assay_or_perturbation": "IL-6 stimulation of hepatocyte or Stat3-null/reconstituted cell systems; SOCS3 promoter STAT3-site analysis; SOCS3 transcript/protein and insulin-signaling feedback readouts",
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
    lr_edge_id = "M21B-E001760"
    lr = edges[lr_edge_id]
    ligand = nodes[lr["source_node_id"]]
    receptor = nodes[lr["target_node_id"]]
    relay = nodes["NODE06016"]
    tf = nodes["NODE10726"]
    rows: list[dict[str, str]] = []
    for index, spec in enumerate(SPECS, start=1):
        target = nodes[spec["target_node_id"]]
        expansion_id = f"M21B-LITEXP-IL6GAP-{index:03d}"
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
                "intracellular_continuation_node_id": "NODE06016",
                "intracellular_continuation_label": relay["canonical_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": "NODE10726",
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
                    f"Primary-evidence route overlay for {spec['name']}. IL-6 receptor/JAK1/STAT3 and target-gene layers are retained "
                    "while unresolved graph handoffs remain explicit; no causal edge or confidence score is created."
                ),
                "evidence_summary": (
                    "Primary IL-6 studies support IL-6 receptor-associated JAK/STAT3 activation and the "
                    f"{spec['output_label']} readout, including STAT3 promoter, chromatin, or perturbation evidence. The route maps those "
                    "observations onto the existing IL-6R/gp130, JAK1, STAT3, and target-gene nodes."
                ),
                "limitations": (
                    "The source systems differ across hepatoma cells, primary hepatocytes, and reconstituted or genetically perturbed models. "
                    "Direct receptor-to-JAK, JAK-to-STAT3, and STAT3-to-target graph handoffs remain evidence-layer links; no SCI transfer "
                    "or causal graph edge is inferred."
                ),
                "curation_status": "curated_primary_route",
                "species_context": "human and mouse cell systems",
                "cell_type_context": "human hepatoma or primary hepatocyte systems and IL-6-responsive receptor-signaling models",
                "compartment_context": "extracellular IL-6; plasma-membrane IL-6R/gp130 receptor complex; intracellular JAK1 signaling; nuclear STAT3 target-gene output",
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
