#!/usr/bin/env python3
"""Integrate the first child-adjudicated exact-pair Module 20A batch.

The child TSVs are read-only review artifacts.  This script accepts only the
listed rows, requires the child verdict to be high, and requires the
pre-existing low-evidence registry to say approve_candidate.  It creates
evidence/decision provenance, updates the review queue, and removes only these
rows from the low-evidence registry.  No SCI-context claims or relay edges are
created.
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTER = ROOT / "work" / "module20_db_seed" / "evidence_escalation_router"
STARTER = ROOT / "work" / "module20_db_seed" / "evidence_escalation_starter"
AGENTS = ROOT / "work" / "module20_db_seed" / "evidence_search_agents"
QUEUE = ROUTER / "module20a_external_review_queue.tsv"
LOW = ROUTER / "module20a_low_evidence_registry.tsv"
EVIDENCE = STARTER / "module20a_child_strong_batch001_evidence_register.tsv"
DECISIONS = STARTER / "module20a_child_strong_batch001_decision_register.tsv"
SUMMARY = STARTER / "module20a_child_strong_batch001_summary.json"

SELECTED = {
    "M20A-LIANA-REMAINING-0046",
    "M20A-LIANA-REMAINING-0057",
    "M20A-LIANA-REMAINING-0058",
    "M20A-LIANA-REMAINING-0059",
    "M20A-LIANA-REMAINING-0080",
    "M20A-LIANA-REMAINING-0093",
    "M20A-CELLCHAT-REMAINING-0450",
    "M20A-CELLCHAT-REMAINING-0452",
    "M20A-CELLCHAT-REMAINING-1250",
    "M20A-CELLCHAT-REMAINING-1251",
}

EVIDENCE_FIELDS = [
    "evidence_item_id", "review_id", "pair_key", "pair_label", "source_kind",
    "source_locator", "support_kind", "species_support", "source_scope",
    "confidence_tier", "citation_note", "evidence_summary", "limitations",
]
DECISION_FIELDS = [
    "review_id", "pair_key", "pair_label_canonical", "review_status",
    "confidence_decision", "mouse_confidence", "mouse_confidence_rank",
    "human_confidence", "human_confidence_rank", "human_evidence_present",
    "receptor_state", "receptor_role", "directness", "species_posture",
    "decision_basis", "evidence_register_ids", "next_action",
]


def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def child_rows() -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for path in sorted(AGENTS.glob("child_task_slice*_adjudication.tsv")):
        for row in read(path):
            rid = row["review_id"]
            if rid in SELECTED:
                if rid in rows:
                    raise SystemExit(f"duplicate selected child row: {rid}")
                rows[rid] = row
    return rows


def tier(species: str, token: str) -> tuple[str, str]:
    return ("high", "3") if token in species.casefold() else ("uncertain", "0")


def main() -> None:
    queue_rows = read(QUEUE)
    low_rows = read(LOW)
    queue = {row["review_id"]: row for row in queue_rows}
    low = {row["review_id"]: row for row in low_rows}
    child = child_rows()
    if SELECTED - set(queue):
        raise SystemExit(f"selected rows missing from queue: {sorted(SELECTED - set(queue))}")
    if SELECTED - set(low):
        raise SystemExit(f"selected rows missing from low registry: {sorted(SELECTED - set(low))}")
    if SELECTED - set(child):
        raise SystemExit(f"selected rows missing from child artifacts: {sorted(SELECTED - set(child))}")
    for rid in SELECTED:
        if low[rid]["agent_verdict"] != "approve_candidate":
            raise SystemExit(f"pre-existing registry does not approve {rid}")
        if child[rid]["verdict"] != "high":
            raise SystemExit(f"child verdict is not high for {rid}")
        if not child[rid]["source_locators"].strip():
            raise SystemExit(f"high child verdict has no source locator for {rid}")

    evidence_rows, decision_rows = [], []
    for index, rid in enumerate(sorted(SELECTED), start=1):
        row = child[rid]
        evidence_id = f"M20A-CHILDSTRONG01-EVID-{index:04d}"
        mouse, mouse_rank = tier(row["species_support"], "mouse")
        human, human_rank = tier(row["species_support"], "human")
        limitation = (row["limitations"] + " No SCI-specific context or intracellular relay inference is asserted by this batch.").strip()
        basis = "Child exact-pair review found high-confidence primary support; curator route requires exact source locators and pre-existing approve_candidate status. High applies to the ligand/receptor evidence claim only, not SCI context or downstream relay."
        evidence_rows.append({
            "evidence_item_id": evidence_id,
            "review_id": rid,
            "pair_key": row["pair_key"],
            "pair_label": row["pair_key"],
            "source_kind": "primary_literature",
            "source_locator": row["source_locators"],
            "support_kind": "child_adjudicated_exact_primary_support",
            "species_support": row["species_support"],
            "source_scope": "child_task_slices_exact_pair_review_batch001",
            "confidence_tier": "high",
            "citation_note": row["assay_or_result"],
            "evidence_summary": row["assay_or_result"],
            "limitations": limitation,
        })
        decision_rows.append({
            "review_id": rid,
            "pair_key": row["pair_key"],
            "pair_label_canonical": row["pair_key"],
            "review_status": "reviewed",
            "confidence_decision": "high",
            "mouse_confidence": mouse,
            "mouse_confidence_rank": mouse_rank,
            "human_confidence": human,
            "human_confidence_rank": human_rank,
            "human_evidence_present": "yes" if human == "high" else "no",
            "receptor_state": "membrane_bound_or_receptor_complex_context",
            "receptor_role": "ligand_receptor_or_receptor_complex_context",
            "directness": "child_adjudicated_primary_binding_or_matching_function",
            "species_posture": "species_scoped_to_child_source_record; no_unlisted_species_inference",
            "decision_basis": basis,
            "evidence_register_ids": evidence_id,
            "next_action": "retain_high_ligand_receptor_evidence; preserve_context; no_SignalingEdge_until_SCI_relevance_and_relay_review",
        })

    write(EVIDENCE, EVIDENCE_FIELDS, evidence_rows)
    write(DECISIONS, DECISION_FIELDS, decision_rows)

    for index, rid in enumerate(sorted(SELECTED), start=1):
        row = queue[rid]
        row["confidence_decision"] = "high"
        evidence_id = f"M20A-CHILDSTRONG01-EVID-{index:04d}"
        prior = row.get("evidence_register_ids", "").strip()
        row["evidence_register_ids"] = ";".join(x for x in (prior, evidence_id) if x)
        row["curator_notes"] = (row.get("curator_notes", "") + " Child-strong batch001: exact primary support rechecked; high for LR evidence only; no SCI or relay inference.").strip()
    write(QUEUE, list(queue_rows[0]), queue_rows)

    remaining_low = [row for row in low_rows if row["review_id"] not in SELECTED]
    write(LOW, list(low_rows[0]), sorted(remaining_low, key=lambda row: row["review_id"]))

    summary = {
        "generated_utc": datetime.now(UTC).isoformat(timespec="seconds"),
        "batch_id": "module20a_child_strong_batch001",
        "rows_reviewed": len(SELECTED),
        "rows_promoted_to_high": len(SELECTED),
        "rows_promoted_to_medium": 0,
        "rows_removed_from_low_evidence_registry": len(SELECTED),
        "signaling_edges_created": 0,
        "selected_review_ids": sorted(SELECTED),
        "policy": "Child high labels were accepted only when exact primary locators and pre-existing approve_candidate status were present; high is limited to the ligand/receptor evidence claim.",
        "child_artifacts": [str(path.relative_to(ROOT)) for path in sorted(AGENTS.glob("child_task_slice*_adjudication.tsv"))],
    }
    SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
