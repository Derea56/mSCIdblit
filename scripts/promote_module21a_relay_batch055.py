#!/usr/bin/env python3
"""Promote the eight bounded Module 21A packets from EVID-5680--5699."""

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
    RELAY / "module21a_pair_relay_review_batches232.tsv",
    RELAY / "module21a_pair_relay_review_batches233.tsv",
]
AUDIT = RELAY / "module21a_relay_promotion_batch055.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch055_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5681": (
        "vcan tlr2",
        "M21A-REUSE-2769",
        "M20A-EXT-3416",
        "PMID:19122641; PMCID:PMC2746432; PMCID:PMC12247142",
        "Versican-associated TLR2/TLR6/CD14 activation with MyD88 and RelB inflammatory/function outputs supports qualified-high promotion; preserve hyaluronan or matrix co-presentation, receptor-complex composition, mouse carcinoma-associated myeloid context, and RelB as a provisional measured endpoint rather than a universal TF claim.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-5682": (
        "vegfa cd44",
        "M21A-REUSE-2770",
        "M20A-EXT-3419",
        "PMCID:PMC4721543",
        "VEGF165-CD44v6 binding and VEGFR2 co-receptor function with migration/sprouting outputs support qualified-high promotion; preserve CD44v6 rather than generic CD44, VEGFR2 dependence, and human/recombinant cell-context boundaries.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-5685": (
        "vegfb nrp1",
        "M21A-REUSE-2772",
        "M20A-EXT-3434",
        "DOI:10.1074/jbc.274.30.21217; PMID:26483474",
        "VEGF-B isoform-dependent NRP1 binding and NRP1-dependent vascular/neuronal developmental function support qualified-high promotion; preserve VEGF-B167/VEGF-B186 processing, zebrafish and recombinant contexts, and NRP1 as a non-kinase co-receptor.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-5687": (
        "vim cd44",
        "M21A-REUSE-2774",
        "M20A-EXT-3444",
        "PMID:22216242; PMCID:PMC3244446",
        "Cell-surface vimentin association with CD44 and CD44-dependent endothelial internalization supports qualified-high promotion at the atypical uptake/function layer; preserve surface vimentin and endothelial model context, without converting it to canonical soluble ligand-receptor signaling.",
        "reviewed_function_only",
    ),
    "M21A-PAIR-EVID-5693": (
        "vwf lrp1",
        "M21A-REUSE-2780",
        "M20A-EXT-3472",
        "PMID:22812646; PMID:35596664; DOI:10.1111/j.1538-7836.2012.04860.x",
        "Activated or conformationally exposed VWF recognition by LRP1 with shear-dependent macrophage uptake and plasma-clearance function supports qualified-high promotion at the scavenging layer; preserve VWF variant/FVIII, shear, and conformation dependence, with no kinase-relay or TF claim.",
        "reviewed_scavenging_only",
    ),
    "M21A-PAIR-EVID-5697": (
        "wnt1 ror2",
        "M21A-REUSE-2784",
        "M20A-EXT-3483",
        "PMID:18762249",
        "Wnt1-dependent ROR2/TAK1 modulation, ROR2 phosphorylation, and model-bounded Wnt function support qualified-high promotion; preserve the incomplete extracellular contact map, ROR2/TAK1 context, and absence of a sole-receptor or terminal-TF claim.",
        "reviewed_relay_candidate",
    ),
    "M21A-PAIR-EVID-5698": (
        "thbs1 ptprj",
        "M21A-REUSE-2785",
        "M20A-EXT-3288",
        "PMID:27149518; PMCID:PMC4858292; DOI:10.1371/journal.pone.0154916",
        "THBS1 type-1-repeat binding to catalytically competent PTPRJ/CD148 with growth-inhibition function supports qualified-high promotion at the direct binding/function layer; preserve the fragment and human A431D context, without assigning an intracellular substrate, kinase relay, SCI function, or terminal TF.",
        "reviewed_function_only",
    ),
    "M21A-PAIR-EVID-5699": (
        "thbs2 itga6",
        "M21A-REUSE-2786",
        "M20A-EXT-3292",
        "PMID:12909644; DOI:10.1074/jbc.M302014200",
        "THBS2 N-terminal module engagement of the alpha6beta1 integrin complex with endothelial adhesion/chemotaxis supports qualified-high promotion at the heterodimeric function layer; preserve alpha6beta1, activation state, matrix presentation, and N-terminal module boundaries, without an ITGA6-only relay or TF claim.",
        "reviewed_function_only",
    ),
}

PROMOTION_NOTE = (
    "Module 21A relay/function promotion batch055 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."
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
            (row for row in pair_rows if row.get("module21a_evidence_ids") == evidence_id),
            None,
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
        if "downstream_pathway_function" not in row.get("evidence_layer", ""):
            raise SystemExit(f"{evidence_id} lacks downstream function layer")
        if review_status == "reviewed_relay_candidate" and "receptor_proximal_relay" not in row.get("evidence_layer", ""):
            raise SystemExit(f"{evidence_id} lacks receptor-proximal relay layer")
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
        reuse[packet[1]]["validation_status"] = "promoted_high_batch055"
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
                "promotion_id": "module21a-relay-function-batch055-2026-09-02",
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
