#!/usr/bin/env python3
"""Build bounded IL-17B/IL-36 NF-kappaB target-gene evidence routes."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROUTES = (
    {
        "name": "IL17B-CXCL1",
        "ligand_node_id": "NODE05335",
        "ligand_label": "IL17B",
        "lr_edge_id": "M21B-E000742",
        "receptor_node_id": "NODE05345",
        "receptor_label": "IL17RB",
        "relay_node_id": "NODE11388",
        "relay_label": "TRAF6-ACT1-TAK1-ERK1/2 signaling cascade",
        "supporting_edge_ids": ["M21B-E008906"],
        "tf_node_id": "NODE08035",
        "tf_label": "NFKB p65/p50 complex",
        "tf_target_edge_id": "M21B-E008191",
        "direct_output_edge_id": "M21B-E008909",
        "prefix": "M21B-LITEXP-IL17B-NFKB-CXCL1",
        "locators": "PMID:10749887; PMID:24280128; PMCID:PMC3952611; PMID:25732306; PMCID:PMC4354366; DOI:10.1084/jem.20141702",
        "summary": "Primary evidence supports IL-17B/IL17RB signaling, an IL-17B-associated TRAF6-ACT1-TAK1-ERK1/2 cascade, and IL17B-associated CXCL1 expression; the route retains the existing NFKB p65/p50-to-CXCL1 graph edge while leaving the receptor-to-relay and relay-to-TF handoffs unresolved.",
    },
    {
        "name": "IL36A-CXCL1",
        "ligand_node_id": "NODE05482",
        "ligand_label": "IL36A",
        "lr_edge_id": "M21B-E001758",
        "receptor_node_id": "NODE05401",
        "receptor_label": "IL1RL2:IL1RAP receptor complex",
        "relay_node_id": "",
        "relay_label": "",
        "supporting_edge_ids": [],
        "tf_node_id": "NODE08035",
        "tf_label": "NFKB p65/p50 complex",
        "tf_target_edge_id": "M21B-E008191",
        "direct_output_edge_id": "M21B-E008788",
        "prefix": "M21B-LITEXP-IL36A-NFKB-CXCL1",
        "locators": "PMID:29180446; DOI:10.1074/jbc.M117.805622; PMID:24829417; PMCID:PMC4048788; PMID:24280128; PMCID:PMC3952611",
        "summary": "Primary evidence supports IL-36A engagement of the IL1RL2:IL1RAP receptor complex and IL36A-associated CXCL1 expression; the route retains the existing NFKB p65/p50-to-CXCL1 graph edge while leaving all intracellular continuation and relay-to-TF handoffs unresolved.",
    },
    {
        "name": "IL36B-CXCL1",
        "ligand_node_id": "NODE05484",
        "ligand_label": "IL36B",
        "lr_edge_id": "M21B-E003267",
        "receptor_node_id": "NODE05401",
        "receptor_label": "IL1RL2:IL1RAP receptor complex",
        "relay_node_id": "",
        "relay_label": "",
        "supporting_edge_ids": [],
        "tf_node_id": "NODE08035",
        "tf_label": "NFKB p65/p50 complex",
        "tf_target_edge_id": "M21B-E008191",
        "direct_output_edge_id": "M21B-E008796",
        "prefix": "M21B-LITEXP-IL36B-NFKB-CXCL1",
        "locators": "PMID:24829417; PMCID:PMC4048788; PMID:24280128; PMCID:PMC3952611",
        "summary": "Primary evidence supports IL-36B binding to the IL1RL2:IL1RAP receptor complex and IL36B-associated CXCL1 expression; the route retains the existing NFKB p65/p50-to-CXCL1 graph edge while leaving all intracellular continuation and relay-to-TF handoffs unresolved.",
    },
    {
        "name": "IL36G-CXCL1",
        "ligand_node_id": "NODE05485",
        "ligand_label": "IL36G",
        "lr_edge_id": "M21B-E003268",
        "receptor_node_id": "NODE05401",
        "receptor_label": "IL1RL2:IL1RAP receptor complex",
        "relay_node_id": "",
        "relay_label": "",
        "supporting_edge_ids": [],
        "tf_node_id": "NODE08035",
        "tf_label": "NFKB p65/p50 complex",
        "tf_target_edge_id": "M21B-E008191",
        "direct_output_edge_id": "M21B-E008804",
        "prefix": "M21B-LITEXP-IL36G-NFKB-CXCL1",
        "locators": "PMID:24829417; PMCID:PMC4048788; PMID:24280128; PMCID:PMC3952611",
        "summary": "Primary evidence supports IL-36G binding to the IL1RL2:IL1RAP receptor complex and IL36G-associated CXCL1 expression; the route retains the existing NFKB p65/p50-to-CXCL1 graph edge while leaving all intracellular continuation and relay-to-TF handoffs unresolved.",
    },
)


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


def make_rows(bundle: Path, only: set[str] | None = None) -> list[dict[str, str]]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    source_by_edge: dict[str, list[dict[str, str]]] = {}
    for source in read_tsv(bundle / "mechanism_edge_sources.tsv"):
        source_by_edge.setdefault(source["edge_id"], []).append(source)

    rows: list[dict[str, str]] = []
    for route in ROUTES:
        if only and route["name"] not in only:
            continue
        required = [
            route["ligand_node_id"], route["receptor_node_id"], route["tf_node_id"],
            route["lr_edge_id"], route["tf_target_edge_id"], route["direct_output_edge_id"],
            *route["supporting_edge_ids"],
        ]
        if route["relay_node_id"]:
            required.append(route["relay_node_id"])
        missing = [item for item in required if item not in nodes and item not in edges]
        if missing:
            raise ValueError(f"{route['name']}: missing graph objects {missing}")

        lr_edge = edges[route["lr_edge_id"]]
        tf_target_edge = edges[route["tf_target_edge_id"]]
        direct_output_edge = edges[route["direct_output_edge_id"]]
        if (lr_edge["source_node_id"], lr_edge["target_node_id"]) != (route["ligand_node_id"], route["receptor_node_id"]):
            raise ValueError(f"{route['name']}: unexpected ligand-receptor endpoints")
        if tf_target_edge["source_node_id"] != route["tf_node_id"]:
            raise ValueError(f"{route['name']}: unexpected TF-target source")
        if direct_output_edge["source_node_id"] != route["ligand_node_id"]:
            raise ValueError(f"{route['name']}: unexpected direct-output source")

        target = nodes[tf_target_edge["target_node_id"]]
        relay_present = bool(route["relay_node_id"])
        locators = unique_join([
            route["locators"],
            *(source.get("source_locator", "") for edge_id in required for source in source_by_edge.get(edge_id, [])),
        ])
        evidence_ids = unique_join([
            *(edge_id for edge_id in required if edge_id in edges),
            *(edge.get("evidence_ids", "") for edge in (lr_edge, tf_target_edge, direct_output_edge)),
            locators,
        ])
        if relay_present:
            path_expression = "ligand>receptor>intracellular>TF>target_gene_expression"
            route_tier = "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges"
            known_layers = "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression"
            missing_layers = "receptor_to_intracellular_edge|intracellular_to_tf_edge"
            intracellular_status = "source_supported_ligand_level"
            linkage = "receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted"
        else:
            path_expression = "ligand>receptor>????>TF>target_gene_expression"
            route_tier = "ligand_receptor_tf_target_missing_intracellular"
            known_layers = "ligand|receptor|transcription_factor|target_gene_expression"
            missing_layers = "intracellular_continuation|receptor_to_intracellular_edge|intracellular_to_tf_edge"
            intracellular_status = "not_mapped"
            linkage = "intracellular_continuation_not_asserted;receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted"

        rows.append({
            "expansion_id": route["prefix"],
            "source_queue_id": "",
            "route_status": "retained_evidence_route",
            "path_expression": path_expression,
            "route_tier": route_tier,
            "known_layers": known_layers,
            "missing_layers": missing_layers,
            "intracellular_status": intracellular_status,
            "ligand_node_id": route["ligand_node_id"],
            "ligand_label": route["ligand_label"],
            "ligand_receptor_edge_id": route["lr_edge_id"],
            "receptor_node_id": route["receptor_node_id"],
            "receptor_label": route["receptor_label"],
            "receptor_intracellular_edge_id": "",
            "intracellular_continuation_node_id": route["relay_node_id"],
            "intracellular_continuation_label": route["relay_label"],
            "intracellular_tf_edge_id": "",
            "transcription_factor_node_id": route["tf_node_id"],
            "transcription_factor_label": route["tf_label"],
            "tf_target_edge_id": route["tf_target_edge_id"],
            "target_gene_node_id": target["node_id"],
            "target_gene_label": target["canonical_label"],
            "output_node_id": target["node_id"],
            "output_label": f"{target['canonical_label']} expression",
            "pathway_name": f"{route['name']}-{route['tf_label']}-{target['canonical_label']}",
            "input_evidence_type": "primary_literature_route_expansion",
            "output_evidence_type": "primary_target_gene_expression",
            "evidence_ids": evidence_ids,
            "source_chain_id": route["prefix"],
            "source_evidence_record_id": "",
            "route_linkage_status": "graph_linked_route_source;manual_primary_il17_il36_route;" + linkage + ";tf_to_target_edge_asserted_as_graph_edge;direct_ligand_output_retained_as_supporting_evidence;evidence_route_only",
            "causal_status": "not_asserted",
            "traversal_status": "evidence_route_not_causal",
            "evidence_contract_version": "mechanism_evidence_v1",
            "evidence_polarity": "supports",
            "negative_evidence_status": "not_evaluated",
            "evidence_directness": "composite_primary_route",
            "output_class": "target_gene_expression",
            "primary_locator": locators,
            "citation_note": "Composite primary route annotation. Direct ligand output and an existing TF-to-target graph edge are retained as separate evidence layers; unresolved intracellular handoffs are explicit.",
            "evidence_summary": route["summary"],
            "limitations": "The route combines complementary primary studies and bounded cell contexts. It is traversable as evidence, not as a causal chain; no SCI transfer or database confidence score is inferred.",
            "curation_status": "curated_primary_route",
            "species_context": "human; mouse as stated in primary model/assay",
            "cell_type_context": "Primary cytokine receptor and inflammatory transcriptional-output models as stated by the cited studies; exact cell context remains source-specific.",
            "compartment_context": "extracellular cytokine; plasma membrane receptor complex; cytoplasm; nucleus; target-gene regulatory locus",
            "injury_context": "no SCI transfer inferred; primary model context only",
            "context_scope": "composite primary evidence; route layers retain source-specific models",
            "assay_or_perturbation": "Ligand stimulation, receptor/relay or target-gene assays, TF-target evidence, and target-gene expression/output measurements from cited primary studies.",
            "effect_polarity": "activating",
            "source_scope": "composite_primary_evidence",
        })
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--only", action="append", help="Route name to emit; may be repeated")
    args = parser.parse_args()
    rows = make_rows(args.bundle.resolve(), set(args.only or []))
    args.output.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
