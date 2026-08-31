#!/usr/bin/env python3
"""Resolve bibliographic metadata for promoted source-anchor paper keys."""

from __future__ import annotations

import csv
import json
import time
from pathlib import Path
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "work" / "cross_module_synthesis" / "module20_24_canonical_paper_anchor_map.tsv"
OUTPUT = ROOT / "work" / "cross_module_synthesis" / "module20_24_canonical_paper_metadata.tsv"
REPORT = ROOT / "work" / "cross_module_synthesis" / "module20_24_canonical_paper_metadata.md"

FIELDS = [
    "canonical_paper_key", "canonical_merge_key", "paper_ready", "metadata_status",
    "title", "authors", "publication_year", "journal", "volume", "issue", "pages",
    "doi", "pmid", "pmcid", "source_metadata_url", "evidence_ids", "modules",
    "evidence_layers",
]


def fetch_json(url: str) -> dict:
    request = Request(url, headers={"User-Agent": "mSCITdb/2026 source-anchor audit"})
    with urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def chunks(items: list[str], size: int) -> list[list[str]]:
    return [items[index:index + size] for index in range(0, len(items), size)]


def normalize_doi(value: str) -> str:
    return value.removeprefix("DOI:").strip().lower()


def pubmed_summary(pmids: list[str]) -> dict[str, dict]:
    output: dict[str, dict] = {}
    for group in chunks(sorted(set(pmids)), 100):
        ids = ",".join(group)
        url = (
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
            "?db=pubmed&id=" + quote(ids) + "&retmode=json&tool=mscitdb"
        )
        payload = fetch_json(url).get("result", {})
        for pmid in payload.get("uids", []):
            output[str(pmid)] = payload.get(str(pmid), {})
        time.sleep(0.35)
    return output


def pmcid_conversion(pmcids: list[str]) -> dict[str, dict]:
    output: dict[str, dict] = {}
    for group in chunks(sorted(set(pmcids)), 100):
        ids = ",".join(group)
        url = (
            "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/"
            "?ids=" + quote(ids) + "&format=json&tool=mscitdb"
        )
        payload = fetch_json(url)
        for record in payload.get("records", []):
            requested = record.get("requested-id", "")
            output["PMCID:" + requested] = record
        time.sleep(0.35)
    return output


def pubmed_doi_search(dois: list[str]) -> dict[str, str]:
    """Resolve DOI strings through PubMed's DOI field when summaries lack DOI IDs."""
    output: dict[str, str] = {}
    for doi in sorted(set(dois)):
        url = (
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
            "?db=pubmed&term=" + quote(doi + "[doi]") + "&retmode=json&retmax=5"
        )
        try:
            payload = fetch_json(url).get("esearchresult", {})
            ids = payload.get("idlist", [])
            if len(ids) == 1:
                output[doi] = str(ids[0])
        except Exception:
            pass
        time.sleep(0.2)
    return output


def crossref_summary(dois: list[str]) -> dict[str, dict]:
    output: dict[str, dict] = {}
    for doi in sorted(set(dois)):
        url = "https://api.crossref.org/works/" + quote(doi, safe="")
        try:
            payload = fetch_json(url).get("message", {})
            output[doi] = payload
        except Exception as exc:  # keep unresolved DOI explicit
            output[doi] = {"_error": str(exc)}
        time.sleep(0.25)
    return output


def pubmed_fields(summary: dict) -> dict[str, str]:
    authors = "; ".join(author.get("name", "") for author in summary.get("authors", []) if author.get("name"))
    pubdate = summary.get("pubdate", "")
    year = pubdate[:4] if pubdate[:4].isdigit() else ""
    article_ids = {item.get("idtype"): item.get("value", "") for item in summary.get("articleids", [])}
    return {
        "title": summary.get("title", ""),
        "authors": authors,
        "publication_year": year,
        "journal": summary.get("fulljournalname") or summary.get("source", ""),
        "volume": summary.get("volume", ""),
        "issue": summary.get("issue", ""),
        "pages": summary.get("pages", ""),
        "doi": article_ids.get("doi", ""),
        "pmid": str(summary.get("uid", "")),
        "pmcid": article_ids.get("pmc", ""),
    }


