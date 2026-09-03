#!/usr/bin/env python3
"""Audit exact Module 22A-to-22B links for already high-confidence evidence.

This is intentionally a linkage audit, not a canonical materialization step.
It promotes no rows in the source registers and never edits the Module 22A
handoff file. A link is emitted only when the handoff, 22B edge, and 22B
evidence records agree, and the evidence is high-confidence either in the B
register or in a reviewed primary extraction overlay.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HANDOFF = ROOT / "work/module21_relay/module22a_ligand_tf_handoff.tsv"
EDGE_REGISTER = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_REGISTER = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
OVERLAYS = [
    ROOT / "work/cross_module_synthesis/canonical_evidence_review/phase2_H_22B_even_tf_program_overlay.tsv",
    ROOT / "work/cross_module_synthesis/canonical_evidence_review/phase2_I_22B_odd_tf_program_overlay.tsv",
    ROOT / "work/module22a_22b_promotion_audit/module22a_new_primary_extractions.tsv",
]
OUT_DIR = ROOT / "work/module22a_22b_promotion_audit"
OUT_TSV = OUT_DIR / "module22a_22b_high_confidence_links.tsv"
OUT_MD = ROOT / "docs/MODULE22A_22B_HIGH_CONFIDENCE_LINKAGE_AUDIT_2026-09-02.md"


# These are exact ligand/receptor handoffs for which the current 22B register
# already contains a high-confidence direct TF-target record. The upstream
# handoff remains bounded to the tested ligand/model context; this table does
# not infer SCI transfer or receptor-complex-specific activity.
LINK_SPECS = [
    {
        "link_id": "M22A22B-LINK-001",
        "handoff_id": "M22A-HANDOFF-001300",
        "edge_id": "M22B-E000448",
        "evidence_id": "M22B-EVID-000007",
        "expected_tf": "STAT5",
        "phase2_extraction_id": "M22B-P2-R-000007-R096",
        "basis": "IL-3/STAT5 binding and promoter-mutagenesis support for Ccnd1 in human hematopoietic comparator cells.",
    },
    {
        "link_id": "M22A22B-LINK-002",
        "handoff_id": "M22A-HANDOFF-001300",
        "edge_id": "M22B-E000449",
        "evidence_id": "M22B-EVID-000006",
        "expected_tf": "STAT5",
        "phase2_extraction_id": "M22B-P2-R-000006-R096",
        "basis": "IL-3/STAT5 recruitment and endogenous Cis/Cish promoter regulation in murine Ba/F3 cells.",
    },
    {
        "link_id": "M22A22B-LINK-003",
        "handoff_id": "M22A-HANDOFF-001300",
        "edge_id": "M22B-E000456",
        "evidence_id": "M22B-EVID-000028",
        "expected_tf": "STAT5",
        "phase2_extraction_id": "M22B-P2-R-000028",
        "basis": "IL-3/STAT5A/B recruitment and endogenous Cis/Cish promoter regulation in murine Ba/F3 cells.",
    },
    {
        "link_id": "M22A22B-LINK-004",
        "handoff_id": "M22A-HANDOFF-001307",
        "edge_id": "M22B-E000459",
        "evidence_id": "M22B-EVID-000010",
        "expected_tf": "STAT6",
        "phase2_extraction_id": "M22B-P2-R-000010-R096",
        "basis": "IL-4/STAT6/PGC-1beta corecruitment and STAT6-site-dependent Arg1 enhancer regulation in mouse macrophages.",
    },
    {
        "link_id": "M22A22B-LINK-005",
        "handoff_id": "M22A-HANDOFF-001307",
        "edge_id": "M22B-E000460",
        "evidence_id": "M22B-EVID-000009",
        "expected_tf": "STAT6",
        "phase2_extraction_id": "",
        "basis": "IL-4/STAT6-dependent Chil3/Ym1 promoter evidence with reporter, site-mutation, and DNA-binding support in mouse macrophage models.",
    },
    {
        "link_id": "M22A22B-LINK-006",
        "handoff_id": "M22A-HANDOFF-001312",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22B-P2-R-RECOVERY-STAT3-SOCS3-000001",
        "basis": "IL-6/sIL-6R, STAT3 promoter binding, and endogenous Socs3 induction with promoter-site controls in mouse comparator systems.",
    },
    {
        "link_id": "M22A22B-LINK-007",
        "handoff_id": "M22A-HANDOFF-001802",
        "edge_id": "M22B-E000036",
        "evidence_id": "M22B-EVID-000137",
        "expected_tf": "CREB",
        "phase2_extraction_id": "M22B-P2-R-000137-R094",
        "basis": "BDNF-TrkB/CREB promoter-IV occupancy, promoter-element mutation, and CREB-family perturbation support in rat cortical neurons.",
    },
    {
        "link_id": "M22A22B-LINK-008",
        "handoff_id": "M22A-HANDOFF-000449",
        "edge_id": "M22B-E000336",
        "evidence_id": "M22B-EVID-000620",
        "expected_tf": "RELB",
        "phase2_extraction_id": "M22B-P2-R-000338",
        "basis": "EDA-A1/EDAR/RelB promoter occupancy and RelB-dependent Ltb transcription in the validated skin-cell models.",
    },
    {
        "link_id": "M22A22B-LINK-009",
        "handoff_id": "M22A-HANDOFF-000450",
        "edge_id": "M22B-E000158",
        "evidence_id": "M22B-EVID-000622",
        "expected_tf": "ELK1",
        "phase2_extraction_id": "M22B-P2-R-000340",
        "basis": "EGF/EGFR/ERK-dependent ELK1 occupancy and promoter perturbation at EGR1 in human PC3 cells.",
    },
    {
        "link_id": "M22A22B-LINK-010",
        "handoff_id": "M22A-HANDOFF-005464",
        "edge_id": "M22B-E000432",
        "evidence_id": "M22B-EVID-000083",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22B-P2-R-000083-R092",
        "basis": "IL-10/STAT3 recruitment and transcriptional activation at the Ttp/Zfp36 promoter in activated mouse macrophages.",
    },
    {
        "link_id": "M22A22B-LINK-011",
        "handoff_id": "M22A-HANDOFF-000440",
        "edge_id": "M22B-E000167",
        "evidence_id": "M22B-EVID-000105",
        "expected_tf": "ESR1",
        "phase2_extraction_id": "M22B-P2-R-000105-R093",
        "basis": "Estradiol-ESR1/JUN occupancy and functional promoter regulation at Cyp19a1 promoter I.f in mouse hypothalamic neuronal models.",
    },
    {
        "link_id": "M22A22B-LINK-012",
        "handoff_id": "M22A-HANDOFF-003978",
        "edge_id": "M22B-E000459",
        "evidence_id": "M22B-EVID-000054",
        "expected_tf": "STAT6",
        "phase2_extraction_id": "M22B-P2-R-000054-R100",
        "basis": "IL-4/IL4RA-IL13RA1 type-II receptor-complex handoff linked to bounded STAT6 occupancy and Arg1 regulation in infected mouse macrophages.",
    },
    {
        "link_id": "M22A22B-LINK-013",
        "handoff_id": "M22A-HANDOFF-003979",
        "edge_id": "M22B-E000459",
        "evidence_id": "M22B-EVID-000054",
        "expected_tf": "STAT6",
        "phase2_extraction_id": "M22B-P2-R-000054-R100",
        "basis": "IL-4/IL4RA-IL13RA1 type-II receptor-complex handoff linked to bounded STAT6 occupancy and Arg1 regulation in infected mouse macrophages.",
    },
    {
        "link_id": "M22A22B-LINK-014",
        "handoff_id": "M22A-HANDOFF-005070",
        "edge_id": "M22B-E000455",
        "evidence_id": "M22B-EVID-000077",
        "expected_tf": "STAT5",
        "phase2_extraction_id": "M22B-P2-R-000077-R091",
        "basis": "TPO/MPL-associated STAT5A/STAT5B recruitment and cyclin D1 promoter activation in UT7-mpl cells.",
    },
    {
        "link_id": "M22A22B-LINK-015",
        "handoff_id": "M22A-HANDOFF-003039",
        "edge_id": "M22B-E000299",
        "evidence_id": "M22B-EVID-000198",
        "expected_tf": "PEA3",
        "phase2_extraction_id": "M22B-P2-B090-003",
        "basis": "Collagen-I/DDR2-associated PEA3 recruitment and functional regulation of the DDR1 promoter in human lung-fibroblast systems.",
    },
    {
        "link_id": "M22A22B-LINK-016",
        "handoff_id": "M22A-HANDOFF-003267",
        "edge_id": "M22B-E000417",
        "evidence_id": "M22B-EVID-000030",
        "expected_tf": "STAT1",
        "phase2_extraction_id": "M22B-P2-R-000028C",
        "basis": "IL-35-associated STAT1:STAT4 co-occupancy and perturbation-supported regulation of the Il12a/Ebi3 promoter module in activated mouse T cells.",
    },
    {
        "link_id": "M22A22B-LINK-017",
        "handoff_id": "M22A-HANDOFF-001806",
        "edge_id": "M22B-E000353",
        "evidence_id": "M22B-EVID-000037",
        "expected_tf": "SMAD1",
        "phase2_extraction_id": "M22A-P2-NEW-BMP2-ID1-20260902",
        "basis": "BMP2-responsive SMAD1/SMAD4 binding and perturbation-supported regulation of the Id1 promoter in mouse myoblast and human Smad4-deficient comparator systems; bounded for the submitted ACVR2A-containing receptor pair and SCI transfer.",
    },
    {
        "link_id": "M22A22B-LINK-018",
        "handoff_id": "M22A-HANDOFF-001808",
        "edge_id": "M22B-E000353",
        "evidence_id": "M22B-EVID-000037",
        "expected_tf": "SMAD1",
        "phase2_extraction_id": "M22A-P2-NEW-BMP2-ID1-20260902",
        "basis": "BMP2-responsive SMAD1/SMAD4 binding and perturbation-supported regulation of the Id1 promoter in mouse myoblast and human Smad4-deficient comparator systems; bounded for the submitted BMPR2-containing receptor pair and SCI transfer.",
    },
    {
        "link_id": "M22A22B-LINK-019",
        "handoff_id": "M22A-HANDOFF-001811",
        "edge_id": "M22B-E000353",
        "evidence_id": "M22B-EVID-000037",
        "expected_tf": "SMAD1",
        "phase2_extraction_id": "M22A-P2-NEW-BMP2-ID1-20260902",
        "basis": "BMP2-responsive SMAD1/SMAD4 binding and perturbation-supported regulation of the Id1 promoter in mouse myoblast and human Smad4-deficient comparator systems; bounded for the submitted BMPR1B/BMPR2 receptor pair and SCI transfer.",
    },
    {
        "link_id": "M22A22B-LINK-020",
        "handoff_id": "M22A-HANDOFF-001284",
        "edge_id": "M22B-E000443",
        "evidence_id": "M22B-EVID-000050",
        "expected_tf": "STAT4",
        "phase2_extraction_id": "M22A-P2-NEW-IL12-TBX21-20260902",
        "basis": "IL12/STAT4 occupancy and mutation-sensitive activation of a conserved Tbx21/T-bet enhancer in CD8 T-cell and reporter systems; bounded for the tested lymphocyte context and SCI transfer.",
    },
    {
        "link_id": "M22A22B-LINK-021",
        "handoff_id": "M22A-HANDOFF-001446",
        "edge_id": "M22B-E000181",
        "evidence_id": "M22B-EVID-000158",
        "expected_tf": "FOXH1",
        "phase2_extraction_id": "M22A-P2-NEW-NODAL-FOXH1-20260902",
        "basis": "Nodal-responsive FOXH1/SMAD2/3 occupancy and loss-of-function-supported regulation of a mesendoderm target module in Xenopus embryos; bounded for receptor-complex substitutions, developmental context, and SCI transfer.",
    },
    {
        "link_id": "M22A22B-LINK-022",
        "handoff_id": "M22A-HANDOFF-003270",
        "edge_id": "M22B-E000207",
        "evidence_id": "M22B-EVID-000207",
        "expected_tf": "HOXD3",
        "phase2_extraction_id": "M22A-P2-NEW-EDIL3-HOXD3-20260902",
        "basis": "EDIL3/Del-1 engagement of endothelial alphaVbeta5 is linked to HOXD3 induction and an angiogenic transcriptional program; bounded for alphaVbeta5 rather than ITGB5 alone, vascular context, and SCI transfer.",
    },
    {
        "link_id": "M22A22B-LINK-023",
        "handoff_id": "M22A-HANDOFF-003608",
        "edge_id": "M22B-E000095",
        "evidence_id": "M22B-EVID-000215",
        "expected_tf": "CREB",
        "phase2_extraction_id": "M22A-P2-NEW-GIP-LPL-20260902",
        "basis": "GIP/GIPR-associated phospho-CREB/TORC2 occupancy and perturbation-supported activation of the LPL promoter in human adipocyte and GIPR-expressing reporter systems; bounded for insulin co-treatment and metabolic-cell context.",
    },
    {
        "link_id": "M22A22B-LINK-024",
        "handoff_id": "M22A-HANDOFF-004124",
        "edge_id": "M22B-E000425",
        "evidence_id": "M22B-EVID-000059",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22A-P2-NEW-LEPTIN-NHLH2-20260902",
        "basis": "Leptin-responsive STAT3 occupancy and promoter-site mutagenesis support for Nhlh2 regulation in mouse hypothalamic models; bounded for long LEPR signaling and hypothalamic context.",
    },
    {
        "link_id": "M22A22B-LINK-025",
        "handoff_id": "M22A-HANDOFF-004583",
        "edge_id": "M22B-E000457",
        "evidence_id": "M22B-EVID-000072",
        "expected_tf": "STAT5",
        "phase2_extraction_id": "M22A-P2-NEW-PRL-CSN2-20260902",
        "basis": "PRL/PRLR/JAK2/STAT5 signaling and STAT5 response-element dependence at the beta-casein/Csn2 promoter in mammary epithelial comparator systems; bounded for receptor isoform and mammary hormonal context.",
    },
    {
        "link_id": "M22A22B-LINK-026",
        "handoff_id": "M22A-HANDOFF-002399",
        "edge_id": "M22B-E000032",
        "evidence_id": "M22B-EVID-000192",
        "expected_tf": "CREB",
        "phase2_extraction_id": "M22A-P2-NEW-A2M-CREB-20260902",
        "basis": "Activated alpha2M/LRP1-associated ERK/Akt/CREB neural response and neurite-output program in neuronal comparator systems; bounded for activated alpha2M rather than native A2M, co-receptor use, and use of a program-level edge rather than a named CREB target gene.",
    },
    {
        "link_id": "M22A22B-LINK-027",
        "handoff_id": "M22A-HANDOFF-001861",
        "edge_id": "M22B-E000174",
        "evidence_id": "M22B-EVID-000141",
        "expected_tf": "ETV5",
        "phase2_extraction_id": "M22A-P2-NEW-FGF10-ETV5-20260902",
        "basis": "FGF10/FGFR2-associated ETV5 occupancy and mutation-sensitive activation of the Shh long-range enhancer in embryonic lung models; bounded for ETV4 paralog transfer, FGFR2 isoform resolution, and SCI transfer.",
    },
    {
        "link_id": "M22A22B-LINK-028",
        "handoff_id": "M22A-HANDOFF-001885",
        "edge_id": "M22B-E000272",
        "evidence_id": "M22B-EVID-000179",
        "expected_tf": "NFAT",
        "phase2_extraction_id": "M22A-P2-NEW-FGF23-NFAT-20260902",
        "basis": "FGF23/FGFR4 activation of the PLCgamma/calcineurin/NFAT cardiac hypertrophy program in cardiomyocyte and rodent disease models; bounded as a program association without a unique NFAT target-gene occupancy claim.",
    },
    {
        "link_id": "M22A22B-LINK-029",
        "handoff_id": "M22A-HANDOFF-003909",
        "edge_id": "M22B-E000443",
        "evidence_id": "M22B-EVID-000050",
        "expected_tf": "STAT4",
        "phase2_extraction_id": "M22A-P2-NEW-IL12-TBX21-20260902",
        "basis": "IL12A/IL12B heterodimer-STAT4 occupancy and mutation-sensitive activation of the conserved Tbx21/T-bet enhancer in CD8 T-cell and reporter systems; bounded for the tested lymphocyte context and SCI transfer.",
    },
    {
        "link_id": "M22A22B-LINK-030",
        "handoff_id": "M22A-HANDOFF-003349",
        "edge_id": "M22B-E000449",
        "evidence_id": "M22B-EVID-000006",
        "expected_tf": "STAT5",
        "phase2_extraction_id": "M22A-P2-NEW-EPO-CISH-20260902",
        "basis": "EPO/EPOR-dependent STAT5 activation and CISH promoter activation in hematopoietic and EPO-receptor/STAT5-reconstituted reporter systems; bounded for the tested hematopoietic context and SCI transfer.",
    },
    {
        "link_id": "M22A22B-LINK-031",
        "handoff_id": "M22A-HANDOFF-003988",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000057",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22B-P2-R-RECOVERY-STAT3-SOCS3-000001",
        "basis": "Normalized IL6/IL6RA-IL6ST handoff linked to the recovered IL6/STAT3/Socs3 promoter mechanism; bounded for soluble-receptor and receptor-isoform context and SCI transfer.",
    },
    {
        "link_id": "M22A22B-LINK-032",
        "handoff_id": "M22A-HANDOFF-005380",
        "edge_id": "M22B-E000207",
        "evidence_id": "M22B-EVID-000207",
        "expected_tf": "HOXD3",
        "phase2_extraction_id": "M22A-P2-NEW-EDIL3-HOXD3-20260902",
        "basis": "EDIL3/ITGAV-containing handoff linked to the primary EDIL3/alphaVbeta5-associated HOXD3 angiogenic program; bounded because the submitted receptor label omits the beta-chain partner and the edge is program-level.",
    },
    {
        "link_id": "M22A22B-LINK-033",
        "handoff_id": "M22A-HANDOFF-001315",
        "edge_id": "M22B-E000378",
        "evidence_id": "M22B-EVID-000378",
        "expected_tf": "SMAD3",
        "phase2_extraction_id": "M22B-P2-R-000305",
        "basis": "Activin A/ACVR1B-associated SMAD3 occupancy and perturbation-supported activation of the Fst intronic enhancer; bounded to the Activin A/ALK4 branch because the primary study and edge record do not isolate ACVR2A from ACVR2B or establish SCI transfer.",
    },
    {
        "link_id": "M22A22B-LINK-034",
        "handoff_id": "M22A-HANDOFF-001316",
        "edge_id": "M22B-E000378",
        "evidence_id": "M22B-EVID-000378",
        "expected_tf": "SMAD3",
        "phase2_extraction_id": "M22B-P2-R-000305",
        "basis": "Activin A/ACVR1B-associated SMAD3 occupancy and perturbation-supported activation of the Fst intronic enhancer; bounded to the Activin A/ALK4 branch because ACVR2A and ACVR2B are partially redundant and the exact ACVR2B-ACVR1B holocomplex was not isolated.",
    },
    {
        "link_id": "M22A22B-LINK-035",
        "handoff_id": "M22A-HANDOFF-005094",
        "edge_id": "M22B-E000310",
        "evidence_id": "M22B-EVID-000271",
        "expected_tf": "RELA",
        "phase2_extraction_id": "M22B-P2-R-000239",
        "basis": "TNF-alpha induction context with canonical NF-kB/RELA promoter occupancy and perturbation-supported FAS transcription; bounded as an indirect TNF-to-RELA-to-FAS transcription chain, not a TNF-FAS binding or receptor-proximal interaction.",
    },
    {
        "link_id": "M22A22B-LINK-036",
        "handoff_id": "M22A-HANDOFF-002935",
        "edge_id": "M22B-E000181",
        "evidence_id": "M22B-EVID-000158",
        "expected_tf": "FOXH1",
        "phase2_extraction_id": "M22A-P2-NEW-NODAL-FOXH1-20260902",
        "basis": "CFC1/ACVR1B-associated Nodal receptor-complex handoff linked to the bounded FOXH1/SMAD2/3 Nodal-responsive target module in Xenopus embryos; receptor composition and developmental context remain explicit.",
    },
    {
        "link_id": "M22A22B-LINK-037",
        "handoff_id": "M22A-HANDOFF-002936",
        "edge_id": "M22B-E000181",
        "evidence_id": "M22B-EVID-000158",
        "expected_tf": "FOXH1",
        "phase2_extraction_id": "M22A-P2-NEW-NODAL-FOXH1-20260902",
        "basis": "CFC1-associated Nodal receptor-complex handoff with ACVR2A context linked to the bounded FOXH1/SMAD2/3 Nodal-responsive target module; the CFC1 association is not treated as a standalone binary receptor claim.",
    },
    {
        "link_id": "M22A22B-LINK-038",
        "handoff_id": "M22A-HANDOFF-004332",
        "edge_id": "M22B-E000181",
        "evidence_id": "M22B-EVID-000158",
        "expected_tf": "FOXH1",
        "phase2_extraction_id": "M22A-P2-NEW-NODAL-FOXH1-20260902",
        "basis": "Nodal/ACVR1B-ACVR2A-CFC1 handoff linked to the bounded FOXH1/SMAD2/3 Nodal-responsive target module in Xenopus embryos; exact receptor-complex and SCI transfer remain unresolved.",
    },
    {
        "link_id": "M22A22B-LINK-039",
        "handoff_id": "M22A-HANDOFF-004334",
        "edge_id": "M22B-E000181",
        "evidence_id": "M22B-EVID-000158",
        "expected_tf": "FOXH1",
        "phase2_extraction_id": "M22A-P2-NEW-NODAL-FOXH1-20260902",
        "basis": "Nodal/ACVR1B-ACVR2B-CFC1 handoff linked to the bounded FOXH1/SMAD2/3 Nodal-responsive target module in Xenopus embryos; exact receptor-complex and SCI transfer remain unresolved.",
    },
    {
        "link_id": "M22A22B-LINK-040",
        "handoff_id": "M22A-HANDOFF-004336",
        "edge_id": "M22B-E000181",
        "evidence_id": "M22B-EVID-000158",
        "expected_tf": "FOXH1",
        "phase2_extraction_id": "M22A-P2-NEW-NODAL-FOXH1-20260902",
        "basis": "Nodal/ACVR1C-ACVR2A handoff linked to the bounded FOXH1/SMAD2/3 Nodal-responsive target module in Xenopus embryos; CFC1 and receptor-composition differences remain outside the asserted reuse.",
    },
    {
        "link_id": "M22A22B-LINK-041",
        "handoff_id": "M22A-HANDOFF-004910",
        "edge_id": "M22B-E000284",
        "evidence_id": "M22B-EVID-000254",
        "expected_tf": "NKX2-2",
        "phase2_extraction_id": "M22A-P2-NEW-SHH-CORECEPTOR-NKX2-2-20260902",
        "basis": "SHH/BOC-associated ventral neural-progenitor program linked to the high-confidence NKX2-2/OLIG2 direct-target module; bounded to coreceptor-dependent developmental models and not treated as a BOC-specific single-gene occupancy claim.",
    },
    {
        "link_id": "M22A22B-LINK-042",
        "handoff_id": "M22A-HANDOFF-004912",
        "edge_id": "M22B-E000284",
        "evidence_id": "M22B-EVID-000254",
        "expected_tf": "NKX2-2",
        "phase2_extraction_id": "M22A-P2-NEW-SHH-CORECEPTOR-NKX2-2-20260902",
        "basis": "SHH/GAS1-associated ventral neural-progenitor program linked to the high-confidence NKX2-2/OLIG2 direct-target module; bounded to GAS1/coreceptor redundancy, developmental models, and no single-gene occupancy assignment.",
    },
    {
        "link_id": "M22A22B-LINK-043",
        "handoff_id": "M22A-HANDOFF-001287",
        "edge_id": "M22B-E000459",
        "evidence_id": "M22B-EVID-000054",
        "expected_tf": "STAT6",
        "phase2_extraction_id": "M22A-P2-NEW-IL13-STAT6-ARG1-20260902",
        "basis": "IL-13/IL4R-IL13RA1 type-II receptor handoff linked to an IL-13Ralpha1-dependent STAT6-responsive Arg1 alternative-macrophage program; bounded as pathway-program reuse without a ligand-specific STAT6-Arg1 occupancy claim.",
    },
    {
        "link_id": "M22A22B-LINK-044",
        "handoff_id": "M22A-HANDOFF-003913",
        "edge_id": "M22B-E000459",
        "evidence_id": "M22B-EVID-000054",
        "expected_tf": "STAT6",
        "phase2_extraction_id": "M22A-P2-NEW-IL13-STAT6-ARG1-20260902",
        "basis": "IL-13/IL13RA1-IL4RA type-II receptor handoff linked to an IL-13Ralpha1-dependent STAT6-responsive Arg1 alternative-macrophage program; bounded as pathway-program reuse without a ligand-specific STAT6-Arg1 occupancy claim.",
    },
    {
        "link_id": "M22A22B-LINK-045",
        "handoff_id": "M22A-HANDOFF-003918",
        "edge_id": "M22B-E000449",
        "evidence_id": "M22B-EVID-000006",
        "expected_tf": "STAT5",
        "phase2_extraction_id": "M22A-P2-NEW-IL15-CISH-20260902",
        "basis": "IL-15-induced Cish feedback in mouse NK cells linked to the high STAT5-to-Cish edge as a bounded pathway program; no IL-15-specific Cish promoter occupancy is asserted.",
    },
    {
        "link_id": "M22A22B-LINK-046",
        "handoff_id": "M22A-HANDOFF-003960",
        "edge_id": "M22B-E000449",
        "evidence_id": "M22B-EVID-000006",
        "expected_tf": "STAT5",
        "phase2_extraction_id": "M22A-P2-NEW-IL2-CISH-20260902",
        "basis": "IL-2-associated STAT5/CISH feedback in hematopoietic and human T-cell comparators, bounded across the high-affinity IL2RA/IL2RB/IL2RG receptor configuration.",
    },
    {
        "link_id": "M22A22B-LINK-047",
        "handoff_id": "M22A-HANDOFF-003961",
        "edge_id": "M22B-E000449",
        "evidence_id": "M22B-EVID-000006",
        "expected_tf": "STAT5",
        "phase2_extraction_id": "M22A-P2-NEW-IL2-CISH-20260902",
        "basis": "IL-2-associated STAT5/CISH feedback in hematopoietic and human T-cell comparators, bounded to the signaling-competent IL2RB/IL2RG receptor subcomplex.",
    },
    {
        "link_id": "M22A22B-LINK-048",
        "handoff_id": "M22A-HANDOFF-003990",
        "edge_id": "M22B-E000449",
        "evidence_id": "M22B-EVID-000006",
        "expected_tf": "STAT5",
        "phase2_extraction_id": "M22A-P2-NEW-IL7-CISH-20260902",
        "basis": "IL-7-associated STAT5 binding and Cish promoter regulation in murine lymphoid models, bounded to the tested pre-B/lymphoid context.",
    },
    {
        "link_id": "M22A22B-LINK-049",
        "handoff_id": "M22A-HANDOFF-003964",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22A-P2-NEW-IL21-SOCS3-20260902",
        "basis": "IL-21-induced Socs3 expression was STAT3-dependent in activated mouse T cells; bounded as an exact-ligand pathway program without direct IL-21-specific Socs3 occupancy.",
    },
    {
        "link_id": "M22A22B-LINK-050",
        "handoff_id": "M22A-HANDOFF-001296",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22A-P2-NEW-IL22-SOCS3-20260902",
        "basis": "IL-22 induced STAT3 activation and SOCS3 expression in IL-22-receptor-positive human epithelial tumor cells; bounded as pathway-program reuse.",
    },
    {
        "link_id": "M22A22B-LINK-051",
        "handoff_id": "M22A-HANDOFF-001301",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22A-P2-NEW-IL31-SOCS3-20260902",
        "basis": "IL-31/IL31RA-OSMR signaling induced SOCS3 feedback alongside STAT3 signaling in receptor-reconstituted systems; bounded for receptor isoforms and direct occupancy.",
    },
    {
        "link_id": "M22A22B-LINK-052",
        "handoff_id": "M22A-HANDOFF-001360",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22A-P2-NEW-LIF-SOCS3-20260902",
        "basis": "LIF-responsive STAT1/STAT3 binding and Socs3 promoter activity in mouse corticotroph cells, bounded to the LIFR-gp130 comparator mechanism.",
    },
    {
        "link_id": "M22A22B-LINK-053",
        "handoff_id": "M22A-HANDOFF-004156",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22A-P2-NEW-LIF-SOCS3-20260902",
        "basis": "LIF-responsive STAT1/STAT3 binding and Socs3 promoter activity in mouse corticotroph cells, applied to the same LIFR/gp130 receptor-label order with explicit ordering limits.",
    },
    {
        "link_id": "M22A22B-LINK-054",
        "handoff_id": "M22A-HANDOFF-001489",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22A-P2-NEW-OSM-SOCS3-20260902",
        "basis": "OSM/gp130-OSMR induced SOCS3 feedback in human hepatoma and mouse fibroblast models; bounded as a pathway program without OSM-specific STAT3 promoter occupancy.",
    },
    {
        "link_id": "M22A22B-LINK-055",
        "handoff_id": "M22A-HANDOFF-000382",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22A-P2-NEW-CTF1-SOCS3-20260902",
        "basis": "CT-1-induced STAT3 activation and subsequent SOCS3/CIS3 upregulation in rat cardiovascular tissues; bounded as a feedback program for the LIFR/gp130 handoff.",
    },
    {
        "link_id": "M22A22B-LINK-056",
        "handoff_id": "M22A-HANDOFF-000368",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22A-P2-NEW-CNTF-SOCS3-20260902",
        "basis": "CNTF-induced STAT3 activation and Socs3 expression in mouse cortical neural progenitors; bounded for methylmercury modulation, composite-receptor detail, and program-level reuse.",
    },
    {
        "link_id": "M22A22B-LINK-057",
        "handoff_id": "M22A-HANDOFF-001311",
        "edge_id": "M22B-E000449",
        "evidence_id": "M22B-EVID-000006",
        "expected_tf": "STAT5",
        "phase2_extraction_id": "M22A-P2-NEW-IL5-CISH-20260902",
        "basis": "IL-5 activated STAT5 DNA-binding activity and induced CIS1/CISH in human eosinophils; bounded to the IL5RA/CSF2RB receptor family and eosinophil context.",
    },
    {
        "link_id": "M22A22B-LINK-058",
        "handoff_id": "M22A-HANDOFF-003984",
        "edge_id": "M22B-E000449",
        "evidence_id": "M22B-EVID-000006",
        "expected_tf": "STAT5",
        "phase2_extraction_id": "M22A-P2-NEW-IL5-CISH-20260902",
        "basis": "IL-5 activated STAT5 DNA-binding activity and induced CIS1/CISH in human eosinophils; applied to the same IL5RA/CSF2RB composite with explicit common-beta-chain limits.",
    },
    {
        "link_id": "M22A22B-LINK-059",
        "handoff_id": "M22A-HANDOFF-001313",
        "edge_id": "M22B-E000449",
        "evidence_id": "M22B-EVID-000006",
        "expected_tf": "STAT5",
        "phase2_extraction_id": "M22A-P2-NEW-IL7-CISH-20260902",
        "basis": "IL-7-associated STAT5 binding and Cish promoter regulation in murine lymphoid models, applied to the exact IL7R/IL2RG handoff.",
    },
    {
        "link_id": "M22A22B-LINK-060",
        "handoff_id": "M22A-HANDOFF-001282",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22A-P2-NEW-IL11-SOCS3-20260902",
        "basis": "IL-11-associated STAT3 phosphorylation and SOCS3 feedback in human endometrial stromal cells; bounded to the IL11R/gp130 cytokine receptor family.",
    },
    {
        "link_id": "M22A22B-LINK-061",
        "handoff_id": "M22A-HANDOFF-003904",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22A-P2-NEW-IL11-SOCS3-20260902",
        "basis": "IL-11-associated STAT3 phosphorylation and SOCS3 feedback in human stromal comparators, applied to the IL11RA1/IL6ST handoff.",
    },
    {
        "link_id": "M22A22B-LINK-062",
        "handoff_id": "M22A-HANDOFF-001299",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22A-P2-NEW-IL27-SOCS3-20260902",
        "basis": "IL-27-induced STAT1/STAT3 signaling and SOCS3 expression in human lymphocyte and epithelial comparators; bounded as pathway-program reuse without SOCS3 promoter occupancy.",
    },
    {
        "link_id": "M22A22B-LINK-063",
        "handoff_id": "M22A-HANDOFF-003268",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22A-P2-NEW-IL27-SOCS3-20260902",
        "basis": "IL-27-induced STAT1/STAT3 signaling and SOCS3 expression in human lymphocyte and epithelial comparators, applied to the EBI3/IL-27 receptor-family handoff with explicit ligand-composition limits.",
    },
    {
        "link_id": "M22A22B-LINK-064",
        "handoff_id": "M22A-HANDOFF-003581",
        "edge_id": "M22B-E000449",
        "evidence_id": "M22B-EVID-000006",
        "expected_tf": "STAT5",
        "phase2_extraction_id": "M22A-P2-NEW-GH-CISH-20260902",
        "basis": "GH induced Cish expression and STAT5A binding at the Cish promoter in mature mouse 3T3-L1 adipocytes; bounded to the GHR/STAT5 adipocyte model and not asserted as SCI-cell activity.",
    },
    {
        "link_id": "M22A22B-LINK-065",
        "handoff_id": "M22A-HANDOFF-001375",
        "edge_id": "M22B-E000336",
        "evidence_id": "M22B-EVID-000620",
        "expected_tf": "RELB",
        "phase2_extraction_id": "M22A-P2-NEW-LTA1B2-RELB-20260902",
        "basis": "Membrane LT-alpha1-beta2 activated the LTBR-NIK-RELB program in cholangiocarcinoma models; bounded to RELB nuclear translocation and pathway activation without direct occupancy at a named target promoter.",
    },
    {
        "link_id": "M22A22B-LINK-066",
        "handoff_id": "M22A-HANDOFF-003178",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22A-P2-NEW-CTF1-SOCS3-20260902",
        "basis": "CT-1-induced STAT3 activation and subsequent SOCS3/CIS3 feedback in rat cardiovascular comparators, applied to the same LIFR/gp130 receptor-complex components despite reversed receptor-label order.",
    },
    {
        "link_id": "M22A22B-LINK-067",
        "handoff_id": "M22A-HANDOFF-001747",
        "edge_id": "M22B-E000449",
        "evidence_id": "M22B-EVID-000006",
        "expected_tf": "STAT5A",
        "phase2_extraction_id": "M22A-P2-NEW-TSLP-STAT5-CISH-20260902",
        "basis": "TSLP induced functional Stat5 DNA-complex formation and CIS transcription in B-lineage comparators; bounded to the TSLPR/IL-7Ralpha complex and pathway-level CISH reuse without direct Cish-promoter occupancy.",
    },
    {
        "link_id": "M22A22B-LINK-068",
        "handoff_id": "M22A-HANDOFF-005163",
        "edge_id": "M22B-E000449",
        "evidence_id": "M22B-EVID-000006",
        "expected_tf": "STAT5",
        "phase2_extraction_id": "M22A-P2-NEW-TSLP-STAT5-CISH-20260902",
        "basis": "TSLP induced functional Stat5 and CIS transcription in B-lineage/reconstituted comparators, applied to the CRLF2/IL7R handoff with receptor-abundance and leukemia-state limits.",
    },
    {
        "link_id": "M22A22B-LINK-069",
        "handoff_id": "M22A-HANDOFF-001854",
        "edge_id": "M22B-E000449",
        "evidence_id": "M22B-EVID-000006",
        "expected_tf": "STAT5",
        "phase2_extraction_id": "M22A-P2-NEW-GMCSF-CISH-20260902",
        "basis": "GM-CSF activated STAT5 and induced CIS1/CISH in human eosinophils; bounded to the CSF2RA/CSF2RB complex and eosinophil comparator program.",
    },
    {
        "link_id": "M22A22B-LINK-070",
        "handoff_id": "M22A-HANDOFF-003349",
        "edge_id": "M22B-E000449",
        "evidence_id": "M22B-EVID-000006",
        "expected_tf": "STAT5",
        "phase2_extraction_id": "",
        "basis": "Canonical EPO/EPOR signaling directly supports STAT5-dependent CIS/CISH promoter regulation in erythroid and receptor-reconstitution comparators; bounded to EPOR and erythroid context.",
    },
    {
        "link_id": "M22A22B-LINK-071",
        "handoff_id": "M22A-HANDOFF-001314",
        "edge_id": "M22B-E000449",
        "evidence_id": "M22B-EVID-000006",
        "expected_tf": "STAT5",
        "phase2_extraction_id": "M22A-P2-NEW-IL9-CIS-20260902",
        "basis": "IL-9 induced CIS and STAT-dependent signaling, with STAT5 contributing to CIS/SOCS2 induction; bounded to the IL9R/IL2RG comparator and non-exclusive STAT-subtype program.",
    },
    {
        "link_id": "M22A22B-LINK-072",
        "handoff_id": "M22A-HANDOFF-003991",
        "edge_id": "M22B-E000449",
        "evidence_id": "M22B-EVID-000006",
        "expected_tf": "STAT5",
        "phase2_extraction_id": "M22A-P2-NEW-IL9-CIS-20260902",
        "basis": "IL-9-associated CIS induction and STAT5-supported signaling program, applied to the reversed IL2RG/IL9R receptor-label order with explicit STAT1/STAT3 co-contribution limits.",
    },
    {
        "link_id": "M22A22B-LINK-079",
        "handoff_id": "M22A-HANDOFF-001908",
        "edge_id": "M22B-E000414",
        "evidence_id": "M22B-EVID-000011",
        "expected_tf": "STAT1",
        "phase2_extraction_id": "M22A-P2-NEW-IFNI-ISGF3-20260902",
        "basis": "IFN-beta-induced ISGF3/ISRE antiviral transcription supports the exact IFNB1-IFNAR1/2 receptor-family program, bounded to shared type-I interferon output.",
    },
    {
        "link_id": "M22A22B-LINK-080",
        "handoff_id": "M22A-HANDOFF-001279",
        "edge_id": "M22B-E000414",
        "evidence_id": "M22B-EVID-000011",
        "expected_tf": "STAT1",
        "phase2_extraction_id": "M22A-P2-NEW-IFNL-ISGF3-20260902",
        "basis": "IFN-lambda-induced ISGF3 activity and ISG transcription support the IFNL2-IFNLR1/IL10RB receptor-family program, bounded to the grouped lambda evidence and hepatocyte context.",
    },
    {
        "link_id": "M22A22B-LINK-081",
        "handoff_id": "M22A-HANDOFF-001280",
        "edge_id": "M22B-E000414",
        "evidence_id": "M22B-EVID-000011",
        "expected_tf": "STAT1",
        "phase2_extraction_id": "M22A-P2-NEW-IFNL-ISGF3-20260902",
        "basis": "IFN-lambda-induced ISGF3 activity and ISG transcription support the IFNL3-IFNLR1/IL10RB receptor-family program, with IFNL2/IFNL3 subtype equivalence explicitly left unresolved.",
    },
    {
        "link_id": "M22A22B-LINK-082",
        "handoff_id": "M22A-HANDOFF-001269",
        "edge_id": "M22B-E000414",
        "evidence_id": "M22B-EVID-000011",
        "expected_tf": "STAT1",
        "phase2_extraction_id": "M22A-P2-NEW-IFNA-ISGF3-20260902",
        "basis": "IFN-alpha-associated ISGF3/ISRE occupancy supports the IFNA1-IFNAR1/2 handoff as a bounded subtype-family program; target-locus selection is not claimed to be IFNA1-specific.",
    },
    {
        "link_id": "M22A22B-LINK-083",
        "handoff_id": "M22A-HANDOFF-001274",
        "edge_id": "M22B-E000414",
        "evidence_id": "M22B-EVID-000011",
        "expected_tf": "STAT1",
        "phase2_extraction_id": "M22A-P2-NEW-IFNA-ISGF3-20260902",
        "basis": "IFN-alpha-associated ISGF3/ISRE occupancy supports the IFNA2-IFNAR1/2 handoff with subtype potency and receptor-kinetic limits.",
    },
    {
        "link_id": "M22A22B-LINK-084",
        "handoff_id": "M22A-HANDOFF-001275",
        "edge_id": "M22B-E000414",
        "evidence_id": "M22B-EVID-000011",
        "expected_tf": "STAT1",
        "phase2_extraction_id": "M22A-P2-NEW-IFNA-ISGF3-20260902",
        "basis": "IFN-alpha-associated ISGF3/ISRE occupancy supports the IFNA4-IFNAR1/2 receptor-family program, bounded for species and subtype-specific occupancy.",
    },
    {
        "link_id": "M22A22B-LINK-085",
        "handoff_id": "M22A-HANDOFF-001276",
        "edge_id": "M22B-E000414",
        "evidence_id": "M22B-EVID-000011",
        "expected_tf": "STAT1",
        "phase2_extraction_id": "M22A-P2-NEW-IFNA-ISGF3-20260902",
        "basis": "IFN-alpha-associated ISGF3/ISRE occupancy supports the IFNA5-IFNAR1/2 handoff as a shared type-I interferon program, not a subtype-specific occupancy claim.",
    },
    {
        "link_id": "M22A22B-LINK-086",
        "handoff_id": "M22A-HANDOFF-001277",
        "edge_id": "M22B-E000414",
        "evidence_id": "M22B-EVID-000011",
        "expected_tf": "STAT1",
        "phase2_extraction_id": "M22A-P2-NEW-IFNA-ISGF3-20260902",
        "basis": "IFN-alpha-associated ISGF3/ISRE occupancy supports the IFNA6-IFNAR1/2 handoff; comparative potency does not establish a distinct downstream target program.",
    },
    {
        "link_id": "M22A22B-LINK-087",
        "handoff_id": "M22A-HANDOFF-001278",
        "edge_id": "M22B-E000414",
        "evidence_id": "M22B-EVID-000011",
        "expected_tf": "STAT1",
        "phase2_extraction_id": "M22A-P2-NEW-IFNA-ISGF3-20260902",
        "basis": "IFN-alpha-associated ISGF3/ISRE occupancy supports the IFNA7-IFNAR1/2 handoff, preserving exact ligand-species and receptor-kinetic limits.",
    },
    {
        "link_id": "M22A22B-LINK-088",
        "handoff_id": "M22A-HANDOFF-001908",
        "edge_id": "M22B-E000414",
        "evidence_id": "M22B-EVID-000011",
        "expected_tf": "STAT1",
        "phase2_extraction_id": "M22A-P2-NEW-IFNI-ISGF3-20260902",
        "basis": "IFN-beta-associated ISGF3/ISRE occupancy supports the exact IFNB1-IFNAR1/2 handoff as a bounded antiviral program.",
    },
    {
        "link_id": "M22A22B-LINK-089",
        "handoff_id": "M22A-HANDOFF-001279",
        "edge_id": "M22B-E000414",
        "evidence_id": "M22B-EVID-000011",
        "expected_tf": "STAT1",
        "phase2_extraction_id": "M22A-P2-NEW-IFNL-ISGF3-20260902",
        "basis": "IFN-lambda-associated ISGF3 activity and ISG transcription support the IFNL2-IFNLR1/IL10RB handoff, bounded to grouped lambda evidence and hepatocyte comparators.",
    },
    {
        "link_id": "M22A22B-LINK-090",
        "handoff_id": "M22A-HANDOFF-001280",
        "edge_id": "M22B-E000414",
        "evidence_id": "M22B-EVID-000011",
        "expected_tf": "STAT1",
        "phase2_extraction_id": "M22A-P2-NEW-IFNL-ISGF3-20260902",
        "basis": "IFN-lambda-associated ISGF3 activity and ISG transcription support the IFNL3-IFNLR1/IL10RB handoff, with IFNL2/IFNL3 subtype equivalence left unresolved.",
    },
    {
        "link_id": "M22A22B-LINK-091",
        "handoff_id": "M22A-HANDOFF-001314",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22A-P2-NEW-IL9-SOCS3-20260902",
        "basis": "IL-9-receptor mutant analysis supports a STAT1/STAT3-dependent SOCS3 branch; bounded to the IL9R/IL2RG comparator and distinct from the STAT5-supported CIS branch.",
    },
    {
        "link_id": "M22A22B-LINK-092",
        "handoff_id": "M22A-HANDOFF-003991",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22A-P2-NEW-IL9-SOCS3-20260902",
        "basis": "IL-9-associated STAT3/SOCS3 feedback supports the reversed IL2RG/IL9R handoff, with STAT1 and STAT5 contributions to other IL-9-induced inhibitors preserved.",
    },
    {
        "link_id": "M22A22B-LINK-093",
        "handoff_id": "M22A-HANDOFF-001488",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22A-P2-NEW-OSM-LIFR-SOCS3-20260902",
        "basis": "OSM induced STAT3 and Socs3 through a LIFR-dependent branch in Osmr-deficient osteoblasts; bounded to the LIFR/gp130 receptor-complex variant and species-specific ligand behavior.",
    },
    {
        "link_id": "M22A22B-LINK-094",
        "handoff_id": "M22A-HANDOFF-004439",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22A-P2-NEW-OSM-LIFR-SOCS3-20260902",
        "basis": "OSM/LIFR-dependent STAT3/Socs3 induction supports the reversed IL6ST/LIFR receptor-label order, bounded to the tested Osmr-deficient osteoblast branch.",
    },
    {
        "link_id": "M22A22B-LINK-095",
        "handoff_id": "M22A-HANDOFF-003973",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22A-P2-NEW-IL24-SOCS3-20260902",
        "basis": "IL-24 induced JAK1/STAT3 phosphorylation and SOCS3 expression in human colonic epithelial cells; bounded to the IL-20-family receptor program and epithelial comparator context.",
    },
    {
        "link_id": "M22A22B-LINK-101",
        "handoff_id": "M22A-HANDOFF-000204",
        "edge_id": "M22B-E000158",
        "evidence_id": "M22B-EVID-000622",
        "expected_tf": "ELK1",
        "phase2_extraction_id": "M22A-P2-NEW-AREG-ELK1-EGR1-20260902",
        "basis": "Amphiregulin activated EGFR-dependent Elk-1 transactivation, while EGFR-ligand/ERK signaling supports EGR1 induction in stromal comparators; bounded as a program-level AREG-EGFR-ELK1/EGR1 reuse.",
    },
    {
        "link_id": "M22A22B-LINK-102",
        "handoff_id": "M22A-HANDOFF-003150",
        "edge_id": "M22B-E000108",
        "evidence_id": "M22B-EVID-000332",
        "expected_tf": "CREB",
        "phase2_extraction_id": "M22A-P2-NEW-CRH-CREB-CFOS-20260902",
        "basis": "CRH/CRHR1 generated cAMP-dependent CREB phosphorylation and c-fos induction in hippocampal neuronal cells; bounded as a program-level CRHR1-CREB/c-FOS reuse without direct promoter occupancy.",
    },
    {
        "link_id": "M22A22B-LINK-103",
        "handoff_id": "M22A-HANDOFF-001905",
        "edge_id": "M22B-E000108",
        "evidence_id": "M22B-EVID-000332",
        "expected_tf": "CREB",
        "phase2_extraction_id": "M22A-P2-NEW-GDNF-CREB-CFOS-20260902",
        "basis": "GDNF/GFRA1-RET activated Ras/ERK-dependent CREB-family phosphorylation and c-fos transcription in mouse spermatogonial stem-cell comparators; bounded as a program-level CREB/c-FOS reuse without promoter occupancy.",
    },
    {
        "link_id": "M22A22B-LINK-104",
        "handoff_id": "M22A-HANDOFF-005137",
        "edge_id": "M22B-E000108",
        "evidence_id": "M22B-EVID-000332",
        "expected_tf": "CREB",
        "phase2_extraction_id": "M22A-P2-NEW-TRH-CREB-CFOS-20260902",
        "basis": "TRH/TRHR signaling induced CREB phosphorylation and pituitary promoter transcription, while independent primary pituitary experiments showed TRH-induced c-fos transcription; bounded as a program-level CREB/c-FOS reuse without claiming direct CREB occupancy at c-fos.",
    },
    {
        "link_id": "M22A22B-LINK-105",
        "handoff_id": "M22A-HANDOFF-001323",
        "edge_id": "M22B-E000135",
        "evidence_id": "M22B-EVID-000129",
        "expected_tf": "CREB",
        "phase2_extraction_id": "M22B-P2-R-000129-R094",
        "basis": "Insulin/IGF-I signaling through IRS-1 engaged CREB and FOXO1, while promoter reporter, mutagenesis, ChIP, and perturbation assays supported their opposing regulation of the mouse Ndn/necdin promoter; bounded to insulin-level evidence rather than Ins1-specific ligand discrimination.",
    },
    {
        "link_id": "M22A22B-LINK-106",
        "handoff_id": "M22A-HANDOFF-004689",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22A-P2-NEW-RBP4-STRA6-SOCS3-20260902",
        "basis": "Holo-RBP4/retinol activated STRA6/JAK2/STAT signaling and induced Socs3 expression in HepG2 cells and mouse adipose/muscle contexts; bounded to the retinol/CRBP1/LRAT-dependent STRA6 relay and the cell-specific STAT3/STAT5 branch.",
    },
    {
        "link_id": "M22A22B-LINK-107",
        "handoff_id": "M22A-HANDOFF-001814",
        "edge_id": "M22B-E000346",
        "evidence_id": "M22B-EVID-000016",
        "expected_tf": "SMAD1",
        "phase2_extraction_id": "M22A-P2-NEW-BMP4-ID1-20260902",
        "basis": "BMP4-induced ID1 expression and BMP4/BMPR1A/BMPR2 receptor utilization in primary human MSCs support a bounded BMP4-SMAD1/5/8-ID1 pathway reuse; direct BMP4-specific promoter occupancy is not inferred for the submitted handoff.",
    },
    {
        "link_id": "M22A22B-LINK-108",
        "handoff_id": "M22A-HANDOFF-001827",
        "edge_id": "M22B-E000346",
        "evidence_id": "M22B-EVID-000016",
        "expected_tf": "SMAD1",
        "phase2_extraction_id": "M22A-P2-NEW-BMP6-ID1-20260902",
        "basis": "BMP6-induced ID1 expression and ACVR1A/BMPR1A with ACVR2A/BMPR2 receptor-utilization evidence support a bounded BMP6-SMAD1/5/8-ID1 pathway reuse for the submitted ACVR1/ACVR2A branch.",
    },
    {
        "link_id": "M22A22B-LINK-109",
        "handoff_id": "M22A-HANDOFF-001829",
        "edge_id": "M22B-E000346",
        "evidence_id": "M22B-EVID-000016",
        "expected_tf": "SMAD1",
        "phase2_extraction_id": "M22A-P2-NEW-BMP6-ID1-20260902",
        "basis": "BMP6-induced ID1 expression and ACVR1A/BMPR1A with ACVR2A/BMPR2 receptor-utilization evidence support a bounded BMP6-SMAD1/5/8-ID1 pathway reuse for the submitted ACVR1/BMPR2 branch.",
    },
    {
        "link_id": "M22A22B-LINK-110",
        "handoff_id": "M22A-HANDOFF-001830",
        "edge_id": "M22B-E000346",
        "evidence_id": "M22B-EVID-000016",
        "expected_tf": "SMAD1",
        "phase2_extraction_id": "M22A-P2-NEW-BMP6-ID1-20260902",
        "basis": "BMP6-induced ID1 expression and ACVR1A/BMPR1A with ACVR2A/BMPR2 receptor-utilization evidence support a bounded BMP6-SMAD1/5/8-ID1 pathway reuse for the submitted BMPR1A/ACVR2A branch.",
    },
    {
        "link_id": "M22A22B-LINK-111",
        "handoff_id": "M22A-HANDOFF-001832",
        "edge_id": "M22B-E000346",
        "evidence_id": "M22B-EVID-000016",
        "expected_tf": "SMAD1",
        "phase2_extraction_id": "M22A-P2-NEW-BMP6-ID1-20260902",
        "basis": "BMP6-induced ID1 expression and ACVR1A/BMPR1A with ACVR2A/BMPR2 receptor-utilization evidence support a bounded BMP6-SMAD1/5/8-ID1 pathway reuse for the submitted BMPR1A/BMPR2 branch.",
    },
    {
        "link_id": "M22A22B-LINK-112",
        "handoff_id": "M22A-HANDOFF-000209",
        "edge_id": "M22B-E000346",
        "evidence_id": "M22B-EVID-000016",
        "expected_tf": "SMAD1",
        "phase2_extraction_id": "M22A-P2-NEW-BMP7-ID1-20260902",
        "basis": "BMP7 induced phospho-SMAD1/5/8 and Id1 expression in nephron-progenitor comparators, with BMP7 receptor-utilization evidence for the submitted BMPR1A/ACVR2A branch; bounded as a pathway-program reuse without BMP7-specific promoter occupancy or SCI transfer.",
    },
    {
        "link_id": "M22A22B-LINK-113",
        "handoff_id": "M22A-HANDOFF-000211",
        "edge_id": "M22B-E000346",
        "evidence_id": "M22B-EVID-000016",
        "expected_tf": "SMAD1",
        "phase2_extraction_id": "M22A-P2-NEW-BMP7-ID1-20260902",
        "basis": "BMP7 induced phospho-SMAD1/5/8 and Id1 expression in comparator systems, while BMPR1B-dependent BMP7 signaling was supported in a separate primary assay; bounded as a BMP7-SMAD1/5/8-ID1 pathway-program reuse rather than exact-pair promoter evidence.",
    },
    {
        "link_id": "M22A22B-LINK-114",
        "handoff_id": "M22A-HANDOFF-002971",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22A-P2-NEW-CNTF-SOCS3-20260902",
        "basis": "CNTF induced STAT3 phosphorylation and SOCS3 expression in neural-progenitor comparators; bounded to the submitted CNTFR/gp130 component and the required LIFR/CNTFRalpha receptor context.",
    },
    {
        "link_id": "M22A22B-LINK-115",
        "handoff_id": "M22A-HANDOFF-002975",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22A-P2-NEW-CNTF-SOCS3-20260902",
        "basis": "CNTF induced STAT3 phosphorylation and SOCS3 expression in neural-progenitor comparators; bounded to the submitted IL6ST/LIFR beta-receptor heterodimer with required CNTFRalpha context and no IL6ST-only inference.",
    },
    {
        "link_id": "M22A22B-LINK-116",
        "handoff_id": "M22A-HANDOFF-001799",
        "edge_id": "M22B-E000158",
        "evidence_id": "M22B-EVID-000622",
        "expected_tf": "ELK1",
        "phase2_extraction_id": "M22A-P2-NEW-AREG-ELK1-EGR1-20260902",
        "basis": "The AREG/EGFR/ERBB2 handoff is linked to the bounded AREG-EGFR/ERK/ELK1-EGR1 program supported by receptor activation, Elk-1 transactivation, and complementary EGFR-ligand EGR1 evidence; exact AREG-specific promoter occupancy is not claimed.",
    },
    {
        "link_id": "M22A22B-LINK-117",
        "handoff_id": "M22A-HANDOFF-000004",
        "edge_id": "M22B-E000288",
        "evidence_id": "M22B-EVID-000096",
        "expected_tf": "NR1H4",
        "phase2_extraction_id": "M22A-P2-NEW-22HC-FXR-CYP3A4-20260902",
        "basis": "FXR binding-site, mutation, and in vivo loss-of-receptor evidence supports reuse of the existing FXR-to-CYP3A4 target edge for the 22HC-CYP3A4 handoff; the submitted 22(R)-HC chemistry and same-cell FXR coupling remain explicitly bounded.",
    },
    {
        "link_id": "M22A22B-LINK-118",
        "handoff_id": "M22A-HANDOFF-002586",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22A-P2-NEW-APOA1-ABCA1-STAT3-SOCS3-20260902",
        "basis": "ApoA-I/ABCA1 interaction studies support an ABCA1/JAK2/STAT3 anti-inflammatory branch whose effect is SOCS3-dependent; reuse of the STAT3-to-Socs3 edge is bounded as a pathway program and does not infer direct ApoA-I/ABCA1 promoter occupancy or isolate lipid efflux from signaling.",
    },
    {
        "link_id": "M22A22B-LINK-119",
        "handoff_id": "M22A-HANDOFF-001309",
        "edge_id": "M22B-E000459",
        "evidence_id": "M22B-EVID-000010",
        "expected_tf": "STAT6",
        "phase2_extraction_id": "",
        "basis": "The high-confidence type-I IL-4 receptor/STAT6 handoff is linked to the existing high IL-4/STAT6 Arg1 promoter evidence in macrophage comparators; the type-I versus type-II receptor and cell-state boundaries remain explicit.",
    },
    {
        "link_id": "M22A22B-LINK-120",
        "handoff_id": "M22A-HANDOFF-003982",
        "edge_id": "M22B-E000459",
        "evidence_id": "M22B-EVID-000010",
        "expected_tf": "STAT6",
        "phase2_extraction_id": "",
        "basis": "The IL4RA/IL2RG type-I receptor handoff is linked to the existing high IL-4/STAT6 Arg1 promoter evidence in macrophage comparators; residual type-II receptor contribution in selected cells is preserved as a limitation.",
    },
    {
        "link_id": "M22A22B-LINK-121",
        "handoff_id": "M22A-HANDOFF-000444",
        "edge_id": "M22B-E000167",
        "evidence_id": "M22B-EVID-000105",
        "expected_tf": "ESR1",
        "phase2_extraction_id": "M22B-P2-R-000105-R093",
        "basis": "The high-confidence E2-generating HSD17B1 context is linked to the existing high ESR1/JUN-to-CYP19A1 promoter record tested with estradiol; HSD17B1 is retained as an upstream enzyme controlling E2 availability, not as an ESR1 subunit or direct receptor complex.",
    },
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def require_unique(rows: list[dict[str, str]], key: str, path: Path) -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for row in rows:
        value = row.get(key, "")
        if not value or value in result:
            raise ValueError(f"{path}: duplicate or empty {key}: {value!r}")
        result[value] = row
    return result


def main() -> None:
    handoffs = require_unique(read_tsv(HANDOFF), "module22a_handoff_id", HANDOFF)
    edges = require_unique(read_tsv(EDGE_REGISTER), "b_edge_id", EDGE_REGISTER)
    evidence = require_unique(read_tsv(EVIDENCE_REGISTER), "b_evidence_id", EVIDENCE_REGISTER)
    overlays: dict[str, dict[str, str]] = {}
    for path in OVERLAYS:
        for row in read_tsv(path):
            extraction_id = row.get("extraction_id", "")
            if not extraction_id or extraction_id in overlays:
                raise ValueError(f"{path}: duplicate or empty extraction_id: {extraction_id!r}")
            overlays[extraction_id] = row

    output_fields = [
        "link_id", "handoff_id", "pair_key", "pair_label_canonical",
        "terminal_tf_entities", "edge_id", "source_entity", "target_entity",
        "evidence_id", "evidence_source_locator", "evidence_confidence_tier",
        "phase2_extraction_id", "phase2_confidence", "link_status", "basis",
        "handoff_limitations", "edge_limitations", "evidence_limitations",
    ]
    output_rows: list[dict[str, str]] = []
    errors: list[str] = []
    for spec in LINK_SPECS:
        handoff = handoffs.get(spec["handoff_id"])
        edge = edges.get(spec["edge_id"])
        source = evidence.get(spec["evidence_id"])
        if handoff is None:
            errors.append(f"missing handoff {spec['handoff_id']}")
            continue
        if edge is None:
            errors.append(f"missing edge {spec['edge_id']}")
            continue
        if source is None:
            errors.append(f"missing evidence {spec['evidence_id']}")
            continue
        observed_terminal_tf = handoff["terminal_tf_entities"].upper()
        if observed_terminal_tf and spec["expected_tf"].upper() not in observed_terminal_tf:
            errors.append(f"{spec['link_id']}: handoff terminal TF mismatch")
        if edge["confidence_tier"].lower() != "high" or edge["exportable"] != "true":
            errors.append(f"{spec['link_id']}: edge is not high and exportable")
        if source["exportable"] != "true":
            errors.append(f"{spec['link_id']}: evidence is not exportable")
        phase2 = overlays.get(spec["phase2_extraction_id"]) if spec["phase2_extraction_id"] else None
        if spec["phase2_extraction_id"] and phase2 is None:
            errors.append(f"{spec['link_id']}: missing strict Phase-2 extraction {spec['phase2_extraction_id']}")
        if phase2 is not None and not phase2["confidence"].lower().startswith("high"):
            errors.append(f"{spec['link_id']}: Phase-2 confidence is not high")
        if source["confidence_tier"].lower() != "high" and phase2 is None:
            errors.append(f"{spec['link_id']}: no high-confidence evidence source")
        new_terminal_tf = not observed_terminal_tf or observed_terminal_tf == "NONE_FOUND"
        output_rows.append({
            "link_id": spec["link_id"],
            "handoff_id": spec["handoff_id"],
            "pair_key": handoff["pair_key"],
            "pair_label_canonical": handoff["pair_label_canonical"],
            "terminal_tf_entities": handoff["terminal_tf_entities"] or "NONE_FOUND",
            "edge_id": spec["edge_id"],
            "source_entity": edge["source_entity"],
            "target_entity": edge["target_entity"],
            "evidence_id": spec["evidence_id"],
            "evidence_source_locator": source["source_locator"],
            "evidence_confidence_tier": source["confidence_tier"] or "not_separately_tiered",
            "phase2_extraction_id": spec["phase2_extraction_id"] or "NONE_REQUIRED_SOURCE_REGISTER_HIGH",
            "phase2_confidence": phase2["confidence"] if phase2 else "not_required_source_register_high",
            "link_status": (
                "promote_existing_high_tf_target_with_new_terminal_tf_bounded_handoff"
                if new_terminal_tf
                else "promote_existing_high_tf_target_bounded_handoff"
            ),
            "basis": spec["basis"],
            "handoff_limitations": handoff["limitations"],
            "edge_limitations": edge["consolidation_note"],
            "evidence_limitations": source["limitations"] or "No additional limitation recorded in the source register.",
        })

    if errors:
        for error in errors:
            print(f"FAIL {error}")
        raise SystemExit(1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with OUT_TSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=output_fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)

    handoff_status = Counter(row["handoff_status"] for row in handoffs.values())
    terminal_status = Counter(row["terminal_tf_status"] for row in handoffs.values())
    candidate_rows = [row for row in handoffs.values() if row["handoff_status"] == "pending_tf_program_review"]
    linked_handoffs = {row["handoff_id"] for row in output_rows}
    unlinked_candidates = len(candidate_rows) - len(linked_handoffs & {row["module22a_handoff_id"] for row in candidate_rows})
    new_terminal_tf_links = sum(
        row["link_status"] == "promote_existing_high_tf_target_with_new_terminal_tf_bounded_handoff"
        for row in output_rows
    )
    lines = [
        "# Module 22A-to-22B High-Confidence Linkage Audit",
        "",
        "This audit identifies exact Module 22A handoffs that can reuse existing",
        "high-confidence Module 22B TF-target evidence. It is deliberately bounded:",
        "it does not edit the Module 22A handoff register, promote a new canonical",
        "edge, or infer SCI receiver-cell activity from comparator models.",
        "",
        "## Gate",
        "",
        "A link requires an exact handoff ID with the expected terminal TF, or an",
        "explicit bounded terminal-TF assignment when the handoff has no TF, an",
        "exportable 22B edge already marked `high`, and exportable evidence marked",
        "`high` or covered by a reviewed primary extraction marked `High`.",
        "",
        f"- Total 22A handoffs: {len(handoffs):,}",
        f"- Pending TF-program candidates: {len(candidate_rows):,}",
        f"- No-terminal-TF handoffs: {terminal_status.get('none_found', 0):,}",
        f"- Promotion-ready bounded links: {len(output_rows):,}",
        f"- Links adding an evidence-backed terminal-TF assignment: {new_terminal_tf_links:,}",
        f"- Candidate handoffs without an exact reusable high-confidence link: {unlinked_candidates:,}",
        "",
        "## Promotion-ready bounded links",
        "",
        "| Link | 22A handoff | Pair | TF | 22B edge | Target | Evidence |",
        "|---|---|---|---|---|---|---|",
    ]
    for row in output_rows:
        lines.append(
            f"| {row['link_id']} | {row['handoff_id']} | {row['pair_key']} | "
            f"{row['source_entity']} | {row['edge_id']} | {row['target_entity']} | {row['evidence_id']} |"
        )
    lines.extend([
        "",
        "## Interpretation boundary",
        "",
        "The `high` label applies to the tested direct TF-target evidence in the",
        "cited comparator systems. It does not mean that the same receptor complex",
        "produces the same target in an SCI receiver cell. IL-3 and IL-4 retain",
        "hematopoietic/macrophage model limits; IL-6 and IL-10 retain cytokine",
        "receptor/soluble-receptor and macrophage-comparator limits; EDA/EDAR and",
        "EGF/EGFR retain skin and PC3 cancer-cell limits; and BDNF/TrkB retains",
        "cortical-neuron limits. Estradiol/ESR1 retains a hypothalamic-neuron",
        "limit, TPO/MPL retains a UT7-mpl hematopoietic limit, and the IL-4",
        "rows retain an infected macrophage and alpha7nAChR co-stimulus limit. The",
        "COL1A1/DDR2 row retains its human lung-fibroblast and receptor-feedback",
        "limits. IL-35 retains an activated-T-cell and partial-receptor-signaling",
        "limit, and its link is restricted to the Il12a/Ebi3 promoter module. The",
        "Activin A links retain the ACVR1B/ALK4 gonadotrope context and the",
        "unresolved ACVR2A-versus-ACVR2B composition; they reuse the Fst enhancer",
        "edge as a bounded receptor-complex branch. The TNF/FAS link is an",
        "indirect TNF-induced RELA-to-FAS transcription chain and does not claim",
        "TNF-FAS binding or a TNF receptor-proximal interaction.",
        "BMP2 links retain the tested Id1-promoter and comparator-cell limits; the",
        "primary paper does not test every submitted type-II receptor complex,",
        "BMP-family ligand transfer, or an SCI receiver cell.",
        "IL12/STAT4 retains the CD8 T-cell and enhancer-specific limit; Nodal/FOXH1",
        "retains the Xenopus developmental target-module and receptor-composition",
        "limits; GIP/CREB retains the human adipocyte insulin co-treatment limit;",
        "leptin/STAT3 retains the hypothalamic LEPR context; PRL/STAT5 retains the",
        "mammary epithelial and glucocorticoid-cofactor context; and A2M/CREB and",
        "EDIL3/HOXD3 are explicitly bounded program-level links, with activated-A2M",
        "or alphaVbeta5 heterodimer requirements respectively. The CRH/CRHR1,",
        "GDNF/GFRA1-RET, and TRH/TRHR additions reuse the existing CREB-cFOS edge",
        "as bounded comparator programs without direct ligand-specific CREB",
        "occupancy at c-fos. Ins1/InsR is bounded to the insulin/IGF-I CREB/FOXO1",
        "recruitment study at the Ndn promoter, and RBP4/STRA6 is bounded to the",
        "holo-RBP-retinol/JAK2/STAT/SOCS3 comparator program; neither is an SCI",
        "receiver-cell claim or an isoform-specific molecular assignment.",
        "",
        f"The remaining {unlinked_candidates:,} candidate handoffs require new",
        "exact-ligand/source review or a bounded program-level assignment. The new",
        "terminal-TF assignments are RELB for EDA-EDAR and ELK1 for EGF-EGFR;",
        "the IL-10 row extends an existing STAT3 assignment to an evidence-backed",
        "target. The related IL-13 receptor-family row is not included because the",
        "strict Arg1 extraction is IL-4-specific. The 5,632 no-terminal-TF handoffs",
        "remain the broader Module 22A search-expansion pool and were not",
        "force-filled from pathway plausibility.",
        "",
        "Generated by `scripts/audit_module22a_22b_high_confidence_links.py`.",
        "",
    ])
    OUT_MD.write_text("\n".join(lines))
    print(f"links={len(output_rows)} candidate_handoffs={len(candidate_rows)} unlinked_candidates={unlinked_candidates}")


if __name__ == "__main__":
    main()
