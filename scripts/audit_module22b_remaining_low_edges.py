#!/usr/bin/env python3
"""Classify every remaining low-confidence Module 22B edge.

This audit is deliberately a register-level review aid.  It does not claim
that a literature search was negative and it does not promote rows.  It
separates the large no-evidence boundary from the small set of rows that
already have bounded program or phenotype evidence and therefore deserve a
targeted re-review.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
DEFAULT_EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
DEFAULT_OUTPUT_DIR = ROOT / "work/module22b_low_confidence_upgrade_audit"

AUDIT_FIELDS = [
    "audit_id",
    "b_edge_id",
    "source_a_edge_id",
    "source_entity",
    "target_entity",
    "pathway_name",
    "edge_status",
    "confidence_tier",
    "exportable",
    "evidence_ids",
    "source_locators",
    "source_kinds",
    "support_kinds",
    "evidence_layers",
    "review_route",
    "promotion_readiness",
    "hold_reason",
    "positive_support_signals",
    "scope_context",
    "limitations",
    "audit_note",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--edge-register", type=Path, default=DEFAULT_EDGE_PATH)
    parser.add_argument("--evidence-register", type=Path, default=DEFAULT_EVIDENCE_PATH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=AUDIT_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def join_unique(values: list[str]) -> str:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        for token in value.split(";"):
            token = token.strip()
            if token and token not in seen:
                seen.add(token)
                result.append(token)
    return ";".join(result)


def classify(edge: dict[str, str], linked: list[dict[str, str]]) -> dict[str, str]:
    status = edge["edge_status"]
    pathway = edge["pathway_name"]
    target = edge["target_entity"]
    if status == "no_evidence_boundary":
        route = "exact_pair_source_review"
        readiness = "not_ready_from_register"
        hold = "no_pair_specific_supported_target_or_program_in_current_register"
    elif status == "unresolved":
        route = "assignment_resolution_review"
        readiness = "hold_unresolved_assignment"
        hold = "edge_assignment_or_target_scope_is_unresolved"
    elif status == "reviewed_program_association":
        route = "bounded_program_re_review"
        readiness = "reviewed_but_low_confidence"
        hold = "program_association_is_bounded_but_current_confidence_remains_low"
    elif status == "reviewed_phenotype_only":
        route = "bounded_phenotype_re_review"
        readiness = "reviewed_but_low_confidence"
        hold = "phenotype_only_support_does_not_define_a_direct_target_gene_edge"
    else:
        route = "manual_status_review"
        readiness = "manual_review_required"
        hold = "unrecognized_edge_status"

    signals: list[str] = []
    for evidence in linked:
        summary = " ".join(
            evidence.get(field, "")
            for field in ("source_kind", "support_kind", "source_scope", "evidence_layer", "evidence_summary")
        ).casefold()
        for token, label in (
            ("direct", "directness_language_present"),
            ("binding", "binding_language_present"),
            ("activation", "activation_language_present"),
            ("target", "target_language_present"),
            ("primary", "primary_source_language_present"),
            ("curated", "curated_database_language_present"),
        ):
            if token in summary and label not in signals:
                signals.append(label)

    limitation_text = join_unique([evidence.get("limitations", "") for evidence in linked])
    scope_text = join_unique(
        [edge.get("context_scope", "")] + [evidence.get("source_scope", "") for evidence in linked]
    )
    audit_note = (
        "Classification is based only on the current Module 22B registers; "
        "a no-evidence boundary means no qualifying pair-specific support is "
        "recorded here, not that the broader literature is negative."
    )
    if pathway in {"cell_state_program", "phenotype"} and target not in {"", "null"}:
        audit_note += " The existing target text is a bounded program/phenotype label, not a canonical target-gene assertion."

    return {
        "review_route": route,
        "promotion_readiness": readiness,
        "hold_reason": hold,
        "positive_support_signals": ";".join(signals),
        "scope_context": scope_text,
        "limitations": limitation_text,
        "audit_note": audit_note,
    }


def main() -> int:
    args = parse_args()
    edges = read_tsv(args.edge_register)
    evidence = read_tsv(args.evidence_register)
    evidence_by_edge: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in evidence:
        for edge_id in row.get("b_edge_ids", "").split(";"):
            if edge_id.strip():
                evidence_by_edge[edge_id.strip()].append(row)

    low_edges = [row for row in edges if row.get("confidence_tier") == "low"]
    audit_rows: list[dict[str, str]] = []
    for index, edge in enumerate(low_edges, start=1):
        linked = evidence_by_edge.get(edge["b_edge_id"], [])
        classification = classify(edge, linked)
        audit_rows.append(
            {
                "audit_id": f"M22B-LOW-AUDIT-{index:04d}",
                "b_edge_id": edge["b_edge_id"],
                "source_a_edge_id": edge.get("source_a_edge_id", ""),
                "source_entity": edge.get("source_entity", ""),
                "target_entity": edge.get("target_entity", ""),
                "pathway_name": edge.get("pathway_name", ""),
                "edge_status": edge.get("edge_status", ""),
                "confidence_tier": edge.get("confidence_tier", ""),
                "exportable": edge.get("exportable", ""),
                "evidence_ids": join_unique([row.get("b_evidence_id", "") for row in linked]),
                "source_locators": join_unique([row.get("source_locator", "") for row in linked]),
                "source_kinds": join_unique([row.get("source_kind", "") for row in linked]),
                "support_kinds": join_unique([row.get("support_kind", "") for row in linked]),
                "evidence_layers": join_unique([row.get("evidence_layer", "") for row in linked]),
                **classification,
            }
        )

    if not audit_rows:
        raise SystemExit("no low-confidence rows found")
    if len({row["b_edge_id"] for row in audit_rows}) != len(audit_rows):
        raise SystemExit("duplicate b_edge_id in low-confidence audit")
    if any(not row["evidence_ids"] for row in audit_rows):
        raise SystemExit("low-confidence edge without linked evidence in current register")

    output_tsv = args.output_dir / "module22b_remaining_low_edges_audit.tsv"
    summary_path = args.output_dir / "module22b_remaining_low_edges_audit_summary.json"
    write_tsv(output_tsv, audit_rows)
    summary = {
        "audit_version": "module22b-remaining-low-edges-2026-09-03",
        "edge_register": str(args.edge_register),
        "evidence_register": str(args.evidence_register),
        "low_confidence_edges_audited": len(audit_rows),
        "linked_evidence_rows": sum(1 for row in audit_rows if row["evidence_ids"]),
        "by_edge_status": dict(sorted(Counter(row["edge_status"] for row in audit_rows).items())),
        "by_pathway_name": dict(sorted(Counter(row["pathway_name"] for row in audit_rows).items())),
        "by_exportable": dict(sorted(Counter(row["exportable"] for row in audit_rows).items())),
        "by_review_route": dict(sorted(Counter(row["review_route"] for row in audit_rows).items())),
        "by_promotion_readiness": dict(sorted(Counter(row["promotion_readiness"] for row in audit_rows).items())),
        "interpretation": (
            "This is a deterministic classification of the current register. "
            "It is not a claim that unlinked or no-evidence-boundary pairs are absent "
            "from external literature, and it does not itself promote any edge."
        ),
    }
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
