from pathlib import Path

from scripts.audit_full_signaling_chains import (
    build_downstream_evidence_records,
    build_downstream_curation_queue,
    build_route_evidence,
    classify_lr_candidate,
    label_matches_alias_patterns,
)


def test_classify_lr_candidate_exposes_receptor_proximal_edges():
    edge = {
        "source_node_id": "R",
        "source_label": "CSF1R/c-Fms",
        "target_label": "PI3K p85/p110",
        "register_relation_type": "recruits/activates",
        "relation_type": "binds_receptor",
        "evidence_layer": "ligand_receptor_binding_or_activation;downstream_or_functional",
        "compartment_context": "extracellular ligand to plasma-membrane receptor or receptor complex",
    }
    semantic_class, assessment = classify_lr_candidate(edge, {"R": {"receptor"}})
    assert semantic_class == "receptor_proximal_or_intracellular"
    assert assessment == "not_a_direct_ligand_receptor_pair"


def test_receptor_identity_alias_matching_avoids_substring_collisions():
    assert label_matches_alias_patterns("MPL/TPO receptor", (("mpl",),))
    assert not label_matches_alias_patterns("complement receptor", (("mpl",),))


def test_module21b_downstream_queue_is_evidence_backed():
    bundle = Path(__file__).parents[1] / "data" / "processed" / "mechanism_graph_module20_24_v2026_09_15"
    rows, summary = build_downstream_curation_queue(bundle)
    assert len(rows) == 3298
    assert summary["queue_records_with_output_terms"] == 2275
    assert summary["queue_records_with_text_matched_tf"] == 85
    assert summary["queue_records_with_text_matched_target_gene"] == 20
    assert {row["curation_status"] for row in rows} == {"pending_manual_curation"}
    assert all(row["evidence_summary"] and row["source_locator"] for row in rows)
    records, record_summary = build_downstream_evidence_records(rows)
    assert len(records) == 4692
    assert record_summary["record_type_counts"] == {
        "generic_output_evidence": 3318,
        "intracellular_cascade_evidence": 331,
        "target_gene_output_evidence": 20,
        "transcription_factor_evidence": 94,
        "unresolved_downstream_claim": 929,
    }
    assert all(row["source_evidence_ids"] for row in records)
    assert {row["causal_status"] for row in records} == {"not_asserted"}
    route_rows, route_summary = build_route_evidence(bundle, [], [], rows, records)
    route_record_ids = {
        record_id
        for row in route_rows
        for record_id in row["source_evidence_record_id"].split(";")
        if record_id
    }
    assert {row["record_id"] for row in records} <= route_record_ids
    assert route_summary["route_evidence_record_count"] > 10812
    assert route_summary["route_evidence_tier_counts"]["ligand_receptor_intracellular_output_missing_tf"] > 0
    assert route_summary["route_evidence_tier_counts"]["ligand_receptor_intracellular_tf_output_missing_target_gene"] > 0
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in route_rows)
