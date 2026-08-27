#!/usr/bin/env python3
"""Stage the first bounded public-TF evidence review.

This pass deliberately separates regulator-level evidence from exact
regulator-target evidence.  A database regulon membership is retained as a
search lead, but it is never converted into a supported TF-target edge by
itself. The first ten source sets in evidence batch 001 were reviewed with
bounded primary-literature searches.  The result is staging-only: no
canonical TF role, regulon membership, Module 22B edge, or route relay is
written here.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/"
    "current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_001/"
    "public_tf_evidence_collection_batch_001.tsv"
)
DEFAULT_OUTPUT = DEFAULT_BATCH.parent

PAIR_FIELDS = [
    "review_id", "batch_id", "batch_rank", "regulator_key", "regulator_symbol",
    "species_scope", "source_registry", "source_record_id", "raw_tf_symbol",
    "target_symbol", "target_graph_modules", "candidate_membership_status",
    "exact_pair_search_url", "exact_pair_status", "regulator_general_evidence_status",
    "target_cell_presence_status", "binding_or_association_status",
    "downstream_expression_or_perturbation_status", "downstream_activation_status",
    "upstream_relay_status",
    "disposition", "primary_citation", "corroborating_citation",
    "near_match_exclusions", "review_notes", "exportable", "canonical_write_performed",
]

EVIDENCE_FIELDS = [
    "evidence_id", "regulator_key", "regulator_symbol", "species_scope", "evidence_layer",
    "support_kind", "cell_or_model", "assay_or_perturbation", "observation",
    "effect_direction", "primary_citation", "corroborating_citation",
    "route_or_module_relevance", "target_pair_scope", "exportable",
    "canonical_write_performed", "limitations",
]


REGULATOR_EVIDENCE = {
    "ebf2": {
        "symbol": "Ebf2",
        "species": "mouse",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5411707/",
        "corroborating": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3622114/",
        "model": "mouse brown adipocytes / adipose tissue",
        "assay": "ChIP-seq with RNA-seq and functional target validation",
        "observation": "EBF2 is treated as a transcriptional regulator with chromatin binding and a regulated brown-adipocyte gene program; this supports regulator capacity, not any of the four queued A2M/ABCA1/ACKR3/ACTR2 pairs.",
        "direction": "context-dependent regulatory program; exact queued-pair direction not established",
        "role": "regulator-level identity and regulatory-capacity evidence only",
        "near": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12705753/ (Osr1-Ackr3, not Ebf2); https://pmc.ncbi.nlm.nih.gov/articles/PMC2951399/ (miR-33-Abca1, not Ebf2)",
    },
    "isx": {
        "symbol": "ISX",
        "species": "mouse",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3610974/",
        "corroborating": "https://pubmed.ncbi.nlm.nih.gov/20061533/",
        "model": "intestinal epithelial / carotenoid metabolism models",
        "assay": "DNA-binding, reporter, ChIP/occupancy and perturbation-based transcriptional assays",
        "observation": "ISX is supported as a sequence-specific transcriptional regulator of an intestinal gene program, including Bcmo1 and SR-BI-related regulation; the queued A2M/ABCA1/ACKR3/ACKR4 pairs are not supported by this evidence.",
        "direction": "reported repressive/activating program effects depend on target and context; queued-pair direction not established",
        "role": "regulator-level identity and regulatory-capacity evidence only",
        "near": "https://pubmed.ncbi.nlm.nih.gov/20061533/ (ISX-SR-BI, not queued targets); https://pmc.ncbi.nlm.nih.gov/articles/PMC2951399/ (miR-33-Abca1, not ISX)",
    },
    "zbtb48": {
        "symbol": "ZBTB48",
        "species": "human",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5452029/",
        "corroborating": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11649694/",
        "model": "human cell models",
        "assay": "RNA-seq, ChIP-seq, proteomics, promoter/chromatin assays",
        "observation": "ZBTB48 is supported as a DNA-binding transcriptional regulator with direct regulatory evidence for genes such as MTFP1 and CIITA; this does not establish the queued ACKR2/ACKR3/ACTR2/ACVR1 pairs.",
        "direction": "activating or priming effects are target- and context-specific; queued-pair direction not established",
        "role": "regulator-level identity and regulatory-capacity evidence only",
        "near": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4015442/ (ZBTB7A/HEY1/EGR1-ACVR1, not ZBTB48); https://pmc.ncbi.nlm.nih.gov/articles/PMC7802253/ (miR-365-ACVR1, not ZBTB48)",
    },
    "tcf7l1": {
        "symbol": "TCF7L1",
        "species": "human",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6265397/",
        "corroborating": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9984534/",
        "model": "vertebrate developmental and mouse embryonic stem-cell models",
        "assay": "promoter/transcriptional assays, chromatin occupancy and perturbation studies",
        "observation": "TCF7L1 is supported as a transcriptional regulator with direct target relationships including KLF4 and developmental regulatory programs; this does not establish the queued A2M/ACKR2/ACTR2/ACVR1 pairs.",
        "direction": "repressive or activating effects depend on Wnt/context and target; queued-pair direction not established",
        "role": "regulator-level identity and regulatory-capacity evidence only",
        "near": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4917863/ (TCF7L1-EPHB3, not queued targets); https://pmc.ncbi.nlm.nih.gov/articles/PMC4920148/ (ACVR1 regulation by other factors, not TCF7L1)",
    },
    "grhl3": {
        "symbol": "GRHL3",
        "species": "human",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5425218/",
        "corroborating": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4836819/",
        "model": "primary human epidermal keratinocytes; mouse and human epithelial models",
        "assay": "ChIP-seq plus siRNA knockdown/gene-expression analysis; promoter and loss-of-function validation",
        "observation": "GRHL3 has direct chromatin-binding and perturbation evidence in human keratinocytes, including state-dependent enhancer/promoter regulation and direct target programs such as SMAP1; this does not establish the queued ABCA1/ACKR3/ACTR2/ACVR1 pairs.",
        "direction": "state-dependent activation and repression; queued-pair direction not established",
        "role": "regulator-level identity and regulatory-capacity evidence only",
        "near": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4885135/ (GRHL3-E-cadherin, not queued targets); https://pmc.ncbi.nlm.nih.gov/articles/PMC4836819/ (GRHL3-GSK3B, not queued targets)",
    },
    "arnt2": {
        "symbol": "ARNT2",
        "species": "mouse",
        "primary": "https://pubmed.ncbi.nlm.nih.gov/12947113/",
        "corroborating": "https://pubmed.ncbi.nlm.nih.gov/30846309/",
        "model": "mouse neuroendocrine and neuronal models",
        "assay": "inducible SIM1/ARNT2 perturbation with microarray/Northern and independent neuronal regulatory studies",
        "observation": "ARNT2 is supported as a transcriptional regulator in neuronal/neuroendocrine models, with reported targets such as Jak2 and Trβ2; the queued A2M/ABCA1/ACKR3/ACTR2 pairs were not supported.",
        "direction": "context-dependent regulatory program; exact queued-pair direction not established",
        "role": "regulator-level identity and regulatory-capacity evidence only",
        "near": "https://pubmed.ncbi.nlm.nih.gov/12947113/ (ARNT2 targets differ from queued targets); co-occurrence in hypoxia/SCI gene lists was not treated as binding evidence",
    },
    "zbtb26": {
        "symbol": "ZBTB26",
        "species": "human",
        "primary": "https://doi.org/10.1096/fj.202504190R",
        "corroborating": "",
        "model": "human HEK293T and related cell models",
        "assay": "AP-MS, ChIP-seq, ZBTB26 knockout and active-chromatin assays",
        "observation": "ZBTB26 is supported as a nuclear DNA-associated transcriptional regulator in human cells; the queued A2M/ACKR2/ACVR1/ACVR1C pairs were not located in the cited study.",
        "direction": "target-level direction for queued pairs not established",
        "role": "regulator-level identity and regulatory-capacity evidence only",
        "near": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4920148/ (ACVR1 promoter study reports other TFs, not ZBTB26); Xenopus thyroid results were not transferred to human queued pairs",
    },
    "zfx": {
        "symbol": "ZFX",
        "species": "human",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5848610/",
        "corroborating": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5085766/",
        "model": "human HEK293T, HCT116, C4-2B and MCF7 models",
        "assay": "ChIP-seq with ZFX knockdown/RNA-seq and independent promoter regulation study",
        "observation": "ZFX is supported as a chromatin-associated transcriptional regulator in human cell models; the queued ACKR2/ACTR2/ACVR1/ACVR1C pairs were not located.",
        "direction": "context-specific regulatory effects; exact queued-pair direction not established",
        "role": "regulator-level identity and regulatory-capacity evidence only",
        "near": "Human ACVR1 promoter studies reporting other TFs and mouse Zfx/Acvr1 co-occurrence were excluded; supplemental binding tables were not treated as retrieved exact-pair evidence",
    },
    "znf281": {
        "symbol": "ZNF281/Zfp281",
        "species": "mouse",
        "primary": "https://pubmed.ncbi.nlm.nih.gov/18757296/",
        "corroborating": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6879198/",
        "model": "mouse embryonic stem cells",
        "assay": "Zfp281/Znf281 ChIP and knockdown microarray studies",
        "observation": "Mouse Zfp281 (the official-symbol relationship for the queued Znf281 alias) is supported as a transcriptional regulator in embryonic stem cells, with reported targets such as Nanog; the queued A2M/ABCA1/ACKR3/ACTR2 pairs were not supported.",
        "direction": "context-dependent developmental regulation; exact queued-pair direction not established",
        "role": "regulator-level identity and regulatory-capacity evidence only",
        "near": "https://www.ncbi.nlm.nih.gov/gene/226442 (mouse official symbol/alias mapping); human ZNF281-ABCA1 co-expression and prediction lists were excluded",
    },
    "znf341": {
        "symbol": "ZNF341",
        "species": "human",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6173313/",
        "corroborating": "",
        "model": "human patient PBMCs, HEK293T and Ramos cell models",
        "assay": "promoter reporter, ChIP and loss-of-function studies",
        "observation": "ZNF341 is supported as a human transcriptional regulator with direct evidence for STAT3 regulation; the queued ACKR2/ACTR2/ACVR1/ACVR1C pairs were not supported.",
        "direction": "activating/maintenance effect for STAT3; queued-pair direction not established",
        "role": "regulator-level identity and regulatory-capacity evidence only",
        "near": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4920148/ (ACVR1 promoter study reports other TFs, not ZNF341); mouse ACVR1C exercise/pathway studies were excluded",
    },
    "zscan22": {
        "symbol": "ZSCAN22",
        "species": "human",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5131825/",
        "corroborating": "",
        "model": "human HEK293 functional-screen models",
        "assay": "C2H2 zinc-finger functional/regulatory screen",
        "observation": "ZSCAN22 has regulator-level functional evidence; the queued ACKR3/ACTR2/ACVR1/ACVR1C pairs were not directly tested.",
        "direction": "queued-pair direction not established",
        "role": "regulator-level identity and regulatory-capacity evidence only",
        "near": "ACKR3-only, ARP2/3, and ACVR1/ACVR1C studies without ZSCAN22 were excluded",
    },
    "purb": {
        "symbol": "PURB",
        "species": "mouse",
        "primary": "https://pubmed.ncbi.nlm.nih.gov/12874279/",
        "corroborating": "https://pubmed.ncbi.nlm.nih.gov/23724822/",
        "model": "mouse transcriptional and smooth-muscle models",
        "assay": "PURB promoter/transcriptional studies with independent Acta2 validation",
        "observation": "PURB has regulator-level evidence including Acta2-related transcriptional regulation; the queued Actr2/Acvr1/Acvr1c/Acvrl1 targets were not directly tested.",
        "direction": "queued-pair direction not established",
        "role": "regulator-level identity and regulatory-capacity evidence only",
        "near": "PURB-to-Acta2 is a different target from queued Actr2; ACVR1/ACVR1C/ACVRL1 studies naming other factors were excluded",
    },
    "zfhx2": {
        "symbol": "ZFHX2",
        "species": "human",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5837393/",
        "corroborating": "",
        "model": "human sensory-neuron/Marsili syndrome models",
        "assay": "human ZFHX2 genetic and transcriptional regulatory studies",
        "observation": "ZFHX2 has human regulator-level evidence in sensory-neuron biology; the queued A2M/ACKR3/ACTR2/ACVR1 targets were not directly tested.",
        "direction": "queued-pair direction not established",
        "role": "regulator-level identity and regulatory-capacity evidence only",
        "near": "ZHX2, ACKR3-only, ARP2/3, and LHX2-to-ACVR1 studies were excluded as different genes or regulators",
    },
    "neurod2": {
        "symbol": "NEUROD2",
        "species": "mouse",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5343279/",
        "corroborating": "https://pubmed.ncbi.nlm.nih.gov/27146976/",
        "model": "mouse neuronal models",
        "assay": "NEUROD2 perturbation, chromatin/target studies, and independent neuronal target validation",
        "observation": "NEUROD2 has regulator-level neuronal evidence with targets such as Stim1 and other neuronal genes; the queued Actr2/Acvr1/Acvr1c/Adam10 targets were not directly tested.",
        "direction": "queued-pair direction not established",
        "role": "regulator-level identity and regulatory-capacity evidence only",
        "near": "Stim1, Reln, Dlg4/Cntn2, LHX2-to-Acvr1, YAP-to-Acvr1c, and Adam10 expression studies were excluded as different targets or regulators",
    },
    "prdm10": {
        "symbol": "PRDM10",
        "species": "human",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6525587/",
        "corroborating": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7368010/",
        "model": "human and mouse PRDM10 cellular models",
        "assay": "PRDM10 perturbation and target-gene transcriptional studies",
        "observation": "PRDM10 has regulator-level evidence including BCL2/EIF3B-related transcriptional targets; the queued ACKR1/ACKR2/ACTR2/ACVR1 targets were not directly tested.",
        "direction": "queued-pair direction not established",
        "role": "regulator-level identity and regulatory-capacity evidence only",
        "near": "PRDM10-to-BCL2/EIF3B, GATA1-to-ACKR2, ARP2/3, and EGR1/HEY1/ZBTB7A/SP1-to-ACVR1 studies were excluded as different pairs",
    },
    "sp140": {
        "symbol": "SP140",
        "species": "human",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5549562/",
        "corroborating": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10266544/",
        "model": "human macrophage and immune-cell models",
        "assay": "ChIP-seq/knockdown and immune chromatin-reader studies",
        "observation": "SP140 is supported as an immune chromatin-associated transcriptional regulator; the queued ABCA1/ACKR1/ACTR2/ACVR1 pairs were not supported.",
        "direction": "context-dependent immune transcriptional effects; exact queued-pair direction not established",
        "role": "regulator-level identity and regulatory-capacity evidence only",
        "near": "SP140-ACKR1 co-occurrence in a mouse expression table and SP140/ACTR2 cancer signatures were treated as list-level or cross-species observations, not direct regulatory edges",
    },
    "hivep3": {
        "symbol": "HIVEP3",
        "species": "mouse",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7721697/",
        "corroborating": "",
        "model": "mouse iNKT/MAIT developmental models",
        "assay": "HIVEP3 knockout and immune-cell transcriptional profiling",
        "observation": "HIVEP3 is supported as an immune developmental transcriptional regulator; the queued Abca1/Ackr3/Actr2/Acvr1 pairs were not supported.",
        "direction": "immune developmental effects; exact queued-pair direction not established",
        "role": "regulator-level identity and regulatory-capacity evidence only",
        "near": "HIVEP3 induction and ABCA1/STAT6 pathway observations were parallel rather than a HIVEP3-to-Abca1 experiment; Schnurri-3/bone and ACVR1/FOP studies were separate interventions",
    },
    "mecom": {
        "symbol": "MECOM",
        "species": "human",
        "primary": "https://pubmed.ncbi.nlm.nih.gov/36522544/",
        "corroborating": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10130150/",
        "model": "human hematopoietic stem-cell and endothelial models",
        "assay": "MECOM perturbation and endothelial regulatory studies",
        "observation": "MECOM is supported as a hematopoietic/endothelial transcriptional regulator; the queued ACKR2/ACKR3/ACTR2/ACVR1 pairs were not supported.",
        "direction": "context-dependent regulatory effects; exact queued-pair direction not established",
        "role": "regulator-level identity and regulatory-capacity evidence only",
        "near": "MECOM and queued targets co-occur in disease-expression, vascular, or insertion-site datasets without a direct target assay",
    },
    "znf467": {
        "symbol": "ZNF467",
        "species": "human",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13181174/",
        "corroborating": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11142749/",
        "model": "human hematopoietic and endothelial models",
        "assay": "transcriptional perturbation and regulatory studies",
        "observation": "ZNF467 is supported as a transcriptional regulator in the cited hematopoietic/endothelial models; the queued A2M/ACVR1/ADA/ADAM10 pairs were not supported.",
        "direction": "context-dependent regulatory effects; exact queued-pair direction not established",
        "role": "regulator-level identity and regulatory-capacity evidence only",
        "near": "A2M, ACVR1, ADA, or ADAM10 co-occurrence in miRNA, expression, or atherosclerosis lists was not treated as a direct ZNF467 edge",
    },
    "zkscan1": {
        "symbol": "ZKSCAN1",
        "species": "human",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5527481/",
        "corroborating": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8144607/",
        "model": "human hepatocellular-carcinoma and tumor cell models",
        "assay": "perturbation/RNA-seq and nuclear-localization studies",
        "observation": "ZKSCAN1 is supported as a nuclear transcriptional regulator in human tumor models; the queued ACKR1/ACKR2/ACTR2/ACVR1 pairs were not supported.",
        "direction": "context-dependent tumor transcriptional effects; exact queued-pair direction not established",
        "role": "regulator-level identity and regulatory-capacity evidence only",
        "near": "ACKR1, ACKR2, ACTR2, and ACVR1 co-occurrence in broad expression, prediction, or metabolic gene tables was not treated as direct ZKSCAN1 regulation",
    },
    "znf639": {
        "symbol": "ZNF639",
        "species": "human",
        "primary": "https://pubmed.ncbi.nlm.nih.gov/20484494/",
        "corroborating": "https://pubmed.ncbi.nlm.nih.gov/16182284/",
        "model": "human DNA-binding and viral-promoter regulatory models",
        "assay": "sequence-specific DNA-binding and promoter-regulation assays",
        "observation": "ZNF639 has regulator-level DNA-binding/promoter evidence; the queued A2M/ACVR1/ADA/ADAM10 pairs were not directly tested.",
        "direction": "queued-pair direction not established",
        "role": "regulator-level identity and regulatory-capacity evidence only",
        "near": "Cancer expression and co-list results for A2M, ACVR1, ADA, or ADAM10 were excluded as non-mechanistic",
    },
    "znf580": {
        "symbol": "ZNF580",
        "species": "human",
        "primary": "https://pubmed.ncbi.nlm.nih.gov/21599657/",
        "corroborating": "https://pubmed.ncbi.nlm.nih.gov/24771066/",
        "model": "human endothelial/TGF-beta regulatory models",
        "assay": "ZNF580-TGF-beta/ALK5/Smad2/eNOS transcriptional studies",
        "observation": "ZNF580 has regulator-level evidence in vascular/TGF-beta models; the separate exact ZNF580-to-ABCA1 functional result is recorded as a partial downstream-evidence row.",
        "direction": "context-dependent regulatory effects; exact queued-pair direction generally not established",
        "role": "regulator-level identity and regulatory-capacity evidence only; one exact target has partial functional support",
        "near": "ZNF580-to-ACVR1/ACVR1C and unrelated metabolic/receptor studies were excluded; direct ABCA1 occupancy was not shown",
    },
    "znf35": {
        "symbol": "ZNF35",
        "species": "human",
        "primary": "https://pubmed.ncbi.nlm.nih.gov/8477855/",
        "corroborating": "",
        "model": "in-vitro DNA-binding model",
        "assay": "sequence-specific DNA-binding assay",
        "observation": "ZNF35 sequence-specific DNA binding was reported in vitro, but no endogenous target-gene relationship was established for the queued ACTR2/ACVR1/ADA/ADAM10 pairs.",
        "direction": "queued-pair direction not established",
        "role": "regulator-level capacity evidence only; endogenous target evidence remains weak",
        "near": "ARP2/3, ACVR1, ADA, and ADAM10 studies without ZNF35 were excluded",
    },
    "znf366": {
        "symbol": "ZNF366",
        "species": "human",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1693901/",
        "corroborating": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6023963/",
        "model": "human estrogen-receptor and dendritic-cell models",
        "assay": "DC-SCRIPT/ZNF366 corepressor and dendritic-cell regulatory studies",
        "observation": "ZNF366 has regulator/coregulator evidence in estrogen-receptor and dendritic-cell contexts; the queued A2M/ACKR3/ACTR2/ACVR1 pairs were not directly tested.",
        "direction": "context-dependent corepressor effects; queued-pair direction not established",
        "role": "regulator-level identity and regulatory-capacity evidence only",
        "near": "Co-expression lists and ACKR3/ARP2/3/ACVR1 studies without ZNF366 were excluded",
    },
    "znf770": {
        "symbol": "ZNF770",
        "species": "human",
        "primary": "",
        "corroborating": "",
        "model": "not established in bounded search",
        "assay": "exact-pair PubMed/PMC search",
        "observation": "No qualifying regulator-level primary article was located in the bounded search for ZNF770, and no queued exact pair was supported.",
        "direction": "not established",
        "role": "search lead only; no regulator-level evidence record for promotion",
        "near": "A colorectal 5hmC study reported ZNF770 motif enrichment, not ZNF770 occupancy or regulation of ACVR1, ACVRL1, ADA, or ADAM10",
    },
}


PAIR_EVIDENCE_OVERRIDES = {
    ("znf580", "abca1"): {
        "exact_pair_status": "partial_functional_support_without_binding_or_independent_corroboration",
        "regulator_general_evidence_status": "supported_general_regulator_evidence",
        "target_cell_presence_status": "supported_human_thp1_oxldl_foam_cells",
        "binding_or_association_status": "not_found_for_exact_pair",
        "downstream_expression_or_perturbation_status": "supported_znf580_overexpression_and_silencing_direction",
        "disposition": "retain_partial_staging_only_pending_direct_binding_and_corroboration",
        "primary_citation": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9353537/",
        "review_notes": "Human THP-1 oxLDL foam-cell study reports ZNF580 overexpression increasing ABCA1 mRNA/protein and silencing decreasing it. No direct promoter occupancy or ZNF580-ABCA1 binding was shown, and no independent exact corroboration was located. This is not sufficient for a canonical Module 22B promotion.",
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


def exact_search_url(regulator: str, target: str, species: str) -> str:
    query = f'"{regulator}" AND "{target}" AND {species}'
    return "https://pubmed.ncbi.nlm.nih.gov/?term=" + quote_plus(query)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    batch_rows = [row for row in read_tsv(args.batch) if int(row["batch_rank"]) <= 25]
    if len(batch_rows) != 100:
        raise SystemExit(f"expected 100 rows from batch ranks 1-25, found {len(batch_rows)}")

    pair_rows: list[dict[str, str]] = []
    for index, row in enumerate(batch_rows, start=1):
        key = row["regulator_key"]
        evidence = REGULATOR_EVIDENCE.get(key)
        if evidence is None:
            raise SystemExit(f"missing regulator evidence map for {key}")
        override = PAIR_EVIDENCE_OVERRIDES.get((key, row["target_symbol"].casefold()), {})
        pair_rows.append({
            "review_id": f"public_tf_evidence_batch001_pair_{index:03d}",
            "batch_id": row["batch_id"],
            "batch_rank": row["batch_rank"],
            "regulator_key": key,
            "regulator_symbol": evidence["symbol"],
            "species_scope": row["species_scope"],
            "source_registry": row["source_registry"],
            "source_record_id": row["source_record_id"],
            "raw_tf_symbol": row["raw_tf_symbol"],
            "target_symbol": row["target_symbol"],
            "target_graph_modules": row["target_graph_modules"],
            "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": exact_search_url(evidence["symbol"], row["target_symbol"], row["species_scope"]),
            "exact_pair_status": override.get("exact_pair_status", "no_exact_pair_support_found_in_bounded_search"),
            "regulator_general_evidence_status": override.get("regulator_general_evidence_status", "supported_general_regulator_evidence" if evidence["primary"] else "not_found_in_bounded_search"),
            "target_cell_presence_status": override.get("target_cell_presence_status", "not_assessed"),
            "binding_or_association_status": override.get("binding_or_association_status", "not_assessed_for_exact_pair"),
            "downstream_expression_or_perturbation_status": override.get("downstream_expression_or_perturbation_status", "not_assessed_for_exact_pair"),
            "downstream_activation_status": "not_assessed",
            "upstream_relay_status": "not_assessed",
            "disposition": override.get("disposition", "retain_database_candidate_as_search_lead_only"),
            "primary_citation": override.get("primary_citation", ""),
            "corroborating_citation": "",
            "near_match_exclusions": evidence["near"],
            "review_notes": override.get("review_notes", "General regulator evidence is stored in the regulator evidence register; it is not attached to this exact target pair. Near matches were excluded rather than used for promotion."),
            "exportable": "false",
            "canonical_write_performed": "false",
        })

    evidence_rows: list[dict[str, str]] = []
    for key, evidence in REGULATOR_EVIDENCE.items():
        if not evidence["primary"]:
            continue
        evidence_rows.append({
            "evidence_id": f"public_tf_evidence_batch001_regulator_{key}",
            "regulator_key": key,
            "regulator_symbol": evidence["symbol"],
            "species_scope": evidence["species"],
            "evidence_layer": "regulator_identity_and_regulatory_capacity",
            "support_kind": "primary_literature_regulator_level",
            "cell_or_model": evidence["model"],
            "assay_or_perturbation": evidence["assay"],
            "observation": evidence["observation"],
            "effect_direction": evidence["direction"],
            "primary_citation": evidence["primary"],
            "corroborating_citation": evidence["corroborating"],
            "route_or_module_relevance": evidence["role"],
            "target_pair_scope": "not evidence for the queued exact pairs; no Module 22B edge or upstream relay inferred",
            "exportable": "false",
            "canonical_write_performed": "false",
            "limitations": "Regulator-level evidence establishes that the named factor can act as a transcriptional regulator in the cited model. It does not establish presence in the target SCI cell, activation downstream of a module 20/21/23/24 relay, or regulation of the queued target.",
        })

    override = PAIR_EVIDENCE_OVERRIDES[("znf580", "abca1")]
    evidence_rows.append({
        "evidence_id": "public_tf_evidence_batch001_pair_znf580_abca1_partial",
        "regulator_key": "znf580",
        "regulator_symbol": "ZNF580",
        "species_scope": "human",
        "evidence_layer": "downstream_expression_or_perturbation",
        "support_kind": "exact_pair_partial_functional",
        "cell_or_model": "human THP-1 oxLDL foam cells",
        "assay_or_perturbation": "ZNF580 overexpression and silencing with ABCA1 mRNA/protein readout",
        "observation": "ZNF580 overexpression increased ABCA1 mRNA/protein and silencing decreased it.",
        "effect_direction": "positive functional association",
        "primary_citation": override["primary_citation"],
        "corroborating_citation": "",
        "route_or_module_relevance": "ABCA1 is a Module 20B target candidate; this row supports only a partial target response, not receptor/relay activation or direct TF binding",
        "target_pair_scope": "ZNF580 -> ABCA1, human",
        "exportable": "false",
        "canonical_write_performed": "false",
        "limitations": "No direct promoter occupancy or binding was shown; no independent exact corroboration was located; target-cell presence is limited to the cited THP-1 foam-cell model; no upstream relay was tested.",
    })

    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch001_pairs.tsv"
    evidence_path = args.output_dir / "public_tf_evidence_review_batch001_regulator_register.tsv"
    summary_path = args.output_dir / "batch_001_evidence_review_summary.json"
    write_tsv(pair_path, PAIR_FIELDS, pair_rows)
    write_tsv(evidence_path, EVIDENCE_FIELDS, evidence_rows)
    summary = {
        "status": "staging_only",
        "batch_id": "public_tf_evidence_batch_001",
        "source_set_ranks_reviewed": list(range(1, 26)),
        "pair_rows_reviewed": len(pair_rows),
        "unique_regulators_reviewed": len({row["regulator_key"] for row in pair_rows}),
        "exact_pair_support_rows": sum(row["exact_pair_status"] == "exact_pair_support_found" for row in pair_rows),
        "partial_functional_pair_rows": sum(row["exact_pair_status"].startswith("partial_") for row in pair_rows),
        "general_regulator_evidence_rows": len(evidence_rows) - 1,
        "target_cell_presence_rows_promoted": 0,
        "downstream_activation_rows_promoted": 0,
        "upstream_relay_rows_promoted": 0,
        "exportable_pair_rows": sum(row["exportable"] == "true" for row in pair_rows),
        "canonical_writes_performed": False,
        "module22b_promotions_performed": False,
        "provenance_preserved": True,
        "outputs": [str(pair_path.relative_to(ROOT)), str(evidence_path.relative_to(ROOT))],
        "decision": "Keep all 100 database-attributed memberships as search leads. Retain ZNF580-to-ABCA1 as partial functional staging evidence only; keep all other regulator-level literature separate from target-pair evidence and do not promote any pair.",
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (args.output_dir / "EVIDENCE_REVIEW_BATCH001.md").write_text(
        "# Evidence review: public TF batch 001\n\n"
        "This bounded first pass reviewed all twenty-five TFLink source sets (100 exact regulator-target pairs). "
        "One pair, ZNF580-to-ABCA1, has partial functional support in human THP-1 oxLDL foam cells but lacks direct binding and independent corroboration, so it remains staging-only. "
        "The other exact pairs remain database-attributed search leads; regulator-level literature is kept separate from target-pair evidence. "
        "Target-cell presence, downstream activation, and upstream relay remain unassessed for the queued route; no canonical or Module 22B writes were performed.\n\n"
        "Near matches are recorded as exclusions so that evidence for another regulator or another target cannot silently migrate onto the queued pair.\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
