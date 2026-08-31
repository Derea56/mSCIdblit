#!/usr/bin/env python3
"""Summarize staged evidence, routed module handoffs, and corroboration state."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INTAKE = ROOT / "data/processed/module20_24_database_intake_v1"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


def main() -> int:
    leads = read_tsv(INTAKE / "database_candidate_leads.tsv")
    literature = read_tsv(INTAKE / "database_literature_review_queue.tsv")
    decisions = read_tsv(INTAKE / "database_evidence_decisions_merged.tsv")
    staging = read_tsv(INTAKE / "agent_evidence_staging.tsv")
    corroboration = read_tsv(INTAKE / "agent_review_corroboration_status.tsv")
    modules = ("20A", "21A", "23A", "24A")
    fields = [
        "module", "candidate_leads", "literature_review_candidates", "abstract_supported",
        "hold_for_fulltext", "context_only", "no_exact_support", "staged_rows",
        "staged_abstract_supported", "staged_hold_for_fulltext", "staged_context_only",
        "staged_no_exact_support", "routed_to_20A", "routed_to_21A", "routed_to_22A",
        "routed_to_23A", "routed_to_24A", "staged_linked_second_source_available",
        "staged_needs_independent_source_search", "status",
    ]
    output = []
    for module in modules:
        module_leads = [row for row in leads if row.get("module_primary") == module]
        module_lit = [row for row in literature if row.get("module_primary") == module]
        module_decisions = [row for row in decisions if row.get("module_primary") == module]
        module_staging = [row for row in staging if row.get("module_primary") == module]
        module_corrob = [row for row in corroboration if row.get("module_primary") == module]
        decision_counts = Counter(row.get("disposition", "") for row in module_decisions)
        staged_counts = Counter(row.get("disposition", "") for row in module_staging)
        routes = Counter(route for row in module_staging for route in row.get("routed_modules", "").split(";") if route)
        corrob_counts = Counter(row.get("corroboration_status", "") for row in module_corrob)
        row = {
            "module": module,
            "candidate_leads": str(len(module_leads)),
            "literature_review_candidates": str(len(module_lit)),
            "abstract_supported": str(decision_counts["abstract_supported_candidate"]),
            "hold_for_fulltext": str(decision_counts["hold_for_fulltext"]),
            "context_only": str(decision_counts["context_only"]),
            "no_exact_support": str(decision_counts["no_exact_support"]),
            "staged_rows": str(len(module_staging)),
            "staged_abstract_supported": str(staged_counts["abstract_supported_candidate"]),
            "staged_hold_for_fulltext": str(staged_counts["hold_for_fulltext"]),
            "staged_context_only": str(staged_counts["context_only"]),
            "staged_no_exact_support": str(staged_counts["no_exact_support"]),
            "routed_to_20A": str(routes["20A"]),
            "routed_to_21A": str(routes["21A"]),
            "routed_to_22A": str(routes["22A"]),
            "routed_to_23A": str(routes["23A"]),
            "routed_to_24A": str(routes["24A"]),
            "staged_linked_second_source_available": str(corrob_counts["linked_second_source_available"]),
            "staged_needs_independent_source_search": str(corrob_counts["needs_independent_source_search"]),
            "status": "staging_only_unless_exact_pair_and_corroborated",
        }
        output.append(row)
    out_path = INTAKE / "module20_24_evidence_summary.tsv"
    write_tsv(out_path, fields, output)
    manifest = {
        "modules": list(modules),
        "output": str(out_path.relative_to(ROOT)),
        "canonical_write_performed": False,
        "staged_rows": len(staging),
        "staged_corroboration_rows": len(corroboration),
    }
    (INTAKE / "module20_24_evidence_summary.manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
