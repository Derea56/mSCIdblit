#!/usr/bin/env python3
"""Stage conservative evidence findings for public-TF batch 005 ranks 6-25."""

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

# symbol, species, primary, corroboration, model, assay, observation, exclusions,
# support kind
REGULATORS = {
    "znf280d": (
        "ZNF280D", "human", "https://www.encodeproject.org/experiments/ENCSR451CYX/", "",
        "human HEK293 cells", "ENCODE ChIP-seq occupancy dataset",
        "An authoritative ZNF280D occupancy dataset exists in human HEK293 cells, but no validated target-level perturbation or queued ACTR2/ADAM10/ADGRE5/ADIPOR2 relationship was found.",
        "Occupancy-only data and promoter predictions were not treated as functional queued-edge evidence.", "authoritative_binding_dataset_only",
    ),
    "osr1": (
        "OSR1", "mouse", "", "", "mouse developmental and prostate models",
        "expression/conditional-model studies; no qualifying queued-target assay located",
        "No qualifying primary regulator-level mechanistic paper with a validated queued-compatible target was located in the bounded search, and no queued Ackr3/Acvr1/Adam10/Adam17 relationship was found.",
        "OSR1/OSR2 paralog or upstream-regulation observations were not transferred to queued edges.", "no_qualifying_primary_regulator_evidence_located",
    ),
    "yy2": (
        "YY2", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5098618/", "https://pubmed.ncbi.nlm.nih.gov/38682484/",
        "human and mouse embryonic-stem-cell and colorectal-cancer models", "YY2 ChIP-seq, knockout/overexpression, RNA-seq, promoter-reporter, and target-expression assays",
        "YY2 has direct regulator-level evidence at non-queued genes including Tdgf1, Oct4, Klf5, Foxd3, and BUB3, but no queued ACTR2/ADAM9/ADORA1/ANXA2 relationship was found.",
        "YY1/YY2 paralog overlap and non-queued target evidence were not transferred to queued edges.", "primary_literature_regulator_level",
    ),
    "znf205": (
        "ZNF205", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC13045463/", "",
        "human HepG2 and SMMC-7721 liver-cancer models", "knockdown/overexpression, RNA-seq, p53 occupancy, and protein-interaction assays",
        "ZNF205 has regulator-level evidence as a modulator of p53 target transcription at non-queued genes, but no queued ACVR1C/ADAM22/ADGRB3/ADGRL1 relationship was found.",
        "ZNF205 did not bind the tested p53 target regulatory regions directly in the cited study; target-only p53 evidence was not transferred.", "primary_literature_regulator_level",
    ),
    "znf280a": (
        "ZNF280A", "human", "https://pubmed.ncbi.nlm.nih.gov/36059657/", "",
        "human colorectal-cancer models", "knockdown/overexpression, expression profiling, and in-vivo tumor assays",
        "ZNF280A has regulator-level cancer evidence involving non-queued RPS14, but no queued ADGRL1/ADGRL2/ANG/APLP1 relationship was found.",
        "The RPS14 downstream claim is not a queued receptor/ligand edge and was not transferred.", "primary_literature_regulator_level",
    ),
    "zscan16": (
        "ZSCAN16", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11546084/", "",
        "human hepatocellular-carcinoma models", "ChIP-qPCR, dual-luciferase, knockdown, rescue, and xenograft assays",
        "ZSCAN16 directly activates non-queued TBC1D31 in HCC models, but no queued ADA/ADAM10/ADAM22/ADAM23 relationship was found.",
        "The TBC1D31 edge was not transferred to queued targets; target co-occurrence and hTFtarget predictions alone were not counted.", "primary_literature_regulator_level",
    ),
    "gmeb1": (
        "GMEB1", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10302989/", "https://pubmed.ncbi.nlm.nih.gov/7665613/",
        "human HepG2 and Huh7 liver-cancer and glucocorticoid-response models", "ChIP-qPCR, dual-luciferase, overexpression/knockdown, and DNA-binding assays",
        "GMEB1 has direct regulator-level evidence at non-queued YAP1 and glucocorticoid-responsive regulatory elements, but no queued ACTR2/ACVR1C/ADIPOR2/ADO relationship was found.",
        "GMEB1 target evidence at YAP1/TAT and glucocorticoid elements was not transferred to queued edges.", "primary_literature_regulator_level",
    ),
    "bhlhe22": (
        "BHLHE22", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11624798/", "https://remap2022.univ-amu.fr/target_page/BHLHE22%3A9606",
        "human lung-cancer/immune-response models and CAL-1 occupancy data", "ChIP, dual-luciferase, knockdown/overexpression, and ReMap occupancy",
        "BHLHE22 has direct regulator-level evidence at non-queued PD-L1, but no queued A2M/ACVR1/ADORA3/ALCAM relationship was found.",
        "BHLHE22/LIP co-regulation of PD-L1 was not transferred to queued edges.", "primary_literature_regulator_level",
    ),
    "hes2": (
        "HES2", "human", "", "", "human annotation and developmental resources",
        "no qualifying primary target-gene assay located",
        "No qualifying primary regulator-level mechanistic paper was located in the bounded search, and no queued ADAM9/ADIPOR2/ANXA1/ANXA2 relationship was found.",
        "HES1/HES5 family-member evidence, annotation, and co-expression were not transferred to HES2 queued edges.", "no_qualifying_primary_regulator_evidence_located",
    ),
    "znf778": (
        "ZNF778", "human", "", "", "human annotation and expression resources",
        "no qualifying primary target-gene assay located",
        "No qualifying primary regulator-level mechanistic paper was located in the bounded search, and no queued ADCYAP1/ADM/ALCAM/BDKRB2 relationship was found.",
        "Protein-interaction, motif, annotation, and co-expression records were not counted as functional evidence.", "no_qualifying_primary_regulator_evidence_located",
    ),
    "cc2d1a": (
        "CC2D1A", "human", "https://www.encodeproject.org/targets/CC2D1A-human/", "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/CC2D1A_TARGET_GENES",
        "human ENCODE/GTRD occupancy resources", "ENCODE/GTRD ChIP-seq target-set evidence",
        "Authoritative occupancy resources exist for CC2D1A, but no validated target-level perturbation or queued AGRN/ANGPT1/AXL/C5AR1 relationship was found.",
        "Binding-target-set evidence without queued-locus verification and perturbation was not treated as a functional edge.", "authoritative_binding_dataset_only",
    ),
    "klf17": (
        "KLF17", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8645209/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4571863/",
        "human lung-cancer and naive-pluripotency models", "overexpression, expression profiling, and promoter/regulatory assays",
        "KLF17 has regulator-level evidence at non-queued EMT/pluripotency targets, but no queued ADGRE5/AVPR2/BDKRB2/BOC relationship was found.",
        "KLF17 target evidence at ID1, VIM, FN1, ZO-1, E-cadherin, and pluripotency genes was not transferred to queued edges.", "primary_literature_regulator_level",
    ),
    "znf266": (
        "ZNF266", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12090625/", "",
        "human lung-adenocarcinoma cells, organoids, and xenografts", "ChIP-qPCR, DNA pull-down, dual-luciferase, RNA-seq, knockout/overexpression, and rescue",
        "ZNF266 directly represses non-queued CA9 and affects the mTOR-linked phenotype, but no queued ACTR2/ADA/ADAM10/ADGRE5 relationship was found.",
        "The CA9 mechanism was not transferred to queued targets.", "primary_literature_regulator_level",
    ),
    "znf768": (
        "ZNF768", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6344866/", "https://www.encodeproject.org/experiments/ENCSR070HWF/",
        "human Raji, U2OS, HEK293, and ENCODE occupancy models", "ChIP-seq, dominant-negative perturbation, RNA-seq, and ENCODE ChIP-seq",
        "ZNF768 has direct regulator-level evidence at non-queued promoter-associated genes and an exact APOE occupancy lead in a GTRD-derived target set; no perturbation/orthogonal validation for the queued APOE edge was located.",
        "The exact ZNF768/APOE hit is occupancy-only target-set evidence, not a promoted functional edge; other queued ADCYAP1R1/C3/CALCRL edges lacked qualifying exact support.", "primary_literature_regulator_level",
    ),
    "zscan30": (
        "ZSCAN30", "human", "https://remap2020.univ-amu.fr/target_page/ZSCAN30%3A9606", "",
        "human ReMap occupancy resources", "ReMap ChIP-seq occupancy resource",
        "An authoritative ReMap occupancy record exists for ZSCAN30, but no validated target-level perturbation or queued ADGRL1/ADIPOR1/APP/BDKRB2 relationship was found.",
        "Occupancy-only data and annotation were not treated as functional queued-edge evidence.", "authoritative_binding_dataset_only",
    ),
    "znf320": (
        "ZNF320", "human", "", "", "human annotation and expression resources",
        "no qualifying primary target-gene assay located",
        "No qualifying primary regulator-level mechanistic paper was located in the bounded search, and no queued ADORA1/AGRN/ANXA2/BMP7 relationship was found.",
        "Annotation, predicted zinc-finger activity, and co-expression were not counted as functional evidence.", "no_qualifying_primary_regulator_evidence_located",
    ),
    "zbtb24": (
        "ZBTB24", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6212772/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6895263/",
        "human lymphoblastoid/HCT116 and mouse embryonic-stem-cell models", "ChIP-seq, shRNA/knockdown, methylation, promoter-reporter, and expression assays",
        "ZBTB24 has direct regulator-level evidence at non-queued genes including CDCA7, TAF6, CDC40, and OSTC, but no queued ADAM22/ADGRB3/ADORA2A/ARTN relationship was found.",
        "ZBTB24 target evidence at non-queued developmental/chromatin loci was not transferred to queued edges.", "primary_literature_regulator_level",
    ),
    "zscan29": (
        "ZSCAN29", "human", "", "", "human annotation and expression resources",
        "no qualifying primary target-gene assay located",
        "No qualifying primary regulator-level mechanistic paper was located in the bounded search, and no queued ACTR2/ADA/ADGRL1/ADO relationship was found.",
        "ZSCAN-family paralog evidence, motif prediction, annotation, and co-expression were not transferred.", "no_qualifying_primary_regulator_evidence_located",
    ),
    "zbtb7b": (
        "ZBTB7B", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10789742/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC13127139/",
        "human and mouse T-cell, liver-cancer, and glioma models", "ChIP-seq/ChIP-PCR, perturbation, RNA-seq, and promoter assays",
        "ZBTB7B has direct regulator-level evidence at non-queued genes including GPR17, CXCL10, c-Jun, and T-cell differentiation loci, but no queued ACTR2/ADAM10/ANG/ANXA2 relationship was found.",
        "ZBTB7B target evidence at non-queued immune and cancer genes was not transferred to queued edges.", "primary_literature_regulator_level",
    ),
    "zfat": (
        "ZFAT", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7641738/", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE134612",
        "human HEK293 and mouse hematopoietic/adipocyte models", "ChIP-seq, RNA-seq, ChIP-PCR, knockout, and expression assays",
        "ZFAT has direct regulator-level evidence at non-queued hematopoietic, adipocyte, and centromeric loci, but no queued ACKR2/ACTR2/ADIPOR1/ALCAM relationship was validated.",
        "ZFAT target evidence and centromeric/noncoding transcription were not transferred to queued protein-coding edges.", "primary_literature_regulator_level",
    ),
}

