#!/usr/bin/env python3
"""Promote a conservative exact-pair subset from Module 21A lanes 5211-5310."""

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
    RELAY / "module21a_pair_relay_review_batches212_213.tsv",
    RELAY / "module21a_pair_relay_review_batches214_215.tsv",
    RELAY / "module21a_pair_relay_review_batches216_217.tsv",
]
AUDIT = RELAY / "module21a_relay_promotion_batch114.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch114_summary.json"

PACKET = [
    (5216, "M20A-EXT-1721", ""),
    (5249, "M20A-EXT-1754", "M21A-REUSE-2449"),
    (5252, "M20A-EXT-1757", "M21A-REUSE-2451"),
    (5253, "M20A-EXT-1758", "M21A-REUSE-2452"),
    (5262, "M20A-EXT-1767", "M21A-REUSE-2455"),
    (5270, "M20A-EXT-1780", "M21A-REUSE-2459"),
    (5271, "M20A-EXT-1781", "M21A-REUSE-2460"),
    (5276, "M20A-EXT-1787", "M21A-REUSE-2463"),
    (5289, "M20A-EXT-1807", "M21A-REUSE-2469"),
    (5296, "M20A-EXT-1935", "M21A-REUSE-2475"),
    (5297, "M20A-EXT-1938", ""),
    (5303, "M20A-EXT-1950", "M21A-REUSE-2477"),
    (5308, "M20A-EXT-1969", "M21A-REUSE-2481"),
]

NOTE = (
    "Module 21A qualified-relay promotion batch114 (2026-09-02): exact FSHR, "
    "megalin/LRP2 uptake, Activin/Nodal receptor-complex, GDF5 receptor-complex, "
    "GH/PRLR, GPC3/UNC5C recognition, progranulin/sortilin trafficking, and "
    "MHC-II/CD4 coreceptor evidence is raised to high only at the recorded "
    "supported layer. Ligand-form, receptor-complex, adaptor, scavenging, "
    "species/model, assay, and no-SCI boundaries remain explicit; no terminal-TF "
    "claim or SQL signaling edge is created."
)

BASIS = {
    5216: "Intact FSH(CGA/FSHB) directly engages FSHR; promotion is binding-only and retains the heterodimer boundary, with no isolated FSHB relay or TF claim.",
    5249: "GC/DBP-containing vitamin-D complex uptake through megalin/LRP2 in a cubilin-associated system supports high at the exact endocytic/scavenging layer; no standalone GC-LRP2 soluble-ligand or kinase relay claim.",
    5252: "GDF1-containing CFC1/Cripto-dependent Activin/Nodal receptor-context evidence supports ACVR1B/ACVR2A binding/relay/function; heterodimer, CFC1, and developmental-context boundaries remain explicit.",
    5253: "GDF1-containing CFC1/Cripto-dependent Activin/Nodal receptor-context evidence supports ACVR1B/ACVR2B binding/relay/function; heterodimer, CFC1, and developmental-context boundaries remain explicit.",
    5262: "GDF11 ACVR2A/ACVR1B receptor-context binding and SMAD2/3 function support high at the recorded composite relay; alternate activin-class type-I receptor usage is not collapsed.",
    5270: "GDF3 CFC1/Cripto-dependent ACVR1B/ACVR2A receptor-complex binding and reporter/developmental function support high at the exact recorded topology; no broader GDF3 receptor map is inferred.",
    5271: "GDF3 CFC1/Cripto-dependent ACVR1B/ACVR2B receptor-complex binding and reporter/developmental function support high at the exact recorded topology; no broader GDF3 receptor map is inferred.",
    5276: "GDF5 BMPR1A/ACVR2B receptor-complex binding and osteoprogenitor function support high at the exact composite; preserve BMPR1A/BMPR2 subtype and quantitative-affinity boundaries.",
    5289: "Human GH directly binds and activates PRLR as a cross-reactive lactogenic receptor; promotion is limited to the recorded receptor-proximal layer and does not infer a canonical GH receptor or terminal TF.",
    5296: "GPC3-LRP1 binding and LRP1-mediated uptake of the GPC3-Shh complex support high at the exact endocytic/scavenging layer; heparan-sulfate and Shh-complex dependence remain explicit.",
    5297: "GPC3 interacts with UNC5-family guidance receptors and exact UNC5C recognition is recorded; promotion is binding-only and does not infer an UNC5C intracellular relay.",
    5303: "Progranulin-SORT1 binding and sortilin-dependent endocytosis/lysosomal trafficking support high at the exact uptake/trafficking layer; no autonomous SORT1 signaling or terminal-TF claim.",
    5308: "MHC-II/CD4 coreceptor engagement with CD4/Lck and TCR-proximal activation supports high at the recorded pMHC-II/CD4 layer; H2-Aa is retained as part of the MHC-II complex and no autonomous H2-Aa relay is inferred.",
}


def read(path):
    with path.open(encoding="utf-8", newline="") as handle:
        r = csv.DictReader(handle, delimiter="\t")
        return list(r.fieldnames or []), list(r)


