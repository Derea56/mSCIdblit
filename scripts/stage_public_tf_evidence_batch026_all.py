#!/usr/bin/env python3
"""Stage conservative evidence findings for all Batch 026 pairs."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/"
    "candidate_triage_v1/evidence_batches/batch_026/"
    "public_tf_evidence_collection_batch_026.tsv"
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
# route/module relevance, profile URL (empty means no profile citation).
REGULATORS = {
    "wiz": ("WIZ", "https://pubmed.ncbi.nlm.nih.gov/25789554/", "https://pubmed.ncbi.nlm.nih.gov/27410475/", "primary_literature_regulator_level", "human U2OS and mouse chromatin-repression models", "ChIP-seq/ChIP-qPCR, siRNA depletion and expression assays", "WIZ is a DNA-binding component of G9a/GLP repression machinery with exact noncanonical CWH43 and DIP2C evidence in human U2OS cells.", "noncanonical chromatin-regulator capacity; exact CWH43/DIP2C candidates", "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/WIZ_TARGET_GENES.html"),
    "smyd5": ("SMYD5", "https://pubmed.ncbi.nlm.nih.gov/28250819/", "https://pubmed.ncbi.nlm.nih.gov/35680905/", "primary_literature_regulator_level", "mouse ESC and chromatin/methylation models", "histone methylation, ChIP-seq and perturbation assays", "SMYD5 is a chromatin methyltransferase with broad mouse ESC and repetitive-element evidence; the queued Eapp row is profile-only and the Gm rows are unsupported.", "noncanonical chromatin-methyltransferase capacity only", "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/SMYD5_TARGET_GENES.html"),
    "cbx1": ("CBX1/HP1beta", "https://remap2022.univ-amu.fr/target_page/CBX1%3A10090", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2582898/", "primary_literature_regulator_level", "mouse heterochromatin/ESC models", "H3K9me reader, ChIP-seq and knockout assays", "CBX1/HP1beta is a chromatin reader and heterochromatin regulator; queued rows are profile or unsupported leads without target direction.", "noncanonical chromatin-reader capacity only", "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/CBX1_TARGET_GENES.html"),
    "atad2": ("ATAD2", "https://pubmed.ncbi.nlm.nih.gov/26459632/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8500222/", "primary_literature_regulator_level", "mouse ESC chromatin-dynamics models", "ChIP-seq, knockdown/overexpression and chromatin assays", "ATAD2 is a chromatin-dynamics facilitator with broad active-gene effects, but no queued target-specific direction was established.", "noncanonical chromatin-regulator capacity only", "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/ATAD2_TARGET_GENES.html"),
    "pcgf5": ("PCGF5", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5954019/", "https://pubmed.ncbi.nlm.nih.gov/29765032/", "primary_literature_regulator_level", "mouse PRC1/neural-differentiation models", "PRC1 occupancy and loss/gain-of-function assays", "PCGF5/PRC1 evidence is strongest at mouse Nodal and Lefty loci; the queued human targets were not validated.", "noncanonical Polycomb-regulator capacity only", ""),
    "usp7": ("USP7", "https://pubmed.ncbi.nlm.nih.gov/37196079/", "https://www.ncbi.nlm.nih.gov/biosample/SAMN05578943", "primary_literature_regulator_level", "mouse ESC Polycomb/chromatin models", "CUT&Tag/ChIP-seq, depletion and chromatin assays", "USP7 is a chromatin-associated deubiquitinase; the queued Rbbp4 relation is complex-level and the other queued pairs lack exact validation.", "noncanonical chromatin-deubiquitinase capacity only", ""),
    "suv39h1": ("SUV39H1", "https://pubmed.ncbi.nlm.nih.gov/10949293/", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE57092", "primary_literature_regulator_level", "mouse ESC heterochromatin models", "H3K9 methyltransferase ChIP-seq/RNA-seq and retrotransposon assays", "SUV39H1 is an H3K9 methyltransferase; its queued Dux/AW822073 and Itln1 rows are profile-only, with direction shown for retrotransposons instead.", "noncanonical chromatin-methyltransferase capacity only", ""),
    "kdm4d": ("KDM4D", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10236313/", "https://pubmed.ncbi.nlm.nih.gov/21293030/", "primary_literature_regulator_level", "mouse MEF interferon and testis models", "ChIP-seq, knockdown/overexpression, stimulation and knockout assays", "KDM4D regulates nonqueued interferon genes and H3K9 methylation; A930009A15Rik remains a profile-only lead.", "noncanonical chromatin-demethylase capacity only", "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/KDM4D_TARGET_GENES.html"),
    "mfsd11": ("MFSD11", "https://www.ncbi.nlm.nih.gov/gene/69900", "https://pubmed.ncbi.nlm.nih.gov/27272503/", "authoritative_annotation_only", "mouse metabolic-expression models", "expression and localization studies", "MFSD11 is a predicted major-facilitator-superfamily membrane protein, not an established TF or chromatin regulator; no queued target mechanism was found.", "not a transcriptional-regulator candidate; retain as database-origin trace only", ""),
    "cul4a": ("CUL4A", "https://www.uniprot.org/uniprotkb/Q13619/entry", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3901356/", "primary_literature_regulator_level", "human ubiquitin-ligase/chromatin models", "CRL4 complex, ChIP-seq, ubiquitination and transcription assays", "CUL4A is a cullin-RING E3-ligase scaffold with protein/chromatin effects at nonqueued loci; ACVR1 is only a complex near-match.", "noncanonical protein/chromatin-regulator capacity only", ""),
    "dtl": ("DTL/CDT2", "https://www.ncbi.nlm.nih.gov/gene/51514/", "https://pubmed.ncbi.nlm.nih.gov/16949367/", "primary_literature_regulator_level", "human and mouse CRL4-DDB1 cell-cycle models", "substrate-receptor, ubiquitination and depletion assays", "DTL/CDT2 is a CRL4-DDB1 substrate receptor regulating proteins such as CDT1 and p21, not a sequence-specific TF; no queued target was validated.", "noncanonical protein-regulator capacity only", ""),
    "hdgfl3": ("HDGFL3/HRP3", "https://pubmed.ncbi.nlm.nih.gov/31162607/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8748221/", "primary_literature_regulator_level", "human PWWP/chromatin models", "DNA/chromatin binding and promoter assays", "HDGFL3/HRP3 is a PWWP-domain chromatin/DNA-binding protein with nonqueued E2F1 promoter evidence; queued targets lack exact validation.", "noncanonical chromatin-regulator capacity only", ""),
    "magi1": ("MAGI1", "https://pubmed.ncbi.nlm.nih.gov/9395497/", "https://pubmed.ncbi.nlm.nih.gov/12042308/", "primary_literature_regulator_level", "human and mouse MAGUK-scaffold models", "protein-interaction and scaffold assays", "MAGI1 is a MAGUK scaffold and protein-interaction organizer, not a TF; the mouse Abca1 row has only a human PPI near-match.", "noncanonical scaffold/protein-regulator capacity only", ""),
    "sinhcaf": ("SINHCAF/FAM60A", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5538769/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3463326/", "primary_literature_regulator_level", "mouse Sin3A-HDAC/ES-cell models", "complex occupancy, promoter assays and repression studies", "SINHCAF/FAM60A is a Sin3A-HDAC coregulator with nonqueued promoter evidence; no queued target-specific direction was found.", "noncanonical transcriptional-coregulator capacity only", ""),
    "ivns1abp": ("IVNS1ABP/NS1-BP", "https://pubmed.ncbi.nlm.nih.gov/30538201/", "https://pubmed.ncbi.nlm.nih.gov/29871674/", "primary_literature_regulator_level", "human patient fibroblast/iPSC/neural-progenitor and RNA-processing models", "pull-down/AP-MS, splicing/export and promoter assays", "IVNS1ABP is primarily an RNA-splicing/export and actin-associated regulator; ACTR2 occurs in a protein complex, without ACTR2 mRNA direction.", "noncanonical RNA/protein-regulator capacity; ACTR2 kept outside TF evidence", ""),
    "zfp217": ("ZFP217", "https://pubmed.ncbi.nlm.nih.gov/26526723/", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE65730", "primary_literature_regulator_level", "mouse ESC pluripotency models", "ChIP-seq, depletion RNA-seq and expression assays", "ZFP217 is a bona fide zinc-finger TF with nonqueued Nanog/Sox2/Klf4/c-Myc evidence; queued targets are profile-only.", "canonical TF identity supported generally; queued edges remain profile-only", ""),
    "wdr43": ("WDR43", "https://pubmed.ncbi.nlm.nih.gov/31128943/", "https://www.ncbi.nlm.nih.gov/sra/SRX9731386", "primary_literature_regulator_level", "mouse chromatin/RNA-polymerase and ribogenesis models", "promoter/nascent-RNA occupancy, knockdown and rapid-degradation assays", "WDR43 is a chromatin-associated RNA-binding/ribogenesis regulator with broad Pol II-release effects, not queued target-specific direction.", "noncanonical chromatin/RNA-regulator capacity only", ""),
    "utp6": ("UTP6/HCA66", "https://pubmed.ncbi.nlm.nih.gov/22434888/", "https://www.ncbi.nlm.nih.gov/gene/55813", "authoritative_annotation_and_primary_literature", "human and mouse SSU-processome/ribosome-biogenesis models", "pre-rRNA processing, complex and centriole assays", "UTP6/HCA66 is primarily an SSU-processome/ribosome-biogenesis component, not a regulator of the queued mRNA loci.", "not a queued transcriptional-regulator mechanism", ""),
    "tbxt": ("TBXT/Brachyury", "https://pubmed.ncbi.nlm.nih.gov/22847733/", "https://pubmed.ncbi.nlm.nih.gov/24616493/", "primary_literature_regulator_level", "human chordoma/gastruloid and mouse embryonic models", "ChIP-seq/ChIP-exo, shRNA, knockout and expression assays", "TBXT is a strict TF with direct nonqueued Foxa2, Lmo2, Mesp1 and Snai1 evidence; queued targets lack pair-specific validation.", "canonical TF identity supported generally; queued edges remain profile-only", ""),
    "abcc9": ("ABCC9/SUR2", "https://www.ncbi.nlm.nih.gov/gene/20928", "https://pubmed.ncbi.nlm.nih.gov/24648545/", "authoritative_annotation_and_primary_literature", "mouse cardiac KATP-channel models", "channel/subunit deletion and cardiac phenotype assays", "ABCC9/SUR2 is a membrane KATP-channel regulatory subunit, not a transcriptional regulator; no queued target mechanism was found.", "not a transcriptional-regulator mechanism", ""),
    "phf19": ("PHF19", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3926938/", "https://www.ncbi.nlm.nih.gov/gene/74016", "primary_literature_regulator_level", "mouse ESC Polycomb/PRC2 models", "H3K36me recognition, occupancy and repression assays", "PHF19 is a PRC2-associated chromatin regulator; queued rows are profile-only and lack target-specific direction.", "noncanonical Polycomb-regulator capacity only", ""),
    "dpep2": ("DPEP2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6416667/", "https://www.uniprot.org/uniprotkb/Q8C255/entry", "authoritative_annotation_and_primary_literature", "mouse macrophage inflammation models", "membrane dipeptidase expression and loss-of-function assays", "DPEP2 is a membrane-bound M19 dipeptidase, not a TF or RNA-binding regulator; no queued target mechanism was found.", "not a transcriptional-regulator mechanism", ""),
    "ptbp1": ("PTBP1", "https://www.nature.com/articles/s41586-020-2077-3", "https://www.uniprot.org/uniprotkb/P26599/entry", "primary_literature_regulator_level", "human eCLIP/RNA-processing models", "eCLIP, CLIP/RIP and splicing perturbation assays", "PTBP1 is an RNA-binding splicing regulator with broad direct RNA targets, not a DNA-binding TF; queued mRNA relationships were not validated.", "noncanonical RNA-processing capacity only", ""),
    "gtf3c5": ("GTF3C5/TFIIIC subunit", "https://pubmed.ncbi.nlm.nih.gov/23966877/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7014570/", "primary_literature_regulator_level", "human and mouse TFIIIC/chromatin-looping models", "TFIIIC occupancy, looping and complex assays", "GTF3C5 is a TFIIIC subunit with complex-dependent chromatin effects at nonqueued loci, not a sequence-specific queued-target TF.", "noncanonical transcriptional-machinery/chromatin capacity only", ""),
    "fbxl19": ("FBXL19", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5997449/", "https://pubmed.ncbi.nlm.nih.gov/28453857/", "primary_literature_regulator_level", "mouse ES-cell promoter/chromatin models", "CpG-island binding, CDK-Mediator recruitment and H2Bub1 assays", "FBXL19 is a CpG-island/chromatin regulator with nonqueued promoter evidence; queued targets lack exact validation.", "noncanonical chromatin/coregulator capacity only", ""),
}


PROFILE_TARGETS = {
    "wiz": {"caskin2", "flcn"},
    "smyd5": {"eapp"},
    "cbx1": {"abcc9", "gm21083", "gm7324"},
    "atad2": {"9930022d16rik", "ecel1", "haus5", "kcna6"},
    "suv39h1": {"aw822073", "itln1"},
    "kdm4d": {"a930009a15rik"},
    "cul4a": {"ackr1", "ackr2", "acvrl1"},
    "zfp217": {"a2m", "ackr3", "actr2", "acvr1"},
    "wdr43": {"a2m", "acvr1", "acvr1c", "adam10"},
    "tbxt": {"actr2", "acvr1", "adam12", "adam17"},
    "phf19": {"abca1", "adam12", "adgrb1", "adgrb3"},
    "ptbp1": {"acvr1", "acvrl1", "adam17", "adc yap1".replace(" ", "")},
    "gtf3c5": {"ackr2", "acvr1", "acvrl1", "adam17"},
    "fbxl19": {"acvr1c", "adam22", "adam23", "adam9"},
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
        "corr": corr if profile else "", "cell": f"{row['species_scope']}_GTRD_or_TFLink_profile_not_SCI_target_cell",
        "binding": f"{row['species_scope']}_promoter_profile_membership_without_queued_locus_validation",
        "downstream": "no_target_specific_perturbation_or_direction_found",
        "disposition": "retain_binding_profile_lead_separately",
        "exclusions": "Profile/database membership is a search lead; it does not establish target-cell presence, causal direction, downstream activation or an upstream relay.",
        "notes": "Exact species-matched profile evidence is retained as a noncanonical binding lead only.",
    }


def classify(row: dict[str, str]) -> dict[str, str]:
    key = row["regulator_key"]
    target = row["target_symbol"].lower()
    info = REGULATORS[key]
    symbol, general_primary, general_corr, kind, model, assay, observation, relevance, _profile = info
    out = {
        "symbol": symbol, "general_primary": general_primary, "general_corr": general_corr,
        "kind": kind, "model": model, "assay": assay, "observation": observation,
        "relevance": relevance, "status": "database_membership_only_not_promotable", "primary": TF_LINK_URL,
        "corr": "", "cell": "not_established_for_exact_pair",
        "binding": "TFLink_membership_only_no_queued_locus_validation", "downstream": "not_found_for_exact_pair",
        "disposition": "retain_provenance_traceable_candidate_without_promotion",
        "exclusions": "TFLink/database membership is a search lead; broad regulator evidence, orthologs, paralogs, reverse directions and complex-level findings were not transferred to this exact pair.",
        "notes": "No exact target-specific causal edge was established; target-cell presence, downstream activation and upstream relay are not inferred.",
    }
    if key == "wiz" and row["species_scope"] == "human" and target in {"cwh43", "dip2c"}:
        out.update(status="functional_noncanonical_chromatin_regulator_candidate_not_strict_tf", primary="https://pubmed.ncbi.nlm.nih.gov/25789554/", corr="https://elifesciences.org/articles/05606.pdf", cell="human_U2OS_model_not_SCI_target_cell", binding="WIZ_ChIP_seq_and_ChIP_qPCR_at_CWH43_or_DIP2C_locus", downstream="WIZ_depletion_increased_target_transcription", disposition="retain_noncanonical_chromatin_candidate_pending_SCI_context", exclusions="The exact human occupancy/siRNA result supports a noncanonical chromatin regulator, not an isolated sequence-specific TF mechanism; SCI target-cell context is absent.", notes="Exact human WIZ-to-target occupancy and perturbation evidence is staged as a noncanonical chromatin-regulator candidate.")
    elif key == "ivns1abp" and row["species_scope"] == "human" and target == "actr2":
        out.update(status="target_protein_complex_association_not_transcriptional", primary="https://pubmed.ncbi.nlm.nih.gov/41857046/", corr="https://www.nature.com/articles/s41467-026-70756-x", cell="human_patient_fibroblast_iPSC_and_neural_progenitor_models_not_SCI_target_cell", binding="ACTR2_detected_in_IVNS1ABP_pull_down_or_AP_MS_complex;_no_locus_occupancy", downstream="WT_or_control_IVNS1ABP_association_enrichment_exceeded_F253C_mutant_without_ACTR2_mRNA_direction", disposition="retain_target_protein_complex_evidence_separately", exclusions="The evidence is a protein-complex association, not DNA occupancy or target-gene regulation. No transcriptional ACTR2 edge is inferred.", notes="Exact human IVNS1ABP-to-ACTR2 protein-complex evidence is routed outside TF evidence and retains the 2026 primary article.")
    elif key == "usp7" and row["species_scope"] == "mouse" and target == "rbbp4":
        out.update(status="complex_level_near_match_not_promotable", primary="https://pubmed.ncbi.nlm.nih.gov/37196079/", cell="mouse_ESC_model_not_SCI_target_cell", binding="USP7_chromatin_occupancy_or_Polycomb_complex_evidence_without_Rbbp4_locus_validation", downstream="no_Rbbp4_specific_direction_found", disposition="retain_complex_level_near_match_separately", exclusions="USP7 and RBBP4 occur in chromatin/Polycomb contexts, but the queued edge lacks target-specific locus and direction evidence.", notes="Complex-level USP7/RBBP4 near-match was not transferred to a causal edge.")
    elif key == "magi1" and row["species_scope"] == "mouse" and target == "abca1":
        out.update(status="cross_species_protein_interaction_near_match_not_promotable", primary="https://pubmed.ncbi.nlm.nih.gov/9395497/", corr="https://www.uniprot.org/uniprotkb/O95477/entry", cell="human_PPI_record_not_mouse_SCI_target_cell", binding="human_MAGI1_ABCA1_binary_interaction_without_mouse_locus_evidence", downstream="no_perturbation_or_direction_found", disposition="retain_cross_species_protein_near_match_separately", exclusions="A human MAGI1-ABCA1 protein-interaction record does not establish mouse Magi1 regulation of Abca1 or transcriptional direction.", notes="Cross-species PPI near-match only.")
    elif key == "cul4a" and row["species_scope"] == "human" and target == "acvr1":
        out.update(status="complex_protein_association_near_match_not_promotable", primary="https://thebiogrid.org/interaction/3585406", corr="https://pubmed.ncbi.nlm.nih.gov/36688959/", cell="human_CRL4_DCAF6_models_not_SCI_target_cell", binding="DCAF6_ACVR1_affinity_capture_not_CUL4A_specific_and_no_ACVR1_locus_occupancy", downstream="no_CUL4A_ACVR1_direction_found", disposition="retain_complex_protein_near_match_separately", exclusions="The affinity-capture association is DCAF6/complex-level and the cited CRL4 substrate study concerns CtBP1/2, not ACVR1. It does not establish CUL4A-to-ACVR1 regulation.", notes="Complex-level CUL4A/ACVR1 near-match is not promoted.")
    elif key == "smyd5" and target in {"gm10717", "gm10722", "gm11168"}:
        out["notes"] = "No exact target-level evidence was located; the queued Gm rows remain unsupported rather than being relabeled as profile hits."
    elif key == "cbx1" and target == "aw822073":
        out["notes"] = "AW822073/Dux network or gene-list context was not treated as Cbx1 locus evidence."
    elif key in PROFILE_TARGETS and target in PROFILE_TARGETS[key]:
        out.update(profile_status(row, info))
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_BATCH.parent)
    args = parser.parse_args()
    rows = read_tsv(args.batch)
    if len(rows) != 93:
        raise SystemExit(f"expected 93 rows, found {len(rows)}")
    pairs: list[dict[str, str]] = []
    evidence: list[dict[str, str]] = []
    seen: set[str] = set()
    for row in rows:
        if row["regulator_key"] not in REGULATORS:
            raise SystemExit(f"missing evidence map for {row['regulator_key']}")
        info = classify(row)
        pairs.append({
            "review_id": f"public_tf_evidence_batch026_pair_{int(row['batch_rank']):02d}_{row['target_rank']}",
            "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": row["regulator_key"],
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
        key = row["regulator_key"]
        if key not in seen:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch026_regulator_{key}", "regulator_key": key,
                "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "evidence_layer": "regulator_identity_and_regulatory_capacity",
                "support_kind": info["kind"], "cell_or_model": info["model"], "assay_or_perturbation": info["assay"],
                "observation": info["observation"], "effect_direction": "queued-pair direction not established except explicitly recorded limited associations",
                "primary_citation": info["general_primary"], "corroborating_citation": info["general_corr"], "route_or_module_relevance": info["relevance"],
                "target_pair_scope": "not evidence for unrelated queued exact pairs; no upstream relay inferred", "exportable": "false", "canonical_write_performed": "false",
                "limitations": "Regulator-level evidence does not establish SCI target-cell presence, exact queued-target direction, downstream activation or upstream relay. Profile, chromatin, cofactor, machinery, protein-regulation, RNA-processing and cross-species evidence is retained separately from canonical promoter-TF evidence.",
            })
            seen.add(key)
    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch026_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch026_regulator_register.tsv"
    summary_path = args.output_dir / "batch_026_evidence_review_summary.json"
    report_path = args.output_dir / "EVIDENCE_REVIEW_BATCH026.md"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    status_counts: dict[str, int] = {}
    for item in pairs:
        status_counts[item["exact_pair_status"]] = status_counts.get(item["exact_pair_status"], 0) + 1
    pair_keys = {(x["regulator_key"], x["target_symbol"], x["species_scope"], x["source_record_id"]) for x in pairs}
    noncanonical = sum(v for k, v in status_counts.items() if k.startswith("functional_noncanonical_"))
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_026", "source_set_ranks_reviewed": list(range(1, 26)),
        "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen), "unique_provenance_aware_pairs": len(pair_keys),
        "exact_pair_status_counts": status_counts, "regulator_register_rows": len(evidence), "strict_tf_promotion_candidate_rows": 0,
        "noncanonical_exact_candidate_rows": noncanonical, "exportable_pair_rows": 0, "canonical_writes_performed": False,
        "module22b_promotions_performed": False, "provenance_preserved": True,
        "limitations": [
            "TFLink/profile resources are search leads, not causal regulation.",
            "Exact-pair negatives are bounded search results, not global absence.",
            "WIZ-to-CWH43 and WIZ-to-DIP2C are exact human noncanonical chromatin-regulator candidates without SCI-cell validation or strict TF mechanism.",
            "IVNS1ABP-to-ACTR2 and CUL4A-to-ACVR1 are protein/complex associations and not transcriptional TF edges.",
            "No canonical or Module 22B write was performed.",
        ],
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path.write_text("\n".join([
        "# Evidence review: public TF batch 026", "", f"Reviewed {len(pairs)} exact regulator-target-species pairs across 25 TFLink source-set ranks.", "",
        f"- **{len(pairs)}** pairs were reviewed across **{len(seen)}** regulators.",
        f"- **{noncanonical}** exact noncanonical chromatin-regulator candidate rows were staged: human WIZ-to-CWH43 and WIZ-to-DIP2C.",
        f"- **{status_counts.get('binding_profile_only_not_promotable', 0)}** profile-only rows were retained without promotion.",
        f"- **{status_counts.get('target_protein_complex_association_not_transcriptional', 0)}** exact protein-complex row was routed outside TF evidence.",
        "- **0** strict TF promotion candidates, exportable rows, canonical writes, or Module 22B writes.", "",
        "All rows retain the original TFLink source record, raw symbol, species, target, graph-module mapping and local source snapshot. Regulator-level chromatin, cofactor, machinery, profile, protein-regulation, RNA-processing and cross-species evidence is recorded separately from exact canonical TF evidence.", "",
    ]) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
