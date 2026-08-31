#!/usr/bin/env python3
"""Generate conservative Paper and paper-anchored edge-source SQL.

Only exact PMID records found in the local Phase-2 source archive or the
resolved paper-metadata table are used. This script deliberately does not
create Experiment, Observation, AuthorClaim, or EvidenceLink rows: those
require an experiment-level extraction that is not present for every paper.
"""

from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
PHASE2 = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review" / "module20_24_integrated_phase2_extractions.tsv"
LEDGER = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review" / "module20_24_evidence_grade_ledger.tsv"
METADATA = ROOT / "work" / "cross_module_synthesis" / "module20_24_canonical_paper_metadata.tsv"
SOURCE_ROOT = ROOT / "data" / "raw" / "evidence" / "module20_24_supervised_cli_phase2"
OUT_SQL = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review" / "module20_24_paper_provenance_materialization.sql"
REPORT = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review" / "module20_24_paper_provenance_materialization.md"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def text(node: ET.Element | None) -> str:
    if node is None:
        return ""
    return " ".join(part.strip() for part in node.itertext() if part.strip())


def child(parent: ET.Element, path: str) -> str:
    return text(parent.find(path))


def xml_records() -> dict[str, dict[str, str]]:
    records: dict[str, dict[str, str]] = {}
    for path in sorted(SOURCE_ROOT.rglob("*.xml")):
        try:
            root = ET.parse(path).getroot()
        except (ET.ParseError, OSError):
            continue
        for article in root.findall(".//PubmedArticle"):
            pmid = child(article, "./MedlineCitation/PMID")
            if not pmid or pmid in records:
                continue
            article_node = article.find("./MedlineCitation/Article")
            if article_node is None:
                continue
            journal = article_node.find("./Journal")
            issue = journal.find("./JournalIssue") if journal is not None else None
            authors = []
            for author in article_node.findall("./AuthorList/Author"):
                name = " ".join(part for part in (child(author, "./ForeName"), child(author, "./LastName")) if part)
                if not name:
                    name = child(author, "./CollectiveName")
                if name:
                    authors.append(name)
            ids = {
                item.attrib.get("IdType", "").lower(): text(item)
                for item in article.findall("./PubmedData/ArticleIdList/ArticleId")
            }
            record = {
                "pmid": pmid,
                "title": child(article_node, "./ArticleTitle"),
                "authors": "; ".join(authors),
                "journal": child(journal, "./Title") if journal is not None else "",
                "volume": child(issue, "./Volume") if issue is not None else "",
                "issue": child(issue, "./Issue") if issue is not None else "",
                "pages": child(article_node, "./Pagination/MedlinePgn"),
                "doi": ids.get("doi", ""),
                "pmcid": ids.get("pmc", ""),
                "publication_year": "",
                "abstract": " ".join(text(node) for node in article_node.findall("./Abstract/AbstractText")),
                "source_url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                "source_file": str(path.relative_to(ROOT)),
            }
            for date_path in ("./ArticleDate", "./Journal/JournalIssue/PubDate"):
                date_node = article_node.find(date_path) if date_path == "./ArticleDate" else article_node.find(date_path)
                candidate = child(date_node, "./Year") if date_node is not None else ""
                if not candidate and date_node is not None:
                    candidate = re.search(r"\b(18\d{2}|19\d{2}|20\d{2})\b", text(date_node)).group(1) if re.search(r"\b(18\d{2}|19\d{2}|20\d{2})\b", text(date_node)) else ""
                if candidate:
                    record["publication_year"] = candidate
                    break
            records[pmid] = record
    return records


def sql(value: str | None) -> str:
    if value is None or not value.strip():
        return "NULL"
    return "'" + value.replace("'", "''") + "'"


def json_sql(payload: dict[str, object]) -> str:
    return sql(json.dumps(payload, sort_keys=True))


def stable_pmids(value: str) -> set[str]:
    return set(re.findall(r"\bPMID:(\d+)\b", value or "", flags=re.I))


def normalize_species(value: str) -> str:
    value = value.lower()
    has_mouse = "mouse" in value
    has_human = "human" in value
    if has_mouse and has_human:
        return "mixed"
    if has_mouse:
        return "mouse"
    if has_human:
        return "human"
    return "not_applicable"


def normalize_scope(value: str) -> str:
    value = value.lower()
    if "negative" in value:
        return "negative_evidence"
    if "direct" in value:
        return "direct_edge"
    if "pathway" in value:
        return "pathway_membership"
    return "contextual_support"


def normalize_support(value: str) -> str:
    value = value.lower()
    if "database" in value:
        return "database_curated"
    if "review" in value:
        return "review_statement"
    if "primary" in value or "experiment" in value:
        return "primary_experiment"
    return "manual_background"


def normalize_confidence(value: str) -> str:
    value = value.strip().lower()
    if value == "high":
        return "high"
    if value == "medium":
        return "medium"
    if value == "low":
        return "low"
    return "uncertain"


