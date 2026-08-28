#!/usr/bin/env python3
"""Create deterministic screening decisions for public-TF module staging.

The decision overlay is deliberately separate from the evidence packets. It
marks D/E rows as low-tier screen-outs retained for context, keeps explicitly
noncanonical A/B rows out of canonical/module candidates, and carries A/B/C
explicit-route rows into a provisional module-owner candidate set. No row is
approved or materialized by this script.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/module_integration_staging_v1"
DEFAULT_OUTPUT = DEFAULT_INPUT
LOW_TIERS = {"D_database_only_no_pair_evidence", "E_reviewed_nonpromotable"}
NONCANONICAL_PREFIX = "role_specific_noncanonical"

DECISION_FIELDS = [
    "decision_id", "module", "integration_id", "queue_key", "promotion_id", "review_id",
    "regulator_key", "regulator_symbol", "raw_tf_symbol", "target_symbol", "species_scope",
    "target_graph_modules", "module_route", "priority_tier", "queue_state", "search_lane",
    "promotion_scope", "promotion_class", "promotion_confidence", "evidence_confidence_tier",
    "evidence_weight_tier", "evidence_weight_rank", "evidence_tier_basis", "disposition",
    "primary_citation", "corroborating_citation", "primary_and_corroborating_citations",
    "source_registry", "source_record_id", "source_registries", "source_record_ids",
    "source_exportable", "module_stage_status", "screening_decision",
    "context_retention_status", "module_fit_status", "module_owner_review_status",
    "candidate_for_later_materialization", "canonical_materialization_allowed", "decision_basis",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=DECISION_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def decide(row: dict[str, str]) -> tuple[str, str, str, str, str, str]:
    tier = row["evidence_weight_tier"]
    if tier in LOW_TIERS:
        return (
            "screen_out_low_tier",
            "retain_for_context_only",
            "not_eligible_low_tier",
            "screened_out_low_tier",
            "false",
            "Reviewed D/E evidence is retained for provenance/context but excluded from module support and materialization.",
        )
    if row["module"] == "catalog_only":
        return (
            "retain_catalog_only",
            "retain_for_catalog_only",
            "no_explicit_module_route",
            "not_selected_no_module_route",
            "false",
            "A/B/C evidence is exportable, but no explicit target_graph_modules route is available for module selection.",
        )
    if row.get("promotion_class", "").startswith(NONCANONICAL_PREFIX):
        return (
            "retain_for_context_only",
            "retain_for_context_only",
            "explicit_route_noncanonical",
            "not_selected_noncanonical_role",
            "false",
            "Explicit module route is retained, but the reviewed mechanism class is noncanonical and is not a canonical TF/module candidate.",
        )
    return (
        "module_fit_candidate",
        "not_applicable",
        "explicit_target_graph_modules",
        "pending_module_owner_approval",
        "true",
        "A/B/C evidence has an explicit target_graph_modules assignment; candidate remains pending module-owner approval.",
    )


def decision_row(row: dict[str, str]) -> dict[str, str]:
    decision, context, fit, review, candidate, basis = decide(row)
    result = {field: row.get(field, "") for field in DECISION_FIELDS}
    result.update(
        {
            "decision_id": f"PTF-SCREEN-{row['integration_id']}",
            "screening_decision": decision,
            "context_retention_status": context,
            "module_fit_status": fit,
            "module_owner_review_status": review,
            "candidate_for_later_materialization": candidate,
            "canonical_materialization_allowed": "false",
            "decision_basis": basis,
        }
    )
    return result


def main() -> int:
    args = parse_args()
    args.input_dir = args.input_dir.resolve()
    args.output_dir = args.output_dir.resolve()
    rows: list[dict[str, str]] = []
    for path in sorted(args.input_dir.glob("module_*_evidence_staging.tsv")):
        rows.extend(read_tsv(path))
    rows.extend(read_tsv(args.input_dir / "catalog_only_evidence.tsv"))
    if not rows:
        raise SystemExit("no staging rows found")

    decisions = [decision_row(row) for row in rows]
    candidate_set = [row for row in decisions if row["candidate_for_later_materialization"] == "true"]
    write_tsv(args.output_dir / "module_screening_decisions.tsv", sorted(decisions, key=lambda row: row["decision_id"]))
    write_tsv(args.output_dir / "module_owner_candidate_set.tsv", sorted(candidate_set, key=lambda row: row["decision_id"]))

    summary = {
        "status": "pass",
        "input_rows": len(rows),
        "decision_counts": dict(sorted(Counter(row["screening_decision"] for row in decisions).items())),
        "module_owner_candidate_rows": len(candidate_set),
        "candidate_module_counts": dict(sorted(Counter(row["module"] for row in candidate_set).items())),
        "candidate_tier_counts": dict(sorted(Counter(row["evidence_weight_tier"] for row in candidate_set).items())),
        "low_tier_screen_out_counts": dict(sorted(Counter(row["evidence_weight_tier"] for row in decisions if row["screening_decision"] == "screen_out_low_tier").items())),
        "noncanonical_context_counts": dict(sorted(Counter(row["evidence_weight_tier"] for row in decisions if row["screening_decision"] == "retain_for_context_only").items())),
        "canonical_materialization_allowed": False,
        "all_candidate_approvals_pending": True,
        "policy": [
            "This is a deterministic screening overlay; it does not change source evidence packets.",
            "D/E rows are screen-out_low_tier and retain_for_context_only; their exact evidence tiers remain unchanged.",
            "Explicitly noncanonical role-specific A/B rows remain retain_for_context_only and are excluded from the candidate set.",
            "A/B/C rows with an explicit module route form a provisional module-owner candidate set, pending approval.",
            "Catalog-only rows are not assigned to modules without an explicit target_graph_modules route.",
            "No canonical TF, Module 22B, module tracker, or mechanism-edge materialization is performed.",
        ],
        "outputs": [
            "module_integration_staging_v1/module_screening_decisions.tsv",
            "module_integration_staging_v1/module_owner_candidate_set.tsv",
        ],
    }
    (args.output_dir / "module_screening_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
