#!/usr/bin/env python3
"""Build a primary-literature PTN/PTPRZ1 intracellular route overlay."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPEC = {
    "expansion_id": "M21B-LITEXP-PTN-PTPRZ1-FYN-AKT-GSC-MAINTENANCE",
    "ligand_node_id": "NODE09470",
    "lr_edge_id": "M20B-E004666",
    "relay_node_id": "NODE00423",
    "pathway_name": "PTN-PTPRZ1-Fyn-AKT-GSC-maintenance",
    "primary_locator": "PMID:28569747",
    "evidence_ids": "M20B-E004666;M20B-EVID-004666",
    "evidence_summary": (
        "A primary glioblastoma study reports that recombinant PTN promotes glioma stem-cell proliferation and "
        "self-renewal through PTPRZ1. PTN stimulation increases AKT phosphorylation, PTPRZ1 associates with Fyn, "
        "and PTN-induced SFK/Fyn activation is reduced by PTPRZ1 blockade. The route retains the graph-linked "
        "PTN-Ptprz1 pair and AKT1 as the intracellular continuation."
    ),
    "limitations": (
        "The study uses human glioblastoma stem cells and xenograft models rather than an SCI receiver state and "
        "does not establish a transcription factor or target gene. Fyn-to-AKT ordering and the full downstream "
        "stemness program remain source-composed evidence; no causal graph edge or confidence score is created."
    ),
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
    return {
        "expansion_id": SPEC["expansion_id"],
        "source_queue_id": "",
        "route_status": "retained_evidence_route",
        "path_expression": "ligand>receptor>intracellular>output",
        "route_tier": "ligand_receptor_intracellular_output_missing_tf",
        "known_layers": "ligand|receptor|intracellular_continuation|output",
        "missing_layers": "receptor_to_intracellular_edge|transcription_factor|target_gene_expression",
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
        "transcription_factor_node_id": "",
        "transcription_factor_label": "",
        "tf_target_edge_id": "",
        "target_gene_node_id": "",
        "target_gene_label": "",
        "target_output_form_id": "",
        "output_node_id": "",
        "output_label": "AKT-dependent glioma stem-cell proliferation and self-renewal",
        "output_form_id": "",
        "bridge_id": "",
        "pathway_name": SPEC["pathway_name"],
        "input_evidence_type": "primary_literature_route_expansion",
        "output_evidence_type": "primary_functional_output",
        "evidence_ids": unique_join(lr.get("evidence_ids", ""), SPEC["evidence_ids"], SPEC["primary_locator"]),
        "source_chain_id": SPEC["expansion_id"],
        "source_evidence_record_id": "",
        "route_linkage_status": (
            "manual_primary_ptn_ptprz1_fyn_akt_gsc_maintenance_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;transcription_factor_unresolved;"
            "target_gene_expression_unresolved;evidence_route_only"
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
        "species_context": "human; mouse xenograft",
        "cell_type_context": "human glioblastoma stem cells and intracranial mouse xenograft models",
        "compartment_context": "extracellular ligand; cell-surface PTPRZ1; Fyn-AKT intracellular signaling; stem-cell functional output",
        "injury_context": "glioblastoma comparator; SCI transfer is not inferred",
        "context_scope": "composite_primary_evidence; route layers retain source-specific models",
        "assay_or_perturbation": "recombinant PTN; PTPRZ1 shRNA or antibody blockade; Fyn co-immunoprecipitation; SFK/Fyn and AKT phosphorylation; glioma stem-cell viability, limiting dilution, tumorsphere and xenograft assays",
        "effect_polarity": "activating",
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
