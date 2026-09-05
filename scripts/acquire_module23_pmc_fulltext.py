#!/usr/bin/env python3
"""Acquire unresolved Module 23 PMC full text through NCBI BioC JSON."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "work/module_b_consolidation/module23b/module23_all_paper_extraction_inventory_2026-09-05.tsv"
DEFAULT_OUTPUT_ROOT = ROOT / "data/raw/evidence/module23_pmc_fulltext_20260905"
DEFAULT_MANIFEST = DEFAULT_OUTPUT_ROOT / "acquisition_manifest.tsv"
FIELDS = ["pmcid", "local_path", "retrieval_status", "retrieval_method", "retrieved_at_utc", "sha256"]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fetch(pmcid: str, timeout: int) -> tuple[bytes, str, str]:
    url = f"https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/{pmcid}/unicode"
    request = Request(url, headers={"User-Agent": "mSCIdblit-module23-pmc-acquisition/1.0"})
    try:
        with urlopen(request, timeout=timeout) as response:
            body = response.read()
        json.loads(body)
    except Exception:
        # Some older PMC articles are not in the BioC open-access subset but
        # remain retrievable through the public PMC XML endpoint.
        xml_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id={pmcid}&retmode=xml"
        xml_request = Request(xml_url, headers={"User-Agent": "mSCIdblit-module23-pmc-acquisition/1.0"})
        with urlopen(xml_request, timeout=timeout) as response:
            body = response.read()
        ET.fromstring(body)
        return body, "ncbi_pmc_xml", "full.xml"
    return body, "ncbi_bioc_json", "bioc.json"


def build(inventory: Path, output_root: Path, manifest: Path, sleep_seconds: float, timeout: int, limit: int | None) -> None:
    rows = read_tsv(inventory)
    requested = sorted({
        row["paper_anchor"].split(":", 1)[1].upper()
        for row in rows
        if row["anchor_type"] == "PMCID" and row["paper_extraction_status"] == "awaiting_local_source_acquisition"
    })
    if limit is not None:
        requested = requested[:limit]
    output_root.mkdir(parents=True, exist_ok=True)
    existing = {row["pmcid"]: row for row in read_tsv(manifest)} if manifest.exists() else {}
    records: dict[str, dict[str, str]] = {}
    for path in output_root.iterdir():
        match = re.match(r"(PMC\d{3,10})_(?:bioc\.json|full\.xml)$", path.name, flags=re.I)
        if not match or not path.is_file() or not path.stat().st_size:
            continue
        pmcid = match.group(1).upper()
        method = "ncbi_bioc_json" if path.name.endswith("_bioc.json") else "ncbi_pmc_xml"
        prior = existing.get(pmcid, {})
        records[pmcid] = {
            "pmcid": pmcid,
            "local_path": f"data/raw/evidence/module23_pmc_fulltext_20260905/{path.name}",
            "retrieval_status": "cached",
            "retrieval_method": prior.get("retrieval_method", method),
            "retrieved_at_utc": prior.get("retrieved_at_utc", datetime.now(timezone.utc).isoformat()),
            "sha256": sha256(path),
        }
    for pmcid in requested:
        existing_paths = [
            output_root / f"{pmcid}_bioc.json",
            output_root / f"{pmcid}_full.xml",
        ]
        path = next((candidate for candidate in existing_paths if candidate.is_file() and candidate.stat().st_size), existing_paths[0])
        now = datetime.now(timezone.utc).isoformat()
        if path.is_file() and path.stat().st_size:
            records[pmcid] = {
                "pmcid": pmcid,
                "local_path": f"data/raw/evidence/module23_pmc_fulltext_20260905/{path.name}",
                "retrieval_status": "cached",
                "retrieval_method": existing.get(pmcid, {}).get("retrieval_method", "ncbi_bioc_json"),
                "retrieved_at_utc": existing.get(pmcid, {}).get("retrieved_at_utc", now),
                "sha256": sha256(path),
            }
            continue
        try:
            body, method, suffix = fetch(pmcid, timeout)
            path = output_root / f"{pmcid}_{suffix}"
            path.write_bytes(body)
        except Exception as error:
            records[pmcid] = {
                "pmcid": pmcid,
                "local_path": f"data/raw/evidence/module23_pmc_fulltext_20260905/{pmcid}_bioc.json",
                "retrieval_status": f"fetch_failed:{type(error).__name__}",
                "retrieval_method": "ncbi_bioc_json",
                "retrieved_at_utc": now,
                "sha256": "",
            }
        else:
            records[pmcid] = {
                "pmcid": pmcid,
                "local_path": f"data/raw/evidence/module23_pmc_fulltext_20260905/{path.name}",
                "retrieval_status": "fetched",
                "retrieval_method": method,
                "retrieved_at_utc": now,
                "sha256": sha256(path),
            }
        time.sleep(sleep_seconds)
    with manifest.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(records[pmcid] for pmcid in sorted(records))
    counts: dict[str, int] = {}
    for row in records.values():
        counts[row["retrieval_status"]] = counts.get(row["retrieval_status"], 0) + 1
    print(f"requested_pmcids={len(requested)} manifest_rows={len(records)} statuses={dict(sorted(counts.items()))}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", type=Path, default=INVENTORY)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--sleep", type=float, default=0.5)
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()
    build(args.inventory, args.output_root, args.manifest, args.sleep, args.timeout, args.limit)


if __name__ == "__main__":
    main()
