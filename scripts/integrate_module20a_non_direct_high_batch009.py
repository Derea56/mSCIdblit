#!/usr/bin/env python3
"""Integrate the species-matched RETN-CAP1 functional packet."""

from __future__ import annotations

import json
from datetime import UTC, datetime

from integrate_module20a_medium_direct_high_batch002 import (
    B_DIR, B_EDGES, QUEUE, STARTER, append_once, read_tsv, species_confidence, write_tsv,
)


A_EVIDENCE = STARTER / "module20a_non_direct_high_batch009_evidence_register.tsv"
A_DECISIONS = STARTER / "module20a_non_direct_high_batch009_decision_register.tsv"
A_SUMMARY = STARTER / "module20a_non_direct_high_batch009_summary.json"
B_AUDIT = B_DIR / "module20b_non_direct_high_batch009_2026_09_01.tsv"
B_EVIDENCE = B_DIR / "module20b_evidence_register.tsv"
EDGE = "M20B-E004691"
PRIMARY = "M20B-EVID-004691-P2-FUNC"
EVIDENCE_FIELDS = ["evidence_item_id", "review_id", "pair_key", "pair_label", "source_kind", "source_locator", "support_kind", "species_support", "source_scope", "confidence_tier", "citation_note", "evidence_summary", "limitations"]
DECISION_FIELDS = ["review_id", "pair_key", "pair_label_canonical", "review_status", "confidence_decision", "mouse_confidence", "mouse_confidence_rank", "human_confidence", "human_confidence_rank", "human_evidence_present", "receptor_state", "receptor_role", "directness", "species_posture", "decision_basis", "evidence_register_ids", "next_action"]
AUDIT_FIELDS = ["review_id", "pair_key", "pair_label_canonical", "b_edge_id", "b_primary_evidence_id", "a_evidence_id", "previous_edge_confidence", "previous_edge_exportable", "previous_frozen_evidence_confidence", "new_edge_confidence", "new_frozen_evidence_confidence", "decision_basis"]
BASIS = "Species-matched mouse resistin/CAP1 functional evidence was adjudicated high at the downstream/functional layer. High applies only to the BNL CL.2 liver-cell CAP1-perturbation response; it does not establish direct binding, receptor-proximal relay, terminal TF occupancy, or SCI relevance."


def main() -> None:
    q_fields, q_rows = read_tsv(QUEUE)
    queue = {r["review_id"]: r for r in q_rows}
    edge_fields, edge_rows = read_tsv(B_EDGES)
    evidence_fields, evidence_rows = read_tsv(B_EVIDENCE)
    edges = {r["b_edge_id"]: r for r in edge_rows}
    frozen = {r["b_edge_ids"]: r for r in evidence_rows if r["source_kind"] == "frozen_module20a_lr_release"}
    evidence = {r["b_evidence_id"]: r for r in evidence_rows}
    edge = edges[EDGE]
    fr = frozen[EDGE]
    p = evidence[PRIMARY]
    aid = edge["source_a_edge_id"]
    if edge["confidence_tier"] != "medium" or edge["exportable"] != "true" or fr["confidence_tier"] != "medium" or queue[aid]["confidence_decision"] != "medium":
        raise SystemExit("E004691 is not in the expected medium state")
    if p["evidence_layer"] != "downstream_or_functional" or p["exportable"].casefold() != "true" or p["confidence_tier"].casefold() not in {"high", "medium-high", "medium"}:
        raise SystemExit("E004691 functional packet is not exportable")
    q = queue[aid]
    new_id = "M20A-NONDIRECTHIGH009-EVID-0001"
    mouse, mouse_rank = species_confidence(p["species_support"], "mouse")
    human, human_rank = species_confidence(p["species_support"], "human")
    a_evidence = [{"evidence_item_id": new_id, "review_id": aid, "pair_key": q["pair_key"], "pair_label": q["pair_label_canonical"], "source_kind": "primary_literature_recovery", "source_locator": p["source_locator"], "support_kind": p["support_kind"], "species_support": p["species_support"], "source_scope": "module20b_exact_primary_packet_reused_for_module20a_adjudication", "confidence_tier": "high", "citation_note": p["citation_note"], "evidence_summary": p["evidence_summary"], "limitations": f"{p['limitations']} High is limited to the cited mouse downstream/function record; no direct binding, receptor-proximal relay, TF, or SCI inference is made."}]
    a_decisions = [{"review_id": aid, "pair_key": q["pair_key"], "pair_label_canonical": q["pair_label_canonical"], "review_status": "reviewed", "confidence_decision": "high", "mouse_confidence": mouse, "mouse_confidence_rank": mouse_rank, "human_confidence": human, "human_confidence_rank": human_rank, "human_evidence_present": "yes" if human == "high" else "no", "receptor_state": "intracellular_or_functional_context", "receptor_role": "functional_context_not_receptor_edge", "directness": "non_direct_exact_pair_functional_support", "species_posture": "mouse_scope_only_for_species_matched_packet; no_unlisted_species_inference", "decision_basis": f"{BASIS} Source packet: {PRIMARY}.", "evidence_register_ids": new_id, "next_action": "retain_high_downstream_function_support; preserve_no_binding_or_receptor_relay_boundary; keep_TF_and_SCI_fields_separate"}]
    audits = [{"review_id": aid, "pair_key": q["pair_key"], "pair_label_canonical": q["pair_label_canonical"], "b_edge_id": EDGE, "b_primary_evidence_id": PRIMARY, "a_evidence_id": new_id, "previous_edge_confidence": edge["confidence_tier"], "previous_edge_exportable": edge["exportable"], "previous_frozen_evidence_confidence": fr["confidence_tier"], "new_edge_confidence": "high", "new_frozen_evidence_confidence": fr["confidence_tier"], "decision_basis": BASIS}]
    q["confidence_decision"] = "high"
    q["evidence_register_ids"] = ";".join(part for part in (q["evidence_register_ids"].strip(), new_id) if part)
    q["curator_notes"] = append_once(q["curator_notes"], "Non-direct-high batch009: species-matched mouse RETN/CAP1 functional evidence promoted at the downstream/function layer; no direct binding, receptor-proximal relay, TF, or SCI inference added.")
    edge.update({"confidence_tier": "high", "export_priority": "high", "exportable": "true", "consolidation_note": append_once(edge["consolidation_note"], "Non-direct-high batch009: species-matched mouse RETN/CAP1 functional evidence promoted at the downstream/function layer; directness and context boundaries retained.")})
    write_tsv(A_EVIDENCE, EVIDENCE_FIELDS, a_evidence)
    write_tsv(A_DECISIONS, DECISION_FIELDS, a_decisions)
    write_tsv(QUEUE, q_fields, q_rows)
    write_tsv(B_EDGES, edge_fields, edge_rows)
    write_tsv(B_AUDIT, AUDIT_FIELDS, audits)
    summary = {"generated_utc": datetime.now(UTC).isoformat(timespec="seconds"), "batch_id": "module20a_non_direct_high_batch009", "rows_reviewed": 1, "rows_promoted_to_high": 1, "module20b_edges_promoted": 1, "module20b_frozen_lr_evidence_promoted": 0, "signaling_edges_created": 0, "direct_binding_upgraded": 0, "policy": BASIS, "selected_b_edge_ids": [EDGE]}
    A_SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
