#!/usr/bin/env python3
"""Build bounded IL-15/JAK/STAT5 evidence routes from primary studies."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


BRANCHES = [
    ("JAK1", "M21B-E011507", "NODE06016", "JAK1"),
    ("JAK3", "M21B-E011508", "NODE06031", "JAK3"),
]


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
    required_nodes = {"NODE05324", "NODE05326", "NODE06016", "NODE06031", "NODE10752", "NODE05331"}
    missing_nodes = sorted(required_nodes - nodes.keys())
    if missing_nodes:
        raise ValueError(f"IL-15 route requires missing nodes: {missing_nodes}")

    lr_edge_id = "M21B-E000246"
    tf_target_edge_id = "M21B-E008925"
    lr_edge = edges[lr_edge_id]
    tf_target_edge = edges[tf_target_edge_id]
    if (lr_edge["source_node_id"], lr_edge["target_node_id"]) != ("NODE05324", "NODE05326"):
        raise ValueError("Unexpected IL-15 receptor endpoints")
    if (tf_target_edge["source_node_id"], tf_target_edge["target_node_id"]) != ("NODE10752", "NODE05331"):
        raise ValueError("Unexpected STAT5/IL17A endpoints")
    for _name, edge_id, node_id, _label in BRANCHES:
        edge = edges[edge_id]
        if (edge["source_node_id"], edge["target_node_id"]) != ("NODE05326", node_id):
            raise ValueError(f"Unexpected IL-15 receptor/JAK endpoints for {_name}")

    locators = "PMID:7568001; PMCID:PMC41035; PMID:22993203; PMCID:PMC3647038; PMID:8530383"
    rows: list[dict[str, str]] = []
    for index, (branch_name, relay_edge_id, relay_node_id, relay_label) in enumerate(BRANCHES, start=1):
        expansion_id = f"M21B-LITEXP-IL15-{index:03d}"
        evidence_ids = unique_join(
            [
                lr_edge_id,
                relay_edge_id,
                tf_target_edge_id,
                "M21B-EVID-000189",
                "M21B-EVID-010819",
                "M21B-EVID-008871",
                "PMID:7568001",
                "PMID:22993203",
            ]
        )
        rows.append(
            {
                "expansion_id": expansion_id,
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "intracellular_to_tf_edge",
                "intracellular_status": "source_supported",
                "ligand_node_id": "NODE05324",
                "ligand_label": "IL15",
                "ligand_receptor_edge_id": lr_edge_id,
                "receptor_node_id": "NODE05326",
                "receptor_label": "IL15RA:IL2RB:IL2RG receptor complex",
                "receptor_intracellular_edge_id": relay_edge_id,
                "intracellular_continuation_node_id": relay_node_id,
                "intracellular_continuation_label": relay_label,
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": "NODE10752",
                "transcription_factor_label": "STAT5",
                "tf_target_edge_id": tf_target_edge_id,
                "target_gene_node_id": "NODE05331",
                "target_gene_label": "IL17A gene",
                "output_node_id": "NODE05331",
                "output_label": "IL17A gene expression/repression",
                "pathway_name": f"IL15-IL15R-{relay_label}-STAT5-IL17A",
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_il15_stat5_target_locus_evidence",
                "evidence_ids": evidence_ids,
                "source_chain_id": expansion_id,
                "source_evidence_record_id": "",
                "route_linkage_status": "graph_linked_route_source;manual_primary_il15_route;receptor_proximal_and_tf_output_evidence_composed;intracellular_to_tf_edge_not_asserted;tf_to_target_edge_asserted_graph_evidence;evidence_route_only",
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression",
                "primary_locator": locators,
                "citation_note": "Composite primary route annotation: IL-15/receptor, JAK1 or JAK3, STAT5 activation, and STAT5 occupancy at the Il17 locus are retained as source-linked layers; the missing kinase-to-STAT5 handoff remains explicit.",
                "evidence_summary": f"Primary evidence supports IL-15 engagement of the common IL-15 receptor complex, the {relay_label} branch, IL-15-induced STAT5 activation, and STAT5 binding at the Il17A locus associated with reduced IL-17A production. The route is composed from independently bounded source layers.",
                "limitations": f"The {relay_label} receptor-proximal branch and STAT5/Il17A output are supported by primary studies, but no single cited experiment establishes the exact IL-15R-to-{relay_label}-to-STAT5-to-Il17A sequence as one direct molecular chain. The STAT5-to-Il17A relation is inhibitory in the cited Th17 context and may be cell-state dependent; no SCI receiver-cell transfer is inferred.",
                "curation_status": "curated_primary_route",
                "species_context": "human; mouse as stated in primary model/assay",
                "cell_type_context": "Human T-cell cytokine signaling assays and mouse CD4 T-cell/Th17 cultures with IL-15 receptor perturbation and STAT5 chromatin-binding measurements.",
                "compartment_context": "extracellular cytokine; plasma membrane receptor complex; cytoplasm; nucleus; Il17A regulatory locus",
                "injury_context": "no SCI transfer inferred; primary lymphocyte model context only",
                "context_scope": "composite primary evidence; route layers retain source-specific models",
                "assay_or_perturbation": "IL-15 stimulation and receptor-loss/neutralization assays, JAK/STAT phosphorylation measurements, STAT5 chromatin immunoprecipitation at the Il17 locus, and IL-17A production assays.",
                "effect_polarity": "inhibitory",
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
