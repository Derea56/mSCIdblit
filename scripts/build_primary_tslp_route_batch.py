#!/usr/bin/env python3
"""Build source-linked TSLP JAK/STAT5 output routes."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROUTES = (
    ("JAK1", "NODE06016"),
    ("JAK2", "NODE06026"),
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def make_rows(bundle: Path) -> list[dict[str, str]]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    receptor_edge = next(
        row for row in read_tsv(bundle / "mechanism_edges.tsv")
        if row["edge_id"] == "M21B-E000683"
    )
    receptor = nodes["NODE11500"]
    tf = nodes["NODE10752"]
    output = nodes["NODE03995"]
    rows: list[dict[str, str]] = []
    for index, (kinase_label, kinase_id) in enumerate(ROUTES, start=1):
        kinase = nodes[kinase_id]
        rows.append(
            {
                "expansion_id": f"M21B-LITEXP-TSLP-JAKSTAT-{index:03d}",
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>output",
                "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
                "missing_layers": "target_gene_expression",
                "intracellular_status": "source_supported_composed",
                "ligand_node_id": receptor_edge["source_node_id"],
                "ligand_label": receptor_edge["source_label"],
                "ligand_receptor_edge_id": receptor_edge["edge_id"],
                "receptor_node_id": receptor["node_id"],
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": kinase_id,
                "intracellular_continuation_label": kinase["canonical_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": tf["node_id"],
                "transcription_factor_label": tf["canonical_label"],
                "tf_target_edge_id": "",
                "target_gene_node_id": "",
                "target_gene_label": "",
                "target_output_form_id": "",
                "output_node_id": output["node_id"],
                "output_label": output["canonical_label"],
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": f"TSLP-TSLPR:IL7RA-{kinase_label}-STAT5-GATA3",
                "input_evidence_type": "primary_graph_linked_layer_evidence",
                "output_evidence_type": "primary_composed_downstream_output",
                "evidence_ids": ";".join(
                    [
                        "M21B-E000683",
                        "M21B-EVID-000626",
                        "M21B-EVID-009001",
                        "PMID:10570284",
                        "PMID:11418668",
                        "PMID:20128689",
                        "PMID:20974963",
                        "PMID:23063330",
                    ]
                ),
                "source_chain_id": f"manual_primary_tslp:PMID:20974963+PMID:23063330:{kinase_label}",
                "source_evidence_record_id": "",
                "route_linkage_status": ";".join(
                    [
                        "manual_primary_tslp_route",
                        "graph_linked_route_source",
                        "primary_layers_source_linked",
                        "receptor_to_intracellular_edge_not_asserted",
                        "intracellular_to_tf_edge_not_asserted",
                        "tf_to_target_edge_not_asserted",
                        "end_to_end_chain_not_asserted_by_single_source",
                        "evidence_route_only",
                    ]
                ),
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "cellular_functional_readout",
                "primary_locator": "PMID:10570284; PMID:11418668; PMID:20128689; PMID:20974963; PMID:23063330",
                "citation_note": "Primary TSLP receptor/JAK/STAT5 and human ILC2 GATA3-output studies are assembled as separately source-linked layers; a terminal GATA3 target gene is not asserted.",
                "evidence_summary": "Primary studies support TSLP signaling through the TSLPR/IL7RA receptor complex, JAK1/JAK2-dependent STAT5 activation, and TSLP-associated GATA3 expression in human ILC2s. JAK1 and JAK2 are represented as parallel continuation alternatives, while the route retains STAT5 as the transcription-factor layer and GATA3 expression as the terminal functional output.",
                "limitations": "The kinase/STAT5 studies use primary CD4 T cells and receptor-reconstituted systems, while the GATA3 output uses human peripheral-blood and nasal-polyp ILC2s. No single source demonstrates every handoff, the receptor-to-kinase and kinase-to-STAT5 edges are not asserted for the exact graph receptor alias, and no terminal GATA3 target gene or SCI transfer is inferred.",
                "curation_status": "curated_primary_route",
                "species_context": "human; mouse",
                "cell_type_context": "Primary human and mouse CD4 T cells; TSLP receptor-reconstituted systems; human peripheral-blood and nasal-polyp ILC2s",
                "compartment_context": "extracellular ligand; plasma-membrane receptor complex; cytoplasmic JAK/STAT5 signaling; ILC2 GATA3 output",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary evidence; route layers retain source-specific models",
                "assay_or_perturbation": "TSLP stimulation; receptor reconstitution; JAK1/JAK2 and STAT5 phosphorylation; GATA3 expression and perturbation assays",
                "effect_polarity": "activating",
                "source_scope": "graph_linked_composite_primary_evidence",
            }
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = make_rows(args.bundle.resolve())
    args.output.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
