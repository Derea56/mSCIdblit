#!/usr/bin/env python3
"""Build primary-literature route overlays for IL-37 and IL-17D."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


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
    specs = [
        {
            "expansion_id": "M21B-LITEXP-IL37-IL18R1IL1R8-STAT3-NFKB-output",
            "ligand_node_id": "NODE05488",
            "ligand_label": "IL37",
            "lr_edge_id": "M21B-E000188",
            "receptor_node_id": "NODE05355",
            "receptor_label": "IL18R1/IL-18Ralpha:IL1R8/SIGIRR",
            "relay_node_id": "NODE10726",
            "relay_label": "STAT3 within the Mer/PTEN anti-inflammatory relay",
            "tf_node_id": "NODE07984",
            "tf_label": "NF-kB",
            "pathway_name": "IL37-IL18R1-IL1R8-STAT3-NF-kB-anti-inflammatory-output",
            "output_label": "IL-6/TNF/IL-1beta inflammatory-output suppression",
            "primary_locator": "PMID:25729923; PMID:19503107; PMID:25654981",
            "evidence_summary": (
                "Primary studies show that IL-37 forms an IL-18Ralpha/IL-1R8 receptor complex, activates or "
                "harnesses STAT3-associated anti-inflammatory signaling, and inhibits NF-kB and MAPK activity. "
                "The same receptor system suppresses IL-6, TNF, and IL-1beta inflammatory outputs in macrophage "
                "and innate immune models."
            ),
            "limitations": (
                "IL-37 signaling is multi-branch and dose- and context-dependent. The route composes the reported "
                "STAT3 and NF-kB layers into one plausibility path; it does not assert that STAT3 is the sole relay "
                "or that every IL-37-stimulated cell has the same inhibitory output."
            ),
            "cell_type_context": "human peripheral blood mononuclear cells and macrophages; mouse innate immune models",
            "assay_or_perturbation": "IL-37 stimulation; IL-1R8 or IL-18Ralpha silencing/deficiency; proteomic and transcriptomic profiling; cytokine and NF-kB/MAPK assays",
            "species_context": "human; mouse",
            "effect_polarity": "inhibitory",
        },
        {
            "expansion_id": "M21B-LITEXP-IL37-IL1R8-STAT3-NFKB-output",
            "ligand_node_id": "NODE05488",
            "ligand_label": "IL37",
            "lr_edge_id": "M21B-E000553",
            "receptor_node_id": "NODE05388",
            "receptor_label": "IL1R8/SIGIRR",
            "relay_node_id": "NODE10726",
            "relay_label": "STAT3 within the Mer/PTEN anti-inflammatory relay",
            "tf_node_id": "NODE07984",
            "tf_label": "NF-kB",
            "pathway_name": "IL37-IL1R8-STAT3-NF-kB-anti-inflammatory-output",
            "output_label": "IL-6/TNF/IL-1beta inflammatory-output suppression",
            "primary_locator": "PMID:25729923; PMID:19503107; PMID:25654981",
            "evidence_summary": (
                "The primary literature identifies IL-1R8/SIGIRR as the required anti-inflammatory coreceptor for "
                "extracellular IL-37, with STAT3-associated anti-inflammatory signaling and inhibition of NF-kB, "
                "TAK1, and MAPK pathways. IL-37/IL-1R8 activity reduces inflammatory cytokine production in innate "
                "immune models."
            ),
            "limitations": (
                "The receptor is part of a tripartite IL-37/IL-18Ralpha/IL-1R8 complex in the strongest primary "
                "mechanistic study; this row preserves the graph's IL-1R8 receptor identity but should not be read "
                "as an IL-1R8-only biochemical mechanism."
            ),
            "cell_type_context": "human peripheral blood mononuclear cells and macrophages; mouse innate immune models",
            "assay_or_perturbation": "IL-37 stimulation; IL-1R8 or IL-18Ralpha silencing/deficiency; cytokine and NF-kB/MAPK assays",
            "species_context": "human; mouse",
            "effect_polarity": "inhibitory",
        },
        {
            "expansion_id": "M21B-LITEXP-IL17D-CD93-P38-SMAD23-output",
            "ligand_node_id": "NODE05337",
            "ligand_label": "IL17D",
            "lr_edge_id": "M21B-E005478",
            "receptor_node_id": "NODE01981",
            "receptor_label": "CD93",
            "relay_node_id": "NODE06785",
            "relay_label": "p38 MAPK–AKT relay",
            "tf_node_id": "NODE10455",
            "tf_label": "SMAD2/3",
            "pathway_name": "IL17D-CD93-p38-AKT-SMAD23-DDX5-inflammatory-output",
            "output_label": "DDX5 suppression and IL-36R inflammatory amplification",
            "primary_locator": "PMID:36271146",
            "evidence_summary": (
                "A primary keratinocyte and mouse skin study reports that IL-17D signals through CD93 and activates "
                "a p38 MAPK–AKT–SMAD2/3 pathway that suppresses DDX5 and amplifies IL-36R-associated inflammation. "
                "The route retains SMAD2/3 as the downstream transcriptional regulator layer."
            ),
            "limitations": (
                "The study resolves a CD93–p38–AKT–SMAD2/3 signaling axis in keratinocytes but does not provide a "
                "single direct transcription-factor-to-DDX5 edge in the normalized graph. The output is therefore "
                "functional and model-specific; no SCI transfer is inferred."
            ),
            "cell_type_context": "primary human keratinocytes; mouse skin inflammation model",
            "assay_or_perturbation": "IL-17D stimulation; CD93 knockdown or deficiency; p38, AKT, and SMAD2/3 inhibitor assays; DDX5 and inflammatory gene expression",
            "species_context": "human; mouse",
            "effect_polarity": "activating",
        },
    ]

    rows: list[dict[str, str]] = []
    for spec in specs:
        for node_id in [spec["ligand_node_id"], spec["receptor_node_id"], spec["relay_node_id"], spec["tf_node_id"]]:
            if node_id not in nodes:
                raise ValueError(f"{spec['expansion_id']}: missing node {node_id}")
        lr = edges.get(spec["lr_edge_id"])
        if not lr or (lr["source_node_id"], lr["target_node_id"]) != (
            spec["ligand_node_id"], spec["receptor_node_id"]
        ):
            raise ValueError(f"{spec['expansion_id']}: ligand-receptor edge endpoints do not match")
        rows.append(
            {
                "expansion_id": spec["expansion_id"],
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>output",
                "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
                "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|target_gene_expression",
                "intracellular_status": "source_supported_composed",
                "ligand_node_id": spec["ligand_node_id"],
                "ligand_label": spec["ligand_label"],
                "ligand_receptor_edge_id": spec["lr_edge_id"],
                "receptor_node_id": spec["receptor_node_id"],
                "receptor_label": spec["receptor_label"],
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": spec["relay_node_id"],
                "intracellular_continuation_label": spec["relay_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": spec["tf_node_id"],
                "transcription_factor_label": spec["tf_label"],
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
                "output_evidence_type": "primary_composed_downstream_output",
                "evidence_ids": unique_join(lr.get("evidence_ids", ""), spec["primary_locator"]),
                "source_chain_id": spec["expansion_id"],
                "source_evidence_record_id": "",
                "route_linkage_status": "graph_linked_route_source;manual_primary_route_expansion;primary_layer_linked;receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;end_to_end_chain_not_asserted_by_single_source;evidence_route_only",
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "generic_functional_readout",
                "primary_locator": spec["primary_locator"],
                "citation_note": "Primary literature supports the listed route layers; unresolved handoffs remain explicitly bounded and no confidence score is assigned.",
                "evidence_summary": spec["evidence_summary"],
                "limitations": spec["limitations"],
                "curation_status": "curated_primary_route",
                "species_context": spec["species_context"],
                "cell_type_context": spec["cell_type_context"],
                "compartment_context": "extracellular ligand; plasma-membrane receptor; intracellular relay; nuclear transcriptional/output layer",
                "injury_context": "no SCI transfer inferred; primary model context only",
                "context_scope": "composite primary evidence with graph-linked ligand-receptor identity",
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
