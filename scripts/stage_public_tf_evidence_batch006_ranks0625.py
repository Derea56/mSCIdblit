#!/usr/bin/env python3
"""Stage conservative evidence findings for public-TF batch 006 ranks 6-25."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/"
    "current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_006/"
    "public_tf_evidence_collection_batch_006.tsv"
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

# symbol, species, primary, corroboration, model, assay, observation, exclusions, support kind
REGULATORS = {
    "hand1": (
        "HAND1", "mouse", "https://www.sciencedirect.com/science/article/pii/S002192582079201X",
        "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/HAND1_TARGET_GENES",
        "mouse cardiac and developmental models", "DNA binding, promoter assays, and developmental perturbation studies",
        "HAND1 has regulator-level evidence and a mouse GTRD-derived occupancy set containing the queued Actr2, Adcyap1r1, Adm, and Agrn genes, but no queued perturbation/target-expression validation was found.",
        "Target-set membership is occupancy-only; nonqueued HAND1 developmental targets and paralog evidence were not transferred.",
        "authoritative_binding_dataset_only",
    ),
    "zbtb21": (
        "ZBTB21", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10359638/",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC13088348/", "human cell-line and cancer models",
        "ChIP-seq/occupancy, chromatin-interaction analysis, and perturbational cancer studies",
        "ZBTB21 has experimental chromatin occupancy and transcriptional-regulatory evidence at nonqueued loci, but no queued ADO/AXL/BDKRB2/CCL4 relationship was validated.",
        "Binding, chromatin-association, motif, and nonqueued target evidence were not transferred to queued edges.",
        "primary_literature_regulator_level",
    ),
    "zbed5": (
        "ZBED5", "human", "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZBED5_TARGET_GENES.html",
        "", "human GTRD-derived target-set resource", "ChIP-seq harmonization target-set membership",
        "The human ZBED5 GTRD-derived target set contains queued ADGRB3, ALCAM, and APLP2, but no matched perturbation or orthogonal target-expression validation was found.",
        "Target-set membership is binding-only; no exact ADAM22 functional evidence was located and no target-set lead was promoted.",
        "authoritative_binding_dataset_only",
    ),
    "lhx6": (
        "LHX6", "mouse", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8930537/", "",
        "mouse embryonic maxillary-arch developmental models", "transcriptional profiling and LHX6/LHX8 ChIP-seq",
        "LHX6 has regulator-level developmental target evidence from transcriptional profiling and ChIP-seq, but no queued Adam23/Adam9/Ambn/Angpt4 relationship was validated.",
        "LHX8 paralog evidence, candidate target lists, and developmental co-expression were not transferred to queued edges.",
        "primary_literature_regulator_level",
    ),
    "znf134": (
        "ZNF134", "human", "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF134_TARGET_GENES",
        "https://remap.univ-amu.fr/target_page/ZNF134%3A9606", "human GTRD/ReMap occupancy resources",
        "GTRD-derived promoter target set and ReMap ChIP-seq occupancy",
        "The ZNF134 target set contains queued ACVR1C, AMFR, and APLP1, but these are occupancy-only database leads without matched perturbation or orthogonal validation.",
        "No queued ADGRB3 functional evidence was located; occupancy-only and predicted regulatory records were not promoted.",
        "authoritative_binding_dataset_only",
    ),
    "znf184": (
        "ZNF184", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12057860/",
        "https://www.encodeproject.org/experiments/ENCSR621ATC/", "human SH-SY5Y/HEK293 and K562 models",
        "overexpression/siRNA, ChIP, promoter mutagenesis, and ENCODE ChIP-seq",
        "ZNF184 directly represses nonqueued ILF3 through promoter occupancy and perturbation, and its GTRD-derived target set contains queued ADA, ADGRE5, ADO, and AGRN; no queued functional validation was found.",
        "The ILF3 edge is nonqueued and was not transferred; queued target-set membership remains binding-only.",
        "primary_literature_regulator_level",
    ),
    "ahrr": (
        "AHRR", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2157559/",
        "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/AHRR_TARGET_GENES.html", "human tumor and occupancy models",
        "siRNA perturbation, tumor phenotype assays, and GTRD-derived promoter occupancy",
        "AHRR has human regulator-level loss-of-function phenotype evidence and an occupancy lead for queued ACTR2, but no queued ADGRB3/ADIPOQ/ALCAM functional relationship was found.",
        "AHRR occupancy at ACTR2 is binding-only; tumor phenotype and AHR-pathway evidence were not transferred to queued edges.",
        "primary_literature_regulator_level",
    ),
    "zfp91": (
        "ZFP91", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8972091/",
        "https://www.gsea-msigdb.org/gsea/msigdb/cards/ZFP91_TARGET_GENES", "human T-cell-lymphoma models",
        "ChIP-seq, knockout, RNA-seq/PRO-seq, and luciferase validation",
        "ZFP91 directly activates nonqueued MAP3K12, FZD2, HDAC5, GHDC, and IKBKE in resistant T-cell lymphoma, while the GTRD-derived set provides an occupancy lead for queued ACVR1; other queued edges were not validated.",
        "The validated targets are nonqueued; ACVR1 is occupancy-only and was not promoted.",
        "primary_literature_regulator_level",
    ),
    "znf652": (
        "Zfp652", "mouse", "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/ZFP652_TARGET_GENES.html",
        "", "mouse GTRD-derived target-set resource", "ChIP-seq harmonization target-set membership",
        "The mouse Zfp652 target set contains queued Acvr1, Acvr1c, and Adgrl3, but no matched perturbation or orthogonal target-expression validation was found.",
        "Target-set membership is binding-only; no queued Adam17 functional evidence was located and no edge was promoted.",
        "authoritative_binding_dataset_only",
    ),
    "znf597": (
        "ZNF597", "human", "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF597_TARGET_GENES.html",
        "", "human GTRD-derived target-set resource", "ChIP-seq harmonization target-set membership",
        "The ZNF597 target set contains queued CCL22, but no matched perturbation or orthogonal target-expression validation was found for queued BCL2/CCL22/CCL5/CCR1.",
        "Occupancy-only CCL22 membership and nonqueued target-set genes were not promoted.",
        "authoritative_binding_dataset_only",
    ),
    "znf30": (
        "ZNF30", "human", "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF30_TARGET_GENES.html",
        "", "human GTRD-derived target-set resource", "ChIP-seq harmonization target-set membership",
        "The ZNF30 target set contains queued ACVRL1, ANG, and APLP1, but no matched perturbation or orthogonal validation was found; ADGRL1 lacked a qualifying exact lead.",
        "Target-set membership is binding-only and was not treated as a functional receptor/ligand edge.",
        "authoritative_binding_dataset_only",
    ),
    "zim3": (
        "ZIM3", "human", "https://www.gsea-msigdb.org/gsea/msigdb/cards/ZIM3_TARGET_GENES",
        "https://remap2020.univ-amu.fr/target_page/ZIM3%3A9606", "human HEK293/HEK293T occupancy models",
        "ChIP-exo/ChIP-seq and GTRD/ReMap occupancy resources",
        "ZIM3 occupancy resources contain queued ADGRL2 and ANXA2, but no queued perturbation or target-expression validation was located for ADGRL2/ANG/ANXA2/BMP6.",
        "Occupancy-only records and nonqueued target-set genes were not promoted.",
        "authoritative_binding_dataset_only",
    ),
    "zbtb18": (
        "ZBTB18", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10724217/",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC9821869/", "human induced-neuron and cancer models",
        "CRISPR knockout, RNA-seq, ATAC-seq/ChIP association, promoter ChIP-qPCR, and expression assays",
        "ZBTB18 has direct regulator-level evidence at nonqueued neuronal/cancer targets, while its GTRD-derived set contains queued AXL; no queued functional target validation was found.",
        "The nonqueued TGFBR2 and neuronal target evidence was not transferred; AXL target-set membership is binding-only.",
        "primary_literature_regulator_level",
    ),
    "znf319": (
        "Zfp319", "mouse", "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/ZFP319_TARGET_GENES",
        "https://remap.univ-amu.fr/target_page/ZNF319%3A9606", "mouse GTRD-derived and human ReMap occupancy resources",
        "ChIP-seq harmonization target-set and ReMap occupancy resources",
        "The mouse Zfp319 target set contains queued Adam17, Anxa1, and Axl, but no matched perturbation or orthogonal validation was found for the queued mouse pairs.",
        "The human ReMap record was not used to infer mouse function; occupancy-only target-set membership was not promoted.",
        "authoritative_binding_dataset_only",
    ),
    "znf596": (
        "ZNF596", "human", "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF596_TARGET_GENES.html",
        "", "human GTRD-derived target-set resource", "ChIP-seq harmonization target-set membership",
        "The ZNF596 target set contains queued ACVR1, ANXA2, BMP7, and CCKBR, but no matched perturbation or orthogonal target-expression validation was found.",
        "Target-set membership is binding-only; no exact functional edge was promoted.",
        "authoritative_binding_dataset_only",
    ),
    "znf407": (
        "ZNF407", "human", "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF407_TARGET_GENES.html",
        "https://www.encodeproject.org/experiments/ENCSR005WGY/", "human HepG2/ENCODE occupancy models",
        "ENCODE ChIP-seq and GTRD-derived promoter target-set membership",
        "ZNF407 occupancy resources contain queued ANG, CCN1, and COL16A1, but no matched perturbation or orthogonal target-expression validation was found.",
        "The target-set/ENCODE records establish occupancy leads only; no queued ADO functional evidence was located.",
        "authoritative_binding_dataset_only",
    ),
    "znf394": (
        "ZNF394", "human", "https://www.gsea-msigdb.org/gsea/msigdb/cards/ZNF394_TARGET_GENES.html",
        "https://www.encodeproject.org/experiments/ENCSR125DNC/", "human HEK293/ENCODE occupancy models",
        "GTRD-derived target-set membership and ENCODE ChIP-seq",
        "The ZNF394 target set contains queued ADA, ADAM10, and ARTN, but no matched perturbation or orthogonal target-expression validation was found; ADGRB3 lacked an exact lead.",
        "Occupancy-only target-set evidence was not promoted to a functional edge.",
        "authoritative_binding_dataset_only",
    ),
    "znf391": (
        "ZNF391", "human", "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF391_TARGET_GENES.html",
        "", "human GTRD-derived target-set resource", "ChIP-seq harmonization target-set membership",
        "The ZNF391 target set provides a binding-resource lead, but no queued ADGRE5/CADM4/CCN1/COL1A1 relationship was validated by perturbation and target expression.",
        "Target-set membership, co-expression, and nonqueued targets were not promoted.",
        "authoritative_binding_dataset_only",
    ),
    "fev": (
        "FEV", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3219954/",
        "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/FEV_TARGET_GENES.html", "human and mouse endocrine/neural models",
        "promoter ChIP, knockout expression, and reporter assays plus GTRD-derived target set",
        "FEV/Pet1 has direct regulator-level evidence at nonqueued endocrine genes, and its GTRD-derived target set contains queued ADAM17; no queued perturbation validation was found.",
        "The nonqueued insulin/Gck/Slc2a2 evidence was not transferred; ADAM17 target-set membership is binding-only.",
        "primary_literature_regulator_level",
    ),
    "znf549": (
        "ZNF549", "human", "https://www.gsea-msigdb.org/gsea/msigdb/cards/ZNF549_TARGET_GENES.html",
        "", "human GTRD-derived target-set resource", "ChIP-seq harmonization target-set membership",
        "The ZNF549 target set contains queued ADGRB1, but no matched perturbation or orthogonal target-expression validation was found for ADGRB1/ADORA2A/ANXA2/APLP1.",
        "The ADORA2A fusion/readthrough listing was not treated as ADORA2A evidence; target-set membership was not promoted.",
        "authoritative_binding_dataset_only",
    ),
}

EXACT_OCCUPANCY_ONLY = {
    ("hand1", "Actr2"): "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/HAND1_TARGET_GENES",
    ("hand1", "Adcyap1r1"): "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/HAND1_TARGET_GENES",
    ("hand1", "Adm"): "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/HAND1_TARGET_GENES",
    ("hand1", "Agrn"): "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/HAND1_TARGET_GENES",
    ("zbed5", "ADGRB3"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZBED5_TARGET_GENES.html",
    ("zbed5", "ALCAM"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZBED5_TARGET_GENES.html",
    ("zbed5", "APLP2"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZBED5_TARGET_GENES.html",
    ("foxn3", "ACTR2"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/FOXN3_TARGET_GENES",
    ("foxn3", "ADA"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/FOXN3_TARGET_GENES",
    ("foxn3", "ADAM17"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/FOXN3_TARGET_GENES",
    ("foxn3", "ADAM23"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/FOXN3_TARGET_GENES",
    ("znf134", "ACVR1C"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF134_TARGET_GENES",
    ("znf134", "AMFR"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF134_TARGET_GENES",
    ("znf134", "APLP1"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF134_TARGET_GENES",
    ("znf184", "ADA"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF184_TARGET_GENES",
    ("znf184", "ADGRE5"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF184_TARGET_GENES",
    ("znf184", "ADO"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF184_TARGET_GENES",
    ("znf184", "AGRN"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF184_TARGET_GENES",
    ("ahrr", "ACTR2"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/AHRR_TARGET_GENES.html",
    ("zfp91", "ACVR1"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZFP91_TARGET_GENES",
    ("znf652", "Acvr1"): "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/ZFP652_TARGET_GENES.html",
    ("znf652", "Acvr1c"): "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/ZFP652_TARGET_GENES.html",
    ("znf652", "Adgrl3"): "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/ZFP652_TARGET_GENES.html",
    ("znf597", "CCL22"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF597_TARGET_GENES.html",
    ("znf30", "ACVRL1"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF30_TARGET_GENES.html",
    ("znf30", "ANG"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF30_TARGET_GENES.html",
    ("znf30", "APLP1"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF30_TARGET_GENES.html",
    ("zim3", "ADGRL2"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZIM3_TARGET_GENES",
    ("zim3", "ANXA2"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZIM3_TARGET_GENES",
    ("zbtb18", "AXL"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZBTB18_TARGET_GENES",
    ("znf319", "Adam17"): "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/ZFP319_TARGET_GENES",
    ("znf319", "Anxa1"): "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/ZFP319_TARGET_GENES",
    ("znf319", "Axl"): "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/ZFP319_TARGET_GENES",
    ("znf596", "ACVR1"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF596_TARGET_GENES.html",
    ("znf596", "ANXA2"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF596_TARGET_GENES.html",
    ("znf596", "BMP7"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF596_TARGET_GENES.html",
    ("znf596", "CCKBR"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF596_TARGET_GENES.html",
    ("znf407", "ANG"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF407_TARGET_GENES.html",
    ("znf407", "CCN1"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF407_TARGET_GENES.html",
    ("znf407", "COL16A1"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF407_TARGET_GENES.html",
    ("znf394", "ADA"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF394_TARGET_GENES.html",
    ("znf394", "ADAM10"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF394_TARGET_GENES.html",
    ("znf394", "ARTN"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF394_TARGET_GENES.html",
    ("fev", "ADAM17"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/FEV_TARGET_GENES.html",
    ("znf549", "ADGRB1"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF549_TARGET_GENES.html",
    ("znf318", "ADGRL1"): "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF318_TARGET_GENES.html",
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_BATCH.parent)
    args = parser.parse_args()
    rows = [row for row in read_tsv(args.batch) if 6 <= int(row["batch_rank"]) <= 25]
    if len(rows) != 80:
        raise SystemExit(f"expected 80 rows for ranks 6-25, found {len(rows)}")

    pairs: list[dict[str, str]] = []
    evidence: list[dict[str, str]] = []
    seen_keys: set[str] = set()
    for i, row in enumerate(rows, 1):
        key = row["regulator_key"]
        if key not in REGULATORS:
            raise SystemExit(f"missing evidence map for {key}")
        symbol, species, primary, corr, model, assay, observation, exclusions, support_kind = REGULATORS[key]
        exact_lead = EXACT_OCCUPANCY_ONLY.get((key, row["target_symbol"]))
        if exact_lead:
            exact_status = "binding_dataset_only_not_promotable"
            binding_status = "authoritative_occupancy_dataset_lead"
            expression_status = "not_found_for_exact_pair"
            pair_primary = exact_lead
            pair_notes = "An authoritative GTRD-derived target-set record indicates regulator occupancy at this exact gene, but no matched perturbation or orthogonal validation was located; do not promote."
        else:
            exact_status = "no_exact_pair_support_found_in_bounded_search"
            binding_status = "not_found_for_exact_pair"
            expression_status = "not_found_for_exact_pair"
            pair_primary = ""
            pair_notes = "No qualifying exact regulator-target assay was located in the bounded search."
        general_status = "supported_authoritative_binding_dataset_only" if support_kind == "authoritative_binding_dataset_only" else ("supported_general_regulator_evidence" if primary else "not_found_in_bounded_search")
        pairs.append({
            "review_id": f"public_tf_evidence_batch006_pair_{int(row['batch_rank']):02d}_{i:02d}",
            "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key,
            "regulator_symbol": symbol, "species_scope": row["species_scope"], "source_registry": row["source_registry"],
            "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"],
            "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": search_url(symbol, row["target_symbol"], row["species_scope"]), "exact_pair_status": exact_status,
            "regulator_general_evidence_status": general_status, "target_cell_presence_status": "not_established_for_exact_pair",
            "binding_or_association_status": binding_status, "downstream_expression_or_perturbation_status": expression_status,
            "downstream_activation_status": "not_assessed", "upstream_relay_status": "not_tested_for_exact_pair",
            "disposition": "retain_database_candidate_as_search_lead_only", "primary_citation": pair_primary,
            "corroborating_citation": "", "near_match_exclusions": exclusions,
            "review_notes": pair_notes + " Regulator-level references are stored separately and are not evidence for this exact queued pair. " + observation,
            "exportable": "false", "canonical_write_performed": "false",
        })
        if key not in seen_keys:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch006_regulator_{key}", "regulator_key": key,
                "regulator_symbol": symbol, "species_scope": species, "evidence_layer": "regulator_identity_and_regulatory_capacity",
                "support_kind": support_kind, "cell_or_model": model, "assay_or_perturbation": assay,
                "observation": observation, "effect_direction": "queued-pair direction not established", "primary_citation": primary,
                "corroborating_citation": corr, "route_or_module_relevance": "regulator-level evidence only" if primary else "regulator-level evidence not established",
                "target_pair_scope": "not evidence for queued exact pairs; no Module 22B edge or upstream relay inferred",
                "exportable": "false", "canonical_write_performed": "false",
                "limitations": "Regulator-level evidence does not establish the queued target relationship, target-cell presence in SCI, downstream activation, or upstream relay.",
            })
        seen_keys.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch006_ranks0625_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch006_ranks0625_regulator_register.tsv"
    summary_path = args.output_dir / "batch_006_ranks0625_evidence_review_summary.json"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    occupancy_rows = sum(row["exact_pair_status"] == "binding_dataset_only_not_promotable" for row in pairs)
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_006", "source_set_ranks_reviewed": list(range(6, 26)),
        "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen_keys), "exact_pair_support_rows": 0,
        "binding_dataset_only_not_promotable_rows": occupancy_rows, "partial_or_near_match_rows": occupancy_rows,
        "general_regulator_evidence_rows": len(evidence), "exportable_pair_rows": 0,
        "canonical_writes_performed": False, "module22b_promotions_performed": False, "provenance_preserved": True,
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
        "decision": "Retain all 80 pairs as database-attributed search leads; exact occupancy-only leads remain non-promotable without matched perturbation or orthogonal validation.",
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
