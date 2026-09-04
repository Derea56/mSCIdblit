#!/usr/bin/env python3
"""Add direct, reusable TF-to-chemokine lanes found in holds 0277-0284."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch054.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch054_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch054-2026-09-04"

UPDATES = [
    {
        "holds": "M22B-HOLD-AUDIT-0277;M22B-HOLD-AUDIT-0278",
        "tf": "RXRA",
        "target": "Ccl6",
        "species": "mouse",
        "locator": "PMID:20498053; PMCID:PMC2890831; DOI:10.1073/pnas.0913545107",
        "context": "Primary mouse peritoneal macrophage and myeloid-RXRA knockout experiments showed RXRA-dependent Ccl6 expression; RXR ligand induction, Ccl6 promoter mutation, RXRA ChIP, and sequence-specific binding supported direct regulation; sepsis/inflammation comparator, non-SCI.",
        "summary": "RXRA ligand response, myeloid knockout, promoter mutation, ChIP, and sequence-specific binding support a direct RXRA-to-Ccl6 target lane in mouse macrophages.",
        "limitations": "The study concerns RXRA transcriptional signaling in mouse macrophages and sepsis/inflammation, not Ccl6-Ccr2 or Ccl6-Ccr3 receptor signaling and not SCI. The standalone RXRA-to-Ccl6 lane is not transferred to either receptor handoff.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0277;M22B-HOLD-AUDIT-0278",
        "tf": "MYCL",
        "target": "Ccl6",
        "species": "mouse",
        "locator": "PMID:12782599; Cancer Research 63(11):2923-2932",
        "context": "Murine IL-3-dependent 32D myeloid-cell experiments identified Ccl6 as a direct positive L-Myc target; L-Myc activated a Ccl6 promoter reporter, bound the promoter by ChIP, and increased endogenous Ccl6 expression; tumor/myeloid comparator, non-SCI.",
        "summary": "L-Myc/MYCL promoter ChIP, reporter activation, and endogenous-expression evidence support a direct MYCL-to-Ccl6 target lane in mouse.",
        "limitations": "The source distinguishes activating L-Myc from repressive full-length c-Myc and uses an engineered myeloid-cell/tumor comparator context. It does not establish Ccl6-Ccr2 or Ccl6-Ccr3 signaling to MYCL and is not an SCI receiver-cell experiment.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0279;M22B-HOLD-AUDIT-0280;M22B-HOLD-AUDIT-0281;M22B-HOLD-AUDIT-0282",
        "tf": "STAT1",
        "target": "CCL7",
        "species": "human",
        "locator": "PMID:33257678; PMCID:PMC7704643; DOI:10.1038/s41467-020-19973-6",
        "context": "Human A549 lung epithelial-cell experiments showed type-I/II interferon induction of CCL7 and direct pSTAT1 binding at the human CCL7 promoter by ChIP; lung-tumor comparator, non-SCI.",
        "summary": "Interferon-induced CCL7 expression and pSTAT1 promoter ChIP support a direct STAT1-to-CCL7 target lane in human lung epithelial cells.",
        "limitations": "The study uses interferon/JAK-STAT stimulation in lung epithelial and tumor models and does not establish signaling from CCL7-ACKR1, CCL7-CCR1L1, CCL7-CCR2, or CCL7-CCR3 to STAT1. It is not an SCI receiver-cell experiment.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0279;M22B-HOLD-AUDIT-0280;M22B-HOLD-AUDIT-0281;M22B-HOLD-AUDIT-0282",
        "tf": "STAT1",
        "target": "Ccl7",
        "species": "mouse",
        "locator": "PMID:33257678; PMCID:PMC7704643; DOI:10.1038/s41467-020-19973-6",
        "context": "Primary mouse lung epithelial-cell experiments showed type-I/II interferon induction of Ccl7 and direct pSTAT1 binding at the mouse Ccl7 promoter by ChIP; lung-tumor comparator, non-SCI.",
        "summary": "Interferon-induced Ccl7 expression and pSTAT1 promoter ChIP support a direct STAT1-to-Ccl7 target lane in mouse lung epithelial cells.",
        "limitations": "The study uses interferon/JAK-STAT stimulation in lung epithelial and tumor models and does not establish signaling from Ccl7-Ackr1, Ccl7-Ccr1l1, Ccl7-Ccr2, or Ccl7-Ccr3 to STAT1. It is not an SCI receiver-cell experiment.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0283;M22B-HOLD-AUDIT-0284",
        "tf": "IRF1",
        "target": "Ccl8",
        "species": "mouse",
        "locator": "PMID:41779805",
        "context": "Mouse CT26 and infection-model experiments identified IRF1 binding at the Ccl8 promoter by ChIP; IRF1 perturbation reduced Ccl8-associated chemotactic output, with infection-linked Ccl8 induction; enteric-infection comparator, non-SCI.",
        "summary": "IRF1 promoter ChIP and IRF1 perturbation evidence support a direct IRF1-to-Ccl8 target lane in mouse infection-associated tumor-cell experiments.",
        "limitations": "The reported mechanism includes the chromatin regulator JMJD1A and uses an enteric-infection/tumor-cell comparator system; it does not establish Ccl8-Ackr1 or Ccl8-Ackr4 signaling to IRF1 and is not an SCI receiver-cell experiment.",
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
            "source_a_edge_id": f"M22B-TARGET-SEARCH-0277-{index:02d}",
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
            "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-0277-{index:02d}",
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
            "consolidation_note": f"{BATCH_ID}: primary-study target-gene evidence; upstream handoffs remain separate and unupgraded.",
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
