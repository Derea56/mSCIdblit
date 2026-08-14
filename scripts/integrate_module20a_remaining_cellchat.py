#!/usr/bin/env python3
"""Integrate CellChat search and citation-audit results conservatively."""

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
SEARCH = WORK / "evidence_search_agents" / "cellchat_remaining_batch_001"
AUDIT_DIRS = [
    WORK / "evidence_search_agents" / "cellchat_candidate_audit_001",
    WORK / "evidence_search_agents" / "cellchat_candidate_audit_002",
]
BATCH = WORK / "evidence_search_agents"
COMPARISON = ROUTER / "module20a_cellchat_liana_pair_comparison.tsv"
QUEUE = ROUTER / "module20a_external_review_queue.tsv"
LOW = ROUTER / "module20a_low_evidence_registry.tsv"
NO = ROUTER / "module20a_no_evidence_registry.tsv"
NON = ROUTER / "module20a_non_ligand_receptor_registry.tsv"
ADJ = BATCH / "cellchat_remaining_adjudication.tsv"
MANUAL = BATCH / "cellchat_remaining_manual_review.tsv"
SUMMARY = BATCH / "cellchat_remaining_integration_summary.json"

REPORT_FIELDS = ["pair_key", "pair_label_canonical", "verdict", "source_locators", "species_support", "support_kind", "evidence_summary", "limitations", "search_notes"]
AUDIT_FIELDS = ["pair_key", "pair_label_canonical", "final_verdict", "source_locators", "species_support", "support_kind", "evidence_summary", "limitations", "audit_notes"]
ADJ_FIELDS = ["review_id", "pair_key", "pair_label_canonical", "final_class", "source_locators", "species_support", "support_kind", "evidence_summary", "limitations", "search_notes"]
MANUAL_FIELDS = ADJ_FIELDS + ["manual_reason"]


def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def backup(path: Path, stamp: str) -> None:
    if path.exists():
        shutil.copy2(path, path.with_name(path.name + f".pre_cellchat_remaining_{stamp}"))


