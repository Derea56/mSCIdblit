#!/usr/bin/env python3
"""Prepare and optionally run local-model triage for Module 20A seed TSVs.

This runner is intentionally conservative:

- source rows remain the truth for all source-controlled columns
- the local model only assigns bucket, short reason, species note, and next action
- outputs are chunked so progress can be resumed and audited mechanically
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import shutil
import subprocess
import time
from dataclasses import asdict, dataclass
from pathlib import Path


OUTPUT_HEADERS = [
    "source_record_id",
    "pair_label",
    "matched_families",
    "module20a_bucket",
    "reason_short",
    "species_note",
    "next_action",
]

BUCKETS = [
    "keep_direct_seed_with_caution",
    "keep_direct_seed",
    "boundary_review",
    "defer_lower_priority",
]
NEXT_ACTIONS = [
    "review_then_primary",
    "primary_first",
    "hold_for_later_family_pass",
]


@dataclass
class ChunkStatus:
    chunk_id: str
    row_count: int
    prompt_path: str
    output_path: str
    status: str
    started_at: float | None = None
    finished_at: float | None = None
    return_code: int | None = None


def parse_args() -> argparse.Namespace:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--model", default="qwen2.5-coder:32b")
    parser.add_argument("--chunk-size", type=int, default=40)
    parser.add_argument("--pause-seconds", type=float, default=1.0)
    parser.add_argument("--max-chunks", type=int, default=0)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--run-ollama", action="store_true")
    parser.add_argument(
        "--normalize-existing",
        action="store_true",
        help="Normalize completed local-model TSVs without invoking Ollama.",
    )
    parser.add_argument("--species-note-values", nargs="+", required=True)
    parser.add_argument("--species-note-guidance", required=True)
    parser.add_argument("--row-context-columns", nargs="+", required=True)
    parser.add_argument("--task-label", required=True)
    parser.add_argument("--notes", default="")
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, headers: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def make_prompt(
    *,
    chunk_rows: list[dict[str, str]],
    headers: list[str],
    task_label: str,
    species_note_values: list[str],
    species_note_guidance: str,
    notes: str,
) -> str:
    lines = [
        "You are helping curate `mSCIdblit` Module 20A.",
        "",
        f"Task: {task_label}",
        "- Read the tab-separated source rows below.",
        "- Treat these rows as seed database entries, not final truth.",
        "- Do not invent biology, receptor-complex requirements, SCI context, or evidence beyond the row.",
        "- Use only the information present in the row fields.",
        "- Preserve one output row for every input row in the same order.",
        "- Copy the first three source columns byte-for-byte, including capitalization.",
        "",
        "For each row, output one TSV row with these columns in this exact order:",
        "",
        *[f"`{value}`" for value in OUTPUT_HEADERS],
        "",
        "Allowed values:",
        "",
        f"- `module20a_bucket`: {', '.join(f'`{value}`' for value in BUCKETS)}",
        f"- `species_note`: {', '.join(f'`{value}`' for value in species_note_values)}",
        f"- `next_action`: {', '.join(f'`{value}`' for value in NEXT_ACTIONS)}",
        "",
        "Decision rules:",
        "",
        "- Prefer `keep_direct_seed` for plausible extracellular ligand-receptor pairs that clearly fit Module 20A.",
        "- Use `keep_direct_seed_with_caution` when the pair looks relevant but needs careful interpretation because of complexes, context, or comparator framing.",
        "- Use `boundary_review` when the row may represent adhesion, ECM/contact context, cofactor/context behavior, indirect mediator structure, or a relation that may not cleanly map to a direct ligand-receptor edge.",
        "- Use `defer_lower_priority` when the row is probably outside the current first-pass Module 20A priorities.",
        "- Decoy, scavenger, atypical, or sink receptors should usually be `boundary_review` or `keep_direct_seed_with_caution`, not plain `keep_direct_seed`.",
        "- Contact, ECM, adhesion, protease, and multimeric-complex rows should usually not be plain `keep_direct_seed` unless the row still reads like a clear direct ligand-receptor edge.",
        f"- Species-note guidance: {species_note_guidance}",
        "- `reason_short` must be very short, fewer than 12 words, and must not cite unstated evidence.",
        "- `reason_short` must not contain tab characters.",
        "- Do not output prose before or after the TSV.",
        "- Do not skip rows.",
    ]
    if notes:
        lines.extend(["", f"Additional notes: {notes}"])
    lines.extend(["", "Rows begin after the next line.", ""])
    lines.append("\t".join(headers))
    for row in chunk_rows:
        lines.append("\t".join(row.get(header, "") for header in headers))
    return "\n".join(lines) + "\n"


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def run_chunk(model: str, prompt_path: Path, output_path: Path) -> int:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with prompt_path.open("rb") as prompt_handle, output_path.open("wb") as output_handle:
        process = subprocess.run(
            ["/opt/homebrew/bin/ollama", "run", model, "--think=false", "--hidethinking", "--nowordwrap"],
            stdin=prompt_handle,
            stdout=output_handle,
            stderr=subprocess.PIPE,
            check=False,
        )
    if process.returncode != 0:
        output_path.with_suffix(output_path.suffix + ".stderr.txt").write_bytes(process.stderr)
    return process.returncode


def normalize_output(
    output_path: Path,
    expected_rows: list[dict[str, str]],
    species_note_values: list[str],
) -> list[str]:
    """Normalize harmless TSV formatting drift while rejecting content changes.

    The model may add tabs inside ``reason_short``, repeat the bucket, or omit a
    fixed species note.  This function only repairs those syntactic issues after
    confirming the source identity columns, bucket, and next action are intact.
    """
    raw_lines = [line for line in output_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not raw_lines:
        return ["empty output"]
    if raw_lines[0].split("\t") != OUTPUT_HEADERS:
        return ["unexpected output header"]
    data_lines = raw_lines[1:]
    if len(data_lines) != len(expected_rows):
        return [f"row count {len(data_lines)} does not match expected {len(expected_rows)}"]

    normalized: list[dict[str, str]] = []
    errors: list[str] = []
    for index, (line, expected) in enumerate(zip(data_lines, expected_rows), start=1):
        fields = line.split("\t")
        if len(fields) < 5:
            errors.append(f"row {index}: fewer than five fields")
            continue
        identity = [expected.get(key, "") for key in OUTPUT_HEADERS[:3]]
        if fields[:3] != identity:
            # Case-only drift is formatting, not a biological assertion. Restore
            # the source-controlled spelling; reject every other identity change.
            if [value.casefold() for value in fields[:3]] != [value.casefold() for value in identity]:
                errors.append(f"row {index}: source identity mismatch")
                continue
        bucket = fields[3]
        if bucket not in BUCKETS:
            errors.append(f"row {index}: invalid bucket {bucket!r}")
            continue
        action = fields[-1]
        if action not in NEXT_ACTIONS:
            errors.append(f"row {index}: invalid next action {action!r}")
            continue

        middle = fields[4:-1]
        species_matches = [value for value in middle if value in species_note_values]
        if len(species_matches) == 1:
            species_note = species_matches[0]
            reason_parts = [value for value in middle if value != species_note and value not in BUCKETS]
        elif not species_matches and len(species_note_values) == 1:
            # This run has one mandated species note, so restoration is mechanical.
            species_note = species_note_values[0]
            reason_parts = [value for value in middle if value not in BUCKETS]
        else:
            errors.append(f"row {index}: missing or ambiguous species note")
            continue
        reason_short = " ".join(part.strip() for part in reason_parts if part.strip())
        if not reason_short:
            errors.append(f"row {index}: empty reason")
            continue
        normalized.append(
            dict(zip(OUTPUT_HEADERS, [*identity, bucket, reason_short, species_note, action]))
        )

    if errors:
        return errors

    raw_path = output_path.with_suffix(".raw.tsv")
    if not raw_path.exists():
        shutil.copy2(output_path, raw_path)
    write_tsv(output_path, OUTPUT_HEADERS, normalized)
    return []


def main() -> None:
    args = parse_args()
    rows = read_rows(args.input)
    if not rows:
        raise SystemExit(f"No rows found in {args.input}")

    run_dir = args.run_dir
    prompts_dir = run_dir / "prompts"
    chunks_dir = run_dir / "chunks"
    outputs_dir = run_dir / "outputs"
    headers = list(rows[0].keys())

    for required in ["source_record_id", "pair_label", "matched_families"]:
        if required not in headers:
            raise SystemExit(f"Missing required column `{required}` in {args.input}")
    for required in args.row_context_columns:
        if required not in headers:
            raise SystemExit(f"Missing row-context column `{required}` in {args.input}")

    source_headers = ["source_record_id", "pair_label", "matched_families", *args.row_context_columns]
    source_headers = list(dict.fromkeys(source_headers))

    chunk_total = math.ceil(len(rows) / args.chunk_size)
    manifest: list[ChunkStatus] = []
    for index in range(chunk_total):
        if args.max_chunks and index >= args.max_chunks:
            break
        start = index * args.chunk_size
        stop = min(len(rows), start + args.chunk_size)
        chunk_id = f"chunk_{index + 1:03d}"
        chunk_rows = [{header: row.get(header, "") for header in source_headers} for row in rows[start:stop]]
        chunk_path = chunks_dir / f"{chunk_id}.tsv"
        prompt_path = prompts_dir / f"{chunk_id}_prompt.txt"
        output_path = outputs_dir / f"{chunk_id}_output.tsv"
        write_tsv(chunk_path, source_headers, chunk_rows)
        prompt_text = make_prompt(
            chunk_rows=chunk_rows,
            headers=source_headers,
            task_label=args.task_label,
            species_note_values=args.species_note_values,
            species_note_guidance=args.species_note_guidance,
            notes=args.notes,
        )
        prompt_path.parent.mkdir(parents=True, exist_ok=True)
        prompt_path.write_text(prompt_text, encoding="utf-8")
        status = "pending"
        if args.resume and output_path.exists() and output_path.stat().st_size > 0:
            errors = normalize_output(output_path, chunk_rows, args.species_note_values)
            status = "completed" if not errors else "invalid"
        manifest.append(
            ChunkStatus(
                chunk_id=chunk_id,
                row_count=len(chunk_rows),
                prompt_path=str(prompt_path),
                output_path=str(output_path),
                status=status,
            )
        )

    summary = {
        "input": str(args.input),
        "row_count": len(rows),
        "chunk_size": args.chunk_size,
        "chunk_count": len(manifest),
        "task_label": args.task_label,
        "model": args.model,
        "run_ollama": args.run_ollama,
    }
    write_json(run_dir / "run_config.json", {"summary": summary, "chunks": [asdict(item) for item in manifest]})

    if args.normalize_existing:
        write_json(run_dir / "run_status.json", {"summary": summary, "chunks": [asdict(entry) for entry in manifest]})
        invalid = [item.chunk_id for item in manifest if item.status == "invalid"]
        if invalid:
            raise SystemExit(f"Could not normalize existing chunks: {', '.join(invalid)}")
        return

    if not args.run_ollama:
        return

    for item in manifest:
        output_path = Path(item.output_path)
        if args.resume and item.status == "completed":
            continue
        if item.status == "invalid" and output_path.exists():
            invalid_path = output_path.with_suffix(".invalid.tsv")
            if not invalid_path.exists():
                shutil.copy2(output_path, invalid_path)
        item.status = "running"
        item.started_at = time.time()
        write_json(run_dir / "run_status.json", {"summary": summary, "chunks": [asdict(entry) for entry in manifest]})
        return_code = run_chunk(args.model, Path(item.prompt_path), output_path)
        if return_code == 0:
            errors = normalize_output(
                output_path,
                read_rows(chunks_dir / f"{item.chunk_id}.tsv"),
                args.species_note_values,
            )
            if errors:
                output_path.with_suffix(output_path.suffix + ".validation.txt").write_text(
                    "\n".join(errors) + "\n", encoding="utf-8"
                )
                return_code = 2
        item.return_code = return_code
        item.finished_at = time.time()
        item.status = "completed" if return_code == 0 else "failed"
        write_json(run_dir / "run_status.json", {"summary": summary, "chunks": [asdict(entry) for entry in manifest]})
        if return_code != 0:
            raise SystemExit(return_code)
        if args.pause_seconds > 0:
            time.sleep(args.pause_seconds)

    write_json(run_dir / "run_status.json", {"summary": summary, "chunks": [asdict(entry) for entry in manifest]})


if __name__ == "__main__":
    main()
