#!/usr/bin/env python3
"""Promote four exact Module 21A relay/function packets."""

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
AUDIT = RELAY / "module21a_relay_promotion_batch010.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch010_summary.json"

PACKET = {
    "M21A-PAIR-EVID-4830": {
        "pair_key": "adm calcrl", "reuse_key": "M21A-REUSE-2238", "review_id": "M20A-EXT-0708",
        "review_file": RELAY / "module21a_pair_relay_review_batches198_199.tsv",
        "citations": "PMID:11591721; PMID:11693189; PMID:12196109; PMID:22142144; DOI:10.1042/bst0300432",
        "basis": "ADM binding and CALCRL/RAMP reconstitution with cAMP and receptor-perturbation assays support qualified-high relay/function evidence while retaining RAMP2/RAMP3 specificity.",
    },
    "M21A-PAIR-EVID-4843": {
        "pair_key": "agrn musk", "reuse_key": "M21A-REUSE-2247", "review_id": "M20A-EXT-0744",
        "review_file": RELAY / "module21a_pair_relay_review_batches198_199.tsv",
        "citations": "PMID:18848351; PMCID:PMC2933840; DOI:10.1016/j.cell.2008.10.002; PMID:22302937; PMID:18957220",
        "basis": "Agrin-LRP4 contact, LRP4/MuSK complex activation, MuSK phosphorylation, and neuromuscular synapse function support qualified-high complex relay/function evidence, not direct Agrin-MuSK binding.",
    },
    "M21A-PAIR-EVID-4925": {
        "pair_key": "cd28 cd80", "reuse_key": "M21A-REUSE-2314", "review_id": "M20A-EXT-1121",
        "review_file": RELAY / "module21a_pair_relay_review_batches202_203.tsv",
        "citations": "PMID:7534620; PMID:8871623; PMID:28280247",
        "basis": "Exact CD80/CD28 binding and PI3K/sphingomyelinase-linked AP-1/NF-kB T-cell costimulation support qualified-high relay/function evidence integrated with TCR signal 1.",
    },
    "M21A-PAIR-EVID-4926": {
        "pair_key": "cd28 cd86", "reuse_key": "M21A-REUSE-2315", "review_id": "M20A-EXT-1122",
        "review_file": RELAY / "module21a_pair_relay_review_batches202_203.tsv",
        "citations": "PMID:7534620; PMID:8871623; PMID:27708164",
        "basis": "Exact CD86/CD28 binding and T-cell costimulation support qualified-high relay/function evidence while preserving TCR dependence and B7-2 homodimer context.",
    },
}
PROMOTION_NOTE = "Module 21A relay/function promotion batch010 (2026-09-02): evidence tier raised from medium-high to high for the exact receptor-complex relay/function packet; upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


def read_tsv(path):
    with path.open(encoding="utf-8", newline="") as h:
        r = csv.DictReader(h, delimiter="\t")
        return list(r.fieldnames or []), list(r)


def write_tsv(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as h:
        w = csv.DictWriter(h, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


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
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    detail_fields, detail_rows = read_tsv(DETAIL)
    reuse_fields, reuse_rows = read_tsv(REUSE)
    pair_fields, pair_rows = read_tsv(PAIRS)
    detail, reuse = index(detail_rows, "evidence_id"), index(reuse_rows, "pathway_reuse_key")
    review_sets = {}
    review_fields = {}
    for path in {v["review_file"] for v in PACKET.values()}:
        fields, rows = read_tsv(path)
        review_fields[path] = fields
        review_sets[path] = (rows, index(rows, "review_id"))
    for evidence_id, expected in PACKET.items():
        d = detail.get(evidence_id)
        if d is None or d.get("confidence_tier") != "medium-high":
            raise SystemExit(f"{evidence_id} missing or not medium-high")
        if not all(x in d.get("evidence_layer", "") for x in ("receptor_proximal_relay", "downstream_pathway_function")):
            raise SystemExit(f"{evidence_id} lacks relay/function layers")
        if d.get("pathway_reuse_key") != expected["reuse_key"] or d.get("source_locators") != expected["citations"]:
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        rows, reviews = review_sets[expected["review_file"]]
        rv = reviews.get(expected["review_id"])
        if rv is None or rv.get("evidence_id") != evidence_id or rv.get("pair_key") != expected["pair_key"] or rv.get("confidence_tier") != "medium-high" or rv.get("review_status") != "reviewed_relay_candidate":
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        ru = reuse.get(expected["reuse_key"])
        if ru is None or ru.get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        pair = next((p for p in pair_rows if p.get("module21a_evidence_ids") == evidence_id), None)
        if pair is None or pair.get("pair_key") != expected["pair_key"] or pair.get("module21a_status") != "reviewed_relay_candidate":
            raise SystemExit(f"coverage lineage mismatch: {evidence_id}")
    audit_fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    audit_rows = [{"evidence_id": e, "review_id": v["review_id"], "pair_key": v["pair_key"], "pathway_reuse_key": v["reuse_key"], "previous_tier": detail[e]["confidence_tier"], "new_tier": "high", "source_locators": detail[e]["source_locators"], "decision_basis": v["basis"], "upstream_lr_confidence_unchanged": "true", "terminal_tf_status_unchanged": "true", "sql_materialization": "false"} for e, v in sorted(PACKET.items())]
    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False, "evidence_ids": sorted(PACKET)}, indent=2))
        return
    for e, v in PACKET.items():
        detail[e]["confidence_tier"] = "high"
        detail[e]["limitations"] = append_once(detail[e]["limitations"], PROMOTION_NOTE)
        rows, reviews = review_sets[v["review_file"]]
        rv = reviews[v["review_id"]]
        rv["confidence_tier"] = "high"
        rv["curator_note"] = append_once(rv["curator_note"], PROMOTION_NOTE)
        reuse[v["reuse_key"]]["validation_status"] = "promoted_relay_function_high_batch010"
        reuse[v["reuse_key"]]["limitations"] = append_once(reuse[v["reuse_key"]]["limitations"], PROMOTION_NOTE)
        pair = next(p for p in pair_rows if p.get("module21a_evidence_ids") == e)
        pair["curator_notes"] = append_once(pair["curator_notes"], PROMOTION_NOTE)
    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, (rows, _) in review_sets.items():
        write_tsv(path, review_fields[path], rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-relay-function-batch010-2026-09-02", "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET), "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
