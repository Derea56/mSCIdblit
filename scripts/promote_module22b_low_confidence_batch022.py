#!/usr/bin/env python3
"""Recover four bounded Module 22B signaling-program associations.

The promoted claims deliberately remove unsupported receptor composites while
retaining the exact downstream program demonstrated by the cited primary
studies.  These are medium-confidence program rows, not direct TF-target
edges and not evidence of SCI-specific activity.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch022.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch022_summary.json"
BATCH_ID = "module22b-low-confidence-upgrade-batch022-2026-09-03"

UPDATES = {
    "M22B-E000499": {
        "evidence_id": "M22B-EVID-005327",
        "relation_type": (
            "BMP6/7 uses ACVR1A, ACVR2A, and BMPR2-associated signaling to induce "
            "ID1/DLX5/IBSP osteoblastic output; the submitted BMPR1B-BMPR2 "
            "composite is not assigned"
        ),
        "target_entity": (
            "BMP6/7 -> ACVR1A/ACVR2A/BMPR2 -> ID1/DLX5/IBSP osteoblastic "
            "differentiation program"
        ),
        "scope": (
            "Primary human mesenchymal-stem-cell receptor-utilization studies "
            "support BMP6/7 osteoblastic differentiation through ACVR1A with "
            "ACVR2A and BMPR2 contributions, while BMPR1B and ACVR2B were low or "
            "not significant. The recovered row is a bounded receptor/program "
            "association; it does not assert the original BMPR1B-BMPR2 composite, "
            "a direct TF-target edge, or SCI transfer."
        ),
        "basis": (
            "Lavery et al. used receptor knockdown in primary human MSCs and "
            "reported BMP6/7-dependent osteoblastic differentiation, ID1/DLX5/IBSP "
            "output, and receptor contributions. The exact BMPR1B-BMPR2 composite "
            "was removed because the study reported low or insignificant BMPR1B "
            "and ACVR2B involvement."
        ),
        "locator": "PMID:18436533; PMCID:PMC3258927; DOI:10.1074/jbc.M800850200",
    },
    "M22B-E000728": {
        "evidence_id": "M22B-EVID-005314",
        "relation_type": (
            "TNF-alpha/Msx2-associated WNT7A/WNT3A paracrine signaling is linked to "
            "beta-catenin/TCF osteogenic output; LDLR is a model background, not a "
            "WNT7A receptor assignment"
        ),
        "target_entity": "TNF-alpha/Msx2 -> WNT7A/WNT3A -> beta-catenin/TCF osteogenic program",
        "scope": (
            "Primary vascular-calcification studies support TNF-alpha/Msx2-linked "
            "induction of Wnt7a/Wnt3a and beta-catenin reporter or osteogenic output "
            "in Ldlr-deficient mouse and vascular-cell contexts. LDLR is retained as "
            "genetic/model context only; no WNT7A-LDLR binding, receptor-dependent "
            "activation, direct TF-target edge, or SCI transfer is inferred."
        ),
        "basis": (
            "Primary in vivo and vascular-cell studies linked TNF-alpha or Msx2 to "
            "Wnt7a/Wnt3a expression, beta-catenin reporter activity, and osteogenic "
            "output. The row is recovered as a bounded paracrine osteogenic program "
            "after removing the unsupported LDLR receptor interpretation."
        ),
        "locator": "PMID:17932314; PMID:15841209; PMCID:PMC1077175",
    },
    "M22B-E000789": {
        "evidence_id": "M22B-EVID-005804",
        "relation_type": (
            "WNT7A-FZD9 activates ERK5-dependent PPARgamma and antitumor output; "
            "the queued LRP5 composite is not assigned"
        ),
        "target_entity": "WNT7A-FZD9 -> ERK5 -> PPARgamma antitumor program",
        "scope": (
            "The primary NSCLC study supports WNT7A/FZD9-associated ERK5 activation "
            "required for PPARgamma activity and antitumor phenotypes. It does not "
            "test LRP5, establish an LRP5-containing complex, define a terminal "
            "TF-target edge, or establish SCI transfer."
        ),
        "basis": (
            "Winn et al. reported that WNT7A and FZD9 expression activated ERK5, "
            "which was required for PPARgamma activation; PPARgamma inhibition "
            "reversed associated antitumor and E-cadherin phenotypes. The unsupported "
            "LRP5 composite was removed while retaining the demonstrated FZD9 program."
        ),
        "locator": "PMID:16835228; DOI:10.1074/jbc.M604145200",
    },
    "M22B-E000790": {
        "evidence_id": "M22B-EVID-005805",
        "relation_type": (
            "WNT7A-FZD9 activates ERK5-dependent PPARgamma and antitumor output; "
            "the queued LRP6 composite is not assigned"
        ),
        "target_entity": "WNT7A-FZD9 -> ERK5 -> PPARgamma antitumor program",
        "scope": (
            "The primary NSCLC study supports WNT7A/FZD9-associated ERK5 activation "
            "required for PPARgamma activity and antitumor phenotypes. It does not "
            "test LRP6, establish an LRP6-containing complex, define a terminal "
            "TF-target edge, or establish SCI transfer."
        ),
        "basis": (
            "Winn et al. reported that WNT7A and FZD9 expression activated ERK5, "
            "which was required for PPARgamma activation; PPARgamma inhibition "
            "reversed associated antitumor and E-cadherin phenotypes. The unsupported "
            "LRP6 composite was removed while retaining the demonstrated FZD9 program."
        ),
        "locator": "PMID:16835228; DOI:10.1074/jbc.M604145200",
    },
}

EDGE_FIELDS = [
    "b_edge_id", "source_entity", "relation_type", "target_entity", "pathway_name",
    "evidence_layer", "source_a_edge_id", "edge_status", "context_scope",
    "cell_type_context", "compartment_context", "species_context", "injury_context",
    "confidence_tier", "export_priority", "exportable", "consolidation_note",
]
EVIDENCE_FIELDS = [
    "b_evidence_id", "source_a_evidence_id", "b_edge_ids", "source_kind",
    "source_locator", "support_kind", "species_support", "source_scope",
    "confidence_tier", "citation_note", "evidence_summary", "limitations",
    "evidence_layer", "exportable", "consolidation_note",
]
AUDIT_FIELDS = [
    "batch_id", "b_edge_id", "b_evidence_id", "old_edge_confidence",
    "new_edge_confidence", "old_evidence_confidence", "new_evidence_confidence",
    "old_target", "new_target", "old_edge_status", "new_edge_status",
    "decision_basis", "source_locator", "module22b_register_changed",
    "canonical_sql_materialization",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def append_once(value: str, addition: str) -> str:
    return value if addition in value else (f"{value}; {addition}" if value else addition)


def main() -> int:
    edges = read_tsv(EDGE_PATH)
    evidence = read_tsv(EVIDENCE_PATH)
    edge_by_id = {row["b_edge_id"]: row for row in edges}
    evidence_by_id = {row["b_evidence_id"]: row for row in evidence}
    audit: list[dict[str, str]] = []

    for edge_id, update in UPDATES.items():
        edge = edge_by_id.get(edge_id)
        ev = evidence_by_id.get(update["evidence_id"])
        if edge is None or ev is None:
            raise SystemExit(f"missing edge/evidence for {edge_id}")
        if edge["confidence_tier"] != "low":
            raise SystemExit(f"{edge_id}: expected low confidence, found {edge['confidence_tier']!r}")
        if edge_id not in (ev.get("b_edge_ids") or "").split(";"):
            raise SystemExit(f"{edge_id}: evidence link mismatch")

        old_target = edge["target_entity"]
        old_status = edge["edge_status"]
        old_edge_confidence = edge["confidence_tier"]
        old_evidence_confidence = ev["confidence_tier"]
        edge.update({
            "relation_type": update["relation_type"],
            "target_entity": update["target_entity"],
            "pathway_name": "cell_state_program",
            "edge_status": "reviewed_program_association",
            "context_scope": update["scope"],
            "confidence_tier": "medium",
            "exportable": "true",
        })
        edge["consolidation_note"] = append_once(
            edge["consolidation_note"],
            f"Low-confidence recovery {BATCH_ID}: medium after bounded exact-source re-review.",
        )
        ev.update({
            "source_kind": "reviewed_program_association",
            "source_locator": update["locator"],
            "confidence_tier": "high",
            "evidence_summary": update["basis"],
            "limitations": update["scope"],
            "exportable": "true",
        })
        ev["consolidation_note"] = append_once(
            ev["consolidation_note"],
            f"Low-confidence recovery {BATCH_ID}: bounded program re-adjudication; exact unsupported receptor composites remain excluded.",
        )
        audit.append({
            "batch_id": BATCH_ID,
            "b_edge_id": edge_id,
            "b_evidence_id": update["evidence_id"],
            "old_edge_confidence": old_edge_confidence,
            "new_edge_confidence": edge["confidence_tier"],
            "old_evidence_confidence": old_evidence_confidence,
            "new_evidence_confidence": ev["confidence_tier"],
            "old_target": old_target,
            "new_target": edge["target_entity"],
            "old_edge_status": old_status,
            "new_edge_status": edge["edge_status"],
            "decision_basis": update["basis"],
            "source_locator": update["locator"],
            "module22b_register_changed": "true",
            "canonical_sql_materialization": "false",
        })

    write_tsv(EDGE_PATH, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    write_tsv(AUDIT_PATH, audit, AUDIT_FIELDS)
    summary = {
        "batch_id": BATCH_ID,
        "records_upgraded": len(audit),
        "medium_edge_upgrades": len(audit),
        "recovered_program_edges": len(audit),
        "low_edges_after": sum(row["confidence_tier"] == "low" for row in edges),
        "medium_edges_after": sum(row["confidence_tier"] == "medium" for row in edges),
        "medium_high_edges_after": sum(row["confidence_tier"] == "medium-high" for row in edges),
        "high_edges_after": sum(row["confidence_tier"] == "high" for row in edges),
        "exportable_edges_after": sum(row["exportable"] == "true" for row in edges),
        "canonical_sql_materialization": False,
        "audit": str(AUDIT_PATH),
        "external_primary_sources": {
            "M22B-E000499": "PMID:18436533",
            "M22B-E000728": "PMID:17932314; PMID:15841209",
            "M22B-E000789": "PMID:16835228",
            "M22B-E000790": "PMID:16835228",
        },
    }
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
