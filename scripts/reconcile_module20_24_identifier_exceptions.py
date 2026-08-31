#!/usr/bin/env python3
"""Reconcile DOI and explicit stable-URL exceptions using validated companions."""

from __future__ import annotations

import csv
import json
import time
from pathlib import Path
from urllib.parse import quote, urlparse
from urllib.error import HTTPError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
METADATA = ROOT / "work" / "cross_module_synthesis" / "module20_24_canonical_paper_metadata.tsv"
OUTPUT = ROOT / "work" / "cross_module_synthesis" / "module20_24_canonical_paper_metadata.tsv"
REPORT_TSV = ROOT / "work" / "cross_module_synthesis" / "module20_24_identifier_reconciliation.tsv"
REPORT_MD = ROOT / "work" / "cross_module_synthesis" / "module20_24_identifier_reconciliation.md"

FIELDS = [
    "canonical_paper_key", "canonical_merge_key", "paper_ready", "metadata_status",
    "title", "authors", "publication_year", "journal", "volume", "issue", "pages",
    "doi", "pmid", "pmcid", "source_metadata_url", "evidence_ids", "modules",
    "evidence_layers",
]

# Exact DOI-indexed PubMed matches established by NCBI ESearch/esummary.
DOI_TO_PMID = {
    "10.1038/nature03873": "16094370",
    "10.1038/s41388-018-0297-x": "29769618",
    "10.1093/intimm/dxh299": "16091383",
    "10.1152/ajpcell.00240.2001": "11832328",
    "10.1182/blood-2002-03-0806": "12393736",
    "10.1242/dev.02210": "16368929",
    "10.1359/jbmr.050111": "15883644",
}

# Validated companion anchors where the DOI row is malformed, not indexed by
# PubMed DOI search, or lacks an API metadata response. The input DOI remains
# preserved in the DOI column; only the canonical merge key and metadata basis
# are reconciled.
DOI_TO_COMPANION = {
    "10.1007/s00441-020-03308-0": "PMCID:PMC7960628",
    "10.1016/j.devcell.2009.06.017": "PMCID:PMC2747264",
    "10.1074/jbc.269.51.32226": "PMID:7798222",
    "10.1182/blood.v88.8.3185.bloodjournal8883185": "PMID:8874219",
    # Legacy Structure PII formatting without punctuation in the DOI string.
    "10.1016/s0969212611001353": "PMCID:PMC3279696",
}

PII_COMPANION_DOIS = {"10.1016/s0969212611001353"}

COMPANION_FALLBACK = {
    "PMCID:PMC3279696": {
        "canonical_merge_key": "PMID:21620717",
        "title": "The crystal structure of the alpha-neurexin-1 extracellular region reveals a hinge point for mediating synaptic adhesion and function.",
        "authors": "Miller MT; Mileni M; Comoletti D; Stevens RC; Harel M; Taylor P",
        "publication_year": "2011",
        "journal": "Structure",
        "volume": "19",
        "issue": "6",
        "pages": "767-778",
        "doi": "10.1016/j.str.2011.03.011",
        "pmid": "21620717",
        "pmcid": "PMC3279696",
        "source_metadata_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3279696/",
    },
}

