#!/usr/bin/env python3
"""Audit PubMed query URLs without treating search hits as source evidence."""

from __future__ import annotations

import csv
import json
import time
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import parse_qs, quote, urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "work" / "cross_module_synthesis" / "module20_24_canonical_paper_metadata.tsv"
OUTPUT = ROOT / "work" / "cross_module_synthesis" / "module20_24_query_url_search_audit.tsv"
REPORT = ROOT / "work" / "cross_module_synthesis" / "module20_24_query_url_search_audit.md"


def fetch_json(url: str) -> dict:
    request = Request(url, headers={"User-Agent": "mSCITdb/2026 query-anchor audit"})
    with urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def search_pubmed(query: str) -> tuple[int, list[str], str]:
    url = (
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed"
        "&term=" + quote(query) + "&retmode=json&retmax=20&sort=relevance&tool=mscitdb"
    )
    for attempt in range(3):
        try:
            result = fetch_json(url).get("esearchresult", {})
            ids = [str(value) for value in result.get("idlist", [])]
            return int(result.get("count", 0)), ids, url
        except HTTPError as exc:
            if exc.code != 429 or attempt == 2:
                return -1, [], url
            time.sleep(2.0 * (attempt + 1))
        except Exception:
            return -1, [], url
    return -1, [], url


def main() -> None:
    with INPUT.open(newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    targets = [row for row in rows if row["metadata_status"] == "url_only_noncanonical"]
    results: list[dict[str, str]] = []
    for row in targets:
        locator = row["source_metadata_url"].removeprefix("URL:")
        parsed = urlparse(locator)
        query_values = parse_qs(parsed.query).get("term", [])
        if parsed.netloc == "pubmed.ncbi.nlm.nih.gov" and query_values:
            query = query_values[0]
            count, pmids, search_url = search_pubmed(query)
            if count < 0:
                status = "search_failed_bounded"
            elif count == 0:
                status = "no_pubmed_hit"
            else:
                status = "candidate_hits_unpromoted"
            results.append({
                "source_key": row["canonical_paper_key"],
                "evidence_ids": row["evidence_ids"],
                "locator": locator,
                "query": query,
                "result_count": str(count),
                "top_pmids": ";".join(pmids),
                "search_url": search_url,
                "status": status,
            })
            time.sleep(0.45)
        else:
            results.append({
                "source_key": row["canonical_paper_key"],
                "evidence_ids": row["evidence_ids"],
                "locator": locator,
                "query": "",
                "result_count": "",
                "top_pmids": "",
                "search_url": "",
                "status": "non-query_url_requires_manual_source_review",
            })

    fields = ["source_key", "evidence_ids", "locator", "query", "result_count", "top_pmids", "search_url", "status"]
    with OUTPUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(results)
    counts: dict[str, int] = {}
    for row in results:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    REPORT.write_text(
        "# Module 20B–24B Query-URL Search Audit\n\n"
        f"- URL-only anchors audited: {len(results):,}\n"
        + "\n".join(f"- `{status}`: {count:,}" for status, count in sorted(counts.items()))
        + "\n\nPubMed search results are candidate discovery only. They were not promoted to canonical Paper/Observation evidence without a stable paper identifier and source-specific validation. Non-query URLs remain explicit manual-review cases.\n"
    )
    print(f"audited={len(results)}")
    print(counts)


if __name__ == "__main__":
    main()
