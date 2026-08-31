#!/usr/bin/env python3
"""Record conservative module-context adjudications for noncanonical candidates."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

from public_tf_vocabulary import MECHANISM_DEFINITIONS, graded_context_profile, mechanism_evidence_type


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/module_integration_staging_v1/noncanonical_module_context_triage.tsv"
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


def recommendation(row: dict[str, str]) -> tuple[str, str]:
    action = row["recommended_next_action"]
    if action == "seek_direct_occupancy_and_SCI_context":
        return (
            "needs_more_context",
            "Keep pending until direct occupancy and SCI target-cell context are established; perturbation alone is insufficient for this module layer.",
        )
    if action in {"seek_independent_corroboration_and_SCI_context", "seek_direct_binding_and_corroboration"}:
        return (
            "needs_more_context",
            "Keep pending until the requested independent corroboration or direct binding evidence and SCI target-cell context are available.",
        )
    return (
        "needs_more_context",
        "The existing source-backed mechanism is plausible for the noncanonical layer, but the record does not establish the required SCI target-cell/module context.",
    )


def main() -> int:
    args = parse_args()
    args.input = args.input.resolve()
    args.output_dir = args.output_dir.resolve()
    source_rows = [row for row in read_tsv(args.input) if row["module_context_candidate"] == "true"]
    if not source_rows:
        raise SystemExit("no module-context candidates found")

    rows: list[dict[str, str]] = []
    for source in source_rows:
        decision, basis = recommendation(source)
        row = dict(source)
        row["adjudication_recommendation"] = decision
        row["adjudication_basis"] = basis
        row["adjudication_scope"] = "noncanonical_module_context_only"
        row["module_owner_decision"] = "pending_review"
        row["owner_approval_status"] = "pending_module_owner_approval"
        row["canonical_tf_eligible"] = "false"
        row["noncanonical_materialization_status"] = "pending_owner_review"
        row["regulator_role_class"] = (
            "non_transcriptional_regulator"
            if row.get("mechanism_scope") == "upstream_or_protein_context"
            else "noncanonical_gene_expression_regulator"
        )
        row["canonical_role_status"] = (
            "not_a_canonical_tf"
            if row.get("mechanism_scope") == "upstream_or_protein_context"
            else "noncanonical_regulator"
        )
        # The adjudication layer records module-owner status; it does not
        # overwrite an independently adjudicated context level/status.
        row["sci_context_status"] = row.get("sci_context_status", "unresolved_sci_context")
        row["sci_context_required"] = "true"
        row["module_fit_status"] = row.get("module_fit_status", "explicit_route_noncanonical")
        row["materialization_lane"] = (
            "external_regulatory_evidence_candidate"
            if row.get("mechanism_scope") == "upstream_or_protein_context"
            else "noncanonical_module_context_candidate"
        )
        row["mechanism_evidence_type"] = mechanism_evidence_type(row)
        row["mechanism_evidence_definition"] = MECHANISM_DEFINITIONS[row["mechanism_evidence_type"]]
        for field, default in graded_context_profile(row).items():
            row[field] = row.get(field, default)
        rows.append(row)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output = args.output_dir / "noncanonical_module_context_adjudication.tsv"
    write_tsv(output, rows)
    summary = {
        "status": "pass",
        "input_candidate_rows": len(source_rows),
        "adjudicated_rows": len(rows),
        "recommendation_counts": dict(sorted(Counter(row["adjudication_recommendation"] for row in rows).items())),
        "tier_counts": dict(sorted(Counter(row["evidence_weight_tier"] for row in rows).items())),
        "module_counts": dict(sorted(Counter(row["module"] for row in rows).items())),
        "owner_approval_status": "pending_module_owner_approval",
        "canonical_tf_eligible": False,
        "role_context_separated": True,
        "regulator_role_class_counts": dict(sorted(Counter(row["regulator_role_class"] for row in rows).items())),
        "sci_context_status_counts": dict(sorted(Counter(row["sci_context_status"] for row in rows).items())),
        "materialization_performed": False,
        "policy": [
            "This adjudication uses the existing source-backed review notes and recorded next actions; it is not a new literature promotion pass.",
            "All 35 candidates remain needs_more_context because SCI target-cell/module context or explicitly requested corroboration/occupancy is not yet satisfied.",
            "Original evidence tiers and provenance are unchanged.",
            "Regulator role class and SCI context status are separate; unresolved SCI context does not imply canonical or noncanonical identity.",
            "No canonical TF, Module 22B, module tracker, or noncanonical materialization is performed.",
        ],
        "output": output.name,
    }
    (args.output_dir / "noncanonical_module_context_adjudication_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
