#!/usr/bin/env python3
"""Materialize curator review slices from a validated ConnectomeDB LR triage TSV."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


HEADERS = [
    "interaction_id",
    "lr_pair",
    "evidence",
    "matched_families",
    "module20a_bucket",
    "reason_short",
    "species_note",
    "next_action",
]

PRIORITY_QUEUE_SPECS = [
    (
        "01_keep_direct_seed_review_then_primary.tsv",
        lambda row: row["module20a_bucket"] == "keep_direct_seed"
        and row["next_action"] == "review_then_primary",
    ),
    (
        "02_keep_direct_seed_with_caution_review_then_primary.tsv",
        lambda row: row["module20a_bucket"] == "keep_direct_seed_with_caution"
        and row["next_action"] == "review_then_primary",
    ),
    (
        "03_boundary_review.tsv",
        lambda row: row["module20a_bucket"] == "boundary_review",
    ),
    (
        "04_primary_first.tsv",
        lambda row: row["next_action"] == "primary_first",
    ),
    (
        "05_hold_for_later_family_pass.tsv",
        lambda row: row["next_action"] == "hold_for_later_family_pass",
    ),
]


def parse_args() -> argparse.Namespace:
    root = Path(__file__).resolve().parents[1]
    validated_dir = (
        root
        / "work"
        / "module20_db_seed"
        / "connectomedb_mouse_priority_direct_microchunks"
        / "validated"
    )
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=validated_dir / "connectomedb_mouse_priority_direct_validated_merged.tsv",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=validated_dir / "review_slices",
    )
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=HEADERS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def family_terms(family_value: str) -> list[str]:
    return [term.strip() for term in family_value.split(";") if term.strip()]


def make_summary(rows: list[dict[str, str]]) -> dict[str, object]:
    bucket_counts = Counter(row["module20a_bucket"] for row in rows)
    action_counts = Counter(row["next_action"] for row in rows)
    species_counts = Counter(row["species_note"] for row in rows)
    family_counts = Counter()
    family_bucket_counts: dict[str, Counter[str]] = defaultdict(Counter)
    family_action_counts: dict[str, Counter[str]] = defaultdict(Counter)

    for row in rows:
        for family in family_terms(row["matched_families"]):
            family_counts[family] += 1
            family_bucket_counts[family][row["module20a_bucket"]] += 1
            family_action_counts[family][row["next_action"]] += 1

    return {
        "row_count": len(rows),
        "bucket_counts": dict(sorted(bucket_counts.items())),
        "action_counts": dict(sorted(action_counts.items())),
        "species_counts": dict(sorted(species_counts.items())),
        "family_counts": dict(family_counts.most_common()),
        "family_bucket_counts": {
            family: dict(sorted(counts.items()))
            for family, counts in sorted(
                family_bucket_counts.items(),
                key=lambda item: (-family_counts[item[0]], item[0]),
            )
        },
        "family_action_counts": {
            family: dict(sorted(counts.items()))
            for family, counts in sorted(
                family_action_counts.items(),
                key=lambda item: (-family_counts[item[0]], item[0]),
            )
        },
    }


def write_summary_markdown(path: Path, summary: dict[str, object]) -> None:
    bucket_counts = summary["bucket_counts"]
    action_counts = summary["action_counts"]
    species_counts = summary["species_counts"]
    family_counts = summary["family_counts"]

    lines = [
        "# ConnectomeDB Review Slice Summary",
        "",
        f"- Input rows: `{summary['row_count']}`",
        "",
        "## Bucket Counts",
        "",
    ]
    for key, value in bucket_counts.items():
        lines.append(f"- `{key}`: `{value}`")

    lines.extend(["", "## Action Counts", ""])
    for key, value in action_counts.items():
        lines.append(f"- `{key}`: `{value}`")

    lines.extend(["", "## Species Counts", ""])
    for key, value in species_counts.items():
        lines.append(f"- `{key}`: `{value}`")

    lines.extend(["", "## Top Families", ""])
    for index, (key, value) in enumerate(family_counts.items(), start=1):
        if index > 12:
            break
        lines.append(f"- `{key}`: `{value}`")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    rows = read_rows(args.input)
    if not rows:
        raise SystemExit(f"No rows found in {args.input}")

    output_dir = args.output_dir
    by_bucket_dir = output_dir / "by_bucket"
    by_action_dir = output_dir / "by_action"
    by_family_dir = output_dir / "by_family"
    priority_dir = output_dir / "priority_queues"

    write_tsv(output_dir / "all_rows.tsv", rows)

    bucket_groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    action_groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    family_groups: dict[str, list[dict[str, str]]] = defaultdict(list)

    for row in rows:
        bucket_groups[row["module20a_bucket"]].append(row)
        action_groups[row["next_action"]].append(row)
        for family in family_terms(row["matched_families"]):
            family_groups[family].append(row)

    for bucket, group_rows in sorted(bucket_groups.items()):
        write_tsv(by_bucket_dir / f"{bucket}.tsv", group_rows)
    for action, group_rows in sorted(action_groups.items()):
        write_tsv(by_action_dir / f"{action}.tsv", group_rows)
    for family, group_rows in sorted(family_groups.items()):
        write_tsv(by_family_dir / f"{family}.tsv", group_rows)

    for filename, predicate in PRIORITY_QUEUE_SPECS:
        write_tsv(priority_dir / filename, [row for row in rows if predicate(row)])

    summary = make_summary(rows)
    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    write_summary_markdown(output_dir / "summary.md", summary)


if __name__ == "__main__":
    main()
