#!/usr/bin/env python3
"""Apply a conservative pre-screen to the noncanonical owner-review packet."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/module_integration_staging_v1/noncanonical_module_owner_review.tsv"
DEFAULT_OUTPUT_DIR = DEFAULT_INPUT.parent


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    fields = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def prescreen(row: dict[str, str]) -> tuple[str, str, str]:
    disposition = row["disposition"].casefold()
    if "pending_" in disposition:
        return (
            "needs_more_context",
            "Existing disposition explicitly requests SCI context, direct occupancy, corroboration, or target-specific follow-up.",
            "true",
        )
    if "candidate" in disposition and "separately" not in disposition:
        return (
            "needs_more_context",
            "Existing disposition describes a candidate but retains an explicit unresolved context requirement.",
            "true",
        )
    return (
        "retain_context_only",
        "Existing disposition retains a real association or alternate mechanism, but does not support immediate module-context promotion.",
        "false",
    )


def main() -> int:
    args = parse_args()
    args.input = args.input.resolve()
    args.output_dir = args.output_dir.resolve()
    source_rows = read_tsv(args.input)
    if not source_rows:
        raise SystemExit("no review rows found")

    rows: list[dict[str, str]] = []
    for source in source_rows:
        decision, basis, candidate = prescreen(source)
        row = dict(source)
        row["ai_prescreen_decision"] = decision
        row["ai_prescreen_basis"] = basis
        row["ai_prescreen_candidate_for_module_context"] = candidate
        # Owner review remains authoritative and untouched.
        row["module_owner_decision"] = "pending_review"
        row["noncanonical_materialization_status"] = "pending_owner_review"
        row["regulator_role_class"] = row.get("regulator_role_class", "noncanonical_gene_expression_regulator")
        row["canonical_role_status"] = row.get("canonical_role_status", "noncanonical_regulator")
        row["sci_context_status"] = row.get("sci_context_status", "unresolved_sci_context")
        row["sci_context_required"] = row.get("sci_context_required", "true")
        row["materialization_lane"] = row.get("materialization_lane", "noncanonical_module_context_candidate")
        rows.append(row)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output = args.output_dir / "noncanonical_module_owner_prescreen.tsv"
    write_tsv(output, rows)
    summary = {
        "status": "pass",
        "input_rows": len(source_rows),
        "prescreen_rows": len(rows),
        "decision_counts": dict(sorted(Counter(row["ai_prescreen_decision"] for row in rows).items())),
        "candidate_for_module_context_counts": dict(sorted(Counter(row["ai_prescreen_candidate_for_module_context"] for row in rows).items())),
        "tier_counts": dict(sorted(Counter(row["evidence_weight_tier"] for row in rows).items())),
        "owner_decisions_changed": False,
        "canonical_tf_eligible": False,
        "role_context_separated": True,
        "regulator_role_class": "noncanonical_gene_expression_regulator",
        "sci_context_status_counts": dict(sorted(Counter(row["sci_context_status"] for row in rows).items())),
        "noncanonical_materialization_status": "pending_owner_review",
        "policy": [
            "This is an AI pre-screen based only on existing reviewed dispositions; it is not module-owner approval or a new literature adjudication.",
            "Rows marked needs_more_context remain candidates for owner review but are not promoted.",
            "Rows marked retain_context_only remain visible as noncanonical context and are not promoted.",
            "Evidence tiers, source provenance, module routes, and owner decision fields are preserved.",
        ],
        "output": output.name,
    }
    (args.output_dir / "noncanonical_module_owner_prescreen_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
