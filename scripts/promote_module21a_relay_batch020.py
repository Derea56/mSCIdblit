#!/usr/bin/env python3
"""Promote six exact Module 21A relay/function packets."""

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
AUDIT = RELAY / "module21a_relay_promotion_batch020.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch020_summary.json"
REVIEW_FILE = RELAY / "module21a_pair_relay_review_batches208_209.tsv"

PACKET = {
    "M21A-PAIR-EVID-5083": {
        "pair_key": "ebi3_il27 il27ra_il6st", "reuse_key": "M21A-REUSE-2382", "review_id": "M20A-EXT-1493",
        "citations": "PMID:14764690; PMID:22069308; PMID:18453571",
        "required_layers": ("receptor_proximal_relay", "downstream_pathway_function"),
        "basis": "IL-27 receptor-complex signaling through IL27RA/IL6ST with JAK/STAT and context-dependent MAPK/Akt outputs supports qualified-high relay/function evidence; the heterodimeric IL-27 ligand is retained and isolated EBI3 activity is not claimed.",
    },
    "M21A-PAIR-EVID-5084": {
        "pair_key": "edn1 ednra", "reuse_key": "M21A-REUSE-2383", "review_id": "M20A-EXT-1496",
        "citations": "PMID:16465602; PMCID:PMC2715373; DOI:10.1046/j.0014-2956.2001.02486.x",
        "required_layers": ("receptor_proximal_relay", "downstream_pathway_function"),
        "basis": "EDN1/EDNRA Gq/PLC/PKC and ERK1/2 signaling with smooth-muscle contractile or proliferative outputs supports qualified-high exact relay/function evidence; tissue and antagonist-specificity boundaries remain explicit.",
    },
    "M21A-PAIR-EVID-5085": {
        "pair_key": "edn1 ednrb", "reuse_key": "M21A-REUSE-2384", "review_id": "M20A-EXT-1497",
        "citations": "PMCID:PMC3663331; DOI:10.1046/j.0014-2956.2001.02486.x",
        "required_layers": ("receptor_proximal_relay", "downstream_pathway_function"),
        "basis": "EDN1/EDNRB receptor signaling with G-protein/PKC and ERK1/2 outputs in the defined melanocyte model supports qualified-high exact relay/function evidence; EDNRA co-usage and cell-type dependence remain explicit.",
    },
    "M21A-PAIR-EVID-5086": {
        "pair_key": "edn2 ednra", "reuse_key": "M21A-REUSE-2385", "review_id": "M20A-EXT-1499",
        "citations": "PMID:20450830; PMCID:PMC3791783; DOI:10.1016/j.ygcen.2019.113231",
        "required_layers": ("receptor_proximal_relay", "downstream_pathway_function"),
        "basis": "EDN2/EDNRA dependence with contractile ovarian and retinal vascular outputs supports qualified-high exact relay/function evidence; tissue, species, and endpoint-specific boundaries remain explicit.",
    },
    "M21A-PAIR-EVID-5091": {
        "pair_key": "efna1 epha2", "reuse_key": "M21A-REUSE-2387", "review_id": "M20A-EXT-1510",
        "citations": "PMCID:PMC6016825; PMCID:PMC2727437",
        "required_layers": ("receptor_proximal_relay", "downstream_pathway_function"),
        "basis": "Membrane-associated ephrin-A1 engagement and clustering of EphA2 with Src/Rho-actomyosin and focal-adhesion outputs support qualified-high exact relay/function evidence in tumor or engineered receptor systems; avidity and model context remain explicit.",
    },
    "M21A-PAIR-EVID-5096": {
        "pair_key": "efna1 epha8", "reuse_key": "M21A-REUSE-2388", "review_id": "M20A-EXT-1516",
        "citations": "DOI:10.1016/S1016-8478(23)13566-7",
        "required_layers": ("receptor_proximal_relay",),
        "basis": "EFNA1/EphA8 binding and receptor phosphorylation in receptor-chimera and NIH3T3 systems support qualified-high receptor-proximal evidence; downstream adaptor, terminal-TF, and native-cell extrapolation are excluded.",
    },
}
PROMOTION_NOTE = "Module 21A relay/function promotion batch020 (2026-09-02): evidence tier raised to high for the exact, context-bounded receptor relay/function packet; upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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
    review_fields, review_rows = read_tsv(REVIEW_FILE)
    detail, reuse, reviews = index(detail_rows, "evidence_id"), index(reuse_rows, "pathway_reuse_key"), index(review_rows, "review_id")
    for evidence_id, expected in PACKET.items():
        d = detail.get(evidence_id)
        if d is None or d.get("confidence_tier") != "medium-high":
            raise SystemExit(f"{evidence_id} missing or not medium-high")
        if not all(x in d.get("evidence_layer", "") for x in expected["required_layers"]):
            raise SystemExit(f"{evidence_id} lacks required evidence layers")
        if d.get("pathway_reuse_key") != expected["reuse_key"] or d.get("source_locators") != expected["citations"]:
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        rv = reviews.get(expected["review_id"])
        if rv is None or rv.get("evidence_id") != evidence_id or rv.get("pair_key") != expected["pair_key"] or rv.get("source_locators") != expected["citations"] or rv.get("confidence_tier") != "medium-high" or rv.get("review_status") != "reviewed_relay_candidate":
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
        rv = reviews[v["review_id"]]
        rv["confidence_tier"] = "high"
        rv["curator_note"] = append_once(rv["curator_note"], PROMOTION_NOTE)
        reuse[v["reuse_key"]]["validation_status"] = "promoted_relay_function_high_batch020"
        reuse[v["reuse_key"]]["limitations"] = append_once(reuse[v["reuse_key"]]["limitations"], PROMOTION_NOTE)
        pair = next(p for p in pair_rows if p.get("module21a_evidence_ids") == e)
        pair["curator_notes"] = append_once(pair["curator_notes"], PROMOTION_NOTE)
    write_tsv(DETAIL, detail_fields, detail_rows)
    write_tsv(REVIEW_FILE, review_fields, review_rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-relay-function-batch020-2026-09-02", "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET), "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
