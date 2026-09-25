#!/usr/bin/env python3
"""Build a primary-literature SPP1/osteopontin route overlay."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPEC = {
    "expansion_id": "M21B-LITEXP-SPP1-ITGAVITGB3-PI3KAKTERK-NFKB-MIGRATION",
    "ligand_node_id": "NODE10627",
    "lr_edge_id": "M20B-E004975",
    "relay_node_id": "NODE08995",
    "tf_node_id": "NODE07984",
    "pathway_name": "SPP1-ITGAV-ITGB3-FAK-PI3K-AKT-ERK-NF-kB-migration",
    "path_expression": "ligand>receptor>intracellular>TF>output",
    "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
    "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
    "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|target_gene_expression",
    "output_label": "NF-kB-dependent lung-cancer-cell migration",
    "primary_locator": "PMID:18996613",
    "evidence_ids": "M20B-E004975;M20B-EVID-004975",
    "evidence_summary": (
        "A primary human lung-cancer-cell study reports that osteopontin signals through alphaVbeta3 integrin "
        "to activate FAK, PI3K, Akt, ERK, IKK, and NF-kB, with NF-kB inhibition or kinase inhibitors reducing "
        "osteopontin-induced migration. The route retains the graph-linked SPP1-alphaVbeta3 pair, PI3K-AKT1 "
        "as the intracellular continuation, NF-kB, and the measured migration output."
    ),
    "limitations": (
        "The study uses A549 lung-cancer cells and a migration assay rather than an SCI receiver state or a "
        "promoter-resolved target gene. FAK/PI3K/Akt/ERK and NF-kB handoffs remain evidence-layer composition; "
        "no causal edge or confidence score is created."
    ),
    "species_context": "human",
    "cell_type_context": "human A549 lung adenocarcinoma cells",
    "assay_or_perturbation": "osteopontin stimulation; PI3K, Akt, ERK, NF-kB, and IKK inhibitors; FAK, p85, Akt, and ERK mutants; kappaB-luciferase and migration assays",
    "effect_polarity": "activating",
}


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
    lr = edges[SPEC["lr_edge_id"]]
    ligand = nodes[SPEC["ligand_node_id"]]
    receptor = nodes[lr["target_node_id"]]
    relay = nodes[SPEC["relay_node_id"]]
    tf = nodes[SPEC["tf_node_id"]]
    return {
        "expansion_id": SPEC["expansion_id"],
        "source_queue_id": "",
        "route_status": "retained_evidence_route",
        "path_expression": SPEC["path_expression"],
        "route_tier": SPEC["route_tier"],
        "known_layers": SPEC["known_layers"],
        "missing_layers": SPEC["missing_layers"],
        "intracellular_status": "source_supported_composed",
        "ligand_node_id": SPEC["ligand_node_id"],
        "ligand_label": ligand["canonical_label"],
        "ligand_receptor_edge_id": SPEC["lr_edge_id"],
        "receptor_node_id": lr["target_node_id"],
        "receptor_label": receptor["canonical_label"],
        "receptor_intracellular_edge_id": "",
        "intracellular_continuation_node_id": SPEC["relay_node_id"],
        "intracellular_continuation_label": relay["canonical_label"],
        "intracellular_tf_edge_id": "",
        "transcription_factor_node_id": SPEC["tf_node_id"],
        "transcription_factor_label": tf["canonical_label"],
        "tf_target_edge_id": "",
        "target_gene_node_id": "",
        "target_gene_label": "",
        "target_output_form_id": "",
        "output_node_id": "",
        "output_label": SPEC["output_label"],
        "output_form_id": "",
        "bridge_id": "",
        "pathway_name": SPEC["pathway_name"],
        "input_evidence_type": "primary_literature_route_expansion",
        "output_evidence_type": "primary_functional_output",
        "evidence_ids": unique_join(lr.get("evidence_ids", ""), SPEC["evidence_ids"], SPEC["primary_locator"]),
        "source_chain_id": SPEC["expansion_id"],
        "source_evidence_record_id": "",
        "route_linkage_status": (
            "manual_primary_spp1_itgavitgb3_pi3kakterk_nfkb_migration_route;"
            "graph_linked_route_source;primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "intracellular_to_tf_edge_not_asserted;target_gene_expression_unresolved;evidence_route_only"
        ),
        "causal_status": "not_asserted",
        "traversal_status": "evidence_route_not_causal",
        "evidence_contract_version": "mechanism_evidence_v1",
        "evidence_polarity": "supports",
        "negative_evidence_status": "not_evaluated",
        "evidence_directness": "composite_primary_route",
        "output_class": "generic_functional_readout",
        "primary_locator": SPEC["primary_locator"],
        "citation_note": (
            "Primary-evidence route overlay; supported layers are retained for mSCS plausibility, while unresolved "
            "handoffs remain explicit and no graph edge, causal assertion, or confidence score is created."
        ),
        "evidence_summary": SPEC["evidence_summary"],
        "limitations": SPEC["limitations"],
        "curation_status": "curated_primary_route",
        "species_context": SPEC["species_context"],
        "cell_type_context": SPEC["cell_type_context"],
        "compartment_context": "extracellular ligand; cell-surface integrin; intracellular signaling; NF-kB and functional output context",
        "injury_context": "primary model context; SCI transfer is not inferred",
        "context_scope": "composite_primary_evidence; route layers retain source-specific models",
        "assay_or_perturbation": SPEC["assay_or_perturbation"],
        "effect_polarity": SPEC["effect_polarity"],
        "source_scope": "composite_primary_evidence",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.resolve().write_text(json.dumps([make_row(args.bundle.resolve())], indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": 1, "output": str(args.output.resolve())}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
