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
            "terminal_tf_entities": handoff["terminal_tf_entities"],
            "edge_id": spec["edge_id"],
            "source_entity": edge["source_entity"],
            "target_entity": edge["target_entity"],
            "evidence_id": spec["evidence_id"],
            "evidence_source_locator": source["source_locator"],
            "evidence_confidence_tier": source["confidence_tier"],
            "phase2_extraction_id": spec["phase2_extraction_id"],
            "phase2_confidence": phase2["confidence"] if phase2 else "",
            "link_status": (
                "promote_existing_high_tf_target_with_new_terminal_tf_bounded_handoff"
                if new_terminal_tf
                else "promote_existing_high_tf_target_bounded_handoff"
            ),
            "basis": spec["basis"],
            "handoff_limitations": handoff["limitations"],
            "edge_limitations": edge["consolidation_note"],
            "evidence_limitations": source["limitations"],
        })

    if errors:
        for error in errors:
            print(f"FAIL {error}")
        raise SystemExit(1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with OUT_TSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=output_fields, delimiter="\t")
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
        "BMP2 links retain the tested Id1-promoter and comparator-cell limits; the",
        "primary paper does not test every submitted type-II receptor complex,",
        "BMP-family ligand transfer, or an SCI receiver cell.",
        "IL12/STAT4 retains the CD8 T-cell and enhancer-specific limit; Nodal/FOXH1",
        "retains the Xenopus developmental target-module and receptor-composition",
        "limits; GIP/CREB retains the human adipocyte insulin co-treatment limit;",
        "leptin/STAT3 retains the hypothalamic LEPR context; PRL/STAT5 retains the",
        "mammary epithelial and glucocorticoid-cofactor context; and A2M/CREB and",
        "EDIL3/HOXD3 are explicitly bounded program-level links, with activated-A2M",
        "or alphaVbeta5 heterodimer requirements respectively.",
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
