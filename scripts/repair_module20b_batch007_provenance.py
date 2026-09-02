#!/usr/bin/env python3
"""Repair the one batch-007 source-A edge mapping caught in audit.

The original batch used the source-A evidence identifier for E004440 instead
of its source-A edge identifier. This repair moves only the batch-007 audit
packet from M20A-EXT-2648 to the canonical E004440 source-A edge
M20A-EXT-2665, and restores the shared M20A-EXT-2648 queue row.
"""

from __future__ import annotations

import json

from integrate_module20a_medium_direct_high_batch002 import (
    B_DIR, QUEUE, STARTER, read_tsv, write_tsv,
)


EVIDENCE_ID = "M20A-MEDHIGH007-EVID-0012"
OLD_REVIEW = "M20A-EXT-2648"
NEW_REVIEW = "M20A-EXT-2665"
B_EDGE = "M20B-E004440"


def main() -> None:
    q_fields, q_rows = read_tsv(QUEUE)
    queue = {r["review_id"]: r for r in q_rows}
    edge_fields, edge_rows = read_tsv(B_DIR / "module20b_edge_register.tsv")
    edges = {r["b_edge_id"]: r for r in edge_rows}
    assert edges[B_EDGE]["source_a_edge_id"] == NEW_REVIEW
    assert OLD_REVIEW in queue and NEW_REVIEW in queue
    old = queue[OLD_REVIEW]
    new = queue[NEW_REVIEW]
    assert old["confidence_decision"] == "high"
    assert EVIDENCE_ID in old["evidence_register_ids"]
    assert new["confidence_decision"] == "medium"
    old["confidence_decision"] = "medium"
    old["evidence_register_ids"] = ";".join(x for x in old["evidence_register_ids"].split(";") if x != EVIDENCE_ID)
    old["curator_notes"] = old["curator_notes"].replace(" Medium-direct-high batch007: exact primary direct or explicitly preserved complex evidence adjudicated high for the tested molecular interaction only; topology, ligand-form, species, downstream, and SCI boundaries preserved.", "")
    assert EVIDENCE_ID not in old["evidence_register_ids"]
    assert "Medium-direct-high batch007:" not in old["curator_notes"]
    new["confidence_decision"] = "high"
    new["evidence_register_ids"] = ";".join(x for x in (new["evidence_register_ids"].strip(), EVIDENCE_ID) if x)
    new["curator_notes"] = (new["curator_notes"].rstrip() + " Medium-direct-high batch007: exact primary direct or explicitly preserved complex evidence adjudicated high for the tested molecular interaction only; topology, ligand-form, species, downstream, and SCI boundaries preserved.").strip()
    write_tsv(QUEUE, q_fields, q_rows)

    a_evidence_path = STARTER / "module20a_medium_direct_high_batch007_evidence_register.tsv"
    a_decision_path = STARTER / "module20a_medium_direct_high_batch007_decision_register.tsv"
    b_audit_path = B_DIR / "module20b_medium_direct_high_batch007_2026_09_01.tsv"
    ae_fields, ae_rows = read_tsv(a_evidence_path)
    ad_fields, ad_rows = read_tsv(a_decision_path)
    ba_fields, ba_rows = read_tsv(b_audit_path)
    ae = next(r for r in ae_rows if r["evidence_item_id"] == EVIDENCE_ID)
    ad = next(r for r in ad_rows if r["evidence_register_ids"] == EVIDENCE_ID)
    ba = next(r for r in ba_rows if r["a_evidence_id"] == EVIDENCE_ID)
    assert ae["review_id"] == OLD_REVIEW and ad["review_id"] == OLD_REVIEW and ba["review_id"] == OLD_REVIEW
    for row in (ae, ad, ba):
        row["review_id"] = NEW_REVIEW
        row["pair_key"] = new["pair_key"]
        if "pair_label" in row:
            row["pair_label"] = new["pair_label_canonical"]
        if "pair_label_canonical" in row:
            row["pair_label_canonical"] = new["pair_label_canonical"]
    write_tsv(a_evidence_path, ae_fields, ae_rows)
    write_tsv(a_decision_path, ad_fields, ad_rows)
    write_tsv(b_audit_path, ba_fields, ba_rows)

    summary_path = STARTER / "module20a_medium_direct_high_batch007_summary.json"
    summary = json.loads(summary_path.read_text())
    summary["selected_review_ids"] = [NEW_REVIEW if x == OLD_REVIEW else x for x in summary["selected_review_ids"]]
    summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"repaired_edge": B_EDGE, "old_review_id": OLD_REVIEW, "new_review_id": NEW_REVIEW, "queue_restored": OLD_REVIEW, "evidence_id": EVIDENCE_ID}, indent=2))


if __name__ == "__main__":
    main()
