#!/usr/bin/env python3
"""Acquire metadata and any publisher-supplied abstract for unresolved Module 23 DOI anchors."""

from __future__ import annotations

import argparse
import csv
import hashlib
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "work/module_b_consolidation/module23b/module23_all_paper_extraction_inventory_2026-09-05.tsv"
DEFAULT_OUTPUT_ROOT = ROOT / "data/raw/evidence/module23_doi_metadata_20260905"
DEFAULT_MANIFEST = DEFAULT_OUTPUT_ROOT / "acquisition_manifest.tsv"
FIELDS = ["doi", "local_path", "retrieval_status", "retrieval_method", "retrieved_at_utc", "sha256"]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_name(doi: str) -> str:
    return "DOI_" + hashlib.sha256(doi.encode("utf-8")).hexdigest()[:16] + ".json"


def curl(url: str, timeout: int, accept: str) -> bytes:
    result = subprocess.run(
        [
            "curl", "-L", "--fail", "--silent", "--show-error",
            "--max-time", str(timeout),
            "-H", f"Accept: {accept}",
            "-H", "User-Agent: mSCIdblit-module23-doi-acquisition/1.0",
            url,
        ],
        check=True,
        capture_output=True,
    )
    return result.stdout


def fetch(doi: str, timeout: int) -> tuple[bytes, str, str]:
    url = "https://api.crossref.org/works/" + quote(doi, safe="")
    try:
        body = curl(url, timeout, "application/json")
        if not body.strip().startswith(b"{"):
            raise ValueError("Crossref response was not JSON")
        return body, "crossref_works_api", "json"
    except Exception as crossref_error:
        # DOI metadata is incomplete for some older records. Try an exact
        # PubMed DOI search before leaving the identifier unresolved.
        search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=" + quote(f"{doi}[doi]", safe="")
        search_body = curl(search_url, timeout, "application/xml")
        root = ET.fromstring(search_body)
        pmid = next((node.text for node in root.findall(".//Id") if node.text), None)
        if not pmid:
            raise crossref_error
        fetch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml"
        pubmed_body = curl(fetch_url, timeout, "application/xml")
        ET.fromstring(pubmed_body)
        return pubmed_body, "ncbi_pubmed_doi_search", "xml"


def build(inventory: Path, output_root: Path, manifest: Path, sleep_seconds: float, timeout: int, limit: int | None) -> None:
    rows = read_tsv(inventory)
    requested = sorted({
        row["paper_anchor"].split(":", 1)[1].lower()
        for row in rows
        if row["anchor_type"] == "DOI" and row["paper_extraction_status"] == "awaiting_local_source_acquisition"
    })
    if limit is not None:
        requested = requested[:limit]
    output_root.mkdir(parents=True, exist_ok=True)
    existing = {row["doi"]: row for row in read_tsv(manifest)} if manifest.exists() else {}
    records: dict[str, dict[str, str]] = {
        doi: row for doi, row in existing.items()
        if (output_root / Path(row.get("local_path", "")).name).is_file()
    }
    for doi in requested:
        existing_paths = [
            output_root / safe_name(doi),
            output_root / f"{safe_name(doi).removesuffix('.json')}.xml",
        ]
        path = next((candidate for candidate in existing_paths if candidate.is_file() and candidate.stat().st_size), existing_paths[0])
        now = datetime.now(timezone.utc).isoformat()
        if path.is_file() and path.stat().st_size:
            records[doi] = {
                "doi": doi,
                "local_path": f"data/raw/evidence/module23_doi_metadata_20260905/{path.name}",
                "retrieval_status": "cached",
                "retrieval_method": existing.get(doi, {}).get("retrieval_method", "crossref_works_api"),
                "retrieved_at_utc": existing.get(doi, {}).get("retrieved_at_utc", now),
                "sha256": sha256(path),
            }
            continue
        try:
            body, method, suffix = fetch(doi, timeout)
            path = output_root / f"{safe_name(doi).removesuffix('.json')}.{suffix}"
            path.write_bytes(body)
        except Exception as error:
            records[doi] = {
                "doi": doi,
                "local_path": f"data/raw/evidence/module23_doi_metadata_20260905/{path.name}",
                "retrieval_status": f"fetch_failed:{type(error).__name__}",
                "retrieval_method": "crossref_works_api",
                "retrieved_at_utc": now,
                "sha256": "",
            }
        else:
            records[doi] = {
                "doi": doi,
                "local_path": f"data/raw/evidence/module23_doi_metadata_20260905/{path.name}",
                "retrieval_status": "fetched",
                "retrieval_method": method,
                "retrieved_at_utc": now,
                "sha256": sha256(path),
            }
        time.sleep(sleep_seconds)
    with manifest.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(records[doi] for doi in sorted(records))
    counts: dict[str, int] = {}
    for row in records.values():
        counts[row["retrieval_status"]] = counts.get(row["retrieval_status"], 0) + 1
    print(f"requested_dois={len(requested)} manifest_rows={len(records)} statuses={dict(sorted(counts.items()))}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", type=Path, default=INVENTORY)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--sleep", type=float, default=0.2)
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()
    build(args.inventory, args.output_root, args.manifest, args.sleep, args.timeout, args.limit)


if __name__ == "__main__":
    main()
