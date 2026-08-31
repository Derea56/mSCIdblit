#!/usr/bin/env python3
"""Merge bounded agent reviews into the abstract-level evidence ledger."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIR = ROOT / "data/processed/module20_24_database_intake_v1"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


def infer_routes(agent: dict[str, str], base: dict[str, str]) -> str:
    """Preserve explicit routes and recover neighboring-module notes from agent prose."""
    explicit = agent.get("routed_modules", "")
    if explicit:
        return explicit
    primary = base.get("module_primary", "")
    text = " ".join(agent.get(field, "") for field in ("module_fit", "evidence_summary", "limitations")).casefold()
    routes = [primary]
    for module in ("20A", "21A", "22A", "23A", "24A"):
        label = module[:2]
        if module == primary:
            continue
        # Only promote a prose mention to a handoff when the agent explicitly
        # marked the row as neighboring/partial or described a cross-module
        # mechanism. Generic entity mentions remain in the base queue.
        if ("neighboring_module_only" in text or "partial" in text or "cross" in text or "rather than" in text) and re.search(rf"module\s*{label}", text):
            routes.append(module)
    return ";".join(dict.fromkeys(routes))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_DIR)
    args = parser.parse_args()
    base_path = args.input_dir / "database_evidence_decisions.tsv"
    base = read_tsv(base_path)
    by_key = {row["candidate_key"]: row for row in base}
    agent_paths = sorted((args.input_dir / "agent_reviews").glob("module_*_agent_*.tsv"))
    errors: list[str] = []
    applied = 0
    agent_rows = []
    for path in agent_paths:
        rows = read_tsv(path)
        for row in rows:
            key = row.get("candidate_key", "")
            if key not in by_key:
                errors.append(f"{path.name}: unknown candidate_key {key}")
                continue
            target = by_key[key]
            target["disposition"] = row.get("disposition", target["disposition"])
            target["pair_support"] = row.get("pair_support", target["pair_support"])
            target["primary_experiment"] = row.get("primary_experiment", target["primary_experiment"])
            target["module_fit"] = row.get("module_fit", target["module_fit"])
            target["corroboration_required"] = "true" if row.get("corroboration_needed", "").casefold() in {"yes", "true", "required"} else target["corroboration_required"]
            target["evidence_excerpt"] = row.get("evidence_summary", target["evidence_excerpt"])
            target["limitations"] = row.get("limitations", target["limitations"])
            target["routed_modules"] = infer_routes(row, target)
            target["decision_basis"] = f"agent_review:{path.name}; " + target.get("decision_basis", "")
            agent_rows.append({
                "agent_file": str(path.relative_to(ROOT)), "module_primary": row.get("module_primary", ""),
                "candidate_key": key, "pmid": row.get("pmid", ""), "disposition": row.get("disposition", ""),
            })
            applied += 1

    fields = list(base[0]) if base else []
    merged_path = args.input_dir / "database_evidence_decisions_merged.tsv"
    write_tsv(merged_path, fields, sorted(by_key.values(), key=lambda row: (-int(row.get("triage_score", "0") or "0"), row.get("module_primary", ""), row.get("pmid", ""))))
    write_tsv(args.input_dir / "agent_review_application.tsv", ["agent_file", "module_primary", "candidate_key", "pmid", "disposition"], agent_rows)
    by_module = Counter(row["module_primary"] for row in agent_rows)
    by_decision = Counter(row["disposition"] for row in agent_rows)
    summary_rows = []
    for path in agent_paths:
        rows = [row for row in agent_rows if row["agent_file"] == str(path.relative_to(ROOT))]
        summary_rows.append({
            "agent_file": str(path.relative_to(ROOT)), "rows": str(len(rows)),
            "modules": ";".join(sorted({row["module_primary"] for row in rows})),
            "dispositions": ";".join(f"{key}={value}" for key, value in sorted(Counter(row["disposition"] for row in rows).items())),
        })
    write_tsv(args.input_dir / "agent_review_summary.tsv", ["agent_file", "rows", "modules", "dispositions"], summary_rows)
    manifest = {
        "agent_files": len(agent_paths), "agent_rows_seen": sum(int(row["rows"]) for row in summary_rows),
        "agent_rows_applied": applied, "by_module": dict(sorted(by_module.items())),
        "by_disposition": dict(sorted(by_decision.items())), "errors": errors,
        "abstract_level_only": True, "canonical_write_performed": False,
    }
    (args.input_dir / "agent_review_merge_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
