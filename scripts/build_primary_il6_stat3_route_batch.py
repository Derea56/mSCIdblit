#!/usr/bin/env python3
"""Build source-linked IL-6/IL-6R-gp130/JAK1/STAT3 target routes."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


TARGET_EDGES = (
    ("M21B-E008279", "SOCS3"),
    ("M21B-E008280", "MYC"),
    ("M21B-E008327", "CRP"),
    ("M21B-E008348", "LCN2"),
    ("M21B-E008403", "CEBPB"),
)
LR_EDGE_ID = "M21B-E001760"
RELAY_EDGE_ID = "M21B-E001716"
INTRACELLULAR_TF_EDGE_ID = "M21B-E011710"
TF_NODE_ID = "NODE10726"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def unique_join(values: list[str]) -> str:
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
    sources_by_edge: dict[str, list[str]] = {}
    for row in read_tsv(bundle / "mechanism_edge_sources.tsv"):
        sources_by_edge.setdefault(row["edge_id"], []).append(row.get("source_locator", ""))

    required_edges = {LR_EDGE_ID, RELAY_EDGE_ID, INTRACELLULAR_TF_EDGE_ID, *(edge_id for edge_id, _ in TARGET_EDGES)}
    missing_edges = sorted(required_edges - edges.keys())
    if missing_edges:
        raise ValueError(f"IL-6 route requires missing edges: {missing_edges}")
    required_nodes = {"NODE05231", "NODE05269", "NODE06016", TF_NODE_ID}
    required_nodes.update(edges[edge_id]["target_node_id"] for edge_id, _ in TARGET_EDGES)
    missing_nodes = sorted(required_nodes - nodes.keys())
    if missing_nodes:
        raise ValueError(f"IL-6 route requires missing nodes: {missing_nodes}")

    lr_edge = edges[LR_EDGE_ID]
    relay_edge = edges[RELAY_EDGE_ID]
    intracellular_tf_edge = edges[INTRACELLULAR_TF_EDGE_ID]
    if (lr_edge["source_node_id"], lr_edge["target_node_id"]) != ("NODE05231", "NODE05269"):
        raise ValueError("Unexpected IL-6 ligand/receptor endpoints")
    if (relay_edge["source_node_id"], relay_edge["target_node_id"]) != ("NODE05269", "NODE06016"):
        raise ValueError("Unexpected IL-6 receptor/JAK1 endpoints")
    if (intracellular_tf_edge["source_node_id"], intracellular_tf_edge["target_node_id"]) != ("NODE06016", TF_NODE_ID):
        raise ValueError("Unexpected IL-6 JAK1/STAT3 endpoints")

    receptor = nodes[lr_edge["target_node_id"]]
    relay = nodes[relay_edge["target_node_id"]]
    tf = nodes[TF_NODE_ID]
    base_locators = [
        *sources_by_edge.get(LR_EDGE_ID, []),
        *sources_by_edge.get(RELAY_EDGE_ID, []),
        *sources_by_edge.get(INTRACELLULAR_TF_EDGE_ID, []),
    ]
    rows: list[dict[str, str]] = []
    for target_edge_id, target_slug in TARGET_EDGES:
        target_edge = edges[target_edge_id]
        target = nodes[target_edge["target_node_id"]]
        locators = unique_join(base_locators + sources_by_edge.get(target_edge_id, []))
        evidence_ids = unique_join(
            [
                LR_EDGE_ID,
                lr_edge.get("evidence_ids", ""),
                RELAY_EDGE_ID,
                relay_edge.get("evidence_ids", ""),
                INTRACELLULAR_TF_EDGE_ID,
                intracellular_tf_edge.get("evidence_ids", ""),
                target_edge_id,
                target_edge.get("evidence_ids", ""),
                locators,
            ]
        )
        expansion_id = f"M21B-LITEXP-IL6-JAK1-STAT3-{target_slug}"
        rows.append(
            {
                "expansion_id": expansion_id,
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "explicit_ligand_receptor_intracellular_tf_target",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "",
                "intracellular_status": "explicit_receptor_proximal_edge",
                "ligand_node_id": "NODE05231",
                "ligand_label": "IL-6",
                "ligand_receptor_edge_id": LR_EDGE_ID,
                "receptor_node_id": receptor["node_id"],
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": RELAY_EDGE_ID,
                "intracellular_continuation_node_id": relay["node_id"],
                "intracellular_continuation_label": relay["canonical_label"],
                "intracellular_tf_edge_id": INTRACELLULAR_TF_EDGE_ID,
                "transcription_factor_node_id": TF_NODE_ID,
                "transcription_factor_label": tf["canonical_label"],
                "tf_target_edge_id": target_edge_id,
                "target_gene_node_id": target["node_id"],
                "target_gene_label": target["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": target["node_id"],
                "output_label": f"{target_slug} gene expression",
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": f"IL6-IL6R-gp130-JAK1-STAT3-{target_slug}",
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": evidence_ids,
                "source_evidence_record_id": "",
                "route_linkage_status": "graph_linked_route_source;manual_primary_il6_stat3_route;direct_receptor_to_jak1_edge;direct_jak1_to_stat3_edge;direct_stat3_to_target_edge;evidence_route_only",
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "gene_expression_or_transcription",
                "primary_locator": locators,
                "citation_note": "Direct graph-linked IL-6 receptor, JAK1, STAT3, and target-gene edges are retained with their primary source locators; this route is a composed evidence annotation rather than a single-paper end-to-end assertion.",
                "evidence_summary": f"Primary sources support IL-6 engagement of the IL-6R/gp130 complex, JAK1 and STAT3 signaling, and STAT3-associated {target_slug} transcriptional regulation. The route makes the ordered intermediate sequence explicit for mSCS plausibility analysis.",
                "limitations": "The receptor-proximal, kinase, STAT3, and target-gene studies use complementary primary systems and do not establish a single-cell, single-paper end-to-end chain for every target. Preserve target-specific cell and species context; no SCI transfer, confidence score, or causal traversal is inferred.",
                "curation_status": "curated_primary_route",
                "species_context": "human; mouse comparator systems as stated in primary studies",
                "cell_type_context": "Primary cytokine-responsive hematopoietic, hepatocyte, epithelial, and inflammatory cell systems represented by the source records.",
                "compartment_context": "extracellular IL-6; plasma-membrane IL-6R/gp130; cytoplasmic JAK1/STAT3 relay; nuclear target-gene regulation",
                "injury_context": "no SCI transfer inferred; primary cytokine signaling contexts only",
                "context_scope": "composite primary evidence; target-specific source contexts retained",
                "assay_or_perturbation": "IL-6 stimulation, receptor-proximal kinase signaling, STAT3 phosphorylation or DNA-binding, target-gene promoter/occupancy or expression assays, and pathway perturbation where reported",
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
    args.output.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
