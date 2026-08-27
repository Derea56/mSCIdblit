#!/usr/bin/env python3
"""Stage conservative evidence findings for all Batch 014 pairs."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_014/"
    "public_tf_evidence_collection_batch_014.tsv"
)
TF_LINK_URL = "https://tflink.net/download/#interaction-gmt"
GTRD_URL = "https://pubmed.ncbi.nlm.nih.gov/30445619/"
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
    "znf136": ("ZNF136", "https://www.ncbi.nlm.nih.gov/gene/7695", "", "authoritative_identity_catalog", "human annotation and TFLink/GTRD", "KRAB/C2H2 annotation and binding records", "ZNF136 has regulator identity/occupancy support; no queued target direction was established."),
    "znf445": ("ZNF445", "https://www.ncbi.nlm.nih.gov/gene/353274", "https://pubmed.ncbi.nlm.nih.gov/30602440/", "primary_literature_regulator_level", "human and mouse imprinting models", "DNA binding and epigenetic repression", "ZNF445/Zfp445 evidence concerns imprinting-control regions, not the queued targets."),
    "znf776": ("ZNF776", "https://www.ncbi.nlm.nih.gov/gene/284309", "https://www.uniprot.org/uniprotkb/Q68DI1/entry", "authoritative_identity_catalog", "human annotation and binding resources", "putative transcription-regulator annotation", "ZNF776 identity/occupancy support does not establish queued target function."),
    "thap4": ("Thap4", "https://www.ncbi.nlm.nih.gov/gene/67026", "https://www.uniprot.org/uniprotkb/Q6P3Z3/entry", "authoritative_identity_catalog", "mouse THAP/DNA-binding annotations", "regulator annotation", "Thap4 identity support does not establish Cenpo, Daxx, Irgq, or Knstrn regulation."),
    "znf419": ("ZNF419", "https://www.ncbi.nlm.nih.gov/gene/79744", "https://www.uniprot.org/uniprotkb/Q96HQ0/entry", "authoritative_identity_catalog", "human TF/DNA-binding records", "identity and binding annotation", "ZNF419 identity/occupancy support does not establish queued target direction."),
    "znf491": ("ZNF491", "https://www.ncbi.nlm.nih.gov/gene/126069", "", "authoritative_identity_catalog", "human annotation and GTRD", "DNA-binding annotation and target-set membership", "ZNF491 has identity/occupancy support, but no queued target was functionally validated."),
    "repin1": ("REPIN1", "https://www.nature.com/articles/ijo2017172", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6413308/", "primary_literature_regulator_level", "human adipose and liver models", "DNA-binding and metabolic perturbation studies", "REPIN1 perturbation changes metabolic phenotypes, not the queued targets."),
    "tfdp2": ("TFDP2", "https://pubmed.ncbi.nlm.nih.gov/7784053/", "https://pubmed.ncbi.nlm.nih.gov/24607859/", "primary_literature_regulator_level", "human and mouse erythroid models", "E2F-coregulator characterization and knockdown", "TFDP2 regulator biology does not establish the queued human target pairs."),
    "zfp37": ("ZFP37", "https://pubmed.ncbi.nlm.nih.gov/9585434/", "https://pubmed.ncbi.nlm.nih.gov/1614869/", "primary_literature_regulator_level", "human and mouse expression models", "putative TF characterization and expression", "ZFP37 regulator identity does not establish queued target function."),
    "zscan26": ("ZSCAN26", "https://pubmed.ncbi.nlm.nih.gov/1569959/", "https://tflink.net/protein/q16670/", "primary_literature_regulator_level", "human biochemical binding model", "serum-response-element zinc-finger binding", "ZSCAN26/SRE-ZBP binding evidence is regulator-level and does not validate queued targets."),
    "znf473": ("ZNF473", "https://pubmed.ncbi.nlm.nih.gov/33326746/", "https://www.encodeproject.org/experiments/ENCSR567XAM/", "primary_literature_regulator_level", "human ChIP/synthetic-reporter models", "ChIP-seq and regulator-function assays", "ZNF473 has regulator-level occupancy/function evidence, but no queued target effect was established."),
    "znf658": ("ZNF658", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4333095/", "", "primary_literature_regulator_level", "human zinc-responsive models", "ZTRE binding and repression assays", "ZNF658 directly regulates nonqueued zinc-responsive targets; no queued target was validated."),
    "hoxb9": ("HOXB9", "https://pubmed.ncbi.nlm.nih.gov/1347944/", "https://pubmed.ncbi.nlm.nih.gov/32015336/", "primary_literature_regulator_level", "Xenopus/mouse promoter and human tumor models", "promoter reporter and expression/phenotype studies", "HOXB9 has regulator-level evidence, but NCAM1 evidence is cross-species/model-mismatched."),
    "znf747": ("ZNF747", "https://www.ncbi.nlm.nih.gov/gene/65988", "https://pubmed.ncbi.nlm.nih.gov/18976975/", "authoritative_identity_catalog", "human annotation and siRNA phenotype", "domain annotation and unrelated phenotype study", "ZNF747 identity/phenotype records do not validate STAT6."),
    "sox3": ("SOX3", "https://pubmed.ncbi.nlm.nih.gov/8111369/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7174399/", "primary_literature_regulator_level", "human and mouse developmental models", "identity, expression, and developmental regulator studies", "SOX3 regulator-level evidence does not establish the queued target pairs."),
    "rax2": ("RAX2", "https://pubmed.ncbi.nlm.nih.gov/32015336/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6997171/", "primary_literature_regulator_level", "human glioblastoma model", "DLG5 promoter binding and activation", "RAX2 directly regulates nonqueued DLG5; this does not validate queued targets."),
    "rxrg": ("Rxrg", "https://pubmed.ncbi.nlm.nih.gov/7988448/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3634743/", "primary_literature_regulator_level", "mouse RXR binding/retinoid models", "DNA-binding specificity and agonist response", "Rxrg has regulator-level evidence, but no queued target was functionally validated."),
    "zfp82": ("ZFP82", "https://pubmed.ncbi.nlm.nih.gov/41053060/", "https://pubmed.ncbi.nlm.nih.gov/30211622/", "primary_literature_regulator_level", "human cancer/inflammatory models", "HDAC3/NF-kB mechanism and phenotype studies", "ZFP82 evidence involves nonqueued HDAC3/NF-kB relationships."),
    "znf502": ("ZNF502", "https://pubmed.ncbi.nlm.nih.gov/37902191/", "", "primary_literature_regulator_level", "human oral-cancer model", "VIM-axis perturbation", "ZNF502 evidence involves nonqueued VIM, not queued targets."),
    "znf112": ("ZNF112", "https://humantfs.ccbr.utoronto.ca/all.php", "", "authoritative_identity_catalog", "human TF catalog", "C2H2 TF annotation", "ZNF112 identity support does not establish queued target regulation."),
    "hivep3": ("HIVEP3", "https://pubmed.ncbi.nlm.nih.gov/12193271/", "", "primary_literature_regulator_level", "human HIVEP3/KRC DNA-binding model", "site-selection and DNA-binding assays", "HIVEP3 binding-capacity evidence does not establish queued target regulation."),
    "znf221": ("ZNF221", "https://humantfs.ccbr.utoronto.ca/all.php", "", "authoritative_identity_catalog", "human TF catalog", "C2H2 TF annotation", "ZNF221 identity support does not establish queued target regulation."),
    "znf513": ("Znf513", "https://pubmed.ncbi.nlm.nih.gov/20797688/", "https://pubmed.ncbi.nlm.nih.gov/37752101/", "primary_literature_regulator_level", "mouse retinal and human cancer models", "ChIP, promoter binding, and perturbation studies", "ZNF513 has direct binding/function evidence at some loci; exact queued pairs are binding-only."),
    "znf138": ("ZNF138", "https://pubmed.ncbi.nlm.nih.gov/7557990/", "https://humantfs.ccbr.utoronto.ca/all.php", "authoritative_identity_catalog", "human zinc-finger identity records", "gene isolation and TF annotation", "ZNF138 identity does not establish queued target regulation."),
    "znf544": ("ZNF544", "https://pubmed.ncbi.nlm.nih.gov/41935629/", "", "primary_literature_regulator_level", "human HCC and mouse orthotopic models", "SPATS2 promoter binding, perturbation, and phenotype", "ZNF544 directly regulates nonqueued SPATS2, not the queued targets."),
    "mnx1": ("MNX1", "https://pubmed.ncbi.nlm.nih.gov/41099694/", "https://pubmed.ncbi.nlm.nih.gov/41554854/", "primary_literature_regulator_level", "human and mouse neuronal/AML models", "occupancy and neuronal gene regulation", "MNX1 evidence involves other loci, not the queued targets."),
    "bbx": ("BBX", "https://pubmed.ncbi.nlm.nih.gov/24885382/", "https://pubmed.ncbi.nlm.nih.gov/32537777/", "primary_literature_regulator_level", "human and mouse odontoblast models", "overexpression/knockdown and knockout", "BBX regulator-level evidence does not establish GALNT14 or TAS2R13 regulation."),
    "bhlha15": ("BHLHA15/MIST1", "https://pubmed.ncbi.nlm.nih.gov/20038531/", "", "primary_literature_regulator_level", "human and mouse secretory-cell models", "ChIP, induction/loss, and dominant-negative RAB26 assay", "MIST1/BHLHA15 exact RAB26/RAB3D evidence is kept separate and is not transferred to SCI context."),
    "hic2": ("HIC2", "https://pubmed.ncbi.nlm.nih.gov/35941187/", "", "primary_literature_regulator_level", "human erythroid model", "BCL11A enhancer binding/repression and perturbation", "HIC2 directly regulates nonqueued BCL11A, not ALPK1 or CHD1."),
    "hoxd8": ("HOXD8", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3616285/", "https://pubmed.ncbi.nlm.nih.gov/7926763/", "primary_literature_regulator_level", "human and developmental HOX models", "functional interaction and promoter studies", "HOXD8 evidence does not establish binding/direction for the queued pairs."),
    "isl2": ("ISL2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9444162/", "", "primary_literature_regulator_level", "human retinal/developmental models", "TF expression and developmental studies", "ISL2 regulator-level evidence does not establish queued target regulation."),
    "znf155": ("ZNF155", "https://www.encodeproject.org/experiments/ENCSR801BWR/", "", "authoritative_binding_dataset_only", "human HEK293 ChIP-seq", "regulator-level ChIP-seq", "ZNF155 occupancy capacity does not establish C1orf159 or TSC22D4 regulation."),
    "znf211": ("ZNF211", "https://remap2022.univ-amu.fr/biotype_page/HEK293%3A9606", "", "authoritative_binding_dataset_only", "human HEK293 ChIP-seq resources", "regulator-level occupancy", "ZNF211 occupancy capacity does not establish queued target direction/function."),
    "znf248": ("ZNF248", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11375549/", "", "primary_literature_regulator_level", "human colorectal-cancer model", "ZEB1 binding/function", "ZNF248 directly regulates nonqueued ZEB1, not TRAV12-1 or TRPM4."),
}

SET_URL = {
    "znf136": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF136_TARGET_GENES.html", "znf445": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF445_TARGET_GENES.html", "znf776": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF776_TARGET_GENES.html", "thap4": "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/THAP4_TARGET_GENES.html", "znf419": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF419_TARGET_GENES.html",
    "znf491": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF491_TARGET_GENES.html", "repin1": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/REPIN1_TARGET_GENES.html", "tfdp2": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/TFDP2_TARGET_GENES.html", "zfp37": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZFP37_TARGET_GENES.html", "zscan26": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZSCAN26_TARGET_GENES.html",
    "znf473": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF473_TARGET_GENES.html", "sox3": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/SOX3_TARGET_GENES.html", "rax2": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/RAX2_TARGET_GENES.html", "rxrg": "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/RXRG_TARGET_GENES.html", "zfp82": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZFP82_TARGET_GENES.html", "znf502": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF502_TARGET_GENES.html", "foxr2": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/FOXR2_TARGET_GENES.html", "znf544": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF544_TARGET_GENES.html", "mnx1": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/MNX1_TARGET_GENES.html", "zbtb49": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZBTB49_TARGET_GENES.html", "znf211": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF211_TARGET_GENES.html", "znf248": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF248_TARGET_GENES.html",
}

BINDING_KEYS = set(SET_URL) | {"znf513"}
DATABASE_ONLY_KEYS = {"bbx", "hic2", "isl2", "znf155", "znf211", "znf248", "znf658", "znf747", "znf112", "hivep3", "znf221", "znf138", "znf837"}


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
    status = "binding_dataset_only_not_promotable" if key in BINDING_KEYS else "database_membership_only_not_promotable"
    primary = SET_URL.get(key, TF_LINK_URL)
    corr = GTRD_URL if key in BINDING_KEYS else ""
    binding = "species_matched_GTRD_or_TFLink_occupancy_lead" if key in BINDING_KEYS else "TFLink_snapshot_membership_only"
    downstream = "not_found_for_exact_pair"
    disposition = "retain_as_staging_search_lead_only"
    cell = "not_established_for_exact_pair"
    exclusions = "Regulator-level evidence at nonqueued targets, orthologs, paralogs, reverse-direction relationships, and cross-species models was not transferred."
    notes = "The species-matched target-set or occupancy result is retained as a search lead only; it does not establish causal direction, target-cell presence, downstream activation, or upstream relay. No exact target-specific functional validation was located in this bounded pass."

    if key == "znf513":
        status = "direct_binding_only_not_promotable"
        primary = "https://pubmed.ncbi.nlm.nih.gov/20797688/"
        corr = "https://pmc.ncbi.nlm.nih.gov/articles/PMC7710524/" if target == "rbp3" else ""
        binding = "WT_ZNF513_direct_promoter_ChIP_binding_mutant_lost_binding"
        notes = "The mouse retinal study reports WT ZNF513 binding at the queued promoter; no activation/repression direction or SCI target-cell context was established. RBP3 is the alias-normalized IRBP target."
    elif key == "bhlha15" and target == "rab26":
        status = "functional_direct_binding_promotion_candidate"
        primary = "https://pubmed.ncbi.nlm.nih.gov/20038531/"
        corr = ""
        binding = "MIST1_ChIP_at_RAB26_regulatory_site"
        downstream = "MIST1_induction_increased_RAB26_mouse_loss_lowered_RAB26_and_dominant_negative_RAB26_blocked_granule_phenotype"
        disposition = "promotion_candidate_pending_SCI_target_cell_context"
        cell = "human_and_mouse_secretory_cell_models_not_SCI_target_cell"
        exclusions = "The exact MIST1/BHLHA15-RAB26 study is retained as staging evidence; secretory-cell context was not transferred to SCI target-cell context."
        notes = "MIST1/BHLHA15 binds the RAB26 regulatory site, induction increases RAB26, mouse loss lowers RAB26, and dominant-negative RAB26 blocks the MIST1-induced secretory-granule phenotype. This is a strong exact pair but remains staging-only pending SCI-cell context."
    elif key == "bhlha15" and target == "rab3d":
        status = "partial_functional_binding_support_not_promotable"
        primary = "https://pubmed.ncbi.nlm.nih.gov/20038531/"
        corr = ""
        binding = "MIST1_ChIP_at_RAB3D_regulatory_site"
        downstream = "MIST1_induction_increased_RAB3D_mouse_loss_lowered_RAB3D_without_RAB3D_specific_rescue"
        disposition = "retain_partial_exact_pair_support_separately"
        cell = "human_and_mouse_secretory_cell_models_not_SCI_target_cell"
        notes = "The MIST1 paper supports direct binding and expression change for RAB3D, but lacks RAB3D-specific loss/rescue; it is not promoted to the stronger exact functional tier."
    elif key == "hoxd8" and target in {"cdkn2a", "hoxd9"}:
        status = "contextual_near_match_not_promotable"
        primary = "https://pmc.ncbi.nlm.nih.gov/articles/PMC3616285/" if target == "cdkn2a" else "https://pubmed.ncbi.nlm.nih.gov/7926763/"
        corr = ""
        binding = "functional_or_interaction_evidence_without_exact_target_binding_or_resolved_direction"
        downstream = "direction_or_expression_mechanism_unresolved"
        disposition = "retain_contextual_near_match_separately"
        notes = "HOXD8 evidence concerns functional interaction or conflicting direction without a demonstrated exact target-promoter binding mechanism; it is not promotable as a direct edge."
    elif key == "isl2" and target == "foxp2":
        status = "contextual_near_match_not_promotable"
        primary = "https://maayanlab.cloud/Harmonizome/gene_set/FOXP2/ENCODE%2BTranscription%2BFactor%2BTargets"
        binding = "reverse_direction_FOXP2_to_ISL2_not_ISL2_to_FOXP2"
        disposition = "retain_contextual_near_match_separately"
        notes = "The available target resource supports the reverse direction FOXP2-to-ISL2, not the queued ISL2-to-FOXP2 relationship."
    elif key == "bhlha15":
        pass
    elif key == "znf155":
        primary = TF_LINK_URL
        notes = "TFLink membership is retained as a search lead; an ENCODE regulator-level ChIP-seq record exists, but queued target-specific binding, direction, and function were not established."
    elif key == "znf211":
        status = "binding_dataset_only_not_promotable"
        primary = SET_URL[key]
        corr = GTRD_URL
        binding = "human_GTRD_promoter_occupancy_lead"
        notes = "The human ZNF211 target set provides promoter occupancy annotation only; no target-specific perturbation or direction was established."
    elif key == "znf248":
        status = "binding_dataset_only_not_promotable"
        primary = SET_URL[key]
        corr = GTRD_URL
        binding = "human_GTRD_promoter_occupancy_lead"
        notes = "The human ZNF248 target set provides promoter occupancy annotation only; nonqueued ZEB1 evidence was not transferred."

    return {"symbol": symbol, "general_primary": general_primary, "general_corr": general_corr, "kind": kind, "model": model, "assay": assay, "observation": observation, "status": status, "primary": primary, "corr": corr, "cell": cell, "binding": binding, "downstream": downstream, "disposition": disposition, "exclusions": exclusions, "notes": notes}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_BATCH.parent)
    args = parser.parse_args()
    rows = read_tsv(args.batch)
    if len(rows) != 81:
        raise SystemExit(f"expected 81 rows, found {len(rows)}")
    pairs: list[dict[str, str]] = []
    evidence: list[dict[str, str]] = []
    seen: set[str] = set()
    for row in rows:
        key = row["regulator_key"]
        if key not in REGULATORS:
            raise SystemExit(f"missing evidence map for {key}")
        info = classify(row)
        pairs.append({
            "review_id": f"public_tf_evidence_batch014_pair_{int(row['batch_rank']):02d}_{row['target_rank']}", "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key, "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "source_registry": row["source_registry"], "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"], "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"], "exact_pair_search_url": search_url(info["symbol"], row["target_symbol"], row["species_scope"]), "exact_pair_status": info["status"], "regulator_general_evidence_status": "supported_general_or_authoritative_regulator_evidence", "target_cell_presence_status": info["cell"], "binding_or_association_status": info["binding"], "downstream_expression_or_perturbation_status": info["downstream"], "downstream_activation_status": "not_established_for_SCI_target_cell", "upstream_relay_status": "not_tested_for_exact_pair", "disposition": info["disposition"], "primary_citation": info["primary"], "corroborating_citation": info["corr"], "near_match_exclusions": info["exclusions"], "review_notes": info["notes"] + " " + info["observation"], "exportable": "false", "canonical_write_performed": "false",
        })
        if key not in seen:
            evidence.append({"evidence_id": f"public_tf_evidence_batch014_regulator_{key}", "regulator_key": key, "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "evidence_layer": "regulator_identity_and_regulatory_capacity", "support_kind": info["kind"], "cell_or_model": info["model"], "assay_or_perturbation": info["assay"], "observation": info["observation"], "effect_direction": "queued-pair direction not established except staged BHLHA15-RAB26 candidate", "primary_citation": info["general_primary"], "corroborating_citation": info["general_corr"], "route_or_module_relevance": "regulator-level evidence only", "target_pair_scope": "not evidence for unrelated queued exact pairs; no upstream relay inferred", "exportable": "false", "canonical_write_performed": "false", "limitations": "Regulator-level evidence does not establish SCI target-cell presence, exact queued-target direction, downstream activation, or upstream relay. The BHLHA15-RAB26 candidate remains staging-only."})
        seen.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch014_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch014_regulator_register.tsv"
    summary_path = args.output_dir / "batch_014_evidence_review_summary.json"
    report_path = args.output_dir / "EVIDENCE_REVIEW_BATCH014.md"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    status_counts: dict[str, int] = {}
    for item in pairs:
        status_counts[item["exact_pair_status"]] = status_counts.get(item["exact_pair_status"], 0) + 1
    pair_keys = {(item["regulator_key"], item["target_symbol"], item["species_scope"], item["source_record_id"]) for item in pairs}
    near = sum(v for k, v in status_counts.items() if "near_match" in k)
    summary = {"status": "staging_only", "batch_id": "public_tf_evidence_batch_014", "source_set_ranks_reviewed": list(range(1, 26)), "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen), "unique_provenance_aware_pairs": len(pair_keys), "exact_pair_status_counts": status_counts, "regulator_register_rows": len(evidence), "exact_pair_support_rows": status_counts.get("functional_direct_binding_promotion_candidate", 0), "promotion_candidate_rows": status_counts.get("functional_direct_binding_promotion_candidate", 0), "partial_or_near_match_rows": near + status_counts.get("partial_functional_binding_support_not_promotable", 0), "binding_dataset_only_not_promotable_rows": status_counts.get("binding_dataset_only_not_promotable", 0) + status_counts.get("direct_binding_only_not_promotable", 0), "database_membership_only_not_promotable_rows": status_counts.get("database_membership_only_not_promotable", 0), "bounded_negative_rows": status_counts.get("no_exact_pair_support_found_in_bounded_search", 0), "exportable_pair_rows": 0, "canonical_writes_performed": False, "module22b_promotions_performed": False, "provenance_preserved": True, "limitations": ["TFLink/GTRD/ENCODE/MSigDB membership or occupancy is not causal regulation.", "Exact pair negatives are bounded-search results, not global absence.", "Near matches across genes, paralogs, isoforms, species, and regulatory directions were retained separately and not transferred.", "Target-cell presence, downstream activation, and upstream relay remain unestablished except as explicitly staged context outside SCI.", "No canonical or Module 22B write was performed."], "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))]}
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path.write_text("\n".join(["# Evidence review: public TF batch 014", "", "Reviewed 81 exact regulator-target-species pairs across 25 selected TFLink source sets.", "", f"- **{len(pairs)} / 81** pairs were reviewed.", f"- **{summary['exact_pair_support_rows']}** exact pairs met the promotion-candidate threshold; BHLHA15/MIST1-to-RAB26 remains staging-only pending SCI-cell context.", f"- **{summary['binding_dataset_only_not_promotable_rows']}** pairs had occupancy/binding leads.", f"- **{summary['database_membership_only_not_promotable_rows']}** pairs remained database-membership-only leads.", f"- **{summary['partial_or_near_match_rows']}** partial/near matches were kept separate.", f"- **{summary['bounded_negative_rows']}** pairs were bounded-search negatives.", "- **0** rows are exportable; no canonical or Module 22B writes were performed.", "", "ZNF513 direct-binding-only rows, BHLHA15/MIST1-RAB26 exact functional evidence, and RAB3D partial binding/expression support are preserved with explicit limitations; no SCI signaling direction is inferred.", ""]), encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
