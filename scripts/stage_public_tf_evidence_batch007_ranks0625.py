#!/usr/bin/env python3
"""Stage conservative evidence findings for public-TF batch 007 ranks 6-25."""

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

# These are regulator-level records only. They are intentionally not used to promote
# any queued edge. Exact target-set members are recorded separately as occupancy-only.
REGULATORS = {
    "znf766": {
        "symbol": "ZNF766", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF766_TARGET_GENES.html",
        "corr": "", "model": "human GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization",
        "observation": "The GTRD-derived ZNF766 target set contains queued ADAM9, ADGRB3, ADIPOR1, and ADORA3; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Target-set membership is occupancy-only; no exact functional pair was promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "znf322": {
        "symbol": "ZNF322", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF322_TARGET_GENES.html",
        "corr": "", "model": "human GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization",
        "observation": "The GTRD-derived ZNF322 target set contains queued ANGPT2, APLP1, APLP2, and APOE; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Target-set membership is occupancy-only; no exact functional pair was promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "zbtb44": {
        "symbol": "ZBTB44", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZBTB44_TARGET_GENES.html",
        "corr": "", "model": "human GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization",
        "observation": "The GTRD-derived ZBTB44 target set contains queued ACVR1, ADAM22, ADGRL1, and ADIPOR1; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Target-set membership is occupancy-only; no exact functional pair was promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "znf518a": {
        "symbol": "ZNF518A", "species": "human", "primary": "https://dbarchive.biosciencedbc.jp/kyushu-u/hg19/target/SRX1389376.5.html",
        "corr": "https://www.encodeproject.org/experiments/ENCSR159GFL/", "model": "human occupancy-resource records", "assay": "ChIP-Atlas/ReMap-style target association and ENCODE factor-targeted experiment metadata",
        "observation": "Public regulatory resources establish ZNF518A as a profiled regulator, but no queued ACKR2, ADA, ADAM17, or ADO edge had matched functional validation.",
        "exclusions": "Resource-level occupancy and factor metadata were not transferred to queued functional edges.", "kind": "authoritative_binding_dataset_only",
    },
    "foxd2": {
        "symbol": "FOXD2", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/FOXD2_TARGET_GENES.html",
        "corr": "https://jaspar.elixir.no/matrix/MA0847.2/", "model": "human FOXD2 binding-profile/target-set resources", "assay": "GTRD-derived target set and validated FOXD2 DNA-binding profile",
        "observation": "The FOXD2 target-set resource contains queued CD44 and CD9; ACTR2 and CHRNA7 were not validated by a matched functional study.",
        "exclusions": "Binding-set membership and motif-profile evidence are not sufficient for target activation or repression.", "kind": "authoritative_binding_dataset_only",
    },
    "znf22": {
        "symbol": "ZNF22", "species": "human", "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9742255/",
        "corr": "https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2022.1027942/pdf", "model": "human brain endothelial-cell blood-tumor-barrier model", "assay": "ZNF22 perturbation, ChIP-qPCR, and promoter luciferase assays",
        "observation": "ZNF22 was reported to bind and repress nonqueued tight-junction genes ZO1, OCLN, and CLDN5; no queued ANXA2, CHL1, EREG, or F3 relationship was validated.",
        "exclusions": "Nonqueued target evidence was not transferred to the queued genes.", "kind": "primary_literature_regulator_level",
    },
    "znf8": {
        "symbol": "ZNF8", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/cards/ZNF8_TARGET_GENES",
        "corr": "", "model": "human GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization",
        "observation": "The GTRD-derived ZNF8 target set contains queued ADGRL2, ADIPOR2, BMP5, and BMPR1A; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Target-set membership is occupancy-only; no exact functional pair was promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "znf75a": {
        "symbol": "ZNF75A", "species": "human", "primary": "https://remap2022.univ-amu.fr/target_page/ZNF75A%3A9606",
        "corr": "", "model": "human K-562 and MCF-7 occupancy datasets", "assay": "ReMap ChIP-seq catalogue",
        "observation": "ReMap lists human ZNF75A occupancy datasets, but no queued ACTR2, ADAM17, ADIPOR1, or APLP2 edge had matched functional validation.",
        "exclusions": "ReMap factor profiling does not establish the queued target relationships.", "kind": "authoritative_binding_dataset_only",
    },
    "znf589": {
        "symbol": "ZNF589", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF589_TARGET_GENES.html",
        "corr": "https://www.ncbi.nlm.nih.gov/gene/51385", "model": "human GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization and curated gene annotation",
        "observation": "The ZNF589 target set contains queued ADAM9 and CD22; ADCYAP1 and ADGRB3 were not confirmed in the fetched set. No queued functional edge was validated.",
        "exclusions": "Occupancy-only membership and regulator annotation were not promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "znf140": {
        "symbol": "ZNF140", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF140_TARGET_GENES.html",
        "corr": "https://maayanlab.cloud/Harmonizome/gene_set/ZNF140/JASPAR%2BPredicted%2BHuman%2BTranscription%2BFactor%2BTargets%2B2025", "model": "human GTRD/JASPAR regulatory resources", "assay": "GTRD promoter occupancy and motif-predicted target catalogues",
        "observation": "The GTRD-derived ZNF140 target set contains queued ADA, ANXA2, and APLP1; APP itself was not confirmed as a target (only APP-DT appeared in the fetched page). No queued functional edge was validated.",
        "exclusions": "Predicted or occupancy-only targets were not promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "sox30": {
        "symbol": "SOX30", "species": "mouse", "primary": "https://pubmed.ncbi.nlm.nih.gov/?term=SOX30+AND+%28Adam12+OR+Adam22+OR+Adipor2+OR+Ado%29",
        "corr": "", "model": "mouse exact-pair literature search", "assay": "bounded PubMed search",
        "observation": "No qualifying exact SOX30-to-queued-target study was located in the bounded search.",
        "exclusions": "SOX30-related developmental or paralog evidence was not transferred.", "kind": "no_qualifying_primary_regulator_evidence_located",
    },
    "znf513": {
        "symbol": "ZNF513", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF513_TARGET_GENES.html",
        "corr": "https://humantfs.ccbr.utoronto.ca/all.php", "model": "human GTRD-derived promoter occupancy and TF catalogue resources", "assay": "GTRD ChIP-seq harmonization and TF annotation",
        "observation": "The ZNF513 target set contains queued ACVR1, ADORA1, BMP7, and BOC; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Binding-set and TF-catalogue records were not promoted to functional edges.", "kind": "authoritative_binding_dataset_only",
    },
    "zscan2": {
        "symbol": "ZSCAN2", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZSCAN2_TARGET_GENES.html",
        "corr": "https://www.ncbi.nlm.nih.gov/gene/54993/", "model": "human GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization and gene annotation",
        "observation": "The ZSCAN2 target set contains queued ACKR2, AHSG, APOA1, and C3; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Target-set membership and gene annotation were not promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "znf528": {
        "symbol": "ZNF528", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/cards/ZNF528_TARGET_GENES",
        "corr": "", "model": "human GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization",
        "observation": "The ZNF528 target set contains queued ADCYAP1R1, ADGRL1, APP, and CALCRL; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Target-set membership is occupancy-only; no exact functional pair was promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "barx1": {
        "symbol": "BARX1", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/BARX1_TARGET_GENES",
        "corr": "https://ismara.unibas.ch/ISMARA/scratch/IBM_v3/ismara_report/pages/BARX1.html", "model": "human regulatory target and motif-activity resources", "assay": "GTRD-derived target set and ISMARA motif/activity analysis",
        "observation": "The BARX1 target-set resource contains queued ADIPOR1; no matched perturbation or orthogonal target-expression validation was located for the four queued pairs.",
        "exclusions": "Motif activity and target-set membership were not promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "znf664": {
        "symbol": "ZNF664", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF664_TARGET_GENES.html",
        "corr": "https://www.encodeproject.org/genes/144348/", "model": "human GTRD/ENCODE regulatory resources", "assay": "GTRD promoter occupancy and ENCODE gene/regulator records",
        "observation": "The ZNF664 target set contains queued ADA, ADAM9, AMFR, and ENG; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Occupancy and gene-level records were not promoted to functional edges.", "kind": "authoritative_binding_dataset_only",
    },
    "insm2": {
        "symbol": "INSM2", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/INSM2_TARGET_GENES.html",
        "corr": "", "model": "human GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization",
        "observation": "The INSM2 target set contains queued ADGRL2 and AXL; CCN1 and CTNNB1 were not confirmed in the fetched target list. No queued functional edge was validated.",
        "exclusions": "Occupancy-only membership was not promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "dmrtb1": {
        "symbol": "DMRTB1", "species": "mouse", "primary": "https://dbarchive.biosciencedbc.jp/kyushu-u/mm10/target/Dmrtb1.5.html",
        "corr": "https://pubmed.ncbi.nlm.nih.gov/?term=DMRTB1+AND+%28Adgrl1+OR+Adipor1+OR+Cish+OR+Cx3cl1%29", "model": "mouse testis ChIP-Atlas target-resource record", "assay": "ChIP-Atlas binding-score target association",
        "observation": "ChIP-Atlas lists Cx3cl1 among potential Dmrtb1 target genes in a mouse testis record; no perturbation or orthogonal target-expression validation was located for queued pairs.",
        "exclusions": "The ChIP-Atlas potential-target record is binding/association-only and was not promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "znf680": {
        "symbol": "ZNF680", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/cards/ZNF680_TARGET_GENES.html",
        "corr": "", "model": "human GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization",
        "observation": "The ZNF680 target set contains queued ADA, BDNF, COL1A2, and FAM3C; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Target-set membership is occupancy-only; no exact functional pair was promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "znf436": {
        "symbol": "ZNF436", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/cards/ZNF436_TARGET_GENES.html",
        "corr": "", "model": "human GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization",
        "observation": "The ZNF436 target set contains queued ALK, BMP7, CD7, and CD81; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Target-set membership is occupancy-only; no exact functional pair was promoted.", "kind": "authoritative_binding_dataset_only",
    },
}

