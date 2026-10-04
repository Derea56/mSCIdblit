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
CANDIDATE_UNIVERSE_SCHEMA = "mechanism_lr_candidate_universe_v3"
COMPONENT_CROSSWALK_SCHEMA = "mechanism_lr_component_crosswalk_v1"

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
    "source_native_variants_json",
    "cellchat_json_pair_variants_json",
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
    "component_mapping_status",
    "component_mapping_id",
]

CROSSWALK_FIELDS = [
    "component_mapping_id",
    "candidate_pair_id",
    "species_scope",
    "ligand_name",
    "receptor_name",
    "ligand_entity_type",
    "receptor_entity_type",
    "ligand_components",
    "receptor_components",
    "component_mapping_status",
    "component_mapping_basis",
    "source_registry_id",
    "source_methods",
    "source_resources",
    "source_record_ids",
    "source_databases",
    "source_evidence_notes",
    "source_registry_path",
    "source_registry_sha256",
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


def read_cellchat_json(path: Path | None) -> dict[str, dict[str, object]]:
    """Index standalone CellChat interactions by their stable source ID.

    The TSV projection and standalone JSON preserve the same CellChat source
    IDs but do not always use the same complex/non-protein spelling.  The JSON
    interaction is the canonical native CellChat representation for candidate
    coverage; the TSV representation remains in the source-native provenance.
    """

    if path is None or not path.is_file():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    interactions = payload.get("interactions", [])
    complexes = payload.get("complexes", {})
    if not isinstance(interactions, list) or not isinstance(complexes, dict):
        raise ValueError(f"Invalid standalone CellChat resource: {path}")
    indexed: dict[str, dict[str, object]] = {}
    for raw in interactions:
        if not isinstance(raw, dict):
            raise ValueError(f"Invalid CellChat interaction row in {path}")
        source_id = str(raw.get("interaction_name") or "").strip()
        ligand = str(raw.get("ligand") or "").strip()
        receptor = str(raw.get("receptor") or "").strip()
        if not source_id or not ligand or not receptor:
            raise ValueError(f"CellChat interaction lacks source ID or LR fields in {path}")
        if source_id in indexed:
            raise ValueError(f"Duplicate CellChat interaction_name: {source_id}")
        indexed[source_id] = {
            "ligand": ligand,
            "receptor": receptor,
            "ligand_components": [str(value) for value in complexes.get(ligand, []) if str(value).strip()],
            "receptor_components": [str(value) for value in complexes.get(receptor, []) if str(value).strip()],
        }
    return indexed


def stable_json(values: Iterable[str]) -> str:
    return json.dumps(sorted({value for value in values if value}), separators=(",", ":"))


def canonical_pair_key(ligand: str, receptor: str) -> tuple[str, str]:
    """Return the cross-export comparison key without changing source text."""

    normalize = lambda value: "".join(character for character in value.casefold() if character.isalnum())
    return normalize(ligand), normalize(receptor)


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


def component_tokens(value: str) -> list[str]:
    """Parse only an explicit pipe-delimited source component field."""
    return [part.strip() for part in value.split("|") if part.strip()]


def validate_registry_component_row(row: dict[str, str]) -> tuple[str, str, str]:
    """Validate one explicit master-registry component mapping.

    This deliberately does not split canonical names.  Components must be
    present in the source registry fields and must agree with the registry's
    entity type.
    """
    statuses = []
    resolved: list[str] = []
    for side in ("ligand", "receptor"):
        entity_type = row.get(f"{side}_entity_type", "").strip()
        name = row.get(side, "").strip()
        values = component_tokens(row.get(f"{side}_components", ""))
        if entity_type not in {"gene", "complex"} or not name or not values:
            statuses.append("unresolved_missing_or_invalid_source_components")
            continue
        if len(values) != len(set(values)):
            statuses.append("unresolved_duplicate_source_components")
            continue
        if entity_type == "gene" and values != [name]:
            statuses.append("unresolved_entity_type_component_mismatch")
            continue
        if entity_type == "complex" and len(values) < 2:
            statuses.append("unresolved_entity_type_component_mismatch")
            continue
        resolved.extend(values)
    if statuses:
        return ";".join(sorted(set(statuses))), "", ""
    ligand = "|".join(component_tokens(row["ligand_components"]))
    receptor = "|".join(component_tokens(row["receptor_components"]))
    status = "explicit_source_complex" if "complex" in {row["ligand_entity_type"], row["receptor_entity_type"]} else "single_gene_identity"
    return status, ligand, receptor


def load_master_component_registry(path: Path) -> tuple[dict[tuple[str, str], dict[str, str]], dict[str, int]]:
    """Load exact pair/component mappings from the frozen master registry."""
    if not path.is_file():
        return {}, {"status": "not_provided"}
    rows = read_tsv(path)
    by_pair: dict[tuple[str, str], dict[str, str]] = {}
    status_counts: dict[str, int] = defaultdict(int)
    for row in rows:
        pair = (row.get("ligand", "").strip(), row.get("receptor", "").strip())
        if not pair[0] or not pair[1]:
            raise ValueError("Master registry contains an empty ligand or receptor")
        if pair in by_pair:
            raise ValueError(f"Master registry contains an ambiguous duplicate pair: {pair}")
        status, ligand, receptor = validate_registry_component_row(row)
        enriched = dict(row)
        enriched["component_mapping_status"] = status
        enriched["validated_ligand_components"] = ligand
        enriched["validated_receptor_components"] = receptor
        by_pair[pair] = enriched
        status_counts[status] += 1
    return by_pair, dict(sorted(status_counts.items()))


def graph_label_key(value: str) -> str:
    """Return the graph-label comparison key without rewriting source text."""

    return str(value or "").strip().casefold()


def index_nodes(
    rows: list[dict[str, str]],
    *,
    case_insensitive: bool = True,
) -> dict[str, set[str]]:
    index: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        node_id = row.get("node_id", "")
        if not node_id:
            continue
        for field in ("canonical_name", "canonical_label", "gene_symbol"):
            value = row.get(field, "").strip()
            if value:
                key = graph_label_key(value) if case_insensitive else value
                index[key].add(node_id)
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
    for values_by_side in result.values():
        for side, values in values_by_side.items():
            first_ordinal_by_component: dict[str, int] = {}
            for ordinal, component in values:
                first_ordinal_by_component[component] = min(first_ordinal_by_component.get(component, ordinal), ordinal)
            values_by_side[side] = sorted((ordinal, component) for component, ordinal in first_ordinal_by_component.items())
    return result


def graph_indexes(
    edges: list[dict[str, str]],
    nodes: list[dict[str, str]],
    *,
    case_insensitive: bool = True,
) -> dict[tuple[str, str], list[dict[str, str]]]:
    node_labels = {row.get("node_id", ""): row.get("canonical_name", "") for row in nodes}
    pairs: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for edge in edges:
        if edge.get("relation_type") != "binds_receptor":
            continue
        ligand = edge.get("source_label", "") or node_labels.get(edge.get("source_node_id", ""), "")
        receptor = edge.get("target_label", "") or node_labels.get(edge.get("target_node_id", ""), "")
        if ligand and receptor:
            key = (
                graph_label_key(ligand) if case_insensitive else ligand.strip(),
                graph_label_key(receptor) if case_insensitive else receptor.strip(),
            )
            pairs[key].append(edge)
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
    parser.add_argument(
        "--cellchat-json",
        type=Path,
        default=None,
        help="Standalone CellChat JSON used to reconcile source-record pair spellings.",
    )
    parser.add_argument(
        "--master-lr-registry",
        type=Path,
        default=None,
        help="Exact compatibility registry with explicit ligand/receptor component fields.",
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    graph = args.graph_bundle_dir.resolve()
    method = args.method_migration_dir.resolve()
    cellchat_json_path = (
        args.cellchat_json.resolve()
        if args.cellchat_json is not None
        else method / "method_native" / "CellChatDB.mouse.standalone.json"
    )
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
    master_registry_path = (
        args.master_lr_registry.resolve()
        if args.master_lr_registry is not None
        else method / "method_native" / "master_lr_registry.tsv"
    )
    master_registry, master_registry_status_counts = load_master_component_registry(master_registry_path)
    node_rows = read_tsv(graph / "mechanism_nodes.tsv")
    edge_rows = read_tsv(graph / "mechanism_edges.tsv")
    cellchat_json = read_cellchat_json(cellchat_json_path)

    records_by_id: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in resource_rows:
        candidate_id = row.get("canonical_communication_id", "")
        if candidate_id:
            records_by_id[candidate_id].append(row)
    components_by_id = component_index(component_rows)
    exact_edges = graph_indexes(edge_rows, node_rows, case_insensitive=False)
    graph_edges = graph_indexes(edge_rows, node_rows, case_insensitive=True)
    exact_node_index = index_nodes(node_rows, case_insensitive=False)
    node_index = index_nodes(node_rows, case_insensitive=True)
    routes = route_index(graph / "mechanism_signaling_route_evidence.tsv.gz")

    output.mkdir(parents=True)
    rows: list[dict[str, str]] = []
    status_counts: dict[str, int] = defaultdict(int)
    cellchat_json_pairs_by_id: dict[str, set[tuple[str, str]]] = defaultdict(set)
    cellchat_tsv_pairs_by_id: dict[str, set[tuple[str, str]]] = defaultdict(set)
    crosswalk_rows: list[dict[str, str]] = []
    component_status_counts: dict[str, int] = defaultdict(int)
    graph_resolution_audit = {
        "normalization": "strip+casefold",
        "case_insensitive_edge_recovery_count": 0,
        "case_insensitive_node_recovery_count": 0,
        "ambiguous_case_insensitive_node_label_count": 0,
    }
    for canonical in canonical_rows:
        candidate_id = canonical.get("canonical_communication_id", "")
        if not candidate_id:
            raise ValueError("Canonical communication row has no candidate_pair_id")
        ligand = canonical.get("normalized_ligand_name", "").strip()
        receptor = canonical.get("normalized_receptor_name", "").strip()
        ligand_nodes = sorted(node_index.get(graph_label_key(ligand), set()))
        receptor_nodes = sorted(node_index.get(graph_label_key(receptor), set()))
        exact_ligand_nodes = sorted(exact_node_index.get(ligand, set()))
        exact_receptor_nodes = sorted(exact_node_index.get(receptor, set()))
        matching_edges = exact_edges.get((ligand, receptor), [])
        if not matching_edges:
            matching_edges = graph_edges.get(
                (graph_label_key(ligand), graph_label_key(receptor)), []
            )
            if matching_edges:
                graph_resolution_audit["case_insensitive_edge_recovery_count"] += 1
        if not exact_ligand_nodes and len(ligand_nodes) == 1:
            graph_resolution_audit["case_insensitive_node_recovery_count"] += 1
        if not exact_receptor_nodes and len(receptor_nodes) == 1:
            graph_resolution_audit["case_insensitive_node_recovery_count"] += 1
        if len(ligand_nodes) > 1:
            graph_resolution_audit["ambiguous_case_insensitive_node_label_count"] += 1
        if len(receptor_nodes) > 1:
            graph_resolution_audit["ambiguous_case_insensitive_node_label_count"] += 1
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
        registry_row = master_registry.get((ligand, receptor))
        component_mapping_id = f"COMPONENTMAP:{candidate_id}"
        component_mapping_status = "unresolved_no_exact_source_registry_pair"
        component_mapping_basis = "no_exact_master_lr_registry_pair"
        registry_ligand_components = ""
        registry_receptor_components = ""
        if registry_row is not None:
            registry_status = registry_row["component_mapping_status"]
            registry_ligand_components = registry_row["validated_ligand_components"]
            registry_receptor_components = registry_row["validated_receptor_components"]
            explicit_sets_agree = (
                set(ligand_components) == set(component_tokens(registry_ligand_components))
                and set(receptor_components) == set(component_tokens(registry_receptor_components))
            )
            if registry_status.startswith("unresolved_"):
                component_mapping_status = registry_status
                component_mapping_basis = "master_lr_registry_explicit_fields_failed_validation"
            elif ligand_components or receptor_components:
                if explicit_sets_agree:
                    component_mapping_status = "source_registry_and_explicit_resource_agree"
                    component_mapping_basis = "exact_master_lr_registry_and_method_resource_component_fields"
                else:
                    component_mapping_status = "unresolved_source_component_disagreement"
                    component_mapping_basis = "master_lr_registry_disagrees_with_method_resource_component_fields"
                    registry_ligand_components = ""
                    registry_receptor_components = ""
            else:
                component_mapping_status = registry_status
                component_mapping_basis = "exact_master_lr_registry_explicit_component_fields"
            if not component_mapping_status.startswith("unresolved_"):
                ligand_components = component_tokens(registry_ligand_components)
                receptor_components = component_tokens(registry_receptor_components)
        component_status_counts[component_mapping_status] += 1
        crosswalk_rows.append({
            "component_mapping_id": component_mapping_id,
            "candidate_pair_id": candidate_id,
            "species_scope": canonical.get("species_scope", ""),
            "ligand_name": ligand,
            "receptor_name": receptor,
            "ligand_entity_type": registry_row.get("ligand_entity_type", "") if registry_row else "",
            "receptor_entity_type": registry_row.get("receptor_entity_type", "") if registry_row else "",
            "ligand_components": registry_ligand_components,
            "receptor_components": registry_receptor_components,
            "component_mapping_status": component_mapping_status,
            "component_mapping_basis": component_mapping_basis,
            "source_registry_id": registry_row.get("registry_id", "") if registry_row else "",
            "source_methods": registry_row.get("source_methods", "") if registry_row else "",
            "source_resources": registry_row.get("source_resources", "") if registry_row else "",
            "source_record_ids": registry_row.get("source_record_ids", "") if registry_row else "",
            "source_databases": registry_row.get("source_databases", "") if registry_row else "",
            "source_evidence_notes": registry_row.get("evidence_notes", "") if registry_row else "",
            "source_registry_path": display_path(master_registry_path),
            "source_registry_sha256": sha256(master_registry_path) if master_registry_path.is_file() else "",
        })
        source_native_variants: list[dict[str, object]] = []
        cellchat_json_variants: dict[tuple[str, str], dict[str, object]] = {}
        for resource_record in resource_records:
            source_id = resource_record.get("source_record_key", "").strip()
            resource_key = resource_record.get("resource_key", "").strip()
            native_variant = {
                "resource_key": resource_key,
                "source_record_key": source_id,
                "representation": "method_resource_tsv",
                "ligand": resource_record.get("native_ligand", ""),
                "receptor": resource_record.get("native_receptor", ""),
            }
            source_native_variants.append(native_variant)
            if resource_key != "mscs_phase2:cellchat_mouse.tsv":
                continue
            tsv_pair = (
                str(resource_record.get("native_ligand", "") or "").strip(),
                str(resource_record.get("native_receptor", "") or "").strip(),
            )
            cellchat_tsv_pairs_by_id[candidate_id].add(canonical_pair_key(*tsv_pair))
            json_variant = cellchat_json.get(source_id)
            if json_variant is None:
                continue
            json_ligand = str(json_variant["ligand"])
            json_receptor = str(json_variant["receptor"])
            json_key = canonical_pair_key(json_ligand, json_receptor)
            cellchat_json_pairs_by_id[candidate_id].add(json_key)
            cellchat_json_variants[json_key] = {
                "source_record_key": source_id,
                "representation": "CellChatDB.mouse.standalone.json",
                "ligand": json_ligand,
                "receptor": json_receptor,
                "ligand_components": "|".join(str(value) for value in json_variant["ligand_components"]),
                "receptor_components": "|".join(str(value) for value in json_variant["receptor_components"]),
            }
            source_native_variants.append(cellchat_json_variants[json_key])
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
            "source_native_variants_json": json.dumps(source_native_variants, ensure_ascii=False, sort_keys=True, separators=(",", ":")),
            "cellchat_json_pair_variants_json": json.dumps(
                sorted(cellchat_json_variants.values(), key=lambda value: (str(value["ligand"]), str(value["receptor"]), str(value["source_record_key"]))),
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ),
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
            "component_mapping_status": component_mapping_status,
            "component_mapping_id": component_mapping_id,
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

    cellchat_source_records = {
        row.get("source_record_key", "").strip()
        for row in resource_rows
        if row.get("resource_key") == "mscs_phase2:cellchat_mouse.tsv" and row.get("source_record_key", "").strip()
    }
    cellchat_projection = {
        key
        for values in cellchat_json_pairs_by_id.values()
        for key in values
    }
    cellchat_tsv_projection = {
        key
        for values in cellchat_tsv_pairs_by_id.values()
        for key in values
    }
    if cellchat_json:
        json_source_records = set(cellchat_json)
        if json_source_records != cellchat_source_records:
            raise ValueError(
                "CellChat standalone JSON/source TSV source-record mismatch: "
                f"json_only={len(json_source_records - cellchat_source_records)}, "
                f"tsv_only={len(cellchat_source_records - json_source_records)}"
            )
        expected_json_pairs = {
            canonical_pair_key(str(value["ligand"]), str(value["receptor"]))
            for value in cellchat_json.values()
        }
        if cellchat_projection != expected_json_pairs:
            raise ValueError(
                "CellChat JSON pair keys were not retained in candidate projection: "
                f"missing={len(expected_json_pairs - cellchat_projection)}, "
                f"extra={len(cellchat_projection - expected_json_pairs)}"
            )
    else:
        expected_json_pairs = set()

    table_path = output / "mechanism_lr_candidate_universe.tsv"
    with table_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    crosswalk_path = output / "mechanism_lr_candidate_component_crosswalk.tsv"
    with crosswalk_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CROSSWALK_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(crosswalk_rows)
    report = {
        "schema_version": CANDIDATE_UNIVERSE_SCHEMA,
        "candidate_role": "method_resource_candidate_projection",
        "mechanism_graph_release": metadata.get("release_id", ""),
        "source_snapshot_id": migration.get("source_snapshot_id", ""),
        "canonical_communication_count": len(rows),
        "cellchat_json_reconciliation": {
            "status": "complete" if cellchat_json else "not_provided",
            "source_record_count": len(cellchat_json),
            "source_record_coverage": 1.0 if cellchat_json and cellchat_source_records == set(cellchat_json) else None,
            "json_unique_pair_count": len(expected_json_pairs),
            "json_pair_key_coverage": (
                round(len(cellchat_projection & expected_json_pairs) / len(expected_json_pairs), 6)
                if expected_json_pairs else None
            ),
            "tsv_unique_pair_key_count": len(cellchat_tsv_projection),
            "shared_canonical_pair_key_count": len(cellchat_tsv_projection & expected_json_pairs),
            "json_only_canonical_pair_key_count": len(expected_json_pairs - cellchat_tsv_projection),
            "tsv_only_canonical_pair_key_count": len(cellchat_tsv_projection - expected_json_pairs),
            "pair_key_semantics": "casefolded alphanumeric comparison only; source spellings and components remain preserved",
        },
        "graph_status_counts": dict(sorted(status_counts.items())),
        "graph_label_resolution": graph_resolution_audit,
        "component_crosswalk": {
            "schema_version": COMPONENT_CROSSWALK_SCHEMA,
            "mapping_count": len(crosswalk_rows),
            "status_counts": dict(sorted(component_status_counts.items())),
            "master_registry_status_counts": master_registry_status_counts,
            "source_registry_path": display_path(master_registry_path),
            "source_registry_sha256": sha256(master_registry_path) if master_registry_path.is_file() else None,
            "path": display_path(crosswalk_path),
            "sha256": sha256(crosswalk_path),
            "bytes": crosswalk_path.stat().st_size,
            "biological_component_inference": False,
            "mapping_rule": "exact normalized ligand/receptor pair lookup in the explicit master registry; no underscore splitting",
        },
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
    report["inputs"][display_path(master_registry_path)] = {
        "sha256": sha256(master_registry_path),
        "bytes": master_registry_path.stat().st_size,
    } if master_registry_path.is_file() else {"available": False}
    if cellchat_json_path.is_file():
        report["inputs"][display_path(cellchat_json_path)] = {
            "sha256": sha256(cellchat_json_path),
            "bytes": cellchat_json_path.stat().st_size,
        }
    handoff = {
        "schema_version": "candidate_component_handoff_v1",
        "candidate_universe_schema": CANDIDATE_UNIVERSE_SCHEMA,
        "candidate_universe_path": display_path(table_path),
        "component_crosswalk_path": display_path(crosswalk_path),
        "candidate_pair_count": len(rows),
        "component_mapping_status_counts": dict(sorted(component_status_counts.items())),
        "component_mapping_rule": "exact source-registry pair lookup; explicit pipe-delimited component fields only; no underscore splitting",
        "biological_component_inference": False,
        "external_downstream_audit": {
            "available_in_repository": False,
            "required_for_pair_level_recovery_accounting": True,
            "coordinator_reported_missing_pair_count": 88,
            "coordinator_reported_potentially_recoverable_lower_bound": 48,
            "coordinator_reported_remaining_count": 40,
            "verification_status": "not_verified_without_the_88_pair_audit_input",
            "required_input_fields": ["ligand", "receptor", "missing_reason", "measured_feature_requirement"],
        },
    }
    handoff_path = output / "candidate_component_handoff.json"
    handoff_path.write_text(json.dumps(handoff, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report["component_crosswalk"]["handoff_path"] = display_path(handoff_path)
    report["component_crosswalk"]["handoff_sha256"] = sha256(handoff_path)
    report["component_crosswalk"]["handoff_bytes"] = handoff_path.stat().st_size
    (output / "mechanism_lr_candidate_universe_report.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
