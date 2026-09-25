#!/usr/bin/env python3
"""Build primary-literature ephrin-A1/Eph intracellular route overlays."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROUTES = [
    {
        "expansion_id": "M21B-LITEXP-EFNA1-EPHA2-AKT-ERK-CORNEAL-MIGRATION-EFNA1",
        "ligand_node_id": "NODE03077",
        "lr_edge_id": "M21B-E000196",
        "relay_node_id": "NODE08995",
        "pathway_name": "EFNA1-EPHA2-PI3K-AKT-ERK-epithelial-migration",
        "primary_locator": "PMID:22247486",
        "output_label": "ephrin-A1/EphA2-dependent PI3K-Akt and ERK state with corneal epithelial migration",
        "evidence_ids": "M21B-E000196;M21B-EVID-000139",
        "evidence_summary": (
            "A primary corneal epithelial study reports that ephrin-A1-Fc targets EphA2, triggers receptor "
            "phosphorylation and downregulation, transiently reduces Akt and ERK1/2 activation, and restricts "
            "scratch-wound migration. PI3K-Akt blockade removes the ephrin-A1-dependent migration restriction. "
            "The route retains the graph-linked EFNA1/ephrin-A1-EphA2 pair and PI3K-AKT1 continuation."
        ),
        "limitations": (
            "The study uses human corneal epithelial cells rather than an SCI receiver state and does not establish "
            "a transcription factor or target gene. The receptor-to-PI3K/Akt handoff is retained as source-supported "
            "intracellular evidence; no causal graph edge or confidence score is created."
        ),
        "species_context": "human; mouse diabetic-corneal comparator",
        "cell_type_context": "primary and telomerase-immortalized human corneal epithelial cells",
        "compartment_context": "cell-surface EphA2; PI3K-Akt and MEK/ERK intracellular signaling; epithelial migration output",
        "injury_context": "corneal wound comparator; SCI transfer is not inferred",
        "assay_or_perturbation": "ephrin-A1-Fc; EphA2 modulation; PI3K and MEK inhibitors; Akt/ERK immunoblotting; scratch-wound migration",
    },
    {
        "expansion_id": "M21B-LITEXP-EFNA1-EPHA2-AKT-ERK-CORNEAL-MIGRATION-Efna1",
        "ligand_node_id": "NODE03076",
        "lr_edge_id": "M20B-E003285",
        "relay_node_id": "NODE08995",
        "pathway_name": "Efna1-Epha2-PI3K-AKT-ERK-epithelial-migration",
        "primary_locator": "PMID:22247486",
        "output_label": "ephrin-A1/EphA2-dependent PI3K-Akt and ERK state with corneal epithelial migration",
        "evidence_ids": "M20B-E003285;M20B-EVID-003285",
        "evidence_summary": (
            "A primary corneal epithelial study reports that ephrin-A1-Fc targets EphA2, triggers receptor "
            "phosphorylation and downregulation, transiently reduces Akt and ERK1/2 activation, and restricts "
            "scratch-wound migration. PI3K-Akt blockade removes the ephrin-A1-dependent migration restriction. "
            "The route retains the graph-linked Efna1-Epha2 pair and PI3K-AKT1 continuation."
        ),
        "limitations": (
            "The study uses human corneal epithelial cells rather than an SCI receiver state and does not establish "
            "a transcription factor or target gene. The receptor-to-PI3K/Akt handoff is retained as source-supported "
            "intracellular evidence; no causal graph edge or confidence score is created."
        ),
        "species_context": "human; mouse diabetic-corneal comparator",
        "cell_type_context": "primary and telomerase-immortalized human corneal epithelial cells",
        "compartment_context": "cell-surface EphA2; PI3K-Akt and MEK/ERK intracellular signaling; epithelial migration output",
        "injury_context": "corneal wound comparator; SCI transfer is not inferred",
        "assay_or_perturbation": "ephrin-A1-Fc; EphA2 modulation; PI3K and MEK inhibitors; Akt/ERK immunoblotting; scratch-wound migration",
    },
    {
        "expansion_id": "M21B-LITEXP-EFNA1-EPHA1-LCK-PYK2-PI3K-RHO-TCELL-MIGRATION",
        "ligand_node_id": "NODE03076",
        "lr_edge_id": "M20B-E003283",
        "relay_node_id": "NODE08995",
        "pathway_name": "Efna1-Epha1-Lck-Pyk2-PI3K-Vav1-Rho-T-cell-migration",
        "primary_locator": "PMID:17634955",
        "output_label": "ephrin-A1/Eph receptor-dependent CD8 T-cell migration",
        "evidence_ids": "M20B-E003283;M20B-EVID-003283",
        "evidence_summary": (
            "A primary human T-cell study reports that ephrin-A1 binding induces Lck phosphorylation and kinase "
            "activity, Pyk2 and Vav1 association, PI3K dependence, Rho-GTPase and ROCK involvement, and migration "
            "of CD8+CCR7+ lymphocytes. The route retains the graph-linked Efna1-Epha1 pair and PI3K-AKT1 as an "
            "intracellular continuation."
        ),
        "limitations": (
            "The study uses human CD8 T lymphocytes rather than an SCI receiver state and does not establish a "
            "transcription factor or target gene. The EphA1-to-PI3K/Rho handoff is retained as source-supported "
            "intracellular evidence; no causal graph edge or confidence score is created."
        ),
        "species_context": "human",
        "cell_type_context": "human CD8+CCR7+ T lymphocytes",
        "compartment_context": "cell-surface Eph receptor; Lck/Pyk2/PI3K/Vav1/Rho intracellular signaling; T-cell migration output",
        "injury_context": "immune-cell migration comparator; SCI transfer is not inferred",
        "assay_or_perturbation": "ephrin-A1 binding; Lck, PI3K and ROCK inhibition; kinase and association assays; lymphocyte migration assays",
    },
]


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


def make_row(bundle: Path, spec: dict[str, str]) -> dict[str, str]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    lr = edges[spec["lr_edge_id"]]
    ligand = nodes[spec["ligand_node_id"]]
    receptor = nodes[lr["target_node_id"]]
    relay = nodes[spec["relay_node_id"]]
    return {
        "expansion_id": spec["expansion_id"],
        "source_queue_id": "",
        "route_status": "retained_evidence_route",
        "path_expression": "ligand>receptor>intracellular>output",
        "route_tier": "ligand_receptor_intracellular_output_missing_tf",
        "known_layers": "ligand|receptor|intracellular_continuation|output",
        "missing_layers": "receptor_to_intracellular_edge|transcription_factor|target_gene_expression",
        "intracellular_status": "source_supported_composed",
        "ligand_node_id": spec["ligand_node_id"],
        "ligand_label": ligand["canonical_label"],
        "ligand_receptor_edge_id": spec["lr_edge_id"],
        "receptor_node_id": lr["target_node_id"],
        "receptor_label": receptor["canonical_label"],
        "receptor_intracellular_edge_id": "",
        "intracellular_continuation_node_id": spec["relay_node_id"],
        "intracellular_continuation_label": relay["canonical_label"],
        "intracellular_tf_edge_id": "",
        "transcription_factor_node_id": "",
        "transcription_factor_label": "",
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
        "evidence_ids": unique_join(lr.get("evidence_ids", ""), spec["evidence_ids"], spec["primary_locator"]),
        "source_chain_id": spec["expansion_id"],
        "source_evidence_record_id": "",
        "route_linkage_status": (
            "manual_primary_route;graph_linked_route_source;primary_layer_linked;"
            "receptor_to_intracellular_edge_not_asserted;transcription_factor_unresolved;"
            "target_gene_expression_unresolved;evidence_route_only"
        ),
        "causal_status": "not_asserted",
        "traversal_status": "evidence_route_not_causal",
        "evidence_contract_version": "mechanism_evidence_v1",
        "evidence_polarity": "supports",
        "negative_evidence_status": "not_evaluated",
        "evidence_directness": "composite_primary_route",
        "output_class": "generic_functional_readout",
        "primary_locator": spec["primary_locator"],
        "citation_note": (
            "Primary-evidence route overlay; supported layers are retained for mSCS plausibility, while unresolved "
            "handoffs remain explicit and no graph edge, causal assertion, or confidence score is created."
        ),
        "evidence_summary": spec["evidence_summary"],
        "limitations": spec["limitations"],
        "curation_status": "curated_primary_route",
        "species_context": spec["species_context"],
        "cell_type_context": spec["cell_type_context"],
        "compartment_context": spec["compartment_context"],
        "injury_context": spec["injury_context"],
        "context_scope": "composite_primary_evidence; route layers retain source-specific models",
        "assay_or_perturbation": spec["assay_or_perturbation"],
        "effect_polarity": "activating",
        "source_scope": "composite_primary_evidence",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    bundle = args.bundle.resolve()
    rows = [make_row(bundle, spec) for spec in ROUTES]
    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "output": str(args.output.resolve())}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
