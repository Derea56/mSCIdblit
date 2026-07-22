#!/usr/bin/env python3
"""Export and audit tracker-level evidence bundles for B-phase modules.

The B trackers are the reviewable curation source of truth. This script turns
their Markdown tables into structured JSON and performs lightweight relational
checks before downstream SQL materialization.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class ModuleConfig:
    key: str
    label: str
    tracker: Path
    output: Path
    id_prefix: str
    boundary_prefix: str
    evidence_link_section: str
    boundary_section: str
    boundary_id_key: str
    consensus_section: str
    consensus_statement_key: str
    expected_counts: dict[str, int]
    required_phrases: tuple[str, ...]


MODULES = {
    "1b": ModuleConfig(
        key="1b",
        label="Module 1B",
        tracker=ROOT / "modules" / "Module_1B_TRACKER.md",
        output=ROOT / "data" / "processed" / "module1_tracker_evidence_bundle.json",
        id_prefix="M1B",
        boundary_prefix="M1B-X",
        evidence_link_section="## Pass 6A: Evidence Links",
        boundary_section="## Contradiction Map",
        boundary_id_key="contradiction_id",
        consensus_section="## Pass 6: Draft Consensus Statements",
        consensus_statement_key="draft_consensus_statement",
        expected_counts={
            "observations": 93,
            "author_claims": 50,
            "evidence_links": 107,
            "boundary_records": 7,
            "consensus_drafts": 8,
        },
        required_phrases=(
            "CONSENSUS-READY FIRST PASS",
            "FULL SQL EXPORTED; CONSENSUS_OBSERVATION VALIDATED",
            "MET FOR ALL FIRST-PASS TOPICS",
            "Module 1 first-pass curation freeze",
        ),
    ),
    "2b": ModuleConfig(
        key="2b",
        label="Module 2B",
        tracker=ROOT / "modules" / "Module_2B_TRACKER.md",
        output=ROOT / "data" / "processed" / "module2_evidence_bundle.json",
        id_prefix="M2B",
        boundary_prefix="M2B-B",
        evidence_link_section="## Pass 6: Evidence Links Drafted",
        boundary_section="## Boundary Conditions Draft",
        boundary_id_key="boundary_id",
        consensus_section="## Consensus Draft Queue",
        consensus_statement_key="draft_statement",
        expected_counts={
            "observations": 90,
            "author_claims": 36,
            "evidence_links": 56,
            "boundary_records": 8,
            "consensus_drafts": 8,
        },
        required_phrases=(
            "CONSENSUS-READY FIRST PASS",
            "Module 2 first-pass curation freeze",
            "COMPLETE FIRST PASS",
        ),
    ),
    "3b": ModuleConfig(
        key="3b",
        label="Module 3B",
        tracker=ROOT / "modules" / "Module_3B_TRACKER.md",
        output=ROOT / "data" / "processed" / "module3_evidence_bundle.json",
        id_prefix="M3B",
        boundary_prefix="M3B-B",
        evidence_link_section="## Pass 6: Evidence Links Drafted",
        boundary_section="## Boundary Conditions Draft",
        boundary_id_key="boundary_id",
        consensus_section="## Consensus Draft Queue",
        consensus_statement_key="draft_statement",
        expected_counts={
            "observations": 94,
            "author_claims": 36,
            "evidence_links": 60,
            "boundary_records": 8,
            "consensus_drafts": 8,
        },
        required_phrases=(
            "CONSENSUS-READY FIRST PASS",
            "Module 3 first-pass curation freeze",
            "COMPLETE FIRST PASS",
        ),
    ),
    "4b": ModuleConfig(
        key="4b",
        label="Module 4B",
        tracker=ROOT / "modules" / "Module_4B_TRACKER.md",
        output=ROOT / "data" / "processed" / "module4_evidence_bundle.json",
        id_prefix="M4B",
        boundary_prefix="M4B-B",
        evidence_link_section="## Pass 6: Evidence Links Drafted",
        boundary_section="## Boundary Conditions Draft",
        boundary_id_key="boundary_id",
        consensus_section="## Consensus Draft Queue",
        consensus_statement_key="draft_statement",
        expected_counts={
            "observations": 98,
            "author_claims": 40,
            "evidence_links": 72,
            "boundary_records": 8,
            "consensus_drafts": 8,
        },
        required_phrases=(
            "CONSENSUS-READY FIRST PASS",
            "Module 4 first-pass curation freeze",
            "COMPLETE FIRST PASS",
        ),
    ),
    "5b": ModuleConfig(
        key="5b",
        label="Module 5B",
        tracker=ROOT / "modules" / "Module_5B_TRACKER.md",
        output=ROOT / "data" / "processed" / "module5_evidence_bundle.json",
        id_prefix="M5B",
        boundary_prefix="M5B-B",
        evidence_link_section="## Pass 6: Evidence Links Drafted",
        boundary_section="## Boundary Conditions Draft",
        boundary_id_key="boundary_id",
        consensus_section="## Consensus Draft Queue",
        consensus_statement_key="draft_statement",
        expected_counts={
            "observations": 94,
            "author_claims": 36,
            "evidence_links": 60,
            "boundary_records": 8,
            "consensus_drafts": 8,
        },
        required_phrases=(
            "CONSENSUS-READY FIRST PASS",
            "Module 5 first-pass curation freeze",
            "COMPLETE FIRST PASS",
        ),
    ),
    "6b": ModuleConfig(
        key="6b",
        label="Module 6B",
        tracker=ROOT / "modules" / "Module_6B_TRACKER.md",
        output=ROOT / "data" / "processed" / "module6_evidence_bundle.json",
        id_prefix="M6B",
        boundary_prefix="M6B-B",
        evidence_link_section="## Pass 6: Evidence Links Drafted",
        boundary_section="## Boundary Conditions Draft",
        boundary_id_key="boundary_id",
        consensus_section="## Consensus Draft Queue",
        consensus_statement_key="draft_statement",
        expected_counts={
            "observations": 36,
            "author_claims": 36,
            "evidence_links": 104,
            "boundary_records": 8,
            "consensus_drafts": 8,
        },
        required_phrases=(
            "CONSENSUS-READY FIRST PASS",
            "Module 6 first-pass curation freeze",
            "MET FOR ALL FIRST-PASS TOPICS",
        ),
    ),
    "7b": ModuleConfig(
        key="7b",
        label="Module 7B",
        tracker=ROOT / "modules" / "Module_7B_TRACKER.md",
        output=ROOT / "data" / "processed" / "module7_evidence_bundle.json",
        id_prefix="M7B",
        boundary_prefix="M7B-B",
        evidence_link_section="## Pass 6: Evidence Links Drafted",
        boundary_section="## Boundary Conditions Draft",
        boundary_id_key="boundary_id",
        consensus_section="## Consensus Draft Queue",
        consensus_statement_key="draft_statement",
        expected_counts={
            "observations": 40,
            "author_claims": 36,
            "evidence_links": 88,
            "boundary_records": 8,
            "consensus_drafts": 8,
        },
        required_phrases=(
            "CONSENSUS-READY FIRST PASS",
            "Module 7 first-pass curation freeze",
            "MET FOR ALL FIRST-PASS TOPICS",
        ),
    ),
    "8b": ModuleConfig(
        key="8b",
        label="Module 8B",
        tracker=ROOT / "modules" / "Module_8B_TRACKER.md",
        output=ROOT / "data" / "processed" / "module8_evidence_bundle.json",
        id_prefix="M8B",
        boundary_prefix="M8B-B",
        evidence_link_section="## Pass 6: Evidence Links Drafted",
        boundary_section="## Boundary Conditions Draft",
        boundary_id_key="boundary_id",
        consensus_section="## Consensus Draft Queue",
        consensus_statement_key="draft_statement",
        expected_counts={
            "observations": 14,
            "author_claims": 16,
            "evidence_links": 40,
            "boundary_records": 8,
            "consensus_drafts": 8,
        },
        required_phrases=(
            "CONSENSUS-READY FIRST PASS",
            "Module 8 first-pass curation freeze",
            "MET FOR ALL FIRST-PASS TOPICS",
        ),
    ),
    "9b": ModuleConfig(
        key="9b",
        label="Module 9B",
        tracker=ROOT / "modules" / "Module_9B_TRACKER.md",
        output=ROOT / "data" / "processed" / "module9_evidence_bundle.json",
        id_prefix="M9B",
        boundary_prefix="M9B-B",
        evidence_link_section="## Pass 6: Evidence Links Drafted",
        boundary_section="## Boundary Conditions Draft",
        boundary_id_key="boundary_id",
        consensus_section="## Consensus Draft Queue",
        consensus_statement_key="draft_statement",
        expected_counts={
            "observations": 17,
            "author_claims": 17,
            "evidence_links": 40,
            "boundary_records": 8,
            "consensus_drafts": 8,
        },
        required_phrases=(
            "CONSENSUS-READY FIRST PASS",
            "Module 9 first-pass curation freeze",
            "MET FOR ALL FIRST-PASS TOPICS",
        ),
    ),
    "10b": ModuleConfig(
        key="10b",
        label="Module 10B",
        tracker=ROOT / "modules" / "Module_10B_TRACKER.md",
        output=ROOT / "data" / "processed" / "module10_evidence_bundle.json",
        id_prefix="M10B",
        boundary_prefix="M10B-B",
        evidence_link_section="## Pass 6: Evidence Links Drafted",
        boundary_section="## Boundary Conditions Draft",
        boundary_id_key="boundary_id",
        consensus_section="## Consensus Draft Queue",
        consensus_statement_key="draft_statement",
        expected_counts={
            "observations": 80,
            "author_claims": 36,
            "evidence_links": 116,
            "boundary_records": 8,
            "consensus_drafts": 8,
        },
        required_phrases=(
            "CONSENSUS-READY FIRST PASS",
            "Module 10 first-pass curation freeze",
            "MET FOR ALL FIRST-PASS TOPICS",
        ),
    ),
    "11b": ModuleConfig(
        key="11b",
        label="Module 11B",
        tracker=ROOT / "modules" / "Module_11B_TRACKER.md",
        output=ROOT / "data" / "processed" / "module11_evidence_bundle.json",
        id_prefix="M11B",
        boundary_prefix="M11B-B",
        evidence_link_section="## Pass 6: Evidence Links Drafted",
        boundary_section="## Boundary Conditions Draft",
        boundary_id_key="boundary_id",
        consensus_section="## Consensus Draft Queue",
        consensus_statement_key="draft_statement",
        expected_counts={
            "observations": 32,
            "author_claims": 32,
            "evidence_links": 72,
            "boundary_records": 8,
            "consensus_drafts": 8,
        },
        required_phrases=(
            "CONSENSUS-READY FIRST PASS",
            "Module 11 first-pass curation freeze",
            "MET FOR ALL FIRST-PASS TOPICS",
        ),
    ),
    "12b": ModuleConfig(
        key="12b",
        label="Module 12B",
        tracker=ROOT / "modules" / "Module_12B_TRACKER.md",
        output=ROOT / "data" / "processed" / "module12_evidence_bundle.json",
        id_prefix="M12B",
        boundary_prefix="M12B-B",
        evidence_link_section="## Pass 6: Evidence Links Drafted",
        boundary_section="## Boundary Conditions Draft",
        boundary_id_key="boundary_id",
        consensus_section="## Consensus Draft Queue",
        consensus_statement_key="draft_statement",
        expected_counts={
            "observations": 24,
            "author_claims": 24,
            "evidence_links": 56,
            "boundary_records": 8,
            "consensus_drafts": 8,
        },
        required_phrases=(
            "CONSENSUS-READY FIRST PASS",
            "Module 12 first-pass curation freeze",
            "MET FOR ALL FIRST-PASS TOPICS",
        ),
    ),
    "13b": ModuleConfig(
        key="13b",
        label="Module 13B",
        tracker=ROOT / "modules" / "Module_13B_TRACKER.md",
        output=ROOT / "data" / "processed" / "module13_evidence_bundle.json",
        id_prefix="M13B",
        boundary_prefix="M13B-B",
        evidence_link_section="## Pass 6: Evidence Links Drafted",
        boundary_section="## Boundary Conditions Draft",
        boundary_id_key="boundary_id",
        consensus_section="## Consensus Draft Queue",
        consensus_statement_key="draft_statement",
        expected_counts={
            "observations": 24,
            "author_claims": 24,
            "evidence_links": 56,
            "boundary_records": 8,
            "consensus_drafts": 8,
        },
        required_phrases=(
            "CONSENSUS-READY FIRST PASS",
            "Module 13 first-pass curation freeze",
            "MET FOR ALL FIRST-PASS TOPICS",
        ),
    ),
    "14b": ModuleConfig(
        key="14b",
        label="Module 14B",
        tracker=ROOT / "modules" / "Module_14B_TRACKER.md",
        output=ROOT / "data" / "processed" / "module14_evidence_bundle.json",
        id_prefix="M14B",
        boundary_prefix="M14B-B",
        evidence_link_section="## Pass 6: Evidence Links Drafted",
        boundary_section="## Boundary Conditions Draft",
        boundary_id_key="boundary_id",
        consensus_section="## Consensus Draft Queue",
        consensus_statement_key="draft_statement",
        expected_counts={
            "observations": 16,
            "author_claims": 16,
            "evidence_links": 40,
            "boundary_records": 8,
            "consensus_drafts": 8,
        },
        required_phrases=(
            "CONSENSUS-READY FIRST PASS",
            "Module 14 first-pass curation freeze",
            "MET FOR ALL FIRST-PASS TOPICS",
        ),
    ),
    "15b": ModuleConfig(
        key="15b",
        label="Module 15B",
        tracker=ROOT / "modules" / "Module_15B_TRACKER.md",
        output=ROOT / "data" / "processed" / "module15_evidence_bundle.json",
        id_prefix="M15B",
        boundary_prefix="M15B-B",
        evidence_link_section="## Pass 6: Evidence Links Drafted",
        boundary_section="## Boundary Conditions Draft",
        boundary_id_key="boundary_id",
        consensus_section="## Consensus Draft Queue",
        consensus_statement_key="draft_statement",
        expected_counts={
            "observations": 16,
            "author_claims": 16,
            "evidence_links": 40,
            "boundary_records": 8,
            "consensus_drafts": 8,
        },
        required_phrases=(
            "CONSENSUS-READY FIRST PASS",
            "Module 15 first-pass curation freeze",
            "MET FOR ALL FIRST-PASS TOPICS",
        ),
    ),
}


SECTION_TITLES = {
    "observations": "## Pass 4A: Atomic Observations Extracted",
    "author_claims": "## Pass 5A: Author Claims Extracted",
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


def normalize_rows(rows: list[dict[str, str]], kind: str, config: ModuleConfig) -> list[dict[str, str]]:
    normalized: list[dict[str, str]] = []
    for row in rows:
        item = dict(row)
        if kind == "observations":
            add_alias(item, "observation_id", "tracker_id")
        elif kind == "author_claims":
            add_alias(item, "claim_id", "tracker_id")
        elif kind == "evidence_links":
            add_alias(item, "link_id", "tracker_id")
            add_alias(item, "evidence_link_id", "tracker_id")
        elif kind == "boundary_records":
            add_alias(item, config.boundary_id_key, "tracker_id")
        elif kind == "consensus_drafts":
            add_alias(item, "consensus_draft_id", "tracker_id")
            add_alias(item, "consensus_id", "tracker_id")
            add_alias(item, config.consensus_statement_key, "consensus_statement")
        normalized.append(item)
    return normalized


def expand_prefixed_range(prefix: str, start: str, end: str) -> list[str]:
    return [f"{prefix}{num:03d}" for num in range(int(start), int(end) + 1)]


def referenced_ids(text: str, full_prefix: str) -> list[str]:
    """Extract full and shorthand tracker IDs from prose.

    Handles forms like `M2B-O004-O008`, `O024-O029`, `M1B-C001/M1B-C002`,
    and `all boundary records`.
    """

    ids: list[str] = []
    seen: set[str] = set()
    short_prefix = full_prefix.rsplit("-", 1)[-1]
    pattern = re.compile(
        rf"\b(?:(?:{re.escape(full_prefix)})|(?:{re.escape(short_prefix)}))"
        r"(\d{3})(?:-(?:(?:"
        + re.escape(full_prefix)
        + r")|(?:"
        + re.escape(short_prefix)
        + r"))?(\d{3}))?\b"
    )
    for match in pattern.finditer(text):
        start, end = match.groups()
        expanded = expand_prefixed_range(full_prefix, start, end) if end else [f"{full_prefix}{start}"]
        for item in expanded:
            if item not in seen:
                seen.add(item)
                ids.append(item)
    return ids


def validate_contiguous(label: str, ids: set[str], prefix: str) -> list[str]:
    if not ids:
        return [f"{label}: no IDs found"]
    nums = sorted(int(item.removeprefix(prefix)) for item in ids)
    expected = list(range(nums[0], nums[-1] + 1))
    missing = sorted(set(expected) - set(nums))
    if missing:
        return [f"{label}: missing numeric IDs {missing}"]
    return []


def build_bundle(config: ModuleConfig) -> dict[str, Any]:
    markdown = config.tracker.read_text()
    bundle: dict[str, Any] = {
        "source_tracker": str(config.tracker.relative_to(ROOT)),
        "module": config.label,
        "status": "first-pass evidence bundle exported from tracker rows",
        "observations": normalize_rows(
            extract_table(markdown, SECTION_TITLES["observations"]), "observations", config
        ),
        "author_claims": normalize_rows(
            extract_table(markdown, SECTION_TITLES["author_claims"]), "author_claims", config
        ),
        "evidence_links": normalize_rows(
            extract_table(markdown, config.evidence_link_section), "evidence_links", config
        ),
        "boundary_records": normalize_rows(
            extract_table(markdown, config.boundary_section), "boundary_records", config
        ),
        "consensus_drafts": normalize_rows(
            extract_table(markdown, config.consensus_section), "consensus_drafts", config
        ),
    }
    return bundle


def validate_bundle(bundle: dict[str, Any], config: ModuleConfig) -> list[str]:
    errors: list[str] = []
    markdown = config.tracker.read_text()
    observation_prefix = f"{config.id_prefix}-O"
    claim_prefix = f"{config.id_prefix}-C"
    link_prefix = f"{config.id_prefix}-L"
    consensus_prefix = f"{config.id_prefix}-S"

    for key, expected in config.expected_counts.items():
        actual = len(bundle[key])
        if actual != expected:
            errors.append(f"{key}: expected {expected}, found {actual}")

    observation_ids = {row["tracker_id"] for row in bundle["observations"]}
    claim_ids = {row["tracker_id"] for row in bundle["author_claims"]}
    link_ids = {row["tracker_id"] for row in bundle["evidence_links"]}
    boundary_ids = {row["tracker_id"] for row in bundle["boundary_records"]}
    consensus_ids = {row["tracker_id"] for row in bundle["consensus_drafts"]}

    errors.extend(validate_contiguous("observations", observation_ids, observation_prefix))
    errors.extend(validate_contiguous("author_claims", claim_ids, claim_prefix))
    errors.extend(validate_contiguous("evidence_links", link_ids, link_prefix))
    errors.extend(validate_contiguous("boundary_records", boundary_ids, config.boundary_prefix))
    errors.extend(validate_contiguous("consensus_drafts", consensus_ids, consensus_prefix))

    for link in bundle["evidence_links"]:
        link_id = link["tracker_id"]
        if link["claim_id"] not in claim_ids:
            errors.append(f"{link_id}: unknown claim_id {link['claim_id']}")
        if link["observation_id"] not in observation_ids:
            errors.append(f"{link_id}: unknown observation_id {link['observation_id']}")

    linked_claims = {link["claim_id"] for link in bundle["evidence_links"]}
    missing_claim_links = sorted(claim_ids - linked_claims)
    if missing_claim_links:
        errors.append(f"claims without evidence links: {missing_claim_links}")

    for boundary in bundle["boundary_records"]:
        text = " ".join(str(value) for value in boundary.values())
        for observation_id in referenced_ids(text, observation_prefix):
            if observation_id not in observation_ids:
                errors.append(f"{boundary['tracker_id']}: unknown observation reference {observation_id}")
        for claim_id in referenced_ids(text, claim_prefix):
            if claim_id not in claim_ids:
                errors.append(f"{boundary['tracker_id']}: unknown claim reference {claim_id}")

    for draft in bundle["consensus_drafts"]:
        text = " ".join(str(value) for value in draft.values())
        if "all boundary records" not in text.lower():
            for boundary_id in referenced_ids(text, config.boundary_prefix):
                if boundary_id not in boundary_ids:
                    errors.append(f"{draft['tracker_id']}: unknown boundary reference {boundary_id}")
        for observation_id in referenced_ids(text, observation_prefix):
            if observation_id not in observation_ids:
                errors.append(f"{draft['tracker_id']}: unknown observation reference {observation_id}")
        for claim_id in referenced_ids(text, claim_prefix):
            if claim_id not in claim_ids:
                errors.append(f"{draft['tracker_id']}: unknown claim reference {claim_id}")

    for phrase in config.required_phrases:
        if phrase not in markdown:
            errors.append(f"missing readiness marker: {phrase}")

    return errors


def write_bundle(bundle: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(bundle, indent=2) + "\n")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--module",
        choices=sorted(MODULES),
        action="append",
        help="Module key to export/audit. May be repeated. Defaults to all modules.",
    )
    parser.add_argument("--check", action="store_true", help="Validate without writing JSON bundles.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    module_keys = args.module or sorted(MODULES)
    failed = False
    for module_key in module_keys:
        config = MODULES[module_key]
        bundle = build_bundle(config)
        errors = validate_bundle(bundle, config)
        if errors:
            failed = True
            for error in errors:
                print(f"FAIL {config.label}: {error}", file=sys.stderr)
            continue
        counts = ", ".join(f"{key}={len(bundle[key])}" for key in config.expected_counts)
        if args.check:
            print(f"PASS {config.label} evidence bundle: {counts}")
        else:
            write_bundle(bundle, config.output)
            print(f"Wrote {config.output.relative_to(ROOT)} ({counts})")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
