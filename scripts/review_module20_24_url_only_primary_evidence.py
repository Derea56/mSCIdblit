#!/usr/bin/env python3
"""Audit URL-only anchors against stable primary citations already on the edge."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qs, urlparse


ROOT = Path(__file__).resolve().parents[1]
META = ROOT / "work/cross_module_synthesis/module20_24_canonical_paper_metadata.tsv"
QUERY_AUDIT = ROOT / "work/cross_module_synthesis/module20_24_query_url_search_audit.tsv"
CANDIDATE_AUDIT = ROOT / "work/cross_module_synthesis/module20_24_query_candidate_triage.tsv"
OUT_TSV = ROOT / "work/cross_module_synthesis/module20_24_url_only_primary_evidence_review.tsv"
OUT_MD = ROOT / "work/cross_module_synthesis/module20_24_url_only_primary_evidence_review.md"

EVIDENCE_FILES = [
    ROOT / "work/module_b_consolidation/module20b/module20b_evidence_register.tsv",
    ROOT / "work/module_b_consolidation/module21b/module21b_evidence_register.tsv",
    ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv",
    ROOT / "work/module_b_consolidation/module23b/module23b_evidence_register.tsv",
    ROOT / "work/module_b_consolidation/module24b/module24b_evidence_register.tsv",
]

FIELDS = [
    "review_id", "source_key", "evidence_ids", "url_class", "query",
    "search_boundary", "stable_source_locators", "primary_research_locators",
    "supplemental_primary_locators", "primary_research_titles", "primary_anchor_count",
    "decision", "reason",
]

NON_PRIMARY_TYPES = {
    "Review", "Meta-Analysis", "Systematic Review", "Editorial", "Comment",
    "Letter", "News", "Practice Guideline", "Guideline", "Consensus Development Conference",
}

# Bounded broad-search repair for the one query whose attached source was only
# a review. The paper is primary research but remains an audit candidate here
# because its CAGA reporter is a pathway/TF readout, not an endogenous target
# gene or a complete ligand-to-TF claim.
SUPPLEMENTAL_PRIMARY_BY_QUERY = {
    "Gdf9 Bmpr2_Tgfbr1 terminal TF transcription factor target gene promoter": {
        "locators": "PMID:14684852;DOI:10.1210/me.2003-0393",
        "title": "Growth differentiation factor-9 signaling is mediated by the type I receptor, activin receptor-like kinase 5",
    },
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def source_key_for_token(token: str) -> str:
    token = token.strip()
    if token.startswith("PMID:"):
        return token.upper()
    if token.startswith("PMCID:"):
        return token.upper()
    if token.startswith("DOI:"):
        return token.upper()
    return token


def url_class(url: str) -> str:
    parsed = urlparse(url.removeprefix("URL:"))
    if parsed.netloc == "pubmed.ncbi.nlm.nih.gov" and parse_qs(parsed.query).get("term"):
        return "pubmed_query"
    if parsed.netloc == "reactome.org":
        return "reactome_pathway"
    if parsed.netloc == "www.sciencedirect.com":
        return "publisher_article"
    return "other_url"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--pubmed-summary-json",
        type=Path,
        default=Path("/private/tmp/module20_24_url_only_pmid_summaries.json"),
        help="NCBI esummary JSON cache for PMIDs associated with URL-only cases.",
    )
    args = parser.parse_args()

    metadata = read_tsv(META)
    url_rows = [row for row in metadata if row["metadata_status"] == "url_only_noncanonical"]
    metadata_by_key = {row["canonical_paper_key"].upper(): row for row in metadata}
    metadata_by_identifier: dict[str, dict[str, str]] = {}
    for row in metadata:
        for field, prefix in (("pmid", "PMID:"), ("pmcid", "PMCID:"), ("doi", "DOI:")):
            if row.get(field):
                metadata_by_identifier[prefix + row[field].upper()] = row

    evidence_by_id: dict[str, dict[str, str]] = {}
    for path in EVIDENCE_FILES:
        if not path.exists():
            continue
        for row in read_tsv(path):
            evidence_id = row.get("b_evidence_id") or row.get("evidence_id") or row.get("evidence_id_stable")
            if evidence_id:
                evidence_by_id[evidence_id] = row

    query_audit = {row["source_key"]: row for row in read_tsv(QUERY_AUDIT)}
    candidate_audit = {row["source_key"]: row for row in read_tsv(CANDIDATE_AUDIT)}
    summaries: dict[str, dict] = {}
    if args.pubmed_summary_json.exists():
        payload = json.loads(args.pubmed_summary_json.read_text())
        result = payload.get("result", {})
        summaries = {str(pmid): result[pmid] for pmid in result.get("uids", []) if pmid in result}

    review_rows: list[dict[str, str]] = []
    for index, row in enumerate(url_rows, start=1):
        source_key = row["canonical_paper_key"]
        url = row["source_metadata_url"]
        url_kind = url_class(url)
        query = parse_qs(urlparse(url.removeprefix("URL:")).query).get("term", [""])[0]
        q_audit = query_audit.get(source_key, {})
        candidate = candidate_audit.get(source_key, {})
        search_boundary = q_audit.get("status", "non_query_manual_review")
        if candidate.get("triage_status"):
            search_boundary += ";" + candidate["triage_status"]

        stable_tokens: list[str] = []
        for evidence_id in row["evidence_ids"].split(";"):
            evidence = evidence_by_id.get(evidence_id, {})
            for token in evidence.get("source_locator", "").split(";"):
                token = token.strip()
                if token.startswith(("PMID:", "PMCID:", "DOI:")):
                    normalized = source_key_for_token(token)
                    if normalized not in stable_tokens:
                        stable_tokens.append(normalized)

        primary_tokens: list[str] = []
        primary_titles: list[str] = []
        for token in stable_tokens:
            metadata_row = metadata_by_key.get(token) or metadata_by_identifier.get(token)
            pmid = ""
            if token.startswith("PMID:"):
                pmid = token.removeprefix("PMID:")
            elif metadata_row and metadata_row.get("pmid"):
                pmid = metadata_row["pmid"]
            summary = summaries.get(pmid, {})
            pubtypes = set(summary.get("pubtype", []))
            is_primary = bool(summary) and not (pubtypes & NON_PRIMARY_TYPES)
            if is_primary:
                primary_tokens.append(token)
                title = summary.get("title") or (metadata_row or {}).get("title", "")
                if title and title not in primary_titles:
                    primary_titles.append(title)

        supplemental = SUPPLEMENTAL_PRIMARY_BY_QUERY.get(query, {}) if not primary_tokens else {}
        supplemental_tokens = [
            token for token in supplemental.get("locators", "").split(";") if token
        ]
        for token in supplemental_tokens:
            if token not in primary_tokens:
                primary_tokens.append(token)
        if supplemental.get("title") and supplemental["title"] not in primary_titles:
            primary_titles.append(supplemental["title"])

        if primary_tokens:
            if supplemental_tokens:
                decision = "reviewed_supplemental_primary_evidence_query_remains_noncanonical"
                reason = "A bounded broader search identified a primary paper for the query, but its reporter/pathway readout does not establish an endogenous target gene or complete ligand-to-TF path. It is recorded as supplemental evidence only."
            elif url_kind == "pubmed_query":
                decision = "reviewed_existing_primary_evidence_query_remains_noncanonical"
                reason = "The query URL is not an exact citation; the associated evidence record already contains stable primary-research anchors. No new edge or directness promotion was made."
            elif url_kind == "reactome_pathway":
                decision = "reviewed_pathway_anchor_with_primary_evidence"
                reason = "Reactome pathway/reaction context is retained as a pathway anchor; associated primary papers remain the evidence basis. No pathway-to-TF directness was inferred."
            else:
                decision = "reviewed_publisher_url_with_primary_evidence"
                reason = "The publisher URL is retained as a noncanonical locator; associated stable primary evidence was identified and the existing evidence layer was preserved."
        elif stable_tokens:
            decision = "reviewed_existing_stable_nonprimary_or_unclassified_evidence"
            reason = "Stable citations are present, but the cached PubMed records did not establish a primary-research anchor under the conservative publication-type filter."
        else:
            decision = "no_stable_primary_anchor_found"
            reason = "No stable PMID, PMCID, or DOI was available on the associated evidence record after bounded review."

        review_rows.append({
            "review_id": f"URL-REVIEW-{index:03d}",
            "source_key": source_key,
            "evidence_ids": row["evidence_ids"],
            "url_class": url_kind,
            "query": query,
            "search_boundary": search_boundary,
            "stable_source_locators": ";".join(stable_tokens),
            "primary_research_locators": ";".join(primary_tokens),
            "supplemental_primary_locators": ";".join(supplemental_tokens),
            "primary_research_titles": " || ".join(primary_titles[:4]),
            "primary_anchor_count": str(len(primary_tokens)),
            "decision": decision,
            "reason": reason,
        })

    with OUT_TSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(review_rows)

    counts = Counter(row["decision"] for row in review_rows)
    class_counts = Counter(row["url_class"] for row in review_rows)
    total_primary = sum(bool(row["primary_research_locators"]) for row in review_rows)
    supplemental_count = sum(bool(row["supplemental_primary_locators"]) for row in review_rows)
    OUT_MD.write_text(
        "# Module 20B–24B URL-Only Primary-Evidence Review\n\n"
        f"- URL-only anchors reviewed: {len(review_rows):,}\n"
        f"- URL classes: {dict(sorted(class_counts.items()))}\n"
        f"- URLs with at least one associated primary-research anchor: {total_primary:,}\n"
        f"- URLs with supplemental primary-paper candidates from broader search: {supplemental_count:,}\n"
        + "\n".join(f"- `{key}`: {value:,}" for key, value in sorted(counts.items()))
        + "\n\n"
        "The URL locators were not promoted as papers. Stable PMID/PMCID/DOI citations already attached to the corresponding evidence records were checked for primary-research publication types. Existing direct, pathway, and functional evidence layers were preserved; no direct molecular interaction or terminal TF endpoint was inferred from a search URL or pathway anchor. Query hits remain bounded by the existing PubMed search audit, and unresolved/no-hit queries remain explicit.\n"
    )
    print(f"reviewed={len(review_rows)} primary_anchor_urls={total_primary}")
    print(dict(sorted(counts.items())))


if __name__ == "__main__":
    main()