def main() -> None:
    comparison = {row["pair_key"]: row for row in read(COMPARISON)}
    queue_rows = read(QUEUE)
    queue_by_key = {row["pair_key"]: row for row in queue_rows}
    input_rows: list[dict[str, str]] = []
    for path in sorted(SEARCH.glob("M20A-CELLCHAT-REMAINING-*.tsv")):
        if path.name.endswith(".report.tsv"):
            continue
        input_rows.extend(read(path))
    if len(input_rows) != 1869 or len({row["pair_key"] for row in input_rows}) != 1869:
        raise SystemExit("CellChat input packets must contain 1869 unique rows")

    search_by_key: dict[str, dict[str, str]] = {}
    for path in sorted(SEARCH.glob("M20A-CELLCHAT-REMAINING-*.report.tsv")):
        for row in read(path):
            if row["pair_key"] in search_by_key:
                raise SystemExit(f"duplicate search report {row['pair_key']}")
            search_by_key[row["pair_key"]] = row
    if set(search_by_key) != {row["pair_key"] for row in input_rows}:
        raise SystemExit("search reports do not cover exactly the 1869 CellChat input pairs")

    candidate_keys = {key for key, row in search_by_key.items() if row["verdict"] == "promote_candidate"}
    audit_by_key: dict[str, dict[str, str]] = {}
    for audit_dir in AUDIT_DIRS:
        for path in sorted(audit_dir.glob("*.report.tsv")):
            for row in read(path):
                if row["pair_key"] in audit_by_key:
                    raise SystemExit(f"duplicate audit report {row['pair_key']}")
                audit_by_key[row["pair_key"]] = row
    if set(audit_by_key) != candidate_keys:
        raise SystemExit(f"candidate audits cover {len(audit_by_key)} rows but {len(candidate_keys)} are required")

    existing_low = read(LOW)
    existing_no = read(NO)
    existing_non = read(NON)
    existing_keys = {row["pair_key"] for row in existing_low + existing_no + existing_non}
    overlap = existing_keys & set(search_by_key)
    if overlap:
        raise SystemExit(f"CellChat rows overlap existing ledgers: {len(overlap)}")

    stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    for path in (QUEUE, LOW, NO, NON):
        backup(path, stamp)

    new_low, new_no, new_non = list(existing_low), list(existing_no), list(existing_non)
    adjudications: list[dict[str, str]] = []
    manuals: list[dict[str, str]] = []
    counts: Counter[str] = Counter()
    max_queue_id = 0

    def new_review_id() -> str:
        nonlocal max_queue_id
        max_queue_id += 1
        return f"M20A-CELLCHAT-REMAINING-{max_queue_id:04d}"

    for item in sorted(input_rows, key=lambda row: row["pair_key"]):
        key = item["pair_key"]
        search = search_by_key[key]
        if search["verdict"] == "promote_candidate":
            source = audit_by_key[key]
            final = {"approve_candidate": "low_evidence", "retain_low": "low_evidence", "no_evidence": "no_evidence", "needs_manual_review": "manual_review", "reject_pair": "non_ligand_receptor"}[source["final_verdict"]]
            note = f"Candidate citation audit verdict={source['final_verdict']}."
        else:
            source = search
            final = {"hold_low": "low_evidence", "no_evidence": "no_evidence", "needs_manual_review": "manual_review", "reject_pair": "non_ligand_receptor"}[search["verdict"]]
            note = f"Expanded CellChat search verdict={search['verdict']}."

        rid = queue_by_key[key]["review_id"] if key in queue_by_key else new_review_id()
        counts[final] += 1
        record = {"review_id": rid, "pair_key": key, "pair_label_canonical": item["pair_label_canonical"], "final_class": final, "source_locators": source["source_locators"], "species_support": source["species_support"], "support_kind": source["support_kind"], "evidence_summary": source["evidence_summary"], "limitations": source["limitations"], "search_notes": (source.get("search_notes") or source.get("audit_notes", "")) + " " + note}
        adjudications.append(record)

        if key not in queue_by_key:
            comp = comparison[key]
            priority = "2" if comp["in_cellchat_priority"] == "yes" else "8"
            queue_by_key[key] = {
                "review_id": rid, "pair_key": key, "pair_label_canonical": item["pair_label_canonical"],
                "in_cellchat_priority": comp["in_cellchat_priority"], "in_cellchat_full": comp["in_cellchat_full"],
                "in_liana_consensus": comp["in_liana_consensus"], "cellchat_priority_annotations": comp["cellchat_priority_annotations"],
                "cellchat_priority_pathways": comp["cellchat_priority_pathways"], "cellchat_priority_directness": comp["cellchat_priority_directness"],
                "complex_receptor_coverage": "not_assessed", "review_priority": priority,
                "review_priority_rationale": "cellchat_priority_signaling" if priority == "2" else "cellchat_remaining_discovery",
                "review_status": "reviewed", "confidence_decision": "uncertain", "evidence_register_ids": "",
                "curator_notes": "Remaining CellChat pair searched in bounded exact-pair and expanded-family pass.",
            }
        q = queue_by_key[key]
        q["review_status"] = "reviewed"
        q["confidence_decision"] = "uncertain" if final == "manual_review" else "low"
        q["curator_notes"] = (q.get("curator_notes", "") + " " + note).strip()

        comp = comparison[key]
        priority = "2" if comp["in_cellchat_priority"] == "yes" else "8"
        rationale = "cellchat_priority_signaling" if priority == "2" else "cellchat_remaining_discovery"
        common = {"review_id": rid, "pair_key": key, "pair_label_canonical": item["pair_label_canonical"], "review_priority": priority, "review_priority_rationale": rationale, "original_confidence": "low", "source_locators": source["source_locators"], "species_support": source["species_support"], "support_kind": source["support_kind"], "evidence_summary": source["evidence_summary"], "limitations": source["limitations"]}
        if final == "low_evidence":
            new_low.append({**common, "review_status": "reviewed", "search_attempt_count": "1", "last_search_iteration": "cellchat_remaining_batch_001", "agent_verdict": source.get("final_verdict", search["verdict"]), "evidence_class": "exact_or_contextual_cellchat_evidence", "curator_status": "pending_manual_approval" if source.get("final_verdict") == "approve_candidate" else "retained_low", "next_review_trigger": "Review exact citation, species, and receptor-complex scope before any confidence promotion."})
        elif final == "no_evidence":
            new_no.append({**common, "search_status": "searched_pending_curator", "search_attempt_count": "1", "last_search_iteration": "cellchat_remaining_batch_001", "last_worker_verdict": "no_evidence", "no_evidence_category": "no_evidence_after_expanded_cellchat_search", "decision_basis": "Expanded CellChat-pair search found no qualifying exact primary evidence.", "next_review_trigger": "Revisit if a new exact primary source or processed/receptor-complex source is identified."})
        elif final == "non_ligand_receptor":
            new_non.append({
                "review_id": rid, "pair_key": key, "pair_label_canonical": item["pair_label_canonical"],
                "review_priority": priority, "review_priority_rationale": rationale, "original_confidence": "low",
                "search_status": "completed_final_adjudication", "last_worker_verdict": "reject_pair",
                "source_locators": source["source_locators"], "support_kind": source["support_kind"],
                "evidence_summary": source["evidence_summary"], "limitations": source["limitations"],
                "disposition": "not_ligand_receptor",
                "decision_basis": "Expanded search classified the submitted relationship as wrong-pair or non-ligand-receptor.",
            })
        else:
            manuals.append({**record, "manual_reason": "Evidence remains unresolved after CellChat search or citation audit; curator review is required before ledger classification."})

    write(QUEUE, list(queue_rows[0]), sorted(queue_by_key.values(), key=lambda row: row["review_id"]))
    write(LOW, list(existing_low[0]), sorted(new_low, key=lambda row: row["review_id"]))
    write(NO, list(existing_no[0]), sorted(new_no, key=lambda row: row["review_id"]))
    write(NON, list(existing_non[0]), sorted(new_non, key=lambda row: row["review_id"]))
    write(ADJ, ADJ_FIELDS, sorted(adjudications, key=lambda row: row["pair_key"]))
    write(MANUAL, MANUAL_FIELDS, sorted(manuals, key=lambda row: row["pair_key"]))
    summary = {"generated_utc": datetime.now(UTC).isoformat(timespec="seconds"), "remaining_cellchat_rows": len(input_rows), "final_class_counts": dict(sorted(counts.items())), "queue_rows_added": sum(1 for row in input_rows if row["pair_key"] not in {r["pair_key"] for r in queue_rows}), "manual_review_rows": len(manuals), "confidence_promotions": 0, "canonical_ledgers_backed_up": True}
    SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
