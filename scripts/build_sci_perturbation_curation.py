#!/usr/bin/env python3
"""Build a staged, source-preserving SCI perturbation-design curation ledger.

The ledger is deliberately separate from contexts.tsv and observations.tsv.
It normalizes only the design class exposed by the existing audit and carries
the exact source text, context fields, artifact checksums, and locators needed
for later source review. It does not create evidence, infer causal responses,
or promote any mechanism mapping.
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PACK = ROOT / "context_packs" / "spinal_cord_injury"
DEFAULT_AUDIT = DEFAULT_PACK / "perturbation_design_audit.tsv"
DEFAULT_OUTPUT = DEFAULT_PACK / "perturbation_design_curation.tsv"

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.build_sci_context_pack import read_tsv

INTERVENTION_CLASSES = {
    "explicit_intervention",
    "explicit_intervention_with_comparator_design",
}

OUTPUT_FIELDS = [
    "context_id",
    "study_id",
    "observation_ids",
    "source_record_keys",
    "modality",
    "dependency_group_count",
    "audit_classification",
    "intervention_class",
    "comparator_class",
    "normalization_status",
    "review_required",
    "perturbation_source_text",
    "treatment_source_text",
    "study_perturbation_status_source_text",
    "experimental_condition_source_text",
    "species",
    "injury_model",
    "injury_level",
    "injury_severity",
    "timepoint_value",
    "timepoint_unit",
    "tissue",
    "cell_type",
    "sample_scope",
    "sample_count",
    "match_fields_present",
    "match_fields_missing",
    "source_artifact_paths",
    "source_artifact_sha256s",
    "source_locators",
    "evidence_roles",
    "observation_statuses",
    "link_statuses",
    "normalization_note",
]


def read_input(path: Path) -> list[dict[str, str]]:
    rows = read_tsv(path)
    missing = {"context_id", "audit_classification", "classification_signals"} - set(rows[0] if rows else ())
    if missing:
        raise ValueError(f"audit input is missing fields: {', '.join(sorted(missing))}")
    return rows


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def intervention_class(signals: str) -> str:
    signal_set = set(filter(None, signals.split(";")))
    genetic = bool(signal_set & {"genetic_or_cellular_perturbation", "expression_or_vector_perturbation"})
    pharmacologic = bool(signal_set & {"drug_or_antibody_intervention", "protein_or_ligand_treatment", "added_agent"})
    physical = "physical_or_behavioral_intervention" in signal_set
    classes = sum((genetic, pharmacologic, physical))
    if classes > 1:
        return "mixed_intervention_classes"
    if genetic:
        return "genetic_or_expression_intervention"
    if pharmacologic:
        return "pharmacologic_or_ligand_intervention"
    if physical:
        return "physical_or_behavioral_intervention"
    return "intervention_class_requires_source_review"


def comparator_class(audit_classification: str, signals: str) -> str:
    signal_set = set(filter(None, signals.split(";")))
    comparator_signals = {
        "arm_comparison",
        "control_or_reference_comparison",
        "genotype_or_line_comparison",
        "injury_severity_comparison",
    }
    if audit_classification == "explicit_intervention_with_comparator_design" or signal_set & comparator_signals:
        return "comparator_present_in_source_design_text"
    return "comparator_not_detected_in_audit_text"


def build(
    audit_path: Path = DEFAULT_AUDIT,
    output_path: Path = DEFAULT_OUTPUT,
    contexts_path: Path | None = None,
) -> dict[str, Any]:
    audit_path = audit_path.resolve()
    output_path = output_path.resolve()
    contexts_path = (contexts_path or audit_path.parent / "contexts.tsv").resolve()
    rows = read_input(audit_path)
    contexts = {row["context_id"]: row for row in read_tsv(contexts_path)}
    selected = [row for row in rows if row["audit_classification"] in INTERVENTION_CLASSES]
    selected.sort(key=lambda row: row["context_id"])

    output_rows: list[dict[str, Any]] = []
    for row in selected:
        context = contexts.get(row["context_id"])
        if context is None:
            raise ValueError(f"audit context is missing from context profiles: {row['context_id']}")
        output_rows.append({
            "context_id": row["context_id"],
            "study_id": row["study_id"],
            "observation_ids": row["observation_ids"],
            "source_record_keys": row["source_record_keys"],
            "modality": row["modality"],
            "dependency_group_count": row["dependency_group_count"],
            "audit_classification": row["audit_classification"],
            "intervention_class": intervention_class(row["classification_signals"]),
            "comparator_class": comparator_class(row["audit_classification"], row["classification_signals"]),
            "normalization_status": "staged_not_promoted",
            "review_required": "true",
            "perturbation_source_text": row["perturbation_source_text"],
            "treatment_source_text": row["treatment_source_text"],
            "study_perturbation_status_source_text": row["study_perturbation_status_source_text"],
            "experimental_condition_source_text": row["experimental_condition_source_text"],
            "species": row["species"],
            "injury_model": row["injury_model"],
            "injury_level": row["injury_level"],
            "injury_severity": row["injury_severity"],
            "timepoint_value": context.get("timepoint_value", ""),
            "timepoint_unit": context.get("timepoint_unit", ""),
            "tissue": row["tissue"],
            "cell_type": row["cell_type"],
            "sample_scope": row["sample_scope"],
            "sample_count": context.get("sample_count", ""),
            "match_fields_present": row["match_fields_present"],
            "match_fields_missing": row["match_fields_missing"],
            "source_artifact_paths": row["source_artifact_paths"],
            "source_artifact_sha256s": row["source_artifact_sha256s"],
            "source_locators": row["source_locators"],
            "evidence_roles": row["evidence_roles"],
            "observation_statuses": row["observation_statuses"],
            "link_statuses": row["link_statuses"],
            "normalization_note": (
                "Controlled class is derived from the perturbation-design audit. "
                "Raw source fields are preserved; intervention target, route, dose, "
                "duration, and comparator labels require source review before promotion. "
                "This row is not a new observation or causal claim."
            ),
        })

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)

    return {
        "input": display_path(audit_path),
        "context_profiles": display_path(contexts_path),
        "output": display_path(output_path),
        "rows": len(output_rows),
        "by_intervention_class": dict(sorted(Counter(row["intervention_class"] for row in output_rows).items())),
        "by_comparator_class": dict(sorted(Counter(row["comparator_class"] for row in output_rows).items())),
        "normalization_status": "staged_not_promoted",
        "policy": "Source text and provenance are preserved; no evidence rows, graph links, route confidence, or numeric modality weights are created.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audit", type=Path, default=DEFAULT_AUDIT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    print(build(args.audit, args.output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
