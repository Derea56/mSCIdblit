#!/usr/bin/env python3
"""Build evidence-only BDNF-TrkB-CREB-Arc route annotations."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


RELAYS = (
    (
        "M21B-E001038",
        "PLCG1",
        "M21B-DOWNSTREAM:00415",
        "M21B-DOWNSTREAM-EVID:000701",
        "PMID:12367511",
    ),
    (
        "M21B-E001039",
        "FRS2A",
        "M21B-DOWNSTREAM:00416",
        "M21B-DOWNSTREAM-EVID:000704",
        "PMID:10196222",
    ),
    (
        "M21B-E001037",
        "SHC1",
        "M21B-DOWNSTREAM:00414",
        "M21B-DOWNSTREAM-EVID:000698",
        "PMID:15372074; PMCID:PMC522798",
    ),
)

TARGET_LOCATORS = (
    "PMID:17711418",
    "PMID:21988201",
    "PMCID:PMC4358108",
    "PMID:32928890",
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

    lr_edge = edges["M21B-E000318"]
    receptor = nodes[lr_edge["target_node_id"]]
    tf = nodes["NODE02446"]
    target = nodes["NODE00734"]
    rows: list[dict[str, str]] = []

    for index, (relay_edge_id, relay_label, queue_id, record_id, relay_locator) in enumerate(RELAYS, start=1):
        relay_edge = edges[relay_edge_id]
        relay = nodes[relay_edge["target_node_id"]]
        queue = queues[queue_id]
        record = records[record_id]
        locators = unique_join(
            [
                relay_locator,
                *TARGET_LOCATORS,
                *(source.get("source_locator", "") for source in source_by_edge.get(relay_edge_id, [])),
                queue.get("source_locator", ""),
                record.get("source_locator", ""),
            ]
        )
        evidence_ids = unique_join(
            [
                lr_edge.get("evidence_ids", ""),
                relay_edge.get("evidence_ids", ""),
                queue.get("source_evidence_ids", ""),
                record.get("source_evidence_ids", ""),
                *TARGET_LOCATORS,
            ]
        )
        expansion_id = f"M21B-LITEXP-BDNF-CREB-ARC-{index:03d}"
        rows.append(
            {
                "expansion_id": expansion_id,
                "source_queue_id": queue_id,
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "intracellular_to_tf_edge|tf_to_target_edge",
                "intracellular_status": "source_supported_composed",
                "ligand_node_id": lr_edge["source_node_id"],
                "ligand_label": lr_edge["source_label"],
                "ligand_receptor_edge_id": lr_edge["edge_id"],
                "receptor_node_id": lr_edge["target_node_id"],
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": relay_edge_id,
                "intracellular_continuation_node_id": relay["node_id"],
                "intracellular_continuation_label": relay["canonical_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": tf["node_id"],
                "transcription_factor_label": tf["canonical_label"],
                "tf_target_edge_id": "",
                "target_gene_node_id": target["node_id"],
                "target_gene_label": target["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": target["node_id"],
                "output_label": "Arc expression",
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": f"BDNF-TrkB-{relay_label}-CREB-Arc",
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": evidence_ids,
                "source_chain_id": expansion_id,
                "source_evidence_record_id": record_id,
                "route_linkage_status": (
                    "manual_primary_bdnf_creb_arc_route;primary_layer_linked;"
                    "parallel_receptor_proximal_alternative;receptor_to_intracellular_edge_not_asserted;"
                    "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;"
                    "evidence_route_only"
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
                    "Primary BDNF/TrkB relay studies support the site-specific PLCG1, FRS2A, or SHC1 "
                    "branch, while independent primary BDNF-stimulation studies support CREB-associated "
                    "Arc expression. The route composes these bounded observations and does not assert "
                    "new intracellular-to-CREB or CREB-to-Arc graph edges."
                ),
                "evidence_summary": (
                    f"Primary evidence supports BDNF engagement of TrkB, the {relay_label} receptor-proximal "
                    "branch, CREB-associated transcriptional response, and Arc expression. This is a "
                    "parallel evidence route for plausibility analysis; the two intermediate handoffs "
                    "remain explicitly unasserted."
                ),
                "limitations": (
                    "The relay and output studies use complementary neuronal, engineered-receptor, and "
                    "mutant-receptor systems. Preserve mature BDNF versus proBDNF, TrkB isoform and "
                    "docking-site context, species/cell-model limits, and Arc assay context; no SCI "
                    "transfer, causal traversal, or database confidence score is inferred."
                ),
                "curation_status": "curated_primary_route",
                "species_context": "mouse; rat; human comparator systems",
                "cell_type_context": "Primary cortical or hippocampal neurons, TrkB-engineered cells, and neuronal BDNF-response models.",
                "compartment_context": "extracellular BDNF; plasma membrane TrkB; cytoplasm; nucleus; Arc regulatory locus",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary evidence; route layers retain source-specific models",
                "assay_or_perturbation": "BDNF stimulation; TrkB docking-site mutation; CREB phosphorylation or activity; Arc transcript or promoter response",
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
