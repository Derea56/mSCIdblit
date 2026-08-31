#!/usr/bin/env python3
"""Validate and normalize local-model TSV triage for ConnectomeDB LR batches.

This script is intentionally conservative:

- source chunk TSVs are treated as the only truth for source-controlled fields
- local-model rows are salvaged only when controlled-vocabulary fields can be
  recovered mechanically from the raw text
- malformed or incomplete rows are pushed into a rerun queue rather than guessed

It is designed for Module 20A database-seed work under work/module20_db_seed/.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path


ANSI_RE = re.compile(r"\x1b\[[0-9;?]*[ -/]*[@-~]")
INTERACTION_ID_RE = re.compile(r"^CDB\d+:\d+$")

ALLOWED_BUCKETS = (
    "keep_direct_seed_with_caution",
    "keep_direct_seed",
    "boundary_review",
    "defer_lower_priority",
)
ALLOWED_SPECIES = (
    "mouse_direct_seed_with_human_ortholog_context",
    "mouse_direct_seed",
)
ALLOWED_ACTIONS = (
    "review_then_primary",
    "hold_for_later_family_pass",
    "primary_first",
)
OUTPUT_HEADERS = [
    "interaction_id",
    "lr_pair",
    "evidence",
    "matched_families",
    "module20a_bucket",
    "reason_short",
    "species_note",
    "next_action",
]


@dataclass
class RowIssue:
    chunk_id: str
    interaction_id: str
    reason: str
    raw_line: str


@dataclass
class ChunkAudit:
    chunk_id: str
    expected_rows: int
    normalized_rows: int = 0
    repaired_rows: int = 0
    skipped_noise_lines: int = 0
    missing_interaction_ids: list[str] = field(default_factory=list)
    duplicate_interaction_ids: list[str] = field(default_factory=list)
    malformed_rows: list[RowIssue] = field(default_factory=list)

    @property
    def status(self) -> str:
        if self.malformed_rows or self.missing_interaction_ids or self.duplicate_interaction_ids:
            return "needs_rerun"
        return "clean"


def parse_args() -> argparse.Namespace:
    root = Path(__file__).resolve().parents[1]
    default_chunk_dir = root / "work" / "module20_db_seed" / "connectomedb_mouse_priority_direct_microchunks"
    default_output_dir = default_chunk_dir / "outputs"
    default_review_dir = default_chunk_dir / "validated"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--chunk-dir", type=Path, default=default_chunk_dir)
    parser.add_argument("--output-dir", type=Path, default=default_output_dir)
    parser.add_argument("--review-dir", type=Path, default=default_review_dir)
    parser.add_argument("--model", default="qwen3.6:latest")
    parser.add_argument("--prompt-dir", type=Path, default=default_chunk_dir / "prompts")
    return parser.parse_args()


def clean_text(text: str) -> str:
    text = ANSI_RE.sub("", text)
    text = text.replace("\r", "")
    return text


def read_source_chunk(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader)


def load_source_chunks(chunk_dir: Path) -> dict[str, list[dict[str, str]]]:
    chunks: dict[str, list[dict[str, str]]] = {}
    for path in sorted(chunk_dir.glob("chunk_*.tsv")):
        if path.parent != chunk_dir:
            continue
        chunks[path.stem] = read_source_chunk(path)
    return chunks


def iter_clean_lines(path: Path) -> list[str]:
    if not path.exists():
        return []
    text = clean_text(path.read_text(encoding="utf-8", errors="replace"))
    lines: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("```"):
            continue
        if line.startswith("interaction_id\t"):
            continue
        lines.append(line)
    return lines


def strip_known_prefix(remainder: str, expected: str) -> tuple[str, bool]:
    if remainder == expected:
        return "", True
    prefix = expected + "\t"
    if remainder.startswith(prefix):
        return remainder[len(prefix):], True
    return remainder, False


def split_tail(tail: str) -> tuple[str, str, str, bool]:
    bucket = next((value for value in ALLOWED_BUCKETS if tail.startswith(value)), "")
    if not bucket:
        return "", "", "", False

    remainder = tail[len(bucket):].lstrip("\t ").rstrip()
    action = next((value for value in ALLOWED_ACTIONS if remainder.endswith(value)), "")
    if not action:
        return "", "", "", False

    before_action = remainder[: -len(action)].rstrip("\t ").rstrip()
    species_match: tuple[int, str] | None = None
    for species in ALLOWED_SPECIES:
        idx = before_action.rfind(species)
        if idx == -1:
            continue
        suffix = before_action[idx + len(species) :]
        if suffix.strip("\t "):
            continue
        if species_match is None or idx > species_match[0]:
            species_match = (idx, species)
    if species_match is None:
        return "", "", "", False

    reason = before_action[: species_match[0]].rstrip("\t ").strip()
    species = species_match[1]
    if not reason:
        return "", "", "", False
    return bucket, reason, species, True


def infer_species_note(source_row: dict[str, str]) -> str:
    human_ligand = source_row.get("human_ligand_symbols", "").strip().lower()
    human_receptor = source_row.get("human_receptor_symbols", "").strip().lower()
    if human_ligand != "no human ortholog" and human_receptor != "no human ortholog":
        return "mouse_direct_seed_with_human_ortholog_context"
    return "mouse_direct_seed"


def normalize_interaction_id(raw_id: str) -> str:
    match = re.fullmatch(r"(CDB\d+):(\d+)", raw_id)
    if not match:
        return raw_id
    prefix, numeric = match.groups()
    return f"{prefix}:{numeric.zfill(7)}"


def extract_bucket_payload(remainder: str) -> tuple[str, str] | None:
    best: tuple[int, str] | None = None
    for bucket in ALLOWED_BUCKETS:
        idx = remainder.find(bucket)
        if idx == -1:
            continue
        if best is None or idx < best[0]:
            best = (idx, bucket)
    if best is None:
        return None
    idx, bucket = best
    tail = remainder[idx:]
    return bucket, tail


def parse_model_row(raw_line: str, source_row: dict[str, str]) -> tuple[dict[str, str] | None, bool, str | None]:
    interaction_id = source_row["interaction_id"]
    lr_pair = source_row["lr_pair"]
    evidence = source_row["evidence"]
    matched_families = source_row["matched_families"]

    raw_parts = raw_line.split("\t")
    if len(raw_parts) < 3:
        return None, False, "prefix_mismatch"
    raw_id = normalize_interaction_id(raw_parts[0])
    if raw_id != interaction_id or raw_parts[1] != lr_pair:
        return None, False, "prefix_mismatch"
    remainder = "\t".join(raw_parts[2:])
    stripped_remainder, stripped_evidence = strip_known_prefix(remainder, evidence)
    tail_source = stripped_remainder if stripped_evidence else remainder
    bucket_payload = extract_bucket_payload(tail_source)
    if bucket_payload is None:
        return None, False, "controlled_vocabulary_parse_failed"
    _, tail = bucket_payload

    bucket, reason, species, ok = split_tail(tail)
    if not ok:
        inferred_species = infer_species_note(source_row)
        for action in ALLOWED_ACTIONS:
            action_idx = tail.rfind(action)
            if action_idx == -1:
                continue
            bucket_value = next((value for value in ALLOWED_BUCKETS if tail.startswith(value)), "")
            reason_text = tail[len(bucket_value):action_idx].strip("\t ").strip()
            if reason_text:
                normalized = {
                    "interaction_id": interaction_id,
                    "lr_pair": lr_pair,
                    "evidence": evidence,
                    "matched_families": matched_families,
                    "module20a_bucket": bucket_value,
                    "reason_short": reason_text,
                    "species_note": inferred_species,
                    "next_action": action,
                }
                repaired = True
                return normalized, repaired, None
        return None, False, "controlled_vocabulary_parse_failed"

    normalized = {
        "interaction_id": interaction_id,
        "lr_pair": lr_pair,
        "evidence": evidence,
        "matched_families": matched_families,
        "module20a_bucket": bucket,
        "reason_short": reason,
        "species_note": species,
        "next_action": next(value for value in ALLOWED_ACTIONS if tail.endswith(value)),
    }
    repaired = "\t".join(normalized[key] for key in OUTPUT_HEADERS) != raw_line
    return normalized, repaired, None


def normalize_chunk(
    chunk_id: str,
    source_rows: list[dict[str, str]],
    output_path: Path,
) -> tuple[list[dict[str, str]], ChunkAudit]:
    audit = ChunkAudit(chunk_id=chunk_id, expected_rows=len(source_rows))
    source_map = {row["interaction_id"]: row for row in source_rows}
    normalized_rows: list[dict[str, str]] = []
    seen_ids: list[str] = []

    for line in iter_clean_lines(output_path):
        first = normalize_interaction_id(line.split("\t", 1)[0])
        if not INTERACTION_ID_RE.fullmatch(first):
            audit.skipped_noise_lines += 1
            continue
        if first not in source_map:
            audit.malformed_rows.append(RowIssue(chunk_id, first, "interaction_id_not_in_source_chunk", line))
            continue
        normalized, repaired, error = parse_model_row(line, source_map[first])
        if normalized is None:
            audit.malformed_rows.append(RowIssue(chunk_id, first, error or "parse_failed", line))
            continue
        normalized_rows.append(normalized)
        seen_ids.append(first)
        if repaired:
            audit.repaired_rows += 1

    duplicates = sorted({interaction_id for interaction_id in seen_ids if seen_ids.count(interaction_id) > 1})
    audit.duplicate_interaction_ids = duplicates
    unique_rows: list[dict[str, str]] = []
    emitted: set[str] = set()
    for row in normalized_rows:
        interaction_id = row["interaction_id"]
        if interaction_id in emitted:
            continue
        emitted.add(interaction_id)
        unique_rows.append(row)

    expected_ids = [row["interaction_id"] for row in source_rows]
    audit.missing_interaction_ids = [interaction_id for interaction_id in expected_ids if interaction_id not in emitted]
    audit.normalized_rows = len(unique_rows)
    return unique_rows, audit


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_HEADERS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def write_markdown_report(
    path: Path,
    audits: list[ChunkAudit],
    total_rows: int,
    clean_rows: int,
    repaired_rows: int,
    rerun_chunks: list[str],
) -> None:
    lines = [
        "# ConnectomeDB Local-Model Batch Validation",
        "",
        "This report is mechanical only. It normalizes rows when controlled-vocabulary parsing is safe and pushes everything else into rerun.",
        "",
        "## Summary",
        "",
        f"- Chunks reviewed: `{len(audits)}`",
        f"- Expected source rows: `{total_rows}`",
        f"- Normalized rows recovered: `{clean_rows}`",
        f"- Mechanically repaired rows: `{repaired_rows}`",
        f"- Chunks needing rerun: `{len(rerun_chunks)}`",
        "",
        "## Chunk Status",
        "",
        "| Chunk | Status | Expected | Normalized | Repaired | Missing IDs | Malformed Rows |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for audit in audits:
        lines.append(
            f"| `{audit.chunk_id}` | `{audit.status}` | `{audit.expected_rows}` | `{audit.normalized_rows}` | `{audit.repaired_rows}` | `{len(audit.missing_interaction_ids)}` | `{len(audit.malformed_rows)}` |"
        )

    lines.extend(["", "## Rerun Queue", ""])
    if rerun_chunks:
        for chunk_id in rerun_chunks:
            lines.append(f"- `{chunk_id}`")
    else:
        lines.append("- None")

    lines.extend(["", "## First Malformed Examples", ""])
    example_count = 0
    for audit in audits:
        for issue in audit.malformed_rows[:3]:
            lines.append(f"- `{issue.chunk_id}` `{issue.interaction_id}`: `{issue.reason}`")
            example_count += 1
            if example_count >= 12:
                break
        if example_count >= 12:
            break
    if example_count == 0:
        lines.append("- None")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_rerun_script(path: Path, rerun_chunks: list[str], prompt_dir: Path, output_dir: Path, model: str) -> None:
    lines = [
        "#!/usr/bin/env bash",
        "set -euo pipefail",
        "",
        f"MODEL={json.dumps(model)}",
        f"PROMPT_DIR={json.dumps(str(prompt_dir))}",
        f"OUTPUT_DIR={json.dumps(str(output_dir))}",
        "",
    ]
    for chunk_id in rerun_chunks:
        prompt = f"$PROMPT_DIR/{chunk_id}_prompt.txt"
        output = f"$OUTPUT_DIR/{chunk_id}_output.tsv"
        lines.extend(
            [
                f"echo \"Rerunning {chunk_id}\"",
                f"/opt/homebrew/bin/ollama run \"$MODEL\" --think=false --hidethinking --nowordwrap < \"{prompt}\" | perl -pe 's{{\\e\\[[0-9;?]*[ -/]*[@-~]}}{{}}g; s/\\r//g;' > \"{output}\"",
                "",
            ]
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    source_chunks = load_source_chunks(args.chunk_dir)
    if not source_chunks:
        raise SystemExit(f"No source chunks found under {args.chunk_dir}")

    normalized_dir = args.review_dir / "normalized_outputs"
    merged_rows: list[dict[str, str]] = []
    audits: list[ChunkAudit] = []
    total_rows = 0

    for chunk_id, source_rows in sorted(source_chunks.items()):
        total_rows += len(source_rows)
        output_path = args.output_dir / f"{chunk_id}_output.tsv"
        rows, audit = normalize_chunk(chunk_id, source_rows, output_path)
        audits.append(audit)
        write_tsv(normalized_dir / f"{chunk_id}_normalized.tsv", rows)
        merged_rows.extend(rows)

    rerun_chunks = [audit.chunk_id for audit in audits if audit.status != "clean"]
    repaired_rows = sum(audit.repaired_rows for audit in audits)
    clean_rows = len(merged_rows)

    write_tsv(args.review_dir / "connectomedb_mouse_priority_direct_validated_merged.tsv", merged_rows)
    write_json(
        args.review_dir / "connectomedb_mouse_priority_direct_validation.json",
        {
            "summary": {
                "chunks_reviewed": len(audits),
                "expected_source_rows": total_rows,
                "normalized_rows": clean_rows,
                "repaired_rows": repaired_rows,
                "rerun_chunks": rerun_chunks,
            },
            "chunks": [asdict(audit) for audit in audits],
        },
    )
    write_markdown_report(
        args.review_dir / "connectomedb_mouse_priority_direct_validation.md",
        audits,
        total_rows,
        clean_rows,
        repaired_rows,
        rerun_chunks,
    )
    write_rerun_script(
        args.review_dir / "rerun_failed_chunks.sh",
        rerun_chunks,
        args.prompt_dir,
        args.output_dir,
        args.model,
    )


if __name__ == "__main__":
    main()
