#!/usr/bin/env python3
"""Build a deterministic review queue from the Module 20–24 artifact bridge.

The queue is a review aid only. It does not change the artifact adjudication
layer, the canonical database, or any mechanism graph. Exact source identity,
evidence grade, and context level are carried through unchanged.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data/processed/module20_24_evidence_artifact_provenance_v1/artifact_adjudication.tsv"
DEFAULT_OUTPUT = ROOT / "data/processed/module20_24_database_intake_v1/module20_24_promotion_review_queue.tsv"
DEFAULT_SUMMARY = ROOT / "data/processed/module20_24_database_intake_v1/module20_24_promotion_review_queue_summary.json"

BASE_FIELDS = [
    "artifact_path", "artifact_sha256", "artifact_byte_size", "artifact_role",
    "artifact_identifier_tokens", "module", "register_edge_id",
    "register_evidence_id", "extraction_id", "canonical_paper_key",
    "resolved_pmid", "paper_match_status", "artifact_support_status",
    "evidence_grade", "context_level", "observation_status", "claim_status",
    "source_locator", "candidate_observation_snippet", "candidate_claim_snippet",
    "adjudication_basis",
]
EXTRA_FIELDS = [
    "review_unit_key", "review_route", "priority_rank", "review_batch",
    "source_artifact_exists",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--summary", type=Path, default=DEFAULT_SUMMARY)
    parser.add_argument("--batch-size", type=int, default=100)
    return parser.parse_args()


def evidence_ready(row: dict[str, str]) -> bool:
    observation = row["observation_status"].lower()
    claim = row["claim_status"].lower()
    blocked = ("unresolved" in observation or "unresolved" in claim or
               "abstract_only" in observation or "abstract_only" in claim or
               "not_required" in observation or "unknown" in claim)
    return (
        row["paper_match_status"].startswith("exact_identifier_match")
        and bool(row["resolved_pmid"])
        and not blocked
        and (observation.startswith("validated") or observation.startswith("reused") or observation.startswith("reuse"))
        and (claim.startswith("validated") or claim.startswith("reused") or claim.startswith("reuse"))
    )


def route(row: dict[str, str]) -> str:
    if evidence_ready(row):
        return "identity_resolved_evidence_ready"
    if row["paper_match_status"].startswith("exact_identifier_match") and row["resolved_pmid"]:
        return "identity_resolved_source_review"
    return "identity_resolution_needed"


def grade_rank(value: str) -> int:
    return {"A": 3, "B": 2, "C": 1}.get(value, 0)


def context_rank(value: str) -> int:
    if value.startswith("L") and value[1:].isdigit():
        return int(value[1:])
    return -1


def role_rank(value: str) -> int:
    if "full_text" in value:
        return 3
    if value == "literature_xml":
        return 2
    if "abstract" in value or "metadata" in value:
        return 1
    return 0


def unit_key(row: dict[str, str]) -> str:
    return row["extraction_id"] or f"artifact:{row['artifact_sha256']}"


def main() -> None:
    args = parse_args()
    with args.input.open(newline="", encoding="utf-8", errors="replace") as handle:
        rows = [row for row in csv.DictReader(handle, delimiter="\t")
                if row["artifact_support_status"] == "candidate_requires_review"]

    unit_best: dict[str, tuple] = {}
    for row in rows:
        key = unit_key(row)
        candidate = (
            1 if route(row) == "identity_resolved_evidence_ready" else 0,
            1 if row["paper_match_status"].startswith("exact_identifier_match") else 0,
            bool(row["resolved_pmid"]),
            grade_rank(row["evidence_grade"]),
            context_rank(row["context_level"]),
            role_rank(row["artifact_role"]),
            row["module"], row["register_evidence_id"], row["artifact_path"],
        )
        if key not in unit_best or candidate > unit_best[key][0]:
            unit_best[key] = (candidate, row)

    units = []
    for key, (candidate, row) in unit_best.items():
        units.append((
            key,
            route(row),
            row,
            candidate,
        ))
    units.sort(key=lambda item: (
        0 if item[1] == "identity_resolved_evidence_ready" else
        1 if item[1] == "identity_resolved_source_review" else 2,
        -grade_rank(item[2]["evidence_grade"]),
        -context_rank(item[2]["context_level"]),
        -role_rank(item[2]["artifact_role"]),
        item[2]["module"], item[0], item[2]["register_evidence_id"],
    ))

    ready_by_module: dict[str, list[tuple]] = defaultdict(list)
    for item in units:
        if item[1] == "identity_resolved_evidence_ready":
            ready_by_module[item[2]["module"]].append(item)
    selected_ready: list[tuple] = []
    module_order = sorted(ready_by_module)
    while len(selected_ready) < args.batch_size and module_order:
        progressed = False
        for module in module_order:
            if ready_by_module[module]:
                selected_ready.append(ready_by_module[module].pop(0))
                progressed = True
                if len(selected_ready) == args.batch_size:
                    break
        if not progressed:
            break
    batch_keys = {item[0] for item in selected_ready}
    rank_by_key = {item[0]: index for index, item in enumerate(units, start=1)}

    output_rows = []
    for row in rows:
        key = unit_key(row)
        selected = unit_best[key][1]
        output = dict(row)
        output.update({
            "review_unit_key": key,
            "review_route": route(selected),
            "priority_rank": str(rank_by_key[key]),
            "review_batch": "batch_001" if key in batch_keys else "",
            "source_artifact_exists": str((ROOT / row["artifact_path"]).is_file()).lower(),
        })
        output_rows.append(output)
    output_rows.sort(key=lambda row: (int(row["priority_rank"]), row["artifact_path"], row["register_evidence_id"]))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=BASE_FIELDS + EXTRA_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)

    route_counts = Counter(row["review_route"] for row in output_rows)
    unit_route_counts = Counter(item[1] for item in units)
    batch_rows = [row for row in output_rows if row["review_batch"] == "batch_001"]
    summary = {
        "input": str(args.input),
        "output": str(args.output),
        "candidate_rows": len(rows),
        "distinct_review_units": len(units),
        "candidate_rows_by_route": dict(sorted(route_counts.items())),
        "review_units_by_route": dict(sorted(unit_route_counts.items())),
        "batch_size_requested": args.batch_size,
        "batch_001_units": len(batch_keys),
        "batch_001_rows": len(batch_rows),
        "batch_001_modules": dict(sorted(Counter(row["module"] for row in batch_rows).items())),
        "batch_001_source_artifacts_present": sum(row["source_artifact_exists"] == "true" for row in batch_rows),
        "evidence_grade_preserved": True,
        "context_level_preserved": True,
        "canonical_database_write_performed": False,
    }
    args.summary.parent.mkdir(parents=True, exist_ok=True)
    args.summary.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
