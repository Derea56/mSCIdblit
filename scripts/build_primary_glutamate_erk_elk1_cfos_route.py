#!/usr/bin/env python3
"""Build a primary-literature glutamate ERK/Elk-1/c-Fos route overlay."""

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

    lr_edge_id = "M21B-E001350"
    relay_node_id = "NODE03370"
    tf_node_id = "NODE03164"
    target_node_id = "NODE02087"
    lr = edges[lr_edge_id]
    ligand = nodes[lr["source_node_id"]]
    receptor = nodes[lr["target_node_id"]]
    relay = nodes[relay_node_id]
    tf = nodes[tf_node_id]
    target = nodes[target_node_id]
    primary_locator = "PMID:8757255; PMID:10414964"

    return {
        "expansion_id": "M21B-LITEXP-GLUTAMATE-ERK-ELK1-CFOS-001",
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
        "intracellular_continuation_node_id": relay_node_id,
        "intracellular_continuation_label": relay["canonical_label"],
        "intracellular_tf_edge_id": "",
        "transcription_factor_node_id": tf_node_id,
        "transcription_factor_label": tf["canonical_label"],
        "tf_target_edge_id": "",
        "target_gene_node_id": target_node_id,
        "target_gene_label": target["canonical_label"],
        "target_output_form_id": "",
        "output_node_id": "",
        "output_label": "cFos gene expression",
        "output_form_id": "",
        "bridge_id": "",
        "pathway_name": "GLUTAMATE-NMDA-Ca2-ERK-Elk1-CFOS",
        "input_evidence_type": "primary_literature_route_expansion",
        "output_evidence_type": "primary_target_gene_expression",
        "evidence_ids": unique_join(lr.get("evidence_ids", ""), primary_locator),
        "source_chain_id": "manual_primary_glutamate_nmda_ca2_erk_elk1_cfos",
        "source_evidence_record_id": "",
        "route_linkage_status": (
            "manual_primary_glutamate_nmda_ca2_erk_elk1_cfos_route;graph_linked_route_source;"
            "primary_layers_source_linked;receptor_to_intracellular_edge_not_asserted;"
            "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;"
            "end_to_end_chain_not_asserted_by_single_source;evidence_route_only"
        ),
        "causal_status": "not_asserted",
        "traversal_status": "evidence_route_not_causal",
        "evidence_contract_version": "mechanism_evidence_v1",
        "evidence_polarity": "supports",
        "negative_evidence_status": "not_evaluated",
        "evidence_directness": "composite_primary_route",
        "output_class": "target_gene_expression",
        "primary_locator": primary_locator,
        "citation_note": (
            "Primary-evidence route overlay for glutamate/NMDA receptor signaling through ERK and Elk-1 to c-Fos. "
            "Unresolved handoffs remain explicit; no graph edge, causal assertion, or confidence score is created."
        ),
        "evidence_summary": (
            "A primary cortical-neuron study reports calcium influx through NMDA receptors, ERK-dependent Elk-1 "
            "phosphorylation, and glutamate-induced c-fos transcription through the serum-response element. A separate "
            "primary striatal-neuron study supports glutamate/NMDA-dependent calcium, CREB, and c-fos responses, "
            "providing complementary context for the retained receptor-to-output route."
        ),
        "limitations": (
            "The route composes complementary cortical and striatal primary-neuron studies. The exact receptor-to-ERK, "
            "ERK-to-Elk-1, and Elk-1-to-c-Fos handoffs are not asserted as graph edges or as one end-to-end chain by a "
            "single source; no SCI transfer is inferred."
        ),
        "curation_status": "curated_primary_route",
        "species_context": "rat",
        "cell_type_context": "primary rat cortical and striatal neurons",
        "compartment_context": "extracellular ligand; plasma-membrane NMDA receptor; intracellular signaling; nuclear gene-expression context",
        "injury_context": "no SCI transfer inferred; primary neuronal model context only",
        "context_scope": "composite primary evidence; route layers retain source-specific models",
        "assay_or_perturbation": "glutamate/NMDA stimulation; ERK phosphorylation; Elk-1 phosphorylation; c-fos serum-response-element transcription; calcium and CREB assays",
        "effect_polarity": "activating",
        "source_scope": "composite_primary_evidence",
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
