#!/usr/bin/env python3
"""Stage conservative evidence findings for public-TF batch 003 ranks 6-10."""

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
    "candidate_membership_status", "exact_pair_search_url", "exact_pair_status", "regulator_general_evidence_status",
    "target_cell_presence_status", "binding_or_association_status", "downstream_expression_or_perturbation_status",
    "downstream_activation_status", "upstream_relay_status", "disposition", "primary_citation",
    "corroborating_citation", "near_match_exclusions", "review_notes", "exportable", "canonical_write_performed",
]
EVIDENCE_FIELDS = [
    "evidence_id", "regulator_key", "regulator_symbol", "species_scope", "evidence_layer", "support_kind",
    "cell_or_model", "assay_or_perturbation", "observation", "effect_direction", "primary_citation",
    "corroborating_citation", "route_or_module_relevance", "target_pair_scope", "exportable",
    "canonical_write_performed", "limitations",
]

# symbol, species, primary, corroboration, model, assay, observation, exclusions
REGULATORS = {
    "znf449": (
        "ZNF449", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11937480/", "",
        "human colorectal-cancer cells", "interaction, perturbation, and promoter-reporter assays",
        "ZNF449 has regulator-level transcriptional evidence at non-queued genes, including a promoter-reporter context, but no queued A2M/ADA/ADAM10/ADAM22 relationship was found.",
        "Target-only studies and ZNF449 co-occurrence with queued genes were excluded; no queued locus occupancy or perturbation was shown.",
    ),
    "zbtb8a": (
        "ZBTB8A", "human", "", "",
        "human annotation and interaction resources", "no qualifying primary target-gene assay located",
        "No qualifying primary regulator-level mechanistic paper was located in the bounded search, and no queued ACVR1C/ADA/ADAM22/ADGRL1 relationship was found.",
        "GO/annotation records and database interactions were not counted as primary regulator evidence.",
    ),
    "zbtb25": (
        "ZBTB25", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5625503/", "",
        "human protein/RNA-binding and viral transcription model", "RNA/protein pulldown and functional viral transcription assays",
        "ZBTB25 has limited regulator/cofactor evidence in a viral RNA-transcription model, but no queued A2M/ABCA1/ACKR2/ACVR1 target relationship was found.",
        "Viral RNA binding, annotation, and co-expression were not treated as evidence for the queued host-gene edges.",
    ),
    "rbak": (
        "RBAK", "human", "https://pubmed.ncbi.nlm.nih.gov/10702291/", "https://pubmed.ncbi.nlm.nih.gov/14664718/",
        "human fibroblast and prostate/androgen-receptor models", "promoter repression and ligand-dependent protein interaction assays",
        "RBAK has direct transcriptional-regulator evidence involving E2F and androgen-receptor regulation, but no queued ADAM22/ADGRE5/ADIPOR2/ADO relationship was found.",
        "Androgen-receptor/E2F regulation and queued-target co-occurrence were not transferred to the queued target edges.",
    ),
    "tead3": (
        "TEAD3", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7483246/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2492741/",
        "human epidermal and mammary epithelial models", "TEAD-family knockdown, ChIP/ChIP-on-chip, and direct-target expression assays",
        "TEAD3 has regulator-level evidence in YAP/TEAD transcriptional programs and epithelial direct-target assays, but no queued A2M/ACTR2/ACVR1/ADA relationship was found.",
        "TEAD-family or YAP target evidence at other genes was not transferred to queued targets; no queued-locus peak was verified.",
    ),
}


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
    rows = [row for row in read_tsv(args.batch) if 6 <= int(row["batch_rank"]) <= 10]
    if len(rows) != 20:
        raise SystemExit(f"expected 20 rows for ranks 6-10, found {len(rows)}")
    pairs: list[dict[str, str]] = []
    evidence: list[dict[str, str]] = []
    seen: set[str] = set()
    for i, row in enumerate(rows, 1):
        key = row["regulator_key"]
        if key not in REGULATORS:
            raise SystemExit(f"missing evidence map for {key}")
        symbol, species, primary, corr, model, assay, observation, exclusions = REGULATORS[key]
        pairs.append({
            "review_id": f"public_tf_evidence_batch003_pair_{int(row['batch_rank']):02d}_{i:02d}",
            "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key,
            "regulator_symbol": symbol, "species_scope": row["species_scope"], "source_registry": row["source_registry"],
            "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"],
            "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": search_url(symbol, row["target_symbol"], row["species_scope"]),
            "exact_pair_status": "no_exact_pair_support_found_in_bounded_search",
            "regulator_general_evidence_status": "supported_general_regulator_evidence" if primary else "not_found_in_bounded_search",
            "target_cell_presence_status": "not_established_for_exact_pair", "binding_or_association_status": "not_found_for_exact_pair",
            "downstream_expression_or_perturbation_status": "not_found_for_exact_pair", "downstream_activation_status": "not_assessed",
            "upstream_relay_status": "not_tested_for_exact_pair", "disposition": "retain_database_candidate_as_search_lead_only",
            "primary_citation": "", "corroborating_citation": "", "near_match_exclusions": exclusions,
            "review_notes": "Regulator-level references are stored separately; they are not evidence for this exact queued pair. " + observation,
            "exportable": "false", "canonical_write_performed": "false",
        })
        if key not in seen and primary:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch003_regulator_{key}", "regulator_key": key,
                "regulator_symbol": symbol, "species_scope": species, "evidence_layer": "regulator_identity_and_regulatory_capacity",
                "support_kind": "primary_literature_regulator_level", "cell_or_model": model, "assay_or_perturbation": assay,
                "observation": observation, "effect_direction": "queued-pair direction not established", "primary_citation": primary,
                "corroborating_citation": corr, "route_or_module_relevance": "regulator-level evidence only",
                "target_pair_scope": "not evidence for queued exact pairs; no Module 22B edge or upstream relay inferred",
                "exportable": "false", "canonical_write_performed": "false",
                "limitations": "Regulator-level evidence does not establish the queued target relationship, target-cell presence in SCI, downstream activation, or upstream relay.",
            })
        seen.add(key)
    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch003_ranks0610_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch003_ranks0610_regulator_register.tsv"
    summary_path = args.output_dir / "batch_003_ranks0610_evidence_review_summary.json"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_003", "source_set_ranks_reviewed": list(range(6, 11)),
        "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen), "exact_pair_support_rows": 0,
        "partial_or_near_match_rows": 0, "general_regulator_evidence_rows": len(evidence), "exportable_pair_rows": 0,
        "canonical_writes_performed": False, "module22b_promotions_performed": False, "provenance_preserved": True,
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
        "decision": "Retain all 20 pairs as database-attributed search leads; no exact pair met the promotion threshold in the bounded search.",
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
