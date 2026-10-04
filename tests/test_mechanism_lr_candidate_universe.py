import csv
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.build_mechanism_lr_candidate_universe import (  # noqa: E402
    graph_indexes,
    index_nodes,
    main,
)


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.write_text(
        "\t".join(fields) + "\n"
        + "\n".join("\t".join(row.get(field, "") for field in fields) for row in rows)
        + "\n"
    )


def test_candidate_projection_preserves_candidates_and_does_not_create_edges(tmp_path, monkeypatch):
    graph = tmp_path / "graph"
    method = tmp_path / "method"
    output = tmp_path / "candidate"
    graph.mkdir()
    method.mkdir()
    (graph / "bundle_metadata.json").write_text(json.dumps({"release_id": "graph:test"}))
    write_tsv(
        graph / "mechanism_nodes.tsv",
        ["node_id", "canonical_name", "canonical_label", "gene_symbol"],
        [
            {"node_id": "NODE1", "canonical_name": "L1", "canonical_label": "L1", "gene_symbol": ""},
            {"node_id": "NODE2", "canonical_name": "R1", "canonical_label": "R1", "gene_symbol": ""},
        ],
    )
    write_tsv(
        graph / "mechanism_edges.tsv",
        ["edge_id", "source_node_id", "target_node_id", "source_label", "target_label", "relation_type", "exportable"],
        [{
            "edge_id": "EDGE1", "source_node_id": "NODE1", "target_node_id": "NODE2",
            "source_label": "L1", "target_label": "R1", "relation_type": "binds_receptor", "exportable": "true",
        }],
    )
    write_tsv(
        method / "canonical_communication_records.tsv",
        [
            "canonical_communication_id", "species_scope", "ligand_name", "receptor_name",
            "normalized_ligand_name", "normalized_receptor_name", "communication_kind", "evidence_status",
            "source_method_count", "source_record_count", "source_methods_json", "normalization_notes",
        ],
        [
            {
                "canonical_communication_id": "PAIR1", "species_scope": "mouse", "ligand_name": "L1",
                "receptor_name": "R1", "normalized_ligand_name": "l1", "normalized_receptor_name": "r1",
                "communication_kind": "direct_lr_candidate", "evidence_status": "method_resource_only",
                "source_method_count": "1", "source_record_count": "1", "source_methods_json": '["liana"]',
            },
            {
                "canonical_communication_id": "PAIR2", "species_scope": "mouse", "ligand_name": "L2",
                "receptor_name": "R2", "normalized_ligand_name": "L2", "normalized_receptor_name": "R2",
                "communication_kind": "direct_lr_candidate", "evidence_status": "method_resource_only",
                "source_method_count": "1", "source_record_count": "1", "source_methods_json": '["nichenet"]',
            },
        ],
    )
    write_tsv(
        method / "method_resource_records.tsv",
        [
            "resource_key", "canonical_communication_id", "source_record_key", "source_record_key_kind",
            "record_kind", "native_ligand", "native_receptor", "normalized_ligand", "normalized_receptor",
            "original_values_json", "normalized_values_json", "transform_notes", "evidence_status", "method_score_json",
        ],
        [
            {"resource_key": "resource:liana", "canonical_communication_id": "PAIR1", "source_record_key": "row:1", "record_kind": "direct_lr_candidate"},
            {"resource_key": "resource:nichenet", "canonical_communication_id": "PAIR2", "source_record_key": "row:2", "record_kind": "direct_lr_candidate"},
        ],
    )
    write_tsv(
        method / "method_resource_complex_components.tsv",
        ["resource_key", "source_record_key", "record_kind", "canonical_communication_id", "side", "component_name", "component_ordinal", "source_field_name", "original_component_value", "notes"],
        [],
    )
    (method / "method_resource_migration_report.json").write_text(json.dumps({
        "source_snapshot_id": "snapshot:test", "canonical_communication_count": 2,
    }))

    monkeypatch.setattr(sys, "argv", ["build_mechanism_lr_candidate_universe.py", "--graph-bundle-dir", str(graph), "--method-migration-dir", str(method), "--output-dir", str(output)])
    assert main() == 0
    rows = (output / "mechanism_lr_candidate_universe.tsv").read_text().splitlines()
    assert len(rows) == 3
    assert "validated_exportable_core_edge" in rows[1]
    assert "staged_unresolved" in rows[2]
    report = json.loads((output / "mechanism_lr_candidate_universe_report.json").read_text())
    assert report["graph_edges_created"] is False
    assert report["canonical_communication_count"] == 2
    assert report["graph_label_resolution"]["case_insensitive_edge_recovery_count"] == 1
    assert report["graph_label_resolution"]["case_insensitive_node_recovery_count"] == 2


def test_graph_label_indexes_casefold_without_collapsing_ambiguous_nodes():
    nodes = [
        {"node_id": "NODE1", "canonical_name": "A2M", "canonical_label": "", "gene_symbol": ""},
        {"node_id": "NODE2", "canonical_name": "a2m", "canonical_label": "", "gene_symbol": ""},
    ]
    edges = [
        {
            "edge_id": "EDGE1",
            "source_node_id": "NODE1",
            "target_node_id": "NODE3",
            "source_label": "A2M",
            "target_label": "MMP9",
            "relation_type": "binds_receptor",
        }
    ]
    assert index_nodes(nodes)["a2m"] == {"NODE1", "NODE2"}
    assert ("a2m", "mmp9") in graph_indexes(edges, nodes)


