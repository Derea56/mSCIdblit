#!/usr/bin/env python3
"""Map agent-reviewed claims to independent linked papers in the intake."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIR = ROOT / "data/processed/module20_24_database_intake_v1"
FIELDS = [
    "staged_evidence_id", "candidate_key", "module_primary", "routed_modules", "entity_a", "entity_b",
    "primary_pmid", "linked_pmids_for_same_module_entity_pair", "independent_linked_pmid_count",
    "available_corrobating_pmids", "corroboration_status", "cross_module_paper_flag", "notes",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def norm(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").casefold()).strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_DIR)
    args = parser.parse_args()
    queue = read_tsv(args.input_dir / "database_literature_review_queue.tsv")
    staged = read_tsv(args.input_dir / "agent_evidence_staging.tsv")
    cross = {row.get("pmid", "") for row in read_tsv(args.input_dir / "cross_module_paper_corroboration_queue.tsv")}
    grouped: dict[tuple[str, str, str], set[str]] = defaultdict(set)
    for row in queue:
        pmid = row.get("pmid", "")
        if pmid:
            grouped[(row.get("module_primary", ""), norm(row.get("entity_a", "")), norm(row.get("entity_b", "")))].add(pmid)
    rows = []
    for staged_row in staged:
        key = (staged_row.get("module_primary", ""), norm(staged_row.get("entity_a", "")), norm(staged_row.get("entity_b", "")))
        pmids = sorted(grouped.get(key, set()), key=int)
        primary = staged_row.get("pmid", "")
        corroborating = [pmid for pmid in pmids if pmid != primary]
        rows.append({
            "staged_evidence_id": staged_row.get("staged_evidence_id", ""),
            "candidate_key": staged_row.get("candidate_key", ""),
            "module_primary": staged_row.get("module_primary", ""),
            "routed_modules": staged_row.get("routed_modules", ""),
            "entity_a": staged_row.get("entity_a", ""),
            "entity_b": staged_row.get("entity_b", ""),
            "primary_pmid": primary,
            "linked_pmids_for_same_module_entity_pair": ";".join(pmids),
            "independent_linked_pmid_count": str(len(pmids)),
            "available_corrobating_pmids": ";".join(corroborating),
            "corroboration_status": "linked_second_source_available" if corroborating else "needs_independent_source_search",
            "cross_module_paper_flag": "true" if primary in cross else "false",
            "notes": "Distinct PMIDs count as available corroboration leads; the second paper still requires exact-fit review and is not automatic promotion.",
        })
    out = args.input_dir / "agent_review_corroboration_status.tsv"
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    manifest = {
        "staged_rows": len(rows),
        "linked_second_source_available": sum(row["corroboration_status"] == "linked_second_source_available" for row in rows),
        "needs_independent_source_search": sum(row["corroboration_status"] == "needs_independent_source_search" for row in rows),
        "cross_module_paper_rows": sum(row["cross_module_paper_flag"] == "true" for row in rows),
        "canonical_write_performed": False,
    }
    (args.input_dir / "agent_review_corroboration_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
