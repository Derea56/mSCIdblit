#!/usr/bin/env python3
"""Integrate the eighth bounded medium-to-high Module 20A LR packet."""

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


A_EVIDENCE = STARTER / "module20a_medium_direct_high_batch008_evidence_register.tsv"
A_DECISIONS = STARTER / "module20a_medium_direct_high_batch008_decision_register.tsv"
A_SUMMARY = STARTER / "module20a_medium_direct_high_batch008_summary.json"
B_AUDIT = B_DIR / "module20b_medium_direct_high_batch008_2026_09_01.tsv"

EDGE_TO_PRIMARY = {
    "M20B-E004248": "M20B-EVID-004248-P2-DIRECT",
    "M20B-E004452": "M20B-EVID-004452-P2-DIRECT",
    "M20B-E004459": "M20B-EVID-004459-P2-DIRECT",
    "M20B-E004537": "M20B-EVID-004537-P2-DIRECT",
    "M20B-E004583": "M20B-EVID-004583-P2-DIRECT",
    "M20B-E004591": "M20B-EVID-004591-P2-DIRECT",
    "M20B-E004592": "M20B-EVID-004592-P2-DIRECT",
    "M20B-E004593": "M20B-EVID-004593-P2-DIRECT",
    "M20B-E004594": "M20B-EVID-004594-P2-DIRECT",
    "M20B-E004597": "M20B-EVID-004597-P2-DIRECT",
    "M20B-E004680": "M20B-EVID-004680-P2-DIRECT",
    "M20B-E004731": "M20B-EVID-004731-P2-DIRECT",
    "M20B-E004734": "M20B-EVID-004734-P2-DIRECT",
    "M20B-E004743": "M20B-EVID-004743-P2-DIRECT",
    "M20B-E004745": "M20B-EVID-004745-P2-DIRECT",
    "M20B-E004813": "M20B-EVID-004813-P2-DIRECT",
    "M20B-E004814": "M20B-EVID-004814-P2-DIRECT",
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
    "Exact pair-specific primary direct-molecular or explicitly preserved "
    "receptor-complex evidence was adjudicated high in Module 20B. High applies "
    "only to the tested molecular engagement or preserved complex; ligand form, "
    "domain, receptor topology, isoform, species, assay, and non-SCI limitations "
    "remain explicit. No relay, TF/program, cellular-output, or SCI context is inferred."
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
    if any(edges[e]["confidence_tier"] != "medium" or edges[e]["exportable"] != "true" for e in EDGE_TO_PRIMARY):
        raise SystemExit("selected edges are not all medium/exportable")
    if any(frozen[e]["confidence_tier"] != "medium" for e in EDGE_TO_PRIMARY):
        raise SystemExit("selected frozen LR evidence is not all medium")
    if set(EDGE_TO_PRIMARY.values()) - set(evidence):
        raise SystemExit("selected primary evidence missing")
    for edge_id, evidence_id in EDGE_TO_PRIMARY.items():
        primary = evidence[evidence_id]
        if primary["evidence_layer"] not in {"ligand_receptor_or_direct_molecular"}:
            raise SystemExit(f"primary evidence is not direct for {edge_id}")
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
        evidence_id = f"M20A-MEDHIGH008-EVID-{index:04d}"
        mouse, mouse_rank = species_confidence(primary["species_support"], "mouse")
        human, human_rank = species_confidence(primary["species_support"], "human")
        limitations = (
            f"{primary['limitations']} High is limited to the tested molecular "
            "interaction or preserved receptor-complex claim; no SCI-context or "
            "downstream relay inference is made."
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
            "receptor_role": "ligand_receptor_or_receptor_associated_molecular_role",
            "directness": "exact_primary_direct_molecular_or_preserved_complex",
            "species_posture": "species_scoped_to_exact_primary_packet; no_unlisted_species_inference",
            "decision_basis": f"{BASIS} Source packet: {primary['b_evidence_id']}.",
            "evidence_register_ids": evidence_id,
            "next_action": "retain_high_direct_molecular_evidence; preserve_topology_and_context; keep_relay_and_SCI_fields_separate",
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
            "new_frozen_evidence_confidence": "high",
            "decision_basis": BASIS,
        })
        q["confidence_decision"] = "high"
        q["evidence_register_ids"] = ";".join(part for part in (q["evidence_register_ids"].strip(), evidence_id) if part)
        q["curator_notes"] = append_once(
            q["curator_notes"],
            "Medium-direct-high batch008: exact primary direct or explicitly preserved complex evidence adjudicated high for the tested molecular interaction only; topology and context boundaries retained.",
        )
        edge.update({
            "confidence_tier": "high",
            "export_priority": "high",
            "exportable": "true",
            "consolidation_note": append_once(
                edge["consolidation_note"],
                "Medium-direct-high batch008: exact primary molecular interaction promoted; topology and context boundaries retained.",
            ),
        })
        frozen_row.update({
            "confidence_tier": "high",
            "exportable": "true",
            "consolidation_note": append_once(
                frozen_row["consolidation_note"],
                "Medium-direct-high batch008: exact primary molecular interaction promoted; topology and context boundaries retained.",
            ),
        })

    write_tsv(A_EVIDENCE, A_EVIDENCE_FIELDS, a_evidence_rows)
    write_tsv(A_DECISIONS, A_DECISION_FIELDS, a_decision_rows)
    write_tsv(QUEUE, queue_fields, queue_rows)
    write_tsv(B_EDGES, edge_fields, edge_rows)
    write_tsv(B_EVIDENCE, evidence_fields, evidence_rows)
    write_tsv(B_AUDIT, B_AUDIT_FIELDS, audit_rows)
    summary = {
        "generated_utc": datetime.now(UTC).isoformat(timespec="seconds"),
        "batch_id": "module20a_medium_direct_high_batch008",
        "rows_reviewed": len(EDGE_TO_PRIMARY),
        "rows_promoted_to_high": len(EDGE_TO_PRIMARY),
        "module20b_edges_promoted": len(EDGE_TO_PRIMARY),
        "module20b_frozen_lr_evidence_promoted": len(EDGE_TO_PRIMARY),
        "signaling_edges_created": 0,
        "policy": BASIS,
        "selected_b_edge_ids": sorted(EDGE_TO_PRIMARY),
    }
    A_SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
