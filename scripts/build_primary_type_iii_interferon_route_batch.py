#!/usr/bin/env python3
"""Build source-linked type-III interferon route annotations.

The graph already contains the IFN-lambda receptor, receptor-proximal
TYK2/STAT layer, ISGF3 target-gene edges, and subtype-specific ligand
records.  This overlay connects those bounded observations for IFN-lambda 2,
3, and 4.  The receptor-proximal-to-ISGF3 handoff remains explicitly
unasserted because no single exported edge represents that transition.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


TARGETS = (
    ("M21B-E008209", "ISG15"),
    ("M21B-E008602", "IFIT1"),
    ("M21B-E008603", "OAS1"),
)

SUBTYPES = (
    {
        "slug": "IFNL2",
        "ligand_node_id": "NODE05015",
        "ligand_label": "IFNL2",
        "lr_edge_id": "M21B-E010391",
        "locators": "PMID:12483210; PMID:23258595; PMCID:PMC3579021",
        "specific_note": "The receptor and type-III interferon signaling layers include primary IFN-lambda studies that directly tested IFN-lambda2 in hepatocyte systems and the shared IFN-lambda receptor complex.",
    },
    {
        "slug": "IFNL3",
        "ligand_node_id": "NODE05016",
        "ligand_label": "IFNL3",
        "lr_edge_id": "M21B-E000132",
        "locators": "PMID:12483210; PMID:23258595; PMCID:PMC3579021; PMID:32353085; PMCID:PMC7217487; PMID:31471108; PMCID:PMC7447158",
        "specific_note": "IFN-lambda3-specific primary studies directly measured IFNLR1-dependent binding and ISG15, IFIT1, and OAS1 induction in human cells, together with STAT1-dependent type-III interferon response kinetics.",
    },
    {
        "slug": "IFNL4",
        "ligand_node_id": "NODE05017",
        "ligand_label": "IFNL4/interferon-lambda-4",
        "lr_edge_id": "M21B-E006516",
        "locators": "PMID:33158978; PMCID:PMC7668538; PMID:23258595; PMCID:PMC3579021; PMID:31471108; PMCID:PMC7447158",
        "specific_note": "IFN-lambda4-specific primary work supports receptor responsiveness and STAT1 phosphorylation in human immune cells; the ISGF3 target layer is retained as shared type-III interferon evidence rather than claimed as a single-paper IFN-lambda4 experiment.",
    },
)

RELAY_EDGE_ID = "M21B-E000062"
TF_NODE_ID = "NODE05712"


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
    required_nodes = {"NODE05015", "NODE05016", "NODE05017", "NODE05019", "NODE11528", TF_NODE_ID}
    required_nodes.update(edges[target_edge_id]["target_node_id"] for target_edge_id, _label in TARGETS)
    missing_nodes = sorted(required_nodes - nodes.keys())
    if missing_nodes:
        raise ValueError(f"Type-III interferon route requires missing nodes: {missing_nodes}")
    required_edges = {RELAY_EDGE_ID, *(item["lr_edge_id"] for item in SUBTYPES), *(item[0] for item in TARGETS)}
    missing_edges = sorted(required_edges - edges.keys())
    if missing_edges:
        raise ValueError(f"Type-III interferon route requires missing edges: {missing_edges}")

    relay_edge = edges[RELAY_EDGE_ID]
    receptor = nodes[relay_edge["source_node_id"]]
    relay = nodes[relay_edge["target_node_id"]]
    tf = nodes[TF_NODE_ID]
    rows: list[dict[str, str]] = []
    for subtype in SUBTYPES:
        lr_edge = edges[subtype["lr_edge_id"]]
        if lr_edge["source_node_id"] != subtype["ligand_node_id"]:
            raise ValueError(f"Unexpected ligand endpoint for {subtype['slug']}")
        if lr_edge["target_node_id"] != receptor["node_id"]:
            raise ValueError(f"Unexpected receptor endpoint for {subtype['slug']}")
        for target_edge_id, target_slug in TARGETS:
            target_edge = edges[target_edge_id]
            target = nodes[target_edge["target_node_id"]]
            expansion_id = f"M21B-LITEXP-{subtype['slug']}-ISGF3-{target_slug}"
            evidence_ids = unique_join(
                [
                    subtype["lr_edge_id"],
                    lr_edge.get("evidence_ids", ""),
                    RELAY_EDGE_ID,
                    relay_edge.get("evidence_ids", ""),
                    target_edge_id,
                    target_edge.get("evidence_ids", ""),
                    subtype["locators"],
                ]
            )
            rows.append(
                {
                    "expansion_id": expansion_id,
                    "source_queue_id": "",
                    "route_status": "retained_evidence_route",
                    "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                    "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                    "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                    "missing_layers": "intracellular_to_tf_edge",
                    "intracellular_status": "source_supported",
                    "ligand_node_id": subtype["ligand_node_id"],
                    "ligand_label": subtype["ligand_label"],
                    "ligand_receptor_edge_id": subtype["lr_edge_id"],
                    "receptor_node_id": receptor["node_id"],
                    "receptor_label": receptor["canonical_label"],
                    "receptor_intracellular_edge_id": RELAY_EDGE_ID,
                    "intracellular_continuation_node_id": relay["node_id"],
                    "intracellular_continuation_label": relay["canonical_label"],
                    "intracellular_tf_edge_id": "",
                    "transcription_factor_node_id": TF_NODE_ID,
                    "transcription_factor_label": tf["canonical_label"],
                    "tf_target_edge_id": target_edge_id,
                    "target_gene_node_id": target["node_id"],
                    "target_gene_label": target["canonical_label"],
                    "target_output_form_id": "",
                    "output_node_id": target["node_id"],
                    "output_label": f"{target_slug} gene expression",
                    "output_form_id": "",
                    "bridge_id": "",
                    "pathway_name": f"{subtype['slug']}-IFNLR1-IL10RB-TYK2-STAT1-STAT2-IRF9-{target_slug}",
                    "input_evidence_type": "primary_literature_route_expansion",
                    "output_evidence_type": "primary_type_III_interferon_target_gene_expression",
                    "evidence_ids": evidence_ids,
                    "source_evidence_record_id": "",
                    "route_linkage_status": "graph_linked_route_source;manual_primary_type_III_interferon_route;shared_type_III_IFN_target_evidence;intracellular_to_tf_edge_not_asserted;tf_to_target_edge_asserted_graph_evidence;evidence_route_only",
                    "causal_status": "not_asserted",
                    "traversal_status": "evidence_route_not_causal",
                    "evidence_contract_version": "mechanism_evidence_v1",
                    "evidence_polarity": "supports",
                    "negative_evidence_status": "not_evaluated",
                    "evidence_directness": "composite_primary_route",
                    "output_class": "gene_expression_or_transcription",
                    "primary_locator": subtype["locators"],
                    "citation_note": "Composite primary route annotation. The ligand/receptor and receptor-proximal signaling layers are joined to an evidence-gated ISGF3 target-gene edge; the receptor-proximal-to-ISGF3 transition remains an explicit missing-link field.",
                    "evidence_summary": f"{subtype['specific_note']} The exported graph also retains ISGF3-associated {target_slug} promoter/target-gene evidence. The route is preserved for plausibility analysis without asserting a new causal edge.",
                    "limitations": "The receptor, kinase/STAT, ISGF3, and target-gene observations come from complementary primary systems and are not a single end-to-end experiment for every subtype and target. Preserve the hepatocyte, epithelial, immune-cell, and synthetic-receptor contexts; no SCI transfer, confidence score, or causal traversal is inferred.",
                    "curation_status": "curated_primary_route",
                    "species_context": "human; mouse comparator systems as stated in primary studies",
                    "cell_type_context": "Primary human hepatocytes, epithelial cells, purified immune-cell subsets, and complementary receptor-reconstitution systems.",
                    "compartment_context": "extracellular IFN-lambda; plasma-membrane IFNLR1/IL10RB; cytoplasmic JAK/STAT relay; nuclear ISGF3 target-gene regulation",
                    "injury_context": "no SCI transfer inferred; primary antiviral and immune model contexts only",
                    "context_scope": "composite primary evidence; subtype and cell-context boundaries retained",
                    "assay_or_perturbation": "ligand-receptor binding, receptor-reconstitution or receptor-expression assays, STAT1/STAT2 phosphorylation and nuclear signaling, ISGF3 target-gene promoter or expression assays, and subtype-specific ISG induction",
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
