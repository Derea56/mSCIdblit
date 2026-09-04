#!/usr/bin/env python3
"""Add human EphB4 promoter-regulation lanes found while reviewing holds 0677-0684."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch080.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch080_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch080-2026-09-04"

UPDATES = [
    {
        "hold": "M22B-HOLD-AUDIT-0684", "tf": "HOXA9", "target": "EPHB4", "species": "human", "relation": "regulates", "status": "reviewed_direct_target", "scope": "direct_edge",
        "locator": "PMID:28292467; DOI:10.1016/j.placenta.2017.01.127",
        "context": "Human trophoblast experiments used HOXA9 gain/loss of function, ChIP, and EPHB4-promoter luciferase assays to support direct transcriptional regulation of EPHB4. Non-SCI placental comparator.",
        "summary": "HOXA9 ChIP at the EPHB4 promoter together with gain/loss-of-function and promoter-reporter evidence supports a direct human HOXA9-to-EPHB4 target relationship.",
        "limitations": "The study examines trophoblasts and preeclampsia rather than EFNB1-EPHB4 signaling or SCI; it does not upgrade the submitted ligand-receptor handoff.",
    },
    {
        "hold": "M22B-HOLD-AUDIT-0684", "tf": "SP1", "target": "EPHB4", "species": "human", "relation": "regulates", "status": "reviewed_regulatory_support", "scope": "functional_edge",
        "locator": "PMID:31810288; PMCID:PMC6947382; DOI:10.3390/genes10120997",
        "context": "Human EphB4 promoter cloning and deletion/reporter experiments mapped multiple proximal Sp1 cis-acting elements and showed that promoter constructs containing the Sp1 region supported serum-responsive EPHB4 transcription. Non-SCI vascular/cancer comparator.",
        "summary": "Human EPHB4 promoter mapping and deletion/reporter assays support proximal Sp1 elements as regulatory support for EPHB4 transcription.",
        "limitations": "The study maps promoter elements and reporter behavior rather than establishing endogenous Sp1 occupancy in the EFNB1-EPHB4 branch; it does not establish SCI activity or upgrade the submitted ligand-receptor handoff.",
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
            "source_a_edge_id": f"M22B-TARGET-SEARCH-0684-{index:02d}", "edge_status": update["status"],
            "context_scope": update["context"], "cell_type_context": update["context"], "compartment_context": "unspecified", "species_context": update["species"], "injury_context": "not_assessed",
            "confidence_tier": "high", "export_priority": "medium", "exportable": "true", "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing {update['hold']}; upstream handoff remains separate and unupgraded.",
        })
        evidence.append({
            "b_evidence_id": evidence_id, "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-0684-{index:02d}", "b_edge_ids": edge_id, "source_kind": "reviewed_direct_target" if update["scope"] == "direct_edge" else "reviewed_functional_target",
            "source_locator": update["locator"], "support_kind": "primary_experiment", "species_support": update["species"], "source_scope": update["scope"],
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
