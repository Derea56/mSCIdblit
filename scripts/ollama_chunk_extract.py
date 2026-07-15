#!/usr/bin/env python3
"""Prepare small, auditable extraction prompts for local Ollama models.

This script does not curate rows into the database. It creates narrow source
chunks and prompt files, optionally sends each prompt to Ollama, and writes a
sanity report so a curator can decide what to trust.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import textwrap
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


SECTION_PATTERNS = {
    "abstract": re.compile(r"^\s*(abstract|summary)\s*$", re.I),
    "introduction": re.compile(r"^\s*(\d+\.?\s*)?(introduction|background)\s*$", re.I),
    "methods": re.compile(
        r"^\s*(\d+\.?\s*)?(materials?\s+and\s+methods|methods|experimental\s+procedures)\s*$",
        re.I,
    ),
    "results": re.compile(r"^\s*(\d+\.?\s*)?results\s*$", re.I),
    "discussion": re.compile(r"^\s*(\d+\.?\s*)?(discussion|conclusion|conclusions)\s*$", re.I),
    "references": re.compile(r"^\s*(references|bibliography)\s*$", re.I),
}

FIGURE_CAPTION_RE = re.compile(r"^\s*(?:Fig(?:ure)?\.?|Supplementary\s+Fig(?:ure)?\.?)\s*([0-9]+[A-Za-z]?)\b", re.I)
RESULT_SUBSECTION_RE = re.compile(r"^\s*(3\.\d+\.?)\s+(.{8,120})$")
METHOD_KEYWORDS = re.compile(
    r"\b("
    r"mouse|mice|rat|rats|spinal cord injury|contusion|compression|transection|clip|"
    r"infinite horizons|impact|kdyn|transplant|culture|immunostain|histolog|section|"
    r"bms|bbb|lesion|scar|gfap|fibronectin|collagen|pdgfr|flow cytometry"
    r")\b",
    re.I,
)
SUSPICIOUS_IN_VITRO_RE = re.compile(
    r"(in[_ -]?vitro|culture|astrocyte culture|cell culture).{0,120}"
    r"(infinite horizons|ih impactor|kdyn|\bt[0-9]{1,2}\b|contusion)",
    re.I | re.S,
)
TASKS = ("extract", "triage", "methods_metadata", "figure_candidate_experiments", "row_sanity_check")


@dataclass
class Chunk:
    chunk_id: str
    chunk_type: str
    title: str
    start_line: int
    end_line: int
    source_excerpt: str


def normalize_text(text: str) -> str:
    text = text.replace("\x00", "")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip() + "\n"


def read_source_text(args: argparse.Namespace) -> str:
    if args.source_text:
        return Path(args.source_text).read_text(encoding="utf-8", errors="replace")
    if args.pdf:
        try:
            from pypdf import PdfReader  # type: ignore
        except ImportError as exc:
            raise SystemExit(
                "--pdf requires the optional pypdf package. Extract text first and pass --source-text, "
                "or install pypdf."
            ) from exc
        reader = PdfReader(args.pdf)
        return "\n\n".join(page.extract_text() or "" for page in reader.pages)
    raise SystemExit("Provide either --source-text or --pdf.")


def section_bounds(lines: list[str]) -> dict[str, tuple[int, int]]:
    starts: dict[str, int] = {}
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if not stripped or len(stripped) > 80:
            continue
        for name, pattern in SECTION_PATTERNS.items():
            if pattern.match(stripped) and name not in starts:
                starts[name] = idx

    ordered = sorted(starts.items(), key=lambda item: item[1])
    bounds: dict[str, tuple[int, int]] = {}
    for pos, (name, start) in enumerate(ordered):
        end = ordered[pos + 1][1] if pos + 1 < len(ordered) else len(lines)
        bounds[name] = (start, end)
    return bounds


def bounded_text(lines: list[str], start: int, end: int, max_chars: int) -> str:
    excerpt = "\n".join(lines[start:end]).strip()
    if len(excerpt) <= max_chars:
        return excerpt
    return excerpt[:max_chars].rsplit("\n", 1)[0].strip()


def split_long_text(chunk_id: str, chunk_type: str, title: str, start_line: int, text: str, max_chars: int) -> list[Chunk]:
    if len(text) <= max_chars:
        line_count = max(1, text.count("\n") + 1)
        return [Chunk(chunk_id, chunk_type, title, start_line, start_line + line_count - 1, text)]

    chunks: list[Chunk] = []
    paragraphs = re.split(r"\n\s*\n", text)
    current: list[str] = []
    current_start = start_line
    line_cursor = start_line
    part = 1

    for para in paragraphs:
        para = para.strip()
        if not para:
            line_cursor += 1
            continue
        candidate = "\n\n".join(current + [para]).strip()
        if current and len(candidate) > max_chars:
            body = "\n\n".join(current).strip()
            line_count = max(1, body.count("\n") + 1)
            chunks.append(
                Chunk(
                    f"{chunk_id}_part{part:02d}",
                    chunk_type,
                    f"{title} part {part}",
                    current_start,
                    current_start + line_count - 1,
                    body,
                )
            )
            part += 1
            current = [para]
            current_start = line_cursor
        else:
            current.append(para)
        line_cursor += max(1, para.count("\n") + 2)

    if current:
        body = "\n\n".join(current).strip()
        line_count = max(1, body.count("\n") + 1)
        chunks.append(
            Chunk(
                f"{chunk_id}_part{part:02d}" if part > 1 else chunk_id,
                chunk_type,
                f"{title} part {part}" if part > 1 else title,
                current_start,
                current_start + line_count - 1,
                body,
            )
        )
    return chunks


def make_chunks(text: str, max_chars: int, figure_context_lines: int, front_chars: int) -> list[Chunk]:
    lines = text.splitlines()
    bounds = section_bounds(lines)
    chunks: list[Chunk] = []

    front_end = min(len(lines), max(1, text[:front_chars].count("\n") + 1))
    chunks.append(
        Chunk(
            "front_matter",
            "paper_context",
            "Title, abstract, and opening context",
            1,
            front_end,
            bounded_text(lines, 0, front_end, front_chars),
        )
    )

    if "methods" in bounds:
        start, end = bounds["methods"]
        methods_lines = [line for line in lines[start:end] if METHOD_KEYWORDS.search(line) or len(line.strip()) > 40]
        methods_text = "\n".join(methods_lines).strip()
        chunks.extend(split_long_text("methods_core", "methods", "Methods relevant to experiment metadata", start + 1, methods_text, max_chars))

    if "results" in bounds:
        results_start, results_end = bounds["results"]
        subsection_starts: list[tuple[int, str]] = []
        for idx in range(results_start, results_end):
            match = RESULT_SUBSECTION_RE.match(lines[idx].strip())
            if match:
                subsection_starts.append((idx, f"{match.group(1)} {match.group(2)}"))
        for pos, (start, heading) in enumerate(subsection_starts):
            end = subsection_starts[pos + 1][0] if pos + 1 < len(subsection_starts) else results_end
            subsection_id = re.sub(r"[^a-z0-9]+", "_", heading.lower()).strip("_")[:60]
            body = "\n".join(lines[start:end]).strip()
            chunks.extend(split_long_text(f"results_{subsection_id}", "results_subsection", heading, start + 1, body, max_chars))

    figure_windows: list[tuple[int, int, str]] = []
    for idx, line in enumerate(lines):
        match = FIGURE_CAPTION_RE.search(line)
        if not match:
            continue
        start = max(0, idx - min(12, figure_context_lines))
        end = min(len(lines), idx + figure_context_lines + 1)
        label = re.sub(r"\s+", "_", match.group(0).lower().replace(".", ""))
        figure_windows.append((start, end, label))

    for idx, (start, end, label) in enumerate(figure_windows, start=1):
        body = "\n".join(lines[start:end]).strip()
        base_id = f"figure_{idx:02d}_{label}"
        chunks.extend(split_long_text(base_id, "figure_or_results", f"Figure/results packet {idx}: {label}", start + 1, body, max_chars))

    if "results" in bounds and not figure_windows:
        start, end = bounds["results"]
        results_text = bounded_text(lines, start, end, max_chars * 2)
        chunks.extend(split_long_text("results_core", "results", "Results section", start + 1, results_text, max_chars))

    seen: set[str] = set()
    unique_chunks: list[Chunk] = []
    for chunk in chunks:
        key = (chunk.chunk_type, chunk.start_line, chunk.end_line)
        if str(key) not in seen and chunk.source_excerpt:
            seen.add(str(key))
            unique_chunks.append(chunk)
    return unique_chunks


def select_chunks(chunks: list[Chunk], task: str) -> list[Chunk]:
    if task == "triage":
        return [chunk for chunk in chunks if chunk.chunk_type in {"paper_context", "results_subsection", "figure_or_results"}]
    if task == "methods_metadata":
        return [chunk for chunk in chunks if chunk.chunk_type in {"methods", "paper_context"}]
    if task == "figure_candidate_experiments":
        return [chunk for chunk in chunks if chunk.chunk_type in {"figure_or_results", "results_subsection"}]
    return chunks


def paper_metadata(args: argparse.Namespace, chunk: Chunk) -> dict[str, str]:
    return {
        "paper_id": args.paper_id,
        "title": args.title,
        "doi": args.doi or "UNKNOWN",
        "pmid": args.pmid or "UNKNOWN",
        "url": args.url or "UNKNOWN",
        "chunk_id": chunk.chunk_id,
        "chunk_type": chunk.chunk_type,
        "line_range": f"{chunk.start_line}-{chunk.end_line}",
        "task": args.task,
    }


def schema_for_task(args: argparse.Namespace, chunk: Chunk) -> dict[str, object]:
    if args.task == "triage":
        return {
            "chunk_id": chunk.chunk_id,
            "paper_id": args.paper_id,
            "contains_extractable_experiments": "yes|no|unclear",
            "module_1a_relevance": "high|medium|low|none",
            "relevance_reason": "brief source-grounded reason",
            "likely_context_types": [],
            "candidate_figures_or_sections": [],
            "do_not_extract_reasons": [],
            "missing_information_needed": [],
        }

    if args.task == "methods_metadata":
        return {
            "chunk_id": chunk.chunk_id,
            "paper_id": args.paper_id,
            "methods_metadata": {
                "species": [],
                "strains": [],
                "sex": "UNKNOWN",
                "ages": [],
                "injury_models": [],
                "injury_devices_and_parameters": [],
                "vertebral_levels": [],
                "surgeries_or_interventions": [],
                "cell_culture_systems": [],
                "transplantation_details": [],
                "antibody_or_drug_treatments": [],
                "timepoints": [],
                "assays": [],
                "sample_sizes": [],
            },
            "fields_not_stated": [],
            "context_separation_notes": [],
            "source_evidence": [],
        }

    if args.task == "figure_candidate_experiments":
        return {
            "chunk_id": chunk.chunk_id,
            "paper_id": args.paper_id,
            "candidate_experiments": [
                {
                    "figure_or_panel": "UNKNOWN",
                    "candidate_comparison": "brief contrast, not a final database row",
                    "context_type": "in_vivo_sci|in_vitro|transplantation_after_sci|transplantation_naive|human_pathology|imaging|other|no_experiment",
                    "control_condition": "UNKNOWN",
                    "intervention_or_contrast": "UNKNOWN",
                    "fields_explicitly_stated": [],
                    "fields_missing_from_chunk": [],
                    "why_candidate_not_final": "what a curator still needs to verify",
                    "contamination_risks": [],
                }
            ],
            "no_experiment_reason": "N/A unless no experiment is present",
        }

    if args.task == "row_sanity_check":
        return {
            "chunk_id": chunk.chunk_id,
            "paper_id": args.paper_id,
            "row_audit": [
                {
                    "row_id_or_label": "UNKNOWN",
                    "supported_by_this_chunk": "yes|no|partial|unclear",
                    "unsupported_fields": [],
                    "contradictions": [],
                    "missing_but_needed_fields": [],
                    "context_contamination_warning": "yes|no",
                    "recommended_curator_action": "keep|revise|split|merge|discard|needs_manual_review",
                    "source_evidence": "brief paraphrase with line/figure reference if possible",
                }
            ],
            "chunk_level_warnings": [],
        }

    return {
        "chunk_id": chunk.chunk_id,
        "paper_id": args.paper_id,
        "experiments": [
            {
                "candidate_experiment_id": f"{args.paper_id}-EX?",
                "figure_or_table": "UNKNOWN",
                "context_type": "one of: in_vivo_sci, in_vitro, transplantation_after_sci, transplantation_naive, human_pathology, imaging, other, no_experiment_in_chunk",
                "control_condition": "UNKNOWN",
                "intervention_or_contrast": "UNKNOWN",
                "species": "UNKNOWN",
                "strain_sex_age": "UNKNOWN",
                "injury_model": "UNKNOWN or N/A",
                "injury_device_and_parameters": "UNKNOWN or N/A",
                "vertebral_level": "UNKNOWN or N/A",
                "chronicity_or_timepoint": "UNKNOWN",
                "assays": [],
                "lesion_compartments": [],
                "methods_summary": "brief source-grounded summary",
                "granularity_decision": "why this should be one experiment, multiple experiments, or no experiment",
                "source_evidence": "short paraphrase with figure/table/page/line reference if available",
                "extraction_confidence": "high|medium|low",
                "sanity_flags": [],
            }
        ],
        "chunk_level_notes": [],
    }


def task_instructions(args: argparse.Namespace) -> str:
    shared = """Use ONLY the source chunk below. If a field is absent in this chunk, write UNKNOWN. If a field is biologically not applicable, write N/A. Do not borrow injury devices, vertebral levels, severities, or timepoints from other experiments or other chunks."""
    guardrails = """Critical guardrails:
