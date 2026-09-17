from __future__ import annotations

from scripts.mechanism_evidence_contract import (
    MECHANISM_EVIDENCE_CONTRACT_VERSION,
    classify_evidence_polarity,
    classify_negative_evidence_status,
    evidence_directness,
    normalize_output_class,
)


def test_output_classes_preserve_generic_readouts_without_promoting_targets():
    assert normalize_output_class(record_type="target_gene_output_evidence", target_gene="Il6") == "target_gene_expression"
    assert normalize_output_class(output_term="protein_secretion_or_release") == "secreted_protein_or_release"
    assert normalize_output_class(output_term="phagocytosis_or_engulfment") == "phagocytosis_or_engulfment"
    assert normalize_output_class(output_term="cellular_function_assay") == "cellular_functional_readout"
    assert normalize_output_class(output_term="") == "unknown"


def test_polarity_does_not_confuse_an_inhibitory_biological_effect_with_negative_evidence():
    assert classify_evidence_polarity(
        ["direct_edge"],
        evidence_text="receptor activation inhibits complement",
    ) == "supports"
    assert classify_evidence_polarity(["negative_evidence"]) == "contradicts"
    assert classify_evidence_polarity(["direct_edge", "negative_evidence"]) == "mixed"
    assert classify_negative_evidence_status(["negative_evidence"]) == "not_supporting_requested_claim"


def test_directness_and_contract_version_are_explicit():
    assert evidence_directness("intracellular_cascade_evidence", "") == "explicit_exported_edge"
    assert evidence_directness("transcription_factor_evidence", "") == "exact_node_mention"
    assert evidence_directness("unresolved_downstream_claim", "") == "unresolved"
    assert MECHANISM_EVIDENCE_CONTRACT_VERSION == "mechanism_evidence_v1"
