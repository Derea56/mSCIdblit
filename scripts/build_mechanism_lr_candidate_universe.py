#!/usr/bin/env python3
"""Build an additive LR candidate projection for an mSCIdblit release.

This table is a release output, not a mechanism graph table.  It preserves the
method-resource candidate universe and records exact, deterministic joins to
the graph and route-evidence layers when those joins are available.  It never
creates graph edges, evidence claims, confidence scores, or causal assertions.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
from collections import defaultdict
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_GRAPH = ROOT / "data" / "processed" / "mechanism_graph_module20_24_v2026_09_25_literature_expansion627"
DEFAULT_METHOD = ROOT / "data" / "processed" / "method_resource_migration_v1"
DEFAULT_OUTPUT = ROOT / "data" / "processed" / "mechanism_lr_candidate_universe_v1"

FIELDS = [
    "candidate_pair_id",
    "species_scope",
    "ligand_name",
    "receptor_name",
    "normalized_ligand_name",
    "normalized_receptor_name",
    "communication_kind",
    "source_method_count",
    "source_record_count",
    "source_methods_json",
    "source_resource_keys_json",
    "source_record_keys_json",
    "ligand_components",
    "receptor_components",
    "ligand_node_id",
    "receptor_node_id",
    "mechanism_graph_status",
    "graph_edge_ids_json",
    "graph_exportable",
    "route_status",
    "route_tier",
    "route_linkage_status",
    "causal_status",
    "traversal_status",
    "evidence_status",
    "unresolved_mapping_reason",
    "source_snapshot_id",
    "mechanism_graph_release",
    "candidate_role",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def read_gzip_tsv(path: Path) -> Iterable[dict[str, str]]:
    with gzip.open(path, "rt", newline="", encoding="utf-8") as handle:
        yield from csv.DictReader(handle, delimiter="\t")


def stable_json(values: Iterable[str]) -> str:
    return json.dumps(sorted({value for value in values if value}), separators=(",", ":"))


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def parse_json_list(value: str) -> list[str]:
    try:
        parsed = json.loads(value or "[]")
    except json.JSONDecodeError as exc:
        raise ValueError(f"Expected JSON list, got {value!r}") from exc
    if not isinstance(parsed, list):
        raise ValueError(f"Expected JSON list, got {type(parsed).__name__}")
    return [str(item) for item in parsed]


def index_nodes(rows: list[dict[str, str]]) -> dict[str, set[str]]:
    index: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        node_id = row.get("node_id", "")
        if not node_id:
            continue
        for field in ("canonical_name", "canonical_label", "gene_symbol"):
            value = row.get(field, "").strip()
            if value:
                index[value].add(node_id)
    return index


def component_index(rows: list[dict[str, str]]) -> dict[str, dict[str, list[tuple[int, str]]]]:
    result: dict[str, dict[str, list[tuple[int, str]]]] = defaultdict(lambda: defaultdict(list))
    for row in rows:
        candidate_id = row.get("canonical_communication_id", "")
        side = row.get("side", "")
        component = row.get("component_name", "")
        if not candidate_id or side not in {"ligand", "receptor"} or not component:
            continue
        try:
            ordinal = int(row.get("component_ordinal", "0") or 0)
        except ValueError:
            ordinal = 0
        result[candidate_id][side].append((ordinal, component))
    return result


def graph_indexes(
    edges: list[dict[str, str]],
    nodes: list[dict[str, str]],
) -> dict[tuple[str, str], list[dict[str, str]]]:
    node_labels = {row.get("node_id", ""): row.get("canonical_name", "") for row in nodes}
    pairs: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for edge in edges:
        if edge.get("relation_type") != "binds_receptor":
            continue
        ligand = edge.get("source_label", "") or node_labels.get(edge.get("source_node_id", ""), "")
        receptor = edge.get("target_label", "") or node_labels.get(edge.get("target_node_id", ""), "")
        if ligand and receptor:
            pairs[(ligand.strip(), receptor.strip())].append(edge)
    return pairs


def route_index(path: Path) -> dict[tuple[str, str], dict[str, set[str]]]:
    result: dict[tuple[str, str], dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    if not path.is_file():
        return result
    for row in read_gzip_tsv(path):
        ligand = row.get("ligand_label", "").strip()
        receptor = row.get("receptor_label", "").strip()
        if not ligand or not receptor:
            continue
        key = (ligand, receptor)
        for field in ("route_status", "route_tier", "route_linkage_status", "causal_status", "traversal_status"):
            value = row.get(field, "").strip()
            if value:
                result[key][field].add(value)
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--graph-bundle-dir", type=Path, default=DEFAULT_GRAPH)
    parser.add_argument("--method-migration-dir", type=Path, default=DEFAULT_METHOD)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    graph = args.graph_bundle_dir.resolve()
    method = args.method_migration_dir.resolve()
    output = args.output_dir.resolve()
    required = [
        graph / "bundle_metadata.json",
        graph / "mechanism_edges.tsv",
        graph / "mechanism_nodes.tsv",
        method / "canonical_communication_records.tsv",
        method / "method_resource_records.tsv",
        method / "method_resource_complex_components.tsv",
        method / "method_resource_migration_report.json",
    ]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        raise SystemExit("Missing candidate-universe inputs: " + ", ".join(missing))
    if output.exists():
        raise SystemExit(f"Refusing to overwrite existing candidate-universe output: {output}")

    metadata = json.loads((graph / "bundle_metadata.json").read_text(encoding="utf-8"))
    migration = json.loads((method / "method_resource_migration_report.json").read_text(encoding="utf-8"))
    canonical_rows = read_tsv(method / "canonical_communication_records.tsv")
    resource_rows = read_tsv(method / "method_resource_records.tsv")
    component_rows = read_tsv(method / "method_resource_complex_components.tsv")
    node_rows = read_tsv(graph / "mechanism_nodes.tsv")
    edge_rows = read_tsv(graph / "mechanism_edges.tsv")

    records_by_id: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in resource_rows:
        candidate_id = row.get("canonical_communication_id", "")
        if candidate_id:
            records_by_id[candidate_id].append(row)
    components_by_id = component_index(component_rows)
    exact_edges = graph_indexes(edge_rows, node_rows)
    node_index = index_nodes(node_rows)
    routes = route_index(graph / "mechanism_signaling_route_evidence.tsv.gz")

    output.mkdir(parents=True)
    rows: list[dict[str, str]] = []
    status_counts: dict[str, int] = defaultdict(int)
    for canonical in canonical_rows:
        candidate_id = canonical.get("canonical_communication_id", "")
        if not candidate_id:
            raise ValueError("Canonical communication row has no candidate_pair_id")
        ligand = canonical.get("normalized_ligand_name", "").strip()
        receptor = canonical.get("normalized_receptor_name", "").strip()
        ligand_nodes = sorted(node_index.get(ligand, set()))
        receptor_nodes = sorted(node_index.get(receptor, set()))
        matching_edges = exact_edges.get((ligand, receptor), [])
        edge_ids = sorted({edge.get("edge_id", "") for edge in matching_edges if edge.get("edge_id")})
        exportable_values = {edge.get("exportable", "").strip().lower() for edge in matching_edges}
        if matching_edges and "true" in exportable_values:
            graph_status = "validated_exportable_core_edge"
            graph_exportable = "true"
            unresolved_reason = ""
        elif matching_edges:
            graph_status = "graph_edge_nonexportable"
            graph_exportable = "false"
            unresolved_reason = "matching_graph_edge_is_not_exportable"
        elif len(ligand_nodes) == 1 and len(receptor_nodes) == 1:
            graph_status = "mapped_not_graph_edge"
            graph_exportable = ""
            unresolved_reason = ""
        else:
            graph_status = "staged_unresolved"
            graph_exportable = ""
            reasons = []
            if not ligand_nodes:
                reasons.append("ligand_label_unresolved")
            elif len(ligand_nodes) > 1:
                reasons.append("ligand_label_ambiguous")
            if not receptor_nodes:
                reasons.append("receptor_label_unresolved")
            elif len(receptor_nodes) > 1:
                reasons.append("receptor_label_ambiguous")
            if not reasons:
                reasons.append("no_exact_graph_edge_match")
            unresolved_reason = ";".join(reasons)

        route_values = routes.get((ligand, receptor), {})
        resource_records = records_by_id.get(candidate_id, [])
        component_values = components_by_id.get(candidate_id, {})
        ligand_components = [value for _ordinal, value in sorted(component_values.get("ligand", []))]
        receptor_components = [value for _ordinal, value in sorted(component_values.get("receptor", []))]
        row = {
            "candidate_pair_id": candidate_id,
            "species_scope": canonical.get("species_scope", ""),
            "ligand_name": canonical.get("ligand_name", ""),
            "receptor_name": canonical.get("receptor_name", ""),
            "normalized_ligand_name": ligand,
            "normalized_receptor_name": receptor,
            "communication_kind": canonical.get("communication_kind", ""),
            "source_method_count": canonical.get("source_method_count", ""),
            "source_record_count": canonical.get("source_record_count", ""),
            "source_methods_json": canonical.get("source_methods_json", "[]"),
            "source_resource_keys_json": stable_json(row.get("resource_key", "") for row in resource_records),
            "source_record_keys_json": stable_json(row.get("source_record_key", "") for row in resource_records),
            "ligand_components": "|".join(ligand_components),
            "receptor_components": "|".join(receptor_components),
            "ligand_node_id": ligand_nodes[0] if len(ligand_nodes) == 1 else "",
            "receptor_node_id": receptor_nodes[0] if len(receptor_nodes) == 1 else "",
            "mechanism_graph_status": graph_status,
            "graph_edge_ids_json": stable_json(edge_ids),
            "graph_exportable": graph_exportable,
            "route_status": "|".join(sorted(route_values.get("route_status", set()))) or "not_present_in_route_evidence",
            "route_tier": "|".join(sorted(route_values.get("route_tier", set()))) or "",
            "route_linkage_status": "|".join(sorted(route_values.get("route_linkage_status", set()))) or "",
            "causal_status": "|".join(sorted(route_values.get("causal_status", set()))) or "",
            "traversal_status": "|".join(sorted(route_values.get("traversal_status", set()))) or "",
            "evidence_status": canonical.get("evidence_status", "method_resource_only"),
            "unresolved_mapping_reason": unresolved_reason,
            "source_snapshot_id": migration.get("source_snapshot_id", ""),
            "mechanism_graph_release": metadata.get("release_id", ""),
            "candidate_role": "candidate_universe_record",
        }
        rows.append(row)
        status_counts[graph_status] += 1

    if len({row["candidate_pair_id"] for row in rows}) != len(rows):
        raise ValueError("Candidate universe contains duplicate candidate_pair_id values")
    if len(rows) != int(migration.get("canonical_communication_count", len(rows))):
        raise ValueError("Candidate universe count does not match migration report")
    for row in rows:
        declared = int(row["source_record_count"] or 0)
        observed = len(parse_json_list(row["source_record_keys_json"]))
        if declared != observed:
            raise ValueError(f"Source record count mismatch for {row['candidate_pair_id']}: {declared} != {observed}")

    table_path = output / "mechanism_lr_candidate_universe.tsv"
    with table_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    report = {
        "schema_version": "mechanism_lr_candidate_universe_v1",
        "candidate_role": "method_resource_candidate_projection",
        "mechanism_graph_release": metadata.get("release_id", ""),
        "source_snapshot_id": migration.get("source_snapshot_id", ""),
        "canonical_communication_count": len(rows),
        "graph_status_counts": dict(sorted(status_counts.items())),
        "evidence_status_counts": {"method_resource_only": len(rows)},
        "graph_edges_created": False,
        "causal_assertions_created": False,
        "numeric_weights_created": False,
        "inputs": {
            display_path(path): {"sha256": sha256(path), "bytes": path.stat().st_size}
            for path in required
        },
        "output": {
            "path": display_path(table_path),
            "sha256": sha256(table_path),
            "bytes": table_path.stat().st_size,
            "row_count": len(rows),
        },
    }
    (output / "mechanism_lr_candidate_universe_report.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
