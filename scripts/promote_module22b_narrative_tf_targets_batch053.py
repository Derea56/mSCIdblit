#!/usr/bin/env python3
"""Add direct, reusable TF-to-chemokine lanes found in holds 0269-0276."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch053.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch053_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch053-2026-09-04"

UPDATES = [
    {
        "holds": "M22B-HOLD-AUDIT-0270",
        "tf": "CEBPB",
        "target": "CCL4",
        "species": "human",
        "confidence": "high",
        "locator": "PMID:20702408; PMCID:PMC2963416; DOI:10.1074/jbc.M110.130377",
        "context": "Human articular-chondrocyte experiments showed C/EBPbeta binding to an IL-1-responsive CCL4 promoter element by EMSA and ChIP, with promoter mutation, C/EBPbeta overexpression, and siRNA perturbation changing CCL4 induction; cartilage-inflammation comparator, non-SCI.",
        "summary": "C/EBPbeta directly bound the human CCL4 promoter, and promoter mutation, C/EBPbeta overexpression, and C/EBPbeta siRNA altered IL-1beta-responsive CCL4 expression, supporting a direct CEBPB-to-CCL4 target lane.",
        "limitations": "The study concerns IL-1beta-responsive human chondrocytes and does not establish downstream signaling from Ccl4-Ackr2. It is not an SCI receiver-cell experiment and does not establish that the submitted atypical-receptor branch activates CEBPB.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0271;M22B-HOLD-AUDIT-0272;M22B-HOLD-AUDIT-0273;M22B-HOLD-AUDIT-0274",
        "tf": "SP1",
        "target": "CCL5",
        "species": "human",
        "confidence": "high",
        "locator": "PMID:19124744; DOI:10.4049/jimmunol.182.2.1011",
        "context": "Peripheral human blood NK-cell experiments identified a compact CCL5 promoter region; EMSA, ChIP, heterologous-promoter assays, and site-directed mutagenesis showed SP1 binding at -75 to -56 and dependence of constitutive CCL5 transcription on this site; immune-cell comparator, non-SCI.",
        "summary": "SP1 binding and site-directed promoter evidence in human NK cells support direct SP1 control of constitutive CCL5 transcription.",
        "limitations": "This is a constitutive human NK-cell CCL5 program and does not establish CCL5 signaling through ACKR2, CCR3, ACKR1, or CCR1L1, nor does it establish SCI receiver-cell activity. The standalone SP1-to-CCL5 target lane is not transferred to any receptor handoff.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0271;M22B-HOLD-AUDIT-0272;M22B-HOLD-AUDIT-0273;M22B-HOLD-AUDIT-0274",
        "tf": "FLI1",
        "target": "Ccl5",
        "species": "mouse",
        "confidence": "high",
        "locator": "PMID:25098295; PMCID:PMC4157095; DOI:10.4049/jimmunol.1302779",
        "context": "Murine Ccl5 promoter experiments showed Fli-1 binding at endogenous distal Ets sites by ChIP, dose-dependent promoter transactivation, DNA-binding-domain dependence, promoter-site deletion effects, and reduced Ccl5 expression after Fli-1 reduction in lupus-prone mouse kidney and endothelial comparator systems; inflammatory comparator, non-SCI.",
        "summary": "Fli-1 occupancy and promoter perturbation/transactivation evidence support a direct FLI1-to-Ccl5 target lane in mouse.",
        "limitations": "The evidence is from lupus-prone mouse kidney and endothelial-cell models and does not establish CCL5 signaling through ACKR2, CCR3, ACKR1, or CCR1L1, nor SCI receiver-cell activity. The standalone FLI1-to-Ccl5 lane is not transferred to any receptor handoff.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0271;M22B-HOLD-AUDIT-0272;M22B-HOLD-AUDIT-0273;M22B-HOLD-AUDIT-0274",
        "tf": "RELA",
        "target": "Ccl5",
        "species": "mouse",
        "confidence": "high",
        "locator": "PMID:23376885; PMCID:PMC4003203",
        "context": "Murine 4T1 breast-tumor-cell experiments showed sequence-specific NF-kB binding at the Ccl5 promoter with p50/p65 supershift, p65-driven Ccl5 promoter-reporter activation, and inhibition by a dominant-negative IkBa mutant; tumor comparator, non-SCI.",
        "summary": "p65/RELA promoter binding and gain- and loss-of-function reporter experiments support a direct RELA-to-Ccl5 regulatory lane in mouse.",
        "limitations": "The study uses a murine breast-tumor cell line and promoter-reporter/EMSA evidence rather than endogenous RelA ChIP at the Ccl5 locus. It does not establish CCL5 signaling through ACKR2, CCR3, ACKR1, or CCR1L1, nor SCI receiver-cell activity. The standalone RELA-to-Ccl5 lane is not transferred to any receptor handoff.",
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
    added = []
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
            "source_a_edge_id": f"M22B-TARGET-SEARCH-0269-{index:02d}",
            "edge_status": "reviewed_direct_target",
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
            "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-0269-{index:02d}",
            "b_edge_ids": edge_id,
            "source_kind": "reviewed_direct_target",
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
        added.append((edge_id, evidence_id))
        edge_num += 1
        evidence_num += 1

    audit_fields = ["batch_id", "hold_edges_reviewed", "tf", "target", "species", "b_edge_id", "b_evidence_id", "source_locator", "upstream_handoff_upgraded", "standalone_target_gene_edge", "decision_basis"]
    write_tsv(AUDIT_PATH, audit_rows, audit_fields)
    write_tsv(EDGE_PATH, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    summary = {
        "batch_id": BATCH_ID,
        "standalone_target_gene_edges_added": len(added),
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
