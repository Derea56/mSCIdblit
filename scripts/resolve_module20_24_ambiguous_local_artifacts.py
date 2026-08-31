#!/usr/bin/env python3
"""Resolve ambiguous Phase-2 keys only from one metadata-bearing local record.

This pass is intentionally narrower than identifier lookup.  For each
ambiguous canonical key, all cited local XML/HTML artifacts are combined.  A
mapping is emitted only when the combined artifact set contains exactly one
record, that record has a PMID and paper title, and the PMID is explicitly one
of the PMIDs already present in the canonical key.  Identifier-only text/TSV
artifacts and multi-record search packets remain unresolved.
"""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

from resolve_module20_24_phase2_paper_identities import all_tokens, artifact_paths, parse_artifact


ROOT = Path(__file__).resolve().parents[1]
REVIEW_ROOT = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review"
EXCEPTIONS = REVIEW_ROOT / "module20_24_phase2_paper_identity_exceptions.tsv"
OUT = REVIEW_ROOT / "module20_24_phase2_paper_identity_local_artifact_resolutions.tsv"
REPORT = REVIEW_ROOT / "module20_24_phase2_paper_identity_local_artifact_resolutions.md"

FIELDS = [
    "module", "canonical_paper_key", "resolved_pmid", "resolved_pmcid",
    "resolved_doi", "resolution_status", "resolution_basis",
    "authoritative_source", "source_metadata_title", "source_metadata_authors",
    "source_metadata_year", "source_metadata_journal", "source_metadata_abstract",
    "source_metadata_url", "extraction_row_count", "extraction_ids",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(rows: list[dict[str, str]]) -> None:
    with OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    groups: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in read_tsv(EXCEPTIONS):
        if row.get("identity_resolution_status") == "unresolved_ambiguous_multiple_canonical_pmids":
            groups[(row.get("module", ""), row.get("canonical_paper_key", ""))].append(row)

    rows: list[dict[str, str]] = []
    inspected_groups = 0
    for (module, key), group in sorted(groups.items()):
        key_pmids = {value for kind, value in all_tokens(key) if kind == "PMID"}
        paths = []
        for source in group:
            for path in artifact_paths(source.get("source_locator", "")):
                if path.suffix.lower() in {".xml", ".xhtml", ".html", ".htm"} and path not in paths:
                    paths.append(path)
        records = []
        for path in paths:
            records.extend(parse_artifact(path))
        inspected_groups += 1
        if len(records) != 1:
            continue
        record = records[0]
        pmid = str(record.get("pmid", ""))
        title = str(record.get("title", ""))
        record_tokens = set(record.get("tokens", set()))
        if not pmid or not title or pmid not in key_pmids or not (record_tokens & all_tokens(key)):
            continue
        source_file = str(record.get("source_file", ""))
        rows.append({
            "module": module,
            "canonical_paper_key": key,
            "resolved_pmid": pmid,
            "resolved_pmcid": str(record.get("pmcid", "")),
            "resolved_doi": str(record.get("doi", "")),
            "resolution_status": "resolved_authoritative_local_artifact",
            "resolution_basis": "one metadata-bearing local artifact record matched one PMID already explicit in canonical_paper_key",
            "authoritative_source": source_file,
            "source_metadata_title": title,
            "source_metadata_authors": str(record.get("authors", "")),
            "source_metadata_year": str(record.get("year", "")),
            "source_metadata_journal": str(record.get("journal", "")),
            "source_metadata_abstract": str(record.get("abstract", "")),
            "source_metadata_url": str(record.get("url", "")),
            "extraction_row_count": str(len(group)),
            "extraction_ids": ";".join(sorted(row.get("extraction_id", "") for row in group)),
        })

    write_tsv(rows)
    report = [
        "# Phase-2 ambiguous local-artifact identity resolution",
        "",
        "Only ambiguous keys with exactly one metadata-bearing local XML/HTML record were considered.",
        "The record PMID had to be explicitly present in the canonical key; multi-record and identifier-only artifacts were excluded.",
        "",
        f"- Ambiguous groups inspected: {inspected_groups:,}",
        f"- Exact local-artifact mappings accepted: {len(rows):,}",
        f"- Extraction rows covered: {sum(int(row['extraction_row_count']) for row in rows):,}",
        "",
        f"The resolver input ledger is {OUT.name}.",
        "Unmatched groups remain in the ambiguous exception queue.",
        "",
    ]
    REPORT.write_text("\n".join(report))
    print(f"ambiguous_groups={inspected_groups} resolved_groups={len(rows)} resolved_rows={sum(int(row['extraction_row_count']) for row in rows)}")


if __name__ == "__main__":
    main()
