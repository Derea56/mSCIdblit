from __future__ import annotations

import csv
import json
from pathlib import Path

from scripts.audit_sci_module_spatial_reconciliation import build


ROOT = Path(__file__).parents[1]
PACK = ROOT / "context_packs" / "spinal_cord_injury"
MODULE_LEDGER = ROOT / "work/cross_module_synthesis/canonical_evidence_review/module20_24_integrated_phase2_extractions.tsv"


def test_module_spatial_reconciliation_is_source_preserving(tmp_path):
    summary = build(PACK, MODULE_LEDGER, PACK / "spatial_localization_audit.tsv", tmp_path)

    assert summary["audit_version"] == "sci_module_spatial_reconciliation_v1"
    assert summary["candidate_counts"]["module_rows_with_explicit_context"] > 0
    assert summary["candidate_counts"]["source_resolved_context_rows"] > 0
    assert summary["candidate_counts"]["review_required_exclusion_rows"] > 0
    assert summary["candidate_counts"]["unique_module_evidence_groups"] > 0
    assert summary["reconciliation_counts"]["candidate_rows_matching_existing_context_pack_observations"] > 0
    assert summary["reconciliation_counts"]["candidate_rows_module_only"] > 0
    assert (tmp_path / "sci_module_spatial_reconciliation.tsv").is_file()
    assert (tmp_path / "sci_module_spatial_reconciliation.json").is_file()

    rows = list(csv.DictReader((tmp_path / "sci_module_spatial_reconciliation.tsv").open(), delimiter="\t"))
    ry = next(row for row in rows if row["b_evidence_id"] == "M21B-EVID-000017" and "PMC5518483" in row["canonical_paper_key"])
    assert ry["source_context_class"] == "explicit_sci_injury_context"
    assert ry["promotion_state"] == "audit_only_not_promoted"
    assert ry["module_dependency_group"] == "M21B-EVID-000017"
    assert ry["source_identifier_keys"]

    il1r2 = next(row for row in rows if row["b_evidence_id"] == "M21B-EVID-000025")
    assert il1r2["source_context_class"] == "explicit_context_with_exclusion_language"


def test_module_spatial_reconciliation_records_exact_inputs(tmp_path):
    build(PACK, MODULE_LEDGER, PACK / "spatial_localization_audit.tsv", tmp_path)
    report = json.loads((tmp_path / "sci_module_spatial_reconciliation.json").read_text())
    assert [item["path"] for item in report["input_artifacts"]] == [
        "work/cross_module_synthesis/canonical_evidence_review/module20_24_integrated_phase2_extractions.tsv",
        "context_packs/spinal_cord_injury/contexts.tsv",
        "context_packs/spinal_cord_injury/observations.tsv",
        "context_packs/spinal_cord_injury/spatial_localization_audit.tsv",
    ]
