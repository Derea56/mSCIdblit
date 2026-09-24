#!/usr/bin/env python3
"""Build IL-20 receptor/STAT3 target-gene evidence routes."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROUTES = (
    ("IL20-type-I-CCL2", "M21B-E000744", "NODE05412", "IL20RA:IL20RB receptor complex", "M21B-E008892", "M21B-E008441", "CCL2", "PMID:22802649; PMID:12351624; PMID:35486004; PMCID:PMC9321592; DOI:10.1096/fj.202101800R"),
    ("IL20-type-I-HGF", "M21B-E000744", "NODE05412", "IL20RA:IL20RB receptor complex", "M21B-E008893", "M21B-E008301", "HGF", "PMID:22802649; PMID:12351624; PMID:17083366; PMID:35486004; PMCID:PMC9321592; DOI:10.1096/fj.202101800R"),
    ("IL20-type-II-CCL2", "M21B-E000746", "NODE05426", "IL22RA1:IL20RB receptor complex", "M21B-E008892", "M21B-E008441", "CCL2", "PMID:12351624; PMID:17083366; PMID:22802649; PMID:35486004; PMCID:PMC9321592; DOI:10.1096/fj.202101800R"),
    ("IL20-type-II-HGF", "M21B-E000746", "NODE05426", "IL22RA1:IL20RB receptor complex", "M21B-E008893", "M21B-E008301", "HGF", "PMID:12351624; PMID:17083366; PMID:22802649; PMID:35486004; PMCID:PMC9321592; DOI:10.1096/fj.202101800R"),
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def unique_join(values: list[str]) -> str:
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
    source_by_edge: dict[str, list[dict[str, str]]] = {}
    for source in read_tsv(bundle / "mechanism_edge_sources.tsv"):
        source_by_edge.setdefault(source["edge_id"], []).append(source)

    rows: list[dict[str, str]] = []
    for name, lr_edge_id, receptor_node_id, receptor_label, output_edge_id, tf_target_edge_id, target_hint, route_locators in ROUTES:
        lr_edge = edges[lr_edge_id]
        output_edge = edges[output_edge_id]
        tf_target_edge = edges[tf_target_edge_id]
        if (lr_edge["source_node_id"], lr_edge["target_node_id"]) != ("NODE05410", receptor_node_id):
            raise ValueError(f"{name}: unexpected receptor endpoints")
        if output_edge["source_node_id"] != "NODE05410" or tf_target_edge["source_node_id"] != "NODE10726":
            raise ValueError(f"{name}: unexpected output or TF endpoints")
        target = nodes[tf_target_edge["target_node_id"]]
        if target_hint.casefold() not in target["canonical_label"].casefold():
            raise ValueError(f"{name}: unexpected target node {target['canonical_label']}")
        locators = unique_join([
            route_locators,
            *(source.get("source_locator", "") for eid in (lr_edge_id, output_edge_id, tf_target_edge_id) for source in source_by_edge.get(eid, [])),
        ])
        evidence_ids = unique_join([
            lr_edge_id, output_edge_id, tf_target_edge_id,
            lr_edge.get("evidence_ids", ""), output_edge.get("evidence_ids", ""), tf_target_edge.get("evidence_ids", ""),
            locators,
        ])
        rows.append({
            "expansion_id": f"M21B-LITEXP-{name}-STAT3",
            "source_queue_id": "",
            "route_status": "retained_evidence_route",
            "path_expression": "ligand>receptor>????>TF>target_gene_expression",
            "route_tier": "ligand_receptor_tf_target_missing_intracellular",
            "known_layers": "ligand|receptor|transcription_factor|target_gene_expression",
            "missing_layers": "intracellular_continuation|receptor_to_intracellular_edge|intracellular_to_tf_edge",
            "intracellular_status": "not_mapped",
            "ligand_node_id": "NODE05410",
            "ligand_label": "IL20",
            "ligand_receptor_edge_id": lr_edge_id,
            "receptor_node_id": receptor_node_id,
            "receptor_label": receptor_label,
            "receptor_intracellular_edge_id": "",
            "intracellular_continuation_node_id": "",
            "intracellular_continuation_label": "",
            "intracellular_tf_edge_id": "",
            "transcription_factor_node_id": "NODE10726",
            "transcription_factor_label": "STAT3",
            "tf_target_edge_id": tf_target_edge_id,
            "target_gene_node_id": target["node_id"],
            "target_gene_label": target["canonical_label"],
            "output_node_id": target["node_id"],
            "output_label": f"{target['canonical_label']} expression",
            "pathway_name": f"{name}-STAT3-{target['canonical_label']}",
            "input_evidence_type": "primary_literature_route_expansion",
            "output_evidence_type": "primary_target_gene_expression",
            "evidence_ids": evidence_ids,
            "source_chain_id": f"M21B-LITEXP-{name}-STAT3",
            "source_evidence_record_id": "",
            "route_linkage_status": "graph_linked_route_source;manual_primary_il20_route;intracellular_continuation_not_asserted;receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;tf_to_target_edge_asserted_as_graph_edge;direct_ligand_output_retained_as_supporting_evidence;evidence_route_only",
            "causal_status": "not_asserted",
            "traversal_status": "evidence_route_not_causal",
            "evidence_contract_version": "mechanism_evidence_v1",
            "evidence_polarity": "supports",
            "negative_evidence_status": "not_evaluated",
            "evidence_directness": "composite_primary_route",
            "output_class": "target_gene_expression",
            "primary_locator": locators,
            "citation_note": "Composite primary route annotation. IL-20 receptor-complex evidence, STAT3 target-gene evidence, and direct IL-20-associated output are retained as separate layers; the intracellular continuation is not asserted.",
            "evidence_summary": f"Primary evidence supports IL-20 engagement of the {receptor_label}, IL-20-associated {target_hint} expression, and an existing STAT3-to-{target_hint} graph edge. The intracellular continuation remains unresolved.",
            "limitations": "The receptor and terminal output studies use complementary human keratinocyte/reconstitution contexts. The route is traversable as evidence, not as a causal chain; no SCI transfer or database confidence score is inferred.",
            "curation_status": "curated_primary_route",
            "species_context": "human; as stated in primary model/assay",
            "cell_type_context": "Primary human keratinocyte and receptor/reporter contexts from the cited studies.",
            "compartment_context": "extracellular cytokine; plasma membrane receptor complex; unresolved intracellular layer; nucleus; target-gene regulatory locus",
            "injury_context": "no SCI transfer inferred; primary model context only",
            "context_scope": "composite primary evidence; route layers retain source-specific models",
            "assay_or_perturbation": "IL-20 stimulation, receptor-complex/reporter assays, STAT3 target evidence, and target-gene expression measurements.",
            "effect_polarity": "activating",
            "source_scope": "composite_primary_evidence",
        })
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
