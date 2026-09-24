#!/usr/bin/env python3
"""Build the next evidence-first route tranche for high-yield ligands.

These rows are deliberately evidence-layer overlays.  They preserve primary
literature support for component sequences while leaving any graph handoff
that is not directly asserted in the current graph unresolved.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "name": "IL27-IL27R-STAT1-STAT3-IL10",
        "lr_edge_id": "M21B-E008854",
        "relay_edge_id": "M21B-E008855",
        "relay_node_id": "NODE10718",
        "tf_node_id": "NODE10709",
        "target_node_id": "NODE05284",
        "primary_locator": "PMID:21041726; PMID:14565860; PMID:14764690",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "intracellular_to_tf_edge",
        "output_label": "IL10 gene transcription",
        "pathway_name": "IL27-IL27RA-gp130-STAT1-STAT3-IL10",
        "evidence_summary": (
            "Primary studies support IL-27 signaling through the IL-27RA/WSX-1:gp130 receptor complex, "
            "STAT1/STAT3 activation and IL10 transcription. A primary promoter study reports STAT1 and "
            "STAT3 recruitment to the IL10 promoter. The route retains the graph-linked receptor and relay "
            "components without asserting an unobserved relay-to-promoter-factor edge."
        ),
        "limitations": (
            "The supporting studies use source-specific immune-cell systems and do not establish every "
            "molecular handoff represented by the composed route. The route is evidence-only; it creates no "
            "causal graph edge and no database confidence score."
        ),
        "species_context": "mouse and human immune-cell systems",
        "cell_type_context": "T cells and macrophage/innate immune-cell models",
        "assay_or_perturbation": "IL-27 stimulation; STAT1/STAT3 activation; promoter occupancy and IL10 transcription assays",
    },
    {
        "name": "IL27-IL27R-STAT1-TBX21",
        "lr_edge_id": "M21B-E008854",
        "relay_edge_id": "M21B-E008855",
        "relay_node_id": "NODE10718",
        "tf_node_id": "NODE10705",
        "target_node_id": "NODE10908",
        "primary_locator": "PMID:14657353; PMID:15356135; PMID:14565860",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "intracellular_to_tf_edge",
        "output_label": "TBX21 gene expression",
        "pathway_name": "IL27-IL27RA-gp130-STAT1-TBX21",
        "evidence_summary": (
            "Primary IL-27 studies support STAT1-dependent induction of T-bet/TBX21 in T-helper-cell "
            "contexts, with STAT1 required for IL-27-induced T-bet expression. The graph-linked IL-27 "
            "receptor-to-STAT1/STAT3 relay is retained as the intracellular continuation."
        ),
        "limitations": (
            "The primary studies resolve IL-27 responsiveness and STAT1/T-bet dependence in specific "
            "T-cell contexts but do not establish a direct edge from the composite STAT1/STAT3 relay node "
            "to the STAT1 factor node. The route remains non-causal and evidence-only."
        ),
        "species_context": "mouse and human T-cell systems",
        "cell_type_context": "T helper-cell and T-cell activation models",
        "assay_or_perturbation": "IL-27 stimulation; STAT1 deficiency or inhibition; T-bet/TBX21 expression assays",
    },
    {
        "name": "IL17A-IL17RA-IL17RC-ACT1-NFkB-DEFB4",
        "lr_edge_id": "M21B-E000450",
        "relay_edge_id": "M21B-E001771",
        "relay_node_id": "NODE00152",
        "tf_node_id": "NODE07994",
        "target_node_id": "NODE02811",
        "primary_locator": "PMID:10748240; PMID:11692108; PMID:20231694; PMID:20935193",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "intracellular_to_tf_edge|tf_to_target_edge",
        "output_label": "DEFB4/hBD-2 expression",
        "pathway_name": "IL17A-IL17RA-IL17RC-ACT1-TRAF6-NFkB-DEFB4",
        "evidence_summary": (
            "Primary studies support IL-17A recognition by the IL-17RA/IL-17RC receptor complex, ACT1 "
            "proximal signaling and TRAF6-dependent NF-kB/JNK output. Independent primary epithelial-cell "
            "studies report IL-17-dependent antimicrobial DEFB4/hBD-2 induction and NF-kB promoter activity. "
            "The route therefore retains the biologically supported sequence while leaving direct TF and "
            "TF-to-DEFB4 graph handoffs unresolved."
        ),
        "limitations": (
            "The receptor, ACT1/TRAF6, NF-kB and DEFB4 observations come from complementary primary models; "
            "they are not a single demonstrated uninterrupted chain. The current graph has no IL17A-specific "
            "NF-kB-to-DEFB4 edge, so this is an evidence route rather than a causal traversal."
        ),
        "species_context": "human and mouse epithelial-cell systems",
        "cell_type_context": "airway and other epithelial-cell models",
        "assay_or_perturbation": "IL-17A stimulation; IL-17RC/ACT1/TRAF6 perturbation; NF-kB/JNK inhibition; DEFB4/hBD-2 expression assays",
    },
    {
        "name": "IL17A-IL17RA-IL17RC-ACT1-NFkB-CCL20",
        "lr_edge_id": "M21B-E000450",
        "relay_edge_id": "M21B-E001771",
        "relay_node_id": "NODE00152",
        "tf_node_id": "NODE07994",
        "target_node_id": "NODE01682",
        "primary_locator": "PMID:10748240; PMID:16272323; PMID:20231694",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "intracellular_to_tf_edge|tf_to_target_edge",
        "output_label": "CCL20 gene expression",
        "pathway_name": "IL17A-IL17RA-IL17RC-ACT1-TRAF6-MEK-NFkB-CCL20",
        "evidence_summary": (
            "Primary work supports IL-17 receptor/ACT1/TRAF6 signaling and reports IL-17-induced CCL20 "
            "expression through MEK and NF-kB-dependent mechanisms in airway epithelial cells. The route "
            "retains the graph-linked IL17A receptor and ACT1 components and represents the NF-kB program as "
            "the candidate transcriptional layer."
        ),
        "limitations": (
            "The CCL20 study uses epithelial-cell models and pharmacologic pathway perturbations; the exact "
            "IL17A-specific ACT1-to-NF-kB and NF-kB-to-CCL20 handoffs are not represented by matching graph "
            "edges. No causal edge or confidence score is added."
        ),
        "species_context": "human and mouse airway epithelial-cell systems",
        "cell_type_context": "airway epithelial cells",
        "assay_or_perturbation": "IL-17 stimulation; MEK/NF-kB pathway inhibition; CCL20 mRNA and protein assays",
    },
    {
        "name": "HBEGF-EGFR-ERK-EGR1-CYP24A1",
        "lr_edge_id": "M20B-E001250",
        "relay_node_id": "NODE03364",
        "tf_node_id": "NODE03137",
        "target_node_id": "NODE02742",
        "primary_locator": "PMID:33159963",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
        "output_label": "CYP24A1 mRNA expression",
        "pathway_name": "HBEGF-EGFR-ERK-EGR1-CYP24A1",
        "evidence_summary": (
            "A primary study reports HBEGF-induced EGFR phosphorylation and ERK activation together with "
            "EGR1 and CYP24A1 mRNA induction; EGFR inhibition blocks the HBEGF response. The route connects "
            "the existing HBEGF-EGFR ligand-receptor entry to the observed ERK/EGR1 and CYP24A1 outputs while "
            "preserving the unasserted intracellular handoffs."
        ),
        "limitations": (
            "The primary study does not establish direct EGR1 binding at the CYP24A1 locus or an exact "
            "HBEGF-EGFR-to-ERK graph edge in this release. The composed route is evidence-only and does not "
            "create causal traversal."
        ),
        "species_context": "human and mouse experimental systems",
        "cell_type_context": "HEK293 and related receptor-response models",
        "assay_or_perturbation": "HBEGF stimulation; EGFR inhibition; ERK activation; EGR1 and CYP24A1 mRNA assays",
    },
    {
        "name": "PDGFA-PDGFRA-ERK-ELK1-EGR1",
        "lr_edge_id": "M21B-E000760",
        "relay_node_id": "NODE03364",
        "tf_node_id": "NODE03165",
        "target_node_id": "NODE03139",
        "tf_target_edge_id": "M22B-E000158",
        "primary_locator": "PMID:8214093; PMID:19030102",
        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
        "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge",
        "output_label": "EGR1 promoter activity and expression",
        "pathway_name": "PDGFA-PDGFRA-ERK-ELK1-EGR1",
        "evidence_summary": (
            "Primary mesangial-cell work reports PDGF-induced Egr-1 transcription through serum-response "
            "elements in the Egr-1 promoter, while broader primary PDGF-PDGFR dissection supports MAPK/ERK "
            "signaling downstream of receptor activation. The current graph's ELK1-to-EGR1-promoter edge is "
            "retained, with the PDGFA-to-ERK and ERK-to-ELK1 handoffs left explicit as unresolved evidence layers."
        ),
        "limitations": (
            "The primary promoter study does not by itself identify PDGFRA, ERK and ELK1 as one uninterrupted "
            "molecular chain, and the broader signaling study is not a substitute for a direct PDGFA-specific "
            "handoff. This route is therefore non-causal and should be scored by mSCS using its component evidence."
        ),
        "species_context": "rat mesangial-cell and mammalian PDGF-PDGFR models",
        "cell_type_context": "rat mesangial cells and receptor-signaling models",
        "assay_or_perturbation": "PDGF stimulation; promoter SRE reporter/deletion assays; MAPK/PDGFR pathway perturbation; Egr-1 expression assays",
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
        relay = nodes[spec["relay_node_id"]]
        tf = nodes.get(spec["tf_node_id"], {})
        target = nodes.get(spec["target_node_id"], {})
        relay_edge_id = spec.get("relay_edge_id", "")
        tf_target_edge_id = spec.get("tf_target_edge_id", "")
        evidence_ids = unique_join(
            lr.get("evidence_ids", ""),
            relay_edge_id and edges.get(relay_edge_id, {}).get("evidence_ids", ""),
            tf_target_edge_id and edges.get(tf_target_edge_id, {}).get("evidence_ids", ""),
            spec["primary_locator"],
        )
        route_id = f"M21B-LITEXP-HIGH-YIELD-{index:03d}"
        rows.append(
            {
                "expansion_id": route_id,
                "source_queue_id": "",
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
                "tf_target_edge_id": tf_target_edge_id,
                "target_gene_node_id": spec["target_node_id"],
                "target_gene_label": target.get("canonical_label", ""),
                "target_output_form_id": "",
                "output_node_id": "",
                "output_label": spec["output_label"],
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": spec["pathway_name"],
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": evidence_ids,
                "source_chain_id": route_id,
                "source_evidence_record_id": "",
                "route_linkage_status": (
                    "graph_linked_route_source;primary_layer_linked;"
                    "evidence_route_only;unresolved_handoffs_retained"
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
                    f"Primary-evidence route overlay for {spec['name']}. Component evidence is retained for "
                    "mSCS plausibility scoring; unresolved handoffs remain explicit and no graph edge, causal "
                    "assertion, or confidence score is created."
                ),
                "evidence_summary": spec["evidence_summary"],
                "limitations": spec["limitations"],
                "curation_status": "curated_primary_route",
                "species_context": spec["species_context"],
                "cell_type_context": spec["cell_type_context"],
                "compartment_context": "extracellular ligand; plasma-membrane receptor; cytoplasmic signaling; nuclear target-gene context",
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