PUBMED_FALLBACK = {
    "16094370": ("Voltage-sensor activation with a tarantula toxin as cargo.", "Phillips LR; Milescu M; Li-Smerin Y; Mindell JA; Kim JI; Swartz KJ", "2005", "Nature", "436", "7052", "857-60"),
    "29769618": ("Inhibitor of apoptosis proteins (IAPs) mediate collagen type XI alpha 1-driven cisplatin resistance in ovarian cancer.", "Rada M; Nallanthighal S; Cha J; Ryan K; Sage J; Eldred C; Ullo M; Orsulic S; Cheon DJ", "2018", "Oncogene", "37", "35", "4809-4820"),
    "16091383": ("Heterotypic interaction of CRTAM with Necl2 induces cell adhesion on activated NK cells and CD8+ T cells.", "Arase N; Takeuchi A; Unno M; Hirano S; Yokosuka T; Arase H; Saito T", "2005", "International immunology", "17", "9", "1227-37"),
    "11832328": ("Vasopressin-mediated mitogenic signaling in intestinal epithelial cells.", "Chiu T; Wu SS; Santiskulvong C; Tangkijvanich P; Yee HF Jr; Rozengurt E", "2002", "American journal of physiology. Cell physiology", "282", "3", "C434-50"),
    "12393736": ("Interaction between von Willebrand factor and glycoprotein Ib activates Src kinase in human platelets: role of phosphoinositide 3-kinase.", "Wu Y; Asazuma N; Satoh K; Yatomi Y; Takafuta T; Berndt MC; Ozaki Y", "2003", "Blood", "101", "9", "3469-76"),
    "16368929": ("The Vg1-related protein Gdf3 acts in a Nodal signaling pathway in the pre-gastrulation mouse embryo.", "Chen C; Ware SM; Sato A; Houston-Hawkins DE; Habas R; Matzuk MM; Shen MM; Brown CW", "2006", "Development (Cambridge, England)", "133", "2", "319-29"),
    "15883644": ("Enamel matrix protein interactions.", "Wang H; Tannukit S; Zhu D; Snead ML; Paine ML", "2005", "Journal of bone and mineral research : the official journal of the American Society for Bone and Mineral Research", "20", "6", "1032-40"),
}

AMBIGUOUS_DOIS = {}


def stable_url_key(value: str) -> str | None:
    raw = value.removeprefix("URL:").strip()
    parsed = urlparse(raw)
    path = parsed.path.strip("/")
    if parsed.netloc == "pubmed.ncbi.nlm.nih.gov" and path.isdigit():
        return "PMID:" + path
    if parsed.netloc == "pmc.ncbi.nlm.nih.gov" and path.startswith("articles/"):
        pmcid = path.split("/", 1)[1].split("/", 1)[0]
        return "PMCID:" + pmcid if pmcid.startswith("PMC") else None
    if parsed.netloc == "doi.org" and path:
        return "DOI:" + path.lower()
    return None


def fetch_json(url: str) -> dict:
    request = Request(url, headers={"User-Agent": "mSCITdb/2026 source-anchor audit"})
    with urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def pubmed_summaries(pmids: list[str]) -> dict[str, dict]:
    if not pmids:
        return {}
    url = (
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
        "?db=pubmed&id=" + quote(",".join(sorted(set(pmids)))) + "&retmode=json&tool=mscitdb"
    )
    for attempt in range(6):
        try:
            payload = fetch_json(url).get("result", {})
            break
        except HTTPError as exc:
            if exc.code != 429 or attempt == 5:
                raise
            time.sleep(2.0 * (attempt + 1))
    time.sleep(1.0)
    return {str(pmid): payload.get(str(pmid), {}) for pmid in payload.get("uids", [])}


def pubmed_id_for_doi(doi: str) -> str:
    url = (
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        "?db=pubmed&term=" + quote(doi + "[doi]") + "&retmode=json&retmax=5"
    )
    for attempt in range(6):
        try:
            ids = fetch_json(url).get("esearchresult", {}).get("idlist", [])
            break
        except HTTPError as exc:
            if exc.code != 429 or attempt == 5:
                raise
            time.sleep(2.0 * (attempt + 1))
    time.sleep(1.0)
    return str(ids[0]) if len(ids) == 1 else ""


def fields_from_summary(summary: dict, pmid: str, pmcid: str = "") -> dict[str, str]:
    authors = "; ".join(author.get("name", "") for author in summary.get("authors", []) if author.get("name"))
    article_ids = {item.get("idtype"): item.get("value", "") for item in summary.get("articleids", [])}
    pubdate = summary.get("pubdate", "")
    return {
        "title": summary.get("title", ""),
        "authors": authors,
        "publication_year": pubdate[:4] if pubdate[:4].isdigit() else "",
        "journal": summary.get("fulljournalname") or summary.get("source", ""),
        "volume": summary.get("volume", ""),
        "issue": summary.get("issue", ""),
        "pages": summary.get("pages", ""),
        "doi": article_ids.get("doi", ""),
        "pmid": pmid,
        "pmcid": pmcid or article_ids.get("pmc", ""),
        "source_metadata_url": "https://pubmed.ncbi.nlm.nih.gov/" + pmid + "/",
    }


