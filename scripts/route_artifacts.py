#!/usr/bin/env python3
"""Materialize normalized node and edge views for signaling route evidence.

The legacy route table remains the compact compatibility view.  These tables
preserve the ordered graph components used by a route so shared intermediates
can be indexed across routes without treating evidence-only routes as causal
graph edges.
"""

from __future__ import annotations

import csv
import gzip
import json
from collections import defaultdict
from pathlib import Path
from typing import Iterable, Mapping


ROUTE_NODE_FIELDS = [
    "route_evidence_id",
    "step_order",
    "node_id",
    "node_label",
    "node_role",
    "node_status",
    "source_edge_id",
    "source_chain_id",
]

ROUTE_EDGE_FIELDS = [
    "route_evidence_id",
    "step_order",
    "source_node_id",
    "source_label",
    "target_node_id",
    "target_label",
    "edge_id",
    "edge_role",
    "edge_status",
    "relation_type",
    "graph_evidence_status",
    "evidence_ids",
    "route_linkage_status",
    "causal_status",
    "traversal_status",
    "source_chain_id",
]

ROUTE_NODE_FILE = "mechanism_route_nodes.tsv.gz"
ROUTE_EDGE_FILE = "mechanism_route_edges.tsv.gz"


def _write_gzip_tsv(path: Path, fieldnames: list[str], rows: Iterable[Mapping[str, object]]) -> int:
    count = 0
    with gzip.open(path, "wt", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: str(row.get(field, "")) for field in fieldnames})
            count += 1
    return count


def _chain_tokens(source_chain_id: str) -> list[str]:
    value = str(source_chain_id or "")
    if value.startswith("graph_components:"):
        value = value.split(":", 1)[1]
        return [token for token in value.split("+") if token]
    if ">" in value:
        return [token for token in value.split(">") if token]
    return []


def _node_role(node_id: str, route: Mapping[str, str], roles_by_node: Mapping[str, set[str]]) -> str:
    role_fields = (
        ("ligand_node_id", "ligand"),
        ("receptor_node_id", "receptor"),
        ("intracellular_continuation_node_id", "signaling_cascade"),
        ("transcription_factor_node_id", "transcription_factor"),
        ("target_gene_node_id", "target_gene"),
    )
    for field, role in role_fields:
        if route.get(field, "") == node_id:
            return role
    if route.get("output_node_id", "") == node_id:
        return "output"
    return "|".join(sorted(roles_by_node.get(node_id, set()))) or "unknown"


def _label(node_id: str, nodes_by_id: Mapping[str, Mapping[str, str]], route: Mapping[str, str]) -> str:
    node = nodes_by_id.get(node_id, {})
    if node.get("canonical_label") or node.get("canonical_name"):
        return node.get("canonical_label") or node.get("canonical_name", "")
    route_label_fields = (
        ("ligand_node_id", "ligand_label"),
        ("receptor_node_id", "receptor_label"),
        ("intracellular_continuation_node_id", "intracellular_continuation_label"),
        ("transcription_factor_node_id", "transcription_factor_label"),
        ("target_gene_node_id", "target_gene_label"),
        ("output_node_id", "output_label"),
    )
    for node_field, label_field in route_label_fields:
        if route.get(node_field, "") == node_id and route.get(label_field, ""):
            return route[label_field]
    return ""


