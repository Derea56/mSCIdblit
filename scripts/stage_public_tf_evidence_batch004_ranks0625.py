#!/usr/bin/env python3
"""Stage conservative evidence findings for public-TF batch 004 ranks 6-25."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/"
    "current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_004/"
    "public_tf_evidence_collection_batch_004.tsv"
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

# symbol, species, primary, corroboration, model, assay, observation, exclusions,
# support kind (optional; used for authoritative binding-only datasets)
REGULATORS = {
    "zxdc": (
        "ZXDC", "human", "https://pubmed.ncbi.nlm.nih.gov/16600381/",
        "https://www.sciencedirect.com/science/article/pii/S0022283607004950",
        "human CIITA/MHC class II transcription models", "protein interaction, promoter/transcription assays, overexpression, and silencing",
        "ZXDC has regulator-level evidence in CIITA-dependent MHC class II transcription, but no queued ACVR1/ADAM2/ADGRE5/ADGRL1 relationship was found.",
        "MHC class II target evidence and queued-target co-occurrence were not transferred to queued edges.", "primary_literature_regulator_level",
    ),
    "znf281": (
        "ZNF281", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6048510/",
        "https://pubmed.ncbi.nlm.nih.gov/31782884/", "human neuroblastoma and differentiation models",
        "ChIP-qPCR, expression perturbation, and functional differentiation assays",
        "ZNF281 has direct regulator-level evidence at non-queued genes including GDNF and NRP2, but no queued ADGRE5/ADGRL1/ADM/ADORA2A relationship was found.",
        "Direct promoter evidence at non-queued targets, miRNA regulation, and expression co-occurrence were not transferred to queued edges.", "primary_literature_regulator_level",
    ),
    "hoxa13": (
        "HOXA13", "mouse", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2367452/",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC1301594/", "mouse placental and embryonic fibroblast models",
        "ChIP/ChIP-chip, EMSA, promoter-reporter, and loss-of-function/overexpression assays",
        "HOXA13 has direct mouse regulator-level evidence at non-queued genes including Tie2, Foxf1, and Enpp2, but no queued Abca1/Adam12/Adam23/Adgrl1 relationship was found.",
        "HOXA13 binding and expression effects at non-queued developmental targets were not transferred to queued edges.", "primary_literature_regulator_level",
    ),
    "znf3": (
        "ZNF3", "human", "", "", "human annotation and genomic resources",
        "no qualifying primary target-gene assay located",
        "No qualifying primary regulator-level mechanistic paper was located in the bounded search, and no queued A2M/ACTR2/ACVR1/ADAM10 relationship was found.",
        "Annotation, motif prediction, co-expression, and database membership were not counted as regulator evidence.", "no_qualifying_primary_regulator_evidence_located",
    ),
    "znf692": (
        "ZNF692", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11034355/",
        "https://www.encodeproject.org/experiments/ENCSR418MKG/", "human osteosarcoma and HEK293 models",
        "ChIP-qPCR, promoter-reporter, overexpression/knockdown, and ENCODE ChIP-seq",
        "ZNF692 has direct regulator-level evidence at non-queued genes including TNK2 and KAT5, but no queued ABCA1/ACTR2/ACVR1/ANGPTL2 relationship was found.",
        "ZNF692 binding and perturbation at non-queued metabolic/cancer targets were not transferred to queued edges.", "primary_literature_regulator_level",
    ),
    "znf701": (
        "ZNF701", "human", "", "", "human annotation and predicted-target resources",
        "no qualifying primary target-gene assay located",
        "No qualifying primary regulator-level mechanistic paper was located in the bounded search, and no queued ACKR3/ADAM17/ADAM22/ADGRE5 relationship was found.",
        "Motif-predicted target sets, annotation, and expression co-occurrence were not counted as functional evidence.", "no_qualifying_primary_regulator_evidence_located",
    ),
    "znf654": (
        "ZNF654", "human", "", "", "human genomic/3D-chromatin resources",
        "no qualifying primary target-gene assay located",
        "No qualifying primary regulator-level mechanistic paper with a validated target gene was located in the bounded search, and no queued ACKR3/ADA/ADGRB3/ADGRL2 relationship was found.",
        "High-throughput occupancy or genome-architecture observations without a validated target-gene perturbation were not treated as functional regulator evidence.", "no_qualifying_primary_regulator_evidence_located",
    ),
    "znf629": (
        "ZNF629", "human", "", "", "human annotation and cistromic resources",
        "no qualifying primary target-gene assay located",
        "No qualifying primary regulator-level mechanistic paper was located in the bounded search, and no queued ACVR1/ADAM10/ADGRE5/ADGRL1 relationship was found.",
        "GeneHancer, ReMap, motif, annotation, and co-expression records were not counted as functional evidence.", "no_qualifying_primary_regulator_evidence_located",
    ),
    "zscan5a": (
        "ZSCAN5A", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5340127/", "",
        "human HEK293 and BeWo cell models", "ChIP-seq, siRNA knockdown, RNA-seq, and locus-specific expression assays",
        "ZSCAN5A has direct regulator-level evidence at non-queued Pol III/extra-TFIIIC loci including RMRP, but no queued ADAM10/ADAM12/ADAM9/ADIPOR2 relationship was found.",
        "Pol III-locus occupancy and RMRP/tRNA expression effects were not transferred to queued protein-coding edges.", "primary_literature_regulator_level",
    ),
    "scrt2": (
        "SCRT2", "human", "", "", "human annotation and expression resources",
        "no qualifying primary target-gene assay located",
        "No qualifying primary regulator-level mechanistic paper was located in the bounded search, and no queued ADIPOR1/ADORA2A/ADORA2B/AGRN relationship was found.",
        "SCRT1 or other family-member evidence, annotation, and co-expression were not transferred to SCRT2 queued edges.", "no_qualifying_primary_regulator_evidence_located",
    ),
    "znf92": (
        "ZNF92", "human", "", "", "human breast-cancer expression studies",
        "expression-signature and association analysis; no qualifying direct target assay located",
        "ZNF92 is reported as an under-characterized expression-associated factor, but no qualifying direct regulator-level target assay or queued ACVR1/ADORA1/ADORA2A/ALK relationship was found.",
        "Expression signatures and HDAC7-associated inference were not counted as direct target evidence.", "no_qualifying_primary_regulator_evidence_located",
    ),
    "zfx": (
        "ZFX", "mouse", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4199880/",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC3936793/", "mouse stem-cell/leukemia and matched human tumor models",
        "ChIP-seq, shRNA/knockdown, expression profiling, and direct-target validation",
        "ZFX has direct regulator-level evidence at non-queued genes including Dis3L and Ube2j1, but no queued Actr2/Adam17/Adam22/Adam9 relationship was found.",
        "ZFX target genes and Notch/leukemia context were not transferred to queued edges; mouse-human cross-species observations were kept as regulator-level context only.", "primary_literature_regulator_level",
    ),
    "foxk1": (
        "FOXK1", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3418304/",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC10641274/", "human cell-cycle and HepG2 liver models",
        "ChIP-seq, siRNA knockdown, promoter-reporter, and target-expression assays",
        "FOXK1 has direct regulator-level evidence at non-queued genes including DHFR, TYMS, TFDP1, ALG10B, and ZNF212, but no queued ACVR1/ADAM22/ADGRL1/ADO relationship was found.",
        "FOXK1 cell-cycle and insulin-response targets were not transferred to queued edges.", "primary_literature_regulator_level",
    ),
    "zbtb40": (
        "ZBTB40", "human", "https://www.encodeproject.org/experiments/ENCSR237VLT/", "",
        "human K562 cells", "released ENCODE TF ChIP-seq",
        "An authoritative ENCODE ZBTB40 ChIP-seq experiment exists in human K562 cells, but no queued ACTR2/ACVR1/ADAM17/ADGRB3 target relationship was validated in the bounded search.",
        "This is occupancy-only dataset evidence without queued-locus verification or perturbation; it is not sufficient for a functional queued edge.", "authoritative_binding_dataset_only",
    ),
    "prdm15": (
        "PRDM15", "mouse", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6954057/",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC7360777/", "mouse embryos, embryonic stem cells, and lymphoma models",
        "ChIP-seq, knockout/conditional deletion, RNA-seq, promoter occupancy, and expression validation",
        "PRDM15 has direct regulator-level evidence at non-queued genes including Rbpj, Notch3, Rspo1, Spry1, Insr, and Igf1r, but no queued Acvr1/Adgrb3/Adgrl1/Adgrl2 relationship was found.",
        "PRDM15 signaling and metabolic targets were not transferred to queued edges.", "primary_literature_regulator_level",
    ),
    "zxdb": (
        "ZXDB", "human", "", "", "human and mouse centromere/annotation resources",
        "no qualifying primary target-gene assay located",
        "No qualifying primary regulator-level transcriptional target paper was located in the bounded search, and no queued ACVR1/ADA/ADO/ADORA2A relationship was found.",
        "Centromere association, annotation, and predicted transcription-factor activity were not counted as evidence for queued transcriptional targets.", "no_qualifying_primary_regulator_evidence_located",
    ),
    "rbpjl": (
        "RBPJL", "mouse", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2902682/",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC9208186/", "mouse pancreatic acinar and inflammatory models",
        "ChIP-seq/ChIP-qPCR, knockout, overexpression/knockdown, RNA-seq, and expression assays",
        "RBPJL has direct regulator-level evidence at non-queued pancreatic and inflammatory targets, but no queued Abca1/Adam17/Adgrb3/Adgrl1 relationship was found.",
        "RBPJL/ PTF1-L target evidence and pancreatic lineage context were not transferred to queued edges.", "primary_literature_regulator_level",
    ),
    "znf324": (
        "ZNF324", "human", "https://www.encodeproject.org/experiments/ENCSR712KVZ/",
        "https://remap.univ-amu.fr/target_page/ZNF324%3A9606", "human K562 and HEK293 cells",
        "ENCODE/ReMap ChIP-seq occupancy datasets",
        "Authoritative occupancy datasets exist for ZNF324 in human cells, but no queued ADGRE5/ADGRL1/ADIPOR1/ADIPOR2 target relationship was validated in the bounded search.",
        "Binding-dataset evidence lacks queued-locus verification and perturbation; it was retained as a follow-up lead only.", "authoritative_binding_dataset_only",
    ),
    "zfp69b": (
        "ZFP69B", "human", "https://pubmed.ncbi.nlm.nih.gov/38003570/", "",
        "human tumor expression and cell models", "RNA-seq, in-vitro phenotype assays, and searches for ZNF643/ZFP69B-bound loci",
        "ZFP69B has limited regulator-level tumor biology and genomic-locus evidence, but no queued ACTR2/ADAM9/ADORA2A/ANXA2 relationship was found.",
        "The paper's broader tumor associations and unvalidated candidate loci were not transferred to queued edges.", "primary_literature_regulator_level",
    ),
    "zbtb10": (
        "ZBTB10", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8934352/",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC6393293/", "human prostate, laryngeal cancer, HEK293, and telomere models",
        "promoter-reporter, ChIP/occupancy, knockdown/overexpression, CRISPR knockout, and expression assays",
        "ZBTB10 has direct regulator-level evidence at non-queued genes including PKLR and HK1 and sequence-specific telomeric DNA binding, but no queued ADA/ADAM10/ADAM9/ADGRB1 relationship was found.",
        "ZBTB10 target evidence at non-queued metabolic or telomeric loci was not transferred to queued edges.", "primary_literature_regulator_level",
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
    rows = [row for row in read_tsv(args.batch) if 6 <= int(row["batch_rank"]) <= 25]
    if len(rows) != 80:
        raise SystemExit(f"expected 80 rows for ranks 6-25, found {len(rows)}")

    pairs: list[dict[str, str]] = []
    evidence: list[dict[str, str]] = []
    seen_keys: set[str] = set()
    for i, row in enumerate(rows, 1):
        key = row["regulator_key"]
        if key not in REGULATORS:
            raise SystemExit(f"missing evidence map for {key}")
        symbol, species, primary, corr, model, assay, observation, exclusions, support_kind = REGULATORS[key]
        general_status = "supported_authoritative_binding_dataset_only" if support_kind == "authoritative_binding_dataset_only" else ("supported_general_regulator_evidence" if primary else "not_found_in_bounded_search")
        pairs.append({
            "review_id": f"public_tf_evidence_batch004_pair_{int(row['batch_rank']):02d}_{i:02d}",
            "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key,
            "regulator_symbol": symbol, "species_scope": row["species_scope"], "source_registry": row["source_registry"],
            "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"],
            "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": search_url(symbol, row["target_symbol"], row["species_scope"]),
            "exact_pair_status": "no_exact_pair_support_found_in_bounded_search",
            "regulator_general_evidence_status": general_status,
            "target_cell_presence_status": "not_established_for_exact_pair", "binding_or_association_status": "not_found_for_exact_pair",
            "downstream_expression_or_perturbation_status": "not_found_for_exact_pair", "downstream_activation_status": "not_assessed",
            "upstream_relay_status": "not_tested_for_exact_pair", "disposition": "retain_database_candidate_as_search_lead_only",
            "primary_citation": "", "corroborating_citation": "", "near_match_exclusions": exclusions,
            "review_notes": "Regulator-level references are stored separately; they are not evidence for this exact queued pair. " + observation,
            "exportable": "false", "canonical_write_performed": "false",
        })
        if key not in seen_keys:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch004_regulator_{key}", "regulator_key": key,
                "regulator_symbol": symbol, "species_scope": species, "evidence_layer": "regulator_identity_and_regulatory_capacity",
                "support_kind": support_kind, "cell_or_model": model, "assay_or_perturbation": assay,
                "observation": observation, "effect_direction": "queued-pair direction not established",
                "primary_citation": primary, "corroborating_citation": corr,
                "route_or_module_relevance": "regulator-level evidence only" if primary else "regulator-level evidence not established",
                "target_pair_scope": "not evidence for queued exact pairs; no Module 22B edge or upstream relay inferred",
                "exportable": "false", "canonical_write_performed": "false",
                "limitations": "Regulator-level evidence does not establish the queued target relationship, target-cell presence in SCI, downstream activation, or upstream relay.",
            })
        seen_keys.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch004_ranks0625_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch004_ranks0625_regulator_register.tsv"
    summary_path = args.output_dir / "batch_004_ranks0625_evidence_review_summary.json"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_004", "source_set_ranks_reviewed": list(range(6, 26)),
        "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen_keys), "exact_pair_support_rows": 0,
        "partial_or_near_match_rows": 0, "general_regulator_evidence_rows": len(evidence), "exportable_pair_rows": 0,
        "canonical_writes_performed": False, "module22b_promotions_performed": False, "provenance_preserved": True,
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
        "decision": "Retain all 80 pairs as database-attributed search leads; no exact pair met the promotion threshold in the bounded search.",
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
