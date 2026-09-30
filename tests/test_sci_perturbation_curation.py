from __future__ import annotations

import csv
from pathlib import Path

from scripts.build_sci_perturbation_curation import build


ROOT = Path(__file__).parents[1]
PACK = ROOT / "context_packs" / "spinal_cord_injury"


def test_staged_perturbation_curation_is_source_preserving(tmp_path):
    output = tmp_path / "perturbation_design_curation.tsv"
    summary = build(PACK / "perturbation_design_audit.tsv", output)

    assert summary["rows"] == 410
    assert summary["normalization_status"] == "staged_not_promoted"
    rows = list(csv.DictReader(output.open(), delimiter="\t"))
    row = next(item for item in rows if item["study_id"] == "FLOW_SCI_020")
    assert row["intervention_class"] == "pharmacologic_or_ligand_intervention"
    assert row["comparator_class"] == "comparator_present_in_source_design_text"
    assert row["normalization_status"] == "staged_not_promoted"
    assert row["review_required"] == "true"
    assert "DB1976 intrathecal PU.1 inhibitor" in row["treatment_source_text"]
    assert row["timepoint_value"] == "28"
    assert row["timepoint_unit"] == "d"
    assert row["source_locators"].startswith("flow_protein.protein_observations.observation_id=")
    assert "target, route, dose" in row["normalization_note"]


def test_curation_ledger_does_not_change_release_tables(tmp_path):
    contexts_before = (PACK / "contexts.tsv").read_bytes()
    observations_before = (PACK / "observations.tsv").read_bytes()
    links_before = (PACK / "mechanism_links.tsv").read_bytes()

    build(PACK / "perturbation_design_audit.tsv", tmp_path / "curation.tsv")

    assert (PACK / "contexts.tsv").read_bytes() == contexts_before
    assert (PACK / "observations.tsv").read_bytes() == observations_before
    assert (PACK / "mechanism_links.tsv").read_bytes() == links_before
