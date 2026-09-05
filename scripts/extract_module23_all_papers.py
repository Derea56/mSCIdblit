#!/usr/bin/env python3
"""Inventory and extract all paper anchors cited by Module 23A and 23B.

This is a paper-level audit layer. It preserves PMID, PMCID, and DOI anchors
as distinct identifiers unless an authoritative resolver has merged them. For
each anchor it records register coverage, known local artifacts, and a short
candidate excerpt when an artifact is present. It never creates canonical
database rows or promotes evidence.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

from extract_module23b_curated_papers import choose_artifact, local_paths, match_excerpt, plain_text, read_tsv


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATHS = {
    "23A": ROOT / "work/module23a/module23a_evidence_register.tsv",
    "23B": ROOT / "work/module_b_consolidation/module23b/module23b_evidence_register.tsv",
}
MANIFEST = ROOT / "work/module23a/module23a_second_pass_source_manifest.tsv"
DEFAULT_OUTPUT = ROOT / "work/module_b_consolidation/module23b/module23_all_paper_extraction_inventory_2026-09-05.tsv"
DEFAULT_REPORT = ROOT / "work/module_b_consolidation/module23b/module23_all_paper_extraction_inventory_2026-09-05.md"

FIELDS = [
    "paper_anchor", "anchor_type", "module_coverage", "source_review_ids",
    "associated_evidence_count", "associated_edge_count", "associated_evidence_ids",
    "associated_edge_ids", "local_source_paths", "source_artifact_status",
    "source_format", "candidate_excerpt", "excerpt_sentence_index",
    "excerpt_match_terms", "extraction_method", "paper_extraction_status",
    "human_validation_status", "promotion_status",
]


def stable_anchors(value: str) -> list[str]:
    """Return normalized stable identifiers without merging variants."""
    found: set[str] = set()
    for match in re.finditer(r"(?i)\b(PMC\d{3,10})\b", value or ""):
        found.add("PMCID:" + match.group(1).upper())
    for match in re.finditer(r"(?i)\bPMID\s*[:_-]?\s*(\d{4,9})\b", value or ""):
        found.add("PMID:" + match.group(1))
    for match in re.finditer(r"(?i)\bDOI\s*:\s*(10\.\d{4,9}/[^;\s]+)", value or ""):
        doi = match.group(1).rstrip(".,)]}'\"").lower().replace("_", "/")
        found.add("DOI:" + doi)
    for match in re.finditer(r"(?i)pubmed\.ncbi\.nlm\.nih\.gov/(\d{4,9})", value or ""):
        found.add("PMID:" + match.group(1))
    return sorted(found)


def source_review_ids(value: str) -> list[str]:
    return sorted(set(re.findall(r"EXPAND23A-(?:REV|SRC)-\d+", value or "")))


def add_anchor(records: dict[str, dict[str, object]], anchor: str, module: str, row: dict[str, str], paths: list[Path], reviews: list[str]) -> None:
    record = records.setdefault(anchor, {
        "modules": set(), "reviews": set(), "evidence_ids": set(), "edge_ids": set(),
        "paths": set(), "summaries": [],
    })
    record["modules"].add(module)
    record["reviews"].update(reviews)
    if row.get("b_evidence_id"):
        record["evidence_ids"].add(row["b_evidence_id"])
    if row.get("b_edge_ids"):
        record["edge_ids"].update(item for item in row["b_edge_ids"].split(";") if item)
    record["paths"].update(paths)
    summary = row.get("evidence_summary", "")
    if summary and summary not in record["summaries"]:
        record["summaries"].append(summary)


def build(output: Path, report: Path) -> None:
    records: dict[str, dict[str, object]] = {}
    unanchored: Counter[str] = Counter()
    register_rows = 0
    for module, path in REGISTER_PATHS.items():
        for row in read_tsv(path):
            register_rows += 1
            locator = row.get("source_locator", "")
            anchors = stable_anchors(locator)
            paths = local_paths(locator)
            reviews = source_review_ids(" ".join(row.get(key, "") for key in ("source_locator", "citation_note", "source_a_evidence_id")))
            if not anchors:
                unanchored[module] += 1
            for anchor in anchors:
                add_anchor(records, anchor, module, row, paths, reviews)

    manifest_rows = 0
    manifest_review_ids: set[str] = set()
    for row in read_tsv(MANIFEST):
        manifest_rows += 1
        review_id = row.get("source_id", "")
        if review_id:
            manifest_review_ids.add(review_id)
        anchors = stable_anchors(row.get("primary_locator", ""))
        paths = local_paths(row.get("local_path", ""))
        synthetic = {
            "b_evidence_id": "", "b_edge_ids": "",
            "evidence_summary": row.get("acquisition_note", ""),
        }
        for anchor in anchors:
            add_anchor(records, anchor, "23A", synthetic, paths, [review_id] if review_id else [])

    rows: list[dict[str, str]] = []
    status_counts: Counter[str] = Counter()
    module_counts: Counter[str] = Counter()
    for anchor in sorted(records):
        record = records[anchor]
        paths = sorted(path for path in record["paths"] if path.is_file())
        artifact, source_format, artifact_status = choose_artifact(paths)
        combined_summary = " ".join(record["summaries"])
        excerpt = ""
        sentence_index = 0
        terms = ""
        if artifact is not None:
            excerpt, sentence_index, terms = match_excerpt(plain_text(artifact), combined_summary, "")
        if artifact is None:
            extraction_status = "awaiting_local_source_acquisition"
        elif artifact_status == "local_full_text_artifact" and excerpt:
            extraction_status = "candidate_extracted_from_full_text"
        elif excerpt:
            extraction_status = "candidate_extracted_from_abstract_or_metadata"
        else:
            extraction_status = "local_artifact_present_excerpt_not_matched"
        modules = ";".join(sorted(record["modules"]))
        module_counts[modules] += 1
        status_counts[extraction_status] += 1
        rows.append({
            "paper_anchor": anchor,
            "anchor_type": anchor.split(":", 1)[0],
            "module_coverage": modules,
            "source_review_ids": ";".join(sorted(record["reviews"])),
            "associated_evidence_count": str(len(record["evidence_ids"])),
            "associated_edge_count": str(len(record["edge_ids"])),
            "associated_evidence_ids": ";".join(sorted(record["evidence_ids"])),
            "associated_edge_ids": ";".join(sorted(record["edge_ids"])),
            "local_source_paths": "; ".join(str(path.relative_to(ROOT)) for path in paths),
            "source_artifact_status": artifact_status if artifact is not None else "no_local_artifact",
            "source_format": source_format if artifact is not None else "not_acquired",
            "candidate_excerpt": excerpt,
            "excerpt_sentence_index": str(sentence_index),
            "excerpt_match_terms": terms,
            "extraction_method": "deterministic_sentence_match_against_local_artifact" if artifact is not None else "paper_anchor_inventory",
            "paper_extraction_status": extraction_status,
            "human_validation_status": "required",
            "promotion_status": "not_promoted",
        })

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "# Module 23 all-paper extraction inventory (2026-09-05)",
        "",
        "This inventory covers every stable paper identifier cited by the Module",
        "23A and 23B evidence registers, plus the Module 23A source manifest.",
        "PMID, PMCID, and DOI identifiers remain separate unless an authoritative",
        "resolver has merged them. Local excerpts are deterministic candidate text",
        "matches only; no canonical database rows or promotions are created.",
        "",
        f"- Register rows inspected: {register_rows:,}",
        f"- Source-manifest rows inspected: {manifest_rows:,}",
        f"- Distinct stable paper anchors: {len(rows):,}",
        f"- Register rows without a stable paper anchor: {sum(unanchored.values()):,}",
        f"- Source-review IDs represented in manifest: {len(manifest_review_ids):,}",
        "",
        "## Extraction status",
        "",
        "| Status | Anchors |",
        "|---|---:|",
    ]
    lines.extend(f"| {key} | {value:,} |" for key, value in sorted(status_counts.items()))
    lines.extend([
        "",
        "## Module coverage",
        "",
        "| Coverage | Anchors |",
        "|---|---:|",
    ])
    lines.extend(f"| {key} | {value:,} |" for key, value in sorted(module_counts.items()))
    lines.extend([
        "",
        "## Unanchored register rows",
        "",
    ])
    lines.extend(f"- {module}: {count:,}" for module, count in sorted(unanchored.items()))
    lines.extend([
        "",
        "## Boundary",
        "",
        "An inventory row is not proof that a unique publication has been resolved",
        "when several identifiers co-occur in a register record. Missing local source",
        "artifacts remain acquisition work, and every row remains human-review-required",
        "and unpromoted.",
        "",
    ])
    report.write_text("\n".join(lines), encoding="utf-8")
    print(f"paper_anchors={len(rows)} register_rows={register_rows} manifest_rows={manifest_rows} output={output}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()
    build(args.output, args.report)


if __name__ == "__main__":
    main()
