#!/usr/bin/env python3
"""Export the Module 12B targeted grant-citation addendum separately.

The addendum is deliberately kept outside the frozen Module 12B first-pass
bundle. It is structurally validated and provenance-linked, but remains queued
for full extraction before gold promotion or SQL materialization.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from export_tracker_evidence_bundle import referenced_ids, snake_case, split_markdown_row


ROOT = Path(__file__).resolve().parents[1]
TRACKER = ROOT / "modules" / "Module_12B_TRACKER.md"
SOURCE_TRACKER = ROOT / "modules" / "Module_12A_TRACKER.md"
DEFAULT_OUTPUT = ROOT / "data" / "processed" / "module12b_targeted_addendum_evidence_bundle.json"

SECTIONS = {
    "observations": "### Addendum Atomic Observations",
    "author_claims": "### Addendum Claims",
    "evidence_links": "### Addendum Evidence Links",
    "boundary_records": "### Addendum Boundary Conditions",
    "consensus_drafts": "### Addendum Consensus Draft Queue",
}

EXPECTED_COUNTS = {
    "observations": 24,
    "author_claims": 4,
    "evidence_links": 24,
    "boundary_records": 4,
    "consensus_drafts": 4,
}


def extract_subsection_table(markdown: str, section_title: str) -> list[dict[str, str]]:
    in_section = False
    headers: list[str] | None = None
    rows: list[dict[str, str]] = []
    for line in markdown.splitlines():
        if line.startswith(section_title):
            in_section = True
            continue
        if in_section and line.startswith("#") and headers is not None:
            break
        if not in_section or not line.startswith("|"):
            continue
        if line.startswith("|---"):
            continue
        cells = split_markdown_row(line)
        if headers is None:
            headers = [snake_case(cell) for cell in cells]
            continue
        if len(cells) != len(headers):
            raise ValueError(
                f"Unexpected row width in {section_title}: expected {len(headers)}, "
                f"found {len(cells)} in {line}"
            )
        rows.append(dict(zip(headers, cells, strict=True)))
    if headers is None:
        raise ValueError(f"Could not find table for {section_title}")
    return rows


def normalize_rows(rows: list[dict[str, str]], kind: str) -> list[dict[str, str]]:
    normalized: list[dict[str, str]] = []
    aliases = {
        "observations": ("observation_id", "tracker_id"),
        "author_claims": ("claim_id", "tracker_id"),
        "evidence_links": ("evidence_link_id", "tracker_id"),
        "boundary_records": ("boundary_id", "tracker_id"),
        "consensus_drafts": ("consensus_id", "tracker_id"),
    }
    for row in rows:
        item = dict(row)
        old_key, new_key = aliases[kind]
        if old_key in item:
            item[new_key] = item[old_key]
        if kind == "consensus_drafts" and "draft_statement" in item:
            item["consensus_statement"] = item["draft_statement"]
        normalized.append(item)
    return normalized


def expected_ids(prefix: str, start: int, end: int) -> set[str]:
    return {f"{prefix}{number:03d}" for number in range(start, end + 1)}


def validate_contiguous(label: str, values: set[str], expected: set[str]) -> list[str]:
    if values != expected:
        return [
            f"{label}: expected {sorted(expected)}, found {sorted(values)}; "
            f"missing={sorted(expected - values)}, extra={sorted(values - expected)}"
        ]
    return []


def build_bundle() -> dict[str, Any]:
    markdown = TRACKER.read_text(encoding="utf-8")
    addendum_start = markdown.index("## Targeted Grant-Citation Consolidation Addendum")
    addendum_text = markdown[addendum_start:]
    bundle: dict[str, Any] = {
        "source_tracker": str(TRACKER.relative_to(ROOT)),
        "module": "Module 12B targeted grant-citation consolidation addendum",
        "status": "queued targeted addendum; full extraction and materialization pending",
        "materialization": {
            "included_in_frozen_first_pass_bundle": False,
            "canonical_materialization_allowed": False,
            "promotion_status": "QUEUED",
            "full_extraction_required": True,
        },
        "source_paper_ids": [f"M12A-P{number:03d}" for number in range(25, 49)],
    }
    for kind, title in SECTIONS.items():
        bundle[kind] = normalize_rows(extract_subsection_table(markdown, title), kind)
    return bundle


def validate_bundle(bundle: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for key, expected in EXPECTED_COUNTS.items():
        actual = len(bundle[key])
        if actual != expected:
            errors.append(f"{key}: expected {expected}, found {actual}")

    observations = {row["tracker_id"] for row in bundle["observations"]}
    claims = {row["tracker_id"] for row in bundle["author_claims"]}
    links = {row["tracker_id"] for row in bundle["evidence_links"]}
    boundaries = {row["tracker_id"] for row in bundle["boundary_records"]}
    consensus = {row["tracker_id"] for row in bundle["consensus_drafts"]}
    errors.extend(validate_contiguous("observations", observations, expected_ids("M12B-O", 25, 48)))
    errors.extend(validate_contiguous("author_claims", claims, expected_ids("M12B-C", 25, 28)))
    errors.extend(validate_contiguous("evidence_links", links, expected_ids("M12B-L", 57, 80)))
    errors.extend(validate_contiguous("boundary_records", boundaries, expected_ids("M12B-B", 9, 12)))
    errors.extend(validate_contiguous("consensus_drafts", consensus, expected_ids("M12B-S", 9, 12)))

    for link in bundle["evidence_links"]:
        if link["claim_id"] not in claims:
            errors.append(f"{link['tracker_id']}: unknown claim {link['claim_id']}")
        if link["observation_id"] not in observations:
            errors.append(f"{link['tracker_id']}: unknown observation {link['observation_id']}")

    for boundary in bundle["boundary_records"]:
        text = " ".join(str(value) for value in boundary.values())
        for observation_id in referenced_ids(text, "M12B-O"):
            if observation_id not in observations:
                errors.append(f"{boundary['tracker_id']}: unknown observation {observation_id}")
        for claim_id in referenced_ids(text, "M12B-C"):
            if claim_id not in claims:
                errors.append(f"{boundary['tracker_id']}: unknown claim {claim_id}")

    for draft in bundle["consensus_drafts"]:
        text = " ".join(str(value) for value in draft.values())
        for observation_id in referenced_ids(text, "M12B-O"):
            if observation_id not in observations:
                errors.append(f"{draft['tracker_id']}: unknown observation {observation_id}")
        for claim_id in referenced_ids(text, "M12B-C"):
            if claim_id not in claims:
                errors.append(f"{draft['tracker_id']}: unknown claim {claim_id}")
        for boundary_id in referenced_ids(text, "M12B-B"):
            if boundary_id not in boundaries:
                errors.append(f"{draft['tracker_id']}: unknown boundary {boundary_id}")

    tracker_text = TRACKER.read_text(encoding="utf-8")
    source_text = SOURCE_TRACKER.read_text(encoding="utf-8")
    addendum_text = tracker_text[tracker_text.index("## Targeted Grant-Citation Consolidation Addendum"):]
    source_ids = set(re.findall(r"\bM12A-P\d{3}\b", source_text))
    expected_sources = set(bundle["source_paper_ids"])
    if not expected_sources <= source_ids:
        errors.append(f"missing Module 12A source IDs: {sorted(expected_sources - source_ids)}")
    if not all(source_id in addendum_text for source_id in expected_sources):
        errors.append("not all Module 12A source IDs are represented in the addendum text")
    for marker in ("TARGETED ADDENDUM", "QUEUED", "Requires full extraction before gold promotion"):
        if marker not in addendum_text:
            errors.append(f"missing addendum marker: {marker}")
    if bundle["materialization"]["canonical_materialization_allowed"] is not False:
        errors.append("canonical materialization must remain false")
    return errors


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true", help="Validate without writing the JSON artifact.")
    return parser.parse_args(argv or sys.argv[1:])


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    bundle = build_bundle()
    errors = validate_bundle(bundle)
    if errors:
        for error in errors:
            print(f"FAIL {error}", file=sys.stderr)
        return 1
    counts = ", ".join(f"{key}={len(bundle[key])}" for key in EXPECTED_COUNTS)
    if args.check:
        print(f"PASS Module 12B targeted addendum: {counts}")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(bundle, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {args.output.relative_to(ROOT)} ({counts})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
