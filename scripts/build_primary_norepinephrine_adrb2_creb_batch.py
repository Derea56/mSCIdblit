#!/usr/bin/env python3
"""Build primary-literature norepinephrine/ADRB2/CREB BDNF route overlays."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "NOREPINEPHRINE-ADRB2-GNAS-CREB-BDNF-EXON-IV",
        "target_node_id": "NODE01183",
        "output_label": "BDNF exon IV mRNA expression",
        "pathway_name": "Norepinephrine-ADRB2-GNAS-CREB-BDNF-exon-IV",
        "primary_locator": "PMID:28983964; PMID:22593004; PMID:17681645",
        "assay_or_perturbation": (
            "Norepinephrine stimulation of cultured rat cortical astrocytes; beta-adrenergic and alpha1-adrenergic "
            "pharmacology; CREB perturbation or phosphorylation assays; BDNF exon IV mRNA/promoter assays; beta2-adrenergic "
            "cAMP/PKA and cellular BDNF measurements"
        ),
    },
    {
        "name": "NOREPINEPHRINE-ADRB2-GNAS-CREB-BDNF-EXON-VI",
        "target_node_id": "NODE01184",
        "output_label": "BDNF exon VI mRNA expression",
        "pathway_name": "Norepinephrine-ADRB2-GNAS-CREB-BDNF-exon-VI",
        "primary_locator": "PMID:28983964; PMID:22593004; PMID:17681645",
        "assay_or_perturbation": (
            "Norepinephrine stimulation of cultured rat cortical astrocytes; beta-adrenergic and alpha1-adrenergic "
            "pharmacology; CREB perturbation or phosphorylation assays; BDNF exon VI mRNA/promoter assays; beta2-adrenergic "
            "cAMP/PKA and cellular BDNF measurements"
        ),
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
    lr_edge_id = "M21B-E001464"
    relay_edge_id = "M21B-E001833"
    tf_node_id = "NODE02454"
    relay_node_id = "NODE04295"
    lr = edges[lr_edge_id]
    relay_edge = edges[relay_edge_id]
    ligand = nodes[lr["source_node_id"]]
    receptor = nodes[lr["target_node_id"]]
    relay = nodes[relay_node_id]
    tf = nodes[tf_node_id]
    rows: list[dict[str, str]] = []
    for index, spec in enumerate(SPECS, start=1):
        target = nodes[spec["target_node_id"]]
        expansion_id = f"M21B-LITEXP-NOREPIADRB2-{index:03d}"
        rows.append(
            {
                "expansion_id": expansion_id,
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
                "intracellular_status": "source_supported_composed",
                "ligand_node_id": lr["source_node_id"],
                "ligand_label": ligand["canonical_label"],
                "ligand_receptor_edge_id": lr_edge_id,
                "receptor_node_id": lr["target_node_id"],
                "receptor_label": receptor["canonical_label"],
                "receptor_intracellular_edge_id": relay_edge_id,
                "intracellular_continuation_node_id": relay_node_id,
                "intracellular_continuation_label": relay["canonical_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": tf_node_id,
                "transcription_factor_label": tf["canonical_label"],
                "tf_target_edge_id": "",
                "target_gene_node_id": spec["target_node_id"],
                "target_gene_label": target["canonical_label"],
                "target_output_form_id": "",
                "output_node_id": spec["target_node_id"],
                "output_label": spec["output_label"],
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": spec["pathway_name"],
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": unique_join(
                    lr.get("evidence_ids", ""), relay_edge.get("evidence_ids", ""), spec["primary_locator"]
                ),
                "source_chain_id": expansion_id,
                "source_evidence_record_id": "",
                "route_linkage_status": (
                    f"manual_primary_{spec['name'].lower().replace('-', '_')}_route;graph_linked_route_source;"
                    "primary_layer_linked;receptor_to_intracellular_edge_supported_by_graph;"
                    "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;"
                    "beta2_contribution_not_exclusive;alternative_creb_mechanisms_retained;evidence_route_only"
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
                    f"Primary-evidence route overlay for {spec['name']}. The existing norepinephrine-ADRB2 and ADRB2-Gs "
                    "layers are retained, while CREB-associated BDNF transcript evidence is mapped as a composed route; "
                    "no causal edge or confidence score is created."
                ),
                "evidence_summary": (
                    "Primary astrocyte studies report norepinephrine-induced BDNF exon-specific transcripts and CREB-dependent "
                    "transcriptional responses. Separate beta-adrenergic pharmacology supports beta2 participation in the "
                    "norepinephrine/cAMP-associated BDNF response, while other primary work identifies noncanonical PKC/ERK/"
                    "CRTC-associated CREB activation. The route preserves these observations without treating ADRB2 as exclusive "
                    "or asserting every molecular handoff."
                ),
                "limitations": (
                    "The primary studies use related but distinct astrocyte systems and pharmacologic or CREB perturbations. "
                    "They support the ligand, receptor-class, intracellular, CREB and BDNF-output layers, but do not establish "
                    "a single ADRB2-to-GNAS-to-CREB chain or direct CREB-to-target graph edge in one experiment. "
                    "No SCI transfer or database confidence score is inferred."
                ),
                "curation_status": "curated_primary_route",
                "species_context": "rat astrocyte culture systems",
                "cell_type_context": "cultured rat cortical astrocytes",
                "compartment_context": (
                    "extracellular norepinephrine; plasma-membrane ADRB2; Gs/GNAS-associated intracellular signaling; "
                    "nuclear CREB-associated BDNF exon-specific transcript output"
                ),
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite_primary_evidence; beta2 contribution not exclusive",
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
