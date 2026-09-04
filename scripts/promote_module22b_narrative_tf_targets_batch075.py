#!/usr/bin/env python3
"""Add primary-study dopamine/monoamine TF-target lanes for holds 0637-0644."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch075.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch075_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch075-2026-09-04"

UPDATES = [
    {
        "hold": "M22B-HOLD-AUDIT-0638;M22B-HOLD-AUDIT-0644", "tf": "Rara", "target": "Drd2", "species": "rat",
        "locator": "PMID:9405615; PMCID:PMC24972; DOI:10.1073/pnas.94.26.14349",
        "context": "Rat Drd2 promoter studies identified a functional retinoic-acid response element; RAR-alpha/RX receptor DNA binding and receptor-reporter assays supported retinoid-dependent promoter activation, with reduced Drd2 expression in receptor-null mice. Non-SCI central-neural comparator.",
        "summary": "RAR-alpha DNA binding and mutation-sensitive Drd2 promoter activation establish rat Drd2 as a retinoid-receptor target.",
        "limitations": "The promoter is rat and the in-vivo expression result is receptor-null mouse evidence; this does not establish the DOPA-DDC-SLC18A1/2 upstream handoffs or SCI activity.",
        "relation": "activates",
    },
    {
        "hold": "M22B-HOLD-AUDIT-0638;M22B-HOLD-AUDIT-0644", "tf": "Klf11", "target": "Drd2", "species": "rat",
        "locator": "PMID:22375010; DOI:10.1074/jbc.M111.306472",
        "context": "Rat Drd2 promoter studies showed KLF11 binding to a defined Sp-KLF site by EMSA, promoter activation, ChIP occupancy, and increased endogenous Drd2 expression in neuronal PC12 cells. Non-SCI neuronal comparator.",
        "summary": "KLF11 binding, promoter-reporter activation, ChIP occupancy, and endogenous expression changes establish rat Drd2 as a Klf11 target.",
        "limitations": "The evidence uses rat promoter/PC12 and mouse DRG corroboration and does not establish the DOPA-DDC-SLC18A1/2 upstream handoffs or SCI activity.",
        "relation": "regulates",
    },
    {
        "hold": "M22B-HOLD-AUDIT-0638;M22B-HOLD-AUDIT-0644", "tf": "KLF11", "target": "DRD2", "species": "human",
        "locator": "PMID:22375010; DOI:10.1074/jbc.M111.306472",
        "context": "The KLF11 study reported KLF11 occupancy at the human DRD2 promoter by ChIP in pancreatic epithelial cells, alongside promoter and neuronal-cell functional assays. Non-SCI human neuronal/regulatory comparator.",
        "summary": "KLF11 ChIP occupancy at the human DRD2 promoter, supported by the promoter-binding and functional assays in the same study, establishes human DRD2 as a KLF11-regulated target.",
        "limitations": "The human occupancy experiment is in a pancreatic epithelial model and the strongest promoter mechanistic assays use rat Drd2; this does not establish the DOPA-DDC-SLC18A1/2 upstream handoffs or SCI activity.",
        "relation": "regulates",
    },
    {
        "hold": "M22B-HOLD-AUDIT-0640", "tf": "Klf11", "target": "Drd4", "species": "rat",
        "locator": "PMID:22375010; DOI:10.1074/jbc.M111.306472",
        "context": "KLF11 ChIP in neuronal PC12 cells identified Drd4 among the neurotransmitter-receptor promoters occupied by KLF11. Non-SCI neuronal comparator.",
        "summary": "KLF11 occupancy at the rat Drd4 promoter identifies Drd4 as a Klf11-regulated neuronal target in the primary study.",
        "limitations": "The source provides promoter occupancy but less gene-specific activation dissection for Drd4 than for Drd2; this does not establish the DOPA-DDC-SLC18A1/2 upstream handoffs or SCI activity.",
        "relation": "regulates",
    },
    {
        "hold": "M22B-HOLD-AUDIT-0637;M22B-HOLD-AUDIT-0643", "tf": "FEV", "target": "DDC", "species": "human",
        "locator": "PMID:10575032; PMCID:PMC6782418; DOI:10.1523/JNEUROSCI.19-23-10348.1999",
        "context": "The Pet-1/FEV study identified conserved Pet-1/FEV sites near the human aromatic L-amino acid decarboxylase (DDC) promoter; the sites bound the ETS domain and supported transcriptional activation in enhancer assays. Non-SCI serotonergic-neuron comparator.",
        "summary": "FEV/Pet-1 binding to a conserved DDC regulatory site and enhancer activation establish human DDC as a FEV target.",
        "limitations": "The functional enhancer assay uses a heterologous reporter and serotonergic rather than SCI neurons; it does not establish the DOPA-DDC-SLC18A1 upstream handoffs or SCI activity.",
        "relation": "activates",
    },
    {
        "hold": "M22B-HOLD-AUDIT-0637;M22B-HOLD-AUDIT-0643", "tf": "Fev", "target": "Ddc", "species": "mouse",
        "locator": "PMID:10575032; PMCID:PMC6782418; DOI:10.1523/JNEUROSCI.19-23-10348.1999",
        "context": "The Pet-1/FEV study identified conserved Pet-1/FEV sites near the mouse Ddc promoter; purified ETS-domain binding and enhancer assays supported transcriptional activation. Non-SCI serotonergic-neuron comparator.",
        "summary": "Fev/Pet-1 binding to a conserved Ddc regulatory site and enhancer activation establish mouse Ddc as a Fev target.",
        "limitations": "The functional enhancer assay uses a heterologous reporter and serotonergic rather than SCI neurons; it does not establish the DOPA-DDC-SLC18A1 upstream handoffs or SCI activity.",
        "relation": "activates",
    },
    {
        "hold": "M22B-HOLD-AUDIT-0642", "tf": "Lmx1b", "target": "Slc18a2", "species": "mouse",
        "locator": "PMID:21246047",
        "context": "Conditional deletion of Lmx1b in adult mouse raphe serotonergic neurons markedly reduced Vmat2/Slc18a2 expression, supporting Lmx1b-dependent maintenance of the vesicular monoamine transporter program. Non-SCI CNS neuronal comparator.",
        "summary": "Adult raphe-specific Lmx1b loss causing reduced Slc18a2/Vmat2 expression supports functional Lmx1b regulation of mouse Slc18a2.",
        "limitations": "The study demonstrates functional dependence but not direct Lmx1b occupancy at the Slc18a2 promoter; it does not establish the DOPA-SLC18A2 upstream handoff or SCI activity.",
        "relation": "regulates",
    },
]


def next_id(rows: list[dict[str, str]], field: str) -> int:
    return max([int(match.group(1)) for row in rows if (match := re.search(r"(\d+)$", row[field]))] or [0]) + 1


def main() -> int:
    edges, evidence = read_tsv(EDGE_PATH), read_tsv(EVIDENCE_PATH)
    existing = {(r.get("species_context", "").casefold(), r.get("source_entity", "").casefold(), r.get("target_entity", "").casefold()) for r in edges if r.get("pathway_name") == "target_gene"}
    edge_num, evidence_num = next_id(edges, "b_edge_id"), next_id(evidence, "b_evidence_id")
    audit_rows = []
    for index, update in enumerate(UPDATES, start=1):
        pair = (update["species"].casefold(), update["tf"].casefold(), update["target"].casefold())
        if pair in existing:
            raise SystemExit(f"target pair already exists: {pair}")
        edge_id, evidence_id = f"M22B-E{edge_num:06d}", f"M22B-EVID-{evidence_num:06d}"
        edges.append({
            "b_edge_id": edge_id, "source_entity": update["tf"], "relation_type": f"{update['tf']} {update['relation']} the {update['target']} target gene in primary-study evidence",
            "target_entity": update["target"], "pathway_name": "target_gene", "evidence_layer": "ligand_receptor_or_direct_molecular",
            "source_a_edge_id": f"M22B-TARGET-SEARCH-0637-{index:02d}", "edge_status": "reviewed_direct_target" if update["tf"].casefold() != "lmx1b" else "reviewed_regulatory_support",
            "context_scope": update["context"], "cell_type_context": update["context"], "compartment_context": "unspecified", "species_context": update["species"], "injury_context": "not_assessed",
            "confidence_tier": "high", "export_priority": "medium", "exportable": "true", "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing {update['hold']}; upstream handoff remains separate and unupgraded.",
        })
        evidence.append({
            "b_evidence_id": evidence_id, "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-0637-{index:02d}", "b_edge_ids": edge_id, "source_kind": "reviewed_direct_target" if update["tf"].casefold() != "lmx1b" else "reviewed_functional_target",
            "source_locator": update["locator"], "support_kind": "primary_experiment", "species_support": update["species"], "source_scope": "direct_edge" if update["tf"].casefold() != "lmx1b" else "functional_edge",
            "confidence_tier": "high", "citation_note": f"Primary-study target-gene evidence identified while reviewing hold row {update['hold']}; standalone general TF-regulon claim.", "evidence_summary": update["summary"], "limitations": update["limitations"],
            "evidence_layer": "ligand_receptor_or_direct_molecular", "exportable": "true", "consolidation_note": f"{BATCH_ID}: primary-study target-gene evidence; upstream handoff remains separate and unupgraded.",
        })
        audit_rows.append({"batch_id": BATCH_ID, "hold_edges_reviewed": update["hold"], "tf": update["tf"], "target": update["target"], "species": update["species"], "b_edge_id": edge_id, "b_evidence_id": evidence_id, "source_locator": update["locator"], "upstream_handoff_upgraded": "false", "standalone_target_gene_edge": "true", "decision_basis": update["summary"]})
        existing.add(pair); edge_num += 1; evidence_num += 1
    fields = ["batch_id", "hold_edges_reviewed", "tf", "target", "species", "b_edge_id", "b_evidence_id", "source_locator", "upstream_handoff_upgraded", "standalone_target_gene_edge", "decision_basis"]
    write_tsv(AUDIT_PATH, audit_rows, fields); write_tsv(EDGE_PATH, edges, EDGE_FIELDS); write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    summary = {"batch_id": BATCH_ID, "standalone_target_gene_edges_added": len(UPDATES), "upstream_handoff_edges_upgraded": 0, "high_edges_after": sum(r["confidence_tier"] == "high" for r in edges), "medium_high_edges_after": sum(r["confidence_tier"] == "medium-high" for r in edges), "exportable_edges_after": sum(r["exportable"] == "true" for r in edges), "target_gene_edges_after": sum(r["pathway_name"] == "target_gene" for r in edges), "upstream_activation_inferred": False, "audit": str(AUDIT_PATH)}
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True); SUMMARY_PATH.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8"); print(json.dumps(summary, indent=2)); return 0


if __name__ == "__main__":
    raise SystemExit(main())
