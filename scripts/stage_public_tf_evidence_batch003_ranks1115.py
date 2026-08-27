#!/usr/bin/env python3
"""Stage conservative evidence findings for public-TF batch 003 ranks 11-15."""

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
    "review_id", "batch_id", "batch_rank", "regulator_key", "regulator_symbol", "species_scope", "source_registry",
    "source_record_id", "raw_tf_symbol", "target_symbol", "target_graph_modules", "candidate_membership_status",
    "exact_pair_search_url", "exact_pair_status", "regulator_general_evidence_status", "target_cell_presence_status",
    "binding_or_association_status", "downstream_expression_or_perturbation_status", "downstream_activation_status",
    "upstream_relay_status", "disposition", "primary_citation", "corroborating_citation", "near_match_exclusions",
    "review_notes", "exportable", "canonical_write_performed",
]
EVIDENCE_FIELDS = [
    "evidence_id", "regulator_key", "regulator_symbol", "species_scope", "evidence_layer", "support_kind",
    "cell_or_model", "assay_or_perturbation", "observation", "effect_direction", "primary_citation",
    "corroborating_citation", "route_or_module_relevance", "target_pair_scope", "exportable",
    "canonical_write_performed", "limitations",
]

# symbol, species, primary, corroboration, model, assay, observation, exclusions
REGULATORS = {
    "hoxd11": (
        "HOXD11", "mouse", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5805373/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12189421/",
        "mouse nephron progenitors and Hox11 developmental models", "factor-specific ChIP-seq/cistromic analysis and tagged-allele binding studies",
        "HOXD11 has developmental regulator and genome-binding evidence in mouse, but no queued Ackr3/Acvr1/Acvr1c/Adam12 relationship was found.",
        "Hoxd11 developmental co-regulation, Hox paralog evidence, and target-only studies were not transferred to queued targets.",
    ),
    "npas4": (
        "NPAS4", "mouse", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4169177/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9946837/",
        "mouse hippocampal neurons and primary neuronal cultures", "NPAS4 ChIP-seq, knockout/knockdown, RNA-seq, ChIP-qPCR, and target functional assays",
        "NPAS4 has direct activity-dependent neuronal target evidence at non-queued genes, but no queued Acvr1/Adam12/Adam17/Adam22 relationship was found.",
        "NPAS4 targets such as Bdnf, Nptx2, and Plk2 and target-only receptor studies were excluded from queued-pair promotion.",
    ),
    "zfat": (
        "ZFAT", "mouse", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2922575/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8248092/",
        "mouse yolk-sac hematopoietic, T-cell, and adipocyte models", "ChIP-PCR/ChIP-seq, promoter reporter assays, deletion, and re-expression studies",
        "ZFAT has direct promoter-binding and perturbation evidence at non-queued genes, but no queued Actr2/Acvr1/Acvr1c/Acvrl1 relationship was found.",
        "ZFAT targets such as Tal1, Lmo2, Gata1, and Brf1 were not transferred to queued receptor/cytoskeletal targets.",
    ),
    "ovol2": (
        "OVOL2", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3790720/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4062651/",
        "human cancer and mouse mammary epithelial models", "OVOL2 depletion/overexpression, promoter ChIP, ChIP-seq, and direct-target expression assays",
        "OVOL2 has direct transcriptional-repressor and genome-binding evidence at non-queued EMT/developmental targets, but no queued ACKR2/ACTR2/ADAM10/ADAM22 relationship was found.",
        "OVOL2 targets such as ZEB1, VIM, and Notch1 and TGF-beta pathway studies were not transferred to queued targets.",
    ),
    "bhlha15": (
        "BHLHA15", "mouse", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5108881/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9811352/",
        "mouse gastric, pancreatic, and plasma-cell secretory models", "genome-wide DNA binding/Bio-ChIP-seq, genetic mouse models, and target-expression assays",
        "BHLHA15/MIST1 has direct secretory-cell regulator evidence at non-queued genes, but no queued Abca1/Acvr1/Ada/Adam10 relationship was found.",
        "MIST1 secretory-network targets and XBP1 co-regulation were not transferred to queued targets.",
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
    rows = [row for row in read_tsv(args.batch) if 11 <= int(row["batch_rank"]) <= 15]
    if len(rows) != 20:
        raise SystemExit(f"expected 20 rows for ranks 11-15, found {len(rows)}")
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
            "regulator_general_evidence_status": "supported_general_regulator_evidence",
            "target_cell_presence_status": "not_established_for_exact_pair", "binding_or_association_status": "not_found_for_exact_pair",
            "downstream_expression_or_perturbation_status": "not_found_for_exact_pair", "downstream_activation_status": "not_assessed",
            "upstream_relay_status": "not_tested_for_exact_pair", "disposition": "retain_database_candidate_as_search_lead_only",
            "primary_citation": "", "corroborating_citation": "", "near_match_exclusions": exclusions,
            "review_notes": "Regulator-level references are stored separately; they are not evidence for this exact queued pair. " + observation,
            "exportable": "false", "canonical_write_performed": "false",
        })
        if key not in seen:
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
    pair_path = args.output_dir / "public_tf_evidence_review_batch003_ranks1115_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch003_ranks1115_regulator_register.tsv"
    summary_path = args.output_dir / "batch_003_ranks1115_evidence_review_summary.json"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_003", "source_set_ranks_reviewed": list(range(11, 16)),
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
