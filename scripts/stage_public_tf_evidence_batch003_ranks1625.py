#!/usr/bin/env python3
"""Stage conservative evidence findings for public-TF batch 003 ranks 16-25."""

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
    "zbtb11": (
        "ZBTB11", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10867109/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9337812/",
        "human lung-cancer and fibroblast models", "ChIP-seq, knockdown, RNA-seq, and ChIP-qPCR validation",
        "ZBTB11 has direct occupancy and perturbation evidence at non-queued genes, but no queued ACTR2/ACVR1/ADA/ADAM17 relationship was found.",
        "ZBTB11 targets such as ATPAF1, ANKRD40, COQ3, and ARHGAP6 and target-only receptor studies were excluded.",
    ),
    "znf511": (
        "ZNF511", "human", "", "",
        "human annotation and expression resources", "no qualifying primary target-gene assay located",
        "No qualifying primary regulator-level mechanistic paper was located in the bounded search, and no queued ACKR2/ACTR2/ADAM17/ADGRB3 relationship was found.",
        "Predicted DNA-binding annotations, co-expression, and database records were not counted as primary regulator evidence.",
    ),
    "sox3": (
        "SOX3", "mouse", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7174399/", "https://pubmed.ncbi.nlm.nih.gov/38891067/",
        "mouse spermatogonial and oligodendrocyte progenitor models", "SOX3 ChIP-PCR/ChIP-seq, null/deletion models, and target-expression assays",
        "SOX3 has direct developmental target evidence at non-queued genes, but no queued Acvr1c/Adam17/Adcyap1r1/Adgrl2 relationship was found.",
        "SOX3 targets such as Ngn3, Bcas1, Enpp6, Zfp488, and Nkx2.2 were not transferred to queued targets.",
    ),
    "znf18": (
        "ZNF18", "human", "", "",
        "human ChIP/annotation resources", "no qualifying primary target-gene perturbation assay located",
        "No qualifying primary regulator-level mechanistic paper was located in the bounded search, and no queued ACKR2/ADA/ADAM10/ADAM17 relationship was found.",
        "ReMap/ENCODE occupancy resources, annotation, and co-expression were retained only as possible follow-up sources, not as pair evidence.",
    ),
    "znf600": (
        "ZNF600", "human", "", "",
        "human expression/annotation resources", "no qualifying primary target-gene assay located",
        "No qualifying primary regulator-level mechanistic paper was located in the bounded search, and no queued ACVR1/ACVR1C/ADAM10/ADAM9 relationship was found.",
        "Predicted transcriptional annotations, expression changes, and database membership were not counted as regulator evidence.",
    ),
    "zfp1": (
        "ZFP1", "human", "", "",
        "human gene/annotation resources", "no qualifying primary target-gene assay located",
        "No qualifying primary regulator-level mechanistic paper was located in the bounded search, and no queued ABCA1/ACVR1/ADAM22/ADGRB3 relationship was found.",
        "ZFP1/ZNF475 annotation, motif prediction, and expression resources were not counted as functional evidence.",
    ),
    "ascl2": (
        "ASCL2", "mouse", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE52839", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4741583/",
        "mouse Tfh and trophoblast/intestinal developmental models", "ChIP-seq, expression perturbation, and promoter/occupancy studies",
        "ASCL2 has direct mouse regulatory evidence at non-queued Tfh/developmental targets, but no queued Ackr4/Actr2/Adam17/Adam9 relationship was found.",
        "ASCL2 targets such as Cxcr5, Cdx2, and other developmental genes were not transferred to queued targets.",
    ),
    "zbed1": (
        "ZBED1", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7471704/", "https://www.encodeproject.org/experiments/ENCSR286PCG/",
        "human fibroblast/K562 and mammalian promoter models", "promoter reporter, depletion, and ChIP-seq/occupancy studies",
        "ZBED1 has regulator-level promoter and occupancy evidence at non-queued ribosomal/housekeeping genes, but no queued ACKR2/ACTR2/ACVR1/ACVRL1 relationship was found.",
        "ZBED1 targets such as histone H1 and ribosomal protein genes, along with ENCODE occupancy without queued-locus verification, were not transferred.",
    ),
    "hoxa6": (
        "HOXA6", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11589199/", "https://chip-atlas.dbcls.jp/data/hg19/target/HOXA6.10.html",
        "human neural differentiation and epithelial/cancer regulatory models", "CUT&RUN/ChIP and differentiation perturbation studies",
        "HOXA6 has direct genome-binding/regulatory evidence at non-queued developmental targets, but no queued ACTR2/ACVR1/ADA/ADAM17 relationship was found.",
        "HOXA6 binding-site predictions and target genes outside the queued set were excluded from pair promotion.",
    ),
    "znf121": (
        "ZNF121", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6275281/", "",
        "human mammary epithelial and cancer models", "protein interaction, promoter/regulatory perturbation, and target-expression assays",
        "ZNF121 has direct transcriptional-regulator evidence at non-queued genes, but no queued ADAM22/ADAM9/ADGRB3/ADGRE5 relationship was found.",
        "ZNF121 targets such as ANG1, HMGA2, BRCA1, and ZBRK1 were not transferred to queued targets.",
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
    rows = [row for row in read_tsv(args.batch) if 16 <= int(row["batch_rank"]) <= 25]
    if len(rows) != 40:
        raise SystemExit(f"expected 40 rows for ranks 16-25, found {len(rows)}")
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
        if key not in seen:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch003_regulator_{key}", "regulator_key": key,
                "regulator_symbol": symbol, "species_scope": species, "evidence_layer": "regulator_identity_and_regulatory_capacity",
                "support_kind": "primary_literature_regulator_level" if primary else "no_qualifying_primary_regulator_evidence_located",
                "cell_or_model": model, "assay_or_perturbation": assay, "observation": observation,
                "effect_direction": "queued-pair direction not established", "primary_citation": primary,
                "corroborating_citation": corr, "route_or_module_relevance": "regulator-level evidence only" if primary else "regulator-level evidence not established",
                "target_pair_scope": "not evidence for queued exact pairs; no Module 22B edge or upstream relay inferred",
                "exportable": "false", "canonical_write_performed": "false",
                "limitations": "Regulator-level evidence does not establish the queued target relationship, target-cell presence in SCI, downstream activation, or upstream relay.",
            })
        seen.add(key)
    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch003_ranks1625_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch003_ranks1625_regulator_register.tsv"
    summary_path = args.output_dir / "batch_003_ranks1625_evidence_review_summary.json"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_003", "source_set_ranks_reviewed": list(range(16, 26)),
        "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen), "exact_pair_support_rows": 0,
        "partial_or_near_match_rows": 0, "general_regulator_evidence_rows": len(evidence), "exportable_pair_rows": 0,
        "canonical_writes_performed": False, "module22b_promotions_performed": False, "provenance_preserved": True,
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
        "decision": "Retain all 40 pairs as database-attributed search leads; no exact pair met the promotion threshold in the bounded search.",
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
