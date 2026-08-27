#!/usr/bin/env python3
"""Stage conservative evidence findings for all Batch 027 pairs."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/"
    "candidate_triage_v1/evidence_batches/batch_027/"
    "public_tf_evidence_collection_batch_027.tsv"
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
# route/module relevance, profile URL.
REGULATORS = {
    "dpep3": ("DPEP3", "https://www.ncbi.nlm.nih.gov/gene/71854", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6283293/", "authoritative_annotation_and_primary_literature", "mouse testis/TEX101 protein-complex models", "membrane dipeptidase, protein-complex and knockout assays", "DPEP3 is a membrane-bound dipeptidase/testis-associated protein; no DNA-locus or queued target mechanism was found.", "not a transcriptional-regulator mechanism", ""),
    "esco2": ("ESCO2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4568707/", "https://www.ncbi.nlm.nih.gov/gene/157570", "primary_literature_regulator_level", "human REST/cohesin chromatin models", "ChIP-seq and depletion-associated chromatin/expression assays", "ESCO2 is a cohesin acetyltransferase and noncanonical chromatin regulator; queued ADAM22 evidence belongs to SRC-1/MYB, not ESCO2.", "noncanonical cohesin/chromatin capacity only", ""),
    "rngtt": ("RNGTT", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11139899/", "https://www.ncbi.nlm.nih.gov/gene/8732", "authoritative_annotation_and_primary_literature", "human RNA-polymerase-II/RNA-capping models", "cryo-EM, Pol II association and RNA-capping assays", "RNGTT is a cotranscriptional mRNA-capping enzyme recruited to Pol II/nascent RNA, not a DNA-locus TF; no queued target was validated.", "noncanonical RNA-processing capacity only", ""),
    "amh": ("AMH", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7286617/", "https://academic.oup.com/mend/article/15/6/936/2526375", "primary_literature_regulator_level", "human AMH receptor-signaling models", "AMH/AMHR2/ACVR1 receptor assays and BRE-luciferase", "AMH is a secreted TGF-beta-family ligand; ACVR1 is a type-I receptor component in AMH signaling, not a transcriptional target.", "ligand-to-receptor signaling capacity; route to receptor evidence, not TF evidence", ""),
    "mbtps2": ("MBTPS2/S2P", "https://www.ncbi.nlm.nih.gov/gene/51360", "https://www.uniprot.org/uniprotkb/O43462/entry", "authoritative_annotation_and_primary_literature", "human intramembrane-protease models", "regulated intramembrane proteolysis and SREBP/ATF6 assays", "MBTPS2 is an intramembrane protease that activates membrane-tethered TFs indirectly; no queued target mechanism was found.", "noncanonical protease/signaling capacity only", ""),
    "aurkb": ("AURKB", "https://www.ncbi.nlm.nih.gov/gene/20877", "https://www.uniprot.org/uniprotkb/Q96GD4/entry", "authoritative_annotation_and_primary_literature", "human and mouse chromosomal-passenger-complex models", "kinase, mitosis and chromosome-segregation assays", "AURKB is a mitotic serine/threonine kinase/chromosomal-passenger component, not a sequence-specific TF; no queued target mechanism was found.", "not a transcriptional-regulator mechanism", ""),
    "hmgb1": ("HMGB1", "https://www.ncbi.nlm.nih.gov/gene/3146", "https://www.uniprot.org/uniprotkb/P09429/entry", "primary_literature_regulator_level", "human chromatin/alarmin and macrophage models", "DNA/chromatin binding, HMGB1 stimulation and inflammatory assays", "HMGB1 is a chromatin-associated DNA-binding protein and extracellular alarmin; the queued ACVR1 result is receptor responsiveness to HMGB1, not HMGB1 regulation of ACVR1.", "noncanonical chromatin/alarmin signaling capacity only", ""),
    "fxr2": ("FXR2", "https://www.nature.com/articles/s41586-020-2077-3", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8693918", "primary_literature_regulator_level", "human K562 RNA-binding models", "eCLIP and transcript-level RNA-binding assays", "FXR2 is an RNA-binding protein; ABCA1 transcript association is binding-only and does not establish DNA-locus regulation or direction.", "noncanonical RNA-binding capacity only", ""),
    "mier2": ("MIER2", "https://pubmed.ncbi.nlm.nih.gov/28046085/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9903721/", "primary_literature_regulator_level", "human HDAC/REST-associated chromatin models", "HDAC1/2 recruitment, RE1 occupancy and perturbation assays", "MIER2 is an HDAC-associated transcriptional corepressor with nonqueued RE1 evidence; no queued target edge was validated.", "noncanonical transcriptional-corepressor capacity only", ""),
    "rai1": ("RAI1", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5098476/", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE81204", "primary_literature_regulator_level", "mouse cortex chromatin/TSS models", "ChIP-seq, promoter/enhancer occupancy and perturbation assays", "RAI1 is a chromatin-associated TF with nonqueued target evidence; none of the queued loci had pair-specific direction.", "canonical TF identity supported generally; queued edges remain unsupported", ""),
    "mettl3": ("METTL3", "https://pmc.ncbi.nlm.nih.gov/articles/PMC13386607/", "https://www.ncbi.nlm.nih.gov/gene/56339", "primary_literature_regulator_level", "human pancreatic-cancer m6A models", "MeRIP-qPCR, mRNA-stability chase, METTL3 perturbation and rescue", "METTL3 is an m6A RNA methyltransferase; ADAM10 m6A, stability, mRNA/protein and downstream phenotypes changed with METTL3 perturbation.", "exact noncanonical RNA-regulator candidate; route ADAM10 transcript/protein evidence separately from TF evidence", ""),
    "htatsf1": ("HTATSF1", "https://www.sciencedirect.com/science/article/pii/S1934590918301085", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE96593", "primary_literature_regulator_level", "mouse RNA-processing/ChIP-seq models", "ChIP-seq, RNA-processing and perturbation assays", "HTATSF1 is an RNA-binding/splicing-associated factor; queued rows have profile-level ChIP evidence but no target-specific direction.", "noncanonical RNA/transcriptional-machinery capacity only", ""),
    "dux": ("DUX", "https://pubmed.ncbi.nlm.nih.gov/28459456/", "https://www.ncbi.nlm.nih.gov/bioproject/PRJNA369387", "primary_literature_regulator_level", "mouse zygotic-genome-activation models", "ChIP-seq/RNA-seq and embryonic perturbation assays", "DUX is a double-homeobox DNA-binding TF with direct ZGA-target evidence, but none of the queued loci had target-specific validation.", "canonical TF identity supported generally; queued edges remain profile-only", ""),
    "tbxt": ("TBXT/Brachyury", "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0033346", "https://www.ncbi.nlm.nih.gov/gene/20997", "primary_literature_regulator_level", "mouse embryonic T-box TF models", "ChIP-chip, binding and perturbation assays", "TBXT is a sequence-specific T-box TF with validated nonqueued targets; queued Adgr rows remain profile-only and Adam17 has an Adam19 paralog near-match.", "canonical TF identity supported generally; queued edges remain unvalidated", ""),
    "insr": ("INSR", "https://pubchem.ncbi.nlm.nih.gov/gene/INSR/human", "https://pubmed.ncbi.nlm.nih.gov/36018759/", "authoritative_annotation_and_primary_literature", "human insulin-receptor signaling models", "receptor tyrosine-kinase and ectodomain-shedding assays", "INSR is a receptor tyrosine kinase, not a DNA-binding TF; ADAM17 cleaves INSR in the reverse direction.", "receptor signaling capacity only; reverse ADAM17-to-INSR evidence kept separate", ""),
    "tox": ("TOX", "https://pubmed.ncbi.nlm.nih.gov/31207604/", "https://pubmed.ncbi.nlm.nih.gov/33579927/", "primary_literature_regulator_level", "mouse T-cell chromatin models", "HMG-box TF occupancy, chromatin remodeling and perturbation", "TOX is a bona fide DNA-binding HMG-box regulator with nonqueued Tcf7 and T-cell-state evidence; queued target loci were not validated.", "canonical TF identity supported generally; queued edges remain unsupported", ""),
    "capg": ("CAPG", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6815964/", "https://www.uniprot.org/uniprotkb/P24452/entry", "primary_literature_regulator_level", "human nuclear actin/transcription models", "ChIP/EMSA and perturbation assays", "CAPG has noncanonical nuclear transcriptional activity at PIK3R1/P50; queued mouse ADAM22 is only a human expression-signature near-match.", "noncanonical nuclear/protein-regulator capacity only", ""),
    "phrf1": ("PHRF1", "https://pubmed.ncbi.nlm.nih.gov/32730336/", "https://www.sciencedirect.com/science/article/pii/S2211124713003562", "primary_literature_regulator_level", "mouse/human chromatin and TGF-beta models", "E3/protein-regulator, reporter and Smad-pathway assays", "PHRF1 is a chromatin-associated E3/protein regulator with nonqueued TGIF/ZEB1 evidence; queued ACVR1 is only a pathway near-match.", "noncanonical chromatin/protein-regulator capacity only", ""),
    "asf1a": ("ASF1A", "https://www.uniprot.org/uniprotkb/Q9Y294/entry", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2933817/", "primary_literature_regulator_level", "human histone-chaperone/HIRA models", "histone H3/H4 chaperoning, HIRA/CAF-1 complex and structural assays", "ASF1A is a histone chaperone rather than a validated sequence-specific regulator of the queued loci.", "noncanonical chromatin-assembly capacity only", ""),
    "mier1": ("MIER1", "https://www.encodeproject.org/experiments/ENCSR426MDV/", "https://pubmed.ncbi.nlm.nih.gov/36934083/", "primary_literature_regulator_level", "human K562 and mouse liver corepressor models", "ChIP-seq, GTRD profile and perturbation assays", "MIER1 is a noncanonical transcriptional corepressor; ADCYAP1 is a profile-only lead and the other queued targets were not supported.", "noncanonical transcriptional-corepressor capacity only", "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/MIER1_TARGET_GENES.html"),
    "stra8": ("STRA8", "https://pubmed.ncbi.nlm.nih.gov/30810530/", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE115928", "primary_literature_regulator_level", "mouse preleptotene meiotic-initiation models", "FLAG-STRA8 ChIP-seq and matched perturbation/RNA-seq", "STRA8 is supported as a strict TF generally; ADAM10 is only a ChIP-Atlas/profile lead without target-specific direction.", "canonical TF identity supported generally; queued ADAM10 remains profile-only", ""),
    "tsc22d4": ("TSC22D4", "https://www.ncbi.nlm.nih.gov/gene/81628", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3569644/", "primary_literature_regulator_level", "human and mouse hepatic transcriptional-regulator models", "leucine-zipper repression and hepatic perturbation assays", "TSC22D4 is a noncanonical transcriptional regulator with broad hepatic effects; no queued target locus/direction was validated.", "noncanonical transcriptional-regulator capacity only", ""),
    "cpsf3": ("CPSF3/CPSF-73", "https://www.ncbi.nlm.nih.gov/gene/51692", "https://www.nature.com/articles/nature05363", "authoritative_annotation_and_primary_literature", "human RNA 3-prime-end-processing models", "RNA-processing biochemistry and inhibitor assays", "CPSF3 is an RNA 3-prime-end-processing endonuclease, not a DNA-binding regulator of the queued genes.", "noncanonical RNA-processing capacity only", ""),
    "prdm11": ("PRDM11", "https://pubmed.ncbi.nlm.nih.gov/25499759/", "https://www.ncbi.nlm.nih.gov/gene/56981", "primary_literature_regulator_level", "human DLBCL chromatin/TF models", "genome-wide binding, transcriptome perturbation and chromatin assays", "PRDM11 has strict-TF-like genome-wide binding and nonqueued FOS/JUN evidence; no queued exact target edge was validated.", "canonical TF-like identity supported generally; queued edges remain unsupported", ""),
    "gtf3c2": ("GTF3C2/TFIIIC", "https://pubmed.ncbi.nlm.nih.gov/32115405/", "https://www.encodeproject.org/experiments/ENCSR000DOD/", "primary_literature_regulator_level", "human TFIIIC/Pol III transcription models", "TFIIIC occupancy, Pol III transcription and ENCODE ChIP-seq", "GTF3C2 is a TFIIIC/Pol III complex subunit; established targets are stable RNAs and queued mRNA loci are unsupported.", "noncanonical transcriptional-machinery capacity only", ""),
}

PROFILE_TARGETS = {
    "wiz": set(), "smyd5": {"eapp"}, "cbx1": {"abcc9", "gm21083", "gm7324"},
    "atad2": {"9930022d16rik", "ecel1", "haus5", "kcna6"}, "suv39h1": {"aw822073", "itln1"},
    "kdm4d": {"a930009a15rik"}, "cul4a": {"ackr1", "ackr2", "acvrl1"},
    "zfp217": {"a2m", "ackr3", "actr2", "acvr1"}, "wdr43": {"a2m", "acvr1", "acvr1c", "adam10"},
    "tbxt": {"adgrb3", "adgre5", "adgrl2"}, "htatsf1": {"actr2", "ada", "adam10", "adgrb1"},
    "dux": {"acvr1", "adam22", "adgrl1", "adgrl2"}, "phf19": {"abca1", "adam12", "adgrb1", "adgrb3"},
    "ptbp1": {"acvr1", "acvrl1", "adam17", "adcyap1"}, "gtf3c2": set(),
    "fbxl19": {"acvr1c", "adam22", "adam23", "adam9"}, "mier1": {"adcyap1"},
    "stra8": {"adam10"},
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


def profile_status(row: dict[str, str], info: tuple[str, ...]) -> dict[str, str]:
    _symbol, primary, corr, _kind, _model, _assay, _obs, _rel, profile = info
    return {
        "status": "binding_profile_only_not_promotable", "primary": profile or TF_LINK_URL,
        "corr": corr if profile else "", "cell": f"{row['species_scope']}_GTRD_or_ChIP_profile_not_SCI_target_cell",
        "binding": f"{row['species_scope']}_regulator_profile_membership_without_queued_locus_validation",
        "downstream": "no_target_specific_perturbation_or_direction_found",
        "disposition": "retain_binding_profile_lead_separately",
        "exclusions": "Regulator-wide/profile membership is a search lead; it does not establish target-cell presence, causal direction, downstream activation or an upstream relay.",
        "notes": "Exact species-matched regulator profile evidence is retained as a binding lead only.",
    }


def classify(row: dict[str, str]) -> dict[str, str]:
    key = row["regulator_key"]
    target = row["target_symbol"].lower()
    info = REGULATORS[key]
    symbol, general_primary, general_corr, kind, model, assay, observation, relevance, _profile = info
    out = {
        "symbol": symbol, "general_primary": general_primary, "general_corr": general_corr,
        "kind": kind, "model": model, "assay": assay, "observation": observation, "relevance": relevance,
        "status": "database_membership_only_not_promotable", "primary": TF_LINK_URL, "corr": "",
        "cell": "not_established_for_exact_pair", "binding": "TFLink_membership_only_no_queued_locus_validation",
        "downstream": "not_found_for_exact_pair", "disposition": "retain_provenance_traceable_candidate_without_promotion",
        "exclusions": "TFLink/database membership is a search lead; broad regulator evidence, orthologs, paralogs, reverse directions and complex-level findings were not transferred to this exact pair.",
        "notes": "No exact target-specific causal edge was established; target-cell presence, downstream activation and upstream relay are not inferred.",
    }
    if key == "wiz":
        # WIZ is not present in this batch; retained for defensive map completeness.
        pass
    if key == "mettl3" and row["species_scope"] == "human" and target == "adam10":
        out.update(status="functional_noncanonical_rna_regulator_candidate_not_strict_tf", primary="https://pmc.ncbi.nlm.nih.gov/articles/PMC13386607/", cell="human_PANC1_and_MIA_PaCa2_pancreatic_models_not_SCI_target_cell", binding="METTL3_dependent_m6A_mapped_to_ADAM10_mRNA_not_DNA_locus", downstream="METTL3_overexpression_increased_ADAM10_m6A_stability_mRNA_and_protein;_knockdown_decreased_them;_ADAM10_rescue_supported_phenotype", disposition="retain_noncanonical_rna_candidate_pending_SCI_context", exclusions="This is exact mRNA modification/stability evidence, not DNA-locus occupancy or a sequence-specific TF mechanism.", notes="Exact human METTL3-to-ADAM10 post-transcriptional evidence is staged in the noncanonical RNA-regulator category.")
    elif key == "amh" and row["species_scope"] == "human" and target == "acvr1":
        out.update(status="ligand_receptor_signaling_not_transcriptional", primary="https://pmc.ncbi.nlm.nih.gov/articles/PMC7286617/", corr="https://academic.oup.com/mend/article/15/6/936/2526375", cell="human_HEK293T_AMH_receptor_assay_not_SCI_target_cell", binding="AMH_binds_AMHR2_and_uses_ACVR1_type_I_receptor_component;_no_gene_locus_occupancy", downstream="AMH_AMHR2_ACVR1_signaling_activated_BRE_luciferase_without_ACVR1_mRNA_direction", disposition="retain_ligand_receptor_evidence_separately", exclusions="This is ligand-to-receptor pathway evidence, not AMH regulation of the ACVR1 gene.", notes="Exact human AMH-to-ACVR1 receptor signaling is routed to the ligand/receptor category, not TF evidence.")
    elif key == "mbtps2" and row["species_scope"] == "human" and target == "adipor1":
        out.update(status="treatment_expression_cooccurrence_not_promotable", primary="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE24188", corr="https://pubmed.ncbi.nlm.nih.gov/21869732/", cell="human_hepatocyte_treatment_expression_model_not_SCI_target_cell", binding="no_MBTPS2_ADIPOR1_locus_or_protein_mechanism", downstream="ADIPOR1_and_MBTPS2_cooccurred_in_treatment_expression_Venn_without_MBTPS2_perturbation", disposition="retain_expression_cooccurrence_separately", exclusions="The perturbation was statin/rifampicin treatment rather than MBTPS2 manipulation; co-occurrence is not a causal edge.", notes="Expression co-occurrence is kept separate from MBTPS2 protease and TF evidence.")
    elif key == "fxr2" and row["species_scope"] == "human" and target == "abca1":
        out.update(status="direct_rna_binding_only_not_transcriptional", primary="https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8693918", corr="https://www.nature.com/articles/s41586-020-2077-3", cell="human_K562_eCLIP_model_not_SCI_target_cell", binding="FXR2_eCLIP_association_with_ABCA1_transcript_not_genomic_locus", downstream="no_FXR2_specific_ABCA1_perturbation_direction_found", disposition="retain_rna_binding_evidence_separately", exclusions="Transcript-level eCLIP association does not establish DNA-locus regulation or target expression direction.", notes="Exact human FXR2-to-ABCA1 RNA binding is routed to RNA-regulator evidence, not TF evidence.")
    elif key == "hmgb1" and row["species_scope"] == "human" and target == "acvr1":
        out.update(status="ligand_response_near_match_not_promotable", primary="https://pmc.ncbi.nlm.nih.gov/articles/PMC8803261/", cell="human_iPSC_derived_macrophage_model_not_SCI_target_cell", binding="no_HMGB1_ACVR1_locus_occupancy;_ACVR1_genotype_changed_HMGB1_response", downstream="HMGB1_stimulation_induced_inflammation_and_ACVR1_R206H_enhanced_responsiveness", disposition="retain_ligand_response_near_match_separately", exclusions="The experiment tests cellular response to HMGB1 and ACVR1 genotype, not HMGB1 regulation of ACVR1 expression or protein.", notes="HMGB1/ACVR1 receptor-response evidence is not transferred to a regulator-target edge.")
    elif key == "magi1" and row["species_scope"] == "mouse" and target == "abca1":
        out.update(status="cross_species_protein_interaction_near_match_not_promotable", primary="https://pubmed.ncbi.nlm.nih.gov/9395497/", cell="human_PPI_record_not_mouse_SCI_target_cell", binding="human_MAGI1_ABCA1_PPI_without_mouse_locus_evidence", downstream="no_perturbation_or_direction_found", disposition="retain_cross_species_protein_near_match_separately", exclusions="A human MAGI1-ABCA1 protein-interaction record does not establish mouse Magi1 regulation of Abca1 or transcriptional direction.", notes="Cross-species PPI near-match only.")
    elif key == "capg" and row["species_scope"] == "mouse" and target == "adam22":
        out.update(status="cross_species_expression_association_near_match_not_promotable", primary="https://pubmed.ncbi.nlm.nih.gov/34166375/", cell="human_PCNSL_expression_signature_not_mouse_SCI_target_cell", binding="no_mouse_CAPG_ADAM22_locus_evidence", downstream="CAPG_and_ADAM22_co_listed_in_human_expression_signature_without_CAPG_perturbation", disposition="retain_cross_species_association_separately", exclusions="A human transcriptomic co-signature does not establish mouse CAPG occupancy or causal ADAM22 regulation.", notes="Cross-species expression association is not transferred.")
    elif key == "phrf1" and row["species_scope"] == "mouse" and target == "acvr1":
        out.update(status="pathway_near_match_not_promotable", primary="https://pubmed.ncbi.nlm.nih.gov/32730336/", cell="mouse_or_human_TGF_beta_models_not_SCI_target_cell", binding="no_PHRF1_ACVR1_locus_occupancy", downstream="PHRF1_TGF_beta_Smad_pathway_evidence_without_ACVR1_specific_direction", disposition="retain_pathway_near_match_separately", exclusions="General TGF-beta/Smad pathway assays do not establish PHRF1 regulation of the ACVR1 gene.", notes="Pathway-level PHRF1 evidence is kept separate from exact ACVR1 regulation.")
    elif key == "insr" and row["species_scope"] == "human" and target == "adam17":
        out.update(status="reverse_direction_near_match_not_promotable", primary="https://pubmed.ncbi.nlm.nih.gov/36018759/", cell="human_receptor_shedding_model_not_SCI_target_cell", binding="ADAM17_cleaves_INSR_not_INSR_to_ADAM17_occupancy", downstream="ADAM17_shedding_reduced_extracellular_INSR_in_reverse_direction", disposition="retain_reverse_direction_evidence_separately", exclusions="The paper supports ADAM17 upstream of INSR protein, not INSR regulation of ADAM17.", notes="Reverse receptor-shedding evidence was explicitly excluded.")
    elif key == "tbxt" and row["species_scope"] == "mouse" and target == "adam17":
        out.update(status="paralog_near_match_not_promotable", primary="https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0033346", cell="mouse_embryonic_Tbxt_model_not_SCI_target_cell", binding="Tbxt_genomic_target_evidence_at_Adam19_not_Adam17", downstream="no_Adam17_specific_direction_found", disposition="retain_paralog_near_match_separately", exclusions="The reported Brachyury near-match involves Adam19, not the queued Adam17 paralog.", notes="Adam19 evidence was not transferred to Tbxt-to-Adam17.")
    elif key == "usp7" and row["species_scope"] == "mouse" and target == "rbbp4":
        out.update(status="complex_level_near_match_not_promotable", primary="https://pubmed.ncbi.nlm.nih.gov/37196079/", cell="mouse_ESC_model_not_SCI_target_cell", binding="USP7_Polycomb_or_chromatin_complex_without_Rbbp4_locus_validation", downstream="no_Rbbp4_specific_direction_found", disposition="retain_complex_level_near_match_separately", exclusions="USP7/RBBP4 chromatin context does not establish target-specific occupancy and direction.", notes="Complex-level near-match only.")
    elif key in PROFILE_TARGETS and target in PROFILE_TARGETS[key]:
        out.update(profile_status(row, info))
    return out


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
            "review_id": f"public_tf_evidence_batch027_pair_{int(row['batch_rank']):02d}_{row['target_rank']}",
            "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key,
            "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "source_registry": row["source_registry"],
            "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"],
            "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": search_url(row["raw_tf_symbol"], row["target_symbol"], row["species_scope"]),
            "exact_pair_status": info["status"], "regulator_general_evidence_status": "supported_general_or_authoritative_regulator_evidence",
            "target_cell_presence_status": info["cell"], "binding_or_association_status": info["binding"],
            "downstream_expression_or_perturbation_status": info["downstream"], "downstream_activation_status": "not_established_for_SCI_target_cell",
            "upstream_relay_status": "not_tested_for_exact_pair", "disposition": info["disposition"],
            "primary_citation": info["primary"], "corroborating_citation": info["corr"], "near_match_exclusions": info["exclusions"],
            "review_notes": info["notes"] + " " + info["observation"], "exportable": "false", "canonical_write_performed": "false",
        })
        if key not in seen:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch027_regulator_{key}", "regulator_key": key,
                "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "evidence_layer": "regulator_identity_and_regulatory_capacity",
                "support_kind": info["kind"], "cell_or_model": info["model"], "assay_or_perturbation": info["assay"], "observation": info["observation"],
                "effect_direction": "queued-pair direction not established except explicitly recorded limited associations", "primary_citation": info["general_primary"],
                "corroborating_citation": info["general_corr"], "route_or_module_relevance": info["relevance"],
                "target_pair_scope": "not evidence for unrelated queued exact pairs; no upstream relay inferred", "exportable": "false", "canonical_write_performed": "false",
                "limitations": "Regulator-level evidence does not establish SCI target-cell presence, exact queued-target direction, downstream activation or upstream relay. Profile, chromatin, cofactor, machinery, protein, RNA and ligand/receptor evidence is retained separately from canonical promoter-TF evidence.",
            })
            seen.add(key)
    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch027_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch027_regulator_register.tsv"
    summary_path = args.output_dir / "batch_027_evidence_review_summary.json"
    report_path = args.output_dir / "EVIDENCE_REVIEW_BATCH027.md"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    status_counts: dict[str, int] = {}
    for item in pairs:
        status_counts[item["exact_pair_status"]] = status_counts.get(item["exact_pair_status"], 0) + 1
    pair_keys = {(x["regulator_key"], x["target_symbol"], x["species_scope"], x["source_record_id"]) for x in pairs}
    noncanonical = sum(v for k, v in status_counts.items() if k.startswith("functional_noncanonical_"))
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_027", "source_set_ranks_reviewed": list(range(1, 26)),
        "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen), "unique_provenance_aware_pairs": len(pair_keys),
        "exact_pair_status_counts": status_counts, "regulator_register_rows": len(evidence), "strict_tf_promotion_candidate_rows": 0,
        "noncanonical_exact_candidate_rows": noncanonical, "exportable_pair_rows": 0, "canonical_writes_performed": False,
        "module22b_promotions_performed": False, "provenance_preserved": True,
        "limitations": [
            "TFLink/profile resources are search leads, not causal regulation.",
            "Exact-pair negatives are bounded search results, not global absence.",
            "METTL3-to-ADAM10 is an exact noncanonical RNA-regulator candidate without SCI-cell validation or DNA occupancy; no strict TF promotion was made.",
            "AMH-to-ACVR1 is ligand/receptor signaling evidence, while HMGB1-to-ACVR1 is receptor-response evidence; neither is a TF edge.",
            "No canonical or Module 22B write was performed.",
        ],
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path.write_text("\n".join([
        "# Evidence review: public TF batch 027", "", f"Reviewed {len(pairs)} exact regulator-target-species pairs across 25 TFLink source-set ranks.", "",
        f"- **{len(pairs)}** pairs were reviewed across **{len(seen)}** regulators.",
        f"- **{noncanonical}** exact noncanonical candidate row was staged: human METTL3-to-ADAM10 mRNA modification/stability regulation.",
        f"- **{status_counts.get('binding_profile_only_not_promotable', 0)}** profile-only rows were retained without promotion.",
        f"- **{status_counts.get('ligand_receptor_signaling_not_transcriptional', 0)}** exact ligand/receptor signaling row was routed outside TF evidence.",
        "- **0** strict TF promotion candidates, exportable rows, canonical writes, or Module 22B writes.", "",
        "All rows retain the original TFLink source record, raw symbol, species, target, graph-module mapping and local source snapshot. Regulator-level chromatin, cofactor, machinery, profile, protein, RNA and ligand/receptor evidence is recorded separately from exact canonical TF evidence.", "",
    ]) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
