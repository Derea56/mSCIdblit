#!/usr/bin/env python3
"""Stage conservative evidence findings for public-TF batch 007 ranks 1-5."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/"
    "current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_007/"
    "public_tf_evidence_collection_batch_007.tsv"
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

REGULATORS = {
    "znf2": {
        "symbol": "ZNF2", "primary": "https://pubmed.ncbi.nlm.nih.gov/1945843/", "corr": "https://www.encodeproject.org/experiments/ENCSR011CKE/",
        "model": "human structural and HEK293 occupancy studies", "assay": "zinc-finger characterization and ENCODE ChIP-seq",
        "observation": "ZNF2 has structural DNA-binding characterization and a human HEK293 occupancy record; no queued target was validated by matched perturbation and target expression.",
        "exclusions": "Occupancy/identity evidence is not exact target regulation.",
    },
    "znf146": {
        "symbol": "ZNF146", "primary": "https://pubmed.ncbi.nlm.nih.gov/8665923/", "corr": "https://pubmed.ncbi.nlm.nih.gov/35100360/",
        "model": "human nuclear and LINE-1 occupancy studies", "assay": "DNA-binding characterization, ChIP-seq, CRISPR, and RNA-seq",
        "observation": "ZNF146/OZF has nuclear DNA-binding evidence and occupancy/perturbation evidence at LINE-1 elements; no queued ADAM22, ADGRB3, ADGRL1, or ADIPOR1 target was validated.",
        "exclusions": "LINE-1/repetitive-element evidence was not transferred to queued genes.",
    },
    "znf7": {
        "symbol": "ZNF7", "primary": "https://pubmed.ncbi.nlm.nih.gov/9268371/", "corr": "",
        "model": "human Jurkat interaction study", "assay": "protein-interaction characterization",
        "observation": "ZNF7/KOX4 has protein-interaction evidence with ribosomal proteins, but no queued target-gene regulation was validated.",
        "exclusions": "Protein interaction is not target-gene regulation; no queued edge was promoted.",
    },
    "znf282": {
        "symbol": "ZNF282", "primary": "https://pubmed.ncbi.nlm.nih.gov/25373738/", "corr": "https://pubmed.ncbi.nlm.nih.gov/22986521/",
        "model": "human ESCC and estrogen-receptor transcriptional models", "assay": "depletion, promoter reporter/ChIP, and coactivator studies",
        "observation": "ZNF282/HUB1/ZFP282 has regulator-level transcriptional evidence at nonqueued targets, including an E2F1-associated program; no queued ACVR1, ADGRL1, ADO, or AMH relationship was validated.",
        "exclusions": "Nonqueued target evidence was not transferred to queued edges.",
    },
    "zbtb12": {
        "symbol": "ZBTB12", "primary": "https://pubmed.ncbi.nlm.nih.gov/36759523/", "corr": "https://pubmed.ncbi.nlm.nih.gov/40543226/",
        "model": "human pluripotency and breast-cancer studies", "assay": "differentiation-associated transcript analysis and proposed promoter-axis analysis",
        "observation": "ZBTB12 has regulator-level evidence in hPSC differentiation and a proposed breast-cancer DNMT3B/ALDH1A2 axis; no queued target was validated by direct occupancy plus perturbation and target expression.",
        "exclusions": "Nonqueued targets and proposed relationships were not transferred to queued edges.",
    },
}

OCCUPANCY_URL = {
    "znf2": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF2_TARGET_GENES.html",
    "znf146": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF146_TARGET_GENES.html",
    "znf7": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF7_TARGET_GENES.html",
    "znf282": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF282_TARGET_GENES.html",
    "zbtb12": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZBTB12_TARGET_GENES.html",
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
        info = REGULATORS[key]
        pair_primary = OCCUPANCY_URL[key]
        pairs.append({
            "review_id": f"public_tf_evidence_batch007_pair_{int(row['batch_rank']):02d}_{i:02d}",
            "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key,
            "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "source_registry": row["source_registry"],
            "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"],
            "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": search_url(info["symbol"], row["target_symbol"], row["species_scope"]),
            "exact_pair_status": "binding_dataset_only_not_promotable", "regulator_general_evidence_status": "supported_general_regulator_evidence",
            "target_cell_presence_status": "not_established_for_exact_pair", "binding_or_association_status": "authoritative_occupancy_dataset_lead",
            "downstream_expression_or_perturbation_status": "not_found_for_exact_pair", "downstream_activation_status": "not_assessed",
            "upstream_relay_status": "not_tested_for_exact_pair", "disposition": "retain_database_candidate_as_search_lead_only",
            "primary_citation": pair_primary, "corroborating_citation": "", "near_match_exclusions": info["exclusions"],
            "review_notes": "The GTRD-derived target-set record supports promoter occupancy membership for this exact pair, but no paired perturbation/target-expression validation was located; do not promote. " + info["observation"],
            "exportable": "false", "canonical_write_performed": "false",
        })
        if key not in seen_keys:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch007_regulator_{key}", "regulator_key": key,
                "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "evidence_layer": "regulator_identity_and_regulatory_capacity",
                "support_kind": "primary_literature_regulator_level", "cell_or_model": info["model"], "assay_or_perturbation": info["assay"],
                "observation": info["observation"], "effect_direction": "queued-pair direction not established", "primary_citation": info["primary"],
                "corroborating_citation": info["corr"], "route_or_module_relevance": "regulator-level evidence only",
                "target_pair_scope": "not evidence for queued exact pairs; no Module 22B edge or upstream relay inferred", "exportable": "false",
                "canonical_write_performed": "false", "limitations": "Regulator-level evidence does not establish the queued target relationship, target-cell presence in SCI, downstream activation, or upstream relay.",
            })
        seen_keys.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch007_ranks0105_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch007_ranks0105_regulator_register.tsv"
    summary_path = args.output_dir / "batch_007_ranks0105_evidence_review_summary.json"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_007", "source_set_ranks_reviewed": list(range(1, 6)),
        "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen_keys), "exact_pair_support_rows": 0,
        "binding_dataset_only_not_promotable_rows": len(pairs), "partial_or_near_match_rows": 0, "general_regulator_evidence_rows": len(evidence),
        "exportable_pair_rows": 0, "canonical_writes_performed": False, "module22b_promotions_performed": False,
        "provenance_preserved": True, "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
        "decision": "Retain all 20 pairs as database-attributed binding search leads; no exact pair meets the promotion threshold.",
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
