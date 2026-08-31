#!/usr/bin/env python3
"""Consolidate manual and agent corroboration decisions into one staging index."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INTAKE = ROOT / "data/processed/module20_24_database_intake_v1"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


FIELDS = [
    "adjudication_id", "source_type", "source_reviewer", "staged_evidence_id",
    "candidate_key", "module_primary", "routed_modules", "primary_pmid",
    "corroborating_pmid", "corroboration_scope", "exactness", "corroboration_status",
    "module_fit", "evidence_summary", "limitations", "canonical_eligible",
    "source_url_primary", "source_url_corroborating",
]


def main() -> int:
    output: list[dict[str, str]] = []
    agent_rows = read_tsv(INTAKE / "corroboration_agent_decisions.tsv")
    for row in agent_rows:
        output.append({
            "adjudication_id": row.get("review_id", ""),
            "source_type": "agent_packet_best_pairing",
            "source_reviewer": row.get("review_agent", ""),
            "staged_evidence_id": row.get("staged_evidence_id", ""),
            "candidate_key": row.get("candidate_key", ""),
            "module_primary": row.get("module_primary", ""),
            "routed_modules": row.get("routed_modules", ""),
            "primary_pmid": row.get("primary_pmid", ""),
            "corroborating_pmid": row.get("corroborating_pmid", ""),
            "corroboration_scope": "agent_selected_best_packet_pairing",
            "exactness": row.get("exactness", ""),
            "corroboration_status": row.get("corroboration_status", ""),
            "module_fit": row.get("module_fit", ""),
            "evidence_summary": row.get("evidence_summary", ""),
            "limitations": row.get("limitations", ""),
            "canonical_eligible": "false",
            "source_url_primary": f"https://pubmed.ncbi.nlm.nih.gov/{row.get('primary_pmid', '')}/",
            "source_url_corroborating": f"https://pubmed.ncbi.nlm.nih.gov/{row.get('corroborating_pmid', '')}/",
        })

    reconciliation_rows = read_tsv(INTAKE / "corroboration_reconciliation.tsv")
    for row in reconciliation_rows:
        output.append({
            "adjudication_id": row.get("reconciliation_id", ""),
            "source_type": "local_parser_correction_reconciliation",
            "source_reviewer": "local",
            "staged_evidence_id": row.get("staged_evidence_id", ""),
            "candidate_key": row.get("candidate_key", ""),
            "module_primary": row.get("module_primary", ""),
            "routed_modules": row.get("routed_modules", ""),
            "primary_pmid": row.get("primary_pmid", ""),
            "corroborating_pmid": row.get("corroborating_pmid", ""),
            "corroboration_scope": "url_decode_reconciliation",
            "exactness": row.get("exactness", ""),
            "corroboration_status": row.get("corroboration_status", ""),
            "module_fit": "local_reconciliation",
            "evidence_summary": row.get("evidence_summary", ""),
            "limitations": row.get("limitations", ""),
            "canonical_eligible": "false",
            "source_url_primary": f"https://pubmed.ncbi.nlm.nih.gov/{row.get('primary_pmid', '')}/",
            "source_url_corroborating": f"https://pubmed.ncbi.nlm.nih.gov/{row.get('corroborating_pmid', '')}/",
        })

    manual_rows = read_tsv(INTAKE / "manual_corroboration_evidence.tsv")
    for row in manual_rows:
        output.append({
            "adjudication_id": row.get("corroboration_id", ""),
            "source_type": "manual_corroboration",
            "source_reviewer": "local",
            "staged_evidence_id": "",
            "candidate_key": row.get("primary_candidate_key", ""),
            "module_primary": row.get("module_primary", ""),
            "routed_modules": row.get("routed_modules", ""),
            "primary_pmid": row.get("primary_pmid", ""),
            "corroborating_pmid": row.get("corroborating_pmid", ""),
            "corroboration_scope": row.get("corroboration_scope", ""),
            "exactness": "exact" if row.get("corroboration_status") == "corroborated" else row.get("corroboration_status", ""),
            "corroboration_status": row.get("corroboration_status", ""),
            "module_fit": row.get("routed_modules", ""),
            "evidence_summary": row.get("evidence_summary", ""),
            "limitations": row.get("limitations", ""),
            "canonical_eligible": "false",
            "source_url_primary": row.get("primary_source_url", ""),
            "source_url_corroborating": row.get("corroborating_source_url", ""),
        })

    output.sort(key=lambda row: (row["module_primary"], row["staged_evidence_id"], row["adjudication_id"]))
    out_path = INTAKE / "module20_24_corroboration_adjudication.tsv"
    write_tsv(out_path, FIELDS, output)
    manifest = {
        "agent_rows": len(agent_rows),
        "reconciliation_rows": len(reconciliation_rows),
        "manual_rows": len(manual_rows),
        "adjudication_rows": len(output),
        "canonical_write_performed": False,
    }
    (INTAKE / "module20_24_corroboration_adjudication.manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
