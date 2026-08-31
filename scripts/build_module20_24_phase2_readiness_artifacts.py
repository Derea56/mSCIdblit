#!/usr/bin/env python3
"""Build conservative unresolved and canonical-import audit manifests.

The outputs are staging proposals only. They do not insert or update canonical
Paper, Observation, AuthorClaim, SignalingEdge, or SignalingEdgeSource rows.
"""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW_ROOT = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review"
PHASE2 = REVIEW_ROOT / "module20_24_integrated_phase2_extractions.tsv"
UNRESOLVED = REVIEW_ROOT / "module20_24_unresolved_no_evidence_register.tsv"
MANIFEST = REVIEW_ROOT / "module20_24_canonical_import_manifest.tsv"
REPORT = REVIEW_ROOT / "module20_24_phase2_readiness_report.md"
MODULES = ("20B", "21B", "22B", "23B", "24B")

MANIFEST_FIELDS = [
    "manifest_id", "action_type", "module", "b_edge_id", "b_evidence_id",
    "evidence_layer", "canonical_paper_key", "paper_anchor_locator",
    "status", "source_section", "figure_or_table", "species",
    "cell_type_or_model", "assay_or_perturbation", "relation_type",
    "pathway_or_branch", "confidence", "source_locator",
    "context_and_limitations", "search_boundary", "reviewer_notes",
]

