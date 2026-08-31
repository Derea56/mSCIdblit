#!/usr/bin/env python3
"""Validate agent batch 007 and refresh Module 20A revisit registries."""

from __future__ import annotations

import csv
import json
import re
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work" / "module20_db_seed"
BATCH = WORK / "evidence_search_agents" / "agent_batch_007"
QUEUE = WORK / "evidence_escalation_router" / "module20a_external_review_queue.tsv"
LEDGER = WORK / "evidence_search_agents" / "iterative" / "low_search_ledger.tsv"
NO_EVIDENCE = WORK / "evidence_escalation_router" / "module20a_no_evidence_registry.tsv"
NON_LR = WORK / "evidence_escalation_router" / "module20a_non_ligand_receptor_registry.tsv"
CURATOR = BATCH / "agent_batch007_curator_review_register.tsv"

REPORT_FIELDS = ["review_id", "pair_key", "verdict", "source_locators", "species_support", "support_kind", "evidence_summary", "limitations", "search_notes"]
NO_FIELDS = ["review_id", "pair_key", "pair_label_canonical", "review_priority", "review_priority_rationale", "original_confidence", "search_status", "search_attempt_count", "last_search_iteration", "last_worker_verdict", "source_locators", "species_support", "support_kind", "evidence_summary", "limitations", "no_evidence_category", "decision_basis", "next_review_trigger"]
NON_FIELDS = ["review_id", "pair_key", "pair_label_canonical", "review_priority", "review_priority_rationale", "original_confidence", "search_status", "last_worker_verdict", "source_locators", "support_kind", "evidence_summary", "limitations", "disposition", "decision_basis"]
CURATOR_FIELDS = ["review_id", "pair_key", "pair_label_canonical", "agent_verdict", "curator_route", "source_locators", "species_support", "support_kind", "evidence_summary", "limitations", "search_notes"]

NO_RE = re.compile(r"none|no_qualifying|no_exact|negative|noncognate|cooccurrence|coexpression|family_context_negative|pathway_lead|network_association|family_triage|isoform_mismatched|family_or_|not_established|not supported|did not establish|did not isolate|not tested|not shown|not a qualifying|not demonstrated|no pair-specific", re.I)
POS_RE = re.compile(r"exact pair is source-anchored|direct_binding|direct binding|direct_.*function|binding_and_contextual_function|source-anchored", re.I)
NON_LR_RE = re.compile(r"non.?ligand.?receptor|non.?lr|intracellular|enzyme.?substrate|receptor.?receptor|wrong.?pair|adaptor|scaffold|transporter", re.I)


def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def old_route(row: dict[str, str]) -> str:
    verdict = row.get("worker_verdict", "")
    text = " ".join((row.get("support_kind", ""), row.get("evidence_summary", ""), row.get("limitations", "")))
    if verdict == "reject_pair":
        return "not_ligand_receptor" if NON_LR_RE.search(text) else "no_evidence_after_search"
    if verdict == "hold_low" and NO_RE.search(text) and not POS_RE.search(text):
        return "no_evidence_after_search"
    return verdict or "unclassified_low"


