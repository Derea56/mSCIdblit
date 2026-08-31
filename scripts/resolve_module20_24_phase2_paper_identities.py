#!/usr/bin/env python3
"""Resolve Phase-2 extraction paper identities from exact local evidence.

The Phase-2 packet preserves a ``canonical_paper_key`` and a richer
``source_locator``.  Some rows use a PMCID or DOI in the key while the PMID
needed by the existing materializers is present only in the locator or in the
local source artifact.  This script makes that relationship explicit on a
per-extraction basis.

Only identifiers explicitly present in one of the following are accepted:

* the Phase-2 canonical key;
* a matching row in the existing paper-metadata ledger;
* an explicit identifier in the Phase-2 source locator;
* an identifier-bearing local XML, HTML, JSON, or TSV artifact whose
  identifier matches the canonical key.

Filename tokens and search-query URLs are never treated as paper identity.
Unresolved and ambiguous cases remain unresolved.  This is an audit manifest;
it does not write to the database or change the Phase-2 grading fields.

The derived resolved_canonical_paper_key is populated only when an
accepted resolution produced one PMID, using the explicit form PMID:<id>.
The original canonical_paper_key is never overwritten.  A lossless
row-level exception queue and a deduplicated triage summary are emitted for
rows without a resolved PMID.
"""

from __future__ import annotations

import csv
import html
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
REVIEW_ROOT = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review"
PHASE2 = REVIEW_ROOT / "module20_24_integrated_phase2_extractions.tsv"
METADATA = ROOT / "work" / "cross_module_synthesis" / "module20_24_canonical_paper_metadata.tsv"
OUT = REVIEW_ROOT / "module20_24_phase2_paper_identity_resolution.tsv"
REPORT = REVIEW_ROOT / "module20_24_phase2_paper_identity_resolution.md"
EXCEPTIONS_OUT = REVIEW_ROOT / "module20_24_phase2_paper_identity_exceptions.tsv"
EXCEPTIONS_SUMMARY_OUT = REVIEW_ROOT / "module20_24_phase2_paper_identity_exceptions_summary.tsv"

FIELDS = [
    "extraction_id", "module", "b_evidence_id", "canonical_paper_key",
    "source_locator", "resolved_canonical_paper_key",
    "resolved_pmid", "resolved_pmcid", "resolved_doi",
    "identity_resolution_status", "resolution_basis", "authoritative_source",
    "source_metadata_title", "source_metadata_authors", "source_metadata_year",
    "source_metadata_journal", "source_metadata_abstract", "source_metadata_url",
    "unresolved_reason",
]

EXCEPTION_FIELDS = [
    "extraction_id", "module", "b_evidence_id", "canonical_paper_key",
    "source_locator", "identity_resolution_status", "unresolved_reason",
    "authoritative_source",
]

EXCEPTION_SUMMARY_FIELDS = [
    "module", "canonical_paper_key", "identity_resolution_status",
    "unresolved_reason", "extraction_row_count", "source_locator_count",
    "extraction_ids",
]

ID_RE = re.compile(
    r"(?i)\bPMID\s*:\s*(?P<pmid>\d+)\b|"
    r"\bPMCID\s*:\s*(?P<pmcid>PMC\d+)\b|"
    r"\bDOI\s*:\s*(?P<doi>10\.\S+?)(?=;|\s|$)"
)
URL_RE = re.compile(r"https?://[^;\s]+", re.IGNORECASE)


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def normalize_doi(value: str) -> str:
    return value.strip().removeprefix("DOI:").rstrip(".,)").lower()


def identifier_tokens(value: str) -> set[tuple[str, str]]:
    tokens: set[tuple[str, str]] = set()
    for match in ID_RE.finditer(value or ""):
        if match.group("pmid"):
            tokens.add(("PMID", match.group("pmid")))
        elif match.group("pmcid"):
            tokens.add(("PMCID", match.group("pmcid").upper()))
        elif match.group("doi"):
            tokens.add(("DOI", normalize_doi(match.group("doi"))))
    return tokens


