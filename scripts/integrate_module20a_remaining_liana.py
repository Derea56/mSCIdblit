#!/usr/bin/env python3
"""Integrate the remaining-LIANA search and citation-audit results conservatively."""

from __future__ import annotations

import csv
import glob
import json
import shutil
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work" / "module20_db_seed"
ROUTER = WORK / "evidence_escalation_router"
SEARCH = WORK / "evidence_search_agents" / "liana_remaining_batch_001"
AUDIT = WORK / "evidence_search_agents" / "liana_candidate_audit_001"
BATCH = WORK / "evidence_search_agents"
COMPARISON = ROUTER / "module20a_cellchat_liana_pair_comparison.tsv"
QUEUE = ROUTER / "module20a_external_review_queue.tsv"
LOW = ROUTER / "module20a_low_evidence_registry.tsv"
NO = ROUTER / "module20a_no_evidence_registry.tsv"
NON = ROUTER / "module20a_non_ligand_receptor_registry.tsv"
ADJ = BATCH / "liana_remaining_adjudication.tsv"
MANUAL = BATCH / "liana_remaining_manual_review.tsv"
SUMMARY = BATCH / "liana_remaining_integration_summary.json"

REPORT_FIELDS = ["pair_key", "pair_label_canonical", "verdict", "source_locators", "species_support", "support_kind", "evidence_summary", "limitations", "search_notes"]
AUDIT_FIELDS = ["pair_key", "pair_label_canonical", "final_verdict", "source_locators", "species_support", "support_kind", "evidence_summary", "limitations", "audit_notes"]
ADJ_FIELDS = ["review_id", "pair_key", "pair_label_canonical", "final_class", "source_locators", "species_support", "support_kind", "evidence_summary", "limitations", "search_notes"]
MANUAL_FIELDS = ADJ_FIELDS + ["manual_reason"]


def read(path: Path, delimiter: str = "\t") -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=delimiter))


