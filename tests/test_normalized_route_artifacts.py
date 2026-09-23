from scripts.route_artifacts import build_normalized_route_artifacts


def _node(node_id: str, label: str, node_type: str) -> dict[str, str]:
    return {
        "node_id": node_id,
        "canonical_name": label,
        "canonical_label": label,
        "node_type": node_type,
    }


def _edge(edge_id: str, source: str, target: str, relation: str = "activates") -> dict[str, str]:
    return {
        "edge_id": edge_id,
        "source_node_id": source,
        "target_node_id": target,
        "relation_type": relation,
        "evidence_status": "primary_support",
    }


def test_normalized_route_preserves_shared_intermediates_and_missing_links():
    nodes = [
        _node("L", "IL1B", "ligand"),
        _node("R", "IL1R1/IL1RAP", "receptor"),
        _node("M", "MYD88", "signaling_effector"),
        _node("I", "IRAK4", "signaling_effector"),
        _node("B", "NF-kappaB branch", "signaling_effector"),
        _node("T", "NF-kB", "transcription_factor"),
        _node("G", "IL6 gene", "target_gene"),
    ]
    edges = [
        _edge("E1", "L", "R", "binds_receptor"),
        _edge("E2", "R", "M", "recruits"),
        _edge("E3", "M", "I", "recruits"),
        _edge("E4", "I", "B", "activates"),
        _edge("E5", "L", "G", "activates"),
    ]
    route = {
        "route_evidence_id": "LITEXP:1",
        "ligand_node_id": "L",
        "receptor_node_id": "R",
        "intracellular_continuation_node_id": "M",
        "transcription_factor_node_id": "T",
        "target_gene_node_id": "G",
        "source_chain_id": "E1>E2>E3>E4>TF:T>E5",
        "route_linkage_status": "tf_to_target_edge_not_asserted",
        "evidence_ids": "OBS1",
    }

    route_nodes, route_edges = build_normalized_route_artifacts(routes=[route], nodes=nodes, edges=edges)

    assert [row["node_id"] for row in route_nodes] == ["L", "R", "M", "I", "B", "T", "G"]
    assert [row["edge_id"] for row in route_edges[:4]] == ["E1", "E2", "E3", "E4"]
    assert [(row["source_node_id"], row["target_node_id"], row["edge_role"]) for row in route_edges[4:6]] == [
        ("B", "T", "intracellular_to_tf_missing"),
        ("T", "G", "tf_to_target_missing"),
    ]
    assert route_edges[-1]["edge_id"] == "E5"
    assert route_edges[-1]["edge_role"] == "output_observation"
    assert all(row["causal_status"] == "not_asserted" for row in route_edges)