def stable_url_tokens(value: str) -> set[tuple[str, str]]:
    tokens: set[tuple[str, str]] = set()
    for url in URL_RE.findall(value or ""):
        clean = html.unescape(url).rstrip(".,)")
        lowered = clean.lower()
        pmid_match = re.search(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)(?:/|$)", lowered)
        if pmid_match:
            tokens.add(("PMID", pmid_match.group(1)))
        pmcid_match = re.search(r"pmc\.ncbi\.nlm\.nih\.gov/articles/(PMC\d+)", clean, re.I)
        if pmcid_match:
            tokens.add(("PMCID", pmcid_match.group(1).upper()))
        doi_match = re.search(r"doi\.org/(10\.\S+)$", clean, re.I)
        if doi_match:
            tokens.add(("DOI", normalize_doi(doi_match.group(1))))
    return tokens


def all_tokens(value: str) -> set[tuple[str, str]]:
    return identifier_tokens(value) | stable_url_tokens(value)


def text(node: ET.Element | None) -> str:
    if node is None:
        return ""
    return " ".join(part.strip() for part in node.itertext() if part.strip())


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def descendants(node: ET.Element, name: str) -> list[ET.Element]:
    wanted = name.lower()
    return [candidate for candidate in node.iter() if local_name(candidate.tag) == wanted]


def direct_child(node: ET.Element | None, name: str) -> ET.Element | None:
    if node is None:
        return None
    wanted = name.lower()
    return next((candidate for candidate in list(node) if local_name(candidate.tag) == wanted), None)


def first_descendant_text(node: ET.Element, names: tuple[str, ...]) -> str:
    wanted = {name.lower() for name in names}
    for candidate in node.iter():
        if local_name(candidate.tag) in wanted:
            value = text(candidate)
            if value:
                return value
    return ""


def article_record(node: ET.Element, source_file: str) -> dict[str, object]:
    tokens: set[tuple[str, str]] = set()
    is_pubmed = local_name(node.tag) == "pubmedarticle"
    if is_pubmed:
        medline = direct_child(node, "MedlineCitation")
        article_node = direct_child(medline, "Article")
        pubmed_data = direct_child(node, "PubmedData")
        id_list = direct_child(pubmed_data, "ArticleIdList")
        pmid_node = direct_child(medline, "PMID")
        if pmid_node is not None and text(pmid_node).isdigit():
            tokens.add(("PMID", text(pmid_node)))
        identifier_nodes = list(id_list) if id_list is not None else []
    else:
        article = direct_child(node, "article")
        if article is None:
            article = node
        meta_nodes = descendants(article, "article-meta")
        article_node = meta_nodes[0] if meta_nodes else article
        id_list = article_node
        identifier_nodes = [candidate for candidate in list(article_node) if local_name(candidate.tag) == "article-id"]

    target_node = article_node if article_node is not None else node
    # Search the article-title element before generic title elements. In
    # PubMed XML the Journal/Title element commonly precedes ArticleTitle;
    # accepting the first generic ``title`` would mislabel the journal as the
    # paper title and create false PMID/title conflicts.
    title = first_descendant_text(target_node, ("ArticleTitle", "article-title"))
    if not title and not is_pubmed:
        title = first_descendant_text(target_node, ("title",))
    authors: list[str] = []
    author_parent = direct_child(article_node, "AuthorList") if is_pubmed else direct_child(article_node, "contrib-group")
    author_nodes = list(author_parent) if author_parent is not None else []
    for author in author_nodes:
        family = first_descendant_text(author, ("LastName", "surname"))
        given = first_descendant_text(author, ("ForeName", "given-names"))
        collective = first_descendant_text(author, ("CollectiveName", "collab"))
        name = " ".join(part for part in (given, family) if part) or collective
        if name and name not in authors:
            authors.append(name)
    for element in identifier_nodes:
        tag = local_name(element.tag)
        value = text(element)
        id_type = (element.attrib.get("IdType") or element.attrib.get("pub-id-type") or "").lower()
        if tag in {"articleid", "article-id"} and id_type in {"pubmed", "pmid"} and value.isdigit():
            tokens.add(("PMID", value))
        elif tag in {"articleid", "article-id"} and id_type in {"pmc", "pmcid"} and value.upper().startswith("PMC"):
            tokens.add(("PMCID", value.upper()))
        elif tag in {"articleid", "article-id"} and id_type == "doi" and value:
            tokens.add(("DOI", normalize_doi(value)))
    year = ""
    for candidate in descendants(target_node, "year"):
        value = text(candidate)
        if re.fullmatch(r"(?:18|19|20)\d{2}", value):
            year = value
            break
    if is_pubmed:
        journal_node = direct_child(article_node, "Journal")
        journal = first_descendant_text(journal_node, ("Title",))
    else:
        journal = first_descendant_text(target_node, ("journal-title",))
    abstract_nodes = descendants(target_node, "Abstract") + descendants(target_node, "abstract-text")
    abstract = " ".join(text(candidate) for candidate in abstract_nodes)
    pmid = next((value for kind, value in sorted(tokens) if kind == "PMID"), "")
    pmcid = next((value for kind, value in sorted(tokens) if kind == "PMCID"), "")
    doi = next((value for kind, value in sorted(tokens) if kind == "DOI"), "")
    return {
        "tokens": tokens,
        "pmid": pmid,
        "pmcid": pmcid,
        "doi": doi,
        "title": title,
        "authors": "; ".join(authors),
        "year": year,
        "journal": journal,
        "abstract": abstract,
        "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else "",
        "source_file": source_file,
    }


