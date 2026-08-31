#!/usr/bin/env python3
"""Refine noncanonical owner pre-screen rows by mechanism/context scope."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

from public_tf_vocabulary import (
    CANONICAL_STATUS_NONCANONICAL,
    LANE_EXTERNAL,
    LANE_NONCANONICAL,
    ROLE_NONCANONICAL,
    ROLE_NONTRANSCRIPTIONAL,
    SCI_CONTEXT_UNRESOLVED,
    MECHANISM_DEFINITIONS,
    mechanism_evidence_type,
    graded_context_profile,
)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/module_integration_staging_v1/noncanonical_module_owner_prescreen.tsv"
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


def scope(row: dict[str, str]) -> tuple[str, str]:
    value = f"{row['promotion_class']} {row['disposition']}".casefold()
    if any(token in value for token in ("ligand_receptor", "secreted_factor", "receptor_autoregulation", "kinase", "protein_ptm", "cytoskeletal")):
        return (
            "upstream_or_protein_context",
            "This is a relay, receptor, kinase, protein/PTM, or cytoskeletal relationship rather than a direct gene-expression regulator.",
        )
    if "rna" in value or "epitranscriptomic" in value or "post_transcriptional" in value:
        return (
            "rna_gene_expression_regulator",
            "This is an RNA-level gene-expression regulator; retain it outside the canonical TF/regulon layer.",
        )
    if "chromatin" in value or "coactivator" in value or "coregulator" in value or "epigenetic" in value:
        return (
            "transcriptional_chromatin_regulator",
            "This is a chromatin, cofactor, or coregulator relationship with a plausible module gene-expression role.",
        )
    return (
        "other_noncanonical_gene_expression_regulator",
        "This is an exact noncanonical relationship, but the regulator role still requires module-specific review.",
    )


def next_action(row: dict[str, str], mechanism_scope: str) -> str:
    value = row["disposition"].casefold()
    if "independent_corroboration" in value or "corrob" in value:
        return "seek_independent_corroboration_and_SCI_context"
    if "direct_occupancy" in value:
        return "seek_direct_occupancy_and_SCI_context"
    if "direct_binding" in value:
        return "seek_direct_binding_and_corroboration"
    if mechanism_scope == "upstream_or_protein_context":
        return "retain_context_only_unless_module_owner_requests_relay_or_protein_layer"
    return "review_module_specific_SCI_target_cell_context"


def main() -> int:
    args = parse_args()
    args.input = args.input.resolve()
    args.output_dir = args.output_dir.resolve()
    source_rows = read_tsv(args.input)
    if not source_rows:
        raise SystemExit("no pre-screen rows found")

    rows: list[dict[str, str]] = []
    for source in source_rows:
        mechanism_scope, basis = scope(source)
        decision = "retain_context_only" if mechanism_scope == "upstream_or_protein_context" else "needs_more_context"
        row = dict(source)
        row["context_triage_decision"] = decision
        row["mechanism_scope"] = mechanism_scope
        row["context_triage_basis"] = basis
        row["recommended_next_action"] = next_action(source, mechanism_scope)
        row["module_context_candidate"] = "false" if decision == "retain_context_only" else "true"
        row["module_owner_decision"] = "pending_review"
        row["noncanonical_materialization_status"] = "pending_owner_review"
        row["regulator_role_class"] = (
            ROLE_NONTRANSCRIPTIONAL
            if mechanism_scope == "upstream_or_protein_context"
            else ROLE_NONCANONICAL
        )
        row["canonical_role_status"] = (
            "not_a_canonical_tf"
            if mechanism_scope == "upstream_or_protein_context"
            else CANONICAL_STATUS_NONCANONICAL
        )
        # Preserve any context adjudication already attached to the screening
        # overlay; triage must not collapse positive CNS/spinal-cord/SCI
        # findings back to unresolved.
        row["sci_context_status"] = row.get("sci_context_status", SCI_CONTEXT_UNRESOLVED)
        row["sci_context_required"] = "true"
        row["materialization_lane"] = LANE_NONCANONICAL if decision == "needs_more_context" else LANE_EXTERNAL
        row["mechanism_evidence_type"] = mechanism_evidence_type(row)
        row["mechanism_evidence_definition"] = MECHANISM_DEFINITIONS[row["mechanism_evidence_type"]]
        for field, default in graded_context_profile(source).items():
            row[field] = source.get(field, default)
        rows.append(row)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output = args.output_dir / "noncanonical_module_context_triage.tsv"
    write_tsv(output, rows)
    candidate = [row for row in rows if row["module_context_candidate"] == "true"]
    summary = {
        "status": "pass",
        "input_rows": len(source_rows),
        "output_rows": len(rows),
        "decision_counts": dict(sorted(Counter(row["context_triage_decision"] for row in rows).items())),
        "mechanism_scope_counts": dict(sorted(Counter(row["mechanism_scope"] for row in rows).items())),
        "candidate_module_context_rows": len(candidate),
        "candidate_tier_counts": dict(sorted(Counter(row["evidence_weight_tier"] for row in candidate).items())),
        "module_counts": dict(sorted(Counter(row["module"] for row in candidate).items())),
        "owner_decisions_changed": False,
        "canonical_tf_eligible": False,
        "role_context_separated": True,
        "regulator_role_class_counts": dict(sorted(Counter(row["regulator_role_class"] for row in rows).items())),
        "sci_context_status_counts": dict(sorted(Counter(row["sci_context_status"] for row in rows).items())),
        "materialization_status": "pending_owner_review",
        "policy": [
            "This is a mechanism-scope triage based only on existing reviewed dispositions; it is not a new literature search or module-owner approval.",
            "Direct chromatin/cofactor/RNA-regulatory rows remain module-context candidates pending module-specific SCI context.",
            "Relay, receptor, kinase, protein/PTM, and cytoskeletal rows remain context-only for this regulator group.",
            "Evidence tiers, provenance, owner decision fields, and legacy canonical eligibility are unchanged.",
            "Regulator role class and SCI context status are recorded as separate axes; unresolved SCI context does not make a row noncanonical.",
        ],
        "output": output.name,
    }
    (args.output_dir / "noncanonical_module_context_triage_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
