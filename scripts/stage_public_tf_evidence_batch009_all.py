#!/usr/bin/env python3
"""Stage conservative evidence findings for all 100 Batch 009 pairs."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/"
    "current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_009/"
    "public_tf_evidence_collection_batch_009.tsv"
)
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
    "znf395": {"symbol": "ZNF395", "primary": "https://pubmed.ncbi.nlm.nih.gov/24086395/", "corr": "https://www.encodeproject.org/experiments/ENCSR462QZZ/", "kind": "primary_literature_regulator_level", "model": "human interferon-response and ENCODE K-562 ChIP-seq studies", "assay": "overexpression/knockdown, promoter-reporter, ChIP, and ENCODE ChIP-seq", "observation": "ZNF395 has human overexpression, knockdown, promoter-reporter, and ChIP evidence for interferon-related genes; the queued pairs have occupancy evidence but no target-specific causal validation.", "exclusions": "IFIT1, IFI44, IFI16, and other validated ZNF395 targets were not substituted for queued genes; no PRF1/perforin alias collision was accepted."},
    "hes4": {"symbol": "HES4", "primary": "https://pubmed.ncbi.nlm.nih.gov/38769389/", "corr": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11813838/", "kind": "primary_literature_regulator_level", "model": "human redox/tumor and HCC ChIP-seq studies", "assay": "RNAi/functional studies and ChIP-seq", "observation": "HES4 has human perturbation and ChIP-seq evidence at nonqueued genes and pathways; no queued target has matched functional validation.", "exclusions": "Xenopus Hedgehog/Hes4 pathway evidence was not transferred to human HES4 target regulation."},
    "dlx6": {"symbol": "DLX6", "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9846190/", "corr": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6522566", "kind": "primary_literature_regulator_level", "model": "human glioma and trophoblast ChIP/knockdown studies", "assay": "ChIP, knockdown, RNA expression, and GEO/ ReMap occupancy", "observation": "DLX6 has human ChIP/knockdown evidence for ATG7 and independent occupancy datasets; none validates the queued targets.", "exclusions": "DLX6-AS1, DLX1, and DLX2 evidence was excluded as lncRNA or paralog evidence; TP63→DLX6 is reverse direction."},
    "nfxl1": {"symbol": "NFXL1", "primary": "https://pubmed.ncbi.nlm.nih.gov/27053962/", "corr": "https://www.encodeproject.org/experiments/ENCSR417DKD/", "kind": "primary_literature_regulator_level", "model": "human characterization and MCF-7 ChIP-seq studies", "assay": "protein characterization and ENCODE ChIP-seq", "observation": "NFXL1 has human expression/localization characterization and an MCF-7 ChIP-seq experiment, but limited validated target-regulatory literature.", "exclusions": "NFX1 evidence was not transferred to the distinct NFXL1 protein."},
    "znf101": {"symbol": "ZNF101", "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11721306/", "corr": "https://pubmed.ncbi.nlm.nih.gov/39782688/", "kind": "primary_literature_regulator_level", "model": "human Huh-7 and mouse lipid-metabolism studies", "assay": "ZNF101 knockdown, APOB promoter reporter, and ortholog experiments", "observation": "ZNF101 has functional evidence at APOB-related lipid biology and human/mouse occupancy, but none of the queued human targets was validated.", "exclusions": "Mouse Zfp961/Apob evidence was treated as ortholog and different-target evidence, not as exact human queued-pair support."},
    "lcorl": {"symbol": "LCORL", "primary": "https://academic.oup.com/endo/article/165/12/bqae146/7848128", "corr": "https://chip-atlas.dbcls.jp/data/hg38/target/LCORL.1.html", "kind": "primary_literature_regulator_level", "model": "human LCORL occupancy and mouse Lcorl knockout studies", "assay": "ChIP-Atlas occupancy and knockout phenotype analysis", "observation": "LCORL has occupancy resources and mouse knockout growth/metabolic phenotypes; no exact queued human target was functionally validated.", "exclusions": "LCOR/ LCoR evidence was excluded as paralog evidence."},
    "zfp3": {"symbol": "ZFP3", "primary": "https://journals.plos.org/plospathogens/article?id=10.1371/journal.ppat.1010555", "corr": "https://www.encodeproject.org/experiments/ENCSR134QIE/", "kind": "primary_literature_regulator_level", "model": "human HEK293 ZFP3 ChIP-seq and HIV-LTR reporter studies", "assay": "DNA binding, ChIP-seq, and reporter repression", "observation": "ZFP3 has human binding/repression evidence at the HIV-1 LTR and occupancy resources, but not at the queued targets with perturbation.", "exclusions": "HIV-LTR repression and nonqueued targets were not transferred to queued genes."},
    "znf223": {"symbol": "ZNF223", "primary": "https://www.encodeproject.org/biosamples/ENCBS727PQJ/", "corr": "https://pubmed.ncbi.nlm.nih.gov/30445619/", "kind": "authoritative_binding_dataset_only", "model": "human eGFP-ZNF223 ENCODE material", "assay": "ENCODE binding material and GTRD-derived promoter occupancy", "observation": "ZNF223 has authoritative human binding-resource material and queued promoter occupancy leads, without target-specific perturbation evidence.", "exclusions": "Binding-resource material alone does not establish direction or causal regulation."},
    "tshz1": {"symbol": "TSHZ1", "primary": "https://www.encodeproject.org/experiments/ENCSR217WRC/", "corr": "https://www.encodeproject.org/experiments/ENCSR958JPH/", "kind": "authoritative_binding_dataset_only", "model": "human TSHZ1 ENCODE ChIP-seq studies", "assay": "ENCODE ChIP-seq and GTRD-derived promoter occupancy", "observation": "TSHZ1 has human ChIP-seq occupancy resources and queued promoter-binding leads, without exact target perturbation evidence.", "exclusions": "Mouse TSHZ1→Prokr2 evidence was not transferred to human queued targets."},
    "znf133": {"symbol": "ZNF133", "primary": "https://pubmed.ncbi.nlm.nih.gov/7649249/", "corr": "https://www.encodeproject.org/experiments/ENCSR283MWQ/", "kind": "primary_literature_regulator_level", "model": "human KRAB-domain reporter and ENCODE ChIP-seq studies", "assay": "KRAB reporter repression and ChIP-seq", "observation": "ZNF133 has regulator-level KRAB-domain repression and human occupancy evidence, but none of the queued targets has causal validation.", "exclusions": "Reporter repression and occupancy were not converted into target-specific direction."},
    "znf507": {"symbol": "ZNF507", "primary": "https://academic.oup.com/g3journal/article/12/3/jkac002/6509542", "corr": "https://pubmed.ncbi.nlm.nih.gov/35100360/", "kind": "primary_literature_regulator_level", "model": "human HEK293 CRISPR and ChIP/ENCODE studies", "assay": "CRISPR disruption, transcriptome analysis, and ChIP/occupancy", "observation": "ZNF507 has human DNA-binding and perturbation evidence; IGF2R is the only queued pair with a perturbation-associated expression signal, but the nearest peak was 26.007 kb away and directness was not demonstrated.", "exclusions": "The IGF2R perturbation signal is not treated as a direct target or promotion-ready edge; nonqueued targets were not transferred."},
    "ovol2": {"symbol": "OVOL2", "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4062651/", "corr": "https://pubmed.ncbi.nlm.nih.gov/24735879/", "kind": "primary_literature_regulator_level", "model": "mouse mammary epithelial Ovol2 deletion, ChIP-seq, ChIP validation, and rescue studies", "assay": "genome-wide ChIP-seq, ChIP validation, deletion, and DNA-binding-dependent isoform rescue", "observation": "Ovol2 has strong mouse regulator-level evidence. Cdh2 is an exact target with direct binding plus deletion/rescue evidence and is staged as the sole promotion candidate in this batch, pending SCI-cell context.", "exclusions": "Mouse mammary evidence is not silently transferred to SCI target-cell context; other Ovol2 targets remain occupancy-only."},
    "rfx7": {"symbol": "RFX7", "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8287911/", "corr": "https://pubmed.ncbi.nlm.nih.gov/34289795/", "kind": "primary_literature_regulator_level", "model": "human p53/stress-axis RFX7 perturbation and binding studies", "assay": "binding plus perturbation/integrated transcriptome analysis", "observation": "RFX7 has strong human binding and perturbation evidence at nonqueued stress-axis targets, but none of the queued targets was directly validated.", "exclusions": "Validated nonqueued RFX7 targets such as PDCD4, PIK3IP1, MXD4, and PNRC1 were not substituted."},
    "ovol3": {"symbol": "OVOL3", "primary": "https://www.ncbi.nlm.nih.gov/gene/728361", "corr": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/OVOL3_TARGET_GENES.html", "kind": "authoritative_binding_dataset_only", "model": "human OVOL3 annotation and GTRD-derived occupancy", "assay": "gene annotation and promoter occupancy", "observation": "OVOL3 has an identity annotation and occupancy leads but limited target-specific functional literature.", "exclusions": "OVOL1 and OVOL2 studies were excluded as paralog evidence."},
    "znf584": {"symbol": "ZNF584", "primary": "https://www.encodeproject.org/experiments/ENCSR149ZBI/", "corr": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE105327", "kind": "authoritative_binding_dataset_only", "model": "human K562 eGFP-ZNF584 ChIP-seq and ReMap aggregation", "assay": "ChIP-seq and ReMap occupancy", "observation": "ZNF584 has human ChIP-seq occupancy evidence, but no queued target-specific perturbation study was located.", "exclusions": "ADCYAP1 and CAP1 were absent from the checked target set; related gene-set names and ADGRB3-DT were not substituted."},
    "znf296": {"symbol": "ZNF296", "primary": "https://pubmed.ncbi.nlm.nih.gov/30389936/", "corr": "https://pubmed.ncbi.nlm.nih.gov/37488353/", "kind": "primary_literature_regulator_level", "model": "mouse Zfp296/Znf296 ESC NuRD and ChIP-seq studies", "assay": "knockout, ChIP-seq, ATAC-seq, and chromatin-complex studies", "observation": "Mouse Znf296 has regulator-level knockout, ChIP-seq, and chromatin evidence; none validates the four queued edges.", "exclusions": "Mouse regulator-level evidence does not establish any queued target direction or SCI-cell presence."},
    "znf16": {"symbol": "ZNF16", "primary": "https://pubmed.ncbi.nlm.nih.gov/41467516/", "corr": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF16_TARGET_GENES.html", "kind": "primary_literature_regulator_level", "model": "human ZNF16 depletion and rDNA/RNA programs", "assay": "depletion, viability, rDNA transcription, and RNA-seq", "observation": "ZNF16 depletion affects viability, rDNA transcription, and broad RNA programs; the queued occupancy leads lack target-specific causal validation.", "exclusions": "Reported nonqueued genes such as NRAS, BIRC3, and EGFR were not transferred; EPOR was not independently verified in the checked set."},
    "znf618": {"symbol": "ZNF618", "primary": "https://pubmed.ncbi.nlm.nih.gov/27129234/", "corr": "https://link.springer.com/article/10.1186/s40001-026-04429-2", "kind": "primary_literature_regulator_level", "model": "human UHRF2/5hmC chromatin and NPC studies", "assay": "chromatin biology, ChIP/occupancy, and perturbation", "observation": "ZNF618 has human chromatin-regulatory evidence and queued occupancy leads; ADORA2A appeared only as a SPECC1L-ADORA2A readthrough/near-match, not a standalone exact target.", "exclusions": "UHRF1 and other paralog evidence was excluded; the ADORA2A readthrough entry was not treated as canonical ADORA2A."},
    "znf524": {"symbol": "ZNF524", "primary": "https://pubmed.ncbi.nlm.nih.gov/38086788/", "corr": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE196661", "kind": "primary_literature_regulator_level", "model": "human telomeric DNA-binding and occupancy studies", "assay": "direct DNA binding, telomere integrity, and GEO occupancy", "observation": "ZNF524 has direct telomeric DNA-binding and integrity evidence, but not transcriptional regulation of queued targets.", "exclusions": "Telomere biology and nonqueued targets were not transferred to queued gene edges."},
    "znf558": {"symbol": "ZNF558", "primary": "https://pubmed.ncbi.nlm.nih.gov/34624206/", "corr": "https://www.encodeproject.org/experiments/ENCSR154YWK/", "kind": "primary_literature_regulator_level", "model": "human organoid, SPATA18, and ENCODE occupancy studies", "assay": "loss-of-function, organoid phenotype, and ChIP-seq", "observation": "ZNF558 has functional evidence at SPATA18 and human occupancy resources, but none of the queued targets was functionally validated.", "exclusions": "SPATA18 and other nonqueued targets were not substituted."},
    "irx2": {"symbol": "IRX2", "primary": "https://www.nature.com/articles/s41467-025-63070-5", "corr": "https://pubmed.ncbi.nlm.nih.gov/42266168/", "kind": "primary_literature_regulator_level", "model": "human keratinocyte perturbation and IRX2 interaction studies", "assay": "perturbation, transcript analysis, and protein interaction", "observation": "IRX2 has human perturbation and interaction evidence at nonqueued contexts; none of the four queued targets was directly validated.", "exclusions": "Other IRX-family factors and reverse-direction relationships were not transferred."},
    "znf486": {"symbol": "ZNF486", "primary": "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM1467732", "corr": "https://remap.univ-amu.fr/target_page/ZNF486%3A9606", "kind": "authoritative_binding_dataset_only", "model": "human ZNF486 ChIP-seq and ReMap occupancy", "assay": "ChIP-seq and ReMap", "observation": "ZNF486 has human binding-resource evidence and queued occupancy leads without exact target perturbation.", "exclusions": "Occupancy alone does not establish causal direction or SCI-cell engagement."},
    "arnt2": {"symbol": "ARNT2", "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13281552/", "corr": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ARNT2_TARGET_GENES.html", "kind": "primary_literature_regulator_level", "model": "human ARNT2 loss/gain-of-function and occupancy studies", "assay": "loss/gain-of-function, transcriptome, and ChIP/occupancy", "observation": "ARNT2 has human perturbation evidence and queued occupancy leads, but none of the four queued targets was directly established.", "exclusions": "Mouse Arnt2, ARNT, and GLI2/3 evidence was excluded as species, paralog, or target mismatch."},
    "rlf": {"symbol": "RLF", "primary": "https://remap.univ-amu.fr/target_page/RLF%3A9606", "corr": "https://pubmed.ncbi.nlm.nih.gov/30445619/", "kind": "authoritative_binding_dataset_only", "model": "human RLF ReMap and GTRD-derived occupancy", "assay": "ReMap/ChIP-seq occupancy", "observation": "RLF has human occupancy-resource evidence and queued binding leads, without exact target-specific perturbation.", "exclusions": "Occupancy-only evidence does not establish activation, repression, or upstream relay."},
    "znf34": {"symbol": "ZNF34", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/download_geneset.jsp?fileType=json&geneSetName=ZNF34_TARGET_GENES", "corr": "https://pubmed.ncbi.nlm.nih.gov/30445619/", "kind": "authoritative_binding_dataset_only", "model": "human ZNF34 GTRD-derived promoter occupancy", "assay": "GTRD-derived promoter occupancy", "observation": "ZNF34 has queued promoter-binding leads but no separate target-specific perturbation study was located.", "exclusions": "Binding-only set membership does not establish direction or target-cell relevance."},
}

OCCUPANCY_URL = {
    "znf395": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF395_TARGET_GENES.html", "hes4": "https://www.gsea-msigdb.org/gsea/msigdb/cards/HES4_TARGET_GENES.html", "dlx6": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/DLX6_TARGET_GENES.html", "nfxl1": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/NFXL1_TARGET_GENES.html", "znf101": "https://www.gsea-msigdb.org/gsea/msigdb/cards/ZNF101_TARGET_GENES.html", "lcorl": "https://www.gsea-msigdb.org/gsea/msigdb/cards/LCORL_TARGET_GENES.html", "zfp3": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZFP3_TARGET_GENES.html", "znf223": "https://www.gsea-msigdb.org/gsea/msigdb/cards/ZNF223_TARGET_GENES.html", "tshz1": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/TSHZ1_TARGET_GENES.html", "znf133": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF133_TARGET_GENES.html", "znf507": "https://www.gsea-msigdb.org/gsea/msigdb/cards/ZNF507_TARGET_GENES.html", "ovol2": "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/OVOL2_TARGET_GENES.html", "rfx7": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/RFX7_TARGET_GENES.html", "ovol3": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/OVOL3_TARGET_GENES.html", "znf584": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF584_TARGET_GENES.html", "znf296": "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/ZFP296_TARGET_GENES.html", "znf16": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF16_TARGET_GENES.html", "znf618": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF618_TARGET_GENES.html", "znf524": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF524_TARGET_GENES.html", "znf558": "https://www.gsea-msigdb.org/gsea/msigdb/cards/ZNF558_TARGET_GENES.html", "irx2": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/IRX2_TARGET_GENES.html", "znf486": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF486_TARGET_GENES.html", "arnt2": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ARNT2_TARGET_GENES.html", "rlf": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/RLF_TARGET_GENES.html", "znf34": "https://www.gsea-msigdb.org/gsea/msigdb/human/download_geneset.jsp?fileType=json&geneSetName=ZNF34_TARGET_GENES",
}

TARGET_CORR = {
    "lcorl": "https://chip-atlas.dbcls.jp/data/hg38/target/LCORL.1.html", "zfp3": "https://chip-atlas.dbcls.jp/data/hg38/target/ZFP3.1.html", "znf223": "https://chip-atlas.dbcls.jp/data/hg38/target/ZNF223.1.html", "tshz1": "https://chip-atlas.dbcls.jp/data/hg38/target/TSHZ1.1.html", "znf133": "https://www.encodeproject.org/experiments/ENCSR283MWQ/", "znf395": "https://www.encodeproject.org/experiments/ENCSR462QZZ/",
}

STATUS_OVERRIDES = {
    ("znf507", "igf2r"): "perturbation_signal_directness_unproven_not_promotable",
    ("ovol2", "cdh2"): "functional_direct_binding_promotion_candidate",
    ("znf584", "adcyap1"): "no_exact_pair_support_found_in_bounded_search",
    ("znf584", "cap1"): "no_exact_pair_support_found_in_bounded_search",
    ("znf618", "adora2a"): "readthrough_near_match_not_promotable",
    ("znf16", "epor"): "no_exact_pair_support_found_in_bounded_search",
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


def pair_fields(row: dict[str, str], key: str, info: dict[str, str], status: str) -> dict[str, str]:
    target_key = row["target_symbol"].lower()
    occupancy = OCCUPANCY_URL[key]
    corr = TARGET_CORR.get(key, "")
    if status == "functional_direct_binding_promotion_candidate":
        cell = "present_in_mouse_mammary_model_not_SCI_target_cell"
        binding = "direct_ChIP_and_orthogonal_ChIP_validation"
        downstream = "Cdh2_increased_after_Ovol2_deletion_and_DNA_binding_dependent_rescue"
        disposition = "promotion_candidate_pending_SCI_target_cell_context"
        primary = info["primary"]
        corr = info["corr"]
        notes = "Ovol2 deletion increased Cdh2/N-cadherin, genome-wide Ovol2 ChIP-seq and ChIP validation identified Cdh2 binding, and rescue required intact DNA binding. This is the strongest exact pair in the batch, but the evidence is from mouse mammary models rather than the SCI target cell; stage for review, do not materialize."
    elif status == "perturbation_signal_directness_unproven_not_promotable":
        cell = "human_HEK293_model_not_SCI_target_cell"
        binding = "authoritative_occupancy_plus_nearest_peak_not_direct_promoter_validation"
        downstream = "IGF2R_expression_changed_after_ZNF507_CRISPR_disruption"
        disposition = "retain_perturbation_signal_as_nonpromotable_search_lead"
        primary = info["primary"]
        corr = info["corr"]
        notes = "ZNF507 CRISPR disruption changed IGF2R expression (log2FC +0.416262343; adjusted P 2.75e-7), but the nearest ZNF507 peak was 26.007 kb away and the authors did not establish direct regulation; do not promote."
    elif status == "readthrough_near_match_not_promotable":
        cell = "not_established_for_exact_pair"
        binding = "readthrough_entry_not_canonical_target_binding"
        downstream = "not_found_for_exact_pair"
        disposition = "retain_near_match_exclusion_only"
        primary = occupancy
        corr = ""
        notes = "The checked ZNF618 resource returned SPECC1L-ADORA2A/readthrough-style evidence rather than a standalone ADORA2A target; this near match is excluded from the exact pair."
    elif status == "no_exact_pair_support_found_in_bounded_search":
        cell = "not_established_for_exact_pair"
        binding = "not_verified_for_exact_pair"
        downstream = "not_found_for_exact_pair"
        disposition = "retain_database_candidate_as_search_lead_only"
        primary = occupancy
        corr = ""
        notes = "The target was not independently verified as an exact functional or target-level binding relationship in the bounded primary-literature and authoritative-dataset search; this is not a global absence claim."
    else:
        cell = "not_established_for_exact_pair"
        binding = "authoritative_occupancy_dataset_lead"
        downstream = "not_found_for_exact_pair"
        disposition = "retain_database_candidate_as_search_lead_only"
        primary = occupancy
        notes = "The GTRD-derived set supports promoter-occupancy membership for this exact pair, but no matched perturbation/target-expression validation was located; retain as a non-promotable binding lead."
    if key == "znf395" and target_key == "epor":
        notes += " ENCODE ranked-peak support was lower-confidence than the conservative pooled overlap."
    return {
        "review_id": f"public_tf_evidence_batch009_pair_{int(row['batch_rank']):02d}_{row['target_rank']}", "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key,
        "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "source_registry": row["source_registry"], "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"], "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"], "exact_pair_search_url": search_url(info["symbol"], row["target_symbol"], row["species_scope"]), "exact_pair_status": status, "regulator_general_evidence_status": "supported_general_regulator_evidence", "target_cell_presence_status": cell, "binding_or_association_status": binding, "downstream_expression_or_perturbation_status": downstream, "downstream_activation_status": "not_established_for_SCI_target_cell", "upstream_relay_status": "not_tested_for_exact_pair", "disposition": disposition, "primary_citation": primary, "corroborating_citation": corr, "near_match_exclusions": info["exclusions"], "review_notes": notes + " " + info["observation"], "exportable": "false", "canonical_write_performed": "false",
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
        if key not in REGULATORS or key not in OCCUPANCY_URL:
            raise SystemExit(f"missing evidence map for {key}")
        status = STATUS_OVERRIDES.get((key, row["target_symbol"].lower()), "binding_dataset_only_not_promotable")
        info = REGULATORS[key]
        pairs.append(pair_fields(row, key, info, status))
        if key not in seen:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch009_regulator_{key}", "regulator_key": key, "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "evidence_layer": "regulator_identity_and_regulatory_capacity", "support_kind": info["kind"], "cell_or_model": info["model"], "assay_or_perturbation": info["assay"], "observation": info["observation"], "effect_direction": "queued-pair direction not established except staged Ovol2-Cdh2 candidate", "primary_citation": info["primary"], "corroborating_citation": info["corr"], "route_or_module_relevance": "regulator-level evidence only", "target_pair_scope": "not evidence for unrelated queued exact pairs; no upstream relay inferred", "exportable": "false", "canonical_write_performed": "false", "limitations": "Regulator-level evidence does not by itself establish target-cell presence in SCI, downstream activation, exact direction, or an upstream relay. The Ovol2-Cdh2 pair is retained separately as a promotion candidate pending SCI-cell context.",
            })
        seen.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch009_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch009_regulator_register.tsv"
    summary_path = args.output_dir / "batch_009_evidence_review_summary.json"
    report_path = args.output_dir / "EVIDENCE_REVIEW_BATCH009.md"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    status_counts: dict[str, int] = {}
    for row in pairs:
        status_counts[row["exact_pair_status"]] = status_counts.get(row["exact_pair_status"], 0) + 1
    kind_counts: dict[str, int] = {}
    for row in evidence:
        kind_counts[row["support_kind"]] = kind_counts.get(row["support_kind"], 0) + 1
    pair_keys = {(row["regulator_key"], row["target_symbol"], row["species_scope"], row["source_record_id"]) for row in pairs}
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_009", "source_set_ranks_reviewed": list(range(1, 26)), "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen), "unique_provenance_aware_pairs": len(pair_keys), "exact_pair_status_counts": status_counts, "regulator_register_rows": len(evidence), "regulator_support_kind_counts": kind_counts, "exact_pair_support_rows": status_counts.get("functional_direct_binding_promotion_candidate", 0), "promotion_candidate_rows": status_counts.get("functional_direct_binding_promotion_candidate", 0), "partial_or_near_match_rows": status_counts.get("perturbation_signal_directness_unproven_not_promotable", 0) + status_counts.get("readthrough_near_match_not_promotable", 0), "binding_dataset_only_not_promotable_rows": status_counts.get("binding_dataset_only_not_promotable", 0), "bounded_negative_rows": status_counts.get("no_exact_pair_support_found_in_bounded_search", 0), "exportable_pair_rows": 0, "canonical_writes_performed": False, "module22b_promotions_performed": False, "provenance_preserved": True, "limitations": ["GTRD/TFLink/MSigDB membership is binding or database evidence, not causal regulation.", "No-exact-support and bounded negatives are restricted to the searches recorded in this batch and are not global absence claims.", "The Ovol2-Cdh2 evidence is strong but from mouse mammary models; SCI target-cell context is not established, so it remains staging-only.", "The ZNF507-IGF2R expression change has unresolved directness and is not promotion-ready."], "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path.write_text(
        "# Evidence review: public TF batch 009\n\n"
        "Reviewed all 25 selected TFLink source sets and 100 exact regulator-target-species pairs.\n\n"
        f"- **{len(pairs)} / 100** pairs were reviewed.\n"
        f"- **{summary['exact_pair_support_rows']}** exact pair was retained as a promotion candidate pending SCI-cell context.\n"
        f"- **{summary['binding_dataset_only_not_promotable_rows']}** pairs were retained as binding/association-only leads.\n"
        f"- **{summary['bounded_negative_rows']}** pairs were bounded negatives for exact target-level support; **{summary['partial_or_near_match_rows']}** were non-promotable partial/near-match records.\n"
        f"- **{len(evidence)}** regulator-level records were retained separately.\n"
        "- **0** rows are exportable; no canonical or Module 22B writes were performed.\n\n"
        "The Ovol2-Cdh2 result has direct binding plus deletion/rescue evidence in a mouse mammary model, but target-cell context for SCI is not established. ZNF507-IGF2R has a perturbation-associated expression change, but directness is unresolved. All other exact rows are occupancy-only, near-match, or bounded-search records.\n\n"
        "`no_exact_pair_support_found_in_bounded_search` is a bounded-search result, not a claim that no evidence exists anywhere.\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