- in_vitro/cell culture experiments must use injury_device_and_parameters=N/A, vertebral_level=N/A, injury_model=N/A unless the chunk explicitly describes a tissue injury model.
- transplantation_naive experiments must not inherit spinal cord injury metadata unless this exact chunk says the recipient animals were injured.
- in_vivo_sci experiments need explicit source support for model, device, severity, level, and chronicity; otherwise use UNKNOWN.
- Prefer fewer, well-supported candidates over speculative rows."""

    if args.task == "triage":
        return f"""{shared}

Task: triage this chunk for whether it is worth curator attention for Module 1A chronic SCI lesion architecture. Do not extract final experiment rows. Identify relevance, likely context types, and whether the chunk can be skipped."""

    if args.task == "methods_metadata":
        return f"""{shared}

Task: index factual methods metadata only. Separate in vivo SCI, in vitro culture, transplantation, and antibody/drug details. Do not decide experiment granularity and do not infer missing metadata.

{guardrails}"""

    if args.task == "figure_candidate_experiments":
        return f"""{shared}

Task: scout candidate figure-level comparisons. These are NOT final database rows. List only comparisons that the source chunk directly supports and explain what a curator still needs to verify.

{guardrails}"""

    if args.task == "row_sanity_check":
        return f"""{shared}

