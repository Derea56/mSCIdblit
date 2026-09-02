#!/usr/bin/env python3
"""Integrate a bounded high-confidence non-direct Module 20B packet.

The selected primary records support exact-pair receptor-proximal relay or
downstream/function evidence. They do not upgrade the graph edge to a direct
binding claim, and the original frozen LR source record remains medium.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime

from integrate_module20a_medium_direct_high_batch002 import (
    B_DIR,
    B_EDGES,
    B_EVIDENCE,
    QUEUE,
    STARTER,
    append_once,
    read_tsv,
    species_confidence,
    write_tsv,
)


A_EVIDENCE = STARTER / "module20a_non_direct_high_batch001_evidence_register.tsv"
A_DECISIONS = STARTER / "module20a_non_direct_high_batch001_decision_register.tsv"
A_SUMMARY = STARTER / "module20a_non_direct_high_batch001_summary.json"
B_AUDIT = B_DIR / "module20b_non_direct_high_batch001_2026_09_01.tsv"

EDGE_TO_PRIMARY = {
    "M20B-E001576": "M20B-EVID-005350-P2-RELAY",
    "M20B-E001577": "M20B-EVID-005352-P2-RELAY",
    "M20B-E001797": "M20B-EVID-005354-P2-RELAY",
    "M20B-E001805": "M20B-EVID-005237-P2-RELAY",
    "M20B-E001865": "M20B-EVID-005265-P2-RELAY",
    "M20B-E001894": "M20B-EVID-005271-P2-RELAY",
    "M20B-E002583": "M20B-EVID-005291-P2-RELAY",
    "M20B-E003150": "M20B-EVID-005299-P2-RELAY",
    "M20B-E003151": "M20B-EVID-005301-P2-RELAY",
    "M20B-E003271": "M20B-EVID-005305-P2-RELAY",
    "M20B-E003272": "M20B-EVID-005307-P2-RELAY",
    "M20B-E003728": "M20B-EVID-003728-P2-FUNC",
    "M20B-E003739": "M20B-EVID-003739-P2-FUNC",
    "M20B-E003878": "M20B-EVID-003878-P2-RELAY",
    "M20B-E003882": "M20B-EVID-003882-P2-FUNC",
    "M20B-E003884": "M20B-EVID-003884-P2-FUNC",
    "M20B-E003899": "M20B-EVID-003899-P2-RELAY",
}

A_EVIDENCE_FIELDS = [
    "evidence_item_id", "review_id", "pair_key", "pair_label", "source_kind",
    "source_locator", "support_kind", "species_support", "source_scope",
    "confidence_tier", "citation_note", "evidence_summary", "limitations",
]
A_DECISION_FIELDS = [
    "review_id", "pair_key", "pair_label_canonical", "review_status",
    "confidence_decision", "mouse_confidence", "mouse_confidence_rank",
    "human_confidence", "human_confidence_rank", "human_evidence_present",
    "receptor_state", "receptor_role", "directness", "species_posture",
    "decision_basis", "evidence_register_ids", "next_action",
]
B_AUDIT_FIELDS = [
    "review_id", "pair_key", "pair_label_canonical", "b_edge_id",
    "b_primary_evidence_id", "a_evidence_id", "previous_edge_confidence",
    "previous_edge_exportable", "previous_frozen_evidence_confidence",
    "new_edge_confidence", "new_frozen_evidence_confidence", "decision_basis",
]

BASIS = (
    "Exact pair-specific primary receptor-proximal relay or downstream/function "
    "evidence was validated at high adjudication tier in Module 20B. High applies "
    "only to the preserved non-direct evidence layer; it does not establish a new "
    "binary binding assay, terminal TF, cellular output beyond the cited record, "
    "or SCI relevance. Species, complex, isoform, ligand-form, assay, and model "
    "limitations remain explicit."
)


def main() -> None:
    queue_fields, queue_rows = read_tsv(QUEUE)
    queue = {row["review_id"]: row for row in queue_rows}
    edge_fields, edge_rows = read_tsv(B_EDGES)
    evidence_fields, evidence_rows = read_tsv(B_EVIDENCE)
    edges = {row["b_edge_id"]: row for row in edge_rows}
    frozen = {
        row["b_edge_ids"]: row
        for row in evidence_rows
        if row["source_kind"] == "frozen_module20a_lr_release"
    }
    evidence = {row["b_evidence_id"]: row for row in evidence_rows}
    if set(EDGE_TO_PRIMARY) - set(edges) or set(EDGE_TO_PRIMARY) - set(frozen):
        raise SystemExit("selected edge or frozen evidence missing")
    if any(edges[edge_id]["confidence_tier"] != "medium" or edges[edge_id]["exportable"] != "true" for edge_id in EDGE_TO_PRIMARY):
        raise SystemExit("selected edges are not all medium/exportable")
    if any(frozen[edge_id]["confidence_tier"] != "medium" for edge_id in EDGE_TO_PRIMARY):
        raise SystemExit("selected frozen LR evidence is not all medium")
    if set(EDGE_TO_PRIMARY.values()) - set(evidence):
        raise SystemExit("selected primary evidence missing")
    for edge_id, evidence_id in EDGE_TO_PRIMARY.items():
        primary = evidence[evidence_id]
        if primary["evidence_layer"] not in {"receptor_proximal_relay", "receptor_proximal_or_pathway", "downstream_or_functional", "downstream_pathway_or_cellular_function"}:
            raise SystemExit(f"primary evidence is not non-direct for {edge_id}: {primary['evidence_layer']}")
        if primary["exportable"].casefold() != "true":
            raise SystemExit(f"primary evidence is not exportable for {edge_id}")
        if primary["confidence_tier"].casefold() not in {"high", "medium-high"}:
            raise SystemExit(f"primary evidence is below high-adjudication input for {edge_id}")

    a_evidence_rows, a_decision_rows, audit_rows = [], [], []
    for index, edge_id in enumerate(sorted(EDGE_TO_PRIMARY), start=1):
        edge = edges[edge_id]
        aid = edge["source_a_edge_id"]
        if aid not in queue:
            raise SystemExit(f"source A edge is absent from review queue: {aid}")
        q = queue[aid]
        if q["confidence_decision"] != "medium":
            raise SystemExit(f"selected queue row is not medium: {aid}")
        primary = evidence[EDGE_TO_PRIMARY[edge_id]]
        frozen_row = frozen[edge_id]
        evidence_id = f"M20A-NONDIRECTHIGH001-EVID-{index:04d}"
        mouse, mouse_rank = species_confidence(primary["species_support"], "mouse")
        human, human_rank = species_confidence(primary["species_support"], "human")
        limitations = (
            f"{primary['limitations']} High is limited to the cited non-direct "
            "relay/function record; no binary binding or SCI-transfer inference is made."
        ).strip()
        a_evidence_rows.append({
            "evidence_item_id": evidence_id,
            "review_id": aid,
            "pair_key": q["pair_key"],
            "pair_label": q["pair_label_canonical"],
            "source_kind": "primary_literature_recovery",
            "source_locator": primary["source_locator"],
            "support_kind": primary["support_kind"],
            "species_support": primary["species_support"],
            "source_scope": "module20b_exact_primary_packet_reused_for_module20a_adjudication",
            "confidence_tier": "high",
            "citation_note": primary["citation_note"],
            "evidence_summary": primary["evidence_summary"],
            "limitations": limitations,
        })
        a_decision_rows.append({
            "review_id": aid,
            "pair_key": q["pair_key"],
            "pair_label_canonical": q["pair_label_canonical"],
            "review_status": "reviewed",
            "confidence_decision": "high",
            "mouse_confidence": mouse,
            "mouse_confidence_rank": mouse_rank,
            "human_confidence": human,
            "human_confidence_rank": human_rank,
            "human_evidence_present": "yes" if human == "high" else "no",
            "receptor_state": "membrane_bound_or_receptor_complex_context",
            "receptor_role": "receptor_proximal_or_functional_context",
            "directness": "non_direct_exact_pair_relay_or_functional_support",
            "species_posture": "species_scoped_to_exact_primary_packet; no_unlisted_species_inference",
            "decision_basis": f"{BASIS} Source packet: {primary['b_evidence_id']}.",
            "evidence_register_ids": evidence_id,
            "next_action": "retain_high_non_direct_support; preserve_directness_boundary; keep_TF_and_SCI_fields_separate",
        })
        audit_rows.append({
            "review_id": aid,
            "pair_key": q["pair_key"],
            "pair_label_canonical": q["pair_label_canonical"],
            "b_edge_id": edge_id,
            "b_primary_evidence_id": primary["b_evidence_id"],
            "a_evidence_id": evidence_id,
            "previous_edge_confidence": edge["confidence_tier"],
            "previous_edge_exportable": edge["exportable"],
            "previous_frozen_evidence_confidence": frozen_row["confidence_tier"],
            "new_edge_confidence": "high",
            "new_frozen_evidence_confidence": frozen_row["confidence_tier"],
            "decision_basis": BASIS,
        })
        q["confidence_decision"] = "high"
        q["evidence_register_ids"] = ";".join(part for part in (q["evidence_register_ids"].strip(), evidence_id) if part)
        q["curator_notes"] = append_once(
            q["curator_notes"],
            "Non-direct-high batch001: exact primary relay/function evidence adjudicated high for the preserved non-direct layer; no binary binding, TF, downstream, or SCI inference added.",
        )
        edge.update({
            "confidence_tier": "high",
            "export_priority": "high",
            "exportable": "true",
            "consolidation_note": append_once(
                edge["consolidation_note"],
                "Non-direct-high batch001: exact primary relay/function evidence promoted at the non-direct layer; directness and context boundaries retained.",
            ),
        })

    write_tsv(A_EVIDENCE, A_EVIDENCE_FIELDS, a_evidence_rows)
    write_tsv(A_DECISIONS, A_DECISION_FIELDS, a_decision_rows)
    write_tsv(QUEUE, queue_fields, queue_rows)
    write_tsv(B_EDGES, edge_fields, edge_rows)
    write_tsv(B_AUDIT, B_AUDIT_FIELDS, audit_rows)
    summary = {
        "generated_utc": datetime.now(UTC).isoformat(timespec="seconds"),
        "batch_id": "module20a_non_direct_high_batch001",
        "rows_reviewed": len(EDGE_TO_PRIMARY),
        "rows_promoted_to_high": len(EDGE_TO_PRIMARY),
        "module20b_edges_promoted": len(EDGE_TO_PRIMARY),
        "module20b_frozen_lr_evidence_promoted": 0,
        "signaling_edges_created": 0,
        "direct_binding_upgraded": 0,
        "policy": BASIS,
        "selected_b_edge_ids": sorted(EDGE_TO_PRIMARY),
    }
    A_SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
