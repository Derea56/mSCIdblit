#!/usr/bin/env python3
"""Build a bounded GPNMB--CD44--p38/STAT3--IL33 evidence route.

The primary study reports the ligand-receptor interaction, pathway
phosphorylation readouts, and IL-33 expression in the same tumor-cell model.
The route intentionally leaves the p38-to-STAT3 and STAT3-to-IL33 handoffs
unasserted; it is an evidence-layer composition, not a causal graph edge.
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

    ligand_node_id = "NODE04368"
    receptor_node_id = "NODE01902"
    relay_node_id = "NODE06785"
    tf_node_id = "NODE10726"
    target_node_id = "NODE05469"
    lr_edge_id = "M21B-E004664"
    for node_id in (ligand_node_id, receptor_node_id, relay_node_id, tf_node_id, target_node_id):
        if node_id not in nodes:
            raise ValueError(f"required node is missing from bundle: {node_id}")
    if lr_edge_id not in edges:
        raise ValueError(f"required ligand-receptor edge is missing from bundle: {lr_edge_id}")
    lr_edge = edges[lr_edge_id]
    if (lr_edge["source_node_id"], lr_edge["target_node_id"]) != (ligand_node_id, receptor_node_id):
        raise ValueError("GPNMB/CD44 edge endpoint mismatch")

    return [
        {
            "expansion_id": "M21B-LITEXP-GPNMB-CD44-P38-STAT3-IL33-001",
            "source_queue_id": "",
            "route_status": "retained_evidence_route",
            "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
            "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
            "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
            "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
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
            "target_gene_node_id": target_node_id,
            "target_gene_label": nodes[target_node_id]["canonical_label"],
            "target_output_form_id": "",
            "output_node_id": target_node_id,
            "output_label": "IL33 gene expression",
            "output_form_id": "",
            "bridge_id": "",
            "pathway_name": "GPNMB-CD44-p38-STAT3-IL33",
            "input_evidence_type": "primary_literature_route_expansion",
            "output_evidence_type": "primary_target_gene_expression",
            "evidence_ids": unique_join(
                lr_edge.get("evidence_ids", ""),
                "PMID:32728200; PMCID:PMC8027814; DOI:10.1038/s41423-020-0501-0",
            ),
            "source_chain_id": "M21B-LITEXP-GPNMB-CD44-P38-STAT3-IL33-001",
            "source_evidence_record_id": "",
            "route_linkage_status": (
                "manual_primary_gpnmb_cd44_p38_stat3_il33_route;graph_linked_route_source;primary_layer_linked;"
                "parallel_receptor_proximal_alternative;receptor_to_intracellular_edge_not_asserted;"
                "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;"
                "evidence_route_only;primary_source_supports_ligand_receptor_pathway_output"
            ),
            "causal_status": "not_asserted",
            "traversal_status": "evidence_route_not_causal",
            "evidence_contract_version": "mechanism_evidence_v1",
            "evidence_polarity": "supports",
            "negative_evidence_status": "not_evaluated",
            "evidence_directness": "composite_primary_route",
            "output_class": "gene_expression_or_transcription",
            "primary_locator": "PMID:32728200; PMCID:PMC8027814; DOI:10.1038/s41423-020-0501-0",
            "citation_note": (
                "The primary study reports GPNMB binding to CD44, increased p38 and STAT3 phosphorylation, "
                "and GPNMB/CD44-associated IL-33 expression. Direct p38-to-STAT3 and STAT3-to-IL33 edges are "
                "not asserted."
            ),
            "evidence_summary": (
                "A primary mouse tumor study reports that soluble macrophage-derived GPNMB binds CD44 on tumor "
                "cells, increases p38 and STAT3 phosphorylation, and promotes IL-33 expression and release. "
                "The same GPNMB/CD44/IL-33 axis promotes tumor-cell spheroid formation and metastatic phenotypes."
            ),
            "limitations": (
                "The source uses primary methylcholanthrene-induced mouse sarcoma cells and mouse tumor models. "
                "p38 and STAT3 phosphorylation are reported as pathway readouts and may represent parallel or "
                "complementary branches; the study does not establish p38-to-STAT3 or STAT3 occupancy at the "
                "IL33 locus. No SCI transfer, causal graph edge, or confidence score is inferred."
            ),
            "curation_status": "curated_primary_route",
            "species_context": "mouse",
            "cell_type_context": "mouse primary methylcholanthrene-induced sarcoma cells and syngeneic tumor models",
            "compartment_context": "extracellular soluble GPNMB; plasma-membrane CD44; intracellular p38/STAT3 readouts; IL33 regulatory output",
            "injury_context": "no SCI transfer inferred; tumor model context only",
            "context_scope": "primary model context; parallel pathway layers bounded",
            "assay_or_perturbation": "recombinant GPNMB; CD44 blocking antibody; p38/STAT3 phosphorylation assays; IL33 qPCR/ELISA; tumor spheroid and metastasis assays",
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
