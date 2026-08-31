#!/usr/bin/env python3
"""Inventory untracked local artifacts without deleting or moving anything.

The inventory separates source evidence from derived outputs, reproducibility
code, and local caches. For database-backed rows, the database still stores
structured provenance rather than the source file itself, so an artifact is
reported as database-linked only when its exact path appears in current local
database notes.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import subprocess
from collections import Counter
from pathlib import Path


DEFAULT_DATABASE_URL = (
    "postgresql:///mscidblit_local?host=/private/tmp/mscidblit_pg_socket&port=55432"
)
DEFAULT_OUTPUT = Path("data/processed/local_artifact_inventory_v1.tsv")
DEFAULT_REPORT = Path("docs/LOCAL_ARTIFACT_RETENTION_INVENTORY_2026-08-31.md")

DB_TABLES = (
    "evidencelink",
    "observation",
    "experiment",
    "authorclaim",
    "signalingedgesource",
)
DB_PATH_RE = re.compile(r"data/(?:raw|processed)/[^\s;,'\"`})]+")

FIELDS = [
    "path",
    "artifact_class",
    "retention_recommendation",
    "database_reference_count",
    "database_link_status",
    "size_bytes",
    "sha256",
]


def run(command: list[str], *, input_text: str | None = None) -> str:
    result = subprocess.run(
        command,
        input=input_text,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    return result.stdout


def untracked_paths(excluded: set[Path]) -> list[Path]:
    raw = run(["git", "status", "--porcelain=v1", "-z", "--untracked-files=all"])
    paths: list[Path] = []
    for record in raw.split("\0"):
        if record.startswith("?? "):
            path = Path(record[3:])
            if path not in excluded:
                paths.append(path)
    return sorted(paths)


def classify(path: Path) -> tuple[str, str]:
    text = path.as_posix()
    if text.startswith(".repowise/"):
        return "local_cache", "safe_to_remove_after_index_review"
    if text in {".mcp.json", "AGENTS.md"} or text.startswith(".vscode/"):
        return "local_configuration", "keep_local_do_not_publish"
    if text.startswith("data/raw/evidence/"):
        return "source_evidence", "retain_until_release_freeze"
    if text.startswith("data/raw/public_database_snapshots/"):
        return "reference_snapshot", "retain_externally_with_manifest"
    if text.startswith("data/processed/"):
        return "derived_output", "review_reproducibility_then_archive"
    if text.startswith("scripts/"):
        return "reproducibility_code", "review_for_commit_or_archive"
    if text.startswith("docs/") or text.startswith("modules/"):
        return "research_documentation", "review_for_commit_or_archive"
    if path.name.startswith("_") and path.suffix == ".py":
        return "local_helper", "review_for_archive_or_removal"
    return "other_local_artifact", "manual_review"


def database_references(database_url: str) -> Counter[str]:
    counts: Counter[str] = Counter()
    for table in DB_TABLES:
        sql = (
            f"SELECT notes FROM {table} "
            "WHERE notes LIKE '%data/raw/%' OR notes LIKE '%data/processed/%';"
        )
        for note in run(["psql", database_url, "-X", "-At", "-c", sql]).splitlines():
            for match in DB_PATH_RE.findall(note):
                counts[match.rstrip(".")] += 1
    return counts


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_inventory(rows: list[dict[str, str]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_report(rows: list[dict[str, str]], report: Path, output: Path) -> None:
    by_class = Counter(row["artifact_class"] for row in rows)
    by_status = Counter(row["database_link_status"] for row in rows)
    sizes = Counter()
    for row in rows:
        sizes[row["artifact_class"]] += int(row["size_bytes"])
    lines = [
        "# Local artifact retention inventory — 2026-08-31",
        "",
        "This report is a non-destructive inventory of files reported by Git as",
        "untracked. It does not imply that an artifact is safe to delete. The",
        "database-link status means only that the exact path occurs in current",
        "database provenance notes; database rows do not contain the source file.",
        "",
        f"- Inventory TSV: `{output.as_posix()}`",
        f"- Untracked files inventoried: {len(rows):,}",
        "",
        "| Artifact class | Files | Bytes | Recommendation |",
        "|---|---:|---:|---|",
    ]
    recommendations = {row["artifact_class"]: row["retention_recommendation"] for row in rows}
    for artifact_class in sorted(by_class):
        lines.append(
            f"| `{artifact_class}` | {by_class[artifact_class]:,} | "
            f"{sizes[artifact_class]:,} | `{recommendations[artifact_class]}` |"
        )
    lines.extend(
        [
            "",
            "| Database link status | Files |",
            "|---|---:|",
        ]
    )
    for status in sorted(by_status):
        lines.append(f"| `{status}` | {by_status[status]:,} |")
    lines.extend(
        [
            "",
            "Recommended next action: retain source evidence and reference",
            "snapshots through release freeze; review derived outputs and code",
            "for reproducibility; then archive or remove only explicitly approved",
            "superseded files. Local caches and configuration should not enter the",
            "public release.",
            "",
        ]
    )
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(lines))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--database-url", default=DEFAULT_DATABASE_URL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--no-checksums", action="store_true")
    args = parser.parse_args()

    references = database_references(args.database_url)
    script_path = Path(__file__).resolve().relative_to(Path.cwd().resolve())
    excluded = {script_path, args.output, args.report}
    rows: list[dict[str, str]] = []
    for path in untracked_paths(excluded):
        artifact_class, recommendation = classify(path)
        path_text = path.as_posix()
        reference_count = references.get(path_text, 0)
        rows.append(
            {
                "path": path_text,
                "artifact_class": artifact_class,
                "retention_recommendation": recommendation,
                "database_reference_count": str(reference_count),
                "database_link_status": "exact_path_referenced" if reference_count else "not_referenced_by_current_db_notes",
                "size_bytes": str(path.stat().st_size),
                "sha256": "" if args.no_checksums else sha256(path),
            }
        )
    write_inventory(rows, args.output)
    write_report(rows, args.report, args.output)
    print(f"files={len(rows):,} output={args.output} report={args.report}")


if __name__ == "__main__":
    main()
