from __future__ import annotations

import gzip
import csv
import json
from pathlib import Path

from scripts.build_mscs_route_connectors import build_route_connectors


def test_route_connectors_preserve_partial_and_full_paths(tmp_path: Path) -> None:
    release = tmp_path / "release"
    graph = release / "mechanism_graph"
    graph.mkdir(parents=True)
    (release / "release_manifest.json").write_text(
        json.dumps({"release_id": "test-release:1"}) + "\n", encoding="utf-8"
    )
    columns = [
        "route_evidence_id", "route_status", "route_tier", "path_expression",
        "known_layers", "missing_layers", "intracellular_status", "ligand_node_id",
        "ligand_label", "ligand_receptor_edge_id", "receptor_node_id", "receptor_label",
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
    rows = [
        {column: "" for column in columns},
        {column: "" for column in columns},
    ]
    rows[0].update(route_evidence_id="R1", route_status="retained_evidence_route", ligand_node_id="L", receptor_node_id="R", intracellular_continuation_node_id="S", transcription_factor_node_id="TF", output_node_id="O")
    rows[1].update(route_evidence_id="R2", route_status="retained_evidence_route", ligand_node_id="L2", receptor_node_id="R2", missing_layers="output")
    source = graph / "mechanism_signaling_route_evidence.tsv.gz"
    with gzip.open(source, "wt", encoding="utf-8", newline="") as handle:
        handle.write("\t".join(columns) + "\n")
        for row in rows:
            handle.write("\t".join(row[column] for column in columns) + "\n")

    output = tmp_path / "connectors"
    manifest = build_route_connectors(release, output)
    assert manifest["counts"]["route_connectors"] == 2
    assert manifest["counts"]["by_route_class"] == {"l_r": 1, "l_r_s_tf_o": 1}
    with gzip.open(output / "route_connectors.tsv.gz", "rt", encoding="utf-8", newline="") as handle:
        rows = [
            (row["route_evidence_id"], row["route_class"], row["missing_layers"])
            for row in sorted(csv.DictReader(handle, delimiter="\t"), key=lambda row: row["route_evidence_id"])
        ]
    assert rows == [("R1", "l_r_s_tf_o", ""), ("R2", "l_r", "output")]
