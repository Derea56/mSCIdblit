#!/usr/bin/env python3
"""Repair explicit target-gene roles for existing evidence-layer routes.

The mechanism export contains many gene-labelled endpoint nodes that are used
in route ``target_gene_node_id`` fields but were retained only as generic
``signaling_cascade`` nodes.  This release-level repair adds a target_gene
role only when the endpoint is supported by an evidence-gated TF-target edge
or by a locator-bearing literature-expansion route.  It does not create graph
edges, rewrite route records, assert causality, or create confidence scores.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import re
import shutil
from collections import defaultdict
from pathlib import Path

try:
    from .build_all_ligand_route_coverage import build as build_ligand_route_coverage
    from .build_all_ligand_route_coverage import write_tsv_gz as write_ligand_route_coverage
except ImportError:  # pragma: no cover - direct script execution
    from build_all_ligand_route_coverage import build as build_ligand_route_coverage
    from build_all_ligand_route_coverage import write_tsv_gz as write_ligand_route_coverage


STABLE_LOCATOR_RE = re.compile(r"\b(?:PMID|PMCID|DOI):[^;\s]+", re.IGNORECASE)
NON_GENE_TARGET_LABEL_RE = re.compile(r"\b(?:program|complex|pathway|branch)\b", re.IGNORECASE)
TF_TARGET_RELATIONS = {"activates", "represses", "induces_target_gene"}
ROLE_SOURCE = "role_repair_target_gene_evidence"
ROLE_EVIDENCE = (
    "Node is used as an existing route target_gene_node_id or TF-target endpoint "
    "and has evidence-gated target-gene support; role repair only."
)


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-bundle", type=Path, required=True)
    parser.add_argument("--output-bundle", type=Path, required=True)
    parser.add_argument("--release-id", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = args.source_bundle.resolve()
    output = args.output_bundle.resolve()
    if output.exists():
        raise FileExistsError(f"Output bundle already exists: {output}")
    shutil.copytree(source, output)

    _, node_rows = read_tsv(output / "mechanism_nodes.tsv")
    nodes = {row["node_id"]: row for row in node_rows}
    role_path = output / "mechanism_node_roles.tsv"
    role_fields, role_rows = read_tsv(role_path)
    existing_roles = defaultdict(set)
    for row in role_rows:
        existing_roles[row["node_id"]].add(row["role"])

    evidence_by_node: defaultdict[str, set[str]] = defaultdict(set)
    _, edge_rows = read_tsv(output / "mechanism_edges.tsv")
    for row in edge_rows:
        source_roles = existing_roles.get(row.get("source_node_id", ""), set())
        target_id = row.get("target_node_id", "")
        relation = row.get("relation_type", "")
        pathway = row.get("pathway_name", "").casefold()
        if (
            "transcription_factor" in source_roles
            and target_id in nodes
            and (
                relation in TF_TARGET_RELATIONS
                or "target_gene" in pathway
                or "transcription" in pathway
            )
        ):
            evidence_by_node[target_id].add(row["edge_id"])

    expansion_path = output / "mechanism_literature_expansion.tsv"
    with expansion_path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            target_id = row.get("target_gene_node_id", "")
            if (
                target_id in nodes
                and target_id
                and STABLE_LOCATOR_RE.search(row.get("primary_locator", ""))
                and row.get("path_expression", "").endswith("target_gene_expression")
            ):
                evidence_by_node[target_id].add(row["expansion_id"])

    route_path = output / "mechanism_signaling_route_evidence.tsv.gz"
    with gzip.open(route_path, "rt", newline="", encoding="utf-8", errors="replace") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            target_id = row.get("target_gene_node_id", "")
            if (
                target_id in nodes
                and target_id
                and STABLE_LOCATOR_RE.search(row.get("evidence_ids", ""))
                and row.get("path_expression", "").endswith("target_gene_expression")
            ):
                evidence_by_node[target_id].add(row["route_evidence_id"])

    candidates = {
        node_id: sorted(evidence_ids)
        for node_id, evidence_ids in evidence_by_node.items()
        if "target_gene" not in existing_roles[node_id]
        and not ({"ligand", "receptor"} & existing_roles[node_id])
        and not NON_GENE_TARGET_LABEL_RE.search(nodes[node_id].get("canonical_label", ""))
    }

    added: list[dict[str, str]] = []
    for node_id, evidence_ids in sorted(candidates.items()):
        added.append(
            {
                "node_id": node_id,
                "role": "target_gene",
                "role_source": ROLE_SOURCE,
                "role_evidence": f"{ROLE_EVIDENCE} evidence_ids={';'.join(evidence_ids)}",
            }
        )

    final_role_rows = role_rows + added
    write_tsv(role_path, role_fields, final_role_rows)

    coverage_rows, coverage_summary = build_ligand_route_coverage(output)
    write_ligand_route_coverage(output / "mechanism_ligand_route_coverage.tsv.gz", coverage_rows)
    (output / "ligand_route_coverage_summary.json").write_text(
        json.dumps(coverage_summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    metadata_path = output / "bundle_metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["release_id"] = args.release_id
    metadata.setdefault("files", {})["mechanism_node_roles"] = "mechanism_node_roles.tsv"
    metadata.setdefault("files", {})["ligand_route_coverage"] = "mechanism_ligand_route_coverage.tsv.gz"
    metadata.setdefault("counts", {})["node_roles"] = len(final_role_rows)
    metadata.setdefault("counts", {})["nodes_with_target_gene_role"] = len(
        {row["node_id"] for row in final_role_rows if row.get("role") == "target_gene"}
    )
    metadata.setdefault("counts", {})["ligand_route_coverage"] = len(coverage_rows)
    metadata.setdefault("graph_policy", {})["target_gene_role_repairs_are_evidence_layer_only"] = True
    statement = (
        "A scoped target-gene role repair adds roles only to existing route endpoints or TF-target endpoints "
        "with evidence-gated support; it does not create graph edges or confidence scores."
    )
    if statement not in metadata.setdefault("accuracy_contract", []):
        metadata["accuracy_contract"].append(statement)
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    summary = {
        "source_bundle": str(source),
        "output_bundle": str(output),
        "release_id": args.release_id,
        "role_repairs_added": len(added),
        "role_repair_nodes": [row["node_id"] for row in added],
        "coverage": coverage_summary,
        "graph_edges_changed": False,
        "route_evidence_rows_changed": False,
        "literature_expansion_rows_changed": False,
        "confidence_scores_created": False,
    }
    (output / "target_gene_role_repair_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    metadata.setdefault("files", {})["target_gene_role_repair_summary"] = "target_gene_role_repair_summary.json"
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
