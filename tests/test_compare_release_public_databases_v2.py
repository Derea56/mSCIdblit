from scripts.compare_release_public_databases_v2 import component_key, evidence_gate, label_key, metrics


def test_component_key_matches_common_complex_encodings():
    left = component_key("Tgfb1", "Tgfbr1_Tgfbr2")
    right = component_key(
        "TGFB1",
        "TGFBR1:TGFBR2 receptor complex",
        receptor_components="TGFBR1|TGFBR2",
    )
    assert left == right


def test_label_key_distinguishes_different_complex_membership():
    assert label_key("Tgfb1", "Tgfbr1_Tgfbr2") != label_key("Tgfb1", "Tgfbr1:Tgfbr3")


def test_metrics_reports_directional_coverage():
    result = metrics({"a", "b"}, {"b", "c"})
    assert result["overlap"] == 1
    assert result["mSCIdblit_coverage_of_public"] == 0.5
    assert result["public_coverage_of_mSCIdblit"] == 0.5


def test_public_locator_is_not_treated_as_verified_primary_evidence():
    assert evidence_gate({"evidence": "PMID:123456", "annotation": "", "citation_note": ""}) == "primary_locator_present_unverified"
    assert evidence_gate({"evidence": "KEGG:mmu04350", "annotation": "", "citation_note": ""}) == "no_primary_locator_in_public_snapshot"
