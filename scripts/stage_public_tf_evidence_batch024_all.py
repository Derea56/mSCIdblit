#!/usr/bin/env python3
"""Stage conservative evidence findings for all Batch 024 pairs."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_024/"
    "public_tf_evidence_collection_batch_024.tsv"
)
TF_LINK_URL = "https://tflink.net/download/#interaction-gmt"
PAIR_FIELDS = ["review_id", "batch_id", "batch_rank", "regulator_key", "regulator_symbol", "species_scope", "source_registry", "source_record_id", "raw_tf_symbol", "target_symbol", "target_graph_modules", "candidate_membership_status", "exact_pair_search_url", "exact_pair_status", "regulator_general_evidence_status", "target_cell_presence_status", "binding_or_association_status", "downstream_expression_or_perturbation_status", "downstream_activation_status", "upstream_relay_status", "disposition", "primary_citation", "corroborating_citation", "near_match_exclusions", "review_notes", "exportable", "canonical_write_performed"]
EVIDENCE_FIELDS = ["evidence_id", "regulator_key", "regulator_symbol", "species_scope", "evidence_layer", "support_kind", "cell_or_model", "assay_or_perturbation", "observation", "effect_direction", "primary_citation", "corroborating_citation", "route_or_module_relevance", "target_pair_scope", "exportable", "canonical_write_performed", "limitations"]

# symbol, primary citation, corroborating citation, support kind, model, assay, observation, relevance
REGULATORS = {
    "kmt2d": ("KMT2D", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4676270/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4813342/", "primary_literature_regulator_level", "human and mouse enhancer/chromatin models", "ChIP-seq, histone-mark profiling, RNA-seq, and loss-of-function", "KMT2D is an enhancer/promoter methyltransferase with nonqueued target evidence.", "noncanonical chromatin methyltransferase capacity only"),
    "cbx5": ("CBX5/HP1alpha", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9942844/", "https://df6sxcketz7bb.cloudfront.net/manuscripts/127000/127111/jci.insight.127111.sd.pdf", "primary_literature_regulator_level", "human lung-cancer and fibroblast chromatin models", "CUT&RUN, promoter enrichment, and knockdown", "CBX5 has chromatin-repressor evidence at E2F1 and PPARGC1A, not queued targets.", "noncanonical chromatin-reader capacity only"),
    "smarcc2": ("SMARCC2", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE37151", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11625021/", "authoritative_binding_dataset_only", "mouse and human BAF/nBAF models", "FLAG ChIP-seq, occupancy, and RNAi expression studies", "SMARCC2 is a BAF chromatin-remodeling subunit with nonqueued Arc and enhancer evidence.", "noncanonical chromatin-remodeler capacity only"),
    "auts2": ("AUTS2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4199417/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4323097/", "primary_literature_regulator_level", "mouse forebrain and human cerebral-organoid models", "ChIP-seq/RNA-seq, CRISPR deletion, reporter, and expression studies", "AUTS2 is a PRC1/P300-associated cofactor; human CCND1 is expression-only and other queued rows are profile leads.", "noncanonical transcriptional coactivator capacity only"),
    "morc2": ("MORC2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2875037/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12216690/", "primary_literature_regulator_level", "human chromatin-silencing models", "CAIX promoter ChIP/re-ChIP, reporter, siRNA, and ATAC studies", "MORC2 is a chromatin-compaction/coregulator factor with nonqueued CAIX evidence.", "noncanonical chromatin-silencing capacity only"),
    "chaf1a": ("CHAF1A/CAF-1", "https://pmc.ncbi.nlm.nih.gov/articles/PMC1630711/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6868363/", "primary_literature_regulator_level", "mouse chromatin-assembly models", "CAF-1 depletion and pluripotency/heterochromatin studies", "CHAF1A is a chromatin-assembly factor, not a sequence-specific queued-target TF.", "noncanonical chromatin-assembly capacity only"),
    "aff4": ("AFF4", "https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1010425", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8865618/", "primary_literature_regulator_level", "mouse SEC and human colorectal-cancer models", "SEC/elongation occupancy, knockdown, overexpression, and rescue", "AFF4 is an SEC scaffold; human CDH1 is a strong cross-species near-match for the queued mouse row.", "noncanonical transcriptional elongation capacity only"),
    "tet1": ("TET1", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3088758/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5868728/", "primary_literature_regulator_level", "human and mouse DNA-demethylation models", "DNA-demethylation, ChIP, catalytic-mutant, and expression studies", "TET1 has nonqueued promoter evidence; human IL5 is expression-only and lacks occupancy.", "noncanonical epigenetic regulator capacity only"),
    "anp32e": ("ANP32E", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7546623/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8422973/", "primary_literature_regulator_level", "mouse H2A.Z/chromatin-accessibility models", "H2A.Z chaperoning, accessibility, and neuronal studies", "ANP32E regulates chromatin accessibility but no queued target edge was validated.", "noncanonical chromatin chaperone capacity only"),
    "setd7": ("SETD7/SET7-9", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4763200/", "https://pubmed.ncbi.nlm.nih.gov/27046831/", "primary_literature_regulator_level", "human and mouse methyltransferase/coregulator models", "protein methylation, ChIP, and promoter-complex studies", "SETD7 regulates nonqueued YY1/YAP/Wnt-associated programs; human CCND1 is an ortholog/complex near-match.", "noncanonical chromatin methyltransferase capacity only"),
    "kat2a": ("KAT2A", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11164963/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4195786/", "primary_literature_regulator_level", "mouse cardiomyocyte and hippocampal models", "promoter ChIP-qPCR, perturbation, and chromatin/NF-kB studies", "KAT2A has nonqueued Hmox1/Tfrc and inflammatory chromatin evidence.", "noncanonical chromatin acetyltransferase capacity only"),
    "pcgf3": ("PCGF3", "https://www.nature.com/articles/s41420-024-02194-x.pdf", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM5581257", "primary_literature_regulator_level", "mouse interferon and brain chromatin models", "ChIP-qPCR, loss/gain of function, and expression", "PCGF3 regulates nonqueued interferon-stimulated genes; queued rows remain resource/profile leads.", "noncanonical Polycomb regulator capacity only"),
    "taf2": ("TAF2", "https://pubmed.ncbi.nlm.nih.gov/38773077/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11109217/", "primary_literature_regulator_level", "human TFIID/HCT116 models", "ChIP-seq, shRNA, degradation, and RNA-seq", "TAF2 has basal promoter-selective transcription evidence at nonqueued genes.", "noncanonical transcriptional machinery capacity only"),
    "chaf1b": ("CHAF1B/CAF-1", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10231401/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10469560/", "primary_literature_regulator_level", "human chromatin and interferon models", "ChIP-qPCR/ChIP-seq, perturbation, and reporter assays", "CHAF1B has direct nonqueued ISG15/IFIT1/TRIM13 evidence; queued ETV5 is reverse-direction.", "noncanonical chromatin-assembly capacity only"),
    "ccar2": ("CCAR2/DBC1", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9371912/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5058359/", "primary_literature_regulator_level", "human nuclear-receptor and beta-catenin models", "co-regulator interaction, chromatin, perturbation, and expression studies", "CCAR2 is a broad transcriptional co-regulator with nonqueued target evidence.", "noncanonical transcriptional coregulator capacity only"),
    "arid4b": ("ARID4B", "https://pubmed.ncbi.nlm.nih.gov/26258622/", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE153635", "primary_literature_regulator_level", "mouse Sertoli and chromatin models", "Rhox5 promoter ChIP, loss-of-function, and expression", "ARID4B has direct nonqueued Rhox5 evidence; queued rows are profile-only.", "noncanonical chromatin-coregulator capacity only"),
    "pcgf1": ("PCGF1", "https://www.nature.com/articles/s41467-021-24894-z", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6561741/", "primary_literature_regulator_level", "human and mouse PRC1 models", "PRC1 complex, occupancy, repression, and perturbation studies", "PCGF1 is a variant PRC1 chromatin regulator; queued profile rows lack target-specific direction.", "noncanonical Polycomb regulator capacity only"),
    "cbx4": ("CBX4", "https://pubmed.ncbi.nlm.nih.gov/35837165/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2879644/", "primary_literature_regulator_level", "human and mouse Polycomb/SUMO models", "promoter occupancy, SUMO/corepressor recruitment, and expression", "CBX4 has nonqueued CDC20/Gata4 promoter evidence and is not a canonical sequence-specific TF.", "noncanonical Polycomb-coregulator capacity only"),
    "cdc73": ("CDC73/Parafibromin", "https://pubmed.ncbi.nlm.nih.gov/15580289/", "https://pubmed.ncbi.nlm.nih.gov/25388829/", "primary_literature_regulator_level", "human PAF1 and tumor-suppressor models", "Pol II association, promoter regulation, and RNA-stability studies", "CDC73 is a PAF1-associated transcriptional regulator with nonqueued CCND1/p53 evidence.", "noncanonical transcriptional machinery capacity only"),
    "brd3": ("BRD3", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3107332/", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE119863", "primary_literature_regulator_level", "human and mouse BET-reader models", "GATA1-linked ChIP and BRD3 binding resources", "BRD3 is a chromatin reader with nonqueued promoter evidence.", "noncanonical chromatin-reader capacity only"),
    "setd1a": ("SETD1A", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7873837/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5009724/", "primary_literature_regulator_level", "human and mouse COMPASS models", "H3K4 methylation, occupancy, enhancer/promoter, and perturbation studies", "SETD1A is a chromatin methyltransferase with nonqueued target evidence.", "noncanonical chromatin methyltransferase capacity only"),
    "banp": ("BANP", "https://pubmed.ncbi.nlm.nih.gov/25963627/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5593228/", "primary_literature_regulator_level", "human p53/chromatin models", "p53/p300 interaction, promoter, and expression studies", "BANP is a nuclear transcriptional cofactor with nonqueued target evidence.", "noncanonical transcriptional coregulator capacity only"),
    "brwd1": ("BRWD1", "https://pubmed.ncbi.nlm.nih.gov/24430503/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5902198/", "primary_literature_regulator_level", "mouse chromatin and reproductive models", "chromatin-reader, expression, and developmental perturbation studies", "BRWD1 is a chromatin reader/complex component; queued rows lack target-specific evidence.", "noncanonical chromatin-reader capacity only"),
    "sap30": ("SAP30", "https://pubmed.ncbi.nlm.nih.gov/9702189/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC164750/", "primary_literature_regulator_level", "human and mouse SIN3A-HDAC models", "corepressor recruitment, ChIP, and perturbation studies", "SAP30 is a SIN3A-HDAC corepressor; queued rows lack target-specific direction.", "noncanonical transcriptional coregulator capacity only"),
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

    if key == "auts2" and row["species_scope"] == "human" and target == "ccnd1":
        status = "expression_only_exact_pair_not_promotable"
        primary = "https://www.nature.com/articles/s41598-024-69912-4"
        cell = "human_AUTS2_deleted_hESC_cerebral_organoid_model_not_SCI_target_cell"
        binding = "no_AUTS2_CCND1_occupancy_retrieved"
        downstream = "AUTS2_deletion_increased_CCND1_expression"
        disposition = "retain_expression_only_association_separately"
        exclusions = "The human expression association lacks direct AUTS2 occupancy and may be indirect; no corroborating exact paper was found."
        notes = "Exact human AUTS2-to-CCND1 expression-only association; not promoted."
    elif key == "tet1" and row["species_scope"] == "human" and target == "il5":
        status = "expression_only_exact_pair_not_promotable"
        primary = "https://pmc.ncbi.nlm.nih.gov/articles/PMC5868728/"
        cell = "human_naive_CD4_T_cells_Th1_differentiation_not_SCI_target_cell"
        binding = "no_TET1_IL5_ChIP_or_CUT_Tag_occupancy"
        downstream = "full_length_TET1_increased_IL5_vs_catalytically_inactive_mutant"
        disposition = "retain_expression_only_association_separately"
        exclusions = "Target-specific expression difference lacks direct TET1 occupancy at IL5 and is not sufficient for causal promotion."
        notes = "Exact human TET1-to-IL5 expression-only association; not promoted."
    elif key == "aff4" and row["species_scope"] == "mouse" and target == "cdh1":
        status = "contextual_ortholog_near_match_not_promotable"
        primary = "https://pmc.ncbi.nlm.nih.gov/articles/PMC8865618/"
        cell = "human_HT29_DLD1_HCT116_LoVo_models_not_mouse_SCI_target_cell"
        binding = "no_AFF4_CDH1_promoter_occupancy_reported"
        downstream = "human_AFF4_knockdown_decreased_CDH1_and_overexpression_increased_it_with_rescue"
        disposition = "retain_cross_species_near_match_separately"
        exclusions = "The strong human AFF4-to-CDH1 result does not establish the queued mouse edge or direct occupancy."
        notes = "Cross-species AFF4-to-CDH1 near-match only."
    elif key == "setd7" and row["species_scope"] == "human" and target == "ccnd1":
        status = "contextual_ortholog_complex_near_match_not_promotable"
        primary = "https://pmc.ncbi.nlm.nih.gov/articles/PMC4825718/"
        cell = "hamster_and_mouse_islet_models_not_human_SCI_target_cell"
        binding = "Set7_9_ChIP_at_Cyclin_D1_promoter_in_ISL1_PDX1_complex"
        downstream = "Set7_9_alone_did_not_activate_Cyclin_D1_reporter"
        disposition = "retain_species_complex_near_match_separately"
        exclusions = "The result is ortholog/species mismatched and activation requires the ISL1/PDX1 complex; it does not validate human SETD7-to-CCND1."
        notes = "SETD7-to-CCND1 is a complex-dependent ortholog near-match, not an exact promotion."
    elif key == "taf2" and row["species_scope"] == "human" and target == "ccnd1":
        status = "paralog_subunit_identity_trap_not_promotable"
        primary = "https://pubmed.ncbi.nlm.nih.gov/9926939/"
        binding = "TAFII250_TAF1_not_TAF2"
        downstream = "no_TAF2_specific_CCND1_direction"
        disposition = "exclude_identity_mismatch_separately"
        exclusions = "The older CCND1 paper concerns TAF(II)250/TAF1, not TAF2; subunit identity is not interchangeable."
        notes = "TAF1 evidence was explicitly excluded from human TAF2-to-CCND1."
    elif key == "chaf1b" and row["species_scope"] == "human" and target == "etv5":
        status = "reverse_direction_near_match_not_promotable"
        primary = "https://pmc.ncbi.nlm.nih.gov/articles/PMC8245179/"
        cell = "human_synovial_sarcoma_model_not_SCI_target_cell"
        binding = "ETV5_E2F1_occupancy_not_CHAF1B_to_ETV5"
        downstream = "ETV5_E2F1_regulated_CHAF1B_in_opposite_direction"
        disposition = "retain_reverse_direction_evidence_separately"
        exclusions = "The paper supports ETV5/E2F1 upstream of CHAF1B, not CHAF1B regulation of ETV5."
        notes = "Reverse-direction ETV5-to-CHAF1B evidence was not transferred."
    elif key == "arid4b" and row["species_scope"] == "mouse":
        status = "binding_profile_only_not_promotable"
        primary = "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/ARID4B_TARGET_GENES.html"
        corr = "https://pubmed.ncbi.nlm.nih.gov/26258622/"
        cell = "mouse_GTRD_profile_not_SCI_target_cell"
        binding = "mouse_GTRD_derived_ARID4B_promoter_profile_membership"
        disposition = "retain_mouse_binding_profile_lead_separately"
        notes = "ARID4B queued rows are profile-only; direct Rhox5 evidence is nonqueued."
    elif key == "pcgf1" and row["species_scope"] == "human":
        status = "binding_profile_only_not_promotable" if target != "adora2a" else status
        if target != "adora2a":
            primary = "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/PCGF1_TARGET_GENES.html"
            binding = "human_GTRD_derived_PCGF1_promoter_profile_membership"
            cell = "human_GTRD_profile_not_SCI_target_cell"
            disposition = "retain_human_binding_profile_lead_separately"
            notes = "PCGF1 profile membership is occupancy evidence only."
    elif key == "setd7" and row["species_scope"] == "human":
        status = "binding_profile_only_not_promotable"
        primary = "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/SETD7_TARGET_GENES.html"
        binding = "human_GTRD_derived_SETD7_promoter_profile_membership"
        cell = "human_GTRD_profile_not_SCI_target_cell"
        disposition = "retain_human_binding_profile_lead_separately"
        notes = "SETD7 profile membership is occupancy evidence only; the CCND1 ortholog/complex near-match is recorded above."
    elif key == "chaf1b" and row["species_scope"] == "human":
        status = "binding_profile_only_not_promotable"
        primary = "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/CHAF1B_TARGET_GENES.html"
        binding = "human_GTRD_derived_CHAF1B_promoter_profile_membership"
        cell = "human_GTRD_profile_not_SCI_target_cell"
        disposition = "retain_human_binding_profile_lead_separately"
        notes = "CHAF1B profile membership is occupancy evidence only; the ETV5 row is handled separately as reverse-direction evidence."
    elif key == "cdc73" and row["species_scope"] == "human":
        status = "binding_profile_only_not_promotable"
        primary = "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/CDC73_TARGET_GENES.html"
        binding = "human_GTRD_derived_CDC73_promoter_profile_membership"
        cell = "human_GTRD_profile_not_SCI_target_cell"
        disposition = "retain_human_binding_profile_lead_separately"
        notes = "CDC73 profile membership is occupancy evidence only; nonqueued CCND1/p53 studies do not transfer to these targets."
    elif key == "brd3" and row["species_scope"] == "mouse":
        status = "binding_profile_only_not_promotable"
        primary = "https://www.gsea-msigdb.org/gsea/msigdb/mouse/genesets.jsp?collection=M3"
        binding = "mouse_GTRD_derived_BRD3_promoter_profile_membership"
        cell = "mouse_GTRD_profile_not_SCI_target_cell"
        disposition = "retain_mouse_binding_profile_lead_separately"
        notes = "BRD3 profile membership is occupancy evidence only; BRD4 paralog results were excluded."
    elif key == "smarcc2" and row["species_scope"] == "mouse":
        status = "binding_profile_only_not_promotable"
        primary = "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE37151"
        cell = "mouse_SMARCC2_profile_not_SCI_target_cell"
        binding = "mouse_SMARCC2_FLAG_ChIP_seq_resource_without_queued_locus_validation"
        disposition = "retain_mouse_binding_profile_lead_separately"
    elif key == "auts2" and target != "ccnd1":
        status = "binding_profile_only_not_promotable"
        primary = "https://www.gsea-msigdb.org/gsea/msigdb/cards/AUTS2_TARGET_GENES.html"
        cell = "AUTS2_profile_not_SCI_target_cell"
        binding = "AUTS2_GTRD_derived_profile_membership"
        disposition = "retain_binding_profile_lead_separately"
    elif key == "tet1" and row["species_scope"] == "human" and target != "il5":
        status = "binding_profile_only_not_promotable"
        primary = "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/TET1_TARGET_GENES.html"
        cell = "human_TET1_profile_not_SCI_target_cell"
        binding = "human_GTRD_derived_TET1_profile_membership"
        disposition = "retain_human_binding_profile_lead_separately"
    elif key == "dpf2" and row["species_scope"] == "mouse":
        status = "binding_profile_only_not_promotable"
        primary = "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/DPF2_TARGET_GENES.html"
        cell = "mouse_DPF2_profile_not_SCI_target_cell"
        binding = "mouse_GTRD_derived_DPF2_profile_membership"
        disposition = "retain_mouse_binding_profile_lead_separately"
    elif key == "morc2" and row["species_scope"] == "human" and target == "ctnnb1":
        status = "reverse_pathway_association_not_promotable"
        binding = "no_direct_MORC2_CTNNB1_locus_occupancy"
        downstream = "indirect_Wnt_beta_catenin_pathway_association"
        disposition = "retain_reverse_pathway_association_separately"
        exclusions = "Cancer/Wnt pathway associations do not establish MORC2 regulation of the CTNNB1 locus or a target-specific direction."
        notes = "Indirect pathway association is not transferred to the exact MORC2-to-CTNNB1 edge."
    elif key == "setd1a" and row["species_scope"] == "human":
        if target == "icam5":
            status = "ortholog_expression_near_match_not_promotable"
            primary = "https://pmc.ncbi.nlm.nih.gov/articles/PMC8896793/"
            cell = "mouse_Setd1a_heterozygous_neurons_not_human_SCI_target_cell"
            binding = "no_human_SETD1A_ICAM5_occupancy"
            downstream = "mouse_Setd1a_heterozygous_neuron_Icam5_DEG_without_individual_direction"
            disposition = "retain_cross_species_expression_near_match_separately"
            exclusions = "Mouse neuronal differential expression does not establish the exact human SETD1A-to-ICAM5 edge or direct occupancy."
            notes = "Cross-species expression near-match only."
        else:
            status = "binding_profile_only_not_promotable"
            primary = "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/SETD1A_TARGET_GENES.html"
            binding = "human_GTRD_derived_SETD1A_promoter_profile_membership"
            cell = "human_GTRD_profile_not_SCI_target_cell"
            disposition = "retain_human_binding_profile_lead_separately"
    elif key == "brwd1" and row["species_scope"] == "mouse":
        if target == "bcl2":
            status = "indirect_coexpression_without_regulator_causality_not_promotable"
            primary = "https://pubmed.ncbi.nlm.nih.gov/34111240/"
            corr = "https://pmc.ncbi.nlm.nih.gov/articles/PMC5333536/"
            cell = "mouse_MLL_AF4_leukemia_model_not_SCI_target_cell"
            binding = "BCL2_occupancy_attributed_to_MLL_AF4_DOT1L_not_BRWD1"
            downstream = "Brwd1_and_Bcl2_coexpression_without_BRWD1_perturbation"
            disposition = "retain_indirect_coexpression_lead_separately"
            exclusions = "The model attributes BCL2 regulation to MLL-AF4/DOT1L and does not establish BRWD1 occupancy or causality."
            notes = "Indirect co-expression and other-regulator evidence is not transferred."
        else:
            status = "binding_profile_only_not_promotable"
            primary = "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/BRWD1_TARGET_GENES.html"
            binding = "mouse_GTRD_derived_BRWD1_promoter_profile_membership"
            cell = "mouse_GTRD_profile_not_SCI_target_cell"
            disposition = "retain_mouse_binding_profile_lead_separately"
    elif key == "sap30" and row["species_scope"] == "mouse":
        status = "binding_profile_only_not_promotable"
        primary = "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/SAP30_TARGET_GENES"
        binding = "mouse_GTRD_derived_SAP30_promoter_profile_membership"
        cell = "mouse_GTRD_profile_not_SCI_target_cell"
        disposition = "retain_mouse_binding_profile_lead_separately"

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
        pairs.append({"review_id": f"public_tf_evidence_batch024_pair_{int(row['batch_rank']):02d}_{row['target_rank']}", "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key, "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "source_registry": row["source_registry"], "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"], "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"], "exact_pair_search_url": search_url(row["raw_tf_symbol"], row["target_symbol"], row["species_scope"]), "exact_pair_status": info["status"], "regulator_general_evidence_status": "supported_general_or_authoritative_regulator_evidence", "target_cell_presence_status": info["cell"], "binding_or_association_status": info["binding"], "downstream_expression_or_perturbation_status": info["downstream"], "downstream_activation_status": "not_established_for_SCI_target_cell", "upstream_relay_status": "not_tested_for_exact_pair", "disposition": info["disposition"], "primary_citation": info["primary"], "corroborating_citation": info["corr"], "near_match_exclusions": info["exclusions"], "review_notes": info["notes"] + " " + info["observation"], "exportable": "false", "canonical_write_performed": "false"})
        if key not in seen:
            evidence.append({"evidence_id": f"public_tf_evidence_batch024_regulator_{key}", "regulator_key": key, "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "evidence_layer": "regulator_identity_and_regulatory_capacity", "support_kind": info["kind"], "cell_or_model": info["model"], "assay_or_perturbation": info["assay"], "observation": info["observation"], "effect_direction": "queued-pair direction not established except explicitly recorded limited associations", "primary_citation": info["general_primary"], "corroborating_citation": info["general_corr"], "route_or_module_relevance": info["relevance"], "target_pair_scope": "not evidence for unrelated queued exact pairs; no upstream relay inferred", "exportable": "false", "canonical_write_performed": "false", "limitations": "Regulator-level evidence does not establish SCI target-cell presence, exact queued-target direction, downstream activation, or upstream relay. Profile, chromatin, cofactor, machinery, expression-only, genetic, and cross-species evidence is retained separately from canonical promoter-TF evidence."})
            seen.add(key)
    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch024_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch024_regulator_register.tsv"
    summary_path = args.output_dir / "batch_024_evidence_review_summary.json"
    report_path = args.output_dir / "EVIDENCE_REVIEW_BATCH024.md"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    status_counts: dict[str, int] = {}
    for item in pairs:
        status_counts[item["exact_pair_status"]] = status_counts.get(item["exact_pair_status"], 0) + 1
    pair_keys = {(item["regulator_key"], item["target_symbol"], item["species_scope"], item["source_record_id"]) for item in pairs}
    summary = {"status": "staging_only", "batch_id": "public_tf_evidence_batch_024", "source_set_ranks_reviewed": list(range(1, 26)), "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen), "unique_provenance_aware_pairs": len(pair_keys), "exact_pair_status_counts": status_counts, "regulator_register_rows": len(evidence), "strict_tf_promotion_candidate_rows": 0, "noncanonical_exact_candidate_rows": 0, "exportable_pair_rows": 0, "canonical_writes_performed": False, "module22b_promotions_performed": False, "provenance_preserved": True, "limitations": ["TFLink/profile resources are search leads, not causal regulation.", "Exact-pair negatives are bounded search results, not global absence.", "AUTS2-to-CCND1 and TET1-to-IL5 are expression-only; AFF4-to-CDH1 and SETD7-to-CCND1 are species/complex near-matches; CHAF1B-to-ETV5 is reverse-direction evidence.", "No canonical or Module 22B write was performed."], "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))]}
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path.write_text("\n".join(["# Evidence review: public TF batch 024", "", "Reviewed 100 exact regulator-target-species pairs across 25 noncanonical TFLink source-set ranks.", "", f"- **{len(pairs)}** pairs were reviewed across **{len(seen)}** regulators.", f"- **{status_counts.get('binding_profile_only_not_promotable', 0)}** profile-only rows, expression-only associations, species/complex near-matches, one genetic co-occurrence, and one reverse-direction result were retained without promotion.", "- **0** strict TF or exact noncanonical functional promotion candidates, exportable rows, canonical writes, or Module 22B writes.", "", "All rows retain the original TFLink source record, raw symbol, species, target, graph-module mapping, and local source snapshot. Regulator-level chromatin, cofactor, machinery, profile, expression-only, genetic, and cross-species evidence is recorded separately from exact canonical TF evidence.", ""]) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