def build_normalized_route_artifacts(
    routes: Iterable[Mapping[str, str]],
    nodes: Iterable[Mapping[str, str]],
    edges: Iterable[Mapping[str, str]],
    edge_sources: Iterable[Mapping[str, str]] = (),
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """Return ordered route-node and route-edge rows for every route.

    Parsed source-chain edges are retained when they form the route path.  A
    graph edge that records a ligand-to-output observation but is not
    contiguous with the route is retained as ``output_observation`` rather
    than being mistaken for a causal signaling hop.  Missing transitions are
    explicit rows with empty edge IDs and non-causal statuses.
    """

    nodes_by_id = {str(row["node_id"]): dict(row) for row in nodes}
    edges_by_id = {str(row["edge_id"]): dict(row) for row in edges}
    roles_by_node: dict[str, set[str]] = defaultdict(set)
    for node in nodes_by_id.values():
        node_type = str(node.get("node_type", ""))
        if node_type in {"ligand", "protein_ligand"}:
            roles_by_node[node["node_id"]].add("ligand")
        elif node_type in {"receptor"}:
            roles_by_node[node["node_id"]].add("receptor")
        elif node_type in {"transcription_factor", "tf"}:
            roles_by_node[node["node_id"]].add("transcription_factor")
        elif node_type == "target_gene":
            roles_by_node[node["node_id"]].add("target_gene")
    edge_sources_by_edge: dict[str, list[str]] = defaultdict(list)
    for source in edge_sources:
        edge_id = str(source.get("edge_id", ""))
        source_id = str(source.get("edge_source_id", ""))
        if edge_id and source_id:
            edge_sources_by_edge[edge_id].append(source_id)

    node_rows: list[dict[str, str]] = []
    edge_rows: list[dict[str, str]] = []
    for route in routes:
        route_id = str(route.get("route_evidence_id", ""))
        if not route_id:
            continue
        source_chain_id = str(route.get("source_chain_id", ""))
        parsed_edges: list[dict[str, str]] = []
        parsed_tf_nodes: list[str] = []
        for token in _chain_tokens(source_chain_id):
            if token.startswith("TF:"):
                node_id = token.split(":", 1)[1]
                if node_id in nodes_by_id:
                    parsed_tf_nodes.append(node_id)
            elif token in edges_by_id:
                parsed_edges.append(edges_by_id[token])

        ligand_id = str(route.get("ligand_node_id", ""))
        receptor_id = str(route.get("receptor_node_id", ""))
        tf_id = str(route.get("transcription_factor_node_id", "")) or (parsed_tf_nodes[-1] if parsed_tf_nodes else "")
        terminal_id = str(route.get("target_gene_node_id", "")) or str(route.get("output_node_id", ""))
        path_node_ids: list[str] = []

        def add_path_node(node_id: str) -> None:
            if node_id and node_id not in path_node_ids:
                path_node_ids.append(node_id)

        add_path_node(ligand_id)
        add_path_node(receptor_id)
        used_edge_ids: set[str] = set()
        path_edge_ids: set[str] = set()
        supplemental_edges: list[tuple[dict[str, str], str]] = []
        for edge in parsed_edges:
            edge_id = str(edge["edge_id"])
            source_id = str(edge["source_node_id"])
            target_id = str(edge["target_node_id"])
            if path_node_ids and source_id == path_node_ids[-1]:
                add_path_node(target_id)
                used_edge_ids.add(edge_id)
                path_edge_ids.add(edge_id)
            elif not path_node_ids:
                add_path_node(source_id)
                add_path_node(target_id)
                used_edge_ids.add(edge_id)
                path_edge_ids.add(edge_id)
            else:
                supplemental_edges.append((edge, "output_observation" if source_id == ligand_id else "supplemental_graph_evidence"))
        for node_id in parsed_tf_nodes:
            add_path_node(node_id)

        # The compact route fields remain authoritative when a source chain
        # is unavailable or only records a subset of the graph components.
        add_path_node(str(route.get("intracellular_continuation_node_id", "")))
        if tf_id:
            add_path_node(tf_id)
        add_path_node(terminal_id)

        explicit_edge_ids = {
            str(route.get(field, ""))
            for field in (
                "ligand_receptor_edge_id", "receptor_intracellular_edge_id",
                "intracellular_tf_edge_id", "tf_target_edge_id",
            )
            if route.get(field, "")
        }
        for edge_id in explicit_edge_ids:
            edge = edges_by_id.get(edge_id)
            if edge and edge_id not in used_edge_ids:
                parsed_edges.append(edge)
                used_edge_ids.add(edge_id)

        edge_by_pair: dict[tuple[str, str], dict[str, str]] = {}
        for edge in parsed_edges:
            edge_by_pair.setdefault((edge["source_node_id"], edge["target_node_id"]), edge)

        def edge_row(
            *,
            source_id: str,
            target_id: str,
            edge: Mapping[str, str] | None,
            role: str,
            status: str,
        ) -> dict[str, str]:
            edge_id = str(edge.get("edge_id", "")) if edge else ""
            return {
                "route_evidence_id": route_id,
                "step_order": "",
                "source_node_id": source_id,
                "source_label": _label(source_id, nodes_by_id, route),
                "target_node_id": target_id,
                "target_label": _label(target_id, nodes_by_id, route),
                "edge_id": edge_id,
                "edge_role": role,
                "edge_status": status,
                "relation_type": str(edge.get("relation_type", "")) if edge else "",
                "graph_evidence_status": str(edge.get("evidence_status", "")) if edge else "not_asserted",
                "evidence_ids": "|".join(edge_sources_by_edge.get(edge_id, [])) if edge_id else str(route.get("evidence_ids", "")),
                "route_linkage_status": str(route.get("route_linkage_status", "")),
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "source_chain_id": source_chain_id,
            }

        route_edge_rows: list[dict[str, str]] = []
        for source_id, target_id in zip(path_node_ids, path_node_ids[1:]):
            edge = edge_by_pair.get((source_id, target_id))
            if edge:
                role = "ligand_receptor" if edge["edge_id"] == route.get("ligand_receptor_edge_id", "") else "mechanistic_component"
                route_edge_rows.append(edge_row(source_id=source_id, target_id=target_id, edge=edge, role=role, status="graph_edge_asserted"))
            else:
                role = "tf_to_target_missing" if source_id == tf_id and target_id == terminal_id else "intracellular_to_tf_missing"
                route_edge_rows.append(edge_row(source_id=source_id, target_id=target_id, edge=None, role=role, status="unasserted_missing_route_link"))
        represented_pairs = {(row["source_node_id"], row["target_node_id"], row["edge_id"]) for row in route_edge_rows}
        for edge, role in supplemental_edges:
            key = (edge["source_node_id"], edge["target_node_id"], edge["edge_id"])
            if key not in represented_pairs:
                route_edge_rows.append(edge_row(source_id=edge["source_node_id"], target_id=edge["target_node_id"], edge=edge, role=role, status="graph_edge_asserted"))
                represented_pairs.add(key)
        for edge in parsed_edges:
            key = (edge["source_node_id"], edge["target_node_id"], edge["edge_id"])
            if key not in represented_pairs:
                role = "output_observation" if edge["source_node_id"] == ligand_id and edge["target_node_id"] == terminal_id else "supplemental_graph_evidence"
                route_edge_rows.append(edge_row(source_id=edge["source_node_id"], target_id=edge["target_node_id"], edge=edge, role=role, status="graph_edge_asserted"))
                represented_pairs.add(key)
        for index, row in enumerate(route_edge_rows, start=1):
            row["step_order"] = str(index)
            edge_rows.append(row)

        for index, node_id in enumerate(path_node_ids, start=1):
            source_edge_id = ""
            for edge in parsed_edges:
                if node_id in {edge["source_node_id"], edge["target_node_id"]}:
                    source_edge_id = edge["edge_id"]
                    break
            node_rows.append(
                {
                    "route_evidence_id": route_id,
                    "step_order": str(index),
                    "node_id": node_id,
                    "node_label": _label(node_id, nodes_by_id, route),
                    "node_role": _node_role(node_id, route, roles_by_node),
                    "node_status": "route_graph_component" if node_id in nodes_by_id else "route_annotation",
                    "source_edge_id": source_edge_id,
                    "source_chain_id": source_chain_id,
                }
            )

    return node_rows, edge_rows


def write_normalized_route_artifacts(
    bundle_dir: Path,
    routes: Iterable[Mapping[str, str]],
    nodes: Iterable[Mapping[str, str]],
    edges: Iterable[Mapping[str, str]],
    edge_sources: Iterable[Mapping[str, str]] = (),
) -> dict[str, int]:
    """Write compressed normalized route artifacts and update bundle metadata."""

    route_rows = list(routes)
    node_rows, edge_rows = build_normalized_route_artifacts(route_rows, nodes, edges, edge_sources)
    node_count = _write_gzip_tsv(bundle_dir / ROUTE_NODE_FILE, ROUTE_NODE_FIELDS, node_rows)
    edge_count = _write_gzip_tsv(bundle_dir / ROUTE_EDGE_FILE, ROUTE_EDGE_FIELDS, edge_rows)
    metadata_path = bundle_dir / "bundle_metadata.json"
    if metadata_path.exists():
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        metadata.setdefault("files", {})["route_nodes"] = ROUTE_NODE_FILE
        metadata.setdefault("files", {})["route_edges"] = ROUTE_EDGE_FILE
        metadata.setdefault("counts", {})["route_nodes"] = node_count
        metadata.setdefault("counts", {})["route_edges"] = edge_count
        policy = metadata.setdefault("graph_policy", {})
        policy["normalized_route_artifacts_are_evidence_layer_only"] = True
        policy["normalized_route_missing_links_are_not_graph_edges"] = True
        metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    return {"route_nodes": node_count, "route_edges": edge_count}
