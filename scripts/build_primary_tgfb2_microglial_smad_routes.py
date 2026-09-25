#!/usr/bin/env python3
"""Build TGFB2/TGFBR/SMAD microglial target-gene route overlays."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


TARGETS = (
    ("CX3CR1", "NODE02617", "M21B-E008812", "M21B-EVID-008758"),
    ("TMEM119", "NODE11222", "M21B-E008813", "M21B-EVID-008759"),
    ("P2RY12", "NODE08685", "M21B-E008819", "M21B-EVID-008765"),
    ("SALL1", "NODE10025", "M21B-E008820", "M21B-EVID-008766"),
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
    ligand_id = "NODE11008"
    receptor_id = "NODE11016"
    relay_id = "NODE10459"
    tf_id = "NODE10462"
    lr_edge_id = "M21B-E000341"
    required = [ligand_id, receptor_id, relay_id, tf_id]
    missing = [node_id for node_id in required if node_id not in nodes]
    if missing:
        raise ValueError(f"TGFB2-microglial-SMAD-routes: missing nodes {missing}")
    lr = edges.get(lr_edge_id)
    if not lr or (lr["source_node_id"], lr["target_node_id"]) != (ligand_id, receptor_id):
        raise ValueError("TGFB2-microglial-SMAD-routes: ligand-receptor endpoints do not match")

    rows: list[dict[str, str]] = []
    for index, (label, target_id, output_edge_id, evidence_id) in enumerate(TARGETS, start=1):
        if target_id not in nodes or output_edge_id not in edges:
            raise ValueError(f"TGFB2-microglial-SMAD-routes: missing target or output edge for {label}")
        output_edge = edges[output_edge_id]
        if (output_edge["source_node_id"], output_edge["target_node_id"]) != (ligand_id, target_id):
            raise ValueError(f"TGFB2-microglial-SMAD-routes: output edge endpoints do not match {label}")
        expansion_id = f"M21B-LITEXP-TGFB2-TGFBR-SMAD23-{label}-001"
        locators = "PMID:31653855; PMCID:PMC6857135"
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
                "ligand_node_id": ligand_id,
                "ligand_label": nodes[ligand_id]["canonical_label"],
                "ligand_receptor_edge_id": lr_edge_id,
                "receptor_node_id": receptor_id,
                "receptor_label": nodes[receptor_id]["canonical_label"],
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": relay_id,
                "intracellular_continuation_label": nodes[relay_id]["canonical_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": tf_id,
                "transcription_factor_label": nodes[tf_id]["canonical_label"],
                "tf_target_edge_id": "",
                "target_gene_node_id": target_id,
                "target_gene_label": nodes[target_id]["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": target_id,
                "output_label": f"{label} microglial homeostasis-marker expression",
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": f"TGFB2-TGFBR1/2-SMAD2/3-SMAD4-{label}",
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": unique_join(lr.get("evidence_ids", ""), output_edge.get("evidence_ids", ""), evidence_id, locators),
                "source_chain_id": expansion_id,
                "source_evidence_record_id": "",
                "route_linkage_status": (
                    "manual_primary_tgfb2_microglial_smad_route;graph_linked_route_source;primary_layer_linked;"
                    "receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;"
                    "tf_to_target_edge_not_asserted;microglial_homeostasis_output_source_linked;evidence_route_only"
                ),
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression",
                "primary_locator": locators,
                "citation_note": (
                    "Primary microglial experiments report TGF-beta2/TGFBR2-dependent SMAD2 phosphorylation and "
                    f"{label} qPCR expression; receptor and SMAD2/3-SMAD4 layers are retained from the graph evidence layer."
                ),
                "evidence_summary": (
                    f"Primary primary-microglial and BV2 experiments support TGF-beta2/TGFBR2 signaling, SMAD2 activation, "
                    f"and {label} expression associated with microglial homeostasis. The route composes the ligand/receptor, "
                    "SMAD2/3-SMAD4, transcription-factor, and target-gene layers while keeping graph handoffs explicit."
                ),
                "limitations": (
                    "The cited study uses primary microglia and BV2 cells with TGFBR1/2 inhibition or TGFBR2 knockdown; "
                    "it reports SMAD2 phosphorylation and target-gene expression but does not establish direct promoter "
                    "occupancy by the SMAD2/3-SMAD4 complex. No causal traversal, graph edge, SCI transfer, or confidence "
                    "score is inferred."
                ),
                "curation_status": "curated_primary_route",
                "species_context": "mouse",
                "cell_type_context": "Primary mouse microglia and BV2 microglial cells",
                "compartment_context": "extracellular TGFB2; plasma-membrane TGFBR complex; cytoplasmic SMAD2/3 signaling; nuclear target-gene regulation",
                "injury_context": "no SCI transfer inferred; primary microglial homeostasis model context only",
                "context_scope": "primary ligand-specific microglial evidence with graph-linked receptor and relay context",
                "assay_or_perturbation": "TGF-beta2 stimulation; TGFBR1/2 inhibitor; TGFBR2 knockdown; SMAD2 phosphorylation; target-gene qPCR",
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
