#!/usr/bin/env python3
"""Resolve the first Phase-2 identity-exception lane through NCBI only.

This pass is deliberately narrow: it considers unresolved rows whose
canonical key contains exactly one PMCID or DOI.  PMCID-to-PMID mappings are
accepted only from NCBI's PMC ID converter.  DOI-to-PMID mappings are accepted
only from an exact PubMed DOI-field search followed by an article-summary
check that contains the same DOI.  Zero, multiple, failed, or mismatched
results remain unresolved in the output ledger.

The output is an evidence ledger consumed by the Phase-2 identity resolver;
it never changes the source extraction key or the database directly.
"""

from __future__ import annotations

import csv
import json
import re
import time
from collections import defaultdict
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
REVIEW_ROOT = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review"
EXCEPTIONS = REVIEW_ROOT / "module20_24_phase2_paper_identity_exceptions_summary.tsv"
OUT = REVIEW_ROOT / "module20_24_phase2_paper_identity_authoritative_resolutions.tsv"
REPORT = REVIEW_ROOT / "module20_24_phase2_paper_identity_authoritative_resolutions.md"

FIELDS = [
    "identifier_type", "identifier_value", "canonical_identifier",
    "resolved_pmid", "resolved_pmcid", "resolved_doi",
    "resolution_status", "resolution_basis", "authoritative_source",
    "source_metadata_title", "source_metadata_authors", "source_metadata_year",
    "source_metadata_journal", "source_metadata_url", "resolution_reason",
]

