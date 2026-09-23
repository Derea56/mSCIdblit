#!/usr/bin/env python3
"""Build source-linked IL-4 JAK3/STAT6 parallel route annotations."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


TARGETS = (
    ("M21B-E008263", "GATA3", "PMID:20956546; PMCID:PMC2964576"),
    ("M21B-E008363", "ARG1", "PMID:15922518; DOI:10.1016/j.gene.2005.04.004"),
    ("M21B-E008364", "CCL26", "PMID:22226123"),
    ("M21B-E008365", "RETNLA", "PMID:12574343"),
    ("M21B-E008366", "CHIL3", "PMID:12215441"),
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
    queues = {row["queue_id"]: row for row in read_tsv(bundle / "mechanism_downstream_curation_queue.tsv")}
    records = {row["record_id"]: row for row in read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")}
    sources = read_tsv(bundle / "mechanism_edge_sources.tsv")
    source_by_edge: dict[str, list[dict[str, str]]] = {}
    for source in sources:
        source_by_edge.setdefault(source["edge_id"], []).append(source)
    queue = queues["M21B-DOWNSTREAM:00814"]
    record = records["M21B-DOWNSTREAM-EVID:001338"]
    lr_edge = edges["M21B-E001754"]
    receptor = nodes["NODE05502"]
    tf = nodes["NODE10761"]
    relay_edge = edges["M21B-E001783"]
    kinase = nodes[relay_edge["target_node_id"]]
    rows: list[dict[str, str]] = []
    for index, (target_edge_id, target_label, target_locators) in enumerate(TARGETS, start=1):
        target_edge = edges[target_edge_id]
        target = nodes[target_edge["target_node_id"]]
        edge_locators = [
            "PMID:9492265",
            "PMID:8887542",
            target_locators,
            *(source.get("source_locator", "") for source in source_by_edge.get(target_edge_id, [])),
            queue.get("source_locator", ""),
            record.get("source_locator", ""),
        ]
        locators = unique_join(edge_locators)
        evidence_ids = unique_join(
            [
                "M21B-E001754; M21B-E001783",
                lr_edge.get("evidence_ids", ""),
                relay_edge.get("evidence_ids", ""),
                target_edge.get("evidence_ids", ""),
                "M21B-EVID-001697; M21B-EVID-001726",
                queue.get("source_evidence_ids", ""),
                record.get("source_evidence_ids", ""),
                locators,
            ]
        )
        rows.append(
            {
                "expansion_id": f"M21B-LITEXP-IL4-JAK3-STAT6-{index:03d}",
                "source_queue_id": "M21B-DOWNSTREAM:00814",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "intracellular_to_tf_edge",
                "intracellular_status": "source_supported",
                "ligand_node_id": lr_edge["source_node_id"],
                "ligand_label": lr_edge["source_label"],
                "ligand_receptor_edge_id": "M21B-E001754",
                "receptor_node_id": lr_edge["target_node_id"],
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": "M21B-E001783",
                "intracellular_continuation_node_id": relay_edge["target_node_id"],
                "intracellular_continuation_label": kinase["canonical_label"],
                "transcription_factor_node_id": "NODE10761",
                "transcription_factor_label": tf["canonical_label"],
                "tf_target_edge_id": target_edge_id,
                "target_gene_node_id": target["node_id"],
                "target_gene_label": target["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": target["node_id"],
                "output_label": f"{target_label} expression",
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": f"IL4-IL4RA:IL2RG-JAK3-STAT6-{target_label}",
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": evidence_ids,
                "source_chain_id": f"M21B-LITEXP-IL4-JAK3-STAT6-{index:03d}",
                "source_evidence_record_id": "M21B-DOWNSTREAM-EVID:001338",
                "route_linkage_status": "manual_primary_il4_jak3_route;primary_layer_linked;parallel_receptor_relay_alternative;intracellular_to_tf_edge_not_asserted;tf_to_target_edge_asserted_as_graph_edge;evidence_route_only",
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression",
                "primary_locator": locators,
                "citation_note": "Primary IL-4 type-I receptor/JAK3 and STAT6 target-gene evidence is assembled as a parallel JAK3 route; the direct JAK3-to-STAT6 relay remains unasserted.",
                "evidence_summary": f"Primary evidence supports IL-4 engagement of the IL4RA:IL2RG type-I receptor, JAK3 receptor-proximal signaling, STAT6-associated regulation, and {target_label} expression. The route complements the existing JAK1 branch without asserting a new graph edge.",
                "limitations": "The receptor/JAK and STAT6 target studies use complementary primary systems and bounded cell contexts. Preserve type-I receptor, macrophage/epithelial/T-helper model limits; no SCI transfer, causal traversal, or database confidence score is inferred.",
                "curation_status": "curated_primary_route",
                "species_context": "human; mouse comparator systems",
                "cell_type_context": "Human type-I IL-4 receptor signaling systems and mouse T-helper/macrophage or human epithelial STAT6 target-gene assays.",
                "compartment_context": "extracellular IL-4; plasma membrane receptor complex; cytoplasm; nucleus; target-gene regulatory locus",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary evidence; route layers retain source-specific models",
                "assay_or_perturbation": "IL-4 stimulation; JAK1/JAK3 receptor-complex signaling; STAT6 perturbation; target-gene promoter, chromatin, transcript, or protein assays",
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
