#!/usr/bin/env python3
"""Audit Module 1 tracker counts and consensus-readiness markers.

The Module 1 curation record currently lives in Markdown trackers. This script
keeps the hand-curated status auditable until a full Markdown-to-SQL loader is
added.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_1A = ROOT / "modules" / "Module_1A_TRACKER.md"
MODULE_1B = ROOT / "modules" / "Module_1B_TRACKER.md"


def unique_ids(pattern: str, text: str) -> set[str]:
    return set(re.findall(pattern, text))


def numeric_suffixes(ids: set[str]) -> list[int]:
    return sorted(int(re.search(r"(\d+)$", item).group(1)) for item in ids)


def check_contiguous(label: str, ids: set[str]) -> list[str]:
    if not ids:
        return [f"FAIL {label}: no IDs found"]

    nums = numeric_suffixes(ids)
    expected = list(range(nums[0], nums[-1] + 1))
    missing = sorted(set(expected) - set(nums))
    if missing:
        return [f"FAIL {label}: missing numeric IDs {missing}"]
    return [f"PASS {label}: {len(ids)} unique IDs, contiguous {nums[0]}-{nums[-1]}"]


def main() -> int:
    one_a = MODULE_1A.read_text()
    one_b = MODULE_1B.read_text()

    checks: list[str] = []

    paper_ids_1b = unique_ids(r"M1A-P\d{3}", one_b)
    experiment_ids_1a = unique_ids(r"M1A-P\d{3}-E\d{3}", one_a)
    observations = unique_ids(r"M1B-O\d{3}", one_b)
    claims = unique_ids(r"M1B-C\d{3}", one_b)
    links = unique_ids(r"M1B-L\d{3}", one_b)
    syntheses = unique_ids(r"M1B-S\d{3}", one_b)
    boundaries = unique_ids(r"M1B-X\d{3}", one_b)

    checks.append(f"PASS Module 1B curated corpus papers: {len(paper_ids_1b)}")
    checks.append(f"PASS Module 1A extracted experiments: {len(experiment_ids_1a)}")
    checks.extend(check_contiguous("Module 1B observations", observations))
    checks.extend(check_contiguous("Module 1B author claims", claims))
    checks.extend(check_contiguous("Module 1B evidence links", links))
    checks.extend(check_contiguous("Module 1B consensus drafts", syntheses))
    checks.extend(check_contiguous("Module 1B boundary records", boundaries))

    expected_counts = {
        "Module 1B curated corpus papers": (len(paper_ids_1b), 30),
        "Module 1A extracted experiments": (len(experiment_ids_1a), 95),
        "Module 1B observations": (len(observations), 84),
        "Module 1B author claims": (len(claims), 50),
        "Module 1B evidence links": (len(links), 107),
        "Module 1B consensus drafts": (len(syntheses), 8),
        "Module 1B boundary records": (len(boundaries), 7),
    }
    for label, (actual, expected) in expected_counts.items():
        if actual != expected:
            checks.append(f"FAIL {label}: expected {expected}, found {actual}")

    required_phrases = [
        "CONSENSUS-READY FIRST PASS",
        "DRAFTED FIRST PASS; CONSENSUS SQL EXPORTED; OBSERVATION LINKS DEFERRED",
        "CONSENSUS SQL EXPORTED; CONSENSUS_OBSERVATION DEFERRED",
        "MET FOR ALL FIRST-PASS TOPICS",
        "Module 1 first-pass curation freeze",
    ]
    for phrase in required_phrases:
        if phrase not in one_b:
            checks.append(f"FAIL Module 1B missing readiness marker: {phrase}")
        else:
            checks.append(f"PASS Module 1B readiness marker present: {phrase}")

    for line in checks:
        print(line)

    return 1 if any(line.startswith("FAIL") for line in checks) else 0


if __name__ == "__main__":
    sys.exit(main())
