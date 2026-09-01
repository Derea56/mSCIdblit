#!/usr/bin/env python3
"""Integrate the fifth bounded medium-to-high Module 20A LR packet."""

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


A_EVIDENCE = STARTER / "module20a_medium_direct_high_batch005_evidence_register.tsv"
A_DECISIONS = STARTER / "module20a_medium_direct_high_batch005_decision_register.tsv"
A_SUMMARY = STARTER / "module20a_medium_direct_high_batch005_summary.json"
B_AUDIT = B_DIR / "module20b_medium_direct_high_batch005_2026_09_01.tsv"

SELECTED = {
    "M20A-EXT-2953", "M20A-EXT-2954", "M20A-EXT-2955", "M20A-EXT-2957",
    "M20A-EXT-2958", "M20A-EXT-2960", "M20A-EXT-2961", "M20A-EXT-2962",
    "M20A-EXT-2963", "M20A-EXT-2964", "M20A-EXT-2965", "M20A-EXT-2966",
    "M20A-EXT-2969", "M20A-EXT-2982", "M20A-EXT-2984", "M20A-EXT-3028",
    "M20A-EXT-3124", "M20A-EXT-3136", "M20A-EXT-3137", "M20A-EXT-3169",
    "M20A-EXT-3187", "M20A-EXT-3317",
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
    "Exact pair-specific primary direct-molecular evidence was validated at high "
    "tier in Module 20B. High applies only to the tested molecular interaction or "
    "explicitly preserved receptor-associated complex; noncanonical receptor, "
    "effector, adhesion, ligand-form, isoform, species, assay, and non-SCI "
    "limitations remain explicit. No canonical-receptor, relay, TF/program, "
    "cellular-output, or SCI context is inferred."
)


def main() -> None:
    queue_fields, queue_rows = read_tsv(QUEUE)
    queue = {row["review_id"]: row for row in queue_rows}
    if SELECTED - set(queue):
        raise SystemExit(f"selected rows missing from queue: {sorted(SELECTED - set(queue))}")
    if any(queue[aid]["confidence_decision"] != "medium" for aid in SELECTED):
        raise SystemExit("selected rows are not all still medium in the Module 20A queue")

    edge_fields, edge_rows = read_tsv(B_EDGES)
    evidence_fields, evidence_rows = read_tsv(B_EVIDENCE)
    edges = {row["source_a_edge_id"]: row for row in edge_rows}
    frozen = {row["source_a_evidence_id"]: row for row in evidence_rows if row["source_kind"] == "frozen_module20a_lr_release"}
    direct = {}
    for row in evidence_rows:
        aid = row["source_a_evidence_id"]
        if aid not in SELECTED:
            continue
        if row["evidence_layer"] == "ligand_receptor_or_direct_molecular" and row["confidence_tier"].casefold() == "high" and row["exportable"].casefold() == "true" and row["b_evidence_id"].endswith("P2-DIRECT"):
            if aid in direct:
                raise SystemExit(f"multiple exact direct records for {aid}; review manually")
            direct[aid] = row
    if SELECTED - set(edges) or SELECTED - set(frozen) or SELECTED - set(direct):
        raise SystemExit("selected row missing B edge, frozen evidence, or exact direct evidence")
    if any(edges[aid]["confidence_tier"] != "medium" or edges[aid]["exportable"] != "true" for aid in SELECTED):
        raise SystemExit("selected B edges are not all medium/exportable")
    if any(frozen[aid]["confidence_tier"] != "medium" for aid in SELECTED):
        raise SystemExit("selected frozen LR evidence is not all medium")

    a_evidence_rows, a_decision_rows, audit_rows = [], [], []
    for index, aid in enumerate(sorted(SELECTED), start=1):
        q = queue[aid]
        primary = direct[aid]
        frozen_row = frozen[aid]
        evidence_id = f"M20A-MEDHIGH005-EVID-{index:04d}"
        mouse, mouse_rank = species_confidence(primary["species_support"], "mouse")
        human, human_rank = species_confidence(primary["species_support"], "human")
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
            "limitations": f"{primary['limitations']} High is limited to the tested molecular interaction; no canonical signaling or SCI-context inference is made.",
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
            "receptor_role": "noncanonical_or_receptor_associated_molecular_role",
            "directness": "exact_primary_direct_molecular_or_preserved_complex",
            "species_posture": "species_scoped_to_exact_primary_packet; no_unlisted_species_inference",
            "decision_basis": f"{BASIS} Source packet: {primary['b_evidence_id']}.",
            "evidence_register_ids": evidence_id,
            "next_action": "retain_high_direct_molecular_evidence; preserve_noncanonical_role; keep_relay_and_SCI_fields_separate",
        })
        edge = edges[aid]
        audit_rows.append({
            "review_id": aid,
            "pair_key": q["pair_key"],
            "pair_label_canonical": q["pair_label_canonical"],
            "b_edge_id": edge["b_edge_id"],
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
        q["curator_notes"] = append_once(q["curator_notes"], "Medium-direct-high batch005: exact primary direct evidence adjudicated high for the tested molecular interaction only; noncanonical role and downstream/SCI boundaries preserved.")
        edge.update({"confidence_tier": "high", "export_priority": "high", "exportable": "true", "consolidation_note": append_once(edge["consolidation_note"], "Medium-direct-high batch005: exact primary molecular interaction promoted; noncanonical role and context boundaries retained.")})
        frozen_row.update({"confidence_tier": "high", "exportable": "true", "consolidation_note": append_once(frozen_row["consolidation_note"], "Medium-direct-high batch005: exact primary molecular interaction promoted; noncanonical role and context boundaries retained.")})

    write_tsv(A_EVIDENCE, A_EVIDENCE_FIELDS, a_evidence_rows)
    write_tsv(A_DECISIONS, A_DECISION_FIELDS, a_decision_rows)
    write_tsv(QUEUE, queue_fields, queue_rows)
    write_tsv(B_EDGES, edge_fields, edge_rows)
    write_tsv(B_EVIDENCE, evidence_fields, evidence_rows)
    write_tsv(B_AUDIT, B_AUDIT_FIELDS, audit_rows)
    summary = {
        "generated_utc": datetime.now(UTC).isoformat(timespec="seconds"),
        "batch_id": "module20a_medium_direct_high_batch005",
        "rows_reviewed": len(SELECTED),
        "rows_promoted_to_high": len(SELECTED),
        "module20b_edges_promoted": len(SELECTED),
        "module20b_frozen_lr_evidence_promoted": len(SELECTED),
        "signaling_edges_created": 0,
        "excluded_known_provenance_collisions": ["M20A-EXT-2329", "M20A-EXT-2648"],
        "policy": BASIS,
        "selected_review_ids": sorted(SELECTED),
    }
    A_SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
