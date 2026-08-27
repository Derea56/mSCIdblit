#!/usr/bin/env python3
"""Stage conservative evidence findings for all Batch 025 pairs.

This is intentionally a staging-only register.  Database membership is kept
with the original source record, while exact literature findings are separated
into canonical-TF, noncanonical-regulator, protein-regulation, and negative or
profile-only dispositions.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/"
    "candidate_triage_v1/evidence_batches/batch_025/"
    "public_tf_evidence_collection_batch_025.tsv"
)
TF_LINK_URL = "https://tflink.net/download/#interaction-gmt"
PAIR_FIELDS = [
    "review_id", "batch_id", "batch_rank", "regulator_key", "regulator_symbol",
    "species_scope", "source_registry", "source_record_id", "raw_tf_symbol",
    "target_symbol", "target_graph_modules", "candidate_membership_status",
    "exact_pair_search_url", "exact_pair_status", "regulator_general_evidence_status",
    "target_cell_presence_status", "binding_or_association_status",
    "downstream_expression_or_perturbation_status", "downstream_activation_status",
    "upstream_relay_status", "disposition", "primary_citation",
    "corroborating_citation", "near_match_exclusions", "review_notes", "exportable",
    "canonical_write_performed",
]
EVIDENCE_FIELDS = [
    "evidence_id", "regulator_key", "regulator_symbol", "species_scope",
    "evidence_layer", "support_kind", "cell_or_model", "assay_or_perturbation",
    "observation", "effect_direction", "primary_citation", "corroborating_citation",
    "route_or_module_relevance", "target_pair_scope", "exportable",
    "canonical_write_performed", "limitations",
]


# symbol, primary, corroboration, support kind, model, assay, observation,
# route/module relevance, profile URL (empty means use TFLink membership).
REGULATORS = {
    "zzz3": ("ZZZ3", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6138639/", "", "primary_literature_regulator_level", "human chromatin-reader/ATAC-complex models", "ATAC-seq, chromatin-complex and expression studies", "ZZZ3 is a histone-acetylation/ATAC-complex component with regulatory capacity, but no queued target-specific result was found.", "noncanonical chromatin-reader capacity only", ""),
    "l3mbtl2": ("L3MBTL2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3647456/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8266391/", "primary_literature_regulator_level", "human and mouse chromatin-repressor models", "promoter occupancy, repressor-complex and loss-of-function studies", "L3MBTL2 is a chromatin repressor; the queued Gpc2 result is complex/locus-level and does not isolate L3MBTL2 causality.", "noncanonical chromatin-repressor capacity only", ""),
    "kdm1b": ("KDM1B", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3518444/", "", "primary_literature_regulator_level", "mouse germ-cell/imprinting models", "H3K4 demethylation, methylation-sensitive expression and imprinting assays", "KDM1B is an epigenetic demethylase with nonqueued imprinting evidence; no queued target edge was validated.", "noncanonical epigenetic-regulator capacity only", ""),
    "baz1a": ("BAZ1A/ACF1", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6391138/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11306231/", "primary_literature_regulator_level", "human and mouse ACF/chromatin-remodeling models", "chromatin occupancy, nucleosome remodeling, knockdown and expression", "BAZ1A is a chromatin-remodeling complex subunit; the queued Ctnnb1 finding is an ortholog/contextual expression association without BAZ1A locus occupancy.", "noncanonical chromatin-remodeler capacity only", ""),
    "carm1": ("CARM1", "https://pubmed.ncbi.nlm.nih.gov/11747826/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7069091/", "primary_literature_regulator_level", "human and mouse nuclear-receptor/coactivator models", "coactivator recruitment, chromatin occupancy, knockdown/CRISPR and expression assays", "CARM1 is a transcriptional coactivator and arginine methyltransferase; human GREB1 has exact target-specific estrogen-response evidence, while other queued rows remain profile leads.", "noncanonical transcriptional-coactivator capacity; GREB1 is an exact queued candidate", ""),
    "smchd1": ("SMCHD1", "https://www.nature.com/articles/s41594-018-0111-z", "https://www.nature.com/articles/s41467-025-62211-0", "primary_literature_regulator_level", "mouse and human chromatin-architecture models", "Hi-C, chromatin-compartment, heterochromatin and loss-of-function assays", "SMCHD1 regulates chromatin architecture and silencing at Hox/X-chromosome and heterochromatin loci, not the queued targets.", "noncanonical chromatin-architecture capacity only", "https://www.gsea-msigdb.org/gsea/msigdb/cards/SMCHD1_TARGET_GENES"),
    "chaf1a": ("CHAF1A/CAF-1", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8498874/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4866648/", "primary_literature_regulator_level", "human neural-crest/neuroblastoma and chromatin models", "ChIP-qPCR, depletion and histone-chaperone assays", "CHAF1A is a CAF-1 histone chaperone/coregulator with direct nonqueued MYCN/ODC1 evidence; queued targets are profile-only.", "noncanonical chromatin-assembly capacity only", ""),
    "prmt5": ("PRMT5", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10312757/", "https://academic.oup.com/nar/article/42/1/235/2437655", "primary_literature_regulator_level", "mouse adipogenesis/MEF/ESC and human cancer models", "ChIP-seq, promoter occupancy, methylation, inhibitor/knockdown and expression assays", "PRMT5 has chromatin occupancy and perturbation evidence at nonqueued loci; EPHA2 is an exact queued post-translational protein-regulation result, not a transcriptional edge.", "noncanonical chromatin/enzyme capacity; receptor-protein regulation kept separate from TF evidence", "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/PRMT5_TARGET_GENES"),
    "bahd1": ("BAHD1", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2728979/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3903274/", "primary_literature_regulator_level", "human chromatin-repression and infection models", "IGF2 promoter ChIP-qPCR, CUT&RUN/ChIP-seq, interaction and perturbation assays", "BAHD1 is a chromatin repressor with direct nonqueued IGF2 evidence; IFNB1 is a same-species complex-level near-match without BAHD1 occupancy at the IFNB1 locus.", "noncanonical chromatin-repressor capacity only", ""),
    "ubn1": ("UBN1", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6171237/", "", "primary_literature_regulator_level", "human and mouse HIRA/H3.3 chromatin models", "HIRA-complex association, chromatin deposition and perturbation assays", "UBN1 is an HIRA-complex chromatin factor; Cebpb and Gpc2 are profile-level leads and the two other queued rows are TFLink-only.", "noncanonical chromatin-assembly capacity only", ""),
    "paf1": ("PAF1", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6055228/", "", "primary_literature_regulator_level", "human PAF1-complex/elongation models", "RNA polymerase II association, ChIP, depletion and transcription assays", "PAF1 is a transcriptional elongation-complex subunit with broad nonqueued regulatory evidence; queued rows are profile-only.", "noncanonical transcriptional-machinery capacity only", "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/PAF1_TARGET_GENES.html"),
    "zmym2": ("ZMYM2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10629813/", "", "primary_literature_regulator_level", "human ZMYM2/CoREST chromatin models", "complex occupancy, repression and perturbation assays", "ZMYM2 is a transcriptional corepressor/complex component; queued rows are profile-only.", "noncanonical transcriptional-corepressor capacity only", "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZMYM2_TARGET_GENES.html"),
    "kat2a": ("KAT2A", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11164963/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4195786/", "primary_literature_regulator_level", "human and mouse acetyltransferase/chromatin models", "promoter ChIP-qPCR, perturbation and chromatin assays", "KAT2A is a chromatin acetyltransferase with nonqueued target evidence; the STAT3 paper is reverse-direction STAT3-to-Kat2a evidence.", "noncanonical chromatin-acetyltransferase capacity only", "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/KAT2A_TARGET_GENES.html"),
    "pcgf6": ("PCGF6", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9357003/", "", "primary_literature_regulator_level", "human and mouse variant-PRC1 models", "PRC1 complex occupancy, repression and stem-cell perturbation assays", "PCGF6 is a Polycomb chromatin regulator with nonqueued SOX2/PRC1 evidence; queued rows are profile-only.", "noncanonical Polycomb-regulator capacity only", "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/PCGF6_TARGET_GENES.html"),
    "asxl2": ("ASXL2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5454368/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7462075/", "primary_literature_regulator_level", "human and mouse ASXL/PR-DUB chromatin models", "complex occupancy, deubiquitination and loss-of-function assays", "ASXL2 is a PR-DUB/chromatin cofactor with nonqueued target evidence; queued rows are profile-only.", "noncanonical chromatin-deubiquitinase capacity only", "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ASXL2_TARGET_GENES.html"),
    "smyd2": ("SMYD2", "https://pubmed.ncbi.nlm.nih.gov/31348575/", "", "primary_literature_regulator_level", "mouse and human lysine-methyltransferase models", "histone/protein methylation, promoter association and perturbation assays", "SMYD2 is a chromatin/protein methyltransferase with nonqueued target evidence; queued mouse rows are profile-only.", "noncanonical chromatin-methyltransferase capacity only", "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/SMYD2_TARGET_GENES.html"),
    "cdyl": ("CDYL", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5572458/", "https://pubmed.ncbi.nlm.nih.gov/28842554/", "primary_literature_regulator_level", "mouse hippocampal chromatin-repression models", "ChIP-seq/qChIP, chromodomain binding and neuronal perturbation assays", "CDYL is a chromatin-repressor/reader; Cacng3 and Glra1 have direct occupancy-only evidence without a secure individual perturbation direction.", "noncanonical chromatin-repressor capacity only", ""),
    "smc4": ("SMC4", "https://www.ncbi.nlm.nih.gov/gene/10051", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4045092/", "primary_literature_regulator_level", "human and mouse cohesin/condensin chromatin models", "condensin complex, chromosome organization and depletion assays", "SMC4 is a condensin structural subunit, not a sequence-specific TF; no queued target-specific edge was validated.", "noncanonical chromosome-organization capacity only", ""),
    "tle5": ("TLE5/AES/Grg5", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3234724/", "https://pubmed.ncbi.nlm.nih.gov/15183720/", "primary_literature_regulator_level", "human AES/TLE5 and mouse Grg5/RUNX2 developmental models", "coregulator interaction, loss-of-function, in situ hybridization and Hedgehog assays", "TLE5/Grg5 is a Groucho-family coregulator that does not bind DNA independently; Grg5 loss affects Ihh and downstream Hedgehog signaling, but direct Ihh occupancy was not shown.", "noncanonical transcriptional-coregulator capacity only", ""),
    "znf532": ("ZNF532", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5448232/", "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF532_TARGET_GENES.html", "authoritative_binding_dataset_only", "human ZNF532/NUT ChIP-seq models", "ChIP-seq and harmonized promoter-profile construction", "ZNF532 has genuine human ChIP-seq/profile evidence for the queued genes, but no target-specific perturbation or regulatory direction was found.", "binding-profile capacity only", "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF532_TARGET_GENES.html"),
    "bap18": ("BAP18", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5041452/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7641737/", "primary_literature_regulator_level", "human androgen-receptor/ERalpha chromatin models", "coregulator recruitment, ChIP and knockdown assays", "BAP18 has direct chromatin-coregulator evidence at AR, ERalpha and S100A9 loci, not the queued targets.", "noncanonical transcriptional-coregulator capacity only", ""),
    "dppa3": ("DPPA3/STELLA", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4354275/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11187062/", "primary_literature_regulator_level", "mouse imprinting/reprogramming and human UHRF1 models", "imprinting methylation, chromatin interaction and perturbation assays", "DPPA3 has chromatin/DNA-demethylation evidence, but the queued human targets lacked exact target-level support and human/mouse functions are not interchangeable.", "noncanonical epigenetic/chromatin capacity only", ""),
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


def profile_status(row: dict[str, str], info: tuple[str, ...], source: str = "GTRD_derived") -> dict[str, str]:
    symbol, primary, corr, _kind, _model, _assay, _obs, _rel, profile = info
    species = row["species_scope"]
    profile_citation = profile or TF_LINK_URL
    return {
        "status": "binding_profile_only_not_promotable",
        "primary": profile_citation,
        "corr": corr if profile else "",
        "cell": f"{species}_{source}_profile_not_SCI_target_cell",
        "binding": f"{species}_{source}_promoter_profile_membership",
        "downstream": "no_target_specific_perturbation_or_direction_found",
        "disposition": "retain_binding_profile_lead_separately",
        "exclusions": "Promoter-profile/database membership is a search lead; it does not establish target-cell presence, causal direction, downstream activation, or an upstream relay.",
        "notes": "Exact species-matched profile evidence is retained as a noncanonical binding lead only.",
    }


def classify(row: dict[str, str]) -> dict[str, str]:
    key = row["regulator_key"]
    target = row["target_symbol"].lower()
    if key not in REGULATORS:
        raise SystemExit(f"missing evidence map for {key}")
    info = REGULATORS[key]
    symbol, general_primary, general_corr, kind, model, assay, observation, relevance, _profile = info
    out = {
        "symbol": symbol, "general_primary": general_primary, "general_corr": general_corr,
        "kind": kind, "model": model, "assay": assay, "observation": observation,
        "relevance": relevance, "status": "database_membership_only_not_promotable",
        "primary": TF_LINK_URL, "corr": "", "cell": "not_established_for_exact_pair",
        "binding": "TFLink_membership_only_no_queued_locus_validation",
        "downstream": "not_found_for_exact_pair",
        "disposition": "retain_provenance_traceable_candidate_without_promotion",
        "exclusions": "TFLink/database membership is a search lead; broad regulator evidence, orthologs, paralogs, reverse directions and complex-level findings were not transferred to this exact pair.",
        "notes": "No exact target-specific causal edge was established; target-cell presence, downstream activation and upstream relay are not inferred.",
    }

    if key == "carm1" and row["species_scope"] == "human" and target == "greb1":
        out.update(status="functional_noncanonical_coactivator_candidate_not_strict_tf", primary="https://pubmed.ncbi.nlm.nih.gov/26505218/", corr="https://pmc.ncbi.nlm.nih.gov/articles/PMC7069091/", cell="human_MCF7_ERalpha_positive_model_not_SCI_target_cell", binding="CARM1_occupancy_at_ERalpha_bound_GREB1_regulatory_regions", downstream="CARM1_knockdown_or_CRISPR_loss_reduced_estrogen_induced_GREB1_and_PolII", disposition="retain_noncanonical_coactivator_candidate_pending_SCI_context", exclusions="The exact human target result is a nuclear-receptor coactivator mechanism, not a sequence-specific TF; no SCI target-cell validation or upstream relay was established.", notes="Exact human CARM1-to-GREB1 occupancy/perturbation evidence is staged in the noncanonical regulatory category.")
    elif key == "tle5" and row["species_scope"] == "mouse" and target == "ihh":
        out.update(status="functional_noncanonical_coregulator_candidate_not_strict_tf", primary="https://pubmed.ncbi.nlm.nih.gov/11984876/", corr="https://pubmed.ncbi.nlm.nih.gov/15183720/", cell="mouse_Grg5_null_growth_plate_model_not_SCI_target_cell", binding="no_direct_Tle5_or_Grg5_Ihh_occupancy;_Runx2_coregulator_interaction", downstream="Grg5_loss_decreased_Ihh_mRNA_or_protein_and_reduced_Ptc_Smo_signaling", disposition="retain_noncanonical_coregulator_candidate_pending_direct_occupancy_and_SCI_context", exclusions="The exact target perturbation is indirect and coregulator/Runx2-mediated; direct Tle5/Grg5 binding at Ihh was not demonstrated, so this is not a strict TF edge.", notes="Exact mouse Tle5/Grg5-to-Ihh perturbation evidence is staged as noncanonical coregulator evidence.")
    elif key == "prmt5" and row["species_scope"] == "human" and target == "epha2":
        out.update(status="target_protein_stability_regulation_not_transcriptional", primary="https://pmc.ncbi.nlm.nih.gov/articles/PMC13042777/", cell="human_SUNE1_HK1_and_HEK293_models_not_SCI_target_cell", binding="PRMT5_directly_interacted_with_and_methylated_EphA2_protein;_no_EPHA2_locus_occupancy", downstream="PRMT5_knockdown_reduced_EphA2_methylation_and_protein_stability_without_EphA2_mRNA_change", disposition="retain_target_protein_regulation_in_receptor_evidence_category", exclusions="This is exact receptor/protein-stability regulation, not transcriptional regulation. It must not be used as evidence that PRMT5 activates or represses the EPHA2 gene.", notes="Exact human PRMT5-to-EPHA2 post-translational evidence is routed to target-protein/receptor evidence, not canonical TF evidence.")
    elif key == "prmt5" and row["species_scope"] == "human" and target == "axl":
        out.update(status="expression_response_without_occupancy_not_promotable", primary="https://link.springer.com/article/10.1186/s13046-024-03270-x", cell="human_HACC2A_and_UFH2_adrenocortical_models_not_SCI_target_cell", binding="no_PRMT5_AXL_locus_occupancy_reported", downstream="selective_PRMT5_inhibitor_PRT543_reduced_AXL_expression", disposition="retain_expression_response_separately", exclusions="The pharmacologic response lacks direct PRMT5 locus occupancy and genetic causal isolation; it is not sufficient for a TF edge.", notes="Exact human AXL expression response is retained separately from transcriptional occupancy evidence.")
    elif key == "bahd1" and row["species_scope"] == "human" and target == "ifnb1":
        out.update(status="contextual_complex_near_match_not_promotable", primary="https://pmc.ncbi.nlm.nih.gov/articles/PMC3903274/", cell="human_epithelial_Listeria_infection_models_not_SCI_target_cell", binding="BAHD1_occupancy_at_IFITM1_and_IFIT3_not_IFNB1_promoter", downstream="LntA_inhibition_of_BAHD1_increased_interferon_response_genes_and_IFNB1_induction_was_complex_dependent", disposition="retain_complex_level_near_match_separately", exclusions="The paper does not establish BAHD1 occupancy at the IFNB1 locus; the result is a contextual LntA-BAHD1 complex effect and not an exact BAHD1-to-IFNB1 edge.", notes="Same-species complex-level interferon evidence is retained without transfer to the exact queued locus.")
    elif key == "l3mbtl2" and row["species_scope"] == "mouse" and target == "gpc2":
        out.update(status="contextual_complex_locus_only_not_promotable", primary="https://pmc.ncbi.nlm.nih.gov/articles/PMC8266391/", cell="mouse_lung_tumor_models_not_SCI_target_cell", binding="promoter_proximal_occupancy_at_Gpc2_with_MGA_E2F6_MAX_complex;_L3MBTL2_not_isolated", downstream="complex_or_MGA_perturbation_effect_not_L3MBTL2_specific", disposition="retain_complex_locus_evidence_separately", exclusions="The locus result is attributable to a multiprotein complex and does not isolate L3MBTL2 occupancy or causal direction.", notes="Mouse Gpc2 complex/locus evidence is retained as noncanonical chromatin-complex evidence.")
    elif key == "baz1a" and row["species_scope"] == "mouse" and target == "ctnnb1":
        out.update(status="contextual_ortholog_expression_only_not_promotable", primary="https://pmc.ncbi.nlm.nih.gov/articles/PMC11306231/", cell="human_HCT116_and_SW620_models_not_mouse_SCI_target_cell", binding="no_BAZ1A_occupancy_at_CTNNB1_locus_reported", downstream="human_BAZ1A_knockdown_reduced_CTNNB1_or_beta_catenin_pathway_expression", disposition="retain_cross_species_expression_near_match_separately", exclusions="The result is human, ortholog/contextual and expression-based without BAZ1A occupancy at CTNNB1; it does not validate the queued mouse edge.", notes="Cross-species BAZ1A-to-CTNNB1 expression association is retained without promotion.")
    elif key == "kat2a" and row["species_scope"] == "human" and target == "stat3":
        out.update(status="reverse_direction_near_match_not_promotable", primary="https://pmc.ncbi.nlm.nih.gov/articles/PMC7618962/", cell="mouse_4T1_and_EMT6_5_models_not_human_SCI_target_cell", binding="STAT3_occupancy_or_regulation_of_Kat2a_not_KAT2A_to_STAT3", downstream="STAT3_knockdown_or_inhibition_changed_Kat2a_in_opposite_direction", disposition="retain_reverse_direction_evidence_separately", exclusions="The evidence supports STAT3 upstream of Kat2a, not KAT2A regulation of STAT3; species and direction also differ.", notes="Reverse-direction evidence was explicitly excluded from the queued KAT2A-to-STAT3 edge.")
    elif key == "cdyl" and row["species_scope"] == "mouse" and target in {"cacng3", "glra1"}:
        out.update(status="direct_binding_only_not_promotable", primary="https://pmc.ncbi.nlm.nih.gov/articles/PMC5572458/", corr="https://pubmed.ncbi.nlm.nih.gov/28842554/", cell="mouse_hippocampal_neuronal_model_not_SCI_target_cell", binding="CDYL_direct_hippocampal_ChIP_seq_or_qChIP_occupancy_at_queued_locus", downstream="no_secure_individual_CDYL_perturbation_direction_for_target", disposition="retain_direct_binding_lead_separately", exclusions="Direct occupancy alone does not establish activation/repression, target-cell presence or an SCI relay.", notes="Exact mouse CDYL binding evidence is staged as occupancy-only noncanonical evidence.")
    elif key == "tle5" and row["species_scope"] == "human" and target == "lef1":
        out.update(status="complex_or_paralog_level_near_match_not_promotable", primary="https://pmc.ncbi.nlm.nih.gov/articles/PMC3234724/", cell="human_AES_TLE5_coregulator_models_not_SCI_target_cell", binding="TLE_family_coregulator_evidence_without_TLE5_LEF1_locus_occupancy", downstream="no_TLE5_specific_LEF1_direction_found", disposition="retain_complex_level_near_match_separately", exclusions="TLE1/Groucho-family studies are not interchangeable with TLE5 and do not establish the queued LEF1 edge.", notes="Paralog/complex evidence was kept separate from exact TLE5-to-LEF1 evidence.")
    elif key in {"ubn1", "paf1", "zmym2", "kat2a", "pcgf6", "asxl2", "smyd2", "znf532", "chaf1a", "smchd1", "prmt5", "bahd1", "carm1"}:
        # Only rows for which the lane report explicitly found a profile hit
        # receive this label.  Specific unsupported exceptions above remain
        # database-only, preserving a bounded negative result.
        profile_keys = {
            "ubn1": {"cebpb", "gpc2"},
            "paf1": {"cyp19a1", "efna1", "abca7", "acin1"},
            "zmym2": {"gdf15", "adprhl1", "adrm1", "ahcy"},
            "kat2a": {"aurakaip1", "bola1", "c11orf68"},
            "pcgf6": {"cklf", "ablim3", "aldoa", "amn1"},
            "asxl2": {"adgrb3", "ap3b2", "barhl1", "ca11"},
            "smyd2": {"lamb1", "btg1b", "ccdc7b", "gata6"},
            "znf532": {"aco2", "aimp1", "alg2", "atp5mg"},
            "chaf1a": {"adgrl1", "igf1r", "insr", "acox2"},
            "smchd1": {"cntn3", "cxcl12", "itga7", "lamp1", "adgrb3", "ang", "ak1"},
            "prmt5": {"nrp1", "abca10"},
            "bahd1": {"nhlh2", "npbwr1", "abcc9"},
            "carm1": {"adora1", "carm1", "lamb1", "col13a1", "col16a1", "cyp19a1", "reln"},
        }
        if target in profile_keys.get(key, set()):
            out.update(profile_status(row, info))
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_BATCH.parent)
    args = parser.parse_args()
    rows = read_tsv(args.batch)
    if len(rows) != 95:
        raise SystemExit(f"expected 95 rows, found {len(rows)}")

    pairs: list[dict[str, str]] = []
    evidence: list[dict[str, str]] = []
    seen: set[str] = set()
    for row in rows:
        info = classify(row)
        pairs.append({
            "review_id": f"public_tf_evidence_batch025_pair_{int(row['batch_rank']):02d}_{row['target_rank']}",
            "batch_id": row["batch_id"], "batch_rank": row["batch_rank"],
            "regulator_key": row["regulator_key"], "regulator_symbol": info["symbol"],
            "species_scope": row["species_scope"], "source_registry": row["source_registry"],
            "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"],
            "target_symbol": row["target_symbol"], "target_graph_modules": row["target_graph_modules"],
            "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": search_url(row["raw_tf_symbol"], row["target_symbol"], row["species_scope"]),
            "exact_pair_status": info["status"],
            "regulator_general_evidence_status": "supported_general_or_authoritative_regulator_evidence",
            "target_cell_presence_status": info["cell"], "binding_or_association_status": info["binding"],
            "downstream_expression_or_perturbation_status": info["downstream"],
            "downstream_activation_status": "not_established_for_SCI_target_cell",
            "upstream_relay_status": "not_tested_for_exact_pair", "disposition": info["disposition"],
            "primary_citation": info["primary"], "corroborating_citation": info["corr"],
            "near_match_exclusions": info["exclusions"], "review_notes": info["notes"] + " " + info["observation"],
            "exportable": "false", "canonical_write_performed": "false",
        })
        key = row["regulator_key"]
        if key not in seen:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch025_regulator_{key}",
                "regulator_key": key, "regulator_symbol": info["symbol"], "species_scope": row["species_scope"],
                "evidence_layer": "regulator_identity_and_regulatory_capacity", "support_kind": info["kind"],
                "cell_or_model": info["model"], "assay_or_perturbation": info["assay"],
                "observation": info["observation"],
                "effect_direction": "queued-pair direction not established except explicitly recorded limited associations",
                "primary_citation": info["general_primary"], "corroborating_citation": info["general_corr"],
                "route_or_module_relevance": info["relevance"],
                "target_pair_scope": "not evidence for unrelated queued exact pairs; no upstream relay inferred",
                "exportable": "false", "canonical_write_performed": "false",
                "limitations": "Regulator-level evidence does not establish SCI target-cell presence, exact queued-target direction, downstream activation or upstream relay. Profile, chromatin, cofactor, machinery, protein-regulation, epigenetic and cross-species evidence is retained separately from canonical promoter-TF evidence.",
            })
            seen.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch025_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch025_regulator_register.tsv"
    summary_path = args.output_dir / "batch_025_evidence_review_summary.json"
    report_path = args.output_dir / "EVIDENCE_REVIEW_BATCH025.md"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    status_counts: dict[str, int] = {}
    for item in pairs:
        status_counts[item["exact_pair_status"]] = status_counts.get(item["exact_pair_status"], 0) + 1
    pair_keys = {(x["regulator_key"], x["target_symbol"], x["species_scope"], x["source_record_id"]) for x in pairs}
    noncanonical = sum(v for k, v in status_counts.items() if k.startswith("functional_noncanonical_"))
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_025",
        "source_set_ranks_reviewed": list(range(1, 26)), "pair_rows_reviewed": len(pairs),
        "unique_regulators_reviewed": len(seen), "unique_provenance_aware_pairs": len(pair_keys),
        "exact_pair_status_counts": status_counts, "regulator_register_rows": len(evidence),
        "strict_tf_promotion_candidate_rows": 0, "noncanonical_exact_candidate_rows": noncanonical,
        "exportable_pair_rows": 0, "canonical_writes_performed": False,
        "module22b_promotions_performed": False, "provenance_preserved": True,
        "limitations": [
            "TFLink/profile resources are search leads, not causal regulation.",
            "Exact-pair negatives are bounded search results, not global absence.",
            "CARM1-to-GREB1 and Tle5/Grg5-to-Ihh are exact noncanonical candidate mechanisms without SCI-cell validation or strict TF occupancy.",
            "PRMT5-to-EPHA2 is protein-stability evidence and BAHD1-to-IFNB1 is a complex-level near-match; neither is a transcriptional TF edge.",
            "No canonical or Module 22B write was performed.",
        ],
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path.write_text("\n".join([
        "# Evidence review: public TF batch 025", "",
        f"Reviewed {len(pairs)} exact regulator-target-species pairs across 25 TFLink source-set ranks.", "",
        f"- **{len(pairs)}** pairs were reviewed across **{len(seen)}** regulators.",
        f"- **{noncanonical}** exact noncanonical candidate rows were staged: human CARM1-to-GREB1 and mouse Tle5/Grg5-to-Ihh.",
        f"- **{status_counts.get('binding_profile_only_not_promotable', 0)}** profile-only rows were retained without promotion.",
        f"- **{status_counts.get('target_protein_stability_regulation_not_transcriptional', 0)}** exact receptor/protein-regulation row was routed outside TF evidence.",
        "- **0** strict TF promotion candidates, exportable rows, canonical writes, or Module 22B writes.", "",
        "All rows retain the original TFLink source record, raw symbol, species, target, graph-module mapping and local source snapshot. Regulator-level chromatin, cofactor, machinery, profile, protein-regulation and cross-species evidence is recorded separately from exact canonical TF evidence.", "",
    ]) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
