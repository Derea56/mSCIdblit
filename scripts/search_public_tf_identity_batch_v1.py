#!/usr/bin/env python3
"""Run bounded PubMed discovery for the identity-staging pilot pair leads.

Search results and abstracts are discovery artifacts only. Exact-pair primary
literature still requires human/full-text adjudication before Module 22B
promotion. The script is resumable through per-query JSON cache files.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LEADS = ROOT / "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/identity_batches/batch_001/tflink_pair_search_leads.tsv"
DEFAULT_OUTPUT = ROOT / "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/identity_batches/batch_001/pubmed_search_v1"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
USER_AGENT = "mSCIdblit-public-tf-identity-pilot/1.0"

NON_PRIMARY = {
    "review", "meta-analysis", "systematic review", "editorial", "comment",
    "letter", "news", "guideline", "practice guideline",
    "consensus development conference",
}
DIRECT_TERMS = re.compile(
    r"\b(regulat\w*|transcri\w*|promot\w*|repress\w*|activat\w*|"
    r"inhibit\w*|suppress\w*|induc\w*|bind\w*|promoter|enhancer|"
    r"chip[- ]?seq|chromatin immunoprecipitation|luciferase|reporter|"
    r"knock(?:down|out)|overexpress\w*|silenc\w*|deplet\w*)\b", re.I
)
EXPERIMENT_TERMS = re.compile(
    r"\b(promoter|enhancer|luciferase|reporter|chip|chromatin|knockdown|"
    r"knockout|overexpress\w*|silenc\w*|siRNA|shRNA|CRISPR|deplet\w*|"
    r"transfect\w*|mutat\w*|deletion|binding site)\b", re.I
)

SEARCH_FIELDS = [
    "batch_rank", "tf_key", "tf_symbol", "species", "target_symbol",
    "tflink_target_count", "lead_rank_within_tf", "query_variant", "query",
    "pubmed_hit_count", "candidate_pmids", "source_registry", "source_version",
    "source_snapshot", "lead_status", "limitations",
]
HIT_FIELDS = [
    "batch_rank", "tf_key", "tf_symbol", "species", "target_symbol", "pmid",
    "search_rank", "query_variant", "title", "abstract", "journal", "year",
    "publication_types", "exact_tf", "exact_target", "primary_article",
    "direct_terms", "experiment_terms", "score", "source_snapshot",
]
SUMMARY_FIELDS = [
    "batch_rank", "tf_key", "tf_symbol", "species", "target_symbol",
    "tflink_target_count", "lead_rank_within_tf", "pubmed_hit_count",
    "primary_candidate_count", "direct_experiment_candidate_count", "best_pmid",
    "best_score", "suggested_action", "query_variant", "source_snapshot",
    "limitations",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


def normalized(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip().casefold()


def organism_term(species: str) -> str:
    return "Homo sapiens[Organism]" if species.casefold() == "human" else "Mus musculus[Organism]"


def exact_token(value: str, text: str) -> bool:
    value = normalized(value)
    text = normalized(text)
    if not value or not text:
        return False
    return bool(re.search(r"(?<![a-z0-9])" + re.escape(value) + r"(?![a-z0-9])", text, re.I))


def primary_article(publication_types: str) -> bool:
    types = {normalized(item) for item in publication_types.split(";") if item.strip()}
    return not types.intersection(NON_PRIMARY)


def build_query(row: dict[str, str], with_organism: bool) -> str:
    tf = row["tf_symbol"]
    target = row["target_symbol"]
    regulation = "(regulat*[Title/Abstract] OR transcri*[Title/Abstract] OR promoter[Title/Abstract] OR binding[Title/Abstract] OR expression[Title/Abstract])"
    terms = [f'"{tf}"[Title/Abstract]', f'"{target}"[Title/Abstract]', regulation]
    if with_organism:
        terms.append(organism_term(row["species"]))
    return " AND ".join(terms)


def request_json(endpoint: str, params: dict[str, str], retries: int = 5) -> dict:
    query = dict(params)
    query.update({"tool": "mSCIdblit_public_tf_identity_pilot", "email": "research@example.org"})
    url = f"{EUTILS}/{endpoint}?{urllib.parse.urlencode(query)}"
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                return json.loads(response.read().decode("utf-8"))
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
            if attempt == retries - 1:
                raise
            time.sleep(min(30.0, 2.0 ** attempt))
    raise RuntimeError("unreachable")


def request_xml(endpoint: str, params: dict[str, str], retries: int = 5) -> bytes:
    query = dict(params)
    query.update({"tool": "mSCIdblit_public_tf_identity_pilot", "email": "research@example.org"})
    url = f"{EUTILS}/{endpoint}?{urllib.parse.urlencode(query)}"
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                return response.read()
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
            if attempt == retries - 1:
                raise
            time.sleep(min(30.0, 2.0 ** attempt))
    raise RuntimeError("unreachable")


def node_text(node: ET.Element | None) -> str:
    return "" if node is None else "".join(node.itertext()).strip()


def parse_articles(raw: bytes) -> dict[str, dict[str, str]]:
    root = ET.fromstring(raw)
    articles: dict[str, dict[str, str]] = {}
    for article in root.findall(".//PubmedArticle"):
        pmid = node_text(article.find(".//PMID"))
        if not pmid:
            continue
        title = node_text(article.find(".//ArticleTitle"))
        abstract = " ".join(node_text(node) for node in article.findall(".//Abstract/AbstractText"))
        journal = node_text(article.find(".//Journal/Title"))
        year = node_text(article.find(".//PubDate/Year")) or node_text(article.find(".//PubDate/MedlineDate"))
        publication_types = ";".join(dict.fromkeys(
            node_text(node) for node in article.findall(".//PublicationTypeList/PublicationType") if node_text(node)
        ))
        articles[pmid] = {
            "pmid": pmid, "title": title, "abstract": abstract, "journal": journal,
            "year": year, "publication_types": publication_types,
        }
    return articles


def score_hit(row: dict[str, str], article: dict[str, str]) -> dict[str, str]:
    body = (article.get("title", "") + " " + article.get("abstract", "")).strip()
    tf_match = exact_token(row["tf_symbol"], body)
    target_match = exact_token(row["target_symbol"], body)
    is_primary = primary_article(article.get("publication_types", ""))
    direct = bool(DIRECT_TERMS.search(body))
    experiment = bool(EXPERIMENT_TERMS.search(body))
    score = (4 if tf_match else 0) + (4 if target_match else 0) + (3 if is_primary else 0) + (3 if direct else 0) + (2 if experiment else 0)
    return {
        "batch_rank": row["batch_rank"], "tf_key": row["tf_key"], "tf_symbol": row["tf_symbol"],
        "species": row["species"], "target_symbol": row["target_symbol"], "pmid": article["pmid"],
        "search_rank": row.get("search_rank", ""), "query_variant": row.get("query_variant", ""),
        "title": article.get("title", ""), "abstract": article.get("abstract", ""),
        "journal": article.get("journal", ""), "year": article.get("year", ""),
        "publication_types": article.get("publication_types", ""), "exact_tf": str(tf_match).lower(),
        "exact_target": str(target_match).lower(), "primary_article": str(is_primary).lower(),
        "direct_terms": str(direct).lower(), "experiment_terms": str(experiment).lower(),
        "score": str(score), "source_snapshot": row.get("source_snapshot", ""),
    }


def cache_key(row: dict[str, str]) -> str:
    raw = "|".join(row[field] for field in ("batch_rank", "species", "tf_key", "target_symbol"))
    return hashlib.sha256(raw.encode()).hexdigest()[:24]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--leads", type=Path, default=DEFAULT_LEADS)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--retmax", type=int, default=10)
    parser.add_argument("--request-interval", type=float, default=0.4)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    cache_dir = args.output_dir / "esearch_cache"
    cache_dir.mkdir(parents=True, exist_ok=True)

    leads = read_tsv(args.leads)
    search_rows: list[dict[str, str]] = []
    all_pmids: set[str] = set()
    for index, row in enumerate(leads, start=1):
        cache_path = cache_dir / f"{cache_key(row)}.json"
        cached_result = json.loads(cache_path.read_text(encoding="utf-8")) if cache_path.exists() else None
        if cached_result is not None and not cached_result.get("error"):
            result = cached_result
        else:
            query_variant = "species_restricted"
            query = build_query(row, True)
            try:
                result = request_json("esearch.fcgi", {"db": "pubmed", "term": query, "retmode": "json", "retmax": str(args.retmax)})
            except Exception as exc:
                result = {"error": repr(exc), "query": query, "query_variant": query_variant, "ids": []}
            ids = result.get("esearchresult", {}).get("idlist", []) if isinstance(result, dict) else []
            if not ids and not result.get("error"):
                query_variant = "species_unrestricted_fallback"
                query = build_query(row, False)
                try:
                    result = request_json("esearch.fcgi", {"db": "pubmed", "term": query, "retmode": "json", "retmax": str(args.retmax)})
                except Exception as exc:
                    result = {"error": repr(exc), "query": query, "query_variant": query_variant, "ids": []}
            result = {
                "query": query, "query_variant": query_variant,
                "ids": result.get("esearchresult", {}).get("idlist", []) if isinstance(result, dict) else [],
                "count": result.get("esearchresult", {}).get("count", "0") if isinstance(result, dict) else "0",
                "error": result.get("error", "") if isinstance(result, dict) else "",
            }
            cache_path.write_text(json.dumps(result, sort_keys=True) + "\n", encoding="utf-8")
            time.sleep(args.request_interval)
        ids = [str(item) for item in result.get("ids", [])]
        all_pmids.update(ids)
        search_rows.append({
            **{field: row.get(field, "") for field in ("batch_rank", "tf_key", "tf_symbol", "species", "target_symbol", "tflink_target_count", "lead_rank_within_tf", "source_registry", "source_version", "source_snapshot", "lead_status", "limitations")},
            "query_variant": result.get("query_variant", ""), "query": result.get("query", ""),
            "pubmed_hit_count": str(result.get("count", "0")),
            "candidate_pmids": ";".join(ids),
        })
        if index % 25 == 0:
            print(json.dumps({"processed_leads": index, "total_leads": len(leads), "unique_pmids": len(all_pmids)}), flush=True)

    articles: dict[str, dict[str, str]] = {}
    pmid_list = sorted(all_pmids, key=lambda item: int(item) if item.isdigit() else 0)
    for start in range(0, len(pmid_list), 150):
        group = pmid_list[start:start + 150]
        if not group:
            continue
        try:
            raw = request_xml("efetch.fcgi", {"db": "pubmed", "id": ",".join(group), "rettype": "abstract", "retmode": "xml"})
            articles.update(parse_articles(raw))
        except Exception as exc:
            print(json.dumps({"efetch_error": repr(exc), "group_start": start}), flush=True)
        time.sleep(args.request_interval)

    hit_rows: list[dict[str, str]] = []
    summaries: list[dict[str, str]] = []
    for row in search_rows:
        ids = [item for item in row["candidate_pmids"].split(";") if item]
        scored = []
        for rank, pmid in enumerate(ids, start=1):
            article = articles.get(pmid)
            if article is None:
                continue
            copied = dict(row)
            copied["search_rank"] = str(rank)
            scored.append(score_hit(copied, article))
        hit_rows.extend(scored)
        primary = [item for item in scored if item["primary_article"] == "true" and item["exact_tf"] == "true" and item["exact_target"] == "true"]
        direct = [item for item in primary if item["direct_terms"] == "true" and item["experiment_terms"] == "true"]
        best = max(scored, key=lambda item: int(item["score"]), default=None)
        if direct:
            action = "fulltext_exact_pair_review"
        elif primary:
            action = "abstract_review_then_fulltext"
        elif scored:
            action = "screen_search_hits"
        else:
            action = "no_retrieved_abstract_candidate"
        summaries.append({
            "batch_rank": row["batch_rank"], "tf_key": row["tf_key"], "tf_symbol": row["tf_symbol"],
            "species": row["species"], "target_symbol": row["target_symbol"],
            "tflink_target_count": row["tflink_target_count"], "lead_rank_within_tf": row["lead_rank_within_tf"],
            "pubmed_hit_count": row["pubmed_hit_count"], "primary_candidate_count": str(len(primary)),
            "direct_experiment_candidate_count": str(len(direct)), "best_pmid": best["pmid"] if best else "",
            "best_score": best["score"] if best else "", "suggested_action": action,
            "query_variant": row["query_variant"], "source_snapshot": row["source_snapshot"],
            "limitations": "Abstract-level discovery only; database/GMT membership is not treated as evidence.",
        })

    write_tsv(args.output_dir / "pair_search_results.tsv", SEARCH_FIELDS, search_rows)
    write_tsv(args.output_dir / "pubmed_candidate_hits.tsv", HIT_FIELDS, hit_rows)
    write_tsv(args.output_dir / "pair_evidence_search_summary.tsv", SUMMARY_FIELDS, summaries)
    manifest = {
        "status": "abstract_discovery_only",
        "input_leads": len(leads),
        "search_rows": len(search_rows),
        "unique_pmids": len(all_pmids),
        "fetched_article_records": len(articles),
        "primary_exact_pair_candidates": sum(int(row["primary_candidate_count"]) > 0 for row in summaries),
        "direct_experiment_candidates": sum(int(row["direct_experiment_candidate_count"]) > 0 for row in summaries),
        "suggested_action_counts": dict(sorted(Counter(row["suggested_action"] for row in summaries).items())),
        "canonical_write_performed": False,
        "module_evidence_promotions_performed": False,
        "outputs": ["pair_search_results.tsv", "pubmed_candidate_hits.tsv", "pair_evidence_search_summary.tsv"],
        "limitations": [
            "Search hits are discovery candidates, not verified evidence.",
            "Exact TF/target text matching is abstract-level and does not resolve aliases or complexes.",
            "Species-restricted search is attempted first; unrestricted fallback is labeled.",
        ],
    }
    (args.output_dir / "search_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
