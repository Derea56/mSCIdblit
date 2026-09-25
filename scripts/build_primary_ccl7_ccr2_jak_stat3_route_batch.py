#!/usr/bin/env python3
"""Build a primary CCL7--CCR2--JAK/STAT3 functional-output route.

This is an evidence-layer overlay.  The primary study reports CCL7/CCR2
binding, JAK/STAT3 activation, and reactivation of dormant colorectal-cancer
cells, but it does not establish a terminal target-gene output or create
exported receptor-to-JAK or JAK-to-STAT3 graph edges.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


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

    ligand_node_id = "NODE01741"
    receptor_node_id = "NODE01767"
    relay_node_id = "NODE06023"
    tf_node_id = "NODE10726"
    lr_edge_id = "M21B-E000408"
    for node_id in (ligand_node_id, receptor_node_id, relay_node_id, tf_node_id):
        if node_id not in nodes:
            raise ValueError(f"required node is missing from bundle: {node_id}")
    if lr_edge_id not in edges:
        raise ValueError(f"required ligand-receptor edge is missing from bundle: {lr_edge_id}")
    lr_edge = edges[lr_edge_id]
    if (lr_edge["source_node_id"], lr_edge["target_node_id"]) != (ligand_node_id, receptor_node_id):
        raise ValueError("CCL7/CCR2 edge endpoint mismatch")

    return [
        {
            "expansion_id": "M21B-LITEXP-CCL7-CCR2-JAK-STAT3-001",
            "source_queue_id": "",
            "route_status": "retained_evidence_route",
            "path_expression": "ligand>receptor>intracellular>TF>output",
            "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
            "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
            "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|target_gene_expression",
            "intracellular_status": "source_supported_composed",
            "ligand_node_id": ligand_node_id,
            "ligand_label": nodes[ligand_node_id]["canonical_label"],
            "ligand_receptor_edge_id": lr_edge_id,
            "receptor_node_id": receptor_node_id,
            "receptor_label": nodes[receptor_node_id]["canonical_label"],
            "receptor_intracellular_edge_id": "",
            "intracellular_continuation_node_id": relay_node_id,
            "intracellular_continuation_label": nodes[relay_node_id]["canonical_label"],
            "intracellular_tf_edge_id": "",
            "transcription_factor_node_id": tf_node_id,
            "transcription_factor_label": nodes[tf_node_id]["canonical_label"],
            "tf_target_edge_id": "",
            "target_gene_node_id": "",
            "target_gene_label": "",
            "target_output_form_id": "",
            "output_node_id": "",
            "output_label": "reactivation of dormant colorectal-cancer micrometastatic cells",
            "output_form_id": "",
            "bridge_id": "",
            "pathway_name": "CCL7-CCR2-JAK-STAT3-dormant-cell-reactivation",
            "input_evidence_type": "primary_literature_route_expansion",
            "output_evidence_type": "primary_functional_output",
            "evidence_ids": unique_join(
                lr_edge.get("evidence_ids", ""),
                "PMID:33986252; PMCID:PMC8119947; DOI:10.1038/s41419-021-03698-5",
            ),
            "source_chain_id": "M21B-LITEXP-CCL7-CCR2-JAK-STAT3-001",
            "source_evidence_record_id": "",
            "route_linkage_status": (
                "manual_primary_ccl7_ccr2_jak_stat3_route;graph_linked_route_source;primary_layer_linked;"
                "receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;"
                "target_gene_expression_unresolved;evidence_route_only;"
                "primary_source_supports_ligand_receptor_relay_output"
            ),
            "causal_status": "not_asserted",
            "traversal_status": "evidence_route_not_causal",
            "evidence_contract_version": "mechanism_evidence_v1",
            "evidence_polarity": "supports",
            "negative_evidence_status": "not_evaluated",
            "evidence_directness": "composite_primary_route",
            "output_class": "generic_functional_readout",
            "primary_locator": "PMID:33986252; PMCID:PMC8119947; DOI:10.1038/s41419-021-03698-5",
            "citation_note": (
                "The primary study reports CCL7/CCR2 co-localization or binding, JAK/STAT3 pathway activation, "
                "and reactivation of dormant colorectal-cancer cells. It does not identify a terminal target gene."
            ),
            "evidence_summary": (
                "A primary colorectal-cancer study reports that CCL7 secreted by monocytic myeloid-derived "
                "suppressor cells binds CCR2 on dormant metastatic cells and stimulates the JAK/STAT3 pathway, "
                "with CCL7 treatment promoting dormant-cell reactivation and CCR2 blockade opposing the response."
            ),
            "limitations": (
                "The evidence comes from human colorectal-cancer cell models and mouse liver-micrometastasis "
                "models. The study reports a JAK/STAT3 pathway-level continuation rather than purified "
                "receptor-to-JAK or JAK-to-STAT3 biochemical edges, and the output is functional rather than "
                "a terminal target-gene expression measurement. No SCI transfer, causal graph edge, or confidence "
                "score is inferred."
            ),
            "curation_status": "curated_primary_route",
            "species_context": "human colorectal-cancer cells; mouse metastatic models",
            "cell_type_context": "dormant colorectal-cancer cells and monocytic myeloid-derived suppressor cells",
            "compartment_context": "extracellular CCL7; plasma-membrane CCR2; intracellular JAK/STAT3 pathway; cell-state output",
            "injury_context": "no SCI transfer inferred; cancer metastasis model context only",
            "context_scope": "primary model context; pathway-level relay bounded",
            "assay_or_perturbation": "recombinant CCL7; CCR2 co-localization/co-immunoprecipitation; CCR2 antagonist or silencing; phospho-JAK/STAT3 and dormant-cell proliferation assays",
            "effect_polarity": "activating",
            "source_scope": "composite_primary_evidence",
        }
    ]


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
