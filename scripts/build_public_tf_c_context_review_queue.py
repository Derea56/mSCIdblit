#!/usr/bin/env python3
"""Build a deduplicated context-review queue for all C-tier rows.

This is a review-planning artifact. C-tier TFLink table evidence is preserved
as C and is never upgraded by this script. Context fields are copied from the
separate adjudication registry; unresolved/unverifiable C records remain L0.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/module_integration_staging_v1/module_screening_decisions.tsv"
DEFAULT_OUTPUT_DIR = ROOT / "data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/module_integration_staging_v1"
DEFAULT_CONTEXT_ADJUDICATIONS = DEFAULT_OUTPUT_DIR / "context_evidence_adjudications.tsv"
C_TIER = "C_tflink_source_table_only"

FIELDS = [
    "review_queue_rank", "priority_band", "route_status", "queue_key", "promotion_id", "regulator_key",
    "regulator_symbol", "raw_tf_symbol", "target_symbol", "species_scope",
    "module_count", "module_assignments", "target_graph_modules", "module_routes",
    "module_row_count", "evidence_weight_tier", "evidence_weight_rank",
    "evidence_tier_basis", "source_registries", "source_record_ids", "review_ids",
    "primary_citations", "regulator_role_class", "canonical_role_status",
    "mechanism_evidence_type", "mechanism_evidence_definition",
    "context_level_regulator", "context_level_target", "context_level_exact_pair",
    "context_evidence_scope", "context_promotion_lane", "context_review_status",
    "context_review_basis",
]


def norm(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip()).casefold()


def unique(values: list[str]) -> list[str]:
    output: list[str] = []
    seen: set[str] = set()
    for value in values:
        value = (value or "").strip()
        if value and value not in seen:
            seen.add(value)
            output.append(value)
    return output


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def priority_band(rows: list[dict[str, str]]) -> tuple[str, int]:
    canonical = any(row.get("canonical_role_status") == "canonical_tf" for row in rows)
    modules = {row.get("module", "") for row in rows if row.get("module") != "catalog_only"}
    if not modules:
        return "C5_catalog_only", 10
    if canonical and len(modules) > 1:
        return "C1_canonical_multi_module", 100
    if canonical:
        return "C2_canonical_single_module", 90
    if len(modules) > 1:
        return "C3_unresolved_multi_module", 70
    return "C4_unresolved_single_module", 50


def aggregate(
    key: tuple[str, str, str],
    rows: list[dict[str, str]],
    context_adjudications: dict[str, dict[str, str]],
) -> dict[str, str]:
    first = rows[0]
    band, score = priority_band(rows)
    routed_rows = [row for row in rows if row.get("module") != "catalog_only"]
    modules = unique([row.get("module", "") for row in routed_rows])
    routes = unique([row.get("module_route", "") for row in routed_rows])
    target_graph_modules = unique([row.get("target_graph_modules", "") for row in rows])
    sources = unique([row.get("source_record_id", "") for row in rows])
    registries = unique([row.get("source_registry", "") for row in rows])
    review_ids = unique([row.get("review_id", "") for row in rows])
    citations = unique([
        citation
        for row in rows
        for citation in (
            row.get("primary_citation", ""),
            row.get("corroborating_citation", ""),
            row.get("primary_and_corroborating_citations", ""),
        )
        for citation in citation.split(";")
    ])
    context = context_adjudications.get(first.get("promotion_id", "")) or next(
        (row for row in rows if row.get("context_review_status") != "not_started"), first
    )
    return {
        "priority_band": f"{band}:{score}",
        "route_status": "module_routed" if modules else "catalog_only",
        "queue_key": "|".join(key),
        "promotion_id": first.get("promotion_id", ""),
        "regulator_key": first.get("regulator_key", ""),
        "regulator_symbol": first.get("regulator_symbol", ""),
        "raw_tf_symbol": first.get("raw_tf_symbol", ""),
        "target_symbol": first.get("target_symbol", ""),
        "species_scope": first.get("species_scope", ""),
        "module_count": str(len(modules)),
        "module_assignments": ";".join(modules),
        "target_graph_modules": ";".join(target_graph_modules),
        "module_routes": ";".join(routes),
        "module_row_count": str(len(rows)),
        "evidence_weight_tier": C_TIER,
        "evidence_weight_rank": "1",
        "evidence_tier_basis": first.get("evidence_tier_basis", ""),
        "source_registries": ";".join(registries),
        "source_record_ids": ";".join(sources),
        "review_ids": ";".join(review_ids),
        "primary_citations": ";".join(citations),
        "regulator_role_class": first.get("regulator_role_class", ""),
        "canonical_role_status": first.get("canonical_role_status", ""),
        "mechanism_evidence_type": first.get("mechanism_evidence_type", ""),
        "mechanism_evidence_definition": first.get("mechanism_evidence_definition", ""),
        "context_level_regulator": context.get("context_level_regulator", "L0_no_context_evidence"),
        "context_level_target": context.get("context_level_target", "L0_no_context_evidence"),
        "context_level_exact_pair": context.get("context_level_exact_pair", "L0_no_context_evidence"),
        "context_evidence_scope": context.get("context_evidence_scope", "not_assessed"),
        "context_promotion_lane": context.get("context_promotion_lane", "context_review_pending"),
        "context_review_status": (
            "adjudicated_context_overlay_applied"
            if context.get("context_review_status") not in {"", "not_started", None}
            else "not_started"
        ),
        "context_review_basis": (
            context.get("context_evidence_basis", "")
            if context.get("context_review_status") not in {"", "not_started", None}
            else (
                "C-tier TFLink source-table-only relationship. Context review is pending; "
                "the TFLink citation is not treated as pair-level causal evidence."
            )
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--slice-size", type=int, default=100)
    parser.add_argument("--context-adjudications", type=Path, default=DEFAULT_CONTEXT_ADJUDICATIONS)
    args = parser.parse_args()

    context_adjudications = {
        row["promotion_id"]: row
        for row in read_tsv(args.context_adjudications.resolve())
    } if args.context_adjudications.resolve().exists() else {}

    rows = [
        row for row in read_tsv(args.input.resolve())
        if row.get("evidence_weight_tier") == C_TIER
    ]
    grouped: dict[tuple[str, str, str], list[dict[str, str]]] = {}
    for row in rows:
        key = (norm(row.get("regulator_symbol", "")), norm(row.get("target_symbol", "")), norm(row.get("species_scope", "")))
        grouped.setdefault(key, []).append(row)

    queue = [aggregate(key, group, context_adjudications) for key, group in grouped.items()]
    queue.sort(key=lambda row: (-int(row["priority_band"].rsplit(":", 1)[1]), row["queue_key"]))
    for index, row in enumerate(queue, start=1):
        row["review_queue_rank"] = str(index)

    args.output_dir.resolve().mkdir(parents=True, exist_ok=True)
    queue_path = args.output_dir.resolve() / "c_tier_context_review_queue.tsv"
    with queue_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(queue)

    slice_rows = queue[:args.slice_size]
    slice_path = args.output_dir.resolve() / "c_tier_context_review_slice_001.tsv"
    with slice_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(slice_rows)

    summary = {
        "status": "pass",
        "source_rows": len(rows),
        "unique_regulator_target_species_relationships": len(queue),
        "module_routed_relationships": sum(row["route_status"] == "module_routed" for row in queue),
        "catalog_only_relationships": sum(row["route_status"] == "catalog_only" for row in queue),
        "deduplication_ratio": round(len(rows) / len(queue), 3) if queue else 0,
        "module_counts": dict(sorted(Counter(row["module_assignments"] for row in queue).items())),
        "priority_band_counts": dict(sorted(Counter(row["priority_band"].split(":", 1)[0] for row in queue).items())),
        "canonical_role_counts": dict(sorted(Counter(row["canonical_role_status"] for row in queue).items())),
        "evidence_tier": C_TIER,
        "context_assignments_performed": any(row["context_review_status"] != "not_started" for row in queue),
        "context_adjudicated_relationships": sum(row["context_review_status"] != "not_started" for row in queue),
        "materialization_performed": False,
        "outputs": [queue_path.name, slice_path.name],
        "policy": [
            "C-tier source-table evidence remains C and is not promoted by queue construction.",
            "Rows are deduplicated by regulator-target-species; all module assignments and source IDs are retained.",
            "Catalog-only relationships remain in the queue with route_status=catalog_only and no inferred module assignment.",
            "Context fields are populated from the adjudication registry; unresolved/unverifiable C records remain L0 and do not change their C tier.",
            "No canonical TF, module, database, or release writes are performed.",
        ],
    }
    (args.output_dir.resolve() / "c_tier_context_review_queue_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
