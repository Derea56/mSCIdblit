#!/usr/bin/env python3
"""Build primary-evidence TNF/TNFR/NF-kB transcriptional route overlays."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROUTES = (
    {
        "suffix": "TNFR1-IL6",
        "lr_edge_id": "M21B-E000110",
        "receptor_id": "NODE11291",
        "receptor_label": "TNFR1/p55 receptor",
        "target_id": "NODE05511",
        "target_label": "IL6 gene",
        "tf_id": "NODE09694",
        "tf_label": "RELA",
        "tf_target_edge_id": "M21B-E008632",
        "locators": "PMID:2158863; PMID:8565075; PMID:16611992; PMID:1644898; PMID:8134378; PMCID:PMC43343",
        "pathway": "TNF-TNFR1-TRADD-NF-kB-RELA-IL6",
        "summary": (
            "Primary receptor studies support TNF engagement of TNFR1 and TRADD/TRAF2-linked NF-kB signaling. "
            "Primary astrocyte experiments show TNF-alpha-induced IL6 transcription through an NF-kB-like promoter "
            "element, while independent promoter work supports RELA/NF-kB control of IL6 transcription. The route "
            "retains the TNFR1 input, NF-kB intracellular continuation, RELA transcription-factor layer, and IL6 "
            "target-gene output as separately bounded evidence layers."
        ),
        "limitations": (
            "The receptor-complex, NF-kB relay, and IL6 promoter studies use complementary human, rat, and monocyte "
            "models; they do not establish every handoff in one experiment or assign the astrocyte IL6 response to "
            "TNFR1 alone. No SCI transfer, causal traversal, or database confidence score is inferred."
        ),
        "assay": "TNF stimulation and receptor-binding assays; TNFR1/TRADD/TRAF2 pathway studies; NF-kB promoter-site and IL6 transcription assays",
        "cell_context": "Human TNFR1-binding systems, primary rat astrocytes, and primary human monocytes",
    },
    {
        "suffix": "TNFR2-IL6",
        "lr_edge_id": "M21B-E001764",
        "receptor_id": "NODE11294",
        "receptor_label": "TNFR2 receptor complex",
        "target_id": "NODE05511",
        "target_label": "IL6 gene",
        "tf_id": "NODE09694",
        "tf_label": "RELA",
        "tf_target_edge_id": "M21B-E008632",
        "locators": "PMID:21081755; PMID:7544915; PMCID:PMC2844188; PMID:20038584; DOI:10.1074/jbc.M109.037341; PMID:1644898; PMID:8134378; PMCID:PMC43343",
        "pathway": "TNF-TNFR2-TRAF2-NF-kB-RELA-IL6",
        "summary": (
            "Primary receptor-aggregation and receptor-selective studies support membrane or oligomerized TNF "
            "engagement of TNFR2, TRAF2-dependent signaling, and NF-kB pathway activation. Complementary primary "
            "astrocyte and promoter studies support TNF-induced NF-kB-like IL6 transcription and RELA/NF-kB control "
            "of the IL6 promoter. The route therefore retains a TNFR2-specific receptor layer with an explicit NF-kB, "
            "RELA, and IL6 output sequence."
        ),
        "limitations": (
            "TNFR2 evidence is strongest for membrane/oligomerized TNF and receptor-selective signaling, whereas the "
            "IL6 output studies use TNF-alpha-stimulated astrocytes and monocytes without isolating TNFR2. The route "
            "is a composed evidence overlay and does not assert a TNFR2-specific IL6 causal chain or SCI transfer."
        ),
        "assay": "Membrane/oligomerized TNF receptor-aggregation assays; TNFR2/TRAF2 and alternative NF-kB studies; NF-kB and IL6 promoter/transcription assays",
        "cell_context": "TNFR2-expressing reporter/receptor systems, primary rat astrocytes, and primary human monocytes",
    },
    {
        "suffix": "TNFR2-ICAM1",
        "lr_edge_id": "M21B-E001764",
        "receptor_id": "NODE11294",
        "receptor_label": "TNFR2 receptor complex",
        "target_id": "NODE04944",
        "target_label": "ICAM1/CD54 gene",
        "tf_id": "NODE07976",
        "tf_label": "NF-kB RelA/c-Rel-containing complex",
        "tf_target_edge_id": "M21B-E008200",
        "locators": "PMID:21081755; PMID:7544915; PMCID:PMC2844188; PMID:20038584; DOI:10.1074/jbc.M109.037341; PMID:7910170; PMID:9442377; DOI:10.1016/S0171-2985(97)80026-5",
        "pathway": "TNF-TNFR2-TRAF2-NF-kB-ICAM1",
        "summary": (
            "Primary TNFR2 receptor-aggregation and membrane-TNF studies support TNFR2/TRAF2-dependent NF-kB "
            "signaling. Primary astrocyte work reports TNF-induced ICAM1 transcription, and promoter studies in "
            "TNF-stimulated monocytes show RelA-containing NF-kB complexes binding and transactivating the ICAM1 "
            "kappa-B site. The route retains these layers as an evidence-supported TNFR2-to-NF-kB-to-ICAM1 sequence."
        ),
        "limitations": (
            "The ICAM1 promoter and astrocyte studies do not isolate TNFR2, and the TNFR2-specific studies use "
            "membrane/oligomerized TNF and receptor-expression systems. Exact receptor-to-relay handoffs remain "
            "source-supported rather than newly asserted graph edges; no SCI transfer or database confidence score is inferred."
        ),
        "assay": "TNFR2 receptor-aggregation and TRAF2/NF-kB assays; TNF-stimulated astrocyte ICAM1 transcription; ICAM1 kappa-B reporter, EMSA, and RelA/c-Rel transactivation assays",
        "cell_context": "TNFR2-expressing receptor systems, primary rat astrocytes, and human THP-1 monocytes",
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
    for index, spec in enumerate(ROUTES, start=1):
        lr = edges[spec["lr_edge_id"]]
        if (lr["source_node_id"], lr["target_node_id"]) != ("NODE11244", spec["receptor_id"]):
            raise ValueError(f"Unexpected TNF ligand-receptor endpoints for {spec['suffix']}")
        for node_id in ("NODE11244", spec["receptor_id"], "NODE05080", spec["tf_id"], spec["target_id"]):
            if node_id not in nodes:
                raise ValueError(f"{spec['suffix']}: missing node {node_id}")
        tf_edge = edges.get(spec["tf_target_edge_id"])
        if not tf_edge or (tf_edge["source_node_id"], tf_edge["target_node_id"]) != (spec["tf_id"], spec["target_id"]):
            raise ValueError(f"{spec['suffix']}: TF-target edge endpoints do not match")
        expansion_id = f"M21B-LITEXP-TNF-{spec['suffix']}-001"
        evidence_ids = unique_join(lr.get("evidence_ids", ""), tf_edge.get("evidence_ids", ""), spec["locators"])
        rows.append(
            {
                "expansion_id": expansion_id,
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge",
                "intracellular_status": "source_supported_composed",
                "ligand_node_id": "NODE11244",
                "ligand_label": nodes["NODE11244"]["canonical_label"],
                "ligand_receptor_edge_id": spec["lr_edge_id"],
                "receptor_node_id": spec["receptor_id"],
                "receptor_label": spec["receptor_label"],
                "receptor_intracellular_edge_id": "",
                "intracellular_continuation_node_id": "NODE05080",
                "intracellular_continuation_label": nodes["NODE05080"]["canonical_label"],
                "intracellular_tf_edge_id": "",
                "transcription_factor_node_id": spec["tf_id"],
                "transcription_factor_label": spec["tf_label"],
                "tf_target_edge_id": spec["tf_target_edge_id"],
                "target_gene_node_id": spec["target_id"],
                "target_gene_label": spec["target_label"],
                "target_output_form_id": "",
                "output_node_id": spec["target_id"],
                "output_label": f"{spec['target_label']} expression",
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": spec["pathway"],
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_gene_expression",
                "evidence_ids": evidence_ids,
                "source_chain_id": expansion_id,
                "source_evidence_record_id": "",
                "route_linkage_status": (
                    "manual_primary_tnf_tnfr_nfkb_route;graph_linked_route_source;primary_layer_linked;"
                    "receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;"
                    "tf_to_target_edge_graph_linked;evidence_route_only"
                ),
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "target_gene_expression",
                "primary_locator": spec["locators"],
                "citation_note": "Primary source locators are retained for the receptor-specific TNF branch, NF-kB continuation, and target-gene evidence layers.",
                "evidence_summary": spec["summary"],
                "limitations": spec["limitations"],
                "curation_status": "curated_primary_route",
                "species_context": "human; mouse; rat",
                "cell_type_context": spec["cell_context"],
                "compartment_context": "extracellular TNF; plasma-membrane TNFR; cytoplasmic NF-kB signaling; nuclear TF and target-gene promoter",
                "injury_context": "no SCI transfer inferred; primary receptor, immune, monocyte, and astrocyte model contexts only",
                "context_scope": "composite_primary_evidence",
                "assay_or_perturbation": spec["assay"],
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
