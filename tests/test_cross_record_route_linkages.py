import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "build_cross_record_route_linkages.py"
SPEC = importlib.util.spec_from_file_location("build_cross_record_route_linkages", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def route_row(**overrides):
    row = {
        "route_evidence_id": "BASE:000001",
        "ligand_node_id": "L1",
        "ligand_label": "Ligand",
        "ligand_receptor_edge_id": "EDGE:LR1",
        "receptor_node_id": "R1",
        "receptor_label": "Receptor",
        "known_layers": "ligand|receptor",
        "evidence_ids": "EVID:1",
        "source_queue_id": "QUEUE:1",
        "source_evidence_record_id": "RECORD:1",
        "intracellular_continuation_node_id": "",
        "intracellular_continuation_label": "",
        "receptor_intracellular_edge_id": "",
        "transcription_factor_node_id": "",
        "transcription_factor_label": "",
        "output_label": "",
        "target_gene_label": "",
    }
    row.update(overrides)
    return row


def test_composes_exact_lr_rows_with_shared_evidence_anchor():
    rows = [
        route_row(
            route_evidence_id="BASE:I",
            known_layers="ligand|receptor|intracellular_continuation",
            intracellular_continuation_node_id="I1",
            intracellular_continuation_label="JAK1",
            receptor_intracellular_edge_id="EDGE:RI1",
            source_queue_id="QUEUE:I",
            source_evidence_record_id="RECORD:I",
        ),
        route_row(
            route_evidence_id="BASE:TF",
            known_layers="ligand|receptor|transcription_factor|output",
            transcription_factor_node_id="TF1",
            transcription_factor_label="STAT3",
            output_label="reporter response",
            source_queue_id="QUEUE:TF",
            source_evidence_record_id="RECORD:TF",
        ),
    ]

    additions, summary = MODULE.compose_routes(rows)

    assert summary["cross_record_route_rows_added"] == 1
    assert summary["distinct_ligand_receptor_edges_linked"] == 1
    assert len(additions) == 1
    addition = additions[0]
    assert addition["known_layers"] == "ligand|receptor|intracellular_continuation|transcription_factor|output"
    assert addition["missing_layers"] == "target_gene_expression"
    assert addition["intracellular_tf_edge_id"] == ""
    assert addition["source_evidence_record_id"] == "RECORD:TF"
    assert "RECORD:I+RECORD:TF" in addition["source_chain_id"]


def test_does_not_compose_independent_evidence_packets():
    rows = [
        route_row(
            known_layers="ligand|receptor|intracellular_continuation",
            intracellular_continuation_node_id="I1",
            receptor_intracellular_edge_id="EDGE:RI1",
            evidence_ids="EVID:intracellular",
        ),
        route_row(
            known_layers="ligand|receptor|transcription_factor|output",
            transcription_factor_node_id="TF1",
            output_label="reporter response",
            evidence_ids="EVID:tf-output",
        ),
    ]

    additions, summary = MODULE.compose_routes(rows)

    assert additions == []
    assert summary["cross_record_route_rows_added"] == 0
