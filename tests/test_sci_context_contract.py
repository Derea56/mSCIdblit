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
    assert manifest["context_pack_version"] == "0.5.8"
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
    assert len(overrides) == 36
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
    assert {row["sex"] for row in by_study["FLOW_SCI_024"]} == {"young adult female Long-Evans rats, approximately 200 g"}
    assert {row["sample_scope"] for row in by_study["FLOW_SCI_024"]} == {"5-mm lesion-epicenter soluble spinal-cord fraction"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_052"]} == {"T11"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_052"]} == {"50 kdyn contusion; 400-500 micrometre tissue displacement"}
    assert {row["sex"] for row in by_study["FLOW_SCI_052"]} == {"adult female C57BL/6J mice"}
    assert {row["injury_level"] for row in by_study["FLOW_MSCS_ITDB_000071"]} == {"T10"}
    assert {row["injury_severity"] for row in by_study["FLOW_MSCS_ITDB_000071"]} == {"full crush for 2 seconds with forceps; forceps width 0.1 mm in the last 5 mm of the tips"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_135"]} == {"0.5 mm displacement contusion at 1.0 m/s"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_071"]} == {"L1/L2"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_071"]} == {"0.4 mm residual closure; 10-second bilateral lateral compression"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_080"]} == {"2,000 dynes moderate contusion"}
    assert {row["sex"] for row in by_study["FLOW_SCI_080"]} == {"adult female mice, 3-4 months, 20-24 g"}
    assert {row["sex"] for row in by_study["FLOW_SCI_204"]} == {"8-10-week-old female C57BL/6 mice, 20-25 g"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_111"]} == {"0.2 mm lateral-compression depth for 20 seconds"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_216"]} == {"T9"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_216"]} == {"30-g vascular clip compression for 10 seconds"}
    assert {row["sample_scope"] for row in by_study["FLOW_SCI_413"]} == {"ependymal layer/central canal; proliferating cells quantified 0.1-0.2 mm from the lesion"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_529"]} == {"1.85 g weight dropped from 20 mm onto an impounder"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_390"]} == {"T10"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_390"]} == {"0.5 mm forceps-tip width; bilateral lateral compression for 5 seconds"}
    assert {row["sex"] for row in by_study["FLOW_SCI_390"]} == {"female C57BL/6J mice, 6-8 weeks"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_001"]} == {"T12"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_001"]} == {"200 kdyn centralized contusion without complete penetration"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_012"]} == {"T10"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_012"]} == {"5-g rod dropped from 15 mm; exact functional severity not reported in the cited methods"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_094"]} == {"L1/L2"}
    assert {row["sex"] for row in by_study["FLOW_SCI_094"]} == {"female C57BL/6 mice, 3-5 months, 30-35 g"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_253"]} == {"T10"}
    assert {row["sample_scope"] for row in by_study["FLOW_SCI_253"]} == {"3-mm spinal-cord blocks centered on, rostral to, and caudal to the lesion"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_470"]} == {"T9"}
    assert {row["sex"] for row in by_study["FLOW_SCI_470"]} == {"female C57BL/6J mice, 7-8 weeks, 17-22 g"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_434"]} == {"T12"}
    assert {row["sex"] for row in by_study["FLOW_SCI_434"]} == {"female C57BL/6 mice, 6-8 weeks, 18-22 g"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_352"]} == {"50 kdyn force; 500-600 micrometre tissue displacement"}
    assert {row["sex"] for row in by_study["FLOW_SCI_352"]} == {"adult female C57BL/6 mice, 18-20 g"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_280"]} == {"T11"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_280"]} == {"50 +/- 5 kdyn force; 400-600 micrometre tissue displacement"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_053"]} == {"T9"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_054"]} == {"T12"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_054"]} == {"50-g compression for 5 minutes over a 2 x 5 mm platform"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_022"]} == {"T10"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_022"]} == {"5-g weight dropped from 8 cm; reported injury energy 40 g x cm"}
    assert {row["injury_level"] for row in by_study["FLOW_MSCS_ITDB_000032"]} == {"T8"}
    assert {row["injury_severity"] for row in by_study["FLOW_MSCS_ITDB_000032"]} == {"dorsal-column transection; exact transection geometry not reported in the cited passage"}
    assert {row["injury_level"] for row in by_study["FLOW_MSCS_ITDB_000057"]} == {"T10"}
    assert {row["sex"] for row in by_study["FLOW_MSCS_ITDB_000057"]} == {"adult male C57BL/6 mice, 8 weeks"}
    assert {row["injury_level"] for row in by_study["FLOW_MSCS_ITDB_000101"]} == {"T9"}
    assert {row["injury_severity"] for row in by_study["FLOW_MSCS_ITDB_000101"]} == {"50 kdyn force with 400-600 micrometre displacement; moderate contusion"}
    assert {row["injury_level"] for row in by_study["FLOW_MSCS_ITDB_000105"]} == {"T9"}
    assert {row["sex"] for row in by_study["FLOW_MSCS_ITDB_000105"]} == {"adult female C57BL/6J congenic mice"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_008"]} == {"T12"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_008"]} == {"150 kdyn force with 1-second dwell time; moderate contusion"}
    assert {row["sex"] for row in by_study["FLOW_SCI_008"]} == {"male Sprague-Dawley rats, 90-110 days, 300-350 g"}
    assert {row["timepoint_value"] for row in by_study["FLOW_SCI_013"]} == {"0-3"}
    assert {row["timepoint_unit"] for row in by_study["FLOW_SCI_013"]} == {"day"}
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
