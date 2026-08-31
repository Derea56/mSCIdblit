#!/usr/bin/env python3
"""Prepare a fillable review packet for noncanonical gene-expression regulators."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

from public_tf_vocabulary import MECHANISM_DEFINITIONS, graded_context_profile, mechanism_evidence_type


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/module_integration_staging_v1/noncanonical_gene_expression_regulators.tsv"
DEFAULT_OUTPUT_DIR = DEFAULT_INPUT.parent
DECISION_VALUES = {
    "promote_to_noncanonical_module_layer",
    "retain_context_only",
    "screen_out",
    "needs_more_context",
}
PRIORITY = {"A_independent_literature_corroborated": 1, "B_independent_literature_single_source": 2}
NONTRANSCRIPTIONAL_SUBCATEGORIES = {"upstream_signaling_or_relay", "protein_ptm_regulator"}

REVIEW_FIELDS = [
    "review_queue_rank", "review_priority", "module_owner_decision", "module_owner_notes",
    "noncanonical_materialization_status", "decision_id", "module", "integration_id",
    "queue_key", "promotion_id", "review_id", "regulator_key", "regulator_symbol",
    "raw_tf_symbol", "target_symbol", "species_scope", "target_graph_modules", "module_route",
    "promotion_scope", "promotion_class", "promotion_confidence", "evidence_confidence_tier",
    "evidence_weight_tier", "evidence_weight_rank", "evidence_tier_basis", "disposition",
    "primary_citation", "corroborating_citation", "primary_and_corroborating_citations",
    "source_registry", "source_record_id", "source_registries", "source_record_ids",
    "source_exportable", "regulatory_role", "role_subcategory", "canonical_tf_eligible",
    "module_context_eligible", "noncanonical_context_candidate", "decision_basis",
    "regulator_role_class", "canonical_role_status", "sci_context_status",
    "sci_context_required", "module_fit_status", "materialization_lane",
    "mechanism_evidence_type", "mechanism_evidence_definition",
    "context_level_regulator", "context_level_target", "context_level_exact_pair",
    "context_evidence_scope", "context_evidence_basis", "context_promotion_lane",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=REVIEW_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    args = parse_args()
    args.input = args.input.resolve()
    args.output_dir = args.output_dir.resolve()
    source_rows = read_tsv(args.input)
    if not source_rows:
        raise SystemExit("no noncanonical rows found")

    ordered = sorted(
        source_rows,
        key=lambda row: (PRIORITY.get(row["evidence_weight_tier"], 9), row["module"], row["queue_key"]),
    )
    review_rows: list[dict[str, str]] = []
    for index, source in enumerate(ordered, start=1):
        regulator_role_class = (
            "non_transcriptional_regulator"
            if source.get("role_subcategory") in NONTRANSCRIPTIONAL_SUBCATEGORIES
            else "noncanonical_gene_expression_regulator"
        )
        canonical_role_status = (
            "not_a_canonical_tf"
            if regulator_role_class == "non_transcriptional_regulator"
            else "noncanonical_regulator"
        )
        materialization_lane = (
            "external_regulatory_evidence_candidate"
            if regulator_role_class == "non_transcriptional_regulator"
            else "noncanonical_module_context_candidate"
        )
        row = {field: source.get(field, "") for field in REVIEW_FIELDS}
        row.update(
            {
                "review_queue_rank": str(index),
                "review_priority": "high" if source["evidence_weight_tier"].startswith("A_") else "standard",
                "module_owner_decision": "pending_review",
                "module_owner_notes": "",
                "noncanonical_materialization_status": "pending_owner_review",
                "canonical_tf_eligible": "false",
                "module_context_eligible": "true",
                "noncanonical_context_candidate": "true",
                "regulator_role_class": regulator_role_class,
                "canonical_role_status": canonical_role_status,
                "sci_context_status": source.get("sci_context_status", "unresolved_sci_context"),
                "sci_context_required": "true",
                "module_fit_status": source.get("module_fit_status", "explicit_route_noncanonical"),
                "materialization_lane": materialization_lane,
                "mechanism_evidence_type": source.get("mechanism_evidence_type", mechanism_evidence_type(source)),
                "mechanism_evidence_definition": source.get(
                    "mechanism_evidence_definition",
                    MECHANISM_DEFINITIONS[mechanism_evidence_type(source)],
                ),
            }
        )
        context_defaults = graded_context_profile(source)
        for field, default in context_defaults.items():
            row[field] = source.get(field, default)
        review_rows.append(row)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    packet = args.output_dir / "noncanonical_module_owner_review.tsv"
    write_tsv(packet, review_rows)
    rubric = args.output_dir / "noncanonical_module_owner_review_rubric.md"
    rubric.write_text(
        "# Noncanonical gene-expression regulator module-owner review\n\n"
        "Each row is a reviewed A/B evidence-backed relationship that has an "
        "explicit module route but is not a canonical sequence-specific TF edge. "
        "The evidence tier and provenance columns are source-controlled; module "
        "owners should only fill `module_owner_decision` and `module_owner_notes`.\n\n"
        "Allowed decisions:\n\n"
        "- `promote_to_noncanonical_module_layer`: exact regulator-target-species "
        "relationship, mechanism fits the module, and the relationship should be "
        "represented in the auxiliary noncanonical layer.\n"
        "- `retain_context_only`: evidence is useful context but is not sufficiently "
        "module-specific or mechanistically actionable.\n"
        "- `screen_out`: identity, species, target, direction, or mechanism does not "
        "support inclusion in the module context layer.\n"
        "- `needs_more_context`: plausible relationship, but module or SCI target-cell "
        "relevance requires additional evidence.\n\n"
        "Regardless of decision, do not change the original evidence tier. The fields "
        "`regulator_role_class` and `canonical_role_status` describe biological role, "
        "while `sci_context_status` records SCI relevance independently. These rows "
        "remain noncanonical and an approved row would be placed only in the separate "
        "noncanonical module-context layer.\n",
        encoding="utf-8",
    )
    summary = {
        "status": "pass",
        "input_rows": len(source_rows),
        "review_packet_rows": len(review_rows),
        "module_counts": dict(sorted(Counter(row["module"] for row in review_rows).items())),
        "tier_counts": dict(sorted(Counter(row["evidence_weight_tier"] for row in review_rows).items())),
        "subcategory_counts": dict(sorted(Counter(row["role_subcategory"] for row in review_rows).items())),
        "all_decisions_start_as": "pending_review",
        "allowed_decisions": sorted(DECISION_VALUES),
        "canonical_tf_eligible": False,
        "role_context_separated": True,
        "regulator_role_class_counts": dict(sorted(Counter(row["regulator_role_class"] for row in review_rows).items())),
        "sci_context_status_counts": dict(sorted(Counter(row["sci_context_status"] for row in review_rows).items())),
        "module_context_eligible": True,
        "outputs": [packet.name, rubric.name],
    }
    (args.output_dir / "noncanonical_module_owner_review_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
