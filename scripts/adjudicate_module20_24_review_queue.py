#!/usr/bin/env python3
"""Adjudicate exact duplicates in the Module 20–24 review queue.

This is a conservative queue-cleanup step. A review unit is resolved only
when an artifact with the same register evidence ID, resolved PMID, and exact
artifact path already has a ``supporting_validated_claim`` adjudication. The
result reuses the existing source unit; it does not create a new claim,
observation, edge, paper relationship, or canonical database row.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_module20_24_artifact_adjudication import (  # noqa: E402
    content_self_identifiers,
    stable_paper_tokens,
)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QUEUE = ROOT / "data/processed/module20_24_database_intake_v1/module20_24_promotion_review_queue.tsv"
DEFAULT_ARTIFACTS = ROOT / "data/processed/module20_24_evidence_artifact_provenance_v1/artifact_adjudication.tsv"
DEFAULT_OUTPUT = ROOT / "data/processed/module20_24_database_intake_v1/module20_24_review_adjudications.tsv"
DEFAULT_SUMMARY = ROOT / "data/processed/module20_24_database_intake_v1/module20_24_review_adjudications_summary.json"


FIELDS = [
    "review_unit_key", "module", "register_edge_id", "register_evidence_id",
    "extraction_id", "canonical_paper_key", "resolved_pmid", "evidence_grade",
    "context_level", "review_batch", "review_route", "artifact_row_count",
    "decision", "existing_support_extraction_ids", "existing_support_artifact_paths",
    "resolved_pmid_from_artifact", "resolution_artifact_path",
    "resolution_artifact_identifiers", "decision_basis",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--queue", type=Path, default=DEFAULT_QUEUE)
    parser.add_argument("--artifacts", type=Path, default=DEFAULT_ARTIFACTS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--summary", type=Path, default=DEFAULT_SUMMARY)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    queue_rows = read_tsv(args.queue)
    artifact_rows = read_tsv(args.artifacts)

    units: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in queue_rows:
        units[row["review_unit_key"]].append(row)

    existing_support: dict[tuple[str, str, str], set[str]] = defaultdict(set)
    for row in artifact_rows:
        if row.get("artifact_support_status") != "supporting_validated_claim":
            continue
        key = (
            row.get("register_evidence_id", ""),
            row.get("resolved_pmid", ""),
            row.get("artifact_path", ""),
        )
        if all(key):
            existing_support[key].add(row.get("extraction_id", ""))

    decisions: list[dict[str, str]] = []
    for unit_key, rows in units.items():
        first = rows[0]
        evidence_id = first.get("register_evidence_id", "")
        pmid = first.get("resolved_pmid", "")
        artifact_paths = sorted({row.get("artifact_path", "") for row in rows})
        matches: dict[str, set[str]] = defaultdict(set)
        for path in artifact_paths:
            for extraction_id in existing_support.get((evidence_id, pmid, path), set()):
                matches[path].add(extraction_id)

        support_ids = sorted({item for values in matches.values() for item in values if item})
        support_paths = sorted(matches)
        key_pmids = {value for kind, value in stable_paper_tokens(first.get("canonical_paper_key", "")) if kind == "PMID"}
        artifact_resolution_options: list[tuple[str, str, str]] = []
        ambiguous_identity_paths: list[str] = []
        for path in artifact_paths:
            artifact_path = ROOT / path
            if not artifact_path.exists():
                continue
            roles = {row.get("artifact_role", "") for row in rows if row.get("artifact_path") == path}
            identifiers = set()
            for role in roles:
                identifiers.update(content_self_identifiers(artifact_path, role))
            self_pmids = {value for kind, value in identifiers if kind == "PMID"}
            overlap = self_pmids & key_pmids
            if len(self_pmids) == 1 and len(overlap) == 1:
                artifact_resolution_options.append(
                    (next(iter(overlap)), path, ";".join(f"{kind}:{value}" for kind, value in sorted(identifiers)))
                )
            elif overlap:
                ambiguous_identity_paths.append(path)
        artifact_resolution_pmids = {pmid for pmid, _, _ in artifact_resolution_options}
        artifact_identity_resolution = (
            not support_ids
            and first.get("review_route") == "identity_resolution_needed"
            and len(artifact_resolution_pmids) == 1
            and not ambiguous_identity_paths
        )
        resolved_from_artifact = ""
        resolution_artifact_path = ""
        resolution_artifact_identifiers = ""
        if artifact_identity_resolution:
            resolved_from_artifact = next(iter(artifact_resolution_pmids))
            selected = next(item for item in artifact_resolution_options if item[0] == resolved_from_artifact)
            resolution_artifact_path = selected[1]
            resolution_artifact_identifiers = selected[2]
        if support_ids:
            decision = "resolved_reuse_existing_support"
            basis = (
                "Exact same register evidence ID, resolved PMID, and artifact path already "
                "map to a supporting_validated_claim source unit. Reuse that existing unit; "
                "do not create a duplicate canonical evidence record."
            )
        elif artifact_identity_resolution:
            decision = "resolved_exact_source_artifact_identity"
            basis = (
                "A retained source artifact contains exactly one PMID in source-record metadata, "
                "that PMID is explicitly present in the original composite canonical paper key, "
                "and no other artifact in the review unit selects a competing key PMID. The "
                "original composite key remains unchanged; this is a row-level identity resolution only."
            )
        elif first.get("review_route") == "identity_resolution_needed":
            decision = "pending_identity_resolution"
            basis = "No exact existing supporting source unit was found and the queue requires authoritative paper identity resolution."
        elif first.get("review_route") == "identity_resolved_source_review":
            decision = "pending_source_review"
            basis = "Paper identity is exact, but the observation/claim gate still requires source-level review."
        else:
            decision = "pending_manual_adjudication"
            basis = "No exact existing supporting source unit was found; retain the queue unit for manual source adjudication."

        decisions.append({
            "review_unit_key": unit_key,
            "module": first.get("module", ""),
            "register_edge_id": first.get("register_edge_id", ""),
            "register_evidence_id": evidence_id,
            "extraction_id": first.get("extraction_id", ""),
            "canonical_paper_key": first.get("canonical_paper_key", ""),
            "resolved_pmid": pmid,
            "evidence_grade": first.get("evidence_grade", ""),
            "context_level": first.get("context_level", ""),
            "review_batch": first.get("review_batch", ""),
            "review_route": first.get("review_route", ""),
            "artifact_row_count": str(len(rows)),
            "decision": decision,
            "existing_support_extraction_ids": ";".join(support_ids),
            "existing_support_artifact_paths": ";".join(support_paths),
            "resolved_pmid_from_artifact": resolved_from_artifact,
            "resolution_artifact_path": resolution_artifact_path,
            "resolution_artifact_identifiers": resolution_artifact_identifiers,
            "decision_basis": basis,
        })

    decisions.sort(key=lambda row: (row["module"], row["review_unit_key"]))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(decisions)

    by_decision = Counter(row["decision"] for row in decisions)
    by_batch = Counter(row["review_batch"] or "unassigned" for row in decisions)
    batch_one = [row for row in decisions if row["review_batch"] == "batch_001"]
    exact_identity = [row for row in decisions if row["decision"] == "resolved_exact_source_artifact_identity"]
    summary = {
        "queue": str(args.queue),
        "artifacts": str(args.artifacts),
        "output": str(args.output),
        "review_units": len(decisions),
        "queue_rows": len(queue_rows),
        "decisions_by_status": dict(sorted(by_decision.items())),
        "review_units_by_batch": dict(sorted(by_batch.items())),
        "batch_001_review_units": len(batch_one),
        "batch_001_exact_reuse_units": sum(
            row["decision"] == "resolved_reuse_existing_support" for row in batch_one
        ),
        "exact_source_artifact_identity_units": len(exact_identity),
        "evidence_grade_preserved": True,
        "context_level_preserved": True,
        "canonical_database_write_performed": False,
    }
    with args.summary.open("w", encoding="utf-8") as handle:
        json.dump(summary, handle, indent=2)
        handle.write("\n")

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
