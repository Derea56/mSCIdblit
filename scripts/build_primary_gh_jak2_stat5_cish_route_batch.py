#!/usr/bin/env python3
"""Build evidence-only growth-hormone/GHR/JAK2/STAT5/Cish routes."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


LIGANDS = (
    ("M21B-E006583", "GH1/growth hormone (GH)", "PMID:1549776"),
    ("M21B-E001427", "Growth hormone", "PMID:8454051"),
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
    queues = {
        row["queue_id"]: row
        for row in read_tsv(bundle / "mechanism_downstream_curation_queue.tsv")
    }
    records = {
        row["record_id"]: row
        for row in read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")
    }
    sources = read_tsv(bundle / "mechanism_edge_sources.tsv")
    source_by_edge: dict[str, list[dict[str, str]]] = {}
    for source in sources:
        source_by_edge.setdefault(source["edge_id"], []).append(source)

    relay_edge = edges["M21B-E001710"]
    relay = nodes[relay_edge["target_node_id"]]
    lr_receptor = nodes[relay_edge["source_node_id"]]
    tf = nodes["NODE10752"]
    target_edge = edges["M22B-E000449"]
    target = nodes[target_edge["target_node_id"]]
    queue = queues["M21B-DOWNSTREAM:00797"]
    record = records["M21B-DOWNSTREAM-EVID:001307"]
    rows: list[dict[str, str]] = []

    for index, (lr_edge_id, ligand_label, lr_locator) in enumerate(LIGANDS, start=1):
        lr_edge = edges[lr_edge_id]
        locators = unique_join(
            [
                lr_locator,
                "PMID:8343952",
                "PMID:9231797",
                "PMID:10509798",
                *(source.get("source_locator", "") for source in source_by_edge.get(lr_edge_id, [])),
                *(source.get("source_locator", "") for source in source_by_edge.get("M21B-E001710", [])),
                *(source.get("source_locator", "") for source in source_by_edge.get("M22B-E000449", [])),
                queue.get("source_locator", ""),
                record.get("source_locator", ""),
            ]
        )
        evidence_ids = unique_join(
            [
                lr_edge.get("evidence_ids", ""),
                relay_edge.get("evidence_ids", ""),
                target_edge.get("evidence_ids", ""),
                queue.get("source_evidence_ids", ""),
                record.get("source_evidence_ids", ""),
                "PMID:10509798",
            ]
        )
        expansion_id = f"M21B-LITEXP-GH-JAK2-STAT5-CISH-{index:03d}"
        rows.append(
            {
                "expansion_id": expansion_id,
                "source_queue_id": queue["queue_id"],
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "intracellular_to_tf_edge",
                "intracellular_status": "source_supported",
                "ligand_node_id": lr_edge["source_node_id"],
                "ligand_label": lr_edge["source_label"],
                "ligand_receptor_edge_id": lr_edge_id,
                "receptor_node_id": lr_edge["target_node_id"],
                "receptor_label": lr_receptor["canonical_label"],
                "receptor_intracellular_edge_id": relay_edge["edge_id"],
                "intracellular_continuation_node_id": relay["node_id"],
                "intracellular_continuation_label": relay["canonical_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": tf["node_id"],
                "transcription_factor_label": tf["canonical_label"],
                "tf_target_edge_id": target_edge["edge_id"],
                "target_gene_node_id": target["node_id"],
                "target_gene_label": target["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": target["node_id"],
                "output_label": "Cish expression",
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": f"{ligand_label}-GHR-JAK2-STAT5-Cish",
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": evidence_ids,
                "source_chain_id": expansion_id,
                "source_evidence_record_id": record["record_id"],
                "route_linkage_status": (
                    "manual_primary_gh_jak2_stat5_cish_route;primary_layer_linked;"
                    "receptor_to_jak2_edge_asserted_as_graph_edge;intracellular_to_tf_edge_not_asserted;"
                    "tf_to_target_edge_asserted_as_graph_edge;evidence_route_only"
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
                    "Primary studies support growth-hormone receptor engagement, GHR-associated JAK2, "
                    "GH-induced STAT5 activation, and GH-induced Cis/Cish expression. The retained "
                    "STAT5-to-Cish graph edge is used as a target-gene component; the JAK2-to-STAT5 "
                    "handoff remains unasserted in this evidence route."
                ),
                "evidence_summary": (
                    f"Primary evidence supports {ligand_label} engagement of GHR, GHR-associated JAK2 "
                    "signaling, STAT5 activation, and Cish expression. The route retains the direct "
                    "STAT5-to-Cish graph component while preserving the unresolved JAK2-to-STAT5 link."
                ),
                "limitations": (
                    "The receptor-proximal and Cish-output studies use complementary engineered, hepatic, "
                    "and hematopoietic systems. Preserve GH isoform, GHR species/isoform, cell-type, "
                    "STAT5A/B, and Cish assay context; no SCI transfer, causal traversal, or database "
                    "confidence score is inferred."
                ),
                "curation_status": "curated_primary_route",
                "species_context": "human; rat; mouse comparator systems",
                "cell_type_context": "GHR-expressing fibroblast or epithelial systems, primary rat hepatocytes, and STAT5-responsive hematopoietic models.",
                "compartment_context": "extracellular growth hormone; plasma membrane GHR; cytoplasm; nucleus; Cish regulatory locus",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary evidence; route layers retain source-specific models",
                "assay_or_perturbation": "growth-hormone stimulation; GHR-JAK2 association or activation; STAT5 phosphorylation/DNA binding; Cish mRNA or target-gene assay",
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
