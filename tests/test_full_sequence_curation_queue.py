from scripts.build_full_sequence_curation_queue import build_queue


def test_full_sequence_queue_aggregates_outputs_without_asserting_missing_links():
    base = {
            "route_evidence_id": "ROUTE:1",
            "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
            "path_expression": "ligand>receptor>intracellular>TF>output",
            "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
            "missing_layers": "target_gene_expression",
            "ligand_node_id": "L",
            "ligand_label": "IL1B",
            "ligand_receptor_edge_id": "LR",
            "receptor_node_id": "R",
            "receptor_label": "IL1R1",
            "receptor_intracellular_edge_id": "RI",
            "intracellular_continuation_node_id": "I",
            "intracellular_continuation_label": "MYD88",
            "intracellular_tf_edge_id": "",
            "transcription_factor_node_id": "T",
            "transcription_factor_label": "NF-kB",
            "tf_target_edge_id": "",
            "target_gene_node_id": "",
            "target_gene_label": "",
            "output_label": "secreted cytokine",
            "output_node_id": "O1",
            "pathway_name": "IL1B-NF-kB",
            "evidence_ids": "E1;RI",
            "source_chain_id": "CHAIN:1",
            "source_scope": "direct_edge",
            "route_linkage_status": "intracellular_to_tf_edge_not_asserted",
    }
    routes = [
        base,
        {
            **base,
            "route_evidence_id": "ROUTE:2",
            "output_label": "ICAM1 transcription",
            "output_node_id": "O2",
            "evidence_ids": "E2;RI",
            "source_chain_id": "CHAIN:2",
        },
    ]
    rows, summary = build_queue(routes, [])

    assert len(rows) == 1
    assert rows[0]["route_count"] == "2"
    assert rows[0]["output_node_ids"] == "O1;O2"
    assert rows[0]["source_chain_ids"] == "CHAIN:1;CHAIN:2"
    assert rows[0]["review_priority"] == "P1"
    assert summary["curation_candidate_count"] == 1