def main() -> None:
    phase2 = read_tsv(PHASE2)
    ledger = read_tsv(LEDGER)
    metadata = read_tsv(METADATA)
    phase_by_evidence: dict[str, set[str]] = defaultdict(set)
    for row in phase2:
        phase_by_evidence[row["b_evidence_id"]].update(stable_pmids(row.get("canonical_paper_key", "")))

    metadata_by_pmid: dict[str, dict[str, str]] = {}
    for row in metadata:
        if row.get("paper_ready") != "true" or not row.get("pmid"):
            continue
        metadata_by_pmid[row["pmid"]] = row

    xml = xml_records()
    pmids = sorted({pmid for row in phase2 for pmid in stable_pmids(row.get("canonical_paper_key", ""))})
    papers: dict[str, dict[str, str]] = {}
    for pmid in pmids:
        record = dict(metadata_by_pmid.get(pmid, {}))
        record.update({key: value for key, value in xml.get(pmid, {}).items() if value})
        if not record.get("title"):
            continue
        record.setdefault("pmid", pmid)
        record.setdefault("source_url", f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/")
        papers[pmid] = record

    source_rows = []
    for row in ledger:
        if row["module"] not in {"20B", "21B", "22B", "23B", "24B"}:
            continue
        for pmid in sorted(phase_by_evidence.get(row["b_evidence_id"], set()) & set(papers)):
            source_rows.append((row, pmid))

    lines = [
        "-- Module 20B-24B paper provenance materialization generated from exact local source records.",
        "-- This file inserts Paper rows and paper-anchored SignalingEdgeSource rows only.",
        "-- It does not create Experiment, Observation, AuthorClaim, or EvidenceLink rows.",
        "BEGIN;",
        "",
    ]
    for pmid in sorted(papers):
        row = papers[pmid]
        year = row.get("publication_year", "")
        if not year.isdigit() or not 1800 < int(year) <= 2026:
            year_sql = "NULL"
        else:
            year_sql = year
        lines.extend([
            "INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, abstract, url)",
            "VALUES (",
            f"  {sql(row.get('title'))}, {sql(row.get('authors'))}, {year_sql}, {sql(row.get('journal'))},",
            f"  {sql(row.get('volume'))}, {sql(row.get('issue'))}, {sql(row.get('pages'))}, {sql(row.get('doi'))},",
            f"  {sql('PMID:' + pmid)}, {sql(row.get('abstract'))}, {sql(row.get('source_url'))}",
            ") ON CONFLICT (pmid) DO NOTHING;",
            "",
        ])

    for row, pmid in source_rows:
        note = {
            "module20_24_register_evidence_id": row["b_evidence_id"],
            "register_edge_ids": row["b_edge_id"],
            "register_source_locator": row["source_locator"],
            "paper_anchor": "PMID:" + pmid,
            "materialization_status": "paper_anchored_register_provenance",
        }
        scope = normalize_scope(row["source_scope"])
        support = normalize_support(row["support_kind"])
        confidence = normalize_confidence(row["confidence_tier"])
        lines.extend([
            "INSERT INTO SignalingEdgeSource (edge_id, paper_id, support_kind, species_support, source_scope, confidence_tier, citation_note, notes, evidence_grade, context_level, grading_basis, grading_status)",
            "SELECT s.edge_id, p.paper_id,",
            f"  {sql(support)}, {sql(normalize_species(row['species_support']))}, {sql(scope)}, {sql(confidence)},",
            f"  {sql(row['citation_note'])}, {json_sql(note)}, {sql(row['evidence_grade'])}, {sql(row['context_level'])},",
            f"  {sql(row['grading_basis'] + ' ' + row.get('context_basis', ''))}, {sql(row['grading_status'])}",
            "FROM SignalingEdgeRegisterSource s",
            "JOIN Paper p ON p.pmid = " + sql("PMID:" + pmid),
            "WHERE s.module = " + sql(row["module"]),
            "  AND s.register_evidence_id = " + sql(row["b_evidence_id"]),
            "  AND NOT EXISTS (",
            "    SELECT 1 FROM SignalingEdgeSource existing",
            "    WHERE existing.edge_id = s.edge_id AND existing.paper_id = p.paper_id",
            "      AND existing.notes = " + json_sql(note),
            "  );",
            "",
        ])
    lines.extend([
        "COMMIT;",
        "",
    ])
    OUT_SQL.write_text("\n".join(lines))

    by_module = defaultdict(int)
    for row, _ in source_rows:
        by_module[row["module"]] += 1
    report = [
        "# Module 20B–24B paper provenance materialization",
        "",
        "Generated SQL is limited to exact local PubMed paper records and",
        "paper-anchored register provenance. It does not create experiment-level",
        "or claim/observation rows.",
        "",
        f"- Unique PMID anchors in Phase-2: {len(pmids):,}",
        f"- Exact local/metadata Paper records: {len(papers):,}",
        f"- Paper-anchored register-source links: {len(source_rows):,}",
        "",
        "| Module | Paper-anchored source links |",
        "|---|---:|",
    ]
    report.extend(f"| {module} | {by_module[module]:,} |" for module in ("20B", "21B", "22B", "23B", "24B"))
    report.extend([
        "",
        "Unresolved PMID anchors, DOI-only/PMCID-only cases without a resolved",
        "Paper row, and all experiment/observation/claim routes remain in staging.",
        "",
    ])
    REPORT.write_text("\n".join(report))
    print(f"paper_records={len(papers)} source_links={len(source_rows)} sql={OUT_SQL}")


if __name__ == "__main__":
    main()
