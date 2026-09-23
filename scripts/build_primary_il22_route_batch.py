#!/usr/bin/env python3
"""Build a small, source-linked IL-22 JAK/STAT route batch.

The two rows intentionally represent parallel JAK1 and TYK2 continuation
possibilities.  They preserve primary IL-22 receptor/JAK/STAT/output evidence
without asserting a graph edge for receptor-to-kinase or kinase-to-STAT3.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROUTES = (
    ("JAK1", "NODE06016"),
    ("TYK2", "NODE11526"),
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def make_rows(bundle: Path) -> list[dict[str, str]]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    route_path = bundle / "mechanism_signaling_route_evidence.tsv.gz"
    import gzip

    routes = {
        row["route_evidence_id"]: row
        for row in csv.DictReader(gzip.open(route_path, "rt", encoding="utf-8", newline=""), delimiter="\t")
    }
    template = routes["ROUTE:15371"]
    receptor_edge = edges["M21B-E000448"]
    receptor = nodes["NODE05425"]
    kinase = nodes
    tf = nodes["NODE10726"]
    target = nodes["NODE10509"]

    rows: list[dict[str, str]] = []
    for index, (kinase_label, kinase_id) in enumerate(ROUTES, start=1):
        kinase_node = kinase[kinase_id]
        rows.append(
            {
                "expansion_id": f"M21B-LITEXP-IL22-JAKSTAT-{index:03d}",
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "intracellular_to_tf_edge|tf_to_target_edge",
                "intracellular_status": "source_supported_composed",
                "ligand_node_id": "NODE05421",
                "ligand_label": "IL22",
                "ligand_receptor_edge_id": "M21B-E000448",
                "receptor_node_id": "NODE05425",
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": kinase_id,
                "intracellular_continuation_label": kinase_node["canonical_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": "NODE10726",
                "transcription_factor_label": tf["canonical_label"],
                "tf_target_edge_id": "",
                "target_gene_node_id": "NODE10509",
                "target_gene_label": target["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": "NODE10509",
                "output_label": "SOCS3 expression",
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": f"IL22-IL22RA1:IL10RB-{kinase_label}-STAT3-SOCS3",
                "input_evidence_type": "primary_graph_linked_layer_evidence",
                "output_evidence_type": "primary_composed_downstream_output",
                "evidence_ids": ";".join(
                    [
                        receptor_edge["edge_id"],
                        "M21B-E000449",
                        "M21B-E008279",
                        "M22B-EVID-000066",
                        "PMID:12087100",
                        "PMID:15120652",
                        "PMID:32611765",
                        "PMCID:PMC7458808",
                    ]
                ),
                "source_chain_id": f"manual_primary_il22:PMID:15120652+PMID:32611765:{kinase_label}",
                "source_evidence_record_id": "",
                "route_linkage_status": ";".join(
                    [
                        "manual_primary_il22_route",
                        "graph_linked_route_source",
                        "primary_layers_source_linked",
                        "receptor_to_intracellular_edge_not_asserted",
                        "intracellular_to_tf_edge_not_asserted",
                        "tf_to_target_edge_context_reused",
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
                "output_class": "target_gene_expression",
                "primary_locator": "PMID:12087100; PMID:15120652; PMID:32611765; PMCID:PMC7458808",
                "citation_note": "Primary IL-22 receptor/JAK/STAT and SOCS3 evidence is assembled as separately source-linked layers; PMID:32611765 uses reconstituted/synthetic receptor systems and PMID:15120652 uses human colon epithelial cells.",
                "evidence_summary": "IL-22 signals through the IL22RA1:IL10RB receptor complex and activates JAK/STAT signaling. Primary IL-22 stimulation studies report JAK1/TYK2 and STAT3 activation in receptor-reconstituted systems, while human colon epithelial cells show IL-22-induced STAT3 phosphorylation and SOCS3 mRNA induction. The existing graph-linked STAT3-SOCS3 relation is retained as reusable TF-target context; the complete handoff is not asserted as a single-source chain.",
                "limitations": "JAK1 and TYK2 are represented as parallel continuation alternatives, not as serial steps. Receptor-to-kinase and kinase-to-STAT3 edges are not asserted in the graph, and the STAT3-SOCS3 target relation is reused as context rather than claimed as IL-22-specific causal evidence. Models are colon epithelial and engineered/reconstituted systems; no SCI transfer is inferred.",
                "curation_status": "curated_primary_route",
                "species_context": "human; mouse",
                "cell_type_context": "Human Colo205 colon epithelial cells; engineered/reconstituted Ba/F3 IL-22 receptor systems",
                "compartment_context": "extracellular ligand; plasma-membrane receptor complex; cytoplasmic JAK/STAT signaling; nuclear SOCS3 regulatory output",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary evidence; route layers retain source-specific models",
                "assay_or_perturbation": "IL-22 stimulation; receptor/JAK/STAT phosphorylation assays; SOCS3 mRNA readout",
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
