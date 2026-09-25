#!/usr/bin/env python3
"""Build a primary-evidence FAM3C/ILEI-LIFR-STAT3-SOCS3 route."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPEC = {
    "lr_edge_id": "M21B-E005616",
    "relay_node_id": "NODE06016",
    "tf_node_id": "NODE10726",
    "target_node_id": "NODE10509",
    "primary_locator": "PMID:30692635; PMID:37927213",
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
    ligand = nodes[lr["source_node_id"]]
    receptor = nodes[lr["target_node_id"]]
    relay = nodes[SPEC["relay_node_id"]]
    tf = nodes[SPEC["tf_node_id"]]
    target = nodes[SPEC["target_node_id"]]
    return {
        "expansion_id": "M21B-LITEXP-FAM3C-STAT3-SOCS3-001",
        "source_queue_id": "",
        "route_status": "retained_evidence_route",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "intracellular_status": "source_supported_composed",
        "ligand_node_id": lr["source_node_id"],
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
        "target_gene_node_id": SPEC["target_node_id"],
        "target_gene_label": target["canonical_label"],
        "target_output_form_id": "",
        "output_node_id": "",
        "output_label": "SOCS3 mRNA expression",
        "output_form_id": "",
        "bridge_id": "",
        "pathway_name": "FAM3C-ILEI-LIFR-JAK1-STAT3-SOCS3",
        "input_evidence_type": "primary_literature_route_expansion",
        "output_evidence_type": "primary_target_gene_expression",
        "evidence_ids": unique_join(lr.get("evidence_ids", ""), SPEC["primary_locator"]),
        "source_chain_id": "M21B-LITEXP-FAM3C-STAT3-SOCS3-001",
        "source_evidence_record_id": "",
        "route_linkage_status": (
            "manual_primary_fam3c_ilei_lifr_stat3_socs3_route;graph_linked_route_source;"
            "graph_linked_ligand_lifr_edge;primary_layer_linked;"
            "source_supported_lifr_stat3;graph_supported_stat3_target_gene;"
            "receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;"
            "tf_to_target_edge_not_asserted;end_to_end_chain_not_asserted_by_single_source;"
            "evidence_route_only"
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
            "Primary-evidence route overlay for FAM3C/ILEI-LIFR-JAK1-STAT3-SOCS3. "
            "The primary studies support LIFR-dependent STAT3 activation; the terminal SOCS3 layer is graph-supported."
        ),
        "evidence_summary": (
            "Primary mammary epithelial and breast-cancer studies support interaction of secreted FAM3C/ILEI "
            "with LIFR and LIFR-dependent STAT3 phosphorylation. The route composes that ligand-receptor/TF "
            "evidence with the exported JAK1 relay and STAT3-to-SOCS3 target-gene relation."
        ),
        "limitations": (
            "The primary studies do not demonstrate one end-to-end FAM3C-to-LIFR-to-JAK1-to-STAT3-to-SOCS3 "
            "experiment, and the terminal SOCS3 layer is supported by the existing graph relation rather than "
            "a FAM3C-specific target assay. Preserve the mammary epithelial/tumor context. No graph edge, "
            "causal traversal, or database confidence score is created."
        ),
        "curation_status": "curated_primary_route",
        "species_context": "human and mouse",
        "cell_type_context": "mammary epithelial and breast-cancer models",
        "compartment_context": "secreted ligand; LIFR cytokine-receptor complex; JAK/STAT intracellular relay; nuclear SOCS3 output",
        "injury_context": "no SCI transfer inferred; primary mammary/tumor model context only",
        "context_scope": "composite primary ligand-specific evidence plus graph-supported downstream target relation",
        "assay_or_perturbation": (
            "recombinant ILEI stimulation; LIFR immunoprecipitation or binding-region perturbation; "
            "STAT3 phosphorylation; RNAi and orthotopic mammary tumor assays"
        ),
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
    print(json.dumps({"output": str(args.output.resolve()), "rows": 1, "ligand": row["ligand_label"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
