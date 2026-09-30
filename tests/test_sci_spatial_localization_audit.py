from __future__ import annotations

import csv
import json
from pathlib import Path

from scripts.audit_sci_spatial_localization import build


ROOT = Path(__file__).parents[1]
PACK = ROOT / "context_packs" / "spinal_cord_injury"


def test_spatial_localization_audit_is_source_preserving(tmp_path):
    summary = build(PACK, tmp_path)

    assert summary["audit_version"] == "sci_spatial_localization_audit_v1"
    assert summary["candidate_counts"] == {
        "if_ihc_or_immunostain_observations": 378,
        "spatial_transcriptomic_dataset_contexts": 19,
        "all_candidates": 397,
    }
    assert summary["class_counts"]["same_cell_colocalization"] == 95
    assert summary["secondary_class_counts"]["structural_density_or_area"] > 0
    assert summary["value_state_counts"]["numeric_value_present"] == 130
    assert summary["value_state_counts"]["qualitative_or_reported_text_present"] == 247
    assert summary["value_state_counts"]["not_measured_or_not_reported"] == 20
    assert "perturbation" in summary["counts_by"]
    assert "unresolved_mapping_reason" in summary["counts_by"]
    assert (tmp_path / "spatial_localization_audit.tsv").is_file()
    assert (tmp_path / "spatial_localization_audit.json").is_file()

    rows = list(csv.DictReader((tmp_path / "spatial_localization_audit.tsv").open(), delimiter="\t"))
    ripk3 = next(row for row in rows if row["observation_id"] == "FLOW_SCI_300__OBS300_RIPK3_NEURON_24H")
    assert ripk3["primary_spatial_class"] == "same_cell_colocalization"
    assert ripk3["value_numeric"] == "78.2"
    assert ripk3["source_artifact_sha256"] == "db992d208fd37ed1483ff711ad05dc45ebf8254638f54b0a752d374c219e2aaf"
    assert ripk3["promotion_state"] == "audit_only_not_promoted"
    assert ripk3["link_status"] in {"linked_included", "linked_staging_unresolved"}

    spatial = next(row for row in rows if row["observation_id"] == "TRANSCRIPTOMIC_CONTEXT:MSCIDATA000008:MSCIDATA000008:A:3dpi")
    assert spatial["primary_spatial_class"] == "spatial_transcriptomic_dataset_context"
    assert spatial["promotion_state"] == "audit_only_not_promoted"


def test_spatial_localization_audit_inputs_are_recorded(tmp_path):
    build(PACK, tmp_path)
    report = json.loads((tmp_path / "spatial_localization_audit.json").read_text())
    assert [item["path"] for item in report["input_artifacts"]] == [
        "context_packs/spinal_cord_injury/contexts.tsv",
        "context_packs/spinal_cord_injury/observations.tsv",
        "context_packs/spinal_cord_injury/mechanism_links.tsv",
    ]
    assert report["interpretation"]["image_reanalysis_status"].startswith("No raw-image")