Task: audit the proposed curated rows against this source chunk. Do not create new rows unless noting that a row may be missing. Mark unsupported fields and context contamination risks clearly.

{guardrails}"""

    return f"""{shared}

Task: extract experiment-level metadata for curator review. These candidate rows must still be manually checked before entering the database.

{guardrails}"""


def prompt_for_chunk(args: argparse.Namespace, chunk: Chunk) -> str:
    metadata = {
        **paper_metadata(args, chunk),
    }
    schema = schema_for_task(args, chunk)
    proposed_rows = ""
    if args.task == "row_sanity_check":
        if not args.rows_file:
            raise SystemExit("--task row_sanity_check requires --rows-file.")
        rows_text = Path(args.rows_file).read_text(encoding="utf-8", errors="replace")
        proposed_rows = f"""

        Proposed curated rows to audit:
        ```text
        {rows_text}
        ```
        """

    return textwrap.dedent(
        f"""\
        You are a local-model subagent helping with an auditable spinal cord injury literature database.
        Your role is limited: provide source-grounded scouting, indexing, or checks for a human/primary curator.

        {task_instructions(args)}

        Paper metadata:
        {json.dumps(metadata, indent=2)}

        Return strict JSON matching this shape:
        {json.dumps(schema, indent=2)}
        {proposed_rows}

        Source chunk:
        ```text
        {chunk.source_excerpt}
        ```
        """
    )


def write_json(path: Path, data: object) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def run_ollama(ollama_bin: str, model: str, prompt: str, timeout: int) -> tuple[int, str, str]:
    proc = subprocess.run(
        [ollama_bin, "run", model],
        input=prompt,
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )
    return proc.returncode, proc.stdout, proc.stderr


def extract_json_objects(text: str) -> Iterable[object]:
    decoder = json.JSONDecoder()
    for match in re.finditer(r"\{", text):
        try:
            value, _ = decoder.raw_decode(text[match.start() :])
        except json.JSONDecodeError:
            continue
        yield value


def sanity_warnings_for_output(output_text: str, output_name: str) -> list[str]:
    warnings: list[str] = []
    if SUSPICIOUS_IN_VITRO_RE.search(output_text):
        warnings.append(f"{output_name}: possible in vitro row contaminated with in vivo SCI device/level/severity metadata.")

    parsed = list(extract_json_objects(output_text))
    if not parsed and output_text.strip():
        warnings.append(f"{output_name}: Ollama output was not parseable as JSON; review manually before curation.")

    for obj in parsed:
        if not isinstance(obj, dict):
            continue
        experiments = obj.get("experiments", [])
        if not isinstance(experiments, list):
            warnings.append(f"{output_name}: JSON has no experiments list.")
            continue
        for idx, experiment in enumerate(experiments, start=1):
            if not isinstance(experiment, dict):
                continue
            context = str(experiment.get("context_type", "")).lower()
            device = str(experiment.get("injury_device_and_parameters", ""))
            level = str(experiment.get("vertebral_level", ""))
            model = str(experiment.get("injury_model", ""))
            if "in_vitro" in context and re.search(r"infinite horizons|kdyn|\bt[0-9]{1,2}\b|contusion", f"{device} {level} {model}", re.I):
                warnings.append(f"{output_name}: experiment {idx} is in_vitro but carries SCI injury metadata.")
            if context == "no_experiment_in_chunk" and len(experiments) > 1:
                warnings.append(f"{output_name}: no_experiment_in_chunk appears with multiple experiment rows.")
    return warnings


def write_review_packet(path: Path, args: argparse.Namespace, chunks: list[Chunk]) -> None:
    lines = [
        f"# Ollama Chunk Review Packet: {args.paper_id}",
        "",
        f"- Title: {args.title}",
        f"- DOI: {args.doi or 'UNKNOWN'}",
        f"- PMID: {args.pmid or 'UNKNOWN'}",
        f"- Task: {args.task}",
        f"- Generated: {datetime.now(timezone.utc).isoformat()}",
        f"- Chunk count: {len(chunks)}",
        "",
        "Use this packet to decide which prompt outputs deserve manual curation into the tracker/database.",
        "",
    ]
    for chunk in chunks:
        lines.extend(
            [
                f"## {chunk.chunk_id}",
                "",
                f"- Type: {chunk.chunk_type}",
                f"- Lines: {chunk.start_line}-{chunk.end_line}",
                f"- Title: {chunk.title}",
                "",
                "```text",
                chunk.source_excerpt[:1800],
                "```",
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def write_sanity_report(path: Path, args: argparse.Namespace, chunks: list[Chunk], warnings: list[str], ran_ollama: bool) -> None:
    lines = [
        "# Ollama Chunk Sanity Report",
        "",
        f"- Generated: {datetime.now(timezone.utc).isoformat()}",
        f"- Task: {args.task}",
        f"- Chunks prepared: {len(chunks)}",
        f"- Ollama executed: {'YES' if ran_ollama else 'NO'}",
        "",
    ]
    if warnings:
        lines.append("## Warnings")
        lines.append("")
        lines.extend(f"- {warning}" for warning in warnings)
    else:
        lines.append("No automated sanity warnings were detected. Manual curation is still required.")
    lines.append("")
    lines.append("## Chunk Inventory")
    lines.append("")
    lines.append("| Chunk | Type | Lines | Prompt | Output |")
    lines.append("|---|---|---:|---|---|")
    for chunk in chunks:
        output = f"ollama_outputs/{chunk.chunk_id}.md" if ran_ollama else "not run"
        lines.append(
            f"| {chunk.chunk_id} | {chunk.chunk_type} | {chunk.start_line}-{chunk.end_line} | prompts/{chunk.chunk_id}.txt | {output} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--source-text", help="Plain text extracted from the paper.")
    source.add_argument("--pdf", help="PDF file to extract with pypdf, if installed.")
    parser.add_argument("--paper-id", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--doi")
    parser.add_argument("--pmid")
    parser.add_argument("--url")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument(
        "--task",
        choices=TASKS,
        default="extract",
        help="Prompt mode: full extraction, triage, methods indexing, figure scouting, or row audit.",
    )
    parser.add_argument("--rows-file", help="Curated/proposed rows to audit with --task row_sanity_check.")
    parser.add_argument("--max-chars", type=int, default=4500, help="Approximate maximum source characters per chunk.")
    parser.add_argument("--figure-context-lines", type=int, default=45)
    parser.add_argument("--front-chars", type=int, default=3500)
    parser.add_argument("--run-ollama", action="store_true", help="Send each prompt to Ollama and save raw outputs.")
    parser.add_argument("--ollama-bin", default="ollama")
    parser.add_argument("--model", default="qwen2.5-coder:32b")
    parser.add_argument("--timeout", type=int, default=900, help="Seconds per Ollama chunk.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if args.task == "row_sanity_check" and not args.rows_file:
        raise SystemExit("--task row_sanity_check requires --rows-file.")
    output_dir = Path(args.output_dir)
    prompts_dir = output_dir / "prompts"
    outputs_dir = output_dir / "ollama_outputs"
    prompts_dir.mkdir(parents=True, exist_ok=True)
    if args.run_ollama:
        outputs_dir.mkdir(parents=True, exist_ok=True)

    source_text = normalize_text(read_source_text(args))
    (output_dir / "source_clean.txt").write_text(source_text, encoding="utf-8")

    all_chunks = make_chunks(source_text, args.max_chars, args.figure_context_lines, args.front_chars)
    chunks = select_chunks(all_chunks, args.task)
    write_json(output_dir / "chunk_manifest.json", [asdict(chunk) for chunk in chunks])
    write_json(output_dir / "all_chunk_manifest.json", [asdict(chunk) for chunk in all_chunks])
    write_review_packet(output_dir / "review_packet.md", args, chunks)

    warnings: list[str] = []
    for chunk in chunks:
        prompt = prompt_for_chunk(args, chunk)
        prompt_path = prompts_dir / f"{chunk.chunk_id}.txt"
        prompt_path.write_text(prompt, encoding="utf-8")
        if args.run_ollama:
            try:
                returncode, stdout, stderr = run_ollama(args.ollama_bin, args.model, prompt, args.timeout)
            except subprocess.TimeoutExpired:
                (outputs_dir / f"{chunk.chunk_id}.md").write_text("TIMEOUT\n", encoding="utf-8")
                warnings.append(f"{chunk.chunk_id}: Ollama timed out after {args.timeout} seconds.")
                continue
            output_text = stdout.strip()
            if stderr.strip():
                output_text += "\n\n--- STDERR ---\n" + stderr.strip()
            (outputs_dir / f"{chunk.chunk_id}.md").write_text(output_text + "\n", encoding="utf-8")
            if returncode != 0:
                warnings.append(f"{chunk.chunk_id}: Ollama exited with status {returncode}.")
            warnings.extend(sanity_warnings_for_output(output_text, chunk.chunk_id))

    write_sanity_report(output_dir / "sanity_report.md", args, chunks, warnings, args.run_ollama)
    print(f"Prepared {len(chunks)} {args.task} chunks in {output_dir}")
    print(f"Prompts: {prompts_dir}")
    if args.run_ollama:
        print(f"Ollama outputs: {outputs_dir}")
    print(f"Sanity report: {output_dir / 'sanity_report.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
