#!/usr/bin/env python3
"""Repair unambiguous TF roles for existing evidence-layer route nodes.

Some legacy mechanism nodes are exported as ``signaling_effector`` even
though they are used as transcription-factor nodes in route evidence and have
direct evidence-gated transcription edges.  This release-level repair adds a
TF role only for an explicit, reviewed allow-list of composite factors.  It
does not rewrite graph nodes, graph edges, route rows, causal fields, or
confidence fields.
"""

from __future__ import annotations

import argparse
import csv
import json
import shutil
from collections import Counter
from pathlib import Path

try:
    from .build_all_ligand_route_coverage import build as build_ligand_route_coverage
    from .build_all_ligand_route_coverage import write_tsv_gz as write_ligand_route_coverage
except ImportError:  # pragma: no cover - direct script execution
    from build_all_ligand_route_coverage import build as build_ligand_route_coverage
    from build_all_ligand_route_coverage import write_tsv_gz as write_ligand_route_coverage


ROLE_REPAIRS = {
    "NODE02454": "CREB1/CREB",
    "NODE04692": "HIF-1 (HIF1A/ARNT) complex",
    "NODE05712": "ISGF3 (STAT1-STAT2-IRF9) complex",
    "NODE06054": "JUN-ATF2 complex",
    "NODE07961": "NF-IL6/NFKB p65 complex",
    "NODE07969": "NF-kappaB p50/p65 complex",
    "NODE07976": "NF-kappaB RelA/c-Rel-containing complex",
    "NODE08035": "NFKB p65/p50 complex",
    "NODE10709": "STAT1 and STAT3 cooperative promoter factors",
}

ROLE_SOURCE = "role_repair_direct_transcription_edge"
ROLE_EVIDENCE = (
    "Node is used in an existing route transcription_factor_node_id field and "
    "has an evidence-gated transcription-like mechanism edge; role repair only."
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

    node_fields, node_rows = read_tsv(output / "mechanism_nodes.tsv")
    nodes = {row["node_id"]: row for row in node_rows}
    role_path = output / "mechanism_node_roles.tsv"
    role_fields, role_rows = read_tsv(role_path)
    existing_roles = {(row["node_id"], row["role"]) for row in role_rows}

    route_path = output / "mechanism_signaling_route_evidence.tsv.gz"
    import gzip

    with gzip.open(route_path, "rt", newline="", encoding="utf-8", errors="replace") as handle:
        route_rows = list(csv.DictReader(handle, delimiter="\t"))
    route_tf_ids = {row.get("transcription_factor_node_id", "") for row in route_rows}

    edge_fields, edge_rows = read_tsv(output / "mechanism_edges.tsv")
    direct_edge_ids: dict[str, list[str]] = {node_id: [] for node_id in ROLE_REPAIRS}
    for row in edge_rows:
        source_id = row.get("source_node_id", "")
        pathway = row.get("pathway_name", "").casefold()
        relation = row.get("relation_type", "").casefold()
        if source_id in direct_edge_ids and (
            "transcription" in pathway
            or "target_gene" in pathway
            or relation in {"activates", "represses", "induces_target_gene"}
        ):
            direct_edge_ids[source_id].append(row["edge_id"])

    added: list[dict[str, str]] = []
    for node_id, expected_label in ROLE_REPAIRS.items():
        if node_id not in nodes:
            raise ValueError(f"Role-repair node is absent from bundle: {node_id}")
        actual_label = nodes[node_id].get("canonical_label", "")
        if actual_label != expected_label:
            raise ValueError(f"Unexpected label for {node_id}: {actual_label!r} != {expected_label!r}")
        if node_id not in route_tf_ids:
            raise ValueError(f"Role-repair node is not used as a route TF: {node_id}")
        if not direct_edge_ids[node_id]:
            raise ValueError(f"Role-repair node has no direct transcription-like edge: {node_id}")
        if (node_id, "transcription_factor") not in existing_roles:
            added.append(
                {
                    "node_id": node_id,
                    "role": "transcription_factor",
                    "role_source": ROLE_SOURCE,
                    "role_evidence": f"{ROLE_EVIDENCE} edge_ids={';'.join(direct_edge_ids[node_id])}",
                }
            )

    write_tsv(role_path, role_fields, role_rows + added)
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
    metadata.setdefault("counts", {})["node_roles"] = len(role_rows) + len(added)
    metadata.setdefault("counts", {})["ligand_route_coverage"] = len(coverage_rows)
    metadata.setdefault("graph_policy", {})["transcription_factor_role_repairs_are_evidence_layer_only"] = True
    statement = (
        "A narrowly scoped TF-role repair adds transcription_factor roles only to existing route TF nodes with "
        "direct evidence-gated transcription-like edges; it does not create graph edges or confidence scores."
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
        "direct_transcription_edge_counts": {node_id: len(edge_ids) for node_id, edge_ids in sorted(direct_edge_ids.items())},
        "coverage": coverage_summary,
        "graph_edges_changed": False,
        "route_evidence_rows_changed": False,
        "literature_expansion_rows_changed": False,
        "confidence_scores_created": False,
    }
    (output / "transcription_factor_role_repair_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    metadata.setdefault("files", {})["transcription_factor_role_repair_summary"] = "transcription_factor_role_repair_summary.json"
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