EXACT_OCCUPANCY_ONLY = {}

def add_targets(key: str, url: str, targets: list[str]) -> None:
    for target in targets:
        EXACT_OCCUPANCY_ONLY[(key, target)] = url


add_targets("znf766", REGULATORS["znf766"]["primary"], ["ADAM9", "ADGRB3", "ADIPOR1", "ADORA3"])
add_targets("znf322", REGULATORS["znf322"]["primary"], ["ANGPT2", "APLP1", "APLP2", "APOE"])
add_targets("zbtb44", REGULATORS["zbtb44"]["primary"], ["ACVR1", "ADAM22", "ADGRL1", "ADIPOR1"])
add_targets("foxd2", REGULATORS["foxd2"]["primary"], ["CD44", "CD9"])
add_targets("znf589", REGULATORS["znf589"]["primary"], ["ADAM9", "CD22"])
add_targets("znf140", REGULATORS["znf140"]["primary"], ["ADA", "ANXA2", "APLP1"])
add_targets("znf8", REGULATORS["znf8"]["primary"], ["ADGRL2", "ADIPOR2", "BMP5", "BMPR1A"])
add_targets("znf513", REGULATORS["znf513"]["primary"], ["ACVR1", "ADORA1", "BMP7", "BOC"])
add_targets("zscan2", REGULATORS["zscan2"]["primary"], ["ACKR2", "AHSG", "APOA1", "C3"])
add_targets("znf528", REGULATORS["znf528"]["primary"], ["ADCYAP1R1", "ADGRL1", "APP", "CALCRL"])
add_targets("barx1", REGULATORS["barx1"]["primary"], ["ADIPOR1"])
add_targets("znf664", REGULATORS["znf664"]["primary"], ["ADA", "ADAM9", "AMFR", "ENG"])
add_targets("insm2", REGULATORS["insm2"]["primary"], ["ADGRL2", "AXL"])
add_targets("dmrtb1", REGULATORS["dmrtb1"]["primary"], ["Cx3cl1"])
add_targets("znf680", REGULATORS["znf680"]["primary"], ["ADA", "BDNF", "COL1A2", "FAM3C"])
add_targets("znf436", REGULATORS["znf436"]["primary"], ["ALK", "BMP7", "CD7", "CD81"])


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
        info = REGULATORS[key]
        exact_lead = EXACT_OCCUPANCY_ONLY.get((key, row["target_symbol"]))
        if exact_lead:
            exact_status = "binding_dataset_only_not_promotable"
            binding_status = "authoritative_occupancy_dataset_lead"
            expression_status = "not_found_for_exact_pair"
            pair_primary = exact_lead
            pair_notes = "An authoritative binding/target-set record indicates regulator association at this exact gene, but no matched perturbation or orthogonal validation was located; do not promote."
        else:
            exact_status = "no_exact_pair_support_found_in_bounded_search"
            binding_status = "not_found_for_exact_pair"
            expression_status = "not_found_for_exact_pair"
            pair_primary = ""
            pair_notes = "No qualifying exact regulator-target assay was located in the bounded search."
        general_status = "supported_authoritative_binding_dataset_only" if info["kind"] == "authoritative_binding_dataset_only" else "supported_general_regulator_evidence"
        pairs.append({
            "review_id": f"public_tf_evidence_batch007_pair_{int(row['batch_rank']):02d}_{i:02d}",
            "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key,
            "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "source_registry": row["source_registry"],
            "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"],
            "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": search_url(info["symbol"], row["target_symbol"], row["species_scope"]), "exact_pair_status": exact_status,
            "regulator_general_evidence_status": general_status, "target_cell_presence_status": "not_established_for_exact_pair",
            "binding_or_association_status": binding_status, "downstream_expression_or_perturbation_status": expression_status,
            "downstream_activation_status": "not_assessed", "upstream_relay_status": "not_tested_for_exact_pair",
            "disposition": "retain_database_candidate_as_search_lead_only", "primary_citation": pair_primary,
            "corroborating_citation": "", "near_match_exclusions": info["exclusions"],
            "review_notes": pair_notes + " Regulator-level references are stored separately and are not evidence for this exact queued pair. " + info["observation"],
            "exportable": "false", "canonical_write_performed": "false",
        })
        if key not in seen_keys:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch007_regulator_{key}", "regulator_key": key,
                "regulator_symbol": info["symbol"], "species_scope": info["species"], "evidence_layer": "regulator_identity_and_regulatory_capacity",
                "support_kind": info["kind"], "cell_or_model": info["model"], "assay_or_perturbation": info["assay"],
                "observation": info["observation"], "effect_direction": "queued-pair direction not established", "primary_citation": info["primary"],
                "corroborating_citation": info["corr"], "route_or_module_relevance": "regulator-level evidence only",
                "target_pair_scope": "not evidence for queued exact pairs; no Module 22B edge or upstream relay inferred",
                "exportable": "false", "canonical_write_performed": "false",
                "limitations": "Regulator-level evidence does not establish the queued target relationship, target-cell presence in SCI, downstream activation, or upstream relay.",
            })
        seen_keys.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch007_ranks0625_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch007_ranks0625_regulator_register.tsv"
    summary_path = args.output_dir / "batch_007_ranks0625_evidence_review_summary.json"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    occupancy_rows = sum(row["exact_pair_status"] == "binding_dataset_only_not_promotable" for row in pairs)
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_007", "source_set_ranks_reviewed": list(range(6, 26)),
        "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen_keys), "exact_pair_support_rows": 0,
        "binding_dataset_only_not_promotable_rows": occupancy_rows, "partial_or_near_match_rows": 0,
        "general_regulator_evidence_rows": len(evidence), "exportable_pair_rows": 0,
        "canonical_writes_performed": False, "module22b_promotions_performed": False, "provenance_preserved": True,
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
        "decision": "Retain all 80 pairs as database-attributed search leads; exact binding-only leads remain non-promotable without matched perturbation or orthogonal validation.",
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
