#!/usr/bin/env python3
"""Build a primary-evidence GREM1/BMP4/SMAD/ID2 route.

GREM1 is a soluble BMP antagonist.  This evidence-layer route therefore
retains inhibitory polarity and does not imply that GREM1 productively
activates the BMP receptor complex.  The route records the experimentally
observed BMP4-responsive SMAD1/5/8 and ID2 layers while leaving the exact
receptor-to-relay and relay-to-TF handoffs unresolved.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPEC = {
    "name": "GREM1-BMP4-BMPR-SMAD1-5-8-ID2",
    "lr_edge_id": "M21B-E000844",
    "relay_node_id": "NODE01301",
    "tf_node_id": "NODE10440",
    "target_node_id": "NODE04962",
    "primary_locator": "PMID:27385727; PMCID:PMC5013871; DOI:10.1093/molehr/gaw044",
    "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
    "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
    "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
    "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
    "output_label": "ID2 mRNA expression",
    "pathway_name": "GREM1-BMP4-BMPR-SMAD1-5-8-ID2",
    "route_linkage_status": (
        "manual_primary_grem1_bmp4_smad_id2_route;graph_linked_route_source;"
        "graph_linked_ligand_bmp_antagonist_edge;"
        "primary_layer_linked;soluble_bmp_antagonism;receptor_to_intracellular_edge_not_asserted;"
        "intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;"
        "end_to_end_chain_not_asserted_by_single_source;evidence_route_only"
    ),
    "evidence_summary": (
        "A primary human fetal-ovarian somatic-cell study reports BMP4-induced ID2 expression and "
        "BMP4-dependent SMAD1/5/8 phosphorylation. Recombinant GREM1 reduced BMP4-mediated "
        "SMAD1/5/8 phosphorylation and abolished the BMP4-induced ID2 response. The route maps "
        "those observations onto the existing GREM1-BMP4 antagonist edge, BMP receptor signaling "
        "relay, SMAD1/5/8 transcription-factor node, and ID2 target-gene node."
    ),
    "limitations": (
        "The study uses primary human fetal-ovarian somatic-cell cultures and does not establish "
        "a single direct GREM1-to-receptor-to-SMAD-to-ID2 molecular chain. GREM1 is an extracellular "
        "BMP antagonist, so the route is inhibitory and should be interpreted as suppression of a "
        "BMP4 response rather than productive receptor activation. No graph edge, causal traversal, "
        "or database confidence score is created."
    ),
    "species_context": "human fetal ovary",
    "cell_type_context": "primary human fetal-ovarian somatic cells",
    "assay_or_perturbation": (
        "recombinant BMP4 and GREM1 treatment; SMAD1/5/8 phosphorylation assay; ID2 qRT-PCR; "
        "BMP4 plus GREM1 antagonism experiment"
    ),
}


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


def make_row(bundle: Path) -> dict[str, str]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    lr = edges[SPEC["lr_edge_id"]]
    ligand = nodes[lr["source_node_id"]]
    receptor = nodes[lr["target_node_id"]]
    relay = nodes[SPEC["relay_node_id"]]
    tf = nodes[SPEC["tf_node_id"]]
    target = nodes[SPEC["target_node_id"]]
    return {
        "expansion_id": "M21B-LITEXP-GREM1-ID2-001",
        "source_queue_id": "",
        "route_status": "retained_evidence_route",
        "path_expression": SPEC["path_expression"],
        "route_tier": SPEC["route_tier"],
        "known_layers": SPEC["known_layers"],
        "missing_layers": SPEC["missing_layers"],
        "intracellular_status": "source_supported_composed",
        "ligand_node_id": lr["source_node_id"],
        "ligand_label": ligand["canonical_label"],
        "ligand_receptor_edge_id": SPEC["lr_edge_id"],
        "receptor_node_id": lr["target_node_id"],
        "receptor_label": receptor["canonical_label"],
        "receptor_intracellular_edge_id": "",
        "intracellular_continuation_node_id": SPEC["relay_node_id"],
        "intracellular_continuation_label": relay["canonical_label"],
        "intracellular_tf_edge_id": "",
        "transcription_factor_node_id": SPEC["tf_node_id"],
        "transcription_factor_label": tf["canonical_label"],
        "tf_target_edge_id": "",
        "target_gene_node_id": SPEC["target_node_id"],
        "target_gene_label": target["canonical_label"],
        "target_output_form_id": "",
        "output_node_id": "",
        "output_label": SPEC["output_label"],
        "output_form_id": "",
        "bridge_id": "",
        "pathway_name": SPEC["pathway_name"],
        "input_evidence_type": "primary_literature_route_expansion",
        "output_evidence_type": "primary_target_gene_expression",
        "evidence_ids": unique_join(lr.get("evidence_ids", ""), SPEC["primary_locator"]),
        "source_chain_id": "M21B-LITEXP-GREM1-ID2-001",
        "source_evidence_record_id": "",
        "route_linkage_status": SPEC["route_linkage_status"],
        "causal_status": "not_asserted",
        "traversal_status": "evidence_route_not_causal",
        "evidence_contract_version": "mechanism_evidence_v1",
        "evidence_polarity": "supports",
        "negative_evidence_status": "not_evaluated",
        "evidence_directness": "composite_primary_route",
        "output_class": "target_gene_expression",
        "primary_locator": SPEC["primary_locator"],
        "citation_note": (
            "Primary-evidence route overlay for GREM1-BMP4-BMPR-SMAD1-5-8-ID2. "
            "The source supports inhibitory BMP4-response modulation; unresolved handoffs remain explicit."
        ),
        "evidence_summary": SPEC["evidence_summary"],
        "limitations": SPEC["limitations"],
        "curation_status": "curated_primary_route",
        "species_context": SPEC["species_context"],
        "cell_type_context": SPEC["cell_type_context"],
        "compartment_context": "extracellular BMP antagonist; plasma-membrane receptor complex; intracellular signaling; nuclear output",
        "injury_context": "no SCI transfer inferred; primary model context only",
        "context_scope": "composite primary evidence; route layers retain source-specific models",
        "assay_or_perturbation": SPEC["assay_or_perturbation"],
        "effect_polarity": "inhibitory",
        "source_scope": "composite_primary_evidence",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    row = make_row(args.bundle.resolve())
    args.output.resolve().write_text(json.dumps([row], indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output.resolve()), "rows": 1, "ligand": row["ligand_label"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
