#!/usr/bin/env python3
"""Build evidence-only PDGF-BB/PDGFRB/STAT3/FOS route annotations."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


RELAYS = (
    ("M21B-E001104", "ABL2", "M21B-DOWNSTREAM:00452", "M21B-DOWNSTREAM-EVID:000786"),
    ("M21B-E001100", "GRB2", "M21B-DOWNSTREAM:00449", "M21B-DOWNSTREAM-EVID:000779"),
    ("M21B-E001050", "PLCG1", "M21B-DOWNSTREAM:00422", "M21B-DOWNSTREAM-EVID:000715"),
    ("M21B-E000143", "PLCgamma1/PLCG1", "M21B-DOWNSTREAM:00006", "M21B-DOWNSTREAM-EVID:000014"),
    ("M21B-E001102", "PTPN11/SHP2", "M21B-DOWNSTREAM:00450", "M21B-DOWNSTREAM-EVID:000781"),
    ("M21B-E001103", "SHP2/PTPN11", "M21B-DOWNSTREAM:00451", "M21B-DOWNSTREAM-EVID:000784"),
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

    lr_edge = edges["M21B-E000182"]
    receptor = nodes[lr_edge["target_node_id"]]
    tf = nodes["NODE10726"]
    target_edge = edges["M21B-E008305"]
    target = nodes[target_edge["target_node_id"]]
    rows: list[dict[str, str]] = []

    for index, (relay_edge_id, relay_label, queue_id, record_id) in enumerate(RELAYS, start=1):
        relay_edge = edges[relay_edge_id]
        relay = nodes[relay_edge["target_node_id"]]
        queue = queues[queue_id]
        record = records[record_id]
        locators = unique_join(
            [
                "PMID:20534510; PMCID:PMC2895058",
                "PMID:8657151",
                "PMID:12600988",
                *(source.get("source_locator", "") for source in source_by_edge.get(relay_edge_id, [])),
                *(source.get("source_locator", "") for source in source_by_edge.get(target_edge["edge_id"], [])),
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
            ]
        )
        expansion_id = f"M21B-LITEXP-PDGFB-STAT3-FOS-{index:03d}"
        rows.append(
            {
                "expansion_id": expansion_id,
                "source_queue_id": queue_id,
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "intracellular_to_tf_edge",
                "intracellular_status": "source_supported",
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
                "tf_target_edge_id": target_edge["edge_id"],
                "target_gene_node_id": target["node_id"],
                "target_gene_label": target["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": target["node_id"],
                "output_label": "FOS gene expression",
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": f"PDGFB-PDGFRB-{relay_label}-STAT3-FOS",
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": evidence_ids,
                "source_chain_id": expansion_id,
                "source_evidence_record_id": record_id,
                "route_linkage_status": (
                    "manual_primary_pdgfb_stat3_fos_route;primary_layer_linked;"
                    "parallel_receptor_proximal_alternative;intracellular_to_tf_edge_not_asserted;"
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
                    "Primary evidence supports PDGF-BB/PDGFRB engagement, the site-specific receptor-proximal "
                    f"{relay_label} branch, STAT3 activation in PDGF-treated systems, and STAT3-associated "
                    "native FOS transcription. The branch-to-STAT3 handoff remains unasserted."
                ),
                "evidence_summary": (
                    f"Primary evidence supports PDGF-BB engagement of PDGFRB, the {relay_label} branch, "
                    "STAT3-associated regulation, and FOS gene expression. The route retains a parallel "
                    "receptor-proximal alternative without asserting a new intracellular-to-STAT3 edge."
                ),
                "limitations": (
                    "The receptor, relay, STAT3, and FOS studies use complementary structural, engineered, "
                    "fibroblast, and native promoter systems. Preserve PDGF-BB processing, PDGFRB dimer, "
                    "relay-site, STAT3 cooperation with mitogen-activated promoter factors, species and "
                    "cell-model limits; no SCI transfer, causal traversal, or database confidence score is inferred."
                ),
                "curation_status": "curated_primary_route",
                "species_context": "human; mouse comparator systems",
                "cell_type_context": "PDGF-treated BALB/c 3T3 cells, PDGFRB-engineered fibroblasts, and native c-FOS promoter systems.",
                "compartment_context": "extracellular PDGF-BB; plasma membrane PDGFRB dimer; cytoplasm; nucleus; FOS regulatory locus",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary evidence; route layers retain source-specific models",
                "assay_or_perturbation": "PDGF-BB stimulation; receptor-docking mutation or association; JAK/STAT activation; native FOS promoter, chromatin, or transcript assay",
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
