#!/usr/bin/env python3
"""Build IL-36 evidence routes through the shared MyD88/IRAK/NFkB/MAPK relay."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROUTES = (
    {
        "name": "IL36A-CXCL1",
        "ligand_node_id": "NODE05482",
        "ligand_label": "IL36A",
        "lr_edge_id": "M21B-E001738",
        "receptor_node_id": "NODE05401",
        "receptor_label": "IL1RL2:IL1RAP receptor complex",
        "relay_node_id": "NODE07613",
        "relay_label": "MyD88/IRAK/NFkB/MAPK",
        "relay_edge_id": "M24B-E000096",
        "tf_node_id": "NODE08035",
        "tf_label": "NFKB p65/p50 complex",
        "tf_target_edge_id": "M21B-E008191",
        "output_edge_id": "M21B-E008788",
        "target_node_id": "NODE02622",
        "target_label": "CXCL1 gene",
        "locator": "PMID:14734551; DOI:10.1074/jbc.M400117200; PMID:24829417; PMCID:PMC4048788; PMID:29180446; DOI:10.1074/jbc.M117.805739",
    },
    {
        "name": "IL36B-CXCL1",
        "ligand_node_id": "NODE05484",
        "ligand_label": "IL36B",
        "lr_edge_id": "M21B-E003267",
        "receptor_node_id": "NODE05401",
        "receptor_label": "IL1RL2:IL1RAP receptor complex",
        "relay_node_id": "NODE07613",
        "relay_label": "MyD88/IRAK/NFkB/MAPK",
        "relay_edge_id": "M24B-E000096",
        "tf_node_id": "NODE08035",
        "tf_label": "NFKB p65/p50 complex",
        "tf_target_edge_id": "M21B-E008191",
        "output_edge_id": "M21B-E008796",
        "target_node_id": "NODE02622",
        "target_label": "CXCL1 gene",
        "locator": "PMID:14734551; DOI:10.1074/jbc.M400117200; PMID:24829417; PMCID:PMC4048788; PMID:29180446; DOI:10.1074/jbc.M117.805739",
    },
    {
        "name": "IL36G-CXCL1",
        "ligand_node_id": "NODE05485",
        "ligand_label": "IL36G",
        "lr_edge_id": "M21B-E003268",
        "receptor_node_id": "NODE05401",
        "receptor_label": "IL1RL2:IL1RAP receptor complex",
        "relay_node_id": "NODE07613",
        "relay_label": "MyD88/IRAK/NFkB/MAPK",
        "relay_edge_id": "M24B-E000096",
        "tf_node_id": "NODE08035",
        "tf_label": "NFKB p65/p50 complex",
        "tf_target_edge_id": "M21B-E008191",
        "output_edge_id": "M21B-E008804",
        "target_node_id": "NODE02622",
        "target_label": "CXCL1 gene",
        "locator": "PMID:14734551; DOI:10.1074/jbc.M400117200; PMID:24829417; PMCID:PMC4048788; PMID:29180446; DOI:10.1074/jbc.M117.805739",
    },
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def join_unique(*values: str) -> str:
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
    sources: dict[str, list[dict[str, str]]] = {}
    for row in read_tsv(bundle / "mechanism_edge_sources.tsv"):
        sources.setdefault(row["edge_id"], []).append(row)

    rows: list[dict[str, str]] = []
    for spec in ROUTES:
        required_nodes = [
            spec["ligand_node_id"], spec["receptor_node_id"], spec["relay_node_id"],
            spec["tf_node_id"], spec["target_node_id"],
        ]
        required_edges = [
            spec["lr_edge_id"], spec["relay_edge_id"], spec["tf_target_edge_id"],
            spec["output_edge_id"],
        ]
        missing = [item for item in required_nodes + required_edges if item not in nodes and item not in edges]
        if missing:
            raise ValueError(f"{spec['name']}: missing graph objects {missing}")
        lr = edges[spec["lr_edge_id"]]
        if (lr["source_node_id"], lr["target_node_id"]) != (spec["ligand_node_id"], spec["receptor_node_id"]):
            raise ValueError(f"{spec['name']}: ligand-receptor endpoints do not match")
        tf_target = edges[spec["tf_target_edge_id"]]
        if (tf_target["source_node_id"], tf_target["target_node_id"]) != (spec["tf_node_id"], spec["target_node_id"]):
            raise ValueError(f"{spec['name']}: TF-target endpoints do not match")
        output = edges[spec["output_edge_id"]]
        if output["source_node_id"] != spec["ligand_node_id"]:
            raise ValueError(f"{spec['name']}: output edge does not start at ligand")

        evidence_ids = join_unique(
            *[edges[edge_id].get("evidence_ids", "") for edge_id in required_edges],
            spec["locator"],
        )
        source_chain = f"M21B-LITEXP-IL36-SHARED-RELAY-{spec['ligand_label']}-CXCL1"
        rows.append({
            "expansion_id": source_chain,
            "source_queue_id": "",
            "route_status": "retained_evidence_route",
            "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
            "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
            "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
            "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge",
            "intracellular_status": "source_supported_ligand_family_level",
            "ligand_node_id": spec["ligand_node_id"],
            "ligand_label": spec["ligand_label"],
            "ligand_receptor_edge_id": spec["lr_edge_id"],
            "receptor_node_id": spec["receptor_node_id"],
            "receptor_label": spec["receptor_label"],
            "receptor_intracellular_edge_id": "",
            "intracellular_continuation_node_id": spec["relay_node_id"],
            "intracellular_continuation_label": spec["relay_label"],
            "intracellular_tf_edge_id": "",
            "transcription_factor_node_id": spec["tf_node_id"],
            "transcription_factor_label": spec["tf_label"],
            "tf_target_edge_id": spec["tf_target_edge_id"],
            "target_gene_node_id": spec["target_node_id"],
            "target_gene_label": spec["target_label"],
            "output_node_id": spec["target_node_id"],
            "output_label": f"{spec['target_label']} expression",
            "pathway_name": f"{spec['ligand_label']}-IL1RL2-IL1RAP-MyD88-IRAK-NFkB-CXCL1",
            "input_evidence_type": "primary_literature_route_expansion",
            "output_evidence_type": "primary_target_gene_expression",
            "evidence_ids": evidence_ids,
            "source_chain_id": source_chain,
            "source_evidence_record_id": "",
            "route_linkage_status": (
                "graph_linked_route_source;manual_primary_il36_shared_relay_route;"
                "shared_ligand_family_relay;receptor_to_intracellular_edge_not_asserted;"
                "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_asserted_as_graph_edge;"
                "direct_ligand_output_retained_as_supporting_evidence;evidence_route_only"
            ),
            "causal_status": "not_asserted",
            "traversal_status": "evidence_route_not_causal",
            "evidence_contract_version": "mechanism_evidence_v1",
            "evidence_polarity": "supports",
            "negative_evidence_status": "not_evaluated",
            "evidence_directness": "composite_primary_route",
            "output_class": "target_gene_expression",
            "primary_locator": spec["locator"],
            "citation_note": "Primary IL-36 receptor/relay and target-output records are composed as an evidence route; exact receptor-to-relay and relay-to-TF handoffs remain explicit gaps.",
            "evidence_summary": (
                f"Primary studies support {spec['ligand_label']} engagement of the IL1RL2/IL1RAP receptor platform, "
                "the shared MyD88/IRAK/NF-kB/MAPK signaling layer for IL-36 cytokines, and IL-36-associated CXCL1 "
                "expression in keratinocyte/inflammatory models. The existing NF-kB-to-CXCL1 edge is retained as "
                "a separate graph-supported layer."
            ),
            "limitations": (
                "This is a composed evidence route, not a single-paper end-to-end chain. The shared IL-36 family "
                "relay is not asserted as a ligand-specific receptor-to-relay edge, and the relay-to-NF-kB handoff "
                "is not asserted as a new graph edge. Processed agonist and source-specific cell contexts are retained; "
                "no SCI transfer, causal traversal, or confidence score is inferred."
            ),
            "curation_status": "curated_primary_route",
            "species_context": "human; mouse comparator as stated in primary model/assay",
            "cell_type_context": "human keratinocyte and receptor/pathway comparator systems; exact context remains source-specific",
            "compartment_context": "extracellular ligand; plasma-membrane receptor complex; cytoplasmic relay; nucleus; target-gene regulatory locus",
            "injury_context": "no SCI transfer inferred; primary model context only",
            "context_scope": "composite primary evidence; shared IL-36 family relay retained with source-specific boundaries",
            "assay_or_perturbation": "IL-36 ligand stimulation; receptor-complex binding/activation; MyD88/IRAK/NF-kB/MAPK pathway assays; CXCL1 expression assays",
            "effect_polarity": "activating",
            "source_scope": "composite_primary_evidence",
        })
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
