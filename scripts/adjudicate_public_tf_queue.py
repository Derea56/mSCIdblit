#!/usr/bin/env python3
"""Record bounded exact-pair literature adjudication for the mouse TF queue.

This is an audit ledger, not an automatic promotion mechanism.  A queue row
is promoted only after a reviewer supplies an exact-pair primary citation and
the validated overlay is regenerated through the strict curation code.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from typing import Mapping


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QUEUE = ROOT / "data/processed/public_tf_curation_v2026_09_04/public_tf_mouse_direct_binding_review_queue.tsv"
DEFAULT_OUTPUT = ROOT / "data/processed/public_tf_curation_v2026_09_04/public_tf_queue_adjudication.tsv"
DEFAULT_SUMMARY = ROOT / "data/processed/public_tf_curation_v2026_09_04/public_tf_queue_adjudication_summary.json"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[Mapping[str, object]]) -> None:
    if not rows:
        raise ValueError(f"Cannot write empty table: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0]),
            delimiter="\t",
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def value(row: Mapping[str, object], key: str) -> str:
    return str(row.get(key, "") or "").strip()


def near_match_note(regulator: str, target: str) -> str:
    pair = (regulator.casefold(), target.casefold())
    notes = {
        ("fezf2", "acvr1"): (
            "A mouse corticospinal Fezf2 study reports Acvr1c among target genes, "
            "not the queued Acvr1 pair; this near-match is not promotion evidence."
        ),
        ("hoxc12", "angptl4"): (
            "Direct mouse Angptl4 regulation was identified for glucocorticoid receptor "
            "in the bounded search, not for HOXC12; this is not exact-pair evidence."
        ),
        ("hes5", "adam22"): (
            "Mouse ADAM22 neural-function papers and HES5 target papers were found, "
            "but no HES5-to-Adam22 regulatory result was identified."
        ),
        ("neurod2", "adam10"): (
            "Mouse NeuroD2 papers support other neuronal targets, including Ulip1 and "
            "genome-wide target sets; Adam10 was not verified as an exact functional target."
        ),
        ("npas4", "adam22"): (
            "Mouse NPAS4 studies support activity-dependent targets such as Bdnf, not "
            "the queued Adam22 pair."
        ),
        ("zfp281", "a2m"): (
            "Mouse Zfp281 direct-target studies support Tet2/miR-302/367 or Ctla4 in "
            "other contexts, not A2m."
        ),
    }
    return notes.get(pair, "")


def adjudicate(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    output: list[dict[str, str]] = []
    for row in rows:
        regulator = value(row, "regulator")
        target = value(row, "target")
        note = near_match_note(regulator, target)
        output.append(
            {
                "source_row_id": value(row, "source_row_id"),
                "module": value(row, "module"),
                "regulator": regulator,
                "target": target,
                "curation_status": "candidate_only",
                "traversal_eligibility": "not_traversable",
                "review_disposition": "retain_candidate_only_no_exact_pair_promotion",
                "search_status": "bounded_exact_pair_search_completed_no_exact_primary_evidence_identified",
                "search_scope": "PubMed/web searches using regulator, target, mouse, direct-binding/functional-target terms; related primary papers checked when surfaced",
                "search_terms": f'"{regulator}" "{target}" mouse direct binding functional target',
                "exact_pair_evidence": "not_identified",
                "binding_evidence": "TFLink/GTRD source-table association only; underlying primary occupancy record not identified",
                "functional_evidence": "not_identified",
                "species": value(row, "species") or "unknown",
                "tissue_cell_context": "unknown",
                "sci_context": "unknown",
                "effect_direction": "unknown",
                "confidence": "low_bounded_search_only",
                "primary_citation": "unknown",
                "source_record_id": value(row, "source_record_id") or "unknown",
                "source_provenance": (
                    f"{value(row, 'source_record_id') or 'unknown'}; "
                    f"TFLink source PMID {value(row, 'tflink_pubmed_id') or 'unknown'} "
                    "is source-database metadata, not exact-pair validation"
                ),
                "limitations": (
                    "No exact-pair primary citation with direct sequence-specific binding "
                    "and functional target response was identified in this bounded pass; "
                    "full-text review, additional databases, and underlying GTRD experiment "
                    "accession remain possible follow-up work."
                ),
                "reviewer_notes": note or "No exact-pair promotion basis identified; preserve unknown values.",
                "reviewed_at": "2026-09-04",
            }
        )
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue", type=Path, default=DEFAULT_QUEUE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--summary", type=Path, default=DEFAULT_SUMMARY)
    args = parser.parse_args()
    rows = read_tsv(args.queue)
    if len(rows) != 112:
        raise ValueError(f"Expected 112 queue rows; observed {len(rows)}")
    adjudicated = adjudicate(rows)
    write_tsv(args.output, adjudicated)
    summary = {
        "schema_version": "mscidblit_public_tf_queue_adjudication_summary_v1",
        "queue_rows_reviewed": len(adjudicated),
        "promotion_decisions": dict(Counter(row["review_disposition"] for row in adjudicated)),
        "exact_pair_evidence": dict(Counter(row["exact_pair_evidence"] for row in adjudicated)),
        "traversable_rows_added": 0,
        "primary_citations_added": 0,
        "method": "bounded exact-pair literature search; no automatic promotion",
        "limitations": [
            "Search results do not establish absence from all literature.",
            "TFLink/GTRD source-table metadata do not substitute for the underlying exact-pair primary record.",
            "Rows require a new exact-pair adjudication record before validated-overlay promotion.",
        ],
    }
    args.summary.parent.mkdir(parents=True, exist_ok=True)
    args.summary.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
