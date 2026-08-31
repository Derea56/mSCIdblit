#!/usr/bin/env python3
"""Resolve unresolved rows with one exact paper identifier in source_locator.

The source locator is accepted only when it contains exactly one explicit
``PMID:<id>`` or exactly one stable PubMed/PMC/DOI article URL, and the local
paper metadata contains the resulting paper with a title. For an ambiguous
canonical key the selected identifier must also be one of the explicit
identifiers in that key. Non-PMID key identifiers, when present, must
co-occur in the local metadata record. Mappings are stored per extraction row.
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

import resolve_module20_24_phase2_paper_identities as base
from materialize_module20_24_paper_provenance import xml_records


ROOT = Path(__file__).resolve().parents[1]
REVIEW_ROOT = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review"
INPUT = REVIEW_ROOT / "module20_24_phase2_paper_identity_resolution.tsv"
METADATA = ROOT / "work" / "cross_module_synthesis" / "module20_24_canonical_paper_metadata.tsv"
OUT = REVIEW_ROOT / "module20_24_phase2_paper_identity_source_locator_resolutions.tsv"
REPORT = REVIEW_ROOT / "module20_24_phase2_paper_identity_source_locator_resolutions.md"

FIELDS = [
    "extraction_id", "module", "b_evidence_id", "canonical_paper_key",
    "source_locator", "resolved_pmid", "resolved_pmcid", "resolved_doi",
    "resolution_status", "resolution_basis", "authoritative_source",
    "source_metadata_title", "source_metadata_authors", "source_metadata_year",
    "source_metadata_journal", "source_metadata_abstract", "source_metadata_url",
]

PMID_RE = re.compile(r"(?i)\bPMID\s*:\s*(\d+)\b")
URL_RE = re.compile(r"https?://[^;\s]+", re.IGNORECASE)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def metadata_by_pmid() -> dict[str, dict[str, object]]:
    records: dict[str, dict[str, object]] = {
        pmid: dict(record) for pmid, record in xml_records().items()
        if record.get("title")
    }
    for row in read_tsv(METADATA):
        pmid = row.get("pmid", "")
        if pmid and row.get("paper_ready") == "true" and row.get("title") and pmid not in records:
            records[pmid] = {
                "pmid": pmid,
                "pmcid": row.get("pmcid", ""),
                "doi": row.get("doi", ""),
                "title": row.get("title", ""),
                "authors": row.get("authors", ""),
                "publication_year": row.get("publication_year", ""),
                "journal": row.get("journal", ""),
                "abstract": "",
                "source_url": row.get("source_metadata_url", ""),
                "source_file": str(METADATA.relative_to(ROOT)),
            }
    return records


def record_tokens(record: dict[str, object]) -> set[tuple[str, str]]:
    """Return normalized identifiers carried by one local metadata record."""
    tokens: set[tuple[str, str]] = set()
    pmid = str(record.get("pmid", "")).strip()
    pmcid = str(record.get("pmcid", "")).strip().upper()
    doi = str(record.get("doi", "")).strip().lower()
    if pmid:
        tokens.add(("PMID", pmid))
    if pmcid:
        tokens.add(("PMCID", pmcid.removeprefix("PMCID:")))
    if doi:
        tokens.add(("DOI", doi.removeprefix("doi:")))
    return tokens


def metadata_by_identifier(metadata: dict[str, dict[str, object]]) -> dict[tuple[str, str], list[dict[str, object]]]:
    """Index local titled records by each exact PMID, PMCID, or DOI."""
    index: dict[tuple[str, str], list[dict[str, object]]] = {}
    for record in metadata.values():
        for token in record_tokens(record):
            index.setdefault(token, []).append(record)
    return index


def stable_locator_tokens(value: str) -> set[tuple[str, str]]:
    """Return identifiers from stable article URLs only, not query URLs."""
    return {
        token
        for url in URL_RE.findall(value or "")
        for token in base.stable_url_tokens(url)
    }


def main() -> None:
    rows = read_tsv(INPUT)
    metadata = metadata_by_pmid()
    metadata_index = metadata_by_identifier(metadata)
    prior = {
        row.get("extraction_id", ""): row
        for row in read_tsv(OUT)
        if row.get("extraction_id") and row.get("resolved_pmid")
    }
    accepted: list[dict[str, str]] = []
    inspected = Counter()
    rejected = Counter()

    for row in rows:
        status = row.get("identity_resolution_status", "")
        if status not in {"unresolved_missing_canonical_identity", "unresolved_no_authoritative_resolution", "unresolved_ambiguous_multiple_canonical_pmids"}:
            continue
        locator_pmids = sorted(set(PMID_RE.findall(row.get("source_locator", ""))))
        stable_tokens = stable_locator_tokens(row.get("source_locator", ""))
        # A stable article URL is a paper-level selector even when the
        # locator also repeats a composite list of candidate PMIDs. Accept
        # only one distinct stable URL identifier; mixed URLs remain queued.
        if len(stable_tokens) == 1:
            locator_token = next(iter(stable_tokens))
        elif len(locator_pmids) == 1:
            locator_token = ("PMID", locator_pmids[0])
        else:
            continue
        inspected[status] += 1
        candidate_records = metadata_index.get(locator_token, [])
        candidate_pmids = sorted({str(candidate.get("pmid", "")) for candidate in candidate_records if candidate.get("pmid")})
        if len(candidate_pmids) != 1:
            rejected["identifier_not_in_unique_local_metadata"] += 1
            continue
        pmid = candidate_pmids[0]
        record = metadata[pmid]
        key_tokens = base.all_tokens(row.get("canonical_paper_key", ""))
        key_pmids = {value for kind, value in key_tokens if kind == "PMID"}
        if locator_token not in key_tokens:
            rejected["stable_locator_identifier_not_explicit_in_key"] += 1
            continue
        if status == "unresolved_ambiguous_multiple_canonical_pmids" and locator_token[0] == "PMID" and pmid not in key_pmids:
            rejected["ambiguous_locator_pmid_not_explicit_in_key"] += 1
            continue
        non_pmid_key_tokens = {token for token in key_tokens if token[0] != "PMID"}
        local_tokens = record_tokens(record)
        if non_pmid_key_tokens and not (non_pmid_key_tokens & local_tokens):
            rejected["key_identifier_not_in_local_metadata"] += 1
            continue
        accepted.append({
            "extraction_id": row.get("extraction_id", ""),
            "module": row.get("module", ""),
            "b_evidence_id": row.get("b_evidence_id", ""),
            "canonical_paper_key": row.get("canonical_paper_key", ""),
            "source_locator": row.get("source_locator", ""),
            "resolved_pmid": pmid,
            "resolved_pmcid": str(record.get("pmcid", "")),
            "resolved_doi": str(record.get("doi", "")),
            "resolution_status": "resolved_authoritative_source_locator_pmid",
            "resolution_basis": (
                "one exact stable article URL identifier in source_locator matched one titled local paper metadata record"
                if stable_tokens
                else "one explicit PMID in source_locator matched one titled local paper metadata record"
            ),
            "authoritative_source": str(record.get("source_file", "")),
            "source_metadata_title": str(record.get("title", "")),
            "source_metadata_authors": str(record.get("authors", "")),
            "source_metadata_year": str(record.get("publication_year", record.get("year", ""))),
            "source_metadata_journal": str(record.get("journal", "")),
            "source_metadata_abstract": str(record.get("abstract", "")),
            "source_metadata_url": str(record.get("source_url", record.get("url", ""))),
        })

    if len({row["extraction_id"] for row in accepted}) != len(accepted):
        raise ValueError("duplicate extraction IDs in source-locator ledger")
    merged = prior.copy()
    merged.update({row["extraction_id"]: row for row in accepted})
    accepted = [merged[key] for key in sorted(merged)]
    with OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(accepted, key=lambda row: row["extraction_id"]))

    report = [
        "# Phase-2 source-locator PMID identity resolution",
        "",
        "Only unresolved rows with exactly one explicit PMID or one stable PubMed/PMC/DOI article URL identifier in source_locator were inspected.",
        "Each identifier had to match a titled local paper metadata record. Ambiguous keys additionally required the selected identifier to be explicit in the key.",
        "",
        f"- New rows with one explicit source-locator PMID or stable article URL inspected: {sum(inspected.values()):,}",
        f"- New accepted exact row-level mappings: {sum(1 for row in accepted if row['extraction_id'] not in prior):,}",
        f"- Total retained exact row-level mappings: {len(accepted):,}",
        f"- Rejected mappings: {sum(rejected.values()):,}",
        "",
        "| Module | Rows |",
        "|---|---:|",
    ]
    report.extend(f"| {module} | {count:,} |" for module, count in sorted(Counter(row["module"] for row in accepted).items()))
    report.extend(["", f"The resolver input ledger is {OUT.name}.", ""])
    REPORT.write_text("\n".join(report))
    print(f"inspected_rows={sum(inspected.values())} accepted_rows={len(accepted)} rejected={sum(rejected.values())}")
    print(dict(sorted(Counter(row["resolution_status"] for row in accepted).items())))


if __name__ == "__main__":
    main()
