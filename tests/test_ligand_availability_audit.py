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
    assert summary["source_register_form_assertions"] == 169
    assert summary["source_register_form_assertion_ids"] == 162
    assert summary["source_register_skipped_existing_ledger"] == 5
    assert summary["source_register_unresolved_mappings"] == []
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
        "M20B-EVID-001844": "both_or_context_dependent",
        "M20B-EVID-002904": "membrane_bound",
        "M20B-EVID-004969": "soluble",
        "M20B-EVID-002994": "ecm_retained",
        "M20B-EVID-003007": "ecm_retained",
        "M20B-EVID-004966": "ecm_retained",
        "M20B-EVID-005357": "both_or_context_dependent",
        "M23B-EVID-000346": "ecm_retained",
        "M20B-EVID-002290": "both_or_context_dependent",
    }
    for evidence_id, candidate in expected_source_candidates.items():
        row = next(item for item in rows if item["b_evidence_id"] == evidence_id)
        assert row["availability_class_candidate"] == candidate
        assert row["availability_evidence_state"] == "source_reported_candidate"

    suppressed_form_records = {
        "M20B-EVID-002230",  # explicit negative: NCAM1 is not a secreted ligand
        "M20B-EVID-003441",  # soluble/membrane-bound FGFRL1 receptor, not FGF2
        "M20B-EVID-003444",  # soluble/immobilized NRP1 receptor, not FGF2
        "M21B-EVID-000052",  # transmembrane IFNGR2 receptor, not IFN-gamma
        "M23B-EVID-000597",  # soluble alphaIIbbeta3 receptor, not CXCL12
        "M23B-EVID-000738",  # cell-surface alphaVbeta1 receptor, not FN1
    }
    for evidence_id in suppressed_form_records:
        row = next(item for item in rows if item["b_evidence_id"] == evidence_id)
        assert row["availability_class_candidate"] == "unknown"
        assert row["availability_evidence_state"] == "assay_or_form_language_not_attached_to_exact_ligand"
        assert "Manual adjudication:" in row["audit_note"]

    source_register_rows = [
        row for row in rows if row["assertion_origin"] == "source_register_form_observation"
    ]
    assert len(source_register_rows) == 169
    assert len({row["b_evidence_id"] for row in source_register_rows}) == 162
    assert all(row["availability_evidence_state"] == "source_register_explicit_form" for row in source_register_rows)
    assert all(row["observation_status"] == "source_register_curated" for row in source_register_rows)
    assert all(row["promotion_state"] == "audit_only_not_promoted" for row in source_register_rows)

    register_expectations = {
        "M21B-EVID-000095": ("membrane_bound", "NODE02888", "PMID:10958687"),
        "M21B-EVID-000137": ("membrane_bound", "NODE10207", "PMID:20877282; PMCID:PMC3587840"),
        "M21B-EVID-000902": ("membrane_bound", "NODE03727", "PMID:22405201; PMCID:PMC3326387"),
        "M21B-EVID-000111": ("both_or_context_dependent", "NODE02607", "PMID:25395671"),
        "M21B-EVID-000122": ("membrane_bound", "NODE01922", "PMID:18657508; PMID:11283158"),
        "M21B-EVID-000206": ("both_or_context_dependent", "NODE01686", "PMID:33875601; PMCID:PMC8092586"),
        "M21B-EVID-000334": ("both_or_context_dependent", "NODE00742", "PMID:7929459"),
        "M21B-EVID-000469": ("ecm_retained", "NODE02354", "PMID:18305222; PMCID:PMC2602586"),
        "M21B-EVID-000585": ("ecm_retained", "NODE11720", "PMID:12709411"),
        "M21B-EVID-000627": ("soluble", "NODE03686", "PMID:30580966; PMCID:PMC6365968; DOI:10.1016/j.cell.2018.11.010"),
        "M21B-EVID-002324": ("soluble", "NODE08446", "PMID:9856994"),
        "M21B-EVID-002336": ("membrane_bound", "NODE05070", "PMID:28864826; PMCID:PMC5581337"),
        "M21B-EVID-002796": ("both_or_context_dependent", "NODE07584", "PMID:20497550; PMCID:PMC2890604; DOI:10.1186/1476-4598-9-118"),
        "M21B-EVID-006991": ("ecm_retained", "NODE01296", "PMID:18339631; PMCID:PMC2376219; DOI:10.1074/jbc.M707820200"),
        "M21B-EVID-009291": ("both_or_context_dependent", "NODE11398", "PMID:27147664; PMCID:PMC4854972; DOI:10.1523/JNEUROSCI.0211-16.2016"),
        "M21B-EVID-009997": ("soluble", "NODE09672", "PMID:19997621; PMCID:PMC2780297; DOI:10.1371/journal.pone.0008141"),
        "M23B-EVID-001470": ("soluble", "NODE01247", "PMID:29777767; PMID:16025156; PMID:25017885; PMID:22821552; PMCID:PMC3527886; PMCID:PMC4099942; local:data/raw/evidence/module23a_review_led_20260904/biglycan_pubmed.xml; local:data/raw/evidence/module23a_review_led_20260904/biglycan_and_sci_review_pubmed.xml; local:data/raw/evidence/module23a_review_led_20260904/PMC3527886_fulltext.xml; local:data/raw/evidence/module23a_review_led_20260904/PMC4099942_fulltext.xml"),
        "M21B-EVID-000241": ("soluble", "NODE04255", "PMID:7679207; PMID:9422729; PMID:8879206"),
        "M21B-EVID-000277": ("both_or_context_dependent", "NODE10230", "PMID:14977921; PMID:36156831"),
        "M21B-EVID-006910": ("ecm_retained", "NODE04057", "PMID:21200028; PMCID:PMC3019558; DOI:10.1083/jcb.201009136"),
        "M21B-EVID-009994": ("soluble", "NODE09672", "PMID:19997621; PMCID:PMC2780297; DOI:10.1371/journal.pone.0008141"),
        "M21B-EVID-010981": ("ecm_retained", "NODE06236", "PMID:29874128"),
        "M23B-EVID-001552": ("soluble", "NODE03078", "PMID:19299512; DOI:10.1074/jbc.M807598200; PMCID:PMC2682911; local:data/raw/evidence/module23a_review_led_20260904/efna2_epha2_osteoclast_pubmed.xml; local:data/raw/evidence/module23a_review_led_20260904/efna2_epha2_osteoclast_pmc.html"),
    }
    for evidence_id, (candidate, node_id, locator) in register_expectations.items():
        row = next(item for item in source_register_rows if item["b_evidence_id"] == evidence_id)
        assert row["availability_class_candidate"] == candidate
        assert row["mechanism_node_id"] == node_id
        assert row["module_source_locator"] == locator
        assert row["dependency_group"] == f"{evidence_id}|{node_id}"

    # Register evidence is additive only for IDs absent from the integrated
    # ledger; these IDs remain represented by their existing ledger rows.
    assert not any(
        row["assertion_origin"] == "source_register_form_observation"
        and row["b_evidence_id"] in {
            "M20B-EVID-002097",
            "M23B-EVID-000580",
            "M23B-EVID-000604",
            "M23B-EVID-001390",
            "M23B-EVID-001392",
        }
        for row in rows
    )
    # Form words referring only to a receptor ectodomain/decoy are not
    # promoted as ligand-form assertions.
    assert not any(
        row["assertion_origin"] == "source_register_form_observation"
        and row["b_evidence_id"] in {
            "M21B-EVID-000104",  # soluble IL-1R2 decoy, not IL-1alpha
            "M21B-EVID-000105",  # soluble IL-1R2/accessory complex, not IL-1beta
            "M21B-EVID-000286",  # soluble endoglin, not BMP9
            "M21B-EVID-000287",  # soluble endoglin, not BMP10
        }
        for row in rows
    )

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
        "work/module_b_consolidation/module20b/module20b_evidence_register.tsv",
        "work/module_b_consolidation/module21b/module21b_evidence_register.tsv",
        "work/module_b_consolidation/module22b/module22b_evidence_register.tsv",
        "work/module_b_consolidation/module23b/module23b_evidence_register.tsv",
        "work/module_b_consolidation/module24b/module24b_evidence_register.tsv",
        "context_packs/spinal_cord_injury/observations.tsv",
        "context_packs/spinal_cord_injury/contexts.tsv",
    ]
