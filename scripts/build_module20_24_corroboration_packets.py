#!/usr/bin/env python3
"""Build local primary/secondary abstract packets for staged corroboration review."""

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


def main() -> int:
    status_rows = read_tsv(INTAKE / "agent_review_corroboration_status.tsv")
    literature_rows = read_tsv(INTAKE / "database_literature_leads.tsv")
    by_pmid: dict[str, dict[str, str]] = {}
    for row in literature_rows:
        pmid = row.get("pmid", "")
        if pmid and pmid not in by_pmid:
            by_pmid[pmid] = row

    fields = [
        "staged_evidence_id", "candidate_key", "module_primary", "routed_modules",
        "entity_a", "entity_b", "primary_pmid", "corroborating_pmid",
        "primary_title", "primary_abstract", "corroborating_title",
        "corroborating_abstract", "primary_source_databases",
        "corroborating_source_databases", "packet_status",
    ]
    output: list[dict[str, str]] = []
    missing = 0
    for row in status_rows:
        pmids = [pmid for pmid in row.get("available_corrobating_pmids", "").split(";") if pmid]
        for secondary in pmids:
            primary = by_pmid.get(row.get("primary_pmid", ""), {})
            corroborating = by_pmid.get(secondary, {})
            if not primary or not corroborating:
                missing += 1
            output.append({
                "staged_evidence_id": row.get("staged_evidence_id", ""),
                "candidate_key": row.get("candidate_key", ""),
                "module_primary": row.get("module_primary", ""),
                "routed_modules": row.get("routed_modules", ""),
                "entity_a": row.get("entity_a", ""),
                "entity_b": row.get("entity_b", ""),
                "primary_pmid": row.get("primary_pmid", ""),
                "corroborating_pmid": secondary,
                "primary_title": primary.get("title", ""),
                "primary_abstract": primary.get("abstract", ""),
                "corroborating_title": corroborating.get("title", ""),
                "corroborating_abstract": corroborating.get("abstract", ""),
                "primary_source_databases": primary.get("source_databases", ""),
                "corroborating_source_databases": corroborating.get("source_databases", ""),
                "packet_status": "ready" if primary and corroborating else "missing_local_record",
            })
    output.sort(key=lambda row: (row["module_primary"], row["candidate_key"], row["corroborating_pmid"]))
    out_path = INTAKE / "agent_review_corroboration_packets.tsv"
    write_tsv(out_path, fields, output)
    manifest = {
        "status_rows": len(status_rows),
        "packet_rows": len(output),
        "status_rows_with_packets": len({row["staged_evidence_id"] for row in output}),
        "missing_local_records": missing,
        "canonical_write_performed": False,
    }
    (INTAKE / "agent_review_corroboration_packets.manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