def crossref_fields(message: dict) -> dict[str, str]:
    authors = "; ".join(
        " ".join(part for part in (author.get("given", ""), author.get("family", "")) if part)
        for author in message.get("author", [])
    )
    date_parts = message.get("published-print") or message.get("published-online") or message.get("issued") or {}
    parts = date_parts.get("date-parts", [[]])
    year = str(parts[0][0]) if parts and parts[0] else ""
    return {
        "title": (message.get("title") or [""])[0],
        "authors": authors,
        "publication_year": year,
        "journal": (message.get("container-title") or [""])[0],
        "volume": message.get("volume", ""),
        "issue": message.get("issue", ""),
        "pages": message.get("page", ""),
        "doi": message.get("DOI", ""),
        "pmid": "",
        "pmcid": "",
    }


def stable_url_key(value: str) -> tuple[str, str] | None:
    """Return a stable identifier represented by a URL, if one is explicit."""
    raw = value.removeprefix("URL:").strip()
    parsed = urlparse(raw)
    path = parsed.path.strip("/")
    if parsed.netloc == "pubmed.ncbi.nlm.nih.gov" and path.isdigit():
        return "PMID", path
    if parsed.netloc == "pmc.ncbi.nlm.nih.gov" and path.startswith("articles/"):
        pmcid = path.split("/", 1)[1].split("/", 1)[0]
        if pmcid.startswith("PMC"):
            return "PMCID", pmcid
    if parsed.netloc == "doi.org" and path:
        return "DOI", path.lower()
    return None


