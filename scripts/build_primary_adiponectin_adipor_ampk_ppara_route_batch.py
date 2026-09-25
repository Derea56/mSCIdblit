#!/usr/bin/env python3
"""Build primary-evidence adiponectin receptor route overlays."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROUTES = (
    {
        "suffix": "ADIPOR1-AMPK",
        "lr_edge_id": "M20B-E002472",
        "relay_node_id": "NODE00303",
        "tf_node_id": "",
        "path_expression": "ligand>receptor>intracellular>output",
        "route_tier": "ligand_receptor_intracellular_output_missing_tf",
        "known_layers": "ligand|receptor|intracellular_continuation|output",
        "missing_layers": "receptor_to_intracellular_edge|transcription_factor|intracellular_to_tf_edge|target_gene_expression",
        "output_label": "AMPK-associated fatty-acid uptake and oxidation",
        "pathway_name": "ADIPOQ-ADIPOR1-APPL1-AMPK-fatty-acid-oxidation",
        "locators": "PMID:20739511; PMCID:PMC2980363",
        "summary": (
            "A primary cardiomyocyte and perfused-heart study reports that adiponectin promotes ADIPOR1/APPL1 "
            "association, APPL1 binding to AMPKalpha2, AMPK activation, ACC phosphorylation, fatty-acid uptake, "
            "and fatty-acid oxidation. The route retains these layers as an evidence-supported intracellular-to-"
            "functional-output branch without assigning a terminal transcription factor or target gene."
        ),
        "limitations": (
            "The study uses cardiomyocytes and perfused hearts and does not establish the exact ADIPOR1-to-APPL1 "
            "handoff as a graph edge or a transcriptional endpoint. The route is evidence-layer support only; no "
            "SCI transfer, causal traversal, or database confidence score is inferred."
        ),
        "species_context": "mouse cardiomyocytes and perfused mouse hearts",
        "cell_type_context": "primary cardiac myocytes and isolated perfused hearts",
        "assay": "adiponectin stimulation; ADIPOR1/APPL1 co-immunoprecipitation; AMPK and ACC phosphorylation; fatty-acid uptake and oxidation assays",
        "effect_polarity": "activating",
    },
    {
        "suffix": "ADIPOR2-PPARA",
        "lr_edge_id": "M20B-E002473",
        "relay_node_id": "NODE00306",
        "tf_node_id": "NODE09191",
        "path_expression": "ligand>receptor>intracellular>TF>output",
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|target_gene_expression",
        "output_label": "PPARalpha-associated fatty-acid oxidation and lipid-metabolism program",
        "pathway_name": "ADIPOQ-ADIPOR2-APPL1-Src-Ras-ERK-PPARalpha-output",
        "locators": "PMID:18842004; PMCID:PMC2665882",
        "summary": (
            "Primary adiponectin-receptor studies report that adiponectin activates ERK1/2 through an APPL1- and "
            "Src/Ras-associated pathway, with ADIPOR2 preferentially associated with PPARalpha signaling and lipid "
            "oxidation. The route retains the ADIPOR2 relay, PPARalpha transcription-factor layer, and measured "
            "metabolic output as a composed evidence route."
        ),
        "limitations": (
            "The receptor, relay, PPARalpha, and metabolic-output observations come from complementary vascular, "
            "hepatic, and heterologous systems; the source does not establish every handoff in one cell state or a "
            "terminal PPARalpha target gene. No new causal graph edge, SCI transfer, or database confidence score is inferred."
        ),
        "species_context": "human and mouse comparator systems",
        "cell_type_context": "primary vascular smooth-muscle cells, endothelial cells, hepatocytes, and receptor-expressing HEK293 cells",
        "assay": "adiponectin stimulation; ADIPOR1/2 perturbation; APPL1, Src/Ras and ERK1/2 assays; PPARalpha and lipid-oxidation readouts",
        "effect_polarity": "activating",
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
        lr = edges[spec["lr_edge_id"]]
        if lr["source_node_id"] != "NODE00299":
            raise ValueError(f"Unexpected adiponectin ligand endpoint for {spec['suffix']}")
        for node_id in (lr["source_node_id"], lr["target_node_id"], spec["relay_node_id"]):
            if node_id not in nodes:
                raise ValueError(f"{spec['suffix']}: missing node {node_id}")
        if spec["tf_node_id"] and spec["tf_node_id"] not in nodes:
            raise ValueError(f"{spec['suffix']}: missing TF node {spec['tf_node_id']}")
        expansion_id = f"M21B-LITEXP-ADIPOQ-{spec['suffix']}-001"
        tf = nodes.get(spec["tf_node_id"], {})
        rows.append(
            {
                "expansion_id": expansion_id,
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": spec["path_expression"],
                "route_tier": spec["route_tier"],
                "known_layers": spec["known_layers"],
                "missing_layers": spec["missing_layers"],
                "intracellular_status": "source_supported_composed",
                "ligand_node_id": lr["source_node_id"],
                "ligand_label": nodes[lr["source_node_id"]]["canonical_label"],
                "ligand_receptor_edge_id": spec["lr_edge_id"],
                "receptor_node_id": lr["target_node_id"],
                "receptor_label": nodes[lr["target_node_id"]]["canonical_label"],
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": spec["relay_node_id"],
                "intracellular_continuation_label": nodes[spec["relay_node_id"]]["canonical_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": spec["tf_node_id"],
                "transcription_factor_label": tf.get("canonical_label", ""),
                "tf_target_edge_id": "",
                "target_gene_node_id": "",
                "target_gene_label": "",
                "target_output_form_id": "",
                "output_node_id": "",
                "output_label": spec["output_label"],
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": spec["pathway_name"],
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_functional_output",
                "evidence_ids": unique_join(lr.get("evidence_ids", ""), spec["locators"]),
                "source_chain_id": expansion_id,
                "source_evidence_record_id": "",
                "route_linkage_status": (
                    "manual_primary_adiponectin_adipor_route;graph_linked_route_source;primary_layer_linked;"
                    "receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;"
                    "target_gene_expression_unresolved;evidence_route_only"
                ),
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "generic_functional_readout",
                "primary_locator": spec["locators"],
                "citation_note": "Primary-evidence adiponectin receptor route overlay; unresolved handoffs remain explicit and no graph edge, causal assertion, or confidence score is created.",
                "evidence_summary": spec["summary"],
                "limitations": spec["limitations"],
                "curation_status": "curated_primary_route",
                "species_context": spec["species_context"],
                "cell_type_context": spec["cell_type_context"],
                "compartment_context": "extracellular adiponectin; plasma-membrane adiponectin receptor; cytoplasmic adaptor/kinase relay; metabolic output context",
                "injury_context": "no SCI transfer inferred; primary metabolic model context only",
                "context_scope": "composite_primary_evidence; route layers retain source-specific models",
                "assay_or_perturbation": spec["assay"],
                "effect_polarity": spec["effect_polarity"],
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
    print(json.dumps({"rows": len(rows), "output": str(args.output.resolve())}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
