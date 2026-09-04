#!/usr/bin/env python3
"""Add reusable TF-target lanes found while reviewing holds 0253-0260."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch051.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch051_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch051-2026-09-04"

UPDATES = [
    {
        "holds": "M22B-HOLD-AUDIT-0255",
        "tf": "PU.1",
        "target": "Ccl22",
        "species": "mouse",
        "status": "reviewed_direct_target",
        "confidence": "high",
        "locator": "PMID:30718772; PMCID:PMC6361964; DOI:10.1038/s41598-018-37894-9",
        "context": "Mouse bone-marrow-derived dendritic-cell and macrophage experiments showed PU.1 binding to two Ccl22 promoter elements by EMSA and ChIP, with Spi1 knockdown reducing Ccl22 expression; immune-cell comparator, non-SCI.",
        "summary": "PU.1 directly bound the mouse Ccl22 promoter in dendritic cells and macrophages, and Spi1 knockdown reduced Ccl22 expression, supporting a direct PU.1-to-Ccl22 target lane.",
        "limitations": "The study concerns myeloid Ccl22 expression and LPS-associated regulation, not downstream signaling from Ccl22-Ackr2 and not an SCI receiver-cell experiment. It does not establish that ACKR2 activates PU.1.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0255",
        "tf": "PU.1",
        "target": "CCL22",
        "species": "human",
        "status": "reviewed_direct_target",
        "confidence": "high",
        "locator": "PMID:30718772; PMCID:PMC6361964; DOI:10.1038/s41598-018-37894-9",
        "context": "Human monocyte experiments in the same primary study identified PU.1 binding at corresponding CCL22 promoter elements; immune-cell comparator, non-SCI.",
        "summary": "The human CCL22 promoter contained corresponding PU.1-bound cis-elements in monocytes, supporting a human PU.1-to-CCL22 target lane alongside the mouse promoter and perturbation evidence.",
        "limitations": "The human result is promoter-binding evidence in monocytes and does not establish downstream signaling from Ccl22-Ackr2 or an SCI receiver-cell endpoint. It does not establish that ACKR2 activates PU.1.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0257",
        "tf": "Cdx1",
        "target": "Ccl25",
        "species": "mouse",
        "status": "reviewed_direct_target",
        "confidence": "high",
        "locator": "PMID:16517733; DOI:10.4049/jimmunol.176.6.3642",
        "context": "Mouse small-intestinal epithelial-cell experiments showed Cdx binding to a Ccl25 promoter motif and Cdx1-dependent enhancement of Ccl25 promoter activity and endogenous mRNA; intestinal-trafficking comparator, non-SCI.",
        "summary": "Cdx1 bound a Ccl25 promoter motif in primary mouse intestinal epithelial extracts and enhanced Ccl25 promoter activity and endogenous Ccl25 mRNA in epithelial cells, supporting a direct Cdx1-to-Ccl25 target lane.",
        "limitations": "The study concerns constitutive intestinal Ccl25 expression, not downstream signaling from Ccl25-Ackr4 and not an SCI receiver-cell experiment. The promoter system indicates a regulatory role but does not establish that ACKR4 activates Cdx1.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0257",
        "tf": "Cdx2",
        "target": "Ccl25",
        "species": "mouse",
        "status": "reviewed_direct_target",
        "confidence": "high",
        "locator": "PMID:16517733; DOI:10.4049/jimmunol.176.6.3642",
        "context": "Mouse small-intestinal epithelial-cell experiments showed Cdx binding to a Ccl25 promoter motif and Cdx2-dependent enhancement of Ccl25 promoter activity and endogenous mRNA; intestinal-trafficking comparator, non-SCI.",
        "summary": "Cdx2 bound a Ccl25 promoter motif in primary mouse intestinal epithelial extracts and enhanced Ccl25 promoter activity and endogenous Ccl25 mRNA in epithelial cells, supporting a direct Cdx2-to-Ccl25 target lane.",
        "limitations": "The study concerns constitutive intestinal Ccl25 expression, not downstream signaling from Ccl25-Ackr4 and not an SCI receiver-cell experiment. The promoter system indicates a regulatory role but does not establish that ACKR4 activates Cdx2.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0258;M22B-HOLD-AUDIT-0259",
        "tf": "STAT6",
        "target": "CCL26",
        "species": "human",
        "status": "reviewed_direct_target",
        "confidence": "high",
        "locator": "PMID:11544308; PMID:16084752",
        "context": "Human dermal fibroblast and intestinal epithelial-cell experiments showed IL-4/IL-13 induction of CCL26/eotaxin-3 through STAT6 promoter binding, promoter-site mutation, and dominant-negative STAT6 tests; allergic/inflammatory comparator, non-SCI.",
        "summary": "STAT6 bound functional sites in the human CCL26 promoter, and mutation or dominant-negative STAT6 disrupted IL-4/IL-13-induced CCL26 promoter activity and expression, supporting a direct STAT6-to-CCL26 target lane.",
        "limitations": "The evidence concerns cytokine-induced CCL26 expression in epithelial/fibroblast systems, not downstream signaling from Ccl26-Ackr2 or Ccl26-Ccr3 and not an SCI receiver-cell experiment. It does not establish that either submitted receptor branch activates STAT6.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0260",
        "tf": "RELA",
        "target": "CCL27",
        "species": "human",
        "status": "reviewed_regulatory_support",
        "confidence": "medium-high",
        "locator": "PMID:15577845; PMID:21993219; DOI:10.1016/j.jdermsci.2004.07.009; DOI:10.1016/j.cyto.2011.08.007",
        "context": "Human keratinocyte studies linked TNF/IL-1-induced CCL27 expression to NF-kB activity, p50/p65 antisense sensitivity, and NF-kB-bound promoter elements; skin-inflammation comparator, non-SCI.",
        "summary": "Human keratinocyte experiments linked CCL27 expression to NF-kB activity and p50/p65 requirement, while promoter studies identified NF-kB binding elements, supporting a RELA-associated CCL27 regulatory lane.",
        "limitations": "The studies support NF-kB pathway and promoter-element involvement but do not fully resolve RELA occupancy and causality at the endogenous CCL27 locus. They concern keratinocyte inflammation, not downstream signaling from Ccl27a-Ccr10 and not an SCI receiver-cell experiment.",
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
    edge_number, evidence_number = next_id(edges, "b_edge_id"), next_id(evidence, "b_evidence_id")
    audit = []
    for index, update in enumerate(UPDATES, start=253):
        pair = (update["species"].casefold(), update["tf"].casefold(), update["target"].casefold())
        if pair in existing:
            raise SystemExit(f"target pair already exists: {pair}")
        edge_id, evidence_id = f"M22B-E{edge_number:06d}", f"M22B-EVID-{evidence_number:06d}"
        edge_number += 1
        evidence_number += 1
        edges.append({
            "b_edge_id": edge_id,
            "source_entity": update["tf"],
            "relation_type": f"{update['tf']} regulates the {update['target']} target gene in primary-study evidence",
            "target_entity": update["target"],
            "pathway_name": "target_gene",
            "evidence_layer": "ligand_receptor_or_direct_molecular",
            "source_a_edge_id": f"M22B-TARGET-SEARCH-{index:04d}",
            "edge_status": update["status"],
            "context_scope": update["context"],
            "cell_type_context": update["context"],
            "compartment_context": "unspecified",
            "species_context": update["species"],
            "injury_context": "not_assessed",
            "confidence_tier": update["confidence"],
            "export_priority": "medium",
            "exportable": "true",
            "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing {update['holds']}; upstream handoffs remain separate and unupgraded.",
        })
        evidence.append({
            "b_evidence_id": evidence_id,
            "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-{index:04d}",
            "b_edge_ids": edge_id,
            "source_kind": update["status"],
            "source_locator": update["locator"],
            "support_kind": "primary_experiment",
            "species_support": update["species"],
            "source_scope": "direct_edge",
            "confidence_tier": update["confidence"],
            "citation_note": f"Primary-study target-gene evidence identified while reviewing hold rows {update['holds']}; standalone general TF-regulon claim.",
            "evidence_summary": update["summary"],
            "limitations": update["limitations"],
            "evidence_layer": "ligand_receptor_or_direct_molecular",
            "exportable": "true",
            "consolidation_note": f"{BATCH_ID}: primary-study target-gene evidence; upstream handoffs remain separate and unupgraded.",
        })
        audit.append({
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
    fields = ["batch_id", "hold_edges_reviewed", "tf", "target", "species", "b_edge_id", "b_evidence_id", "source_locator", "upstream_handoff_upgraded", "standalone_target_gene_edge", "decision_basis"]
    write_tsv(AUDIT_PATH, audit, fields)
    write_tsv(EDGE_PATH, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    summary = {
        "batch_id": BATCH_ID,
        "standalone_target_gene_edges_added": len(audit),
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