def main() -> None:
    with INPUT.open(newline="") as handle:
        anchors = list(csv.DictReader(handle, delimiter="\t"))
    pmids = [row["canonical_paper_key"].split(":", 1)[1] for row in anchors if row["canonical_paper_key"].startswith("PMID:")]
    pmcids = [row["canonical_paper_key"].split(":", 1)[1] for row in anchors if row["canonical_paper_key"].startswith("PMCID:")]
    dois = [row["canonical_paper_key"].split(":", 1)[1] for row in anchors if row["canonical_paper_key"].startswith("DOI:")]
    summaries = pubmed_summary(pmids)
    conversions = pmcid_conversion(pmcids)
    for pmcid, record in conversions.items():
        if record.get("pmid") and str(record["pmid"]) not in summaries:
            summaries[str(record["pmid"])] = pubmed_summary([str(record["pmid"])])[str(record["pmid"])]
    doi_metadata = crossref_summary(dois)
    searched_doi_pmids = pubmed_doi_search(dois)
    missing_search_pmids = [pmid for pmid in searched_doi_pmids.values() if pmid not in summaries]
    if missing_search_pmids:
        summaries.update(pubmed_summary(missing_search_pmids))
    doi_to_pubmed = {}
    for pmid, summary in summaries.items():
        fields = pubmed_fields(summary)
        if fields["doi"]:
            doi_to_pubmed[normalize_doi(fields["doi"])] = pmid
    for doi, pmid in searched_doi_pmids.items():
        doi_to_pubmed[normalize_doi(doi)] = pmid

    rows = []
    for anchor in anchors:
        key = anchor["canonical_paper_key"]
        fields = {field: "" for field in FIELDS}
        fields.update({
            "canonical_paper_key": key,
            "evidence_ids": anchor["evidence_ids"],
            "modules": anchor["modules"],
            "evidence_layers": anchor["evidence_layers"],
        })
        if key.startswith("PMID:"):
            pmid = key.split(":", 1)[1]
            fields.update(pubmed_fields(summaries.get(pmid, {})))
            fields["source_metadata_url"] = "https://pubmed.ncbi.nlm.nih.gov/" + pmid + "/"
            fields["metadata_status"] = "metadata_resolved_pubmed" if fields["title"] else "identifier_resolved_no_metadata"
            fields["canonical_merge_key"] = "PMID:" + pmid
        elif key.startswith("PMCID:"):
            pmcid = key.split(":", 1)[1]
            conversion = conversions.get(key, {})
            pmid = str(conversion.get("pmid", ""))
            fields.update(pubmed_fields(summaries.get(pmid, {})))
            fields["pmcid"] = pmcid
            fields["source_metadata_url"] = "https://pmc.ncbi.nlm.nih.gov/articles/" + pmcid + "/"
            fields["metadata_status"] = "metadata_resolved_pubmed_via_pmc" if fields["title"] else "identifier_resolved_no_metadata"
            fields["canonical_merge_key"] = "PMID:" + pmid if pmid else key
        elif key.startswith("DOI:"):
            doi = key.split(":", 1)[1]
            pmid = doi_to_pubmed.get(normalize_doi(doi), "")
            if pmid:
                fields.update(pubmed_fields(summaries[pmid]))
                fields["canonical_merge_key"] = "PMID:" + pmid
                fields["metadata_status"] = "metadata_resolved_pubmed_via_doi"
            else:
                fields.update(crossref_fields(doi_metadata.get(doi, {})))
                fields["canonical_merge_key"] = key
                fields["metadata_status"] = "metadata_resolved_crossref" if fields["title"] else "identifier_resolved_no_metadata"
            fields["doi"] = doi
            fields["source_metadata_url"] = "https://doi.org/" + doi
        else:
            stable = stable_url_key(anchor["primary_anchor_locator"])
            if stable:
                kind, identifier = stable
                stable_key = kind + ":" + identifier
                companion = next((candidate for candidate in rows if candidate["canonical_paper_key"] == stable_key), None)
                if companion and companion["title"]:
                    fields.update({
                        field: companion.get(field, "")
                        for field in ("title", "authors", "publication_year", "journal", "volume", "issue", "pages", "pmid", "pmcid")
                    })
                    fields["doi"] = companion.get("doi", "")
                    fields["canonical_merge_key"] = companion.get("canonical_merge_key", stable_key)
                    fields["metadata_status"] = "metadata_resolved_stable_url"
                    fields["source_metadata_url"] = companion.get("source_metadata_url", anchor["primary_anchor_locator"])
                else:
                    fields["canonical_merge_key"] = stable_key
                    fields["metadata_status"] = "stable_url_lookup_required"
                    fields["source_metadata_url"] = anchor["primary_anchor_locator"]
            else:
                fields["canonical_merge_key"] = key
                fields["metadata_status"] = "url_only_noncanonical"
                fields["source_metadata_url"] = anchor["primary_anchor_locator"]
        fields["paper_ready"] = "true" if fields["title"] and (fields["pmid"] or fields["pmcid"] or fields["doi"]) else "false"
        rows.append(fields)

    # DOI anchors can be malformed or duplicated in source ledgers while a
    # companion stable PMID/PMCID anchor carries the validated metadata. Use a
    # companion only when the overlapping evidence resolves to one unique
    # stable paper; ambiguous companions remain explicit unresolved cases.
    evidence_to_companions: dict[str, set[str]] = {}
    for candidate in rows:
        ckey = candidate["canonical_paper_key"]
        if ckey.startswith(("DOI:", "URL:")) or candidate["paper_ready"] != "true":
            continue
        for evidence_id in filter(None, candidate["evidence_ids"].split(";")):
            evidence_to_companions.setdefault(evidence_id, set()).add(candidate["canonical_merge_key"])
    by_merge_key = {candidate["canonical_merge_key"]: candidate for candidate in rows}
    for fields in rows:
        if not fields["canonical_paper_key"].startswith("DOI:") or fields["paper_ready"] == "true":
            continue
        candidates = set()
        for evidence_id in filter(None, fields["evidence_ids"].split(";")):
            candidates.update(evidence_to_companions.get(evidence_id, set()))
        candidates.discard(fields["canonical_merge_key"])
        if len(candidates) == 1:
            companion = by_merge_key[next(iter(candidates))]
            fields.update({
                field: companion.get(field, "")
                for field in ("title", "authors", "publication_year", "journal", "volume", "issue", "pages", "pmid", "pmcid")
            })
            fields["canonical_merge_key"] = companion["canonical_merge_key"]
            fields["source_metadata_url"] = companion["source_metadata_url"]
            fields["metadata_status"] = "metadata_resolved_companion_anchor"
            fields["paper_ready"] = "true"

    with OUTPUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    ready = sum(row["paper_ready"] == "true" for row in rows)
    statuses = {}
    for row in rows:
        statuses[row["metadata_status"]] = statuses.get(row["metadata_status"], 0) + 1
    REPORT.write_text(
        "# Module 20B–24B Canonical Paper Metadata Resolution\n\n"
        f"- Canonical paper keys audited: {len(rows):,}\n"
        f"- Paper-ready metadata rows: {ready:,}\n"
        f"- URL-only non-canonical rows: {statuses.get('url_only_noncanonical', 0):,}\n"
        "\n## Metadata status\n\n"
        "| Status | Rows |\n|---|---:|\n"
        + "\n".join(f"| {key} | {value:,} |" for key, value in sorted(statuses.items()))
        + "\n\nStable identifiers were queried through NCBI PubMed/PMC and Crossref. URL-only query anchors remain excluded from Paper candidates. This file is an audit ledger only; canonical SQL tables were not modified.\n"
    )
    print(f"paper_keys={len(rows)} paper_ready={ready}")
    print(statuses)


if __name__ == "__main__":
    main()
