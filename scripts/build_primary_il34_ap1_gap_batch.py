#!/usr/bin/env python3
"""Build a primary-literature route overlay for the IL-34 CSF1R/AP-1 gap."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


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


def make_row(bundle: Path) -> dict[str, str]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    lr = edges["M21B-E000121"]
    ligand = nodes[lr["source_node_id"]]
    receptor = nodes[lr["target_node_id"]]
    relay = nodes["NODE02515"]
    tf = nodes["NODE00609"]
    target = nodes["NODE02087"]
    expansion_id = "M21B-LITEXP-IL34GAP-001"
    return {
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
        "ligand_receptor_edge_id": "M21B-E000121",
        "receptor_node_id": lr["target_node_id"],
        "receptor_label": receptor["canonical_label"],
        "receptor_intracellular_edge_id": "",
        "intracellular_continuation_node_id": "NODE02515",
        "intracellular_continuation_label": relay["canonical_label"],
        "intracellular_tf_edge_id": "",
        "transcription_factor_node_id": "NODE00609",
        "transcription_factor_label": tf["canonical_label"],
        "tf_target_edge_id": "",
        "target_gene_node_id": "NODE02087",
        "target_gene_label": target["canonical_label"],
        "target_output_form_id": "",
        "output_node_id": "",
        "output_label": "c-FOS/cFos gene expression",
        "output_form_id": "",
        "bridge_id": "",
        "pathway_name": "IL34-CSF1R-MEK-ERK-JNK-AP1-cFOS",
        "input_evidence_type": "primary_literature_route_expansion",
        "output_evidence_type": "primary_target_gene_expression",
        "evidence_ids": unique_join(lr.get("evidence_ids", ""), "PMID:33800170"),
        "source_chain_id": expansion_id,
        "source_evidence_record_id": "",
        "route_linkage_status": (
            "manual_primary_il34_csf1r_mek_erk_jnk_ap1_cfos_route;graph_linked_route_source;"
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
        "primary_locator": "PMID:33800170",
        "citation_note": (
            "Primary-evidence route overlay for IL-34-CSF1R-MEK-ERK-JNK-AP1-cFOS. The source supports the receptor-linked "
            "kinase and AP-1 readouts, while graph handoffs remain explicit and no causal edge or confidence score is created."
        ),
        "evidence_summary": (
            "A primary IL-34 study reports CSF1R-dependent phosphorylation of MEK1/2, ERK1/2, JNK1/2, and c-Jun, increased "
            "c-Fos and c-Jun promoter activity, and increased AP-1 transactivation after IL-34 stimulation. The route retains "
            "the graph-linked CSF1R/ERK relay and c-FOS terminal expression layer."
        ),
        "limitations": (
            "The primary study uses epithelial and breast-cancer models and reports kinase phosphorylation and promoter/AP-1 "
            "readouts rather than one uninterrupted molecular chain. Direct CSF1R-to-relay, relay-to-AP-1, and AP-1-to-c-FOS "
            "graph edges remain unasserted; no SCI transfer is inferred."
        ),
        "curation_status": "curated_primary_route",
        "species_context": "mouse and human cell systems",
        "cell_type_context": "mouse JB6 Cl41 epidermal cells and human MCF7 breast-cancer cells",
        "compartment_context": "extracellular IL-34; plasma-membrane CSF1R; intracellular MEK/ERK/JNK relay; nuclear AP-1 promoter output",
        "injury_context": "no SCI transfer inferred; primary model context only",
        "context_scope": "single primary study; model-specific route evidence",
        "assay_or_perturbation": "IL-34 stimulation; CSF1R dependence; MEK1/2, ERK1/2, JNK1/2, and c-Jun phosphorylation; c-Fos/c-Jun promoter assays; AP-1 transactivation; PIN1 inhibition and silencing",
        "effect_polarity": "activating",
        "source_scope": "single_primary_study",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    row = make_row(args.bundle.resolve())
    args.output.resolve().write_text(json.dumps([row], indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": 1, "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