UNRESOLVED_FIELDS = [
    "module", "b_edge_id", "b_evidence_id", "exportable", "evidence_layer",
    "disposition", "canonical_paper_key", "source_locator", "confidence",
    "blocker", "search_boundary", "context_and_limitations", "reviewer_notes",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def stable_anchor(value: str) -> bool:
    return bool(re.search(r"\b(?:PMID|PMCID|DOI):\S+|https?://\S+", value or "", re.I))


def useful(value: str) -> bool:
    normalized = (value or "").strip().lower()
    return bool(normalized) and normalized not in {
        "not located", "not verified", "not available", "not applicable",
        "not specified", "not specified at atomic experiment level",
    }


def validated_observation(row: dict[str, str]) -> bool:
    status = row.get("observation_status", "").lower()
    if "validated" not in status or "abstract" in status or "metadata" in status:
        return False
    return stable_anchor(row.get("canonical_paper_key", "")) and useful(row.get("observation_source_section", "")) and useful(row.get("observation_value_or_blocker", ""))


def validated_claim(row: dict[str, str]) -> bool:
    status = row.get("claim_status", "").lower()
    if "validated" not in status or "abstract" in status or "metadata" in status:
        return False
    return stable_anchor(row.get("canonical_paper_key", "")) and useful(row.get("claim_source_section", "")) and useful(row.get("claim_text_or_blocker", ""))


def register(module: str, kind: str) -> list[dict[str, str]]:
    key = module.lower()
    path = ROOT / "work" / "module_b_consolidation" / f"module{key}" / f"module{key}_{kind}_register.tsv"
    return read_tsv(path)


def main() -> None:
    phase2 = read_tsv(PHASE2)
    by_evidence: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in phase2:
        by_evidence[(row["module"], row["b_evidence_id"])].append(row)

    manifest_rows: list[dict[str, str]] = []
    action_counts = Counter()
    for index, row in enumerate(phase2, start=1):
        paper_ok = stable_anchor(row.get("canonical_paper_key", "")) and not row.get("paper_status", "").lower().startswith(("unresolved", "metadata", "search_boundary", "boundary"))
        obs_ok = validated_observation(row)
        claim_ok = validated_claim(row)
        common = {
            "module": row["module"], "b_edge_id": row["b_edge_id"], "b_evidence_id": row["b_evidence_id"],
            "evidence_layer": row["evidence_layer"], "canonical_paper_key": row["canonical_paper_key"],
            "paper_anchor_locator": row["canonical_paper_key"], "species": row["observation_species"],
            "cell_type_or_model": row["observation_cell_or_model"], "assay_or_perturbation": row["observation_assay"],
            "relation_type": "", "pathway_or_branch": "", "confidence": row["confidence"],
            "source_locator": row["source_locator"], "context_and_limitations": row["context_and_limitations"],
            "search_boundary": row["search_boundary"], "reviewer_notes": row["reviewer_notes"],
        }
        actions = [
            ("Paper", "reuse_candidate" if paper_ok else "unresolved", "", ""),
            ("Observation", "validated_candidate" if obs_ok else "defer_unresolved", row["observation_source_section"], row["observation_figure_or_table"]),
            ("AuthorClaim", "validated_candidate" if claim_ok else "defer_unresolved", row["claim_source_section"], ""),
            ("SignalingEdge", "existing_edge_support_candidate" if (obs_ok or claim_ok) else "defer_unresolved", "", ""),
            ("SignalingEdgeSource", "link_candidate" if (paper_ok or obs_ok or claim_ok) else "defer_unresolved", "", ""),
        ]
        for action_type, status, section, figure in actions:
            record = {field: "" for field in MANIFEST_FIELDS}
            record.update(common)
            record.update({
                "manifest_id": f"M20_24-{index:06d}-{action_type}",
                "action_type": action_type,
                "status": status,
                "source_section": section,
                "figure_or_table": figure,
            })
            manifest_rows.append(record)
            action_counts[(action_type, status)] += 1

    with MANIFEST.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(manifest_rows)

    unresolved_rows: list[dict[str, str]] = []
    for module in MODULES:
        evidence_rows = register(module, "evidence")
        for evidence in evidence_rows:
            evidence_id = evidence["b_evidence_id"]
            rows = by_evidence.get((module, evidence_id), [])
            if rows:
                paper_ok = any(stable_anchor(row.get("canonical_paper_key", "")) for row in rows)
                obs_ok = any(validated_observation(row) for row in rows)
                claim_ok = any(validated_claim(row) for row in rows)
                if paper_ok and (obs_ok or claim_ok):
                    disposition = "partial_support_with_deferred_routes" if not (obs_ok and claim_ok) else "candidate_import_route"
                else:
                    disposition = "unresolved_primary_support"
                row = rows[0]
                blocker_values = []
                for candidate in rows:
                    for value in (candidate.get("observation_value_or_blocker", ""), candidate.get("claim_text_or_blocker", "")):
                        if value and "DO_NOT_CREATE" not in value:
                            blocker_values.append(value)
                blocker = " || ".join(sorted(set(blocker_values)))
                boundary = " || ".join(sorted({r.get("search_boundary", "") for r in rows if r.get("search_boundary", "")}))
                context = " || ".join(sorted({r.get("context_and_limitations", "") for r in rows if r.get("context_and_limitations", "")}))
                reviewer = " || ".join(sorted({r.get("reviewer_notes", "") for r in rows if r.get("reviewer_notes", "")}))
                if disposition == "candidate_import_route":
                    continue
                unresolved_rows.append({
                    "module": module, "b_edge_id": evidence.get("b_edge_id", ""), "b_evidence_id": evidence_id,
                    "exportable": evidence.get("exportable", ""), "evidence_layer": evidence.get("evidence_layer", ""),
                    "disposition": disposition, "canonical_paper_key": row.get("canonical_paper_key", ""),
                    "source_locator": row.get("source_locator", ""), "confidence": row.get("confidence", ""),
                    "blocker": blocker or "No import-ready atomic route retained.", "search_boundary": boundary,
                    "context_and_limitations": context, "reviewer_notes": reviewer,
                })
            else:
                unresolved_rows.append({
                    "module": module, "b_edge_id": evidence.get("b_edge_id", ""), "b_evidence_id": evidence_id,
                    "exportable": evidence.get("exportable", ""), "evidence_layer": evidence.get("evidence_layer", ""),
                    "disposition": "boundary_not_processed" if evidence.get("exportable") != "true" else "unresolved_no_phase2_route",
                    "canonical_paper_key": "", "source_locator": evidence.get("source_locator", ""),
                    "confidence": evidence.get("confidence", ""), "blocker": "No supervised Phase-2 route was retained for this evidence record.",
                    "search_boundary": evidence.get("search_boundary", "") or "Repository and primary-literature follow-up remains required before import.",
                    "context_and_limitations": evidence.get("context_and_limitations", ""),
                    "reviewer_notes": "Explicitly unresolved; no directness or pathway promotion.",
                })

    with UNRESOLVED.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=UNRESOLVED_FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(unresolved_rows)

    lines = [
        "# Module 20B–24B Phase-2 readiness report",
        "",
        "This report describes audit-layer staging only. Canonical SQL materialization remains blocked and no canonical Paper, Observation, AuthorClaim, SignalingEdge, or SignalingEdgeSource rows were written.",
        "",
        f"- Integrated Phase-2 rows: {len(phase2):,}",
        f"- Manifest actions: {len(manifest_rows):,}",
        f"- Unresolved/boundary evidence records: {len(unresolved_rows):,}",
        "",
        "## Evidence coverage",
        "",
        "| Module | Exportable evidence | Phase-2 evidence covered |",
        "|---|---:|---:|",
    ]
    for module in MODULES:
        expected = {r["b_evidence_id"] for r in register(module, "evidence") if r.get("exportable") == "true"}
        covered = {r["b_evidence_id"] for r in phase2 if r["module"] == module}
        lines.append(f"| {module} | {len(expected):,} | {len(expected & covered):,} |")
    lines.extend(["", "## Candidate action counts", "", "| Action | Status | Rows |", "|---|---|---:|"])
    lines.extend(f"| {action} | {status} | {count:,} |" for (action, status), count in sorted(action_counts.items()))
    lines.extend([
        "",
        "## Gates",
        "",
        "- Evidence-layer drift was excluded from the integrated phase-2 ledger; the B-layer register remains the layer authority.",
        "- All exportable evidence IDs are represented in the integrated Phase-2 ledger.",
        "- Fallback and unresolved rows are not import-ready.",
        "- Generated isolated staging SQL loaded successfully in a temporary PostgreSQL cluster; canonical materialization was not run.",
        "- Frozen Module 20A ledgers, classifications, and manifest were not modified.",
        "",
        "## Files",
        "",
        f"- `{PHASE2.relative_to(ROOT)}`",
        f"- `{UNRESOLVED.relative_to(ROOT)}`",
        f"- `{MANIFEST.relative_to(ROOT)}`",
        f"- `{REPORT.relative_to(ROOT)}`",
        "",
    ])
    REPORT.write_text("\n".join(lines))
    print(f"phase2_rows={len(phase2)} manifest_rows={len(manifest_rows)} unresolved_rows={len(unresolved_rows)}")


if __name__ == "__main__":
    main()
