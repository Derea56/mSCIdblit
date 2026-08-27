#!/usr/bin/env python3
"""Merge the bounded Batch 002 evidence lanes into one audit register."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIR = ROOT / (
    "data/processed/public_tf_union_expansion_v1/"
    "current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_002"
)

PAIR_FIELDS = [
    "review_id", "batch_id", "batch_rank", "regulator_key", "regulator_symbol",
    "species_scope", "source_registry", "source_record_id", "raw_tf_symbol",
    "target_symbol", "target_graph_modules", "candidate_membership_status",
    "exact_pair_search_url", "exact_pair_status", "regulator_general_evidence_status",
    "target_cell_presence_status", "binding_or_association_status",
    "downstream_expression_or_perturbation_status", "downstream_activation_status",
    "upstream_relay_status", "disposition", "primary_citation",
    "corroborating_citation", "near_match_exclusions", "review_notes", "exportable",
    "canonical_write_performed",
]

EVIDENCE_FIELDS = [
    "evidence_id", "regulator_key", "regulator_symbol", "species_scope", "evidence_layer",
    "support_kind", "cell_or_model", "assay_or_perturbation", "observation",
    "effect_direction", "primary_citation", "corroborating_citation",
    "route_or_module_relevance", "target_pair_scope", "exportable",
    "canonical_write_performed", "limitations",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_DIR)
    args = parser.parse_args()
    input_dir = args.input_dir.resolve()
    pair_paths = [
        input_dir / "public_tf_evidence_review_batch002_ranks0015_pairs.tsv",
        input_dir / "public_tf_evidence_review_batch002_ranks16_20.tsv",
        input_dir / "public_tf_evidence_review_batch002_ranks2125_pairs.tsv",
    ]
    register_paths = [
        input_dir / "public_tf_evidence_review_batch002_ranks0015_regulator_register.tsv",
        input_dir / "public_tf_evidence_review_batch002_ranks16_20_regulator_register.tsv",
        input_dir / "public_tf_evidence_review_batch002_ranks2125_regulator_register.tsv",
    ]
    pairs = [row for path in pair_paths for row in read_tsv(path)]
    evidence = [row for path in register_paths for row in read_tsv(path)]
    if len(pairs) != 100:
        raise SystemExit(f"expected 100 pair rows, found {len(pairs)}")
    pair_keys = {(row["regulator_key"], row["target_symbol"], row["species_scope"], row["source_record_id"]) for row in pairs}
    if len(pair_keys) != 100:
        raise SystemExit(f"expected 100 unique provenance-aware pairs, found {len(pair_keys)}")
    ranks = {int(row["batch_rank"]) for row in pairs}
    if ranks != set(range(1, 26)):
        raise SystemExit(f"unexpected batch ranks: {sorted(ranks)}")
    if any(row.get("exportable", "").lower() != "false" or row.get("canonical_write_performed", "").lower() != "false" for row in pairs):
        raise SystemExit("promotion/write guard failed in pair rows")
    if any(row.get("exportable", "").lower() != "false" or row.get("canonical_write_performed", "").lower() != "false" for row in evidence):
        raise SystemExit("promotion/write guard failed in regulator register")

    pair_path = input_dir / "public_tf_evidence_review_batch002_pairs.tsv"
    register_path = input_dir / "public_tf_evidence_review_batch002_regulator_register.tsv"
    summary_path = input_dir / "batch_002_evidence_review_summary.json"
    report_path = input_dir / "EVIDENCE_REVIEW_BATCH002.md"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    exact_status_counts: dict[str, int] = {}
    for row in pairs:
        exact_status_counts[row["exact_pair_status"]] = exact_status_counts.get(row["exact_pair_status"], 0) + 1
    general_status_counts: dict[str, int] = {}
    for row in evidence:
        general_status_counts[row["support_kind"]] = general_status_counts.get(row["support_kind"], 0) + 1
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_002",
        "source_set_ranks_reviewed": list(range(1, 26)), "pair_rows_reviewed": len(pairs),
        "unique_regulators_reviewed": len({row["regulator_key"] for row in pairs}),
        "unique_provenance_aware_pairs": len(pair_keys), "exact_pair_status_counts": exact_status_counts,
        "regulator_register_rows": len(evidence), "regulator_support_kind_counts": general_status_counts,
        "exact_pair_support_rows": sum(row["exact_pair_status"] in {"supported", "supported_exact_pair"} for row in pairs),
        "partial_or_near_match_rows": sum(row["exact_pair_status"] not in {"no_exact_pair_support_found_in_bounded_search"} for row in pairs),
        "exportable_pair_rows": sum(row["exportable"].lower() == "true" for row in pairs),
        "canonical_writes_performed": False, "module22b_promotions_performed": False,
        "provenance_preserved": True,
        "limitations": [
            "No-exact-support is bounded to the PubMed/PMC searches recorded in each lane; it is not a global absence claim.",
            "Regulator-level evidence for different targets is retained separately and is not attached to queued pairs.",
            "Target-cell presence, downstream activation, and upstream relay remain unestablished for all queued exact pairs.",
        ],
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path.write_text(
        "# Evidence review: public TF batch 002\n\n"
        "Reviewed all 25 selected TFLink source sets and 100 exact regulator-target-species pairs.\n\n"
        f"- **{len(pairs)} / 100** pairs were reviewed.\n"
        f"- **{summary['exact_pair_support_rows']}** exact pairs met the promotion threshold.\n"
        f"- **{summary['partial_or_near_match_rows']}** pairs were partial or near matches.\n"
        f"- **{len(evidence)}** regulator-level records were retained separately.\n"
        "- **0** rows are exportable; no canonical or Module 22B writes were performed.\n\n"
        "The regulator register contains real literature on several regulators at other targets, including ASCL2, OSR2, ZBTB6, CASZ1, TCF7L1, and ZNF644. Those observations were not transferred to the queued edges. Database membership, co-expression, annotation, motif-only predictions, cross-species observations, and target-only papers were excluded from promotion.\n\n"
        "`no_exact_pair_support_found_in_bounded_search` is a bounded-search result, not a claim that no evidence exists anywhere.\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
