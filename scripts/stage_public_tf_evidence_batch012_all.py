#!/usr/bin/env python3
"""Stage conservative evidence findings for all Batch 012 pairs."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/"
    "current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_012/"
    "public_tf_evidence_collection_batch_012.tsv"
)
TF_LINK_URL = "https://tflink.net/download/#interaction-gmt"
GTRD_METHOD_URL = "https://pubmed.ncbi.nlm.nih.gov/30445619/"
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

# regulator-level evidence is deliberately separate from exact queued-pair evidence
REGULATORS = {
    "znf774": ("ZNF774", "https://pubmed.ncbi.nlm.nih.gov/31659254/", "https://doi.org/10.1038/s41388-019-1075-0", "primary_literature_regulator_level", "human HCC models", "ChIP-seq, NuRD association, and perturbation", "ZNF774 has regulator-level repression and HCC phenotype evidence involving NOTCH2, not the queued targets."),
    "znf26": ("ZNF26", "https://pubmed.ncbi.nlm.nih.gov/34178996/", "https://doi.org/10.3389/fcell.2021.671211", "primary_literature_regulator_level", "human colorectal-cancer models", "knockdown and cell-cycle analysis", "ZNF26 knockdown altered CDK2, CCNE2, CDK6, and CHEK1 and reduced proliferation, not the queued targets."),
    "znf292": ("ZNF292", "https://pubmed.ncbi.nlm.nih.gov/40257863/", "https://doi.org/10.1016/j.celrep.2025.115597", "primary_literature_regulator_level", "human neural models", "genome-wide occupancy plus deficiency-linked transcriptomics", "ZNF292 has occupancy and perturbation-linked transcriptomic evidence at other neural targets, not the queued targets."),
    "znf23": ("ZNF23", "https://pubmed.ncbi.nlm.nih.gov/17137575/", "https://doi.org/10.1016/j.yexcr.2006.10.009", "primary_literature_regulator_level", "human cancer models", "ectopic expression and cell-cycle/apoptosis assays", "ZNF23 perturbation affects p27 and cell-cycle/apoptosis phenotypes, not the queued targets."),
    "znf354c": ("ZNF354C", "https://pubmed.ncbi.nlm.nih.gov/33154469/", "https://www.encodeproject.org/experiments/ENCSR289NSN/", "primary_literature_regulator_level", "human HEK293 and other cell models", "ChIP-qPCR, CRISPR/RNAi, and ChIP-seq", "ZNF354C directly regulates other reported loci including RGS5, PATL2, HAP1, and NRAV; none is a queued target."),
    "zfp90": ("ZFP90", "https://pubmed.ncbi.nlm.nih.gov/23543754/", "https://pubmed.ncbi.nlm.nih.gov/21284946/", "primary_literature_regulator_level", "human immune and cardiac models", "FIK-complex promoter occupancy/repression and NRSF-mediated repression", "ZFP90/FIK has regulator-level evidence, but IFNG/IL2 evidence uses the FIK splice product in a FOXP3/KAP1 complex rather than isolated full-length ZFP90."),
    "znf662": ("ZNF662", "https://pubmed.ncbi.nlm.nih.gov/42243650/", "", "primary_literature_regulator_level", "human ovarian-cancer model", "repression and perturbation", "ZNF662 repression evidence involves NUPR1, not ITGB2 or STAT6."),
    "tgif2": ("Tgif2", "https://pubmed.ncbi.nlm.nih.gov/16436215/", "https://www.ncbi.nlm.nih.gov/gene/228839", "primary_literature_regulator_level", "mouse developmental models", "splice-form and transcriptional-repressor characterization", "Mouse Tgif2 has transcriptional-repressor evidence, but no queued target was functionally validated."),
    "znf677": ("ZNF677", "https://pubmed.ncbi.nlm.nih.gov/35678231/", "https://www.ncbi.nlm.nih.gov/gene/342926", "primary_literature_regulator_level", "human renal-cancer models", "transcriptional repression and perturbation", "ZNF677 repression evidence involves CDKN3, not the queued targets."),
    "zfp28": ("ZFP28", "https://pubmed.ncbi.nlm.nih.gov/12127974/", "https://pubmed.ncbi.nlm.nih.gov/19329283/", "primary_literature_regulator_level", "human expression and melanoma models", "gene characterization and expression/phenotype studies", "ZFP28 has human regulator-level evidence, but no queued target pair was functionally validated."),
    "znf322": ("ZNF322", "https://pubmed.ncbi.nlm.nih.gov/15555580/", "https://pubmed.ncbi.nlm.nih.gov/32929330/", "primary_literature_regulator_level", "human ZNF322/ZNF322A models", "transcriptional activity and cancer-associated perturbation", "Human ZNF322 evidence was not transferred to the queued mouse pairs."),
    "znf704": ("ZNF704", "https://pubmed.ncbi.nlm.nih.gov/32651256/", "https://pubmed.ncbi.nlm.nih.gov/34188544/", "primary_literature_regulator_level", "human cancer models", "repressor/oncogenic perturbation studies", "ZNF704 has regulator-level repressor evidence, but no queued target pair was validated."),
    "znf777": ("ZNF777", "https://pubmed.ncbi.nlm.nih.gov/25560148/", "https://pubmed.ncbi.nlm.nih.gov/31856708/", "primary_literature_regulator_level", "human cell and cancer models", "FAM129A-associated function and transcriptional repression", "ZNF777 evidence involves FAM129A and DUF3669, not the queued targets."),
    "znf548": ("ZNF548", "https://pubmed.ncbi.nlm.nih.gov/28273063/", "https://remap2022.univ-amu.fr/target_page/ZNF548%3A9606", "authoritative_binding_dataset_only", "human KRAB-ZNF ChIP-exo and binding resources", "ChIP-exo and regulator-level binding annotations", "ZNF548 has regulator-level binding records, but no queued target pair has functional validation."),
    "hox a13": ("HOXA13", "https://pmc.ncbi.nlm.nih.gov/articles/PMC1301594/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2367452/", "primary_literature_regulator_level", "mouse developmental models", "developmental target perturbation and expression studies", "HOXA13 regulates other developmental loci; mouse Hoxa13-Aldh1a2 is kept only as an ortholog/model near match for the human row."),
    "hoxa13": ("HOXA13", "https://pmc.ncbi.nlm.nih.gov/articles/PMC1301594/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2367452/", "primary_literature_regulator_level", "mouse developmental models", "developmental target perturbation and expression studies", "HOXA13 regulates other developmental loci; mouse Hoxa13-Aldh1a2 is kept only as an ortholog/model near match for the human row."),
    "znf560": ("ZNF560", TF_LINK_URL, "", "authoritative_binding_dataset_only", "human TFLink/GTRD candidate set", "species-matched target-set membership", "No qualifying regulator-level functional evidence was verified for the queued targets in this bounded pass."),
    "znf169": ("ZNF169", TF_LINK_URL, "", "authoritative_binding_dataset_only", "human TFLink/GTRD candidate set", "species-matched target-set membership", "No qualifying regulator-level functional evidence was verified for the queued targets in this bounded pass."),
    "znf510": ("ZNF510", TF_LINK_URL, "", "authoritative_binding_dataset_only", "human TFLink/GTRD candidate set", "species-matched target-set membership", "No qualifying regulator-level functional evidence was verified for the queued targets in this bounded pass."),
    "znf354a": ("ZNF354A", TF_LINK_URL, "", "authoritative_binding_dataset_only", "human TFLink/GTRD candidate set", "species-matched target-set membership", "No qualifying regulator-level functional evidence was verified for the queued targets in this bounded pass."),
    "znf493": ("ZNF493", "https://www.ncbi.nlm.nih.gov/gene/284443", "", "authoritative_binding_dataset_only", "human KRAB/C2H2 zinc-finger annotation and binding resources", "gene annotation and target-set membership", "ZNF493 identity and candidate binding support were verified, but no queued target was functionally validated."),
    "znf404": ("ZNF404", "https://pmc.ncbi.nlm.nih.gov/articles/PMC403638/", "", "primary_literature_regulator_level", "human KRAB/C2H2 zinc-finger locus", "locus characterization", "ZNF404 locus/regulator evidence exists, but no queued target was validated."),
    "znf214": ("ZNF214", "https://www.ncbi.nlm.nih.gov/gene/7761", "", "authoritative_binding_dataset_only", "human annotation and binding resources", "gene annotation and target-set membership", "ZNF214 annotation supports regulator identity, but no queued target was functionally validated."),
    "znf19": ("ZNF19", "https://jaspar.elixir.no/matrix/UN0599.2/", "", "authoritative_binding_dataset_only", "human DNA-binding profile resource", "motif/DNA-binding profile", "ZNF19 DNA-binding capacity is supported by a profile resource, not by queued target regulation."),
    "barx1": ("Barx1", "https://pubmed.ncbi.nlm.nih.gov/15809042/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4529797/", "primary_literature_regulator_level", "mouse developmental models", "developmental perturbation and ChIP occupancy", "Mouse Barx1 regulates nonqueued Wnt-related loci; no queued target was functionally validated."),
    "znf514": ("ZNF514", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12593293/", "", "primary_literature_regulator_level", "human esophageal-cancer model", "knockdown and pathway/phenotype analysis", "ZNF514 perturbation affects cancer phenotypes and broad pathways, not the queued target pairs."),
}

SET_URL = {
    "znf774": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF774_TARGET_GENES.html",
    "znf26": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF26_TARGET_GENES.html",
    "znf292": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF292_TARGET_GENES.html",
    "znf23": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF23_TARGET_GENES.html",
    "znf354c": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF354C_TARGET_GENES.html",
    "znf493": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF493_TARGET_GENES.html",
    "tgif2": "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/TGIF2_TARGET_GENES.html",
    "znf677": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF677_TARGET_GENES.html",
    "zfp28": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZFP28_TARGET_GENES.html",
    "znf560": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF560_TARGET_GENES.html",
    "hoxa13": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/HOXA13_TARGET_GENES.html",
    "znf169": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF169_TARGET_GENES.html",
    "znf510": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF510_TARGET_GENES.html",
    "znf354a": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF354A_TARGET_GENES.html",
    "znf404": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF404_TARGET_GENES.html",
    "znf214": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF214_TARGET_GENES.html",
    "znf19": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF19_TARGET_GENES.html",
    "barx1": "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/BARX1_TARGET_GENES.html",
    "znf514": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF514_TARGET_GENES.html",
}

BINDING_KEYS = {
    "znf774", "znf26", "znf292", "znf23", "znf354c", "znf493", "tgif2", "znf677",
    "znf560", "hoxa13", "znf169", "znf354a", "znf404", "znf214", "znf19", "barx1", "znf514",
}
DATABASE_ONLY_KEYS = {"zfp28", "znf322", "znf704", "znf777", "znf548"}


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


def classify(row: dict[str, str]) -> dict[str, str]:
    key = row["regulator_key"]
    target = row["target_symbol"].lower()
    symbol, general_primary, general_corr, kind, model, assay, observation = REGULATORS[key]
    set_url = SET_URL.get(key, TF_LINK_URL)
    status = "binding_dataset_only_not_promotable"
    primary = set_url
    corr = GTRD_METHOD_URL
    cell = "not_established_for_exact_pair"
    binding = "species_matched_GTRD_or_TFLink_target_set_membership"
    downstream = "not_found_for_exact_pair"
    disposition = "retain_as_staging_search_lead_only"
    exclusions = "Regulator-level evidence at nonqueued targets, orthologs, related isoforms, reverse-direction relationships, and lineage-driver use was not transferred to queued edges."
    notes = "The species-matched target-set membership is retained as an occupancy/search lead; it does not establish causal direction, target-cell presence, downstream activation, or upstream relay. No exact target-specific functional validation was located in this bounded pass."

    if key == "zfp90" and target in {"ifng", "il2"}:
        status = "contextual_near_match_not_promotable"
        primary = "https://pmc.ncbi.nlm.nih.gov/articles/PMC4197931/"
        corr = SET_URL.get(key, TF_LINK_URL)
        binding = "FIK_FOXP3_KAP1_complex_promoter_occupancy_not_isolated_full_length_ZFP90"
        downstream = "FIK_complex_repressed_IFNG_or_IL2_after_stimulation"
        disposition = "retain_contextual_near_match_separately"
        exclusions = "FIK is an alternatively spliced ZFP90-derived product tested in a FOXP3/KAP1 complex; this does not establish isolated full-length ZFP90 regulation."
        notes = "The primary study reports promoter occupancy and repression of this target by the FOXP3-FIK-KAP1 complex. Because the tested regulator is the FIK splice product in a complex rather than isolated full-length ZFP90, this is contextual evidence only and is not promotable."
    elif key == "znf662":
        status = "no_exact_pair_support_found_in_bounded_search"
        primary = "https://www.ncbi.nlm.nih.gov/gene/389114"
        corr = ""
        binding = "no_exact_authoritative_pair_record_located"
        disposition = "retain_bounded_negative_only"
        notes = "No exact ZNF662-target primary assay or authoritative pair record was located in this bounded pass; TFLink membership remains a search lead only."
    elif key == "hoxa13" and target == "aldh1a2":
        status = "ortholog_model_near_match_not_promotable"
        primary = "https://pubmed.ncbi.nlm.nih.gov/23553814/"
        corr = SET_URL[key]
        binding = "human_GTRD_occupancy_plus_mouse_Hoxa13_Aldh1a2_functional_evidence"
        downstream = "mouse_Hoxa13_Aldh1a2_relationship_reported"
        disposition = "retain_ortholog_model_near_match_separately"
        cell = "mouse_developmental_model_not_SCI_target_cell"
        exclusions = "Mouse Hoxa13-Aldh1a2 evidence was not transferred to the human pair or to SCI target-cell context."
        notes = "A mouse study reports Hoxa13-Aldh1a2 evidence, while the queued row is human. This is a useful ortholog/model near match but is not an exact human or SCI-cell promotion."
    elif key == "znf510" and target == "ada":
        status = "regulator_swapped_near_match_not_promotable"
        primary = "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF577_TARGET_GENES.html"
        corr = ""
        binding = "target_found_under_ZNF577_not_ZNF510"
        disposition = "retain_regulator_swapped_near_match_separately"
        notes = "ADA was found in a ZNF577 target set, not as evidence for ZNF510; the regulator-swapped near match is explicitly excluded."
    elif key == "znf510" and target == "abcc12":
        status = "regulator_swapped_near_match_not_promotable"
        primary = "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/TOP2B_TARGET_GENES.html"
        corr = ""
        binding = "target_found_under_TOP2B_not_ZNF510"
        disposition = "retain_regulator_swapped_near_match_separately"
        notes = "ABCC12 was found in a TOP2B target set, not as evidence for ZNF510; the regulator-swapped near match is explicitly excluded."
    elif key == "znf354a" and target == "c17orf64":
        status = "database_membership_only_not_promotable"
        primary = TF_LINK_URL
        corr = ""
        binding = "TFLink_snapshot_membership_only"
        disposition = "retain_database_candidate_as_search_lead_only"
        notes = "TFLink membership was retained as a search lead, but no direct authoritative binding or functional record for ZNF354A-C17orf64 was located."
    elif key in DATABASE_ONLY_KEYS:
        status = "database_membership_only_not_promotable"
        primary = TF_LINK_URL if not (key == "zfp28" and target == "plaur") else SET_URL[key]
        corr = ""
        binding = "TFLink_snapshot_membership_only"
        if key == "znf548" and target == "arl4a":
            primary = "https://ccsm.uth.edu/DRMref/gene_analysis_result.cgi?page=page&quick_search=ARL4A&type=quick_search"
            corr = "https://pubmed.ncbi.nlm.nih.gov/28273063/"
            binding = "motif_annotation_only_not_direct_occupancy"
            notes = "DRMref records a ZNF548 motif annotation for ARL4A; the underlying ChIP-exo resource does not establish direct ARL4A regulation in this row."
        else:
            notes = "The TFLink membership is retained as a database search lead only; no pair-specific functional or directly traceable occupancy evidence was established in this bounded pass."
        disposition = "retain_database_candidate_as_search_lead_only"

    return {
        "symbol": symbol, "general_primary": general_primary, "general_corr": general_corr, "kind": kind,
        "model": model, "assay": assay, "observation": observation, "status": status, "primary": primary,
        "corr": corr, "cell": cell, "binding": binding, "downstream": downstream, "disposition": disposition,
        "exclusions": exclusions, "notes": notes,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_BATCH.parent)
    args = parser.parse_args()
    rows = read_tsv(args.batch)
    if len(rows) != 96:
        raise SystemExit(f"expected 96 rows, found {len(rows)}")
    pairs: list[dict[str, str]] = []
    evidence: list[dict[str, str]] = []
    seen: set[str] = set()
    for row in rows:
        key = row["regulator_key"]
        if key not in REGULATORS:
            raise SystemExit(f"missing evidence map for {key}")
        info = classify(row)
        row_status = "supported_general_regulator_evidence"
        if info["kind"] == "authoritative_binding_dataset_only":
            row_status = "supported_general_or_authoritative_regulator_evidence"
        pairs.append({
            "review_id": f"public_tf_evidence_batch012_pair_{int(row['batch_rank']):02d}_{row['target_rank']}",
            "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key,
            "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "source_registry": row["source_registry"],
            "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"],
            "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": search_url(info["symbol"], row["target_symbol"], row["species_scope"]),
            "exact_pair_status": info["status"], "regulator_general_evidence_status": row_status,
            "target_cell_presence_status": info["cell"], "binding_or_association_status": info["binding"],
            "downstream_expression_or_perturbation_status": info["downstream"],
            "downstream_activation_status": "not_established_for_SCI_target_cell",
            "upstream_relay_status": "not_tested_for_exact_pair", "disposition": info["disposition"],
            "primary_citation": info["primary"], "corroborating_citation": info["corr"],
            "near_match_exclusions": info["exclusions"], "review_notes": info["notes"] + " " + info["observation"],
            "exportable": "false", "canonical_write_performed": "false",
        })
        if key not in seen:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch012_regulator_{key}", "regulator_key": key,
                "regulator_symbol": info["symbol"], "species_scope": row["species_scope"],
                "evidence_layer": "regulator_identity_and_regulatory_capacity", "support_kind": info["kind"],
                "cell_or_model": info["model"], "assay_or_perturbation": info["assay"], "observation": info["observation"],
                "effect_direction": "queued-pair direction not established", "primary_citation": info["general_primary"],
                "corroborating_citation": info["general_corr"], "route_or_module_relevance": "regulator-level evidence only",
                "target_pair_scope": "not evidence for unrelated queued exact pairs; no upstream relay inferred",
                "exportable": "false", "canonical_write_performed": "false",
                "limitations": "Regulator-level evidence does not establish SCI target-cell presence, exact queued-target direction, downstream activation, or upstream relay. Contextual and ortholog/model near matches remain staging-only.",
            })
        seen.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch012_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch012_regulator_register.tsv"
    summary_path = args.output_dir / "batch_012_evidence_review_summary.json"
    report_path = args.output_dir / "EVIDENCE_REVIEW_BATCH012.md"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    status_counts: dict[str, int] = {}
    for item in pairs:
        status_counts[item["exact_pair_status"]] = status_counts.get(item["exact_pair_status"], 0) + 1
    pair_keys = {(item["regulator_key"], item["target_symbol"], item["species_scope"], item["source_record_id"]) for item in pairs}
    exact_support = status_counts.get("functional_direct_binding_promotion_candidate", 0)
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_012", "source_set_ranks_reviewed": list(range(1, 26)),
        "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen), "unique_provenance_aware_pairs": len(pair_keys),
        "exact_pair_status_counts": status_counts, "regulator_register_rows": len(evidence), "exact_pair_support_rows": exact_support,
        "promotion_candidate_rows": exact_support, "partial_or_near_match_rows": sum(v for k, v in status_counts.items() if "near_match" in k),
        "binding_dataset_only_not_promotable_rows": status_counts.get("binding_dataset_only_not_promotable", 0),
        "database_membership_only_not_promotable_rows": status_counts.get("database_membership_only_not_promotable", 0),
        "bounded_negative_rows": status_counts.get("no_exact_pair_support_found_in_bounded_search", 0), "exportable_pair_rows": 0,
        "canonical_writes_performed": False, "module22b_promotions_performed": False, "provenance_preserved": True,
        "limitations": ["TFLink/GTRD/MSigDB membership is database or occupancy evidence, not causal regulation.", "Exact pair negatives are bounded-search results, not claims of global absence.", "Contextual splice-product, ortholog/model, motif-only, and regulator-swapped evidence is kept separate and not transferred.", "Target-cell presence, downstream activation, and upstream relay remain unestablished for all queued pairs.", "No canonical or Module 22B write was performed."],
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report = [
        "# Evidence review: public TF batch 012", "", "Reviewed 96 exact regulator-target-species pairs across 25 selected TFLink source sets.", "",
        f"- **{len(pairs)} / 96** pairs were reviewed.",
        f"- **{summary['exact_pair_support_rows']}** exact pairs met the promotion-candidate threshold.",
        f"- **{summary['binding_dataset_only_not_promotable_rows']}** pairs had species-matched GTRD/MSigDB occupancy leads.",
        f"- **{summary['database_membership_only_not_promotable_rows']}** pairs remained database-membership-only leads.",
        f"- **{summary['partial_or_near_match_rows']}** contextual/ortholog/regulator-swapped near matches were kept separate.",
        f"- **{summary['bounded_negative_rows']}** pairs had no exact support located in the bounded search.",
        "- **0** rows are exportable; no canonical or Module 22B writes were performed.", "",
        "No queued pair had exact target-level functional validation in this bounded pass. ZFP90-derived FIK evidence for IFNG/IL2 and mouse Hoxa13-Aldh1a2 evidence are explicitly non-promotable near matches.", "",
    ]
    report_path.write_text("\n".join(report), encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
