#!/usr/bin/env python3
"""Build source-linked CNTF JAK/STAT3 route annotations.

The CNTF receptor-to-JAK and JAK-to-STAT3 handoffs are retained as
evidence-layer compositions because the current graph does not export those
exact intermediate edges.  The routes do not create causal edges or scores.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROUTES = (
    ("JAK1", "NODE06016"),
    ("JAK2", "NODE06026"),
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def join_unique(values: list[str]) -> str:
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
    queues = {row["queue_id"]: row for row in read_tsv(bundle / "mechanism_downstream_curation_queue.tsv")}
    records = {row["record_id"]: row for row in read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")}
    queue = queues["M21B-DOWNSTREAM:00820"]
    record = records["M21B-DOWNSTREAM-EVID:001352"]
    lr_edge = edges["M21B-E001761"]
    receptor = nodes["NODE02289"]
    tf = nodes["NODE10726"]
    target = nodes["NODE06057"]
    rows: list[dict[str, str]] = []
    for index, (kinase_label, kinase_id) in enumerate(ROUTES, start=1):
        kinase = nodes[kinase_id]
        locators = join_unique(
            [
                "PMID:8390097; PMID:8385113; PMID:7500350",
                "PMID:11882386",
                "PMID:7898939",
                queue.get("source_locator", ""),
                record.get("source_locator", ""),
            ]
        )
        evidence_ids = join_unique(
            [
                "M21B-E001761; M21B-E000058; M21B-E008331",
                "M21B-EVID-001704; M21B-EVID-000015; M21B-EVID-008277",
                queue.get("source_evidence_ids", ""),
                record.get("source_evidence_ids", ""),
                locators,
            ]
        )
        rows.append(
            {
                "expansion_id": f"M21B-LITEXP-CNTF-JAKSTAT3-{index:03d}",
                "source_queue_id": "M21B-DOWNSTREAM:00820",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge",
                "intracellular_status": "source_supported_composed",
                "ligand_node_id": lr_edge["source_node_id"],
                "ligand_label": lr_edge["source_label"],
                "ligand_receptor_edge_id": "M21B-E001761",
                "receptor_node_id": lr_edge["target_node_id"],
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": kinase_id,
                "intracellular_continuation_label": kinase["canonical_label"],
                "transcription_factor_node_id": "NODE10726",
                "transcription_factor_label": tf["canonical_label"],
                "tf_target_edge_id": "M21B-E008331",
                "target_gene_node_id": "NODE06057",
                "target_gene_label": target["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": "NODE06057",
                "output_label": "JUNB expression",
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": f"CNTF-CNTFR-alpha-gp130-LIFR-{kinase_label}-STAT3-JUNB",
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": evidence_ids,
                "source_chain_id": f"M21B-LITEXP-CNTF-JAKSTAT3-{index:03d}",
                "source_evidence_record_id": "M21B-DOWNSTREAM-EVID:001352",
                "route_linkage_status": "manual_primary_cntf_route;primary_layer_linked;receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;tf_to_target_edge_asserted_as_graph_edge;evidence_route_only",
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression",
                "primary_locator": locators,
                "citation_note": "Primary CNTF receptor/JAK/STAT3 and CNTF-responsive JUNB promoter evidence are assembled as separately source-linked layers; direct receptor-to-JAK and JAK-to-STAT3 graph edges are not asserted.",
                "evidence_summary": f"Primary evidence supports CNTF engagement of the CNTFR-alpha:gp130:LIFR receptor complex, parallel {kinase_label} and STAT3 activation, and CNTF/IL-6-responsive STAT3-dependent JUNB promoter activation. The route is retained as a bounded evidence composition.",
                "limitations": "The receptor-complex, JAK/STAT3 activation, and JUNB promoter studies are complementary primary systems rather than one end-to-end experiment. Preserve the neuroblastoma/HepG2 and receptor-reconstitution contexts; no SCI transfer, causal traversal, or database confidence score is inferred.",
                "curation_status": "curated_primary_route",
                "species_context": "human; rodent comparator systems",
                "cell_type_context": "Human neuroblastoma and HepG2/receptor-signaling systems used for CNTF JAK/STAT3 and JUNB promoter assays.",
                "compartment_context": "extracellular CNTF; plasma membrane receptor complex; cytoplasm; nucleus; JUNB regulatory locus",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary evidence; receptor, kinase, TF, and target layers retain source-specific models",
                "assay_or_perturbation": "CNTF stimulation; JAK1/JAK2 and STAT3 phosphorylation; receptor-complex signaling; JUNB promoter reporter and STAT3 DNA-binding assays",
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
