from pathlib import Path

from scripts.audit_full_signaling_chains import (
    build_downstream_curation_queue,
    classify_lr_candidate,
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


def test_module21b_downstream_queue_is_evidence_backed():
    bundle = Path(__file__).parents[1] / "data" / "processed" / "mechanism_graph_module20_24_v2026_09_15"
    rows, summary = build_downstream_curation_queue(bundle)
    assert len(rows) == 3298
    assert summary["queue_records_with_output_terms"] == 2275
    assert summary["queue_records_with_text_matched_tf"] == 85
    assert summary["queue_records_with_text_matched_target_gene"] == 20
    assert {row["curation_status"] for row in rows} == {"pending_manual_curation"}
    assert all(row["evidence_summary"] and row["source_locator"] for row in rows)
