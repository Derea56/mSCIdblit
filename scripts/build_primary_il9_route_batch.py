#!/usr/bin/env python3
"""Build source-linked IL-9 JAK/STAT feedback routes."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


TARGETS = (
    ("STAT5", "NODE10752", "M21B-E008251", "M21B-EVID-008943", "CISH", "PMID:9129017"),
    ("STAT5", "NODE10752", "M21B-E008258", "M21B-EVID-008944", "SOCS2", "PMID:28009300; PMCID:PMC5217531"),
    ("STAT3", "NODE10726", "M21B-E008279", "M21B-EVID-008945", "SOCS3", "PMID:16718380; PMCID:PMC2441693"),
)
RELAYS = (("JAK1", "M21B-E011511"), ("JAK3", "M21B-E011512"))


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
    source_by_edge = {}
    for source in sources:
        source_by_edge.setdefault(source["edge_id"], []).append(source)
    queue = queues["M21B-DOWNSTREAM:00106"]
    record = records["M21B-DOWNSTREAM-EVID:000195"]
    lr_edge = edges["M21B-E000325"]
    receptor = nodes["NODE05534"]
    rows: list[dict[str, str]] = []
    index = 1
    for tf_label, tf_id, target_edge_id, target_evidence_id, target_label, target_locators in TARGETS:
        target_edge = edges[target_edge_id]
        tf = nodes[tf_id]
        target = nodes[target_edge["target_node_id"]]
        for kinase_label, relay_edge_id in RELAYS:
            relay_edge = edges[relay_edge_id]
            kinase = nodes[relay_edge["target_node_id"]]
            locators = unique_join(
                [
                    "PMID:7718508",
                    "PMID:9535918",
                    "PMID:11115404",
                    target_locators,
                    *(source.get("source_locator", "") for source in source_by_edge.get(target_edge_id, [])),
                    queue.get("source_locator", ""),
                    record.get("source_locator", ""),
                ]
            )
            evidence_ids = unique_join(
                [
                    "M21B-E000325; M21B-E011511; M21B-E011512",
                    relay_edge.get("evidence_ids", ""),
                    target_edge.get("evidence_ids", ""),
                    f"M21B-EVID-000268; M21B-EVID-010820; {target_evidence_id}",
                    queue.get("source_evidence_ids", ""),
                    record.get("source_evidence_ids", ""),
                    locators,
                ]
            )
            rows.append(
                {
                    "expansion_id": f"M21B-LITEXP-IL9-JAKSTAT-{index:03d}",
                    "source_queue_id": "M21B-DOWNSTREAM:00106",
                    "route_status": "retained_evidence_route",
                    "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                    "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                    "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                    "missing_layers": "intracellular_to_tf_edge",
                    "intracellular_status": "source_supported",
                    "ligand_node_id": lr_edge["source_node_id"],
                    "ligand_label": lr_edge["source_label"],
                    "ligand_receptor_edge_id": "M21B-E000325",
                    "receptor_node_id": lr_edge["target_node_id"],
                    "receptor_label": receptor["canonical_label"],
                    "receptor_intracellular_edge_id": relay_edge_id,
                    "intracellular_continuation_node_id": relay_edge["target_node_id"],
                    "intracellular_continuation_label": kinase["canonical_label"],
                    "transcription_factor_node_id": tf_id,
                    "transcription_factor_label": tf["canonical_label"],
                    "tf_target_edge_id": target_edge_id,
                    "target_gene_node_id": target["node_id"],
                    "target_gene_label": target["canonical_label"],
                    "target_output_form_id": "",
                    "output_node_id": target["node_id"],
                    "output_label": f"{target_label} expression",
                    "output_form_id": "",
                    "bridge_id": "",
                    "pathway_name": f"IL9-IL9RA:IL2RG-{kinase_label}-{tf_label}-{target_label}",
                    "input_evidence_type": "primary_literature_route_expansion",
                    "output_evidence_type": "primary_target_gene_expression",
                    "evidence_ids": evidence_ids,
                    "source_chain_id": f"M21B-LITEXP-IL9-JAKSTAT-{index:03d}",
                    "source_evidence_record_id": "M21B-DOWNSTREAM-EVID:000195",
                    "route_linkage_status": "manual_primary_il9_route;primary_layer_linked;intracellular_to_tf_edge_not_asserted;tf_to_target_edge_asserted_as_graph_edge;evidence_route_only",
                    "causal_status": "not_asserted",
                    "traversal_status": "evidence_route_not_causal",
                    "evidence_contract_version": "mechanism_evidence_v1",
                    "evidence_polarity": "supports",
                    "negative_evidence_status": "not_evaluated",
                    "evidence_directness": "composite_primary_route",
                    "output_class": "target_gene_expression",
                    "primary_locator": locators,
                    "citation_note": "Primary IL-9 receptor/JAK/STAT and STAT-dependent feedback-gene studies are assembled as source-linked layers; the direct JAK-to-STAT handoff remains unasserted.",
                    "evidence_summary": f"Primary evidence supports IL-9 engagement of the IL9RA:IL2RG receptor complex, JAK1/JAK3-associated activation of {tf_label}, and IL-9-dependent {target_label} induction through STAT-linked signaling. The route is retained as a bounded evidence composition.",
                    "limitations": "The receptor-reconstitution, kinase/STAT activation, and feedback-gene studies use complementary cell systems. Preserve the IL-9R/γc and lymphoma/T-cell contexts; no SCI transfer, universal STAT weighting, causal traversal, or database confidence score is inferred.",
                    "curation_status": "curated_primary_route",
                    "species_context": "human; mouse comparator systems",
                    "cell_type_context": "Human IL-9 receptor reconstitution and T-cell lymphoma/lymphoid signaling systems used for JAK/STAT and CIS/SOCS output assays.",
                    "compartment_context": "extracellular IL-9; plasma membrane receptor complex; cytoplasm; nucleus; feedback-gene regulatory locus",
                    "injury_context": "no SCI transfer inferred; primary model context only",
                    "context_scope": "composite primary evidence; route layers retain source-specific models",
                    "assay_or_perturbation": "IL-9 stimulation; receptor heteromerization/mutant assays; JAK1/JAK3 and STAT activation; CIS/SOCS transcript and promoter assays",
                    "effect_polarity": "activating",
                    "source_scope": "composite_primary_evidence",
                }
            )
            index += 1
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
