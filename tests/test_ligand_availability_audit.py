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
    assert summary["source_register_form_assertions"] == 466
    assert summary["source_register_form_assertion_ids"] == 459
    assert summary["source_register_skipped_existing_ledger"] == 29
    assert summary["source_register_form_applied_to_ledger"] == 27
    assert summary["source_register_form_applied_to_ledger_ids"] == [
        "M20B-EVID-002097",
        "M20B-EVID-003285",
        "M20B-EVID-003287",
        "M20B-EVID-003426",
        "M23B-EVID-000350",
        "M23B-EVID-000475",
        "M23B-EVID-000476",
        "M23B-EVID-000477",
        "M23B-EVID-000580",
        "M23B-EVID-000581",
        "M23B-EVID-000582",
        "M23B-EVID-000604",
        "M23B-EVID-000606",
        "M23B-EVID-000610",
        "M23B-EVID-000611",
        "M23B-EVID-000612",
        "M23B-EVID-000709",
        "M23B-EVID-000711",
        "M23B-EVID-001390",
        "M23B-EVID-001392",
        "M23B-EVID-001424",
        "M23B-EVID-001426",
        "M23B-EVID-001427",
        "M23B-EVID-001429",
        "M23B-EVID-001437",
        "M24B-EVID-000008",
        "M24B-EVID-000110",
    ]
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

    expected_additional_ledger_forms = {
        "M20B-EVID-000472": ("both_or_context_dependent", "source_reported_candidate"),
        "M20B-EVID-001792": ("soluble", "source_reported_candidate"),
        "M20B-EVID-002382": ("soluble", "source_reported_candidate"),
        "M20B-EVID-002567": ("soluble", "source_reported_candidate"),
        "M20B-EVID-002886": ("membrane_bound", "source_reported_candidate"),
        "M20B-EVID-002906": ("soluble", "source_reported_candidate"),
        "M20B-EVID-002912": ("membrane_bound", "source_reported_candidate"),
        "M20B-EVID-002929": ("both_or_context_dependent", "source_reported_candidate"),
        "M20B-EVID-002958": ("soluble", "source_reported_candidate"),
        "M20B-EVID-002981": ("membrane_bound", "source_reported_candidate"),
        "M20B-EVID-002982": ("membrane_bound", "source_reported_candidate"),
        "M20B-EVID-002985": ("membrane_bound", "source_reported_candidate"),
        "M20B-EVID-003389": ("soluble", "source_reported_candidate"),
        "M20B-EVID-003739": ("soluble", "source_reported_candidate"),
        "M20B-EVID-003767": ("soluble", "source_reported_candidate"),
        "M20B-EVID-003768": ("soluble", "source_reported_candidate"),
        "M20B-EVID-005366": ("both_or_context_dependent", "source_reported_candidate"),
        "M24B-EVID-000043": ("soluble", "source_reported_candidate"),
        "M24B-EVID-000152": ("ecm_retained", "source_reported_candidate"),
        "M24B-EVID-000167": ("soluble", "source_reported_candidate"),
        "M24B-EVID-000195": ("soluble", "source_reported_candidate"),
        "M24B-EVID-000008": ("soluble", "source_register_explicit_form"),
        "M20B-EVID-001856": ("membrane_bound", "source_reported_candidate"),
        "M20B-EVID-001983": ("soluble", "source_reported_candidate"),
        "M20B-EVID-002893": ("membrane_bound", "source_reported_candidate"),
        "M20B-EVID-002980": ("membrane_bound", "source_reported_candidate"),
        "M20B-EVID-002984": ("membrane_bound", "source_reported_candidate"),
        "M20B-EVID-003707": ("membrane_bound", "source_reported_candidate"),
        "M24B-EVID-000085": ("soluble", "source_reported_candidate"),
        "M24B-EVID-000165": ("soluble", "source_reported_candidate"),
        "M23B-EVID-000350": ("ecm_retained", "source_register_explicit_form"),
        "M23B-EVID-000475": ("soluble", "source_register_explicit_form"),
        "M23B-EVID-000476": ("soluble", "source_register_explicit_form"),
        "M23B-EVID-000477": ("soluble", "source_register_explicit_form"),
        "M23B-EVID-000581": ("both_or_context_dependent", "source_register_explicit_form"),
        "M23B-EVID-000582": ("both_or_context_dependent", "source_register_explicit_form"),
        "M23B-EVID-000606": ("both_or_context_dependent", "source_register_explicit_form"),
        "M23B-EVID-000610": ("membrane_bound", "source_register_explicit_form"),
        "M23B-EVID-000611": ("membrane_bound", "source_register_explicit_form"),
        "M23B-EVID-000612": ("membrane_bound", "source_register_explicit_form"),
        "M23B-EVID-000709": ("ecm_retained", "source_register_explicit_form"),
        "M23B-EVID-000711": ("ecm_retained", "source_register_explicit_form"),
        "M20B-EVID-002097": ("ecm_retained", "source_register_explicit_form"),
        "M20B-EVID-003285": ("membrane_bound", "source_register_explicit_form"),
        "M20B-EVID-003287": ("soluble", "source_register_explicit_form"),
        "M23B-EVID-000580": ("both_or_context_dependent", "source_register_explicit_form"),
        "M23B-EVID-000604": ("both_or_context_dependent", "source_register_explicit_form"),
        "M23B-EVID-001390": ("membrane_bound", "source_register_explicit_form"),
        "M23B-EVID-001392": ("membrane_bound", "source_register_explicit_form"),
        "M23B-EVID-001429": ("soluble", "source_register_explicit_form"),
        "M24B-EVID-000110": ("soluble", "source_register_explicit_form"),
    }
    for evidence_id, (candidate, state) in expected_additional_ledger_forms.items():
        assert any(
            row["b_evidence_id"] == evidence_id
            and row["availability_class_candidate"] == candidate
            and row["availability_evidence_state"] == state
            for row in rows
        )

    expected_new_source_register_forms = {
        "M21B-EVID-002700": "soluble",
        "M21B-EVID-000121": "both_or_context_dependent",
        "M21B-EVID-000814": "both_or_context_dependent",
        "M21B-EVID-003183": "both_or_context_dependent",
        "M21B-EVID-003184": "soluble",
        "M21B-EVID-004722": "membrane_bound",
        "M21B-EVID-004723": "both_or_context_dependent",
        "M21B-EVID-007028": "soluble",
        "M21B-EVID-000543": "both_or_context_dependent",
        "M21B-EVID-000709": "membrane_bound",
        "M21B-EVID-000710": "membrane_bound",
        "M21B-EVID-004638": "ecm_retained",
        "M21B-EVID-004639": "soluble",
        "M21B-EVID-004647": "soluble",
        "M21B-EVID-004658": "soluble",
        "M21B-EVID-004659": "soluble",
        "M21B-EVID-004687": "membrane_bound",
        "M21B-EVID-004688": "membrane_bound",
        "M21B-EVID-004693": "membrane_bound",
        "M21B-EVID-004695": "membrane_bound",
        "M21B-EVID-004709": "membrane_bound",
        "M21B-EVID-004710": "membrane_bound",
        "M21B-EVID-004718": "membrane_bound",
        "M21B-EVID-006490": "both_or_context_dependent",
        "M21B-EVID-006557": "both_or_context_dependent",
        "M21B-EVID-002108": "soluble",
        "M21B-EVID-002109": "soluble",
        "M21B-EVID-002155": "both_or_context_dependent",
        "M21B-EVID-002557": "membrane_bound",
        "M21B-EVID-004645": "soluble",
        "M21B-EVID-004800": "soluble",
        "M21B-EVID-004807": "soluble",
        **{f"M21B-EVID-{evidence_id:06d}": "soluble" for evidence_id in range(4825, 4835)},
        "M21B-EVID-004905": "soluble",
        "M21B-EVID-004911": "both_or_context_dependent",
        "M21B-EVID-004912": "both_or_context_dependent",
        "M21B-EVID-004915": "soluble",
        "M21B-EVID-004916": "soluble",
        "M21B-EVID-004917": "soluble",
        "M21B-EVID-004919": "soluble",
        "M21B-EVID-004920": "soluble",
        "M21B-EVID-004923": "soluble",
        "M21B-EVID-005419": "soluble",
        "M21B-EVID-005457": "soluble",
        "M21B-EVID-005552": "soluble",
        "M21B-EVID-005587": "membrane_bound",
        "M21B-EVID-005740": "both_or_context_dependent",
        "M21B-EVID-005816": "soluble",
        "M21B-EVID-006087": "soluble",
        "M21B-EVID-006221": "soluble",
        "M21B-EVID-006224": "soluble",
        "M21B-EVID-006225": "soluble",
        "M21B-EVID-006226": "soluble",
        "M21B-EVID-006239": "soluble",
        "M21B-EVID-006297": "soluble",
        "M21B-EVID-007077": "soluble",
        "M21B-EVID-007078": "soluble",
        "M23B-EVID-001425": "soluble",
    }
    for evidence_id, candidate in expected_new_source_register_forms.items():
        matches = [
            row
            for row in rows
            if row["b_evidence_id"] == evidence_id
            and row["assertion_origin"] == "source_register_form_observation"
        ]
        assert matches
        assert {row["availability_class_candidate"] for row in matches} == {candidate}
        assert all(row["module_source_locator"] for row in matches)

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
    assert len(source_register_rows) == 466
    assert len({row["b_evidence_id"] for row in source_register_rows}) == 459
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
        "M21B-EVID-000157": ("soluble", "NODE10169", "PMID:9829984; PMID:7532174"),
        "M21B-EVID-000249": ("membrane_bound", "NODE07703", "PMID:11736641"),
        "M21B-EVID-000638": ("both_or_context_dependent", "NODE01806", "PMCID:PMC7477951; PMID:25179432; PMCID:PMC4163173; DOI:10.1186/s12967-014-0217-y"),
        "M21B-EVID-000774": ("membrane_bound", "NODE09761", "PMID:23744777; PMCID:PMC4730555"),
        "M21B-EVID-002824": ("soluble", "NODE08176", "PMID:11201742; DOI:10.1038/35053072"),
        "M21B-EVID-004681": ("both_or_context_dependent", "NODE09236", "PMID:19850343; DOI:10.1016/j.molimm.2009.07.017"),
        "M21B-EVID-005527": ("both_or_context_dependent", "NODE03752", "PMID:8896403; PMID:12969963"),
        "M21B-EVID-005548": ("both_or_context_dependent", "NODE03110", "PMID:23386126"),
        "M21B-EVID-006331": ("ecm_retained", "NODE03721", "PMID:11805835; DOI:10.1038/415168a"),
        "M21B-EVID-006496": ("ecm_retained", "NODE02405", "PMID:37356721; PMCID:PMC10382678; DOI:10.1016/j.jbc.2023.104962"),
        "M21B-EVID-010922": ("soluble", "NODE06593", "PMID:9552007"),
        "M21B-EVID-010952": ("membrane_bound", "NODE03085", "PMCID:PMC3499309; PMCID:PMC6782661"),
        "M21B-EVID-010953": ("membrane_bound", "NODE03085", "PMCID:PMC3499309; PMCID:PMC6782661"),
        "M21B-EVID-010954": ("membrane_bound", "NODE03085", "PMCID:PMC3499309; PMCID:PMC6782661"),
        "M21B-EVID-010955": ("membrane_bound", "NODE03085", "PMCID:PMC3499309; PMCID:PMC6782661"),
        "M21B-EVID-010956": ("membrane_bound", "NODE03089", "PMCID:PMC3499309; PMCID:PMC6782661"),
        "M21B-EVID-010957": ("membrane_bound", "NODE03089", "PMCID:PMC3499309; PMCID:PMC6782661"),
        "M21B-EVID-010958": ("membrane_bound", "NODE03089", "PMCID:PMC3499309; PMCID:PMC6782661"),
        "M21B-EVID-010988": ("ecm_retained", "NODE03620", "PMID:12697740; PMCID:PMC152937"),
        "M21B-EVID-000337": ("membrane_bound", "NODE02568", "PMID:15358134; DOI:10.1016/j.bbrc.2004.07.066"),
        "M21B-EVID-000462": ("soluble", "NODE08848", "PMID:11297552; DOI:10.1074/jbc.M101056200"),
        "M21B-EVID-000785": ("soluble", "NODE08175", "PMID:8752214"),
        "M21B-EVID-000791": ("soluble", "NODE02144", "PMCID:PMC3070603"),
        "M21B-EVID-000792": ("soluble", "NODE03837", "PMID:16198295; PMCID:PMC1409725"),
        "M21B-EVID-000795": ("soluble", "NODE10531", "PMID:12702725"),
        "M21B-EVID-000796": ("soluble", "NODE10531", "PMID:12702725"),
        "M21B-EVID-000800": ("soluble", "NODE04444", "PMID:22381466; PMCID:PMC3319168; PMID:15039429"),
        "M21B-EVID-000801": ("soluble", "NODE04444", "PMID:22381466; PMCID:PMC3319168; PMID:15039429"),
        "M21B-EVID-000803": ("soluble", "NODE11492", "PMID:15363410"),
        "M21B-EVID-000805": ("soluble", "NODE01247", "PMID:16025156; PMCID:PMC1174916"),
        "M21B-EVID-000806": ("soluble", "NODE01247", "PMID:16025156; PMCID:PMC1174916"),
        "M21B-EVID-000810": ("soluble", "NODE02790", "PMID:9988678; PMID:12105206"),
        "M21B-EVID-000812": ("soluble", "NODE02790", "PMCID: PMC5029092"),
        "M21B-EVID-000813": ("soluble", "NODE02790", "PMCID: PMC5029092"),
        "M21B-EVID-000857": ("soluble", "NODE10515", "PMID:30656676"),
        "M21B-EVID-000927": ("soluble", "NODE02262", "PMID:24381170; PMCID:PMC3924281"),
        "M21B-EVID-001061": ("soluble", "NODE01422", "PMID:37442133; DOI:10.1016/j.immuni.2023.06.016"),
        "M21B-EVID-000535": ("membrane_bound", "NODE06037", "PMID:12208882; PMID:15485832"),
        "M21B-EVID-000837": ("soluble", "NODE03969", "PMID:25753426; PMID:28128358"),
        "M21B-EVID-000928": ("soluble", "NODE02262", "PMID:24381170; PMCID:PMC3924281"),
        "M21B-EVID-001104": ("both_or_context_dependent", "NODE03051", "PMCID:PMC529342"),
        "M21B-EVID-006592": ("soluble", "NODE09906", "PMID:24225776; PMCID:PMC3905715"),
        "M21B-EVID-006603": ("soluble", "NODE10534", "PMID:19116665; PMCID:PMC2605561; DOI:10.1371/journal.pone.0004092"),
        "M21B-EVID-006605": ("soluble", "NODE03495", "PMID:29799787; DOI:10.1096/fj.201800020RRR"),
        "M21B-EVID-006639": ("soluble", "NODE03110", "PMID:19503073; DOI:10.1038/ncb1896"),
        "M21B-EVID-006915": ("soluble", "NODE11584", "PMID:30139743; PMCID:PMC6200953; DOI:10.1074/jbc.RA118.003950"),
        "M21B-EVID-006920": ("soluble", "NODE09200", "PMID:11943775; PMCID:PMC3048706; PMID:19500591"),
        "M21B-EVID-006924": ("soluble", "NODE03503", "PMID:33975953; PMCID:PMC8158011; DOI:10.1073/pnas.2100342118"),
        "M21B-EVID-006943": ("soluble", "NODE07541", "PMID:24442440"),
        "M21B-EVID-006948": ("membrane_bound", "NODE10227", "PMID:15814794; PMCID:PMC6725384; DOI:10.1016/j.neuron.2005.03.013"),
        "M21B-EVID-007067": ("both_or_context_dependent", "NODE03548", "PMID:7515913; PMID:7691616; PMID:8344338; PMCID:PMC2212946"),
        "M21B-EVID-007079": ("soluble", "NODE03566", "PMID:12421953; PMID:18031558; PMID:10679061"),
        "M21B-EVID-007080": ("soluble", "NODE03567", "PMID:22238349; PMID:11907111"),
        "M21B-EVID-007081": ("soluble", "NODE03565", "PMID:16305643; DOI:10.1111/j.1365-3083.2005.01685.x"),
        "M21B-EVID-007082": ("soluble", "NODE02383", "PMID:23220946; PMCID:PMC6741501; PMID:30323815"),
        "M21B-EVID-007086": ("soluble", "NODE02382", "PMID:23814060; PMID:22475410"),
        "M21B-EVID-007087": ("soluble", "NODE02383", "PMID:20956340; PMID:23220946"),
        "M21B-EVID-007088": ("soluble", "NODE02383", "PMID:20956340; PMID:23220946"),
        "M21B-EVID-010939": ("membrane_bound", "NODE10220", "PMID:21835343"),
        "M21B-EVID-010983": ("ecm_retained", "NODE02344", "PMID:1730778"),
        "M21B-EVID-000463": ("soluble", "NODE08848", "PMID:11297552; DOI:10.1074/jbc.M101056200"),
        "M21B-EVID-001862": ("soluble", "NODE03031", "PMID:32027618; PMCID:PMC7141396"),
        "M21B-EVID-002084": ("soluble", "NODE01618", "PMID:20537373; PMID:22457515; PMID:27926833"),
        "M21B-EVID-002085": ("soluble", "NODE01618", "PMID:20535596; PMID:27418511; PMID:22457515"),
        "M21B-EVID-002087": ("soluble", "NODE01619", "PMID:34135511; PMID:22220752"),
        "M21B-EVID-002095": ("both_or_context_dependent", "NODE08414", "PMID:25411505"),
        "M21B-EVID-002131": ("ecm_retained", "NODE06258", "PMID:19940114; PMCID:PMC2823405"),
        "M21B-EVID-002323": ("soluble", "NODE00550", "PMID:29100074; PMCID:PMC5847377"),
        "M21B-EVID-002331": ("soluble", "NODE01491", "PMID:28154140; PMCID:PMC5320979"),
        "M21B-EVID-002417": ("ecm_retained", "NODE03531", "PMID:15304491; PMID:32765223; PMCID:PMC7378325"),
        "M21B-EVID-002444": ("both_or_context_dependent", "NODE06637", "PMID:21252236; PMID:27460145"),
        "M21B-EVID-002763": ("membrane_bound", "NODE10221", "PMID:15814794"),
        "M21B-EVID-002797": ("soluble", "NODE06373", "PMID:25320078; PMCID:PMC4246102; DOI:10.1074/jbc.M114.612648"),
        "M21B-EVID-003036": ("soluble", "NODE09311", "PMID:20826454; PMCID:PMC2964349; PMID:22081071"),
        "M21B-EVID-003054": ("soluble", "NODE09314", "PMID:16046412; DOI:10.1074/jbc.M503007200"),
        "M21B-EVID-004612": ("soluble", "NODE10152", "PMID:7535771; PMCID:PMC10826034; PMID:38287411; DOI:10.1186/s12974-024-03026-6"),
        "M21B-EVID-004613": ("soluble", "NODE10152", "PMID:21268013; DOI:10.1002/eji.201040429"),
        "M21B-EVID-004614": ("soluble", "NODE10152", "PMID:21268013; DOI:10.1002/eji.201040429"),
        "M21B-EVID-005510": ("membrane_bound", "NODE02327", "PMID:33306155; PMCID:PMC7960628; DOI:10.1007/s00441-020-03300-y"),
        "M21B-EVID-005566": ("soluble", "NODE03687", "PMID:18991288"),
        "M21B-EVID-005575": ("membrane_bound", "NODE09606", "PMID:12732206; DOI:10.1016/S0006-291X(03)00714-9; https://pubmed.ncbi.nlm.nih.gov/12732206/"),
        "M21B-EVID-005780": ("soluble", "NODE02145", "PMID:30344043; PMCID:PMC6382071; DOI:10.1016/j.neuron.2018.09.043"),
        "M21B-EVID-005817": ("soluble", "NODE04348", "PMID:29024665; PMCID:PMC5663462; DOI:10.1016/j.neuron.2017.09.053"),
        "M21B-EVID-005909": ("membrane_bound", "NODE10202", "PMID:38781210; PMCID:PMC11145257; DOI:10.1073/pnas.2400648121"),
        "M21B-EVID-005975": ("soluble", "NODE07014", "PMID:38101413; DOI:10.1016/j.devcel.2023.11.018"),
        "M21B-EVID-006091": ("soluble", "NODE04384", "PMID:25351403; PMCID:PMC4212244; DOI:10.1038/srep06812"),
        "M21B-EVID-006099": ("soluble", "NODE11516", "PMID:20978472; PMCID:PMC3020645; DOI:10.1038/emboj.2010.265"),
        "M21B-EVID-006113": ("membrane_bound", "NODE02233", "PMID:20194751; PMCID:PMC2841919; DOI:10.1073/pnas.0913108107"),
        "M21B-EVID-006119": ("soluble", "NODE10966", "PMID:21982860; DOI:10.1016/j.ymeth.2012.06.004"),
        "M21B-EVID-006120": ("soluble", "NODE10968", "PMID:21982860; DOI:10.1016/j.ymeth.2012.06.004"),
        "M21B-EVID-006193": ("soluble", "NODE06180", "PMID:7543026; DOI:10.1016/0092-8674(95)90320-8"),
        "M21B-EVID-006362": ("soluble", "NODE10551", "PMID:33753902; PMCID:PMC8408247; DOI:10.1038/s41418-021-00772-5"),
        "M21B-EVID-006457": ("soluble", "NODE03498", "PMID:25109685; PMCID:PMC4579646; DOI:10.1038/cmi.2014.61"),
        "M21B-EVID-006462": ("soluble", "NODE10549", "PMID:17178915; DOI:10.1189/jlb.1105664"),
        "M21B-EVID-006480": ("soluble", "NODE04339", "PMID:8940123; DOI:10.1074/jbc.271.49.31215"),
        "M21B-EVID-006493": ("soluble", "NODE10182", "PMID:29661844"),
        "M21B-EVID-006497": ("soluble", "NODE06593", "PMID:8387891; DOI:10.1016/0092-8674(93)90132-A"),
        "M21B-EVID-006507": ("soluble", "NODE06201", "PMID:16982797"),
        "M21B-EVID-006538": ("membrane_bound", "NODE03107", "PMID:12383247; PMID:31011859; DOI:10.1046/j.1460-9568.2002.02166.x; DOI:10.1038/s41586-019-1151-3"),
        "M21B-EVID-006662": ("membrane_bound", "NODE03104", "PMID:10066262; PMCID:PMC6782574; DOI:10.1523/JNEUROSCI.19-06-02090.1999"),
        "M21B-EVID-007033": ("soluble", "NODE10406", "PMID:11375980; PMID:10364234; DOI:10.1074/jbc.M100240200; DOI:10.1074/jbc.274.25.17885"),
        "M21B-EVID-001861": ("soluble", "NODE08961", "PMID:25595774; PMCID:PMC4319313"),
        "M21B-EVID-002787": ("soluble", "NODE04756", "PMID:10190900; PMCID:PMC2193010; PMCID:PMC1318474; PMID:16366734"),
        "M21B-EVID-004607": ("soluble", "NODE04368", "PMID:34582891; PMCID:PMC8524194; DOI:10.3390/ijms222112057"),
        "M21B-EVID-004611": ("soluble", "NODE04368", "PMID:39455836; DOI:10.1038/s44161-024-00555-4"),
        "M21B-EVID-004640": ("soluble", "NODE04777", "PMID:17448537; DOI:10.1016/j.molimm.2007.03.003"),
        "M21B-EVID-004642": ("soluble", "NODE04891", "PMID:19896716; DOI:10.1016/j.molimm.2009.10.006"),
        "M21B-EVID-004643": ("both_or_context_dependent", "NODE11905", "PMID:17132743; PMCID:PMC1664712; DOI:10.1073/pnas.0605668103"),
        "M21B-EVID-004644": ("soluble", "NODE02824", "PMID:20308361; PMCID:PMC2856034; DOI:10.1084/jem.20092545"),
        "M21B-EVID-004682": ("both_or_context_dependent", "NODE09236", "PMID:19850343; DOI:10.1016/j.molimm.2009.07.017"),
        "M21B-EVID-004684": ("soluble", "NODE09236", "PMID:28860090; DOI:10.1016/j.molimm.2017.07.010"),
        "M21B-EVID-004809": ("soluble", "NODE02115", "PMID:15153520; DOI:10.4049/jimmunol.172.11.6994"),
        "M21B-EVID-004876": ("soluble", "NODE04621", "PMID:19428671; DOI:10.1016/j.molbiopara.2009.02.007"),
        "M21B-EVID-004877": ("both_or_context_dependent", "NODE11510", "PMID:30587214; PMCID:PMC6307294; DOI:10.1186/s13071-018-3258-x"),
        "M21B-EVID-004880": ("both_or_context_dependent", "NODE03176", "PMID:36668954; PMCID:PMC9864966"),
        "M21B-EVID-004881": ("soluble", "NODE03176", "PMID:40333123; PMCID:PMC12030537; DOI:10.3390/pathogens14040354"),
        "M21B-EVID-004882": ("soluble", "NODE04622", "PMID:26332726; DOI:10.1111/pim.12273"),
        "M21B-EVID-004883": ("soluble", "NODE04622", "PMID:23927077; DOI:10.1111/pim.12058; PMID:26332726; DOI:10.1111/pim.12273"),
        "M21B-EVID-004889": ("soluble", "NODE10043", "PMID:36063565; DOI:10.1016/j.imbio.2022.152263"),
        "M21B-EVID-004890": ("soluble", "NODE10043", "PMID:36063565; DOI:10.1016/j.imbio.2022.152263"),
        "M21B-EVID-005409": ("soluble", "NODE01898", "PMID:17182621; DOI:10.1074/jbc.M608342200; PMID:22461623"),
        "M21B-EVID-005455": ("soluble", "NODE03765", "PMID:34016966; PMCID:PMC8137956; DOI:10.1038/s41467-021-22579-1"),
        "M21B-EVID-005528": ("ecm_retained", "NODE07224", "PMID:16105980"),
        "M21B-EVID-006140": ("soluble", "NODE03246", "PMID:29981429; PMID:30261040; PMID:32978170"),
        "M21B-EVID-006220": ("soluble", "NODE03547", "PMID:10037797"),
        "M21B-EVID-006674": ("soluble", "NODE11512", "PMID:22884297; PMCID:PMC3466361; DOI:10.1016/j.jneuroim.2012.07.009"),
        "M21B-EVID-006687": ("soluble", "NODE02328", "PMID:11956183; DOI:10.1074/jbc.M107583200"),
        "M21B-EVID-006688": ("soluble", "NODE02328", "PMID:11956183; DOI:10.1074/jbc.M107583200"),
        "M21B-EVID-006689": ("soluble", "NODE02328", "PMID:11956183; DOI:10.1074/jbc.M107583200"),
        "M21B-EVID-006946": ("membrane_bound", "NODE06594", "PMID:7594541; PMID:7916655"),
        "M23B-EVID-001602": ("ecm_retained", "NODE02392", "PMID:2269670; PMCID:PMC2116373; DOI:10.1083/jcb.111.6.3177; PMID:8305732; PMCID:PMC275746; DOI:10.1091/mbc.4.11.1097; local:data/raw/evidence/module23a_review_led_20260904/collagen_vi_ng2_interaction_fulltext.html; local:data/raw/evidence/module23a_review_led_20260904/collagen_vi_ng2_interaction_pubmed.xml; local:data/raw/evidence/module23a_review_led_20260904/collagen_vi_ng2_fulltext.html; local:data/raw/evidence/module23a_review_led_20260904/collagen_vi_ng2_pubmed.xml"),
        "M21B-EVID-000391": ("soluble", "NODE05421", "PMID:12513909; PMID:12087100"),
        "M21B-EVID-000770": ("soluble", "NODE10179", "PMID:18922901"),
        "M21B-EVID-000794": ("soluble", "NODE02075", "PMCID:PMC2323273"),
        "M21B-EVID-000898": ("soluble", "NODE11887", "PMID:30304675; PMCID:PMC6338448"),
        "M21B-EVID-000899": ("soluble", "NODE11895", "PMID:30304675; PMCID:PMC6338448"),
        "M21B-EVID-001428": ("membrane_bound", "NODE01457", "PMID:11955431"),
        "M21B-EVID-001429": ("soluble", "NODE01465", "PMID:14734749"),
        "M21B-EVID-001432": ("membrane_bound", "NODE04936", "PMID:16530040"),
        "M21B-EVID-001703": ("soluble", "NODE05231", "PMID:11412113; PMID:8511589; PMID:7744001"),
        "M21B-EVID-001707": ("both_or_context_dependent", "NODE11244", "PMID:21081755; PMID:7544915"),
        "M21B-EVID-002102": ("soluble", "NODE06379", "PMID:16990550; PMCID:PMC2840530"),
        "M21B-EVID-002112": ("soluble", "NODE06380", "PMID:20220021"),
        "M21B-EVID-002113": ("soluble", "NODE06381", "PMID:20220021"),
        "M21B-EVID-002835": ("soluble", "NODE06379", "PMID:20463223; PMCID:PMC6632578"),
        "M21B-EVID-002914": ("soluble", "NODE01123", "PMID:24133212; PMCID:PMC3843045"),
        "M21B-EVID-002915": ("soluble", "NODE04746", "PMID:12486241; PMCID:PMC139252"),
        "M21B-EVID-003053": ("soluble", "NODE04881", "PMID:23868935; PMCID:PMC3892666; DOI:10.1161/ATVBAHA.113.301893"),
        "M21B-EVID-004650": ("both_or_context_dependent", "NODE10567", "PMID:18768877; PMCID:PMC2774262; DOI:10.4049/jimmunol.181.6.4199"),
        "M21B-EVID-004651": ("both_or_context_dependent", "NODE10567", "PMID:18768877; PMCID:PMC2774262; DOI:10.4049/jimmunol.181.6.4199"),
        "M21B-EVID-005373": ("both_or_context_dependent", "NODE02894", "PMID:17533181; DOI:10.1161/CIRCRESAHA.106.135988"),
        "M21B-EVID-005378": ("membrane_bound", "NODE02575", "PMID:18606138"),
        "M21B-EVID-005379": ("membrane_bound", "NODE02575", "PMID:18606138"),
        "M21B-EVID-005380": ("membrane_bound", "NODE02575", "PMID:18606138"),
        "M21B-EVID-005396": ("soluble", "NODE10264", "PMID:28840375"),
        "M21B-EVID-005397": ("soluble", "NODE10262", "PMID:16172602"),
        "M21B-EVID-005559": ("soluble", "NODE03505", "PMID:30692635; PMID:37927213"),
        "M21B-EVID-005781": ("soluble", "NODE10547", "PMID:21788491; PMCID:PMC3156217; DOI:10.1073/pnas.1104977108"),
        "M21B-EVID-006123": ("soluble", "NODE00445", "PMID:25331893; DOI:10.1073/pnas.1414841111"),
        "M21B-EVID-006124": ("soluble", "NODE00446", "PMID:25331893; DOI:10.1073/pnas.1414841111"),
        "M21B-EVID-006158": ("soluble", "NODE02119", "PMID:38503280; DOI:10.1016/j.cell.2024.02.024"),
        "M21B-EVID-006165": ("soluble", "NODE09080", "PMID:37438365; PMCID:PMC10338493; DOI:10.1038/s41467-023-39881-9"),
        "M21B-EVID-006208": ("both_or_context_dependent", "NODE03620", "PMID:35348113; PMCID:PMC8986318; DOI:10.7554/eLife.75545"),
        "M21B-EVID-006465": ("both_or_context_dependent", "NODE02575", "PMID:18606138; DOI:10.1016/j.devcel.2008.05.007"),
        "M21B-EVID-006514": ("soluble", "NODE01434", "PMID:16600989"),
        "M21B-EVID-006586": ("soluble", "NODE02045", "PMID:25080593; PMCID:PMC4115139"),
        "M21B-EVID-006587": ("soluble", "NODE02045", "PMID:25080593; PMCID:PMC4115139"),
        "M21B-EVID-006608": ("soluble", "NODE06632", "PMID:36178190; PMCID:PMC9578707; DOI:10.7554/eLife.81398"),
        "M21B-EVID-006609": ("soluble", "NODE08317", "PMID:36178190; PMCID:PMC9578707; DOI:10.7554/eLife.81398"),
        "M21B-EVID-006610": ("soluble", "NODE11809", "PMID:36178190; PMCID:PMC9578707; DOI:10.7554/eLife.81398"),
        "M21B-EVID-006611": ("soluble", "NODE10108", "PMID:36178190; PMCID:PMC9578707; DOI:10.7554/eLife.81398"),
        "M21B-EVID-006615": ("soluble", "NODE10487", "PMID:36178190; PMCID:PMC9578707; DOI:10.7554/eLife.81398"),
        "M21B-EVID-006642": ("soluble", "NODE03110", "PMID:19503073; DOI:10.1038/ncb1896"),
        "M21B-EVID-006643": ("soluble", "NODE03110", "PMID:19503073; DOI:10.1038/ncb1896"),
        "M21B-EVID-006644": ("soluble", "NODE03110", "PMID:19503073; DOI:10.1038/ncb1896"),
        "M21B-EVID-006911": ("ecm_retained", "NODE08357", "PMID:21200028; PMCID:PMC3019558; DOI:10.1083/jcb.201009136"),
        "M21B-EVID-006912": ("ecm_retained", "NODE00776", "PMID:21200028; PMCID:PMC3019558; DOI:10.1083/jcb.201009136"),
        "M21B-EVID-000824": ("soluble", "NODE09969", "PMID:24952599; PMCID:PMC4102805"),
        "M21B-EVID-008802": ("soluble", "NODE05097", "PMID:10948192"),
        "M21B-EVID-001700": ("soluble", "NODE05292", "PMID:10948192; PMID:11141475"),
        "M21B-EVID-002817": ("membrane_bound", "NODE01462", "PMID:7868901; PMID:11352728"),
        "M21B-EVID-002900": ("membrane_bound", "NODE06989", "PMID:11239445; DOI:10.1016/S1074-7613(01)00095-4"),
        "M21B-EVID-002901": ("membrane_bound", "NODE11575", "PMID:11239445; PMID:11777960; DOI:10.4049/jimmunol.168.2.671"),
        "M21B-EVID-002903": ("membrane_bound", "NODE11577", "PMID:11239445; PMID:11777960; DOI:10.4049/jimmunol.168.2.671"),
        "M21B-EVID-003194": ("membrane_bound", "NODE03982", "PMID:16362042; PMID:8621659"),
        "M21B-EVID-005513": ("ecm_retained", "NODE11857", "PMID:27157618; DOI:10.1038/onc.2016.149; PMCID:PMC5346747"),
        "M21B-EVID-006080": ("ecm_retained", "NODE03620", "PMID:23124902; PMCID:PMC3656602; DOI:10.1371/journal.pone.0056142"),
        "M21B-EVID-006201": ("ecm_retained", "NODE03620", "PMID:9462693; DOI:10.1002/(SICI)1097-4652(199803)174:3<310::AID-JCP5>3.0.CO;2-R"),
        "M21B-EVID-006202": ("ecm_retained", "NODE03642", "PMID:9531542; PMCID:PMC316674; DOI:10.1101/gad.12.7.1058"),
        "M21B-EVID-006203": ("ecm_retained", "NODE03652", "PMID:9531542; PMCID:PMC316674; DOI:10.1101/gad.12.7.1058"),
        "M21B-EVID-006212": ("ecm_retained", "NODE03599", "PMID:17959718; DOI:10.1016/j.devcell.2007.09.017"),
        "M21B-EVID-006213": ("ecm_retained", "NODE03599", "PMID:17959718; DOI:10.1016/j.devcell.2007.09.017"),
        "M21B-EVID-006502": ("membrane_bound", "NODE00255", "PMID:19389207; DOI:10.1111/j.1537-2995.2008.01978.x"),
        "M21B-EVID-006668": ("ecm_retained", "NODE04678", "PMID:11830493"),
        "M21B-EVID-003784": ("membrane_bound", "NODE08875", "PMID:18215137; PMID:17616532"),
        "M21B-EVID-000779": ("both_or_context_dependent", "NODE09762", "PMID:16103117; PMID:18335997; PMCID:PMC2819367"),
        "M21B-EVID-000780": ("membrane_bound", "NODE09762", "PMID:18287331; PMID:18335997; PMCID:PMC2819367"),
        "M21B-EVID-002453": ("membrane_bound", "NODE06638", "PMID:19246390; PMCID:PMC2657456"),
        "M21B-EVID-002563": ("membrane_bound", "NODE10786", "PMID:24662763"),
        "M21B-EVID-002564": ("membrane_bound", "NODE10786", "PMID:24662763"),
        "M21B-EVID-002783": ("membrane_bound", "NODE06661", "PMID:12060703; PMID:17537914; PMCID:PMC1891256; PMID:18566392; PMCID:PMC2507881"),
        "M21B-EVID-002899": ("membrane_bound", "NODE06988", "PMID:10426993; PMID:11955595; DOI:10.1126/science.285.5428.727"),
        "M21B-EVID-003132": ("membrane_bound", "NODE02051", "PMID:26483485; PMCID:PMC4640789; DOI:10.1073/pnas.1511617112; PMID:11590190; PMID:11095950"),
        "M21B-EVID-005174": ("membrane_bound", "NODE08455", "PMID:41248277; PMCID:PMC12663928; DOI:10.1073/pnas.2517436122; https://pubmed.ncbi.nlm.nih.gov/41248277/"),
        "M21B-EVID-005175": ("membrane_bound", "NODE08405", "PMID:41248277; PMCID:PMC12663928; DOI:10.1073/pnas.2517436122; https://pubmed.ncbi.nlm.nih.gov/41248277/"),
        "M21B-EVID-005791": ("membrane_bound", "NODE03084", "PMID:12496762; DOI:10.1038/nn994"),
        "M21B-EVID-005798": ("membrane_bound", "NODE02295", "PMID:14567914; DOI:10.1016/S0092-8674(03)00810-9"),
        "M21B-EVID-006117": ("soluble", "NODE00374", "PMID:25646014; PMCID:PMC4710371; DOI:10.1158/1535-7163.MCT-14-0470"),
        "M21B-EVID-006121": ("membrane_bound", "NODE05998", "PMID:27309808; DOI:10.1038/nature18596"),
        "M21B-EVID-006137": ("membrane_bound", "NODE03088", "PMID:33436772; PMCID:PMC7804096"),
        "M21B-EVID-006376": ("membrane_bound", "NODE01493", "PMID:39768175; PMCID:PMC11674933; DOI:10.3390/cells13242083"),
        "M21B-EVID-006460": ("membrane_bound", "NODE11432", "PMID:36399563; PMCID:PMC9674301; DOI:10.1126/scitranslmed.abq4077"),
        "M21B-EVID-006467": ("soluble", "NODE08260", "PMID:10748068; DOI:10.1074/jbc.M002254200"),
        "M21B-EVID-006468": ("membrane_bound", "NODE00607", "PMID:21238923; PMCID:PMC6775579"),
        "M21B-EVID-006556": ("soluble", "NODE04758", "PMID:16809620; DOI:10.1182/blood-2005-12-019919"),
        "M21B-EVID-006716": ("both_or_context_dependent", "NODE10124", "PMID:21813734; PMCID:PMC3183016; DOI:10.1371/journal.pone.0021952"),
        "M21B-EVID-006941": ("both_or_context_dependent", "NODE02887", "PMID:21419176; DOI:10.1016/j.bbamcr.2011.03.004"),
        "M23B-EVID-001546": ("membrane_bound", "NODE03078", "PMID:9053851; DOI:10.1038/sj.onc.1200857; local:data/raw/evidence/module23a_review_led_20260904/efna2_epha8_activation_pubmed.xml"),
        "M21B-EVID-006667": ("membrane_bound", "NODE03728", "PMID:26633812; PMCID:PMC4737655; DOI:10.7554/eLife.08149"),
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
