#!/usr/bin/env python3
"""Review every Module 22B no-evidence-boundary hold.

The no-evidence-boundary rows are upstream handoffs, not implicit TF-target
edges.  This audit keeps those rows unchanged and records whether the handoff
names a terminal TF for which a separate, reusable target-gene lane exists.
It never converts a generic regulon membership into evidence that the
upstream ligand/receptor route activated that TF.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
QUEUE_PATH = ROOT / "data/processed/public_tf_union_v1/module_curation/module_22_priority_tf_review_queue.tsv"
STAGE_PATH = ROOT / "work/module22b_consolidation/materialization_round_register_2026_09_03/module22b_promoted_pairs.tsv"
DEFAULT_OUTPUT = ROOT / "work/module22b_low_confidence_upgrade_audit"

OUTPUT_FIELDS = [
    "audit_id", "b_edge_id", "source_a_edge_id", "source_entity", "relation_type",
    "target_entity", "pathway_name", "edge_status", "confidence_tier", "exportable",
    "evidence_ids", "source_locators", "hold_reason", "terminal_tf_names",
    "terminal_tf_resolution", "relation_tf_mentions", "relation_tf_resolution",
    "current_target_gene_rows", "current_target_pairs",
    "signed_queue_rows", "signed_queue_pairs", "recommended_action", "audit_note",
]

# This is intentionally a conservative vocabulary.  Family labels and
# unresolved composites remain visible in terminal_tf_resolution and are not
# silently treated as one canonical TF symbol.
KNOWN_TFS = {
    "AR", "ATF1", "ATF2", "ATF4", "BCL6", "CREB1", "CREM1", "CTNNB1",
    "EGR1", "ELK1", "ERF", "ESR2", "ETV4", "ETV5", "FOXO1", "GATA3",
    "GLI1", "HHEX", "HIF1A", "HOXD3", "JUN", "MYOD1", "MYOG", "NANOG",
    "NFATC1", "NFATC3", "NR1I2", "NR3C2", "RELA", "RORA", "RORB", "RORC",
    "RUNX2", "SMAD1", "SMAD2", "SMAD3", "SMAD4", "SMAD5", "SMAD8", "SMAD9",
    "SOX2", "STAT1", "STAT3", "STAT4", "STAT5", "TBX21", "TCF4", "THRB",
    "YAP",
}
FAMILY_LABELS = {"AP-1", "ATFx", "CREB", "NFAT", "TCF/LEF family", "TAZ;TEAD"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--edge-register", type=Path, default=EDGE_PATH)
    parser.add_argument("--evidence-register", type=Path, default=EVIDENCE_PATH)
    parser.add_argument("--queue", type=Path, default=QUEUE_PATH)
    parser.add_argument("--stage", type=Path, default=STAGE_PATH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def unique(values: list[str]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        value = value.strip()
        if value and value.casefold() not in {"null", "none", "none_identified", "\\n"} and value.casefold() not in seen:
            seen.add(value.casefold())
            result.append(value)
    return result


def join_unique(values: list[str]) -> str:
    return ";".join(unique(values))


def resolve_terminal_tfs(source_entity: str) -> tuple[list[str], str]:
    label = source_entity.strip()
    if not label or label.casefold() in {"null", "none", "none_identified", "\\n"}:
        return [], "none_named"
    symbols = find_known_tf_symbols(label)
    symbols = sorted(unique(symbols), key=str.casefold)
    family = any(token.casefold() in label.casefold() for token in FAMILY_LABELS)
    composite = any(separator in label for separator in (";", "/", "_")) or len(symbols) > 1
    if composite or family:
        resolution = "composite_or_family_manual_review"
    elif symbols:
        resolution = "single_named_tf"
    else:
        resolution = "named_noncanonical_or_unresolved"
    return symbols, resolution


def find_known_tf_symbols(text: str) -> list[str]:
    return sorted(
        unique(
            [name for name in KNOWN_TFS if re.search(rf"(?<![A-Za-z0-9]){re.escape(name)}(?![A-Za-z0-9])", text, re.I)]
        ),
        key=str.casefold,
    )


def main() -> int:
    args = parse_args()
    edges = read_tsv(args.edge_register)
    evidence = read_tsv(args.evidence_register)
    queue = read_tsv(args.queue)
    stage = read_tsv(args.stage)

    evidence_by_edge: dict[str, list[dict[str, str]]] = defaultdict(list)
    for evidence_row in evidence:
        for edge_id in evidence_row.get("b_edge_ids", "").split(";"):
            if edge_id.strip():
                evidence_by_edge[edge_id.strip()].append(evidence_row)

    current_by_tf: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in stage:
        current_by_tf[row.get("tf_symbol", "").casefold()].append(row)
    queue_by_tf: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in queue:
        # Level A/B rows are the signed/public curation lane; other queue rows
        # are retained in the source queue but are not counted as reusable here.
        if row.get("dorothea_level", "") in {"A", "B", "A;D", "B;D"} or row.get("confidence_tier") in {"high", "medium-high"}:
            queue_by_tf[row.get("tf_symbol", "").casefold()].append(row)

    holds = [
        row for row in edges
        if row.get("edge_status") == "no_evidence_boundary"
        and row.get("confidence_tier") == "low"
        and row.get("source_a_edge_id", "").startswith("M22A")
    ]
    if len(holds) != 4957:
        raise SystemExit(f"expected 4957 Module 22A no-evidence-boundary holds, found {len(holds)}")

    audit_rows: list[dict[str, str]] = []
    for index, edge in enumerate(holds, start=1):
        linked = evidence_by_edge.get(edge["b_edge_id"], [])
        if not linked:
            raise SystemExit(f"{edge['b_edge_id']}: hold has no linked evidence")
        tfs, resolution = resolve_terminal_tfs(edge.get("source_entity", ""))
        relation_tfs = find_known_tf_symbols(edge.get("relation_type", ""))
        current_rows: list[dict[str, str]] = []
        queue_rows: list[dict[str, str]] = []
        for tf in tfs:
            current_rows.extend(current_by_tf.get(tf.casefold(), []))
            queue_rows.extend(queue_by_tf.get(tf.casefold(), []))
        current_rows = sorted({row["materialization_id"]: row for row in current_rows}.values(), key=lambda row: row["materialization_id"])
        queue_rows = sorted({row["curation_id"]: row for row in queue_rows}.values(), key=lambda row: row["curation_id"])
        target_missing = edge.get("target_entity", "").casefold() in {"", "null", "none", "none_identified", "\\n"}
        if resolution == "composite_or_family_manual_review":
            reason = "composite_or_family_terminal_tf_and_no_target_gene"
            action = "manual_composite_tf_decomposition_required"
        elif not tfs:
            if relation_tfs:
                reason = "relation_text_mentions_possible_tf_but_no_target_gene"
                action = "manual_relation_tf_terminal_resolution_required"
            else:
                reason = "no_terminal_tf_and_no_target_gene"
                action = "retain_no_evidence_boundary"
        else:
            reason = "named_terminal_tf_but_no_target_gene"
            action = "review_separate_tf_regulon_lane_keep_handoff_separate"
        if not target_missing:
            reason += "_target_text_present_but_not_gene" if edge.get("pathway_name") != "target_gene" else "_target_gene_scope_requires_review"
        audit_rows.append({
            "audit_id": f"M22B-HOLD-AUDIT-{index:04d}",
            "b_edge_id": edge["b_edge_id"],
            "source_a_edge_id": edge.get("source_a_edge_id", ""),
            "source_entity": edge.get("source_entity", ""),
            "relation_type": edge.get("relation_type", ""),
            "target_entity": edge.get("target_entity", ""),
            "pathway_name": edge.get("pathway_name", ""),
            "edge_status": edge.get("edge_status", ""),
            "confidence_tier": edge.get("confidence_tier", ""),
            "exportable": edge.get("exportable", ""),
            "evidence_ids": join_unique([row.get("b_evidence_id", "") for row in linked]),
            "source_locators": join_unique([row.get("source_locator", "") for row in linked]),
            "hold_reason": reason,
            "terminal_tf_names": ";".join(tfs),
            "terminal_tf_resolution": resolution,
            "relation_tf_mentions": ";".join(relation_tfs),
            "relation_tf_resolution": "narrative_only_manual_review" if relation_tfs else "none_found",
            "current_target_gene_rows": str(len(current_rows)),
            "current_target_pairs": ";".join(f"{row.get('species', '')}|{row.get('tf_symbol', '')}|{row.get('target_symbol', '')}" for row in current_rows),
            "signed_queue_rows": str(len(queue_rows)),
            "signed_queue_pairs": ";".join(f"{row.get('pair_key', '')}|{row.get('curation_id', '')}" for row in queue_rows),
            "recommended_action": action,
            "audit_note": (
                "Reviewed against current Module 22B registers, materialized target-gene stage, and the signed/public TF queue. "
                "This bounded hold is not a global negative-literature claim. Separate TF-target coverage does not prove that the Module 22A upstream route activates the TF."
            ),
        })

    if len(audit_rows) != 4957 or len({row["b_edge_id"] for row in audit_rows}) != 4957:
        raise SystemExit("hold audit is not row-complete and unique")
    if any(not row["evidence_ids"] for row in audit_rows):
        raise SystemExit("hold audit contains an unlinked row")

    output_tsv = args.output_dir / "module22b_no_evidence_holds_audit.tsv"
    summary_path = args.output_dir / "module22b_no_evidence_holds_audit_summary.json"
    write_tsv(output_tsv, audit_rows)
    summary = {
        "audit_version": "module22b-no-evidence-holds-2026-09-03",
        "edge_register": str(args.edge_register),
        "evidence_register": str(args.evidence_register),
        "priority_tf_queue": str(args.queue),
        "materialization_stage": str(args.stage),
        "holds_audited": len(audit_rows),
        "unique_hold_edges": len({row["b_edge_id"] for row in audit_rows}),
        "linked_hold_rows": sum(bool(row["evidence_ids"]) for row in audit_rows),
        "by_source_entity": dict(sorted(Counter(row["source_entity"] or "<blank>" for row in audit_rows).items(), key=lambda item: (-item[1], item[0]))),
        "by_hold_reason": dict(sorted(Counter(row["hold_reason"] for row in audit_rows).items())),
        "by_terminal_tf_resolution": dict(sorted(Counter(row["terminal_tf_resolution"] for row in audit_rows).items())),
        "by_relation_tf_resolution": dict(sorted(Counter(row["relation_tf_resolution"] for row in audit_rows).items())),
        "by_recommended_action": dict(sorted(Counter(row["recommended_action"] for row in audit_rows).items())),
        "holds_with_relation_text_tf_mentions": sum(bool(row["relation_tf_mentions"]) for row in audit_rows),
        "structured_source_none_with_relation_tf_mentions": sum(
            not row["terminal_tf_names"] and bool(row["relation_tf_mentions"]) for row in audit_rows
        ),
        "holds_with_current_target_gene_coverage": sum(int(row["current_target_gene_rows"]) > 0 for row in audit_rows),
        "holds_with_signed_queue_coverage": sum(int(row["signed_queue_rows"]) > 0 for row in audit_rows),
        "current_target_gene_rows_reused_as_context_only": sum(int(row["current_target_gene_rows"]) for row in audit_rows),
        "signed_queue_rows_reused_as_context_only": sum(int(row["signed_queue_rows"]) for row in audit_rows),
        "promotions_from_hold_rows": 0,
        "interpretation": (
            "All 4957 rows were reviewed. They remain no_evidence_boundary because the upstream handoff does not establish a target gene. "
            "Rows with named TFs are routed to a separate TF-regulon review lane; their existing regulon coverage is not attached to the upstream handoff and does not establish upstream TF activation."
        ),
    }
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
