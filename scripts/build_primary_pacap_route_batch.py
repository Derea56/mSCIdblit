#!/usr/bin/env python3
"""Build bounded PACAP/PAC1 evidence routes from primary source layers.

These rows retain the PACAP/PAC1 receptor-proximal branches and the
PACAP-associated CREB/Bdnf output as separate evidence layers.  They do not
assert that either G-protein branch is the complete intracellular route to the
target gene in one experiment.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROUTES = [
    {
        "suffix": "GS",
        "receptor_edge_id": "M23B-E000101",
        "receptor_node_id": "NODE00266",
        "receptor_label": "ADCYAP1R1/PAC1",
        "intracellular_edge_id": "M21B-E001897",
        "intracellular_node_id": "NODE04295",
        "intracellular_label": "GNAS",
        "pathway_label": "PACAP-PAC1-Gs-cAMP-CREB-Bdnf",
        "branch_note": "PAC1-Gs coupling",
    },
    {
        "suffix": "GQ",
        "receptor_edge_id": "M23B-E000101",
        "receptor_node_id": "NODE00266",
        "receptor_label": "ADCYAP1R1/PAC1",
        "intracellular_edge_id": "M21B-E001898",
        "intracellular_node_id": "NODE04294",
        "intracellular_label": "GNAQ/GNA11",
        "pathway_label": "PACAP-PAC1-Gq11-CREB-Bdnf",
        "branch_note": "PAC1-Gq/11 functional branch",
    },
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
    required_nodes = {"NODE08747", "NODE00266", "NODE04295", "NODE04294", "NODE02446", "NODE01191"}
    missing_nodes = sorted(required_nodes - nodes.keys())
    if missing_nodes:
        raise ValueError(f"PACAP route requires missing nodes: {missing_nodes}")

    target_node_id = "NODE01191"
    for route in ROUTES:
        lr_edge = edges[route["receptor_edge_id"]]
        if (lr_edge["source_node_id"], lr_edge["target_node_id"]) != ("NODE08747", route["receptor_node_id"]):
            raise ValueError(f"Unexpected PACAP receptor endpoints for {route['suffix']}")
        relay_edge = edges[route["intracellular_edge_id"]]
        if (relay_edge["source_node_id"], relay_edge["target_node_id"]) != (
            route["receptor_node_id"],
            route["intracellular_node_id"],
        ):
            raise ValueError(f"Unexpected PAC1 intracellular endpoints for {route['suffix']}")

    rows: list[dict[str, str]] = []
    for index, route in enumerate(ROUTES, start=1):
        locators = "PMID:25855176; PMCID:PMC6605314; PMID:15082190; PMID:32157248; PMID:21693142"
        evidence_ids = unique_join(
            [
                route["receptor_edge_id"],
                route["intracellular_edge_id"],
                "M23B-EVID-000163",
                "M21B-EVID-001840" if route["suffix"] == "GS" else "M21B-EVID-001841",
                "PMID:25855176",
                "PMID:15082190",
            ]
        )
        expansion_id = f"M23B-LITEXP-PACAP-{index:03d}"
        rows.append(
            {
                "expansion_id": expansion_id,
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "intracellular_to_tf_edge|tf_to_target_edge",
                "intracellular_status": "source_supported",
                "ligand_node_id": "NODE08747",
                "ligand_label": "PACAP/ADCYAP1",
                "ligand_receptor_edge_id": route["receptor_edge_id"],
                "receptor_node_id": route["receptor_node_id"],
                "receptor_label": route["receptor_label"],
                "receptor_intracellular_edge_id": route["intracellular_edge_id"],
                "intracellular_continuation_node_id": route["intracellular_node_id"],
                "intracellular_continuation_label": route["intracellular_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": "NODE02446",
                "transcription_factor_label": "CREB",
                "tf_target_edge_id": "",
                "target_gene_node_id": target_node_id,
                "target_gene_label": "Bdnf promoter IV",
                "output_node_id": target_node_id,
                "output_label": "Bdnf promoter IV expression",
                "pathway_name": route["pathway_label"],
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_pacap_transcriptional_output",
                "evidence_ids": evidence_ids,
                "source_chain_id": expansion_id,
                "source_evidence_record_id": "",
                "route_linkage_status": "graph_linked_route_source;manual_primary_pacap_route;receptor_proximal_and_tf_output_evidence_composed;intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;evidence_route_only",
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression",
                "primary_locator": locators,
                "citation_note": "Composite primary route annotation: PACAP/PAC1 activation, a receptor-proximal G-protein branch, PACAP-associated CREB/CRTC1 signaling, and Bdnf promoter-IV output are retained as separate source-linked layers.",
                "evidence_summary": f"Primary evidence supports PACAP activation of PAC1, the {route['branch_note']}, PACAP-associated CREB/CRTC1-dependent Bdnf transcriptional output, and PAC1-dependent BDNF regulation in vivo. The route is composed from independently bounded source layers.",
                "limitations": f"The {route['branch_note']} is supported at the receptor-proximal layer, while the PACAP-to-CREB/CRTC1 and CREB-to-Bdnf promoter-IV handoffs are supported by neuronal transcription studies but are not asserted as direct edge-level claims for this exact graph branch. The cited models are neuronal or heterologous and do not establish an SCI receiver-cell route.",
                "curation_status": "curated_primary_route",
                "species_context": "human; mouse; rat as stated in primary model/assay",
                "cell_type_context": "Primary cortical neurons and mouse brain PAC1/Bdnf studies, with receptor-proximal PAC1 coupling assays in human or rat systems.",
                "compartment_context": "extracellular ligand; plasma membrane; cytoplasm; nucleus; target-gene regulatory locus",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary evidence; route layers retain source-specific models",
                "assay_or_perturbation": "PACAP/PAC1 activation and G-protein coupling assays, PACAP-induced Bdnf-eIV transcription and CREB/CRTC1 studies, and PAC1-deficient BDNF expression comparisons as described by the cited primary sources.",
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
