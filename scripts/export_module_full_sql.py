#!/usr/bin/env python3
"""Generate first-pass SQL materialization for B-phase modules.

This generic exporter loads validated tracker evidence bundles into the core
schema used by the Module 1 and Module 2 materializers:

- Paper
- ExperimentalParadigm
- Experiment
- ControlledVocabulary_EvidenceType / ControlledVocabulary_OutcomeType
- Observation
- AuthorClaim
- EvidenceLink
- Consensus
- Consensus_Observation

The generated SQL preserves tracker IDs in JSON notes and creates synthetic
paper records only for composite tracker references that cannot be resolved to a
single Paper Inventory or Review row.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from export_tracker_evidence_bundle import MODULES, ModuleConfig, build_bundle, referenced_ids, validate_bundle


ROOT = Path(__file__).resolve().parents[1]


MODULE_A_TRACKERS = {
    "2b": ROOT / "modules" / "Module_2A_TRACKER.md",
    "3b": ROOT / "modules" / "Module_3A_TRACKER.md",
    "4b": ROOT / "modules" / "Module_4A_TRACKER.md",
    "5b": ROOT / "modules" / "Module_5A_TRACKER.md",
    "6b": ROOT / "modules" / "Module_6A_TRACKER.md",
    "7b": ROOT / "modules" / "Module_7A_TRACKER.md",
    "8b": ROOT / "modules" / "Module_8A_TRACKER.md",
    "9b": ROOT / "modules" / "Module_9A_TRACKER.md",
    "10b": ROOT / "modules" / "Module_10A_TRACKER.md",
    "11b": ROOT / "modules" / "Module_11A_TRACKER.md",
    "12b": ROOT / "modules" / "Module_12A_TRACKER.md",
    "13b": ROOT / "modules" / "Module_13A_TRACKER.md",
    "14b": ROOT / "modules" / "Module_14A_TRACKER.md",
}

MODULE_TOPICS = {
    "2b": "biomaterials and scaffold repair",
    "3b": "immune and myeloid modulation",
    "4b": "cell transplantation and graft integration",
    "5b": "axon regeneration, remyelination, and white matter repair",
    "6b": "human chronic SCI pathology and translational imaging",
    "7b": "host fibroinflammatory conditioning",
    "8b": "in vivo SCI model systems",
    "9b": "in vitro and ex vivo SCI model systems",
    "10b": "SCI clinical trials",
    "11b": "spinal cord ischemic conditioning in cardiac and aortic surgery",
    "12b": "innate immune conditioning and tolerance biology",
    "13b": "traumatic SCI pathobiology and chronic lesion formation",
    "14b": "CRISPR-based epigenome editing for neuroregeneration",
}


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
        return []
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
    match = re.search(r"\d{4}", value)
    return match.group(0) if match else "NULL"


def json_note(payload: dict[str, Any]) -> str:
    return json.dumps(payload, sort_keys=True)


def table_value(row: dict[str, str], *keys: str) -> str | None:
    for key in keys:
        value = row.get(key)
        if value not in {None, "", "-", "—"}:
            return value
    return None


def parse_papers(module_a: Path) -> dict[str, dict[str, str | None]]:
    markdown = module_a.read_text()
    papers: dict[str, dict[str, str | None]] = {}
    for row in extract_table(markdown, "## Paper Inventory"):
        paper_id = table_value(row, "paper_id")
        if not paper_id:
            continue
        papers[paper_id] = {
            "title": table_value(row, "title") or f"Untitled tracker paper {paper_id}",
            "authors": table_value(row, "authors", "first_author") or "mSCIdblit curator",
            "year": table_value(row, "year"),
            "journal": table_value(row, "journal"),
            "volume": table_value(row, "volume"),
            "issue": table_value(row, "issue"),
            "pages": table_value(row, "pages"),
            "doi": table_value(row, "doi"),
            "pmid": table_value(row, "pmid"),
            "url": table_value(row, "url"),
            "notes": table_value(row, "notes", "status"),
        }
    for row in extract_table(markdown, "## Review and Map Anchors"):
        paper_id = table_value(row, "review_id")
        if not paper_id:
            continue
        papers[paper_id] = {
            "title": table_value(row, "title") or f"Untitled tracker review {paper_id}",
            "authors": table_value(row, "authors", "first_author") or "mSCIdblit curator",
            "year": table_value(row, "year"),
            "journal": table_value(row, "journal"),
            "volume": table_value(row, "volume"),
            "issue": table_value(row, "issue"),
            "pages": table_value(row, "pages"),
            "doi": table_value(row, "doi"),
            "pmid": table_value(row, "pmid"),
            "url": table_value(row, "url"),
            "notes": table_value(row, "notes", "focus", "review_focus"),
        }
    return papers


def expanded_ids(value: str, config: ModuleConfig, suffix: str) -> list[str]:
    module_a_prefix = config.id_prefix.replace("B", "A")
    return referenced_ids(value, f"{module_a_prefix}-{suffix}")


def expanded_paper_ids(value: str, config: ModuleConfig) -> list[str]:
    return expanded_ids(value, config, "P") + expanded_ids(value, config, "R")


def canonical_paper_id(value: str, config: ModuleConfig) -> str:
    expanded = expanded_paper_ids(value, config)
    return expanded[0] if expanded else value


def referenced_papers(bundle: dict[str, Any], config: ModuleConfig) -> list[str]:
    paper_ids: set[str] = set()
    for row in bundle["observations"] + bundle["author_claims"]:
        expanded = expanded_paper_ids(row["paper_id"], config)
        if expanded:
            paper_ids.update(expanded)
        else:
            paper_ids.add(row["paper_id"])
    return sorted(paper_ids)


def experiment_key(row: dict[str, str]) -> str:
    return f"{row['paper_id']}::{row['experiment_id']}"


def referenced_experiment_rows(bundle: dict[str, Any]) -> list[dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for observation in bundle["observations"]:
        rows[experiment_key(observation)] = observation
    return [rows[key] for key in sorted(rows)]


def experiment_number(experiment_id: str) -> str:
    match = re.search(r"-E(\d{3})", experiment_id)
    return str(int(match.group(1))) if match else "NULL"


def synthetic_paper(paper_id: str, module_label: str) -> dict[str, str | None]:
    return {
        "title": f"{module_label} synthetic source record for {paper_id}",
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


def normalized_link_type(row: dict[str, str]) -> str:
    return row.get("link_type") or row.get("relationship") or "supports"


def link_strength(row: dict[str, str]) -> str | None:
    return row.get("strength") or row.get("evidence_weight")


def consensus_observation_ids(draft: dict[str, str], config: ModuleConfig) -> list[str]:
    observation_prefix = f"{config.id_prefix}-O"
    text = " ".join(str(value) for value in draft.values())
    return referenced_ids(text, observation_prefix)


def consensus_boundary_ids(draft: dict[str, str], config: ModuleConfig) -> list[str]:
    text = " ".join(str(value) for value in draft.values())
    if "all boundary records" in text.lower():
        return ["all boundary records"]
    return referenced_ids(text, config.boundary_prefix)


def render_materialization_sql(
    config: ModuleConfig,
    bundle: dict[str, Any],
    papers: dict[str, dict[str, str | None]],
) -> str:
    module_num = config.key.removesuffix("b")
    module_label = config.label
    table_prefix = f"_m{module_num}"
    paper_ids = referenced_papers(bundle, config)
    for paper_id in paper_ids:
        papers.setdefault(paper_id, synthetic_paper(paper_id, module_label))

    experiment_rows = referenced_experiment_rows(bundle)
    module_topic = MODULE_TOPICS.get(config.key, module_label)
    lines: list[str] = [
        f"-- {module_label} full first-pass materialization generated from tracker-derived JSON.",
        "-- This script is intended for a fresh database loaded with schema/schema.sql and scripts/seed_controlled_vocab.sql.",
        "BEGIN;",
        "",
        f"CREATE TEMP TABLE {table_prefix}_paper_map (tracker_id TEXT PRIMARY KEY, paper_id INTEGER NOT NULL);",
        f"CREATE TEMP TABLE {table_prefix}_paradigm_map (tracker_id TEXT PRIMARY KEY, paradigm_id INTEGER NOT NULL);",
        f"CREATE TEMP TABLE {table_prefix}_experiment_map (tracker_id TEXT PRIMARY KEY, experiment_id INTEGER NOT NULL);",
        f"CREATE TEMP TABLE {table_prefix}_observation_map (tracker_id TEXT PRIMARY KEY, observation_id INTEGER NOT NULL);",
        f"CREATE TEMP TABLE {table_prefix}_claim_map (tracker_id TEXT PRIMARY KEY, claim_id INTEGER NOT NULL);",
        f"CREATE TEMP TABLE {table_prefix}_link_map (tracker_id TEXT PRIMARY KEY, link_id INTEGER NOT NULL);",
        f"CREATE TEMP TABLE {table_prefix}_consensus_map (tracker_id TEXT PRIMARY KEY, consensus_id INTEGER NOT NULL);",
        "",
    ]

    for paper_id in paper_ids:
        paper = papers[paper_id]
        notes = json_note({"tracker_id": paper_id, "module": module_label, "curator_notes": paper.get("notes")})
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
                f"INSERT INTO {table_prefix}_paper_map (tracker_id, paper_id) SELECT {sql_literal(paper_id)}, paper_id FROM inserted;",
                "",
            ]
        )

    for paper_id in paper_ids:
        lines.extend(
            [
                "WITH inserted AS (",
                "  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)",
                f"  SELECT paper_id, {sql_literal(module_label + ' curated evidence extraction')},",
                f"    {sql_literal('First-pass ' + module_label + ' ' + module_topic + ' curation for ' + paper_id)},",
                f"    {sql_literal('Tracker-derived materialization from ' + config.tracker.name)}",
                f"  FROM {table_prefix}_paper_map WHERE tracker_id = " + sql_literal(paper_id),
                "  RETURNING paradigm_id",
                ")",
                f"INSERT INTO {table_prefix}_paradigm_map (tracker_id, paradigm_id) SELECT {sql_literal(paper_id)}, paradigm_id FROM inserted;",
                "",
            ]
        )

    for row in experiment_rows:
        key = experiment_key(row)
        paper_id = canonical_paper_id(row["paper_id"], config)
        notes = json_note(
            {
                "tracker_key": key,
                "source_paper_tracker_id": row["paper_id"],
                "source_experiment_tracker_id": row["experiment_id"],
                "observation_tracker_ids": [
                    obs["tracker_id"] for obs in bundle["observations"] if experiment_key(obs) == key
                ],
            }
        )
        lines.extend(
            [
                "WITH inserted AS (",
                "  INSERT INTO Experiment (",
                "    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes",
                "  )",
                "  SELECT p.paper_id, ep.paradigm_id,",
                f"    {experiment_number(row['experiment_id'])},",
                f"    {sql_literal(row['figure_ref'])},",
                f"    {sql_literal('Tracker experiment ' + row['experiment_id'])},",
                f"    {sql_literal(module_label + ' tracker-derived experiment placeholder for SQL materialization.')},",
                f"    {sql_literal(notes)}",
                f"  FROM {table_prefix}_paper_map p",
                f"  JOIN {table_prefix}_paradigm_map ep ON ep.tracker_id = p.tracker_id",
                "  WHERE p.tracker_id = " + sql_literal(paper_id),
                "  RETURNING experiment_id",
                ")",
                f"INSERT INTO {table_prefix}_experiment_map (tracker_id, experiment_id) SELECT {sql_literal(key)}, experiment_id FROM inserted;",
                "",
            ]
        )

    evidence_types = sorted({row["evidence_type"] for row in bundle["observations"]})
    outcome_types = sorted({row["outcome_type"] for row in bundle["observations"]})
    for evidence_type in evidence_types:
        lines.append(
            "INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) "
            f"VALUES ({sql_literal(evidence_type)}, {sql_literal(module_label + ' tracker-derived evidence type')}) "
            "ON CONFLICT (evidence_type_name) DO NOTHING;"
        )
    lines.append("")
    for outcome_type in outcome_types:
        lines.append(
            "INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) "
            f"VALUES ({sql_literal(outcome_type)}, {sql_literal(module_label + ' tracker-derived outcome type')}) "
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
                f"  FROM {table_prefix}_experiment_map e",
                "  CROSS JOIN ControlledVocabulary_EvidenceType et",
                "  CROSS JOIN ControlledVocabulary_OutcomeType ot",
                "  WHERE e.tracker_id = " + sql_literal(experiment_key(row)),
                "    AND et.evidence_type_name = " + sql_literal(row["evidence_type"]),
                "    AND ot.outcome_type_name = " + sql_literal(row["outcome_type"]),
                "  RETURNING observation_id",
                ")",
                f"INSERT INTO {table_prefix}_observation_map (tracker_id, observation_id) SELECT {sql_literal(row['tracker_id'])}, observation_id FROM inserted;",
                "",
            ]
        )

    for row in bundle["author_claims"]:
        paper_id = canonical_paper_id(row["paper_id"], config)
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
                f"  FROM {table_prefix}_paper_map p",
                "  WHERE p.tracker_id = " + sql_literal(paper_id),
                "  RETURNING claim_id",
                ")",
                f"INSERT INTO {table_prefix}_claim_map (tracker_id, claim_id) SELECT {sql_literal(row['tracker_id'])}, claim_id FROM inserted;",
                "",
            ]
        )

    for row in bundle["evidence_links"]:
        notes = json_note({"tracker_id": row["tracker_id"], "strength": link_strength(row), "notes": row["notes"]})
        lines.extend(
            [
                "WITH inserted AS (",
                "  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)",
                "  SELECT c.claim_id, o.observation_id,",
                f"  {sql_literal(normalized_link_type(row))},",
                f"  {sql_literal(notes)}",
                f"  FROM {table_prefix}_claim_map c",
                f"  JOIN {table_prefix}_observation_map o ON o.tracker_id = " + sql_literal(row["observation_id"]),
                "  WHERE c.tracker_id = " + sql_literal(row["claim_id"]),
                "  RETURNING link_id",
                ")",
                f"INSERT INTO {table_prefix}_link_map (tracker_id, link_id) SELECT {sql_literal(row['tracker_id'])}, link_id FROM inserted;",
                "",
            ]
        )

    consensus_observation_count = 0
    for draft in bundle["consensus_drafts"]:
        observation_ids = consensus_observation_ids(draft, config)
        consensus_observation_count += len(observation_ids)
        boundary_ids = consensus_boundary_ids(draft, config)
        notes = json_note(
            {
                "consensus_draft_id": draft["tracker_id"],
                "topic_id": draft["topic_id"],
                "readiness_status": draft.get("readiness_status") or draft.get("status"),
                "source_agreement_label": draft.get("source_agreement_label"),
                "supporting_evidence_notes": draft.get("notes") or draft.get("boundary_notes"),
                "claim_tracker_ids": referenced_ids(" ".join(str(value) for value in draft.values()), f"{config.id_prefix}-C"),
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
                f"INSERT INTO {table_prefix}_consensus_map (tracker_id, consensus_id) SELECT {sql_literal(draft['tracker_id'])}, consensus_id FROM inserted;",
                "",
            ]
        )
        for observation_id in observation_ids:
            lines.extend(
                [
                    "INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)",
                    "SELECT c.consensus_id, o.observation_id, 'supporting'",
                    f"FROM {table_prefix}_consensus_map c",
                    f"JOIN {table_prefix}_observation_map o ON o.tracker_id = " + sql_literal(observation_id),
                    "WHERE c.tracker_id = " + sql_literal(draft["tracker_id"]) + ";",
                    "",
                ]
            )

    expected = config.expected_counts
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
            f"  SELECT COUNT(*) INTO paper_count FROM {table_prefix}_paper_map;",
            f"  SELECT COUNT(*) INTO experiment_count FROM {table_prefix}_experiment_map;",
            f"  SELECT COUNT(*) INTO observation_count FROM {table_prefix}_observation_map;",
            f"  SELECT COUNT(*) INTO claim_count FROM {table_prefix}_claim_map;",
            f"  SELECT COUNT(*) INTO link_count FROM {table_prefix}_link_map;",
            f"  SELECT COUNT(*) INTO consensus_count FROM {table_prefix}_consensus_map;",
            "  SELECT COUNT(*) INTO consensus_observation_count",
            "  FROM Consensus_Observation co",
            f"  JOIN {table_prefix}_consensus_map cm ON cm.consensus_id = co.consensus_id;",
            "  IF paper_count <> "
            + str(len(paper_ids))
            + " THEN RAISE EXCEPTION 'Expected "
            + str(len(paper_ids))
            + " papers, found %', paper_count; END IF;",
            "  IF experiment_count <> "
            + str(len(experiment_rows))
            + " THEN RAISE EXCEPTION 'Unexpected experiment count %', experiment_count; END IF;",
            "  IF observation_count <> "
            + str(expected["observations"])
            + " THEN RAISE EXCEPTION 'Expected "
            + str(expected["observations"])
            + " observations, found %', observation_count; END IF;",
            "  IF claim_count <> "
            + str(expected["author_claims"])
            + " THEN RAISE EXCEPTION 'Expected "
            + str(expected["author_claims"])
            + " claims, found %', claim_count; END IF;",
            "  IF link_count <> "
            + str(expected["evidence_links"])
            + " THEN RAISE EXCEPTION 'Expected "
            + str(expected["evidence_links"])
            + " evidence links, found %', link_count; END IF;",
            "  IF consensus_count <> "
            + str(expected["consensus_drafts"])
            + " THEN RAISE EXCEPTION 'Expected "
            + str(expected["consensus_drafts"])
            + " consensus rows, found %', consensus_count; END IF;",
            "  IF consensus_observation_count <> "
            + str(consensus_observation_count)
            + " THEN RAISE EXCEPTION 'Unexpected consensus-observation count %', consensus_observation_count; END IF;",
            "END $$;",
            "",
            "COMMIT;",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--module",
        choices=sorted(key for key in MODULES if key != "1b"),
        action="append",
        help="Module key to materialize. May be repeated. Defaults to 3b-14b.",
    )
    parser.add_argument("--check", action="store_true", help="Validate generated SQL without writing it.")
    return parser.parse_args(argv)


def default_output(config: ModuleConfig) -> Path:
    module_num = config.key.removesuffix("b")
    return ROOT / "data" / "processed" / f"module{module_num}_full_materialization.sql"


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    module_keys = args.module or ["3b", "4b", "5b", "6b", "7b", "8b", "9b", "10b", "11b", "12b", "13b", "14b"]
    failed = False
    for module_key in module_keys:
        config = MODULES[module_key]
        bundle = build_bundle(config)
        errors = validate_bundle(bundle, config)
        if errors:
            failed = True
            for error in errors:
                print(f"FAIL {config.label}: {error}", file=sys.stderr)
            continue
        papers = parse_papers(MODULE_A_TRACKERS[module_key])
        sql = render_materialization_sql(config, bundle, papers)
        output = default_output(config)
        if args.check:
            print(
                f"PASS generated {config.label} full SQL "
                f"({len(referenced_papers(bundle, config))} papers/review anchors, "
                f"{len(referenced_experiment_rows(bundle))} tracker experiments, "
                f"{len(bundle['observations'])} observations)"
            )
        else:
            output.write_text(sql)
            print(f"Wrote {output.relative_to(ROOT)}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