def html_record(raw: str, source_file: str) -> dict[str, object]:
    values: dict[str, list[str]] = defaultdict(list)
    for match in re.finditer(
        r"<meta\b[^>]*?\bname=[\"']([^\"']+)[\"'][^>]*?\bcontent=[\"']([^\"']*)[\"'][^>]*>",
        raw,
        re.IGNORECASE,
    ):
        values[match.group(1).lower()].append(html.unescape(match.group(2)).strip())
    tokens: set[tuple[str, str]] = set()
    for value in values.get("citation_pmid", []):
        if value.isdigit():
            tokens.add(("PMID", value))
    for value in values.get("citation_pmcid", []):
        if value.upper().startswith("PMC"):
            tokens.add(("PMCID", value.upper()))
    for value in values.get("citation_doi", []):
        if value:
            tokens.add(("DOI", normalize_doi(value)))
    title = (values.get("citation_title") or [""])[0]
    authors = "; ".join(dict.fromkeys(values.get("citation_author", [])))
    year = ""
    for value in values.get("citation_publication_date", []) + values.get("citation_date", []):
        match = re.search(r"(?:18|19|20)\d{2}", value)
        if match:
            year = match.group(0)
            break
    pmid = next((value for kind, value in sorted(tokens) if kind == "PMID"), "")
    pmcid = next((value for kind, value in sorted(tokens) if kind == "PMCID"), "")
    doi = next((value for kind, value in sorted(tokens) if kind == "DOI"), "")
    canonical = next((value for value in values.get("citation_fulltext_html_url", []) if value), "")
    return {
        "tokens": tokens,
        "pmid": pmid,
        "pmcid": pmcid,
        "doi": doi,
        "title": title,
        "authors": authors,
        "year": year,
        "journal": (values.get("citation_journal_title") or [""])[0],
        "abstract": "",
        "url": canonical,
        "source_file": source_file,
    }


def text_record(raw: str, source_file: str) -> dict[str, object]:
    tokens = identifier_tokens(raw)
    pmid = next((value for kind, value in sorted(tokens) if kind == "PMID"), "")
    pmcid = next((value for kind, value in sorted(tokens) if kind == "PMCID"), "")
    doi = next((value for kind, value in sorted(tokens) if kind == "DOI"), "")
    return {
        "tokens": tokens,
        "pmid": pmid,
        "pmcid": pmcid,
        "doi": doi,
        "title": "",
        "authors": "",
        "year": "",
        "journal": "",
        "abstract": "",
        "url": "",
        "source_file": source_file,
    }


