#!/usr/bin/env python3
"""Build bounded IL-33 and IL-18 evidence routes from primary-linked edges.

These routes preserve the receptor-proximal MyD88 layer while leaving the
MyD88-to-TF handoff unasserted.  The terminal TF-to-target edges are existing
graph edges; direct ligand output edges are carried as supporting evidence but
are not treated as a causal end-to-end chain.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROUTES = (
    {
        "name": "IL1A-IL6",
        "ligand_node_id": "NODE05362",
        "ligand_label": "IL1A",
        "lr_edge_id": "M21B-E001765",
        "receptor_node_id": "NODE05380",
        "receptor_label": "IL1R1-IL1RAP receptor complex",
        "relay_edge_id": "M21B-E000023",
        "supporting_edge_ids": [],
        "relay_node_id": "NODE07611",
        "relay_label": "MYD88",
        "tf_node_id": "NODE09694",
        "tf_label": "RELA",
        "tf_target_edge_id": "M21B-E008632",
        "direct_output_edge_id": "M21B-E008919",
        "prefix": "M21B-LITEXP-IL1A-MYD88-RELA-IL6",
        "locators": "PMID:9820540; PMID:11416133; PMID:11594800; PMID:8134378",
        "summary": "Primary-linked evidence supports IL-1A engagement of the IL1R1-IL1RAP receptor complex, receptor-associated MYD88, and IL1A-associated IL6 expression; the route retains the existing RELA-to-IL6 graph edge while leaving the MYD88-to-RELA handoff unresolved.",
    },
    {
        "name": "IL33-IL10",
        "ligand_node_id": "NODE05467",
        "ligand_label": "IL33",
        "lr_edge_id": "M21B-E000187",
        "receptor_node_id": "NODE05397",
        "receptor_label": "IL1RL1/ST2:IL1RAP",
        "relay_edge_id": "",
        "supporting_edge_ids": ["M21B-E011485"],
        "relay_node_id": "NODE07611",
        "relay_label": "MYD88",
        "tf_node_id": "NODE10726",
        "tf_label": "STAT3",
        "tf_target_edge_id": "M21B-E008186",
        "direct_output_edge_id": "M21B-E008646",
        "prefix": "M21B-LITEXP-IL33-MYD88-STAT3-IL10",
        "locators": "PMID:29099095; PMCID:PMC5704190",
        "summary": "Primary evidence supports IL-33 engagement of the ST2/IL1RAP receptor context and IL-33-associated IL10 expression; the route retains the existing STAT3-to-IL10 graph edge while leaving the MyD88-to-STAT3 handoff unresolved.",
    },
    {
        "name": "IL33-MMP9",
        "ligand_node_id": "NODE05467",
        "ligand_label": "IL33",
        "lr_edge_id": "M21B-E000187",
        "receptor_node_id": "NODE05397",
        "receptor_label": "IL1RL1/ST2:IL1RAP",
        "relay_edge_id": "",
        "supporting_edge_ids": ["M21B-E011485"],
        "relay_node_id": "NODE07611",
        "relay_label": "MYD88",
        "tf_node_id": "NODE10726",
        "tf_label": "STAT3",
        "tf_target_edge_id": "M21B-E008299",
        "direct_output_edge_id": "M21B-E008649",
        "prefix": "M21B-LITEXP-IL33-MYD88-STAT3-MMP9",
        "locators": "PMID:30333314; PMCID:PMC6237443",
        "summary": "Primary evidence supports IL-33-associated MMP9 expression in the recorded receptor context; the route retains the existing STAT3-to-MMP9 graph edge while leaving the MyD88-to-STAT3 handoff unresolved.",
    },
    {
        "name": "IL18-IFNG",
        "ligand_node_id": "NODE05348",
        "ligand_label": "IL18",
        "lr_edge_id": "M21B-E001752",
        "receptor_node_id": "NODE05357",
        "receptor_label": "IL18R1:IL18RAP receptor complex",
        "relay_edge_id": "M21B-E001727",
        "supporting_edge_ids": [],
        "relay_node_id": "NODE07611",
        "relay_label": "MYD88",
        "tf_node_id": "NODE10748",
        "tf_label": "STAT4",
        "tf_target_edge_id": "M21B-E008260",
        "direct_output_edge_id": "M21B-E009019",
        "prefix": "M21B-LITEXP-IL18-MYD88-STAT4-IFNG",
        "locators": "PMID:9792649; PMID:10229825",
        "summary": "Primary evidence supports IL-18 receptor-complex signaling and IL-18-associated IFNG transcription in IL-12-stimulated NK cells; the route retains the existing STAT4-to-IFNG graph edge while leaving the MyD88-to-STAT4 handoff unresolved.",
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
            route["ligand_node_id"],
            route["receptor_node_id"],
            route["relay_node_id"],
            route["tf_node_id"],
            route["lr_edge_id"],
            route["tf_target_edge_id"],
            route["direct_output_edge_id"],
        ]
        required.extend(route.get("supporting_edge_ids", []))
        if route["relay_edge_id"]:
            required.append(route["relay_edge_id"])
        missing = [item for item in required if item not in nodes and item not in edges]
        if missing:
            raise ValueError(f"{route['name']}: missing graph objects {missing}")

        lr_edge = edges[route["lr_edge_id"]]
        relay_edge = edges.get(route["relay_edge_id"]) if route["relay_edge_id"] else None
        tf_target_edge = edges[route["tf_target_edge_id"]]
        direct_output_edge = edges[route["direct_output_edge_id"]]
        expected_lr = (route["ligand_node_id"], route["receptor_node_id"])
        expected_relay = (route["receptor_node_id"], route["relay_node_id"])
        expected_tf_target = (route["tf_node_id"], tf_target_edge["target_node_id"])
        if (lr_edge["source_node_id"], lr_edge["target_node_id"]) != expected_lr:
            raise ValueError(f"{route['name']}: unexpected ligand-receptor endpoints")
        if relay_edge and (relay_edge["source_node_id"], relay_edge["target_node_id"]) != expected_relay:
            raise ValueError(f"{route['name']}: unexpected receptor-relay endpoints")
        if (tf_target_edge["source_node_id"], tf_target_edge["target_node_id"]) != expected_tf_target:
            raise ValueError(f"{route['name']}: unexpected TF-target endpoints")
        if direct_output_edge["source_node_id"] != route["ligand_node_id"]:
            raise ValueError(f"{route['name']}: direct output is not sourced by ligand")

        target = nodes[tf_target_edge["target_node_id"]]
        locators = unique_join(
            [
                route["locators"],
                *(source.get("source_locator", "") for edge_id in required if edge_id in edges for source in source_by_edge.get(edge_id, [])),
            ]
        )
        evidence_ids = unique_join(
            [
                *(required_item for required_item in required if required_item in edges),
                *(edge.get("evidence_ids", "") for edge in (lr_edge, relay_edge, tf_target_edge, direct_output_edge) if edge),
                locators,
            ]
        )
        rows.append(
            {
                "expansion_id": route["prefix"],
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "intracellular_to_tf_edge" if relay_edge else "receptor_to_intracellular_edge|intracellular_to_tf_edge",
                "intracellular_status": "source_supported" if relay_edge else "source_supported_component_alias",
                "ligand_node_id": route["ligand_node_id"],
                "ligand_label": route["ligand_label"],
                "ligand_receptor_edge_id": route["lr_edge_id"],
                "receptor_node_id": route["receptor_node_id"],
                "receptor_label": route["receptor_label"],
                "receptor_intracellular_edge_id": route["relay_edge_id"],
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
                "pathway_name": f"{route['name']}-{route['relay_label']}-{route['tf_label']}-{target['canonical_label']}",
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": evidence_ids,
                "source_chain_id": route["prefix"],
                "source_evidence_record_id": "",
                "route_linkage_status": "graph_linked_route_source;manual_primary_cytokine_route;receptor_to_intracellular_edge_asserted_as_graph_edge;intracellular_to_tf_edge_not_asserted;tf_to_target_edge_asserted_as_graph_edge;direct_ligand_output_retained_as_supporting_evidence;evidence_route_only" if relay_edge else "graph_linked_route_source;manual_primary_cytokine_route;receptor_to_intracellular_edge_not_asserted;intracellular_component_supported_by_adjacent_graph_alias;intracellular_to_tf_edge_not_asserted;tf_to_target_edge_asserted_as_graph_edge;direct_ligand_output_retained_as_supporting_evidence;evidence_route_only",
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression",
                "primary_locator": locators,
                "citation_note": "Composite primary route annotation: receptor engagement, MyD88 continuation, TF-target evidence, and direct ligand-associated target output are retained as separate source-linked layers; the MyD88-to-TF handoff is not asserted.",
                "evidence_summary": route["summary"],
                "limitations": "The route combines complementary primary studies and bounded cell contexts. It is traversable as evidence, not as a causal chain; no SCI transfer or database confidence score is inferred.",
                "curation_status": "curated_primary_route",
                "species_context": "human; mouse as stated in primary model/assay",
                "cell_type_context": "Primary cytokine receptor and transcriptional-output models as stated by the cited studies; exact cell context remains source-specific.",
                "compartment_context": "extracellular cytokine; plasma membrane receptor complex; cytoplasm; nucleus; target-gene regulatory locus",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary evidence; route layers retain source-specific models",
                "assay_or_perturbation": "Ligand stimulation, receptor-proximal signaling, TF-target evidence, and target-gene expression/output assays from the cited primary studies.",
                "effect_polarity": "activating",
                "source_scope": "composite_primary_evidence",
            }
        )
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
