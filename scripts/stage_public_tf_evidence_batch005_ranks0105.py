#!/usr/bin/env python3
"""Stage conservative evidence findings for public-TF batch 005 ranks 1-5."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/"
    "current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_005/"
    "public_tf_evidence_collection_batch_005.tsv"
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

# symbol, species, primary, corroboration, model, assay, observation, exclusions, support kind
REGULATORS = {
    "znf614": (
        "ZNF614", "human", "https://remap2022.univ-amu.fr/target_page/ZNF614%3A9606",
        "https://www.encodeproject.org/experiments/ENCSR011CIR/", "human ReMap/ENCODE occupancy resources",
        "ReMap and ENCODE ChIP-seq occupancy datasets",
        "Authoritative human ZNF614 occupancy resources exist, but no validated queued A2M/ACKR2/ADAM9/ADGRB3 target relationship was found.",
        "Occupancy-only, co-listing, motif, and expression evidence were not treated as functional queued-edge evidence.",
        "authoritative_binding_dataset_only",
    ),
    "znf189": (
        "ZNF189", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10776019/", "",
        "human adipocyte models", "depletion, ChIP-seq, RNA-seq/BETA integration, and downstream validation",
        "ZNF189 has direct regulator-level evidence at nonqueued PDE1B/PDE1B2 in human adipocyte models, but no queued ACVR1/ADAM10/ADAM22/ADGRL1 relationship was found.",
        "The nonqueued PDE1B/PDE1B2 evidence was not transferred to queued receptor or metalloprotease targets.",
        "primary_literature_regulator_level",
    ),
    "znf317": (
        "ZNF317", "human", "https://www.encodeproject.org/experiments/ENCSR795KRU/", "",
        "human ENCODE and expression resources", "ChIP-seq occupancy and overexpression-expression resources",
        "ZNF317 occupancy and perturbational expression resources exist, but no validated queued ADAM17/ADGRB1/ADGRB3/ADIPOR2 relationship was found.",
        "Occupancy, overexpression RNA-seq, target-set membership, and paralog evidence were not treated as a validated queued edge.",
        "authoritative_binding_dataset_only",
    ),
    "zscan4": (
        "ZSCAN4", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7314663/",
        "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZSCAN4_TARGET_GENES",
        "human HNSCC models and GTRD-derived target-set resources",
        "induction/depletion, promoter occupancy/epigenetic assays, downstream expression, and ChIP-derived target set",
        "ZSCAN4 has regulator-level evidence at nonqueued pluripotency genes and ChIP-derived occupancy leads for the queued ADAM10/ADGRE5/ANGPT4/ANXA2 genes, but no queued perturbation/target-expression validation was found.",
        "The four exact queued hits are binding-set membership only; the nonqueued pluripotency targets were not transferred.",
        "primary_literature_regulator_level",
    ),
    "foxk1": (
        "FOXK1;Foxk1", "mouse", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6591025/",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC3561855/", "mouse MEF and muscle/atrophy models",
        "ChIP, knockdown, promoter reporter, qPCR/protein assays, and interaction/EMSA studies",
        "Foxk1 has strong nonqueued regulator-level evidence at Hif1a and Foxo4/Mef2c-associated programs, but no queued Abca1/Acvr1/Adam17/Adipor2 relationship was found.",
        "Nonqueued Foxk1 targets and interaction-dependent repression were not transferred to queued edges.",
        "primary_literature_regulator_level",
    ),
}

EXACT_OCCUPANCY_ONLY = {
    ("zscan4", "ADAM10"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZSCAN4_TARGET_GENES",
    ("zscan4", "ADGRE5"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZSCAN4_TARGET_GENES",
    ("zscan4", "ANGPT4"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZSCAN4_TARGET_GENES",
    ("zscan4", "ANXA2"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZSCAN4_TARGET_GENES",
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
        symbol, species, primary, corr, model, assay, observation, exclusions, support_kind = REGULATORS[key]
        exact_lead = EXACT_OCCUPANCY_ONLY.get((key, row["target_symbol"]))
        if exact_lead:
            exact_status = "binding_dataset_only_not_promotable"
            binding_status = "authoritative_occupancy_dataset_lead"
            expression_status = "not_found_for_exact_pair"
            pair_primary = exact_lead
            pair_notes = "An authoritative GTRD-derived target-set record indicates regulator occupancy at this exact gene, but no matched perturbation or orthogonal validation was located; do not promote."
        else:
            exact_status = "no_exact_pair_support_found_in_bounded_search"
            binding_status = "not_found_for_exact_pair"
            expression_status = "not_found_for_exact_pair"
            pair_primary = ""
            pair_notes = "No qualifying exact regulator-target assay was located in the bounded search."
        general_status = "supported_authoritative_binding_dataset_only" if support_kind == "authoritative_binding_dataset_only" else ("supported_general_regulator_evidence" if primary else "not_found_in_bounded_search")
        pairs.append({
            "review_id": f"public_tf_evidence_batch005_pair_{int(row['batch_rank']):02d}_{i:02d}",
            "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key,
            "regulator_symbol": symbol, "species_scope": row["species_scope"], "source_registry": row["source_registry"],
            "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"],
            "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": search_url(symbol, row["target_symbol"], row["species_scope"]), "exact_pair_status": exact_status,
            "regulator_general_evidence_status": general_status, "target_cell_presence_status": "not_established_for_exact_pair",
            "binding_or_association_status": binding_status, "downstream_expression_or_perturbation_status": expression_status,
            "downstream_activation_status": "not_assessed", "upstream_relay_status": "not_tested_for_exact_pair",
            "disposition": "retain_database_candidate_as_search_lead_only", "primary_citation": pair_primary,
            "corroborating_citation": "", "near_match_exclusions": exclusions,
            "review_notes": pair_notes + " Regulator-level references are stored separately and are not evidence for this exact queued pair. " + observation,
            "exportable": "false", "canonical_write_performed": "false",
        })
        if key not in seen_keys:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch005_regulator_{key}", "regulator_key": key,
                "regulator_symbol": symbol, "species_scope": species, "evidence_layer": "regulator_identity_and_regulatory_capacity",
                "support_kind": support_kind, "cell_or_model": model, "assay_or_perturbation": assay,
                "observation": observation, "effect_direction": "queued-pair direction not established", "primary_citation": primary,
                "corroborating_citation": corr, "route_or_module_relevance": "regulator-level evidence only" if primary else "regulator-level evidence not established",
                "target_pair_scope": "not evidence for queued exact pairs; no Module 22B edge or upstream relay inferred",
                "exportable": "false", "canonical_write_performed": "false",
                "limitations": "Regulator-level evidence does not establish the queued target relationship, target-cell presence in SCI, downstream activation, or upstream relay.",
            })
        seen_keys.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch005_ranks0105_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch005_ranks0105_regulator_register.tsv"
    summary_path = args.output_dir / "batch_005_ranks0105_evidence_review_summary.json"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    occupancy_rows = sum(row["exact_pair_status"] == "binding_dataset_only_not_promotable" for row in pairs)
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_005", "source_set_ranks_reviewed": list(range(1, 6)),
        "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen_keys), "exact_pair_support_rows": 0,
        "binding_dataset_only_not_promotable_rows": occupancy_rows, "partial_or_near_match_rows": occupancy_rows,
        "general_regulator_evidence_rows": len(evidence), "exportable_pair_rows": 0,
        "canonical_writes_performed": False, "module22b_promotions_performed": False, "provenance_preserved": True,
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
        "decision": "Retain all 20 pairs as database-attributed search leads; exact occupancy-only leads remain non-promotable without matched perturbation or orthogonal validation.",
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
