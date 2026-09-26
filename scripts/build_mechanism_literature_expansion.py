#!/usr/bin/env python3
"""Materialize a small primary-literature route overlay for mSCS.

The overlay is evidence-layer data. It may connect independently curated
ligand/receptor, intracellular, TF, and output observations for plausibility
analysis, including graph-linked route records with stable primary locators,
but it never creates or rewrites a causal graph edge.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import shutil
from collections import Counter
from pathlib import Path

try:
    from .audit_full_signaling_chains import ROUTE_EVIDENCE_FIELDS
    from .mechanism_evidence_contract import MECHANISM_EVIDENCE_CONTRACT_VERSION
    from .route_artifacts import write_normalized_route_artifacts
except ImportError:  # pragma: no cover - direct script execution
    from audit_full_signaling_chains import ROUTE_EVIDENCE_FIELDS
    from mechanism_evidence_contract import MECHANISM_EVIDENCE_CONTRACT_VERSION
    from route_artifacts import write_normalized_route_artifacts

try:
    from .build_all_ligand_route_coverage import build as build_ligand_route_coverage
    from .build_all_ligand_route_coverage import write_tsv_gz as write_ligand_route_coverage
except ImportError:  # pragma: no cover - helper was removed from the current branch
    try:
        from build_all_ligand_route_coverage import build as build_ligand_route_coverage
        from build_all_ligand_route_coverage import write_tsv_gz as write_ligand_route_coverage
    except ImportError:
        build_ligand_route_coverage = None
        write_ligand_route_coverage = None


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch001.json"
DEFAULT_SOURCE_BUNDLE = ROOT / "data/processed/mechanism_graph_module20_24_v2026_09_16_evidence_contract"
DEFAULT_OUTPUT_BUNDLE = ROOT / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion001"


def read_tsv(path: Path) -> list[dict[str, str]]:
    opener = gzip.open if path.suffix == ".gz" else open
    open_kwargs = {
        "newline": "",
        "encoding": "utf-8",
        "errors": "replace",
    }
    with opener(path, "rt", **open_kwargs) if path.suffix == ".gz" else opener(path, **open_kwargs) as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def read_input(path: Path) -> list[dict[str, str]]:
    if path.suffix.casefold() == ".json":
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, list) or not all(isinstance(row, dict) for row in payload):
            raise ValueError("Literature expansion JSON must contain a list of objects")
        return [{str(key): "" if value is None else str(value) for key, value in row.items()} for row in payload]
    return read_tsv(path)


def write_tsv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: str(row.get(field, "")) for field in fieldnames} for row in rows)


def write_tsv_gz(
    path: Path,
    fieldnames: list[str],
    rows: list[dict[str, object]],
    *,
    append: bool = False,
) -> None:
    mode = "at" if append and path.exists() else "wt"
    with gzip.open(path, mode, newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        if mode == "wt":
            writer.writeheader()
        writer.writerows({field: str(row.get(field, "")) for field in fieldnames} for row in rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--source-bundle", type=Path, default=DEFAULT_SOURCE_BUNDLE)
    parser.add_argument("--output-bundle", type=Path, default=DEFAULT_OUTPUT_BUNDLE)
    parser.add_argument(
        "--release-id",
        default="",
        help="Release identifier; required when writing a non-default output bundle.",
    )
    parser.add_argument(
        "--reuse-output-bundle",
        action="store_true",
        help="Reuse an already-created copy-on-write clone of the source bundle instead of copying it again.",
    )
    parser.add_argument(
        "--incremental-output-bundle",
        action="store_true",
        help="Append to an existing copy-on-write output bundle and rewrite only derived route artifacts.",
    )
    return parser.parse_args()


def validate_rows(rows: list[dict[str, str]], source_bundle: Path) -> None:
    required = {
        "expansion_id", "source_queue_id", "path_expression", "route_tier", "known_layers", "missing_layers",
        "intracellular_status", "ligand_node_id", "ligand_label", "ligand_receptor_edge_id", "receptor_node_id",
        "receptor_label", "transcription_factor_node_id", "transcription_factor_label", "target_gene_node_id",
        "target_gene_label", "source_evidence_record_id", "causal_status", "traversal_status",
        "evidence_contract_version", "evidence_polarity", "negative_evidence_status", "evidence_directness",
        "output_class", "primary_locator", "citation_note", "evidence_summary", "limitations", "curation_status"
    }
    if not rows:
        raise ValueError("Literature expansion input is empty")
    missing = sorted(required - set(rows[0]))
    if missing:
        raise ValueError(f"Literature expansion input is missing columns: {missing}")

    nodes = {row["node_id"] for row in read_tsv(source_bundle / "mechanism_nodes.tsv")}
    edges = {
        row["edge_id"]: (row["source_node_id"], row["target_node_id"])
        for row in read_tsv(source_bundle / "mechanism_edges.tsv")
    }
    queue_ids = {row["queue_id"] for row in read_tsv(source_bundle / "mechanism_downstream_curation_queue.tsv")}
    downstream_ids = {row["record_id"] for row in read_tsv(source_bundle / "mechanism_downstream_evidence_records.tsv")}
    source_route_path = source_bundle / "mechanism_signaling_route_evidence.tsv"
    if not source_route_path.exists():
        source_route_path = source_route_path.with_suffix(source_route_path.suffix + ".gz")
    existing_routes = {row["route_evidence_id"] for row in read_tsv(source_route_path)}
    existing_literature_route_numbers = {
        int(route_id.split(":", 1)[1])
        for route_id in existing_routes
        if route_id.startswith("LITEXP:") and route_id.split(":", 1)[1].isdigit()
    }
    next_route_number = max(existing_literature_route_numbers, default=0) + 1

    expansion_ids: set[str] = set()
    for row in rows:
        expansion_id = row["expansion_id"]
        if not expansion_id or expansion_id in expansion_ids:
            raise ValueError(f"Duplicate or empty expansion_id: {expansion_id!r}")
        expansion_ids.add(expansion_id)
        graph_linked_route = "graph_linked_route_source" in row.get("route_linkage_status", "")
        if row["source_queue_id"] and row["source_queue_id"] not in queue_ids:
            raise ValueError(f"{expansion_id} references missing source queue {row['source_queue_id']}")
        if row["source_evidence_record_id"] and row["source_evidence_record_id"] not in downstream_ids:
            raise ValueError(f"{expansion_id} references missing downstream evidence record {row['source_evidence_record_id']}")
        if not graph_linked_route and (not row["source_queue_id"] or not row["source_evidence_record_id"]):
            raise ValueError(f"{expansion_id} requires downstream source linkage unless marked graph_linked_route_source")
        if row["evidence_contract_version"] != MECHANISM_EVIDENCE_CONTRACT_VERSION:
            raise ValueError(f"{expansion_id} uses unsupported evidence contract {row['evidence_contract_version']!r}")
        if row.get("route_status", "retained_evidence_route") != "retained_evidence_route":
            raise ValueError(f"{expansion_id} must use retained_evidence_route")
        if row["causal_status"] != "not_asserted" or row["traversal_status"] != "evidence_route_not_causal":
            raise ValueError(f"{expansion_id} must remain non-causal and non-traversable as a graph edge")
        for field in ("ligand_node_id", "receptor_node_id", "intracellular_continuation_node_id", "transcription_factor_node_id", "target_gene_node_id", "output_node_id"):
            if row.get(field, "") and row[field] not in nodes:
                raise ValueError(f"{expansion_id} references missing {field} {row[field]}")
        for field in ("ligand_receptor_edge_id", "receptor_intracellular_edge_id", "intracellular_tf_edge_id", "tf_target_edge_id"):
            if row.get(field, "") and row[field] not in edges:
                raise ValueError(f"{expansion_id} references missing {field} {row[field]}")
        lr_edge = edges.get(row.get("ligand_receptor_edge_id", ""))
        if lr_edge and lr_edge != (row["ligand_node_id"], row["receptor_node_id"]):
            raise ValueError(f"{expansion_id} ligand-receptor endpoints do not match its edge")
        tf_edge = edges.get(row.get("tf_target_edge_id", ""))
        if tf_edge and tf_edge != (row["transcription_factor_node_id"], row["target_gene_node_id"]):
            raise ValueError(f"{expansion_id} TF-target endpoints do not match its edge")
        if not row["primary_locator"] or not row["evidence_summary"] or not row["limitations"]:
            raise ValueError(f"{expansion_id} must include primary locator, evidence summary, and limitations")
        route_id = f"LITEXP:{next_route_number + len(expansion_ids) - 1:06d}"
        if route_id in existing_routes:
            raise ValueError(f"Generated route ID already exists: {route_id}")


def main() -> int:
    args = parse_args()
    source_bundle = args.source_bundle.resolve()
    output_bundle = args.output_bundle.resolve()
    if output_bundle != DEFAULT_OUTPUT_BUNDLE.resolve() and not args.release_id:
        raise ValueError("--release-id is required for a non-default output bundle")
    release_id = args.release_id or "module20_24_mechanism_graph:2026-09-16-literature-expansion-001"
    rows = read_input(args.input.resolve())
    validate_rows(rows, source_bundle)
    if output_bundle.exists() and not args.reuse_output_bundle:
        raise FileExistsError(f"Output bundle already exists: {output_bundle}")
    if args.incremental_output_bundle and not args.reuse_output_bundle:
        raise ValueError("--incremental-output-bundle requires --reuse-output-bundle")
    if not output_bundle.exists():
        shutil.copytree(source_bundle, output_bundle)

    route_path = output_bundle / "mechanism_signaling_route_evidence.tsv"
    if not route_path.exists():
        route_path = route_path.with_suffix(route_path.suffix + ".gz")
    existing_routes = read_tsv(route_path)
    existing_literature_route_numbers = {
        int(row["route_evidence_id"].split(":", 1)[1])
        for row in existing_routes
        if row["route_evidence_id"].startswith("LITEXP:")
        and row["route_evidence_id"].split(":", 1)[1].isdigit()
    }
    next_route_number = max(existing_literature_route_numbers, default=0) + 1
    expansion_rows: list[dict[str, str]] = []
    route_rows: list[dict[str, str]] = []
    for index, input_row in enumerate(rows, start=1):
        route = {field: input_row.get(field, "") for field in ROUTE_EVIDENCE_FIELDS}
        route["route_evidence_id"] = f"LITEXP:{next_route_number + index - 1:06d}"
        route["route_status"] = input_row.get("route_status", "retained_evidence_route")
        route["source_chain_id"] = input_row.get("source_chain_id", input_row["expansion_id"])
        route_rows.append(route)
        expansion = dict(input_row)
        expansion["route_evidence_id"] = route["route_evidence_id"]
        expansion_rows.append(expansion)

    compressed_route_path = output_bundle / "mechanism_signaling_route_evidence.tsv.gz"
    if args.incremental_output_bundle:
        write_tsv_gz(compressed_route_path, ROUTE_EVIDENCE_FIELDS, route_rows, append=True)
    else:
        write_tsv_gz(compressed_route_path, ROUTE_EVIDENCE_FIELDS, existing_routes + route_rows)
    normalized_counts = write_normalized_route_artifacts(
        output_bundle,
        route_rows if args.incremental_output_bundle else existing_routes + route_rows,
        read_tsv(output_bundle / "mechanism_nodes.tsv"),
        read_tsv(output_bundle / "mechanism_edges.tsv"),
        read_tsv(output_bundle / "mechanism_edge_sources.tsv"),
        append=args.incremental_output_bundle,
    )
    expansion_path = output_bundle / "mechanism_literature_expansion.tsv"
    existing_expansions = read_tsv(expansion_path) if expansion_path.exists() else []
    expansion_fields = list(rows[0].keys()) + ["route_evidence_id"]
    if existing_expansions:
        expansion_fields = list(existing_expansions[0].keys())
        for field in expansion_rows[0]:
            if field not in expansion_fields:
                expansion_fields.append(field)
    cumulative_expansions = existing_expansions + expansion_rows
    if args.incremental_output_bundle:
        missing_existing_fields = sorted(set(expansion_rows[0]) - set(existing_expansions[0]))
        if missing_existing_fields:
            raise ValueError(
                "Incremental expansion append requires existing columns for: "
                f"{missing_existing_fields}"
            )
        with expansion_path.open("a", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=expansion_fields, delimiter="\t", lineterminator="\n")
            writer.writerows({field: str(row.get(field, "")) for field in expansion_fields} for row in expansion_rows)
    else:
        write_tsv(expansion_path, expansion_fields, cumulative_expansions)

    if build_ligand_route_coverage is None or write_ligand_route_coverage is None:
        raise RuntimeError(
            "The all-ligand route-coverage helper is unavailable on this branch; "
            "restore scripts/build_all_ligand_route_coverage.py before building "
            "a literature-expansion release."
        )
    coverage_rows, coverage_summary = build_ligand_route_coverage(output_bundle)
    coverage_path = output_bundle / "mechanism_ligand_route_coverage.tsv.gz"
    write_ligand_route_coverage(coverage_path, coverage_rows)
    (output_bundle / "ligand_route_coverage_summary.json").write_text(
        json.dumps(coverage_summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    audit_path = output_bundle / "full_signaling_chain_audit.json"
    if audit_path.exists():
        audit_summary = json.loads(audit_path.read_text(encoding="utf-8"))
        route_summary = audit_summary.setdefault("signaling_route_evidence_counts", {})
        route_summary["route_evidence_record_count"] = len(existing_routes) + len(route_rows)
        tiers = route_summary.setdefault("route_evidence_tier_counts", {})
        for row in expansion_rows:
            tiers[row["route_tier"]] = tiers.get(row["route_tier"], 0) + 1
        audit_summary["literature_expansion_counts"] = {
            "literature_expansion_rows": len(cumulative_expansions),
            "literature_expansion_rows_added": len(expansion_rows),
            "route_evidence_rows_added": len(route_rows),
        }
        audit_path.write_text(json.dumps(audit_summary, indent=2) + "\n", encoding="utf-8")

    metadata_path = output_bundle / "bundle_metadata.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata["release_id"] = release_id
    metadata.setdefault("files", {})["literature_expansion"] = "mechanism_literature_expansion.tsv"
    metadata.setdefault("files", {})["signaling_route_evidence"] = "mechanism_signaling_route_evidence.tsv.gz"
    metadata.setdefault("files", {})["ligand_route_coverage"] = "mechanism_ligand_route_coverage.tsv.gz"
    metadata.setdefault("counts", {})["literature_expansion"] = len(cumulative_expansions)
    metadata.setdefault("counts", {})["signaling_route_evidence"] = len(existing_routes) + len(route_rows)
    metadata.setdefault("counts", {})["ligand_route_coverage"] = len(coverage_rows)
    metadata.setdefault("graph_policy", {})["literature_expansion_is_evidence_layer_only"] = True
    statement = (
        "Selective primary-literature expansion adds source-linked route annotations for mSCS plausibility analysis; "
        "annotations do not create causal graph edges or database confidence scores."
    )
    if statement not in metadata.setdefault("accuracy_contract", []):
        metadata["accuracy_contract"].append(statement)
    graph_linked_statement = (
        "Graph-linked literature compositions may retain empty downstream queue/evidence pointers when the source route "
        "itself is explicitly marked graph_edge_linked; stable primary locators and component limitations remain required."
    )
    if graph_linked_statement not in metadata.setdefault("accuracy_contract", []):
        metadata["accuracy_contract"].append(graph_linked_statement)
    coverage_statement = (
        "The all-ligand route-coverage index is a derived evidence-layer summary; it does not assign confidence, "
        "authorize causal traversal, or create graph edges."
    )
    if coverage_statement not in metadata.setdefault("accuracy_contract", []):
        metadata["accuracy_contract"].append(coverage_statement)
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    summary = {
        "source_bundle": str(source_bundle),
        "output_bundle": str(output_bundle),
        "release_id": metadata["release_id"],
        "literature_expansion_rows": len(cumulative_expansions),
        "literature_expansion_rows_added": len(expansion_rows),
        "route_evidence_rows_before": len(existing_routes),
        "route_evidence_rows_after": len(existing_routes) + len(route_rows),
        **normalized_counts,
        "route_tier_counts": dict(sorted(Counter(row["route_tier"] for row in expansion_rows).items())),
        "primary_locators": sorted({row["primary_locator"] for row in expansion_rows}),
        "ligand_route_coverage": coverage_summary,
        "graph_edges_changed": False,
        "causal_edges_created": False,
        "confidence_scores_created": False,
    }
    (output_bundle / "mechanism_literature_expansion_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
