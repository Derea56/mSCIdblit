#!/usr/bin/env python3
"""Export Module 1B tracker evidence rows into a structured JSON bundle.

This bundle is the bridge between the reviewable Markdown tracker and future
full SQL materialization. It preserves tracker IDs for observations, claims,
evidence links, boundary records, and consensus drafts.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from export_module1_consensus import parse_drafts


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TRACKER = ROOT / "modules" / "Module_1B_TRACKER.md"
DEFAULT_OUTPUT = ROOT / "data" / "processed" / "module1_evidence_bundle.json"

EXPECTED_COUNTS = {
    "observations": 84,
    "author_claims": 50,
    "evidence_links": 107,
    "boundary_records": 7,
    "consensus_drafts": 8,
}


SECTION_TITLES = {
    "observations": "## Pass 4A: Atomic Observations Extracted",
    "author_claims": "## Pass 5A: Author Claims Extracted",
    "evidence_links": "## Pass 6A: Evidence Links",
    "boundary_records": "## Contradiction Map",
}


def snake_case(value: str) -> str:
    normalized = value.strip().lower()
    normalized = normalized.replace("/", " ")
    normalized = normalized.replace("-", " ")
    normalized = re.sub(r"[^a-z0-9]+", "_", normalized)
    return normalized.strip("_")


def split_markdown_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def extract_table(markdown: str, section_title: str) -> list[dict[str, str]]:
    in_section = False
    headers: list[str] | None = None
    rows: list[dict[str, str]] = []
    for line in markdown.splitlines():
        if line.startswith(section_title):
            in_section = True
            continue
        if in_section and line.startswith("## ") and headers is not None:
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


def add_alias(row: dict[str, str], old_key: str, new_key: str) -> None:
    if old_key in row:
        row[new_key] = row[old_key]


def normalize_rows(rows: list[dict[str, str]], kind: str) -> list[dict[str, str]]:
    normalized: list[dict[str, str]] = []
    for row in rows:
        item = dict(row)
        if kind == "observations":
            add_alias(item, "observation_id", "tracker_id")
        elif kind == "author_claims":
            add_alias(item, "claim_id", "tracker_id")
        elif kind == "evidence_links":
            add_alias(item, "link_id", "tracker_id")
        elif kind == "boundary_records":
            add_alias(item, "contradiction_id", "tracker_id")
        normalized.append(item)
    return normalized


def tracker_ids(text: str, prefix: str) -> set[str]:
    return set(re.findall(rf"\b{prefix}\d{{3}}\b", text))


def validate_bundle(bundle: dict[str, object]) -> list[str]:
    errors: list[str] = []
    for key, expected in EXPECTED_COUNTS.items():
        actual = len(bundle[key])  # type: ignore[arg-type]
        if actual != expected:
            errors.append(f"{key}: expected {expected}, found {actual}")

    observation_ids = {row["tracker_id"] for row in bundle["observations"]}  # type: ignore[index]
    claim_ids = {row["tracker_id"] for row in bundle["author_claims"]}  # type: ignore[index]
    boundary_ids = {row["tracker_id"] for row in bundle["boundary_records"]}  # type: ignore[index]

    for link in bundle["evidence_links"]:  # type: ignore[assignment]
        link_id = link["tracker_id"]
        if link["claim_id"] not in claim_ids:
            errors.append(f"{link_id}: unknown claim_id {link['claim_id']}")
        if link["observation_id"] not in observation_ids:
            errors.append(f"{link_id}: unknown observation_id {link['observation_id']}")

    for boundary in bundle["boundary_records"]:  # type: ignore[assignment]
        for claim_id in tracker_ids(boundary["claim_1"] + " " + boundary["claim_2"], "M1B-C"):
            if claim_id not in claim_ids:
                errors.append(f"{boundary['tracker_id']}: unknown boundary claim {claim_id}")

    for draft in bundle["consensus_drafts"]:  # type: ignore[assignment]
        draft_id = draft["consensus_draft_id"]
        for observation_id in draft["observation_tracker_ids"]:
            if observation_id not in observation_ids:
                errors.append(f"{draft_id}: unknown observation reference {observation_id}")
        for claim_id in draft["claim_tracker_ids"]:
            if claim_id not in claim_ids:
                errors.append(f"{draft_id}: unknown claim reference {claim_id}")
        for boundary_id in draft["boundary_tracker_ids"]:
            if boundary_id not in boundary_ids:
                errors.append(f"{draft_id}: unknown boundary reference {boundary_id}")

    return errors


def build_bundle(tracker: Path) -> dict[str, object]:
    markdown = tracker.read_text()
    bundle: dict[str, object] = {
        "source_tracker": str(tracker.relative_to(ROOT)),
        "module": "Module 1",
        "status": "first-pass evidence bundle exported from tracker rows",
        "observations": normalize_rows(extract_table(markdown, SECTION_TITLES["observations"]), "observations"),
        "author_claims": normalize_rows(extract_table(markdown, SECTION_TITLES["author_claims"]), "author_claims"),
        "evidence_links": normalize_rows(extract_table(markdown, SECTION_TITLES["evidence_links"]), "evidence_links"),
        "boundary_records": normalize_rows(extract_table(markdown, SECTION_TITLES["boundary_records"]), "boundary_records"),
        "consensus_drafts": [draft.__dict__ for draft in parse_drafts(tracker)],
    }
    return bundle


def write_bundle(bundle: dict[str, object], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(bundle, indent=2) + "\n")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tracker", type=Path, default=DEFAULT_TRACKER)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true", help="Validate bundle without writing it.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    bundle = build_bundle(args.tracker)
    errors = validate_bundle(bundle)
    if errors:
        for error in errors:
            print(f"FAIL {error}", file=sys.stderr)
        return 1
    if args.check:
        counts = ", ".join(f"{key}={len(bundle[key])}" for key in EXPECTED_COUNTS)
        print(f"PASS Module 1 evidence bundle: {counts}")
        return 0
    write_bundle(bundle, args.output)
    print(f"Wrote {args.output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
