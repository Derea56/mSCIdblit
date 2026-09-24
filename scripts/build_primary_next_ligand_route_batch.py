#!/usr/bin/env python3
"""Build a bounded primary-evidence tranche for currently incomplete ligands.

These records extend the evidence layer only.  They retain explicit missing
handoffs where the primary study supports a downstream response but the
current graph does not contain a matching edge or a terminal TF/target-gene
assertion.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "FGF2-FGFR1-ERK-EGR1-GDNF",
        "lr_edge_id": "M20B-E001875",
        "relay_node_id": "NODE03370",
        "tf_node_id": "NODE03137",
        "target_node_id": "NODE04062",
        "source_queue_id": "M21B-DOWNSTREAM:00446",
        "source_record_id": "M21B-DOWNSTREAM-EVID:000772",
        "primary_locator": "PMCID:PMC2781613; PMID:19721135; DOI:10.1074/jbc.M109.010678",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "output_label": "GDNF mRNA expression in rat astroglial cells",
        "pathway_name": "FGF2-FGFR1-ERK-JNK-Elk1-EGR1-GDNF",
        "route_linkage_status": (
            "manual_primary_fgf2_erk_egr1_gdnf_route;primary_layer_linked;"
            "receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;"
            "tf_to_target_edge_not_asserted;single_primary_downstream_chain_with_separate_lr_evidence;"
            "evidence_route_only"
        ),
        "evidence_summary": (
            "A primary astrocyte study reports FGF2-induced ERK and JNK signaling, Elk-1 activity, "
            "Egr-1 induction and direct Egr-1 binding to the Gdnf promoter; loss of Egr-1 attenuates "
            "FGF2-induced Gdnf expression. The FGF2-FGFR1 input is retained from the existing graph "
            "and receptor-proximal evidence layer."
        ),
        "limitations": (
            "The primary downstream study uses rat astrocytes, C6 glioma cells and Egr-1 knockout "
            "astrocytes; it does not by itself establish the exact FGF2-FGFR1 receptor handoff. "
            "ERK/JNK-to-Elk-1 and Elk-1/Egr-1-to-Gdnf are retained as an evidence route without "
            "creating graph edges, causal traversal or a database confidence score."
        ),
        "species_context": "rat astrocytes; C6 glioma cells; mouse Egr-1 knockout astrocytes",
        "cell_type_context": "primary astrocytes and C6 glioma cells",
        "assay_or_perturbation": "FGF2 stimulation; ERK/JNK inhibition; Elk-1 reporter; Egr-1 ChIP; Egr-1 siRNA/knockout; Gdnf promoter and mRNA assays",
    },
    {
        "name": "LPA-LPAR1-ERK-EGR1",
        "lr_edge_id": "M21B-E001512",
        "relay_node_id": "NODE06483",
        "tf_node_id": "",
        "target_node_id": "NODE03139",
        "source_queue_id": "M21B-DOWNSTREAM:00671",
        "source_record_id": "M21B-DOWNSTREAM-EVID:001131",
        "primary_locator": "PMID:9600933; PMID:22577133; DOI:10.1074/jbc.M112.363218",
        "path_expression": "ligand>receptor>intracellular>????>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_output_missing_tf",
        "known_layers": "ligand|receptor|intracellular_continuation|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|transcription_factor|intracellular_to_tf_edge",
        "output_label": "EGR1 promoter/mRNA expression",
        "pathway_name": "LPA-LPAR1-PKCdelta-ERK-JNK-EGR1",
        "route_linkage_status": (
            "manual_primary_lpa_lpar1_erk_egr1_route;primary_layer_linked;"
            "receptor_to_intracellular_edge_not_asserted;transcription_factor_unresolved;"
            "intracellular_to_tf_edge_not_asserted;evidence_route_only"
        ),
        "evidence_summary": (
            "Primary LPA1 studies support LPA binding and receptor activation. A separate primary "
            "vascular smooth-muscle study reports LPA1-dependent PKC-delta-mediated ERK/JNK activation "
            "required for Egr-1 mRNA and protein induction. The route therefore retains the intracellular "
            "MAPK continuation and terminal EGR1 expression while leaving the TF handoff unresolved."
        ),
        "limitations": (
            "The downstream study uses rat vascular smooth-muscle cells and pharmacologic kinase or "
            "dominant-negative perturbations; a direct TF identity between ERK/JNK and the EGR1 promoter "
            "is not asserted here. No new receptor-to-MAPK or causal graph edge is created."
        ),
        "species_context": "rat vascular smooth-muscle cells",
        "cell_type_context": "vascular smooth-muscle cells",
        "assay_or_perturbation": "LPA stimulation; LPAR1 dependence; PKC-delta perturbation; ERK/JNK inhibitors; Egr-1 mRNA/protein assays",
    },
    {
        "name": "VEGFA-VEGFR2-PLCgamma-PKC-ERK-output",
        "lr_edge_id": "M21B-E000183",
        "relay_node_id": "NODE09093",
        "tf_node_id": "",
        "target_node_id": "",
        "source_queue_id": "",
        "source_record_id": "",
        "primary_locator": "PMID:10671553; PMID:15920019",
        "path_expression": "ligand>receptor>intracellular>????>output",
        "route_tier": "ligand_receptor_intracellular_output_missing_tf",
        "known_layers": "ligand|receptor|intracellular_continuation|output",
        "missing_layers": "receptor_to_intracellular_edge|transcription_factor|target_gene_expression",
        "output_label": "VEGF-RTK-PLCgamma-PKC-ERK endothelial proliferation output",
        "pathway_name": "VEGFA-VEGFR2-PLCgamma-PKC-ERK-endothelial-output",
        "route_linkage_status": (
            "manual_primary_vegfa_vegfr2_plcg1_erk_route;graph_linked_route_source;"
            "primary_layer_linked;receptor_to_intracellular_edge_not_asserted;"
            "transcription_factor_unresolved;target_gene_expression_unresolved;evidence_route_only"
        ),
        "evidence_summary": (
            "Primary VEGF receptor studies support VEGFR2/KDR-dependent PLCgamma, PKC and ERK signaling "
            "and endothelial proliferation. The route is retained as an intracellular-to-functional-output "
            "record without assigning a terminal TF or target gene."
        ),
        "limitations": (
            "The primary output study resolves receptor-proximal signaling and endothelial proliferation "
            "rather than a terminal transcription factor or gene. The exact receptor-complex-to-PLCG1 "
            "handoff is preserved as unresolved in this evidence layer."
        ),
        "species_context": "mammalian endothelial-cell and receptor-reconstitution models",
        "cell_type_context": "endothelial cells and receptor-reconstituted cells",
        "assay_or_perturbation": "VEGF stimulation; KDR/VEGFR2 receptor expression; PLCgamma, PKC, PI3K and MEK inhibition; DNA-synthesis/proliferation assays",
    },
    {
        "name": "Norepinephrine-ADRA1A-Gq-CREB-output",
        "lr_edge_id": "M21B-E001452",
        "relay_edge_id": "M21B-E001834",
        "relay_node_id": "NODE04294",
        "tf_node_id": "NODE02454",
        "target_node_id": "",
        "source_queue_id": "M21B-DOWNSTREAM:00632",
        "source_record_id": "M21B-DOWNSTREAM-EVID:001077",
        "primary_locator": "PMID:11358336; PMID:9792725; DOI:10.1074/jbc.273.45.30033",
        "path_expression": "ligand>receptor>intracellular>TF>output",
        "route_tier": "ligand_receptor_intracellular_tf_output_missing_target_gene",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|output",
        "missing_layers": "tf_to_target_gene_expression",
        "output_label": "CREB phosphorylation and cAMP-responsive enhancer activation",
        "pathway_name": "Norepinephrine-ADRA1A-Gq-cAMP-PKA-CREB-output",
        "route_linkage_status": (
            "manual_primary_norepinephrine_adra1a_creb_route;primary_layer_linked;"
            "receptor_to_intracellular_edge_asserted_as_graph_edge;intracellular_to_tf_edge_not_asserted;"
            "tf_to_target_gene_expression_not_asserted;evidence_route_only"
        ),
        "evidence_summary": (
            "Primary cloned-alpha1-adrenoceptor work supports norepinephrine-dependent receptor signaling. "
            "A separate primary study reports alpha1A/alpha1B-dependent CREB phosphorylation and cAMP "
            "responsive-enhancer activation through a PKA-dependent pathway; no terminal target gene is "
            "assigned."
        ),
        "limitations": (
            "The receptor-subtype and CREB studies use heterologous Rat1-cell systems and distinguish "
            "alpha1 subtypes; the exact Gq-to-CREB molecular handoff and target-gene identity remain "
            "unasserted. No causal edge or confidence score is created."
        ),
        "species_context": "human alpha1-adrenoceptor constructs in Rat1 cells",
        "cell_type_context": "Rat1 cells expressing cloned alpha1-adrenoceptor subtypes",
        "assay_or_perturbation": "norepinephrine stimulation; alpha1 subtype expression; CREB phosphorylation; cAMP-responsive enhancer reporter; PKA inhibition",
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
        relay = nodes[spec["relay_node_id"]]
        tf = nodes.get(spec["tf_node_id"], {})
        target = nodes.get(spec["target_node_id"], {})
        relay_edge_id = spec.get("relay_edge_id", "")
        record = records.get(spec["source_record_id"], {})
        queue = queues.get(spec["source_queue_id"], {})
        evidence_ids = unique_join(
            lr.get("evidence_ids", ""),
            relay_edge_id and edges.get(relay_edge_id, {}).get("evidence_ids", ""),
            queue.get("source_evidence_ids", ""),
            record.get("source_evidence_ids", ""),
            spec["primary_locator"],
        )
        row = {
            "expansion_id": f"M21B-LITEXP-NEXT-LIGAND-{index:03d}",
            "source_queue_id": spec["source_queue_id"],
            "route_status": "retained_evidence_route",
            "path_expression": spec["path_expression"],
            "route_tier": spec["route_tier"],
            "known_layers": spec["known_layers"],
            "missing_layers": spec["missing_layers"],
            "intracellular_status": "source_supported_composed",
            "ligand_node_id": lr["source_node_id"],
            "ligand_label": ligand["canonical_label"],
            "ligand_receptor_edge_id": spec["lr_edge_id"],
            "receptor_node_id": lr["target_node_id"],
            "receptor_label": receptor["canonical_label"],
            "receptor_intracellular_edge_id": relay_edge_id,
            "intracellular_continuation_node_id": spec["relay_node_id"],
            "intracellular_continuation_label": relay["canonical_label"],
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
            "source_chain_id": f"M21B-LITEXP-NEXT-LIGAND-{index:03d}",
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
                f"Primary-evidence route overlay for {spec['name']}. Source-specific layer boundaries and "
                "unresolved handoffs are retained explicitly; no new graph edge, causal assertion, or "
                "confidence score is created."
            ),
            "evidence_summary": spec["evidence_summary"],
            "limitations": spec["limitations"],
            "curation_status": "curated_primary_route",
            "species_context": spec["species_context"],
            "cell_type_context": spec["cell_type_context"],
            "compartment_context": "extracellular ligand; plasma-membrane receptor; cytoplasmic signaling; nuclear or functional output context",
            "injury_context": "no SCI transfer inferred; primary model context only",
            "context_scope": "composite primary evidence; route layers retain source-specific models",
            "assay_or_perturbation": spec["assay_or_perturbation"],
            "effect_polarity": "activating",
            "source_scope": "composite_primary_evidence",
        }
        rows.append(row)
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
