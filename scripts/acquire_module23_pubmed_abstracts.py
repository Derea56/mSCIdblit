#!/usr/bin/env python3
"""Acquire PubMed XML abstracts for unresolved Module 23 paper anchors.

The PMID list is taken from the complete Module 23 extraction inventory. The
script stores one source XML artifact per PMID and writes a checksummed
manifest. It does not infer paper identity, full-text availability, or
biological support.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "work/module_b_consolidation/module23b/module23_all_paper_extraction_inventory_2026-09-05.tsv"
DEFAULT_OUTPUT_ROOT = ROOT / "data/raw/evidence/module23_pubmed_abstracts_20260905"
DEFAULT_MANIFEST = DEFAULT_OUTPUT_ROOT / "acquisition_manifest.tsv"
FIELDS = ["pmid", "local_path", "retrieval_status", "retrieval_method", "retrieved_at_utc", "sha256", "title"]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def title_for(article: ET.Element) -> str:
    title = article.findtext(".//ArticleTitle", default="")
    return " ".join(title.split())


def pmid_for(article: ET.Element) -> str:
    return "".join(article.findtext(".//MedlineCitation/PMID", default="").split())


def fetch_batch(pmids: list[str], timeout: int) -> dict[str, ET.Element]:
    params = urlencode({"db": "pubmed", "id": ",".join(pmids), "rettype": "abstract", "retmode": "xml"})
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?{params}"
    request = Request(url, headers={"User-Agent": "mSCIdblit-module23-pubmed-acquisition/1.0"})
    with urlopen(request, timeout=timeout) as response:
        root = ET.fromstring(response.read())
    return {pmid_for(article): article for article in root.findall(".//PubmedArticle") if pmid_for(article)}


def build(inventory: Path, output_root: Path, manifest: Path, batch_size: int, sleep_seconds: float, timeout: int, limit: int | None) -> None:
    rows = read_tsv(inventory)
    requested = sorted({
        row["paper_anchor"].split(":", 1)[1]
        for row in rows
        if row["anchor_type"] == "PMID" and row["paper_extraction_status"] == "awaiting_local_source_acquisition"
    })
    if limit is not None:
        requested = requested[:limit]
    output_root.mkdir(parents=True, exist_ok=True)
    existing: dict[str, dict[str, str]] = {}
    if manifest.exists():
        existing = {row["pmid"]: row for row in read_tsv(manifest)}
    records: dict[str, dict[str, str]] = {}
    now = datetime.now(timezone.utc).isoformat()
    for start in range(0, len(requested), batch_size):
        batch = requested[start : start + batch_size]
        pending = [pmid for pmid in batch if not (output_root / f"PMID_{pmid}_pubmed.xml").is_file()]
        fetched: dict[str, ET.Element] = {}
        if pending:
            try:
                fetched = fetch_batch(pending, timeout)
            except Exception as error:  # retain explicit failures for retry
                for pmid in pending:
                    records[pmid] = {
                        "pmid": pmid,
                        "local_path": f"data/raw/evidence/module23_pubmed_abstracts_20260905/PMID_{pmid}_pubmed.xml",
                        "retrieval_status": f"fetch_failed:{type(error).__name__}",
                        "retrieval_method": "ncbi_pubmed_efetch_xml",
                        "retrieved_at_utc": now,
                        "sha256": "",
                        "title": "",
                    }
            else:
                for pmid, article in fetched.items():
                    path = output_root / f"PMID_{pmid}_pubmed.xml"
                    path.write_bytes(ET.tostring(article, encoding="utf-8", xml_declaration=True))
                    records[pmid] = {
                        "pmid": pmid,
                        "local_path": f"data/raw/evidence/module23_pubmed_abstracts_20260905/PMID_{pmid}_pubmed.xml",
                        "retrieval_status": "fetched",
                        "retrieval_method": "ncbi_pubmed_efetch_xml",
                        "retrieved_at_utc": now,
                        "sha256": sha256(path),
                        "title": title_for(article),
                    }
                for pmid in set(pending) - set(fetched):
                    records[pmid] = {
                        "pmid": pmid,
                        "local_path": f"data/raw/evidence/module23_pubmed_abstracts_20260905/PMID_{pmid}_pubmed.xml",
                        "retrieval_status": "not_returned_by_ncbi",
                        "retrieval_method": "ncbi_pubmed_efetch_xml",
                        "retrieved_at_utc": now,
                        "sha256": "",
                        "title": "",
                    }
        for pmid in batch:
            path = output_root / f"PMID_{pmid}_pubmed.xml"
            if pmid not in records and path.is_file():
                records[pmid] = {
                    "pmid": pmid,
                    "local_path": f"data/raw/evidence/module23_pubmed_abstracts_20260905/PMID_{pmid}_pubmed.xml",
                    "retrieval_status": "cached",
                    "retrieval_method": "ncbi_pubmed_efetch_xml",
                    "retrieved_at_utc": existing.get(pmid, {}).get("retrieved_at_utc", now),
                    "sha256": sha256(path),
                    "title": existing.get(pmid, {}).get("title", ""),
                }
        time.sleep(sleep_seconds)
    for pmid, row in existing.items():
        if pmid not in records and pmid in requested:
            records[pmid] = row
    with manifest.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(records[pmid] for pmid in sorted(records))
    counts: dict[str, int] = {}
    for row in records.values():
        counts[row["retrieval_status"]] = counts.get(row["retrieval_status"], 0) + 1
    print(f"requested_pmids={len(requested)} manifest_rows={len(records)} statuses={dict(sorted(counts.items()))}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", type=Path, default=INVENTORY)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--batch-size", type=int, default=100)
    parser.add_argument("--sleep", type=float, default=0.5)
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()
    build(args.inventory, args.output_root, args.manifest, args.batch_size, args.sleep, args.timeout, args.limit)


if __name__ == "__main__":
    main()
