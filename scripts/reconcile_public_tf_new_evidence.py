#!/usr/bin/env python3
"""Reconcile newly graded Module 22B/23B evidence against the public-TF queue.

The evidence passes are broader mechanism evidence, not automatic TF
promotions.  This audit performs exact structured matching where a register
contains source and target fields and records when an evidence-only or grade
file cannot support pair matching because those fields are absent.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QUEUE = ROOT / "data/processed/public_tf_curation_v2026_09_04/public_tf_mouse_direct_binding_review_queue.tsv"
DEFAULT_OUTPUT = ROOT / "data/processed/public_tf_curation_v2026_09_04/public_tf_new_evidence_reconciliation.json"


def norm(value: object) -> str:
    return " ".join(str(value or "").split()).casefold()


def display_path(path: Path) -> str:
    """Keep committed audit paths repository-relative and portable."""

    parts = path.resolve().parts
    for repo_name in ("mSCIdblit-latent-pipeline", "mSCIdblit"):
        if repo_name in parts:
            index = parts.index(repo_name)
            return "/".join((repo_name, *parts[index + 1 :]))
    return str(path)


def read_rows(path: Path) -> tuple[list[str], Iterable[dict[str, str]]]:
    handle = path.open(newline="", encoding="utf-8", errors="replace")
    reader = csv.DictReader(handle, delimiter="\t")
    rows = list(reader)
    handle.close()
    return reader.fieldnames or [], rows


def queue_pairs(path: Path) -> dict[tuple[str, str], dict[str, str]]:
    fields, rows = read_rows(path)
    required = {"regulator", "target", "source_row_id", "module"}
    if not required.issubset(fields):
        raise ValueError(f"Queue missing fields: {sorted(required - set(fields))}")
    return {
        (norm(row["regulator"]), norm(row["target"])): row
        for row in rows
    }


def inspect_input(
    label: str,
    path: Path,
    queue: dict[tuple[str, str], dict[str, str]],
) -> dict[str, object]:
    fields, rows = read_rows(path)
    has_pair_fields = {"source_entity", "target_entity"}.issubset(fields)
    hits: list[dict[str, str]] = []
    if has_pair_fields:
        for row in rows:
            pair = (norm(row.get("source_entity")), norm(row.get("target_entity")))
            if pair in queue:
                hits.append(
                    {
                        "source_row_id": queue[pair]["source_row_id"],
                        "module": queue[pair]["module"],
                        "regulator": queue[pair]["regulator"],
                        "target": queue[pair]["target"],
                        "evidence_row_id": row.get("b_edge_id", "") or row.get("b_evidence_id", ""),
                    }
                )
    return {
        "label": label,
        "path": display_path(path),
        "rows": len(rows),
        "fields": fields,
        "structured_pair_fields_present": has_pair_fields,
        "exact_queue_pair_hits": hits,
        "exact_queue_pair_count": len({(h["regulator"].casefold(), h["target"].casefold()) for h in hits}),
        "interpretation": (
            "Exact structured source_entity/target_entity comparison performed."
            if has_pair_fields
            else "No structured regulator/target fields; this file cannot independently establish pair overlap."
        ),
    }


def parse_input(spec: str) -> tuple[str, Path]:
    if "=" not in spec:
        raise ValueError(f"Input must use LABEL=PATH: {spec}")
    label, raw_path = spec.split("=", 1)
    if not label or not raw_path:
        raise ValueError(f"Input must use LABEL=PATH: {spec}")
    path = Path(raw_path)
    if not path.is_file():
        raise FileNotFoundError(path)
    return label, path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue", type=Path, default=DEFAULT_QUEUE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--revision", action="append", default=[], help="LABEL=COMMIT")
    parser.add_argument("--input", action="append", required=True, help="LABEL=TSV_PATH")
    args = parser.parse_args()

    _, queue_rows_data = read_rows(args.queue)
    queue_row_count = len(queue_rows_data)
    queue = queue_pairs(args.queue)
    revisions = dict(spec.split("=", 1) for spec in args.revision if "=" in spec)
    inputs = [inspect_input(label, path, queue) for label, path in (parse_input(spec) for spec in args.input)]
    exact_pairs = {
        (hit["regulator"].casefold(), hit["target"].casefold())
        for item in inputs
        for hit in item["exact_queue_pair_hits"]
    }
    payload = {
        "schema_version": "mscidblit_public_tf_new_evidence_reconciliation_v1",
        "review_date": "2026-09-05",
        "queue_path": display_path(args.queue),
        "queue_rows": queue_row_count,
        "queue_unique_pairs": len(queue),
        "source_revisions": revisions,
        "inputs": inputs,
        "result": {
            "exact_structured_queue_pair_overlap": len(exact_pairs),
            "queue_pairs_with_new_exact_structured_evidence": len(exact_pairs),
            "promotion_candidates_identified": 0,
            "queue_rows_remaining_candidate_only": queue_row_count,
            "queue_unique_pairs_remaining_candidate_only": len(queue),
            "candidate_rows_remain_non_traversable": True,
        },
        "limitations": [
            "Mechanism evidence and grading passes were not treated as automatic public-TF promotions.",
            "Files without structured regulator/target fields cannot establish exact pair overlap by themselves.",
            "Zero structured overlap does not establish absence from unindexed supplements or other sources.",
            "A qualifying promotion still requires exact mouse TF binding, functional target response, citation, direction, and explicit module/context adjudication.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload["result"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
