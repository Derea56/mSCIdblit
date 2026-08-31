#!/usr/bin/env python3
"""Audit staged Module 20–24 database intake and cross-module paper reuse."""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
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


def git_frozen_diff() -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--name-only", "eeb9960", "--",
         "data/processed/mechanism_bundle_module20_24_db_v1_0_0",
         "data/processed/mechanism_graph_module20_24_v2026_08_25"],
        cwd=ROOT, check=False, capture_output=True, text=True,
    )
    return [line for line in result.stdout.splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_DIR)
    args = parser.parse_args()
    leads = read_tsv(args.input_dir / "database_candidate_leads.tsv")
    literature = read_tsv(args.input_dir / "database_literature_leads.tsv")
    review = read_tsv(args.input_dir / "database_literature_review_queue.tsv")
    registry = read_tsv(args.input_dir / "database_source_registry_audit.tsv")
    merged_path = args.input_dir / "database_evidence_decisions_merged.tsv"
    staging_path = args.input_dir / "agent_evidence_staging.tsv"
    merged = read_tsv(merged_path) if merged_path.exists() else []
    agent_staging = read_tsv(staging_path) if staging_path.exists() else []
    manual_claim_path = args.input_dir / "manual_cross_module_evidence.tsv"
    manual_record_path = args.input_dir / "manual_cross_module_pubmed_records.tsv"
    manual_claims = read_tsv(manual_claim_path) if manual_claim_path.exists() else []
    manual_records = read_tsv(manual_record_path) if manual_record_path.exists() else []
    corroboration_path = args.input_dir / "manual_corroboration_evidence.tsv"
    corroboration_record_path = args.input_dir / "manual_corroboration_pubmed_records.tsv"
    corroboration_rows = read_tsv(corroboration_path) if corroboration_path.exists() else []
    corroboration_records = read_tsv(corroboration_record_path) if corroboration_record_path.exists() else []
    agent_record_path = args.input_dir / "agent_corroboration_pubmed_records.tsv"
    agent_records = read_tsv(agent_record_path) if agent_record_path.exists() else []
    agent_corroboration_path = args.input_dir / "corroboration_agent_decisions.tsv"
    reconciliation_path = args.input_dir / "corroboration_reconciliation.tsv"
    adjudication_path = args.input_dir / "module20_24_corroboration_adjudication.tsv"
    agent_corroboration = read_tsv(agent_corroboration_path) if agent_corroboration_path.exists() else []
    reconciliations = read_tsv(reconciliation_path) if reconciliation_path.exists() else []
    adjudications = read_tsv(adjudication_path) if adjudication_path.exists() else []
    errors: list[str] = []
    valid_a = {"20A", "21A", "23A", "24A"}
    if any(row.get("module_primary") not in valid_a for row in leads):
        errors.append("candidate lead has an unsupported primary module")
    if any(row.get("module_consolidation") != row.get("module_primary", "").replace("A", "B") for row in leads):
        errors.append("candidate lead has mismatched A/B consolidation module")
    lead_ids = [row.get("lead_id", "") for row in leads]
    if len(lead_ids) != len(set(lead_ids)):
        errors.append("candidate lead IDs are not unique")
    candidate_pmids = {pmid for row in leads for pmid in (row.get("linked_pmids", "") or "").split(";") if pmid}
    literature_pmids = {row.get("pmid", "") for row in literature if row.get("pmid")}
    if not literature_pmids.issubset(candidate_pmids):
        errors.append("literature packet contains PMID not present in candidate leads")
    if any(not row.get("source_path") for row in leads):
        errors.append("candidate lead is missing source_path")
    imported_missing = [row["database_id"] for row in registry if row.get("intake_status") == "imported" and row.get("exists") != "true"]
    if imported_missing:
        errors.append("imported registry source is missing: " + ",".join(imported_missing))
    if merged and not {row.get("candidate_key", "") for row in merged}.issubset({row.get("candidate_key", "") for row in review}):
        errors.append("merged evidence decision contains candidate not present in review queue")
    if any(row.get("canonical_eligible") != "false" for row in agent_staging):
        errors.append("agent staging row is marked canonical-eligible")
    if len({row.get("staged_evidence_id", "") for row in agent_staging}) != len(agent_staging):
        errors.append("agent staging IDs are not unique")
    allowed_routes = {"17A", "20A", "21A", "22A", "23A", "24A"}
    for row in agent_staging:
        if any(route not in allowed_routes for route in filter(None, row.get("routed_modules", "").split(";"))):
            errors.append("agent staging row has unsupported routed module")
            break
    manual_pmids = {pmid for row in manual_claims for pmid in (row.get("primary_pmid", "") + ";" + row.get("corroborating_pmids", "")).split(";") if pmid}
    retrieved_manual_pmids = {row.get("pmid", "") for row in manual_records if row.get("retrieval_status") == "retrieved"}
    if not manual_pmids.issubset(retrieved_manual_pmids):
        errors.append("manual cross-module claim has a PMID without a retrieved PubMed record")
    if any(row.get("canonical_eligible") != "false" for row in manual_claims):
        errors.append("manual cross-module claim is marked canonical-eligible")
    required_corroboration_fields = {
        "corroboration_id", "primary_candidate_key", "module_primary", "routed_modules",
        "primary_pmid", "corroborating_pmid", "corroboration_scope", "corroboration_status",
        "evidence_summary", "limitations", "primary_source_url", "corroborating_source_url",
    }
    if corroboration_rows and not required_corroboration_fields.issubset(corroboration_rows[0]):
        errors.append("manual corroboration evidence is missing required fields")
    corroboration_ids = [row.get("corroboration_id", "") for row in corroboration_rows]
    if len(corroboration_ids) != len(set(corroboration_ids)):
        errors.append("manual corroboration IDs are not unique")
    corroboration_pmids = {
        pmid for row in corroboration_rows
        for pmid in (row.get("primary_pmid", "") + ";" + row.get("corroborating_pmid", "")).split(";")
        if pmid
    }
    retrieved_corroboration_pmids = {
        row.get("pmid", "") for row in corroboration_records
        if row.get("retrieval_status") == "retrieved"
    }
    if not corroboration_pmids.issubset(retrieved_corroboration_pmids):
        errors.append("manual corroboration row has a PMID without a retrieved PubMed record")
    if any(
        any(route not in allowed_routes for route in filter(None, row.get("routed_modules", "").split(";")))
        for row in corroboration_rows
    ):
        errors.append("manual corroboration row has unsupported routed module")
    known_staged_ids = {row.get("staged_evidence_id", "") for row in agent_staging}
    for row in agent_corroboration + reconciliations:
        if row.get("staged_evidence_id", "") not in known_staged_ids:
            errors.append("corroboration decision targets unknown staged evidence ID")
            break
        if row.get("canonical_eligible") != "false":
            errors.append("corroboration decision is marked canonical-eligible")
            break
        if any(route not in allowed_routes for route in filter(None, row.get("routed_modules", "").split(";"))):
            errors.append("corroboration decision has unsupported routed module")
            break
    corroboration_decision_pmids = {
        pmid for row in agent_corroboration + reconciliations
        for pmid in (row.get("primary_pmid", "") + ";" + row.get("corroborating_pmid", "")).split(";")
        if pmid
    }
    retrieved_agent_pmids = {
        row.get("pmid", "") for row in agent_records
        if row.get("retrieval_status") == "retrieved"
    }
    if not corroboration_decision_pmids.issubset(
        literature_pmids | retrieved_manual_pmids | retrieved_corroboration_pmids | retrieved_agent_pmids
    ):
        errors.append("corroboration decision has a PMID absent from retrieved local records")
    adjudication_ids = [row.get("adjudication_id", "") for row in adjudications]
    if len(adjudication_ids) != len(set(adjudication_ids)):
        errors.append("consolidated corroboration adjudication IDs are not unique")
    for row in adjudications:
        staged_id = row.get("staged_evidence_id", "")
        if staged_id and staged_id not in known_staged_ids:
            errors.append("consolidated corroboration adjudication targets unknown staged evidence ID")
            break
        if row.get("canonical_eligible") != "false":
            errors.append("consolidated corroboration adjudication is marked canonical-eligible")
            break

    # Paper reuse across modules must be independently corroborated before any
    # one paper is used as support for multiple module-specific claims.
    paper_modules: dict[str, set[str]] = defaultdict(set)
    paper_rows: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in literature:
        pmid = row.get("pmid", "")
        if pmid:
            paper_modules[pmid].add(row.get("module_primary", ""))
            paper_rows[pmid].append(row)
    reuse_rows: list[dict[str, str]] = []
    for pmid, modules in sorted(paper_modules.items(), key=lambda item: int(item[0])):
        if len(modules) < 2:
            continue
        rows = paper_rows[pmid]
        reuse_rows.append({
            "pmid": pmid,
            "modules": ";".join(sorted(modules)),
            "module_count": str(len(modules)),
            "titles": " | ".join(sorted({row.get("title", "") for row in rows if row.get("title")})),
            "database_ids": ";".join(sorted({row.get("database_id", "") for row in rows if row.get("database_id")})),
            "entity_pairs": " | ".join(sorted({f"{row.get('entity_a','')}->{row.get('entity_b','')}" for row in rows})),
            "independent_corroboration_required": "true",
            "review_state": "queued_for_second_source_before_cross_module_promotion",
            "notes": "The same paper may be relevant to multiple items, but each module claim requires separate exact-fit review and an independent corroborating source where feasible.",
        })
    write_tsv(
        args.input_dir / "cross_module_paper_corroboration_queue.tsv",
        ["pmid", "modules", "module_count", "titles", "database_ids", "entity_pairs", "independent_corroboration_required", "review_state", "notes"],
        reuse_rows,
    )

    by_module = Counter(row.get("module_primary", "") for row in leads)
    literature_by_module = Counter(row.get("module_primary", "") for row in literature)
    review_by_module = Counter(row.get("module_primary", "") for row in review)
    module_rows = []
    for module in ("20A", "20B", "21A", "21B", "22A", "22B", "23A", "23B", "24A", "24B"):
        if module.endswith("A") and module != "22A":
            candidate = by_module[module]
            lit = literature_by_module[module]
            review_count = review_by_module[module]
            status = "assembled" if candidate else "no_imported_leads"
        elif module == "22A":
            candidate = 0
            lit = 0
            review_count = 0
            status = "already_processed_public_tf_union"
        else:
            parent = module.replace("B", "A")
            candidate = by_module[parent]
            lit = literature_by_module[parent]
            review_count = review_by_module[parent]
            status = "consolidation_queue_ready" if candidate else "awaiting_A_layer"
        module_rows.append({
            "module": module,
            "database_candidate_leads": str(candidate),
            "literature_leads": str(lit),
            "deduplicated_review_candidates": str(review_count),
            "status": status,
        })
    write_tsv(args.input_dir / "module_20_24_database_intake_coverage.tsv", list(module_rows[0]), module_rows)

    frozen_diff = git_frozen_diff()
    if frozen_diff:
        errors.append("frozen graph/database paths changed relative to eeb9960")
    manifest = {
        "candidate_leads": len(leads),
        "literature_leads": len(literature),
        "review_candidates": len(review),
        "merged_decisions": len(merged),
        "agent_staging_rows": len(agent_staging),
        "manual_cross_module_claims": len(manual_claims),
        "manual_cross_module_pubmed_records": len(manual_records),
        "manual_corroboration_rows": len(corroboration_rows),
        "manual_corroboration_pubmed_records": len(corroboration_records),
        "agent_corroboration_pubmed_records": len(agent_records),
        "corroboration_agent_decisions": len(agent_corroboration),
        "corroboration_reconciliation_rows": len(reconciliations),
        "corroboration_adjudication_rows": len(adjudications),
        "cross_module_pmids_requiring_corroboration": len(reuse_rows),
        "imported_registry_sources": sum(row.get("exists") == "true" for row in registry),
        "planned_registry_sources": sum(row.get("exists") != "true" for row in registry),
        "frozen_graph_database_diff": frozen_diff,
        "errors": errors,
        "status": "pass" if not errors else "fail",
        "canonical_write_performed": False,
    }
    (args.input_dir / "database_intake_audit_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