def copy_metadata(target: dict[str, str], source: dict[str, str]) -> None:
    for field in ("title", "authors", "publication_year", "journal", "volume", "issue", "pages", "pmid", "pmcid"):
        target[field] = source.get(field, "")
    target["doi"] = target["canonical_paper_key"].removeprefix("DOI:") if target["canonical_paper_key"].startswith("DOI:") else source.get("doi", "")
    target["paper_ready"] = "true" if target["title"] and (target["pmid"] or target["pmcid"] or target["doi"]) else "false"


def fallback_source(pmid: str) -> dict[str, str]:
    title, authors, year, journal, volume, issue, pages = PUBMED_FALLBACK[pmid]
    return {
        "title": title, "authors": authors, "publication_year": year,
        "journal": journal, "volume": volume, "issue": issue, "pages": pages,
        "pmid": pmid, "pmcid": "", "doi": "",
        "source_metadata_url": "https://pubmed.ncbi.nlm.nih.gov/" + pmid + "/",
    }


def main() -> None:
    with METADATA.open(newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    by_key = {row["canonical_paper_key"]: row for row in rows}
    by_merge = {row["canonical_merge_key"]: row for row in rows if row["canonical_merge_key"]}
    audit: list[dict[str, str]] = []

    stable_targets = {}
    for row in rows:
        if row["metadata_status"] not in {"url_only_noncanonical", "stable_url_lookup_required"}:
            continue
        stable_key = stable_url_key(row["source_metadata_url"])
        if stable_key:
            stable_targets[stable_key] = True
    stable_pmids = [key.removeprefix("PMID:") for key in stable_targets if key.startswith("PMID:")]
    stable_pmcids = [key.removeprefix("PMCID:") for key in stable_targets if key.startswith("PMCID:")]
    stable_dois = [key.removeprefix("DOI:") for key in stable_targets if key.startswith("DOI:")]
    summaries = pubmed_summaries(stable_pmids)
    pmcid_to_pmid = {}
    if stable_pmcids:
        url = (
            "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids="
            + quote(",".join(sorted(set(stable_pmcids)))) + "&format=json&tool=mscitdb"
        )
        pmcid_records = fetch_json(url).get("records", [])
        pmcid_pmids = []
        for record in pmcid_records:
            if record.get("pmid"):
                pmcid_to_pmid["PMCID:" + record.get("requested-id", "")] = str(record["pmid"])
                pmcid_pmids.append(str(record["pmid"]))
        summaries.update(pubmed_summaries(pmcid_pmids))
    doi_to_pmid = {doi: pubmed_id_for_doi(doi) for doi in stable_dois}
    for pmid in doi_to_pmid.values():
        if pmid and pmid not in summaries:
            summaries.update(pubmed_summaries([pmid]))

    for row in rows:
        key = row["canonical_paper_key"]
        if key.startswith("DOI:"):
            doi = key.removeprefix("DOI:").lower()
            if doi in DOI_TO_PMID:
                pmid_key = "PMID:" + DOI_TO_PMID[doi]
                source = by_key.get(pmid_key) or fallback_source(DOI_TO_PMID[doi])
                if source:
                    copy_metadata(row, source)
                    row["canonical_merge_key"] = pmid_key
                    row["metadata_status"] = "metadata_resolved_pubmed_via_doi"
                    row["source_metadata_url"] = source["source_metadata_url"]
                    audit.append({"source_key": key, "resolution_status": row["metadata_status"], "resolved_key": pmid_key, "reason": "exact PubMed DOI search"})
            elif doi in DOI_TO_COMPANION:
                companion_key = DOI_TO_COMPANION[doi]
                source = by_key.get(companion_key) or by_merge.get(companion_key) or COMPANION_FALLBACK.get(companion_key)
                if source:
                    copy_metadata(row, source)
                    row["canonical_merge_key"] = source["canonical_merge_key"]
                    row["metadata_status"] = (
                        "metadata_resolved_pii_to_doi_companion"
                        if doi in PII_COMPANION_DOIS
                        else "metadata_resolved_companion_anchor"
                    )
                    row["source_metadata_url"] = source["source_metadata_url"]
                    reason = (
                        "Legacy Structure PII S0969-2126(11)00135-3 maps to DOI "
                        "10.1016/j.str.2011.03.011; validated primary paper PMCID:PMC3279696."
                        if doi in PII_COMPANION_DOIS
                        else "validated overlapping stable companion anchor"
                    )
                    audit.append({"source_key": key, "resolution_status": row["metadata_status"], "resolved_key": source["canonical_merge_key"], "reason": reason})
            elif doi in AMBIGUOUS_DOIS:
                status, reason = AMBIGUOUS_DOIS[doi]
                row["metadata_status"] = status
                audit.append({"source_key": key, "resolution_status": status, "resolved_key": "", "reason": reason})

        elif key.startswith("URL:") and row["metadata_status"] in {"url_only_noncanonical", "stable_url_lookup_required"}:
            stable_key = stable_url_key(row["source_metadata_url"])
            source = by_key.get(stable_key or "") or by_merge.get(stable_key or "")
            if source is row or (source is not None and not source.get("title")):
                source = None
            if source is None and stable_key and stable_key.startswith("PMCID:"):
                source = next((candidate for candidate in rows if candidate.get("pmcid") == stable_key.removeprefix("PMCID:")), None)
            if source is None and stable_key:
                if stable_key.startswith("PMID:"):
                    pmid = stable_key.removeprefix("PMID:")
                    source = fields_from_summary(summaries.get(pmid, {}), pmid)
                elif stable_key.startswith("PMCID:"):
                    pmid = pmcid_to_pmid.get(stable_key, "")
                    if pmid:
                        source = fields_from_summary(summaries.get(pmid, {}), pmid, stable_key.removeprefix("PMCID:"))
                elif stable_key.startswith("DOI:"):
                    pmid = doi_to_pmid.get(stable_key.removeprefix("DOI:"), "")
                    if pmid:
                        source = fields_from_summary(summaries.get(pmid, {}), pmid)
            if source and source["title"]:
                copy_metadata(row, source)
                row["canonical_merge_key"] = source.get("canonical_merge_key", stable_key)
                row["metadata_status"] = "metadata_resolved_stable_url"
                row["source_metadata_url"] = source.get("source_metadata_url", row["source_metadata_url"])
                audit.append({"source_key": key, "resolution_status": row["metadata_status"], "resolved_key": row["canonical_merge_key"], "reason": "explicit PMID/PMCID/DOI URL"})

    with OUTPUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    with REPORT_TSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["source_key", "resolution_status", "resolved_key", "reason"], delimiter="\t")
        writer.writeheader()
        writer.writerows(audit)
    counts: dict[str, int] = {}
    for item in audit:
        counts[item["resolution_status"]] = counts.get(item["resolution_status"], 0) + 1
    REPORT_MD.write_text(
        "# Module 20B–24B Identifier Reconciliation\n\n"
        f"- Identifier exception rows reconciled: {len(audit):,}\n"
        + "\n".join(f"- `{status}`: {count:,}" for status, count in sorted(counts.items()))
        + "\n\nDOI strings remain preserved as source locators. Companion reconciliation is used only where the overlapping stable anchor is validated, including the repaired legacy Structure PII mapping. Explicit PMID/PMCID/DOI URLs are canonicalized to their stable identifiers; query URLs and non-paper URLs remain non-canonical.\n"
    )
    print(f"reconciled={len(audit)}")
    print(counts)


if __name__ == "__main__":
    main()
