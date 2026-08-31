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
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
PHASE2 = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review" / "module20_24_integrated_phase2_extractions.tsv"
LEDGER = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review" / "module20_24_evidence_grade_ledger.tsv"
METADATA = ROOT / "work" / "cross_module_synthesis" / "module20_24_canonical_paper_metadata.tsv"
IDENTITY = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review" / "module20_24_phase2_paper_identity_resolution.tsv"
SOURCE_ROOT = ROOT / "data" / "raw" / "evidence" / "module20_24_supervised_cli_phase2"
OUT_SQL = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review" / "module20_24_paper_provenance_materialization.sql"
REPORT = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review" / "module20_24_paper_provenance_materialization.md"


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
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


def bioc_records() -> dict[str, dict[str, str]]:
    """Read exact bibliographic metadata embedded in local BioC artifacts.

    BioC exports are full-text source artifacts rather than filename-derived
    metadata.  This reader accepts a PMID only when it is present in the
    document or passage ``infons`` and accepts a title only when it is present
    in a title passage.  Files without both values remain unavailable to the
    Paper materializer.  Existing PubMed XML records take precedence when the
    two formats contain the same PMID.
    """

    records: dict[str, dict[str, str]] = {}
    for path in sorted(SOURCE_ROOT.rglob("*bioc.json")):
        try:
            payload = json.loads(path.read_text())
        except (json.JSONDecodeError, OSError, UnicodeDecodeError):
            continue

        collections = payload if isinstance(payload, list) else [payload]
        for collection in collections:
            if not isinstance(collection, dict):
                continue
            for document in collection.get("documents", []) or []:
                if not isinstance(document, dict):
                    continue
                document_infons = document.get("infons", {}) or {}
                passages = [
                    passage for passage in (document.get("passages", []) or [])
                    if isinstance(passage, dict)
                ]
                pmid = str(
                    document_infons.get("article-id_pmid")
                    or document_infons.get("pmid")
                    or ""
                ).strip()
                title = ""
                abstract_parts: list[str] = []
                journal = ""
                volume = ""
                issue = ""
                publication_year = ""
                authors: list[str] = []
                doi = ""
                pmcid = ""
                for passage in passages:
                    infons = passage.get("infons", {}) or {}
                    text_value = str(passage.get("text") or "").strip()
                    passage_pmid = str(
                        infons.get("article-id_pmid")
                        or infons.get("pmid")
                        or ""
                    ).strip()
                    if not pmid and passage_pmid:
                        pmid = passage_pmid
                    if not doi:
                        doi = str(infons.get("article-id_doi") or "").strip()
                    if not pmcid:
                        pmcid = str(infons.get("article-id_pmc") or "").strip()
                    section_type = str(infons.get("section_type") or "").upper()
                    passage_type = str(infons.get("type") or "").lower()
                    if not title and section_type == "TITLE" and text_value:
                        title = text_value
                    if text_value and (section_type == "ABSTRACT" or passage_type == "abstract"):
                        abstract_parts.append(text_value)
                    journal = journal or str(infons.get("journal") or "").strip()
                    volume = volume or str(infons.get("volume") or "").strip()
                    issue = issue or str(infons.get("issue") or "").strip()
                    publication_year = publication_year or str(infons.get("year") or "").strip()
                    for key, value in infons.items():
                        if not str(key).startswith("name_"):
                            continue
                        raw_name = str(value).strip()
                        if raw_name and raw_name not in authors:
                            authors.append(raw_name)

                if not pmid.isdigit() or not title:
                    continue
                records.setdefault(
                    pmid,
                    {
                        "pmid": pmid,
                        "title": title,
                        "authors": "; ".join(authors),
                        "publication_year": publication_year,
                        "journal": journal,
                        "volume": volume,
                        "issue": issue,
                        "pages": "",
                        "doi": doi,
                        "pmcid": pmcid,
                        "abstract": " ".join(abstract_parts),
                        "source_url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                        "source_file": str(path.relative_to(ROOT)),
                    },
                )
    return records


