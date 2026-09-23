#!/usr/bin/env python3
"""Build evidence-only IL-12 JAK2/TYK2-STAT4-TBX21 route annotations."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


RELAYS = (
    ("M21B-E001769", "JAK2"),
    ("M21B-E001770", "TYK2"),
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

    lr_edge = edges["M21B-E001767"]
    receptor = nodes[lr_edge["target_node_id"]]
    tf = nodes["NODE10748"]
    target_edge = edges["M21B-E008249"]
    target = nodes[target_edge["target_node_id"]]
    queue = queues["M21B-DOWNSTREAM:00823"]
    record = records["M21B-DOWNSTREAM-EVID:001357"]
    rows: list[dict[str, str]] = []
    for index, (relay_edge_id, relay_label) in enumerate(RELAYS, start=1):
        relay_edge = edges[relay_edge_id]
        kinase = nodes[relay_edge["target_node_id"]]
        locators = unique_join(
            [
                "PMID:8943050; PMID:9498755; PMID:7638186",
                "PMID:17575072; PMCID:PMC1988915",
                *(source.get("source_locator", "") for source in source_by_edge.get(relay_edge_id, [])),
                *(source.get("source_locator", "") for source in source_by_edge.get(target_edge["edge_id"], [])),
                queue.get("source_locator", ""),
                record.get("source_locator", ""),
            ]
        )
        evidence_ids = unique_join(
            [
                "M21B-E001767; M21B-EVID-001710; M21B-EVID-001712; M21B-EVID-001713",
                target_edge.get("evidence_ids", ""),
                queue.get("source_evidence_ids", ""),
                record.get("source_evidence_ids", ""),
                locators,
            ]
        )
        rows.append(
            {
                "expansion_id": f"M21B-LITEXP-IL12-{relay_label}-STAT4-TBX21-{index:03d}",
                "source_queue_id": "M21B-DOWNSTREAM:00823",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge",
                "intracellular_status": "source_supported",
                "ligand_node_id": lr_edge["source_node_id"],
                "ligand_label": lr_edge["source_label"],
                "ligand_receptor_edge_id": "M21B-E001767",
                "receptor_node_id": lr_edge["target_node_id"],
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": relay_edge["target_node_id"],
                "intracellular_continuation_label": kinase["canonical_label"],
                "transcription_factor_node_id": "NODE10748",
                "transcription_factor_label": tf["canonical_label"],
                "tf_target_edge_id": target_edge["edge_id"],
                "target_gene_node_id": target["node_id"],
                "target_gene_label": target["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": target["node_id"],
                "output_label": "TBX21 expression",
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": f"IL12-IL12RB1:IL12RB2-{relay_label}-STAT4-TBX21",
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": evidence_ids,
                "source_chain_id": f"M21B-LITEXP-IL12-{relay_label}-STAT4-TBX21-{index:03d}",
                "source_evidence_record_id": "M21B-DOWNSTREAM-EVID:001357",
                "route_linkage_status": "manual_primary_il12_tbx21_route;primary_layer_linked;parallel_receptor_proximal_alternative;receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;tf_to_target_edge_asserted_as_graph_edge;evidence_route_only",
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression",
                "primary_locator": locators,
                "citation_note": "Primary IL-12 receptor-pair/JAK2-TYK2/STAT4 and STAT4-responsive TBX21-enhancer evidence is assembled as parallel receptor-proximal alternatives; both the receptor-to-JAK and JAK-to-STAT4 handoffs remain unasserted.",
                "evidence_summary": f"Primary evidence supports IL-12 engagement of the IL12RB1:IL12RB2 receptor pair, {relay_label}-associated receptor-proximal signaling, STAT4 activity, and TBX21 expression. The route adds a plausible branch without reusing an IL-23 receptor edge or asserting new graph connectivity.",
                "limitations": "The receptor, kinase, STAT4, and TBX21 studies use complementary primary systems and bounded lymphocyte/reconstitution contexts. Preserve IL-12 p35/p40 heterodimer, beta1/beta2 receptor, human/mouse T-cell, and enhancer-assay limits; no SCI transfer, causal traversal, or database confidence score is inferred.",
                "curation_status": "curated_primary_route",
                "species_context": "human; mouse comparator systems",
                "cell_type_context": "Human receptor-reconstitution and PHA-activated T/NK systems with mouse CD8-positive or Th1 STAT4/TBX21 enhancer studies.",
                "compartment_context": "extracellular IL-12; plasma membrane receptor complex; cytoplasm; nucleus; TBX21 regulatory locus",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary evidence; route layers retain source-specific models",
                "assay_or_perturbation": "IL-12 stimulation; receptor reconstitution; JAK2/TYK2/STAT4 phosphorylation; STAT4 enhancer binding and TBX21 expression assays",
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
