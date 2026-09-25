#!/usr/bin/env python3
"""Build a primary-literature Netrin-1/CD146 intracellular route overlay."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPEC = {
    "expansion_id": "M21B-LITEXP-NTN1-MCAM-GAI-GAB1-AKT-ERK-ANGIOGENESIS",
    "ligand_node_id": "NODE08407",
    "lr_edge_id": "M23B-E000985",
    "relay_node_id": "NODE08995",
    "pathway_name": "NTN1-MCAM-Galpha-i-Gab1-AKT-mTOR-ERK-angiogenesis",
    "primary_locator": "PMID:37153740",
    "evidence_ids": "M23B-E000985;M23B-EVID-001331",
    "evidence_summary": (
        "A primary study reports that Netrin-1 induces CD146 association with G-alpha-i1/3 and Gab1, followed by "
        "Akt-mTOR and Erk activation. CD146, Gab1, or G-alpha-i1/3 perturbation reduces Netrin-1-induced signaling, "
        "and the same pathway supports endothelial proliferation, migration, tube formation, and retinal angiogenesis. "
        "The route retains the graph-linked Netrin-1-CD146 pair and PI3K-AKT1 as the intracellular continuation."
    ),
    "limitations": (
        "The study uses endothelial, mouse embryonic fibroblast, and retinal angiogenesis systems rather than an SCI "
        "receiver state. PI3K-AKT1 represents the Akt/mTOR branch while ERK and the G-alpha-i/Gab1 handoffs remain "
        "source-composed evidence; no TF, target gene, causal graph edge, or confidence score is created."
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
        "output_label": "Akt-mTOR/ERK-dependent endothelial angiogenesis",
        "output_form_id": "",
        "bridge_id": "",
        "pathway_name": SPEC["pathway_name"],
        "input_evidence_type": "primary_literature_route_expansion",
        "output_evidence_type": "primary_functional_output",
        "evidence_ids": unique_join(lr.get("evidence_ids", ""), SPEC["evidence_ids"], SPEC["primary_locator"]),
        "source_chain_id": SPEC["expansion_id"],
        "source_evidence_record_id": "",
        "route_linkage_status": (
            "manual_primary_ntn1_mcam_gai_gab1_akt_erk_angiogenesis_route;graph_linked_route_source;"
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
        "species_context": "human; mouse",
        "cell_type_context": "human endothelial cells, mouse embryonic fibroblasts, and mouse retinal vascular systems",
        "compartment_context": "extracellular ligand; cell-surface CD146; G-alpha-i/Gab1 intracellular signaling; endothelial functional output",
        "injury_context": "retinal angiogenesis comparator; SCI transfer is not inferred",
        "context_scope": "composite_primary_evidence; route layers retain source-specific models",
        "assay_or_perturbation": "Netrin-1 stimulation; CD146, Gab1, and G-alpha-i1/3 silencing or knockout; Akt-mTOR and Erk phosphorylation; endothelial proliferation, migration, tube formation, and retinal angiogenesis assays",
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
