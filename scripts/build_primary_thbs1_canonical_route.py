#!/usr/bin/env python3
"""Build the canonical Thbs1 primary-literature route overlay."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPEC = {
    "expansion_id": "M21B-LITEXP-THBS1-CD36-TLR4-NFKB-TNF-CANONICAL",
    "ligand_node_id": "NODE11042",
    "lr_edge_id": "M20B-E002238",
    "relay_node_id": "NODE11180",
    "tf_node_id": "NODE07984",
    "target_gene_node_id": "NODE11249",
    "pathway_name": "THBS1-CD36-TLR4-MyD88-NF-kB-TNF-canonical",
    "primary_locator": "PMID:23954950",
    "evidence_ids": "M20B-E002238;M20B-EVID-002238",
    "evidence_summary": (
        "A primary macrophage study reports that recombinant or purified TSP1 stimulates TNF-alpha expression, "
        "TLR4 expression, and NF-kB activity. TSP1-induced TNF production is lost in TLR4-null macrophages and "
        "is attenuated by blocking the TSP1-CD36 association. The route retains the canonical Thbs1-Cd36 graph "
        "pair, the existing TLR4/MD2/MyD88/p38/NF-kB relay, NF-kB, and the TNF gene node."
    ),
    "limitations": (
        "The study uses mouse bone-marrow-derived and peritoneal macrophages rather than an SCI receiver state. "
        "The CD36-to-TLR4, TLR4-to-relay, and NF-kB-to-TNF handoffs remain evidence-layer composition; no causal "
        "graph edge or confidence score is created."
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
    tf = nodes[SPEC["tf_node_id"]]
    target_gene = nodes[SPEC["target_gene_node_id"]]
    return {
        "expansion_id": SPEC["expansion_id"],
        "source_queue_id": "",
        "route_status": "retained_evidence_route",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
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
        "target_gene_node_id": SPEC["target_gene_node_id"],
        "target_gene_label": target_gene["canonical_label"],
        "target_output_form_id": "",
        "output_node_id": "",
        "output_label": "TNF/TNF-alpha expression and release",
        "output_form_id": "",
        "bridge_id": "",
        "pathway_name": SPEC["pathway_name"],
        "input_evidence_type": "primary_literature_route_expansion",
        "output_evidence_type": "primary_target_gene_expression",
        "evidence_ids": unique_join(lr.get("evidence_ids", ""), SPEC["evidence_ids"], SPEC["primary_locator"]),
        "source_chain_id": SPEC["expansion_id"],
        "source_evidence_record_id": "",
        "route_linkage_status": (
            "manual_primary_thbs1_canonical_cd36_tlr4_nfkb_tnf_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;"
            "tf_to_target_edge_not_asserted;target_gene_expression_unresolved;evidence_route_only"
        ),
        "causal_status": "not_asserted",
        "traversal_status": "evidence_route_not_causal",
        "evidence_contract_version": "mechanism_evidence_v1",
        "evidence_polarity": "supports",
        "negative_evidence_status": "not_evaluated",
        "evidence_directness": "composite_primary_route",
        "output_class": "target_gene_expression",
        "primary_locator": SPEC["primary_locator"],
        "citation_note": (
            "Primary-evidence route overlay; supported layers are retained for mSCS plausibility, while unresolved "
            "handoffs remain explicit and no graph edge, causal assertion, or confidence score is created."
        ),
        "evidence_summary": SPEC["evidence_summary"],
        "limitations": SPEC["limitations"],
        "curation_status": "curated_primary_route",
        "species_context": "mouse; human TSP1 reagent",
        "cell_type_context": "mouse bone-marrow-derived macrophages and peritoneal macrophages",
        "compartment_context": "extracellular or matrix ligand; cell-surface receptor; intracellular signaling; nuclear target-gene output context",
        "injury_context": "primary model context; SCI transfer is not inferred",
        "context_scope": "composite_primary_evidence; route layers retain source-specific models",
        "assay_or_perturbation": "recombinant or purified human TSP1; TLR4-null macrophages; CD36-blocking peptide or antibody; TNF qPCR/ELISA; NF-kB activity assays",
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
