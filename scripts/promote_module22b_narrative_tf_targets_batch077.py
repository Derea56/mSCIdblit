#!/usr/bin/env python3
"""Add primary-study RBPJ/Notch target lanes for holds 0653-0660."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch077.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch077_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch077-2026-09-04"

UPDATES = [
    {
        "tf": "Rbpj", "target": "Hey1", "locator": "PMID:23651858; PMCID:PMC3656323; DOI:10.1101/gad.211912.112",
        "summary": "Mouse myogenic-cell RBPJ/NICD ChIP-seq and expression profiling identified Hey1 as a Notch-pathway target with RBPJ-associated regulatory occupancy.",
        "limitations": "The evidence is for the RBPJ/NICD complex in myogenic cells and does not establish DLL1/3/4 activation of any submitted Notch paralog or SCI activity.",
    },
    {
        "tf": "Rbpj", "target": "Hes5", "locator": "PMID:30941015",
        "summary": "Mouse cortical and hippocampal tissue ChIP validation detected RBPJ and NICD at the canonical Hes5 promoter target region.",
        "limitations": "The source validates RBPJ/NICD occupancy in neural tissue but does not establish DLL1/3/4 activation of any submitted Notch paralog or SCI activity.",
    },
    {
        "tf": "Rbpj", "target": "Sox9", "locator": "PMID:22991339",
        "summary": "Mouse cartilage Notch gain-of-function and Rbpj-deficiency experiments linked Sox9 regulation to the Rbpj/NICD complex, with ChIP detecting recruitment at Sox9 upstream RBPJ sites.",
        "limitations": "The source uses a cartilage developmental model and does not establish DLL1/3/4 activation of any submitted Notch paralog or SCI activity.",
    },
    {
        "tf": "Rbpj", "target": "Sox2", "locator": "PMID:22232070; PMCID:PMC3734558; DOI:10.1002/stem.1030",
        "summary": "In vivo mouse cortical neural stem-cell ChIP-seq/transcriptome analysis identified Sox2 among the directly regulated RBPJ/N1ICD target genes.",
        "limitations": "The evidence is for activated Notch1/RBPJ in developing cortical neural stem cells and does not establish DLL1/3/4 activation of any submitted Notch paralog or SCI activity.",
    },
    {
        "tf": "Rbpj", "target": "Pax6", "locator": "PMID:22232070; PMCID:PMC3734558; DOI:10.1002/stem.1030",
        "summary": "In vivo mouse cortical neural stem-cell ChIP-seq/transcriptome analysis identified Pax6 among the directly regulated RBPJ/N1ICD target genes.",
        "limitations": "The evidence is for activated Notch1/RBPJ in developing cortical neural stem cells and does not establish DLL1/3/4 activation of any submitted Notch paralog or SCI activity.",
    },
    {
        "tf": "Rbpj", "target": "Tlx", "locator": "PMID:22232070; PMCID:PMC3734558; DOI:10.1002/stem.1030",
        "summary": "In vivo mouse cortical neural stem-cell ChIP-seq/transcriptome analysis identified Tlx among the directly regulated RBPJ/N1ICD target genes.",
        "limitations": "The evidence is for activated Notch1/RBPJ in developing cortical neural stem cells and does not establish DLL1/3/4 activation of any submitted Notch paralog or SCI activity.",
    },
    {
        "tf": "Rbpj", "target": "Id4", "locator": "PMID:22232070; PMCID:PMC3734558; DOI:10.1002/stem.1030",
        "summary": "In vivo mouse cortical neural stem-cell ChIP-seq/transcriptome analysis identified Id4 among the directly regulated RBPJ/N1ICD target genes.",
        "limitations": "The evidence is for activated Notch1/RBPJ in developing cortical neural stem cells and does not establish DLL1/3/4 activation of any submitted Notch paralog or SCI activity.",
    },
    {
        "tf": "Rbpj", "target": "Tcf4", "locator": "PMID:22232070; PMCID:PMC3734558; DOI:10.1002/stem.1030",
        "summary": "In vivo mouse cortical neural stem-cell ChIP-seq/transcriptome analysis identified Tcf4 among the directly regulated RBPJ/N1ICD target genes.",
        "limitations": "The evidence is for activated Notch1/RBPJ in developing cortical neural stem cells and does not establish DLL1/3/4 activation of any submitted Notch paralog or SCI activity.",
    },
    {
        "tf": "Rbpj", "target": "Gli2", "locator": "PMID:22232070; PMCID:PMC3734558; DOI:10.1002/stem.1030",
        "summary": "In vivo mouse cortical neural stem-cell ChIP-seq/transcriptome analysis identified Gli2 among the directly regulated RBPJ/N1ICD target genes.",
        "limitations": "The evidence is for activated Notch1/RBPJ in developing cortical neural stem cells and does not establish DLL1/3/4 activation of any submitted Notch paralog or SCI activity.",
    },
    {
        "tf": "Rbpj", "target": "Gli3", "locator": "PMID:22232070; PMCID:PMC3734558; DOI:10.1002/stem.1030",
        "summary": "In vivo mouse cortical neural stem-cell ChIP-seq/transcriptome analysis identified Gli3 among the directly regulated RBPJ/N1ICD target genes.",
        "limitations": "The evidence is for activated Notch1/RBPJ in developing cortical neural stem cells and does not establish DLL1/3/4 activation of any submitted Notch paralog or SCI activity.",
    },
    {
        "tf": "Rbpj", "target": "Yap1", "locator": "PMID:22232070; PMCID:PMC3734558; DOI:10.1002/stem.1030",
        "summary": "In vivo mouse cortical neural stem-cell ChIP-seq/transcriptome analysis identified Yap1 among the directly regulated RBPJ/N1ICD target genes.",
        "limitations": "The evidence is for activated Notch1/RBPJ in developing cortical neural stem cells and does not establish DLL1/3/4 activation of any submitted Notch paralog or SCI activity.",
    },
    {
        "tf": "Rbpj", "target": "Tead2", "locator": "PMID:22232070; PMCID:PMC3734558; DOI:10.1002/stem.1030",
        "summary": "In vivo mouse cortical neural stem-cell ChIP-seq/transcriptome analysis identified Tead2 among the directly regulated RBPJ/N1ICD target genes.",
        "limitations": "The evidence is for activated Notch1/RBPJ in developing cortical neural stem cells and does not establish DLL1/3/4 activation of any submitted Notch paralog or SCI activity.",
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
        pair = ("mouse", update["tf"].casefold(), update["target"].casefold())
        if pair in existing:
            raise SystemExit(f"target pair already exists: {pair}")
        edge_id, evidence_id = f"M22B-E{edge_num:06d}", f"M22B-EVID-{evidence_num:06d}"
        context = f"{update['summary']} Non-SCI developmental, neural, or myogenic comparator."
        edges.append({
            "b_edge_id": edge_id, "source_entity": update["tf"], "relation_type": f"{update['tf']} regulates the {update['target']} target gene in primary-study evidence",
            "target_entity": update["target"], "pathway_name": "target_gene", "evidence_layer": "ligand_receptor_or_direct_molecular",
            "source_a_edge_id": f"M22B-TARGET-SEARCH-0653-{index:02d}", "edge_status": "reviewed_direct_target",
            "context_scope": context, "cell_type_context": context, "compartment_context": "unspecified", "species_context": "mouse", "injury_context": "not_assessed",
            "confidence_tier": "high", "export_priority": "medium", "exportable": "true", "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing M22B-HOLD-AUDIT-0653 through M22B-HOLD-AUDIT-0660; upstream handoff remains separate and unupgraded.",
        })
        evidence.append({
            "b_evidence_id": evidence_id, "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-0653-{index:02d}", "b_edge_ids": edge_id, "source_kind": "reviewed_direct_target",
            "source_locator": update["locator"], "support_kind": "primary_experiment", "species_support": "mouse", "source_scope": "direct_edge",
            "confidence_tier": "high", "citation_note": "Primary-study target-gene evidence identified while reviewing Module 22B Notch ligand-receptor hold rows 0653-0660; standalone general TF-regulon claim.", "evidence_summary": update["summary"], "limitations": update["limitations"],
            "evidence_layer": "ligand_receptor_or_direct_molecular", "exportable": "true", "consolidation_note": f"{BATCH_ID}: primary-study target-gene evidence; upstream handoff remains separate and unupgraded.",
        })
        audit_rows.append({"batch_id": BATCH_ID, "hold_edges_reviewed": "M22B-HOLD-AUDIT-0653;M22B-HOLD-AUDIT-0654;M22B-HOLD-AUDIT-0655;M22B-HOLD-AUDIT-0656;M22B-HOLD-AUDIT-0657;M22B-HOLD-AUDIT-0658;M22B-HOLD-AUDIT-0659;M22B-HOLD-AUDIT-0660", "tf": update["tf"], "target": update["target"], "species": "mouse", "b_edge_id": edge_id, "b_evidence_id": evidence_id, "source_locator": update["locator"], "upstream_handoff_upgraded": "false", "standalone_target_gene_edge": "true", "decision_basis": update["summary"]})
        existing.add(pair); edge_num += 1; evidence_num += 1
    fields = ["batch_id", "hold_edges_reviewed", "tf", "target", "species", "b_edge_id", "b_evidence_id", "source_locator", "upstream_handoff_upgraded", "standalone_target_gene_edge", "decision_basis"]
    write_tsv(AUDIT_PATH, audit_rows, fields); write_tsv(EDGE_PATH, edges, EDGE_FIELDS); write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    summary = {"batch_id": BATCH_ID, "standalone_target_gene_edges_added": len(UPDATES), "upstream_handoff_edges_upgraded": 0, "high_edges_after": sum(r["confidence_tier"] == "high" for r in edges), "medium_high_edges_after": sum(r["confidence_tier"] == "medium-high" for r in edges), "exportable_edges_after": sum(r["exportable"] == "true" for r in edges), "target_gene_edges_after": sum(r["pathway_name"] == "target_gene" for r in edges), "upstream_activation_inferred": False, "audit": str(AUDIT_PATH)}
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True); SUMMARY_PATH.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8"); print(json.dumps(summary, indent=2)); return 0


if __name__ == "__main__":
    raise SystemExit(main())
