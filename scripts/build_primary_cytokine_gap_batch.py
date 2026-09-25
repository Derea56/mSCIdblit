#!/usr/bin/env python3
"""Build primary-literature route overlays for cytokine signaling gaps."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "CNTF-CNTFR-JAK2-STAT3-BCL2",
        "lr_edge_id": "M21B-E000107",
        "relay_node_id": "NODE06026",
        "tf_node_id": "NODE10726",
        "target_node_id": "NODE01155",
        "primary_locator": "PMID:27060559; PMID:29171438",
        "pathway_name": "CNTF-CNTFR-gp130-LIFR-JAK2-STAT3-BCL2",
        "source_chain_id": "manual_primary_cntf_cntfr_jak2_stat3_bcl2",
        "evidence_summary": (
            "A primary rat oligodendrocyte study reports CNTF-family stimulation with JAK2/STAT3 activation and "
            "BCL2 expression, with JAK2 inhibition reducing the response. A primary embryonic-rat dorsal-root-ganglion "
            "study independently identifies CNTF neuroprotection as dependent on JAK2/STAT3 signaling."
        ),
        "limitations": (
            "The route composes primary oligodendrocyte and dorsal-root-ganglion experiments and retains the CNTF-family "
            "receptor complex as the graph-linked input. The complete receptor-to-JAK2-to-STAT3-to-BCL2 handoff is not "
            "asserted as a single graph chain, and no SCI transfer is inferred."
        ),
        "species_context": "rat",
        "cell_type_context": "primary rat oligodendrocytes and embryonic rat dorsal-root-ganglion neurons",
        "assay_or_perturbation": "CNTF stimulation; JAK2 inhibition; STAT3 phosphorylation; BCL2 expression; neuroprotection assays",
    },
    {
        "name": "IL22-IL22R-JAK1-STAT3-SOCS3",
        "lr_edge_id": "M21B-E000448",
        "relay_node_id": "NODE06016",
        "tf_node_id": "NODE10726",
        "target_node_id": "NODE10509",
        "primary_locator": "PMID:15120652",
        "pathway_name": "IL22-IL22RA1-IL10RB-JAK1-STAT3-SOCS3",
        "source_chain_id": "manual_primary_il22_il22r_jak1_stat3_socs3",
        "evidence_summary": (
            "A primary colon-epithelial study identifies the IL-22R1/IL-10R2 receptor complex, reports IL-22-induced "
            "STAT3 phosphorylation, and shows increased SOCS3 mRNA as a STAT3-responsive output. The route preserves the "
            "graph-linked IL-22 receptor and the JAK1/STAT3 intermediate context."
        ),
        "limitations": (
            "The primary study reports receptor expression, STAT1/STAT3 phosphorylation, and SOCS3 induction in a colon "
            "epithelial cell line; it does not establish every receptor-to-JAK1 and STAT3-to-SOCS3 handoff as a graph edge. "
            "No SCI transfer is inferred."
        ),
        "species_context": "human",
        "cell_type_context": "human colon epithelial Colo205 cells",
        "assay_or_perturbation": "IL-22 stimulation; IL-22R1/IL-10R2 blockade; STAT1/STAT3 phosphorylation; SOCS3 mRNA and cytokine-expression assays",
    },
    {
        "name": "IL13-IL13R-TYK2-STAT6-ARG1",
        "lr_edge_id": "M21B-E000740",
        "relay_node_id": "NODE11526",
        "tf_node_id": "NODE10761",
        "target_node_id": "NODE00751",
        "primary_locator": "PMID:9278458; PMID:25766112",
        "pathway_name": "IL13-IL4RA-IL13RA1-TYK2-STAT6-ARG1",
        "source_chain_id": "manual_primary_il13_il13r_tyk2_stat6_arg1",
        "evidence_summary": (
            "A primary receptor-reconstitution study reports IL-13 receptor-dependent JAK1/TYK2 and STAT6 "
            "phosphorylation. A primary macrophage study shows that IL-13-induced STAT6 activation and Arg1 expression "
            "require IL-13Rα1, supporting the retained receptor-to-TYK2/STAT6-to-ARG1 route."
        ),
        "limitations": (
            "The route composes receptor-reconstitution and primary macrophage experiments; the cited studies do not "
            "establish the exact TYK2-to-STAT6-to-ARG1 handoff in one uninterrupted assay. Missing graph links remain "
            "explicit and no SCI transfer is inferred."
        ),
        "species_context": "human and mouse",
        "cell_type_context": "factor-dependent human/mouse cell systems and primary mouse macrophages",
        "assay_or_perturbation": "IL-13 receptor reconstitution; JAK1/TYK2 and STAT6 phosphorylation; Il13ra1 knockout macrophages; Arg1 gene-expression assays",
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
    for spec in SPECS:
        lr = edges[spec["lr_edge_id"]]
        ligand = nodes[lr["source_node_id"]]
        receptor = nodes[lr["target_node_id"]]
        relay = nodes[spec["relay_node_id"]]
        tf = nodes[spec["tf_node_id"]]
        target = nodes[spec["target_node_id"]]
        rows.append(
            {
                "expansion_id": f"M21B-LITEXP-CYTOKINE-GAP-{spec['name']}-001",
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
                "intracellular_status": "source_supported_composed",
                "ligand_node_id": lr["source_node_id"],
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
                "target_gene_node_id": spec["target_node_id"],
                "target_gene_label": target["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": "",
                "output_label": f"{target['canonical_label']} gene expression",
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": spec["pathway_name"],
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": unique_join(lr.get("evidence_ids", ""), spec["primary_locator"]),
                "source_chain_id": spec["source_chain_id"],
                "source_evidence_record_id": "",
                "route_linkage_status": (
                    f"{spec['source_chain_id']}_route;graph_linked_route_source;primary_layers_source_linked;"
                    "receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;"
                    "tf_to_target_edge_not_asserted;end_to_end_chain_not_asserted_by_single_source;evidence_route_only"
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
                    f"Primary-evidence route overlay for {spec['name']}. Missing handoffs remain explicit; no graph edge, "
                    "causal assertion, or confidence score is created."
                ),
                "evidence_summary": spec["evidence_summary"],
                "limitations": spec["limitations"],
                "curation_status": "curated_primary_route",
                "species_context": spec["species_context"],
                "cell_type_context": spec["cell_type_context"],
                "compartment_context": "extracellular ligand; plasma-membrane receptor; intracellular signaling; nuclear gene-expression context",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary evidence; route layers retain source-specific models",
                "assay_or_perturbation": spec["assay_or_perturbation"],
                "effect_polarity": "activating",
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
