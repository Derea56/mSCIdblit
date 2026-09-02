#!/usr/bin/env python3
"""Integrate the seventh bounded medium-to-high Module 20A LR packet.

This packet promotes only exact primary direct-molecular or explicitly
preserved receptor-complex evidence. Species, ligand form, isoform, atypical
receptor, assay, and non-SCI limitations remain attached to each source record.
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


A_EVIDENCE = STARTER / "module20a_medium_direct_high_batch007_evidence_register.tsv"
A_DECISIONS = STARTER / "module20a_medium_direct_high_batch007_decision_register.tsv"
A_SUMMARY = STARTER / "module20a_medium_direct_high_batch007_summary.json"
B_AUDIT = B_DIR / "module20b_medium_direct_high_batch007_2026_09_01.tsv"

EDGE_TO_REVIEW = {
    "M20B-E001780": "M20A-EXT-0005",
    "M20B-E001842": "M20A-EXT-0067",
    "M20B-E001843": "M20A-EXT-0068",
    "M20B-E001844": "M20A-EXT-0069",
    "M20B-E001884": "M20A-EXT-0109",
    "M20B-E001890": "M20A-EXT-0115",
    "M20B-E001891": "M20A-EXT-0116",
    "M20B-E002837": "M20A-EXT-1062",
    "M20B-E004107": "M20A-EXT-2332",
    "M20B-E004124": "M20A-EXT-2349",
    "M20B-E004126": "M20A-EXT-2351",
    "M20B-E004440": "M20A-EXT-2665",
    "M20B-E004521": "M20A-EXT-2746",
    "M20B-E005111": "M20A-EXT-3336",
    "M20B-E005209": "M20A-EXT-3434",
}
SELECTED = set(EDGE_TO_REVIEW.values())

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
    "receptor-complex evidence was validated at high tier in Module 20B. High "
    "applies only to the tested molecular interaction; atypical receptor or "
    "receptor-complex topology, ligand form, isoform, species, assay, and "
    "non-SCI limitations remain explicit. No relay, TF/program, cellular-output, "
    "or SCI context is inferred."
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
    edges = {row["b_edge_id"]: row for row in edge_rows}
    frozen = {
        row["source_a_evidence_id"]: row
        for row in evidence_rows
        if row["source_kind"] == "frozen_module20a_lr_release"
    }
    direct = {}
    for row in evidence_rows:
        edge_ids = set(row["b_edge_ids"].split(";"))
        matching_edges = edge_ids & set(EDGE_TO_REVIEW)
        if len(matching_edges) != 1:
            continue
        edge_id = next(iter(matching_edges))
        if (
            row["evidence_layer"] == "ligand_receptor_or_direct_molecular"
            and row["confidence_tier"].casefold() == "high"
            and row["exportable"].casefold() == "true"
            and "-P2-DIRECT" in row["b_evidence_id"]
        ):
            if edge_id in direct:
                raise SystemExit(f"multiple exact direct records for {edge_id}; review manually")
            direct[edge_id] = row
    if SELECTED - set(frozen) or set(EDGE_TO_REVIEW) - set(direct):
        raise SystemExit("selected row missing B edge, frozen evidence, or exact direct evidence")
    if any(edges[edge_id]["confidence_tier"] != "medium" or edges[edge_id]["exportable"] != "true" for edge_id in EDGE_TO_REVIEW):
        raise SystemExit("selected B edges are not all medium/exportable")
    if any(frozen[aid]["confidence_tier"] != "medium" for aid in SELECTED):
        raise SystemExit("selected frozen LR evidence is not all medium")

    a_evidence_rows, a_decision_rows, audit_rows = [], [], []
    for index, aid in enumerate(sorted(SELECTED), start=1):
        q = queue[aid]
        edge_id = next(edge_id for edge_id, review_id in EDGE_TO_REVIEW.items() if review_id == aid)
        edge = edges[edge_id]
        if edge["source_a_edge_id"] != aid:
            raise SystemExit(f"source A edge mapping mismatch for {edge_id}: {aid} != {edge['source_a_edge_id']}")
        primary = direct[edge_id]
        frozen_row = frozen[aid]
        evidence_id = f"M20A-MEDHIGH007-EVID-{index:04d}"
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
        q["evidence_register_ids"] = ";".join(
            part for part in (q["evidence_register_ids"].strip(), evidence_id) if part
        )
        q["curator_notes"] = append_once(
            q["curator_notes"],
            "Medium-direct-high batch007: exact primary direct or explicitly preserved complex evidence adjudicated high for the tested molecular interaction only; topology, ligand-form, species, downstream, and SCI boundaries preserved.",
        )
        edge.update({
            "confidence_tier": "high",
            "export_priority": "high",
            "exportable": "true",
            "consolidation_note": append_once(
                edge["consolidation_note"],
                "Medium-direct-high batch007: exact primary molecular interaction promoted; topology and context boundaries retained.",
            ),
        })
        frozen_row.update({
            "confidence_tier": "high",
            "exportable": "true",
            "consolidation_note": append_once(
                frozen_row["consolidation_note"],
                "Medium-direct-high batch007: exact primary molecular interaction promoted; topology and context boundaries retained.",
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
        "batch_id": "module20a_medium_direct_high_batch007",
        "rows_reviewed": len(SELECTED),
        "rows_promoted_to_high": len(SELECTED),
        "module20b_edges_promoted": len(EDGE_TO_REVIEW),
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
