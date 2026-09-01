#!/usr/bin/env python3
"""Reconcile the already-adjudicated 2026-08-26 Module 20B high staging.

The staging file contains exact-pair high decisions that were materialized in
Module 20B but were not yet reflected in the Module 20A external queue.  This
script adds explicit Module 20A provenance, raises the corresponding frozen LR
evidence rows, and leaves the existing high B edges unchanged.
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
STAGING = ROOT / "work" / "module_b_consolidation" / "staging_round_2026_08_26" / "module20b" / "module20b_promoted_edge_candidates.tsv"
A_EVIDENCE = STARTER / "module20a_staged_high_reconciliation_2026_09_01_evidence_register.tsv"
A_DECISIONS = STARTER / "module20a_staged_high_reconciliation_2026_09_01_decision_register.tsv"
A_SUMMARY = STARTER / "module20a_staged_high_reconciliation_2026_09_01_summary.json"
B_EDGES = B_DIR / "module20b_edge_register.tsv"
B_EVIDENCE = B_DIR / "module20b_evidence_register.tsv"
B_AUDIT = B_DIR / "module20b_staged_high_reconciliation_2026_09_01.tsv"

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
    "review_id", "pair_key", "pair_label_canonical", "staging_candidate_id",
    "b_edge_id", "previous_edge_confidence", "previous_edge_exportable",
    "previous_frozen_evidence_confidence", "new_edge_confidence",
    "new_frozen_evidence_confidence", "a_evidence_id", "decision_basis",
]


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


def append_once(existing: str, note: str) -> str:
    return existing if note in existing else f"{existing} {note}".strip()


def main() -> None:
    _, queue_rows = read_tsv(QUEUE)
    queue = {row["review_id"]: row for row in queue_rows}
    _, staged = read_tsv(STAGING)
    if len(staged) != 44:
        raise SystemExit(f"Expected 44 staged high rows, found {len(staged)}")
    if any(row["decision"].casefold() not in {"promote_to_high", "promote_high"} for row in staged):
        raise SystemExit("staging contains a non-high decision")
    staged_by_id = {row["source_a_edge_id"]: row for row in staged}
    if len(staged_by_id) != len(staged):
        raise SystemExit("staging contains duplicate source_a_edge_id values")
    if any(aid not in queue for aid in staged_by_id):
        raise SystemExit("staging contains a row missing from the Module 20A queue")
    if any(queue[aid]["confidence_decision"] != "medium" for aid in staged_by_id):
        raise SystemExit("staging row is no longer medium in the Module 20A queue")

    edge_fields, edge_rows = read_tsv(B_EDGES)
    evidence_fields, evidence_rows = read_tsv(B_EVIDENCE)
    edges = {row["source_a_edge_id"]: row for row in edge_rows}
    frozen = {
        row["source_a_evidence_id"]: row
        for row in evidence_rows
        if row["source_kind"] == "frozen_module20a_lr_release"
    }
    if set(staged_by_id) - set(edges) or set(staged_by_id) - set(frozen):
        raise SystemExit("staging row missing from B edge or frozen evidence register")
    if any(edges[aid]["confidence_tier"] != "high" or edges[aid]["exportable"] != "true" for aid in staged_by_id):
        raise SystemExit("staging row does not have the expected high/exportable B edge")
    if any(frozen[aid]["confidence_tier"] != "medium" for aid in staged_by_id):
        raise SystemExit("staging row does not have the expected medium frozen evidence")

    a_evidence_rows = []
    a_decision_rows = []
    audit_rows = []
    for index, aid in enumerate(sorted(staged_by_id), start=1):
        s = staged_by_id[aid]
        q = queue[aid]
        evidence_id = f"M20A-STAGEDHIGH001-EVID-{index:04d}"
        locators = "; ".join(
            f"PMID:{value.strip()}" for value in (
                s["promotion_primary_pmids"], s["promotion_corroborating_pmids"]
            ) if value.strip()
        )
        a_evidence_rows.append({
            "evidence_item_id": evidence_id,
            "review_id": aid,
            "pair_key": q["pair_key"],
            "pair_label": q["pair_label_canonical"],
            "source_kind": "primary_literature_staging_reconciliation",
            "source_locator": locators,
            "support_kind": "staged_exact_pair_primary_support",
            "species_support": "mouse release scope from prior staged adjudication",
            "source_scope": "module20b_staging_round_2026_08_26_exact_pair_review",
            "confidence_tier": "high",
            "citation_note": s["evidence_summary"],
            "evidence_summary": s["evidence_summary"],
            "limitations": (
                f"{s['limitations']} High is limited to the staged pair-level LR claim; "
                "no relay, TF/program, cellular-output, or SCI-context inference is made."
            ),
        })
        basis = (
            "Reconciled the existing Module 20B staged high decision into Module 20A. "
            "The staged record states exact pair support and preserves complex, splice, "
            "cofactor, ligand-polarity, species, and context boundaries."
        )
        a_decision_rows.append({
            "review_id": aid,
            "pair_key": q["pair_key"],
            "pair_label_canonical": q["pair_label_canonical"],
            "review_status": "reviewed",
            "confidence_decision": "high",
            "mouse_confidence": "high",
            "mouse_confidence_rank": "3",
            "human_confidence": "uncertain",
            "human_confidence_rank": "0",
            "human_evidence_present": "no",
            "receptor_state": "membrane_bound_or_receptor_complex_context",
            "receptor_role": "ligand_receptor_or_receptor_complex_context",
            "directness": s["exact_evidence_status"],
            "species_posture": "mouse_release_scope_from_staged_record; no_unlisted_species_inference",
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
            "staging_candidate_id": s["staging_candidate_id"],
            "b_edge_id": edge["b_edge_id"],
            "previous_edge_confidence": edge["confidence_tier"],
            "previous_edge_exportable": edge["exportable"],
            "previous_frozen_evidence_confidence": frozen_row["confidence_tier"],
            "new_edge_confidence": "high",
            "new_frozen_evidence_confidence": "high",
            "a_evidence_id": evidence_id,
            "decision_basis": basis,
        })
        q["confidence_decision"] = "high"
        q["evidence_register_ids"] = ";".join(
            part for part in (q["evidence_register_ids"].strip(), evidence_id) if part
        )
        q["curator_notes"] = append_once(
            q["curator_notes"],
            "Staged-high reconciliation 2026-09-01: prior Module 20B exact-pair high decision reflected in Module 20A; context boundaries preserved.",
        )
        frozen_row.update({
            "confidence_tier": "high",
            "exportable": "true",
            "consolidation_note": append_once(
                frozen_row["consolidation_note"],
                "Staged-high reconciliation 2026-09-01: prior exact-pair high decision reflected in frozen LR evidence.",
            ),
        })

    write_tsv(A_EVIDENCE, A_EVIDENCE_FIELDS, a_evidence_rows)
    write_tsv(A_DECISIONS, A_DECISION_FIELDS, a_decision_rows)
    write_tsv(QUEUE, list(queue_rows[0]), queue_rows)
    write_tsv(B_EDGES, edge_fields, edge_rows)
    write_tsv(B_EVIDENCE, evidence_fields, evidence_rows)
    write_tsv(B_AUDIT, B_AUDIT_FIELDS, audit_rows)
    summary = {
        "generated_utc": datetime.now(UTC).isoformat(timespec="seconds"),
        "batch_id": "module20a_staged_high_reconciliation_2026_09_01",
        "rows_reconciled": len(staged),
        "rows_promoted_to_high_in_module20a_queue": len(staged),
        "module20b_edges_changed": 0,
        "module20b_frozen_lr_evidence_promoted": len(staged),
        "signaling_edges_created": 0,
        "source_staging": str(STAGING.relative_to(ROOT)),
        "policy": "Prior staged high decisions were reconciled only; no new pair or downstream claim was inferred.",
    }
    A_SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
