#!/usr/bin/env python3
"""Build an auditable public-TF evidence layer and validated-edge subset.

The public-TF staging packet contains heterogeneous evidence classes. This
builder exports every reviewed relationship as a release layer while allowing
only an explicit, manually adjudicated subset to be marked as a validated
mechanism-edge candidate. It never promotes rows based on evidence tier alone.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = (
    ROOT
    / "data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1"
    / "module_integration_staging_v1"
)
DEFAULT_OUTPUT = ROOT / "data/processed/public_tf_mechanism_layer_v2026_08_30"

LAYER_FIELDS = [
    "layer_record_id", "layer_membership", "traversal_status", "decision_id",
    "integration_id", "promotion_id", "module", "module_route", "queue_key",
    "regulator_symbol", "raw_tf_symbol", "target_symbol", "species_scope",
    "target_graph_modules", "promotion_class", "promotion_confidence",
    "evidence_confidence_tier", "evidence_weight_tier", "evidence_weight_rank",
    "evidence_tier_basis", "independent_literature_support_status",
    "independent_literature_source_count", "exact_pair_status", "effect_polarity",
    "binding_or_association_status", "downstream_expression_or_perturbation_status",
    "downstream_activation_status", "upstream_relay_status", "primary_citation",
    "corroborating_citation", "additional_corroborating_citation",
    "primary_and_corroborating_citations", "source_registry", "source_record_id",
    "source_registries", "source_record_ids", "tflink_source_database",
    "tflink_detection_method", "tflink_pubmed_id", "tflink_source_url",
    "tflink_raw_snapshot_path", "tflink_raw_snapshot_sha256", "source_review_file",
    "review_notes", "near_match_exclusions", "source_exportable", "module_stage_status",
    "module_materialization_allowed", "screening_decision", "module_owner_review_status",
    "materialization_status", "regulator_role_class", "canonical_role_status",
    "sci_context_status", "materialization_lane", "mechanism_evidence_type",
    "mechanism_evidence_definition", "context_level_regulator", "context_level_target",
    "context_level_exact_pair", "context_evidence_scope", "context_evidence_basis",
    "context_promotion_lane", "candidate_for_later_materialization",
    "canonical_materialization_allowed", "decision_basis",
]

ADJUDICATION_FIELDS = [
    "decision_id", "review_decision", "validated_relation_type",
    "validated_effect_polarity", "validation_scope", "validation_basis", "limitations",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--adjudications",
        type=Path,
        default=DEFAULT_INPUT / "public_tf_validated_edge_adjudications.tsv",
    )
    return parser.parse_args()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fieldnames,
            delimiter="\t",
            lineterminator="\n",
            extrasaction="ignore",
        )
        writer.writeheader()
        writer.writerows(rows)


def load_source_rows(input_dir: Path) -> dict[str, dict[str, str]]:
    source_rows: dict[str, dict[str, str]] = {}
    paths = sorted(input_dir.glob("module_*_evidence_staging.tsv"))
    paths.append(input_dir / "catalog_only_evidence.tsv")
    for path in paths:
        if not path.exists():
            continue
        for row in read_tsv(path):
            key = row.get("integration_id", "")
            if not key:
                raise ValueError(f"source row has no integration_id: {path}")
            if key in source_rows:
                raise ValueError(f"duplicate integration_id across staging files: {key}")
            source_rows[key] = row
    if not source_rows:
        raise ValueError(f"no public-TF staging rows found under {input_dir}")
    return source_rows


def strict_gate(row: dict[str, str], source: dict[str, str]) -> tuple[bool, str]:
    requirements = [
        (row.get("evidence_weight_tier", "").startswith(("A_", "B_")), "A/B evidence tier"),
        (row.get("source_exportable") == "true", "exportable source"),
        (row.get("module") != "catalog_only", "explicit module route"),
        (row.get("target_graph_modules", "") != "", "target graph module assignment"),
        (row.get("canonical_role_status") == "canonical_tf", "canonical TF role"),
        (
            row.get("mechanism_evidence_type") == "direct_sequence_specific_tf_binding",
            "direct sequence-specific binding evidence type",
        ),
        (row.get("context_evidence_scope") == "exact_pair", "exact-pair context scope"),
        (source.get("binding_or_association_status", "") != "", "binding/association record"),
    ]
    for passed, label in requirements:
        if not passed:
            return False, label
    return True, "all explicit validated-edge gate fields satisfied"


def main() -> int:
    args = parse_args()
    input_dir = args.input_dir.resolve()
    output_dir = args.output_dir.resolve()
    decisions_path = input_dir / "module_screening_decisions.tsv"
    if not decisions_path.exists():
        raise SystemExit(f"missing screening decisions: {decisions_path}")
    source_rows = load_source_rows(input_dir)
    decisions = read_tsv(decisions_path)
    decision_by_id = {row["decision_id"]: row for row in decisions}
    if len(decision_by_id) != len(decisions):
        raise SystemExit("duplicate decision_id in module_screening_decisions.tsv")

    adjudications = read_tsv(args.adjudications.resolve())
    adjudication_by_id: dict[str, dict[str, str]] = {}
    for row in adjudications:
        decision_id = row.get("decision_id", "")
        if not decision_id or decision_id in adjudication_by_id:
            raise SystemExit(f"invalid or duplicate adjudication decision_id: {decision_id}")
        if decision_id not in decision_by_id:
            raise SystemExit(f"adjudication decision_id not found in staging: {decision_id}")
        if row.get("review_decision") != "validated_general_mechanism_edge":
            raise SystemExit(f"unsupported review_decision for {decision_id}")
        adjudication_by_id[decision_id] = row

    validated_rows: list[dict[str, str]] = []
    layer_rows: list[dict[str, str]] = []
    gate_reasons: Counter[str] = Counter()
    for decision in decisions:
        integration_id = decision.get("integration_id", "")
        source = source_rows.get(integration_id)
        if source is None:
            raise SystemExit(f"decision has no source staging row: {integration_id}")
        adjudication = adjudication_by_id.get(decision["decision_id"])
        if adjudication:
            passed, reason = strict_gate(decision, source)
            if not passed:
                raise SystemExit(f"validated adjudication failed gate ({decision['decision_id']}): {reason}")
            gate_reasons[reason] += 1
            membership = "validated_mechanism_edge"
            traversal = "validated_edge_candidate"
            validated = dict(decision)
            validated.update(source)
            validated.update(adjudication)
            validated["layer_record_id"] = decision["decision_id"]
            validated["layer_membership"] = membership
            validated["traversal_status"] = traversal
            validated_rows.append(validated)
        else:
            membership = "evidence_candidate"
            traversal = "not_traversable"
            gate_reasons["not manually adjudicated"] += 1
        combined = dict(source)
        combined.update(decision)
        combined["layer_record_id"] = decision["decision_id"]
        combined["layer_membership"] = membership
        combined["traversal_status"] = traversal
        layer_rows.append(combined)

    layer_rows.sort(key=lambda row: row["layer_record_id"])
    validated_rows.sort(key=lambda row: row["layer_record_id"])
    write_tsv(output_dir / "public_tf_candidate_layer.tsv", LAYER_FIELDS, layer_rows)
    write_tsv(
        output_dir / "public_tf_validated_edge_layer.tsv",
        LAYER_FIELDS + ADJUDICATION_FIELDS[1:],
        validated_rows,
    )

    metadata = {
        "layer_name": "public_tf_mechanism_evidence_layer",
        "release_status": "candidate_overlay_with_explicit_validated_edge_subset",
        "source_scope": "reviewed public-TF module-screening staging packet",
        "input_decision_rows": len(decisions),
        "candidate_rows": len(layer_rows),
        "validated_edge_candidate_rows": len(validated_rows),
        "validated_edge_candidate_unique_pairs": len({
            (r["regulator_symbol"], r["target_symbol"], r["species_scope"])
            for r in validated_rows
        }),
        "validated_edge_candidate_module_rows_by_module": dict(
            sorted(Counter(r["module"] for r in validated_rows).items())
        ),
        "candidate_rows_by_evidence_tier": dict(
            sorted(Counter(r["evidence_weight_tier"] for r in layer_rows).items())
        ),
        "candidate_rows_by_layer_membership": dict(
            sorted(Counter(r["layer_membership"] for r in layer_rows).items())
        ),
        "validated_edge_gate": [
            "A- or B-tier reviewed evidence",
            "source_exportable=true",
            "explicit target_graph_modules assignment",
            "canonical_role_status=canonical_tf",
            "mechanism_evidence_type=direct_sequence_specific_tf_binding",
            "context_evidence_scope=exact_pair",
            "manual literature adjudication with citations and limitations",
        ],
        "policy": [
            "All reviewed rows are retained in the candidate layer regardless of tier.",
            "D/E and unresolved rows remain non-traversable and retain their original evidence fields.",
            "Evidence tier and context level remain independent axes.",
            "No row is promoted by tier alone; validated rows require explicit adjudication.",
            "The validated subset is a release candidate and does not itself perform database writes.",
        ],
        "outputs": [
            "public_tf_candidate_layer.tsv",
            "public_tf_validated_edge_layer.tsv",
            "layer_metadata.json",
        ],
    }
    (output_dir / "layer_metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(metadata, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
