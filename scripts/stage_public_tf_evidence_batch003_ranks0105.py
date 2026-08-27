#!/usr/bin/env python3
"""Stage conservative evidence findings for public-TF batch 003 ranks 1-5.

This lane records the agent's bounded alias-aware PubMed/PMC review.  The
single contextual ZNF750/ADAM10 co-mention is retained as a non-promotable
near match; database membership and co-occurrence are never exported as a
Module 22B edge.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/"
    "current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_003/"
    "public_tf_evidence_collection_batch_003.tsv"
)

PAIR_FIELDS = [
    "review_id", "batch_id", "batch_rank", "regulator_key", "regulator_symbol", "species_scope",
    "source_registry", "source_record_id", "raw_tf_symbol", "target_symbol", "target_graph_modules",
    "candidate_membership_status", "exact_pair_search_url", "exact_pair_status",
    "regulator_general_evidence_status", "target_cell_presence_status", "binding_or_association_status",
    "downstream_expression_or_perturbation_status", "downstream_activation_status", "upstream_relay_status",
    "disposition", "primary_citation", "corroborating_citation", "near_match_exclusions", "review_notes",
    "exportable", "canonical_write_performed",
]
EVIDENCE_FIELDS = [
    "evidence_id", "regulator_key", "regulator_symbol", "species_scope", "evidence_layer", "support_kind",
    "cell_or_model", "assay_or_perturbation", "observation", "effect_direction", "primary_citation",
    "corroborating_citation", "route_or_module_relevance", "target_pair_scope", "exportable",
    "canonical_write_performed", "limitations",
]

# symbol, species, primary, corroboration, model, assay, observation, exclusions
REGULATORS = {
    "znf652": (
        "ZNF652", "human", "https://www.sciencedirect.com/science/article/pii/S0021925820815026",
        "https://pubmed.ncbi.nlm.nih.gov/39500884/", "human promoter and perturbation models",
        "promoter binding/reporter, knockdown, overexpression, and rescue assays",
        "ZNF652 has regulator-level evidence at non-queued genes including TCF12/HEB and CCND3, but no queued A2M/ADAM10/ADAM22/ADGRB3 relationship was found.",
        "Disease-association co-mentions and queued-target co-occurrence were excluded; no queued-locus occupancy or perturbation was shown.",
    ),
    "hoxc5": (
        "HOXC5", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5758779/", "",
        "human cancer regulatory model", "ChIP-seq occupancy, perturbation, and long-range enhancer assays",
        "HOXC5 has regulator-level evidence at a distal hTERT enhancer, but no queued ADAM22/ADAM9/ADGRB3/ADGRL2 relationship was found.",
        "The hTERT enhancer result was not transferred to queued targets; target-only studies and expression co-listings were excluded.",
    ),
    "zkscan8": (
        "ZKSCAN8", "human", "", "", "human annotation and transcriptomic resources",
        "no qualifying primary target-gene assay located",
        "No qualifying primary paper with a validated non-queued ZKSCAN8 target was located in the bounded search, and no queued A2M/ACKR2/ACVR1/ADAM10 relationship was found.",
        "ZKSCAN3/ZKSCAN7 paralog evidence, annotation, and high-throughput co-occurrence were excluded.",
    ),
    "znf750": (
        "ZNF750", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3306457/",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC5415641/", "human epidermal/skin epithelial models",
        "promoter occupancy, depletion/overexpression, reporter, and functional assays",
        "ZNF750 has direct regulator-level evidence at non-queued genes including KLF4 and LAMC2, but no queued ACKR2/ACKR3/ACTR2 relationship was found.",
        "The contextual ZNF750/ADAM10 co-mention was retained as a near match only: no ZNF750 occupancy, perturbation, or reporter evidence at ADAM10 was shown.",
    ),
    "znf398": (
        "ZNF398", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7217929/", "",
        "human TGF-beta/epithelial regulatory models", "co-occupancy with SMAD3, perturbation, and functional expression assays",
        "ZNF398 has regulator-level evidence at non-queued TGF-beta targets including LEFTY1, LIN28B, and ESRP1, but no queued ACKR3/ACVR1/ADAM10/ADAM22 relationship was found.",
        "Co-occupancy and expression effects at non-queued genes were not transferred to queued targets; no queued-locus occupancy or perturbation was shown.",
    ),
}

NEAR_MATCH_URL = "https://www.sciencedirect.com/science/article/pii/S0022202X2601167X"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


def search_url(regulator: str, target: str, species: str) -> str:
    return "https://pubmed.ncbi.nlm.nih.gov/?term=" + quote_plus(f'"{regulator}" AND "{target}" AND {species}')


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_BATCH.parent)
    args = parser.parse_args()
    rows = [row for row in read_tsv(args.batch) if 1 <= int(row["batch_rank"]) <= 5]
    if len(rows) != 20:
        raise SystemExit(f"expected 20 rows for ranks 1-5, found {len(rows)}")

    pairs: list[dict[str, str]] = []
    evidence: list[dict[str, str]] = []
    seen_keys: set[str] = set()
    for i, row in enumerate(rows, 1):
        key = row["regulator_key"]
        if key not in REGULATORS:
            raise SystemExit(f"missing evidence map for {key}")
        symbol, species, primary, corr, model, assay, observation, exclusions = REGULATORS[key]
        is_near_match = key == "znf750" and row["target_symbol"] == "ADAM10"
        pair_exclusions = exclusions
        if is_near_match:
            pair_exclusions = f"{NEAR_MATCH_URL} — contextual co-mention only; no ZNF750 occupancy, perturbation, or reporter evidence at ADAM10."
        pairs.append({
            "review_id": f"public_tf_evidence_batch003_pair_{int(row['batch_rank']):02d}_{i:02d}",
            "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key,
            "regulator_symbol": symbol, "species_scope": row["species_scope"], "source_registry": row["source_registry"],
            "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"],
            "target_symbol": row["target_symbol"], "target_graph_modules": row["target_graph_modules"],
            "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": search_url(symbol, row["target_symbol"], row["species_scope"]),
            "exact_pair_status": "contextual_co-mention_only_not_promotable" if is_near_match else "no_exact_pair_support_found_in_bounded_search",
            "regulator_general_evidence_status": "supported_general_regulator_evidence" if primary else "not_found_in_bounded_search",
            "target_cell_presence_status": "not_established_for_exact_pair", "binding_or_association_status": "not_found_for_exact_pair",
            "downstream_expression_or_perturbation_status": "not_found_for_exact_pair", "downstream_activation_status": "not_assessed",
            "upstream_relay_status": "not_tested_for_exact_pair", "disposition": "retain_database_candidate_as_search_lead_only",
            "primary_citation": "", "corroborating_citation": "", "near_match_exclusions": pair_exclusions,
            "review_notes": "Regulator-level references are stored separately; they are not evidence for this exact queued pair. " + observation,
            "exportable": "false", "canonical_write_performed": "false",
        })
        if key not in seen_keys:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch003_regulator_{key}", "regulator_key": key,
                "regulator_symbol": symbol, "species_scope": species, "evidence_layer": "regulator_identity_and_regulatory_capacity",
                "support_kind": "primary_literature_regulator_level" if primary else "no_qualifying_primary_regulator_evidence_located",
                "cell_or_model": model, "assay_or_perturbation": assay, "observation": observation,
                "effect_direction": "queued-pair direction not established", "primary_citation": primary,
                "corroborating_citation": corr, "route_or_module_relevance": "regulator-level evidence only",
                "target_pair_scope": "not evidence for queued exact pairs; no Module 22B edge or upstream relay inferred",
                "exportable": "false", "canonical_write_performed": "false",
                "limitations": "Regulator-level evidence does not establish the queued target relationship, target-cell presence in SCI, downstream activation, or upstream relay.",
            })
        seen_keys.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch003_ranks0105_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch003_ranks0105_regulator_register.tsv"
    summary_path = args.output_dir / "batch_003_ranks0105_evidence_review_summary.json"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_003", "source_set_ranks_reviewed": list(range(1, 6)),
        "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen_keys),
        "exact_pair_support_rows": 0, "partial_or_near_match_rows": sum(row["exact_pair_status"] != "no_exact_pair_support_found_in_bounded_search" for row in pairs),
        "general_regulator_evidence_rows": len(evidence), "exportable_pair_rows": 0,
        "canonical_writes_performed": False, "module22b_promotions_performed": False, "provenance_preserved": True,
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
        "decision": "Retain all 20 pairs as database-attributed search leads; the one contextual ZNF750/ADAM10 co-mention is not promotable and no exact pair met the promotion threshold.",
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
