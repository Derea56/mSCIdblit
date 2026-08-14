#!/usr/bin/env python3
"""Build a reproducible frozen manifest for the curated Module 20A LR release."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROUTER = ROOT / "work" / "module20_db_seed" / "evidence_escalation_router"
OUT = ROUTER / "module20a_lr_release_manifest.json"
COMPARISON = ROUTER / "module20a_cellchat_liana_pair_comparison.tsv"
QUEUE = ROUTER / "module20a_external_review_queue.tsv"
LEDGERS = {
    "low_evidence": ROUTER / "module20a_low_evidence_registry.tsv",
    "no_evidence": ROUTER / "module20a_no_evidence_registry.tsv",
    "non_ligand_receptor": ROUTER / "module20a_non_ligand_receptor_registry.tsv",
}


def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_commit() -> str | None:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def classify(key: str, ledgers: dict[str, set[str]], queue: dict[str, dict[str, str]]) -> str:
    for name, keys in ledgers.items():
        if key in keys:
            return name
    return queue.get(key, {}).get("confidence_decision", "unclassified")


def main() -> None:
    comparison = read(COMPARISON)
    queue_rows = read(QUEUE)
    queue = {row["pair_key"]: row for row in queue_rows}
    ledgers = {name: {row["pair_key"] for row in read(path)} for name, path in LEDGERS.items()}
    universe = {row["pair_key"] for row in comparison}
    if len(universe) != len(comparison):
        raise SystemExit("comparison contains duplicate pair keys")
    source_union = {row["pair_key"] for row in comparison if row["in_cellchat_full"] == "yes" or row["in_liana_consensus"] == "yes"}
    all_counts = Counter(classify(key, ledgers, queue) for key in source_union)
    comparison_only_counts = Counter(classify(key, ledgers, queue) for key in universe - source_union)
    cellchat_counts = Counter(classify(row["pair_key"], ledgers, queue) for row in comparison if row["in_cellchat_full"] == "yes")
    liana_counts = Counter(classify(row["pair_key"], ledgers, queue) for row in comparison if row["in_liana_consensus"] == "yes")
    files = [COMPARISON, QUEUE, *LEDGERS.values()]
    manifest = {
        "manifest_version": "module20a-lr-release-2026-08-14",
        "generated_utc": datetime.now(UTC).isoformat(timespec="seconds"),
        "source_git_commit": git_commit(),
        "pair_universe": {"comparison_total": len(comparison), "source_union_total": len(source_union), "comparison_only_total": len(universe - source_union), "cellchat_full_total": sum(row["in_cellchat_full"] == "yes" for row in comparison), "liana_consensus_total": sum(row["in_liana_consensus"] == "yes" for row in comparison)},
        "classification_counts": {"source_union": dict(sorted(all_counts.items())), "comparison_only": dict(sorted(comparison_only_counts.items())), "cellchat_full": dict(sorted(cellchat_counts.items())), "liana_consensus": dict(sorted(liana_counts.items()))},
        "ledger_row_counts": {name: len(read(path)) for name, path in LEDGERS.items()},
        "queue_row_count": len(queue_rows),
        "files": {str(path.relative_to(ROOT)): {"sha256": sha256(path), "bytes": path.stat().st_size} for path in files},
        "classification_rule": "ledger membership takes precedence over queue confidence; remaining queue confidence is retained as high, medium, or uncertain; unclassified is explicit.",
        "module21a_guardrail": "LR evidence establishes ligand/receptor evidence only; intracellular relay edges require separate primary evidence and must retain species, assay, branch, and context qualifiers.",
    }
    OUT.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