def test_candidate_projection_reconciles_cellchat_native_json_variants(tmp_path, monkeypatch):
    graph = tmp_path / "graph"
    method = tmp_path / "method"
    output = tmp_path / "candidate"
    graph.mkdir()
    method.mkdir()
    (method / "method_native").mkdir()
    (graph / "bundle_metadata.json").write_text(json.dumps({"release_id": "graph:test"}))
    write_tsv(
        graph / "mechanism_nodes.tsv",
        ["node_id", "canonical_name", "canonical_label", "gene_symbol"],
        [],
    )
    write_tsv(
        graph / "mechanism_edges.tsv",
        ["edge_id", "source_node_id", "target_node_id", "source_label", "target_label", "relation_type", "exportable"],
        [],
    )
    write_tsv(
        method / "canonical_communication_records.tsv",
        [
            "canonical_communication_id", "species_scope", "ligand_name", "receptor_name",
            "normalized_ligand_name", "normalized_receptor_name", "communication_kind", "evidence_status",
            "source_method_count", "source_record_count", "source_methods_json", "normalization_notes",
        ],
        [
            {
                "canonical_communication_id": "PAIR1", "species_scope": "mouse", "ligand_name": "Tgfbr1",
                "receptor_name": "Tgfbr2", "normalized_ligand_name": "Tgfbr1", "normalized_receptor_name": "Tgfbr2",
                "communication_kind": "direct_lr_candidate", "evidence_status": "method_resource_only",
                "source_method_count": "1", "source_record_count": "1", "source_methods_json": '["cellchat"]',
            },
            {
                "canonical_communication_id": "PAIR2", "species_scope": "mouse", "ligand_name": "Inhba_Inhbb",
                "receptor_name": "Acvr2a", "normalized_ligand_name": "Inhba_Inhbb", "normalized_receptor_name": "Acvr2a",
                "communication_kind": "direct_lr_candidate", "evidence_status": "method_resource_only",
                "source_method_count": "1", "source_record_count": "1", "source_methods_json": '["cellchat"]',
            },
        ],
    )
    write_tsv(
        method / "method_resource_records.tsv",
        [
            "resource_key", "canonical_communication_id", "source_record_key", "source_record_key_kind",
            "record_kind", "native_ligand", "native_receptor", "normalized_ligand", "normalized_receptor",
            "original_values_json", "normalized_values_json", "transform_notes", "evidence_status", "method_score_json",
        ],
        [
            {
                "resource_key": "mscs_phase2:cellchat_mouse.tsv", "canonical_communication_id": "PAIR1",
                "source_record_key": "TGFbR1_TGFbR2", "record_kind": "direct_lr_candidate",
                "native_ligand": "Tgfbr1", "native_receptor": "Tgfbr2",
            },
            {
                "resource_key": "mscs_phase2:cellchat_mouse.tsv", "canonical_communication_id": "PAIR2",
                "source_record_key": "Activin_AB_ACVR2A", "record_kind": "direct_lr_candidate",
                "native_ligand": "Inhba_Inhbb", "native_receptor": "Acvr2a",
            },
        ],
    )
    write_tsv(
        method / "method_resource_complex_components.tsv",
        ["resource_key", "source_record_key", "record_kind", "canonical_communication_id", "side", "component_name", "component_ordinal", "source_field_name", "original_component_value", "notes"],
        [],
    )
    (method / "method_resource_migration_report.json").write_text(json.dumps({
        "source_snapshot_id": "snapshot:test", "canonical_communication_count": 2,
    }))
    (method / "method_native" / "CellChatDB.mouse.standalone.json").write_text(json.dumps({
        "interactions": [
            {"interaction_name": "TGFbR1_TGFbR2", "ligand": "TGFbR1_R2", "receptor": "Tgfbr2"},
            {"interaction_name": "Activin_AB_ACVR2A", "ligand": "Activin AB", "receptor": "Acvr2a"},
        ],
        "complexes": {
            "TGFbR1_R2": ["Tgfbr1", "Tgfbr2"],
            "Activin AB": ["Inhba", "Inhbb"],
        },
    }))

    monkeypatch.setattr(sys, "argv", [
        "build_mechanism_lr_candidate_universe.py", "--graph-bundle-dir", str(graph),
        "--method-migration-dir", str(method), "--output-dir", str(output),
    ])
    assert main() == 0
    with (output / "mechanism_lr_candidate_universe.tsv").open(newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    assert len(rows) == 2
    assert rows[0]["cellchat_json_pair_variants_json"]
    variants = json.loads(rows[0]["cellchat_json_pair_variants_json"])
    assert variants[0]["representation"] == "CellChatDB.mouse.standalone.json"
    assert variants[0]["ligand_components"] == "Tgfbr1|Tgfbr2"
    report = json.loads((output / "mechanism_lr_candidate_universe_report.json").read_text())
    reconciliation = report["cellchat_json_reconciliation"]
    assert reconciliation["status"] == "complete"
    assert reconciliation["source_record_count"] == 2
    assert reconciliation["source_record_coverage"] == 1.0
    assert reconciliation["json_pair_key_coverage"] == 1.0
    assert reconciliation["json_only_canonical_pair_key_count"] == 2
    assert report["schema_version"] == "mechanism_lr_candidate_universe_v3"
