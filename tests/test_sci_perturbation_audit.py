from __future__ import annotations

import json
from pathlib import Path

from scripts.audit_sci_perturbation_context import build


ROOT = Path(__file__).parents[1]
PACK = ROOT / "context_packs" / "spinal_cord_injury"


def test_perturbation_audit_is_reproducible_and_does_not_change_pack_tables(tmp_path):
    summary = build(PACK, tmp_path)

    assert summary["audit_version"] == "sci_perturbation_design_audit_v1"
    assert summary["pack_counts"] == {
        "evidence_context_profiles": 683,
        "observations": 910,
        "mechanism_links": 910,
        "contexts_with_perturbation_or_design_text": 651,
        "observations_with_perturbation_text": 828,
    }
    assert sum(summary["classification_counts"]["contexts"].values()) == 683
    assert sum(summary["classification_counts"]["observations"].values()) == 910
    assert summary["interpretation"]["is_a_separate_perturbation_response_layer_needed_now"] is False
    assert summary["interpretation"]["is_normalized_perturbation_design_audit_useful"] is True
    assert (tmp_path / "perturbation_design_audit.tsv").is_file()
    assert (tmp_path / "perturbation_design_audit.json").is_file()

    written = json.loads((tmp_path / "perturbation_design_audit.json").read_text())
    assert written["input_artifacts"][0]["path"] == "context_packs/spinal_cord_injury/contexts.tsv"


def test_audit_preserves_exact_source_text_and_marks_links_separately(tmp_path):
    build(PACK, tmp_path)
    rows = (tmp_path / "perturbation_design_audit.tsv").read_text().splitlines()
    header = rows[0].split("\t")
    assert "perturbation_source_text" in header
    assert "source_locators" in header
    assert "link_statuses" in header
    assert "audit_decision" in header
    assert all("retain_existing_evidence_only" in row for row in rows[1:])
