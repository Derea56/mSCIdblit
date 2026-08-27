#!/usr/bin/env python3
"""Stage conservative evidence findings for public-TF batch 008 ranks 1-5."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/"
    "current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_008/"
    "public_tf_evidence_collection_batch_008.tsv"
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
    "znf490": {
        "symbol": "ZNF490", "primary": "https://pubmed.ncbi.nlm.nih.gov/33326746/", "corr": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9264634/",
        "model": "human transcriptional-effector and methylation-sensitive DNA-binding studies", "assay": "transcriptional-effector screen and DNA-binding characterization",
        "observation": "ZNF490 has regulator-level KRAB/C2H2 zinc-finger, methylation-sensitive DNA-binding, and transcriptional-effector evidence; none validates a queued target by matched perturbation and target expression.",
        "exclusions": "Regulator identity and DNA-binding evidence do not establish regulation of any queued target.",
    },
    "znf512": {
        "symbol": "ZNF512", "primary": "https://pubmed.ncbi.nlm.nih.gov/27114546/", "corr": "https://www.uniprot.org/uniprotkb/Q96ME7/entry",
        "model": "human HeLa and sequence-specific DNA-binding annotation", "assay": "virus-associated regulator perturbation and DNA-binding annotation",
        "observation": "ZNF512 has regulator-level evidence including HIV-associated downregulation and sequence-specific DNA-binding/heterochromatin annotation; none validates a queued target relationship.",
        "exclusions": "ZNF512B evidence was not transferred to ZNF512; regulator-level perturbation is not queued-target regulation.",
    },
    "znf10": {
        "symbol": "ZNF10", "primary": "https://pubmed.ncbi.nlm.nih.gov/26096782/", "corr": "https://pubmed.ncbi.nlm.nih.gov/9278146/",
        "model": "human HIV-1 LTR reporter and KRAB-domain studies", "assay": "depletion, reporter, and corepressor-association experiments",
        "observation": "ZNF10 has regulator-level repression evidence at the HIV-1 LTR and KRAB-domain reporter systems; none tests C1QL3, CCKBR, CD72, or EFNA3.",
        "exclusions": "Viral and nonqueued reporter targets were not transferred to queued genes.",
    },
    "znf257": {
        "symbol": "ZNF257", "primary": "https://pubmed.ncbi.nlm.nih.gov/33326746/", "corr": "https://www.uniprot.org/uniprotkb/Q9Y2Q1/entry",
        "model": "human KRAB-domain transcriptional-repressor annotation", "assay": "transcriptional-effector screen and protein-domain annotation",
        "observation": "ZNF257 has regulator-level KRAB-domain transcriptional-repressor evidence; no queued target was validated by direct occupancy plus perturbation and target expression.",
        "exclusions": "Isolated regulator/domain evidence is not target-specific evidence for queued pairs.",
    },
    "znf579": {
        "symbol": "ZNF579", "primary": "https://pubmed.ncbi.nlm.nih.gov/22190034/", "corr": "https://www.ncbi.nlm.nih.gov/gene/163033",
        "model": "human HIV protein-interaction and gene annotation studies", "assay": "protein-interaction assay and nuclear DNA-binding annotation",
        "observation": "ZNF579 has protein-interaction evidence involving HIV Tat and a predicted nuclear DNA-binding annotation; neither establishes regulation of a queued target.",
        "exclusions": "Protein interaction and predicted annotation are not target-gene regulation; a fusion transcript involving ADORA2A was excluded from the canonical target pair.",
    },
}

OCCUPANCY_URL = {
    "znf490": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF490_TARGET_GENES.html",
    "znf512": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF512_TARGET_GENES.html",
    "znf10": "https://www.gsea-msigdb.org/gsea/msigdb/human/cards/ZNF10_TARGET_GENES.html",
    "znf257": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF257_TARGET_GENES.html",
    "znf579": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF579_TARGET_GENES.html",
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
        pairs.append({
            "review_id": f"public_tf_evidence_batch008_pair_{int(row['batch_rank']):02d}_{i:02d}",
            "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key,
            "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "source_registry": row["source_registry"],
            "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"],
            "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": search_url(info["symbol"], row["target_symbol"], row["species_scope"]),
            "exact_pair_status": "binding_dataset_only_not_promotable", "regulator_general_evidence_status": "supported_general_regulator_evidence",
            "target_cell_presence_status": "not_established_for_exact_pair", "binding_or_association_status": "authoritative_occupancy_dataset_lead",
            "downstream_expression_or_perturbation_status": "not_found_for_exact_pair", "downstream_activation_status": "not_assessed",
            "upstream_relay_status": "not_tested_for_exact_pair", "disposition": "retain_database_candidate_as_search_lead_only",
            "primary_citation": OCCUPANCY_URL[key], "corroborating_citation": "", "near_match_exclusions": info["exclusions"],
            "review_notes": "The GTRD-derived target-set record supports promoter occupancy membership for this exact pair, but no paired perturbation/target-expression validation was located; do not promote. " + info["observation"],
            "exportable": "false", "canonical_write_performed": "false",
        })
        if key not in seen_keys:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch008_regulator_{key}", "regulator_key": key,
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
    pair_path = args.output_dir / "public_tf_evidence_review_batch008_ranks0105_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch008_ranks0105_regulator_register.tsv"
    summary_path = args.output_dir / "batch_008_ranks0105_evidence_review_summary.json"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_008", "source_set_ranks_reviewed": list(range(1, 6)),
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
