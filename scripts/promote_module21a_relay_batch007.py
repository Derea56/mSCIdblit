#!/usr/bin/env python3
"""Promote five exact Module 21A chemokine/growth-factor relay packets."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELAY = ROOT / "work" / "module21_relay"
DETAIL = RELAY / "module21a_pair_relay_evidence_detail.tsv"
REVIEW = RELAY / "module21a_pair_relay_review_batches192_193.tsv"
REUSE = RELAY / "module21a_pathway_reuse_registry.tsv"
PAIRS = RELAY / "module21a_all_pair_relay_coverage.tsv"
AUDIT = RELAY / "module21a_relay_promotion_batch007.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch007_summary.json"

PACKET = {
    "M21A-PAIR-EVID-4704": ("ccl8 ccr5", "M21A-REUSE-2161", "M20A-CELLCHAT-REMAINING-0274", "DOI:10.1006/cimm.1998.1379; URL:https://academic.oup.com/jid/article/185/8/1174/817869; PMCID:PMC1573204", "CCL8/CCR5 binding, Gi/o-sensitive calcium, chemotaxis, and CCR5-linked functional assays support the exact chemokine relay."),
    "M21A-PAIR-EVID-4709": ("csf1 csf1r", "M21A-REUSE-2164", "M20A-CELLCHAT-REMAINING-0381", "PMID:3029775; PMCID:PMC304408; PMID:22153499; PMCID:PMC3260422", "CSF1/CSF1R complex assembly, receptor autophosphorylation, and myeloid survival/proliferation/differentiation function support the exact RTK relay."),
    "M21A-PAIR-EVID-4714": ("cxcl11 cxcr3", "M21A-REUSE-2165", "M20A-CELLCHAT-REMAINING-0393", "PMID:15273303; PMCID:PMC2279818; PMID:12750173; PMID:15150261; PMID:17363734", "CXCL11/CXCR3 binding and activation, Gi/o/PLC-calcium signaling, and T-cell chemotaxis support the exact chemokine relay."),
    "M21A-PAIR-EVID-4721": ("cxcl9 cxcr3", "M21A-REUSE-2166", "M20A-CELLCHAT-REMAINING-0401", "PMID:16847335; PMID:15150261; PMID:12750173; DOI:10.1182/blood-2002-12-3945", "CXCL9/CXCR3 binding, receptor-domain dependence, Gi/o/PLC-calcium signaling, and activated-T-cell chemotaxis support the exact relay."),
    "M21A-PAIR-EVID-4722": ("egf egfr", "M21A-REUSE-2167", "M20A-CELLCHAT-REMAINING-0450", "PMID:12297050; DOI:10.1016/S0092-8674(02)00963-7; PMID:28988771; PMCID:PMC5650921; PMID:6090945", "EGF/EGFR dimerization, receptor autophosphorylation, and MAPK/AKT growth-function assays support the exact RTK relay."),
}
PROMOTION_NOTE = "Module 21A relay/function promotion batch007 (2026-09-02): evidence tier raised from medium-high to high for the exact receptor-complex relay/function packet; upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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
    out = {}
    for row in rows:
        value = row.get(key, "")
        if value and value in out:
            raise SystemExit(f"duplicate {key}: {value}")
        if value:
            out[value] = row
    return out


def append_once(value, note):
    return value if note in value else f"{value} {note}".strip()


def validate(detail, review, reuse, pairs):
    for evidence_id, (pair_key, reuse_key, review_id, citations, _) in PACKET.items():
        d = detail.get(evidence_id)
        if d is None or d.get("confidence_tier") != "medium-high":
            raise SystemExit(f"{evidence_id} missing or not medium-high")
        if not all(x in d.get("evidence_layer", "") for x in ("receptor_proximal_relay", "downstream_pathway_function")):
            raise SystemExit(f"{evidence_id} lacks relay/function layers")
        if d.get("pathway_reuse_key") != reuse_key or d.get("source_locators") != citations:
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        rv = review.get(review_id)
        if rv is None or rv.get("evidence_id") != evidence_id or rv.get("pair_key") != pair_key or rv.get("confidence_tier") != "medium-high" or rv.get("review_status") != "reviewed_relay_candidate":
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        ru = reuse.get(reuse_key)
        if ru is None or ru.get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        pair = next((p for p in pairs if p.get("module21a_evidence_ids") == evidence_id), None)
        if pair is None or pair.get("pair_key") != pair_key or pair.get("module21a_status") != "reviewed_relay_candidate":
            raise SystemExit(f"coverage lineage mismatch: {evidence_id}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    detail_fields, detail_rows = read_tsv(DETAIL)
    review_fields, review_rows = read_tsv(REVIEW)
    reuse_fields, reuse_rows = read_tsv(REUSE)
    pair_fields, pair_rows = read_tsv(PAIRS)
    detail, review, reuse = index(detail_rows, "evidence_id"), index(review_rows, "review_id"), index(reuse_rows, "pathway_reuse_key")
    validate(detail, review, reuse, pair_rows)
    audit_fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    audit_rows = [{"evidence_id": e, "review_id": v[2], "pair_key": v[0], "pathway_reuse_key": v[1], "previous_tier": detail[e]["confidence_tier"], "new_tier": "high", "source_locators": detail[e]["source_locators"], "decision_basis": v[4], "upstream_lr_confidence_unchanged": "true", "terminal_tf_status_unchanged": "true", "sql_materialization": "false"} for e, v in sorted(PACKET.items())]
    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False, "evidence_ids": sorted(PACKET)}, indent=2))
        return
    for e, (pair_key, reuse_key, review_id, _, _) in PACKET.items():
        detail[e]["confidence_tier"] = "high"
        detail[e]["limitations"] = append_once(detail[e]["limitations"], PROMOTION_NOTE)
        review[review_id]["confidence_tier"] = "high"
        review[review_id]["curator_note"] = append_once(review[review_id]["curator_note"], PROMOTION_NOTE)
        reuse[reuse_key]["validation_status"] = "promoted_relay_function_high_batch007"
        reuse[reuse_key]["limitations"] = append_once(reuse[reuse_key]["limitations"], PROMOTION_NOTE)
        next(p for p in pair_rows if p.get("module21a_evidence_ids") == e)["curator_notes"] = append_once(next(p for p in pair_rows if p.get("module21a_evidence_ids") == e)["curator_notes"], PROMOTION_NOTE)
    write_tsv(DETAIL, detail_fields, detail_rows)
    write_tsv(REVIEW, review_fields, review_rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-relay-function-batch007-2026-09-02", "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET), "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
