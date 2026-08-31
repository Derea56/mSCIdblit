#!/usr/bin/env python3
"""Resolve one-shared DOI/PMCID extraction rows through NCBI.

This lane is intentionally limited to unresolved rows where exactly one
non-PMID identifier is shared by canonical_paper_key and source_locator. NCBI
must map that exact DOI/PMCID to one titled PubMed record. Rows with multiple
shared identifiers are handled only when a separate exact same-paper rule
establishes their relationship; they are not collapsed here.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

import resolve_module20_24_phase2_paper_identities as base
import resolve_module20_24_source_locator_ncbi as ncbi_lane


ROOT = Path(__file__).resolve().parents[1]
REVIEW_ROOT = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review"
INPUT = REVIEW_ROOT / "module20_24_phase2_paper_identity_resolution.tsv"
OUT = REVIEW_ROOT / "module20_24_phase2_paper_identity_shared_identifier_ncbi_resolutions.tsv"
REPORT = REVIEW_ROOT / "module20_24_phase2_paper_identity_shared_identifier_ncbi_resolutions.md"

FIELDS = [
    "extraction_id", "module", "b_evidence_id", "canonical_paper_key",
    "source_locator", "resolved_pmid", "resolved_pmcid", "resolved_doi",
    "resolution_status", "resolution_basis", "authoritative_source",
    "source_metadata_title", "source_metadata_authors", "source_metadata_year",
    "source_metadata_journal", "source_metadata_abstract", "source_metadata_url",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def main() -> None:
    phase_rows = {
        row.get("extraction_id", ""): row
        for row in read_tsv(INPUT)
        if row.get("extraction_id")
    }
    prior = {
        row.get("extraction_id", ""): row
        for row in read_tsv(OUT)
        if row.get("extraction_id")
        and row.get("resolved_pmid")
        and not (
            phase_rows.get(row.get("extraction_id", ""), {}).get("identity_resolution_status")
            == "unresolved_ambiguous_multiple_canonical_pmids"
            and row.get("resolved_pmid") not in {
                value
                for kind, value in base.all_tokens(
                    phase_rows.get(row.get("extraction_id", ""), {}).get("canonical_paper_key", "")
                )
                if kind == "PMID"
            }
        )
    }
    accepted: list[dict[str, str]] = []
    cache: dict[tuple[str, str], tuple[dict[str, str] | None, str, str]] = {}
    inspected = Counter()
    rejected = Counter()

    for row in read_tsv(INPUT):
        status = row.get("identity_resolution_status", "")
        if not status.startswith("unresolved_"):
            continue
        key_tokens = base.all_tokens(row.get("canonical_paper_key", ""))
        locator_tokens = base.all_tokens(row.get("source_locator", ""))
        shared = sorted(token for token in key_tokens & locator_tokens if token[0] in {"DOI", "PMCID"})
        if len(shared) != 1:
            continue
        token = shared[0]
        inspected[status] += 1
        cache.setdefault(token, ncbi_lane.resolve_token(token))
        record, source, reason = cache[token]
        if record is None:
            rejected[reason] += 1
            continue
        if status == "unresolved_ambiguous_multiple_canonical_pmids":
            key_pmids = {
                value for kind, value in key_tokens if kind == "PMID"
            }
            if record["pmid"] not in key_pmids:
                rejected["resolved_pmid_not_explicit_in_ambiguous_key"] += 1
                continue
        accepted.append({
            "extraction_id": row.get("extraction_id", ""),
            "module": row.get("module", ""),
            "b_evidence_id": row.get("b_evidence_id", ""),
            "canonical_paper_key": row.get("canonical_paper_key", ""),
            "source_locator": row.get("source_locator", ""),
            "resolved_pmid": record["pmid"],
            "resolved_pmcid": record["pmcid"],
            "resolved_doi": record["doi"],
            "resolution_status": "resolved_authoritative_shared_identifier_ncbi",
            "resolution_basis": f"one shared {token[0]} identifier in canonical_paper_key and source_locator mapped uniquely to a titled PubMed record through NCBI",
            "authoritative_source": source,
            "source_metadata_title": record["source_metadata_title"],
            "source_metadata_authors": record["source_metadata_authors"],
            "source_metadata_year": record["source_metadata_year"],
            "source_metadata_journal": record["source_metadata_journal"],
            "source_metadata_abstract": record["source_metadata_abstract"],
            "source_metadata_url": record["source_metadata_url"],
        })

    if len({row["extraction_id"] for row in accepted}) != len(accepted):
        raise ValueError("duplicate extraction IDs in NCBI shared-identifier ledger")
    merged = prior.copy()
    merged.update({row["extraction_id"]: row for row in accepted})
    retained = [merged[key] for key in sorted(merged)]
    with OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writeheader()
        writer.writerows(retained)

    report = [
        "# Phase-2 shared DOI/PMCID NCBI identity resolution",
        "",
        "Only unresolved rows with exactly one shared DOI or PMCID in canonical_paper_key and source_locator were inspected.",
        "NCBI established one PMID and a titled PubMed record before acceptance. Rows with multiple shared identifiers were not collapsed in this lane.",
        "",
        f"- New eligible rows inspected: {sum(inspected.values()):,}",
        f"- New accepted mappings: {sum(1 for row in retained if row['extraction_id'] not in prior):,}",
        f"- Total retained mappings: {len(retained):,}",
        f"- Unique shared identifiers queried: {len(cache):,}",
        f"- Rejected or unresolved candidates: {sum(rejected.values()):,}",
        "",
        "| Module | Rows |",
        "|---|---:|",
    ]
    report.extend(f"| {module} | {count:,} |" for module, count in sorted(Counter(row["module"] for row in retained).items()))
    report.extend(["", f"The resolver input ledger is {OUT.name}.", ""])
    REPORT.write_text("\n".join(report))
    print(f"inspected_rows={sum(inspected.values())} new_accepted_rows={sum(1 for row in retained if row['extraction_id'] not in prior)} retained_rows={len(retained)} rejected={sum(rejected.values())}")


if __name__ == "__main__":
    main()
