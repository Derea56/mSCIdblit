#!/usr/bin/env python3
"""Adjudicate a bounded medium-to-high Module 20A LR batch.

The selected rows already have exact, exportable high-confidence primary
direct-molecular records in the Module 20B evidence register.  This script
copies those source-bounded records into an explicit Module 20A decision
packet, updates the queue, and raises only the corresponding frozen LR edge
and frozen LR evidence row in Module 20B.  It does not infer relay, TF,
cellular-output, or SCI-context evidence.
"""

from __future__ import annotations

import csv
import io
import json
from datetime import UTC, datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ROUTER = ROOT / "work" / "module20_db_seed" / "evidence_escalation_router"
STARTER = ROOT / "work" / "module20_db_seed" / "evidence_escalation_starter"
B_DIR = ROOT / "work" / "module_b_consolidation" / "module20b"
QUEUE = ROUTER / "module20a_external_review_queue.tsv"
A_EVIDENCE = STARTER / "module20a_medium_direct_high_batch001_evidence_register.tsv"
A_DECISIONS = STARTER / "module20a_medium_direct_high_batch001_decision_register.tsv"
A_SUMMARY = STARTER / "module20a_medium_direct_high_batch001_summary.json"
B_EDGES = B_DIR / "module20b_edge_register.tsv"
B_EVIDENCE = B_DIR / "module20b_evidence_register.tsv"
B_AUDIT = B_DIR / "module20b_medium_direct_high_promotion_2026_09_01.tsv"

