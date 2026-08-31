#!/usr/bin/env python3
"""Audit completed Module 20A triage runs and materialize curator review slices."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


HEADERS = [
    "source_record_id",
    "pair_label",
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

KNOWN_AUDIT_FLAGS = {
    "CellChat:CCL8_ACKR4": (
        "Local-model output kept an ACKR-family row as plain keep_direct_seed; "
        "review before any promotion."
    ),
}


def parse_args() -> argparse.Namespace:
    root = Path(__file__).resolve().parents[1]
    overnight_root = root / "work" / "module20_db_seed" / "overnight_runs_v2"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--run-dir",
        type=Path,
        action="append",
        required=True,
        help="Completed triage run directory containing run_status.json and outputs/.",
    )
    parser.add_argument(
        "--combined-output-dir",
        type=Path,
        default=overnight_root / "review_slices_consolidated",
        help="Destination for the merged multi-lane review slices.",
    )
    parser.add_argument(
        "--skip-per-run",
        action="store_true",
        help="Only emit the combined consolidated review slices.",
    )
    return parser.parse_args()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != HEADERS:
            raise SystemExit(
                f"Unexpected header in {path}: {reader.fieldnames!r}; expected {HEADERS!r}"
            )
        return list(reader)


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=HEADERS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def family_terms(family_value: str) -> list[str]:
    return [term.strip() for term in family_value.split(";") if term.strip()]


def source_name(source_record_id: str) -> str:
    return source_record_id.split(":", 1)[0] if ":" in source_record_id else source_record_id


def load_run(run_dir: Path) -> tuple[dict[str, object], list[dict[str, str]]]:
    status_path = run_dir / "run_status.json"
    if not status_path.exists():
        raise SystemExit(f"Missing run status file: {status_path}")
    status = json.loads(status_path.read_text(encoding="utf-8"))
    summary = status.get("summary", {})
    chunks = status.get("chunks", [])
    if not chunks:
        raise SystemExit(f"No chunk manifest found in {status_path}")

    merged_rows: list[dict[str, str]] = []
    for chunk in chunks:
        if chunk.get("status") != "completed":
            raise SystemExit(
                f"Run {run_dir} is not fully completed; chunk {chunk.get('chunk_id')} "
                f"has status {chunk.get('status')!r}"
            )
        output_path = Path(chunk["output_path"])
        if not output_path.exists():
            raise SystemExit(f"Missing normalized chunk output: {output_path}")
        rows = read_tsv(output_path)
        expected_rows = int(chunk.get("row_count", 0))
        if len(rows) != expected_rows:
            raise SystemExit(
                f"Chunk row-count mismatch for {output_path}: got {len(rows)}, "
                f"expected {expected_rows}"
            )
        merged_rows.extend(rows)

    expected_total = int(summary.get("row_count", 0))
    if expected_total and len(merged_rows) != expected_total:
        raise SystemExit(
            f"Run row-count mismatch for {run_dir}: got {len(merged_rows)}, expected {expected_total}"
        )

    seen_ids: set[str] = set()
    duplicates: list[str] = []
    for row in merged_rows:
        record_id = row["source_record_id"]
        if record_id in seen_ids:
            duplicates.append(record_id)
        seen_ids.add(record_id)
    if duplicates:
        duplicate_preview = ", ".join(sorted(set(duplicates))[:10])
        raise SystemExit(f"Duplicate source_record_id values in {run_dir}: {duplicate_preview}")

    lane_name = run_dir.name
    lane_summary = {
        "lane_name": lane_name,
        "task_label": summary.get("task_label", lane_name),
        "input": summary.get("input", ""),
        "row_count": len(merged_rows),
    }
    return lane_summary, merged_rows


def make_summary(
    rows: list[dict[str, str]],
    *,
    title: str,
    lane_rows: dict[str, int] | None = None,
) -> dict[str, object]:
    bucket_counts = Counter(row["module20a_bucket"] for row in rows)
    action_counts = Counter(row["next_action"] for row in rows)
    species_counts = Counter(row["species_note"] for row in rows)
    source_counts = Counter(source_name(row["source_record_id"]) for row in rows)
    family_counts = Counter()
    family_bucket_counts: dict[str, Counter[str]] = defaultdict(Counter)
    family_action_counts: dict[str, Counter[str]] = defaultdict(Counter)

    audit_flags: list[dict[str, str]] = []
    for row in rows:
        record_id = row["source_record_id"]
        if record_id in KNOWN_AUDIT_FLAGS:
            audit_flags.append(
                {
                    "source_record_id": record_id,
                    "pair_label": row["pair_label"],
                    "module20a_bucket": row["module20a_bucket"],
                    "next_action": row["next_action"],
                    "note": KNOWN_AUDIT_FLAGS[record_id],
                }
            )
        for family in family_terms(row["matched_families"]):
            family_counts[family] += 1
            family_bucket_counts[family][row["module20a_bucket"]] += 1
            family_action_counts[family][row["next_action"]] += 1

    return {
        "title": title,
        "row_count": len(rows),
        "lane_rows": dict(sorted((lane_rows or {}).items())),
        "source_counts": dict(sorted(source_counts.items())),
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
        "audit_flags": audit_flags,
    }


def write_summary_markdown(path: Path, summary: dict[str, object]) -> None:
    lines = [
        f"# {summary['title']}",
        "",
        f"- Input rows: `{summary['row_count']}`",
    ]

    lane_rows = summary.get("lane_rows") or {}
    if lane_rows:
        lines.extend(["", "## Lane Counts", ""])
        for key, value in lane_rows.items():
            lines.append(f"- `{key}`: `{value}`")

    lines.extend(["", "## Source Counts", ""])
    for key, value in summary["source_counts"].items():
        lines.append(f"- `{key}`: `{value}`")

    lines.extend(["", "## Bucket Counts", ""])
    for key, value in summary["bucket_counts"].items():
        lines.append(f"- `{key}`: `{value}`")

    lines.extend(["", "## Action Counts", ""])
    for key, value in summary["action_counts"].items():
        lines.append(f"- `{key}`: `{value}`")

    lines.extend(["", "## Species Counts", ""])
    for key, value in summary["species_counts"].items():
        lines.append(f"- `{key}`: `{value}`")

    lines.extend(["", "## Top Families", ""])
    for index, (key, value) in enumerate(summary["family_counts"].items(), start=1):
        if index > 12:
            break
        lines.append(f"- `{key}`: `{value}`")

    audit_flags = summary.get("audit_flags") or []
    if audit_flags:
        lines.extend(["", "## Audit Flags", ""])
        for item in audit_flags:
            lines.append(
                "- "
                f"`{item['source_record_id']}` / `{item['pair_label']}`: "
                f"`{item['module20a_bucket']}` + `{item['next_action']}`. {item['note']}"
            )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def export_review_slices(
    rows: list[dict[str, str]],
    output_dir: Path,
    *,
    title: str,
    lane_rows: dict[str, int] | None = None,
) -> dict[str, object]:
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

    summary = make_summary(rows, title=title, lane_rows=lane_rows)
    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    write_summary_markdown(output_dir / "summary.md", summary)
    return summary


def main() -> None:
    args = parse_args()

    lane_summaries: list[dict[str, object]] = []
    combined_rows: list[dict[str, str]] = []
    lane_counts: dict[str, int] = {}

    for run_dir in args.run_dir:
        lane_summary, rows = load_run(run_dir)
        lane_name = str(lane_summary["lane_name"])
        lane_summaries.append(lane_summary)
        lane_counts[lane_name] = len(rows)
        combined_rows.extend(rows)
        if not args.skip_per_run:
            export_review_slices(
                rows,
                run_dir / "review_slices",
                title=f"Module 20A Review Slice Summary: {lane_name}",
                lane_rows={lane_name: len(rows)},
            )

    export_review_slices(
        combined_rows,
        args.combined_output_dir,
        title="Module 20A Review Slice Summary: Consolidated Completed Overnight Lanes",
        lane_rows=lane_counts,
    )


if __name__ == "__main__":
    main()
