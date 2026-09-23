#!/usr/bin/env python3
"""Build evidence-only routes that link curated ligand outputs to TF targets."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


FAMILIES = (
    {
        "name": "IL4",
        "lr_edge_id": "M21B-E001754",
        "relays": (("JAK1", "M21B-E001782"), ("JAK3", "M21B-E001783")),
        "tf": "STAT6",
        "targets": (
            ("M21B-E008943", "GATA3", "M21B-E008263"),
            ("M21B-E008950", "CCL17", "M21B-E008389"),
            ("M21B-E008952", "ARG1", "M21B-E008363"),
            ("M21B-E008953", "MRC1", "M21B-E008629"),
            ("M21B-E008955", "RETNLA", "M21B-E008365"),
            ("M21B-E008957", "CHIL3", "M21B-E008366"),
        ),
    },
    {
        "name": "IL10",
        "lr_edge_id": "M21B-E001753",
        "relays": (("JAK1", "M21B-E001721"), ("TYK2", "M21B-E001722")),
        "tf": "STAT3",
        "targets": (
            ("M21B-E008648", "LCN2", "M21B-E008348"),
            ("M21B-E008962", "BCL3", "M21B-E008623"),
            ("M21B-E008963", "SOCS3", "M21B-E008279"),
        ),
    },
    {
        "name": "IL7",
        "lr_edge_id": "M21B-E000324",
        "relays": (("JAK1", "M21B-E011504"), ("JAK3", "M21B-E011505")),
        "tf": "STAT5",
        "targets": (
            ("M21B-E008939", "BCL2", "M21B-E008257"),
            ("M21B-E008985", "BCL2L1", "M21B-E008253"),
        ),
    },
    {
        "name": "IL9",
        "lr_edge_id": "M21B-E000325",
        "relays": (("JAK1", "M21B-E011511"), ("JAK3", "M21B-E011512")),
        "tf": "STAT5",
        "targets": (
            ("M21B-E008996", "BCL3", "M21B-E008623", "STAT3"),
            ("M21B-E008997", "CISH", "M21B-E008251", "STAT5"),
            ("M21B-E008998", "SOCS2", "M21B-E008258", "STAT5"),
            ("M21B-E008999", "SOCS3", "M21B-E008279", "STAT3"),
            ("M21B-E009004", "PIM1", "M21B-E008307", "STAT3"),
            ("M21B-E009004", "PIM1", "M21B-E008252", "STAT5"),
        ),
    },
    {
        "name": "IL21",
        "lr_edge_id": "M21B-E001756",
        "relays": (("JAK1/JAK3", "M21B-E000555"),),
        "tf": "STAT3",
        "targets": (
            ("M21B-E008876", "BCL6", "M21B-E008246", "STAT5"),
            ("M21B-E008877", "IL2RA", "M21B-E008250", "STAT5"),
            ("M21B-E009006", "IRF4", "M21B-E008341", "STAT3"),
            ("M21B-E009007", "IL21", "M21B-E008223", "STAT3"),
            ("M21B-E009008", "IL17A", "M21B-E008226", "STAT3"),
            ("M21B-E009008", "IL17A", "M21B-E008925", "STAT5"),
            ("M21B-E009009", "IL17F", "M21B-E008227", "STAT3"),
            ("M21B-E009010", "RORC", "M21B-E008338", "STAT3"),
            ("M21B-E009011", "IL22", "M21B-E008229", "STAT3"),
            ("M21B-E009012", "AHR", "M21B-E008342", "STAT3"),
            ("M21B-E009013", "IL23R", "M21B-E008336", "STAT3"),
        ),
    },
    {
        "name": "IFN-gamma",
        "lr_edge_id": "M21B-E001763",
        "relays": (("JAK1", "M21B-E000013"), ("JAK2", "M21B-E000014")),
        "tf": "STAT1",
        "targets": (
            ("M21B-E008706", "ICAM1", "M21B-E008362"),
            ("M21B-E008748", "CXCL9", "M21B-E008361"),
            ("M21B-E008965", "IRF1", "M21B-E008259"),
            ("M21B-E008966", "GBP2", "M21B-E008203"),
        ),
    },
    {
        "name": "IL-6",
        "lr_edge_id": "M21B-E001760",
        "relays": (("JAK1", "M21B-E001716"), ("JAK2", "M21B-E001729"), ("TYK2", "M21B-E001730")),
        "tf": "STAT3",
        "targets": (
            ("M21B-E008654", "CEBPD", "M21B-E008416"),
            ("M21B-E008655", "CRP", "M21B-E008327"),
            ("M21B-E008971", "SOCS3", "M21B-E008279"),
        ),
    },
    {
        "name": "IL15",
        "lr_edge_id": "M21B-E001755",
        "relays": (("JAK1", "M21B-E011507"), ("JAK3", "M21B-E011508")),
        "tf": "STAT5",
        "targets": (
            ("M21B-E008979", "MCL1", "M21B-E008277", "STAT3"),
            ("M21B-E008980", "BCL2", "M21B-E008257", "STAT5"),
            ("M21B-E008983", "VEGFA", "M21B-E008300", "STAT3"),
        ),
    },
    {
        "name": "IL17A",
        "lr_edge_id": "M21B-E000450",
        "relays": (("ACT1/CIKS", "M21B-E001771"),),
        "tf": "STAT3",
        "targets": (
            ("M21B-E008669", "IL1B", "M21B-E008228"),
            ("M21B-E008671", "CXCL2", "M21B-E008401"),
        ),
    },
    {
        "name": "IL31",
        "lr_edge_id": "M21B-E000490",
        "relays": (("JAK1", "M21B-E000552"),),
        "tf": "STAT3",
        "targets": (
            ("M21B-E008870", "POMC", "M21B-E008321"),
            ("M21B-E008872", "CCL2", "M21B-E008441"),
        ),
    },
    {
        "name": "IL2",
        "lr_edge_id": "M21B-E000236",
        "relays": (("JAK1/JAK3", "M21B-E000237"),),
        "tf": "STAT5",
        "targets": (
            ("M21B-E008941", "IL9", "M21B-E008484", "STAT5"),
            ("M21B-E008942", "IRF4", "M21B-E008341", "STAT3"),
            ("M21B-E008987", "CISH", "M21B-E008251", "STAT5"),
            ("M21B-E008988", "MYC", "M21B-E008480", "STAT5"),
            ("M21B-E008988", "MYC", "M21B-E008280", "STAT3"),
            ("M21B-E008989", "BCL2", "M21B-E008257", "STAT5"),
            ("M21B-E008989", "BCL2", "M21B-E008285", "STAT3"),
            ("M21B-E008990", "BCL2L1", "M21B-E008253", "STAT5"),
        ),
    },
    {
        "name": "GM-CSF/CSF2",
        "lr_edge_id": "M21B-E000177",
        "relays": (("JAK2", "M21B-E001776"),),
        "tf": "STAT5",
        "targets": (
            ("M21B-E008945", "CISH", "M21B-E008251", "STAT5"),
            ("M21B-E008946", "IRF4", "M21B-E008341", "STAT3"),
            ("M21B-E008947", "CCL17", "M21B-E008389", "STAT6"),
            ("M21B-E008994", "BCL2L1", "M21B-E008253", "STAT5"),
        ),
    },
    {
        "name": "IL3",
        "lr_edge_id": "M21B-E000326",
        "relays": (("JAK2", "M21B-E001778"),),
        "tf": "STAT5",
        "targets": (
            ("M21B-E008938", "BCL2L1", "M21B-E008253"),
            ("M21B-E008992", "CISH", "M21B-E008251"),
        ),
    },
    {
        "name": "IL5",
        "lr_edge_id": "M21B-E000327",
        "relays": (("JAK2", "M21B-E001780"),),
        "tf": "STAT5",
        "targets": (
            ("M21B-E008936", "CISH", "M21B-E008251"),
            ("M21B-E008991", "BCL2", "M21B-E008257"),
        ),
    },
    {
        "name": "OSM",
        "lr_edge_id": "M21B-E008848",
        "relays": (("JAK1", "M21B-E000003"), ("JAK2", "M21B-E000004"), ("TYK2", "M21B-E000005")),
        "tf": "STAT3",
        "targets": (
            ("M21B-E008702", "SOCS3", "M21B-E008279"),
            ("M21B-E008711", "PTGS2", "M21B-E008328"),
        ),
    },
    {
        "name": "IL12B/IL23A",
        "lr_edge_id": "M21B-E001768",
        "relays": (("JAK2", "M21B-E001769"), ("TYK2", "M21B-E001770")),
        "tf": "STAT3",
        "targets": (
            ("M21B-E009015", "CSF2", "M21B-E008442", "STAT5"),
            ("M21B-E009016", "IL23R", "M21B-E008336", "STAT3"),
        ),
    },
    {
        "name": "LIF",
        "lr_edge_id": "M21B-E001732",
        "relays": (("JAK1", "M21B-E000001"),),
        "tf": "STAT3",
        "targets": (
            ("M21B-E008967", "SOCS3", "M21B-E008279"),
            ("M21B-E008968", "POMC", "M21B-E008321"),
        ),
    },
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def unique_join(values: list[str]) -> str:
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
    sources = read_tsv(bundle / "mechanism_edge_sources.tsv")
    source_by_edge: dict[str, list[dict[str, str]]] = {}
    for source in sources:
        source_by_edge.setdefault(source["edge_id"], []).append(source)

    rows: list[dict[str, str]] = []
    index = 1
    for family in FAMILIES:
        lr_edge = edges[family["lr_edge_id"]]
        receptor = nodes[lr_edge["target_node_id"]]
        for relay_label, relay_edge_id in family["relays"]:
            relay_edge = edges[relay_edge_id]
            relay = nodes[relay_edge["target_node_id"]]
            for target_spec in family["targets"]:
                output_edge_id, target_label, tf_target_edge_id = target_spec[:3]
                target_tf_label = target_spec[3] if len(target_spec) == 4 else family["tf"]
                tf = next(row for row in nodes.values() if row["canonical_label"] == target_tf_label)
                output_edge = edges[output_edge_id]
                tf_target_edge = edges[tf_target_edge_id]
                target = nodes[output_edge["target_node_id"]]
                locators = unique_join(
                    [
                        *(source.get("source_locator", "") for source in source_by_edge.get(lr_edge["edge_id"], [])),
                        *(source.get("source_locator", "") for source in source_by_edge.get(relay_edge_id, [])),
                        *(source.get("source_locator", "") for source in source_by_edge.get(output_edge_id, [])),
                        *(source.get("source_locator", "") for source in source_by_edge.get(tf_target_edge_id, [])),
                    ]
                )
                evidence_ids = unique_join(
                    [
                        lr_edge.get("evidence_ids", ""),
                        relay_edge.get("evidence_ids", ""),
                        output_edge.get("evidence_ids", ""),
                        tf_target_edge.get("evidence_ids", ""),
                        *(source.get("evidence_id", "") for source in source_by_edge.get(lr_edge["edge_id"], [])),
                        *(source.get("evidence_id", "") for source in source_by_edge.get(relay_edge_id, [])),
                        *(source.get("evidence_id", "") for source in source_by_edge.get(output_edge_id, [])),
                        *(source.get("evidence_id", "") for source in source_by_edge.get(tf_target_edge_id, [])),
                        locators,
                    ]
                )
                rows.append(
                    {
                        "expansion_id": f"M21B-LITEXP-{family['name']}-{relay_label}-{target_tf_label}-{target_label}-{index:03d}",
                        "source_queue_id": "",
                        "route_status": "retained_evidence_route",
                        "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
                        "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                        "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                        "missing_layers": "intracellular_to_tf_edge",
                        "intracellular_status": "source_supported",
                        "ligand_node_id": lr_edge["source_node_id"],
                        "ligand_label": lr_edge["source_label"],
                        "ligand_receptor_edge_id": lr_edge["edge_id"],
                        "receptor_node_id": lr_edge["target_node_id"],
                        "receptor_label": receptor["canonical_label"],
                        "receptor_intracellular_edge_id": relay_edge_id,
                        "intracellular_continuation_node_id": relay["node_id"],
                        "intracellular_continuation_label": relay["canonical_label"],
                        "intracellular_tf_edge_id": "",
                        "transcription_factor_node_id": tf["node_id"],
                        "transcription_factor_label": target_tf_label,
                        "tf_target_edge_id": tf_target_edge_id,
                        "target_gene_node_id": target["node_id"],
                        "target_gene_label": target["canonical_label"],
                        "target_output_form_id": "",
                        "output_node_id": target["node_id"],
                        "output_label": f"{target_label} expression",
                        "output_form_id": "",
                        "output_edge_id": output_edge_id,
                        "bridge_id": "",
                        "pathway_name": f"{family['name']}-{receptor['canonical_label']}-{relay_label}-{family['tf']}-{target_label}",
                        "input_evidence_type": "primary_literature_route_expansion",
                        "output_evidence_type": "primary_target_gene_expression",
                        "evidence_ids": evidence_ids,
                        "source_chain_id": f"M21B-LITEXP-{family['name']}-{relay_label}-{target_tf_label}-{target_label}-{index:03d}",
                        "source_evidence_record_id": "",
                        "route_linkage_status": f"manual_primary_{family['name'].lower()}_output_linked_route;graph_linked_route_source;primary_layer_linked;receptor_to_intracellular_edge_asserted_as_graph_edge;intracellular_to_tf_edge_not_asserted;tf_to_target_edge_asserted_as_graph_edge;output_edge_asserted_as_graph_edge;evidence_route_only",
                        "causal_status": "not_asserted",
                        "traversal_status": "evidence_route_not_causal",
                        "evidence_contract_version": "mechanism_evidence_v1",
                        "evidence_polarity": "supports",
                        "negative_evidence_status": "not_evaluated",
                        "evidence_directness": "composite_primary_route",
                        "output_class": "target_gene_expression",
                        "primary_locator": locators,
                        "citation_note": f"Primary {family['name']} receptor, {relay_label}-associated, {target_tf_label}-target, and target-gene evidence is retained as a linked evidence route; the intracellular-to-TF handoff remains unasserted.",
                        "evidence_summary": f"Primary evidence supports {family['name']} engagement of the {receptor['canonical_label']} receptor complex, {relay_label}-associated signaling, {target_tf_label} regulation, and {target_label} expression. The direct ligand-output and TF-target graph edges are preserved as linked components without asserting a new causal chain.",
                        "limitations": "The receptor, kinase, TF, and target-gene studies use complementary model systems and may not arise from one experiment or cell type. Preserve source-specific context and the distinction between evidence-route composition and asserted graph connectivity; no SCI transfer, causal traversal, or database confidence score is inferred.",
                        "curation_status": "curated_primary_route",
                        "species_context": "human; mouse comparator systems",
                        "cell_type_context": "Primary and transformed immune-cell, macrophage, or reporter systems represented by the component evidence records.",
                        "compartment_context": "extracellular cytokine; plasma membrane receptor complex; cytoplasm; nucleus; target-gene regulatory locus",
                        "injury_context": "no SCI transfer inferred; primary model context only",
                        "context_scope": "composite primary evidence; route layers retain source-specific models",
                        "assay_or_perturbation": f"{family['name']} stimulation; receptor or kinase perturbation; {family['tf']} activity or target binding; target-gene RNA, promoter, or protein measurements",
                        "effect_polarity": "activating",
                        "source_scope": "composite_primary_evidence",
                    }
                )
                index += 1
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
