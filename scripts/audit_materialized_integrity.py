#!/usr/bin/env python3
"""Audit generated module bundles and materialized SQL before database load.

This is a file-level integrity gate for environments without a local PostgreSQL
server. It does not replace a `psql` fresh-load, but it catches broken tracker
references, missing experiment-level observations, and SQL/count drift.
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
class ModuleAudit:
    module_num: int
    observations: int
    experiments: int
    claims: int
    links: int
    consensus: int
    consensus_observations: int
    a_experiments: int
    covered_a_experiments: int
    extra_exact_experiments: int


def split_markdown_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


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


def extract_section_table(markdown: str, section_title: str) -> list[dict[str, str]]:
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
        if len(cells) == len(headers):
            rows.append(dict(zip(headers, cells, strict=True)))
    return rows


def referenced_ids(text: str, full_prefix: str) -> list[str]:
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
        expanded = (
            [f"{full_prefix}{num:03d}" for num in range(int(start), int(end) + 1)]
            if end
            else [f"{full_prefix}{start}"]
        )
        for item in expanded:
            if item not in seen:
                seen.add(item)
                ids.append(item)
    return ids


def load_bundle(module_num: int) -> dict[str, Any]:
    path = ROOT / "data" / "processed" / f"module{module_num}_evidence_bundle.json"
    return json.loads(path.read_text())


def exact_experiment_pattern(module_num: int) -> re.Pattern[str]:
    return re.compile(rf"^M{module_num}A-[PT]\d{{3}}-E\d{{3}}$")


def a_experiments(module_num: int) -> set[str]:
    tracker = ROOT / "modules" / f"Module_{module_num}A_TRACKER.md"
    pattern = exact_experiment_pattern(module_num)
    ids: set[str] = set()
    for row in extract_section_table(tracker.read_text(), "## Experiment-Level Rows"):
        experiment_id = row.get("experiment_id", "")
        if pattern.fullmatch(experiment_id):
            ids.add(experiment_id)
    return ids


def exact_observation_experiments(bundle: dict[str, Any], module_num: int) -> set[str]:
    pattern = exact_experiment_pattern(module_num)
    return {
        row["experiment_id"]
        for row in bundle["observations"]
        if pattern.fullmatch(row.get("experiment_id", ""))
    }


def sql_insert_count(sql: str, table_name: str) -> int:
    return len(re.findall(rf"\bINSERT INTO {re.escape(table_name)}\b", sql))


def sql_insert_pattern_count(sql: str, table_pattern: str) -> int:
    return len(re.findall(rf"\bINSERT INTO {table_pattern}", sql))


def sql_consensus_observation_count(sql: str) -> int:
    return sql_insert_count(sql, "Consensus_Observation")


def experiment_key(row: dict[str, str]) -> str:
    return f"{row['paper_id']}::{row['experiment_id']}"


def audit_bundle(module_num: int, bundle: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    obs_prefix = f"M{module_num}B-O"
    claim_prefix = f"M{module_num}B-C"
    boundary_prefix = f"M{module_num}B-" + ("X" if module_num == 1 else "B")

    observations = bundle["observations"]
    claims = bundle["author_claims"]
    links = bundle["evidence_links"]
    boundaries = bundle["boundary_records"]
    consensus = bundle["consensus_drafts"]

    observation_ids = [row["tracker_id"] for row in observations]
    claim_ids = [row["tracker_id"] for row in claims]
    link_ids = [row["tracker_id"] for row in links]
    boundary_ids = [row["tracker_id"] for row in boundaries]
    consensus_ids = [row.get("tracker_id") or row.get("consensus_draft_id") or row.get("consensus_id") for row in consensus]

    for label, values in {
        "observations": observation_ids,
        "claims": claim_ids,
        "links": link_ids,
        "boundaries": boundary_ids,
        "consensus": consensus_ids,
    }.items():
        duplicates = sorted({value for value in values if values.count(value) > 1})
        if duplicates:
            errors.append(f"Module {module_num} duplicate {label}: {duplicates[:8]}")

    observation_set = set(observation_ids)
    claim_set = set(claim_ids)
    boundary_set = set(boundary_ids)

    required_observation_fields = (
        "paper_id",
        "experiment_id",
        "figure_ref",
        "evidence_type",
        "outcome_type",
        "observation_value",
        "source_section",
        "extraction_confidence",
    )
    for row in observations:
        for field in required_observation_fields:
            if not row.get(field):
                errors.append(f"Module {module_num} {row['tracker_id']} missing {field}")
        if row.get("extraction_confidence") not in {"high", "medium", "low", "uncertain"}:
            errors.append(f"Module {module_num} {row['tracker_id']} invalid extraction_confidence")

    linked_claims: set[str] = set()
    linked_observations: set[str] = set()
    for link in links:
        linked_claims.add(link["claim_id"])
        linked_observations.add(link["observation_id"])
        if link["claim_id"] not in claim_set:
            errors.append(f"Module {module_num} {link['tracker_id']} unknown claim {link['claim_id']}")
        if link["observation_id"] not in observation_set:
            errors.append(f"Module {module_num} {link['tracker_id']} unknown observation {link['observation_id']}")

    claims_without_links = sorted(claim_set - linked_claims)
    if claims_without_links:
        errors.append(f"Module {module_num} claims without evidence links: {claims_without_links[:8]}")

    for boundary in boundaries:
        text = " ".join(str(value) for value in boundary.values())
        for claim_id in referenced_ids(text, claim_prefix):
            if claim_id not in claim_set:
                errors.append(f"Module {module_num} {boundary['tracker_id']} unknown boundary claim {claim_id}")
        for observation_id in referenced_ids(text, obs_prefix):
            if observation_id not in observation_set:
                errors.append(f"Module {module_num} {boundary['tracker_id']} unknown boundary observation {observation_id}")

    consensus_observation_total = 0
    for draft in consensus:
        text = " ".join(str(value) for value in draft.values())
        draft_observations = referenced_ids(text, obs_prefix)
        consensus_observation_total += len(draft_observations)
        if len(draft_observations) < 2:
            draft_id = draft.get("tracker_id") or draft.get("consensus_draft_id") or draft.get("consensus_id")
            warnings.append(f"Module {module_num} {draft_id} has fewer than two observation refs")
        for observation_id in draft_observations:
            if observation_id not in observation_set:
                draft_id = draft.get("tracker_id") or draft.get("consensus_draft_id") or draft.get("consensus_id")
                errors.append(f"Module {module_num} {draft_id} unknown consensus observation {observation_id}")
        for claim_id in referenced_ids(text, claim_prefix):
            if claim_id not in claim_set:
                draft_id = draft.get("tracker_id") or draft.get("consensus_draft_id") or draft.get("consensus_id")
                errors.append(f"Module {module_num} {draft_id} unknown consensus claim {claim_id}")
        if "all boundary records" not in text.lower():
            for boundary_id in referenced_ids(text, boundary_prefix):
                if boundary_id not in boundary_set:
                    draft_id = draft.get("tracker_id") or draft.get("consensus_draft_id") or draft.get("consensus_id")
                    errors.append(f"Module {module_num} {draft_id} unknown consensus boundary {boundary_id}")

    unused_observations = sorted(observation_set - linked_observations)
    if unused_observations:
        warnings.append(
            f"Module {module_num} has {len(unused_observations)} observations not linked to author claims "
            "(expected for per-experiment backfill rows)"
        )

    return errors, warnings


def audit_module(module_num: int) -> tuple[ModuleAudit, list[str], list[str]]:
    bundle = load_bundle(module_num)
    errors, warnings = audit_bundle(module_num, bundle)
    sql_path = ROOT / "data" / "processed" / f"module{module_num}_full_materialization.sql"
    sql = sql_path.read_text()

    experiments = {experiment_key(row) for row in bundle["observations"]}
    sql_checks = {
        "Observation": len(bundle["observations"]),
        "AuthorClaim": len(bundle["author_claims"]),
        "EvidenceLink": len(bundle["evidence_links"]),
        "Consensus": len(bundle["consensus_drafts"]),
    }
    for table, expected in sql_checks.items():
        actual = sql_insert_count(sql, table)
        if actual != expected:
            errors.append(f"Module {module_num} SQL {table} inserts expected {expected}, found {actual}")

    experiment_inserts = sql_insert_pattern_count(sql, r"Experiment\s*\(")
    if experiment_inserts != len(experiments):
        errors.append(
            f"Module {module_num} SQL Experiment inserts expected {len(experiments)}, found {experiment_inserts}"
        )

    consensus_observation_count = 0
    obs_prefix = f"M{module_num}B-O"
    for draft in bundle["consensus_drafts"]:
        text = " ".join(str(value) for value in draft.values())
        consensus_observation_count += len(referenced_ids(text, obs_prefix))
    sql_co_count = sql_consensus_observation_count(sql)
    if sql_co_count != consensus_observation_count:
        errors.append(
            f"Module {module_num} SQL Consensus_Observation inserts expected "
            f"{consensus_observation_count}, found {sql_co_count}"
        )

    a_ids = a_experiments(module_num)
    exact_ids = exact_observation_experiments(bundle, module_num)
    missing_a = sorted(a_ids - exact_ids)
    if missing_a:
        errors.append(f"Module {module_num} missing exact observations for A experiments: {missing_a[:12]}")
    extra_exact = sorted(exact_ids - a_ids)
    if extra_exact and module_num not in {1, 4, 6}:
        warnings.append(f"Module {module_num} has {len(extra_exact)} exact B experiments not in parsed A table")

    audit = ModuleAudit(
        module_num=module_num,
        observations=len(bundle["observations"]),
        experiments=len(experiments),
        claims=len(bundle["author_claims"]),
        links=len(bundle["evidence_links"]),
        consensus=len(bundle["consensus_drafts"]),
        consensus_observations=consensus_observation_count,
        a_experiments=len(a_ids),
        covered_a_experiments=len(a_ids & exact_ids),
        extra_exact_experiments=len(extra_exact),
    )
    return audit, errors, warnings


def render_report(audits: list[ModuleAudit], warnings: list[str]) -> str:
    lines = [
        "# Materialized Integrity Audit",
        "",
        "Generated from `scripts/audit_materialized_integrity.py`.",
        "",
        "| Module | A Experiments Covered | SQL Experiments | Observations | Claims | Links | Consensus | Consensus-Observation Links |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for audit in audits:
        coverage = (
            "N/A"
            if audit.a_experiments == 0
            else f"{audit.covered_a_experiments}/{audit.a_experiments}"
        )
        lines.append(
            f"| Module {audit.module_num} | {coverage} | {audit.experiments} | {audit.observations} | "
            f"{audit.claims} | {audit.links} | {audit.consensus} | {audit.consensus_observations} |"
        )
    if warnings:
        lines.extend(["", "## Warnings", ""])
        lines.extend(f"- {warning}" for warning in warnings)
    return "\n".join(lines) + "\n"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate without writing the Markdown report.")
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "docs" / "MATERIALIZED_INTEGRITY_AUDIT.md",
        help="Report path written unless --check is set.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    audits: list[ModuleAudit] = []
    all_errors: list[str] = []
    all_warnings: list[str] = []
    for module_num in range(1, 16):
        audit, errors, warnings = audit_module(module_num)
        audits.append(audit)
        all_errors.extend(errors)
        all_warnings.extend(warnings)

    if all_errors:
        for error in all_errors:
            print(f"FAIL {error}", file=sys.stderr)
        return 1

    report = render_report(audits, all_warnings)
    if args.check:
        print(
            "PASS materialized integrity audit: "
            f"{sum(a.observations for a in audits)} observations, "
            f"{sum(a.experiments for a in audits)} SQL experiments, "
            f"{sum(a.consensus for a in audits)} consensus statements"
        )
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report)
        print(f"Wrote {args.output.relative_to(ROOT)}")
    if all_warnings:
        print(f"WARN {len(all_warnings)} non-blocking audit notes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
