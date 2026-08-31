#!/usr/bin/env python3
"""Resolve rows where one authoritative DOI/PMCID is shared by key and locator.

This is an extraction-row adjudication lane for composite keys. It accepts only
one shared DOI or PMCID whose exact mapping is already present in the accepted
NCBI ledger. Rows with zero or multiple shared authoritative identifiers stay
unresolved.
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

import resolve_module20_24_identity_exception_batch as ncbi
import resolve_module20_24_phase2_paper_identities as base


ROOT = Path(__file__).resolve().parents[1]
REVIEW_ROOT = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review"
INPUT = REVIEW_ROOT / "module20_24_phase2_paper_identity_resolution.tsv"
OUT = REVIEW_ROOT / "module20_24_phase2_paper_identity_shared_identifier_resolutions.tsv"
REPORT = REVIEW_ROOT / "module20_24_phase2_paper_identity_shared_identifier_resolutions.md"

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
    authoritative = {
        (row.get("identifier_type", ""), row.get("identifier_value", "")): row
        for row in read_tsv(ncbi.OUT)
        if row.get("resolution_status") == "resolved_authoritative_ncbi" and row.get("resolved_pmid")
    }
    accepted: list[dict[str, str]] = []
    inspected = Counter()
    rejected = Counter()
    for row in read_tsv(INPUT):
        if not row.get("identity_resolution_status", "").startswith("unresolved_"):
            continue
        key_tokens = base.all_tokens(row.get("canonical_paper_key", ""))
        locator_tokens = base.all_tokens(row.get("source_locator", ""))
        shared = sorted(
            token for token in key_tokens & locator_tokens
            if token[0] in {"DOI", "PMCID"} and token in authoritative
        )
        if not shared:
            continue
        inspected[row["identity_resolution_status"]] += 1
        if len(shared) != 1:
            rejected["multiple_shared_authoritative_identifiers"] += 1
            continue
        token = shared[0]
        record = authoritative[token]
        accepted.append({
            "extraction_id": row.get("extraction_id", ""),
            "module": row.get("module", ""),
            "b_evidence_id": row.get("b_evidence_id", ""),
            "canonical_paper_key": row.get("canonical_paper_key", ""),
            "source_locator": row.get("source_locator", ""),
            "resolved_pmid": record.get("resolved_pmid", ""),
            "resolved_pmcid": record.get("resolved_pmcid", ""),
            "resolved_doi": record.get("resolved_doi", ""),
            "resolution_status": "resolved_authoritative_shared_identifier",
            "resolution_basis": f"one shared authoritative {token[0]} in canonical_paper_key and source_locator mapped uniquely through the NCBI ledger",
            "authoritative_source": record.get("authoritative_source", ""),
            "source_metadata_title": record.get("source_metadata_title", ""),
            "source_metadata_authors": record.get("source_metadata_authors", ""),
            "source_metadata_year": record.get("source_metadata_year", ""),
            "source_metadata_journal": record.get("source_metadata_journal", ""),
            "source_metadata_abstract": record.get("source_metadata_abstract", ""),
            "source_metadata_url": record.get("source_metadata_url", ""),
        })
    if len({row["extraction_id"] for row in accepted}) != len(accepted):
        raise ValueError("duplicate extraction IDs in shared-identifier ledger")
    with OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(accepted, key=lambda row: row["extraction_id"]))
    report = [
        "# Phase-2 shared DOI/PMCID identity resolution",
        "",
        "Only unresolved rows with one shared authoritative DOI or PMCID in both canonical_paper_key and source_locator were accepted.",
        "The shared identifier had to have one accepted exact NCBI mapping; rows with competing shared identifiers were rejected.",
        "",
        f"- Rows with shared authoritative identifier inspected: {sum(inspected.values()):,}",
        f"- Accepted exact row-level mappings: {len(accepted):,}",
        f"- Rejected competing mappings: {sum(rejected.values()):,}",
        "",
        "| Module | Rows |",
        "|---|---:|",
    ]
    report.extend(f"| {module} | {count:,} |" for module, count in sorted(Counter(row["module"] for row in accepted).items()))
    report.extend(["", f"The resolver input ledger is {OUT.name}.", ""])
    REPORT.write_text("\n".join(report))
    print(f"inspected_rows={sum(inspected.values())} accepted_rows={len(accepted)} rejected={sum(rejected.values())}")


if __name__ == "__main__":
    main()
