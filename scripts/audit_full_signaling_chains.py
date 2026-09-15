#!/usr/bin/env python3
"""Audit complete and incomplete ligand-to-target signaling paths.

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
    "chain_status",
    "missing_steps",
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
POSSIBLE_PATH_FIELDS = [
    "possible_path_id",
    "path_status",
    "path_expression",
    "missing_link",
    "ligand_node_id",
    "ligand_label",
    "ligand_receptor_edge_id",
    "receptor_node_id",
    "receptor_label",
    "unknown_relay_label",
    "target_gene_node_id",
    "target_gene_label",
    "target_output_form_id",
    "bridge_id",
    "pathway_name",
    "evidence_ids",
    "causal_status",
    "traversal_status",
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


def write_possible_paths(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=POSSIBLE_PATH_FIELDS,
            delimiter="\t",
            lineterminator="\n",
        )
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

    ligand_receptor_by_target: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in ligand_receptor:
        ligand_receptor_by_target[row["target_node_id"]].append(row)

    # Retain evidence-backed path fragments as well as complete chains.  A
    # fragment is only emitted when an adjacent graph edge is absent; this
    # does not infer a missing mechanism or turn the fragment into a causal
    # edge.
    raw_chains: list[tuple[dict[str, str] | None, dict[str, str] | None, dict[str, str] | None]] = []
    for first in ligand_receptor:
        seconds = receptor_tf_by_source[first["target_node_id"]]
        if not seconds:
            raw_chains.append((first, None, None))
            continue
        for second in seconds:
            thirds = tf_target_by_source[second["target_node_id"]]
            if thirds:
                raw_chains.extend((first, second, third) for third in thirds)
            else:
                raw_chains.append((first, second, None))

    receptor_nodes_with_ligand = set(ligand_receptor_by_target)
    tf_nodes_with_receptor = {
        row["target_node_id"] for row in receptor_tf
    }
    for second in receptor_tf:
        if second["source_node_id"] not in receptor_nodes_with_ligand:
            thirds = tf_target_by_source[second["target_node_id"]]
            if thirds:
                raw_chains.extend((None, second, third) for third in thirds)
            else:
                raw_chains.append((None, second, None))
    for third in tf_target:
        if third["source_node_id"] not in tf_nodes_with_receptor:
            raw_chains.append((None, None, third))

    def edge_sort_key(edge: dict[str, str] | None) -> str:
        return edge["edge_id"] if edge else ""

    raw_chains = list({
        tuple(edge["edge_id"] if edge else "" for edge in chain): chain
        for chain in raw_chains
    }.values())
    raw_chains.sort(key=lambda chain: tuple(edge_sort_key(edge) for edge in chain))
    chain_rows: list[dict[str, object]] = []
    for index, (first, second, third) in enumerate(raw_chains, start=1):
        missing_steps = []
        if first is None:
            missing_steps.append("ligand_to_receptor")
        if second is None:
            missing_steps.append("receptor_to_transcription_factor")
        if third is None:
            missing_steps.append("transcription_factor_to_target_gene")
        evidence_ids = ";".join(
            dict.fromkeys(
                value
                for edge in (first, second, third)
                if edge is not None
                for value in edge.get("evidence_ids", "").split(";")
                if value
            )
        )
        first = first or {}
        second = second or {}
        third = third or {}
        chain_rows.append(
            {
                "chain_id": f"CHAIN:{index:05d}",
                "chain_status": "complete" if not missing_steps else "partial",
                "missing_steps": ";".join(missing_steps),
                "ligand_node_id": first.get("source_node_id", ""),
                "ligand_label": first.get("source_label", ""),
                "ligand_receptor_edge_id": first.get("edge_id", ""),
                "ligand_receptor_pathway": first.get("pathway_name", ""),
                "receptor_node_id": first.get("target_node_id", ""),
                "receptor_label": first.get("target_label", ""),
                "receptor_tf_edge_id": second.get("edge_id", ""),
                "receptor_tf_pathway": second.get("pathway_name", ""),
                "transcription_factor_node_id": second.get("target_node_id", ""),
                "transcription_factor_label": second.get("target_label", ""),
                "tf_target_edge_id": third.get("edge_id", ""),
                "tf_target_pathway": third.get("pathway_name", ""),
                "target_gene_node_id": third.get("target_node_id", ""),
                "target_gene_label": third.get("target_label", ""),
                "target_relation": third.get("relation_type", ""),
                "module_sequence": ">".join(
                    edge["module"] for edge in (first, second, third) if edge
                ),
                "evidence_ids": evidence_ids,
            }
        )

    complete_rows = [row for row in chain_rows if row["chain_status"] == "complete"]
    unique_node_chains = {
        (
            row["ligand_node_id"],
            row["receptor_node_id"],
            row["transcription_factor_node_id"],
            row["target_gene_node_id"],
        )
        for row in complete_rows
    }
    unique_edge_chains = {
        (row["ligand_receptor_edge_id"], row["receptor_tf_edge_id"], row["tf_target_edge_id"])
        for row in complete_rows
    }
    same_pathway = [
        row for row in complete_rows
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
            "edge_chain_instances": len(complete_rows),
            "unique_edge_chains": len(unique_edge_chains),
            "unique_four_node_topologies": len(unique_node_chains),
            "same_pathway_edge_chain_instances": len(same_pathway),
        },
        "partial_chain_counts": dict(Counter(
            row["missing_steps"]
            for row in chain_rows
            if row["chain_status"] == "partial"
        )),
        "retained_chain_record_count": len(chain_rows),
        "distinct_receptor_transcription_factor_pairs": len({
            (row["receptor_node_id"], row["transcription_factor_node_id"])
            for row in chain_rows
        }),
        "distinct_ligand_receptor_transcription_factor_routes": len({
            (row["ligand_node_id"], row["receptor_node_id"], row["transcription_factor_node_id"])
            for row in chain_rows
        }),
        "module_sequences": dict(Counter(row["module_sequence"] for row in complete_rows)),
        "target_relations_in_full_chains": dict(Counter(row["target_relation"] for row in complete_rows)),
    }
    return chain_rows, summary


def audit_possible_paths(bundle_dir: Path) -> tuple[list[dict[str, object]], dict[str, object]]:
    """Retain conservative ligand-to-target hypotheses with an unknown relay."""
    roles: dict[str, set[str]] = defaultdict(set)
    for row in read_tsv(bundle_dir / "mechanism_node_roles.tsv"):
        roles[row["node_id"]].add(row["role"])
    nodes = {
        row["node_id"]: row
        for row in read_tsv(bundle_dir / "mechanism_nodes.tsv")
    }
    edges = {
        row["edge_id"]: row
        for row in read_tsv(bundle_dir / "mechanism_edges.tsv")
    }
    validated_path = bundle_dir / "mechanism_output_bridges_validated.tsv"
    if not validated_path.exists():
        return [], {
            "possible_missing_relay_instances": 0,
            "unique_possible_ligand_receptor_target_paths": 0,
        }

    rows: list[dict[str, object]] = []
    for bridge in read_tsv(validated_path):
        target_forms = []
        for form_id in bridge.get("product_form_ids", "").split(";"):
            if not form_id.startswith("OUTPUT_PROTEIN:"):
                continue
            target_node_id = form_id.split(":", 1)[1]
            if "target_gene" in roles[target_node_id]:
                target_forms.append((form_id, target_node_id))
        for edge_id in bridge.get("source_edge_ids", "").split(";"):
            edge = edges.get(edge_id)
            if not edge:
                continue
            if (
                edge["relation_type"] != "binds_receptor"
                or "ligand" not in roles[edge["source_node_id"]]
                or "receptor" not in roles[edge["target_node_id"]]
            ):
                continue
            for form_id, target_node_id in target_forms:
                evidence_ids = ";".join(dict.fromkeys(
                    value
                    for value in (
                        edge.get("evidence_ids", ""),
                        bridge.get("review_evidence_ids", ""),
                    )
                    for value in value.split(";")
                    if value
                ))
                rows.append(
                    {
                        "possible_path_id": "",
                        "path_status": "possible_missing_relay",
                        "path_expression": "ligand>receptor>????>target_gene_expression",
                        "missing_link": "receptor_to_transcription_factor_or_internal_relay",
                        "ligand_node_id": edge["source_node_id"],
                        "ligand_label": edge["source_label"],
                        "ligand_receptor_edge_id": edge_id,
                        "receptor_node_id": edge["target_node_id"],
                        "receptor_label": edge["target_label"],
                        "unknown_relay_label": "????",
                        "target_gene_node_id": target_node_id,
                        "target_gene_label": nodes[target_node_id]["canonical_name"],
                        "target_output_form_id": form_id,
                        "bridge_id": bridge["bridge_id"],
                        "pathway_name": edge["pathway_name"],
                        "evidence_ids": evidence_ids,
                        "causal_status": "not_asserted",
                        "traversal_status": "possible_path_not_traversable",
                    }
                )

    rows.sort(key=lambda row: (
        row["ligand_receptor_edge_id"],
        row["target_gene_node_id"],
        row["bridge_id"],
    ))
    for index, row in enumerate(rows, start=1):
        row["possible_path_id"] = f"POSSIBLE:{index:05d}"
    summary = {
        "possible_missing_relay_instances": len(rows),
        "unique_possible_ligand_receptor_target_paths": len({
            (
                row["ligand_receptor_edge_id"],
                row["target_gene_node_id"],
            )
            for row in rows
        }),
    }
    return rows, summary


def update_bundle_metadata(
    bundle_dir: Path,
    possible_path: Path,
    possible_count: int,
) -> None:
    """Register the hypothesis artifact without changing graph-edge counts."""
    metadata_path = bundle_dir / "bundle_metadata.json"
    if not metadata_path.exists():
        return
    metadata = json.loads(metadata_path.read_text())
    metadata.setdefault("files", {})["possible_signaling_paths"] = possible_path.name
    metadata.setdefault("counts", {})["possible_signaling_paths"] = possible_count
    policy = metadata.setdefault("graph_policy", {})
    policy["possible_signaling_paths_are_hypotheses_only"] = True
    policy["possible_signaling_paths_are_not_graph_edges"] = True
    contract = metadata.setdefault("accuracy_contract", [])
    statement = (
        "Possible signaling paths retain validated ligand-receptor and target-output "
        "evidence with unknown relays; they are hypotheses, not causal graph edges."
    )
    if statement not in contract:
        contract.append(statement)
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n")


def main() -> None:
    args = parse_args()
    bundle_dir = args.bundle_dir.resolve()
    output = (args.output or bundle_dir / "full_signaling_chain_audit.tsv").resolve()
    summary_path = (args.summary or bundle_dir / "full_signaling_chain_audit.json").resolve()
    possible_output = bundle_dir / "mechanism_possible_signaling_paths.tsv"
    rows, summary = audit(bundle_dir)
    possible_rows, possible_summary = audit_possible_paths(bundle_dir)
    summary["possible_path_counts"] = possible_summary
    if args.compare_bundle:
        _, previous = audit(args.compare_bundle.resolve())
        current_counts = summary["full_chain_counts"]
        previous_counts = previous["full_chain_counts"]
        summary["comparison"] = {
            "prior_bundle_dir": release_path(args.compare_bundle.resolve()),
            "prior_full_chain_counts": previous_counts,
            "prior_partial_chain_counts": previous["partial_chain_counts"],
            "prior_retained_chain_record_count": previous["retained_chain_record_count"],
            "delta": {
                key: current_counts[key] - previous_counts[key]
                for key in current_counts
                if key in previous_counts
            },
            "partial_delta": {
                key: summary["partial_chain_counts"].get(key, 0) - previous["partial_chain_counts"].get(key, 0)
                for key in set(summary["partial_chain_counts"]) | set(previous["partial_chain_counts"])
            },
            "retained_chain_record_delta": (
                summary["retained_chain_record_count"]
                - previous["retained_chain_record_count"]
            ),
        }
    write_tsv(output, rows)
    write_possible_paths(possible_output, possible_rows)
    update_bundle_metadata(bundle_dir, possible_output, len(possible_rows))
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary["full_chain_counts"], sort_keys=True))


if __name__ == "__main__":
    main()
