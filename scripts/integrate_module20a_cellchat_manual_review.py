#!/usr/bin/env python3
"""Integrate the focused CellChat manual/uncertain re-review."""

from __future__ import annotations

import csv
import json
import shutil
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work" / "module20_db_seed"
ROUTER = WORK / "evidence_escalation_router"
REPORTS = WORK / "evidence_search_agents" / "cellchat_manual_review_batch_001"
QUEUE = ROUTER / "module20a_external_review_queue.tsv"
LOW = ROUTER / "module20a_low_evidence_registry.tsv"
NO = ROUTER / "module20a_no_evidence_registry.tsv"
NON = ROUTER / "module20a_non_ligand_receptor_registry.tsv"
ADJ = WORK / "evidence_search_agents" / "cellchat_manual_review_adjudication.tsv"
SUMMARY = WORK / "evidence_search_agents" / "cellchat_manual_review_integration_summary.json"

ADJ_FIELDS = ["review_id", "pair_key", "pair_label_canonical", "final_class", "source_locators", "species_support", "support_kind", "evidence_summary", "limitations", "review_notes"]


def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def backup(path: Path, stamp: str) -> None:
    shutil.copy2(path, path.with_name(path.name + f".pre_cellchat_manual_{stamp}"))


def main() -> None:
    reports: list[dict[str, str]] = []
    for path in sorted(REPORTS.glob("M20A-CELLCHAT-MANUAL-*.report.tsv")):
        reports.extend(read(path))
    if len(reports) != 411 or len({row["pair_key"] for row in reports}) != 411:
        raise SystemExit("manual re-review must contain 411 unique rows")

    queue_rows = read(QUEUE)
    queue_by_key = {row["pair_key"]: row for row in queue_rows}
    low_rows, no_rows, non_rows = read(LOW), read(NO), read(NON)
    low_keys = {row["pair_key"] for row in low_rows}
    no_keys = {row["pair_key"] for row in no_rows}
    non_keys = {row["pair_key"] for row in non_rows}
    overlap = (low_keys | no_keys | non_keys) & {row["pair_key"] for row in reports}
    if overlap:
        raise SystemExit(f"manual re-review pairs already classified in a ledger: {len(overlap)}")
    missing_queue = {row["pair_key"] for row in reports} - set(queue_by_key)
    if missing_queue:
        raise SystemExit(f"manual re-review pairs missing from queue: {len(missing_queue)}")

    stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    for path in (QUEUE, LOW, NO, NON):
        backup(path, stamp)

    counts: Counter[str] = Counter()
    adjudications = []
    for row in sorted(reports, key=lambda item: item["pair_key"]):
        key = row["pair_key"]
        final = row["final_class"]
        counts[final] += 1
        q = queue_by_key[key]
        if final == "promote_medium":
            confidence = "medium"
            qnote = "Focused manual re-review promoted to medium: " + row["evidence_summary"]
        elif final == "promote_low":
            confidence = "low"
            qnote = "Focused manual re-review promoted to low evidence: " + row["evidence_summary"]
        elif final in {"no_evidence", "non_ligand_receptor"}:
            confidence = "low"
            qnote = f"Focused manual re-review final disposition={final}: " + row["evidence_summary"]
        else:
            confidence = "uncertain"
            qnote = "Focused manual re-review retained uncertainty: " + row["evidence_summary"]
        q["review_status"] = "reviewed"
        q["confidence_decision"] = confidence
        q["curator_notes"] = (q.get("curator_notes", "") + " " + qnote).strip()
        adjudications.append(row)

        common = {
            "review_id": row["review_id"], "pair_key": key, "pair_label_canonical": row["pair_label_canonical"],
            "review_priority": q["review_priority"], "review_priority_rationale": q["review_priority_rationale"],
            "original_confidence": "uncertain", "source_locators": row["source_locators"],
            "species_support": row["species_support"], "support_kind": row["support_kind"],
            "evidence_summary": row["evidence_summary"], "limitations": row["limitations"],
        }
        if final == "promote_low":
            low_rows.append({**common, "review_status": "reviewed", "search_attempt_count": "2", "last_search_iteration": "cellchat_manual_review_batch_001", "agent_verdict": "promote_low", "evidence_class": "focused_manual_exact_or_contextual_cellchat_evidence", "curator_status": "retained_low", "next_review_trigger": "Revisit if a stronger exact-pair primary study supports medium confidence."})
        elif final == "no_evidence":
            no_rows.append({**common, "search_status": "searched_final_manual_review", "search_attempt_count": "2", "last_search_iteration": "cellchat_manual_review_batch_001", "last_worker_verdict": "no_evidence", "no_evidence_category": "no_evidence_after_focused_manual_review", "decision_basis": "Focused manual re-review found no qualifying exact-pair evidence.", "next_review_trigger": "Revisit only if a new exact primary source is identified."})
        elif final == "non_ligand_receptor":
            non_rows.append({"review_id": row["review_id"], "pair_key": key, "pair_label_canonical": row["pair_label_canonical"], "review_priority": q["review_priority"], "review_priority_rationale": q["review_priority_rationale"], "original_confidence": "uncertain", "search_status": "completed_final_manual_adjudication", "last_worker_verdict": "non_ligand_receptor", "source_locators": row["source_locators"], "support_kind": row["support_kind"], "evidence_summary": row["evidence_summary"], "limitations": row["limitations"], "disposition": "not_ligand_receptor", "decision_basis": "Focused manual re-review classified the submitted relationship as invalid ligand-receptor notation or wrong relationship."})

    write(QUEUE, list(queue_rows[0]), sorted(queue_by_key.values(), key=lambda row: row["review_id"]))
    write(LOW, list(low_rows[0]), sorted(low_rows, key=lambda row: row["review_id"]))
    write(NO, list(no_rows[0]), sorted(no_rows, key=lambda row: row["review_id"]))
    write(NON, list(non_rows[0]), sorted(non_rows, key=lambda row: row["review_id"]))
    write(ADJ, ADJ_FIELDS, adjudications)
    summary = {"generated_utc": datetime.now(UTC).isoformat(timespec="seconds"), "reviewed_rows": len(reports), "final_class_counts": dict(sorted(counts.items())), "medium_promotions": counts["promote_medium"], "low_promotions": counts["promote_low"], "no_evidence_added": counts["no_evidence"], "non_ligand_receptor_added": counts["non_ligand_receptor"], "retained_manual": counts["retain_manual"], "canonical_ledgers_backed_up": True}
    SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
