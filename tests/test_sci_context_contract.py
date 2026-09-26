from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

from scripts.build_sci_context_pack import protein_form_requires_state_review
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
    assert manifest["context_pack_version"] == "0.5.14"
    assert manifest["counts"]["observations"] == 760
    assert manifest["counts"]["mechanism_links"] == 760
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
    assert len(overrides) == 80
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
    assert {row["injury_level"] for row in by_study["FLOW_SCI_334"]} == {"T10"}
    assert {row["sex"] for row in by_study["FLOW_SCI_334"]} == {"adult male ICR mice, 7 weeks, 20-25 g"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_274"]} == {"T7"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_272"]} == {"T8-T9"}
    assert {row["sex"] for row in by_study["FLOW_SCI_272"]} == {"female C57BL/6 mice, 8-10 weeks, 25-30 g"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_293"]} == {"1-minute artery clamp after laminectomy; recovery-period SCI model"}
    assert {row["sex"] for row in by_study["FLOW_SCI_293"]} == {"male ICR mice, 6-8 weeks"}
    sci_294_in_vivo = [row for row in by_study["FLOW_SCI_294"] if row["timepoint_value"] == "7"]
    assert {row["injury_severity"] for row in sci_294_in_vivo} == {"0.3-mm-spacer clamp compression for 30 seconds"}
    assert {row["sex"] for row in sci_294_in_vivo} == {"male C57BL/6 mice, 6-8 weeks"}
    sci_294_in_vitro = [row for row in by_study["FLOW_SCI_294"] if row["timepoint_value"] == "-1.0"]
    assert {row["injury_severity"] for row in sci_294_in_vitro} == {"clamp-compression; exact force not extracted"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_311"]} == {"10-g weight dropped from 5 cm after T8-T10 laminectomy"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_311"]} == {"T9"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_322"]} == {"10-g weight dropped from 12.5 mm"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_322"]} == {"T11-T12"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_343"]} == {"T10"}
    assert {row["sex"] for row in by_study["FLOW_SCI_343"]} == {"female CD1 mice"}
    assert {row["sex"] for row in by_study["FLOW_SCI_344"]} == {"female C57BL/6 mice, 10 weeks"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_030"]} == {"T6-T7"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_030"]} == {"24-g bilateral aneurysm-clip compression for 1 minute"}
    assert {row["sex"] for row in by_study["FLOW_SCI_030"]} == {"male C57BL/6 mice, 22±2 g"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_103"]} == {"50 kdyn moderate contusion"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_103"]} == {"T9"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_252"]} == {"1-g weight dropped from 30 mm; moderate contusion"}
    assert {row["sex"] for row in by_study["FLOW_SCI_252"]} == {"male C57BL/6 mice"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_312"]} == {"0.5-mm displacement at 1.00 m/s"}
    assert {row["sample_scope"] for row in by_study["FLOW_SCI_312"]} == {"1-cm lesion-centered spinal-cord segment"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_341"]} == {"75 kdyn moderate contusion"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_341"]} == {"T9"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_424"]} == {"60 kdyn contusion; 500-700 micrometre displacement range"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_431"]} == {"T10"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_435"]} == {"8.3-g clip compression for 60 seconds"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_473"]} == {"T9"}
    assert {row["sample_scope"] for row in by_study["FLOW_SCI_473"]} == {"6-mm lesion-centered spinal-cord segment"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_002"]} == {"75 kdyn moderate contusion; approximately 500 micrometres displacement"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_010"]} == {"T9"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_032"]} == {"50 +/- 5 kDynes; 400-600 micrometres displacement"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_092"]} == {"T8"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_100"]} == {"T9-T10"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_101"]} == {"30-g vascular clip compression for 10 seconds"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_112"]} == {"5-g weight dropped from 5 cm; moderate contusion"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_130"]} == {"T10"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_152"]} == {"T11"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_255"]} == {"T10"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_260"]} == {"60-kdyn moderate-to-severe contusion"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_271"]} == {"forceps compression for 15 seconds; severe injury"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_300"]} == {"T10"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_304"]} == {"24-g clip-compression injury; severe trauma in the reported model"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_361"]} == {"T9"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_370"]} == {"0.45-mm displacement at 1.0 m/s; severe contusion"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_374"]} == {"T8"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_402"]} == {"75-kdyne moderate contusion"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_421"]} == {"T11"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_422"]} == {"60 kdyn moderate contusion"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_430"]} == {"T11-T12 laminectomy/contusion region"}
    assert {row["injury_level"] for row in by_study["FLOW_SCI_432"]} == {"T13"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_442"]} == {"0.4-mm maximum closure for 60 seconds"}
    assert {row["injury_severity"] for row in by_study["FLOW_SCI_533"]} == {"80 kdyn moderate contusion"}
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
    sci253_t2 = [row for row in contexts if row["study_id"] == "FLOW_SCI_253" and row["timepoint_value"] == "24 h; 48 h; 5 d; 8 d"]
    assert len(sci253_t2) == 1
    assert sci253_t2[0]["timepoint_unit"] == "mixed"
    ev_contexts = [row for row in contexts if row["study_id"] == "FLOW_SCI_471"]
    assert {row["sample_scope"] for row in ev_contexts} == {
        "plasma EV and T10 lesion-centered spinal-cord samples",
        "plasma extracellular-vesicle fraction",
    }
    observations = list(csv.DictReader((PACK / "observations.tsv").open(), delimiter="\t"))
    curated_context_ids = {
        context["context_id"]
        for context in contexts
        if context["study_id"] in by_study and "context_curation=" in context["provenance_note"]
    }
    curated = [row for row in observations if row["context_id"] in curated_context_ids]
    assert curated
    assert all("context_curation" in json.loads(row["provenance_note"]) for row in curated)


def test_sci_context_pack_validator_accepts_populated_release():
    summary = validate_pack(PACK)

    assert summary["pack_id"] == "spinal_cord_injury"
    assert summary["counts"]["observations"] == 760
    assert summary["counts"]["mechanism_links"] == 760


def test_sci_observations_and_links_preserve_evidence_boundaries():
    observations = list(csv.DictReader((PACK / "observations.tsv").open(), delimiter="\t"))
    links = list(csv.DictReader((PACK / "mechanism_links.tsv").open(), delimiter="\t"))
    assert Counter(row["modality"] for row in observations) == {"protein": 743, "epigenomics": 17}
    assert Counter(row["evidence_role"] for row in observations) == {"dataset_observation": 760}
    assert all(row["dependency_group"] for row in observations)
    assert all(row["mechanism_release_id"] == "module20_24_mechanism_graph:2026-09-25-literature-expansion-627" for row in links)
    assert all(row["mechanism_target_kind"] == "node" for row in links if row["release_status"] == "included")
    assert all(row["mechanism_target_key"] == "21B" for row in links if row["release_status"] == "staging")
    assert all(row["mechanism_route_id"] == "" for row in links)


def test_sci_protein_context_gap_audit_is_reproducible_and_separate_from_evidence():
    audit = json.loads((PACK / "protein_context_gap_audit.json").read_text())
    assert (PACK / "protein_context_coverage.tsv").is_file()
    assert (PACK / "protein_context_gap_candidates.tsv").is_file()
    assert audit["pack_inputs"]["protein_observations"] == 743
    assert audit["pack_inputs"]["protein_expression_observations"] == 633
    assert audit["canonical_store"]["protein_observations"] == 1259
    assert audit["canonical_store"]["remaining_gap_records"] == 516
    assert audit["policy"].startswith("This audit prioritizes metadata refinement only")


def test_sci_protein_selector_keeps_direct_expression_and_excludes_unresolved_states():
    observations = {
        row["observation_id"]: row
        for row in csv.DictReader((PACK / "observations.tsv").open(), delimiter="\t")
    }
    for observation_id in {
        "FLOW_SCI_001__O1",  # intracellular protein flow
        "FLOW_SCI_015__FLOW_SCI_015_OBS2",  # human SCI plasma CRP
        "FLOW_SCI_065__FLOW_SCI_065_O_IL6",  # protein array
        "FLOW_SCI_202__O1",  # antibody array
        "FLOW_SCI_223__OBS223_12H_S100A8_MILD",  # discovery proteomics
        "FLOW_SCI_300__OBS300_MLKL_1H",  # total MLKL; phospho unresolved
        "FLOW_SCI_526__OBS526_CXCL12",  # antibody array
    }:
        assert observation_id in observations

    # A timepoint explicitly marked inferred remains outside the release.
    assert "FLOW_SCI_536__OBS536_FTH1" not in observations
    assert "FLOW_SCI_553__O_PERK5_WB" not in observations
    assert not protein_form_requires_state_review({"protein_form": "soluble C-reactive protein", "measurement_kind": "group median"})
    assert not protein_form_requires_state_review({"protein_form": "total MLKL; phospho-MLKL not directly resolved", "measurement_kind": "MLKL protein by Western blot"})
    assert protein_form_requires_state_review({"protein_form": "phosphorylated ERK5", "measurement_kind": "relative abundance"})
