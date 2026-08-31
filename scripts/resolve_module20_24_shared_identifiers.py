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
import resolve_module20_24_source_locator_pmids as local


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
    metadata = local.metadata_by_pmid()
    local_index: dict[tuple[str, str], set[str]] = {}
    for pmid, record in metadata.items():
        tokens = {("PMID", pmid)}
        if record.get("pmcid"):
            tokens.add(("PMCID", str(record["pmcid"]).upper().removeprefix("PMCID:")))
        if record.get("doi"):
            tokens.add(("DOI", str(record["doi"]).lower().removeprefix("doi:")))
        for token in tokens:
            local_index.setdefault(token, set()).add(pmid)
    prior = {
        row.get("extraction_id", ""): row
        for row in read_tsv(OUT)
        if row.get("extraction_id") and row.get("resolved_pmid")
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
            if token[0] in {"DOI", "PMCID"}
        )
        if not shared:
            continue
        inspected[row["identity_resolution_status"]] += 1
        if len(shared) != 1:
            local_pmids = [local_index.get(token, set()) for token in shared]
            if not local_pmids or not all(len(pmids) == 1 for pmids in local_pmids) or len({next(iter(pmids)) for pmids in local_pmids}) != 1:
                rejected["multiple_shared_identifiers_not_one_local_paper"] += 1
                continue
            pmid = next(iter(local_pmids[0]))
            record = metadata[pmid]
            token_text = ",".join(f"{kind}:{value}" for kind, value in shared)
            accepted.append({
                "extraction_id": row.get("extraction_id", ""),
                "module": row.get("module", ""),
                "b_evidence_id": row.get("b_evidence_id", ""),
                "canonical_paper_key": row.get("canonical_paper_key", ""),
                "source_locator": row.get("source_locator", ""),
                "resolved_pmid": pmid,
                "resolved_pmcid": str(record.get("pmcid", "")),
                "resolved_doi": str(record.get("doi", "")),
                "resolution_status": "resolved_authoritative_shared_local_identifier",
                "resolution_basis": f"all shared identifiers ({token_text}) mapped to one titled local paper metadata record",
                "authoritative_source": str(record.get("source_file", "")),
                "source_metadata_title": str(record.get("title", "")),
                "source_metadata_authors": str(record.get("authors", "")),
                "source_metadata_year": str(record.get("publication_year", record.get("year", ""))),
                "source_metadata_journal": str(record.get("journal", "")),
                "source_metadata_abstract": str(record.get("abstract", "")),
                "source_metadata_url": str(record.get("source_url", record.get("url", ""))),
            })
            continue
        token = shared[0]
        if token not in authoritative:
            local_pmids = local_index.get(token, set())
            if len(local_pmids) != 1:
                rejected["shared_identifier_not_in_unique_local_paper"] += 1
                continue
            pmid = next(iter(local_pmids))
            record = metadata[pmid]
            accepted.append({
                "extraction_id": row.get("extraction_id", ""),
                "module": row.get("module", ""),
                "b_evidence_id": row.get("b_evidence_id", ""),
                "canonical_paper_key": row.get("canonical_paper_key", ""),
                "source_locator": row.get("source_locator", ""),
                "resolved_pmid": pmid,
                "resolved_pmcid": str(record.get("pmcid", "")),
                "resolved_doi": str(record.get("doi", "")),
                "resolution_status": "resolved_authoritative_shared_local_identifier",
                "resolution_basis": f"one shared local {token[0]} identifier in canonical_paper_key and source_locator mapped to one titled local paper metadata record",
                "authoritative_source": str(record.get("source_file", "")),
                "source_metadata_title": str(record.get("title", "")),
                "source_metadata_authors": str(record.get("authors", "")),
                "source_metadata_year": str(record.get("publication_year", record.get("year", ""))),
                "source_metadata_journal": str(record.get("journal", "")),
                "source_metadata_abstract": str(record.get("abstract", "")),
                "source_metadata_url": str(record.get("source_url", record.get("url", ""))),
            })
            continue
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
    merged = prior.copy()
    merged.update({row["extraction_id"]: row for row in accepted})
    accepted = [merged[key] for key in sorted(merged)]
    with OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(accepted, key=lambda row: row["extraction_id"]))
    report = [
        "# Phase-2 shared DOI/PMCID identity resolution",
        "",
        "Only unresolved rows with shared exact DOI/PMCID identifiers in both canonical_paper_key and source_locator were accepted.",
        "A row was accepted either through one accepted exact NCBI mapping or when all shared identifiers mapped to one titled local paper metadata record; competing papers were rejected.",
        "",
        f"- Rows with shared authoritative identifier inspected: {sum(inspected.values()):,}",
        f"- New accepted exact row-level mappings: {sum(1 for row in accepted if row['extraction_id'] not in prior):,}",
        f"- Total retained exact row-level mappings: {len(accepted):,}",
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
