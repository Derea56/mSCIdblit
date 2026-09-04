#!/usr/bin/env python3
"""Add reusable direct TF-to-target lanes found while reviewing holds 0589-0596."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch069.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch069_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch069-2026-09-04"

UPDATES = [
    {
        "holds": "M22B-HOLD-AUDIT-0591",
        "tf": "NRF1",
        "target": "CD47",
        "species": "human",
        "locator": "PMID:14747477; PMID:39742254; PMCID:PMC11685207; DOI:10.3389/fimmu.2024.1495032",
        "context": "Human promoter and melanoma-cell studies identified alpha-Pal/NRF-1 binding at the CD47 promoter; the recent melanoma study used ChIP, promoter deletion/luciferase assays, and NRF1 knockdown to link NRF1 occupancy to CD47 activation. Non-SCI melanoma comparator.",
        "summary": "NRF1 promoter occupancy plus promoter-activation and NRF1 loss-of-function evidence support direct NRF1 regulation and activation of human CD47.",
        "limitations": "The studies concern human erythroid/promoter or melanoma-cell regulation and do not establish COMP-CD47 signaling to NRF1 or SCI activity.",
        "relation": "activates",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0592",
        "tf": "Sp3",
        "target": "Itga3",
        "species": "mouse",
        "locator": "PMID:16211576; DOI:10.1002/jcb.20663",
        "context": "Studies of the mouse Itga3 promoter in tumor cell lines identified Sp3 binding at a GC-rich promoter motif by EMSA with antibody specificity and showed promoter-element dependence in luciferase assays. Non-SCI carcinoma comparator.",
        "summary": "Sp3 binding to the mouse Itga3 promoter and promoter-element reporter dependence support a direct Sp3-to-Itga3 target-gene lane.",
        "limitations": "The study concerns mouse Itga3 promoter regulation in carcinoma cell lines and does not establish COMP-ITGA3_ITGB1 signaling to Sp3 or SCI activity.",
        "relation": "regulates",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0596",
        "tf": "SPI1",
        "target": "CSF1R",
        "species": "human",
        "locator": "PMID:8264604; PMCID:PMC358386; DOI:10.1128/mcb.14.1.373-381.1994",
        "context": "Human monocytic studies showed PU.1/SPI1 binding to a specific CSF1R promoter site, reduced promoter activity after site mutation, and promoter transactivation by PU.1. Myeloid-lineage comparator.",
        "summary": "PU.1/SPI1 promoter binding, site-mutant loss of activity, and transactivation support direct SPI1 activation of human CSF1R.",
        "limitations": "The study concerns human monocyte/macrophage differentiation and does not establish CSF1-CSF1R handoff-specific signaling to SPI1 or traumatic SCI activity.",
        "relation": "activates",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0596",
        "tf": "Spi1",
        "target": "Csf1r",
        "species": "mouse",
        "locator": "PMCID:PMC3561417; PMID:17116688",
        "context": "Mouse macrophage-lineage studies of the Csf1r promoter and FIRE enhancer identify PU.1/Spi1 occupancy and show that PU.1-dependent regulatory elements are required for macrophage-restricted Csf1r transcription. Myeloid-lineage comparator.",
        "summary": "Mouse Csf1r regulatory-element occupancy and PU.1-dependent promoter/enhancer activity support direct Spi1 activation of Csf1r.",
        "limitations": "The study concerns mouse macrophage differentiation and does not establish CSF1-CSF1R handoff-specific signaling to Spi1 or traumatic SCI activity.",
        "relation": "activates",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0596",
        "tf": "Ets2",
        "target": "Csf1r",
        "species": "mouse",
        "locator": "PMCID:PMC3561417",
        "context": "Mouse Csf1r promoter studies identified Ets-family regulation and Ets2 transactivation of the macrophage receptor promoter in myeloid cells. Myeloid-lineage comparator.",
        "summary": "The mouse Csf1r promoter study reports Ets2 transactivation of the promoter, supporting a direct Ets2-to-Csf1r target-gene lane.",
        "limitations": "The study concerns mouse macrophage-lineage promoter regulation and does not establish CSF1-CSF1R handoff-specific signaling to Ets2 or traumatic SCI activity.",
        "relation": "activates",
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
            "relation_type": f"{update['tf']} {update['relation']} the {update['target']} target gene in primary-study evidence",
            "target_entity": update["target"],
            "pathway_name": "target_gene",
            "evidence_layer": "ligand_receptor_or_direct_molecular",
            "source_a_edge_id": f"M22B-TARGET-SEARCH-0589-{index:02d}",
            "edge_status": "reviewed_direct_target",
            "context_scope": update["context"],
            "cell_type_context": update["context"],
            "compartment_context": "unspecified",
            "species_context": update["species"],
            "injury_context": "not_assessed",
            "confidence_tier": "high",
            "export_priority": "medium",
            "exportable": "true",
            "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing {update['holds']}; upstream handoff remains separate and unupgraded.",
        })
        evidence.append({
            "b_evidence_id": evidence_id,
            "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-0589-{index:02d}",
            "b_edge_ids": edge_id,
            "source_kind": "reviewed_direct_target",
            "source_locator": update["locator"],
            "support_kind": "primary_experiment",
            "species_support": update["species"],
            "source_scope": "direct_edge",
            "confidence_tier": "high",
            "citation_note": f"Primary-study target-gene evidence identified while reviewing hold row {update['holds']}; standalone general TF-regulon claim.",
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