def artifact_paths(value: str) -> list[Path]:
    paths: list[Path] = []
    candidates = re.findall(r"/Users/derea/Documents/SCI/mSCIdblit/[^;]+|(?:data|work)/[^;]+", value or "")
    for candidate in candidates:
        clean = candidate.strip().rstrip(".,)")
        if " " in clean and not clean.endswith((".json", ".xml", ".html", ".htm", ".tsv", ".txt")):
            clean = clean.split(" ", 1)[0]
        path = Path(clean)
        if not path.is_absolute():
            path = ROOT / path
        if path.exists() and path.is_file() and path not in paths:
            paths.append(path)
    return paths


def parse_artifact(path: Path) -> list[dict[str, object]]:
    relative = str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)
    suffix = path.suffix.lower()
    if suffix in {".xml", ".xhtml"}:
        try:
            root = ET.parse(path).getroot()
        except (ET.ParseError, OSError):
            return []
        articles = descendants(root, "PubmedArticle")
        if articles:
            return [article_record(article, relative) for article in articles]
        return [article_record(root, relative)]
    try:
        raw = path.read_text(errors="replace")
    except OSError:
        return []
    if suffix in {".html", ".htm"}:
        return [html_record(raw, relative)]
    return [text_record(raw, relative)]


def metadata_record(row: dict[str, str]) -> dict[str, object]:
    return {
        "tokens": all_tokens("; ".join(row.get(field, "") for field in ("canonical_paper_key", "pmid", "pmcid", "doi"))),
        "pmid": row.get("pmid", ""),
        "pmcid": row.get("pmcid", ""),
        "doi": normalize_doi(row.get("doi", "")) if row.get("doi") else "",
        "title": row.get("title", ""),
        "authors": row.get("authors", ""),
        "year": row.get("publication_year", ""),
        "journal": row.get("journal", ""),
        "abstract": "",
        "url": row.get("source_metadata_url", ""),
        "source_file": str(METADATA.relative_to(ROOT)),
    }


def output_row(row: dict[str, str]) -> dict[str, str]:
    return {field: row.get(field, "") for field in FIELDS}


def fill_from_record(result: dict[str, str], record: dict[str, object]) -> None:
    result["resolved_pmid"] = str(record.get("pmid", ""))
    result["resolved_pmcid"] = str(record.get("pmcid", ""))
    result["resolved_doi"] = str(record.get("doi", ""))
    result["source_metadata_title"] = str(record.get("title", ""))
    result["source_metadata_authors"] = str(record.get("authors", ""))
    result["source_metadata_year"] = str(record.get("year", ""))
    result["source_metadata_journal"] = str(record.get("journal", ""))
    result["source_metadata_abstract"] = str(record.get("abstract", ""))
    result["source_metadata_url"] = str(record.get("url", ""))


def set_derived_canonical_key(result: dict[str, str]) -> None:
    """Set the derived key only from an accepted, single resolved PMID."""
    pmid = result.get("resolved_pmid", "").strip()
    result["resolved_canonical_paper_key"] = f"PMID:{pmid}" if pmid else ""