def write(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        w = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def index(rows, key):
    out = {}
    for row in rows:
        value = row.get(key, "")
        if value and value in out:
            raise SystemExit(f"duplicate {key}: {value}")
        if value:
            out[value] = row
    return out


def tokens(value):
    return {x.strip() for x in value.split(";") if x.strip()}


def once(value):
    return value if NOTE in value else f"{value} {NOTE}".strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    detail_fields, detail_rows = read(DETAIL)
    reuse_fields, reuse_rows = read(REUSE)
    pair_fields, pair_rows = read(PAIRS)
    review_tables = [read(path) for path in REVIEW_FILES]
    reviews = index([row for _, rows in review_tables for row in rows], "review_id")
    detail = index(detail_rows, "evidence_id")
    reuse = index(reuse_rows, "pathway_reuse_key")
    coverage = {}
    audit = []

    for number, review_id, reuse_key in PACKET:
        evidence_id = f"M21A-PAIR-EVID-{number}"
        row = detail.get(evidence_id)
        review = reviews.get(review_id)
        if row is None or row.get("confidence_tier") not in {"medium", "medium-high"}:
            raise SystemExit(f"detail tier mismatch: {evidence_id}")
        if not tokens(row.get("evidence_layer", "")) & {
            "binding_activation", "ligand_receptor_binding_or_activation",
            "receptor_proximal_relay", "downstream_pathway_function",
        }:
            raise SystemExit(f"detail layer mismatch: {evidence_id}")
        if row.get("pathway_reuse_key", "") != reuse_key:
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        if review is None or review.get("evidence_id") != evidence_id:
            raise SystemExit(f"review identity mismatch: {evidence_id}")
        if review.get("pathway_reuse_key", "") != reuse_key or review.get("source_locators") != row.get("source_locators"):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if review.get("review_status") not in {
            "reviewed_relay_candidate", "reviewed_binding_only", "reviewed_function_only", "reviewed_scavenging_only",
        }:
            raise SystemExit(f"review status mismatch: {evidence_id}")
        if reuse_key and (reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id):
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        matching = [
            pair for pair in pair_rows
            if evidence_id in tokens(pair.get("module21a_evidence_ids", ""))
            and pair.get("pair_key") == review.get("pair_key")
        ]
        if len(matching) != 1:
            raise SystemExit(f"coverage mapping mismatch: {evidence_id}")
        pair = matching[0]
        coverage[evidence_id] = pair
        if pair.get("module21a_status") != review.get("review_status"):
            raise SystemExit(f"coverage status mismatch: {evidence_id}")
        if pair.get("module22a_status") != "no_terminal_tf_evidence":
            raise SystemExit(f"TF-boundary mismatch: {evidence_id}")
        hits = []
        for path in RELAY.glob("module21a_relay_promotion_batch*.tsv"):
            if path == AUDIT:
                continue
            for candidate in read(path)[1]:
                if candidate.get("evidence_id") == evidence_id or candidate.get("pair_key") == review["pair_key"]:
                    hits.append(path.name)
                    break
        if hits:
            raise SystemExit(f"promotion overlap for {evidence_id}: {hits}")
        audit.append({
            "evidence_id": evidence_id,
            "review_id": review_id,
            "pair_key": review["pair_key"],
            "pathway_reuse_key": reuse_key,
            "previous_tier": row["confidence_tier"],
            "new_tier": "high",
            "source_locators": row["source_locators"],
            "decision_basis": BASIS[number],
            "upstream_lr_confidence_unchanged": "true",
            "terminal_tf_status_unchanged": "true",
            "sql_materialization": "false",
        })

    if not args.apply:
        print(json.dumps({"validated": len(audit), "apply": False, "evidence_ids": [x["evidence_id"] for x in audit]}, indent=2))
        return

    for number, review_id, reuse_key in PACKET:
        evidence_id = f"M21A-PAIR-EVID-{number}"
        detail[evidence_id]["confidence_tier"] = "high"
        detail[evidence_id]["limitations"] = once(detail[evidence_id]["limitations"])
        reviews[review_id]["confidence_tier"] = "high"
        reviews[review_id]["curator_note"] = once(reviews[review_id]["curator_note"])
        if reuse_key:
            reuse[reuse_key]["validation_status"] = "promoted_high_batch114"
            reuse[reuse_key]["limitations"] = once(reuse[reuse_key]["limitations"])
        coverage[evidence_id]["curator_notes"] = once(coverage[evidence_id]["curator_notes"])

    write(DETAIL, detail_fields, detail_rows)
    write(REUSE, reuse_fields, reuse_rows)
    write(PAIRS, pair_fields, pair_rows)
    for path, (fields, rows) in zip(REVIEW_FILES, review_tables):
        write(path, fields, rows)
    audit_fields = [
        "evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier",
        "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged",
        "terminal_tf_status_unchanged", "sql_materialization",
    ]
    write(AUDIT, audit_fields, audit)
    SUMMARY.write_text(json.dumps({
        "promotion_id": "module21a-local-register-exact-pair-batch114-2026-09-02",
        "records_promoted": len(audit),
        "evidence_ids": [x["evidence_id"] for x in audit],
        "promotion_note": NOTE,
        "upstream_module20a_lr_confidence_changed": False,
        "terminal_tf_assignments_created": False,
        "sql_signaling_edges_created": False,
        "malformed_legacy_rows_touched": False,
    }, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit), "applied": len(audit), "evidence_ids": [x["evidence_id"] for x in audit]}, indent=2))


if __name__ == "__main__":
    main()
