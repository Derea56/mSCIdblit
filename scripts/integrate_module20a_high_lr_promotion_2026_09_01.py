#!/usr/bin/env python3
"""Promote the current Module 20A high-confidence LR rows into Module 20B.

This is a narrow register update.  It does not create canonical SQL rows and
does not infer receptor-proximal relay, transcription-factor, cellular-output,
or SCI-context evidence from ligand-receptor evidence alone.  Existing
per-source evidence rows attached to the same pair are preserved with their
own confidence tiers; only the frozen LR evidence row is updated.
"""

from __future__ import annotations

import csv
import io
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ROUTER = ROOT / "work" / "module20_db_seed" / "evidence_escalation_router"
QUEUE = ROUTER / "module20a_external_review_queue.tsv"
EDGE_REGISTER = ROOT / "work" / "module_b_consolidation" / "module20b" / "module20b_edge_register.tsv"
EVIDENCE_REGISTER = ROOT / "work" / "module_b_consolidation" / "module20b" / "module20b_evidence_register.tsv"
OUT = ROOT / "work" / "module_b_consolidation" / "module20b" / "module20b_high_lr_promotion_2026_09_01.tsv"
SUMMARY = ROOT / "work" / "module_b_consolidation" / "module20b" / "module20b_high_lr_promotion_2026_09_01_summary.json"

PROMOTION_NOTE = (
    "High-confidence Module 20A LR promotion 2026-09-01; direct ligand-receptor "
    "evidence only; no relay, TF/program, cellular-output, or SCI-context inference."
)


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    old_endings: list[str] = []
    old_contents: list[str] = []
    if path.exists():
        for line in path.read_bytes().splitlines(keepends=True):
            old_endings.append("\r\n" if line.endswith(b"\r\n") else "\n")
            old_contents.append(line.rstrip(b"\r\n").decode("utf-8"))
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    generated_lines = buffer.getvalue().splitlines()
    default_ending = old_endings[-1] if old_endings else "\n"
    with path.open("w", encoding="utf-8", newline="") as handle:
        for index, line in enumerate(generated_lines):
            unchanged = index < len(old_contents) and generated_lines[index] == old_contents[index]
            ending = old_endings[index] if unchanged and index < len(old_endings) else "\n"
            handle.write(line + ending)


def append_note(existing: str) -> str:
    return existing if PROMOTION_NOTE in existing else f"{existing} {PROMOTION_NOTE}".strip()


def main() -> None:
    _, queue_rows = read_tsv(QUEUE)
    high = {row["review_id"]: row for row in queue_rows if row["confidence_decision"] == "high"}
    if len(high) != 109:
        raise SystemExit(f"Expected exactly 109 current high queue rows, found {len(high)}")

    edge_fields, edges = read_tsv(EDGE_REGISTER)
    evidence_fields, evidence = read_tsv(EVIDENCE_REGISTER)
    edges_by_source = {row["source_a_edge_id"]: row for row in edges}
    if len(edges_by_source) != len(edges):
        raise SystemExit("Module 20B edge register has duplicate source_a_edge_id values")
    missing_edges = sorted(set(high) - set(edges_by_source))
    if missing_edges:
        raise SystemExit(f"High queue rows missing from Module 20B edge register: {missing_edges}")

    frozen_evidence = {}
    for row in evidence:
        if row["source_a_evidence_id"] in high and row["source_kind"] == "frozen_module20a_lr_release":
            if row["source_a_evidence_id"] in frozen_evidence:
                raise SystemExit(f"Duplicate frozen LR evidence for {row['source_a_evidence_id']}")
            frozen_evidence[row["source_a_evidence_id"]] = row
    missing_evidence = sorted(set(high) - set(frozen_evidence))
    if missing_evidence:
        raise SystemExit(f"High queue rows missing frozen LR evidence rows: {missing_evidence}")

    audit_fields = [
        "review_id", "pair_key", "pair_label_canonical", "b_edge_id", "b_evidence_id",
        "previous_edge_confidence", "previous_edge_exportable", "previous_evidence_confidence",
        "new_edge_confidence", "new_evidence_confidence", "evidence_register_ids", "decision_basis",
    ]
    audit_rows = []
    changed_edges = 0
    changed_evidence = 0
    for review_id, queue_row in sorted(high.items()):
        edge = edges_by_source[review_id]
        frozen = frozen_evidence[review_id]
        old_edge = (edge["confidence_tier"], edge["exportable"], edge["evidence_layer"])
        # A high queue row can already be present in the B register because a
        # prior promotion pass materialized it.  Preserve those annotations
        # and only repair rows that are still boundary/low in this layer.
        if old_edge[0] != "high" or old_edge[1] != "true":
            edge.update({
                "edge_status": "frozen_lr_supported",
                "evidence_layer": "ligand_receptor_or_direct_molecular",
                "confidence_tier": "high",
                "export_priority": "high",
                "exportable": "true",
                "consolidation_note": append_note(edge["consolidation_note"]),
            })
        new_edge = (edge["confidence_tier"], edge["exportable"], edge["evidence_layer"])
        changed_edges += old_edge != new_edge

        old_evidence = (frozen["confidence_tier"], frozen["exportable"], frozen["evidence_layer"])
        if old_evidence[0] != "high" or old_evidence[1] != "true":
            frozen.update({
                "support_kind": "database_curated",
                "source_scope": "direct_edge",
                "confidence_tier": "high",
                "evidence_layer": "ligand_receptor_or_direct_molecular",
                "exportable": "true",
                "consolidation_note": append_note(frozen["consolidation_note"]),
            })
        new_evidence = (frozen["confidence_tier"], frozen["exportable"], frozen["evidence_layer"])
        changed_evidence += old_evidence != new_evidence
        audit_rows.append({
            "review_id": review_id,
            "pair_key": queue_row["pair_key"],
            "pair_label_canonical": queue_row["pair_label_canonical"],
            "b_edge_id": edge["b_edge_id"],
            "b_evidence_id": frozen["b_evidence_id"],
            "previous_edge_confidence": old_edge[0],
            "previous_edge_exportable": old_edge[1],
            "previous_evidence_confidence": old_evidence[0],
            "new_edge_confidence": new_edge[0],
            "new_evidence_confidence": new_evidence[0],
            "evidence_register_ids": queue_row["evidence_register_ids"],
            "decision_basis": PROMOTION_NOTE,
        })

    write_tsv(EDGE_REGISTER, edge_fields, edges)
    write_tsv(EVIDENCE_REGISTER, evidence_fields, evidence)
    write_tsv(OUT, audit_fields, audit_rows)
    summary = {
            "promotion_id": "module20a-high-lr-2026-09-01",
            "queue": str(QUEUE.relative_to(ROOT)),
            "edge_register": str(EDGE_REGISTER.relative_to(ROOT)),
            "evidence_register": str(EVIDENCE_REGISTER.relative_to(ROOT)),
            "high_queue_rows": len(high),
            "changed_edges": changed_edges,
            "changed_frozen_evidence_rows": changed_evidence,
            "all_high_rows_exportable": all(
                edges_by_source[key]["exportable"] == "true" for key in high
            ),
            "evidence_boundary": PROMOTION_NOTE,
            "canonical_sql_materialization": False,
        }
    if not SUMMARY.exists() or changed_edges or changed_evidence:
        SUMMARY.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"high_queue_rows": len(high), "changed_edges": changed_edges, "changed_frozen_evidence_rows": changed_evidence}, indent=2))


if __name__ == "__main__":
    main()
