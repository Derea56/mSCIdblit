#!/usr/bin/env python3
"""Resolve exact stable source-locator identifiers through NCBI.

This lane handles unresolved extraction rows whose source_locator contains one
stable PubMed, PMC, or DOI article URL, but whose matching paper is absent from
the local metadata cache. The URL identifier must be exact and, for an
ambiguous canonical key, must also be listed in that key. NCBI must establish
one PMID and a titled PubMed record before the row is accepted.
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
OUT = REVIEW_ROOT / "module20_24_phase2_paper_identity_source_locator_ncbi_resolutions.tsv"
REPORT = REVIEW_ROOT / "module20_24_phase2_paper_identity_source_locator_ncbi_resolutions.md"

FIELDS = [
    "extraction_id", "module", "b_evidence_id", "canonical_paper_key",
    "source_locator", "resolved_pmid", "resolved_pmcid", "resolved_doi",
    "resolution_status", "resolution_basis", "authoritative_source",
    "source_metadata_title", "source_metadata_authors", "source_metadata_year",
    "source_metadata_journal", "source_metadata_abstract", "source_metadata_url",
]

URL_RE = re.compile(r"https?://[^;\s]+", re.IGNORECASE)


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def stable_locator_tokens(value: str) -> set[tuple[str, str]]:
    return {
        token
        for url in URL_RE.findall(value or "")
        for token in base.stable_url_tokens(url)
    }


def normalize_pmc(value: str) -> str:
    match = re.search(r"PMC\d+", value or "", re.IGNORECASE)
    return match.group(0).upper() if match else ""


def summary_record(pmid: str, summary: dict) -> dict[str, str] | None:
    title = str(summary.get("title", "")).strip()
    if not title:
        return None
    ids = ncbi.article_ids(summary)
    pmcid = ids.get("pmcid", "") or ids.get("pmc", "")
    pmcid = normalize_pmc(pmcid) if pmcid.upper().startswith("PMC") else ""
    doi = ncbi.normalize_doi(ids.get("doi", ""))
    fields = ncbi.metadata_fields(summary, pmid)
    return {
        "pmid": pmid,
        "pmcid": pmcid,
        "doi": doi,
        **fields,
        "source_metadata_abstract": "",
    }


def resolve_token(token: tuple[str, str]) -> tuple[dict[str, str] | None, str, str]:
    kind, value = token
    pmid = ""
    source: list[str] = []
    if kind == "PMID":
        pmid = value
        source.append("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi")
    elif kind == "PMCID":
        mappings, errors = ncbi.pmcid_mappings([value])
        record = mappings.get(value)
        if record is None or not str(record.get("pmid", "")):
            return None, ";".join(source), errors.get(value, "NCBI ID converter returned no PMID")
        pmid = str(record["pmid"])
        source.extend([
            "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/",
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi",
        ])
    elif kind == "DOI":
        matches, errors = ncbi.doi_pmids([value])
        pmids = matches.get(value, [])
        if len(pmids) != 1:
            return None, "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi", errors.get(value, f"exact DOI search returned {len(pmids)} PMIDs")
        pmid = pmids[0]
        source.extend([
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi",
        ])
    else:
        return None, "", f"unsupported stable locator identifier type: {kind}"

    summaries = ncbi.summaries([pmid])
    summary = summaries.get(pmid)
    if summary is None:
        return None, ";".join(source), "NCBI returned no PubMed summary for the exact PMID"
    record = summary_record(pmid, summary)
    if record is None:
        return None, ";".join(source), "NCBI PubMed summary has no titled article record"
    # A correction record is not the evidentiary primary paper. When NCBI
    # explicitly links one correction to one original article, use that
    # original PMID while preserving both the stable URL and NCBI relation in
    # the resolution basis.
    pubtypes = {str(value).lower() for value in summary.get("pubtype", [])}
    originals = sorted({
        str(reference.get("pmid", ""))
        for reference in summary.get("references", [])
        if str(reference.get("reftype", "")).lower() in {"erratum for", "correction for"}
        and str(reference.get("pmid", "")).isdigit()
    })
    if "published erratum" in pubtypes and len(originals) == 1:
        original_pmid = originals[0]
        original_summary = ncbi.summaries([original_pmid]).get(original_pmid)
        original_record = summary_record(original_pmid, original_summary or {})
        if original_record is not None:
            original_record["_resolution_note"] = (
                f"NCBI identifies source PMID:{pmid} as an erratum for PMID:{original_pmid}; "
                "the original article is used for the evidence record"
            )
            original_record["_source"] = ";".join(source)
            return original_record, original_record["_source"], ""
    record["_source"] = ";".join(source)
    return record, record["_source"], ""


def main() -> None:
    rows = read_tsv(INPUT)
    prior = {
        row.get("extraction_id", ""): row
        for row in read_tsv(OUT)
        if row.get("extraction_id") and row.get("resolved_pmid")
    }
    cache: dict[tuple[str, str], tuple[dict[str, str] | None, str, str]] = {}
    accepted: list[dict[str, str]] = []
    inspected = Counter()
    rejected = Counter()

    for row in rows:
        status = row.get("identity_resolution_status", "")
        if status not in {
            "unresolved_ambiguous_multiple_canonical_pmids",
            "unresolved_missing_canonical_identity",
            "unresolved_no_authoritative_resolution",
        }:
            continue
        stable = stable_locator_tokens(row.get("source_locator", ""))
        if len(stable) != 1:
            continue
        token = next(iter(stable))
        key_tokens = base.all_tokens(row.get("canonical_paper_key", ""))
        if key_tokens and token not in key_tokens:
            rejected["stable_locator_identifier_not_explicit_in_key"] += 1
            continue
        if status == "unresolved_ambiguous_multiple_canonical_pmids" and token[0] != "PMID":
            # A non-PMID stable URL can select the paper only when the exact
            # PMCID/DOI itself is listed in the ambiguous key.
            if token not in key_tokens:
                rejected["ambiguous_stable_identifier_not_explicit_in_key"] += 1
                continue
        inspected[status] += 1
        cache.setdefault(token, resolve_token(token))
        record, source, reason = cache[token]
        if record is None:
            rejected[reason] += 1
            continue
        basis = f"one exact stable {token[0]} identifier in source_locator mapped uniquely to a titled PubMed record through NCBI"
        if record.get("_resolution_note"):
            basis += f"; {record['_resolution_note']}"
        accepted.append({
            "extraction_id": row.get("extraction_id", ""),
            "module": row.get("module", ""),
            "b_evidence_id": row.get("b_evidence_id", ""),
            "canonical_paper_key": row.get("canonical_paper_key", ""),
            "source_locator": row.get("source_locator", ""),
            "resolved_pmid": record["pmid"],
            "resolved_pmcid": record["pmcid"],
            "resolved_doi": record["doi"],
            "resolution_status": "resolved_authoritative_source_locator_ncbi",
            "resolution_basis": basis,
            "authoritative_source": source,
            "source_metadata_title": record["source_metadata_title"],
            "source_metadata_authors": record["source_metadata_authors"],
            "source_metadata_year": record["source_metadata_year"],
            "source_metadata_journal": record["source_metadata_journal"],
            "source_metadata_abstract": record["source_metadata_abstract"],
            "source_metadata_url": record["source_metadata_url"],
        })

    if len({row["extraction_id"] for row in accepted}) != len(accepted):
        raise ValueError("duplicate extraction IDs in NCBI source-locator ledger")
    merged = prior.copy()
    merged.update({row["extraction_id"]: row for row in accepted})
    retained = [merged[key] for key in sorted(merged)]
    with OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writeheader()
        writer.writerows(retained)

    report = [
        "# Phase-2 source-locator NCBI identity resolution",
        "",
        "Only rows with one exact stable PubMed, PMC, or DOI article URL identifier were inspected.",
        "The identifier had to be explicit in a non-empty canonical key; ambiguous keys were never collapsed by semantic similarity.",
        "NCBI established one PMID and a titled PubMed record before acceptance.",
        "",
        f"- New eligible rows inspected: {sum(inspected.values()):,}",
        f"- New accepted mappings: {sum(1 for row in retained if row['extraction_id'] not in prior):,}",
        f"- Total retained mappings: {len(retained):,}",
        f"- Unique stable identifiers queried: {len(cache):,}",
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
