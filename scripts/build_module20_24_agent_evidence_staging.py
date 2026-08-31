#!/usr/bin/env python3
"""Build module-specific provisional evidence staging from agent decisions."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIR = ROOT / "data/processed/module20_24_database_intake_v1"
FIELDS = [
    "staged_evidence_id", "agent_file", "module_primary", "module_consolidation", "candidate_key",
    "pmid", "entity_a", "entity_b", "source_databases", "disposition", "evidence_status",
    "pair_support", "primary_experiment", "module_fit", "routed_modules", "independent_corroboration_required",
    "evidence_summary", "limitations", "canonical_eligible", "notes",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in FIELDS} for row in rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_DIR)
    args = parser.parse_args()
    decisions = {row["candidate_key"]: row for row in read_tsv(args.input_dir / "database_evidence_decisions_merged.tsv")}
    rows: list[dict[str, str]] = []
    errors: list[str] = []
    counter = 0
    for agent_path in sorted((args.input_dir / "agent_reviews").glob("module_*_agent_*.tsv")):
        for agent in read_tsv(agent_path):
            key = agent.get("candidate_key", "")
            base = decisions.get(key)
            if not base:
                errors.append(f"unknown candidate key: {key}")
                continue
            counter += 1
            routed = agent.get("routed_modules", "") or base.get("routed_modules", base.get("module_primary", ""))
            required = "true" if agent.get("corroboration_needed", "").casefold() in {"yes", "true", "required"} else base.get("corroboration_required", "true")
            disposition = agent.get("disposition", "")
            status = "provisional_abstract_supported" if disposition == "abstract_supported_candidate" else "agent_hold_or_boundary"
            rows.append({
                "staged_evidence_id": f"DBINT-AGENT-{counter:06d}",
                "agent_file": str(agent_path.relative_to(ROOT)),
                "module_primary": base.get("module_primary", ""),
                "module_consolidation": base.get("module_consolidation", ""),
                "candidate_key": key, "pmid": agent.get("pmid", base.get("pmid", "")),
                "entity_a": agent.get("entity_a", base.get("entity_a", "")),
                "entity_b": agent.get("entity_b", base.get("entity_b", "")),
                "source_databases": base.get("database_ids", ""), "disposition": disposition,
                "evidence_status": status, "pair_support": agent.get("pair_support", base.get("pair_support", "")),
                "primary_experiment": agent.get("primary_experiment", base.get("primary_experiment", "")),
                "module_fit": agent.get("module_fit", base.get("module_fit", "")),
                "routed_modules": routed, "independent_corroboration_required": required,
                "evidence_summary": agent.get("evidence_summary", base.get("evidence_excerpt", "")),
                "limitations": agent.get("limitations", base.get("limitations", "")),
                "canonical_eligible": "false",
                "notes": "Agent abstract review is a provisional staging decision; full text and exact module-specific corroboration remain required.",
            })
    rows.sort(key=lambda row: row["staged_evidence_id"])
    write_tsv(args.input_dir / "agent_evidence_staging.tsv", rows)
    for module in ("20A", "21A", "23A", "24A"):
        write_tsv(args.input_dir / f"module_{module}_agent_evidence_staging.tsv", [row for row in rows if row["module_primary"] == module])
    manifest = {
        "agent_files": len(list((args.input_dir / "agent_reviews").glob("module_*_agent_*.tsv"))),
        "agent_evidence_rows": len(rows),
        "by_module": dict(sorted(Counter(row["module_primary"] for row in rows).items())),
        "by_disposition": dict(sorted(Counter(row["disposition"] for row in rows).items())),
        "corroboration_required": sum(row["independent_corroboration_required"] == "true" for row in rows),
        "canonical_write_performed": False, "errors": errors,
    }
    (args.input_dir / "agent_evidence_staging_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
