#!/usr/bin/env python3
"""Add the direct mouse Sox9-to-Adgrg6 lane found in hold 0430."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch068.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch068_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch068-2026-09-04"

UPDATE = {
    "holds": "M22B-HOLD-AUDIT-0430",
    "tf": "Sox9",
    "target": "Adgrg6",
    "species": "mouse",
    "locator": "PMID:41994120; PMCID:PMC13082157; DOI:10.21203/rs.3.rs-9271349/v1",
    "context": "Mouse intervertebral-disc studies identified SOX9 occupancy at an accessible intronic Adgrg6 regulatory region by CUT&Run and linked Sox9 dosage to Adgrg6 expression in a feedforward spinal-stability circuit. AIS/spinal-stability comparator; the source is a preprint.",
    "summary": "Mouse IVD SOX9 CUT&Run occupancy at Adgrg6 together with expression and genetic-interaction data support direct SOX9 promotion of Adgrg6 transcription.",
    "limitations": "The study is a preprint on mouse intervertebral-disc and adolescent-idiopathic-scoliosis biology; it does not establish COL4A1-ADGRG6 signaling to SOX9 or traumatic SCI activity.",
}


def next_id(rows: list[dict[str, str]], field: str) -> int:
    return max([int(match.group(1)) for row in rows if (match := re.search(r"(\d+)$", row[field]))] or [0]) + 1


def main() -> int:
    edges, evidence = read_tsv(EDGE_PATH), read_tsv(EVIDENCE_PATH)
    pair = (UPDATE["species"].casefold(), UPDATE["tf"].casefold(), UPDATE["target"].casefold())
    existing = {
        (r.get("species_context", "").casefold(), r.get("source_entity", "").casefold(), r.get("target_entity", "").casefold())
        for r in edges
        if r.get("pathway_name") == "target_gene"
    }
    if pair in existing:
        raise SystemExit(f"target pair already exists: {pair}")
    edge_id = f"M22B-E{next_id(edges, 'b_edge_id'):06d}"
    evidence_id = f"M22B-EVID-{next_id(evidence, 'b_evidence_id'):06d}"
    edges.append({
        "b_edge_id": edge_id,
        "source_entity": UPDATE["tf"],
        "relation_type": f"{UPDATE['tf']} promotes the {UPDATE['target']} target gene in primary-study evidence",
        "target_entity": UPDATE["target"],
        "pathway_name": "target_gene",
        "evidence_layer": "ligand_receptor_or_direct_molecular",
        "source_a_edge_id": "M22B-TARGET-SEARCH-0430-01",
        "edge_status": "reviewed_direct_target",
        "context_scope": UPDATE["context"],
        "cell_type_context": UPDATE["context"],
        "compartment_context": "unspecified",
        "species_context": UPDATE["species"],
        "injury_context": "not_assessed",
        "confidence_tier": "high",
        "export_priority": "medium",
        "exportable": "true",
        "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing {UPDATE['holds']}; upstream handoff remains separate and unupgraded.",
    })
    evidence.append({
        "b_evidence_id": evidence_id,
        "source_a_evidence_id": "M22B-TARGET-SEARCH-EVID-0430-01",
        "b_edge_ids": edge_id,
        "source_kind": "reviewed_direct_target",
        "source_locator": UPDATE["locator"],
        "support_kind": "primary_experiment",
        "species_support": UPDATE["species"],
        "source_scope": "direct_edge",
        "confidence_tier": "high",
        "citation_note": f"Primary-study target-gene evidence identified while reviewing hold row {UPDATE['holds']}; standalone general TF-regulon claim.",
        "evidence_summary": UPDATE["summary"],
        "limitations": UPDATE["limitations"],
        "evidence_layer": "ligand_receptor_or_direct_molecular",
        "exportable": "true",
        "consolidation_note": f"{BATCH_ID}: primary-study target-gene evidence; upstream handoff remains separate and unupgraded.",
    })
    audit_fields = ["batch_id", "hold_edges_reviewed", "tf", "target", "species", "b_edge_id", "b_evidence_id", "source_locator", "upstream_handoff_upgraded", "standalone_target_gene_edge", "decision_basis"]
    write_tsv(AUDIT_PATH, [{
        "batch_id": BATCH_ID,
        "hold_edges_reviewed": UPDATE["holds"],
        "tf": UPDATE["tf"],
        "target": UPDATE["target"],
        "species": UPDATE["species"],
        "b_edge_id": edge_id,
        "b_evidence_id": evidence_id,
        "source_locator": UPDATE["locator"],
        "upstream_handoff_upgraded": "false",
        "standalone_target_gene_edge": "true",
        "decision_basis": UPDATE["summary"],
    }], audit_fields)
    write_tsv(EDGE_PATH, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    summary = {
        "batch_id": BATCH_ID,
        "standalone_target_gene_edges_added": 1,
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
