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
    RELAY / "module21a_pair_relay_review_batches040_041.tsv",
    RELAY / "module21a_pair_relay_review_batches042_043_044_045.tsv",
]
AUDIT = RELAY / "module21a_relay_promotion_batch059.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch059_summary.json"


# tuple: pair_key, reuse_key, review_id, source_locators, decision_basis, review_status
PACKET = {
    "M21A-PAIR-EVID-863": (
        "ctsg f2rl3", "M21A-REUSE-0507", "M20A-CELLCHAT-REMAINING-0386",
        "PMID:10702240; PMID:17142351; PMID:41370205; DOI:10.1074/jbc.275.10.6819",
        "Human PAR4/F2RL3 proteolytic activation by cathepsin G with G-alpha-q/Ca2+, Akt/RhoA, and platelet outputs supports qualified-high promotion at the exact proteolytic receptor-relay layer. Preserve human PAR4, biased G-protein, and cell-context boundaries; no terminal-TF or SCI claim.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-864": (
        "ctsg fpr1", "M21A-REUSE-0508", "M20A-CELLCHAT-REMAINING-0387",
        "PMID:15210802; DOI:10.4049/jimmunol.173.1.428; PMCID:PMC3464519",
        "FPR1-dependent chemotaxis, internalization, and phagocyte effector function support qualified-high promotion at the exact receptor-proximal relay layer. Preserve the unresolved distinction between direct cathepsin-G agonism and secondary FPR agonist generation; no terminal-TF or SCI claim.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-904": (
        "e2-cyp19a1 esr1", "M21A-REUSE-0524", "M20A-CELLCHAT-REMAINING-0440",
        "PMID:12554768; PMID:9278514; PMID:25617485; DOI:10.1210/me.2002-0331",
        "Mature 17-beta-estradiol activation of ESR1 with receptor-domain/transcriptional function supports qualified-high promotion at the direct receptor/TF relay layer. Preserve CYP19A1 as biosynthetic context rather than an ESR1 subunit; no direct enzyme-receptor complex or new terminal-TF assignment.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-905": (
        "e2-cyp19a1 esr2", "M21A-REUSE-0525", "M20A-CELLCHAT-REMAINING-0441",
        "PMID:9292936; PMID:12554768; PMID:9278514; DOI:10.1210/me.2002-0331",
        "Mature 17-beta-estradiol activation of ESR2 with ligand-binding, coactivator recruitment, and reporter function supports qualified-high promotion at the direct receptor/TF relay layer. Preserve CYP19A1 as biosynthetic context rather than an ESR2 subunit and retain species/receptor-domain boundaries; no new terminal-TF assignment.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-906": (
        "e2-cyp19a1 gper1", "M21A-REUSE-0526", "M20A-CELLCHAT-REMAINING-0442",
        "PMID:34069403; PMID:22306083; PMCID:PMC3474542",
        "Mature E2/E2-BSA, GPER1 blockade/knockdown, cAMP/ERK/p38 signaling, and cellular function support qualified-high promotion at the GPER1 relay layer. Preserve CYP19A1 as biosynthetic context and CREB/c-Jun as measured pathway outputs rather than new terminal-TF assignments.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-908": (
        "e2-hsd17b1 esr1", "M21A-REUSE-0527", "M20A-CELLCHAT-REMAINING-0444",
        "PMID:25617485; PMID:12554768; PMID:9278514; DOI:10.1016/j.cbi.2015.01.008",
        "Mature E2 activation of ESR1 with HSD17B1-dependent estrogen-response amplitude supports qualified-high promotion at the direct receptor/TF relay layer. Preserve HSD17B1 as E1/E2 biosynthetic context rather than an ESR1 subunit; no direct enzyme-receptor complex or new terminal-TF assignment.",
        "reviewed_relay_candidate",
    ),
}

PROMOTION_NOTE = (
    "Module 21A relay/function promotion batch059 (2026-09-02): evidence tier raised to high for the exact, context-bounded proteolytic GPCR or mature-ligand receptor packet; biosynthetic enzyme context, terminal-TF status, evidence-layer scope, upstream Module 20A confidence, and SCI transfer remain unchanged."
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
        reuse[packet[1]]["validation_status"] = "promoted_high_batch059"
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
                "promotion_id": "module21a-relay-function-batch059-2026-09-02",
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
