#!/usr/bin/env python3
"""Stage conservative evidence findings for public-TF batch 002 ranks 21-25.

This lane records exact-pair negative findings and regulator-level literature
without converting database membership or co-occurrence into an exportable
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
    "current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_002/"
    "public_tf_evidence_collection_batch_002.tsv"
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

# key: symbol, species, primary citation, corroboration, model, assay, observation, exclusions
REGULATORS = {
    "znf644": (
        "ZNF644", "human", "https://elifesciences.org/articles/05606", "",
        "human cell chromatin/regulatory models", "ChIP-seq, DNA-binding motif validation, and loss-of-function",
        "ZNF644 has direct chromatin/DNA-binding evidence in a corepressor complex, but no queued A2M/ACKR2/ACVR1/ACVR1C target relationship was found.",
        "HCC microarray co-occurrence of ZNF644 with A2M and pathway/annotation lists were excluded.",
    ),
    "casz1": (
        "CASZ1", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3131958/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3318574/",
        "human neuroblastoma and neural differentiation models", "CASZ1 restoration/knockdown, expression profiling, promoter reporter, and transcription-domain assays",
        "CASZ1 is experimentally supported as a zinc-finger transcription factor and regulator of developmental/tumor-suppressor genes, but no queued ADA/ADAM22/ADAM23/ADAM9 target relationship was found.",
        "CASZ1-ADAM23 co-listing in genetic/expression datasets was excluded as non-mechanistic; known CASZ1 targets such as NGFR/TH are not queued targets.",
    ),
    "znf823": (
        "ZNF823", "human", "", "",
        "human brain genetic/transcriptomic datasets", "cis-eQTL and expression association studies",
        "No qualifying regulator-level mechanistic paper was located in the bounded search, and no queued ACVR1/ADAM10/ADAM17/ADAM22 edge was found.",
        "ZNF823/ADAM10 co-occurrence in eQTL or gene-list datasets was excluded; no direct perturbation or occupancy evidence was identified.",
    ),
    "tcf7l1": (
        "TCF7L1", "mouse", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6265397/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9984534/",
        "mouse developmental/Wnt regulatory models", "TCF7L1 repression/activation and Wnt-pathway transcriptional studies",
        "TCF7L1 has regulator-level Wnt/developmental evidence, but no queued Abca1/Ackr4/Adam9/Adgrb1 edge was found.",
        "ABCA1 or ADAM9 co-expression with TCF7L1 and TCF7L2/ADAM10 studies were excluded; TCF7L2 is a distinct paralog.",
    ),
    "znf264": (
        "ZNF264", "human", "", "",
        "human transcriptomic/epigenomic datasets", "expression, methylation, and motif/annotation studies",
        "No qualifying regulator-level mechanistic paper was located in the bounded search, and no queued A2M/ACKR1/ACKR2/ADAM2 edge was found.",
        "Genome annotation, methylation, co-expression, and gene-list co-occurrence were excluded as non-mechanistic.",
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
    rows = [row for row in read_tsv(args.batch) if 21 <= int(row["batch_rank"]) <= 25]
    if len(rows) != 20:
        raise SystemExit(f"expected 20 rows for ranks 21-25, found {len(rows)}")

    pairs: list[dict[str, str]] = []
    evidence: list[dict[str, str]] = []
    seen_keys: set[str] = set()
    for i, row in enumerate(rows, 1):
        key = row["regulator_key"]
        if key not in REGULATORS:
            raise SystemExit(f"missing evidence map for {key}")
        symbol, species, primary, corr, model, assay, observation, exclusions = REGULATORS[key]
        pairs.append({
            "review_id": f"public_tf_evidence_batch002_pair_{int(row['batch_rank']):02d}_{i:02d}",
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
        if key not in seen_keys and primary:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch002_regulator_{key}", "regulator_key": key,
                "regulator_symbol": symbol, "species_scope": species, "evidence_layer": "regulator_identity_and_regulatory_capacity",
                "support_kind": "primary_literature_regulator_level", "cell_or_model": model, "assay_or_perturbation": assay,
                "observation": observation, "effect_direction": "queued-pair direction not established",
                "primary_citation": primary, "corroborating_citation": corr,
                "route_or_module_relevance": "regulator-level evidence only",
                "target_pair_scope": "not evidence for queued exact pairs; no Module 22B edge or upstream relay inferred",
                "exportable": "false", "canonical_write_performed": "false",
                "limitations": "Regulator-level evidence does not establish the queued target relationship, target-cell presence in SCI, downstream activation, or upstream relay.",
            })
        seen_keys.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch002_ranks2125_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch002_ranks2125_regulator_register.tsv"
    summary_path = args.output_dir / "batch_002_ranks2125_evidence_review_summary.json"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_002", "source_set_ranks_reviewed": list(range(21, 26)),
        "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen_keys),
        "exact_pair_support_rows": 0, "partial_or_near_match_rows": 0,
        "general_regulator_evidence_rows": len(evidence), "exportable_pair_rows": 0,
        "canonical_writes_performed": False, "module22b_promotions_performed": False,
        "provenance_preserved": True, "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
        "decision": "Retain all 20 pairs as database-attributed search leads; no exact pair met the promotion threshold in the bounded search.",
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
