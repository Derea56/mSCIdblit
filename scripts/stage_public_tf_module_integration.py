#!/usr/bin/env python3
"""Stage reviewed public-TF evidence for module-level screening.

This is an additive, file-based integration layer. It expands every reviewed
A--E queue row with an explicit ``target_graph_modules`` assignment into one
row per module while preserving the source overlay or queue provenance,
original evidence tier, species, citations, and review disposition. D/E rows
are visible for screening but have zero ranking weight and cannot be
materialized. U rows are excluded. This script does not write canonical TF,
Module 22B, or database records.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QUEUE = ROOT / "data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/evidence_priority_queue.tsv"
DEFAULT_PROMOTED = ROOT / "data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/promoted_interactions.tsv"
DEFAULT_OUTPUT = ROOT / "data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/module_integration_staging_v1"
MODULES = {"20B", "21B", "22B", "23B", "24B"}
TIER_WEIGHTS = {
    "A_independent_literature_corroborated": 3,
    "B_independent_literature_single_source": 2,
    "C_tflink_source_table_only": 1,
    "D_database_only_no_pair_evidence": 0,
    "E_reviewed_nonpromotable": 0,
}
U_TIER_PREFIX = "U_"

OUTPUT_FIELDS = [
    "integration_id", "module", "queue_key", "promotion_id", "review_id", "batch_id", "batch_rank",
    "regulator_key", "regulator_symbol", "raw_tf_symbol", "target_symbol", "species_scope",
    "target_graph_modules", "module_route", "priority_tier", "queue_state", "search_lane",
    "promotion_scope", "promotion_class", "promotion_confidence", "evidence_confidence_tier",
    "evidence_weight_tier", "evidence_weight_rank", "evidence_tier_basis",
    "independent_literature_support_status", "independent_literature_source_count",
    "exact_pair_status", "effect_polarity", "disposition", "binding_or_association_status",
    "downstream_expression_or_perturbation_status", "downstream_activation_status",
    "upstream_relay_status", "primary_citation", "corroborating_citation",
    "additional_corroborating_citation", "primary_and_corroborating_citations",
    "source_registry", "source_record_id", "source_registries", "source_record_ids",
    "tflink_source_database", "tflink_detection_method", "tflink_pubmed_id",
    "tflink_source_url", "tflink_raw_snapshot_path", "tflink_raw_snapshot_sha256",
    "tflink_source_selection", "source_review_file", "review_notes", "near_match_exclusions",
    "source_exportable", "canonical_write_performed", "module22b_write_performed",
    "module_stage_status", "module_materialization_allowed",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue", type=Path, default=DEFAULT_QUEUE)
    parser.add_argument("--promoted", type=Path, default=DEFAULT_PROMOTED)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def split_modules(value: str) -> list[str]:
    return [item.strip() for item in (value or "").split(";") if item.strip()]


def normalize_key(regulator: str, target: str, species: str) -> str:
    return "|".join((regulator or "", target or "", species or "")).casefold()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def base_row(queue_row: dict[str, str], promoted_row: dict[str, str] | None) -> dict[str, str]:
    """Merge the promoted overlay when present, retaining queue audit fields."""
    if promoted_row is not None:
        result = {field: promoted_row.get(field, "") for field in OUTPUT_FIELDS}
        result.update(
            {
                "queue_key": queue_row["queue_key"],
                "priority_tier": queue_row["priority_tier"],
                "queue_state": queue_row["queue_state"],
                "search_lane": queue_row["search_lane"],
                "evidence_confidence_tier": queue_row["evidence_confidence_tier"],
                "evidence_tier_basis": queue_row["evidence_tier_basis"],
                "primary_and_corroborating_citations": queue_row["primary_and_corroborating_citations"],
                "source_registries": queue_row["source_registries"],
                "source_record_ids": queue_row["source_record_ids"],
            }
        )
        return result

    # D/E rows are represented directly from the reviewed queue. These fields
    # are intentionally blank where the promotion overlay has no row.
    return {
        "queue_key": queue_row["queue_key"],
        "review_id": queue_row["review_ids"],
        "regulator_key": queue_row["queue_key"].split("|", 1)[0],
        "regulator_symbol": queue_row["regulator_symbol"],
        "target_symbol": queue_row["target_symbol"],
        "species_scope": queue_row["species_scope"],
        "target_graph_modules": queue_row["target_graph_modules"],
        "module_route": queue_row["search_lane"],
        "priority_tier": queue_row["priority_tier"],
        "queue_state": queue_row["queue_state"],
        "search_lane": queue_row["search_lane"],
        "evidence_confidence_tier": queue_row["evidence_confidence_tier"],
        "evidence_weight_tier": queue_row["evidence_confidence_tier"],
        "evidence_tier_basis": queue_row["evidence_tier_basis"],
        "exact_pair_status": queue_row["exact_pair_statuses"],
        "disposition": queue_row["dispositions"],
        "primary_and_corroborating_citations": queue_row["primary_and_corroborating_citations"],
        "source_registries": queue_row["source_registries"],
        "source_record_ids": queue_row["source_record_ids"],
        "review_notes": queue_row["next_action"],
        "source_exportable": "false",
        "canonical_write_performed": "false",
        "module22b_write_performed": "false",
    }


def staged_row(queue_row: dict[str, str], promoted_row: dict[str, str] | None, module: str, index: int) -> dict[str, str]:
    tier = queue_row["evidence_confidence_tier"] if promoted_row is None else promoted_row["evidence_weight_tier"]
    result = {field: "" for field in OUTPUT_FIELDS}
    result.update(base_row(queue_row, promoted_row))
    result.update(
        {
            "integration_id": f"PTF-MODULE-{module}-{index:06d}",
            "module": module,
            "evidence_confidence_tier": queue_row["evidence_confidence_tier"],
            "evidence_weight_tier": tier,
            "evidence_weight_rank": str(TIER_WEIGHTS[tier]),
            "source_exportable": "true" if promoted_row is not None else "false",
            "canonical_write_performed": "false",
            "module22b_write_performed": "false",
            "module_stage_status": (
                "staged_review_only" if promoted_row is not None else "staged_low_tier_screening_only"
            ),
            "module_materialization_allowed": "false",
        }
    )
    return result


def main() -> int:
    args = parse_args()
    args.queue = args.queue.resolve()
    args.promoted = args.promoted.resolve()
    args.output_dir = args.output_dir.resolve()
    queue_rows = read_tsv(args.queue)
    promoted_rows = read_tsv(args.promoted)

    errors: list[str] = []
    queue_keys = [row.get("queue_key", "") for row in queue_rows]
    if len(queue_keys) != len(set(queue_keys)):
        errors.append("duplicate queue_key in evidence priority queue")

    promoted_by_key: dict[str, dict[str, str]] = {}
    for row in promoted_rows:
        key = normalize_key(row.get("regulator_symbol", ""), row.get("target_symbol", ""), row.get("species_scope", ""))
        if key in promoted_by_key:
            errors.append(f"duplicate promoted pair key: {key}")
        promoted_by_key[key] = row
        if row.get("exportable") != "true":
            errors.append(f"non-exportable promoted input row: {row.get('promotion_id', '')}")
        if row.get("canonical_write_performed") != "false":
            errors.append(f"canonical write flag is not false: {row.get('promotion_id', '')}")
        if row.get("module22b_write_performed") != "false":
            errors.append(f"Module 22B write flag is not false: {row.get('promotion_id', '')}")

    queue_by_key = {row["queue_key"]: row for row in queue_rows}
    for key, row in promoted_by_key.items():
        if key not in queue_by_key:
            errors.append(f"promoted pair missing from queue: {key}")

    module_rows: dict[str, list[tuple[dict[str, str], dict[str, str] | None]]] = defaultdict(list)
    catalog_only: list[tuple[dict[str, str], dict[str, str] | None]] = []
    seen_assignments: set[tuple[str, str]] = set()
    assignment_count_by_key: Counter[str] = Counter()
    reviewed_tier_counts: Counter[str] = Counter()
    for queue_row in queue_rows:
        key = queue_row["queue_key"]
        tier = queue_row.get("evidence_confidence_tier", "")
        reviewed_tier_counts[tier] += 1
        if tier.startswith(U_TIER_PREFIX):
            # U is explicitly not module-integrated; retain it in the queue,
            # where it can be audited if such rows are introduced later.
            continue
        if tier not in TIER_WEIGHTS:
            errors.append(f"unsupported evidence tier {tier!r}: {key}")
            continue

        promoted_row = promoted_by_key.get(key)
        if promoted_row is None:
            normalized = normalize_key(queue_row["regulator_symbol"], queue_row["target_symbol"], queue_row["species_scope"])
            promoted_row = promoted_by_key.get(normalized)
        if promoted_row is not None and promoted_row["evidence_weight_tier"] != tier:
            errors.append(f"queue/promoted tier mismatch: {key}")

        modules = split_modules(queue_row.get("target_graph_modules", ""))
        unknown = sorted(set(modules) - MODULES)
        if unknown:
            errors.append(f"unknown module assignment {unknown}: {key}")
        if not modules:
            catalog_only.append((queue_row, promoted_row))
            continue
        for module in modules:
            assignment = (module, key)
            if assignment in seen_assignments:
                errors.append(f"duplicate module assignment: {assignment}")
            seen_assignments.add(assignment)
            assignment_count_by_key[key] += 1
            module_rows[module].append((queue_row, promoted_row))

    if errors:
        raise SystemExit("\n".join(errors))

    staged: dict[str, list[dict[str, str]]] = {}
    for module in sorted(MODULES):
        pairs = sorted(module_rows[module], key=lambda pair: pair[0]["queue_key"])
        staged[module] = [
            staged_row(queue_row, promoted_row, module, index)
            for index, (queue_row, promoted_row) in enumerate(pairs, start=1)
        ]
        write_tsv(args.output_dir / f"module_{module}_evidence_staging.tsv", staged[module])

    catalog_rows = []
    for index, (queue_row, promoted_row) in enumerate(sorted(catalog_only, key=lambda pair: pair[0]["queue_key"]), start=1):
        item = staged_row(queue_row, promoted_row, "catalog_only", index)
        item["module_stage_status"] = (
            "catalog_only_no_explicit_module_route" if promoted_row is not None else "catalog_only_low_tier_screening_only"
        )
        catalog_rows.append(item)
    write_tsv(args.output_dir / "catalog_only_evidence.tsv", catalog_rows)

    all_staged = [row for rows in staged.values() for row in rows]
    module_tier_counts = {
        module: dict(sorted(Counter(row["evidence_weight_tier"] for row in rows).items()))
        for module, rows in sorted(staged.items())
    }
    catalog_tier_counts = dict(sorted(Counter(row["evidence_weight_tier"] for row in catalog_rows).items()))
    manifest = {
        "status": "pass",
        "queue_path": str(args.queue.relative_to(ROOT)),
        "promoted_overlay_path": str(args.promoted.relative_to(ROOT)),
        "reviewed_queue_rows": len(queue_rows),
        "reviewed_tier_counts": dict(sorted(reviewed_tier_counts.items())),
        "module_staged_rows": len(all_staged),
        "catalog_only_rows": len(catalog_rows),
        "module_assignment_counts": {module: len(rows) for module, rows in sorted(staged.items())},
        "evidence_weight_tier_counts_module_staged": dict(sorted(Counter(row["evidence_weight_tier"] for row in all_staged).items())),
        "module_evidence_weight_tier_counts": module_tier_counts,
        "catalog_only_evidence_weight_tier_counts": catalog_tier_counts,
        "promoted_rows_with_multiple_module_assignments": sum(
            count > 1 for key, count in assignment_count_by_key.items() if key in promoted_by_key
        ),
        "reviewed_rows_with_multiple_module_assignments": sum(count > 1 for count in assignment_count_by_key.values()),
        "reviewed_rows_represented_once_or_more": len(queue_rows),
        "canonical_tf_writes": False,
        "module22b_writes": False,
        "module_materialization_allowed": False,
        "policy": [
            "This is an additive module-evidence staging layer, not a canonical database materialization.",
            "All reviewed A-E rows are retained for screening; U rows are excluded from module and catalog staging.",
            "One staged row is emitted per explicit target_graph_modules assignment; multi-module rows are not collapsed.",
            "The original textual evidence tier is preserved exactly; evidence_weight_rank is only a later-ranking aid (A=3, B=2, C=1, D=0, E=0).",
            "D/E rows are screening-only with source_exportable=false and module_materialization_allowed=false.",
            "Rows without explicit target_graph_modules remain catalog_only and are not silently assigned to a module.",
            "No canonical TF, Module 22B, SignalingEdge, Regulon, or other database writes are performed.",
        ],
        "outputs": [
            str((args.output_dir / f"module_{module}_evidence_staging.tsv").relative_to(ROOT))
            for module in sorted(MODULES)
        ] + [str((args.output_dir / "catalog_only_evidence.tsv").relative_to(ROOT))],
    }
    (args.output_dir / "module_integration_staging_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (args.output_dir / "README.md").write_text(
        "# Public TF module integration staging\n\n"
        "This directory is an additive, review-only module staging layer generated "
        "from the comprehensive public-TF review queue and promotion overlay. It "
        "does not write canonical TF, Module 22B, SignalingEdge, Regulon, or other "
        "database rows.\n\n"
        "All reviewed A-E rows are retained. Rows are split one-per-explicit-module "
        "assignment; multi-module assignments remain separate, and rows without an "
        "explicit module route remain in `catalog_only_evidence.tsv`. The original "
        "textual evidence tier is kept unchanged. A/B/C retain ranking aids of 3/2/1; "
        "D/E are screening-only with rank 0, `source_exportable=false`, and "
        "`module_materialization_allowed=false`. U rows are excluded. Source registry, "
        "record, review, species, effect, citation, mechanism, limitation, and raw "
        "snapshot fields are copied when present; queue-level provenance is retained "
        "for reviewed D/E rows.\n\n"
        "See `module_integration_staging_manifest.json` for counts and the explicit "
        "no-materialization policy.\n",
        encoding="utf-8",
    )
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
