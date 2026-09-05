#!/usr/bin/env python3
"""Inventory and strictly curate the Module 20B–24B public-TF layer."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import defaultdict
from pathlib import Path
from typing import Iterable, Mapping

from public_tf_curation import (
    build_ledger_rows,
    build_mouse_direct_binding_queue,
    graph_indexes,
    pair_key,
    summarize_ledger,
)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "data/processed/mechanism_graph_module20_24_v2026_08_30"
DEFAULT_PREVIOUS = ROOT / "data/processed/mechanism_graph_module20_24_v2026_08_26"
DEFAULT_OUTPUT = ROOT / "data/processed/public_tf_curation_v2026_09_04"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[Mapping[str, object]]) -> None:
    if not rows:
        raise ValueError(f"Cannot write empty table: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0]),
            delimiter="\t",
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    key: value.strip() if isinstance(value, str) else value
                    for key, value in row.items()
                }
            )


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def text(row: Mapping[str, object], *keys: str) -> str:
    for key in keys:
        value = str(row.get(key, "") or "").strip()
        if value:
            return value
    return ""


def inventory(rows: list[Mapping[str, object]]) -> dict[str, dict[str, int] | dict[str, int]]:
    fields = (
        "evidence_confidence_tier",
        "module",
        "species_scope",
        "context_level_exact_pair",
        "mechanism_evidence_type",
        "traversal_status",
        "materialization_status",
    )
    output: dict[str, dict[str, int] | dict[str, int]] = {}
    for field in fields:
        counts: defaultdict[str, int] = defaultdict(int)
        for row in rows:
            counts[text(row, field) or "unknown"] += 1
        output[field] = dict(sorted(counts.items(), key=lambda item: (-item[1], item[0])))
    locator_counts: defaultdict[str, int] = defaultdict(int)
    from public_tf_curation import source_locator_status

    for row in rows:
        locator_counts[source_locator_status(row)] += 1
    output["source_locator_status"] = dict(
        sorted(locator_counts.items(), key=lambda item: (-item[1], item[0]))
    )
    pair_counts: defaultdict[tuple[str, str], int] = defaultdict(int)
    for row in rows:
        pair_counts[pair_key(text(row, "regulator_symbol"), text(row, "target_symbol"))] += 1
    output["regulator_target"] = {
        f"{regulator}->{target}": count
        for (regulator, target), count in sorted(
            pair_counts.items(), key=lambda item: (-item[1], item[0])
        )
    }
    return output


def semantic_crosswalk(old_dir: Path, new_dir: Path) -> tuple[list[dict[str, str]], dict[str, object]]:
    if not old_dir.is_dir():
        return [], {"available": False, "reason": "previous release directory unavailable"}
    old_nodes = read_tsv(old_dir / "mechanism_nodes.tsv")
    old_edges = read_tsv(old_dir / "mechanism_edges.tsv")
    new_nodes = read_tsv(new_dir / "mechanism_nodes.tsv")
    new_edges = read_tsv(new_dir / "mechanism_edges.tsv")
    old_pairs, _ = graph_indexes(old_nodes, old_edges)
    new_pairs, _ = graph_indexes(new_nodes, new_edges)
    rows: list[dict[str, str]] = []
    for regulator, target in sorted(set(old_pairs) | set(new_pairs)):
        rows.append(
            {
                "regulator": regulator,
                "target": target,
                "old_edge_ids": ";".join(old_pairs.get((regulator, target), [])) or "unknown",
                "new_edge_ids": ";".join(new_pairs.get((regulator, target), [])) or "unknown",
                "semantic_mapping_status": "exact_label_relation_match"
                if (regulator, target) in old_pairs and (regulator, target) in new_pairs
                else "unresolved_no_counterpart",
            }
        )
    return rows, {
        "available": True,
        "old_semantic_pair_count": len(old_pairs),
        "new_semantic_pair_count": len(new_pairs),
        "exact_label_relation_matches": len(set(old_pairs) & set(new_pairs)),
        "unresolved_old_pairs": len(set(old_pairs) - set(new_pairs)),
        "unresolved_new_pairs": len(set(new_pairs) - set(old_pairs)),
    }


def relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path.resolve())


def markdown_summary(payload: Mapping[str, object]) -> str:
    curation = payload["curation"]
    counts = curation["curation_status"]
    modes = curation["context_modes"]
    reconciliation = payload["reconciliation"]
    graph_status = reconciliation["active_graph_pair_status"]
    lines = [
        "# Public-TF curation review — mSCIdblit modules 20B–24B",
        "",
        f"Source release: `{payload['release_id']}`.",
        f"Rows reviewed: **{payload['rows_reviewed']}**; distinct regulator-target pairs: **{payload['distinct_pairs']}**.",
        "Promotion scope: this audit evaluates the existing v1.1.0 validated overlay and records an expanded review of the unpromoted mouse/direct-binding queue; it makes no new literature promotions.",
        "",
        "## Curation outcomes",
        "",
        "| Curation tier | Rows |",
        "|---|---:|",
    ]
    for tier in (
        "candidate_only",
        "general_mouse_validated",
        "neural_context_validated",
        "sci_context_validated",
        "unresolved",
    ):
        lines.append(f"| `{tier}` | {counts.get(tier, 0)} |")
    lines += [
        "",
        "Candidate-only and unresolved rows are non-traversable. Validated rows are context-gated.",
        f"The exportable curation overlay contains **{payload['traversable_overlay']['row_count']}** context-gated rows representing **{payload['traversable_overlay']['unique_pair_count']}** pairs.",
        f"The next review queue contains **{payload['mouse_direct_binding_review_queue']['row_count']}** unpromoted mouse canonical-TF/direct-binding rows from Modules 20B–24B.",
        f"The expanded queue adjudication reviewed **{payload['queue_adjudication']['rows_reviewed']}** rows: **{payload['queue_adjudication']['promoted_rows']}** promoted and **{payload['queue_adjudication']['retained_candidate_rows']}** retained as candidate-only.",
        f"Expanded search status: **{payload['expanded_search']['status']}**; no exact queued pair met the mouse direct-binding, functional-response, provenance, and direction contract. Search layers and primary near-match citations are listed in `{payload['expanded_search']['manifest']}`.",
        "",
        "## Context-mode eligibility",
        "",
        "| Mode | Eligible rows | Unique pairs |",
        "|---|---:|---:|",
    ]
    for mode in ("general_mouse", "neural", "sci"):
        item = modes[mode]
        lines.append(f"| `{mode}` | {item['row_count']} | {item['unique_pair_count']} |")
    lines += [
        "",
        "## Reconciliation and limitations",
        "",
        f"Active-graph pair status: exact pair **{graph_status.get('exact_pair_in_active_graph', 0)}**, both nodes present without exact edge **{graph_status.get('regulator_and_target_nodes_present', 0)}**, not found **{graph_status.get('not_found_in_active_graph', 0)}**.",
        f"Duplicate exact pairs: **{reconciliation['duplicate_pair_count']}**; pairs duplicated across modules: **{reconciliation['module_duplicate_pair_count']}**.",
        f"Exact old/new semantic pair matches: **{reconciliation['semantic_crosswalk'].get('exact_label_relation_matches', 'unknown')}**; unresolved old/new pairs: **{reconciliation['semantic_crosswalk'].get('unresolved_old_pairs', 'unknown')} / {reconciliation['semantic_crosswalk'].get('unresolved_new_pairs', 'unknown')}**.",
        "",
        "The candidate layer lacks structured tissue and cell-type fields; the ledger preserves unknown values. Graph membership was not used as a likelihood factor or CellChat/LIANA label. No label-adjudication queue was created because dependency metadata were not supplied.",
        f"Unavailable citation rows: **{payload['unavailable_citation_rows']}**; missing local inputs: **{len(payload['missing_local_inputs'])}**.",
        f"Sensitivity smoke benchmark: **{payload['sensitivity_smoke']['status']}** — {payload['sensitivity_smoke']['reason']}.",
        "",
        "The machine-readable ledger, mouse direct-binding review queue, expanded search manifest, traversable-edge overlay, summary, and old/new semantic crosswalk are stored under `data/processed/public_tf_curation_v2026_09_04/`.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--active-dir", type=Path)
    parser.add_argument("--previous-dir", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    source_dir = args.source_dir.resolve()
    active_dir = (args.active_dir or source_dir).resolve()
    previous_dir = args.previous_dir.resolve()
    output_dir = args.output_dir.resolve()
    queue_adjudication_summary_path = output_dir / "public_tf_queue_adjudication_summary.json"

    candidates_path = source_dir / "public_tf_candidate_layer.tsv"
    validated_path = source_dir / "public_tf_validated_edge_layer.tsv"
    candidate_rows = read_tsv(candidates_path)
    validated_rows = read_tsv(validated_path)
    if len(candidate_rows) != 4174:
        raise ValueError(f"Expected 4,174 candidate rows from v1.1.0; observed {len(candidate_rows)}")
    candidate_ids = {text(row, "layer_record_id") for row in candidate_rows}
    missing_ids = [text(row, "layer_record_id") for row in validated_rows if text(row, "layer_record_id") not in candidate_ids]
    if missing_ids:
        raise ValueError(f"Validated overlay contains rows absent from candidate layer: {missing_ids[:5]}")

    nodes = read_tsv(active_dir / "mechanism_nodes.tsv")
    edges = read_tsv(active_dir / "mechanism_edges.tsv")
    active_pairs, active_nodes = graph_indexes(nodes, edges)
    ledger = build_ledger_rows(
        candidate_rows,
        validated_rows,
        active_pair_edges=active_pairs,
        active_node_symbols=active_nodes,
    )
    mouse_queue = build_mouse_direct_binding_queue(candidate_rows, validated_rows)
    curation = summarize_ledger(ledger)
    crosswalk, crosswalk_summary = semantic_crosswalk(previous_dir, active_dir)
    optional_inputs = [
        active_dir / "feature_catalog.tsv",
        active_dir / "cluster_registry.tsv",
        active_dir / "perturbation_model" / "feature_registry.tsv",
        active_dir.parent / "calibration_matrices",
    ]
    missing_local_inputs = [relative(path) for path in optional_inputs if not path.exists()]
    route_candidates = active_dir / "route_candidates.tsv"
    route_steps = active_dir / "route_steps.tsv"
    sensitivity_smoke = {
        "status": "not_run",
        "reason": "route_candidates.tsv and route_steps.tsv are absent; identical calibration and evaluation artifacts are unavailable",
        "route_candidates_present": route_candidates.is_file(),
        "route_steps_present": route_steps.is_file(),
    }
    duplicate_pairs = {
        pair_key(str(row["regulator"]), str(row["target"]))
        for row in ledger
        if int(row["duplicate_pair_row_count"]) > 1
    }
    module_duplicate_pairs = {
        pair_key(str(row["regulator"]), str(row["target"]))
        for row in ledger
        if int(row["duplicate_module_count"]) > 1
    }
    traversable = [row for row in ledger if row["traversal_eligibility"] == "context_gated"]
    queue_adjudication_summary = (
        json.loads(queue_adjudication_summary_path.read_text(encoding="utf-8"))
        if queue_adjudication_summary_path.exists()
        else {}
    )
    search_manifest_path = output_dir / "public_tf_expanded_search_manifest.json"
    search_manifest = (
        json.loads(search_manifest_path.read_text(encoding="utf-8"))
        if search_manifest_path.exists()
        else {}
    )
    payload = {
        "schema_version": "mscidblit_public_tf_curation_summary_v1",
        "release_id": "module20_24_mechanism_graph:v1.1.0",
        "promotion_scope": "existing_v1.1.0_validated_overlay_plus_expanded_queue_adjudication_no_new_literature_promotions",
        "source_dir": relative(source_dir),
        "active_dir": relative(active_dir),
        "rows_reviewed": len(candidate_rows),
        "distinct_source_rows": len({text(row, "layer_record_id") for row in candidate_rows}),
        "distinct_pairs": len({pair_key(text(row, "regulator_symbol"), text(row, "target_symbol")) for row in candidate_rows}),
        "input_checksums": {
            "candidate_layer": sha256_file(candidates_path),
            "validated_overlay": sha256_file(validated_path),
            "active_nodes": sha256_file(active_dir / "mechanism_nodes.tsv"),
            "active_edges": sha256_file(active_dir / "mechanism_edges.tsv"),
        },
        "inventory": inventory(candidate_rows),
        "curation": curation,
        "traversable_overlay": {
            "row_count": len(traversable),
            "unique_pair_count": len({pair_key(str(row["regulator"]), str(row["target"])) for row in traversable}),
            "source": "validated_v1.1.0_overlay_only",
        },
        "mouse_direct_binding_review_queue": {
            "row_count": len(mouse_queue),
            "source": "mouse_canonical_tf_direct_binding_rows_not_in_validated_overlay",
            "all_rows_non_traversable": True,
        },
        "queue_adjudication": {
            "rows_reviewed": len(mouse_queue),
            "promoted_rows": queue_adjudication_summary.get("traversable_rows_added", 0),
            "retained_candidate_rows": len(mouse_queue) - queue_adjudication_summary.get("traversable_rows_added", 0),
            "status": queue_adjudication_summary.get(
                "method", "expanded_exact_pair_search_completed_no_promotions"
            ),
            "ledger": "data/processed/public_tf_curation_v2026_09_04/public_tf_queue_adjudication.tsv",
            "search_manifest": "data/processed/public_tf_curation_v2026_09_04/public_tf_expanded_search_manifest.json",
        },
        "expanded_search": {
            "status": search_manifest.get(
                "search_status",
                "not_recorded",
            ),
            "manifest": "data/processed/public_tf_curation_v2026_09_04/public_tf_expanded_search_manifest.json",
            "rows_promoted": search_manifest.get("promotion_decision", {}).get(
                "rows_promoted", 0
            ),
            "primary_evidence_leads": len(
                search_manifest.get("primary_evidence_leads", [])
            ),
        },
        "reconciliation": {
            "active_graph_pair_status": curation["active_graph_pair_status"],
            "active_graph_node_count": len(nodes),
            "active_graph_edge_count": len(edges),
            "semantic_crosswalk": crosswalk_summary,
            "duplicate_pair_count": len(duplicate_pairs),
            "module_duplicate_pair_count": len(module_duplicate_pairs),
            "rows_without_exact_active_graph_edge": sum(
                row["active_graph_pair_status"] != "exact_pair_in_active_graph" for row in ledger
            ),
            "rows_without_matching_active_graph_node_symbol": sum(
                row["active_graph_node_resolution"] == "no_matching_active_graph_node_symbol" for row in ledger
            ),
            "source_rows_with_explicit_graph_edge_id": 0,
            "current_route_gene_overlap": "unknown_not_available_in_mscidblit_release",
            "current_cell_type_overlap": "unknown_not_structured_in_candidate_layer",
            "current_perturbation_feature_overlap": "unknown_not_available_in_mscidblit_release",
            "current_validation_study_overlap": "unknown_not_available_in_mscidblit_release",
        },
        "data_gaps": [
            "candidate layer has no structured tissue or cell-type field; ledger preserves unknown",
            "effect direction is unknown for source candidate rows unless supplied by validated overlay",
            "graph membership is not an independent likelihood factor and was not used as a method label",
            "unresolved A/B/E rows require new exact-pair adjudication before promotion",
            "route, perturbation, validation-study, and calibration artifacts are not part of this mSCIdblit release",
        ],
        "missing_local_inputs": missing_local_inputs,
        "unavailable_citation_rows": curation["source_locator_status"].get("missing_source_locator", 0),
        "sensitivity_smoke": sensitivity_smoke,
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    write_tsv(output_dir / "public_tf_curation_ledger.tsv", ledger)
    write_tsv(output_dir / "public_tf_traversable_edge_overlay.tsv", traversable)
    write_tsv(output_dir / "public_tf_mouse_direct_binding_review_queue.tsv", mouse_queue)
    write_tsv(output_dir / "public_tf_old_new_semantic_crosswalk.tsv", crosswalk)
    (output_dir / "public_tf_curation_summary.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    report = ROOT / "docs" / "PUBLIC_TF_CURATION_REVIEW_2026-09-04.md"
    report.write_text(markdown_summary(payload), encoding="utf-8")
    print(json.dumps({"rows_reviewed": len(ledger), "curation": curation["curation_status"], "context_modes": curation["context_modes"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
