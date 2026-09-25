#!/usr/bin/env python3
"""Build source-linked IL-11 and IL-36alpha route overlays.

The primary studies support the ligand, receptor/proximal, intracellular, and
gene-expression layers.  The records intentionally retain unresolved handoffs
between those layers; they do not create causal graph edges or confidence
scores.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


SPECS = (
    {
        "family": "IL11",
        "expansion_id": "M21B-LITEXP-IL11-STAT3-IL33-001",
        "ligand_node_id": "NODE05292",
        "ligand_receptor_edge_id": "M21B-E001757",
        "receptor_node_id": "NODE05295",
        "relay_node_id": "NODE05100",
        "tf_node_id": "NODE10726",
        "target_node_id": "NODE05469",
        "target_edge_id": "M21B-E008975",
        "pathway_name": "IL11-IL11R-gp130-STAT3-IL33",
        "primary_locator": "PMID:36012165; PMCID:PMC9408968; PMID:11141475; PMCID:PMC1850253",
        "evidence_ids": "M21B-E001757;M21B-E008857;M21B-E008975;M21B-EVID-008921;PMID:36012165;PMCID:PMC9408968;PMID:11141475;PMCID:PMC1850253",
        "citation_note": "Primary human fibroblast study: IL-11 caused transient STAT3 phosphorylation and IL33 induction; STAT3 inhibition prevented the IL33 response. The receptor/proximal IL-11 evidence is retained from the primary-supported graph layer.",
        "cell_type_context": "primary human kidney, lung, and skin fibroblasts; human DU-145 epithelial comparator",
        "assay_or_perturbation": "IL-11 stimulation; time-course RNA-seq/qPCR; STAT3 phosphorylation; STAT3 inhibition; IL-33 expression and secretome assays",
    },
    {
        "family": "IL11",
        "expansion_id": "M21B-LITEXP-IL11-STAT3-CCL20-001",
        "ligand_node_id": "NODE05292",
        "ligand_receptor_edge_id": "M21B-E001757",
        "receptor_node_id": "NODE05295",
        "relay_node_id": "NODE05100",
        "tf_node_id": "NODE10726",
        "target_node_id": "NODE01682",
        "target_edge_id": "M21B-E008976",
        "pathway_name": "IL11-IL11R-gp130-STAT3-CCL20",
        "primary_locator": "PMID:36012165; PMCID:PMC9408968; PMID:11141475; PMCID:PMC1850253",
        "evidence_ids": "M21B-E001757;M21B-E008857;M21B-E008976;M21B-EVID-008922;PMID:36012165;PMCID:PMC9408968;PMID:11141475;PMCID:PMC1850253",
        "citation_note": "Primary human fibroblast study: IL-11 produced an early STAT3-associated inflammatory transcriptional response including CCL20 induction. The source also measured CCL20 in the fibroblast secretome; transcription and secretion remain separate layers here.",
        "cell_type_context": "primary human kidney, lung, and skin fibroblasts; human DU-145 epithelial comparator",
        "assay_or_perturbation": "IL-11 stimulation; time-course RNA-seq/qPCR; STAT3 phosphorylation and inhibition; CCL20 transcript and secretome assays",
    },
    {
        "family": "IL11",
        "expansion_id": "M21B-LITEXP-IL11-STAT3-CXCL8-001",
        "ligand_node_id": "NODE05292",
        "ligand_receptor_edge_id": "M21B-E001757",
        "receptor_node_id": "NODE05295",
        "relay_node_id": "NODE05100",
        "tf_node_id": "NODE10726",
        "target_node_id": "NODE02684",
        "target_edge_id": "M21B-E008977",
        "pathway_name": "IL11-IL11R-gp130-STAT3-CXCL8",
        "primary_locator": "PMID:36012165; PMCID:PMC9408968; PMID:11141475; PMCID:PMC1850253",
        "evidence_ids": "M21B-E001757;M21B-E008857;M21B-E008977;M21B-EVID-008923;PMID:36012165;PMCID:PMC9408968;PMID:11141475;PMCID:PMC1850253",
        "citation_note": "Primary human fibroblast study: IL-11 produced an early STAT3-associated inflammatory transcriptional response including CXCL8/IL-8 induction. Transcript and secretome observations are retained as distinct evidence layers.",
        "cell_type_context": "primary human kidney, lung, and skin fibroblasts; human DU-145 epithelial comparator",
        "assay_or_perturbation": "IL-11 stimulation; time-course RNA-seq/qPCR; STAT3 phosphorylation and inhibition; CXCL8 transcript and secretome assays",
    },
    {
        "family": "IL11",
        "expansion_id": "M21B-LITEXP-IL11-STAT3-IL6-001",
        "ligand_node_id": "NODE05292",
        "ligand_receptor_edge_id": "M21B-E001757",
        "receptor_node_id": "NODE05295",
        "relay_node_id": "NODE05100",
        "tf_node_id": "NODE10726",
        "target_node_id": "NODE05233",
        "target_edge_id": "M21B-E008978",
        "pathway_name": "IL11-IL11R-gp130-STAT3-IL6",
        "primary_locator": "PMID:36012165; PMCID:PMC9408968; PMID:11141475; PMCID:PMC1850253",
        "evidence_ids": "M21B-E001757;M21B-E008857;M21B-E008978;M21B-EVID-008924;PMID:36012165;PMCID:PMC9408968;PMID:11141475;PMCID:PMC1850253",
        "citation_note": "Primary human fibroblast study: IL-11-associated early inflammatory transcription included IL6 induction and increased IL-6 in the fibroblast secretome. Gene and protein-output layers remain separate here.",
        "cell_type_context": "primary human kidney, lung, and skin fibroblasts; human DU-145 epithelial comparator",
        "assay_or_perturbation": "IL-11 stimulation; time-course RNA-seq/qPCR; STAT3 phosphorylation; IL-6 transcript and secretome assays",
    },
    {
        "family": "IL36",
        "expansion_id": "M21B-LITEXP-IL36A-NFKB-CXCL1-001",
        "ligand_node_id": "NODE05482",
        "ligand_receptor_edge_id": "M21B-E001758",
        "receptor_node_id": "NODE05401",
        "relay_node_id": "NODE07613",
        "tf_node_id": "NODE07984",
        "target_node_id": "NODE02622",
        "target_edge_id": "M21B-E008788",
        "pathway_name": "IL36A-IL36R-MyD88-IRAK-NFkB-CXCL1",
        "primary_locator": "PMID:24829417; PMCID:PMC4048788; PMID:29180446; PMCID:PMC5767850",
        "evidence_ids": "M21B-E001758;M24B-E000096;M21B-E008788;M21B-EVID-001701;M24B-EVID-000133;M21B-EVID-008734;PMID:24829417;PMCID:PMC4048788;PMID:29180446;PMCID:PMC5767850",
        "citation_note": "Primary human keratinocyte study: IL-36alpha induced CXCL1 mRNA. Primary receptor studies support IL-36R/IL-1RAcP activation, while the reviewed graph layer retains the MyD88/IRAK/NF-kB/MAPK continuation.",
        "cell_type_context": "post-confluent normal human keratinocytes; receptor-reconstituted mammalian cells",
        "assay_or_perturbation": "recombinant truncated IL-36alpha; qRT-PCR; IL-36R/IL-1RAcP binding and activation assays; MyD88/IRAK/NF-kB/MAPK pathway assays",
    },
    {
        "family": "IL36",
        "expansion_id": "M21B-LITEXP-IL36A-NFKB-CCL5-001",
        "ligand_node_id": "NODE05482",
        "ligand_receptor_edge_id": "M21B-E001758",
        "receptor_node_id": "NODE05401",
        "relay_node_id": "NODE07613",
        "tf_node_id": "NODE07984",
        "target_node_id": "NODE01732",
        "target_edge_id": "M21B-E008789",
        "pathway_name": "IL36A-IL36R-MyD88-IRAK-NFkB-CCL5",
        "primary_locator": "PMID:24829417; PMCID:PMC4048788; PMID:29180446; PMCID:PMC5767850",
        "evidence_ids": "M21B-E001758;M24B-E000096;M21B-E008789;M21B-EVID-001701;M24B-EVID-000133;M21B-EVID-008735;PMID:24829417;PMCID:PMC4048788;PMID:29180446;PMCID:PMC5767850",
        "citation_note": "Primary human keratinocyte study: IL-36alpha induced CCL5 mRNA. Primary receptor studies support IL-36R/IL-1RAcP activation, while the reviewed graph layer retains the MyD88/IRAK/NF-kB/MAPK continuation.",
        "cell_type_context": "post-confluent normal human keratinocytes; receptor-reconstituted mammalian cells",
        "assay_or_perturbation": "recombinant truncated IL-36alpha; qRT-PCR; IL-36R/IL-1RAcP binding and activation assays; MyD88/IRAK/NF-kB/MAPK pathway assays",
    },
    {
        "family": "IL36",
        "expansion_id": "M21B-LITEXP-IL36A-NFKB-CXCL8-001",
        "ligand_node_id": "NODE05482",
        "ligand_receptor_edge_id": "M21B-E001758",
        "receptor_node_id": "NODE05401",
        "relay_node_id": "NODE07613",
        "tf_node_id": "NODE07984",
        "target_node_id": "NODE02684",
        "target_edge_id": "M21B-E008790",
        "pathway_name": "IL36A-IL36R-MyD88-IRAK-NFkB-CXCL8",
        "primary_locator": "PMID:24829417; PMCID:PMC4048788; PMID:29180446; PMCID:PMC5767850",
        "evidence_ids": "M21B-E001758;M24B-E000096;M21B-E008790;M21B-EVID-001701;M24B-EVID-000133;M21B-EVID-008736;PMID:24829417;PMCID:PMC4048788;PMID:29180446;PMCID:PMC5767850",
        "citation_note": "Primary human keratinocyte study: IL-36alpha induced CXCL8/IL-8 mRNA and protein secretion. Primary receptor studies support IL-36R/IL-1RAcP activation, while the reviewed graph layer retains the MyD88/IRAK/NF-kB/MAPK continuation.",
        "cell_type_context": "post-confluent normal human keratinocytes; receptor-reconstituted mammalian cells",
        "assay_or_perturbation": "recombinant truncated IL-36alpha; qRT-PCR; conditioned-medium ELISA; IL-36R/IL-1RAcP binding and activation assays; MyD88/IRAK/NF-kB/MAPK pathway assays",
    },
    {
        "family": "IL36",
        "expansion_id": "M21B-LITEXP-IL36A-NFKB-CCL20-001",
        "ligand_node_id": "NODE05482",
        "ligand_receptor_edge_id": "M21B-E001758",
        "receptor_node_id": "NODE05401",
        "relay_node_id": "NODE07613",
        "tf_node_id": "NODE07984",
        "target_node_id": "NODE01682",
        "target_edge_id": "M21B-E008791",
        "pathway_name": "IL36A-IL36R-MyD88-IRAK-NFkB-CCL20",
        "primary_locator": "PMID:24829417; PMCID:PMC4048788; PMID:29180446; PMCID:PMC5767850",
        "evidence_ids": "M21B-E001758;M24B-E000096;M21B-E008791;M21B-EVID-001701;M24B-EVID-000133;M21B-EVID-008737;PMID:24829417;PMCID:PMC4048788;PMID:29180446;PMCID:PMC5767850",
        "citation_note": "Primary human keratinocyte study: IL-36alpha induced CCL20 mRNA and protein secretion. Primary receptor studies support IL-36R/IL-1RAcP activation, while the reviewed graph layer retains the MyD88/IRAK/NF-kB/MAPK continuation.",
        "cell_type_context": "post-confluent normal human keratinocytes; receptor-reconstituted mammalian cells",
        "assay_or_perturbation": "recombinant truncated IL-36alpha; qRT-PCR; conditioned-medium ELISA; IL-36R/IL-1RAcP binding and activation assays; MyD88/IRAK/NF-kB/MAPK pathway assays",
    },
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def make_rows(bundle: Path) -> list[dict[str, str]]:
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    edges = {row["edge_id"]: row for row in read_tsv(bundle / "mechanism_edges.tsv")}
    rows: list[dict[str, str]] = []
    for spec in SPECS:
        ligand = nodes[spec["ligand_node_id"]]
        receptor = nodes[spec["receptor_node_id"]]
        relay = nodes[spec["relay_node_id"]]
        tf = nodes[spec["tf_node_id"]]
        target = nodes[spec["target_node_id"]]
        lr = edges[spec["ligand_receptor_edge_id"]]
        if (lr["source_node_id"], lr["target_node_id"]) != (
            spec["ligand_node_id"],
            spec["receptor_node_id"],
        ):
            raise ValueError(f"{spec['expansion_id']}: ligand-receptor endpoints do not match")
        target_edge = edges[spec["target_edge_id"]]
        if target_edge["target_node_id"] != spec["target_node_id"]:
            raise ValueError(f"{spec['expansion_id']}: target edge endpoint does not match")
        rows.append(
            {
                "expansion_id": spec["expansion_id"],
                "source_queue_id": "",
                "route_status": "retained_evidence_route",
                "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                "missing_layers": "receptor_to_intracellular_edge|intracellular_to_tf_edge|tf_to_target_edge",
                "intracellular_status": "source_supported_composed",
                "ligand_node_id": spec["ligand_node_id"],
                "ligand_label": ligand["canonical_label"],
                "ligand_receptor_edge_id": spec["ligand_receptor_edge_id"],
                "receptor_node_id": spec["receptor_node_id"],
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
                "output_node_id": spec["target_node_id"],
                "output_label": f"{target['canonical_label']} expression",
                "output_form_id": "",
                "bridge_id": "",
                "pathway_name": spec["pathway_name"],
                "input_evidence_type": "primary_literature_route_expansion",
                "output_evidence_type": "primary_target_transcription_output",
                "evidence_ids": spec["evidence_ids"],
                "source_chain_id": f"manual_primary_{spec['pathway_name'].lower().replace('-', '_')}",
                "source_evidence_record_id": "",
                "route_linkage_status": "manual_primary_route;graph_linked_route_source;primary_layers_source_linked;receptor_to_intracellular_edge_not_asserted;intracellular_to_tf_edge_not_asserted;tf_to_target_edge_not_asserted;end_to_end_chain_not_asserted_by_single_source;evidence_route_only",
                "causal_status": "not_asserted",
                "traversal_status": "evidence_route_not_causal",
                "evidence_contract_version": "mechanism_evidence_v1",
                "evidence_polarity": "supports",
                "negative_evidence_status": "not_evaluated",
                "evidence_directness": "composite_primary_route",
                "output_class": "gene_expression_or_transcription",
                "primary_locator": spec["primary_locator"],
                "citation_note": spec["citation_note"],
                "evidence_summary": (
                    "Primary evidence supports IL-11 engagement of the IL-11Ralpha/gp130 complex, a STAT3-associated "
                    "intracellular response, and the listed gene-expression output in human fibroblast systems. The "
                    "route preserves these layers for mSCS plausibility analysis without asserting the unmeasured "
                    "receptor-to-relay, relay-to-TF, or TF-to-target handoffs."
                    if spec["family"] == "IL11"
                    else "Primary evidence supports IL-36alpha engagement of the IL-36R/IL-1RAcP complex, a MyD88/IRAK/NF-kB/MAPK pathway layer, and the listed keratinocyte gene-expression output. The route preserves these layers for mSCS plausibility analysis without asserting the unmeasured receptor-to-relay, relay-to-TF, or TF-to-target handoffs."
                ),
                "limitations": (
                    "The IL-11 fibroblast study uses primary human kidney, lung, and skin fibroblasts and reports a "
                    "source-composed STAT3-associated transcriptional response. It does not establish every represented "
                    "edge as one uninterrupted molecular chain, and no SCI transfer, causal traversal, or confidence "
                    "score is inferred."
                    if spec["family"] == "IL11"
                    else "The IL-36alpha receptor and keratinocyte output studies support complementary layers rather than one uninterrupted ligand-to-target experiment. The NF-kB layer is retained as pathway evidence, not as a newly asserted TF-to-target edge; no SCI transfer, causal traversal, or confidence score is inferred."
                ),
                "curation_status": "curated_primary_route",
                "species_context": "human",
                "cell_type_context": spec["cell_type_context"],
                "compartment_context": "extracellular ligand; plasma-membrane receptor complex; intracellular pathway response; nuclear gene-expression output",
                "injury_context": "No SCI transfer inferred; primary comparator contexts only",
                "context_scope": "composite primary evidence; source-specific fibroblast context retained",
                "assay_or_perturbation": spec["assay_or_perturbation"],
                "effect_polarity": "activating",
                "source_scope": "graph_linked_composite_primary_evidence",
                "route_evidence_id": "",
                "output_edge_id": spec["target_edge_id"],
            }
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = make_rows(args.bundle.resolve())
    args.output.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
