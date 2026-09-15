#!/usr/bin/env python3
"""Audit complete ligand-to-target signaling chains in a graph bundle.

The audit is deliberately narrower than generic graph reachability. A full
chain is one exported, evidence-gated sequence with these role-compatible
steps: ligand --binds_receptor--> receptor --(any exported relay)-->
transcription factor --(induces/represses/regulates_target_gene)--> target
gene. The three edges may have different pathway labels because the current
release stores receptor-proximal and target-gene evidence in separate module
pathway namespaces. Output bridges and typed-form transitions are excluded;
the graph release contract marks them as conditional or non-causal.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BUNDLE = ROOT / "data" / "processed" / "mechanism_graph_module20_24_v2026_09_01"
TARGET_RELATIONS = {"induces_target_gene", "represses_target_gene", "regulates_target_gene"}

CHAIN_FIELDS = [
    "chain_id",
    "ligand_node_id",
    "ligand_label",
    "ligand_receptor_edge_id",
    "ligand_receptor_pathway",
    "receptor_node_id",
    "receptor_label",
    "receptor_tf_edge_id",
    "receptor_tf_pathway",
    "transcription_factor_node_id",
    "transcription_factor_label",
    "tf_target_edge_id",
    "tf_target_pathway",
    "target_gene_node_id",
    "target_gene_label",
    "target_relation",
    "module_sequence",
    "evidence_ids",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument(
        "--compare-bundle",
        type=Path,
        default=None,
        help="Optional earlier bundle used to record chain-count deltas.",
    )
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--summary", type=Path, default=None)
    return parser.parse_args()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CHAIN_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def release_path(path: Path) -> str:
    """Return repository-relative paths when the audited bundle is in-repo."""
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def audit(bundle_dir: Path) -> tuple[list[dict[str, object]], dict[str, object]]:
    roles: dict[str, set[str]] = defaultdict(set)
    for row in read_tsv(bundle_dir / "mechanism_node_roles.tsv"):
        roles[row["node_id"]].add(row["role"])
    edges = read_tsv(bundle_dir / "mechanism_edges.tsv")

    ligand_receptor = [
        row for row in edges
        if row["relation_type"] == "binds_receptor"
        and "ligand" in roles[row["source_node_id"]]
        and "receptor" in roles[row["target_node_id"]]
    ]
    receptor_tf = [
        row for row in edges
        if "receptor" in roles[row["source_node_id"]]
        and "transcription_factor" in roles[row["target_node_id"]]
    ]
    tf_target = [
        row for row in edges
        if row["relation_type"] in TARGET_RELATIONS
        and "transcription_factor" in roles[row["source_node_id"]]
        and "target_gene" in roles[row["target_node_id"]]
    ]

    receptor_tf_by_source: dict[str, list[dict[str, str]]] = defaultdict(list)
    tf_target_by_source: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in receptor_tf:
        receptor_tf_by_source[row["source_node_id"]].append(row)
    for row in tf_target:
        tf_target_by_source[row["source_node_id"]].append(row)

    raw_chains: list[tuple[dict[str, str], dict[str, str], dict[str, str]]] = []
    for first in ligand_receptor:
        for second in receptor_tf_by_source[first["target_node_id"]]:
            for third in tf_target_by_source[second["target_node_id"]]:
                raw_chains.append((first, second, third))

    raw_chains.sort(key=lambda chain: tuple(edge["edge_id"] for edge in chain))
    chain_rows: list[dict[str, object]] = []
    for index, (first, second, third) in enumerate(raw_chains, start=1):
        evidence_ids = ";".join(
            dict.fromkeys(
                value
                for edge in (first, second, third)
                for value in edge.get("evidence_ids", "").split(";")
                if value
            )
        )
        chain_rows.append(
            {
                "chain_id": f"CHAIN:{index:05d}",
                "ligand_node_id": first["source_node_id"],
                "ligand_label": first["source_label"],
                "ligand_receptor_edge_id": first["edge_id"],
                "ligand_receptor_pathway": first["pathway_name"],
                "receptor_node_id": first["target_node_id"],
                "receptor_label": first["target_label"],
                "receptor_tf_edge_id": second["edge_id"],
                "receptor_tf_pathway": second["pathway_name"],
                "transcription_factor_node_id": second["target_node_id"],
                "transcription_factor_label": second["target_label"],
                "tf_target_edge_id": third["edge_id"],
                "tf_target_pathway": third["pathway_name"],
                "target_gene_node_id": third["target_node_id"],
                "target_gene_label": third["target_label"],
                "target_relation": third["relation_type"],
                "module_sequence": ">".join(edge["module"] for edge in (first, second, third)),
                "evidence_ids": evidence_ids,
            }
        )

    unique_node_chains = {
        (
            row["ligand_node_id"],
            row["receptor_node_id"],
            row["transcription_factor_node_id"],
            row["target_gene_node_id"],
        )
        for row in chain_rows
    }
    unique_edge_chains = {
        (row["ligand_receptor_edge_id"], row["receptor_tf_edge_id"], row["tf_target_edge_id"])
        for row in chain_rows
    }
    same_pathway = [
        row for row in chain_rows
        if row["ligand_receptor_pathway"] == row["receptor_tf_pathway"] == row["tf_target_pathway"]
    ]
    summary: dict[str, object] = {
        "bundle_dir": release_path(bundle_dir),
        "definition": {
            "step_1": "ligand-role source --binds_receptor--> receptor-role target",
            "step_2": "receptor-role source --any exported relay--> transcription_factor-role target",
            "step_3": "transcription_factor-role source --induces/represses/regulates_target_gene--> target_gene-role target",
            "pathway_label_requirement": "none; pathway labels may differ across module namespaces",
            "excluded": ["mechanism_output_bridge_candidates.tsv", "mechanism_output_bridges_validated.tsv", "mechanism_entity_transitions.tsv"],
        },
        "step_edge_counts": {
            "ligand_receptor": len(ligand_receptor),
            "receptor_transcription_factor": len(receptor_tf),
            "transcription_factor_target_gene": len(tf_target),
        },
        "full_chain_counts": {
            "edge_chain_instances": len(chain_rows),
            "unique_edge_chains": len(unique_edge_chains),
            "unique_four_node_topologies": len(unique_node_chains),
            "same_pathway_edge_chain_instances": len(same_pathway),
        },
        "distinct_receptor_transcription_factor_pairs": len({
            (row["receptor_node_id"], row["transcription_factor_node_id"])
            for row in chain_rows
        }),
        "distinct_ligand_receptor_transcription_factor_routes": len({
            (row["ligand_node_id"], row["receptor_node_id"], row["transcription_factor_node_id"])
            for row in chain_rows
        }),
        "module_sequences": dict(Counter(row["module_sequence"] for row in chain_rows)),
        "target_relations_in_full_chains": dict(Counter(row["target_relation"] for row in chain_rows)),
    }
    return chain_rows, summary


def main() -> None:
    args = parse_args()
    bundle_dir = args.bundle_dir.resolve()
    output = (args.output or bundle_dir / "full_signaling_chain_audit.tsv").resolve()
    summary_path = (args.summary or bundle_dir / "full_signaling_chain_audit.json").resolve()
    rows, summary = audit(bundle_dir)
    if args.compare_bundle:
        _, previous = audit(args.compare_bundle.resolve())
        current_counts = summary["full_chain_counts"]
        previous_counts = previous["full_chain_counts"]
        summary["comparison"] = {
            "prior_bundle_dir": release_path(args.compare_bundle.resolve()),
            "prior_full_chain_counts": previous_counts,
            "delta": {
                key: current_counts[key] - previous_counts[key]
                for key in current_counts
                if key in previous_counts
            },
        }
    write_tsv(output, rows)
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary["full_chain_counts"], sort_keys=True))


if __name__ == "__main__":
    main()
