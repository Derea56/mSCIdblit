#!/usr/bin/env python3
"""Build primary-literature route overlays for three unresolved ligands.

These rows are evidence-layer compositions for mSCS route plausibility.  They
retain graph-linked ligand/receptor identities and source-supported downstream
layers without asserting causal graph edges or confidence scores.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "expansion_id": "M21B-LITEXP-HMGB1-RAGE-NFKB-TF",
        "ligand_node_id": "NODE04760",
        "lr_edge_id": "M21B-E000145",
        "relay_node_id": "NODE07995",
        "tf_node_id": "NODE07984",
        "pathway_name": "HMGB1-RAGE-RhoA-Rac1-NF-kB-tissue-factor",
        "path_expression": "ligand>receptor>intracellular>TF>output",
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|target_gene_expression",
        "output_label": "tissue-factor expression and procoagulant activity",
        "primary_locator": "PMID:25490770; PMID:19652887",
        "evidence_ids": "M21B-E000145;M21B-EVID-000088",
        "evidence_summary": (
            "Primary endothelial studies report that HMGB1 uses RAGE-associated signaling to increase "
            "RhoA/Rac1 activity and NF-kB phosphorylation, with RAGE or MT1-MMP inhibition suppressing "
            "tissue-factor induction. A complementary primary study reports receptor-blockade-sensitive "
            "HMGB1 induction of NF-kB/Egr-1 and tissue-factor promoter activity. The route retains the "
            "graph-linked HMGB1-RAGE pair and NF-kB/p65 phosphorylation layer."
        ),
        "limitations": (
            "The studies use vascular endothelial models and do not establish an uninterrupted normalized "
            "graph chain or SCI-specific transfer. RhoA/Rac1 and the handoffs into NF-kB remain source-supported "
            "route layers; tissue factor is retained as a functional output because an F3 gene node is not "
            "currently represented as a target-gene node in this bundle."
        ),
        "species_context": "human endothelial cells; mouse macrophage comparator",
        "cell_type_context": "human aortic endothelial cells and vascular endothelial cells; murine macrophages",
        "assay_or_perturbation": "HMGB1 stimulation; RAGE or MT1-MMP inhibition; RhoA/Rac1 and phospho-NF-kB assays; tissue-factor mRNA, protein, promoter, and activity assays",
        "effect_polarity": "activating",
    },
    {
        "expansion_id": "M21B-LITEXP-VEGFA-KDR-ERK-EGR1-TF",
        "ligand_node_id": "NODE11726",
        "lr_edge_id": "M21B-E000183",
        "relay_node_id": "NODE03370",
        "tf_node_id": "NODE03137",
        "pathway_name": "VEGFA-KDR-ERK1-2-EGR1-tissue-factor",
        "path_expression": "ligand>receptor>intracellular>TF>output",
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|target_gene_expression",
        "output_label": "tissue-factor expression",
        "primary_locator": "PMID:10339488; PMID:11149911",
        "evidence_ids": "M21B-E000183;M21B-EVID-000122",
        "evidence_summary": (
            "Primary human endothelial studies report that VEGF activates ERK1/2 and induces nuclear EGR-1, "
            "which binds the tissue-factor promoter and is required for VEGF-dependent tissue-factor induction. "
            "The route retains the graph-linked VEGFA-KDR receptor pair and ERK1/2 relay before EGR1."
        ),
        "limitations": (
            "The cited studies use endothelial models and do not provide a complete normalized graph chain or "
            "SCI-specific transfer. The KDR-to-ERK and ERK-to-EGR1 handoffs remain evidence-layer composition, "
            "and tissue factor is reported as a functional output because an F3 target-gene node is not currently "
            "available in the bundle."
        ),
        "species_context": "human",
        "cell_type_context": "human vascular endothelial cells",
        "assay_or_perturbation": "VEGF stimulation; MAPK inhibition; EGR-1 nuclear localization and DNA-binding assays; tissue-factor promoter reporter, mRNA, and protein assays",
        "effect_polarity": "activating",
    },
    {
        "expansion_id": "M21B-LITEXP-IGF1-IGF1R-PI3KAKT-NFKB-VEGFA",
        "ligand_node_id": "NODE05034",
        "lr_edge_id": "M21B-E000987",
        "relay_node_id": "NODE08995",
        "tf_node_id": "NODE07984",
        "target_gene_node_id": "NODE11724",
        "pathway_name": "IGF1-IGF1R-PI3K-AKT-NF-kB-VEGFA",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "output_label": "VEGF/VEGFA transcription and protein up-regulation",
        "primary_locator": "PMID:15277220",
        "evidence_ids": "M21B-E000987;M21B-EVID-000930",
        "evidence_summary": (
            "A primary retinal-pigment-epithelium study reports IGF-I-dependent VEGF promoter activation and "
            "VEGF up-regulation through PI3K/Akt with contributions from NF-kB, AP-1, and HIF-1alpha. The route "
            "retains the graph-linked IGF1-IGF1R pair, PI3K-AKT1 continuation, NF-kB transcriptional layer, and "
            "the existing VEGFA gene node."
        ),
        "limitations": (
            "The study does not isolate every IGF1R-to-PI3K/Akt or Akt-to-NF-kB handoff with a single uninterrupted "
            "molecular chain, and the model is not SCI-specific. The route is evidence-only: direct signaling and "
            "TF-target edges remain unasserted and no confidence score is assigned."
        ),
        "species_context": "human; mouse comparator",
        "cell_type_context": "human retinal pigment epithelial cells and fibroblast comparator cells",
        "assay_or_perturbation": "IGF-I stimulation; IGF-I promoter reporter truncations; PI3K, Akt, NF-kB, JNK, HIF-1alpha, and RelA perturbations; VEGF expression assays",
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
        target_gene_id = spec.get("target_gene_node_id", "")
        target_gene = nodes[target_gene_id] if target_gene_id else {}
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
                "target_gene_node_id": target_gene_id,
                "target_gene_label": target_gene.get("canonical_label", ""),
                "target_output_form_id": "",
                "output_node_id": "",
                "output_label": spec["output_label"],
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": spec["pathway_name"],
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression" if target_gene_id else "primary_functional_output",
                "evidence_ids": unique_join(lr.get("evidence_ids", ""), spec["evidence_ids"], spec["primary_locator"]),
                "source_chain_id": spec["expansion_id"],
                "source_evidence_record_id": "",
                "route_linkage_status": (
                    f"manual_primary_{spec['expansion_id'].removeprefix('M21B-LITEXP-').lower()}_route;"
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
                "output_class": "target_gene_expression" if target_gene_id else "generic_functional_readout",
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
                "compartment_context": "extracellular ligand; plasma-membrane receptor; intracellular signaling; nuclear or functional output context",
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
