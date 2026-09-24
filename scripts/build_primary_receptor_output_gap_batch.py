#!/usr/bin/env python3
"""Build receptor-to-output evidence routes with unresolved intracellular layers."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "TSP1-CD47-NFkBAP1-IL1B",
        "lr_edge_id": "M21B-E000173",
        "relay_node_id": "NODE01924",
        "tf_node_id": "NODE07984",
        "primary_locator": "PMID:8550562; PMID:26813769",
        "path_expression": "ligand>receptor>intracellular>TF>output",
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": "receptor_to_intracellular_edge|target_gene_expression",
        "output_label": "LPS-induced IL-1beta mRNA/protein modulation",
        "pathway_name": "TSP1-CD47-NFkBAP1-IL1B",
        "route_linkage_status": (
            "manual_primary_tsp1_cd47_nfkb_ap1_il1b_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "target_gene_node_unresolved;evidence_route_only"
        ),
        "evidence_summary": (
            "Primary macrophage studies report TSP1 binding CD47 and limiting LPS-induced IL-1beta mRNA/protein "
            "induction by disrupting CD47-CD14 signaling, thereby limiting NF-kB/AP-1 activation. The route retains "
            "the graph-linked CD47-CD14 inflammatory relay and NF-kB layer while preserving the output as a functional readout."
        ),
        "limitations": (
            "The source separates CD47 binding from the downstream macrophage LPS experiments and also reports domain-"
            "specific effects on inflammasome-dependent IL-1beta maturation. The route is inhibitory for the transcriptional "
            "readout and does not create a direct TF-to-target edge."
        ),
        "species_context": "human and mouse macrophage systems",
        "cell_type_context": "human THP-1 monocyte-derived macrophages and mouse bone-marrow-derived macrophages",
        "assay_or_perturbation": "TSP1/CD47 binding; LPS stimulation; CD47 blockade or deficiency; NF-kB/AP-1 readouts; IL-1beta mRNA and protein assays",
        "effect_polarity": "inhibitory",
    },
    {
        "name": "C1q-LAIR1-CREB-NFkB-IL10",
        "lr_edge_id": "M21B-E000693",
        "relay_node_id": "",
        "tf_node_id": "NODE02446",
        "primary_locator": "PMID:23093673; PMID:17209050",
        "path_expression": "ligand>receptor>TF>output",
        "route_tier": "ligand_receptor_tf_output_annotation_missing_intracellular",
        "known_layers": "ligand|receptor|transcription_factor|output",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_continuation|intracellular_to_tf_edge|target_gene_expression",
        "output_label": "IL-10 induction and anti-inflammatory cytokine modulation",
        "pathway_name": "C1q-LAIR1-CREB-NFkB-IL10",
        "route_linkage_status": (
            "manual_primary_c1q_lair1_creb_nfkb_il10_route;graph_linked_route_source;"
            "primary_layer_linked;intracellular_continuation_unresolved;"
            "receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;"
            "target_gene_expression_unresolved;evidence_route_only"
        ),
        "evidence_summary": (
            "Primary human monocyte studies report C1q-associated LAIR1 immune-regulatory signaling and C1q-induced "
            "NF-kB p50 and CREB activity with IL-10 induction and suppression of selected inflammatory cytokines. "
            "The route preserves the C1q-LAIR1 receptor layer and CREB/output evidence while leaving the intracellular continuation unresolved."
        ),
        "limitations": (
            "The cited C1q transcription study does not establish LAIR1 as the sole receptor for every measured output, "
            "so receptor-to-TF linkage is intentionally composed and unasserted. The output is not represented as a clean "
            "terminal target-gene node."
        ),
        "species_context": "human",
        "cell_type_context": "primary human monocytes and LAIR1-associated myeloid systems",
        "assay_or_perturbation": "C1q treatment; LAIR1 binding and phosphorylation assays; NF-kB/CREB DNA-binding assays; IL-10 and inflammatory-cytokine expression assays",
        "effect_polarity": "activating",
    },
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def unique_join(*values: str) -> str:
    out: list[str] = []
    seen: set[str] = set()
    for value in values:
        for item in value.split(";"):
            item = item.strip()
            if item and item not in seen:
                seen.add(item)
                out.append(item)
    return "; ".join(out)


def make_rows(bundle: Path) -> list[dict[str, str]]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    rows: list[dict[str, str]] = []
    for index, spec in enumerate(SPECS, start=1):
        lr = edges[spec["lr_edge_id"]]
        ligand = nodes[lr["source_node_id"]]
        receptor = nodes[lr["target_node_id"]]
        relay = nodes.get(spec["relay_node_id"], {})
        tf = nodes[spec["tf_node_id"]]
        rows.append(
            {
                "expansion_id": f"M21B-LITEXP-RECGAP-{index:03d}",
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": spec["path_expression"],
                "route_tier": spec["route_tier"],
                "known_layers": spec["known_layers"],
                "missing_layers": spec["missing_layers"],
                "intracellular_status": "unresolved_between_receptor_and_tf" if spec["relay_node_id"] == "" else "source_supported_composed",
                "ligand_node_id": lr["source_node_id"],
                "ligand_label": ligand["canonical_label"],
                "ligand_receptor_edge_id": spec["lr_edge_id"],
                "receptor_node_id": lr["target_node_id"],
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": spec["relay_node_id"],
                "intracellular_continuation_label": relay.get("canonical_label", ""),
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": spec["tf_node_id"],
                "transcription_factor_label": tf["canonical_label"],
                "tf_target_edge_id": "",
                "target_gene_node_id": "",
                "target_gene_label": "",
                "target_output_form_id": "",
                "output_node_id": "",
                "output_label": spec["output_label"],
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": spec["pathway_name"],
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_functional_output",
                "evidence_ids": unique_join(lr.get("evidence_ids", ""), spec["primary_locator"]),
                "source_chain_id": f"M21B-LITEXP-RECGAP-{index:03d}",
                "source_evidence_record_id": "",
                "route_linkage_status": spec["route_linkage_status"],
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "generic_functional_readout",
                "primary_locator": spec["primary_locator"],
                "citation_note": (
                    f"Primary-evidence route overlay for {spec['name']}. Unresolved handoffs and graph target "
                    "limitations are retained explicitly; no graph edge, causal assertion, or confidence score is created."
                ),
                "evidence_summary": spec["evidence_summary"],
                "limitations": spec["limitations"],
                "curation_status": "curated_primary_route",
                "species_context": spec["species_context"],
                "cell_type_context": spec["cell_type_context"],
                "compartment_context": "extracellular ligand; plasma-membrane receptor; intracellular signaling; nuclear or functional output context",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary evidence; route layers retain source-specific models",
                "assay_or_perturbation": spec["assay_or_perturbation"],
                "effect_polarity": spec["effect_polarity"],
                "source_scope": "composite_primary_evidence",
            }
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = make_rows(args.bundle.resolve())
    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
