from __future__ import annotations

import csv
import json
from pathlib import Path

from scripts.audit_ligand_availability import build


ROOT = Path(__file__).parents[1]
RELEASE = ROOT / "data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion627"
LEDGER = ROOT / "work/cross_module_synthesis/canonical_evidence_review/module20_24_integrated_phase2_extractions.tsv"
PACK = ROOT / "context_packs/spinal_cord_injury"


def test_ligand_availability_audit_is_source_preserving(tmp_path):
    summary = build(RELEASE, LEDGER, PACK, tmp_path)

    assert summary["audit_version"] == "ligand_availability_audit_v1"
    assert summary["mechanism_release_id"] == "module20_24_mechanism_graph:2026-09-25-literature-expansion-627"
    assert summary["release_ligand_node_count"] > 0
    assert summary["ligand_evidence_associations"] > 0
    assert summary["ligand_context_form_assertions"] == 123
    assert summary["ligand_context_form_assertion_nodes"] == 24
    assert summary["counts_by"]["availability_evidence_state"]["not_reported_in_source_record"] > 0
    assert (tmp_path / "ligand_availability_audit.tsv").is_file()
    assert (tmp_path / "ligand_availability_audit.json").is_file()

    rows = list(csv.DictReader((tmp_path / "ligand_availability_audit.tsv").open(), delimiter="\t"))
    slit2 = next(row for row in rows if row["b_evidence_id"] == "M20B-EVID-001792")
    assert slit2["mechanism_node_id"] == "NODE10400"
    assert slit2["dependency_group"] == "M20B-EVID-001792|NODE10400"
    assert slit2["availability_class_candidate"] == "soluble"
    assert slit2["promotion_state"] == "audit_only_not_promoted"

    ada = next(row for row in rows if row["b_evidence_id"] == "M20B-EVID-002407")
    assert ada["availability_evidence_state"] != "source_reported_candidate"

    adam10 = next(row for row in rows if row["b_evidence_id"] == "M23B-EVID-000636")
    assert adam10["availability_evidence_state"] != "source_reported_candidate"

    clcf1 = next(row for row in rows if row["b_evidence_id"] == "M20B-EVID-002958")
    assert clcf1["availability_class_candidate"] == "soluble"
    assert clcf1["availability_evidence_state"] == "source_reported_candidate"

    cd48 = next(row for row in rows if row["b_evidence_id"] == "M20B-EVID-002905")
    assert cd48["availability_class_candidate"] == "membrane_bound"
    assert cd48["availability_evidence_state"] == "source_reported_candidate"

    collagen = next(row for row in rows if row["b_evidence_id"] == "M20B-EVID-001936")
    assert collagen["availability_class_candidate"] == "ecm_retained"
    assert collagen["availability_evidence_state"] == "source_reported_candidate"

    perlecan = next(row for row in rows if row["b_evidence_id"] == "M20B-EVID-002127")
    assert perlecan["availability_class_candidate"] == "ecm_retained"
    assert perlecan["availability_evidence_state"] == "source_reported_candidate"

    netrin = next(row for row in rows if row["b_evidence_id"] == "M20B-EVID-002232")
    assert netrin["availability_class_candidate"] == "soluble"
    assert netrin["availability_evidence_state"] == "source_reported_candidate"

    fibronectin = next(row for row in rows if row["b_evidence_id"] == "M23B-EVID-000749")
    assert fibronectin["availability_class_candidate"] == "both_or_context_dependent"
    assert fibronectin["availability_evidence_state"] == "source_reported_candidate"

    for evidence_id in ("M20B-EVID-002154", "M20B-EVID-002199", "M20B-EVID-003229"):
        row = next(item for item in rows if item["b_evidence_id"] == evidence_id)
        assert row["availability_class_candidate"] == "both_or_context_dependent"
        assert row["availability_evidence_state"] == "source_reported_candidate"

    expected_source_candidates = {
        "M20B-EVID-002904": "membrane_bound",
        "M20B-EVID-004969": "soluble",
        "M20B-EVID-002994": "ecm_retained",
        "M20B-EVID-003007": "ecm_retained",
        "M20B-EVID-004966": "ecm_retained",
        "M23B-EVID-000346": "ecm_retained",
    }
    for evidence_id, candidate in expected_source_candidates.items():
        row = next(item for item in rows if item["b_evidence_id"] == evidence_id)
        assert row["availability_class_candidate"] == candidate
        assert row["availability_evidence_state"] == "source_reported_candidate"

    context_rows = [
        row
        for row in rows
        if row["assertion_origin"] == "sci_context_observation"
        and row["context_observation_id"] == "FLOW_SCI_061__FLOW_SCI_061_O_CCL2_3D"
        and row["mechanism_node_id"] == "NODE01661"
    ]
    assert len(context_rows) == 1
    ccl2 = context_rows[0]
    assert ccl2["availability_class_candidate"] == "soluble"
    assert ccl2["availability_evidence_state"] == "context_observation_explicit_protein_form"
    assert ccl2["context_study_id"] == "FLOW_SCI_061"
    assert ccl2["context_timepoint_value"] == "3"
    assert ccl2["context_timepoint_unit"] == "days"
    assert ccl2["context_injury_model"] == "Dosed thoracic contusion spinal cord injury"
    assert ccl2["context_injury_level"] == "Th8"
    assert ccl2["context_protein_form"] == "soluble"
    assert ccl2["promotion_state"] == "audit_only_not_promoted"

    fn1 = next(
        row
        for row in rows
        if row["assertion_origin"] == "sci_context_observation"
        and row["mechanism_node_id"] == "NODE03756"
        and row["context_observation_id"] == "FLOW_SCI_334__OBS334_FN"
    )
    assert fn1["availability_class_candidate"] == "ecm_retained"
    assert fn1["context_protein_form"] == "matrix-associated"
    assert fn1["availability_evidence_state"] == "context_observation_explicit_protein_form"

    fn1_soluble = next(
        row
        for row in rows
        if row["assertion_origin"] == "sci_context_observation"
        and row["mechanism_node_id"] == "NODE03756"
        and row["context_observation_id"] == "FLOW_SCI_251__O1"
    )
    assert fn1_soluble["availability_class_candidate"] == "soluble"
    assert fn1_soluble["availability_basis_fields"] == "observations.tsv:value_text"
    assert fn1_soluble["context_timepoint_value"] == "3"

    assert not any(
        row["assertion_origin"] == "sci_context_observation"
        and row["context_observation_id"] == "FLOW_SCI_202__O4"
        for row in rows
    )
    assert not any(
        row["assertion_origin"] == "sci_context_observation"
        and row["context_observation_id"] == "FLOW_SCI_221__OBS221_1H_IL33_CSF"
        for row in rows
    )


def test_ligand_availability_audit_records_exact_inputs(tmp_path):
    build(RELEASE, LEDGER, PACK, tmp_path)
    report = json.loads((tmp_path / "ligand_availability_audit.json").read_text())
    assert [item["path"] for item in report["input_artifacts"]] == [
        "data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion627/bundle_metadata.json",
        "data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion627/mechanism_nodes.tsv",
        "data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion627/mechanism_edges.tsv",
        "work/cross_module_synthesis/canonical_evidence_review/module20_24_integrated_phase2_extractions.tsv",
        "context_packs/spinal_cord_injury/observations.tsv",
        "context_packs/spinal_cord_injury/contexts.tsv",
    ]
