#!/usr/bin/env python3
"""Build a disposition ledger for downstream queue records without output routes.

The ledger is deliberately non-causal. It records what the stored curated
summary supports at the current release boundary; it does not claim that the
underlying primary paper lacks additional results.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


FIELDS = [
    "queue_id",
    "module",
    "edge_id",
    "source_label",
    "target_label",
    "evidence_scope",
    "curation_priority",
    "disposition",
    "output_class_observed",
    "route_action",
    "review_basis",
    "source_locator",
    "source_evidence_ids",
    "evidence_summary",
    "limitations",
    "next_action",
]


def main() -> int:
    args = parse_args()
    bundle = args.bundle_dir.resolve()
    queue = read_tsv(bundle / "mechanism_downstream_curation_queue.tsv")
    curated_ids: set[str] = set()
    for path in sorted(bundle.parent.glob("mechanism_graph_module20_24_v2026_09_21_literature_expansion*/mechanism_literature_expansion.tsv")):
        curated_ids.update(row.get("source_queue_id", "") for row in read_tsv(path))

    rows: list[dict[str, str]] = []
    for source in queue:
        queue_id = source["queue_id"]
        if queue_id in curated_ids:
            continue
        scope = source.get("evidence_scope", "")
        if scope == "direct_edge":
            disposition = "reviewed_no_explicit_downstream_output_in_curated_record"
        elif scope == "contextual_support":
            disposition = "reviewed_contextual_association_without_explicit_output"
        elif scope == "pathway_membership":
            disposition = "reviewed_pathway_context_without_explicit_output"
        else:
            disposition = "reviewed_without_explicit_output"
        rows.append(
            {
                "queue_id": queue_id,
                "module": source.get("module", ""),
                "edge_id": source.get("edge_id", ""),
                "source_label": source.get("source_label", ""),
                "target_label": source.get("target_label", ""),
                "evidence_scope": scope,
                "curation_priority": source.get("curation_priority", ""),
                "disposition": disposition,
                "output_class_observed": source.get("output_class", "unknown"),
                "route_action": "retain_entry_evidence_only",
                "review_basis": (
                    "Manual audit of the stored primary-supported evidence_summary and "
                    "assay_or_perturbation fields; no explicit downstream output/readout "
                    "was retained in the curated record."
                ),
                "source_locator": source.get("source_locator", ""),
                "source_evidence_ids": source.get("source_evidence_ids", ""),
                "evidence_summary": source.get("evidence_summary", ""),
                "limitations": source.get("limitations", ""),
                "next_action": "full_text_primary_review_if_output_route_is_needed",
            }
        )

    rows.sort(key=lambda row: row["queue_id"])
    args.output.resolve().parent.mkdir(parents=True, exist_ok=True)
    write_tsv(args.output.resolve(), FIELDS, rows)
    print(
        {
            "bundle_dir": str(bundle),
            "output": str(args.output.resolve()),
            "disposition_rows": len(rows),
            "dispositions": {
                disposition: sum(row["disposition"] == disposition for row in rows)
                for disposition in sorted({row["disposition"] for row in rows})
            },
        }
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
