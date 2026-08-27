#!/usr/bin/env python3
"""Stage conservative evidence findings for all literal Batch 030 pairs."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/"
    "candidate_triage_v1/evidence_batches/batch_030/"
    "public_tf_evidence_collection_batch_030.tsv"
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


# symbol, primary, corroboration, support kind, model, assay, observation,
# module relevance.
REGULATORS = {
    "ebna1bp2": ("EBNA1BP2/EBP2", "https://www.ncbi.nlm.nih.gov/gene/10969", "https://pubmed.ncbi.nlm.nih.gov/24481446/", "primary_literature_regulator_level", "human nucleolar/rRNA-processing models", "RNA binding, nucleolar localization and c-Myc/ribosome-biogenesis assays", "EBNA1BP2 is an RNA-binding nucleolar/rRNA-processing protein, not a canonical TF; no queued target was validated.", "noncanonical RNA/ribosome-biogenesis capacity only"),
    "nlrc5": ("NLRC5", "https://pubmed.ncbi.nlm.nih.gov/20639463/", "https://www.nature.com/articles/ncomms10554", "primary_literature_regulator_level", "mouse immune and MHC-I transcription models", "promoter ChIP, reporter, knockdown and conditional perturbation assays", "NLRC5 is an atypical immune transcriptional transactivator with validated MHC-I targets, not the queued Adipor2/Ado/Calcrl/Cd48 edges.", "canonical immune transactivator capacity; queued edges unsupported"),
    "phf20": ("PHF20", "https://pubmed.ncbi.nlm.nih.gov/22072714/", "https://pubmed.ncbi.nlm.nih.gov/27760318/", "primary_literature_regulator_level", "human MOF/NSL chromatin models", "methyl-lysine reading, chromatin complex, knockout and RNA-seq assays", "PHF20 is a chromatin reader/NSL cofactor with nonqueued target evidence; the queued target genes were not validated.", "noncanonical chromatin-reader/cofactor capacity only"),
    "zfp708": ("ZFP708", "https://pubmed.ncbi.nlm.nih.gov/30846446/", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE125673", "primary_literature_regulator_level", "mouse embryo and mESC KRAB-ZFP models", "RMER19B occupancy, TRIM28 recruitment, H3K9me3 and methylation assays", "ZFP708 is a KRAB-C2H2 repressor with retrotransposon-locus evidence, not queued protein-coding target evidence.", "canonical KRAB-ZFP repressor capacity; queued edges unsupported"),
    "pbxip1": ("PBXIP1/HPIP", "https://pubmed.ncbi.nlm.nih.gov/12360403/", "https://www.uniprot.org/uniprotkb/Q96AQ6/entry", "primary_literature_regulator_level", "human PBX1-scaffold/corepressor models", "protein interaction, nuclear shuttling and PBX1-dependent transcription assays", "PBXIP1 is a protein scaffold/corepressor rather than a canonical DNA-binding TF; queued targets were not validated.", "noncanonical protein-scaffold/corepressor capacity only"),
    "f10": ("F10/factor Xa", "https://www.uniprot.org/uniprot/P00742/", "https://pubmed.ncbi.nlm.nih.gov/11342437/", "primary_literature_regulator_level", "human factor-Xa/PAR1 signaling models", "protease, PAR1 blockade and target-expression assays", "F10 encodes a secreted serine protease; exact CCN1 RNA-relay evidence is retained separately from TF evidence.", "ligand/protease/PAR1 signaling and downstream RNA regulation; exact CCN1 candidate"),
    "psmb5": ("PSMB5", "https://www.ncbi.nlm.nih.gov/gene/5693", "https://ashpublications.org/blood/article/112/6/2489/24848/Molecular-basis-of-bortezomib-resistance", "authoritative_annotation_and_primary_literature", "human 20S proteasome and leukemia models", "proteasome mutation, overexpression, siRNA and drug-sensitivity assays", "PSMB5 is a catalytic 20S proteasome subunit, not a TF; no queued target edge was validated.", "noncanonical proteasome/protein-complex capacity only"),
    "supt16h": ("SUPT16H/SPT16", "https://www.ncbi.nlm.nih.gov/gene/11198", "https://pubmed.ncbi.nlm.nih.gov/26378236/", "primary_literature_regulator_level", "human FACT transcription-elongation/chromatin models", "histone-chaperone, elongation, depletion and transcription assays", "SUPT16H is a FACT histone chaperone/elongation factor, not a sequence-specific TF; CCND1 protein response is retained as partial noncanonical evidence.", "noncanonical chromatin/elongation machinery; exact CCND1 protein readout"),
    "sap18": ("SAP18", "https://www.ncbi.nlm.nih.gov/gene/20220", "https://pubmed.ncbi.nlm.nih.gov/33273692/", "primary_literature_regulator_level", "mouse Sin3-associated corepressor models", "Sin3 complex, corepressor and target-repression assays", "SAP18 is a Sin3-associated transcriptional corepressor; validated examples are nonqueued and do not establish the four queued targets.", "noncanonical transcriptional-cofactor capacity only"),
    "dyrk1a": ("DYRK1A", "https://www.ncbi.nlm.nih.gov/gene/1859", "https://pubmed.ncbi.nlm.nih.gov/24119401/", "primary_literature_regulator_level", "human kinase and cell-cycle models", "co-immunoprecipitation, in-vitro kinase, CCND1-T286 mutant and cell-cycle assays", "DYRK1A is a dual-specificity kinase, not a TF; exact human CCND1 protein phosphorylation/stability regulation is retained separately.", "noncanonical kinase/cell-cycle protein regulation; exact CCND1 protein edge"),
    "lmtk3": ("LMTK3", "https://www.ncbi.nlm.nih.gov/gene/114783", "https://pubmed.ncbi.nlm.nih.gov/28260052/", "authoritative_annotation_and_primary_literature", "human LMTK3 kinase models", "kinase, knockdown and cancer-cell assays", "LMTK3 is a serine/threonine kinase, not a canonical TF; no queued target-specific mechanism was validated.", "noncanonical kinase capacity only"),
    "stfa1": ("STFA1/stefin A1", "https://www.ncbi.nlm.nih.gov/gene/20861", "https://pubmed.ncbi.nlm.nih.gov/8468045/", "authoritative_annotation_and_primary_literature", "mouse cysteine-protease-inhibitor models", "protein purification and protease-inhibition assays", "Stfa1 is a cysteine-protease inhibitor protein, not a TF; no queued target mechanism was validated.", "noncanonical protein/protease-inhibitor capacity only"),
    "supt20h": ("SUPT20H/SPT20", "https://www.ncbi.nlm.nih.gov/gene/55578", "https://pubmed.ncbi.nlm.nih.gov/19114550/", "primary_literature_regulator_level", "human SAGA-complex transcription models", "SAGA complex, ChIP/knockdown and ER-stress transcription assays", "SUPT20H is a SAGA chromatin/transcription cofactor, not a sequence-specific TF; queued targets were not validated.", "noncanonical chromatin/transcriptional-cofactor capacity only"),
    "ada2": ("ADA2/CECR1", "https://www.ncbi.nlm.nih.gov/gene/51816", "https://pubmed.ncbi.nlm.nih.gov/15926889/", "authoritative_identity_and_primary_literature", "human secreted ADA2/CECR1 models", "adenosine-deaminase activity, secretion and growth-factor assays", "ADA2 in this queue is CECR1/adenosine deaminase 2, a secreted enzyme; it is not TADA2A and not a TF.", "noncanonical secreted enzyme/growth-factor capacity only"),
    "pwwp2b": ("PWWP2B", "https://www.informatics.jax.org/marker/MGI%3A2142008", "https://pubmed.ncbi.nlm.nih.gov/34180153/", "primary_literature_regulator_level", "mouse NuRD/chromatin-reader models", "chromatin binding, NuRD association and thermogenic perturbation assays", "PWWP2B is a chromatin reader/NuRD component with nonqueued thermogenic evidence; queued targets were not validated.", "noncanonical chromatin-reader/cofactor capacity only"),
    "h1-6": ("H1-6/HIST1H1T", "https://www.ncbi.nlm.nih.gov/gene/3010", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4889250/", "authoritative_annotation_and_primary_literature", "human linker-histone/chromatin models", "ChIP-seq, ChIP-qPCR, nuclease sensitivity and rDNA expression assays", "H1-6/HIST1H1T is a linker histone/chromatin protein, not a sequence-specific TF; queued targets were not validated.", "noncanonical chromatin capacity only"),
    "nacc1": ("NACC1", "https://www.ncbi.nlm.nih.gov/gene/66830", "https://pubmed.ncbi.nlm.nih.gov/17254023/", "primary_literature_regulator_level", "mouse NACC1/CoREST and ESC models", "protein interaction, BEN-domain binding, repression and expression assays", "NACC1 is a transcriptional repressor/cofactor with nonqueued target evidence; none of the queued targets was validated.", "noncanonical transcriptional coregulator capacity only"),
    "hsd17b8": ("HSD17B8", "https://www.ncbi.nlm.nih.gov/gene/7923", "https://test-docs.gsea-msigdb.org/MSigDB/Release_Notes/MSigDB_2024.1.Hs/", "authoritative_identity_and_annotation_review", "human steroid-enzyme annotation and promoter-study context", "enzyme annotation, promoter assays for CEBPB→HSD17B8, and MSigDB set curation", "HSD17B8 is an enzyme, not a TF; MSigDB reports HSD17B8_TARGET_GENES was renamed RING2_TARGET_GENES to correct an upstream annotation error.", "annotation-review hold; not a transcriptional-regulator mechanism"),
    "gucy1b1": ("GUCY1B1", "https://www.ncbi.nlm.nih.gov/gene/2983", "https://pubmed.ncbi.nlm.nih.gov/7559610/", "authoritative_annotation_and_primary_literature", "human soluble guanylyl-cyclase signaling models", "NO activation, deletion-mutagenesis and cGMP assays", "GUCY1B1 is the beta subunit of soluble guanylyl cyclase, not a TF; queued promoter-profile rows were not validated.", "noncanonical signaling-enzyme capacity only"),
    "phf21a": ("PHF21A/BHC80", "https://www.uniprot.org/uniprotkb/Q96BD5/entry", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2702779/", "primary_literature_regulator_level", "human LSD1/CoREST chromatin-reader models", "H3K4me0 binding, chromatin association, knockdown and expression assays", "PHF21A is a chromatin reader/corepressor with nonqueued target evidence; queued genes were not validated.", "noncanonical chromatin-reader/corepressor capacity only"),
    "ubn2": ("UBN2", "https://www.informatics.jax.org/marker/MGI%3A2444236", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12165345/", "primary_literature_regulator_level", "mouse HIRA-associated chromatin/developmental models", "HIRA-complex, ESC multi-omics and developmental assays", "UBN2 is a HIRA-associated chromatin cofactor, not a sequence-specific TF; queued targets were not validated.", "noncanonical chromatin-cofactor capacity only"),
    "rtf1": ("RTF1", "https://www.informatics.jax.org/marker/MGI%3A1309480", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10219292/", "primary_literature_regulator_level", "mouse PAF1-complex/elongation models", "PAF1-complex, elongation and cardiomyocyte perturbation assays", "RTF1 is a transcription-elongation/chromatin cofactor, not a sequence-specific TF; queued targets were not validated.", "noncanonical transcriptional-machinery capacity only"),
    "duxbl2": ("DUXBL2", "https://www.informatics.jax.org/marker/MGI%3A3710620", "https://pubmed.ncbi.nlm.nih.gov/20063414/", "authoritative_identity_and_primary_literature", "mouse DUXBL-family developmental models", "family-level expression and developmental assays", "DUXBL2 is a limitedly characterized homeobox-family candidate; DUXBL-family evidence cannot be assigned to the queued targets.", "identity/family review only"),
    "taf9b": ("TAF9B", "https://www.ncbi.nlm.nih.gov/gene/51616", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4083437/", "primary_literature_regulator_level", "human TAF9B core-promoter/neuronal models", "ChIP/RNA-seq, TAF complex and neuronal transcription assays", "TAF9B is a TFIID/core-promoter cofactor, not a sequence-specific TF; queued target edges were not validated.", "noncanonical transcriptional-machinery capacity only"),
    "gtf2e2": ("GTF2E2", "https://www.ncbi.nlm.nih.gov/gene/2961", "https://www.encodeproject.org/experiments/ENCSR532KTI/", "authoritative_annotation_and_database_context", "human TFIIE/Pol II initiation models", "general-transcription-factor annotation and ENCODE ChIP-seq", "GTF2E2 is a TFIIE/Pol II initiation cofactor, not a sequence-specific TF; ENCODE assay availability does not validate queued targets.", "noncanonical transcriptional-machinery capacity only"),
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
    info = REGULATORS[key]
    symbol, general_primary, general_corr, kind, model, assay, observation, relevance = info
    out = {
        "symbol": symbol, "general_primary": general_primary, "general_corr": general_corr,
        "kind": kind, "model": model, "assay": assay, "observation": observation, "relevance": relevance,
        "status": "database_membership_only_not_promotable", "primary": TF_LINK_URL, "corr": "",
        "cell": "not_established_for_exact_pair", "binding": "TFLink_membership_only_no_queued_locus_validation",
        "downstream": "not_found_for_exact_pair", "disposition": "retain_provenance_traceable_candidate_without_promotion",
        "exclusions": "TFLink/database membership is a search lead; broad regulator evidence, orthologs, paralogs, reverse directions, general assay availability and complex-level findings were not transferred to this exact pair.",
        "notes": "No exact target-specific causal edge was established; target-cell presence, downstream activation and upstream relay are not inferred.",
    }

    if key == "f10" and target == "ccn1":
        out.update(status="functional_noncanonical_ligand_rna_candidate_not_tf", primary="https://pubmed.ncbi.nlm.nih.gov/11342437/", cell="human_HeLa_factor_Xa_PAR1_model_not_SCI_target_cell", binding="factor_Xa_activated_PAR1;_no_CCN1_locus_occupancy", downstream="factor_Xa_induced_CCN1_CYR61_expression_and_PAR1_blockade_abolished_induction", disposition="retain_noncanonical_ligand_rna_candidate_pending_SCI_context", exclusions="This is an extracellular protease/PAR1 signaling relay with downstream CCN1 RNA induction, not a TF-to-promoter edge or evidence of F10 DNA binding.", notes="Exact human F10/factor-Xa-to-CCN1 RNA relay is routed to ligand/protease signaling and downstream RNA evidence.")
    elif key == "f10" and target == "cdh2":
        out.update(status="engineered_target_protein_substrate_near_match_not_promotable", primary="https://pubmed.ncbi.nlm.nih.gov/21170270/", corr="https://pmc.ncbi.nlm.nih.gov/articles/PMC3003141/", cell="engineered_human_tumor_cell_factor_Xa_N_cadherin_model_not_endogenous_regulation", binding="factor_Xa_cleaved_engineered_factor_Xa_site_in_N_cadherin_precursor;_no_CDH2_locus_mechanism", downstream="engineered_cleavage_restored_adhesion_and_reduced_migration_invasion", disposition="retain_engineered_protein_substrate_near_match_separately", exclusions="The assay uses an engineered factor-Xa site and substrate construct; it does not establish physiological F10 regulation of endogenous CDH2 transcription or protein abundance.", notes="Engineered target-protein substrate evidence was not promoted.")
    elif key == "f10" and target == "col3a1":
        out.update(status="cross_species_ligand_rna_near_match_not_promotable", primary="https://pubmed.ncbi.nlm.nih.gov/32495720/", cell="mouse_Ren_Tg_cardiac_fibroblast_factor_Xa_PAR1_model_not_human_SCI_target_cell", binding="no_COL3A1_locus_occupancy;_PAR1-mediated_factor_Xa_signal", downstream="factor_Xa_increased_mouse_Col3a1_mRNA_and_PAR1_antagonist_blocked_increase", disposition="retain_cross_species_ligand_rna_near_match_separately", exclusions="The target direction is from mouse cardiac fibroblasts, not the exact human row, and is indirect through PAR1 without locus occupancy.", notes="Cross-species indirect RNA evidence was not transferred to the exact human pair.")
    elif key == "supt16h" and target == "ccnd1":
        out.update(status="target_protein_response_without_direct_mechanism_not_promotable", primary="https://pmc.ncbi.nlm.nih.gov/articles/PMC7648015/", cell="human_A549_NCI_H1299_NCI_H460_lung_cancer_models_not_SCI_target_cell", binding="no_CCND1_locus_occupancy_or_direct_SUPT16H_CCND1_binding", downstream="SUPT16H_siRNA_or_shRNA_depletion_decreased_CCND1_protein;_mRNA_direction_not_established", disposition="retain_target_protein_response_separately", exclusions="A target-protein response after FACT depletion lacks direct SUPT16H-CCND1 binding or a transcriptional mechanism; it is not a TF edge.", notes="Partial target-specific protein readout retained outside canonical TF evidence.")
    elif key == "dyrk1a" and target == "ccnd1":
        out.update(status="target_protein_regulation_not_transcriptional", primary="https://pubmed.ncbi.nlm.nih.gov/24119401/", corr="https://pubmed.ncbi.nlm.nih.gov/24806449/", cell="human_fibroblast_and_SH_SY5Y_kinase_models_not_SCI_target_cell", binding="DYRK1A_directly_phosphorylated_CCND1_T286;_no_CCND1_locus_occupancy", downstream="DYRK1A_activity_increased_CCND1_T286_phosphorylation_nuclear_export_and_proteasomal_loss", disposition="retain_target_protein_regulation_in_noncanonical_evidence_category", exclusions="This is a direct kinase-substrate/stability relationship, not transcriptional regulation. It must not be used as evidence that DYRK1A activates or represses the CCND1 gene.", notes="Exact human DYRK1A-to-CCND1 phosphorylation/stability evidence is routed to kinase/cell-cycle protein regulation.")
    elif key == "dyrk1a" and target == "col1a1":
        out.update(status="cross_species_indirect_rna_near_match_not_promotable", primary="https://pubmed.ncbi.nlm.nih.gov/19801542/", corr="https://pmc.ncbi.nlm.nih.gov/articles/PMC2785177/", cell="mouse_DYRK1A_transgenic_calvarial_osteoblast_model_not_human_SCI_target_cell", binding="no_COL1A1_locus_occupancy_or_direct_DYRK1A_COL1A1_protein_mechanism", downstream="increased_human_DYRK1A_dosage_reduced_mouse_Col1a1_mRNA_through_indirect_NFATc1_context", disposition="retain_cross_species_indirect_rna_near_match_separately", exclusions="The evidence is an indirect mouse near-match and does not validate the exact human DYRK1A-to-COL1A1 pair.", notes="Cross-species indirect RNA association was not promoted.")
    elif key == "ada2" and target == "anxa2":
        out.update(status="expression_association_not_promotable", primary="https://pubmed.ncbi.nlm.nih.gov/32845709/", cell="human_sepsis_time_series_biomarker_analysis_not_SCI_target_cell", binding="ADA2_and_ANXA2_co-occurrence_without_binding_or_protein_interaction_assay", downstream="co-expression_or_WGCNA_association_only;_no_ADA2_perturbation_direction", disposition="retain_weak_expression_association_separately", exclusions="A biomarker/co-expression association does not establish ADA2 regulation of ANXA2 RNA, protein or locus.", notes="Weak association was preserved without promotion; ADA2 was not confused with TADA2A.")
    elif key == "hsd17b8":
        out.update(status="annotation_review_hold_not_promotable", primary="https://test-docs.gsea-msigdb.org/MSigDB/Release_Notes/MSigDB_2024.1.Hs/", corr="https://www.ncbi.nlm.nih.gov/gene/7923", cell="human_annotation_review_not_SCI_target_cell", binding="queued_set_identity_requires_RING2_annotation_review;_no_HSD17B8_target_locus_validation", downstream="no_HSD17B8-specific_target_direction_found", disposition="retain_annotation_review_hold_separately", exclusions="MSigDB documents a prior HSD17B8_TARGET_GENES to RING2_TARGET_GENES correction; these queued rows must not be treated as validated HSD17B8 edges until source identity is resolved.", notes="Annotation identity uncertainty was retained explicitly.")
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
        info = classify(row)
        pairs.append({
            "review_id": f"public_tf_evidence_batch030_pair_{int(row['batch_rank']):02d}_{row['target_rank']}",
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
            "upstream_relay_status": "not_tested_for_exact_pair",
            "disposition": info["disposition"], "primary_citation": info["primary"],
            "corroborating_citation": info["corr"], "near_match_exclusions": info["exclusions"],
            "review_notes": info["notes"] + " " + info["observation"],
            "exportable": "false", "canonical_write_performed": "false",
        })
        key = row["regulator_key"]
        if key not in seen:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch030_regulator_{key}",
                "regulator_key": key, "regulator_symbol": info["symbol"], "species_scope": row["species_scope"],
                "evidence_layer": "regulator_identity_and_regulatory_capacity", "support_kind": info["kind"],
                "cell_or_model": info["model"], "assay_or_perturbation": info["assay"],
                "observation": info["observation"],
                "effect_direction": "queued-pair direction not established except explicitly recorded limited associations",
                "primary_citation": info["general_primary"], "corroborating_citation": info["general_corr"],
                "route_or_module_relevance": info["relevance"],
                "target_pair_scope": "not evidence for unrelated queued exact pairs; no upstream relay inferred",
                "exportable": "false", "canonical_write_performed": "false",
                "limitations": "Regulator-level evidence does not establish SCI target-cell presence, exact queued-target direction, downstream activation or upstream relay. Ligand, protein, RNA, chromatin, machinery, profile and near-match evidence is retained separately from canonical promoter-TF evidence.",
            })
            seen.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch030_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch030_regulator_register.tsv"
    summary_path = args.output_dir / "batch_030_evidence_review_summary.json"
    report_path = args.output_dir / "EVIDENCE_REVIEW_BATCH030.md"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    status_counts: dict[str, int] = {}
    for item in pairs:
        status_counts[item["exact_pair_status"]] = status_counts.get(item["exact_pair_status"], 0) + 1
    pair_keys = {(x["regulator_key"], x["target_symbol"], x["species_scope"], x["source_record_id"]) for x in pairs}
    noncanonical = sum(v for k, v in status_counts.items() if k.startswith("functional_noncanonical_"))
    near_match = sum(v for k, v in status_counts.items() if k not in {"database_membership_only_not_promotable", "functional_noncanonical_ligand_rna_candidate_not_tf"})
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_030",
        "source_set_ranks_reviewed": list(range(1, 26)), "pair_rows_reviewed": len(pairs),
        "unique_regulators_reviewed": len(seen), "unique_provenance_aware_pairs": len(pair_keys),
        "exact_pair_status_counts": status_counts, "regulator_register_rows": len(evidence),
        "strict_tf_promotion_candidate_rows": 0, "noncanonical_exact_candidate_rows": noncanonical,
        "partial_or_near_match_rows": near_match, "exportable_pair_rows": 0,
        "canonical_writes_performed": False, "module22b_promotions_performed": False,
        "provenance_preserved": True,
        "limitations": [
            "TFLink membership is a search lead, not causal regulation.",
            "Exact-pair negatives are bounded-search results, not global absence.",
            "F10-to-CCN1 is an exact indirect protease/PAR1 RNA relay; DYRK1A-to-CCND1 is exact kinase/protein regulation; neither is canonical promoter-TF evidence.",
            "The literal queue contains F10, PSMB5, SUPT16H, SAP18 and DYRK1A at ranks 6-10; alternate reconstructed regulators were not ingested.",
            "HSD17B8 rows remain annotation-review holds because MSigDB documents a prior source-set identity correction.",
            "No canonical or Module 22B write was performed.",
        ],
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path.write_text("\n".join([
        "# Evidence review: public TF batch 030", "",
        f"Reviewed {len(pairs)} exact regulator-target-species pairs across 25 TFLink source-set ranks.", "",
        f"- **{len(pairs)}** pairs were reviewed across **{len(seen)}** regulators.",
        f"- **{noncanonical}** exact noncanonical candidate row(s) were staged: human F10/factor-Xa-to-CCN1 via PAR1 and downstream RNA induction.",
        f"- **{status_counts.get('target_protein_regulation_not_transcriptional', 0)}** exact kinase/protein-regulation row(s) were routed outside TF evidence; SUPT16H-to-CCND1 remains a partial protein readout.",
        f"- **{near_match}** protein, RNA, cross-species, engineered, annotation or other limited rows were retained separately.",
        "- **0** strict TF, exportable, canonical or Module 22B writes were performed.", "",
        "All rows retain the original TFLink source record, raw symbol, species, target, graph-module mapping and local source snapshot. Literal Batch 030 queue membership was preserved; reconstructed names from a separate lane were not added as rows.", "",
    ]) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
