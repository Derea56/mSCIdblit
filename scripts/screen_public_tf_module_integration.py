#!/usr/bin/env python3
"""Create deterministic screening decisions for public-TF module staging.

The decision overlay is deliberately separate from the evidence packets. It
marks D/E rows as low-tier screen-outs retained for context, routes explicitly
noncanonical gene-expression regulators to their own module-context group, and
carries A/B/C explicit-route rows into a provisional module-owner candidate
set. No row is approved or materialized by this script.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

from public_tf_vocabulary import (
    CANONICAL_STATUS_NOT_ASSIGNED,
    LANE_CANONICAL,
    LANE_CATALOG_ONLY,
    LANE_EXTERNAL,
    LANE_LOW_TIER,
    LANE_NONCANONICAL,
    ROLE_CANONICAL,
    ROLE_LOW_TIER,
    ROLE_NONCANONICAL,
    ROLE_UNRESOLVED,
    canonical_status_for_role,
    mechanism_evidence_type,
    MECHANISM_DEFINITIONS,
    graded_context_profile,
    role_class_for_promotion,
    sci_context_status,
)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/module_integration_staging_v1"
DEFAULT_OUTPUT = DEFAULT_INPUT
DEFAULT_CONTEXT_ADJUDICATIONS = DEFAULT_INPUT / "context_evidence_adjudications.tsv"
LOW_TIERS = {"D_database_only_no_pair_evidence", "E_reviewed_nonpromotable"}
NONCANONICAL_PREFIX = "role_specific_noncanonical"


def noncanonical_subcategory(promotion_class: str) -> str:
    value = promotion_class.casefold()
    if "chromatin" in value or "epigenetic" in value:
        return "chromatin_modifier_or_reader"
    if "rna" in value or "post_transcriptional" in value:
        return "rna_post_transcriptional_regulator"
    if "protein_ptm" in value or "kinase" in value:
        return "protein_ptm_regulator"
    if "ligand_receptor" in value or "secreted_factor" in value or "pathway" in value:
        return "upstream_signaling_or_relay"
    if "coactivator" in value or "coregulator" in value or "complex" in value:
        return "transcriptional_cofactor_or_coregulator"
    return "noncanonical_exact_gene_expression_regulator"

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
    "regulatory_role", "role_subcategory", "canonical_tf_eligible", "module_context_eligible",
    "noncanonical_context_candidate", "materialization_status", "regulator_role_class",
    "canonical_role_status", "sci_context_status", "sci_context_required", "materialization_lane",
    "mechanism_evidence_type", "mechanism_evidence_definition",
    "context_level_regulator", "context_level_target", "context_level_exact_pair",
    "context_evidence_scope", "context_evidence_basis", "context_promotion_lane",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--context-adjudications", type=Path, default=DEFAULT_CONTEXT_ADJUDICATIONS)
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


def decision_row(row: dict[str, str], context_adjudications: dict[str, dict[str, str]]) -> dict[str, str]:
    decision, context, fit, review, candidate, basis = decide(row)
    result = {field: row.get(field, "") for field in DECISION_FIELDS}
    is_noncanonical = row.get("promotion_class", "").startswith(NONCANONICAL_PREFIX)
    is_low_tier = row["evidence_weight_tier"] in LOW_TIERS
    has_module_route = row["module"] != "catalog_only"
    if is_noncanonical:
        regulatory_role = "noncanonical_gene_expression_regulator"
        role_subcategory = noncanonical_subcategory(row.get("promotion_class", ""))
        canonical_tf_eligible = "false"
        module_context_eligible = "true" if has_module_route else "false"
        noncanonical_context_candidate = "true" if has_module_route else "false"
        materialization_status = "separate_noncanonical_layer_pending_approval"
        regulator_role_class = ROLE_NONCANONICAL
        canonical_role_status = canonical_status_for_role(regulator_role_class)
        materialization_lane = LANE_NONCANONICAL if has_module_route else LANE_EXTERNAL
    elif is_low_tier:
        regulatory_role = "reviewed_low_tier_evidence"
        role_subcategory = row["evidence_weight_tier"].split("_", 1)[0]
        canonical_tf_eligible = "false"
        module_context_eligible = "false"
        noncanonical_context_candidate = "false"
        materialization_status = "screened_out_low_tier"
        regulator_role_class = ROLE_LOW_TIER
        canonical_role_status = CANONICAL_STATUS_NOT_ASSIGNED
        materialization_lane = LANE_LOW_TIER
    elif has_module_route:
        regulatory_role = "public_tf_evidence_candidate"
        role_subcategory = row.get("promotion_class", "")
        canonical_tf_eligible = "pending"
        module_context_eligible = "true"
        noncanonical_context_candidate = "false"
        materialization_status = "pending_module_owner_approval"
        regulator_role_class = role_class_for_promotion(row.get("promotion_class", ""))
        canonical_role_status = canonical_status_for_role(regulator_role_class)
        materialization_lane = LANE_CANONICAL if regulator_role_class == ROLE_CANONICAL else LANE_EXTERNAL
    else:
        regulatory_role = "public_tf_evidence_candidate"
        role_subcategory = row.get("promotion_class", "")
        canonical_tf_eligible = "false"
        module_context_eligible = "false"
        noncanonical_context_candidate = "false"
        materialization_status = "catalog_only_no_module_route"
        regulator_role_class = role_class_for_promotion(row.get("promotion_class", ""))
        canonical_role_status = canonical_status_for_role(regulator_role_class)
        materialization_lane = LANE_CATALOG_ONLY
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
            "regulatory_role": regulatory_role,
            "role_subcategory": role_subcategory,
            "canonical_tf_eligible": canonical_tf_eligible,
            "module_context_eligible": module_context_eligible,
            "noncanonical_context_candidate": noncanonical_context_candidate,
            "materialization_status": materialization_status,
            "regulator_role_class": regulator_role_class,
            "canonical_role_status": canonical_role_status,
            "sci_context_status": sci_context_status(row, not_applicable=not has_module_route),
            "sci_context_required": "true" if has_module_route and not is_low_tier else "false",
            "materialization_lane": materialization_lane,
            "mechanism_evidence_type": mechanism_evidence_type(row),
            "mechanism_evidence_definition": MECHANISM_DEFINITIONS[mechanism_evidence_type(row)],
        }
    )
    result.update(graded_context_profile(row, low_tier=is_low_tier, no_module_route=not has_module_route))
    # Context is applied as a separate overlay. It is keyed by promotion_id
    # so that one reviewed relationship gets the same context fields in every
    # explicitly routed module row, without changing evidence tier or role.
    context = context_adjudications.get(row.get("promotion_id", ""))
    if context and has_module_route:
        for field in (
            "context_level_regulator", "context_level_target", "context_level_exact_pair",
            "context_evidence_scope", "context_evidence_basis", "context_promotion_lane",
        ):
            result[field] = context[field]
        result["sci_context_status"] = context["sci_context_status"]
    return result


def main() -> int:
    args = parse_args()
    args.input_dir = args.input_dir.resolve()
    args.output_dir = args.output_dir.resolve()
    args.context_adjudications = args.context_adjudications.resolve()
    context_adjudications = {}
    if args.context_adjudications.exists():
        for context in read_tsv(args.context_adjudications):
            context_adjudications[context["promotion_id"]] = context
    rows: list[dict[str, str]] = []
    for path in sorted(args.input_dir.glob("module_*_evidence_staging.tsv")):
        rows.extend(read_tsv(path))
    rows.extend(read_tsv(args.input_dir / "catalog_only_evidence.tsv"))
    if not rows:
        raise SystemExit("no staging rows found")

    decisions = [decision_row(row, context_adjudications) for row in rows]
    candidate_set = [row for row in decisions if row["candidate_for_later_materialization"] == "true"]
    noncanonical_rows = [row for row in decisions if row["noncanonical_context_candidate"] == "true"]
    write_tsv(args.output_dir / "module_screening_decisions.tsv", sorted(decisions, key=lambda row: row["decision_id"]))
    write_tsv(args.output_dir / "module_owner_candidate_set.tsv", sorted(candidate_set, key=lambda row: row["decision_id"]))
    write_tsv(args.output_dir / "noncanonical_gene_expression_regulators.tsv", sorted(noncanonical_rows, key=lambda row: row["decision_id"]))

    summary = {
        "status": "pass",
        "input_rows": len(rows),
        "decision_counts": dict(sorted(Counter(row["screening_decision"] for row in decisions).items())),
        "module_owner_candidate_rows": len(candidate_set),
        "candidate_module_counts": dict(sorted(Counter(row["module"] for row in candidate_set).items())),
        "candidate_tier_counts": dict(sorted(Counter(row["evidence_weight_tier"] for row in candidate_set).items())),
        "noncanonical_module_context_rows": len(noncanonical_rows),
        "noncanonical_module_counts": dict(sorted(Counter(row["module"] for row in noncanonical_rows).items())),
        "noncanonical_subcategory_counts": dict(sorted(Counter(row["role_subcategory"] for row in noncanonical_rows).items())),
        "noncanonical_tier_counts": dict(sorted(Counter(row["evidence_weight_tier"] for row in noncanonical_rows).items())),
        "low_tier_screen_out_counts": dict(sorted(Counter(row["evidence_weight_tier"] for row in decisions if row["screening_decision"] == "screen_out_low_tier").items())),
        "noncanonical_context_counts": dict(sorted(Counter(row["evidence_weight_tier"] for row in decisions if row["screening_decision"] == "retain_for_context_only").items())),
        "canonical_materialization_allowed": False,
        "all_candidate_approvals_pending": True,
        "policy": [
            "This is a deterministic screening overlay; it does not change source evidence packets.",
            "D/E rows are screen-out_low_tier and retain_for_context_only; their exact evidence tiers remain unchanged.",
            "Regulator role, SCI context, evidence tier, module fit, and materialization lane are independent fields.",
            "Mechanism evidence type states what molecular bridge is actually supported; it does not imply that omitted intermediate steps or promoter occupancy were demonstrated.",
            "Rows without a context adjudication remain conservatively at L0_no_context_evidence with context_evidence_scope=not_assessed; reviewed overlays record non-CNS, CNS, spinal-cord-tissue, SCI, or explicitly unresolved/unverifiable context and its scope.",
            f"{len(context_adjudications)} promotion-level context adjudications are applied from {args.context_adjudications.name}; component-level context never upgrades an exact pair.",
            "Explicitly noncanonical role-specific A/B rows are routed to noncanonical_gene_expression_regulators.tsv with regulator_role_class=noncanonical_gene_expression_regulator; canonical_tf_eligible=false is a role field and is not an SCI-context result.",
            "SCI context remains unresolved when the reviewed record cannot verify a higher context level; this is separate from the L0 context grade and from evidence tier.",
            "A/B/C rows with an explicit module route form a provisional module-owner candidate set, pending approval.",
            "Catalog-only rows are not assigned to modules without an explicit target_graph_modules route.",
            "No canonical TF, Module 22B, module tracker, or mechanism-edge materialization is performed.",
        ],
        "outputs": [
            "module_integration_staging_v1/module_screening_decisions.tsv",
            "module_integration_staging_v1/module_owner_candidate_set.tsv",
            "module_integration_staging_v1/noncanonical_gene_expression_regulators.tsv",
        ],
    }
    (args.output_dir / "module_screening_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