ID_RE = re.compile(
    r"(?i)\bPMID\s*:\s*(?P<pmid>\d+)\b|"
    r"\bPMCID\s*:\s*(?P<pmcid>PMC\d+)\b|"
    r"\bDOI\s*:\s*(?P<doi>10\.\S+?)(?=;|\s|$)"
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def normalize_doi(value: str) -> str:
    return value.strip().removeprefix("DOI:").rstrip(".,)").lower()


def identifiers(value: str) -> list[tuple[str, str]]:
    output = []
    for match in ID_RE.finditer(value or ""):
        if match.group("pmid"):
            output.append(("PMID", match.group("pmid")))
        elif match.group("pmcid"):
            output.append(("PMCID", match.group("pmcid").upper()))
        elif match.group("doi"):
            output.append(("DOI", normalize_doi(match.group("doi"))))
    return output


def fetch_json(url: str) -> dict:
    request = Request(url, headers={"User-Agent": "mSCITdb/2026 identity-exception audit"})
    with urlopen(request, timeout=45) as response:
        return json.loads(response.read().decode("utf-8"))


def query_json(url: str) -> tuple[dict | None, str]:
    for attempt in range(4):
        try:
            return fetch_json(url), ""
        except HTTPError as exc:
            if exc.code == 429 and attempt < 3:
                time.sleep(2.0 * (attempt + 1))
                continue
            return None, f"HTTP {exc.code}"
        except (URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
            if attempt < 3:
                time.sleep(1.0 * (attempt + 1))
                continue
            return None, str(exc)
    return None, "query failed after retries"


def chunks(values: list[str], size: int) -> list[list[str]]:
    return [values[index:index + size] for index in range(0, len(values), size)]


def pmcid_mappings(pmcids: list[str]) -> tuple[dict[str, dict], dict[str, str]]:
    mappings: dict[str, dict] = {}
    errors: dict[str, str] = {}
    for group in chunks(sorted(set(pmcids)), 100):
        url = (
            "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids="
            + quote(",".join(group))
            + "&format=json&tool=mscitdb"
        )
        payload, error = query_json(url)
        if payload is None:
            errors.update({pmcid: error for pmcid in group})
            continue
        returned = {str(record.get("requested-id", "")).upper(): record for record in payload.get("records", [])}
        for pmcid in group:
            record = returned.get(pmcid)
            if record is None:
                errors[pmcid] = "NCBI ID converter returned no record"
            else:
                mappings[pmcid] = record
        time.sleep(0.35)
    return mappings, errors


def doi_pmids(dois: list[str]) -> tuple[dict[str, list[str]], dict[str, str]]:
    matches: dict[str, list[str]] = {}
    errors: dict[str, str] = {}
    for doi in sorted(set(dois)):
        query = quote(f"{doi}[doi]", safe="[]")
        url = (
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
            "?db=pubmed&term=" + query + "&retmode=json&retmax=5&tool=mscitdb"
        )
        payload, error = query_json(url)
        if payload is None:
            errors[doi] = error
        else:
            matches[doi] = [str(value) for value in payload.get("esearchresult", {}).get("idlist", [])]
        time.sleep(0.35)
    return matches, errors


def summaries(pmids: list[str]) -> dict[str, dict]:
    output: dict[str, dict] = {}
    for group in chunks(sorted(set(pmids)), 100):
        url = (
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
            "?db=pubmed&id=" + quote(",".join(group)) + "&retmode=json&tool=mscitdb"
        )
        payload, error = query_json(url)
        if payload is not None:
            result = payload.get("result", {})
            for pmid in result.get("uids", []):
                output[str(pmid)] = result.get(str(pmid), {})
        time.sleep(0.35)
    return output


def article_ids(summary: dict) -> dict[str, str]:
    return {
        str(item.get("idtype", "")).lower(): str(item.get("value", ""))
        for item in summary.get("articleids", [])
        if item.get("value")
    }


def metadata_fields(summary: dict, pmid: str) -> dict[str, str]:
    authors = "; ".join(
        str(author.get("name", ""))
        for author in summary.get("authors", [])
        if author.get("name")
    )
    pubdate = str(summary.get("pubdate", ""))
    return {
        "source_metadata_title": str(summary.get("title", "")),
        "source_metadata_authors": authors,
        "source_metadata_year": pubdate[:4] if pubdate[:4].isdigit() else "",
        "source_metadata_journal": str(summary.get("fulljournalname") or summary.get("source", "")),
        "source_metadata_url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
    }


def base_row(kind: str, value: str) -> dict[str, str]:
    return {
        field: "" for field in FIELDS
    } | {
        "identifier_type": kind,
        "identifier_value": value,
        "canonical_identifier": f"{kind}:{value}",
    }


def write_tsv(rows: list[dict[str, str]]) -> None:
    with OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    prior = {
        (row.get("identifier_type", ""), row.get("identifier_value", "")): row
        for row in read_tsv(OUT)
        if row.get("identifier_type") and row.get("identifier_value")
    }
    summary_rows = read_tsv(EXCEPTIONS)
    selected: dict[tuple[str, str], set[str]] = defaultdict(set)
    for row in summary_rows:
        if row.get("identity_resolution_status") != "unresolved_no_authoritative_resolution":
            continue
        tokens = identifiers(row.get("canonical_paper_key", ""))
        if len(tokens) == 1 and tokens[0][0] in {"DOI", "PMCID"}:
            selected[tokens[0]].update(row.get("extraction_ids", "").split(";") if row.get("extraction_ids") else [])

    pmcids = [value for kind, value in selected if kind == "PMCID"]
    dois = [value for kind, value in selected if kind == "DOI"]
    pmc_map, pmc_errors = pmcid_mappings(pmcids)
    doi_map, doi_errors = doi_pmids(dois)
    candidate_pmids = [str(record.get("pmid", "")) for record in pmc_map.values() if str(record.get("pmid", ""))]
    candidate_pmids.extend(pmid for values in doi_map.values() for pmid in values)
    summary_map = summaries(candidate_pmids)

    rows: list[dict[str, str]] = []
    for kind, value in sorted(selected):
        row = base_row(kind, value)
        pmid = ""
        basis = ""
        source = ""
        reason = ""
        if kind == "PMCID":
            record = pmc_map.get(value)
            if record is None:
                row["resolution_status"] = "unresolved_ncbi_query_error"
                row["resolution_reason"] = pmc_errors.get(value, "NCBI ID converter did not establish a mapping")
            elif str(record.get("pmid", "")):
                pmid = str(record["pmid"])
                basis = "exact NCBI PMC ID converter PMCID-to-PMID mapping"
                source = "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/"
                row["resolved_pmcid"] = value
            else:
                row["resolution_status"] = "unresolved_ncbi_no_pmid_mapping"
                row["resolution_reason"] = "NCBI ID converter returned no PMID for the exact PMCID"
        else:
            values = doi_map.get(value, [])
            if value in doi_errors:
                row["resolution_status"] = "unresolved_ncbi_query_error"
                row["resolution_reason"] = doi_errors[value]
            elif len(values) != 1:
                row["resolution_status"] = "unresolved_ncbi_nonunique_doi_match"
                row["resolution_reason"] = f"exact PubMed DOI-field search returned {len(values)} PMIDs"
            else:
                pmid = values[0]
                summary = summary_map.get(pmid, {})
                ids = article_ids(summary)
                returned_doi = normalize_doi(ids.get("doi", ""))
                if returned_doi != value:
                    row["resolution_status"] = "unresolved_ncbi_identifier_mismatch"
                    row["resolution_reason"] = "PubMed summary did not contain the exact queried DOI"
                else:
                    basis = "exact PubMed DOI-field search with matching PubMed article DOI"
                    source = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        if pmid:
            summary = summary_map.get(pmid, {})
            ids = article_ids(summary)
            row.update(metadata_fields(summary, pmid))
            row["resolved_pmid"] = pmid
            row["resolved_pmcid"] = row["resolved_pmcid"] or ids.get("pmc", "")
            row["resolved_doi"] = ids.get("doi", "")
            row["resolution_status"] = "resolved_authoritative_ncbi"
            row["resolution_basis"] = basis
            row["authoritative_source"] = source
        rows.append(row)

    merged = prior.copy()
    merged.update({(row["identifier_type"], row["identifier_value"]): row for row in rows})
    rows = [merged[key] for key in sorted(merged)]
    write_tsv(rows)
    counts = defaultdict(int)
    for row in rows:
        counts[row["resolution_status"]] += 1
    report = [
        "# Phase-2 authoritative identity-exception resolution",
        "",
        "This pass evaluates only unresolved groups with exactly one PMCID or DOI in the canonical key.",
        "NCBI is used as the authoritative source. Only exact, unique, metadata-checked mappings are accepted.",
        "The ledger is an input to the identity resolver; it does not overwrite source extraction keys.",
        "",
        f"- Candidate identifier groups: {len(rows):,}",
        f"- Candidate extraction rows: {sum(len(selected[key]) for key in selected):,}",
        f"- Resolved authoritative mappings: {sum(1 for row in rows if row['resolved_pmid']):,}",
        f"- Unresolved mappings: {sum(1 for row in rows if not row['resolved_pmid']):,}",
        "",
        "## Result status",
        "",
        "| Status | Groups |",
        "|---|---:|",
    ]
    report.extend(f"| {status} | {count:,} |" for status, count in sorted(counts.items()))
    report.extend([
        "",
        f"The resolver input ledger is {OUT.name}.",
        "Rows without a unique, exact NCBI mapping remain unresolved and continue in the exception queue.",
        "",
    ])
    REPORT.write_text("\n".join(report))
    print(f"candidate_groups={len(rows)} resolved={sum(1 for row in rows if row['resolved_pmid'])} unresolved={sum(1 for row in rows if not row['resolved_pmid'])}")
    print(dict(sorted(counts.items())))


if __name__ == "__main__":
    main()
