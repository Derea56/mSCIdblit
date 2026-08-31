#!/usr/bin/env python3
"""Resolve ambiguous Phase-2 keys from an exact metadata-bearing local record.

This pass is intentionally narrower than identifier lookup.  For each
ambiguous canonical key, each cited local XML/HTML artifact is inspected. A
mapping is emitted only when at least one cited artifact contains exactly one
record, that record has a PMID and paper title, and the PMID is explicitly one
of the PMIDs already present in the canonical key. Multi-record search packets
and identifier-only text/TSV artifacts are ignored rather than used to select
a paper.
"""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

from resolve_module20_24_phase2_paper_identities import all_tokens, artifact_paths, parse_artifact


ROOT = Path(__file__).resolve().parents[1]
REVIEW_ROOT = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review"
PHASE2 = REVIEW_ROOT / "module20_24_integrated_phase2_extractions.tsv"
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
    prior = {
        (row.get("module", ""), row.get("canonical_paper_key", "")): row
        for row in read_tsv(OUT)
        if row.get("resolution_status") == "resolved_authoritative_local_artifact"
    }
    groups: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in read_tsv(PHASE2):
        key_pmids = {value for kind, value in all_tokens(row.get("canonical_paper_key", "")) if kind == "PMID"}
        if len(key_pmids) > 1:
            groups[(row.get("module", ""), row.get("canonical_paper_key", ""))].append(row)

    new_rows: list[dict[str, str]] = []
    inspected_groups = 0
    for (module, key), group in sorted(groups.items()):
        key_pmids = {value for kind, value in all_tokens(key) if kind == "PMID"}
        paths = []
        for source in group:
            for path in artifact_paths(source.get("source_locator", "")):
                if path.suffix.lower() in {".xml", ".xhtml", ".html", ".htm"} and path not in paths:
                    paths.append(path)
        strong_records = []
        for path in paths:
            records = parse_artifact(path)
            if len(records) != 1:
                continue
            record = records[0]
            pmid = str(record.get("pmid", ""))
            title = str(record.get("title", ""))
            record_tokens = set(record.get("tokens", set()))
            if pmid and title and pmid in key_pmids and (record_tokens & all_tokens(key)):
                strong_records.append(record)
        inspected_groups += 1
        strong_pmids = {str(record.get("pmid", "")) for record in strong_records}
        if len(strong_pmids) != 1:
            continue
        record = sorted(strong_records, key=lambda item: str(item.get("source_file", "")))[0]
        pmid = str(record.get("pmid", ""))
        title = str(record.get("title", ""))
        source_file = str(record.get("source_file", ""))
        new_rows.append({
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

    merged = prior.copy()
    merged.update({(row["module"], row["canonical_paper_key"]): row for row in new_rows})
    rows = [merged[key] for key in sorted(merged)]
    write_tsv(rows)
    report = [
        "# Phase-2 ambiguous local-artifact identity resolution",
        "",
        "All Phase-2 keys with more than one explicit PMID were inspected for an exact single-record metadata-bearing local XML/HTML artifact.",
        "The selected record PMID had to be explicitly present in the canonical key; multi-record and identifier-only artifacts were excluded.",
        "",
        f"- Multi-PMID Phase-2 groups inspected: {inspected_groups:,}",
        f"- New exact local-artifact mappings accepted: {len(new_rows):,}",
        f"- Retained plus new local-artifact mappings: {len(rows):,}",
        f"- Extraction rows covered: {sum(int(row['extraction_row_count']) for row in rows):,}",
        "",
        f"The resolver input ledger is {OUT.name}.",
        "Unmatched groups remain in the ambiguous exception queue.",
        "",
    ]
    REPORT.write_text("\n".join(report))
    print(f"ambiguous_groups={inspected_groups} new_groups={len(new_rows)} total_groups={len(rows)} total_rows={sum(int(row['extraction_row_count']) for row in rows)}")


if __name__ == "__main__":
    main()
