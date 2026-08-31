#!/usr/bin/env python3
"""Classify query-search hits for manual review without evidence promotion."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "work" / "cross_module_synthesis" / "module20_24_query_url_search_audit.tsv"
OUTPUT = ROOT / "work" / "cross_module_synthesis" / "module20_24_query_candidate_triage.tsv"
REPORT = ROOT / "work" / "cross_module_synthesis" / "module20_24_query_candidate_triage.md"

STRONG = {
    "M22B-EVID-005378": "CXCL16/CXCR6 axis and downstream PI3K/AKT/FOXO3A are named in the singleton-relevant top result; full-text claim validation still required.",
    "M22B-EVID-004982": "EPO/STAT5/SOCS2 signaling is named in the singleton top result; receptor-complex and assay-context validation still required.",
    "M22B-EVID-005054": "TGF-beta and integrin-alphaVbeta1 signaling are named in the top result; ligand/receptor-context and species validation still required.",
    "M22B-EVID-003355": "Decorin/PDCD4 signaling is named in the singleton top result; TLR4-specific attribution and assay validation still required.",
}


def main() -> None:
    with INPUT.open(newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    results = []
    for row in rows:
        if row["status"].strip() != "candidate_hits_unpromoted":
            continue
        evidence = row["evidence_ids"]
        if evidence in STRONG:
            triage = "strong_candidate_requires_full_text_validation"
            reason = STRONG[evidence]
        elif row["result_count"] == "1":
            triage = "singleton_candidate_not_promoted"
            reason = "A single PubMed hit was found, but the query URL is not a paper citation and source-specific claim validation is still missing."
        else:
            triage = "multiple_candidates_not_promoted"
            reason = "Multiple PubMed hits were found; the search URL does not identify which paper supports the claim."
        results.append({
            "source_key": row["source_key"],
            "evidence_ids": evidence,
            "query": row["query"],
            "result_count": row["result_count"],
            "top_pmids": row["top_pmids"],
            "triage_status": triage,
            "reason": reason,
        })
    fields = ["source_key", "evidence_ids", "query", "result_count", "top_pmids", "triage_status", "reason"]
    with OUTPUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(results)
    counts = {}
    for row in results:
        counts[row["triage_status"]] = counts.get(row["triage_status"], 0) + 1
    REPORT.write_text(
        "# Module 20B–24B Query Candidate Triage\n\n"
        f"- Candidate query rows triaged: {len(results):,}\n"
        + "\n".join(f"- `{status}`: {count:,}" for status, count in sorted(counts.items()))
        + "\n\nNo query hit was promoted to canonical evidence. A search URL does not establish paper identity, assay, species, cell model, or layer-specific support.\n"
    )
    print(f"triaged={len(results)}")
    print(counts)


if __name__ == "__main__":
    main()
