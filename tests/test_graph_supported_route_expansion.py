import csv
import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "build_graph_supported_route_expansion.py"
SPEC = importlib.util.spec_from_file_location("graph_supported_route_expansion", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


ROUTE_FIELDS = [
    "route_evidence_id", "route_status", "route_tier", "path_expression", "known_layers",
    "missing_layers", "intracellular_status", "ligand_node_id", "ligand_label",
    "ligand_receptor_edge_id", "receptor_node_id", "receptor_label",
    "receptor_intracellular_edge_id", "intracellular_continuation_node_id",
    "intracellular_continuation_label", "intracellular_tf_edge_id",
    "transcription_factor_node_id", "transcription_factor_label", "tf_target_edge_id",
    "target_gene_node_id", "target_gene_label", "target_output_form_id", "output_node_id",
    "output_label", "output_form_id", "bridge_id", "pathway_name", "input_evidence_type",
    "output_evidence_type", "evidence_ids", "source_queue_id", "source_evidence_record_id",
    "route_linkage_status", "causal_status", "traversal_status", "source_chain_id",
    "evidence_contract_version", "evidence_polarity", "negative_evidence_status",
    "evidence_directness", "output_class", "species_context", "cell_type_context",
    "compartment_context", "injury_context", "context_scope", "assay_or_perturbation",
    "effect_polarity", "source_scope",
]


def edge(edge_id, source, target, pathway, relation, layer, target_label, *, evidence="E1"):
    return {
        "edge_id": edge_id,
        "source_node_id": source,
        "target_node_id": target,
        "pathway_label": pathway,
        "relation_type": relation,
        "effect_polarity": "activating",
        "species_context": "mouse",
        "cell_type_context": "test cells",
        "compartment_context": "test compartment",
        "injury_context": "test context",
        "evidence_status": "primary",
        "context_scope": "test scope",
        "module": "21B",
        "source_label": source,
        "target_label": target_label,
        "pathway_name": pathway,
        "evidence_layer": layer,
        "edge_status": "supported",
        "evidence_ids": evidence,
    }


def write_tsv(path, fields, rows):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def synthetic_bundle(tmp_path, *, unrelated_output=False):
    bundle = tmp_path / "bundle"
    bundle.mkdir()
    nodes = [
        {"node_id": "L", "canonical_name": "Ligand", "node_type": "ligand"},
        {"node_id": "R", "canonical_name": "Receptor", "node_type": "receptor"},
        {"node_id": "J", "canonical_name": "JAK1", "node_type": "signaling_effector"},
        {"node_id": "T", "canonical_name": "STAT1", "node_type": "transcription_factor"},
        {"node_id": "G", "canonical_name": "Target gene", "node_type": "signaling_effector"},
        {"node_id": "O", "canonical_name": "Secreted output", "node_type": "signaling_effector"},
    ]
    write_tsv(bundle / "mechanism_nodes.tsv", list(nodes[0]), nodes)
    roles = [
        {"node_id": "L", "role": "ligand"},
        {"node_id": "R", "role": "receptor"},
        {"node_id": "T", "role": "transcription_factor"},
        {"node_id": "G", "role": "target_gene"},
    ]
    write_tsv(bundle / "mechanism_node_roles.tsv", ["node_id", "role"], roles)
    output_pathway = "OTHER-PATH" if unrelated_output else "P-JAK-STAT-LIGAND"
    edges = [
        edge("LR", "L", "R", "P-JAK-STAT", "binds_receptor", "ligand_receptor_or_direct_molecular", "Receptor", evidence="E-LR"),
        edge("RELAY", "R", "J", "P-JAK-STAT", "activates", "receptor_proximal_or_pathway", "JAK1", evidence="E-RELAY"),
        edge("RTF", "R", "T", "P-JAK-STAT", "activates", "receptor_proximal_or_pathway", "STAT1", evidence="E-RTF"),
        edge("TGT", "T", "G", "P-JAK-STAT-TF1-GENE", "regulates_target_gene", "downstream_or_functional", "Target gene", evidence="E-TGT"),
        edge("LOUT", "L", "O", output_pathway, "supports", "downstream_or_functional", "Secreted output", evidence="E-LOUT"),
        edge("LGENE", "L", "G", "P-JAK-STAT-LIGAND-GENE", "supports", "downstream_or_functional", "Target gene", evidence="E-LGENE"),
    ]
    write_tsv(bundle / "mechanism_edges.tsv", list(edges[0]), edges)
    route = {field: "" for field in ROUTE_FIELDS}
    route.update({"route_evidence_id": "ROUTE:00001", "route_status": "retained_evidence_route"})
    return bundle, [route]


def test_composes_only_anchor_compatible_routes(tmp_path):
    bundle, rows = synthetic_bundle(tmp_path)
    additions, summary = MODULE.compose_graph_routes(rows, bundle)

    assert summary["graph_supported_route_rows_added"] == len(additions)
    assert {row["route_tier"] for row in additions} == {
        "ligand_receptor_output_missing_intracellular_and_tf",
        "ligand_receptor_intracellular_output_missing_tf",
        "ligand_receptor_tf_target_missing_intracellular",
        "explicit_ligand_receptor_intracellular_tf_target",
    }
    assert all(row["causal_status"] == "not_asserted" for row in additions)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in additions)
    relayed_tf_rows = [
        row for row in additions
        if row["intracellular_continuation_node_id"] == "J"
        and row["transcription_factor_node_id"] == "T"
    ]
    assert relayed_tf_rows
    assert all(row["intracellular_tf_edge_id"] == "" for row in relayed_tf_rows)
    assert all("intracellular_to_tf_edge_not_asserted" in row["route_linkage_status"] for row in relayed_tf_rows)
    assert any(
        row["intracellular_continuation_node_id"] == "J"
        and row["transcription_factor_node_id"] == "T"
        and row["target_gene_node_id"] == "G"
        for row in additions
    )


def test_does_not_cross_product_unrelated_pathways(tmp_path):
    bundle, rows = synthetic_bundle(tmp_path, unrelated_output=True)
    additions, summary = MODULE.compose_graph_routes(rows, bundle)

    assert summary["graph_supported_route_rows_added"] == 4
    assert all(row["output_node_id"] == "G" for row in additions)
    assert not any(row["output_node_id"] == "O" for row in additions)
