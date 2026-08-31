#!/usr/bin/env python3
"""Curator-approved integration for Module 20A agent batch 008.

Only source-backed, non-lead promotion calls are moved to medium confidence.
No-evidence and non-LR calls are recorded in revisit registries; they remain
low in the compatibility queue. No high-confidence rows or SignalingEdges are
created by this script.
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work" / "module20_db_seed"
BATCH = WORK / "evidence_search_agents" / "agent_batch_008"
QUEUE = WORK / "evidence_escalation_router" / "module20a_external_review_queue.tsv"
LEDGER = WORK / "evidence_search_agents" / "iterative" / "low_search_ledger.tsv"
NO_EVIDENCE = WORK / "evidence_escalation_router" / "module20a_no_evidence_registry.tsv"
NON_LR = WORK / "evidence_escalation_router" / "module20a_non_ligand_receptor_registry.tsv"
STARTER = WORK / "evidence_escalation_starter"
EVIDENCE = STARTER / "module20a_external_agent_review_batch08_evidence_register.tsv"
DECISIONS = STARTER / "module20a_external_agent_review_batch08_decision_register.tsv"
CURATOR = BATCH / "agent_batch008_curator_review_register.tsv"

EVIDENCE_FIELDS = ["evidence_item_id", "review_id", "pair_key", "pair_label", "source_kind", "source_locator", "support_kind", "species_support", "source_scope", "confidence_tier", "citation_note", "evidence_summary", "limitations"]
DECISION_FIELDS = ["review_id", "pair_key", "pair_label_canonical", "review_status", "confidence_decision", "mouse_confidence", "mouse_confidence_rank", "human_confidence", "human_confidence_rank", "human_evidence_present", "receptor_state", "receptor_role", "directness", "species_posture", "decision_basis", "evidence_register_ids", "next_action"]
CURATOR_FIELDS = ["review_id", "pair_key", "agent_verdict", "curator_route", "source_locators", "species_support", "support_kind", "evidence_summary", "limitations", "search_notes"]
NO_FIELDS = ["review_id", "pair_key", "pair_label_canonical", "review_priority", "review_priority_rationale", "original_confidence", "search_status", "search_attempt_count", "last_search_iteration", "last_worker_verdict", "source_locators", "species_support", "support_kind", "evidence_summary", "limitations", "no_evidence_category", "decision_basis", "next_review_trigger"]
NON_FIELDS = ["review_id", "pair_key", "pair_label_canonical", "review_priority", "review_priority_rationale", "original_confidence", "search_status", "last_worker_verdict", "source_locators", "support_kind", "evidence_summary", "limitations", "disposition", "decision_basis"]


def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def approved_medium(row: dict[str, str]) -> bool:
    """Approve only an anchored source-backed candidate at medium confidence."""
    if row["verdict"] != "promote_candidate":
        return False
    locators = row["source_locators"].strip()
    if not locators or locators.upper() == "NONE" or "no exact primary" in locators.casefold():
        return False
    if re.search(r"lead|negative", row["support_kind"], re.I):
        return False
    text = f"{row['evidence_summary']} {row['limitations']}"
    # These phrases indicate a family/complex lead, unresolved chain, or
    # computational assignment rather than enough exact-pair support for this
    # integration pass.
    if re.search(r"not isolated|individual collagen chains|not assigned|subunit inference|exact pair.{0,20}unresolved|no direct|not central|computational/provisional", text, re.I):
        return False
    return True


def species_tiers(species: str) -> tuple[str, str, str, str, str]:
    s = species.casefold()
    mouse = "medium" if "mouse" in s else "uncertain"
    human = "medium" if "human" in s else "uncertain"
    if mouse == "medium" and human == "medium":
        posture = "mouse_and_human_support_reported"
    elif mouse == "medium":
        posture = "mouse_support_reported_human_unknown"
    elif human == "medium":
        posture = "human_support_reported_mouse_unknown"
    else:
        posture = "species_not_resolved_in_agent_packet"
    return mouse, "2" if mouse == "medium" else "0", human, "2" if human == "medium" else "0", posture


def merge_registry(path: Path, fields: list[str], new_rows: list[dict[str, str]]) -> None:
    old_rows = read(path) if path.exists() else []
    by_id = {row["review_id"]: row for row in old_rows}
    for row in new_rows:
        by_id[row["review_id"]] = row
    write(path, fields, sorted(by_id.values(), key=lambda row: row["review_id"]))


def main() -> None:
    reports = read(BATCH / "validated_reports.tsv")
    if len(reports) != 1000 or len({r["review_id"] for r in reports}) != 1000:
        raise SystemExit("batch 008 must be validated as 1000 unique report rows first")
    queue_rows = read(QUEUE)
    queue = {row["review_id"]: row for row in queue_rows}
    ledger = {row["review_id"]: row for row in read(LEDGER)}
    if any(row["review_id"] not in queue for row in reports):
        raise SystemExit("batch 008 contains a review_id outside the canonical queue")

    approved = [row for row in reports if approved_medium(row)]
    no_reports = [row for row in reports if row["verdict"] == "no_evidence"]
    non_reports = [row for row in reports if row["verdict"] == "reject_pair"]
    if set(r["review_id"] for r in approved) & set(r["review_id"] for r in no_reports + non_reports):
        raise SystemExit("route overlap detected")

    evidence_rows, decision_rows = [], []
    for index, row in enumerate(approved, start=1):
        eid = f"M20A-EXTLR08-EVID-{index:04d}"
        mouse, mouse_rank, human, human_rank, posture = species_tiers(row["species_support"])
        pair = row["pair_key"]
        if any(x in pair for x in ("itga", "itgb", "dag1", "sdc", "gpc", "plxdc", "unc5")):
            role = "membrane_or_matrix_adhesion_receptor_context"
        else:
            role = "ligand_receptor_or_receptor_complex_context"
        limitations = (row["limitations"] + " Agent promotion was curator-approved only to medium; retain all species, assay, processing, complex, and non-SCI caveats.").strip()
        basis = "Curator-approved medium from an anchored primary-literature locator and non-lead exact-pair report; no high-confidence or SCI-specific inference made."
        evidence_rows.append({
            "evidence_item_id": eid, "review_id": row["review_id"], "pair_key": pair, "pair_label": pair,
            "source_kind": "primary_literature", "source_locator": row["source_locators"], "support_kind": row["support_kind"],
            "species_support": row["species_support"], "source_scope": "agent_batch008_exact_pair_source_review",
            "confidence_tier": "medium", "citation_note": row["evidence_summary"], "evidence_summary": row["evidence_summary"],
            "limitations": limitations,
        })
        decision_rows.append({
            "review_id": row["review_id"], "pair_key": pair, "pair_label_canonical": pair, "review_status": "reviewed",
            "confidence_decision": "medium", "mouse_confidence": mouse, "mouse_confidence_rank": mouse_rank,
            "human_confidence": human, "human_confidence_rank": human_rank, "human_evidence_present": "yes" if human == "medium" else "no",
            "receptor_state": "membrane_bound_or_receptor_complex_context", "receptor_role": role,
            "directness": "source_backed_pair_at_medium_with_assay_scope_caveat", "species_posture": posture,
            "decision_basis": basis, "evidence_register_ids": eid,
            "next_action": "retain_medium; no_SignalingEdge_until_SCI_relevance_and_relay_review",
        })

    write(EVIDENCE, EVIDENCE_FIELDS, evidence_rows)
    write(DECISIONS, DECISION_FIELDS, decision_rows)

    # Canonical queue mutation is limited to the curator-approved medium set.
    by_id = {row["review_id"]: row for row in decision_rows}
    changed = 0
    for row in queue_rows:
        decision = by_id.get(row["review_id"])
        if decision is None:
            continue
        row["confidence_decision"] = "medium"
        row["evidence_register_ids"] = ";".join(x for x in (row.get("evidence_register_ids", ""), decision["evidence_register_ids"]) if x)
        row["curator_notes"] = (row.get("curator_notes", "") + " " + decision["decision_basis"]).strip()
        changed += 1
    if changed != len(approved):
        raise SystemExit(f"expected {len(approved)} queue updates, got {changed}")
    write(QUEUE, list(queue_rows[0]), queue_rows)

    no_rows, non_rows, curator_rows = [], [], []
    for row in reports:
        rid = row["review_id"]
        q = queue[rid]
        if row["verdict"] == "no_evidence":
            old = ledger.get(rid, {})
            no_rows.append({
                "review_id": rid, "pair_key": q["pair_key"], "pair_label_canonical": q["pair_label_canonical"],
                "review_priority": q["review_priority"], "review_priority_rationale": q["review_priority_rationale"],
                "original_confidence": "low", "search_status": old.get("search_status", "completed_agent_review"),
                "search_attempt_count": old.get("attempt_count", ""), "last_search_iteration": "agent_batch_008",
                "last_worker_verdict": row["verdict"], "source_locators": row["source_locators"] or "NONE",
                "species_support": row["species_support"] or "unknown", "support_kind": row["support_kind"],
                "evidence_summary": row["evidence_summary"], "limitations": row["limitations"],
                "no_evidence_category": "no_evidence_after_search",
                "decision_basis": "Exact-pair symbols, aliases, complex/chain names, PubMed, and Europe PMC were searched without qualifying primary evidence.",
                "next_review_trigger": "Revisit only after a new primary binding, receptor-activation, receptor-dependent-function, or species-resolved complex source.",
            })
        elif row["verdict"] == "reject_pair":
            non_rows.append({
                "review_id": rid, "pair_key": q["pair_key"], "pair_label_canonical": q["pair_label_canonical"],
                "review_priority": q["review_priority"], "review_priority_rationale": q["review_priority_rationale"],
                "original_confidence": "low", "search_status": "completed_agent_review", "last_worker_verdict": row["verdict"],
                "source_locators": row["source_locators"] or "NONE", "support_kind": row["support_kind"],
                "evidence_summary": row["evidence_summary"], "limitations": row["limitations"],
                "disposition": "not_ligand_receptor",
                "decision_basis": "Agent review classified the candidate as a non-ligand-receptor relationship or wrong ligand/receptor assignment; it is excluded from the no-evidence registry.",
            })
        elif rid not in by_id:
            route = "manual_exact_pair_review_required" if row["verdict"] == "needs_manual_review" else "retain_low_contextual_or_unresolved"
            curator_rows.append({
                "review_id": rid, "pair_key": q["pair_key"], "agent_verdict": row["verdict"], "curator_route": route,
                "source_locators": row["source_locators"], "species_support": row["species_support"], "support_kind": row["support_kind"],
                "evidence_summary": row["evidence_summary"], "limitations": row["limitations"], "search_notes": row["search_notes"],
            })
    # Keep a complete decision trail, including rows routed to the registries.
    for row in no_rows:
        curator_rows.append({"review_id": row["review_id"], "pair_key": row["pair_key"], "agent_verdict": "no_evidence", "curator_route": "no_evidence_after_search", "source_locators": row["source_locators"], "species_support": row["species_support"], "support_kind": row["support_kind"], "evidence_summary": row["evidence_summary"], "limitations": row["limitations"], "search_notes": "recorded in no-evidence registry"})
    for row in non_rows:
        curator_rows.append({"review_id": row["review_id"], "pair_key": row["pair_key"], "agent_verdict": "reject_pair", "curator_route": "not_ligand_receptor", "source_locators": row["source_locators"], "species_support": "", "support_kind": row["support_kind"], "evidence_summary": row["evidence_summary"], "limitations": row["limitations"], "search_notes": "recorded in non-LR registry"})
    write(CURATOR, CURATOR_FIELDS, sorted(curator_rows, key=lambda row: row["review_id"]))
    merge_registry(NO_EVIDENCE, NO_FIELDS, no_rows)
    merge_registry(NON_LR, NON_FIELDS, non_rows)

    summary = {
        "generated_utc": datetime.now(UTC).isoformat(timespec="seconds"), "batch_id": "agent_batch_008", "batch_rows": len(reports),
        "agent_verdict_counts": dict(sorted(Counter(row["verdict"] for row in reports).items())),
        "curator_approved_medium": len(approved), "curator_excluded_from_promotion": len([row for row in reports if row["verdict"] == "promote_candidate"]) - len(approved),
        "no_evidence_registry_added": len(no_rows), "non_ligand_receptor_registry_added": len(non_rows),
        "canonical_queue_medium_updates": changed, "canonical_queue_high_updates": 0, "signaling_edges_created": 0,
        "approval_rule": "promote_candidate + nonempty primary locator + non-lead support + no unresolved chain/complex/assignment caveat",
    }
    (BATCH / "integration_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
