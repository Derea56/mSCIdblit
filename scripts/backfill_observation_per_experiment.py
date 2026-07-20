#!/usr/bin/env python3
"""Backfill one exact B-layer observation row for each A-layer experiment.

The first consensus-ready B pass sometimes used one observation row to summarize
paired A experiments, e.g. `M3A-P001-E001-M3A-P001-E002`. This script preserves
those rows and appends exact per-experiment rows for downstream materialization.
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def split_markdown_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def render_markdown_row(cells: list[str]) -> str:
    return "| " + " | ".join(sanitize_cell(cell) for cell in cells) + " |"


def sanitize_cell(value: str) -> str:
    return " ".join(value.replace("|", "/").split())


def snake_case(value: str) -> str:
    normalized = value.strip().lower()
    normalized = normalized.replace("/", " ")
    normalized = normalized.replace("-", " ")
    normalized = re.sub(r"[^a-z0-9]+", "_", normalized)
    return normalized.strip("_")


def extract_tables(markdown: str) -> list[tuple[list[str], list[dict[str, str]]]]:
    lines = markdown.splitlines()
    tables: list[tuple[list[str], list[dict[str, str]]]] = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("|") and i + 1 < len(lines) and lines[i + 1].startswith("|---"):
            headers = [snake_case(cell) for cell in split_markdown_row(lines[i])]
            rows: list[dict[str, str]] = []
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                if not lines[i].startswith("|---"):
                    cells = split_markdown_row(lines[i])
                    if len(cells) == len(headers):
                        rows.append(dict(zip(headers, cells, strict=True)))
                i += 1
            tables.append((headers, rows))
            continue
        i += 1
    return tables


def extract_section_table(markdown: str, section_title: str) -> tuple[list[str], list[list[str]], int, int]:
    lines = markdown.splitlines()
    in_section = False
    header_idx: int | None = None
    rows_start: int | None = None
    rows_end: int | None = None
    for idx, line in enumerate(lines):
        if line.startswith(section_title):
            in_section = True
            continue
        if not in_section:
            continue
        if header_idx is None and line.startswith("|"):
            header_idx = idx
            rows_start = idx + 2
            continue
        if header_idx is not None and rows_end is None:
            if not line.startswith("|"):
                rows_end = idx
                break
    if header_idx is None or rows_start is None:
        raise ValueError(f"Could not find table for {section_title}")
    if rows_end is None:
        rows_end = len(lines)
    headers = split_markdown_row(lines[header_idx])
    rows = [split_markdown_row(line) for line in lines[rows_start:rows_end] if line.startswith("|")]
    return headers, rows, rows_start, rows_end


def experiment_id_pattern(module_num: int) -> re.Pattern[str]:
    return re.compile(rf"\bM{module_num}A-[PT]\d{{3}}-E\d{{3}}\b")


def exact_experiment_id(value: str, module_num: int) -> str | None:
    pattern = experiment_id_pattern(module_num)
    stripped = value.strip()
    return stripped if pattern.fullmatch(stripped) else None


def expanded_experiment_ids(value: str, module_num: int) -> set[str]:
    pattern = experiment_id_pattern(module_num)
    ids = set(pattern.findall(value))
    range_pattern = re.compile(
        rf"\b(M{module_num}A-[PT]\d{{3}}-E)(\d{{3}})"
        rf"(?:-M{module_num}A-[PT]\d{{3}}-E|-E)(\d{{3}})\b"
    )
    for match in range_pattern.finditer(value):
        prefix, start, end = match.groups()
        ids.update(f"{prefix}{num:03d}" for num in range(int(start), int(end) + 1))
    return ids


def ordered_expanded_experiment_ids(value: str, module_num: int) -> list[str]:
    pattern = experiment_id_pattern(module_num)
    ids: list[str] = []
    seen: set[str] = set()
    range_pattern = re.compile(
        rf"\b(M{module_num}A-[PT]\d{{3}}-E)(\d{{3}})"
        rf"(?:-M{module_num}A-[PT]\d{{3}}-E|-E)(\d{{3}})\b"
    )
    ranges: list[tuple[tuple[int, int], list[str]]] = []
    for match in range_pattern.finditer(value):
        prefix, start, end = match.groups()
        ranges.append(
            (
                match.span(),
                [f"{prefix}{num:03d}" for num in range(int(start), int(end) + 1)],
            )
        )
    for match in pattern.finditer(value):
        inside_range = any(start <= match.start() and match.end() <= end for (start, end), _ in ranges)
        if not inside_range and match.group(0) not in seen:
            seen.add(match.group(0))
            ids.append(match.group(0))
    for _, expanded in ranges:
        for experiment_id in expanded:
            if experiment_id not in seen:
                seen.add(experiment_id)
                ids.append(experiment_id)
    return ids


def a_experiment_rows(module_num: int) -> list[dict[str, str]]:
    module_a = ROOT / "modules" / f"Module_{module_num}A_TRACKER.md"
    rows: list[dict[str, str]] = []
    for headers, table_rows in extract_tables(module_a.read_text()):
        if "experiment_id" not in headers or "observation_id" in headers:
            continue
        for row in table_rows:
            experiment_id = row.get("experiment_id", "")
            if exact_experiment_id(experiment_id, module_num):
                rows.append(row)
    return rows


def paper_inventory(module_num: int) -> dict[str, dict[str, str]]:
    module_a = ROOT / "modules" / f"Module_{module_num}A_TRACKER.md"
    papers: dict[str, dict[str, str]] = {}
    for headers, rows in extract_tables(module_a.read_text()):
        if "paper_id" not in headers and "review_id" not in headers:
            continue
        if not ({"title", "first_author"} & set(headers)):
            continue
        id_key = "paper_id" if "paper_id" in headers else "review_id"
        for row in rows:
            tracker_id = row.get(id_key)
            if tracker_id:
                papers[tracker_id] = row
    return papers


def next_observation_number(rows: list[list[str]], module_num: int) -> int:
    nums = []
    for row in rows:
        if row:
            match = re.fullmatch(rf"M{module_num}B-O(\d{{3}})", row[0])
            if match:
                nums.append(int(match.group(1)))
    return max(nums, default=0) + 1


def row_index(headers: list[str], name: str) -> int:
    normalized = [snake_case(header) for header in headers]
    return normalized.index(name)


def topic_for_position(module_num: int, position: int) -> str:
    return f"M{module_num}B-T{((position - 1) % 8) + 1:03d}"


def generated_row(
    module_num: int,
    observation_id: str,
    experiment: dict[str, str],
    papers: dict[str, dict[str, str]],
    template: list[str] | None,
    headers: list[str],
    position: int,
) -> list[str]:
    idx = {snake_case(header): offset for offset, header in enumerate(headers)}
    cells = list(template) if template else [""] * len(headers)
    paper_id = experiment.get("paper_id", "")
    experiment_id = experiment["experiment_id"]
    paper = papers.get(paper_id, {})
    author = paper.get("first_author") or paper.get("authors") or paper_id
    year = paper.get("year") or ""
    title = paper.get("title") or "A-layer experiment"
    figure = experiment.get("figure_ref") or experiment.get("figure_table_ref") or "A-layer tracker"
    source = experiment.get("source_section") or "Module A tracker"
    confidence = experiment.get("confidence") or "medium"
    model = (
        experiment.get("model_system")
        or experiment.get("species_system")
        or experiment.get("species_population")
        or experiment.get("species")
        or "SCI model/system"
    )
    intervention = (
        experiment.get("intervention_type")
        or experiment.get("host_directed_intervention")
        or experiment.get("conditioning_protection_intervention")
        or experiment.get("conditioning_innate_immune_intervention")
        or experiment.get("injury_stimulus")
        or experiment.get("injury_model")
        or "curated intervention/model"
    )
    endpoint = (
        experiment.get("endpoint")
        or experiment.get("remodeling_integration_endpoint")
        or experiment.get("experiment_level_finding")
        or experiment.get("methods_summary")
        or "experiment-level endpoint"
    )
    seed = experiment.get("observation_seed") or experiment.get("experiment_level_finding") or experiment.get("methods_summary") or endpoint
    value = (
        f"{author} {year} {experiment_id} preserves a distinct {model} experiment testing "
        f"{intervention} with endpoint/readout: {seed}."
    )
    normalized = f"{experiment_id} preserves distinct model/timing/intervention/endpoint boundary"
    notes = (
        f"Per-experiment atomization backfill from A-layer row; source title: {title}. "
        "Existing consensus links remain on original curated observations."
    )
    assignments = {
        "observation_id": observation_id,
        "topic_id": cells[idx["topic_id"]] if template and cells[idx["topic_id"]] else topic_for_position(module_num, position),
        "paper_id": paper_id,
        "experiment_id": experiment_id,
        "figure_ref": figure,
        "evidence_type": cells[idx["evidence_type"]] if template and cells[idx["evidence_type"]] else "A-layer experiment evidence",
        "outcome_type": endpoint,
        "observation_value": value,
        "normalized_value": normalized,
        "unit": "qualitative",
        "quantitative": "NO",
        "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.",
        "source_section": source,
        "extraction_confidence": confidence,
        "notes": notes,
    }
    for key, value in assignments.items():
        cells[idx[key]] = value
    return cells


def normalize_module10_experiment_ids(rows: list[list[str]], headers: list[str]) -> int:
    experiment_idx = row_index(headers, "experiment_id")
    changed = 0
    for cells in rows:
        match = re.fullmatch(r"M10A-P(\d{3})-E001", cells[experiment_idx])
        if match:
            cells[experiment_idx] = f"M10A-T{match.group(1)}-E001"
            changed += 1
    return changed


def is_backfill_row(row: list[str], headers: list[str]) -> bool:
    notes_idx = row_index(headers, "notes")
    return "Per-experiment atomization backfill" in row[notes_idx]


def atomize_composite_observation_ids(rows: list[list[str]], headers: list[str], module_num: int) -> int:
    experiment_idx = row_index(headers, "experiment_id")
    changed = 0
    for cells in rows:
        if is_backfill_row(cells, headers):
            continue
        expanded = ordered_expanded_experiment_ids(cells[experiment_idx], module_num)
        if len(expanded) > 1:
            cells[experiment_idx] = expanded[0]
            changed += 1
    return changed


def remove_duplicate_backfill_rows(rows: list[list[str]], headers: list[str], module_num: int) -> tuple[list[list[str]], int]:
    experiment_idx = row_index(headers, "experiment_id")
    seen: set[str] = set()
    kept: list[list[str]] = []
    removed = 0
    for cells in rows:
        experiment_id = exact_experiment_id(cells[experiment_idx], module_num)
        if experiment_id is None:
            kept.append(cells)
            continue
        if experiment_id in seen and is_backfill_row(cells, headers):
            removed += 1
            continue
        kept.append(cells)
        seen.add(experiment_id)
    return kept, removed


def renumber_backfill_rows(rows: list[list[str]], headers: list[str], module_num: int) -> int:
    observation_idx = row_index(headers, "observation_id")
    original_nums = []
    for cells in rows:
        if is_backfill_row(cells, headers):
            continue
        match = re.fullmatch(rf"M{module_num}B-O(\d{{3}})", cells[observation_idx])
        if match:
            original_nums.append(int(match.group(1)))
    next_num = max(original_nums, default=0) + 1
    changed = 0
    for cells in rows:
        if not is_backfill_row(cells, headers):
            continue
        new_id = f"M{module_num}B-O{next_num:03d}"
        if cells[observation_idx] != new_id:
            cells[observation_idx] = new_id
            changed += 1
        next_num += 1
    return changed


def update_module(module_num: int) -> tuple[int, int]:
    module_b = ROOT / "modules" / f"Module_{module_num}B_TRACKER.md"
    markdown = module_b.read_text()
    lines = markdown.splitlines()
    headers, observation_rows, rows_start, rows_end = extract_section_table(
        markdown, "## Pass 4A: Atomic Observations Extracted"
    )
    experiment_idx = row_index(headers, "experiment_id")
    paper_idx = row_index(headers, "paper_id")

    normalized = normalize_module10_experiment_ids(observation_rows, headers) if module_num == 10 else 0
    normalized += atomize_composite_observation_ids(observation_rows, headers, module_num)
    observation_rows, removed = remove_duplicate_backfill_rows(observation_rows, headers, module_num)
    normalized += renumber_backfill_rows(observation_rows, headers, module_num)
    exact_ids = {
        exact
        for row in observation_rows
        if (exact := exact_experiment_id(row[experiment_idx], module_num)) is not None
    }
    template_by_experiment: dict[str, list[str]] = {}
    for row in observation_rows:
        for experiment_id in expanded_experiment_ids(row[experiment_idx], module_num):
            template_by_experiment.setdefault(experiment_id, row)

    additions: list[list[str]] = []
    papers = paper_inventory(module_num)
    next_num = next_observation_number(observation_rows, module_num)
    for experiment in a_experiment_rows(module_num):
        experiment_id = experiment["experiment_id"]
        if experiment_id in exact_ids:
            continue
        observation_id = f"M{module_num}B-O{next_num:03d}"
        template = template_by_experiment.get(experiment_id)
        row = generated_row(module_num, observation_id, experiment, papers, template, headers, next_num)
        if not row[paper_idx]:
            row[paper_idx] = experiment.get("paper_id", "")
        additions.append(row)
        exact_ids.add(experiment_id)
        next_num += 1

    if not additions and not normalized and not removed:
        return 0, 0

    new_rows = observation_rows + additions
    rendered_rows = [render_markdown_row(row) for row in new_rows]
    new_lines = lines[:rows_start] + rendered_rows + lines[rows_end:]
    module_b.write_text("\n".join(new_lines) + "\n")
    return len(additions) - removed, normalized


def main() -> int:
    for module_num in range(1, 13):
        added, normalized = update_module(module_num)
        print(f"Module {module_num}: added {added} observation rows; normalized {normalized} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
