#!/usr/bin/env python3
"""Add reusable direct TF-to-target lanes found while reviewing holds 0605-0612."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch071.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch071_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch071-2026-09-04"

UPDATES = [
    {
        "holds": "M22B-HOLD-AUDIT-0605",
        "tf": "GATA1",
        "target": "CCR3",
        "species": "human",
        "locator": "PMID:21041734; PMID:15807893; PMCID:PMC1080127; DOI:10.1186/1471-2172-6-7",
        "context": "Human eosinophil/erythroid promoter studies showed GATA1 occupancy at CCR3 exon-1 and intron-1 regulatory elements by ChIP, EMSA, and antibody interference; motif mutation and GATA1 loss reduced CCR3 reporter activity. Hematopoietic comparator.",
        "summary": "GATA1 promoter occupancy, motif mutation, and GATA1 loss-of-function support direct GATA1 activation of human CCR3.",
        "limitations": "The studies concern human eosinophil/erythroid chemokine-receptor regulation and do not establish CXCL10-CCR3 signaling to GATA1 or SCI activity.",
        "relation": "activates",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0608",
        "tf": "HIC1",
        "target": "ACKR3",
        "species": "human",
        "locator": "PMID:19525223",
        "context": "Human fibroblast and osteosarcoma-cell studies identified a conserved HIC1-responsive element in the ACKR3/CXCR7 promoter, demonstrated HIC1 ChIP occupancy, promoter-reporter dependence, and reduced ACKR3 after HIC1 expression. Tumor/stromal comparator.",
        "summary": "HIC1 promoter occupancy, promoter-reporter dependence, and expression repression support direct HIC1 regulation of human ACKR3/CXCR7.",
        "limitations": "The study concerns human tumor/stromal cells and a transcriptional repressor; it does not establish CXCL11-ACKR3 signaling to HIC1 or SCI activity.",
        "relation": "represses",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0609",
        "tf": "IRF3",
        "target": "CXCR3",
        "species": "human",
        "locator": "PMID:34527676",
        "context": "Human monocyte studies showed HIV-Tat-induced IRF3 binding at the CXCR3 promoter by ChIP and linked IRF3 activation to increased CXCR3 expression. Blood-brain-barrier inflammatory comparator.",
        "summary": "IRF3 promoter occupancy and stimulus-linked CXCR3 induction support direct IRF3 regulation of human CXCR3.",
        "limitations": "The study concerns HIV-Tat-treated human monocytes and does not establish CXCL11-CXCR3 signaling to IRF3 or SCI activity.",
        "relation": "activates",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0609",
        "tf": "Stat1",
        "target": "Cxcr3",
        "species": "mouse",
        "locator": "PMID:39560988; PMCID:PMC11721307; DOI:10.1172/jci.insight.180287",
        "context": "Mouse Th1-cell studies showed STAT1 association with Cxcr3 regulatory regions by ChIP and linked IFN-gamma/STAT1 signaling to Cxcr3 expression. T-cell inflammatory comparator.",
        "summary": "STAT1 Cxcr3-region occupancy and pathway-dependent expression data support direct Stat1 regulation of mouse Cxcr3.",
        "limitations": "The study concerns mouse Th1 differentiation and does not establish CXCL11-CXCR3 signaling to Stat1 or SCI activity.",
        "relation": "regulates",
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
            "source_a_edge_id": f"M22B-TARGET-SEARCH-0605-{index:02d}",
            "edge_status": "reviewed_direct_target", "context_scope": update["context"],
            "cell_type_context": update["context"], "compartment_context": "unspecified",
            "species_context": update["species"], "injury_context": "not_assessed",
            "confidence_tier": "high", "export_priority": "medium", "exportable": "true",
            "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing {update['holds']}; upstream handoff remains separate and unupgraded.",
        })
        evidence.append({
            "b_evidence_id": evidence_id, "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-0605-{index:02d}",
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
