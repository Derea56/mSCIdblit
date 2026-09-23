#!/usr/bin/env python3
"""Build source-linked IL-17A receptor-proximal output routes."""

from __future__ import annotations

import argparse
import csv
import gzip
import json
from pathlib import Path


OUTPUTS = (
    ("DEFB4", "NODE02811", "M21B-E008666", "PMID:15322213"),
    ("CCL20", "NODE01682", "M21B-E008667", "PMID:16272323"),
    ("CXCL8", "NODE02684", "M21B-E008683", "PMID:11692108"),
)
CONTINUATIONS = (
    ("ACT1", "NODE00152", "M21B-E001771", "source_supported"),
    ("TRAF6", "NODE11385", "", "source_supported_composed"),
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def make_rows(bundle: Path) -> list[dict[str, str]]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    route_path = bundle / "mechanism_signaling_route_evidence.tsv.gz"
    with gzip.open(route_path, "rt", encoding="utf-8", newline="") as handle:
        route_rows = list(csv.DictReader(handle, delimiter="\t"))
    route_by_id = {row["route_evidence_id"]: row for row in route_rows}
    output_routes = {
        "NODE02811": "GRAPHROUTE:012958",
        "NODE01682": "GRAPHROUTE:012959",
        "NODE02684": "GRAPHROUTE:012975",
    }
    receptor_edge = edges["M21B-E000450"]
    receptor = nodes["NODE05342"]
    rows: list[dict[str, str]] = []
    index = 1
    for output_label, output_id, output_edge_id, output_locator in OUTPUTS:
        output_route = route_by_id[output_routes[output_id]]
        target = nodes[output_id]
        target_label = target["canonical_label"]
        for continuation_label, continuation_id, receptor_continuation_edge, status in CONTINUATIONS:
            continuation = nodes[continuation_id]
            edge_ids = [
                "M21B-E000450",
                "M21B-E001771",
                "M21B-E001772",
                output_edge_id,
                "M21B-EVID-000393",
                "M21B-EVID-001714",
                "M21B-EVID-001715",
                "M21B-EVID-008612" if output_id == "NODE02811" else "M21B-EVID-008613" if output_id == "NODE01682" else "M21B-EVID-008629",
                "PMID:17035243",
                "PMID:17277779",
                "PMID:21335551",
                "PMID:19825828",
                output_locator,
            ]
            rows.append(
                {
                    "expansion_id": f"M21B-LITEXP-IL17A-{index:03d}",
                    "source_queue_id": "",
                    "route_status": "retained_evidence_route",
                    "path_expression": "ligand>receptor>intracellular>????>target_gene_expression",
                    "route_tier": "ligand_receptor_intracellular_output_missing_tf",
                    "known_layers": "ligand|receptor|intracellular_continuation|target_gene_expression",
                    "missing_layers": "transcription_factor",
                    "intracellular_status": status,
                    "ligand_node_id": "NODE05330",
                    "ligand_label": "IL17A",
                    "ligand_receptor_edge_id": "M21B-E000450",
                    "receptor_node_id": "NODE05342",
                    "receptor_label": receptor["canonical_label"],
                    "receptor_intracellular_edge_id": receptor_continuation_edge,
                    "intracellular_continuation_node_id": continuation_id,
                    "intracellular_continuation_label": continuation["canonical_label"],
                    "intracellular_tf_edge_id": "",
                    "transcription_factor_node_id": "",
                    "transcription_factor_label": "",
                    "tf_target_edge_id": "",
                    "target_gene_node_id": output_id,
                    "target_gene_label": target["canonical_label"],
                    "target_output_form_id": "",
                    "output_node_id": output_id,
                    "output_label": f"{target_label} expression",
                    "output_form_id": "",
                    "bridge_id": "",
                    "pathway_name": f"IL17A-IL17RA:IL17RC-{continuation_label}-{output_label}",
                    "input_evidence_type": "primary_graph_linked_layer_evidence",
                    "output_evidence_type": "primary_target_gene_expression",
                    "evidence_ids": ";".join(dict.fromkeys(edge_ids)),
                    "source_chain_id": f"manual_primary_il17a:{output_locator}:{continuation_label}",
                    "source_evidence_record_id": "",
                    "route_linkage_status": ";".join(
                        [
                            "manual_primary_il17a_route",
                            "graph_linked_route_source",
                            "primary_layers_source_linked",
                            "intracellular_to_tf_edge_not_asserted",
                            "transcription_factor_layer_missing",
                            "end_to_end_chain_not_asserted_by_single_source",
                            "evidence_route_only",
                        ]
                        + (["receptor_to_intracellular_edge_not_asserted"] if not receptor_continuation_edge else [])
                    ),
                    "causal_status": "not_asserted",
                    "traversal_status": "evidence_route_not_causal",
                    "evidence_contract_version": "mechanism_evidence_v1",
                    "evidence_polarity": "supports",
                    "negative_evidence_status": "not_evaluated",
                    "evidence_directness": "composite_primary_route",
                    "output_class": "target_gene_expression",
                    "primary_locator": "; ".join(
                        [
                            "PMID:17035243",
                            "PMID:17277779",
                            "PMID:21335551",
                            "PMID:19825828",
                            output_locator,
                        ]
                    ),
                    "citation_note": "Primary IL-17A receptor-proximal and epithelial output studies are assembled as separately source-linked layers; the TF layer remains unresolved.",
                    "evidence_summary": f"Primary studies support IL-17A binding to the IL17RA:IL17RC receptor complex, receptor-proximal recruitment of ACT1/CIKS and ACT1-dependent TRAF6 signaling, and IL-17A-induced {output_label} expression in epithelial systems. The route preserves {continuation_label} as an intracellular continuation while leaving the TF handoff unasserted.",
                    "limitations": "The receptor-proximal and output studies use bounded fibroblast, astroglial, airway epithelial, and reconstituted contexts; they do not demonstrate a single-cell ligand-to-target sequence. NF-kappaB/other TF participation is biologically plausible but not encoded as an asserted TF layer here, and no SCI transfer is inferred.",
                    "curation_status": "curated_primary_route",
                    "species_context": "human; mouse",
                    "cell_type_context": "IL-17 receptor-expressing fibroblasts and mouse embryo fibroblasts/astroglial cells; primary human and mouse airway epithelial cultures",
                    "compartment_context": "extracellular ligand; plasma-membrane receptor complex; receptor-proximal ACT1/TRAF6 signaling; epithelial target-gene output",
                    "injury_context": "no SCI transfer inferred; primary model context only",
                    "context_scope": "composite primary evidence; route layers retain source-specific models",
                    "assay_or_perturbation": "IL-17 stimulation; receptor/ACT1 association and Act1 loss/rescue; TRAF6 recruitment/ubiquitination; target-gene mRNA/protein readouts",
                    "effect_polarity": "activating",
                    "source_scope": "graph_linked_composite_primary_evidence",
                }
            )
            index += 1
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
