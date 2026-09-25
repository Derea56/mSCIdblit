#!/usr/bin/env python3
"""Build primary-literature route overlays for THBS1 and THBS2."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "expansion_id": "M21B-LITEXP-THBS1-CD36-TLR4-NFKB-TNF",
        "ligand_node_id": "NODE11503",
        "lr_edge_id": "M21B-E000206",
        "relay_node_id": "NODE11180",
        "tf_node_id": "NODE07984",
        "target_gene_node_id": "NODE11249",
        "pathway_name": "TSP1-CD36-TLR4-MyD88-NF-kB-TNF",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "output_label": "TNF/TNF-alpha expression and release",
        "primary_locator": "PMID:23954950",
        "evidence_ids": "M21B-E000206;M21B-EVID-000149",
        "evidence_summary": (
            "A primary macrophage study reports that recombinant or purified TSP1 stimulates TNF-alpha "
            "expression, TLR4 expression, and NF-kB activity. TSP1-induced TNF production is lost in TLR4-null "
            "macrophages and is attenuated by blocking the TSP1-CD36 association. The route retains the "
            "graph-linked TSP1-CD36 pair, the existing TLR4/MD2/MyD88/p38/NF-kB relay, NF-kB, and the TNF gene node."
        ),
        "limitations": (
            "The study uses mouse bone-marrow-derived and peritoneal macrophages rather than an SCI receiver "
            "state. The CD36-to-TLR4, TLR4-to-relay, and NF-kB-to-TNF handoffs remain evidence-layer composition; "
            "no causal graph edges or confidence score are created."
        ),
        "species_context": "mouse; human TSP1 reagent",
        "cell_type_context": "mouse bone-marrow-derived macrophages and peritoneal macrophages",
        "assay_or_perturbation": "recombinant or purified human TSP1; TLR4-null macrophages; CD36-blocking peptide or antibody; TNF qPCR/ELISA; NF-kB activity assays",
        "effect_polarity": "activating",
    },
    {
        "expansion_id": "M23B-LITEXP-THBS2-NOTCH3-NICD-RBPJ-HES1",
        "ligand_node_id": "NODE11052",
        "lr_edge_id": "M23B-E000738",
        "relay_node_id": "NODE08209",
        "tf_node_id": "NODE09657",
        "target_gene_node_id": "NODE04668",
        "pathway_name": "THBS2-NOTCH3-JAG1-NICD-RBPJ-HES1",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "output_label": "HES1/Notch reporter and target-gene expression",
        "primary_locator": "PMID:19147503; PMID:20472562",
        "evidence_ids": "M23B-E000738;M23B-EVID-000990",
        "evidence_summary": (
            "Primary studies report that TSP2 binds Notch3 and Jagged1, potentiates Notch3/Jagged1 signaling, "
            "and increases HES1-luciferase reporter activity; loss of TSP2 reduces Notch target-gene expression. "
            "A follow-up study shows that LRP1-dependent endocytosis is required for TSP2 enhancement of Notch3 "
            "activity. The route retains the graph-linked THBS2-NOTCH3:JAG1 complex, NOTCH3/NICD3 continuation, "
            "RBPJ/CSL, and the HES1 target-gene node."
        ),
        "limitations": (
            "The studies use cancer-cell, fibroblast, and coculture systems and do not establish SCI transfer. "
            "The exact THBS2-to-NICD3, NICD3-to-RBPJ, and RBPJ-to-HES1 handoffs are preserved as evidence-layer "
            "composition; the route does not assert new graph edges."
        ),
        "species_context": "human; mouse TSP2",
        "cell_type_context": "H460 Notch3-expressing cells, fibroblasts, and primary human skin fibroblasts",
        "assay_or_perturbation": "TSP2 expression or recombinant TSP2; Notch3/Jagged1 coculture; LRP1 inhibition or deficiency; HES1-luciferase reporter; Notch target-gene and endocytosis assays",
        "effect_polarity": "activating",
    },
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def unique_join(*values: str) -> str:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        for item in value.split(";"):
            item = item.strip()
            if item and item not in seen:
                seen.add(item)
                result.append(item)
    return "; ".join(result)


def make_rows(bundle: Path) -> list[dict[str, str]]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    rows: list[dict[str, str]] = []
    for spec in SPECS:
        lr = edges[spec["lr_edge_id"]]
        ligand = nodes[spec["ligand_node_id"]]
        receptor = nodes[lr["target_node_id"]]
        relay = nodes[spec["relay_node_id"]]
        tf = nodes[spec["tf_node_id"]]
        target_gene = nodes[spec["target_gene_node_id"]]
        rows.append(
            {
                "expansion_id": spec["expansion_id"],
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": spec["path_expression"],
                "route_tier": spec["route_tier"],
                "known_layers": spec["known_layers"],
                "missing_layers": spec["missing_layers"],
                "intracellular_status": "source_supported_composed",
                "ligand_node_id": spec["ligand_node_id"],
                "ligand_label": ligand["canonical_label"],
                "ligand_receptor_edge_id": spec["lr_edge_id"],
                "receptor_node_id": lr["target_node_id"],
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": spec["relay_node_id"],
                "intracellular_continuation_label": relay["canonical_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": spec["tf_node_id"],
                "transcription_factor_label": tf["canonical_label"],
                "tf_target_edge_id": "",
                "target_gene_node_id": spec["target_gene_node_id"],
                "target_gene_label": target_gene["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": "",
                "output_label": spec["output_label"],
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": spec["pathway_name"],
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": unique_join(lr.get("evidence_ids", ""), spec["evidence_ids"], spec["primary_locator"]),
                "source_chain_id": spec["expansion_id"],
                "source_evidence_record_id": "",
                "route_linkage_status": (
                    f"manual_primary_{spec['expansion_id'].removeprefix('M21B-LITEXP-').removeprefix('M23B-LITEXP-').lower()}_route;"
                    "graph_linked_route_source;primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
                    "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;"
                    "target_gene_expression_unresolved;evidence_route_only"
                ),
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression",
                "primary_locator": spec["primary_locator"],
                "citation_note": (
                    "Primary-evidence route overlay; supported layers are retained for mSCS plausibility, while "
                    "unresolved handoffs remain explicit and no graph edge, causal assertion, or confidence score is created."
                ),
                "evidence_summary": spec["evidence_summary"],
                "limitations": spec["limitations"],
                "curation_status": "curated_primary_route",
                "species_context": spec["species_context"],
                "cell_type_context": spec["cell_type_context"],
                "compartment_context": "extracellular or matrix ligand; cell-surface receptor; intracellular signaling; nuclear target-gene output context",
                "injury_context": "primary model context; SCI transfer is not inferred",
                "context_scope": "composite_primary_evidence; route layers retain source-specific models",
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
    print(json.dumps({"rows": len(rows), "output": str(args.output.resolve())}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
