#!/usr/bin/env python3
"""Build bounded WNT3A canonical evidence routes from source-linked records.

These rows are evidence-layer annotations.  They preserve receptor-specific
WNT3A observations, the canonical beta-catenin/LEF1 module, and independently
curated WNT3A target-gene observations without asserting a missing causal edge
or a single-experiment end-to-end chain.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


PRIMARY_KINDS = {
    "primary_article",
    "pubmed_pmid",
    "review_guided_primary_validation",
}


RECEPTORS = [
    {
        "name": "fzd2",
        "queue_id": "M21B-DOWNSTREAM:02056",
        "lr_edge_id": "M21B-E006692",
        "receptor_node_id": "NODE03875",
        "receptor_label": "FZD2",
        "context": "WNT3A-stimulated FZD2-engineered 32D cells and purified WNT3A-FZD2 cysteine-rich-domain binding assays.",
        "limitation": "The receptor-specific source supports WNT3A-FZD2 binding and canonical LRP6 phosphorylation, DVL, and beta-catenin readouts, while target-gene evidence is independently curated from WNT3A-stimulated C57MG cells; no single assay demonstrates the complete FZD2-to-LEF1-to-target sequence.",
    },
    {
        "name": "fzd4",
        "queue_id": "M21B-DOWNSTREAM:02060",
        "lr_edge_id": "M21B-E006697",
        "receptor_node_id": "NODE03879",
        "receptor_label": "FZD4",
        "context": "WNT3A-stimulated FZD4-engineered 32D cells and purified WNT3A-FZD4 cysteine-rich-domain binding assays.",
        "limitation": "The receptor-specific source supports WNT3A-FZD4 binding and canonical LRP6 phosphorylation, DVL, and beta-catenin readouts, while target-gene evidence is independently curated from WNT3A-stimulated C57MG cells; no single assay demonstrates the complete FZD4-to-LEF1-to-target sequence.",
    },
    {
        "name": "fzd5",
        "queue_id": "M21B-DOWNSTREAM:02061",
        "lr_edge_id": "M21B-E006698",
        "receptor_node_id": "NODE03883",
        "receptor_label": "FZD5",
        "context": "WNT3A-stimulated FZD5-engineered 32D cells and purified WNT3A-FZD5 cysteine-rich-domain binding assays.",
        "limitation": "The receptor-specific source supports WNT3A-FZD5 binding and canonical LRP6 phosphorylation, DVL, and beta-catenin readouts, while target-gene evidence is independently curated from WNT3A-stimulated C57MG cells; no single assay demonstrates the complete FZD5-to-LEF1-to-target sequence.",
    },
    {
        "name": "fzd7",
        "queue_id": "M21B-DOWNSTREAM:02057",
        "lr_edge_id": "M21B-E006693",
        "receptor_node_id": "NODE03889",
        "receptor_label": "FZD7",
        "context": "WNT3A-treated FZD-family multiplex-mutant and FZD7-rescue mammalian cells with canonical WNT reporter and beta-catenin pathway readouts.",
        "limitation": "The receptor-specific source supports functional WNT3A-FZD7 coupling and canonical beta-catenin activation, while target-gene evidence is independently curated from WNT3A-stimulated C57MG cells; no single assay demonstrates the complete FZD7-to-LEF1-to-target sequence or direct LEF1 occupancy at the selected loci.",
    },
    {
        "name": "fzd10",
        "queue_id": "M21B-DOWNSTREAM:02049",
        "lr_edge_id": "M21B-E006682",
        "receptor_node_id": "NODE03873",
        "receptor_label": "FZD10/Frizzled-10",
        "context": "Developing chick spinal-cord and mammalian reporter systems with WNT3A, FZD10, LRP6, beta-catenin reporter, and FZD10 perturbation assays.",
        "limitation": "The receptor-specific source supports WNT3A-FZD10/LRP6-dependent canonical activation in developmental models, while target-gene evidence is independently curated from WNT3A-stimulated C57MG cells; no single assay demonstrates the complete FZD10-to-LEF1-to-target sequence or SCI transfer.",
    },
]


TARGETS = [
    ("M21B-E008927", "MYC gene"),
    ("M21B-E008928", "CCND1 gene"),
    ("M21B-E008929", "CDKN1A gene"),
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
    queue = {row["queue_id"]: row for row in read_tsv(bundle / "mechanism_downstream_curation_queue.tsv")}
    evidence = read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")
    evidence_by_queue: dict[str, dict[str, str]] = {}
    for row in evidence:
        evidence_by_queue.setdefault(row["source_queue_id"], row)
    sources = read_tsv(bundle / "mechanism_edge_sources.tsv")
    sources_by_edge: dict[str, list[dict[str, str]]] = {}
    for row in sources:
        if row.get("source_kind") in PRIMARY_KINDS:
            sources_by_edge.setdefault(row["edge_id"], []).append(row)

    if "NODE02581" not in nodes or "NODE06343" not in nodes:
        raise ValueError("WNT3A route requires the canonical beta-catenin and LEF1 nodes")
    rows: list[dict[str, str]] = []
    for receptor in RECEPTORS:
        q = queue[receptor["queue_id"]]
        source_record = evidence_by_queue[receptor["queue_id"]]
        lr_edge = edges[receptor["lr_edge_id"]]
        if (lr_edge["source_node_id"], lr_edge["target_node_id"]) != ("NODE11857", receptor["receptor_node_id"]):
            raise ValueError(f"Unexpected WNT3A receptor endpoints for {receptor['name']}")
        receptor_sources = sources_by_edge.get(receptor["lr_edge_id"], [])
        for target_edge_id, target_label in TARGETS:
            target_edge = edges[target_edge_id]
            target_node = nodes[target_edge["target_node_id"]]
            target_sources = sources_by_edge.get(target_edge_id, [])
            locators = unique_join(
                [
                    q.get("source_locator", ""),
                    *[s.get("source_locator", "") for s in receptor_sources],
                    *[s.get("source_locator", "") for s in target_sources],
                    "PMID:8757136; PMID:8892228",
                ]
            )
            evidence_ids = unique_join(
                [
                    receptor["lr_edge_id"],
                    target_edge_id,
                    q.get("source_evidence_ids", ""),
                    source_record.get("record_id", ""),
                    *[s.get("source_evidence_id", "") for s in receptor_sources],
                    *[s.get("source_evidence_id", "") for s in target_sources],
                    "M21B-E007531",
                    locators,
                ]
            )
            suffix = len(rows) + 1
            rows.append(
                {
                    "expansion_id": f"M21B-LITEXP-WNT3A-{suffix:03d}",
                    "source_queue_id": receptor["queue_id"],
                    "route_status": "retained_evidence_route",
                    "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                    "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                    "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                    "missing_layers": "intracellular_to_tf_edge|tf_to_target_edge",
                    "intracellular_status": "source_supported",
                    "ligand_node_id": "NODE11857",
                    "ligand_label": "WNT3A",
                    "ligand_receptor_edge_id": receptor["lr_edge_id"],
                    "receptor_node_id": receptor["receptor_node_id"],
                    "receptor_label": receptor["receptor_label"],
                    "receptor_intracellular_edge_id": "",
                    "intracellular_continuation_node_id": "NODE02581",
                    "intracellular_continuation_label": "CTNNB1-beta-catenin",
                    "intracellular_tf_edge_id": "",
                    "transcription_factor_node_id": "NODE06343",
                    "transcription_factor_label": "LEF1",
                    "tf_target_edge_id": "",
                    "target_gene_node_id": target_node["node_id"],
                    "target_gene_label": target_label,
                    "output_node_id": target_node["node_id"],
                    "output_label": f"{target_label} expression",
                    "pathway_name": f"WNT3A-{receptor['receptor_label']}-beta-catenin-LEF1-{target_label}",
                    "input_evidence_type": "primary_literature_route_expansion",
                    "output_evidence_type": "primary_wnt3a_target_gene_expression",
                    "evidence_ids": evidence_ids,
                    "source_chain_id": f"M21B-LITEXP-WNT3A-{suffix:03d}",
                    "source_evidence_record_id": source_record["record_id"],
                    "route_linkage_status": "manual_primary_wnt3a_route;cross_record_exact_lr_pair;receptor_proximal_and_tf_output_evidence_composed;intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;evidence_route_only",
                    "causal_status": "not_asserted",
                    "traversal_status": "evidence_route_not_causal",
                    "evidence_contract_version": "mechanism_evidence_v1",
                    "evidence_polarity": "supports",
                    "negative_evidence_status": "not_evaluated",
                    "evidence_directness": "composite_primary_route",
                    "output_class": "target_gene_expression",
                    "primary_locator": locators,
                    "citation_note": "Composite primary route annotation: receptor-specific WNT3A evidence, the beta-catenin/LEF1 nuclear module, and WNT3A target-gene expression are retained as separate source-linked layers.",
                    "evidence_summary": f"Primary evidence supports WNT3A engagement of {receptor['receptor_label']}, canonical beta-catenin pathway activation, beta-catenin association with LEF1, and WNT3A-associated {target_label} expression. The route is composed from independently curated source layers.",
                    "limitations": receptor["limitation"],
                    "curation_status": "curated_primary_route",
                    "species_context": q.get("species_context", "human; mouse; chick as stated in primary model/assay"),
                    "cell_type_context": receptor["context"],
                    "compartment_context": "extracellular ligand; plasma membrane; cytoplasm; nucleus; target-gene regulatory locus",
                    "injury_context": "no SCI transfer inferred; primary model context only",
                    "context_scope": "composite primary evidence; route layers retain source-specific models",
                    "assay_or_perturbation": f"Receptor-specific WNT3A binding/activation and canonical beta-catenin readouts; beta-catenin-LEF1 interaction evidence; WNT3A target-gene expression measurements for {target_label}.",
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