class _CitationMetaParser(HTMLParser):
    """Collect citation metadata without interpreting page text as identity."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.values: dict[str, list[str]] = defaultdict(list)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "meta":
            return
        attributes = {key.lower(): (value or "").strip() for key, value in attrs}
        name = attributes.get("name") or attributes.get("property")
        content = attributes.get("content", "")
        if name and content:
            self.values[name.lower()].append(content)


def html_records() -> dict[str, dict[str, str]]:
    """Read exact citation metadata embedded in local HTML artifacts.

    Only ``citation_pmid`` and ``citation_title`` meta values are used to
    establish a Paper record.  Other fields are copied only when the same
    page exposes the corresponding citation metadata.  Filenames and page
    URLs are never used to infer identity.
    """

    records: dict[str, dict[str, str]] = {}
    for path in sorted(SOURCE_ROOT.rglob("*.html")):
        parser = _CitationMetaParser()
        try:
            parser.feed(path.read_text(errors="ignore"))
            parser.close()
        except (OSError, UnicodeError):
            continue
        values = parser.values
        pmids = [value for value in values.get("citation_pmid", []) if value.isdigit()]
        titles = values.get("citation_title", [])
        if not pmids or not titles or not titles[0].strip():
            continue
        pmid = pmids[0]
        year_match = re.search(r"\b(18\d{2}|19\d{2}|20\d{2})\b", " ".join(values.get("citation_publication_date", [])))
        records.setdefault(
            pmid,
            {
                "pmid": pmid,
                "title": titles[0].strip(),
                "authors": "; ".join(values.get("citation_author", [])),
                "publication_year": year_match.group(1) if year_match else "",
                "journal": " ".join(values.get("citation_journal_title", [])),
                "volume": " ".join(values.get("citation_volume", [])),
                "issue": " ".join(values.get("citation_issue", [])),
                "pages": "-".join(values.get("citation_firstpage", []) + values.get("citation_lastpage", [])),
                "doi": " ".join(values.get("citation_doi", [])),
                "pmcid": " ".join(values.get("citation_pmcid", [])),
                "abstract": "",
                "source_url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                "source_file": str(path.relative_to(ROOT)),
            },
        )
    return records


def sql(value: str | None) -> str:
    if value is None or not value.strip():
        return "NULL"
    return "'" + value.replace("'", "''") + "'"


def json_sql(payload: dict[str, object]) -> str:
    return sql(json.dumps(payload, sort_keys=True))


def stable_pmids(value: str) -> set[str]:
    return set(re.findall(r"\bPMID:(\d+)\b", value or "", flags=re.I))


def identity_metadata_record(row: dict[str, str]) -> dict[str, str]:
    """Convert exact resolver metadata to the Paper materializer shape."""
    return {
        "pmid": row.get("resolved_pmid", ""),
        "pmcid": row.get("resolved_pmcid", ""),
        "doi": row.get("resolved_doi", ""),
        "title": row.get("source_metadata_title", ""),
        "authors": row.get("source_metadata_authors", ""),
        "publication_year": row.get("source_metadata_year", ""),
        "journal": row.get("source_metadata_journal", ""),
        "volume": "",
        "issue": "",
        "pages": "",
        "abstract": row.get("source_metadata_abstract", ""),
        "source_url": row.get("source_metadata_url", ""),
    }


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


def normalized_title(value: str) -> str:
    """Compare titles without treating punctuation/case as identity conflicts."""
    greek_names = {
        "α": "alpha", "β": "beta", "γ": "gamma", "δ": "delta",
        "ε": "epsilon", "θ": "theta", "κ": "kappa", "λ": "lambda",
        "μ": "mu", "π": "pi", "ρ": "rho", "σ": "sigma", "τ": "tau",
        "φ": "phi", "χ": "chi", "ψ": "psi", "ω": "omega",
    }
    lowered = (value or "").lower()
    lowered = "".join(greek_names.get(char, char) for char in lowered)
    return re.sub(r"[^a-z0-9]+", "", lowered)


def main() -> None:
    phase2 = read_tsv(PHASE2)
    ledger = read_tsv(LEDGER)
    metadata = read_tsv(METADATA)
    identities = read_tsv(IDENTITY)
    identity_manifest_present = IDENTITY.exists()
    identity_by_extraction = {
        row["extraction_id"]: row for row in identities if row.get("extraction_id")
    }
    phase_by_evidence: dict[str, set[str]] = defaultdict(set)
    for row in phase2:
        identity = identity_by_extraction.get(row.get("extraction_id", ""), {})
        if identity.get("resolved_pmid"):
            phase_by_evidence[row["b_evidence_id"]].add(identity["resolved_pmid"])
        elif not identity_manifest_present:
            # Preserve the pre-bridge route only when the resolver has not run.
            # Once it exists, unresolved/ambiguous rows must remain unresolved.
            phase_by_evidence[row["b_evidence_id"]].update(stable_pmids(row.get("canonical_paper_key", "")))

    metadata_by_pmid: dict[str, dict[str, str]] = {}
    for row in metadata:
        if row.get("paper_ready") != "true" or not row.get("pmid"):
            continue
        metadata_by_pmid[row["pmid"]] = row

    identity_by_pmid: dict[str, dict[str, str]] = {}
    identity_conflicts: set[str] = set()
    for row in identities:
        pmid = row.get("resolved_pmid", "")
        title = row.get("source_metadata_title", "")
        if not pmid or not title:
            continue
        if pmid in identity_conflicts:
            continue
        record = identity_metadata_record(row)
        existing = identity_by_pmid.get(pmid)
        if existing and existing.get("title") and normalized_title(existing["title"]) != normalized_title(title):
            identity_conflicts.add(pmid)
            identity_by_pmid.pop(pmid, None)
            continue
        identity_by_pmid.setdefault(pmid, record)

    # XML is the most structured local source, followed by metadata embedded
    # in exact BioC full-text artifacts.  Neither route derives identity from
    # filenames; the PMID must occur in the parsed source content.
    html = html_records()
    bioc = bioc_records()
    xml = xml_records()
    pmids = sorted({pmid for values in phase_by_evidence.values() for pmid in values})
    papers: dict[str, dict[str, str]] = {}
    for pmid in pmids:
        record = dict(metadata_by_pmid.get(pmid, {}))
        record.update({key: value for key, value in identity_by_pmid.get(pmid, {}).items() if value})
        record.update({key: value for key, value in html.get(pmid, {}).items() if value})
        record.update({key: value for key, value in bioc.get(pmid, {}).items() if value})
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
        "CREATE TEMP TABLE m2024_paper_source_pairs (register_evidence_id TEXT NOT NULL, pmid TEXT NOT NULL, PRIMARY KEY (register_evidence_id, pmid));",
        "",
    ]
    if source_rows:
        pairs = sorted({(row["b_evidence_id"], pmid) for row, pmid in source_rows})
        lines.extend([
            "INSERT INTO m2024_paper_source_pairs (register_evidence_id, pmid) VALUES",
            ",\n".join(f"  ({sql(evidence_id)}, {sql(pmid)})" for evidence_id, pmid in pairs) + ";",
            "",
            "-- Remove only stale paper-anchored provenance from prior resolver runs.",
            "DELETE FROM SignalingEdgeSource s",
            "WHERE s.notes LIKE '%\"materialization_status\": \"paper_anchored_register_provenance\"%'",
            "  AND NOT EXISTS (",
            "    SELECT 1 FROM m2024_paper_source_pairs keep",
            "    WHERE keep.register_evidence_id=substring(s.notes FROM '\"module20_24_register_evidence_id\": \"([^\"]+)\"')",
            "      AND keep.pmid=substring(s.notes FROM '\"paper_anchor\": \"PMID:([0-9]+)\"')",
            "  );",
            "",
        ])
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
            "canonicalization_batch": "module20_24_paper_provenance",
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
        f"- Identity metadata conflicts retained unresolved: {len(identity_conflicts):,}",
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
