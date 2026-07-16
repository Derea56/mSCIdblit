#!/usr/bin/env python3
"""Generate full first-pass SQL materialization for Module 2.

The generated SQL loads the Module 2B tracker evidence bundle into the same
core tables used by Module 1. It intentionally preserves tracker IDs in notes
and uses synthetic records for review-map/composite rows that do not correspond
to a single primary-paper experiment.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from export_tracker_evidence_bundle import MODULES, build_bundle, referenced_ids, validate_bundle


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODULE_2A = ROOT / "modules" / "Module_2A_TRACKER.md"
DEFAULT_OUTPUT = ROOT / "data" / "processed" / "module2_full_materialization.sql"


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


def sql_literal(value: Any) -> str:
    if value is None:
        return "NULL"
    if isinstance(value, str):
        cleaned = value.strip()
        if cleaned in {"", "-", "—", "N/A", "UNKNOWN"}:
            return "NULL"
        return "'" + cleaned.replace("'", "''") + "'"
    return str(value)


def sql_int(value: str | None) -> str:
    if not value or value.strip() in {"", "-", "—", "N/A", "UNKNOWN"}:
        return "NULL"
    return value.strip()


def json_note(payload: dict[str, Any]) -> str:
    return json.dumps(payload, sort_keys=True)


def parse_primary_papers(module_2a: Path) -> dict[str, dict[str, str]]:
    rows = extract_table(module_2a.read_text(), "## Paper Inventory")
    papers: dict[str, dict[str, str]] = {}
    for row in rows:
        papers[row["paper_id"]] = {
            "title": row["title"],
            "authors": row["first_author"],
            "year": row["year"],
            "journal": None,
            "volume": None,
            "issue": None,
            "pages": None,
            "doi": None,
            "pmid": None,
            "url": None,
            "notes": row.get("notes", ""),
        }
    return papers


def parse_review_papers(module_2a: Path) -> dict[str, dict[str, str]]:
    rows = extract_table(module_2a.read_text(), "## Review and Map Anchors")
    papers: dict[str, dict[str, str]] = {}
    for row in rows:
        papers[row["review_id"]] = {
            "title": row["title"],
            "authors": row["first_author"],
            "year": row["year"],
            "journal": None,
            "volume": None,
            "issue": None,
            "pages": None,
            "doi": None,
            "pmid": None,
            "url": None,
            "notes": row.get("notes", ""),
        }
    return papers


def parse_experiments(module_2a: Path) -> dict[str, dict[str, str]]:
    rows = extract_table(module_2a.read_text(), "### Pass 3: Experiments Extracted")
    return {row["experiment_id"]: row for row in rows}


def expanded_paper_ids(paper_id: str) -> list[str]:
    primary_ids = referenced_ids(paper_id, "M2A-P")
    review_ids = referenced_ids(paper_id, "M2A-R")
    return primary_ids + review_ids


def canonical_paper_id(paper_id: str) -> str:
    expanded = expanded_paper_ids(paper_id)
    return expanded[0] if expanded else paper_id


def experiment_key(row: dict[str, str]) -> str:
    return f"{row['paper_id']}::{row['experiment_id']}"


def experiment_number(experiment_id: str) -> str:
    match = re.search(r"-E(\d{3})", experiment_id)
    return str(int(match.group(1))) if match else "NULL"


def referenced_papers(bundle: dict[str, Any]) -> list[str]:
    ids: set[str] = set()
    for row in bundle["observations"] + bundle["author_claims"]:
        expanded = expanded_paper_ids(row["paper_id"])
        if expanded:
            ids.update(expanded)
        else:
            ids.add(row["paper_id"])
    return sorted(ids)


def referenced_experiment_rows(bundle: dict[str, Any]) -> list[dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for observation in bundle["observations"]:
        key = experiment_key(observation)
        rows[key] = observation
    return [rows[key] for key in sorted(rows)]


def synthetic_paper(paper_id: str) -> dict[str, str | None]:
    return {
        "title": f"Module 2 synthetic source record for {paper_id}",
        "authors": "mSCIdblit curator",
        "year": "2026",
        "journal": None,
        "volume": None,
        "issue": None,
        "pages": None,
        "doi": None,
        "pmid": None,
        "url": None,
        "notes": "Synthetic record created for a composite tracker source that is not a single bibliographic paper.",
    }


def render_materialization_sql(
    bundle: dict[str, Any],
    papers: dict[str, dict[str, str | None]],
    experiments: dict[str, dict[str, str]],
) -> str:
    paper_ids = referenced_papers(bundle)
    for paper_id in paper_ids:
        papers.setdefault(paper_id, synthetic_paper(paper_id))

    experiment_rows = referenced_experiment_rows(bundle)
    lines: list[str] = [
        "-- Module 2 full first-pass materialization generated from tracker-derived JSON.",
        "-- This script is intended for a fresh database loaded with schema/schema.sql and scripts/seed_controlled_vocab.sql.",
        "BEGIN;",
        "",
        "CREATE TEMP TABLE _m2_paper_map (tracker_id TEXT PRIMARY KEY, paper_id INTEGER NOT NULL);",
        "CREATE TEMP TABLE _m2_paradigm_map (tracker_id TEXT PRIMARY KEY, paradigm_id INTEGER NOT NULL);",
        "CREATE TEMP TABLE _m2_experiment_map (tracker_id TEXT PRIMARY KEY, experiment_id INTEGER NOT NULL);",
        "CREATE TEMP TABLE _m2_observation_map (tracker_id TEXT PRIMARY KEY, observation_id INTEGER NOT NULL);",
        "CREATE TEMP TABLE _m2_claim_map (tracker_id TEXT PRIMARY KEY, claim_id INTEGER NOT NULL);",
        "CREATE TEMP TABLE _m2_consensus_map (tracker_id TEXT PRIMARY KEY, consensus_id INTEGER NOT NULL);",
        "",
    ]

    for paper_id in paper_ids:
        paper = papers[paper_id]
        notes = json_note({"tracker_id": paper_id, "module": "Module 2", "curator_notes": paper.get("notes")})
        lines.extend(
            [
                "WITH inserted AS (",
                "  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)",
                "  VALUES (",
                f"    {sql_literal(paper['title'])}, {sql_literal(paper['authors'])}, {sql_int(paper['year'])},",
                f"    {sql_literal(paper['journal'])}, {sql_literal(paper['volume'])}, {sql_literal(paper['issue'])},",
                f"    {sql_literal(paper['pages'])}, {sql_literal(paper['doi'])}, {sql_literal(paper['pmid'])},",
                f"    {sql_literal(paper['url'])}, {sql_literal(notes)}",
                "  )",
                "  RETURNING paper_id",
                ")",
                f"INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT {sql_literal(paper_id)}, paper_id FROM inserted;",
                "",
            ]
        )

    for paper_id in paper_ids:
        lines.extend(
            [
                "WITH inserted AS (",
                "  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)",
                "  SELECT paper_id, 'Module 2 curated evidence extraction',",
                f"    {sql_literal('First-pass Module 2 biomaterials/scaffold curation for ' + paper_id)},",
                "    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'",
                "  FROM _m2_paper_map WHERE tracker_id = " + sql_literal(paper_id),
                "  RETURNING paradigm_id",
                ")",
                f"INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT {sql_literal(paper_id)}, paradigm_id FROM inserted;",
                "",
            ]
        )

    for row in experiment_rows:
        key = experiment_key(row)
        paper_id = canonical_paper_id(row["paper_id"])
        source_experiment = experiments.get(row["experiment_id"], {})
        notes = json_note(
            {
                "tracker_key": key,
                "source_paper_tracker_id": row["paper_id"],
                "source_experiment_tracker_id": row["experiment_id"],
                "source_experiment": source_experiment,
                "observation_tracker_ids": [
                    obs["tracker_id"] for obs in bundle["observations"] if experiment_key(obs) == key
                ],
            }
        )
        lines.extend(
            [
                "WITH inserted AS (",
                "  INSERT INTO Experiment (",
                "    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,",
                "    control_type, intervention_type, notes",
                "  )",
                "  SELECT p.paper_id, ep.paradigm_id,",
                f"    {experiment_number(row['experiment_id'])},",
                f"    {sql_literal(row['figure_ref'])},",
                f"    {sql_literal('Tracker experiment ' + row['experiment_id'])},",
                f"    {sql_literal(source_experiment.get('methods_summary', 'Module 2 tracker-derived experiment placeholder.'))},",
                f"    {sql_literal(source_experiment.get('control_type'))},",
                f"    {sql_literal(source_experiment.get('intervention_type'))},",
                f"    {sql_literal(notes)}",
                "  FROM _m2_paper_map p",
                "  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id",
                "  WHERE p.tracker_id = " + sql_literal(paper_id),
                "  RETURNING experiment_id",
                ")",
                f"INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT {sql_literal(key)}, experiment_id FROM inserted;",
                "",
            ]
        )

    evidence_types = sorted({row["evidence_type"] for row in bundle["observations"]})
    outcome_types = sorted({row["outcome_type"] for row in bundle["observations"]})
    for evidence_type in evidence_types:
        lines.append(
            "INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) "
            f"VALUES ({sql_literal(evidence_type)}, 'Module 2 tracker-derived evidence type') "
            "ON CONFLICT (evidence_type_name) DO NOTHING;"
        )
    lines.append("")
    for outcome_type in outcome_types:
        lines.append(
            "INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) "
            f"VALUES ({sql_literal(outcome_type)}, 'Module 2 tracker-derived outcome type') "
            "ON CONFLICT (outcome_type_name) DO NOTHING;"
        )
    lines.append("")

    for row in bundle["observations"]:
        notes = json_note(
            {
                "tracker_id": row["tracker_id"],
                "topic_id": row["topic_id"],
                "paper_tracker_id": row["paper_id"],
                "experiment_tracker_id": row["experiment_id"],
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
                "  FROM _m2_experiment_map e",
                "  CROSS JOIN ControlledVocabulary_EvidenceType et",
                "  CROSS JOIN ControlledVocabulary_OutcomeType ot",
                "  WHERE e.tracker_id = " + sql_literal(experiment_key(row)),
                "    AND et.evidence_type_name = " + sql_literal(row["evidence_type"]),
                "    AND ot.outcome_type_name = " + sql_literal(row["outcome_type"]),
                "  RETURNING observation_id",
                ")",
                f"INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT {sql_literal(row['tracker_id'])}, observation_id FROM inserted;",
                "",
            ]
        )

    for row in bundle["author_claims"]:
        paper_id = canonical_paper_id(row["paper_id"])
        notes = json_note(
            {
                "tracker_id": row["tracker_id"],
                "topic_id": row["topic_id"],
                "source_paper_tracker_id": row["paper_id"],
                "curator_notes": row["notes"],
            }
        )
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
                "  FROM _m2_paper_map p",
                "  WHERE p.tracker_id = " + sql_literal(paper_id),
                "  RETURNING claim_id",
                ")",
                f"INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT {sql_literal(row['tracker_id'])}, claim_id FROM inserted;",
                "",
            ]
        )

    for row in bundle["evidence_links"]:
        lines.extend(
            [
                "INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)",
                "SELECT c.claim_id, o.observation_id,",
                f"  {sql_literal(row['link_type'])},",
                f"  {sql_literal(json_note({'tracker_id': row['tracker_id'], 'strength': row['strength'], 'notes': row['notes']}))}",
                "FROM _m2_claim_map c",
                "JOIN _m2_observation_map o ON o.tracker_id = " + sql_literal(row["observation_id"]),
                "WHERE c.tracker_id = " + sql_literal(row["claim_id"]) + ";",
                "",
            ]
        )

    for draft in bundle["consensus_drafts"]:
        draft_text = " ".join(str(value) for value in draft.values())
        observation_ids = referenced_ids(draft_text, "M2B-O")
        boundary_ids = referenced_ids(draft_text, "M2B-B")
        notes = json_note(
            {
                "consensus_draft_id": draft["tracker_id"],
                "topic_id": draft["topic_id"],
                "evidence_status": draft["evidence_status"],
                "supporting_evidence_notes": draft["notes"],
                "observation_tracker_ids": observation_ids,
                "boundary_tracker_ids": boundary_ids,
            }
        )
        lines.extend(
            [
                "WITH inserted AS (",
                "  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)",
                "  VALUES (",
                f"    {sql_literal(draft['consensus_statement'])},",
                f"    {sql_literal(draft['topic_id'])},",
                "    1,",
                "    'consensus-ready first pass',",
                f"    {sql_literal(notes)}",
                "  )",
                "  RETURNING consensus_id",
                ")",
                f"INSERT INTO _m2_consensus_map (tracker_id, consensus_id) SELECT {sql_literal(draft['tracker_id'])}, consensus_id FROM inserted;",
                "",
            ]
        )
        for observation_id in observation_ids:
            lines.extend(
                [
                    "INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)",
                    "SELECT c.consensus_id, o.observation_id, 'supporting'",
                    "FROM _m2_consensus_map c",
                    "JOIN _m2_observation_map o ON o.tracker_id = " + sql_literal(observation_id),
                    "WHERE c.tracker_id = " + sql_literal(draft["tracker_id"]) + ";",
                    "",
                ]
            )

    consensus_observation_count = sum(
        len(referenced_ids(" ".join(str(value) for value in draft.values()), "M2B-O"))
        for draft in bundle["consensus_drafts"]
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
            "  SELECT COUNT(*) INTO paper_count FROM _m2_paper_map;",
            "  SELECT COUNT(*) INTO experiment_count FROM _m2_experiment_map;",
            "  SELECT COUNT(*) INTO observation_count FROM _m2_observation_map;",
            "  SELECT COUNT(*) INTO claim_count FROM _m2_claim_map;",
            "  SELECT COUNT(*) INTO link_count FROM EvidenceLink;",
            "  SELECT COUNT(*) INTO consensus_count FROM _m2_consensus_map;",
            "  SELECT COUNT(*) INTO consensus_observation_count FROM Consensus_Observation;",
            "  IF paper_count <> " + str(len(paper_ids)) + " THEN RAISE EXCEPTION 'Expected " + str(len(paper_ids)) + " papers, found %', paper_count; END IF;",
            "  IF experiment_count <> " + str(len(experiment_rows)) + " THEN RAISE EXCEPTION 'Unexpected experiment count %', experiment_count; END IF;",
            "  IF observation_count <> 50 THEN RAISE EXCEPTION 'Expected 50 observations, found %', observation_count; END IF;",
            "  IF claim_count <> 36 THEN RAISE EXCEPTION 'Expected 36 claims, found %', claim_count; END IF;",
            "  IF link_count <> 56 THEN RAISE EXCEPTION 'Expected 56 evidence links, found %', link_count; END IF;",
            "  IF consensus_count <> 8 THEN RAISE EXCEPTION 'Expected 8 consensus rows, found %', consensus_count; END IF;",
            "  IF consensus_observation_count <> " + str(consensus_observation_count) + " THEN RAISE EXCEPTION 'Unexpected consensus-observation count %', consensus_observation_count; END IF;",
            "END $$;",
            "",
            "COMMIT;",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--module-2a", type=Path, default=DEFAULT_MODULE_2A)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true", help="Validate generated SQL without writing it.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    config = MODULES["2b"]
    bundle = build_bundle(config)
    errors = validate_bundle(bundle, config)
    if errors:
        for error in errors:
            print(f"FAIL {error}", file=sys.stderr)
        return 1
    papers: dict[str, dict[str, str | None]] = {}
    papers.update(parse_primary_papers(args.module_2a))
    papers.update(parse_review_papers(args.module_2a))
    experiments = parse_experiments(args.module_2a)
    sql = render_materialization_sql(bundle, papers, experiments)
    if args.check:
        print(
            "PASS generated Module 2 full SQL "
            f"({len(referenced_papers(bundle))} papers/review anchors, "
            f"{len(referenced_experiment_rows(bundle))} tracker experiments, "
            f"{len(bundle['observations'])} observations)"
        )
        return 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(sql)
    print(f"Wrote {args.output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
