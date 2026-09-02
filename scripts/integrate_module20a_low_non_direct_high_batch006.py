#!/usr/bin/env python3
"""Promote low-confidence Module 20B relay packets after exact review."""

from __future__ import annotations

import json
from datetime import UTC, datetime

from integrate_module20a_medium_direct_high_batch002 import (
    B_DIR, B_EDGES, QUEUE, STARTER, append_once, read_tsv, species_confidence, write_tsv,
)


A_EVIDENCE = STARTER / "module20a_low_non_direct_high_batch006_evidence_register.tsv"
A_DECISIONS = STARTER / "module20a_low_non_direct_high_batch006_decision_register.tsv"
A_SUMMARY = STARTER / "module20a_low_non_direct_high_batch006_summary.json"
B_AUDIT = B_DIR / "module20b_low_non_direct_high_batch006_2026_09_01.tsv"
B_EVIDENCE = B_DIR / "module20b_evidence_register.tsv"

EDGE_TO_PRIMARY = {
    "M20B-E003920": "M20B-EVID-003920-P2-RELAY",
    "M20B-E004259": "M20B-EVID-004259-P2-RELAY",
}

EVIDENCE_FIELDS = ["evidence_item_id", "review_id", "pair_key", "pair_label", "source_kind", "source_locator", "support_kind", "species_support", "source_scope", "confidence_tier", "citation_note", "evidence_summary", "limitations"]
DECISION_FIELDS = ["review_id", "pair_key", "pair_label_canonical", "review_status", "confidence_decision", "mouse_confidence", "mouse_confidence_rank", "human_confidence", "human_confidence_rank", "human_evidence_present", "receptor_state", "receptor_role", "directness", "species_posture", "decision_basis", "evidence_register_ids", "next_action"]
AUDIT_FIELDS = ["review_id", "pair_key", "pair_label_canonical", "b_edge_id", "b_primary_evidence_id", "a_evidence_id", "previous_edge_confidence", "previous_edge_exportable", "previous_frozen_evidence_confidence", "new_edge_confidence", "new_frozen_evidence_confidence", "decision_basis"]

BASIS = (
    "Exact pair-specific primary receptor-proximal relay evidence was adjudicated "
    "high at the preserved non-direct layer. High applies only to the cited relay "
    "and model; it does not establish isolated binary binding, a terminal TF, SCI "
    "relevance, or an outcome beyond the cited record."
)


