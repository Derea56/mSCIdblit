#!/usr/bin/env python3
"""Build a primary-literature acetylcholine/M1/ERK/EGR1 route overlay."""

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


def make_rows(bundle: Path) -> list[dict[str, str]]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    lr_edge_id = "M21B-E001347"
    relay_node_id = "NODE03364"
    tf_node_id = "NODE03137"
    output_node_id = "NODE06656"
    lr = edges[lr_edge_id]
    ligand = nodes[lr["source_node_id"]]
    receptor = nodes[lr["target_node_id"]]
    relay = nodes[relay_node_id]
    tf = nodes[tf_node_id]
    output = nodes[output_node_id]
    expansion_id = "M21B-LITEXP-ACETYLCHOLINEM1ERK-EGR1-001"
    primary_locator = "PMID:11922142; PMID:24023725; PMID:19187099; PMID:9789819"
    evidence_ids = unique_join(lr.get("evidence_ids", ""), primary_locator)
    return [
        {
            "expansion_id": expansion_id,
            "source_queue_id": "",
            "route_status": "retained_evidence_route",
            "path_expression": "ligand>receptor>intracellular>TF>output",
            "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
            "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
            "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|target_gene_expression",
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
            "target_gene_node_id": "",
            "target_gene_label": "",
            "target_output_form_id": "",
            "output_node_id": output_node_id,
            "output_label": "EGR1 transcription-factor induction",
            "output_form_id": "",
            "bridge_id": "",
            "pathway_name": "acetylcholine-CHRM1-ERK-EGR1",
            "input_evidence_type": "primary_literature_route_expansion",
            "output_evidence_type": "primary_transcription_factor_output",
            "evidence_ids": evidence_ids,
            "source_chain_id": expansion_id,
            "source_evidence_record_id": "",
            "route_linkage_status": (
                "manual_primary_acetylcholine_m1_erk_egr1_route;graph_linked_route_source;"
                "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
                "intracellular_to_tf_edge_not_asserted;target_gene_node_unresolved;"
                "evidence_route_only"
            ),
            "causal_status": "not_asserted",
            "traversal_status": "evidence_route_not_causal",
            "evidence_contract_version": "mechanism_evidence_v1",
            "evidence_polarity": "supports",
            "negative_evidence_status": "not_evaluated",
            "evidence_directness": "composite_primary_route",
            "output_class": "gene_expression_or_transcription",
            "primary_locator": primary_locator,
            "citation_note": (
                "Primary-evidence route overlay for acetylcholine/M1 muscarinic receptor/ERK-dependent EGR1 induction. "
                "The graph has no dedicated terminal AChE or EGR1 target-gene node for this route."
            ),
            "evidence_summary": (
                "Primary hippocampal-slice studies identify M1 receptors as the muscarinic subtype required for ERK "
                "activation. Independent primary M1-receptor studies report MEK/ERK-dependent EGR1 induction, while "
                "cholinergic neuroblastoma and muscarinic receptor studies report EGR1 transcription-factor induction "
                "and downstream promoter activity."
            ),
            "limitations": (
                "The receptor-to-ERK and ERK-to-EGR1 observations are composed across primary systems and agonist/model "
                "contexts. The current graph lacks a dedicated terminal target-gene node for this route, so EGR1 is kept "
                "as the TF/output layer; no SCI transfer, causal traversal or database confidence score is inferred."
            ),
            "curation_status": "curated_primary_route",
            "species_context": "mouse; human; rat",
            "cell_type_context": "Mouse hippocampal CA1 slices, human M1-expressing HEK293 cells, and cholinergic neuroblastoma model systems",
            "compartment_context": "extracellular acetylcholine; plasma-membrane CHRM1; cytoplasmic ERK signaling; nuclear EGR1 transcription-factor output",
            "injury_context": "no SCI transfer inferred; primary neuronal and receptor-expression model contexts only",
            "context_scope": "composite_primary_evidence",
            "assay_or_perturbation": "carbachol/acetylcholine stimulation; atropine and M1 antagonist/knockout controls; MEK/ERK inhibition; EGR1 mRNA/protein and promoter assays",
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
    print(json.dumps({"rows": len(rows), "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
