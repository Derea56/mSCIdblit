#!/usr/bin/env python3
"""Stage conservative evidence findings for all Batch 018 pairs.

Batch 018 is a noncanonical chromatin/cofactor slice.  A few exact-target or
contextual findings are retained as limited evidence, but no strict TF or
Module 22B write is performed.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_018/"
    "public_tf_evidence_collection_batch_018.tsv"
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
    "nelfe": ("NELFE/WHSC2", "https://pubmed.ncbi.nlm.nih.gov/12612062/", "https://pubmed.ncbi.nlm.nih.gov/29523821/", "primary_literature_regulator_level", "human biochemical and neuronal NELF models", "NELF reconstitution, promoter-proximal pausing, and phosphorylation/release studies", "NELFE is a Pol II pausing/elongation subunit; no queued target edge was established.", "noncanonical transcriptional modifier capacity only"),
    "dppa2": ("DPPA2", "https://pubmed.ncbi.nlm.nih.gov/30692203/", "https://pubmed.ncbi.nlm.nih.gov/34878123/", "primary_literature_regulator_level", "mouse ESC and maternal knockout models", "Dux ChIP-seq, overexpression, knockdown, knockout, and rescue", "DPPA2/4 regulates Dux in mouse ESC models, not the queued targets.", "noncanonical chromatin regulator capacity only"),
    "nipbl": ("NIPBL/SCC2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2953795/", "https://pubmed.ncbi.nlm.nih.gov/29094699/", "primary_literature_regulator_level", "mouse ESC and liver cohesin models", "promoter/enhancer occupancy, knockdown expression, and TAD-loss studies", "NIPBL has cohesin-loading and chromatin-architecture evidence at other loci, not the queued targets.", "noncanonical chromatin architecture capacity only"),
    "sap30": ("SAP30", "https://pubmed.ncbi.nlm.nih.gov/9702189/", "https://pubmed.ncbi.nlm.nih.gov/36302855/", "primary_literature_regulator_level", "human SIN3/HDAC corepressor models", "SIN3/HDAC recruitment and SAP30 depletion studies", "SAP30 corepressor evidence concerns nonqueued promoters such as MXD4, not the queued targets.", "noncanonical transcriptional coregulator capacity only"),
    "epop": ("EPOP/C17orf96", "https://pubmed.ncbi.nlm.nih.gov/27863225/", "https://pubmed.ncbi.nlm.nih.gov/41519789/", "primary_literature_regulator_level", "mouse pluripotent-cell PRC2.1 models", "Elongin BC recruitment and PRC2.1 chromatin association", "EPOP is a PRC2-associated chromatin regulator; no queued target edge was established.", "noncanonical chromatin coregulator capacity only"),
    "kdm6a": ("KDM6A/UTX", "https://www.nature.com/articles/s41467-026-70846-w", "https://assets-eu.researchsquare.com/files/rs-6065505/v1/76a9acd44dea6bd7ab94a025.pdf", "primary_literature_regulator_level", "human and mouse liver/macrophage chromatin models", "KDM6A CUT&Tag/ChIP, liver loss-of-function, and lipid-gene expression studies", "KDM6A chromatin-coregulator activity is documented at APOA1/APOM/APOH and related lipid genes; queued Abca1 evidence is ambiguous and separately recorded.", "noncanonical chromatin coregulator capacity only"),
    "cbx3": ("CBX3/HP1gamma", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5358721/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3409256/", "primary_literature_regulator_level", "human and neural CBX3 chromatin/RNA-processing models", "ChIP-seq, chromatin association, and perturbation studies", "CBX3/HP1gamma has promoter/gene-body chromatin and RNA-processing evidence, not the queued targets.", "noncanonical chromatin-reader capacity only"),
    "setd1a": ("SETD1A", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7873837/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5009724/", "primary_literature_regulator_level", "mouse macrophage, erythroid, and PFC models", "COMPASS occupancy, H3K4 methylation, enhancer/promoter regulation, and looping", "SETD1A has chromatin-regulator evidence at other loci, not the queued targets.", "noncanonical chromatin methyltransferase capacity only"),
    "brd3": ("BRD3", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3107332/", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE119863", "primary_literature_regulator_level", "human and mouse BET-reader models", "GATA1-linked promoter occupancy and human BRD3 ChIP resource", "BRD3 chromatin-reader activity is supported at other loci, not the queued targets.", "noncanonical chromatin-reader capacity only"),
    "smc3": ("SMC3", "https://www.encodeproject.org/experiments/ENCSR000ETL/", "https://pubmed.ncbi.nlm.nih.gov/37641131/", "authoritative_binding_dataset_only", "mouse MEL and human cancer cohesin models", "SMC3 ChIP-seq and enhancer regulation at nonqueued loci", "SMC3 occupancy resources exist, but no queued target-specific call or direction was established.", "noncanonical chromatin architecture capacity only"),
    "ssrp1": ("SSRP1/FACT", "https://pubmed.ncbi.nlm.nih.gov/17209051/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6238418/", "primary_literature_regulator_level", "human H1299 and FACT chromatin models", "siRNA/microarray, ChIP-qPCR, and chromatin-accessibility studies", "SSRP1 supports transcriptional elongation and chromatin accessibility at other loci, not the queued targets.", "noncanonical chromatin-remodeler/elongation capacity only"),
    "ncaph2": ("NCAPH2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5479651/", "", "primary_literature_regulator_level", "human condensin-II model", "condensin-II occupancy and knockdown at TFIIIC/histone-associated loci", "NCAPH2 chromosome architecture evidence does not establish queued target regulation.", "noncanonical chromosome-architecture capacity only"),
    "ell2": ("ELL2", "https://pubmed.ncbi.nlm.nih.gov/30297340/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2771556/", "primary_literature_regulator_level", "mouse B-cell/plasma-cell models", "ChIP-seq, Pol II elongation, expression, and RNA-splicing studies", "ELL2 is an elongation/cofactor regulator with nonqueued B-cell target evidence.", "noncanonical transcriptional modifier capacity only"),
    "stag2": ("STAG2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9439679/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3483546/", "primary_literature_regulator_level", "mouse cohesin/chromatin-architecture models", "cohesin occupancy, 3D architecture, and developmental gene regulation", "STAG2 is a cohesin/chromatin-architecture factor; the queued mouse target edges were not independently established.", "noncanonical chromatin architecture capacity only"),
    "jmjd6": ("JMJD6", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6258263/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3886918/", "primary_literature_regulator_level", "human enhancer and transcription-pause models", "ERalpha enhancer ChIP-seq, CARM1/MED12 recruitment, and pause-release studies", "JMJD6 has transcriptional co-regulator and RNA-processing evidence at other loci, not the queued targets.", "noncanonical transcriptional coregulator capacity only"),
    "yap1": ("YAP1", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4546604/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6307859/", "primary_literature_regulator_level", "mouse and human TEAD/coactivator models", "TEAD-dependent enhancer activity and YAP1 perturbation studies", "YAP1 is a transcriptional coactivator; the queued Abca1 evidence is a KLF11-directed complex association and reverse-direction pathway evidence was not transferred.", "noncanonical transcriptional coactivator capacity only"),
    "aff1": ("AFF1", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11113081/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4499153/", "primary_literature_regulator_level", "human SEC/Pol II elongation models", "AFF1/AFF4 ChIP-seq, elongation, and SEC studies", "AFF1 is an SEC scaffold/elongation regulator, not a sequence-specific TF for the queued targets.", "noncanonical transcriptional coregulator capacity only"),
    "cbx1": ("CBX1/HP1beta", "https://pmc.ncbi.nlm.nih.gov/articles/PMC1665633/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4587738/", "primary_literature_regulator_level", "human and mouse heterochromatin models", "DamID/heterochromatin binding and repression studies", "CBX1 is a heterochromatin reader/organizer with nonqueued target evidence.", "noncanonical chromatin-reader capacity only"),
    "setdb1": ("SETDB1", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2779743/", "https://pubmed.ncbi.nlm.nih.gov/16682412/", "primary_literature_regulator_level", "human and mouse chromatin-repression models", "H3K9me3 occupancy, knockdown, and promoter-associated silencing", "SETDB1 chromatin-repressor capacity is documented at other loci, not the queued targets.", "noncanonical chromatin methyltransferase capacity only"),
    "sap130": ("SAP130", "https://pubmed.ncbi.nlm.nih.gov/38172660/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8460660/", "primary_literature_regulator_level", "human Sin3A-HDAC and kidney-injury DAMP models", "transcriptional repression and Mincle signaling studies", "SAP130 has corepressor and extracellular DAMP evidence; neither establishes queued target regulation.", "noncanonical transcriptional coregulator and signaling-DAMP capacity only"),
    "brd9": ("BRD9", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10724271/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8536317/", "primary_literature_regulator_level", "mouse HSPC and macrophage chromatin models", "BRD9 ChIP-seq, ATAC/ChIP, deletion, and glucocorticoid-receptor cistrome studies", "BRD9 chromatin-remodeling evidence is real at other loci; no queued target-specific call was retrieved.", "noncanonical chromatin regulator capacity only"),
    "mllt1": ("MLLT1/ENL", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2234781/", "https://www.nature.com/articles/nature21687", "primary_literature_regulator_level", "human AML elongation/chromatin models", "ENL complex, ChIP-seq, H3K79 methylation, and elongation studies", "MLLT1/ENL is an elongation/chromatin-associated regulator with nonqueued promoter evidence.", "noncanonical transcriptional modifier capacity only"),
    "kmt2c": ("KMT2C/MLL3", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5662137/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7951951/", "primary_literature_regulator_level", "mouse ESC and hematopoietic enhancer models", "enhancer H3K4 methylation, Pol II/eRNA, ATAC/ChIPmentation, and cytokine-response studies", "KMT2C has enhancer/coactivator evidence at other loci, not the queued targets.", "noncanonical chromatin methyltransferase capacity only"),
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
    status = "chromatin_or_transcriptional_machinery_database_only_not_promotable"
    primary = TF_LINK_URL
    corr = ""
    cell = "not_established_for_exact_pair"
    binding = "TFLink_or_curated_database_membership_only"
    downstream = "not_found_for_exact_pair"
    disposition = "retain_noncanonical_regulator_candidate_separately"
    exclusions = "General regulator-level evidence at nonqueued loci, orthologs, reverse directions, co-models, and broad chromatin programs was not transferred to this exact pair."
    notes = "TFLink membership is a search lead only; it does not establish causal direction, target-cell presence, downstream activation, or upstream relay."

    if key == "kmt2d" and target == "abca1":
        status = "functional_chromatin_coregulator_promotion_candidate_not_strict_tf"
        primary = "https://pubmed.ncbi.nlm.nih.gov/18372346/"
        corr = "https://pmc.ncbi.nlm.nih.gov/articles/PMC2422828/"
        cell = "mouse_E9_5_MEF_model_not_SCI_target_cell"
        binding = "ASC2_MLL4_occupancy_at_Abca1_LXRE_and_H3K4me3"
        downstream = "LXR_ligand_increased_Abca1_with_MLL4_complex_dependent_reporter_or_expression_response"
        disposition = "retain_noncanonical_chromatin_coactivator_candidate_pending_SCI_context"
        exclusions = "MLL3 and MLL4 are redundant and ASC-2 loss disrupts the complex; the study did not selectively test KMT2D alone in an SCI model."
        notes = "Mouse LXR/ASC-2/MLL4 assays support Abca1 chromatin activation, but this is a noncanonical chromatin coactivator relationship rather than a strict sequence-specific TF edge."
    elif key == "gps2" and target == "abca1":
        status = "functional_noncanonical_coregulator_promotion_candidate_not_strict_tf"
        primary = "https://pubmed.ncbi.nlm.nih.gov/30153049/"
        binding = "GPS2_and_NFkB_p65_cooccupancy_at_Abca1_promoter_or_enhancers"
        downstream = "GPS2_loss_reduced_LPS_induced_Abca1_and_cholesterol_efflux"
        disposition = "retain_noncanonical_coregulator_candidate_pending_SCI_context"
        cell = "mouse_RAW_BMDM_and_peritoneal_macrophage_models_not_SCI_target_cell"
        exclusions = "GPS2 is a transcriptional coregulator rather than a sequence-specific DNA-binding TF; no SCI target-cell validation or independent second exact paper was found."
        notes = "GPS2 loss, Abca1 promoter/enhancer co-occupancy with NF-kB p65, and reduced lipid efflux support an exact module-relevant coregulator relationship, not a canonical TF promotion."
    elif key == "stag2" and target == "abca1":
        status = "ortholog_species_near_match_not_promotable"
        primary = "https://aacrjournals.org/cancerres/article/85/8_Supplement_1/1422/757047/Abstract-1422-STAG2-mediated-gene-expression"
        corr = "https://www.biorxiv.org/content/10.64898/2026.06.10.731379v1"
        cell = "human_MIBC_model_not_mouse_or_SCI_target_cell"
        binding = "human_STAG2_ChIP_seq_and_ChIP_qPCR_at_ABCA1_locus"
        downstream = "human_STAG2_loss_reduced_ABCA1_and_promoter_histone_acetylation"
        disposition = "retain_cross_species_noncanonical_chromatin_candidate_separately"
        exclusions = "The exact target evidence is human MIBC, while the queued row is mouse; STAG2 is a cohesin component rather than a sequence-specific TF."
        notes = "Human STAG2 occupancy and loss-of-function effects at ABCA1 are a useful cross-species chromatin lead, but they do not establish the queued mouse edge."
    elif key == "kdm6a" and row["species_scope"] == "mouse" and target == "abca1":
        status = "ambiguous_expression_panel_not_promotable"
        primary = "https://www.nature.com/articles/s41467-026-70846-w"
        corr = "https://assets-eu.researchsquare.com/files/rs-6065505/v1/76a9acd44dea6bd7ab94a025.pdf"
        cell = "mouse_primary_hepatocyte_and_liver_loss_of_function_model_not_SCI_target_cell"
        binding = "no_KDM6A_Abca1_locus_binding_established"
        downstream = "Abca1_in_supplementary_LXR_agonist_panel_without_assignable_Kdm6a_only_direction"
        disposition = "retain_ambiguous_chromatin_expression_context_separately"
        notes = "Abca1 appeared in an LXR-agonist qPCR panel, but the accessible report did not assign a clear Kdm6a-only effect or direction and showed KDM6A occupancy at other lipid loci."
    elif key == "yap1" and target == "abca1":
        status = "contextual_complex_association_not_promotable"
        primary = "https://pmc.ncbi.nlm.nih.gov/articles/PMC12199419/"
        binding = "KLF11_direct_Abca1_promoter_enrichment_in_YAP1_associated_complex"
        downstream = "YAP1_PPARalpha_KLF11_complex_associated_with_ABCA1_expression_and_cholesterol_efflux"
        disposition = "retain_contextual_cofactor_association_separately"
        cell = "mouse_macrophage_atherosclerosis_model_not_SCI_target_cell"
        exclusions = "KLF11, not YAP1, had the direct Abca1 promoter enrichment and reporter evidence; YAP1-specific binding, perturbation, and rescue were not shown."
        notes = "This is contextual YAP1 complex evidence, not a direct YAP1-to-Abca1 edge."
    elif key == "yap1" and target == "ackr3":
        status = "reverse_direction_pathway_association_not_promotable"
        primary = "https://pubmed.ncbi.nlm.nih.gov/36210463/"
        binding = "no_YAP1_Ackr3_locus_binding_established"
        downstream = "ACKR3_CXCR7_signaling_promoted_YAP1_nuclear_or_Hippo_YAP_activity"
        disposition = "retain_reverse_direction_pathway_association_separately"
        cell = "mouse_or_nonqueued_model_not_SCI_target_cell"
        notes = "The evidence is ACKR3/CXCR7 upstream of YAP activity, not YAP1 regulation of Ackr3."
    elif key == "yap1" and target == "actr2":
        status = "reverse_noncanonical_association_not_promotable"
        primary = "https://pmc.ncbi.nlm.nih.gov/articles/PMC12199419/"
        binding = "no_YAP1_Actr2_locus_binding_established"
        downstream = "ACTR2_derived_circular_RNA_associated_with_macrophage_polarization_through_YAP_signaling"
        disposition = "retain_reverse_noncanonical_association_separately"
        notes = "The evidence is ACTR2-derived RNA upstream of YAP signaling, not YAP1 transcriptional regulation of Actr2."
    elif key == "yap1" and target == "acvr1":
        status = "reverse_direction_pathway_association_not_promotable"
        primary = "https://pmc.ncbi.nlm.nih.gov/articles/PMC7209824/"
        binding = "no_YAP1_Acvr1_locus_binding_established"
        downstream = "mutant_ACVR1_increased_nuclear_YAP1_and_YAP_target_expression"
        disposition = "retain_reverse_direction_pathway_association_separately"
        notes = "The evidence is ACVR1 upstream of YAP1 in an FOP model, not YAP1 regulation of Acvr1."
    elif key == "sap130" and target == "actr2":
        status = "network_cooccurrence_only_not_promotable"
        primary = "https://pubmed.ncbi.nlm.nih.gov/38172660/"
        binding = "no_SAP130_ACTR2_binding_or_promoter_assay_established"
        downstream = "network_or_cooccurrence_only"
        disposition = "retain_network_cooccurrence_separately"
        notes = "SAP130 and ACTR2 co-occurrence in a review/network context is not regulatory evidence."
    elif key == "brd9" and target == "abca1" and row["species_scope"] == "mouse":
        status = "chromatin_resource_without_target_call_not_promotable"
        primary = "https://pmc.ncbi.nlm.nih.gov/articles/PMC10724271/"
        binding = "mouse_BRD9_chromatin_resource_without_retrieved_Abca1_call"
        disposition = "retain_chromatin_resource_lead_separately"
        notes = "Mouse BRD9 ChIP/ATAC resources support chromatin-regulator capacity, but no Abca1-specific call or direction was retrieved."

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
            "review_id": f"public_tf_evidence_batch018_pair_{int(row['batch_rank']):02d}_{row['target_rank']}",
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
            "primary_citation": info["primary"], "corroborating_citation": info["corr"], "near_match_exclusions": info["exclusions"],
            "review_notes": info["notes"] + " " + info["observation"], "exportable": "false", "canonical_write_performed": "false",
        })
        if key not in seen:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch018_regulator_{key}", "regulator_key": key,
                "regulator_symbol": info["symbol"], "species_scope": row["species_scope"],
                "evidence_layer": "regulator_identity_and_regulatory_capacity", "support_kind": info["kind"],
                "cell_or_model": info["model"], "assay_or_perturbation": info["assay"], "observation": info["observation"],
                "effect_direction": "queued-pair direction not established except explicitly recorded limited associations",
                "primary_citation": info["general_primary"], "corroborating_citation": info["general_corr"],
                "route_or_module_relevance": info["relevance"], "target_pair_scope": "not evidence for unrelated queued exact pairs; no upstream relay inferred",
                "exportable": "false", "canonical_write_performed": "false",
                "limitations": "Regulator-level evidence does not establish SCI target-cell presence, exact queued-target direction, downstream activation, or upstream relay. Chromatin-associated, cofactor, and reverse-direction evidence is retained separately from canonical promoter-TF evidence.",
            })
            seen.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch018_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch018_regulator_register.tsv"
    summary_path = args.output_dir / "batch_018_evidence_review_summary.json"
    report_path = args.output_dir / "EVIDENCE_REVIEW_BATCH018.md"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    status_counts: dict[str, int] = {}
    for item in pairs:
        status_counts[item["exact_pair_status"]] = status_counts.get(item["exact_pair_status"], 0) + 1
    pair_keys = {(item["regulator_key"], item["target_symbol"], item["species_scope"], item["source_record_id"]) for item in pairs}
    noncanonical_exact = sum(v for k, v in status_counts.items() if k in {"functional_chromatin_coregulator_promotion_candidate_not_strict_tf", "functional_noncanonical_coregulator_promotion_candidate_not_strict_tf"})
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_018", "source_set_ranks_reviewed": list(range(1, 26)),
        "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen), "unique_provenance_aware_pairs": len(pair_keys),
        "exact_pair_status_counts": status_counts, "regulator_register_rows": len(evidence), "strict_tf_promotion_candidate_rows": 0,
        "noncanonical_exact_candidate_rows": noncanonical_exact, "exportable_pair_rows": 0, "canonical_writes_performed": False,
        "module22b_promotions_performed": False, "provenance_preserved": True,
        "limitations": ["TFLink membership is a search lead, not causal regulation.", "Exact pair negatives are bounded-search results, not global absence.", "STAG2-ABCA1 evidence is human while the queued row is mouse.", "YAP1-ABCA1 direct promoter evidence belongs to KLF11, not YAP1.", "No canonical or Module 22B write was performed."],
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path.write_text("\n".join([
        "# Evidence review: public TF batch 018", "", "Reviewed 100 exact regulator-target-species pairs across 25 selected source-set ranks.", "",
        f"- **{len(pairs)}** pairs were reviewed across **{len(seen)}** regulators.",
        f"- **{noncanonical_exact}** exact noncanonical candidates were retained: none are strict TF promotions.",
        f"- **{status_counts.get('ambiguous_expression_panel_not_promotable', 0)}** ambiguous expression-panel result and **{status_counts.get('network_cooccurrence_only_not_promotable', 0)}** network co-occurrence result were kept separate.",
        f"- **{status_counts.get('ortholog_species_near_match_not_promotable', 0)}** cross-species chromatin near-match and **{status_counts.get('contextual_complex_association_not_promotable', 0)}** cofactor-complex association were not transferred to the queued exact edge.",
        "- **0** strict TF promotion candidates, exportable rows, canonical writes, or Module 22B writes.", "",
        "All rows retain the original TFLink source record, raw symbol, species, target, graph-module mapping, and local source snapshot. General chromatin, cofactor, network, and reverse-direction evidence is recorded separately from exact canonical TF evidence.", "",
    ]) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