def main() -> None:
    q_fields, q_rows = read_tsv(QUEUE)
    queue = {r["review_id"]: r for r in q_rows}
    edge_fields, edge_rows = read_tsv(B_EDGES)
    evidence_fields, evidence_rows = read_tsv(B_EVIDENCE)
    edges = {r["b_edge_id"]: r for r in edge_rows}
    frozen = {r["b_edge_ids"]: r for r in evidence_rows if r["source_kind"] == "frozen_module20a_lr_release"}
    evidence = {r["b_evidence_id"]: r for r in evidence_rows}
    if set(EDGE_TO_PRIMARY) - set(edges) or set(EDGE_TO_PRIMARY) - set(frozen) or set(EDGE_TO_PRIMARY.values()) - set(evidence):
        raise SystemExit("selected edge, frozen evidence, or primary evidence missing")
    if any(edges[e]["confidence_tier"] != "low" or edges[e]["exportable"] != "false" for e in EDGE_TO_PRIMARY):
        raise SystemExit("selected edges are not all low/non-exportable")
    if any(frozen[e]["confidence_tier"] != "low" for e in EDGE_TO_PRIMARY):
        raise SystemExit("selected frozen LR evidence is not all low")
    for edge_id, evidence_id in EDGE_TO_PRIMARY.items():
        p = evidence[evidence_id]
        if p["evidence_layer"] not in {"receptor_proximal_relay", "receptor_proximal_or_pathway", "downstream_or_functional", "downstream_pathway_or_cellular_function"} or p["exportable"].casefold() != "true":
            raise SystemExit(f"primary evidence is not exportable relay/function evidence for {edge_id}")
        if p["confidence_tier"].casefold() not in {"high", "medium-high", "medium"}:
            raise SystemExit(f"unexpected primary confidence for {edge_id}")

    a_evidence, a_decisions, audits = [], [], []
    for index, edge_id in enumerate(sorted(EDGE_TO_PRIMARY), start=1):
        edge = edges[edge_id]
        aid = edge["source_a_edge_id"]
        if aid not in queue or queue[aid]["confidence_decision"] != "low":
            raise SystemExit(f"selected source A queue row is absent or not low: {aid}")
        q = queue[aid]
        p = evidence[EDGE_TO_PRIMARY[edge_id]]
        fr = frozen[edge_id]
        new_id = f"M20A-LOWNONDIRECTHIGH006-EVID-{index:04d}"
        mouse, mouse_rank = species_confidence(p["species_support"], "mouse")
        human, human_rank = species_confidence(p["species_support"], "human")
        a_evidence.append({"evidence_item_id": new_id, "review_id": aid, "pair_key": q["pair_key"], "pair_label": q["pair_label_canonical"], "source_kind": "primary_literature_recovery", "source_locator": p["source_locator"], "support_kind": p["support_kind"], "species_support": p["species_support"], "source_scope": "module20b_exact_primary_packet_reused_for_module20a_adjudication", "confidence_tier": "high", "citation_note": p["citation_note"], "evidence_summary": p["evidence_summary"], "limitations": f"{p['limitations']} High is limited to the cited non-direct relay record; no binary binding, TF, or SCI-transfer inference is made."})
        a_decisions.append({"review_id": aid, "pair_key": q["pair_key"], "pair_label_canonical": q["pair_label_canonical"], "review_status": "reviewed", "confidence_decision": "high", "mouse_confidence": mouse, "mouse_confidence_rank": mouse_rank, "human_confidence": human, "human_confidence_rank": human_rank, "human_evidence_present": "yes" if human == "high" else "no", "receptor_state": "membrane_bound_or_receptor_complex_context", "receptor_role": "receptor_proximal_or_functional_context", "directness": "non_direct_exact_pair_relay_support", "species_posture": "species_scoped_to_exact_primary_packet; no_unlisted_species_inference", "decision_basis": f"{BASIS} Source packet: {p['b_evidence_id']}.", "evidence_register_ids": new_id, "next_action": "retain_high_non_direct_relay_support; preserve_directness_and_context_boundary; keep_TF_and_SCI_fields_separate"})
        audits.append({"review_id": aid, "pair_key": q["pair_key"], "pair_label_canonical": q["pair_label_canonical"], "b_edge_id": edge_id, "b_primary_evidence_id": p["b_evidence_id"], "a_evidence_id": new_id, "previous_edge_confidence": edge["confidence_tier"], "previous_edge_exportable": edge["exportable"], "previous_frozen_evidence_confidence": fr["confidence_tier"], "new_edge_confidence": "high", "new_frozen_evidence_confidence": fr["confidence_tier"], "decision_basis": BASIS})
        q["confidence_decision"] = "high"
        q["evidence_register_ids"] = ";".join(part for part in (q["evidence_register_ids"].strip(), new_id) if part)
        q["curator_notes"] = append_once(q["curator_notes"], "Low-non-direct-high batch006: exact primary relay evidence adjudicated high for the preserved non-direct layer; no binary binding, TF, downstream, or SCI inference added.")
        edge.update({"confidence_tier": "high", "export_priority": "high", "exportable": "true", "consolidation_note": append_once(edge["consolidation_note"], "Low-non-direct-high batch006: exact primary relay evidence promoted at the non-direct layer; directness and context boundaries retained.")})

    write_tsv(A_EVIDENCE, EVIDENCE_FIELDS, a_evidence)
    write_tsv(A_DECISIONS, DECISION_FIELDS, a_decisions)
    write_tsv(QUEUE, q_fields, q_rows)
    write_tsv(B_EDGES, edge_fields, edge_rows)
    write_tsv(B_AUDIT, AUDIT_FIELDS, audits)
    summary = {"generated_utc": datetime.now(UTC).isoformat(timespec="seconds"), "batch_id": "module20a_low_non_direct_high_batch006", "rows_reviewed": len(EDGE_TO_PRIMARY), "rows_promoted_to_high": len(EDGE_TO_PRIMARY), "module20b_edges_promoted": len(EDGE_TO_PRIMARY), "module20b_frozen_lr_evidence_promoted": 0, "signaling_edges_created": 0, "direct_binding_upgraded": 0, "policy": BASIS, "selected_b_edge_ids": sorted(EDGE_TO_PRIMARY)}
    A_SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
