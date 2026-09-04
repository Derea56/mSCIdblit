#!/usr/bin/env python3
"""Add reusable direct TF-to-target lanes found while reviewing holds 0597-0604."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch070.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch070_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch070-2026-09-04"

UPDATES = [
    {
        "holds": "M22B-HOLD-AUDIT-0601",
        "tf": "SPI1",
        "target": "FPR1",
        "species": "human",
        "locator": "PMID:22174875",
        "context": "Human myeloid-cell studies identified a PU.1/SPI1 site in the FPR1 promoter by ChIP and EMSA; site mutagenesis reduced promoter-reporter expression. Myeloid differentiation comparator.",
        "summary": "SPI1 promoter occupancy, in-vitro binding, and binding-site mutagenesis support direct SPI1 activation of human FPR1.",
        "limitations": "The study concerns human myeloid differentiation and does not establish CTSG-FPR1 signaling to SPI1 or SCI activity.",
        "relation": "activates",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0602",
        "tf": "SPI1",
        "target": "CXCR1",
        "species": "human",
        "locator": "PMID:9867862; DOI:10.1074/jbc.274.1.438",
        "context": "Human myeloid-cell studies mapped a PU.1/SPI1-bound CXCR1 promoter element and showed PU.1 transactivation of the CXCR1 promoter in reporter assays. Neutrophil-lineage comparator.",
        "summary": "SPI1 binding to the CXCR1 promoter and promoter transactivation support direct SPI1 activation of human CXCR1.",
        "limitations": "The study concerns human myeloid/neutrophil-lineage promoter regulation and does not establish CTSG-PARD3 or CTSG-CXCR1 signaling to SPI1 or SCI activity.",
        "relation": "activates",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0603",
        "tf": "SNAI1",
        "target": "PARD3",
        "species": "human",
        "locator": "PMID:33931921",
        "context": "Human bladder-cancer studies showed SNAI1/Snail binding at an E-box in the PARD3 promoter-proximal region and linked Snail to reduced PARD3 expression. Tumor epithelial comparator.",
        "summary": "Snail promoter binding and repression of PARD3 support a direct SNAI1-to-PARD3 regulatory lane.",
        "limitations": "The study concerns human bladder-cancer epithelial cells and does not establish CTSG-PARD3 signaling to SNAI1 or SCI activity.",
        "relation": "represses",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0604",
        "tf": "GATA1",
        "target": "ACKR1",
        "species": "human",
        "locator": "PMID:7663520; PMID:8651934; DOI:10.1038/ng0695-224; DOI:10.1006/bbrc.1996.0833",
        "context": "Human erythroid promoter studies identified GATA1 binding at the ACKR1/DARC promoter; mutation or deletion of the proximal GATA motif abolished erythroid promoter activity. Erythroid blood-group comparator.",
        "summary": "GATA1 promoter binding and motif-disruption effects support direct GATA1 activation of human ACKR1 in erythroid cells.",
        "limitations": "The studies concern erythroid ACKR1/DARC expression and do not establish CTSG-ACKR1 signaling to GATA1 or SCI activity.",
        "relation": "activates",
    },
]


def next_id(rows: list[dict[str, str]], field: str) -> int:
    return max([int(match.group(1)) for row in rows if (match := re.search(r"(\d+)$", row[field]))] or [0]) + 1


def main() -> int:
    edges, evidence = read_tsv(EDGE_PATH), read_tsv(EVIDENCE_PATH)
    existing = {
        (r.get("species_context", "").casefold(), r.get("source_entity", "").casefold(), r.get("target_entity", "").casefold())
        for r in edges if r.get("pathway_name") == "target_gene"
    }
    edge_num, evidence_num, audit_rows = next_id(edges, "b_edge_id"), next_id(evidence, "b_evidence_id"), []
    for index, update in enumerate(UPDATES, start=1):
        pair = (update["species"].casefold(), update["tf"].casefold(), update["target"].casefold())
        if pair in existing:
            raise SystemExit(f"target pair already exists: {pair}")
        edge_id, evidence_id = f"M22B-E{edge_num:06d}", f"M22B-EVID-{evidence_num:06d}"
        edges.append({
            "b_edge_id": edge_id, "source_entity": update["tf"],
            "relation_type": f"{update['tf']} {update['relation']} the {update['target']} target gene in primary-study evidence",
            "target_entity": update["target"], "pathway_name": "target_gene",
            "evidence_layer": "ligand_receptor_or_direct_molecular",
            "source_a_edge_id": f"M22B-TARGET-SEARCH-0597-{index:02d}",
            "edge_status": "reviewed_direct_target", "context_scope": update["context"],
            "cell_type_context": update["context"], "compartment_context": "unspecified",
            "species_context": update["species"], "injury_context": "not_assessed",
            "confidence_tier": "high", "export_priority": "medium", "exportable": "true",
            "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing {update['holds']}; upstream handoff remains separate and unupgraded.",
        })
        evidence.append({
            "b_evidence_id": evidence_id, "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-0597-{index:02d}",
            "b_edge_ids": edge_id, "source_kind": "reviewed_direct_target", "source_locator": update["locator"],
            "support_kind": "primary_experiment", "species_support": update["species"], "source_scope": "direct_edge",
            "confidence_tier": "high", "citation_note": f"Primary-study target-gene evidence identified while reviewing hold row {update['holds']}; standalone general TF-regulon claim.",
            "evidence_summary": update["summary"], "limitations": update["limitations"],
            "evidence_layer": "ligand_receptor_or_direct_molecular", "exportable": "true",
            "consolidation_note": f"{BATCH_ID}: primary-study target-gene evidence; upstream handoff remains separate and unupgraded.",
        })
        audit_rows.append({
            "batch_id": BATCH_ID, "hold_edges_reviewed": update["holds"], "tf": update["tf"], "target": update["target"],
            "species": update["species"], "b_edge_id": edge_id, "b_evidence_id": evidence_id,
            "source_locator": update["locator"], "upstream_handoff_upgraded": "false",
            "standalone_target_gene_edge": "true", "decision_basis": update["summary"],
        })
        existing.add(pair); edge_num += 1; evidence_num += 1
    fields = ["batch_id", "hold_edges_reviewed", "tf", "target", "species", "b_edge_id", "b_evidence_id", "source_locator", "upstream_handoff_upgraded", "standalone_target_gene_edge", "decision_basis"]
    write_tsv(AUDIT_PATH, audit_rows, fields)
    write_tsv(EDGE_PATH, edges, EDGE_FIELDS); write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    summary = {
        "batch_id": BATCH_ID, "standalone_target_gene_edges_added": len(UPDATES), "upstream_handoff_edges_upgraded": 0,
        "high_edges_after": sum(r["confidence_tier"] == "high" for r in edges),
        "medium_high_edges_after": sum(r["confidence_tier"] == "medium-high" for r in edges),
        "exportable_edges_after": sum(r["exportable"] == "true" for r in edges),
        "target_gene_edges_after": sum(r["pathway_name"] == "target_gene" for r in edges),
        "upstream_activation_inferred": False, "audit": str(AUDIT_PATH),
    }
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True); SUMMARY_PATH.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2)); return 0


if __name__ == "__main__":
    raise SystemExit(main())