SELECTED = {
    "M20A-EXT-2545", "M20A-EXT-2549", "M20A-EXT-2567", "M20A-EXT-2568",
    "M20A-EXT-2569", "M20A-EXT-2570", "M20A-EXT-2574", "M20A-EXT-2581",
    "M20A-EXT-2589", "M20A-EXT-2590", "M20A-EXT-2594", "M20A-EXT-2605",
    "M20A-EXT-2606", "M20A-EXT-2607", "M20A-EXT-2630", "M20A-EXT-2632",
    "M20A-EXT-2670", "M20A-EXT-2772", "M20A-EXT-2809", "M20A-EXT-2856",
    "M20A-EXT-2867", "M20A-EXT-2910", "M20A-EXT-2931", "M20A-EXT-2946",
    "M20A-EXT-2948", "M20A-EXT-2949", "M20A-EXT-3210", "M20A-EXT-3211",
    "M20A-EXT-3213", "M20A-EXT-3214", "M20A-EXT-3402", "M20A-EXT-3460",
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

PROMOTION_BASIS = (
    "Exact pair-specific primary direct-molecular evidence was already validated "
    "at high tier in Module 20B. High applies to the ligand-receptor claim only; "
    "species, ligand processing, isoform, assay, receptor topology, and non-SCI "
    "limitations remain explicit. No relay, TF/program, cellular-output, or SCI "
    "context is inferred."
)


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    old_endings: list[str] = []
    old_contents: list[str] = []
    if path.exists():
        for line in path.read_bytes().splitlines(keepends=True):
            old_endings.append("\r\n" if line.endswith(b"\r\n") else "\n")
            old_contents.append(line.rstrip(b"\r\n").decode("utf-8"))
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    generated = buffer.getvalue().splitlines()
    default_ending = old_endings[-1] if old_endings else "\n"
    with path.open("w", encoding="utf-8", newline="") as handle:
        for index, line in enumerate(generated):
            unchanged = index < len(old_contents) and line == old_contents[index]
            ending = old_endings[index] if unchanged and index < len(old_endings) else default_ending
            handle.write(line + ending)


def species_confidence(species_support: str, species: str) -> tuple[str, str]:
    token = species.casefold()
    if token in species_support.casefold():
        return "high", "3"
    return "uncertain", "0"


def append_once(existing: str, note: str) -> str:
    return existing if note in existing else f"{existing} {note}".strip()


def main() -> None:
    queue_fields, queue_rows = read_tsv(QUEUE)
    queue = {row["review_id"]: row for row in queue_rows}
    if SELECTED - set(queue):
        raise SystemExit(f"selected rows missing from queue: {sorted(SELECTED - set(queue))}")
    if any(queue[rid]["confidence_decision"] != "medium" for rid in SELECTED):
        bad = sorted(rid for rid in SELECTED if queue[rid]["confidence_decision"] != "medium")
        raise SystemExit(f"selected rows are not currently medium: {bad}")

    edge_fields, edge_rows = read_tsv(B_EDGES)
    evidence_fields, evidence_rows = read_tsv(B_EVIDENCE)
    edges = {row["source_a_edge_id"]: row for row in edge_rows}
    if len(edges) != len(edge_rows):
        raise SystemExit("Module 20B edge register has duplicate source_a_edge_id values")

    direct = {}
    frozen = {}
    for row in evidence_rows:
        aid = row["source_a_evidence_id"]
        if aid not in SELECTED:
            continue
        if row["source_kind"] == "frozen_module20a_lr_release":
            if row["evidence_layer"] != "ligand_receptor_or_direct_molecular":
                continue
            if aid in frozen:
                raise SystemExit(f"duplicate frozen evidence for {aid}")
            frozen[aid] = row
        elif (
            row["evidence_layer"] == "ligand_receptor_or_direct_molecular"
            and row["confidence_tier"].casefold() == "high"
            and row["exportable"].casefold() == "true"
            and row["b_evidence_id"].endswith("P2-DIRECT")
        ):
            if aid in direct:
                raise SystemExit(f"multiple exact direct records for {aid}; review manually")
            direct[aid] = row
    missing = sorted(SELECTED - set(direct))
    if missing:
        raise SystemExit(f"selected rows missing exact high direct evidence: {missing}")
    missing = sorted(SELECTED - set(frozen))
    if missing:
        raise SystemExit(f"selected rows missing frozen evidence: {missing}")
    for aid in SELECTED:
        if aid not in edges:
            raise SystemExit(f"selected row missing B edge: {aid}")
        if edges[aid]["confidence_tier"] != "medium" or edges[aid]["exportable"] != "true":
            raise SystemExit(f"selected B edge is not medium/exportable: {aid}")

    a_evidence_rows = []
    a_decision_rows = []
    audit_rows = []
    for index, aid in enumerate(sorted(SELECTED), start=1):
        q = queue[aid]
        primary = direct[aid]
        frozen_row = frozen[aid]
        evidence_id = f"M20A-MEDHIGH001-EVID-{index:04d}"
        mouse, mouse_rank = species_confidence(primary["species_support"], "mouse")
        human, human_rank = species_confidence(primary["species_support"], "human")
        limitations = (
            f"{primary['limitations']} High is limited to the exact ligand-receptor "
            "claim; no SCI-context or downstream relay inference is made."
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
        basis = f"{PROMOTION_BASIS} Source packet: {primary['b_evidence_id']}."
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
            "receptor_role": "ligand_receptor_or_receptor_complex_context",
            "directness": "exact_primary_direct_binding_or_activation",
            "species_posture": "species_scoped_to_exact_primary_packet; no_unlisted_species_inference",
            "decision_basis": basis,
            "evidence_register_ids": evidence_id,
            "next_action": "retain_high_ligand_receptor_evidence; preserve_context; keep_relay_and_SCI_fields_separate",
        })

        edge = edges[aid]
        frozen_row = frozen[aid]
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
            "decision_basis": PROMOTION_BASIS,
        })

        q["confidence_decision"] = "high"
        q["evidence_register_ids"] = ";".join(
            part for part in (q["evidence_register_ids"].strip(), evidence_id) if part
        )
        q["curator_notes"] = append_once(
            q["curator_notes"],
            "Medium-direct-high batch001: exact primary direct evidence adjudicated high for LR evidence only; relay, TF/program, cellular output, and SCI context remain separate.",
        )

        edge.update({
            "confidence_tier": "high",
            "export_priority": "high",
            "exportable": "true",
            "consolidation_note": append_once(
                edge["consolidation_note"],
                "Medium-direct-high batch001: exact primary LR evidence promoted; context boundaries retained.",
            ),
        })
        frozen_row.update({
            "confidence_tier": "high",
            "exportable": "true",
            "consolidation_note": append_once(
                frozen_row["consolidation_note"],
                "Medium-direct-high batch001: exact primary LR evidence promoted; context boundaries retained.",
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
        "batch_id": "module20a_medium_direct_high_batch001",
        "rows_reviewed": len(SELECTED),
        "rows_promoted_to_high": len(SELECTED),
        "rows_promoted_to_medium": 0,
        "module20b_edges_promoted": len(SELECTED),
        "module20b_frozen_lr_evidence_promoted": len(SELECTED),
        "signaling_edges_created": 0,
        "excluded_known_provenance_collision": "M20A-EXT-2329",
        "policy": PROMOTION_BASIS,
        "selected_review_ids": sorted(SELECTED),
        "source_evidence": "Each selected row requires one exact, exportable high-tier P2-DIRECT record in module20b_evidence_register.tsv.",
    }
    A_SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
