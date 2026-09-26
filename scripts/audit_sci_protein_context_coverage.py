#!/usr/bin/env python3
"""Audit context completeness and remaining protein curation gaps for the SCI pack.

This is an audit layer, not a mechanism promotion step.  It reads the current
SCI pack and the canonical mSCS flow-protein store, retaining exact study,
timepoint, population, assay, and source identifiers for every gap candidate.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sqlite3
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MSCS_ROOT = ROOT.parent / "mSCS"
DEFAULT_PACK = ROOT / "context_packs" / "spinal_cord_injury"

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from scripts.build_sci_context_pack import is_protein_expression_candidate, nonempty_context, read_tsv

CORE_CONTEXT_FIELDS = [
    "injury_model", "injury_level", "timepoint_value", "timepoint_unit",
    "tissue", "cell_type", "experimental_condition", "study_perturbation_status",
    "sample_scope",
]
SECONDARY_CONTEXT_FIELDS = [
    "injury_severity", "sex", "injury_distance", "injury_distance_unit", "sample_count",
]
GAP_FIELDS = [
    "observation_id", "study_id", "timepoint_id", "population_id", "protein",
    "gene_symbol", "assay", "measurement_kind", "protein_form", "protein_resolution",
    "extraction_status", "evidence_grade", "evidence_status", "post_injury_value",
    "timepoint_unit", "tissue_region", "injury_distance", "injury_distance_unit",
    "condition", "perturbation_status", "injury_model", "injury_severity",
    "injury_level", "sex", "reported_label", "sample_scope", "source_location",
    "source_repository_accession", "gap_reason",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, Any]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: "" if row.get(field) is None else row.get(field, "") for field in fields})


def missing_fields(row: dict[str, str], fields: list[str]) -> list[str]:
    return [field for field in fields if not nonempty_context(row.get(field))]


def context_priority(row: dict[str, Any]) -> str:
    if row["missing_core_fields"]:
        return "high" if int(row["protein_expression_observation_count"]) else "medium"
    if row["missing_secondary_fields"]:
        return "medium"
    return "complete"


def classify_gap(row: dict[str, Any], selected_ids: set[str], imported_ids: set[str]) -> str:
    if row["observation_id"] in imported_ids:
        return "already_imported"
    if row["observation_id"] in selected_ids:
        return "selected_state_record_not_in_current_pack"
    if row.get("extraction_status") not in {"figure_table_transcribed", "source_data_transcribed"}:
        return "source_extraction_not_final"
    if not (
        row.get("value") is not None
        or row.get("transcribed_value_numeric") is not None
        or nonempty_context(row.get("transcribed_value_text"))
        or row.get("direction_vs_control") not in (None, "", "unknown", "not_reported")
    ):
        return "no_measured_value_or_reported_direction"
    assay = (row.get("assay") or "").lower()
    form = (row.get("protein_form") or "").lower()
    measurement = (row.get("measurement_kind") or "").lower()
    if any(token in form for token in ("phosph", "active")):
        return "phospho_or_active_form_review_scope"
    if "ambiguous:" in assay or "reporter" in assay or "reporter" in form:
        return "ambiguous_or_reporter_assay"
    if any(token in assay for token in ("emsa", "enzyme activity", "lipid assay", "zymography")):
        return "activity_or_non_expression_assay"
    if "association" in measurement or "complex" in measurement:
        return "protein_association_not_expression"
    if not is_protein_expression_candidate(row, selected_ids):
        return "outside_current_expression_selection_rule"
    return "candidate_selection_reconciliation_needed"


def build(mscs_root: Path, pack: Path) -> dict[str, Any]:
    protein_db = mscs_root / "data/flow_protein/flow_protein.sqlite"
    phospho_view = mscs_root / "data/derived/phosphorylation_support_observations.tsv"
    if not protein_db.exists() or not phospho_view.exists():
        raise FileNotFoundError("required mSCS protein artifacts are missing")

    contexts = {row["context_id"]: row for row in read_tsv(pack / "contexts.tsv")}
    observations = read_tsv(pack / "observations.tsv")
    protein_observations = [row for row in observations if row["modality"] == "protein"]
    imported_ids = {row["observation_id"] for row in protein_observations}
    selected_ids = {row["observation_id"] for row in read_tsv(phospho_view)}

    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in protein_observations:
        grouped[row["context_id"]].append(row)
    coverage_rows: list[dict[str, Any]] = []
    for context_id, rows in sorted(grouped.items()):
        context = contexts[context_id]
        missing_core = missing_fields(context, CORE_CONTEXT_FIELDS)
        missing_secondary = missing_fields(context, SECONDARY_CONTEXT_FIELDS)
        coverage = {
            "context_id": context_id,
            "study_id": context.get("study_id", ""),
            "injury_model": context.get("injury_model", ""),
            "injury_level": context.get("injury_level", ""),
            "injury_severity": context.get("injury_severity", ""),
            "sex": context.get("sex", ""),
            "timepoint_value": context.get("timepoint_value", ""),
            "timepoint_unit": context.get("timepoint_unit", ""),
            "tissue": context.get("tissue", ""),
            "injury_distance": context.get("injury_distance", ""),
            "injury_distance_unit": context.get("injury_distance_unit", ""),
            "sample_scope": context.get("sample_scope", ""),
            "cell_type": context.get("cell_type", ""),
            "experimental_condition": context.get("experimental_condition", ""),
            "study_perturbation_status": context.get("study_perturbation_status", ""),
            "protein_observation_count": len(rows),
            "protein_state_observation_count": sum(row["measured_entity_type"] != "protein_expression" for row in rows),
            "protein_expression_observation_count": sum(row["measured_entity_type"] == "protein_expression" for row in rows),
            "numeric_observation_count": sum(row["value_kind"] == "numeric" for row in rows),
            "missing_core_fields": ";".join(missing_core),
            "missing_secondary_fields": ";".join(missing_secondary),
        }
        coverage["core_context_completeness"] = f"{len(CORE_CONTEXT_FIELDS) - len(missing_core)}/{len(CORE_CONTEXT_FIELDS)}"
        coverage["secondary_context_completeness"] = f"{len(SECONDARY_CONTEXT_FIELDS) - len(missing_secondary)}/{len(SECONDARY_CONTEXT_FIELDS)}"
        coverage["refinement_priority"] = context_priority(coverage)
        coverage_rows.append(coverage)

    query = """
        SELECT po.*, st.organism, st.injury_model, st.injury_severity, st.injury_level,
               st.sex, st.perturbation_status, tp.post_injury_value,
               tp.unit AS timepoint_unit, tp.condition, tp.tissue_region,
               tp.injury_distance, tp.injury_distance_unit, tp.sample_count,
               cp.reported_label, cp.normalized_label,
               src.source_location, src.repository_accession,
               ec.evidence_status, ec.evidence_id
        FROM protein_observations po
        JOIN studies st USING(study_id)
        JOIN study_timepoints tp USING(timepoint_id)
        JOIN cell_populations cp USING(population_id)
        LEFT JOIN sources src USING(source_id)
        LEFT JOIN evidence_claims ec USING(observation_id)
        ORDER BY po.observation_id
    """
    with sqlite3.connect(protein_db) as db:
        db.row_factory = sqlite3.Row
        canonical = [dict(row) for row in db.execute(query)]

    gap_rows: list[dict[str, Any]] = []
    for row in canonical:
        gap = classify_gap(row, selected_ids, imported_ids)
        if gap == "already_imported":
            continue
        gap_rows.append({field: row.get(field, "") for field in GAP_FIELDS} | {"gap_reason": gap})

    pack.mkdir(parents=True, exist_ok=True)
    coverage_path = pack / "protein_context_coverage.tsv"
    gap_path = pack / "protein_context_gap_candidates.tsv"
    write_tsv(coverage_path, list(coverage_rows[0]) if coverage_rows else [], coverage_rows)
    write_tsv(gap_path, GAP_FIELDS, gap_rows)

    summary = {
        "audit_version": "sci_protein_context_coverage_v1",
        "source_artifact": {
            "path": "mSCS/data/flow_protein/flow_protein.sqlite",
            "sha256": sha256(protein_db),
            "size_bytes": protein_db.stat().st_size,
        },
        "pack_inputs": {
            "protein_observations": len(protein_observations),
            "protein_context_profiles": len(coverage_rows),
            "protein_expression_observations": sum(int(row["protein_expression_observation_count"]) for row in coverage_rows),
            "protein_state_observations": sum(int(row["protein_state_observation_count"]) for row in coverage_rows),
        },
        "context_completeness": {
            "by_refinement_priority": dict(sorted(Counter(row["refinement_priority"] for row in coverage_rows).items())),
            "by_core_completeness": dict(sorted(Counter(row["core_context_completeness"] for row in coverage_rows).items())),
            "by_secondary_completeness": dict(sorted(Counter(row["secondary_context_completeness"] for row in coverage_rows).items())),
        },
        "canonical_store": {
            "protein_observations": len(canonical),
            "imported_observations": len(imported_ids),
            "remaining_gap_records": len(gap_rows),
            "gap_records_by_reason": dict(sorted(Counter(row["gap_reason"] for row in gap_rows).items())),
        },
        "priority_contexts": [
            {
                "context_id": row["context_id"],
                "study_id": row["study_id"],
                "protein_observation_count": row["protein_observation_count"],
                "missing_core_fields": row["missing_core_fields"],
                "missing_secondary_fields": row["missing_secondary_fields"],
                "refinement_priority": row["refinement_priority"],
            }
            for row in sorted(
                coverage_rows,
                key=lambda row: ({"high": 0, "medium": 1, "complete": 2}[row["refinement_priority"]], -int(row["protein_observation_count"]), row["context_id"]),
            )[:50]
        ],
        "artifacts": {
            "coverage_tsv": coverage_path.name,
            "gap_candidates_tsv": gap_path.name,
        },
        "policy": "This audit prioritizes metadata refinement only. It does not assign numeric confidence, create graph edges, or promote unresolved mechanism mappings.",
    }
    report_path = pack / "protein_context_gap_audit.json"
    report_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mscs-root", type=Path, default=DEFAULT_MSCS_ROOT)
    parser.add_argument("--pack", type=Path, default=DEFAULT_PACK)
    args = parser.parse_args()
    summary = build(args.mscs_root, args.pack)
    print(json.dumps(summary["canonical_store"] | summary["pack_inputs"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