def exception_summary(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    grouped: dict[tuple[str, str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        key = (
            row["module"],
            row["canonical_paper_key"],
            row["identity_resolution_status"],
            row["unresolved_reason"],
        )
        grouped[key].append(row)
    summary = []
    for key, group in sorted(grouped.items()):
        source_locators = sorted({row["source_locator"] for row in group if row["source_locator"]})
        summary.append({
            "module": key[0],
            "canonical_paper_key": key[1],
            "identity_resolution_status": key[2],
            "unresolved_reason": key[3],
            "extraction_row_count": str(len(group)),
            "source_locator_count": str(len(source_locators)),
            "extraction_ids": ";".join(sorted(row["extraction_id"] for row in group)),
        })
    return summary


def write_tsv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fieldnames,
            delimiter="\t",
            quoting=csv.QUOTE_ALL,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def validate_resolution_rows(rows: list[dict[str, str]], phase2: list[dict[str, str]]) -> None:
    """Fail closed if the manifest loses rows or contradicts its derived key."""
    phase2_ids = [row.get("extraction_id", "") for row in phase2]
    result_ids = [row.get("extraction_id", "") for row in rows]
    if result_ids != phase2_ids:
        raise ValueError("identity manifest extraction IDs/order do not match Phase-2 input")
    if len(result_ids) != len(set(result_ids)):
        raise ValueError("identity manifest contains duplicate extraction IDs")
    for row in rows:
        pmid = row["resolved_pmid"]
        derived = row["resolved_canonical_paper_key"]
        expected = f"PMID:{pmid}" if pmid else ""
        if derived != expected:
            raise ValueError(f"derived canonical key mismatch for {row['extraction_id']}")
        if row["identity_resolution_status"].startswith("unresolved_") and pmid:
            raise ValueError(f"unresolved row has resolved PMID: {row['extraction_id']}")


def main() -> None:
    phase2 = read_tsv(PHASE2)
    metadata = {
        row.get("canonical_paper_key", ""): row
        for row in read_tsv(METADATA)
        if row.get("canonical_paper_key") and row.get("paper_ready") == "true" and row.get("pmid")
    }
    artifact_cache: dict[Path, list[dict[str, object]]] = {}
    rows: list[dict[str, str]] = []
    status_counts = Counter()
    basis_counts = Counter()

    for source in phase2:
        result = output_row({
            "extraction_id": source.get("extraction_id", ""),
            "module": source.get("module", ""),
            "b_evidence_id": source.get("b_evidence_id", ""),
            "canonical_paper_key": source.get("canonical_paper_key", ""),
            "source_locator": source.get("source_locator", ""),
        })
        key = source.get("canonical_paper_key", "")
        key_ids = all_tokens(key)
        non_pmid_key_ids = {item for item in key_ids if item[0] != "PMID"}
        direct_pmids = sorted(value for kind, value in key_ids if kind == "PMID")
        locator = source.get("source_locator", "")
        locator_ids = all_tokens(locator)

        metadata_row = metadata.get(key)
        if metadata_row:
            record = metadata_record(metadata_row)
            fill_from_record(result, record)
            result["identity_resolution_status"] = "resolved_authoritative_metadata_ledger"
            result["resolution_basis"] = "exact canonical_paper_key match in paper_ready metadata ledger"
            result["authoritative_source"] = str(METADATA.relative_to(ROOT))
        else:
            if len(direct_pmids) == 1:
                result["resolved_pmid"] = direct_pmids[0]
                result["identity_resolution_status"] = "resolved_canonical_pmid"
                result["resolution_basis"] = "single explicit PMID in canonical_paper_key"
                result["authoritative_source"] = "canonical_paper_key"
            else:
                artifact_records: list[dict[str, object]] = []
                for path in artifact_paths(locator):
                    artifact_cache.setdefault(path, parse_artifact(path))
                    artifact_records.extend(artifact_cache[path])
                matching_records = []
                if non_pmid_key_ids:
                    matching_records = [
                        record for record in artifact_records
                        if non_pmid_key_ids & set(record.get("tokens", set()))
                    ]
                artifact_pmids = sorted({str(record.get("pmid", "")) for record in matching_records if record.get("pmid")})
                shared_locator_ids = non_pmid_key_ids & {item for item in locator_ids if item[0] != "PMID"}
                locator_pmids = sorted(value for kind, value in locator_ids if kind == "PMID")
                # A key that already lists several PMIDs is ambiguous unless
                # the local artifact/source locator selects one of those exact
                # PMIDs. Never replace the canonical PMID set with a PMID
                # found elsewhere in a multi-record search artifact.
                if direct_pmids:
                    artifact_pmids = sorted(set(artifact_pmids) & set(direct_pmids))
                    locator_pmids = sorted(set(locator_pmids) & set(direct_pmids))
                if len(artifact_pmids) == 1:
                    record = next(record for record in matching_records if str(record.get("pmid", "")) == artifact_pmids[0])
                    fill_from_record(result, record)
                    result["identity_resolution_status"] = "resolved_authoritative_local_artifact"
                    result["resolution_basis"] = "canonical identifier matched the same identifier in local source artifact"
                    result["authoritative_source"] = str(record.get("source_file", ""))
                elif shared_locator_ids and len(locator_pmids) == 1:
                    result["resolved_pmid"] = locator_pmids[0]
                    result["identity_resolution_status"] = "resolved_authoritative_source_locator"
                    result["resolution_basis"] = "canonical identifier and one PMID co-occur explicitly in source_locator"
                    result["authoritative_source"] = "source_locator"
                elif len(direct_pmids) > 1:
                    result["identity_resolution_status"] = "unresolved_ambiguous_multiple_canonical_pmids"
                    result["unresolved_reason"] = "canonical_paper_key contains multiple PMIDs and no exact paper-level disambiguator was established"
                elif non_pmid_key_ids and len(artifact_pmids) > 1:
                    result["identity_resolution_status"] = "unresolved_ambiguous_local_artifact"
                    result["unresolved_reason"] = "matching local artifact contains multiple PMID records"
                elif key in {"", "unknown"}:
                    result["identity_resolution_status"] = "unresolved_missing_canonical_identity"
                    result["unresolved_reason"] = "no explicit canonical PMID, PMCID, DOI, or stable paper URL"
                else:
                    result["identity_resolution_status"] = "unresolved_no_authoritative_resolution"
                    result["unresolved_reason"] = "no exact metadata-ledger, source-locator, or content-level local-artifact resolution"

        if not result["identity_resolution_status"]:
            result["identity_resolution_status"] = "unresolved_no_authoritative_resolution"
            result["unresolved_reason"] = "resolver produced no accepted identity"
        set_derived_canonical_key(result)
        rows.append(result)
        status_counts[result["identity_resolution_status"]] += 1
        basis_counts[result["resolution_basis"] or result["unresolved_reason"]] += 1

    validate_resolution_rows(rows, phase2)

    # Quote every field so rows with intentionally empty trailing fields do
    # not become indistinguishable from whitespace-truncated records.
    write_tsv(OUT, FIELDS, rows)

    resolved = [row for row in rows if row["resolved_pmid"]]
    unresolved = [row for row in rows if not row["resolved_pmid"]]
    exception_rows = [
        {field: row.get(field, "") for field in EXCEPTION_FIELDS}
        for row in unresolved
    ]
    write_tsv(EXCEPTIONS_OUT, EXCEPTION_FIELDS, exception_rows)
    exception_groups = exception_summary(unresolved)
    write_tsv(EXCEPTIONS_SUMMARY_OUT, EXCEPTION_SUMMARY_FIELDS, exception_groups)
    report = [
        "# Module 20B–24B Phase-2 paper identity resolution",
        "",
        "This manifest bridges exact paper identifiers to Phase-2 extraction rows.",
        "It preserves the original canonical_paper_key and does not alter evidence",
        "grades, context levels, claims, observations, or the database schema.",
        "Filename tokens and search-query URLs are not accepted as paper identity.",
        "The derived resolved_canonical_paper_key is PMID:<id> only after an accepted single-PMID resolution; the original canonical_paper_key is preserved.",
        "",
        f"- Phase-2 extraction rows audited: {len(rows):,}",
        f"- Rows with resolved PMID: {len(resolved):,}",
        f"- Rows without resolved PMID: {len(unresolved):,}",
        f"- Row-level unresolved exception queue: {len(exception_rows):,}",
        f"- Deduplicated exception groups: {len(exception_groups):,}",
        f"- Local artifacts parsed (only when cited by a row): {len(artifact_cache):,}",
        "",
        "## Resolution status",
        "",
        "| Status | Rows |",
        "|---|---:|",
    ]
    report.extend(f"| {status} | {count:,} |" for status, count in sorted(status_counts.items()))
    report.extend([
        "",
        "## Unresolved policy",
        "",
        "Rows without a single authoritative resolved PMID remain in the Phase-2 staging ledger.",
        "Ambiguous multiple-PMID keys and local artifacts are not collapsed by guessing.",
        "The original key and unresolved reason are retained for later adjudication.",
        f"The lossless row-level queue is {EXCEPTIONS_OUT.name}; its deduplicated triage index is {EXCEPTIONS_SUMMARY_OUT.name}.",
        "",
    ])
    REPORT.write_text("\n".join(report))
    print(f"rows={len(rows)} resolved_pmid={len(resolved)} unresolved={len(unresolved)} artifacts={len(artifact_cache)}")
    print(dict(sorted(status_counts.items())))


if __name__ == "__main__":
    main()