def write(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def backup(path: Path, stamp: str) -> None:
    if path.exists():
        shutil.copy2(path, path.with_name(path.name + f".pre_liana_remaining_{stamp}"))


def main() -> None:
    comparison = {row["pair_key"]: row for row in read(COMPARISON)}
    queue_rows = read(QUEUE)
    queue_by_key = {row["pair_key"]: row for row in queue_rows}
    input_rows = []
    for path in sorted(SEARCH.glob("M20A-LIANA-REMAINING-*.tsv")):
        if path.name.endswith(".report.tsv"):
            continue
        input_rows.extend(read(path))
    if len(input_rows) != 799 or len({row["pair_key"] for row in input_rows}) != 799:
        raise SystemExit("remaining LIANA input packets must contain 799 unique rows")

    search_by_key: dict[str, dict[str, str]] = {}
    for path in sorted(SEARCH.glob("M20A-LIANA-REMAINING-*.report.tsv")):
        for row in read(path):
            if row["pair_key"] in search_by_key:
                raise SystemExit(f"duplicate search report {row['pair_key']}")
            search_by_key[row["pair_key"]] = row
    audit_by_key: dict[str, dict[str, str]] = {}
    for path in sorted(AUDIT.glob("M20A-LIANA-AUDIT-*.report.tsv")):
        for row in read(path):
            if row["pair_key"] in audit_by_key:
                raise SystemExit(f"duplicate audit report {row['pair_key']}")
            audit_by_key[row["pair_key"]] = row
    if set(search_by_key) != {row["pair_key"] for row in input_rows}:
        raise SystemExit("search reports do not cover exactly the 799 input pairs")
    if set(audit_by_key) != {key for key, row in search_by_key.items() if row["verdict"] == "promote_candidate"}:
        raise SystemExit("candidate audits do not cover exactly the 206 candidate rows")

    existing_low = read(LOW)
    existing_no = read(NO)
    existing_non = read(NON)
    existing_keys = {row["pair_key"] for row in existing_low + existing_no + existing_non}
    overlap = existing_keys & set(search_by_key)
    if overlap:
        raise SystemExit(f"remaining LIANA rows overlap existing ledgers: {len(overlap)}")

    stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    for path in (QUEUE, LOW, NO, NON):
        backup(path, stamp)

    new_low = list(existing_low)
    new_no = list(existing_no)
    new_non = list(existing_non)
    adjudications = []
    manuals = []
    counts = Counter()
    max_queue_id = 0

    def new_review_id(pair_key: str) -> str:
        nonlocal max_queue_id
        max_queue_id += 1
        return f"M20A-LIANA-REMAINING-{max_queue_id:04d}"

    for item in sorted(input_rows, key=lambda row: row["pair_key"]):
        key = item["pair_key"]
        search = search_by_key[key]
        if search["verdict"] == "promote_candidate":
            audit = audit_by_key[key]
            final = {
                "approve_candidate": "low_evidence",
                "retain_low": "low_evidence",
                "no_evidence": "no_evidence",
                "needs_manual_review": "manual_review",
                "reject_pair": "non_ligand_receptor",
            }[audit["final_verdict"]]
            source = audit
            verdict_note = f"Candidate audit verdict={audit['final_verdict']}."
        else:
            final = {
                "hold_low": "low_evidence",
                "no_evidence": "no_evidence",
                "needs_manual_review": "manual_review",
                "reject_pair": "non_ligand_receptor",
            }[search["verdict"]]
            source = search
            verdict_note = f"Expanded search verdict={search['verdict']}."
        rid = queue_by_key[key]["review_id"] if key in queue_by_key else new_review_id(key)
        counts[final] += 1
        record = {"review_id": rid, "pair_key": key, "pair_label_canonical": item["pair_label_canonical"], "final_class": final, "source_locators": source["source_locators"], "species_support": source["species_support"], "support_kind": source["support_kind"], "evidence_summary": source["evidence_summary"], "limitations": source["limitations"], "search_notes": (source.get("search_notes") or source.get("audit_notes", "")) + " " + verdict_note}
        adjudications.append(record)

        if key not in queue_by_key:
            comp = comparison[key]
            queue_by_key[key] = {
                "review_id": rid,
                "pair_key": key,
                "pair_label_canonical": item["pair_label_canonical"],
                "in_cellchat_priority": comp["in_cellchat_priority"],
                "in_cellchat_full": comp["in_cellchat_full"],
                "in_liana_consensus": "yes",
                "cellchat_priority_annotations": comp["cellchat_priority_annotations"],
                "cellchat_priority_pathways": comp["cellchat_priority_pathways"],
                "cellchat_priority_directness": comp["cellchat_priority_directness"],
                "complex_receptor_coverage": "not_assessed",
                "review_priority": "8",
                "review_priority_rationale": "liana_only_discovery",
                "review_status": "reviewed",
                "confidence_decision": "uncertain",
                "evidence_register_ids": "",
                "curator_notes": "Remaining LIANA pair searched in bounded exact-pair and expanded-family pass.",
            }
        q = queue_by_key[key]
        q["review_status"] = "reviewed"
        q["confidence_decision"] = "uncertain" if final == "manual_review" else "low"
        q["curator_notes"] = (q.get("curator_notes", "") + " " + verdict_note).strip()

        if final == "low_evidence":
            new_low.append({
                "review_id": rid, "pair_key": key, "pair_label_canonical": item["pair_label_canonical"], "review_priority": "8", "review_priority_rationale": "liana_only_discovery", "original_confidence": "low", "review_status": "reviewed", "search_attempt_count": "1", "last_search_iteration": "liana_remaining_batch_001", "agent_verdict": source.get("final_verdict", search["verdict"]), "source_locators": source["source_locators"], "species_support": source["species_support"], "support_kind": source["support_kind"], "evidence_summary": source["evidence_summary"], "limitations": source["limitations"], "evidence_class": "exact_or_contextual_liana_evidence", "curator_status": "pending_manual_approval" if source.get("final_verdict") == "approve_candidate" else "retained_low", "next_review_trigger": "Review exact citation, species, and receptor-complex scope before any confidence promotion.",
            })
        elif final == "no_evidence":
            new_no.append({
                "review_id": rid, "pair_key": key, "pair_label_canonical": item["pair_label_canonical"], "review_priority": "8", "review_priority_rationale": "liana_only_discovery", "original_confidence": "low", "search_status": "searched_pending_curator", "search_attempt_count": "1", "last_search_iteration": "liana_remaining_batch_001", "last_worker_verdict": "no_evidence", "source_locators": source["source_locators"], "species_support": source["species_support"], "support_kind": source["support_kind"], "evidence_summary": source["evidence_summary"], "limitations": source["limitations"], "no_evidence_category": "no_evidence_after_expanded_liana_search", "decision_basis": "Expanded LIANA-pair search found no qualifying exact primary evidence.", "next_review_trigger": "Revisit if a new exact primary source or processed/receptor-complex source is identified.",
            })
        elif final == "non_ligand_receptor":
            new_non.append({
                "review_id": rid, "pair_key": key, "pair_label_canonical": item["pair_label_canonical"], "review_priority": "8", "review_priority_rationale": "liana_only_discovery", "original_confidence": "low", "search_status": "completed_final_adjudication", "last_worker_verdict": "reject_pair", "source_locators": source["source_locators"], "support_kind": source["support_kind"], "evidence_summary": source["evidence_summary"], "limitations": source["limitations"], "disposition": "not_ligand_receptor", "decision_basis": "Expanded search classified the submitted relationship as wrong-pair or non-ligand-receptor.",
            })
        else:
            manuals.append({**record, "manual_reason": "Candidate or expanded search produced unresolved evidence requiring explicit curator review before low-evidence integration."})

    write(QUEUE, list(queue_rows[0]), sorted(queue_by_key.values(), key=lambda row: row["review_id"]))
    write(LOW, list(existing_low[0]), sorted(new_low, key=lambda row: row["review_id"]))
    write(NO, list(existing_no[0]), sorted(new_no, key=lambda row: row["review_id"]))
    write(NON, list(existing_non[0]), sorted(new_non, key=lambda row: row["review_id"]))
    write(ADJ, ADJ_FIELDS, sorted(adjudications, key=lambda row: row["pair_key"]))
    write(MANUAL, MANUAL_FIELDS, sorted(manuals, key=lambda row: row["pair_key"]))
    summary = {"generated_utc": datetime.now(UTC).isoformat(timespec="seconds"), "remaining_liana_rows": len(input_rows), "final_class_counts": dict(sorted(counts.items())), "queue_rows_added": sum(1 for row in input_rows if row["pair_key"] not in {r["pair_key"] for r in queue_rows}), "manual_review_rows": len(manuals), "confidence_promotions": 0, "canonical_ledgers_backed_up": True}
    SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
