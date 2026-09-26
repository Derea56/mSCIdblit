from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

from scripts.validate_context_pack import validate_pack


ROOT = Path(__file__).parents[1]
PACK = ROOT / "context_packs" / "spinal_cord_injury"


def _header(path: Path) -> list[str]:
    with path.open(newline="") as handle:
        return next(csv.reader(handle, delimiter="\t"))


def test_sci_context_manifest_pins_neutral_mechanism_release():
    manifest = json.loads((PACK / "context_manifest.json").read_text())

    assert manifest["context_pack_id"] == "spinal_cord_injury"
    assert manifest["status"] == "populated"
    assert manifest["mechanism_dependency"]["generic_graph_is_unchanged"] is True
    assert manifest["mechanism_dependency"]["context_links_are_not_graph_edges"] is True
    assert manifest["evidence_policy"]["route_confidence_stored"] is False
    assert manifest["evidence_policy"]["numeric_modality_weights_stored"] is False
    bundle_path = PACK / manifest["mechanism_dependency"]["bundle_metadata"]
    assert bundle_path.resolve().is_file()
    assert manifest["counts"]["context_profiles"] > 1
    assert manifest["context_pack_version"] == "0.5.0"
    assert manifest["counts"]["observations"] == 741
    assert manifest["counts"]["mechanism_links"] == 741
    assert 0 < manifest["counts"]["included_mechanism_links"] < manifest["counts"]["mechanism_links"]


def test_sci_context_tables_have_stable_contract_headers():
    contexts = _header(PACK / "contexts.tsv")
    observations = _header(PACK / "observations.tsv")
    links = _header(PACK / "mechanism_links.tsv")

    assert contexts[:4] == [
        "context_id",
        "context_name",
        "context_kind",
        "disease_context",
    ]
    assert observations[:8] == [
        "observation_id",
        "context_id",
        "source_system",
        "source_database",
        "source_record_type",
        "source_record_key",
        "source_version",
        "modality",
    ]
    assert links[:8] == [
        "link_id",
        "observation_id",
        "mechanism_release_id",
        "mechanism_target_kind",
        "mechanism_target_key",
        "mechanism_route_id",
        "route_stage",
        "link_role",
    ]


def test_sci_context_profiles_preserve_scope_and_reported_study_fields():
    rows = list(csv.DictReader((PACK / "contexts.tsv").open(), delimiter="\t"))

    assert len(rows) > 1
    assert rows[0]["context_kind"] == "ontology_scope"
    assert rows[0]["context_status"] == "defined"
    assert rows[0]["sample_id"] == ""
    assert rows[0]["study_id"] == ""
    assert rows[0]["tissue"] == ""
    for row in rows[1:]:
        assert row["study_id"]
        assert row["tissue"]
        assert row["disease_context"] == "spinal_cord_injury"
        assert row["anatomical_context"] == "spinal_cord"


def test_sci_protein_context_curation_overrides_are_applied_with_source_provenance():
    overrides = list(csv.DictReader((PACK / "protein_context_curation_overrides.tsv").open(), delimiter="\t"))
    assert len(overrides) == 8
    assert all(row["curation_status"] == "applied" for row in overrides)
    assert all(row["source_locator"] and row["source_url"] for row in overrides)

    contexts = list(csv.DictReader((PACK / "contexts.tsv").open(), delimiter="\t"))
    by_study = {}
    for study_id in {row["study_id"] for row in overrides}:
        by_study[study_id] = [row for row in contexts if row["study_id"] == study_id]
        assert by_study[study_id]
    assert {row["injury_level"] for row in by_study["FLOW_MSCS_ITDB_000006"]} == {"T9"}
    assert {row["injury_severity"] for row in by_study["FLOW_MSCS_ITDB_000006"]} == {"75 kdyne contusion"}
    assert {row["injury_level"] for row in by_study["FLOW_MSCS_ITDB_000010"]} == {"T9"}
    assert {row["injury_severity"] for row in by_study["FLOW_MSCS_ITDB_000010"]} == {"60 kdyn moderate contusion"}
    assert {row["injury_level"] for row in by_study["FLOW_MSCS_ITDB_000005"]} == {"C5"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_414"]} == {"T9"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_414"]} == {"60 kdyn contusion"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_024"]} == {"T10"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_024"]} == {"150 kdyn mild-to-moderate contusion"}
    assert {row["sample_scope"] for row in by_study["FLOW_SCI_024"]} == {"5-mm lesion-epicenter soluble spinal-cord fraction"}
    ev_contexts = [row for row in contexts if row["study_id"] == "FLOW_SCI_471"]
    assert {row["sample_scope"] for row in ev_contexts} == {
        "plasma EV and T10 lesion-centered spinal-cord samples",
        "plasma extracellular-vesicle fraction",
    }
    observations = list(csv.DictReader((PACK / "observations.tsv").open(), delimiter="\t"))
    curated = [row for row in observations if row["context_id"] in {context["context_id"] for context in contexts if context["study_id"] in by_study}]
    assert curated
    assert all("context_curation" in json.loads(row["provenance_note"]) for row in curated)


def test_sci_context_pack_validator_accepts_populated_release():
    summary = validate_pack(PACK)

    assert summary["pack_id"] == "spinal_cord_injury"
    assert summary["counts"]["observations"] == 741
    assert summary["counts"]["mechanism_links"] == 741


def test_sci_observations_and_links_preserve_evidence_boundaries():
    observations = list(csv.DictReader((PACK / "observations.tsv").open(), delimiter="\t"))
    links = list(csv.DictReader((PACK / "mechanism_links.tsv").open(), delimiter="\t"))
    assert Counter(row["modality"] for row in observations) == {"protein": 724, "epigenomics": 17}
    assert Counter(row["evidence_role"] for row in observations) == {"dataset_observation": 741}
    assert all(row["dependency_group"] for row in observations)
    assert all(row["mechanism_release_id"] == "module20_24_mechanism_graph:2026-09-25-literature-expansion-627" for row in links)
    assert all(row["mechanism_target_kind"] == "node" for row in links if row["release_status"] == "included")
    assert all(row["mechanism_target_key"] == "21B" for row in links if row["release_status"] == "staging")
    assert all(row["mechanism_route_id"] == "" for row in links)


def test_sci_protein_context_gap_audit_is_reproducible_and_separate_from_evidence():
    audit = json.loads((PACK / "protein_context_gap_audit.json").read_text())
    assert (PACK / "protein_context_coverage.tsv").is_file()
    assert (PACK / "protein_context_gap_candidates.tsv").is_file()
    assert audit["pack_inputs"]["protein_observations"] == 724
    assert audit["pack_inputs"]["protein_expression_observations"] == 614
    assert audit["canonical_store"]["protein_observations"] == 1259
    assert audit["canonical_store"]["remaining_gap_records"] == 535
    assert audit["policy"].startswith("This audit prioritizes metadata refinement only")
