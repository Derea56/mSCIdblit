#!/usr/bin/env python3
"""Add reusable direct TF-to-target lanes found while reviewing holds 0621-0628."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch073.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch073_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch073-2026-09-04"

UPDATES = [
    {
        "holds": "M22B-HOLD-AUDIT-0621",
        "tf": "ESR1",
        "target": "SULT2A1",
        "species": "human",
        "locator": "PMID:24492894",
        "context": "Human hepatocyte and HepG2-ER studies showed estrogen-receptor-alpha/ESR1 recruitment to the SULT2A1 promoter by ChIP, promoter cis-element dependence, and estrogen/antiestrogen-sensitive induction. Steroid-metabolism comparator.",
        "summary": "ESR1 promoter recruitment, cis-element mutation, and antiestrogen-sensitive induction support direct ESR1 activation of human SULT2A1.",
        "limitations": "The study concerns human hepatocyte and HepG2 steroid-metabolism regulation and does not establish DHEA-STS signaling to ESR1 or SCI activity.",
        "relation": "activates",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0621",
        "tf": "CEBPA",
        "target": "SULT2A1",
        "species": "human",
        "locator": "PMID:16357103; DOI:10.1210/me.2005-0428",
        "context": "Human SULT2A1 promoter studies identified a C/EBP-alpha/CEBPA-bound composite regulatory element by EMSA, supershift, footprinting, and recruitment assays; C/EBP-alpha deficiency abolished induction and cotransfected C/EBP-alpha restored it. Steroid-metabolism comparator.",
        "summary": "CEBPA binding and rescue of SULT2A1 promoter induction support direct CEBPA regulation of human SULT2A1.",
        "limitations": "The study concerns human vitamin-D-responsive steroid metabolism and does not establish DHEA-STS signaling to CEBPA or SCI activity.",
        "relation": "regulates",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0622",
        "tf": "NR1I2",
        "target": "SULT1E1",
        "species": "human",
        "locator": "PMID:21764778",
        "context": "Human primary-hepatocyte and Huh7 studies showed ligand-activated PXR/NR1I2 repression of SULT1E1 through a mapped PXR-responsive enhancer, with siRNA, ChIP, and chromatin-conformation evidence. Hepatic xenobiotic-metabolism comparator.",
        "summary": "PXR/NR1I2 enhancer engagement and perturbation-linked repression support direct NR1I2 regulation of human SULT1E1.",
        "limitations": "The study concerns human hepatic PXR repression and does not establish DHEA-STS signaling to NR1I2 or SCI activity.",
        "relation": "represses",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0623",
        "tf": "HNF4A",
        "target": "Ppara",
        "species": "mouse",
        "locator": "PMID:19933841",
        "context": "Mouse liver studies used promoter occupancy and expression analyses to identify HNF4A as a direct activator of the Ppara gene in vivo within a hepatic metabolic transcription-factor network. Metabolic comparator.",
        "summary": "HNF4A promoter occupancy and in-vivo expression evidence support direct HNF4A activation of mouse Ppara.",
        "limitations": "The study concerns mouse hepatic metabolic regulation and does not establish DHEA-STS signaling to Ppara or HNF4A or SCI activity.",
        "relation": "activates",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0622",
        "tf": "PPARA",
        "target": "NR1I2",
        "species": "human",
        "locator": "PMID:16243957; DOI:10.1124/dmd.105.006064",
        "context": "Human PXR/NR1I2 promoter studies identified a functional PPAR-alpha/PPARA binding site in the proximal promoter and showed PPAR-alpha-dependent promoter activity. Hepatic xenobiotic-metabolism comparator.",
        "summary": "PPARA binding-site and promoter-reporter evidence support direct PPARA regulation of human NR1I2/PXR.",
        "limitations": "The study concerns human PXR promoter regulation and does not establish DHEA-STS signaling to PPARA or SCI activity.",
        "relation": "regulates",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0625",
        "tf": "Rora",
        "target": "Sult1e1",
        "species": "mouse",
        "locator": "PMID:30025153",
        "context": "Mouse hepatic studies showed ROR-alpha/Rora binding to the Sult1e1 promoter and conversion from a basal repressor to an activator after CAR-dependent phosphorylation, with promoter-reporter support. Hepatic xenobiotic-metabolism comparator.",
        "summary": "Rora promoter binding and phosphorylation-dependent promoter activation support direct Rora regulation of mouse Sult1e1.",
        "limitations": "The study concerns mouse liver and phenobarbital/CAR signaling and does not establish DHEAS-SULT1E1 signaling to Rora or SCI activity.",
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
            "source_a_edge_id": f"M22B-TARGET-SEARCH-0621-{index:02d}",
            "edge_status": "reviewed_direct_target", "context_scope": update["context"],
            "cell_type_context": update["context"], "compartment_context": "unspecified",
            "species_context": update["species"], "injury_context": "not_assessed",
            "confidence_tier": "high", "export_priority": "medium", "exportable": "true",
            "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing {update['holds']}; upstream handoff remains separate and unupgraded.",
        })
        evidence.append({
            "b_evidence_id": evidence_id, "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-0621-{index:02d}",
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
