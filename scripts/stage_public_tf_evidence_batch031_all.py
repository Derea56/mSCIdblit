#!/usr/bin/env python3
"""Stage conservative evidence findings for all literal Batch 031 pairs."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/"
    "candidate_triage_v1/evidence_batches/batch_031/"
    "public_tf_evidence_collection_batch_031.tsv"
)
TF_LINK_URL = "https://tflink.net/download/"
PAIR_FIELDS = [
    "review_id", "batch_id", "batch_rank", "regulator_key", "regulator_symbol", "species_scope",
    "source_registry", "source_record_id", "raw_tf_symbol", "target_symbol", "target_graph_modules",
    "candidate_membership_status", "exact_pair_search_url", "exact_pair_status",
    "regulator_general_evidence_status", "target_cell_presence_status", "binding_or_association_status",
    "downstream_expression_or_perturbation_status", "downstream_activation_status", "upstream_relay_status",
    "disposition", "primary_citation", "corroborating_citation", "near_match_exclusions", "review_notes",
    "exportable", "canonical_write_performed",
]
EVIDENCE_FIELDS = [
    "evidence_id", "regulator_key", "regulator_symbol", "species_scope", "evidence_layer", "support_kind",
    "cell_or_model", "assay_or_perturbation", "observation", "effect_direction", "primary_citation",
    "corroborating_citation", "route_or_module_relevance", "target_pair_scope", "exportable",
    "canonical_write_performed", "limitations",
]

# symbol, primary, corroboration, support kind, model, assay, observation, relevance.
# These are regulator-level identity/capacity sources and are deliberately not
# treated as evidence for any exact queued target pair.
REGULATORS = {
    "ice2": ("ICE2/NARG2", "https://www.ncbi.nlm.nih.gov/gene/79664", "https://pubmed.ncbi.nlm.nih.gov/25575120/", "authoritative_identity_and_primary_literature", "human ICE2/NARG2 little-elongation-complex models", "LEC-complex assembly and snRNA-transcription assays", "ICE2/NARG2 is a little elongation complex subunit involved in snRNA transcription, not a sequence-specific TF; the queued targets were not validated.", "noncanonical transcriptional-machinery capacity only"),
    "znf830": ("ZNF830", "https://www.ncbi.nlm.nih.gov/gene/?term=ZNF830%5BGene%20Name%5D%20AND%20Homo%20sapiens%5BOrganism%5D", "https://www.uniprot.org/uniprotkb/Q96NB3/entry", "authoritative_identity_and_profile_context", "human ZNF830 annotation and regulon-profile context", "gene/protein annotation and GTRD-derived profile", "ZNF830 identity is supported, and JAG1 is present in a documented ZNF830 target profile; no causal direction or SCI-cell validation was found.", "profile-only regulon lead; queued edges unsupported"),
    "cshl1": ("CSHL1/CSH1L", "https://www.ncbi.nlm.nih.gov/gene/1444", "https://www.ncbi.nlm.nih.gov/gene/?term=CSHL1%5BGene%20Name%5D%20AND%20Homo%20sapiens%5BOrganism%5D", "authoritative_identity_review", "human chorionic-somatomammotropin-like protein annotation", "gene/protein identity and secreted-protein annotation", "CSHL1 is a chorionic somatomammotropin hormone-like secreted protein, not a sequence-specific TF; no queued target mechanism was validated.", "identity/category mismatch; secreted-protein lead only"),
    "h1-6": ("H1-6/H1F6/H1T", "https://www.ncbi.nlm.nih.gov/gene/107970", "https://www.uniprot.org/uniprotkb/Q07133/entry", "authoritative_identity_and_chromatin_annotation", "mouse testis-specific linker-histone/chromatin models", "histone occupancy, knockout and chromatin assays", "The mouse H1-6 record is H1f6/H1t, a linker histone/chromatin protein, not a sequence-specific TF; the queued targets were not validated.", "noncanonical chromatin capacity only"),
    "za": ("ZA (identity unresolved)", "https://www.genenames.org/", "https://tflink.net/download/", "identity_unresolved", "human source-record identity review", "symbol reconciliation and source-record review", "The raw symbol ZA could not be mapped confidently to an approved human gene identity; no target evidence is assigned.", "identity-review hold"),
    "cavin1": ("CAVIN1/PTRF", "https://www.ncbi.nlm.nih.gov/gene/?term=CAVIN1%5BGene%20Name%5D%20AND%20Homo%20sapiens%5BOrganism%5D", "https://www.uniprot.org/uniprotkb/Q6NZI2/entry", "authoritative_identity_and_protein_annotation", "human caveolar/cavin protein models", "protein-complex and caveolae annotation", "CAVIN1 is a caveolar structural protein, not a canonical TF; queued target edges were not validated.", "noncanonical structural/protein-complex capacity only"),
    "mettl14": ("METTL14", "https://www.ncbi.nlm.nih.gov/gene/?term=METTL14%5BGene%20Name%5D%20AND%20Homo%20sapiens%5BOrganism%5D", "https://pubmed.ncbi.nlm.nih.gov/27892910/", "primary_literature_regulator_level", "human METTL3-METTL14 RNA-modification models", "m6A-complex, RNA-modification and perturbation assays", "METTL14 is an m6A RNA-methyltransferase-complex component, not a DNA-binding TF; JUND is retained only as a regulon-profile lead.", "noncanonical RNA-regulatory capacity; profile-only queued lead"),
    "rbp2": ("RBP2/CRBP2 (P50120)", "https://www.ncbi.nlm.nih.gov/gene/5948", "https://www.uniprot.org/uniprotkb/P50120/entry", "authoritative_identity_correction", "human cellular-retinol-binding-protein-2 annotation", "gene/protein identity review and retinoid-binding annotation", "The queued RBP2 record maps to CRBP2/P50120, a cellular retinol-binding protein; it is not the separate KDM5A/RBP2 alias. No queued target was validated.", "identity-correction hold; no TF or chromatin evidence transferred"),
    "rimbp2": ("RIMBP2", "https://www.ncbi.nlm.nih.gov/gene/?term=RIMBP2%5BGene%20Name%5D%20AND%20Homo%20sapiens%5BOrganism%5D", "https://www.uniprot.org/uniprotkb/Q7Z5W3/entry", "authoritative_identity_and_protein_annotation", "human presynaptic RIMBP2 models", "protein-interaction and synaptic-release assays", "RIMBP2 is a presynaptic scaffold, not a canonical TF; queued target edges were not validated.", "noncanonical neuronal protein-scaffold capacity only"),
    "srpk1": ("SRPK1", "https://www.ncbi.nlm.nih.gov/gene/?term=SRPK1%5BGene%20Name%5D%20AND%20Homo%20sapiens%5BOrganism%5D", "https://www.uniprot.org/uniprotkb/Q96SB4/entry", "authoritative_identity_and_primary_literature", "human SRPK1 kinase/splicing models", "kinase, SR-protein phosphorylation, splicing and perturbation assays", "SRPK1 is a serine-arginine protein kinase with splicing functions, not a sequence-specific TF; four queued targets are retained only as profile leads.", "noncanonical kinase/RNA-processing capacity; profile-only queued leads"),
    "brf2": ("BRF2", "https://www.ncbi.nlm.nih.gov/gene/?term=BRF2%5BGene%20Name%5D%20AND%20Homo%20sapiens%5BOrganism%5D", "https://www.uniprot.org/uniprotkb/Q9HAW0/entry", "authoritative_identity_and_transcriptional_machinery_annotation", "human RNA-polymerase-III initiation models", "TFIIIB/Pol-III complex and transcription assays", "BRF2 is a general transcription-initiation factor, not a sequence-specific TF; queued targets were not validated.", "noncanonical transcriptional-machinery capacity only"),
    "zfp36l2": ("ZFP36L2", "https://www.ncbi.nlm.nih.gov/gene/?term=ZFP36L2%5BGene%20Name%5D%20AND%20Homo%20sapiens%5BOrganism%5D", "https://www.uniprot.org/uniprotkb/P47974/entry", "authoritative_identity_and_primary_literature", "human ZFP36L2 RNA-binding immune models", "RNA-binding, mRNA-destabilization and lymphocyte assays", "ZFP36L2 is an RNA-binding post-transcriptional regulator; the queued targets were not validated as direct transcriptional targets.", "noncanonical RNA-regulatory capacity only"),
    "cgas": ("CGAS/MB21D1", "https://www.ncbi.nlm.nih.gov/gene/?term=MB21D1%5BGene%20Name%5D%20AND%20Homo%20sapiens%5BOrganism%5D", "https://pubmed.ncbi.nlm.nih.gov/23258412/", "primary_literature_regulator_level", "mouse cGAS-STING innate-immune models", "DNA sensing, cGAMP, STING and cytokine assays", "cGAS/MB21D1 is a cytosolic DNA sensor, not a canonical TF; the mouse queued targets were not validated as direct cGAS-regulated loci.", "noncanonical innate-signaling capacity only"),
    "cobll1": ("COBLL1", "https://www.ncbi.nlm.nih.gov/gene/?term=COBLL1%5BGene%20Name%5D%20AND%20Homo%20sapiens%5BOrganism%5D", "https://www.uniprot.org/uniprotkb/Q53SF7/entry", "authoritative_identity_and_protein_annotation", "human COBLL1 cytoskeletal models", "protein localization and cell-shape assays", "COBLL1 is a cytoskeletal/actin-associated protein, not a canonical TF; queued targets were not validated.", "noncanonical structural capacity only"),
    "maml3": ("MAML3", "https://www.ncbi.nlm.nih.gov/gene/55534", "https://pubmed.ncbi.nlm.nih.gov/22069191/", "primary_literature_regulator_level", "mouse Notch/MAML3 models", "Notch intracellular-domain, CSL-complex and developmental assays", "MAML3 is a Notch transcriptional coactivator; the queued target-specific edges were not validated.", "noncanonical Notch coactivator capacity only"),
    "ube2i": ("UBE2I/UBC9", "https://www.uniprot.org/uniprotkb/P63279/entry", "https://reactome.org/content/detail/R-HSA-2984281", "authoritative_identity_and_primary_pathway_annotation", "human SUMO-conjugation models", "SUMO E2-conjugation, interaction and pathway assays", "UBE2I/UBC9 is a SUMO E2-conjugating enzyme, not a TF; four queued targets are retained only as GTRD profile leads.", "noncanonical post-translational/protein-regulatory capacity; profile-only queued leads"),
    "igf1r": ("IGF1R", "https://www.ncbi.nlm.nih.gov/gene/3480", "https://www.uniprot.org/uniprotkb/P08069/entry", "authoritative_identity_and_primary_literature", "human IGF1R receptor-signaling models", "ligand binding, kinase and downstream signaling assays", "IGF1R is a receptor tyrosine kinase, not a TF; its self-target profile row is retained only as a database profile lead.", "ligand/receptor signaling capacity; profile-only queued lead"),
    "nfam1": ("NFAM1", "https://www.ncbi.nlm.nih.gov/gene/?term=NFAM1%5BGene%20Name%5D", "https://www.uniprot.org/uniprotkb/Q8NET1/entry", "authoritative_identity_and_immune_annotation", "human and mouse NFAM1 immune-receptor models", "immune-receptor signaling and expression assays", "NFAM1 is an immune receptor-associated signaling protein, not a canonical TF; the queued cytokine edges were not validated.", "noncanonical immune-signaling capacity only"),
    "tert": ("TERT", "https://www.ncbi.nlm.nih.gov/gene/7015", "https://pubmed.ncbi.nlm.nih.gov/27548225/", "primary_literature_regulator_level", "human telomerase and cancer models", "telomerase, promoter, chromatin and noncanonical-function assays", "TERT has documented telomerase and noncanonical nuclear functions, but the queued target rows are only GTRD profile leads and do not establish TERT DNA binding or causal target regulation.", "noncanonical nuclear/telomerase capacity; profile-only queued leads"),
    "syncrip": ("SYNCRIP/hnRNP Q", "https://www.ncbi.nlm.nih.gov/gene/10492", "https://www.uniprot.org/uniprotkb/O60506/entry", "authoritative_identity_and_rna_annotation", "human SYNCRIP RNA-binding models", "RNA binding, localization and post-transcriptional assays", "SYNCRIP is an RNA-binding protein, not a canonical TF; ANXA2 is retained only as a GTRD profile lead.", "noncanonical RNA-regulatory capacity; profile-only queued lead"),
    "casp8ap2": ("CASP8AP2/FLASH", "https://www.ncbi.nlm.nih.gov/gene/9994", "https://www.uniprot.org/uniprotkb/Q9UKL3/entry", "authoritative_identity_and_cellular_annotation", "human CASP8AP2/FLASH apoptosis and RNA-processing models", "protein-complex, apoptosis and RNA-processing assays", "CASP8AP2/FLASH is a cellular cofactor, not a canonical TF; queued target edges were not validated.", "noncanonical cofactor capacity only"),
    "ice1": ("ICE1", "https://www.ncbi.nlm.nih.gov/gene/?term=ICE1%5BGene%20Name%5D%20AND%20Homo%20sapiens%5BOrganism%5D", "https://www.uniprot.org/uniprotkb/Q9Y2F5/entry", "authoritative_identity_and_complex_annotation", "human ICE1/MYC transcriptional-complex models", "complex, RNA-processing and transcription assays", "ICE1 is a transcriptional-complex/RNA-processing factor rather than a sequence-specific TF; queued target edges were not validated.", "noncanonical transcriptional-complex capacity only"),
    "ptpra": ("PTPRA", "https://www.ncbi.nlm.nih.gov/gene/5786", "https://www.uniprot.org/uniprotkb/P18433/entry", "authoritative_identity_and_primary_literature", "human receptor-protein-tyrosine-phosphatase models", "phosphatase, receptor-signaling and substrate assays", "PTPRA is a receptor-type protein tyrosine phosphatase, not a TF; queued targets were not validated.", "noncanonical receptor/phosphatase capacity only"),
    "gadd45a": ("GADD45A", "https://www.ncbi.nlm.nih.gov/gene/1647", "https://www.uniprot.org/uniprotkb/P24522/entry", "authoritative_identity_and_stress_response_annotation", "mouse Gadd45a stress/DNA-repair models", "stress response, DNA-repair and expression assays", "Gadd45a is a stress-response/DNA-repair regulator, not a sequence-specific TF; queued target edges were not validated.", "noncanonical stress/DNA-repair capacity only"),
    "srpk2": ("SRPK2", "https://www.ncbi.nlm.nih.gov/gene/?term=SRPK2%5BGene%20Name%5D%20AND%20Homo%20sapiens%5BOrganism%5D", "https://www.uniprot.org/uniprotkb/Q9H2W6/entry", "authoritative_identity_and_primary_literature", "human/mouse SRPK2 kinase and RNA-splicing models", "kinase, SR-protein phosphorylation, splicing and perturbation assays", "SRPK2 is a serine/arginine protein kinase that regulates RNA splicing, not a sequence-specific TF; ACSS2 is retained as an exact RNA-regulatory candidate.", "noncanonical kinase/RNA-processing capacity; exact ACSS2 RNA candidate"),
    "mrtfa": ("MRTFA/MKL1", "https://www.ncbi.nlm.nih.gov/gene/57591", "https://www.uniprot.org/uniprotkb/Q969V6/entry", "primary_literature_regulator_level", "human and mouse MRTF-A/SRF/coactivator models", "promoter ChIP, reporter, coactivator, knockdown and genetic perturbation assays", "MRTFA/MKL1 is a signal-regulated transcriptional coactivator that works mainly with SRF; several queued targets have direct coactivator evidence but are not standalone sequence-specific TF edges.", "noncanonical transcriptional-coactivator capacity; exact queued candidates routed separately"),
}

# These are exact regulator-target memberships on documented GTRD-derived
# promoter-profile pages. They provide a reproducible regulon lead, not effect
# direction, occupancy in the SCI target cell, or perturbation evidence.
PROFILE_TARGETS = {
    "znf830": {"jag1"},
    "mettl14": {"jund"},
    "srpk1": {"col6a3", "fzd6", "igf1r", "lamp1"},
    "ube2i": {"bdnf", "col6a1", "plxdc1", "vim"},
    "igf1r": {"igf1r"},
    "tert": {"ang", "jund", "plxdc1", "relb"},
    "syncrip": {"anxa2"},
}
PROFILE_URLS = {
    "znf830": "https://www.gsea-msigdb.org/gsea/msigdb/cards/ZNF830_TARGET_GENES.html",
    "mettl14": "https://www.gsea-msigdb.org/gsea/msigdb/cards/METTL14_TARGET_GENES.html",
    "srpk1": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/SRPK1_TARGET_GENES.html",
    "ube2i": "https://www.gsea-msigdb.org/gsea/msigdb/cards/UBE2I_TARGET_GENES.html",
    "igf1r": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/IGF1R_TARGET_GENES.html",
    "tert": "https://www.gsea-msigdb.org/gsea/msigdb/cards/TERT_TARGET_GENES.html",
    "syncrip": "https://www.gsea-msigdb.org/gsea/msigdb/cards/SYNCRIP_TARGET_GENES.html",
}
GTRD_CORR = "https://pubmed.ncbi.nlm.nih.gov/30445619/"

# Exact target-specific findings from primary studies. These are deliberately
# routed outside canonical sequence-specific TF evidence when the regulator is
# a kinase, RNA-processing factor, or transcriptional coactivator.
SPECIAL_EDGES = {
    ("ube2i", "vim", "human"): {
        "status": "functional_noncanonical_protein_ptm_candidate_not_tf",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5606578/",
        "corr": "https://www.uniprot.org/uniprotkb/P63279/entry",
        "cell": "human_HEK293T_with_HL60_and_rhesus_RF6A_Anaplasma_infection_models_not_SCI_target_cell",
        "binding": "Ubc9_knockdown_changed_vimentin_assembly_at_pathogen_vacuoles;_biochemical_vimentin_SUMOylation_was_not_confirmed",
        "downstream": "UBE2I_Ubc9_loss_reduced_vimentin_assembly_at_the_vacuole;_protein/PTM_phenotype_not_VIM_transcription",
        "disposition": "retain_noncanonical_protein_PTМ_cytoskeletal_candidate_pending_SCI_context",
        "exclusions": "This is infection-specific Ubc9-dependent vimentin assembly/protein evidence with an incompletely confirmed SUMOylation mechanism, not transcriptional regulation or Module 22B evidence.",
        "notes": "Exact human UBE2I-to-VIM protein/PTM evidence is routed to the noncanonical cytoskeletal/protein category.",
    },
    ("igf1r", "apob", "human"): {
        "status": "functional_noncanonical_kinase_lipid_transport_candidate_not_tf",
        "primary": "https://pubmed.ncbi.nlm.nih.gov/40171617/",
        "corr": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12236071/",
        "cell": "human_HUVEC_inducible_IGF1R_models_with_ApoE-null_mouse_in_vivo_context_not_SCI_target_cell",
        "binding": "kinase-dependent_APOB-positive_LDL_particle_trafficking_phenotype;_no_APOB_locus_occupancy_or_APOB_RNA_regulation",
        "downstream": "wild-type_IGF1R_changed_cholesterol-rich_LDL_uptake_and_ApoB-particle_association;_kinase-dead_K1003R_did_not_reproduce_effect",
        "disposition": "retain_noncanonical_Module24B_lipid_vascular_transport_candidate_pending_SCI_context",
        "exclusions": "ApoB was measured as a particle/trafficking phenotype, not APOB transcript or locus regulation; this is receptor-kinase biology, not a TF edge.",
        "notes": "Exact human IGF1R-to-ApoB/LDL transport evidence is routed to Module 24B-style lipid/vascular transport staging, not 20B or 22B.",
    },
    ("igf1r", "igf1r", "human"): {
        "status": "functional_noncanonical_receptor_autoregulation_candidate_not_tf",
        "primary": "https://pubmed.ncbi.nlm.nih.gov/22128190/",
        "corr": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3268434/",
        "cell": "human_C4.12.5_and_MCF7_breast-cancer_models_with_rat_IGF1R_promoter-reporter_caveat_not_SCI_target_cell",
        "binding": "full-length_IGF1R_binding_to_cognate_promoter_by_DNA-affinity_and_ChIP;_promoter-reporter_activation_in_receptor-overexpression_context",
        "downstream": "IGF1R_overexpression_increased_IGF1R_promoter-reporter_activity;_promoter_construct_species/fragment_caveat_remains",
        "disposition": "retain_noncanonical_receptor_autoregulation_candidate_pending_SCI_context",
        "exclusions": "This is noncanonical nuclear receptor autoregulation with a promoter-construct species caveat, not canonical sequence-specific TF evidence; no SCI-cell validation.",
        "notes": "Exact IGF1R self-promoter evidence is routed to noncanonical receptor autoregulation with a Module 22B overlay only.",
    },
    ("nfam1", "il2", "mouse"): {
        "status": "functional_noncanonical_receptor_relay_cytokine_candidate_not_tf",
        "primary": "https://pubmed.ncbi.nlm.nih.gov/15143214/",
        "corr": "https://pmc.ncbi.nlm.nih.gov/articles/PMC419568/",
        "cell": "mouse_43-1_T-cell_NFAM1_crosslinking_model_not_SCI_target_cell",
        "binding": "NFAM1_ITAM_crosslinking_activated_ZAP70_or_Syk_and_NFAT;_no_direct_Il2_locus_occupancy_by_NFAM1",
        "downstream": "NFAM1_crosslinking_induced_NFAT_activation_and_IL2_production;_ITAM_mutants_and_FK506_blocked_response",
        "disposition": "retain_noncanonical_Module21B_like_receptor_relay_candidate_pending_SCI_context",
        "exclusions": "This is an ITAM receptor-to-NFAT cytokine-output relay, not direct Nfam1 transcriptional regulation of Il2 or Module 20B ligand-binding evidence.",
        "notes": "Exact mouse Nfam1-to-Il2 receptor-relay evidence is routed to cytokine-output/relay staging.",
    },
    ("tert", "relb", "human"): {
        "status": "functional_noncanonical_rna_perturbation_candidate_not_tf",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3723976/",
        "corr": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4772727/",
        "cell": "human_MCF7_breast-cancer_TERT-siRNA_model_not_SCI_target_cell",
        "binding": "TERT_siRNA_qPCR_panel_association;_no_RELB_locus_occupancy_or_direct_TERT-DNA_binding",
        "downstream": "TERT_silencing_increased_RELB_RNA_in_MCF7;_single_panel_result_without_direct_rescue_or_independent_target_mechanism",
        "disposition": "retain_noncanonical_RNA_perturbation_candidate_pending_SCI_context",
        "exclusions": "The evidence is a limited TERT-knockdown RNA association and separate literature supports the reverse RelB-to-TERT direction; it is not direct TERT transcriptional activation of RELB.",
        "notes": "Human TERT-to-RELB RNA perturbation evidence is retained outside strict TF evidence with reverse-direction literature noted.",
    },
    ("tert", "ang", "human"): {
        "status": "reverse_direction_near_match_not_promotable",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12281399/",
        "corr": "https://www.gsea-msigdb.org/gsea/msigdb/cards/TERT_TARGET_GENES.html",
        "cell": "human_hematopoietic_stem_or_progenitor_context_not_SCI_target_cell",
        "binding": "ANG-induced_TERT_expression_or_telomerase_activity_is_reverse_direction;_no_TERT-to-ANG_binding",
        "downstream": "ANG_stimulation_increased_TERT_or_telomerase_readout;_does_not_support_TERT_regulation_of_ANG",
        "disposition": "retain_reverse_direction_near_match_separately",
        "exclusions": "The located functional relationship is ANG-to-TERT, not TERT-to-ANG; the profile membership does not repair the directionality gap.",
        "notes": "Reverse-direction ANG-to-TERT evidence was retained as an exclusion and not promoted.",
    },
    ("tert", "jund", "human"): {
        "status": "reverse_direction_near_match_not_promotable",
        "primary": "https://pubmed.ncbi.nlm.nih.gov/16135795/",
        "corr": "https://www.gsea-msigdb.org/gsea/msigdb/cards/TERT_TARGET_GENES.html",
        "cell": "human_hTERT-promoter_and_cancer-cell_models_not_SCI_target_cell",
        "binding": "JunD_or_c-Jun_binding_and_regulation_of_hTERT_promoter_is_reverse_direction;_no_TERT-to-JUND_mechanism",
        "downstream": "JunD_context_activated_or_repressed_hTERT_expression;_does_not_support_TERT_regulation_of_JUND",
        "disposition": "retain_reverse_direction_near_match_separately",
        "exclusions": "The located functional relationship is JunD-to-TERT, not TERT-to-JUND; GTRD profile membership does not establish the asserted direction.",
        "notes": "Reverse-direction JunD-to-TERT evidence was retained as an exclusion and not promoted.",
    },
    ("mettl14", "hmgb1", "human"): {
        "status": "cross_species_functional_rna_protein_near_match_not_promotable",
        "primary": "https://pubmed.ncbi.nlm.nih.gov/41247402/",
        "corr": "https://link.springer.com/article/10.1007/s00592-025-02623-y",
        "cell": "mouse_BV2_high-glucose_and_STZ_models_with_human_patient_expression_context_not_exact_human_SCI_target_cell",
        "binding": "RIP_and_expression_evidence_reported;_no_direct_human_METTL14_DNA-locus_or_site-specific_m6A_mechanism_established",
        "downstream": "METTL14_overexpression_reduced_HMGB1_and_NF-kB_signaling_in_mainly_murine_models;_human_samples_were_expression_context",
        "disposition": "retain_cross_species_indirect_RNA_inflammatory_near_match_separately",
        "exclusions": "The functional perturbation evidence is mainly murine and does not establish a direct human METTL14-to-HMGB1 m6A site or target-cell mechanism; HMGB1 module membership is not evidence for the regulator edge.",
        "notes": "Cross-species/partial METTL14-to-HMGB1 evidence is retained as an indirect RNA/inflammatory near-match without promotion.",
    },
    ("mettl14", "fgfr4", "human"): {
        "status": "functional_noncanonical_rna_regulation_candidate_not_tf",
        "primary": "https://www.nature.com/articles/s41467-022-30217-7",
        "corr": "https://pubmed.ncbi.nlm.nih.gov/35562334/",
        "cell": "human_rSKBR3_MDA-MB-361_and_related_HER2-positive_breast-cancer_models_not_SCI_target_cell",
        "binding": "METTL14-dependent_m6A_on_FGFR4_mRNA_supported_by_MeRIP_and_m6A-site_reporter_mutation;_no_DNA-locus_TF_binding",
        "downstream": "METTL14_reduction_or_knockdown_increased_FGFR4_mRNA_and_protein;_actinomycin-D_decay_and_rescue_assays_supported_mRNA_destabilization",
        "disposition": "retain_noncanonical_epitranscriptomic_RNA_candidate_pending_SCI_context",
        "exclusions": "This is direct RNA-level m6A/stability regulation, not METTL14 DNA binding or canonical promoter-TF evidence; models are HER2-positive breast cancer.",
        "notes": "Exact human METTL14-to-FGFR4 RNA-regulatory evidence is routed to epitranscriptomic and downstream-expression evidence.",
    },
    ("srpk1", "igf1r", "human"): {
        "status": "functional_noncanonical_kinase_protein_response_candidate_not_tf",
        "primary": "https://pubmed.ncbi.nlm.nih.gov/32994315/",
        "corr": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7710141/",
        "cell": "human_SPEC2_uterine_serous_carcinoma_cells_not_SCI_target_cell",
        "binding": "MIB-MS_kinome_and_protein-response_evidence;_no_IGF1R_locus_occupancy_or_direct_SRPK1_substrate_claim",
        "downstream": "SRPK1_inhibition_or_knockdown_increased_total_and_activating_phospho-IGF1R_or_INSR_and_downstream_AKT_signaling",
        "disposition": "retain_noncanonical_kinase_protein_response_candidate_pending_SCI_context",
        "exclusions": "This is a target-protein/signaling response after SRPK1 perturbation, not evidence of SRPK1 transcriptional regulation of IGF1R; a separate apparent paper was retracted and was not counted.",
        "notes": "Exact human SRPK1-to-IGF1R protein-level adaptive response is routed to kinase/signaling evidence outside canonical TF evidence.",
    },
    ("srpk2", "acss2", "human"): {
        "status": "functional_noncanonical_rna_regulation_candidate_not_tf",
        "primary": "https://pubmed.ncbi.nlm.nih.gov/29153836/",
        "corr": "https://www.nature.com/articles/s41416-019-0650-z",
        "cell": "human_and_mouse_mTORC1_S6K1_SRPK2_lipogenesis_models_not_SCI_target_cell",
        "binding": "no_ACSS2_locus_occupancy;_SRPK2_controls_SR-protein-dependent_splicing",
        "downstream": "SRPK2_inhibition_caused_ACSS2_intron_retention_and_nonsense-mediated_mRNA_decay_with_reduced_lipogenic_expression",
        "disposition": "retain_noncanonical_RNA_splicing_candidate_pending_SCI_context",
        "exclusions": "This is an indirect post-transcriptional RNA-splicing/stability relationship, not SRPK2 DNA binding or promoter-TF evidence.",
        "notes": "Exact SRPK2-to-ACSS2 RNA-regulatory evidence is routed to RNA-processing and downstream-expression evidence.",
    },
    ("mrtfa", "col1a1", "human"): {
        "status": "functional_noncanonical_coactivator_candidate_not_tf",
        "primary": "https://pubmed.ncbi.nlm.nih.gov/29807221/",
        "corr": "",
        "cell": "human_MCF7_breast_cancer_cells_not_SCI_target_cell",
        "binding": "MRTF-A_physically_interacted_with_COL1A1_promoter;_no_sequence-specific_MRTFA_DNA-binding_claim",
        "downstream": "MRTF-A_depletion_abrogated_TGF-beta_or_Wnt_induction_of_COL1A1;_histone_acetylation_and_RNA_Pol_II_recruitment_were_measured",
        "disposition": "retain_noncanonical_coactivator_candidate_pending_SCI_context",
        "exclusions": "MRTF-A is an SRF coactivator and the study is in MCF-7 breast-cancer cells; this is not evidence of a standalone sequence-specific TF motif or SCI-cell activity.",
        "notes": "Direct human MRTF-A/COL1A1 promoter and depletion evidence is routed to the transcriptional-coactivator category.",
    },
    ("mrtfa", "myl9", "human"): {
        "status": "functional_noncanonical_coactivator_candidate_not_tf",
        "primary": "https://academic.oup.com/abbs/article/45/11/921/1178",
        "corr": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5880600/",
        "cell": "human_MCF7_breast_cancer_cells_and_promoter-reporter_context_not_SCI_target_cell",
        "binding": "MRTF-A-responsive_CArG_element_in_MYL9_promoter_reporter;_coactivator/SRF_context",
        "downstream": "MRTF-A_overexpression_increased_MYL9_RNA_and_protein;_RNAi_reduced_MYL9;_CArG_mutation_reduced_promoter_response",
        "disposition": "retain_noncanonical_coactivator_candidate_pending_SCI_context",
        "exclusions": "The evidence is promoter-reporter and coactivator/SRF-context evidence rather than standalone MRTFA sequence-specific DNA binding; model is breast cancer, not SCI target cell.",
        "notes": "Two human breast-cancer studies support an MRTF-A-dependent MYL9 transcriptional response; it remains noncanonical and unmaterialized.",
    },
    ("mrtfa", "mmp9", "human"): {
        "status": "functional_noncanonical_coactivator_candidate_not_tf",
        "primary": "https://www.frontiersin.org/journals/molecular-biosciences/articles/10.3389/fmolb.2021.568868/full",
        "corr": "https://pubmed.ncbi.nlm.nih.gov/33722605/",
        "cell": "human_BGC823_gastric_cancer_cells_not_SCI_target_cell",
        "binding": "EGF-induced_MRTF-A_enrichment_at_MMP9_promoter_by_ChIP;_no_standalone_sequence-specific_TF_binding_claim",
        "downstream": "MRTF-A_siRNA_reduced_MMP9_RNA_and_protein_and_MICAL2_or_EGF_signaling_induced_the_response",
        "disposition": "retain_noncanonical_coactivator_candidate_pending_SCI_context",
        "exclusions": "MRTF-A is a coactivator in an EGF/MICAL2 signaling context and the study uses gastric-cancer cells; it is not canonical standalone TF evidence.",
        "notes": "Direct human promoter-occupancy plus perturbation evidence is routed to coactivator and downstream-expression evidence.",
    },
    ("mrtfa", "id3", "mouse"): {
        "status": "functional_noncanonical_coactivator_candidate_not_tf",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3258938/",
        "corr": "",
        "cell": "mouse_C2C12_myoblast_myogenic_differentiation_model_not_SCI_target_cell",
        "binding": "MRTF-A_Smad-dependent_Id3_transcriptional_control_in_RhoA_ROCK_context;_not_standalone_MRTFA_DNA-binding",
        "downstream": "RhoA_ROCK_signaling_and_MRTF-A_Smad1_4_controlled_Id3_transcription_during_myogenic_differentiation",
        "disposition": "retain_noncanonical_coactivator_candidate_pending_SCI_context",
        "exclusions": "The mechanism is a cooperative MRTF-A/Smad/FKHR transcriptional context in mouse myoblasts, not a standalone sequence-specific TF edge or SCI-cell result.",
        "notes": "Exact mouse Mrtfa-to-Id3 transcriptional evidence is routed to the coactivator/signaling-relay category.",
    },
    ("mrtfa", "tagln", "mouse"): {
        "status": "binding_and_cofactor_dependence_near_match_not_promotable",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8831594/",
        "corr": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3801009/",
        "cell": "mouse_NIH3T3_and_dermal_fibroblast_MRTF-A_SRF_models_not_SCI_target_cell",
        "binding": "MRTF-A_and_SRF_ChIP-seq_context_at_serum-responsive_genes_including_classical_Tagln_target_program",
        "downstream": "Tagln_expression_changed_after_Lap2alpha_cofactor_depletion;_MRTF-A_itself_was_not_perturbed_in_the_queued_pair_assay",
        "disposition": "retain_binding_and_cofactor_dependence_near_match_separately",
        "exclusions": "The cited experiment establishes an MRTF-A/SRF target context and cofactor dependence, but does not isolate Mrtfa perturbation for this exact Tagln edge.",
        "notes": "Mouse Mrtfa/Tagln evidence is retained as binding/cofactor context without overstating causality.",
    },
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
    if key not in REGULATORS:
        raise SystemExit(f"missing evidence map for {key}")
    symbol, general_primary, general_corr, kind, model, assay, observation, relevance = REGULATORS[key]
    profile = key in PROFILE_TARGETS and target in PROFILE_TARGETS[key]
    special = SPECIAL_EDGES.get((key, target, row["species_scope"]))
    if special:
        status = special["status"]
        primary = special["primary"]
        corr = special["corr"]
        cell = special["cell"]
        binding = special["binding"]
        downstream = special["downstream"]
        disposition = special["disposition"]
        exclusions = special["exclusions"]
        notes = special["notes"]
    elif key == "za":
        status = "identity_unresolved_not_promotable"
        primary = general_primary
        corr = general_corr
        cell = "regulator_identity_not_resolved"
        binding = "no_target_binding_or_association_assigned"
        downstream = "not_assessed"
        disposition = "retain_identity_review_hold_without_target_evidence"
        exclusions = "The raw symbol ZA is unresolved; no approved-gene or target-specific evidence was assigned."
        notes = "Identity uncertainty prevents evidence transfer to the queued pairs."
    elif profile:
        status = "gtrd_promoter_profile_membership_only_not_promotable"
        primary = PROFILE_URLS[key]
        corr = GTRD_CORR
        cell = "profile_source_context_not_SCI_target_cell"
        binding = "GTRD_promoter_profile_membership_only_no_pairwise_locus_validation"
        downstream = "profile_membership_without_effect_direction_or_perturbation"
        disposition = "retain_profile_traceable_candidate_without_promotion"
        exclusions = "The MSigDB/GTRD profile is a database-derived promoter-target membership and does not establish occupancy, direction, target-cell presence or causal perturbation for this exact pair."
        notes = "Exact profile membership was retained as a reproducible regulon lead; it is not a strict TF promotion."
    else:
        status = "database_membership_only_not_promotable"
        primary = TF_LINK_URL
        corr = ""
        cell = "not_established_for_exact_pair"
        binding = "TFLink_membership_only_no_queued_locus_validation"
        downstream = "not_found_for_exact_pair"
        disposition = "retain_provenance_traceable_candidate_without_promotion"
        exclusions = "TFLink membership and regulator-level annotations are search leads; broad regulator evidence, orthologs, paralogs, reverse directions, general assay availability and complex-level findings were not transferred to this exact pair."
        notes = "No exact target-specific causal edge was established; target-cell presence, downstream activation and upstream relay are not inferred."
    return {
        "symbol": symbol, "general_primary": general_primary, "general_corr": general_corr,
        "kind": kind, "model": model, "assay": assay, "observation": observation, "relevance": relevance,
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
    species_by_key: dict[str, set[str]] = {}
    status_counts: dict[str, int] = {}
    for row in rows:
        info = classify(row)
        key = row["regulator_key"]
        species_by_key.setdefault(key, set()).add(row["species_scope"])
        status_counts[info["status"]] = status_counts.get(info["status"], 0) + 1
        pairs.append({
            "review_id": f"public_tf_evidence_batch031_pair_{int(row['batch_rank']):02d}_{row['target_rank']}",
            "batch_id": row["batch_id"], "batch_rank": row["batch_rank"],
            "regulator_key": key, "regulator_symbol": info["symbol"],
            "species_scope": row["species_scope"], "source_registry": row["source_registry"],
            "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"],
            "target_symbol": row["target_symbol"], "target_graph_modules": row["target_graph_modules"],
            "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": search_url(row["raw_tf_symbol"], row["target_symbol"], row["species_scope"]),
            "exact_pair_status": info["status"],
            "regulator_general_evidence_status": "identity_unresolved" if key == "za" else "supported_general_or_authoritative_regulator_evidence",
            "target_cell_presence_status": info["cell"],
            "binding_or_association_status": info["binding"],
            "downstream_expression_or_perturbation_status": info["downstream"],
            "downstream_activation_status": "not_established_for_SCI_target_cell",
            "upstream_relay_status": "not_tested_for_exact_pair",
            "disposition": info["disposition"], "primary_citation": info["primary"],
            "corroborating_citation": info["corr"], "near_match_exclusions": info["exclusions"],
            "review_notes": info["notes"] + " " + info["observation"],
            "exportable": "false", "canonical_write_performed": "false",
        })
        if key not in seen:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch031_regulator_{key}",
                "regulator_key": key, "regulator_symbol": info["symbol"],
                "species_scope": row["species_scope"],
                "evidence_layer": "regulator_identity_and_regulatory_capacity",
                "support_kind": info["kind"], "cell_or_model": info["model"],
                "assay_or_perturbation": info["assay"], "observation": info["observation"],
                "effect_direction": "queued-pair direction not established except profile membership without direction",
                "primary_citation": info["general_primary"], "corroborating_citation": info["general_corr"],
                "route_or_module_relevance": info["relevance"],
                "target_pair_scope": "profile membership, where explicitly marked, is not evidence for unrelated queued pairs; no upstream relay inferred",
                "exportable": "false", "canonical_write_performed": "false",
                "limitations": "Regulator-level identity/capacity and GTRD profile membership do not establish SCI target-cell presence, exact queued-target direction, downstream activation or upstream relay. Ligand, protein, RNA, chromatin, machinery and profile evidence remains separate from canonical promoter-TF evidence.",
            })
            seen.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch031_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch031_regulator_register.tsv"
    summary_path = args.output_dir / "batch_031_evidence_review_summary.json"
    report_path = args.output_dir / "EVIDENCE_REVIEW_BATCH031.md"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    pair_keys = {(x["regulator_key"], x["target_symbol"], x["species_scope"], x["source_record_id"]) for x in pairs}
    noncanonical = sum(v for k, v in status_counts.items() if k.startswith("functional_noncanonical_"))
    profile_rows = status_counts.get("gtrd_promoter_profile_membership_only_not_promotable", 0)
    unresolved_rows = status_counts.get("identity_unresolved_not_promotable", 0)
    database_rows = status_counts.get("database_membership_only_not_promotable", 0)
    near_match_rows = len(pairs) - noncanonical - profile_rows - unresolved_rows - database_rows
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_031",
        "source_set_ranks_reviewed": list(range(1, 26)), "pair_rows_reviewed": len(pairs),
        "unique_regulators_reviewed": len(seen), "unique_provenance_aware_pairs": len(pair_keys),
        "exact_pair_status_counts": status_counts, "regulator_register_rows": len(evidence),
        "strict_tf_promotion_candidate_rows": 0, "noncanonical_exact_candidate_rows": noncanonical,
        "profile_only_rows": profile_rows, "identity_review_hold_rows": unresolved_rows,
        "database_only_rows": database_rows, "partial_or_near_match_rows": near_match_rows, "exportable_pair_rows": 0,
        "canonical_writes_performed": False, "module22b_promotions_performed": False,
        "provenance_preserved": True,
        "limitations": [
            "TFLink membership is a search lead, not causal regulation.",
            "The documented MSigDB/GTRD profile memberships are retained as regulon leads without effect direction or SCI-cell validation.",
            "METTL14-to-FGFR4, SRPK1-to-IGF1R, UBE2I-to-VIM, IGF1R-to-APOB/IGF1R, NFAM1-to-Il2, and TERT-to-RELB queued findings are routed to noncanonical RNA, protein-response, receptor-relay or lipid-transport evidence; none is a canonical standalone TF edge.",
            "ZA remains an unresolved raw symbol and no target evidence was assigned.",
            "Exact-pair negatives are bounded-search results, not global absence.",
            "No canonical or Module 22B write was performed.",
        ],
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path.write_text("\n".join([
        "# Evidence review: public TF batch 031", "",
        f"Reviewed {len(pairs)} literal exact regulator-target-species pairs across 25 TFLink source-set ranks.", "",
        f"- **{len(pairs)}** pairs were reviewed across **{len(seen)}** regulators.",
        f"- **{noncanonical}** exact functional noncanonical candidate rows were staged: METTL14-to-FGFR4, SRPK1-to-IGF1R, UBE2I-to-VIM, IGF1R-to-APOB/IGF1R, NFAM1-to-Il2, and TERT-to-RELB.",
        f"- **{profile_rows}** exact GTRD-derived promoter-profile memberships were staged as nonpromotable regulon leads.",
        f"- **{unresolved_rows}** rows remain an identity-review hold for raw symbol ZA.",
        f"- **{database_rows}** rows remain database-membership or bounded-search leads without target-specific evidence; **{near_match_rows}** are partial or near-match findings.",
        "- **0** strict TF, noncanonical functional, exportable, canonical or Module 22B writes were performed.", "",
        "All rows retain the original TFLink source record, raw symbol, species, target, graph-module mapping and local source snapshot. Profile memberships cite the corresponding MSigDB/GTRD set page and are not treated as occupancy, effect direction or perturbation evidence.", "",
    ]) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