def main() -> None:
    queue_rows = read(QUEUE)
    queue = {r["review_id"]: r for r in queue_rows}
    ledger = {r["review_id"]: r for r in read(LEDGER)}
    selected = [r for r in queue_rows if r["confidence_decision"] == "low" and r["review_priority"] in {"1", "2", "6", "7"}]
    selected.sort(key=lambda r: (int(r["review_priority"]), r["review_id"]))
    selected = selected[:200]
    selected_ids = {r["review_id"] for r in selected}
    reports: dict[str, dict[str, str]] = {}
    for i in range(1, 9):
        path = BATCH / f"M20A-AGENT007-{i:02d}.report.tsv"
        rows = read(path)
        if list(rows[0]) != REPORT_FIELDS or len(rows) != 25:
            raise SystemExit(f"invalid report schema or row count: {path}")
        for row in rows:
            if row["review_id"] not in selected_ids or row["review_id"] in reports:
                raise SystemExit(f"unexpected or duplicate report row: {row['review_id']}")
            reports[row["review_id"]] = row
    if set(reports) != selected_ids:
        raise SystemExit(f"report coverage mismatch: expected {len(selected_ids)}, got {len(reports)}")

    # Overlay the agent's exact-pair verdicts onto the prior search ledger for
    # this batch. Rows outside the batch retain their prior audited disposition.
    final_routes: dict[str, str] = {}
    for q in queue_rows:
        if q["confidence_decision"] != "low" or q["review_id"] not in ledger:
            continue
        if q["review_id"] in reports:
            rep = reports[q["review_id"]]
            text = " ".join((rep["support_kind"], rep["evidence_summary"], rep["limitations"]))
            if rep["verdict"] == "no_evidence":
                route = "no_evidence_after_search"
            elif rep["verdict"] == "reject_pair":
                route = "not_ligand_receptor" if NON_LR_RE.search(text) else "no_evidence_after_search"
            else:
                route = rep["verdict"]
        else:
            route = old_route(ledger[q["review_id"]])
        final_routes[q["review_id"]] = route

    no_rows, non_rows, curator_rows = [], [], []
    for rid, route in final_routes.items():
        q, old = queue[rid], ledger[rid]
        rep = reports.get(rid)
        source = rep["source_locators"] if rep else old.get("source_locators", "")
        species = rep["species_support"] if rep else old.get("species_support", "")
        support = rep["support_kind"] if rep else old.get("support_kind", "")
        summary = rep["evidence_summary"] if rep else old.get("evidence_summary", "")
        limitations = rep["limitations"] if rep else old.get("limitations", "")
        if route == "no_evidence_after_search":
            no_rows.append({
                "review_id": rid, "pair_key": q["pair_key"], "pair_label_canonical": q["pair_label_canonical"],
                "review_priority": q["review_priority"], "review_priority_rationale": q["review_priority_rationale"],
                "original_confidence": q["confidence_decision"], "search_status": old.get("search_status", ""),
                "search_attempt_count": old.get("attempt_count", ""), "last_search_iteration": old.get("last_iteration", ""),
                "last_worker_verdict": rep["verdict"] if rep else old.get("worker_verdict", ""),
                "source_locators": source or "NONE", "species_support": species or "unknown", "support_kind": support,
                "evidence_summary": summary, "limitations": limitations,
                "no_evidence_category": "no_evidence_after_search",
                "decision_basis": "Exact-pair literature searches were exhausted in the recorded worker passes without qualifying direct primary evidence; related family, expression, database, noncognate, or negative findings are retained as limitations.",
                "next_review_trigger": "Revisit only if a new primary binding, receptor-activation, receptor-dependent-function, or species-resolved receptor-complex source is identified.",
            })
        elif route == "not_ligand_receptor":
            non_rows.append({
                "review_id": rid, "pair_key": q["pair_key"], "pair_label_canonical": q["pair_label_canonical"],
                "review_priority": q["review_priority"], "review_priority_rationale": q["review_priority_rationale"],
                "original_confidence": q["confidence_decision"], "search_status": old.get("search_status", ""),
                "last_worker_verdict": rep["verdict"] if rep else old.get("worker_verdict", ""),
                "source_locators": source or "NONE", "support_kind": support, "evidence_summary": summary,
                "limitations": limitations, "disposition": "not_ligand_receptor",
                "decision_basis": "The bounded source review classified the candidate as a non-ligand-receptor relationship or wrong-pair annotation; it is excluded from the no-evidence registry.",
            })
        elif rep:
            curator_rows.append({
                "review_id": rid, "pair_key": q["pair_key"], "pair_label_canonical": q["pair_label_canonical"],
                "agent_verdict": rep["verdict"],
                "curator_route": {"promote_candidate": "source_validation_required_before_medium", "needs_manual_review": "manual_exact_pair_review_required", "hold_low": "retain_low_contextual_or_chain_ambiguous"}.get(rep["verdict"], "review_required"),
                "source_locators": source, "species_support": species, "support_kind": support,
                "evidence_summary": summary, "limitations": limitations, "search_notes": rep["search_notes"],
            })

    no_rows.sort(key=lambda r: r["review_id"])
    non_rows.sort(key=lambda r: r["review_id"])
    curator_rows.sort(key=lambda r: r["review_id"])
    write(NO_EVIDENCE, NO_FIELDS, no_rows)
    write(NON_LR, NON_FIELDS, non_rows)
    write(CURATOR, CURATOR_FIELDS, curator_rows)

    counts = {}
    for route in final_routes.values():
        counts[route] = counts.get(route, 0) + 1
    summary = {
        "generated_utc": datetime.now(UTC).isoformat(timespec="seconds"),
        "batch_id": "agent_batch_007",
        "batch_rows": 200,
        "batch_verdict_counts": {v: sum(1 for r in reports.values() if r["verdict"] == v) for v in sorted({r["verdict"] for r in reports.values()})},
        "cumulative_low_route_counts": counts,
        "canonical_queue_mutated": False,
        "signaling_edges_created": False,
    }
    (BATCH / "reconciliation_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
