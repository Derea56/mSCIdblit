#!/usr/bin/env python3
"""Resolve unkeyed Phase-2 rows from exact single-paper local artifacts.

This pass is intentionally row-level. It accepts only an unresolved missing-
identity or no-authoritative-resolution row whose cited local XML/HTML
artifacts contain a unique PMID-bearing paper record with a title. If the
canonical key contains any identifier, the artifact record must also carry
one of those exact identifiers. Blank or placeholder keys are not grouped:
each extraction row receives its own explicit mapping.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

import resolve_module20_24_phase2_paper_identities as base


ROOT = Path(__file__).resolve().parents[1]
REVIEW_ROOT = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review"
INPUT = REVIEW_ROOT / "module20_24_phase2_paper_identity_resolution.tsv"
OUT = REVIEW_ROOT / "module20_24_phase2_paper_identity_unkeyed_local_artifact_resolutions.tsv"
REPORT = REVIEW_ROOT / "module20_24_phase2_paper_identity_unkeyed_local_artifact_resolutions.md"

FIELDS = [
    "extraction_id", "module", "b_evidence_id", "canonical_paper_key",
    "source_locator", "resolved_pmid", "resolved_pmcid", "resolved_doi",
    "resolution_status", "resolution_basis", "authoritative_source",
    "source_metadata_title", "source_metadata_authors", "source_metadata_year",
    "source_metadata_journal", "source_metadata_abstract", "source_metadata_url",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def main() -> None:
    rows = read_tsv(INPUT)
    cache: dict[Path, list[dict[str, object]]] = {}
    accepted: list[dict[str, str]] = []
    inspected = Counter()
    rejected = Counter()

    for row in rows:
        status = row.get("identity_resolution_status", "")
        if status not in {"unresolved_missing_canonical_identity", "unresolved_no_authoritative_resolution"}:
            continue
        paths = []
        for path in base.artifact_paths(row.get("source_locator", "")):
            if path.suffix.lower() in {".xml", ".xhtml", ".html", ".htm"} and path not in paths:
                paths.append(path)
        if not paths:
            continue
        inspected[status] += 1
        key_tokens = base.all_tokens(row.get("canonical_paper_key", ""))
        strong: list[dict[str, object]] = []
        for path in paths:
            if path not in cache:
                cache[path] = base.parse_artifact(path)
            records = cache[path]
            if len(records) != 1:
                continue
            record = records[0]
            pmid = str(record.get("pmid", ""))
            title = str(record.get("title", ""))
            if not pmid or not title:
                continue
            record_tokens = set(record.get("tokens", set()))
            if key_tokens and not (key_tokens & record_tokens):
                continue
            strong.append(record)
        pmids = sorted({str(record.get("pmid", "")) for record in strong})
        if len(pmids) != 1:
            rejected["non_unique_or_unmatched_pmid"] += 1
            continue
        record = sorted(strong, key=lambda item: str(item.get("source_file", "")))[0]
        accepted.append({
            "extraction_id": row.get("extraction_id", ""),
            "module": row.get("module", ""),
            "b_evidence_id": row.get("b_evidence_id", ""),
            "canonical_paper_key": row.get("canonical_paper_key", ""),
            "source_locator": row.get("source_locator", ""),
            "resolved_pmid": pmids[0],
            "resolved_pmcid": str(record.get("pmcid", "")),
            "resolved_doi": str(record.get("doi", "")),
            "resolution_status": "resolved_authoritative_unkeyed_local_artifact",
            "resolution_basis": "one metadata-bearing local artifact record carried a unique PMID for this extraction row",
            "authoritative_source": str(record.get("source_file", "")),
            "source_metadata_title": str(record.get("title", "")),
            "source_metadata_authors": str(record.get("authors", "")),
            "source_metadata_year": str(record.get("year", "")),
            "source_metadata_journal": str(record.get("journal", "")),
            "source_metadata_abstract": str(record.get("abstract", "")),
            "source_metadata_url": str(record.get("url", "")),
        })

    if len({row["extraction_id"] for row in accepted}) != len(accepted):
        raise ValueError("duplicate extraction IDs in unkeyed local-artifact ledger")
    with OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(accepted, key=lambda row: row["extraction_id"]))

    report = [
        "# Phase-2 unkeyed local-artifact identity resolution",
        "",
        "Only unresolved missing-identity and no-authoritative-resolution rows with cited XML/HTML artifacts were inspected.",
        "A row was accepted only when a cited artifact parsed to exactly one paper record with a PMID and title.",
        "If a non-empty canonical key contained identifiers, the artifact record also had to carry one of those exact identifiers.",
        "Rows were resolved individually; blank or placeholder keys were never grouped.",
        "",
        f"- Eligible unresolved rows with cited XML/HTML artifacts: {sum(inspected.values()):,}",
        f"- Accepted exact row-level mappings: {len(accepted):,}",
        f"- Rejected non-unique or unmatched artifact cases: {sum(rejected.values()):,}",
        f"- Unique local artifacts parsed: {len(cache):,}",
        "",
        "## Accepted rows by module",
        "",
        "| Module | Rows |",
        "|---|---:|",
    ]
    report.extend(f"| {module} | {count:,} |" for module, count in sorted(Counter(row["module"] for row in accepted).items()))
    report.extend(["", f"The resolver input ledger is {OUT.name}.", ""])
    REPORT.write_text("\n".join(report))
    print(f"eligible_rows={sum(inspected.values())} accepted_rows={len(accepted)} rejected={sum(rejected.values())} artifacts={len(cache)}")


if __name__ == "__main__":
    main()
