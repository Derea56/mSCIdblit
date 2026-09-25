#!/usr/bin/env python3
"""Build primary-evidence BMP-antagonist routes to SMAD1/5/8 and Id genes."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = [
    {
        "prefix": "NOG-BMP4",
        "ligand_edge_id": "M21B-E000842",
        "primary_locator": "PMID:27573479",
        "targets": [
            ("NODE04961", "ID1", "ID1 mRNA expression"),
            ("NODE04962", "ID2 gene", "Id2 expression"),
            ("NODE04964", "ID3 gene", "Id3 expression"),
        ],
        "pathway_name": "NOG-BMP4-BMPR-SMAD1-5-8-ID1-2-3",
        "species_context": "mouse",
        "cell_type_context": "developing muscle progenitors",
        "assay_or_perturbation": (
            "Noggin loss-of-function in developing mouse muscle; pSMAD1/5/8 immunoblot or "
            "immunostaining; Id1, Id2 and Id3 expression measurements"
        ),
        "effect_polarity": "inhibitory",
        "evidence_summary": (
            "A primary mouse study reports that loss of the secreted BMP antagonist Noggin increases "
            "BMP signaling, measured by SMAD1/5/8 phosphorylation, and induces the BMP target genes "
            "Id1, Id2 and Id3 in developing muscle progenitors. The route maps this inverse genetic "
            "perturbation onto the existing NOG-BMP4 antagonist edge and the exported BMP-SMAD relay."
        ),
        "limitations": (
            "The paper uses Noggin loss-of-function rather than a direct recombinant-Noggin/BMP4 "
            "time-course and measures the BMP response in developing muscle. It does not establish "
            "a single direct NOG-to-receptor-to-SMAD-to-Id chain, and the BMP ligand contribution "
            "is not resolved to BMP4 in that experiment. No graph edge, causal traversal, or database "
            "confidence score is created."
        ),
        "context_scope": "primary genetic perturbation; route layers retain source-specific context",
    },
    {
        "prefix": "CHRDL1-BMP7",
        "ligand_edge_id": "M21B-E007042",
        "primary_locator": "PMID:19357253; PMCID:PMC2678041; DOI:10.1681/ASN.2008070768",
        "targets": [
            ("NODE04961", "ID1", "ID1 mRNA expression"),
            ("NODE04962", "ID2 gene", "Id2 expression"),
            ("NODE04964", "ID3 gene", "Id3 expression"),
        ],
        "pathway_name": "CHRDL1-BMP7-BMPR-SMAD1-5-8-ID1-2-3",
        "species_context": "mouse and human cell systems",
        "cell_type_context": "P19, MDCK and HK-2 renal-cell systems",
        "assay_or_perturbation": (
            "recombinant BMP7, CHRDL1 and TWSG1 treatment; pSMAD1/5/8 immunoblot; Id1, Id2 and "
            "Id3 RT-PCR; CHRDL1/BMP7 co-precipitation and kidney-injury model"
        ),
        "effect_polarity": "context_dependent",
        "evidence_summary": (
            "A primary renal-signaling study reports that CHRDL1 associates with BMP7 and modulates "
            "BMP7-induced SMAD1/5/8 phosphorylation and Id1, Id2 and Id3 transcription. In the "
            "reported renal-cell context, CHRDL1-dependent suppression of the BMP7 response is most "
            "clear when TWSG1 is present; the route therefore preserves the cofactor dependence."
        ),
        "limitations": (
            "The response is context dependent: CHRDL1 alone had limited or different effects in some "
            "assays, while CHRDL1 plus TWSG1 reduced BMP7-associated signaling and Id transcription. "
            "The paper does not establish a single direct CHRDL1-to-receptor-to-SMAD-to-Id chain. "
            "No graph edge, causal traversal, or database confidence score is created."
        ),
        "context_scope": "composite primary evidence; TWSG1-dependent renal-cell context is explicit",
    },
]


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
    relay = nodes["NODE01301"]
    tf = nodes["NODE10440"]
    for spec in SPECS:
        lr = edges[spec["ligand_edge_id"]]
        ligand = nodes[lr["source_node_id"]]
        receptor = nodes[lr["target_node_id"]]
        for index, (target_node_id, target_label, output_label) in enumerate(spec["targets"], start=1):
            target = nodes[target_node_id]
            route_id = f"M21B-LITEXP-{spec['prefix']}-ID{index:02d}"
            rows.append(
                {
                    "expansion_id": route_id,
                    "source_queue_id": "",
                    "route_status": "retained_evidence_route",
                    "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                    "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                    "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                    "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
                    "intracellular_status": "source_supported_composed",
                    "ligand_node_id": lr["source_node_id"],
                    "ligand_label": ligand["canonical_label"],
                    "ligand_receptor_edge_id": spec["ligand_edge_id"],
                    "receptor_node_id": lr["target_node_id"],
                    "receptor_label": receptor["canonical_label"],
                    "receptor_intracellular_edge_id": "",
                    "intracellular_continuation_node_id": relay["node_id"],
                    "intracellular_continuation_label": relay["canonical_label"],
                    "intracellular_tf_edge_id": "",
                    "transcription_factor_node_id": tf["node_id"],
                    "transcription_factor_label": tf["canonical_label"],
                    "tf_target_edge_id": "",
                    "target_gene_node_id": target_node_id,
                    "target_gene_label": target["canonical_label"],
                    "target_output_form_id": "",
                    "output_node_id": "",
                    "output_label": output_label,
                    "output_form_id": "",
                    "bridge_id": "",
                    "pathway_name": spec["pathway_name"],
                    "input_evidence_type": "primary_literature_route_expansion",
                    "output_evidence_type": "primary_target_gene_expression",
                    "evidence_ids": unique_join(lr.get("evidence_ids", ""), spec["primary_locator"]),
                    "source_chain_id": route_id,
                    "source_evidence_record_id": "",
                    "route_linkage_status": (
                        f"manual_primary_{spec['prefix'].lower()}_id_route;graph_linked_route_source;"
                        "graph_linked_ligand_bmp_antagonist_edge;primary_layer_linked;"
                        "receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;"
                        "tf_to_target_edge_not_asserted;end_to_end_chain_not_asserted_by_single_source;"
                        "evidence_route_only"
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
                        f"Primary-evidence route overlay for {spec['pathway_name']}. "
                        "Unresolved handoffs and context dependence remain explicit."
                    ),
                    "evidence_summary": spec["evidence_summary"],
                    "limitations": spec["limitations"],
                    "curation_status": "curated_primary_route",
                    "species_context": spec["species_context"],
                    "cell_type_context": spec["cell_type_context"],
                    "compartment_context": "extracellular BMP antagonist; plasma-membrane receptor complex; intracellular signaling; nuclear output",
                    "injury_context": "no SCI transfer inferred; primary model context only",
                    "context_scope": spec["context_scope"],
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
    print(json.dumps({"output": str(args.output.resolve()), "rows": len(rows), "ligands": sorted({r["ligand_label"] for r in rows})}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
