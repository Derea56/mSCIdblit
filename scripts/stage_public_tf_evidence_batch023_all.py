#!/usr/bin/env python3
"""Stage conservative evidence findings for all Batch 023 pairs."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_023/"
    "public_tf_evidence_collection_batch_023.tsv"
)
TF_LINK_URL = "https://tflink.net/download/#interaction-gmt"
PAIR_FIELDS = ["review_id", "batch_id", "batch_rank", "regulator_key", "regulator_symbol", "species_scope", "source_registry", "source_record_id", "raw_tf_symbol", "target_symbol", "target_graph_modules", "candidate_membership_status", "exact_pair_search_url", "exact_pair_status", "regulator_general_evidence_status", "target_cell_presence_status", "binding_or_association_status", "downstream_expression_or_perturbation_status", "downstream_activation_status", "upstream_relay_status", "disposition", "primary_citation", "corroborating_citation", "near_match_exclusions", "review_notes", "exportable", "canonical_write_performed"]
EVIDENCE_FIELDS = ["evidence_id", "regulator_key", "regulator_symbol", "species_scope", "evidence_layer", "support_kind", "cell_or_model", "assay_or_perturbation", "observation", "effect_direction", "primary_citation", "corroborating_citation", "route_or_module_relevance", "target_pair_scope", "exportable", "canonical_write_performed", "limitations"]

# symbol, primary citation, corroborating citation, support kind, model, assay, observation, relevance
REGULATORS = {
    "kdm3b": ("KDM3B/JMJD1B", "https://pubmed.ncbi.nlm.nih.gov/22615488/", "https://pubmed.ncbi.nlm.nih.gov/31592194/", "primary_literature_regulator_level", "human leukemia and prostate chromatin models", "H3K9 demethylase occupancy and perturbation", "KDM3B has nonqueued LMO2 and broad chromatin-regulatory evidence.", "noncanonical chromatin-demethylase capacity only"),
    "cbx2": ("CBX2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10499018/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5503153/", "primary_literature_regulator_level", "mouse spermatogonia and PRC1 models", "CUT&RUN, occupancy, inducible loss, and expression", "CBX2 occupies and regulates nonqueued differentiation loci such as Foxc2, Pax7, and Sall4.", "noncanonical chromatin-repressor capacity only"),
    "kdm7a": ("KDM7A/KIAA1718", "https://pubmed.ncbi.nlm.nih.gov/34249916/", "https://pubmed.ncbi.nlm.nih.gov/30183076/", "primary_literature_regulator_level", "human MKL1 and androgen-receptor chromatin models", "promoter occupancy, recruitment, and expression assays", "KDM7A regulates nonqueued RHOJ and androgen-receptor target loci through recruited complexes.", "noncanonical chromatin-demethylase capacity only"),
    "kdm3a": ("KDM3A/JMJD1A", "https://pubmed.ncbi.nlm.nih.gov/19194461/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5689571/", "primary_literature_regulator_level", "mouse mammary and human breast-cancer models", "knockout, promoter occupancy, reporter, and expression studies", "KDM3A has nonqueued metabolic, mammary, and cell-proliferation evidence; queued mouse ADAM/adhesion-GPCR rows were not validated.", "noncanonical chromatin-demethylase capacity only"),
    "tet3": ("TET3", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3590984/", "https://pubmed.ncbi.nlm.nih.gov/27141829/", "primary_literature_regulator_level", "human and mouse TET3/OGT epigenetic models", "DNA-demethylation, methylome, and promoter studies", "TET3 is an epigenetic regulator with nonqueued promoter evidence; mouse Agrn is separately recorded as locus-level epigenetic evidence.", "noncanonical epigenetic regulator capacity only"),
    "nsd2": ("NSD2/WHSC1", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6786427/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8528846/", "primary_literature_regulator_level", "human TNBC and colorectal cancer models", "ChIP-qPCR, active/catalytic-dead overexpression, knockdown, and expression", "NSD2 has an exact ADAM9 promoter and perturbation result with independent direction corroboration; it is a chromatin regulator rather than a strict TF.", "noncanonical chromatin-methyltransferase capacity; exact ADAM9 edge kept separate"),
    "ash2l": ("ASH2L", "https://pubmed.ncbi.nlm.nih.gov/37879562/", "https://pubmed.ncbi.nlm.nih.gov/25258321/", "primary_literature_regulator_level", "mouse diabetic-nephropathy and human COMPASS models", "H3K4me3/promoter association, chromatin-complex recruitment, and perturbation", "ASH2L is a COMPASS/MLL cofactor; mouse Adam17 is separately staged as an exact noncanonical chromatin-regulator candidate.", "noncanonical chromatin cofactor capacity; exact Adam17 edge kept separate"),
    "ep400": ("EP400", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11132066/", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE64786", "primary_literature_regulator_level", "mouse embryo, ESC, and oligodendrocyte models", "H3.3/chromatin remodeling, occupancy, and expression", "EP400 has nonqueued promoter and chromatin-remodeler evidence.", "noncanonical chromatin-remodeler capacity only"),
    "sap130": ("SAP130", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11707140/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC164750/", "primary_literature_regulator_level", "mouse brain and SIN3A-HDAC models", "ChIP-seq, mutant transcriptomics, and corepressor assays", "SAP130 is a SIN3A-HDAC corepressor component with nonqueued target evidence.", "noncanonical transcriptional coregulator capacity only"),
    "dpf2": ("DPF2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6486830/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10313367/", "primary_literature_regulator_level", "mouse ESC and hematopoietic models", "BAF occupancy, enhancer/promoter regulation, and perturbation", "DPF2 is a BAF-associated chromatin regulator with nonqueued Tbx3/NRF2/Cacna1d evidence.", "noncanonical chromatin-reader capacity only"),
    "sfmbt1": ("SFMBT1", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3585059/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3779763/", "primary_literature_regulator_level", "human and mouse chromatin-corepressor models", "occupancy, LSD1/CoREST/Polycomb interaction, and perturbation", "SFMBT1 has nonqueued Myogenin, histone, SIX2, and EMT regulatory evidence.", "noncanonical chromatin-corepressor capacity only"),
    "dido1": ("DIDO1", "https://pubmed.ncbi.nlm.nih.gov/20547754/", "https://pubmed.ncbi.nlm.nih.gov/26149686/", "primary_literature_regulator_level", "human and mouse chromatin/mitotic models", "isoform, chromatin, and cell-cycle perturbation studies", "DIDO1 is a nuclear chromatin/termination regulator; no queued target edge was validated.", "noncanonical chromatin regulator capacity only"),
    "bap1": ("BAP1", "https://pubmed.ncbi.nlm.nih.gov/22105359/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4678392/", "primary_literature_regulator_level", "human and mouse PR-DUB/chromatin models", "deubiquitinase complex, occupancy, and loss-of-function studies", "BAP1 has genuine PR-DUB chromatin-regulatory evidence at nonqueued loci.", "noncanonical chromatin deubiquitinase capacity only"),
    "kansl3": ("KANSL3/NSL3", "https://pubmed.ncbi.nlm.nih.gov/32382029/", "https://pubmed.ncbi.nlm.nih.gov/35177641/", "primary_literature_regulator_level", "human and mouse NSL-complex models", "promoter-associated complex studies and mouse phenotypes", "KANSL3 is an NSL chromatin/transcriptional cofactor; queued targets were not validated.", "noncanonical transcriptional machinery capacity only"),
    "rcor1": ("RCOR1/CoREST", "https://pubmed.ncbi.nlm.nih.gov/21433225/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4736047/", "primary_literature_regulator_level", "mouse REST/CoREST neural models", "complex occupancy, LSD1 recruitment, and perturbation", "RCOR1 has nonqueued chromatin-corepressor evidence.", "noncanonical transcriptional coregulator capacity only"),
    "kdm5d": ("KDM5D", "https://pubmed.ncbi.nlm.nih.gov/27185910/", "", "primary_literature_regulator_level", "human prostate androgen-receptor models", "AR interaction, H3K4 demethylation, and transcription assays", "KDM5D regulates androgen-receptor activity at nonqueued loci.", "noncanonical chromatin-demethylase capacity only"),
    "znf592": ("ZNF592", "https://pubmed.ncbi.nlm.nih.gov/20531441/", "https://pubmed.ncbi.nlm.nih.gov/21620140/", "primary_literature_regulator_level", "human developmental/coregulator models", "disease genetics and proteomics", "ZNF592 has developmental/coregulator evidence, but direct queued target mechanisms remain unresolved.", "noncanonical transcriptional coregulator capacity only"),
    "ell2": ("ELL2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2771556/", "https://pubmed.ncbi.nlm.nih.gov/25238757/", "primary_literature_regulator_level", "mouse B-cell/plasma-cell models", "Igh association, elongation, and RNA-processing studies", "ELL2 regulates nonqueued immunoglobulin transcription/RNA processing.", "noncanonical transcriptional elongation capacity only"),
    "rcor2": ("RCOR2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7724517/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4736047/", "primary_literature_regulator_level", "human and mouse REST/CoREST neural models", "complex occupancy, reprogramming, and expression", "RCOR2 is a REST/CoREST coregulator with nonqueued Dlx2, Shh, and pluripotency evidence.", "noncanonical transcriptional coregulator capacity only"),
    "supt6h": ("SUPT6H/SPT6", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE103180", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3630356/", "primary_literature_regulator_level", "mouse ESC and myogenic models", "ChIP-seq, depletion, and Pol II elongation", "SUPT6H is a chromatin/elongation factor with broad nonqueued transcriptional effects.", "noncanonical transcriptional machinery capacity only"),
    "med26": ("MED26", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4646223/", "", "primary_literature_regulator_level", "mouse Mediator/LEC models", "Mediator recruitment and snRNA transcription studies", "MED26 is Mediator machinery; no queued target edge was validated.", "noncanonical transcriptional machinery capacity only"),
    "adnp": ("ADNP", "https://www.gsea-msigdb.org/gsea/msigdb/cards/ADNP_TARGET_GENES", "https://pubmed.ncbi.nlm.nih.gov/30445619/", "authoritative_binding_dataset_only", "human GTRD-derived promoter-profile models", "harmonized ChIP-seq target-set construction", "ADNP queued rows occur in a GTRD-derived promoter profile, not a target-specific perturbation study.", "binding-profile capacity only"),
    "kansl1": ("KANSL1/NSL1", "https://pubmed.ncbi.nlm.nih.gov/32382029/", "https://pubmed.ncbi.nlm.nih.gov/35177641/", "primary_literature_regulator_level", "human and mouse NSL-complex models", "promoter-associated complex studies and mouse phenotypes", "KANSL1 is an NSL chromatin/transcriptional cofactor; queued targets were not validated.", "noncanonical transcriptional machinery capacity only"),
    "taf10": ("TAF10", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4438247/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5650055/", "primary_literature_regulator_level", "mouse erythroid and embryo models", "TFIID complex, conditional loss, and GATA1-associated transcription", "TAF10 has complex-level evidence at nonqueued erythroid/developmental targets.", "noncanonical transcriptional machinery capacity only"),
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


def classify(row: dict[str, str]) -> dict[str, str]:
    key = row["regulator_key"]
    target = row["target_symbol"].lower()
    symbol, general_primary, general_corr, kind, model, assay, observation, relevance = REGULATORS[key]
    status = "database_membership_only_not_promotable"
    primary = TF_LINK_URL
    corr = ""
    cell = "not_established_for_exact_pair"
    binding = "TFLink_or_profile_membership_only_no_queued_locus_validation"
    downstream = "not_found_for_exact_pair"
    disposition = "retain_provenance_traceable_candidate_without_promotion"
    exclusions = "TFLink/profile membership is a search lead; broad regulator evidence, orthologs, paralogs, reverse directions, and complex-level findings were not transferred to this exact pair."
    notes = "No exact target-specific causal edge was established; target-cell presence, downstream activation, and upstream relay are not inferred."

    if key == "nsd2" and row["species_scope"] == "human" and target == "adam9":
        status = "functional_noncanonical_chromatin_regulator_candidate_not_strict_tf"
        primary = "https://pmc.ncbi.nlm.nih.gov/articles/PMC6786427/"
        corr = "https://pmc.ncbi.nlm.nih.gov/articles/PMC8528846/"
        cell = "human_TNBC_and_colorectal_cancer_models_not_SCI_target_cell"
        binding = "NSD2_ChIP_qPCR_at_ADAM9_promoter"
        downstream = "NSD2_knockdown_reduced_ADAM9_and_active_NS D2_overexpression_increased_it_catalytic_dead_NS D2_did_not"
        disposition = "retain_noncanonical_chromatin_candidate_pending_SCI_context"
        exclusions = "Direct ADAM9 promoter and perturbation evidence is for a chromatin methyltransferase, not a strict sequence-specific TF; independent corroboration supports direction but not occupancy."
        notes = "Exact human NSD2-to-ADAM9 promoter/perturbation evidence is staged as a noncanonical chromatin-regulator candidate; EGFR-AKT/STAT3 pathway effects are recorded as downstream context only."
    elif key == "ash2l" and row["species_scope"] == "mouse" and target == "adam17":
        status = "functional_noncanonical_chromatin_regulator_candidate_not_strict_tf"
        primary = "https://pubmed.ncbi.nlm.nih.gov/37879562/"
        cell = "mouse_db_db_nephropathy_and_glomerular_mesangial_models_not_SCI_target_cell"
        binding = "ASH2L_associated_H3K4me3_enrichment_at_Adam17_promoter"
        downstream = "Ash2l_loss_reduced_Adam17_transcription_and_pathway_activity"
        disposition = "retain_noncanonical_chromatin_candidate_pending_independent_corroboration_and_SCI_context"
        exclusions = "The evidence supports a COMPASS/MLL cofactor-associated chromatin mechanism; only one direct Adam17 paper was found and no strict TF mechanism is implied."
        notes = "Exact mouse ASH2L-associated Adam17 promoter/H3K4me3 and loss-of-function evidence is staged separately from strict TF promotion."
    elif key == "tet3" and row["species_scope"] == "mouse" and target == "agrn":
        status = "exact_locus_epigenetic_evidence_without_direct_occupancy_not_promotable"
        primary = "https://pmc.ncbi.nlm.nih.gov/articles/PMC4542306/"
        cell = "mouse_zygote_methylome_model_not_SCI_target_cell"
        binding = "no_direct_TET3_Agrn_ChIP;_locus_level_methylation_evidence"
        downstream = "Tet3_loss_increased_Agrn_CGI_promoter_methylation_without_standalone_Agrn_expression_direction"
        disposition = "retain_noncanonical_epigenetic_locus_lead_separately"
        exclusions = "Locus-level methylation protection/demethylation is not direct TET3 occupancy or a complete target-expression perturbation result."
        notes = "Exact mouse Agrn locus epigenetic association is retained as noncanonical evidence only."
    elif key == "adnp" and row["species_scope"] == "human":
        status = "binding_profile_only_not_promotable"
        primary = "https://www.gsea-msigdb.org/gsea/msigdb/cards/ADNP_TARGET_GENES"
        corr = "https://pubmed.ncbi.nlm.nih.gov/30445619/"
        cell = "human_GTRD_profile_not_SCI_target_cell"
        binding = "GTRD_derived_ADNP_promoter_profile_membership"
        disposition = "retain_human_binding_profile_lead_separately"
        exclusions = "The GTRD-derived profile indicates promoter-proximal ChIP target membership but lacks independent locus validation, target perturbation, and direction."
        notes = "ADNP profile rows are search leads only."
    elif key == "dido1" and row["species_scope"] == "human" and target == "ado":
        status = "binding_profile_only_not_promotable"
        primary = "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/DIDO1_TARGET_GENES.html"
        corr = "https://academic.oup.com/nar/article/49/D1/D104/5999890"
        cell = "human_GTRD_profile_not_SCI_target_cell"
        binding = "GTRD_derived_DIDO1_promoter_profile_membership"
        disposition = "retain_human_binding_profile_lead_separately"
        exclusions = "The DIDO1 GTRD-derived profile is harmonized ChIP evidence without independent locus validation or target perturbation/direction."
        notes = "DIDO1-to-ADO is profile-only and is not promoted."
    elif key == "rcor1" and row["species_scope"] == "mouse":
        status = "binding_profile_only_not_promotable"
        primary = "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/RCOR1_TARGET_GENES.html"
        corr = "https://academic.oup.com/nar/article/49/D1/D104/5999890"
        cell = "mouse_GTRD_profile_not_SCI_target_cell"
        binding = "mouse_GTRD_derived_RCOR1_promoter_profile_membership"
        disposition = "retain_mouse_binding_profile_lead_separately"
        exclusions = "The mouse RCOR1 GTRD-derived profile provides promoter-proximal binding membership without target-specific perturbation or direction."
        notes = "RCOR1 mouse rows are profile-only and are not promoted."
    elif key == "kansl3" and row["species_scope"] == "mouse" and target == "adipor2":
        status = "contextual_go_near_match_not_promotable"
        primary = "https://pubmed.ncbi.nlm.nih.gov/41044006/"
        cell = "mouse_liver_KANSL3_knockout_model_not_SCI_target_cell"
        binding = "no_isolated_KANSL3_Adipor2_locus_validation"
        downstream = "KANSL3_loss_changed_broad_liver_metabolic_programs_without_Adipor2_specific_direction"
        disposition = "retain_contextual_metabolic_near_match_separately"
        exclusions = "Mouse liver KANSL3 knockout/ChIP-seq supports broad metabolic regulation but not an isolated Adipor2 target edge."
        notes = "Contextual/GO-level near-match only; no promotion."
    elif key == "znf592" and row["species_scope"] == "human":
        status = "binding_profile_only_not_promotable"
        primary = "https://www.gsea-msigdb.org/gsea/msigdb/Human/geneset/ZNF592_TARGET_GENES.html"
        binding = "GTRD_derived_ZNF592_promoter_profile_membership"
        cell = "human_GTRD_profile_not_SCI_target_cell"
        disposition = "retain_human_binding_profile_lead_separately"
        exclusions = "GTRD-derived profile membership is occupancy/profile evidence only; no target-specific perturbation or expression direction was found."
        notes = "ZNF592 profile rows are retained as binding leads only."
    elif key == "rcor2" and row["species_scope"] == "mouse" and target == "ang":
        status = "ortholog_profile_near_match_not_promotable"
        primary = "https://maayanlab.cloud/Harmonizome/gene_set/RCOR2/CHEA%2BTranscription%2BFactor%2BTargets"
        cell = "human_RCOR2_profile_for_ANG_not_mouse_SCI_target_cell"
        binding = "human_ChEA_profile_contains_ANG_without_mouse_locus_validation"
        disposition = "retain_ortholog_profile_near_match_separately"
        exclusions = "Human RCOR2 profile membership for ANG does not establish mouse Rcor2 occupancy or target perturbation."
        notes = "Ortholog/profile-only near-match is not transferred to the mouse queued edge."

    return {"symbol": symbol, "general_primary": general_primary, "general_corr": general_corr, "kind": kind, "model": model, "assay": assay, "observation": observation, "relevance": relevance, "status": status, "primary": primary, "corr": corr, "cell": cell, "binding": binding, "downstream": downstream, "disposition": disposition, "exclusions": exclusions, "notes": notes}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_BATCH.parent)
    args = parser.parse_args()
    rows = read_tsv(args.batch)
    if len(rows) != 100:
        raise SystemExit(f"expected 100 rows, found {len(rows)}")
    pairs: list[dict[str, str]] = []
    evidence: list[dict[str, str]] = []
    seen: set[str] = set()
    for row in rows:
        key = row["regulator_key"]
        if key not in REGULATORS:
            raise SystemExit(f"missing evidence map for {key}")
        info = classify(row)
        pairs.append({"review_id": f"public_tf_evidence_batch023_pair_{int(row['batch_rank']):02d}_{row['target_rank']}", "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key, "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "source_registry": row["source_registry"], "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"], "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"], "exact_pair_search_url": search_url(row["raw_tf_symbol"], row["target_symbol"], row["species_scope"]), "exact_pair_status": info["status"], "regulator_general_evidence_status": "supported_general_or_authoritative_regulator_evidence", "target_cell_presence_status": info["cell"], "binding_or_association_status": info["binding"], "downstream_expression_or_perturbation_status": info["downstream"], "downstream_activation_status": "not_established_for_SCI_target_cell", "upstream_relay_status": "not_tested_for_exact_pair", "disposition": info["disposition"], "primary_citation": info["primary"], "corroborating_citation": info["corr"], "near_match_exclusions": info["exclusions"], "review_notes": info["notes"] + " " + info["observation"], "exportable": "false", "canonical_write_performed": "false"})
        if key not in seen:
            evidence.append({"evidence_id": f"public_tf_evidence_batch023_regulator_{key}", "regulator_key": key, "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "evidence_layer": "regulator_identity_and_regulatory_capacity", "support_kind": info["kind"], "cell_or_model": info["model"], "assay_or_perturbation": info["assay"], "observation": info["observation"], "effect_direction": "queued-pair direction not established except explicitly recorded limited associations", "primary_citation": info["general_primary"], "corroborating_citation": info["general_corr"], "route_or_module_relevance": info["relevance"], "target_pair_scope": "not evidence for unrelated queued exact pairs; no upstream relay inferred", "exportable": "false", "canonical_write_performed": "false", "limitations": "Regulator-level evidence does not establish SCI target-cell presence, exact queued-target direction, downstream activation, or upstream relay. Profile, chromatin, cofactor, machinery, epigenetic, and cross-species evidence is retained separately from canonical promoter-TF evidence."})
            seen.add(key)
    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch023_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch023_regulator_register.tsv"
    summary_path = args.output_dir / "batch_023_evidence_review_summary.json"
    report_path = args.output_dir / "EVIDENCE_REVIEW_BATCH023.md"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    status_counts: dict[str, int] = {}
    for item in pairs:
        status_counts[item["exact_pair_status"]] = status_counts.get(item["exact_pair_status"], 0) + 1
    pair_keys = {(item["regulator_key"], item["target_symbol"], item["species_scope"], item["source_record_id"]) for item in pairs}
    noncanonical = status_counts.get("functional_noncanonical_chromatin_regulator_candidate_not_strict_tf", 0)
    summary = {"status": "staging_only", "batch_id": "public_tf_evidence_batch_023", "source_set_ranks_reviewed": list(range(1, 26)), "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen), "unique_provenance_aware_pairs": len(pair_keys), "exact_pair_status_counts": status_counts, "regulator_register_rows": len(evidence), "strict_tf_promotion_candidate_rows": 0, "noncanonical_exact_candidate_rows": noncanonical, "exportable_pair_rows": 0, "canonical_writes_performed": False, "module22b_promotions_performed": False, "provenance_preserved": True, "limitations": ["TFLink/profile resources are search leads, not causal regulation.", "Exact-pair negatives are bounded search results, not global absence.", "NSD2-to-ADAM9 and ASH2L-to-Adam17 are exact noncanonical chromatin-regulator candidates without SCI-cell validation; TET3-to-Agrn is locus-level epigenetic evidence without direct occupancy.", "No canonical or Module 22B write was performed."], "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))]}
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path.write_text("\n".join(["# Evidence review: public TF batch 023", "", "Reviewed 100 exact regulator-target-species pairs across 25 noncanonical TFLink source-set ranks.", "", f"- **{len(pairs)}** pairs were reviewed across **{len(seen)}** regulators.", f"- **{noncanonical}** exact noncanonical chromatin-regulator candidates were staged: human NSD2-to-ADAM9 and mouse ASH2L-to-Adam17.", f"- **{status_counts.get('binding_profile_only_not_promotable', 0)}** profile-only rows, one locus-level epigenetic row, and one ortholog/profile near-match were retained without promotion.", "- **0** strict TF promotion candidates, exportable rows, canonical writes, or Module 22B writes.", "", "All rows retain the original TFLink source record, raw symbol, species, target, graph-module mapping, and local source snapshot. Regulator-level chromatin, cofactor, machinery, profile, epigenetic, and cross-species evidence is recorded separately from exact canonical TF evidence.", ""]) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
