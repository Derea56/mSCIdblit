#!/usr/bin/env python3
"""Promote independently verified Module 21A receptor/function packets."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELAY = ROOT / "work" / "module21_relay"
DETAIL = RELAY / "module21a_pair_relay_evidence_detail.tsv"
REUSE = RELAY / "module21a_pathway_reuse_registry.tsv"
PAIRS = RELAY / "module21a_all_pair_relay_coverage.tsv"
REVIEW_FILES = [
    RELAY / "module21a_pair_relay_review_batches032_033_034_035.tsv",
    RELAY / "module21a_pair_relay_review_batches036_037_038_039.tsv",
]
AUDIT = RELAY / "module21a_relay_promotion_batch057.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch057_summary.json"


# tuple: pair_key, reuse_key, review_id, source_locators, decision_basis, review_status
PACKET = {
    "M21A-PAIR-EVID-711": (
        "agt agtr1b", "M21A-REUSE-0448", "M20A-CELLCHAT-REMAINING-0182",
        "PMID:7614710; PMID:12176659; PMID:24370594",
        "Direct AT1B pharmacology and Gq/PLC/IP3-Ca2+/PKC receptor-proximal signaling support qualified-high promotion. Preserve the cloned AT1B evidence and distinguish downstream native AT1R work; no terminal-TF or SCI claim.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-713": (
        "aldo-cyp11b2 nr3c2", "M21A-REUSE-0449", "M20A-CELLCHAT-REMAINING-0184",
        "PMID:15967794; PMID:32652691; PMID:24491541",
        "Aldosterone-dependent NR3C2 nuclear-receptor activation and target-gene/function outputs support qualified-high promotion at the receptor/TF relay layer. CYP11B2 flux was not manipulated, and NR3C2 is the directly activated node; no direct enzyme-receptor interaction is inferred.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-714": (
        "amh amhr2_acvr1", "M21A-REUSE-0450", "M20A-CELLCHAT-REMAINING-0185",
        "PMID:11376112; PMID:20861221; PMCID:PMC7286617",
        "AMHR2/ACVR1 complex-dependent SMAD1/5/8 signaling and Mullerian-duct regression support qualified-high promotion at the exact receptor-complex relay layer. Preserve type-I-receptor redundancy and tissue context; no terminal-TF overreach.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-715": (
        "androstenedione-cyp17a1 ar", "M21A-REUSE-0451", "M20A-CELLCHAT-REMAINING-0186",
        "PMID:15522925; PMID:15336702; DOI:10.1210/jc.2004-1577",
        "Androstenedione supports partial AR ligand-binding/nuclear-receptor function and myogenic/prostate outputs. Preserve weaker activity than DHT, conversion to testosterone, and the unmanipulated CYP17A1 source branch; no direct enzyme-receptor claim.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-721": (
        "anxa1 fpr2", "M21A-REUSE-0452", "M20A-CELLCHAT-REMAINING-0192",
        "PMCID:PMC3397896; PMID:36279933; PMID:31552142",
        "ANXA1/FPR2-dependent Gi/o-Ca2+/ERK signaling and context-specific inflammatory or repair function support qualified-high promotion. Preserve ANXA1 isoform/peptide bias and cell context; no universal downstream branch, terminal TF, or SCI claim.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-724": (
        "apela aplnr", "M21A-REUSE-0453", "M20A-CELLCHAT-REMAINING-0195",
        "PMID:28817612; PMID:30631305; PMID:28904225",
        "Direct APELA/APLNR Gi-linked cAMP inhibition and ERK signaling support qualified-high promotion at the GPCR-proximal relay layer. Preserve tissue-specific endothelial metabolism and distinguish phenotypes using apelin rather than APELA; no terminal-TF claim.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-725": (
        "apoa1 cubn_amn", "M21A-REUSE-0454", "M20A-CELLCHAT-REMAINING-0196",
        "DOI:10.1038/nm0699_656; PMCID:PMC17859; PMID:24357674",
        "ApoA1 binding to the CUBN/AMN membrane complex and megalin-assisted endocytosis/reabsorption support qualified-high promotion at the exact uptake/function layer. This is not a kinase relay; preserve intestinal epithelial complex and processing context.",
        "reviewed_function_only",
    ),
    "M21A-PAIR-EVID-728": (
        "apob apobr", "M21A-REUSE-0455", "M20A-CELLCHAT-REMAINING-0199",
        "PMCID:PMC16572; PMID:10638201; PMID:9633939",
        "ApoB48/apoB-containing lipoprotein uptake through APOBR and foam-cell function support qualified-high promotion at the exact scavenging/function layer. Preserve apoB isoform and particle context; no intracellular kinase or terminal-TF claim.",
        "reviewed_function_only",
    ),
    "M21A-PAIR-EVID-730": (
        "apoe trem2_tyrobp", "M21A-REUSE-0456", "M20A-CELLCHAT-REMAINING-0201",
        "PMID:26374899; PMCID:PMC4646257; PMID:27477018; PMID:10799849",
        "ApoE-dependent TREM2/TYROBP complex function and microglial uptake/phagocytosis support qualified-high promotion at the ligand-complex/function layer. Do not assert every TYROBP/SYK step as a same-experiment relay; no terminal-TF or SCI claim.",
        "reviewed_function_only",
    ),
    "M21A-PAIR-EVID-731": (
        "app sorl1", "M21A-REUSE-0457", "M20A-CELLCHAT-REMAINING-0202",
        "PMID:27466343; PMID:28799085; PMID:35226190",
        "APP-SORL1 cargo sorting/recycling and Aβ-processing function support qualified-high promotion at the exact trafficking/function layer. This is not receptor-proximal kinase signaling and does not support a terminal-TF claim.",
        "reviewed_function_only",
    ),
    "M21A-PAIR-EVID-733": (
        "b-endorphin-pomc oprd1", "M21A-REUSE-0458", "M20A-CELLCHAT-REMAINING-0205",
        "PMID:1328614; PMID:8942644; PMID:1963478",
        "Mature beta-endorphin activation of OPRD1 with Gi/o-linked adenylyl-cyclase inhibition and cAMP reduction supports qualified-high promotion at the receptor-proximal relay layer. Preserve nonselective beta-endorphin/POMC processing and tissue context; no terminal-TF claim.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-735": (
        "b-endorphin-pomc oprm1", "M21A-REUSE-0459", "M20A-CELLCHAT-REMAINING-0207",
        "PMID:9689128; PMID:23348513",
        "Mature beta-endorphin-dependent OPRM1 Gi/o-GIRK neuronal inhibition supports qualified-high promotion at the receptor-proximal relay layer. Preserve species/receptor-variant dependence and POMC precursor boundaries; no terminal-TF claim.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-739": (
        "cadm1 nectin3", "M21A-REUSE-0460", "M20A-CELLCHAT-REMAINING-0230",
        "PMID:22703826; PMID:24465823; PMCID:PMC3631237",
        "Exact CADM1-nectin-3 cell adhesion, mast-cell attachment, and measured Ca2+ function support qualified-high promotion at the adhesion/function layer. The molecular intracellular relay is unresolved; no terminal-TF or SCI claim.",
        "reviewed_function_only",
    ),
    "M21A-PAIR-EVID-740": (
        "cadm3 cadm3", "M21A-REUSE-0461", "M20A-CELLCHAT-REMAINING-0231",
        "PMID:37022761; https://rupress.org/jcb/article/222/6/e202204098/214005",
        "Homophilic CADM3 adhesion and retinal neuroepithelial proliferation support qualified-high promotion at the exact adhesion/function layer. No receptor-proximal relay or terminal-TF claim is made.",
        "reviewed_function_only",
    ),
    "M21A-PAIR-EVID-741": (
        "cadm3 cadm4", "M21A-REUSE-0462", "M20A-CELLCHAT-REMAINING-0232",
        "PMID:30585357; PMID:27658374; PMCID:PMC5073025",
        "Exact CADM3-CADM4 axon-Schwann adhesion and myelination function support qualified-high promotion at the adhesion/function layer. Preserve the ErbB3/PI3K-Akt association as context-specific rather than a complete pair-specific relay; no terminal-TF claim.",
        "reviewed_function_only",
    ),
}

PROMOTION_NOTE = (
    "Module 21A relay/function promotion batch057 (2026-09-02): evidence tier raised to high for the exact, context-bounded receptor, uptake, trafficking, or adhesion packet; upstream Module 20A confidence, evidence-layer scope, terminal-TF status, and SCI transfer remain unchanged."
)


def read_tsv(path: Path):
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def write_tsv(path: Path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def index(rows, key):
    result = {}
    for row in rows:
        value = row.get(key, "")
        if value and value in result:
            raise SystemExit(f"duplicate {key}: {value}")
        if value:
            result[value] = row
    return result


def append_once(value, note):
    return value if note in value else f"{value} {note}".strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    detail_fields, detail_rows = read_tsv(DETAIL)
    reuse_fields, reuse_rows = read_tsv(REUSE)
    pair_fields, pair_rows = read_tsv(PAIRS)
    review_tables = [read_tsv(path) for path in REVIEW_FILES]
    review_fields = [fields for fields, _ in review_tables]
    review_rows_by_file = [rows for _, rows in review_tables]
    detail = index(detail_rows, "evidence_id")
    reuse = index(reuse_rows, "pathway_reuse_key")
    reviews = index([row for rows in review_rows_by_file for row in rows], "review_id")
    coverage = {
        evidence_id: next(
            (row for row in pair_rows if row.get("module21a_evidence_ids") == evidence_id), None
        )
        for evidence_id in PACKET
    }

    for evidence_id, (pair_key, reuse_key, review_id, citations, _basis, review_status) in PACKET.items():
        row = detail.get(evidence_id)
        if (
            row is None
            or row.get("confidence_tier") not in {"medium", "medium-high"}
            or row.get("pathway_reuse_key") != reuse_key
            or row.get("source_locators") != citations
        ):
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        if not any(layer in row.get("evidence_layer", "") for layer in (
            "receptor_proximal_relay", "downstream_pathway_function", "ligand_receptor_binding_or_activation"
        )):
            raise SystemExit(f"{evidence_id} lacks a supported evidence layer")
        review = reviews.get(review_id)
        if (
            review is None
            or review.get("evidence_id") != evidence_id
            or review.get("pair_key") != pair_key
            or review.get("source_locators") != citations
            or review.get("confidence_tier") not in {"medium", "medium-high"}
            or review.get("review_status") != review_status
        ):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        if coverage[evidence_id] is None or coverage[evidence_id].get("pair_key") != pair_key or coverage[evidence_id].get("module21a_status") != review_status:
            raise SystemExit(f"coverage lineage mismatch: {evidence_id}")

    audit_fields = [
        "evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier",
        "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged",
        "terminal_tf_status_unchanged", "sql_materialization",
    ]
    audit_rows = [
        {
            "evidence_id": evidence_id,
            "review_id": packet[2],
            "pair_key": packet[0],
            "pathway_reuse_key": packet[1],
            "previous_tier": detail[evidence_id]["confidence_tier"],
            "new_tier": "high",
            "source_locators": detail[evidence_id]["source_locators"],
            "decision_basis": packet[4],
            "upstream_lr_confidence_unchanged": "true",
            "terminal_tf_status_unchanged": "true",
            "sql_materialization": "false",
        }
        for evidence_id, packet in sorted(PACKET.items())
    ]
    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False, "evidence_ids": sorted(PACKET)}, indent=2))
        return

    for evidence_id, packet in PACKET.items():
        detail[evidence_id]["confidence_tier"] = "high"
        detail[evidence_id]["limitations"] = append_once(detail[evidence_id]["limitations"], PROMOTION_NOTE)
        review = reviews[packet[2]]
        review["confidence_tier"] = "high"
        review["curator_note"] = append_once(review["curator_note"], PROMOTION_NOTE)
        reuse[packet[1]]["validation_status"] = "promoted_high_batch057"
        reuse[packet[1]]["limitations"] = append_once(reuse[packet[1]]["limitations"], PROMOTION_NOTE)
        coverage[evidence_id]["curator_notes"] = append_once(coverage[evidence_id]["curator_notes"], PROMOTION_NOTE)

    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, fields, rows in zip(REVIEW_FILES, review_fields, review_rows_by_file):
        write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(
        json.dumps(
            {
                "promotion_id": "module21a-relay-function-batch057-2026-09-02",
                "records_promoted": len(audit_rows),
                "evidence_ids": sorted(PACKET),
                "promotion_note": PROMOTION_NOTE,
                "upstream_module20a_lr_confidence_changed": False,
                "terminal_tf_assignments_created": False,
                "sql_signaling_edges_created": False,
                "malformed_legacy_rows_touched": False,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