EXACT_OCCUPANCY_ONLY = {
    ("znf768", "APOE"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF768_TARGET_GENES",
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
        exact_lead = EXACT_OCCUPANCY_ONLY.get((key, row["target_symbol"]))
        if exact_lead:
            exact_status = "binding_dataset_only_not_promotable"
            binding_status = "authoritative_occupancy_dataset_lead"
            expression_status = "not_found_for_exact_pair"
            pair_primary = exact_lead
            pair_notes = "An authoritative target-set record indicates regulator occupancy at this exact gene, but no matched perturbation or orthogonal validation was located; do not promote."
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
    pair_path = args.output_dir / "public_tf_evidence_review_batch005_ranks0625_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch005_ranks0625_regulator_register.tsv"
    summary_path = args.output_dir / "batch_005_ranks0625_evidence_review_summary.json"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    occupancy_rows = sum(row["exact_pair_status"] == "binding_dataset_only_not_promotable" for row in pairs)
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_005", "source_set_ranks_reviewed": list(range(6, 26)),
        "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen_keys), "exact_pair_support_rows": 0,
        "binding_dataset_only_not_promotable_rows": occupancy_rows, "partial_or_near_match_rows": occupancy_rows,
        "general_regulator_evidence_rows": len(evidence), "exportable_pair_rows": 0,
        "canonical_writes_performed": False, "module22b_promotions_performed": False, "provenance_preserved": True,
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
        "decision": "Retain all 80 pairs as database-attributed search leads; exact occupancy-only leads remain non-promotable without matched perturbation or orthogonal validation.",
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
