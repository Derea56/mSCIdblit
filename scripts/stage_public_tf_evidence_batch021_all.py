#!/usr/bin/env python3
"""Stage conservative evidence findings for all Batch 021 pairs."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_021/"
    "public_tf_evidence_collection_batch_021.tsv"
)
TF_LINK_URL = "https://tflink.net/download/#interaction-gmt"
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


# symbol, primary regulator-level citation, corroborating citation, support kind,
# model, assay, observation, role relevance
REGULATORS = {
    "bicra": ("BICRA/GLTSCR1", "https://pubmed.ncbi.nlm.nih.gov/29374058/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5858003/", "primary_literature_regulator_level", "human GBAF/BAF chromatin models", "complex purification, interaction assays, and chromatin occupancy", "BICRA is a noncanonical BAF/GBAF chromatin-complex component; queued ACTR2, ACVR1, ADAM22, and ADGRB3 edges were not validated.", "noncanonical chromatin-complex capacity only"),
    "leo1": ("LEO1", "https://pubmed.ncbi.nlm.nih.gov/26659056/", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE62171", "primary_literature_regulator_level", "human THP-1 and PAF1-complex models", "ChIP-seq, promoter-proximal pausing, and transcription studies", "LEO1 is a PAF1-complex elongation factor with broad occupancy, not a sequence-specific queued-target regulator.", "noncanonical transcriptional machinery capacity only"),
    "kat7": ("KAT7/HBO1", "https://pubmed.ncbi.nlm.nih.gov/34724565/", "https://pubmed.ncbi.nlm.nih.gov/32764680/", "primary_literature_regulator_level", "mouse HSC and human AML chromatin models", "histone-acetyltransferase deletion, occupancy, and transcription studies", "KAT7/HBO1 is a chromatin acetyltransferase with nonqueued target effects.", "noncanonical chromatin-enzyme capacity only"),
    "kdm3a": ("KDM3A/JMJD1A", "https://pubmed.ncbi.nlm.nih.gov/25535969/", "https://pubmed.ncbi.nlm.nih.gov/19481530/", "primary_literature_regulator_level", "human chromatin and nuclear-receptor models", "cofactor recruitment, demethylase, ChIP/re-ChIP, and expression studies", "KDM3A is a chromatin demethylase/coregulator; the queued ABCA1 result is an adjacent/complex-level near-match centered on ABCG1.", "noncanonical chromatin-coregulator capacity only"),
    "kdm5a": ("KDM5A/JARID1A/RBP2", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE28343", "https://pubmed.ncbi.nlm.nih.gov/25190814/", "authoritative_binding_dataset_only", "mouse ESC and NuRD/Notch models", "ChIP-seq, chromatin-complex, and perturbation studies", "KDM5A has broad promoter/TSS and corepressor evidence at nonqueued loci; queued mouse profile rows remain profile-only.", "noncanonical chromatin-demethylase capacity only"),
    "rbbp4": ("RBBP4", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7940252/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7617683/", "primary_literature_regulator_level", "mouse ESC and cortical progenitor models", "PRC2/HDAC occupancy, deletion, knockdown, and rescue", "RBBP4 is a PRC2/HDAC chromatin cofactor with nonqueued Cdon and pluripotency evidence.", "noncanonical chromatin-coregulator capacity only"),
    "phf6": ("PHF6", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10933485/", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE247836", "primary_literature_regulator_level", "mouse developing cortex models", "ChIP-seq and conditional loss with expression analysis", "PHF6 has chromatin-associated transcriptional evidence in Ephrin/receptor programs, not queued targets.", "noncanonical chromatin regulator capacity only"),
    "aff3": ("AFF3/LAF4", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4146563/", "", "primary_literature_regulator_level", "mouse neural-development models", "occupancy, Aff3 perturbation, expression, and partial rescue", "AFF3 has a real Mdga2 regulatory edge outside the queued receptors/proteases.", "noncanonical transcriptional coregulator capacity only"),
    "taf7": ("TAF7", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3434555/", "https://pubmed.ncbi.nlm.nih.gov/16407123/", "primary_literature_regulator_level", "human TFIID/Pol II models", "ChIP, depletion, and promoter checkpoint studies", "TAF7 is a basal TFIID initiation/elongation factor with nonqueued CCND1/CCNA evidence.", "noncanonical transcriptional machinery capacity only"),
    "yap1": ("YAP1", "https://www.nature.com/articles/s41586-022-04924-6", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12554403/", "primary_literature_regulator_level", "human fibroblast, vascular, and lymphatic-endothelial models", "YAP/TAZ ChIP-qPCR, depletion/rescue, RT-qPCR, and pathway perturbation", "YAP1 is a TEAD-associated coactivator; ACTR2 is staged separately as a YAP/TAZ-combined exact candidate and ACKR2 as expression-only.", "noncanonical transcriptional coactivator capacity only"),
    "taf2": ("TAF2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11109217/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC84407/", "primary_literature_regulator_level", "human TFIID and cell-cycle promoter models", "TAF2 depletion, ChIP/profiling, and RNA-seq", "TAF2 has promoter-selective basal transcription evidence at nonqueued genes; mouse queued rows remain profile-only.", "noncanonical transcriptional machinery capacity only"),
    "pcf11": ("PCF11", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6458999/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2241900/", "primary_literature_regulator_level", "human HeLa RNA-processing models", "depletion, mNET-seq, 3-prime RNA-seq, chromatin RNA-seq, and ChIP-seq", "PCF11 is a Pol II termination and cleavage/polyadenylation factor, not a sequence-specific queued-target TF.", "noncanonical RNA-processing capacity only"),
    "cdk7": ("CDK7", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2865308/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5681959/", "primary_literature_regulator_level", "mouse ES-cell and neuronal TFIIH models", "Pol II phosphorylation, knockdown, and transcription studies", "CDK7 is a TFIIH/elongation kinase; queued Abca1 is only a Mat1/CDK7 PPARgamma near-match.", "noncanonical transcriptional machinery capacity only"),
    "cxxc1": ("CXXC1/CFP1", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3730110/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5603731/", "primary_literature_regulator_level", "human and mouse CpG-promoter chromatin models", "CpG-island binding, SETD1 recruitment, ChIP, and depletion", "CXXC1 binds CpG-rich promoters and recruits SETD1/H3K4me3 machinery; queued targets were not validated.", "noncanonical chromatin cofactor capacity only"),
    "kdm5c": ("KDM5C", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10785505/", "https://pubmed.ncbi.nlm.nih.gov/38285760/", "primary_literature_regulator_level", "human chromatin and enhancer models", "ChIP-qPCR, expression, and BRD4 cooperation studies", "KDM5C has nonqueued target and enhancer evidence; other KDM-family results were not transferred.", "noncanonical chromatin-demethylase capacity only"),
    "nsd3": ("NSD3", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4688131/", "https://pubmed.ncbi.nlm.nih.gov/32967925/", "primary_literature_regulator_level", "human and mouse chromatin/super-enhancer models", "BRD4/CHD8 complex, occupancy, and expression studies", "NSD3 is a chromatin methyltransferase/adaptor with nonqueued NOTCH3, ADAM12, DLL4, and nephrin evidence.", "noncanonical chromatin-coregulator capacity only"),
    "hmg20a": ("HMG20A", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9884267/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9505946/", "primary_literature_regulator_level", "human H2A.Z/NuRD and MEF2C models", "ChIP-seq, perturbation, and chromatin-complex studies", "HMG20A is a chromatin coregulator with nonqueued MEF2C and PHF14/TGFbeta/Hippo evidence.", "noncanonical chromatin-coregulator capacity only"),
    "ssrp1": ("SSRP1/FACT", "https://pmc.ncbi.nlm.nih.gov/articles/PMC129072/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8982582/", "primary_literature_regulator_level", "human p63 and mouse FACT models", "promoter co-occupancy, conditional knockout, and mESC ChIP-seq", "SSRP1 is a FACT chromatin/elongation cofactor with nonqueued MDM2/p21 complex-level evidence.", "noncanonical chromatin-remodeler capacity only"),
    "hdac6": ("HDAC6", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2750862/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10799458/", "primary_literature_regulator_level", "human chromatin and mouse APP/PS1 models", "ChIP-seq, protein-interaction, and pharmacologic perturbation", "HDAC6 is a deacetylase/coregulator; the queued ADAM10 result is a mouse pharmacologic association with unresolved mechanism.", "noncanonical chromatin-coregulator capacity only"),
    "rcor2": ("RCOR2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7724517/", "https://pubmed.ncbi.nlm.nih.gov/21433225/", "primary_literature_regulator_level", "human and mouse REST/CoREST models", "complex occupancy, reprogramming, and expression studies", "RCOR2 is a REST/CoREST/LSD1 coregulator with nonqueued Nanog/Oct4/Sox2 evidence.", "noncanonical transcriptional coregulator capacity only"),
    "hdac8": ("HDAC8", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4237248/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10799458/", "primary_literature_regulator_level", "human colon-cancer and mouse APP/PS1 models", "promoter regulation, deacetylase perturbation, and pharmacologic studies", "HDAC8 is a histone deacetylase/coregulator with nonqueued BMF evidence; queued ADAM10 is a separate mouse pharmacologic near-match for HDAC6.", "noncanonical chromatin-coregulator capacity only"),
    "atf7ip": ("ATF7IP", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5081395/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6719416/", "primary_literature_regulator_level", "human HUSH/SETDB1 and mouse immune models", "H3K9me3/HUSH occupancy, deletion, and expression studies", "ATF7IP is a SETDB1/HUSH chromatin cofactor with broad derepression and nonqueued Il2 evidence.", "noncanonical chromatin-coregulator capacity only"),
    "sirt6": ("SIRT6", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3128103/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6468300/", "primary_literature_regulator_level", "mouse and human fibroblast chromatin models", "mouse ChIP, human siRNA, expression, and enhancer studies", "SIRT6 has broad chromatin occupancy; mouse Adam12 is a cross-species near-match and Actr2/Adam23 are profile-only.", "noncanonical chromatin-enzyme capacity only"),
    "cdk12": ("CDK12", "https://pubmed.ncbi.nlm.nih.gov/22012619/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7641311/", "primary_literature_regulator_level", "human Pol II elongation and DNA-repair models", "elongation, phosphorylation, and transcription studies", "CDK12 is a transcription-elongation kinase with nonqueued DNA-repair target evidence.", "noncanonical transcriptional machinery capacity only"),
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
    binding = "TFLink_or_profile_membership_only_no_retrieved_target_locus_call"
    downstream = "not_found_for_exact_pair"
    disposition = "retain_provenance_traceable_candidate_without_promotion"
    exclusions = "TFLink/profile membership is a search lead; broad regulator evidence, orthologs, paralogs, reverse directions, and complex-level findings were not transferred to this exact pair."
    notes = "No exact target-specific causal edge was established; target-cell presence, downstream activation, and upstream relay are not inferred."

    if key == "yap1" and row["species_scope"] == "human" and target == "actr2":
        status = "functional_noncanonical_coactivator_candidate_not_strict_tf"
        primary = "https://www.nature.com/articles/s41586-022-04924-6"
        cell = "human_WI_38_fibroblast_and_vascular_smooth_muscle_models_not_SCI_target_cell"
        binding = "YAP_TAZ_ChIP_qPCR_enrichment_at_ACTR2_enhancer"
        downstream = "YAP_TAZ_depletion_reduced_ACTR2_and_constitutively_active_YAP_rescued_expression"
        disposition = "retain_noncanonical_coactivator_candidate_pending_YAP1_specific_corrobation_and_SCI_context"
        exclusions = "The exact human ACTR2 result combines YAP and TAZ and does not fully isolate YAP1; it is a coactivator edge, not strict sequence-specific TF evidence."
        notes = "Exact human YAP/TAZ-to-ACTR2 enhancer occupancy and perturbation support is staged separately as noncanonical coactivator evidence."
    elif key == "yap1" and row["species_scope"] == "human" and target == "ackr2":
        status = "target_expression_association_without_direct_binding_not_promotable"
        primary = "https://pmc.ncbi.nlm.nih.gov/articles/PMC12554403/"
        cell = "human_dermal_lymphatic_endothelial_cells_not_SCI_target_cell"
        binding = "no_YAP1_ACKR2_locus_occupancy_retrieved"
        downstream = "YAP_pathway_activation_increased_ACKR2_mRNA_and_verteporfin_blocked_VEGFC_response"
        disposition = "retain_expression_pathway_association_separately"
        exclusions = "The study supports target-specific expression association but not direct YAP1 occupancy or YAP1-specific causality; verteporfin and pathway activation are confounded."
        notes = "Human ACKR2 expression response is retained as a pathway-associated lead, not a functional YAP1 promoter edge."
    elif key == "kdm3a" and target == "abca1":
        status = "contextual_complex_association_not_promotable"
        primary = "https://pubmed.ncbi.nlm.nih.gov/19481530/"
        corr = "https://www.sciencedirect.com/science/article/pii/S1097276509003141"
        cell = "human_HepG2_TH P1_and_mouse_LXR_models_not_SCI_target_cell"
        binding = "KDM3A_associated_complex_evidence_centered_on_ABCG1_not_isolated_ABCA1_occupancy"
        downstream = "ABCA1_used_as_contrasting_locus_without_KDM3A_specific_target_effect"
        disposition = "retain_adjacent_target_near_match_separately"
        exclusions = "The reported demethylase recruitment is centered on ABCG1 and distinguishes ABCA1 as an adjacent/contrast locus; no isolated KDM3A-to-ABCA1 edge was shown."
        notes = "Complex-level adjacent-target evidence is not promoted to the exact KDM3A-to-ABCA1 pair."
    elif key == "kdm5a" and row["species_scope"] == "mouse":
        status = "binding_profile_only_not_promotable"
        primary = "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE28343"
        cell = "mouse_ESC_profile_not_SCI_target_cell"
        binding = "mouse_KDM5A_ChIP_seq_profile_without_queued_locus_validation"
        downstream = "no_target_specific_perturbation_or_expression_direction"
        disposition = "retain_mouse_binding_profile_lead_separately"
        exclusions = "The mouse KDM5A ChIP-seq dataset supports broad promoter/TSS occupancy but no queued-locus call plus target-specific direction was established."
        notes = "Mouse KDM5A rows are retained as binding-profile leads only."
    elif key == "taf2" and row["species_scope"] == "mouse":
        status = "binding_profile_only_not_promotable"
        primary = "https://remap2022.univ-amu.fr/target_page/TAF2%3A10090"
        binding = "mouse_ReMap_TAF2_profile_without_queued_locus_validation"
        disposition = "retain_mouse_binding_profile_lead_separately"
        notes = "Mouse TAF2 ReMap availability is profile evidence only; no exact queued functional edge was established."
    elif key == "cdk7" and row["species_scope"] == "mouse" and target == "abca1":
        status = "contextual_complex_association_not_promotable"
        primary = "https://pmc.ncbi.nlm.nih.gov/articles/PMC2612500/"
        cell = "mouse_MEF_and_3T3_L1_models_not_SCI_target_cell"
        binding = "no_CDK7_Abca1_locus_occupancy;_MAT1_CDK7_complex_context"
        downstream = "MAT1_CDK7_perturbation_changed_PPARgamma_phosphorylation_and_adipogenesis_without_Abca1_readout"
        disposition = "retain_complex_level_near_match_separately"
        exclusions = "The study implicates the MAT1/CDK7 complex in PPARgamma phosphorylation/adipogenesis but has no Abca1 readout or direct Cdk7 occupancy."
        notes = "Complex-level adipogenesis evidence is not transferred to the exact mouse Cdk7-to-Abca1 pair."
    elif key == "hdac6" and row["species_scope"] == "human" and target == "adam10":
        status = "contextual_ortholog_near_match_not_promotable"
        primary = "https://pmc.ncbi.nlm.nih.gov/articles/PMC10799458/"
        cell = "mouse_APP_PS1_cortex_not_human_SCI_target_cell"
        binding = "no_human_HDAC6_ADAM10_locus_occupancy"
        downstream = "mouse_pharmacologic_VPA_WT161_treatment_increased_ADAM10_with_unresolved_HDAC6_mechanism"
        disposition = "retain_cross_species_pharmacologic_near_match_separately"
        exclusions = "The result is mouse, pharmacologic, and explicitly lacks a resolved HDAC6-specific mechanism; it does not support the exact human edge."
        notes = "Cross-species pharmacologic association only; not promoted."
    elif key == "sirt6" and row["species_scope"] == "mouse" and target in {"actr2", "adam23"}:
        status = "binding_profile_only_not_promotable"
        primary = "https://maayanlab.cloud/Harmonizome/gene_set/SIRT6/ENCODE%2BTranscription%2BFactor%2BTargets"
        cell = "mouse_SIRT6_profile_not_SCI_target_cell"
        binding = "aggregated_SIRT6_ChIP_profile_membership"
        downstream = "no_target_specific_perturbation_or_expression_direction"
        disposition = "retain_mouse_binding_profile_lead_separately"
        exclusions = "Aggregated SIRT6/ENCODE profile membership does not establish locus-specific validation, direction, or target-cell context."
        notes = "Profile-only SIRT6 rows are kept separate from functional evidence."
    elif key == "sirt6" and row["species_scope"] == "mouse" and target == "adam12":
        status = "contextual_ortholog_near_match_not_promotable"
        primary = "https://pubmed.ncbi.nlm.nih.gov/30753595/"
        corr = "https://pmc.ncbi.nlm.nih.gov/articles/PMC6468300/"
        cell = "human_IMR90_MRC5_fibroblasts_and_published_mouse_ChIP_resource_not_SCI_target_cell"
        binding = "mouse_Sirt6_ChIP_resource_at_Adam12_without_mouse_perturbation"
        downstream = "human_SIRT6_loss_or_siRNA_increased_ADAM12"
        disposition = "retain_cross_species_near_match_for_deeper_validation"
        exclusions = "Human SIRT6 loss/siRNA and a mouse genome-wide ChIP resource do not provide a same-species target-specific perturbation plus occupancy assay."
        notes = "Promising but cross-species Sirt6-to-Adam12 lead; not strict promotion."

    return {
        "symbol": symbol, "general_primary": general_primary, "general_corr": general_corr, "kind": kind,
        "model": model, "assay": assay, "observation": observation, "relevance": relevance,
        "status": status, "primary": primary, "corr": corr, "cell": cell, "binding": binding,
        "downstream": downstream, "disposition": disposition, "exclusions": exclusions, "notes": notes,
    }


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
        pairs.append({
            "review_id": f"public_tf_evidence_batch021_pair_{int(row['batch_rank']):02d}_{row['target_rank']}",
            "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key,
            "regulator_symbol": info["symbol"], "species_scope": row["species_scope"],
            "source_registry": row["source_registry"], "source_record_id": row["source_record_id"],
            "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"],
            "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": search_url(row["raw_tf_symbol"], row["target_symbol"], row["species_scope"]),
            "exact_pair_status": info["status"], "regulator_general_evidence_status": "supported_general_or_authoritative_regulator_evidence",
            "target_cell_presence_status": info["cell"], "binding_or_association_status": info["binding"],
            "downstream_expression_or_perturbation_status": info["downstream"], "downstream_activation_status": "not_established_for_SCI_target_cell",
            "upstream_relay_status": "not_tested_for_exact_pair", "disposition": info["disposition"],
            "primary_citation": info["primary"], "corroborating_citation": info["corr"],
            "near_match_exclusions": info["exclusions"], "review_notes": info["notes"] + " " + info["observation"],
            "exportable": "false", "canonical_write_performed": "false",
        })
        if key not in seen:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch021_regulator_{key}", "regulator_key": key,
                "regulator_symbol": info["symbol"], "species_scope": row["species_scope"],
                "evidence_layer": "regulator_identity_and_regulatory_capacity", "support_kind": info["kind"],
                "cell_or_model": info["model"], "assay_or_perturbation": info["assay"], "observation": info["observation"],
                "effect_direction": "queued-pair direction not established except explicitly recorded limited associations",
                "primary_citation": info["general_primary"], "corroborating_citation": info["general_corr"],
                "route_or_module_relevance": info["relevance"], "target_pair_scope": "not evidence for unrelated queued exact pairs; no upstream relay inferred",
                "exportable": "false", "canonical_write_performed": "false",
                "limitations": "Regulator-level evidence does not establish SCI target-cell presence, exact queued-target direction, downstream activation, or upstream relay. Profile, chromatin, cofactor, machinery, pathway, and cross-species evidence is retained separately from canonical promoter-TF evidence.",
            })
            seen.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch021_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch021_regulator_register.tsv"
    summary_path = args.output_dir / "batch_021_evidence_review_summary.json"
    report_path = args.output_dir / "EVIDENCE_REVIEW_BATCH021.md"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    status_counts: dict[str, int] = {}
    for item in pairs:
        status_counts[item["exact_pair_status"]] = status_counts.get(item["exact_pair_status"], 0) + 1
    pair_keys = {(item["regulator_key"], item["target_symbol"], item["species_scope"], item["source_record_id"]) for item in pairs}
    noncanonical = status_counts.get("functional_noncanonical_coactivator_candidate_not_strict_tf", 0)
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_021", "source_set_ranks_reviewed": list(range(1, 26)),
        "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen), "unique_provenance_aware_pairs": len(pair_keys),
        "exact_pair_status_counts": status_counts, "regulator_register_rows": len(evidence), "strict_tf_promotion_candidate_rows": 0,
        "noncanonical_exact_candidate_rows": noncanonical, "exportable_pair_rows": 0, "canonical_writes_performed": False,
        "module22b_promotions_performed": False, "provenance_preserved": True,
        "limitations": ["TFLink/profile resources are search leads, not causal regulation.", "Exact-pair negatives are bounded search results, not global absence.", "YAP1-to-ACTR2 is a YAP/TAZ-combined human coactivator result and is not strict TF evidence.", "YAP1-to-ACKR2 is expression-only; KDM3A, CDK7, HDAC6, and SIRT6 leads are indirect or cross-species.", "No canonical or Module 22B write was performed."],
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path.write_text("\n".join([
        "# Evidence review: public TF batch 021", "", "Reviewed 100 exact regulator-target-species pairs across 25 noncanonical TFLink source-set ranks.", "",
        f"- **{len(pairs)}** pairs were reviewed across **{len(seen)}** regulators.",
        f"- **{noncanonical}** exact noncanonical coactivator candidate was staged: human YAP1/YAP-TAZ-to-ACTR2, supported by enhancer ChIP-qPCR, depletion, and active-YAP rescue.",
        f"- **{status_counts.get('binding_profile_only_not_promotable', 0)}** mouse profile-only rows and **{status_counts.get('contextual_ortholog_near_match_not_promotable', 0) + status_counts.get('contextual_complex_association_not_promotable', 0)}** contextual/cross-species/complex near-matches were retained without promotion.",
        "- **0** strict TF promotion candidates, exportable rows, canonical writes, or Module 22B writes.", "",
        "All rows retain the original TFLink source record, raw symbol, species, target, graph-module mapping, and local source snapshot. Regulator-level chromatin, cofactor, machinery, profile, pathway, and cross-species evidence is recorded separately from exact canonical TF evidence.", "",
    ]) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
