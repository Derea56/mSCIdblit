#!/usr/bin/env python3
"""Build a small primary-literature tranche for remaining route gaps.

The rows are evidence-layer overlays.  They retain source-supported layers and
make unresolved handoffs explicit; they do not create graph edges, causal
traversal, or confidence scores.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "HGF-MET-STAT3-TWIST1",
        "lr_edge_id": "M21B-E000167",
        "relay_node_id": "NODE04680",
        "tf_node_id": "NODE10726",
        "target_node_id": "NODE11520",
        "source_queue_id": "M21B-DOWNSTREAM:00020",
        "source_record_id": "M21B-DOWNSTREAM-EVID:000043",
        "primary_locator": "PMID:30158543; PMCID:PMC6115420",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "output_label": "TWIST1 gene expression",
        "pathway_name": "HGF-MET-STAT3-TWIST1",
        "route_linkage_status": (
            "manual_primary_hgf_met_stat3_twist1_route;primary_layer_linked;"
            "receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;"
            "tf_to_target_edge_not_asserted;evidence_route_only"
        ),
        "evidence_summary": (
            "A primary gastric-cancer/stromal study reports CAF-derived HGF activating c-MET, STAT3 "
            "and TWIST1, with STAT3 knockdown reducing TWIST1 expression and chromatin-immunoprecipitation "
            "supporting STAT3 occupancy at the TWIST1 promoter. The route retains the existing HGF-MET "
            "receptor and intracellular program nodes while preserving the unasserted graph handoffs."
        ),
        "limitations": (
            "The study uses human gastric-cancer cells with cancer-associated fibroblast or normal-fibroblast "
            "co-culture and also describes IL-6/STAT3 crosstalk. The row isolates the reported HGF-MET-STAT3 "
            "branch but does not claim that every represented handoff is a single experimentally isolated edge "
            "or that the route transfers directly to SCI."
        ),
        "species_context": "human gastric-cancer and fibroblast co-culture systems",
        "cell_type_context": "human gastric-cancer cells with cancer-associated fibroblasts or normal fibroblasts",
        "assay_or_perturbation": "HGF/CAF co-culture; MET and STAT3 perturbation; TWIST1 expression; STAT3 chromatin immunoprecipitation",
    },
    {
        "name": "CXCL12-CXCR4-PLCbeta3-RasERK-AP1-IL10",
        "lr_edge_id": "M21B-E000158",
        "relay_node_id": "NODE09091",
        "tf_node_id": "NODE00609",
        "target_node_id": "NODE05284",
        "source_queue_id": "",
        "source_record_id": "",
        "primary_locator": "PMID:21705626; PMCID:PMC3140596; PMID:17237407; PMCID:PMC2905171",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "output_label": "IL10 promoter activity and IL10 gene transcription",
        "pathway_name": "CXCL12-CXCR4-PLCbeta3-RasERK-AP1-IL10",
        "route_linkage_status": (
            "manual_primary_cxcl12_cxcr4_plcb3_raser k_ap1_il10_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;evidence_route_only"
        ).replace("raser k", "raserk"),
        "evidence_summary": (
            "Primary human T-cell studies report SDF-1/CXCL12-CXCR4-TCR signaling through Gi proteins and "
            "PLC-beta3 to Ras-ERK with downstream AP-1-dependent transcription. A separate primary T-cell "
            "study reports CXCL12 costimulation of IL10 promoter activity, AP-1 binding at the IL10 promoter, "
            "and increased IL10 transcription. The route is therefore a source-composed evidence route with "
            "the receptor, relay, TF, and target identities retained explicitly."
        ),
        "limitations": (
            "The route composes two primary human T-cell studies: the PLC-beta3/Ras-ERK mechanism and the "
            "AP-1/IL10 promoter mechanism were not established as one uninterrupted experiment. CXCL12 "
            "costimulation also depends on T-cell receptor context, and no causal graph edges are created."
        ),
        "species_context": "human",
        "cell_type_context": "human T cells and Jurkat T-cell signaling models",
        "assay_or_perturbation": "SDF-1 stimulation; CXCR4-TCR signaling; Gi/PLC inhibition; ERK and AP-1 assays; IL10 promoter reporter, ChIP, and transcription assays",
    },
    {
        "name": "CXCL12-CXCR4-NOS2-output",
        "lr_edge_id": "M21B-E000158",
        "relay_node_id": "",
        "tf_node_id": "",
        "target_node_id": "NODE08188",
        "source_queue_id": "",
        "source_record_id": "",
        "primary_locator": "PMID:19059114; PMCID:PMC2645593",
        "path_expression": "ligand>receptor>????>????>target_gene_expression",
        "route_tier": "ligand_receptor_output_annotation_missing_intracellular_and_tf",
        "known_layers": "ligand|receptor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_continuation|transcription_factor|intracellular_to_tf_edge",
        "output_label": "iNOS/NOS2 mRNA and protein expression in human CD8 T cells",
        "pathway_name": "CXCL12-CXCR4-NOS2-transcriptional-output",
        "route_linkage_status": (
            "manual_primary_cxcl12_cxcr4_nos2_output_route;graph_linked_route_source;"
            "primary_layer_linked;intracellular_continuation_unresolved;transcription_factor_unresolved;"
            "evidence_route_only"
        ),
        "evidence_summary": (
            "A primary study reports that CXCL12 induces iNOS/NOS2 mRNA and protein in primary human CD8 T "
            "cells through increased gene transcription and that the response tracks CXCR4 expression. The "
            "route preserves this ligand-receptor-to-transcriptional-output observation without assigning an "
            "intracellular kinase cascade or terminal transcription factor."
        ),
        "limitations": (
            "The study does not identify the intracellular relay or transcription factor responsible for NOS2 "
            "induction, and the response is cell-type and activation-state dependent. The row is intentionally "
            "a partial route rather than a completed mechanistic chain."
        ),
        "species_context": "human",
        "cell_type_context": "primary human CD8 T cells and humanized/allograft artery specimens",
        "assay_or_perturbation": "CXCL12 stimulation; CXCR4 measurement; iNOS mRNA/protein assays; iNOS promoter reporter; T-cell activation and CXCR4 downregulation assays",
    },
    {
        "name": "WNT5A-ROR2-JNK-JUNATF2-MMP13-output",
        "lr_edge_id": "M21B-E000472",
        "relay_node_id": "NODE06048",
        "tf_node_id": "NODE06054",
        "target_node_id": "",
        "source_queue_id": "",
        "source_record_id": "",
        "primary_locator": "PMID:22128168; PMCID:PMC3256912; DOI:10.1074/jbc.M111.315127",
        "path_expression": "ligand>receptor>intracellular>TF>output",
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|target_gene_node",
        "output_label": "MMP13/MMP-13 gene expression",
        "pathway_name": "WNT5A-ROR2-DVL2-Rac1-JNK-JUNATF2-MMP13",
        "route_linkage_status": (
            "manual_primary_wnt5a_ror2_jnk_jun_atf2_mmp13_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "intracellular_to_tf_edge_not_asserted;target_gene_node_unresolved;evidence_route_only"
        ),
        "evidence_summary": (
            "A primary osteosarcoma study reports WNT5A-ROR2-dependent MMP13 induction through DVL2, Rac1, "
            "JNK and AP-1-site recruitment of c-Jun and ATF2 at the MMP13 promoter. The route retains the "
            "JNK and JUN-ATF2 layers while exposing the MMP13 expression readout as an output because the "
            "current graph has no clean MMP13 target-gene node."
        ),
        "limitations": (
            "The study uses osteosarcoma cell lines and describes context-dependent DVL2 versus DVL3 usage. "
            "The terminal MMP13 output is primary-supported, but its graph target-gene identity is unresolved; "
            "no target-gene node or causal edge is invented."
        ),
        "species_context": "human osteosarcoma cell lines",
        "cell_type_context": "SaOS-2 and U2OS osteosarcoma cells",
        "assay_or_perturbation": "WNT5A/ROR2 suppression; DVL2 and Rac1 perturbation; JNK inhibition; MMP13 promoter reporter; ChIP for c-Jun and ATF2; MMP13 mRNA assays",
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
    queues = {row["queue_id"]: row for row in read_tsv(bundle / "mechanism_downstream_curation_queue.tsv")}
    records = {row["record_id"]: row for row in read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")}
    rows: list[dict[str, str]] = []
    for index, spec in enumerate(SPECS, start=1):
        lr = edges[spec["lr_edge_id"]]
        ligand = nodes[lr["source_node_id"]]
        receptor = nodes[lr["target_node_id"]]
        relay = nodes.get(spec["relay_node_id"], {})
        tf = nodes.get(spec["tf_node_id"], {})
        target = nodes.get(spec["target_node_id"], {})
        queue = queues.get(spec["source_queue_id"], {})
        record = records.get(spec["source_record_id"], {})
        evidence_ids = unique_join(
            lr.get("evidence_ids", ""),
            queue.get("source_evidence_ids", ""),
            record.get("source_evidence_ids", ""),
            spec["primary_locator"],
        )
        rows.append(
            {
                "expansion_id": f"M21B-LITEXP-GAPFULL-{index:03d}",
                "source_queue_id": spec["source_queue_id"],
                "route_status": "retained_evidence_route",
                "path_expression": spec["path_expression"],
                "route_tier": spec["route_tier"],
                "known_layers": spec["known_layers"],
                "missing_layers": spec["missing_layers"],
                "intracellular_status": "source_supported_composed" if spec["relay_node_id"] else "source_supported_output_only",
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
                "transcription_factor_label": tf.get("canonical_label", ""),
                "tf_target_edge_id": "",
                "target_gene_node_id": spec["target_node_id"],
                "target_gene_label": target.get("canonical_label", ""),
                "target_output_form_id": "",
                "output_node_id": "",
                "output_label": spec["output_label"],
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": spec["pathway_name"],
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression" if spec["target_node_id"] else "primary_functional_output",
                "evidence_ids": evidence_ids,
                "source_chain_id": f"M21B-LITEXP-GAPFULL-{index:03d}",
                "source_evidence_record_id": spec["source_record_id"],
                "route_linkage_status": spec["route_linkage_status"],
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression" if spec["target_node_id"] else "generic_functional_readout",
                "primary_locator": spec["primary_locator"],
                "citation_note": (
                    f"Primary-evidence route overlay for {spec['name']}. Unresolved handoffs and graph "
                    "target limitations are retained explicitly; no graph edge, causal assertion, or "
                    "confidence score is created."
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
