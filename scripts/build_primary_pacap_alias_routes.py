#!/usr/bin/env python3
"""Promote bounded PACAP target routes to exact peptide aliases.

This intentionally avoids the broad alias cross-product.  It promotes only
aliases with an existing primary-supported PAC1 ligand-receptor edge and a
matching PAC1 receptor/relay branch already represented by the curated PACAP
routes.  The resulting rows remain evidence-layer overlays.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "alias_node_id": "NODE00264",
        "alias_label": "ADCYAP1/PACAP",
        "lr_edge_id": "M21B-E007113",
        "receptor_node_id": "NODE00267",
        "relay_node_id": "NODE04295",
        "relay_edge_id": "",
        "template_id": "M23B-LITEXP-PACAP-001",
    },
    {
        "alias_node_id": "NODE00264",
        "alias_label": "ADCYAP1/PACAP",
        "lr_edge_id": "M21B-E007113",
        "receptor_node_id": "NODE00267",
        "relay_node_id": "NODE04294",
        "relay_edge_id": "",
        "template_id": "M23B-LITEXP-PACAP-002",
    },
    {
        "alias_node_id": "NODE08746",
        "alias_label": "PACAP-27/PACAP-38",
        "lr_edge_id": "M21B-E001263",
        "receptor_node_id": "NODE00266",
        "relay_node_id": "NODE04295",
        "relay_edge_id": "M21B-E001897",
        "template_id": "M23B-LITEXP-PACAP-001",
    },
    {
        "alias_node_id": "NODE08746",
        "alias_label": "PACAP-27/PACAP-38",
        "lr_edge_id": "M21B-E001263",
        "receptor_node_id": "NODE00266",
        "relay_node_id": "NODE04294",
        "relay_edge_id": "M21B-E001898",
        "template_id": "M23B-LITEXP-PACAP-002",
    },
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def unique_join(*values: str) -> str:
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
    expansions = {row["expansion_id"]: row for row in read_tsv(bundle / "mechanism_literature_expansion.tsv")}
    rows: list[dict[str, str]] = []
    for index, spec in enumerate(SPECS, start=1):
        lr = edges[spec["lr_edge_id"]]
        template = expansions[spec["template_id"]]
        if lr["source_node_id"] != spec["alias_node_id"] or lr["target_node_id"] != spec["receptor_node_id"]:
            raise ValueError(f"Unexpected ligand-receptor endpoints for {spec['alias_label']}")
        relay = nodes[spec["relay_node_id"]]
        receptor = nodes[spec["receptor_node_id"]]
        alias = nodes[spec["alias_node_id"]]
        relay_edge = edges.get(spec["relay_edge_id"], {})
        missing_layers = "intracellular_to_tf_edge|tf_to_target_edge"
        if not spec["relay_edge_id"]:
            missing_layers = "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge"
        route_status = dict(template)
        route_status.update(
            {
                "expansion_id": f"M21B-LITEXP-PACAP-ALIAS-{index:03d}",
                "ligand_node_id": alias["node_id"],
                "ligand_label": alias["canonical_label"],
                "ligand_receptor_edge_id": spec["lr_edge_id"],
                "receptor_node_id": receptor["node_id"],
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": spec["relay_edge_id"],
                "intracellular_continuation_node_id": relay["node_id"],
                "intracellular_continuation_label": relay["canonical_label"],
                "missing_layers": missing_layers,
                "intracellular_status": "source_supported_alias_composed",
                "evidence_ids": unique_join(
                    lr.get("evidence_ids", ""),
                    relay_edge.get("evidence_ids", ""),
                    template.get("evidence_ids", ""),
                ),
                "source_chain_id": f"M21B-LITEXP-PACAP-ALIAS-{index:03d}",
                "route_linkage_status": unique_join(
                    lr.get("edge_status", ""),
                    template.get("route_linkage_status", ""),
                    "literature_expansion:bounded_pacap_alias_promotion",
                    "alias_receptor_identity_source_linked",
                    "receptor_to_intracellular_edge_asserted_as_graph_edge"
                    if spec["relay_edge_id"]
                    else "receptor_to_intracellular_edge_not_asserted",
                    "end_to_end_chain_not_asserted_by_single_source",
                    "evidence_route_only",
                ),
                "primary_locator": template.get("primary_locator", ""),
                "citation_note": (
                    f"Bounded alias promotion for {alias['canonical_label']}; the source-linked ligand-receptor "
                    "edge is joined to the existing PACAP/PAC1 primary route. No graph edge, causal assertion, "
                    "or confidence score is created."
                ),
                "evidence_summary": (
                    f"The {alias['canonical_label']} ligand-receptor record supports PAC1 input, while the "
                    "existing primary PACAP route supports the listed receptor-proximal branch, CREB layer, "
                    "and Bdnf promoter-IV output. The alias route preserves unresolved handoffs explicitly."
                ),
                "limitations": unique_join(
                    template.get("limitations", ""),
                    "This is a bounded alias-composed evidence route, not a single-paper demonstration of every handoff; no causal edge or confidence score is inferred.",
                ),
                "curation_status": "curated_primary_alias_route",
                "source_scope": "bounded_alias_composed_primary_evidence",
            }
        )
        rows.append(route_status)
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = make_rows(args.bundle.resolve())
    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output.resolve()), "rows": len(rows)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
