#!/usr/bin/env python3
"""Audit unresolved Module 23 DOI strings against independently retrieved records."""

from __future__ import annotations

import argparse
import csv
import re
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "work/module_b_consolidation/module23b/module23_all_paper_extraction_inventory_2026-09-05.tsv"
REGISTER = ROOT / "work/module_b_consolidation/module23b/module23b_evidence_register.tsv"
DOI_MANIFEST = ROOT / "data/raw/evidence/module23_doi_metadata_20260905/acquisition_manifest.tsv"
ARCHIVE_ROOT = ROOT.parent / "mSCIdblit_local_archive/module20_24_supervised_cli_phase2_2026-08-31"
OUTPUT = ROOT / "work/module_b_consolidation/module23b/module23_unresolved_doi_resolution_audit_2026-09-05.tsv"
FIELDS = [
    "target_doi", "acquisition_status", "coidentified_pmids", "coidentified_pmcids",
    "observed_source_dois", "observed_source_titles", "resolution_disposition",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def source_locator(doi: str, register_rows: list[dict[str, str]]) -> str:
    for row in register_rows:
        if doi.casefold() in row.get("source_locator", "").casefold():
            return row["source_locator"]
    return ""


def artifact_paths(kind: str, identifier: str, archive_root: Path) -> list[Path]:
    if kind == "PMID":
        paths = list((ROOT / "data/raw/evidence/module23_pubmed_abstracts_20260905").glob(f"*{identifier}*"))
    else:
        paths = list((ROOT / "data/raw/evidence/module23_pmc_fulltext_20260905").glob(f"*{identifier}*"))
    paths.extend(archive_root.glob(f"*{identifier}*"))
    return [path for path in paths if path.is_file() and path.stat().st_size]


def metadata(path: Path) -> tuple[list[str], str]:
    try:
        root = ET.fromstring(path.read_bytes())
    except (ET.ParseError, UnicodeDecodeError):
        return [], ""
    if path.suffix.lower() == ".xml":
        ids = []
        article_id_list = root.find(".//PubmedData/ArticleIdList")
        if article_id_list is not None:
            for element in article_id_list.findall("ArticleId"):
                if element.attrib.get("IdType") == "doi" and element.text:
                    ids.append(element.text.strip())
        if not ids:
            for element in root.findall(".//article-meta/article-id"):
                if element.attrib.get("pub-id-type") == "doi" and element.text:
                    ids.append(element.text.strip())
        title = root.findtext(".//Article/ArticleTitle") or root.findtext(".//article-meta/title-group/article-title") or ""
        return ids, " ".join(title.split())
    return [], ""


def build(output: Path) -> None:
    inventory = read_tsv(INVENTORY)
    register_rows = read_tsv(REGISTER)
    acquisition = {row["doi"]: row for row in read_tsv(DOI_MANIFEST)} if DOI_MANIFEST.exists() else {}
    rows: list[dict[str, str]] = []
    for record in inventory:
        if record["paper_extraction_status"] != "awaiting_local_source_acquisition" or record["anchor_type"] != "DOI":
            continue
        doi = record["paper_anchor"].split(":", 1)[1]
        locator = source_locator(doi, register_rows)
        pmids = sorted(set(re.findall(r"(?i)PMID\s*:\s*(\d+)", locator)))
        pmcids = sorted(set(x.upper() for x in re.findall(r"(?i)(PMC\d+)", locator)))
        observed_dois: set[str] = set()
        observed_titles: set[str] = set()
        for kind, identifiers in (("PMID", pmids), ("PMCID", pmcids)):
            for identifier in identifiers:
                for path in artifact_paths(kind, identifier, ARCHIVE_ROOT):
                    source_dois, title = metadata(path)
                    observed_dois.update(source_dois)
                    if title:
                        observed_titles.add(title)
        rows.append({
            "target_doi": doi,
            "acquisition_status": acquisition.get(doi, {}).get("retrieval_status", "not_attempted"),
            "coidentified_pmids": ";".join(pmids),
            "coidentified_pmcids": ";".join(pmcids),
            "observed_source_dois": ";".join(sorted(observed_dois)),
            "observed_source_titles": " || ".join(sorted(observed_titles)),
            "resolution_disposition": "requires_manual_identifier_correction; identifiers_not_merged",
        })
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"unresolved_dois={len(rows)} output={output}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    build(args.output)


if __name__ == "__main__":
    main()
