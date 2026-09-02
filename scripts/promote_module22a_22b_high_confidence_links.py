#!/usr/bin/env python3
"""Materialize the reviewed Module 22A-to-22B promotion pack.

The source audit already verifies the exact handoff, high-confidence 22B edge,
and exportable evidence gate.  This script turns those verified rows into an
explicit promotion ledger.  It is additive and audit-layer only: it does not
edit the Module 21A handoff, the Module 22B registers, or PostgreSQL.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "work/module22a_22b_promotion_audit/module22a_22b_high_confidence_links.tsv"
DEFAULT_OUTPUT_DIR = ROOT / "work/module22a_22b_promotion_audit"
DEFAULT_DOC = ROOT / "docs/MODULE22A_22B_PROMOTION_2026-09-02.md"
PROMOTION_ID = "module22a-22b-high-confidence-bounded-2026-09-02"

REQUIRED_INPUT_FIELDS = {
    "link_id",
    "handoff_id",
    "pair_key",
    "pair_label_canonical",
    "terminal_tf_entities",
    "edge_id",
    "source_entity",
    "target_entity",
    "evidence_id",
    "evidence_source_locator",
    "evidence_confidence_tier",
    "phase2_extraction_id",
    "phase2_confidence",
    "link_status",
    "basis",
    "handoff_limitations",
    "edge_limitations",
    "evidence_limitations",
}

OUTPUT_FIELDS = [
    "promotion_id",
    "link_id",
    "handoff_id",
    "pair_key",
    "pair_label_canonical",
    "terminal_tf_entities",
    "source_entity",
    "target_entity",
    "edge_id",
    "evidence_id",
    "evidence_source_locator",
    "evidence_confidence_tier",
    "phase2_extraction_id",
    "phase2_confidence",
    "promotion_status",
    "promotion_confidence_tier",
    "decision_basis",
    "handoff_limitations",
    "edge_limitations",
    "evidence_limitations",
    "module21a_handoff_unchanged",
    "module22b_register_unchanged",
    "sql_materialization",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--doc", type=Path, default=DEFAULT_DOC)
    return parser.parse_args()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        missing = REQUIRED_INPUT_FIELDS - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"{path}: missing fields: {', '.join(sorted(missing))}")
        return list(reader)


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def validate(rows: list[dict[str, str]], path: Path) -> None:
    if not rows:
        raise ValueError(f"{path}: no audited links found")
    link_ids = [row["link_id"] for row in rows]
    if len(link_ids) != len(set(link_ids)):
        raise ValueError(f"{path}: duplicate link_id")
    for row in rows:
        if not row["link_status"].startswith("promote_existing_high_tf_target"):
            raise ValueError(f"{row['link_id']}: audit status is not promotion-ready")
        if row["evidence_confidence_tier"].lower() != "high" and not row["phase2_confidence"].lower().startswith("high"):
            raise ValueError(f"{row['link_id']}: no high-confidence evidence route")
        if not row["edge_id"] or not row["evidence_id"] or not row["handoff_id"]:
            raise ValueError(f"{row['link_id']}: incomplete cross-module key")


def promotion_rows(audited: list[dict[str, str]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for row in audited:
        rows.append(
            {
                "promotion_id": PROMOTION_ID,
                "link_id": row["link_id"],
                "handoff_id": row["handoff_id"],
                "pair_key": row["pair_key"],
                "pair_label_canonical": row["pair_label_canonical"],
                "terminal_tf_entities": row["terminal_tf_entities"],
                "source_entity": row["source_entity"],
                "target_entity": row["target_entity"],
                "edge_id": row["edge_id"],
                "evidence_id": row["evidence_id"],
                "evidence_source_locator": row["evidence_source_locator"],
                "evidence_confidence_tier": row["evidence_confidence_tier"],
                "phase2_extraction_id": row["phase2_extraction_id"],
                "phase2_confidence": row["phase2_confidence"],
                "promotion_status": row["link_status"],
                "promotion_confidence_tier": "high",
                "decision_basis": row["basis"],
                "handoff_limitations": row["handoff_limitations"],
                "edge_limitations": row["edge_limitations"],
                "evidence_limitations": row["evidence_limitations"],
                "module21a_handoff_unchanged": "true",
                "module22b_register_unchanged": "true",
                "sql_materialization": "false",
            }
        )
    return rows


def write_doc(path: Path, rows: list[dict[str, str]]) -> None:
    unique_handoffs = {row["handoff_id"] for row in rows}
    pending_handoffs = {
        row["handoff_id"]
        for row in rows
        if row["terminal_tf_entities"] and row["terminal_tf_entities"].upper() != "NONE_FOUND"
    }
    new_tf = sum("new_terminal_tf" in row["promotion_status"] for row in rows)
    edge_ids = Counter(row["edge_id"] for row in rows)
    lines = [
        "# Module 22A-to-22B high-confidence promotion — 2026-09-02",
        "",
        "This promotion pack records the bounded reuse of existing, exportable",
        "high-confidence Module 22B TF-target evidence for exact Module 22A",
        "ligand/receptor handoffs. It is an audit-layer cross-module linkage",
        "artifact, not a new canonical SignalingEdge or evidence-unit write.",
        "",
        "## Result",
        "",
        f"- Promotion records: {len(rows):,}",
        f"- Distinct 22A handoffs represented: {len(unique_handoffs):,}",
        f"- Handoffs with an existing terminal-TF assignment: {len(pending_handoffs):,}",
        f"- Evidence-backed terminal-TF assignments added in the linkage layer: {new_tf:,}",
        f"- Distinct reused 22B edges: {len(edge_ids):,}",
        "- Module 21A handoff register changed: false",
        "- Module 22B edge/evidence registers changed: false",
        "- PostgreSQL/canonical materialization performed: false",
        "",
        "## Gate and boundaries",
        "",
        "Each row is carried forward only from the high-confidence linkage audit",
        "after checking the handoff identity, terminal TF, exportable 22B edge,",
        "exportable evidence, and either high register evidence or a reviewed",
        "primary extraction with High confidence. The `high` tier applies to the",
        "tested TF-target evidence in its recorded comparator model; it does not",
        "assert the same receptor-complex activity in an SCI receiver cell.",
        "",
        "The source handoff, edge, and evidence limitations are copied into the",
        "promotion ledger. This preserves receptor-complex ambiguity, ligand or",
        "cofactor specificity, model/species limits, program-level edges, and",
        "the distinction between a bounded upstream handoff and the reused 22B",
        "TF-target record.",
        "",
        "## Reproduction",
        "",
        "- Audit input: `work/module22a_22b_promotion_audit/module22a_22b_high_confidence_links.tsv`",
        "- Promotion ledger: `work/module22a_22b_promotion_audit/module22a_22b_high_confidence_promotions.tsv`",
        "- Generator: `scripts/promote_module22a_22b_high_confidence_links.py`",
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    args = parse_args()
    audited = read_tsv(args.input)
    validate(audited, args.input)
    promoted = promotion_rows(audited)
    output = args.output_dir / "module22a_22b_high_confidence_promotions.tsv"
    write_tsv(output, promoted)
    write_doc(args.doc, promoted)
    summary = {
        "promotion_id": PROMOTION_ID,
        "records_promoted": len(promoted),
        "distinct_handoffs": len({row["handoff_id"] for row in promoted}),
        "distinct_22b_edges": len({row["edge_id"] for row in promoted}),
        "new_terminal_tf_assignments": sum("new_terminal_tf" in row["promotion_status"] for row in promoted),
        "module21a_handoff_changed": False,
        "module22b_register_changed": False,
        "sql_materialization": False,
        "source_audit": str(args.input),
        "promotion_ledger": str(output),
    }
    summary_path = args.output_dir / "module22a_22b_high_confidence_promotions_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
