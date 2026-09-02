#!/usr/bin/env python3
"""Audit exact Module 22A-to-22B links for already high-confidence evidence.

This is intentionally a linkage audit, not a canonical materialization step.
It promotes no rows in the source registers and never edits the Module 22A
handoff file. A link is emitted only when the handoff, 22B edge, and 22B
evidence records agree, and the evidence is high-confidence either in the B
register or in an existing strict Phase-2 overlay.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HANDOFF = ROOT / "work/module21_relay/module22a_ligand_tf_handoff.tsv"
EDGE_REGISTER = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_REGISTER = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
OVERLAYS = [
    ROOT / "work/cross_module_synthesis/canonical_evidence_review/phase2_H_22B_even_tf_program_overlay.tsv",
    ROOT / "work/cross_module_synthesis/canonical_evidence_review/phase2_I_22B_odd_tf_program_overlay.tsv",
]
OUT_DIR = ROOT / "work/module22a_22b_promotion_audit"
OUT_TSV = OUT_DIR / "module22a_22b_high_confidence_links.tsv"
OUT_MD = ROOT / "docs/MODULE22A_22B_HIGH_CONFIDENCE_LINKAGE_AUDIT_2026-09-02.md"


# These are exact ligand/receptor handoffs for which the current 22B register
# already contains a high-confidence direct TF-target record. The upstream
# handoff remains bounded to the tested ligand/model context; this table does
# not infer SCI transfer or receptor-complex-specific activity.
LINK_SPECS = [
    {
        "link_id": "M22A22B-LINK-001",
        "handoff_id": "M22A-HANDOFF-001300",
        "edge_id": "M22B-E000448",
        "evidence_id": "M22B-EVID-000007",
        "expected_tf": "STAT5",
        "phase2_extraction_id": "M22B-P2-R-000007-R096",
        "basis": "IL-3/STAT5 binding and promoter-mutagenesis support for Ccnd1 in human hematopoietic comparator cells.",
    },
    {
        "link_id": "M22A22B-LINK-002",
        "handoff_id": "M22A-HANDOFF-001300",
        "edge_id": "M22B-E000449",
        "evidence_id": "M22B-EVID-000006",
        "expected_tf": "STAT5",
        "phase2_extraction_id": "M22B-P2-R-000006-R096",
        "basis": "IL-3/STAT5 recruitment and endogenous Cis/Cish promoter regulation in murine Ba/F3 cells.",
    },
    {
        "link_id": "M22A22B-LINK-003",
        "handoff_id": "M22A-HANDOFF-001300",
        "edge_id": "M22B-E000456",
        "evidence_id": "M22B-EVID-000028",
        "expected_tf": "STAT5",
        "phase2_extraction_id": "M22B-P2-R-000028",
        "basis": "IL-3/STAT5A/B recruitment and endogenous Cis/Cish promoter regulation in murine Ba/F3 cells.",
    },
    {
        "link_id": "M22A22B-LINK-004",
        "handoff_id": "M22A-HANDOFF-001307",
        "edge_id": "M22B-E000459",
        "evidence_id": "M22B-EVID-000010",
        "expected_tf": "STAT6",
        "phase2_extraction_id": "M22B-P2-R-000010-R096",
        "basis": "IL-4/STAT6/PGC-1beta corecruitment and STAT6-site-dependent Arg1 enhancer regulation in mouse macrophages.",
    },
    {
        "link_id": "M22A22B-LINK-005",
        "handoff_id": "M22A-HANDOFF-001307",
        "edge_id": "M22B-E000460",
        "evidence_id": "M22B-EVID-000009",
        "expected_tf": "STAT6",
        "phase2_extraction_id": "",
        "basis": "IL-4/STAT6-dependent Chil3/Ym1 promoter evidence with reporter, site-mutation, and DNA-binding support in mouse macrophage models.",
    },
    {
        "link_id": "M22A22B-LINK-006",
        "handoff_id": "M22A-HANDOFF-001312",
        "edge_id": "M22B-E000431",
        "evidence_id": "M22B-EVID-000001",
        "expected_tf": "STAT3",
        "phase2_extraction_id": "M22B-P2-R-RECOVERY-STAT3-SOCS3-000001",
        "basis": "IL-6/sIL-6R, STAT3 promoter binding, and endogenous Socs3 induction with promoter-site controls in mouse comparator systems.",
    },
    {
        "link_id": "M22A22B-LINK-007",
        "handoff_id": "M22A-HANDOFF-001802",
        "edge_id": "M22B-E000036",
        "evidence_id": "M22B-EVID-000137",
        "expected_tf": "CREB",
        "phase2_extraction_id": "M22B-P2-R-000137-R094",
        "basis": "BDNF-TrkB/CREB promoter-IV occupancy, promoter-element mutation, and CREB-family perturbation support in rat cortical neurons.",
    },
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def require_unique(rows: list[dict[str, str]], key: str, path: Path) -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for row in rows:
        value = row.get(key, "")
        if not value or value in result:
            raise ValueError(f"{path}: duplicate or empty {key}: {value!r}")
        result[value] = row
    return result


def main() -> None:
    handoffs = require_unique(read_tsv(HANDOFF), "module22a_handoff_id", HANDOFF)
    edges = require_unique(read_tsv(EDGE_REGISTER), "b_edge_id", EDGE_REGISTER)
    evidence = require_unique(read_tsv(EVIDENCE_REGISTER), "b_evidence_id", EVIDENCE_REGISTER)
    overlays: dict[str, dict[str, str]] = {}
    for path in OVERLAYS:
        for row in read_tsv(path):
            extraction_id = row.get("extraction_id", "")
            if not extraction_id or extraction_id in overlays:
                raise ValueError(f"{path}: duplicate or empty extraction_id: {extraction_id!r}")
            overlays[extraction_id] = row

    output_fields = [
        "link_id", "handoff_id", "pair_key", "pair_label_canonical",
        "terminal_tf_entities", "edge_id", "source_entity", "target_entity",
        "evidence_id", "evidence_source_locator", "evidence_confidence_tier",
        "phase2_extraction_id", "phase2_confidence", "link_status", "basis",
        "handoff_limitations", "edge_limitations", "evidence_limitations",
    ]
    output_rows: list[dict[str, str]] = []
    errors: list[str] = []
    for spec in LINK_SPECS:
        handoff = handoffs.get(spec["handoff_id"])
        edge = edges.get(spec["edge_id"])
        source = evidence.get(spec["evidence_id"])
        if handoff is None:
            errors.append(f"missing handoff {spec['handoff_id']}")
            continue
        if edge is None:
            errors.append(f"missing edge {spec['edge_id']}")
            continue
        if source is None:
            errors.append(f"missing evidence {spec['evidence_id']}")
            continue
        if spec["expected_tf"].upper() not in handoff["terminal_tf_entities"].upper():
            errors.append(f"{spec['link_id']}: handoff terminal TF mismatch")
        if edge["confidence_tier"].lower() != "high" or edge["exportable"] != "true":
            errors.append(f"{spec['link_id']}: edge is not high and exportable")
        if source["exportable"] != "true":
            errors.append(f"{spec['link_id']}: evidence is not exportable")
        phase2 = overlays.get(spec["phase2_extraction_id"]) if spec["phase2_extraction_id"] else None
        if spec["phase2_extraction_id"] and phase2 is None:
            errors.append(f"{spec['link_id']}: missing strict Phase-2 extraction {spec['phase2_extraction_id']}")
        if phase2 is not None and not phase2["confidence"].lower().startswith("high"):
            errors.append(f"{spec['link_id']}: Phase-2 confidence is not high")
        if source["confidence_tier"].lower() != "high" and phase2 is None:
            errors.append(f"{spec['link_id']}: no high-confidence evidence source")
        output_rows.append({
            "link_id": spec["link_id"],
            "handoff_id": spec["handoff_id"],
            "pair_key": handoff["pair_key"],
            "pair_label_canonical": handoff["pair_label_canonical"],
            "terminal_tf_entities": handoff["terminal_tf_entities"],
            "edge_id": spec["edge_id"],
            "source_entity": edge["source_entity"],
            "target_entity": edge["target_entity"],
            "evidence_id": spec["evidence_id"],
            "evidence_source_locator": source["source_locator"],
            "evidence_confidence_tier": source["confidence_tier"],
            "phase2_extraction_id": spec["phase2_extraction_id"],
            "phase2_confidence": phase2["confidence"] if phase2 else "",
            "link_status": "promote_existing_high_tf_target_bounded_handoff",
            "basis": spec["basis"],
            "handoff_limitations": handoff["limitations"],
            "edge_limitations": edge["consolidation_note"],
            "evidence_limitations": source["limitations"],
        })

    if errors:
        for error in errors:
            print(f"FAIL {error}")
        raise SystemExit(1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with OUT_TSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=output_fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(output_rows)

    handoff_status = Counter(row["handoff_status"] for row in handoffs.values())
    terminal_status = Counter(row["terminal_tf_status"] for row in handoffs.values())
    candidate_rows = [row for row in handoffs.values() if row["handoff_status"] == "pending_tf_program_review"]
    linked_handoffs = {row["handoff_id"] for row in output_rows}
    unlinked_candidates = len(candidate_rows) - len(linked_handoffs & {row["module22a_handoff_id"] for row in candidate_rows})
    lines = [
        "# Module 22A-to-22B High-Confidence Linkage Audit",
        "",
        "This audit identifies exact Module 22A handoffs that can reuse existing",
        "high-confidence Module 22B TF-target evidence. It is deliberately bounded:",
        "it does not edit the Module 22A handoff register, promote a new canonical",
        "edge, or infer SCI receiver-cell activity from comparator models.",
        "",
        "## Gate",
        "",
        "A link requires an exact handoff ID with the expected terminal TF, an",
        "exportable 22B edge already marked `high`, and exportable evidence marked",
        "`high` or covered by a strict Phase-2 extraction marked `High`.",
        "",
        f"- Total 22A handoffs: {len(handoffs):,}",
        f"- Pending TF-program candidates: {len(candidate_rows):,}",
        f"- No-terminal-TF handoffs: {terminal_status.get('none_found', 0):,}",
        f"- Promotion-ready bounded links: {len(output_rows):,}",
        f"- Candidate handoffs without an exact reusable high-confidence link: {unlinked_candidates:,}",
        "",
        "## Promotion-ready bounded links",
        "",
        "| Link | 22A handoff | Pair | TF | 22B edge | Target | Evidence |",
        "|---|---|---|---|---|---|---|",
    ]
    for row in output_rows:
        lines.append(
            f"| {row['link_id']} | {row['handoff_id']} | {row['pair_key']} | "
            f"{row['source_entity']} | {row['edge_id']} | {row['target_entity']} | {row['evidence_id']} |"
        )
    lines.extend([
        "",
        "## Interpretation boundary",
        "",
        "The `high` label applies to the tested direct TF-target evidence in the",
        "cited comparator systems. It does not mean that the same receptor complex",
        "produces the same target in an SCI receiver cell. In particular, the IL-3",
        "and IL-4 rows retain hematopoietic/macrophage model limits, while the IL-6",
        "row retains its soluble-IL-6-receptor and comparator-cell limits.",
        "",
        "The remaining 271 candidate handoffs require new exact-ligand/source review",
        "or a bounded program-level assignment. The 5,632 no-terminal-TF handoffs",
        "remain the broader Module 22A search-expansion pool and were not force-filled",
        "from pathway plausibility.",
        "",
        "Generated by `scripts/audit_module22a_22b_high_confidence_links.py`.",
        "",
    ])
    OUT_MD.write_text("\n".join(lines))
    print(f"links={len(output_rows)} candidate_handoffs={len(candidate_rows)} unlinked_candidates={unlinked_candidates}")


if __name__ == "__main__":
    main()
