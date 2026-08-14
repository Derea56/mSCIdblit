#!/usr/bin/env python3
"""Integrate the independent CellChat non-LR audit."""

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
REPORTS = WORK / "evidence_search_agents" / "cellchat_nonlr_audit_batch_001"
QUEUE = ROUTER / "module20a_external_review_queue.tsv"
LOW = ROUTER / "module20a_low_evidence_registry.tsv"
NO = ROUTER / "module20a_no_evidence_registry.tsv"
NON = ROUTER / "module20a_non_ligand_receptor_registry.tsv"
ADJ = WORK / "evidence_search_agents" / "cellchat_nonlr_audit_adjudication.tsv"
SUMMARY = WORK / "evidence_search_agents" / "cellchat_nonlr_audit_integration_summary.json"
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
    shutil.copy2(path, path.with_name(path.name + f".pre_cellchat_nonlr_audit_{stamp}"))


def main() -> None:
    reports: list[dict[str, str]] = []
    for path in sorted(REPORTS.glob("M20A-CELLCHAT-NONLR-AUDIT-*.report.tsv")):
        reports.extend(read(path))
    if len(reports) != 397 or len({row["pair_key"] for row in reports}) != 397:
        raise SystemExit("non-LR audit must contain 397 unique CellChat-full rows")

    queue_rows = read(QUEUE)
    queue_by_key = {row["pair_key"]: row for row in queue_rows}
    low_rows, no_rows, non_rows = read(LOW), read(NO), read(NON)
    non_by_key = {row["pair_key"]: row for row in non_rows}
    keys = {row["pair_key"] for row in reports}
    if keys - set(queue_by_key) or keys - set(non_by_key):
        raise SystemExit("audited non-LR rows must already exist in queue and non-LR registry")

    stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    for path in (QUEUE, LOW, NO, NON):
        backup(path, stamp)

    counts: Counter[str] = Counter()
    adjudications = []
    restored_low = []
    retained_non = []
    for row in sorted(reports, key=lambda item: item["pair_key"]):
        key = row["pair_key"]
        final = row["final_class"]
        counts[final] += 1
        q = queue_by_key[key]
        if final == "restore_medium":
            q["confidence_decision"] = "medium"
            qnote = "Independent non-LR audit restored this as medium-confidence LR evidence: " + row["evidence_summary"]
        elif final == "restore_low":
            q["confidence_decision"] = "low"
            qnote = "Independent non-LR audit restored this as low-evidence LR: " + row["evidence_summary"]
            restored_low.append({
                "review_id": row["review_id"], "pair_key": key, "pair_label_canonical": row["pair_label_canonical"],
                "review_priority": q["review_priority"], "review_priority_rationale": q["review_priority_rationale"], "original_confidence": "low",
                "review_status": "reviewed", "search_attempt_count": "2", "last_search_iteration": "cellchat_nonlr_audit_batch_001", "agent_verdict": "restore_low",
                "source_locators": row["source_locators"], "species_support": row["species_support"], "support_kind": row["support_kind"],
                "evidence_summary": row["evidence_summary"], "limitations": row["limitations"], "evidence_class": "restored_from_non_ligand_receptor_audit",
                "curator_status": "retained_low", "next_review_trigger": "Revisit processed-ligand or complex notation if a stronger exact-pair source becomes available.",
            })
        elif final == "retain_manual":
            q["confidence_decision"] = "uncertain"
            qnote = "Independent non-LR audit retained manual status: " + row["evidence_summary"]
        else:
            q["confidence_decision"] = "low"
            qnote = "Independent non-LR audit confirmed invalid LR notation: " + row["evidence_summary"]
            retained_non.append(non_by_key[key])
        q["review_status"] = "reviewed"
        q["curator_notes"] = (q.get("curator_notes", "") + " " + qnote).strip()
        adjudications.append(row)

    remaining_non = [row for key, row in non_by_key.items() if key not in keys] + retained_non
    write(QUEUE, list(queue_rows[0]), sorted(queue_by_key.values(), key=lambda row: row["review_id"]))
    write(LOW, list(low_rows[0]), sorted(low_rows + restored_low, key=lambda row: row["review_id"]))
    write(NO, list(no_rows[0]), sorted(no_rows, key=lambda row: row["review_id"]))
    write(NON, list(non_rows[0]), sorted(remaining_non, key=lambda row: row["review_id"]))
    write(ADJ, ADJ_FIELDS, adjudications)
    summary = {"generated_utc": datetime.now(UTC).isoformat(timespec="seconds"), "audited_rows": len(reports), "final_class_counts": dict(sorted(counts.items())), "restored_low": counts["restore_low"], "restored_medium": counts["restore_medium"], "retained_manual": counts["retain_manual"], "confirmed_non_ligand_receptor": counts["retain_non_ligand_receptor"], "canonical_ledgers_backed_up": True}
    SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
