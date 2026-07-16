#!/usr/bin/env python3
"""Generate full first-pass SQL materialization for Module 1.

The generated SQL loads:
- Paper
- ExperimentalParadigm
- Experiment
- ControlledVocabulary_EvidenceType / ControlledVocabulary_OutcomeType terms
- Observation
- AuthorClaim
- EvidenceLink
- Consensus
- Consensus_Observation

Temporary tracker-ID mapping tables are used so reviewable IDs such as
`M1B-O001` become database primary keys only inside the load transaction.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from export_module1_evidence_bundle import build_bundle, validate_bundle


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODULE_1A = ROOT / "modules" / "Module_1A_TRACKER.md"
DEFAULT_MODULE_1B = ROOT / "modules" / "Module_1B_TRACKER.md"
DEFAULT_OUTPUT = ROOT / "data" / "processed" / "module1_full_materialization.sql"


def split_markdown_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def snake_case(value: str) -> str:
    normalized = value.strip().lower()
    normalized = normalized.replace("/", " ")
    normalized = normalized.replace("-", " ")
    normalized = re.sub(r"[^a-z0-9]+", "_", normalized)
    return normalized.strip("_")


def extract_table(markdown: str, section_title: str) -> list[dict[str, str]]:
    in_section = False
    headers: list[str] | None = None
    rows: list[dict[str, str]] = []
    for line in markdown.splitlines():
        if line.startswith(section_title):
            in_section = True
            continue
        if in_section and line.startswith("#") and headers is not None:
            break
        if not in_section or not line.startswith("|"):
            continue
        if line.startswith("|---"):
            continue
        cells = split_markdown_row(line)
        if headers is None:
            headers = [snake_case(cell) for cell in cells]
            continue
        if len(cells) != len(headers):
            raise ValueError(
                f"Unexpected row width in {section_title}: expected {len(headers)}, "
                f"found {len(cells)} in {line}"
            )
        rows.append(dict(zip(headers, cells, strict=True)))
    if headers is None:
        raise ValueError(f"Could not find table for {section_title}")
    return rows


def parse_papers(module_1a: Path) -> dict[str, dict[str, str]]:
    rows = extract_table(module_1a.read_text(), "### Pass 0: Paper Registration")
    return {row["paper_id"]: row for row in rows}


def sql_literal(value: Any) -> str:
    if value is None:
        return "NULL"
    if isinstance(value, str):
        cleaned = value.strip()
        if cleaned in {"", "—", "-"}:
            return "NULL"
        return "'" + cleaned.replace("'", "''") + "'"
    return str(value)


def sql_int(value: str | None) -> str:
    if not value or value.strip() in {"", "—", "-"}:
        return "NULL"
    return value.strip()


def json_note(payload: dict[str, Any]) -> str:
    return json.dumps(payload, sort_keys=True)


def paper_from_experiment(experiment_tracker_id: str) -> str:
    match = re.match(r"(M1A-P\d{3})", experiment_tracker_id)
    if not match:
        raise ValueError(f"Cannot infer paper ID from experiment tracker ID {experiment_tracker_id}")
    return match.group(1)


def experiment_number(experiment_tracker_id: str) -> str:
    match = re.search(r"-E(\d{3})", experiment_tracker_id)
    return str(int(match.group(1))) if match else "NULL"


def referenced_papers(bundle: dict[str, Any]) -> list[str]:
    ids = {row["paper_id"] for row in bundle["observations"]}
    ids.update(row["paper_id"] for row in bundle["author_claims"])
    return sorted(ids)


def referenced_experiments(bundle: dict[str, Any]) -> list[str]:
    return sorted({row["experiment_id"] for row in bundle["observations"]})


def statement_topic(topic: str) -> str:
    return topic


def render_materialization_sql(bundle: dict[str, Any], papers: dict[str, dict[str, str]]) -> str:
    paper_ids = referenced_papers(bundle)
    missing = [paper_id for paper_id in paper_ids if paper_id not in papers]
    if missing:
        raise ValueError(f"Missing paper metadata for {missing}")

    lines: list[str] = [
        "-- Module 1 full first-pass materialization generated from tracker-derived JSON.",
        "-- This script is intended for a fresh database loaded with schema/schema.sql and scripts/seed_controlled_vocab.sql.",
        "BEGIN;",
        "",
        "CREATE TEMP TABLE _m1_paper_map (tracker_id TEXT PRIMARY KEY, paper_id INTEGER NOT NULL);",
        "CREATE TEMP TABLE _m1_paradigm_map (tracker_id TEXT PRIMARY KEY, paradigm_id INTEGER NOT NULL);",
        "CREATE TEMP TABLE _m1_experiment_map (tracker_id TEXT PRIMARY KEY, experiment_id INTEGER NOT NULL);",
        "CREATE TEMP TABLE _m1_observation_map (tracker_id TEXT PRIMARY KEY, observation_id INTEGER NOT NULL);",
        "CREATE TEMP TABLE _m1_claim_map (tracker_id TEXT PRIMARY KEY, claim_id INTEGER NOT NULL);",
        "CREATE TEMP TABLE _m1_consensus_map (tracker_id TEXT PRIMARY KEY, consensus_id INTEGER NOT NULL);",
        "",
    ]

    for paper_id in paper_ids:
        paper = papers[paper_id]
        lines.extend(
            [
                "WITH inserted AS (",
                "  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url)",
                "  VALUES (",
                f"    {sql_literal(paper['title'])}, {sql_literal(paper['authors'])}, {sql_int(paper['year'])},",
                f"    {sql_literal(paper['journal'])}, {sql_literal(paper['volume'])}, {sql_literal(paper['issue'])},",
                f"    {sql_literal(paper['pages'])}, {sql_literal(paper['doi'])}, {sql_literal(paper['pmid'])},",
                f"    {sql_literal(paper['url'])}",
                "  )",
                "  RETURNING paper_id",
                ")",
                f"INSERT INTO _m1_paper_map (tracker_id, paper_id) SELECT {sql_literal(paper_id)}, paper_id FROM inserted;",
                "",
            ]
        )

    for paper_id in paper_ids:
        lines.extend(
            [
                "WITH inserted AS (",
                "  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)",
                "  SELECT paper_id, 'Module 1 curated evidence extraction',",
                f"    {sql_literal('First-pass Module 1 lesion-architecture curation for ' + paper_id)},",
                "    'Tracker-derived materialization from Module_1A_TRACKER.md and Module_1B_TRACKER.md'",
                "  FROM _m1_paper_map WHERE tracker_id = " + sql_literal(paper_id),
                "  RETURNING paradigm_id",
                ")",
                f"INSERT INTO _m1_paradigm_map (tracker_id, paradigm_id) SELECT {sql_literal(paper_id)}, paradigm_id FROM inserted;",
                "",
            ]
        )

    for experiment_id in referenced_experiments(bundle):
        paper_id = paper_from_experiment(experiment_id)
        obs_for_experiment = [row["tracker_id"] for row in bundle["observations"] if row["experiment_id"] == experiment_id]
        notes = json_note({"tracker_id": experiment_id, "observation_tracker_ids": obs_for_experiment})
        lines.extend(
            [
                "WITH inserted AS (",
                "  INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, title, description, notes)",
                "  SELECT p.paper_id, ep.paradigm_id,",
                f"    {experiment_number(experiment_id)},",
                f"    {sql_literal('Tracker experiment ' + experiment_id)},",
                f"    {sql_literal('Module 1 tracker-derived experiment placeholder for SQL materialization.')},",
                f"    {sql_literal(notes)}",
                "  FROM _m1_paper_map p",
                "  JOIN _m1_paradigm_map ep ON ep.tracker_id = p.tracker_id",
                "  WHERE p.tracker_id = " + sql_literal(paper_id),
                "  RETURNING experiment_id",
                ")",
                f"INSERT INTO _m1_experiment_map (tracker_id, experiment_id) SELECT {sql_literal(experiment_id)}, experiment_id FROM inserted;",
                "",
            ]
        )

    evidence_types = sorted({row["evidence_type"] for row in bundle["observations"]})
    outcome_types = sorted({row["outcome_type"] for row in bundle["observations"]})
    for evidence_type in evidence_types:
        lines.append(
            "INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) "
            f"VALUES ({sql_literal(evidence_type)}, 'Module 1 tracker-derived evidence type') "
            "ON CONFLICT (evidence_type_name) DO NOTHING;"
        )
    lines.append("")
    for outcome_type in outcome_types:
        lines.append(
            "INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) "
            f"VALUES ({sql_literal(outcome_type)}, 'Module 1 tracker-derived outcome type') "
            "ON CONFLICT (outcome_type_name) DO NOTHING;"
        )
    lines.append("")

    for row in bundle["observations"]:
        notes = json_note(
            {
                "tracker_id": row["tracker_id"],
                "topic_id": row["topic_id"],
                "paper_tracker_id": row["paper_id"],
                "statistics_reported": row["statistics_reported"],
                "quantitative": row["quantitative"],
                "curator_notes": row["notes"],
            }
        )
        lines.extend(
            [
                "WITH inserted AS (",
                "  INSERT INTO Observation (",
                "    experiment_id, evidence_type_id, outcome_type_id, observation_value,",
                "    unit, raw_observation_text, normalized_observation_value, source_section,",
                "    figure_panel_reference, extraction_confidence, notes",
                "  )",
                "  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,",
                f"    {sql_literal(row['observation_value'])},",
                f"    {sql_literal(row['unit'])},",
                f"    {sql_literal(row['observation_value'])},",
                f"    {sql_literal(row['normalized_value'])},",
                f"    {sql_literal(row['source_section'])},",
                f"    {sql_literal(row['figure_ref'])},",
                f"    {sql_literal(row['extraction_confidence'])},",
                f"    {sql_literal(notes)}",
                "  FROM _m1_experiment_map e",
                "  CROSS JOIN ControlledVocabulary_EvidenceType et",
                "  CROSS JOIN ControlledVocabulary_OutcomeType ot",
                "  WHERE e.tracker_id = " + sql_literal(row["experiment_id"]),
                "    AND et.evidence_type_name = " + sql_literal(row["evidence_type"]),
                "    AND ot.outcome_type_name = " + sql_literal(row["outcome_type"]),
                "  RETURNING observation_id",
                ")",
                f"INSERT INTO _m1_observation_map (tracker_id, observation_id) SELECT {sql_literal(row['tracker_id'])}, observation_id FROM inserted;",
                "",
            ]
        )

    for row in bundle["author_claims"]:
        notes = json_note({"tracker_id": row["tracker_id"], "topic_id": row["topic_id"], "curator_notes": row["notes"]})
        lines.extend(
            [
                "WITH inserted AS (",
                "  INSERT INTO AuthorClaim (",
                "    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes",
                "  )",
                "  SELECT p.paper_id,",
                f"    {sql_literal(row['claim_text'])},",
                f"    {sql_literal(row['claim_type'])},",
                f"    {sql_literal(row['confidence_level'])},",
                f"    {sql_literal(row['source_section'])},",
                f"    {sql_literal(row['extraction_confidence'])},",
                f"    {sql_literal(notes)}",
                "  FROM _m1_paper_map p",
                "  WHERE p.tracker_id = " + sql_literal(row["paper_id"]),
                "  RETURNING claim_id",
                ")",
                f"INSERT INTO _m1_claim_map (tracker_id, claim_id) SELECT {sql_literal(row['tracker_id'])}, claim_id FROM inserted;",
                "",
            ]
        )

    for row in bundle["evidence_links"]:
        lines.extend(
            [
                "INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)",
                "SELECT c.claim_id, o.observation_id,",
                f"  {sql_literal(row['link_type'])},",
                f"  {sql_literal(json_note({'tracker_id': row['tracker_id'], 'notes': row['notes']}))}",
                "FROM _m1_claim_map c",
                "JOIN _m1_observation_map o ON o.tracker_id = " + sql_literal(row["observation_id"]),
                "WHERE c.tracker_id = " + sql_literal(row["claim_id"]) + ";",
                "",
            ]
        )

    for draft in bundle["consensus_drafts"]:
        notes = json_note(
            {
                "consensus_draft_id": draft["consensus_draft_id"],
                "topic_id": draft["topic_id"],
                "source_tracker": draft["source_tracker"],
                "source_agreement_label": draft["source_agreement_label"],
                "supporting_evidence_scope": draft["supporting_evidence_scope"],
                "boundary_or_contradiction_handling": draft["boundary_or_contradiction_handling"],
                "observation_tracker_ids": draft["observation_tracker_ids"],
                "claim_tracker_ids": draft["claim_tracker_ids"],
                "boundary_tracker_ids": draft["boundary_tracker_ids"],
            }
        )
        lines.extend(
            [
                "WITH inserted AS (",
                "  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)",
                "  VALUES (",
                f"    {sql_literal(draft['consensus_statement'])},",
                f"    {sql_literal(statement_topic(draft['topic']))},",
                "    1,",
                f"    {sql_literal(draft['agreement_level'])},",
                f"    {sql_literal(notes)}",
                "  )",
                "  RETURNING consensus_id",
                ")",
                f"INSERT INTO _m1_consensus_map (tracker_id, consensus_id) SELECT {sql_literal(draft['consensus_draft_id'])}, consensus_id FROM inserted;",
                "",
            ]
        )
        for observation_id in draft["observation_tracker_ids"]:
            lines.extend(
                [
                    "INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)",
                    "SELECT c.consensus_id, o.observation_id, 'supporting'",
                    "FROM _m1_consensus_map c",
                    "JOIN _m1_observation_map o ON o.tracker_id = " + sql_literal(observation_id),
                    "WHERE c.tracker_id = " + sql_literal(draft["consensus_draft_id"]) + ";",
                    "",
                ]
            )

    lines.extend(
        [
            "DO $$",
            "DECLARE",
            "  paper_count INTEGER;",
            "  experiment_count INTEGER;",
            "  observation_count INTEGER;",
            "  claim_count INTEGER;",
            "  link_count INTEGER;",
            "  consensus_count INTEGER;",
            "  consensus_observation_count INTEGER;",
            "BEGIN",
            "  SELECT COUNT(*) INTO paper_count FROM _m1_paper_map;",
            "  SELECT COUNT(*) INTO experiment_count FROM _m1_experiment_map;",
            "  SELECT COUNT(*) INTO observation_count FROM _m1_observation_map;",
            "  SELECT COUNT(*) INTO claim_count FROM _m1_claim_map;",
            "  SELECT COUNT(*) INTO link_count FROM EvidenceLink;",
            "  SELECT COUNT(*) INTO consensus_count FROM _m1_consensus_map;",
            "  SELECT COUNT(*) INTO consensus_observation_count FROM Consensus_Observation;",
            "  IF paper_count <> " + str(len(paper_ids)) + " THEN RAISE EXCEPTION 'Expected " + str(len(paper_ids)) + " papers, found %', paper_count; END IF;",
            "  IF experiment_count <> " + str(len(referenced_experiments(bundle))) + " THEN RAISE EXCEPTION 'Unexpected experiment count %', experiment_count; END IF;",
            "  IF observation_count <> 84 THEN RAISE EXCEPTION 'Expected 84 observations, found %', observation_count; END IF;",
            "  IF claim_count <> 50 THEN RAISE EXCEPTION 'Expected 50 claims, found %', claim_count; END IF;",
            "  IF link_count <> 107 THEN RAISE EXCEPTION 'Expected 107 evidence links, found %', link_count; END IF;",
            "  IF consensus_count <> 8 THEN RAISE EXCEPTION 'Expected 8 consensus rows, found %', consensus_count; END IF;",
            "  IF consensus_observation_count <> 84 THEN RAISE EXCEPTION 'Expected 84 consensus-observation links, found %', consensus_observation_count; END IF;",
            "END $$;",
            "",
            "COMMIT;",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--module-1a", type=Path, default=DEFAULT_MODULE_1A)
    parser.add_argument("--module-1b", type=Path, default=DEFAULT_MODULE_1B)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true", help="Validate generated SQL without writing it.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    bundle = build_bundle(args.module_1b)
    errors = validate_bundle(bundle)
    if errors:
        for error in errors:
            print(f"FAIL {error}", file=sys.stderr)
        return 1
    papers = parse_papers(args.module_1a)
    sql = render_materialization_sql(bundle, papers)
    if args.check:
        print(
            "PASS generated Module 1 full SQL "
            f"({len(referenced_papers(bundle))} papers, "
            f"{len(referenced_experiments(bundle))} experiments, "
            f"{len(bundle['observations'])} observations)"
        )
        return 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(sql)
    print(f"Wrote {args.output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
