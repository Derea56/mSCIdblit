#!/usr/bin/env python3
"""Run a resumable PubMed exact-pair screen for C-tier pair-level L0 rows.

This is a candidate-discovery step.  A PubMed hit is not treated as
species-matched mechanism evidence until its article is adjudicated separately.
The script does not modify context grades or any release/materialization file.
"""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import time
from pathlib import Path
from urllib.parse import urlencode


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QUEUE = (
    ROOT
    / "data/processed/public_tf_union_expansion_v1/"
    "comprehensive_interaction_promotion_v1/module_integration_staging_v1/"
    "c_tier_context_review_queue.tsv"
)
DEFAULT_CONTEXT = (
    ROOT
    / "data/processed/public_tf_union_expansion_v1/"
    "comprehensive_interaction_promotion_v1/module_integration_staging_v1/"
    "context_evidence_adjudications.tsv"
)
DEFAULT_OUTPUT = (
    ROOT
    / "data/processed/public_tf_union_expansion_v1/"
    "comprehensive_interaction_promotion_v1/module_integration_staging_v1/"
    "c_tier_exact_pair_pubmed_screen_round_242.tsv"
)

FIELDS = [
    "round_id",
    "promotion_id",
    "regulator_symbol",
    "target_symbol",
    "species_scope",
    "context_level_exact_pair",
    "query",
    "pubmed_hit_count",
    "pubmed_ids",
    "screen_outcome",
    "screen_basis",
]


def split_symbols(value: str) -> list[str]:
    result = []
    for chunk in (value or "").replace("/", ";").split(";"):
        chunk = chunk.strip()
        if chunk and len(chunk) >= 3 and chunk not in result:
            result.append(chunk)
    return result


def term_for(symbols: list[str]) -> str:
    quoted = [f'"{symbol}"[Title/Abstract]' for symbol in symbols]
    return quoted[0] if len(quoted) == 1 else "(" + " OR ".join(quoted) + ")"


def query_pubmed(
    query: str, retmax: int, retries: int, retry_delay: float
) -> tuple[int, list[str]]:
    params = urlencode(
        {
            "db": "pubmed",
            "retmode": "json",
            "retmax": str(retmax),
            "sort": "relevance",
            "term": query,
        }
    )
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + params
    last_error: Exception | None = None
    for attempt in range(retries + 1):
        try:
            completed = subprocess.run(
                ["curl", "-L", "--fail", "--max-time", "30", "-sS", url],
                capture_output=True,
                text=True,
                check=True,
            )
            payload = json.loads(completed.stdout)
            break
        except Exception as exc:
            last_error = exc
            if attempt >= retries:
                raise
            time.sleep(retry_delay * (2**attempt))
    else:  # pragma: no cover - loop either breaks or raises above
        raise last_error or RuntimeError("PubMed request failed")
    result = payload["esearchresult"]
    return int(result.get("count", "0")), list(result.get("idlist", []))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--queue", type=Path, default=DEFAULT_QUEUE)
    parser.add_argument("--context", type=Path, default=DEFAULT_CONTEXT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--delay", type=float, default=0.36)
    parser.add_argument("--retries", type=int, default=5)
    parser.add_argument("--retry-delay", type=float, default=1.0)
    parser.add_argument("--retmax", type=int, default=20)
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    with args.context.open(newline="", encoding="utf-8") as handle:
        l0_ids = {
            row["promotion_id"]
            for row in csv.DictReader(handle, delimiter="\t")
            if row.get("evidence_weight_tier", "").startswith("C_")
            and row.get("context_level_exact_pair", "").startswith("L0_")
        }
    with args.queue.open(newline="", encoding="utf-8") as handle:
        queue = {
            row["promotion_id"]: row
            for row in csv.DictReader(handle, delimiter="\t")
            if row["promotion_id"] in l0_ids
        }

    completed: set[str] = set()
    existing_rows: list[dict[str, str]] = []
    if args.output.exists():
        with args.output.open(newline="", encoding="utf-8") as handle:
            existing_rows = list(csv.DictReader(handle, delimiter="\t"))
        completed = {
            row["promotion_id"]
            for row in existing_rows
            if row.get("screen_outcome") != "pubmed_query_error"
        }
        failed_rows = [
            row for row in existing_rows if row.get("screen_outcome") == "pubmed_query_error"
        ]
        if failed_rows:
            with args.output.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t")
                writer.writeheader()
                writer.writerows(
                    row for row in existing_rows if row.get("screen_outcome") != "pubmed_query_error"
                )
            print(f"removed {len(failed_rows)} prior transient-error rows for retry")
    pending = [
        queue[promotion_id]
        for promotion_id in sorted(
            queue, key=lambda value: int(value.rsplit("_", 1)[1])
        )
        if promotion_id not in completed
    ]
    if args.limit:
        pending = pending[: args.limit]

    args.output.parent.mkdir(parents=True, exist_ok=True)
    needs_header = not args.output.exists() or args.output.stat().st_size == 0
    with args.output.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t")
        if needs_header:
            writer.writeheader()
        for index, row in enumerate(pending, start=1):
            regulator_symbols = split_symbols(row.get("regulator_symbol", ""))
            raw_symbols = split_symbols(row.get("raw_tf_symbol", ""))
            for symbol in raw_symbols:
                if symbol not in regulator_symbols:
                    regulator_symbols.append(symbol)
            target_symbols = split_symbols(row.get("target_symbol", ""))
            query = f"{term_for(regulator_symbols)} AND {term_for(target_symbols)}"
            try:
                hit_count, ids = query_pubmed(
                    query, args.retmax, args.retries, args.retry_delay
                )
                outcome = (
                    "candidate_pubmed_hits_require_article_adjudication"
                    if hit_count
                    else "no_pubmed_title_abstract_hit_in_bounded_screen"
                )
                basis = (
                    "PubMed ESearch exact symbol query; hit presence is candidate discovery only, "
                    "not evidence of species-matched direct regulation or occupancy."
                )
            except Exception as exc:  # retain a reproducible failure, then continue
                hit_count, ids = -1, []
                outcome = "pubmed_query_error"
                basis = f"PubMed ESearch error retained for retry: {type(exc).__name__}: {exc}"
            writer.writerow(
                {
                    "round_id": "242",
                    "promotion_id": row["promotion_id"],
                    "regulator_symbol": row.get("regulator_symbol", ""),
                    "target_symbol": row.get("target_symbol", ""),
                    "species_scope": row.get("species_scope", ""),
                    "context_level_exact_pair": "L0_no_context_evidence",
                    "query": query,
                    "pubmed_hit_count": str(hit_count),
                    "pubmed_ids": ";".join(ids),
                    "screen_outcome": outcome,
                    "screen_basis": basis,
                }
            )
            handle.flush()
            if index < len(pending):
                time.sleep(max(args.delay, 0.0))
            if index % 50 == 0:
                print(f"screened {index}/{len(pending)} pending exact pairs")
    print(f"screened {len(pending)} pending exact pairs; total records now {len(completed) + len(pending)}")


if __name__ == "__main__":
    main()
