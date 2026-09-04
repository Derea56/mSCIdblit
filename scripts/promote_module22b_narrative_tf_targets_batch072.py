#!/usr/bin/env python3
"""Add reusable direct TF-to-target lanes found while reviewing holds 0613-0620."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch072.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch072_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch072-2026-09-04"

UPDATES = [
    {
        "holds": "M22B-HOLD-AUDIT-0616",
        "tf": "CTCF",
        "target": "CXCR2",
        "species": "human",
        "locator": "PMID:41353667",
        "context": "Human acute-myeloid-leukemia studies identified CTCF binding at the CXCR2 locus by chromatin immunoprecipitation and linked CTCF perturbation to CXCR2 expression in an AML regulatory axis. Non-SCI leukemia comparator.",
        "summary": "CTCF occupancy at the CXCR2 locus plus perturbation-linked expression evidence support direct CTCF regulation of human CXCR2.",
        "limitations": "The study concerns human AML cells and does not establish CXCL3-CXCR2 signaling to CTCF or SCI activity.",
        "relation": "activates",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0616",
        "tf": "Stat3",
        "target": "Cxcr2",
        "species": "mouse",
        "locator": "PMID:23024284; PMCID:PMC3501897; DOI:10.1189/jlb.0312126",
        "context": "Mouse bone-marrow neutrophil studies showed G-CSF-activated STAT3 association with the proximal Cxcr2/Il8rb promoter region during myeloid mobilization. Myeloid inflammatory comparator.",
        "summary": "STAT3 association with the mouse Cxcr2/Il8rb promoter region during transcriptional induction supports direct Stat3 regulation of Cxcr2.",
        "limitations": "The study concerns mouse G-CSF-responsive neutrophils and does not establish CXCL3-CXCR2 signaling to Stat3 or SCI activity.",
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
            "source_a_edge_id": f"M22B-TARGET-SEARCH-0613-{index:02d}",
            "edge_status": "reviewed_direct_target", "context_scope": update["context"],
            "cell_type_context": update["context"], "compartment_context": "unspecified",
            "species_context": update["species"], "injury_context": "not_assessed",
            "confidence_tier": "high", "export_priority": "medium", "exportable": "true",
            "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing {update['holds']}; upstream handoff remains separate and unupgraded.",
        })
        evidence.append({
            "b_evidence_id": evidence_id, "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-0613-{index:02d}",
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
