#!/usr/bin/env python3
"""Add direct, reusable TF-to-target lanes found in holds 0381-0388."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch064.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch064_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch064-2026-09-04"

UPDATES = [
    {
        "holds": "M22B-HOLD-AUDIT-0381",
        "tf": "EBF2",
        "target": "Cntn1",
        "species": "mouse",
        "locator": "PMID:25820347; DOI:10.1002/dneu.22293",
        "context": "Mouse embryonic and early postnatal cerebellar studies showed reduced Cntn1 expression and promoter activity in Ebf2-null mice; EBF2 bound the Cntn1 5-prime flanking region by ChIP and EBF-factor expression constructs transactivated a Cntn1 promoter reporter. Non-SCI developmental-neural comparator.",
        "summary": "EBF2 ChIP at the Cntn1 5-prime flanking region, Ebf2-loss effects, and promoter-reporter transactivation support direct mouse EBF2 activation of Cntn1.",
        "limitations": "The study concerns cerebellar development and does not establish CNTN1 signaling to NOTCH1 or SCI activity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0387",
        "tf": "TFAP2E",
        "target": "ITGA10",
        "species": "human",
        "locator": "PMID:16684505; DOI:10.1016/j.bbrc.2006.04.123",
        "context": "Human chondrocyte promoter studies localized an ITGA10 regulatory region, identified AP-2 sites, confirmed AP-2-dependent reporter activation, and identified AP-2epsilon as the major AP-2 protein binding the sites by EMSA. Non-SCI cartilage comparator.",
        "summary": "AP-2epsilon binding and AP-2-dependent ITGA10 promoter-reporter activation support direct TFAP2E activation of human ITGA10 in chondrocytes.",
        "limitations": "The study concerns human chondrocyte ITGA10 regulation and does not establish COL1A1-integrin signaling to TFAP2E or SCI activity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0387",
        "tf": "ETS1",
        "target": "ITGA10",
        "species": "human",
        "locator": "PMID:16684505; DOI:10.1016/j.bbrc.2006.04.123",
        "context": "Human chondrocyte promoter studies identified Ets-1 as a positive regulator of ITGA10 expression in the promoter-analysis system. Non-SCI cartilage comparator.",
        "summary": "The primary human chondrocyte promoter study identifies Ets-1 as a positive regulator of ITGA10 transcription.",
        "limitations": "The study does not establish COL1A1-integrin signaling to ETS1 or SCI activity; the Ets-1 result is less mechanistically resolved than the AP-2epsilon binding evidence.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0386",
        "tf": "GATA1",
        "target": "GP6",
        "species": "human",
        "locator": "PMID:12359731; DOI:10.1074/jbc.M206127200",
        "context": "Human megakaryocytic promoter studies identified a functional GP6 promoter with essential GATA, Ets, and Sp1 sites and showed GATA-1 binding and activation. Non-SCI megakaryocyte comparator.",
        "summary": "GATA-site mutagenesis, GATA-1 binding, and promoter activation support direct GATA1 activation of human GP6.",
        "limitations": "The study concerns megakaryocytic GP6 expression and does not establish COL1A1-GP6 signaling to GATA1 or SCI activity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0386",
        "tf": "FLI1",
        "target": "GP6",
        "species": "human",
        "locator": "PMID:12359731; DOI:10.1074/jbc.M206127200",
        "context": "Human megakaryocytic promoter studies identified an essential Ets site in the GP6 promoter and showed Fli-1 binding and promoter activation; Fli-1 overexpression induced endogenous GP6 in a compatible cell line. Non-SCI megakaryocyte comparator.",
        "summary": "Ets-site mutagenesis, FLI1 binding, promoter activation, and FLI1 overexpression support direct FLI1 activation of human GP6.",
        "limitations": "The study concerns megakaryocytic GP6 expression and does not establish COL1A1-GP6 signaling to FLI1 or SCI activity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0386",
        "tf": "SP1",
        "target": "GP6",
        "species": "human",
        "locator": "PMID:12359731; DOI:10.1074/jbc.M206127200",
        "context": "Human megakaryocytic promoter studies identified an essential Sp1 site in the GP6 promoter and showed Sp1 binding and activation. Non-SCI megakaryocyte comparator.",
        "summary": "Sp1-site mutagenesis, Sp1 binding, and promoter activation support direct SP1 activation of human GP6.",
        "limitations": "The study concerns megakaryocytic GP6 expression and does not establish COL1A1-GP6 signaling to SP1 or SCI activity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0386",
        "tf": "TAL1",
        "target": "Gp6",
        "species": "mouse",
        "locator": "PMCID:PMC3292579; DOI:10.1371/journal.pone.0032981",
        "context": "Mouse ES-cell-derived and primary megakaryocyte studies showed reduced Gp6 after Scl/Tal1 excision, SCL occupancy at the Gp6 promoter, and promoter activity for the SCL complex with FLI1. Non-SCI megakaryocyte comparator.",
        "summary": "Mouse Scl/Tal1 loss, Gp6 expression reduction, promoter occupancy, and SCL-complex transactivation support direct TAL1-associated activation of mouse Gp6.",
        "limitations": "The mouse study tests a megakaryocytic SCL complex and does not establish COL1A1-Gp6 signaling to TAL1 or SCI activity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0386",
        "tf": "FLI1",
        "target": "Gp6",
        "species": "mouse",
        "locator": "PMCID:PMC3292579; DOI:10.1371/journal.pone.0032981",
        "context": "Mouse ES-cell-derived and primary megakaryocyte studies detected FLI1 at the Gp6 promoter and showed FLI1-containing SCL-complex transactivation with loss of activity after Ets-motif mutation. Non-SCI megakaryocyte comparator.",
        "summary": "Mouse FLI1 promoter occupancy, Ets-motif dependence, and FLI1-containing complex transactivation support direct FLI1-associated activation of Gp6.",
        "limitations": "The mouse study concerns megakaryocytic Gp6 regulation and does not establish COL1A1-Gp6 signaling to FLI1 or SCI activity.",
    },
]


def next_id(rows: list[dict[str, str]], field: str) -> int:
    return max([int(match.group(1)) for row in rows if (match := re.search(r"(\d+)$", row[field]))] or [0]) + 1


def main() -> int:
    edges, evidence = read_tsv(EDGE_PATH), read_tsv(EVIDENCE_PATH)
    existing = {
        (r.get("species_context", "").casefold(), r.get("source_entity", "").casefold(), r.get("target_entity", "").casefold())
        for r in edges
        if r.get("pathway_name") == "target_gene"
    }
    edge_num = next_id(edges, "b_edge_id")
    evidence_num = next_id(evidence, "b_evidence_id")
    audit_rows = []
    for index, update in enumerate(UPDATES, start=1):
        pair = (update["species"].casefold(), update["tf"].casefold(), update["target"].casefold())
        if pair in existing:
            raise SystemExit(f"target pair already exists: {pair}")
        edge_id = f"M22B-E{edge_num:06d}"
        evidence_id = f"M22B-EVID-{evidence_num:06d}"
        edges.append({
            "b_edge_id": edge_id,
            "source_entity": update["tf"],
            "relation_type": f"{update['tf']} regulates the {update['target']} target gene in primary-study evidence",
            "target_entity": update["target"],
            "pathway_name": "target_gene",
            "evidence_layer": "ligand_receptor_or_direct_molecular",
            "source_a_edge_id": f"M22B-TARGET-SEARCH-0381-{index:02d}",
            "edge_status": "reviewed_direct_target",
            "context_scope": update["context"],
            "cell_type_context": update["context"],
            "compartment_context": "unspecified",
            "species_context": update["species"],
            "injury_context": "not_assessed",
            "confidence_tier": "high",
            "export_priority": "medium",
            "exportable": "true",
            "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing {update['holds']}; upstream handoffs remain separate and unupgraded.",
        })
        evidence.append({
            "b_evidence_id": evidence_id,
            "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-0381-{index:02d}",
            "b_edge_ids": edge_id,
            "source_kind": "reviewed_direct_target",
            "source_locator": update["locator"],
            "support_kind": "primary_experiment",
            "species_support": update["species"],
            "source_scope": "direct_edge",
            "confidence_tier": "high",
            "citation_note": f"Primary-study target-gene evidence identified while reviewing hold rows {update['holds']}; standalone general TF-regulon claim.",
            "evidence_summary": update["summary"],
            "limitations": update["limitations"],
            "evidence_layer": "ligand_receptor_or_direct_molecular",
            "exportable": "true",
            "consolidation_note": f"{BATCH_ID}: primary-study target-gene evidence; upstream handoff remains separate and unupgraded.",
        })
        audit_rows.append({
            "batch_id": BATCH_ID,
            "hold_edges_reviewed": update["holds"],
            "tf": update["tf"],
            "target": update["target"],
            "species": update["species"],
            "b_edge_id": edge_id,
            "b_evidence_id": evidence_id,
            "source_locator": update["locator"],
            "upstream_handoff_upgraded": "false",
            "standalone_target_gene_edge": "true",
            "decision_basis": update["summary"],
        })
        existing.add(pair)
        edge_num += 1
        evidence_num += 1
    audit_fields = ["batch_id", "hold_edges_reviewed", "tf", "target", "species", "b_edge_id", "b_evidence_id", "source_locator", "upstream_handoff_upgraded", "standalone_target_gene_edge", "decision_basis"]
    write_tsv(AUDIT_PATH, audit_rows, audit_fields)
    write_tsv(EDGE_PATH, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    summary = {
        "batch_id": BATCH_ID,
        "standalone_target_gene_edges_added": len(UPDATES),
        "upstream_handoff_edges_upgraded": 0,
        "high_edges_after": sum(r["confidence_tier"] == "high" for r in edges),
        "medium_high_edges_after": sum(r["confidence_tier"] == "medium-high" for r in edges),
        "exportable_edges_after": sum(r["exportable"] == "true" for r in edges),
        "target_gene_edges_after": sum(r["pathway_name"] == "target_gene" for r in edges),
        "upstream_activation_inferred": False,
        "audit": str(AUDIT_PATH),
    }
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
