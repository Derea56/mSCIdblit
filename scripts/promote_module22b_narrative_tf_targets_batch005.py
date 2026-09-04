#!/usr/bin/env python3
"""Stage another conservative set of standalone primary-study TF targets."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch005.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch005_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch005-2026-09-03"

UPDATES = [
    ("M22B-E000143", "CTNNB1", "MYC", "human", "PMID:17360646", "Human HCT116 colorectal-carcinoma cells with beta-catenin/TCF4 chromatin-occupancy and target-gene analyses; non-SCI comparator.", "Primary serial-analysis and chromatin-occupancy experiments identified MYC as a high-confidence beta-catenin/TCF4 target and showed beta-catenin/TCF4 binding at the MYC regulatory region.", "The activation is beta-catenin/TCF4-complex dependent and cancer-cell-context dependent; this does not establish the reviewed Wnt5a-FZD6 handoff or SCI activation."),
    ("M22B-E000143", "CTNNB1", "CCND1", "human", "PMID:17360646", "Human HCT116 colorectal-carcinoma cells with beta-catenin/TCF4 chromatin-occupancy and target-gene analyses; non-SCI comparator.", "Primary serial-analysis and chromatin-occupancy experiments identified CCND1 as a beta-catenin/TCF4-associated target and showed beta-catenin/TCF4 binding at the cyclin-D1 promoter.", "The activation is beta-catenin/TCF4-complex dependent and cancer-cell-context dependent; this does not establish the reviewed Wnt5a-FZD6 handoff or SCI activation."),
    ("M22B-E000143", "TCF4", "MYC", "human", "PMID:17360646", "Human HCT116 colorectal-carcinoma cells with TCF4/beta-catenin chromatin-occupancy and target-gene analyses; TCF4 denotes the TCF7L2 alias; non-SCI comparator.", "Primary experiments identified MYC as a high-confidence TCF4/beta-catenin target and showed TCF4/beta-catenin occupancy at the MYC regulatory region.", "The activation is TCF7L2/TCF4-alias and beta-catenin-complex dependent and cancer-cell-context dependent; this does not establish the reviewed Wnt5a-FZD6 handoff or SCI activation."),
    ("M22B-E000143", "TCF4", "CCND1", "human", "PMID:17360646", "Human HCT116 colorectal-carcinoma cells with TCF4/beta-catenin chromatin-occupancy and target-gene analyses; TCF4 denotes the TCF7L2 alias; non-SCI comparator.", "Primary experiments identified CCND1 as a TCF4/beta-catenin-associated target and showed TCF4/beta-catenin occupancy at the cyclin-D1 promoter.", "The activation is TCF7L2/TCF4-alias and beta-catenin-complex dependent and cancer-cell-context dependent; this does not establish the reviewed Wnt5a-FZD6 handoff or SCI activation."),
    ("M22B-E000173", "ETV4", "TNF", "human", "PMID:37670477; PMCID:PMC10693303", "Human HepG2/Huh7 cells and mouse hepatocyte-specific ETV4 models with ETV4 promoter ChIP, site-mutagenesis, reporter, and perturbation experiments; non-SCI comparator.", "Primary experiments showed ETV4 occupancy at the TNF promoter and ETV4-dependent TNF transcription, with promoter-site mutation and gain/loss-of-function assays supporting direct activation.", "The effect is hepatic, inflammatory, and cancer-model dependent and does not establish the reviewed FGF18-FGFR handoff or SCI activation."),
    ("M22B-E000173", "ETV4", "MAPK11", "human", "PMID:37670477; PMCID:PMC10693303", "Human HepG2/Huh7 cells and mouse hepatocyte-specific ETV4 models with ETV4 promoter ChIP, site-mutagenesis, reporter, and perturbation experiments; non-SCI comparator.", "Primary experiments showed ETV4 occupancy at the MAPK11 promoter and ETV4-dependent MAPK11 transcription, with promoter-site mutation and gain/loss-of-function assays supporting direct activation.", "The effect is hepatic, inflammatory, and cancer-model dependent and does not establish the reviewed FGF18-FGFR handoff or SCI activation."),
    ("M22B-E000388", "SMAD3", "SERPINE1", "human", "PMID:9765209; PMCID:PMC317197", "Human PAI-1/SERPINE1 promoter assays with Smad3/Smad4 and TFE3 cooperation; non-SCI comparator.", "Primary promoter and transactivation experiments showed Smad3/Smad4 cooperates with TFE3 to activate the human PAI-1/SERPINE1 promoter.", "The activation is cooperative with Smad4/TFE3 and TGF-beta-context dependent; this does not establish the reviewed BMP8B/activin/MSTN handoff or SCI activation."),
    ("M22B-E000246", "MYOD1", "Ckm", "mouse", "PMID:21797989", "Mouse skeletal-muscle differentiation models with MyoD occupancy at the muscle creatine kinase intronic enhancer, ChIP/ChIP-seq, and enhancer-activity assays; non-SCI comparator.", "Primary enhancer studies identified MyoD occupancy at the Ckm intronic enhancer and showed enhancer activity during myogenic differentiation, supporting MyoD-associated activation of Ckm.", "The enhancer response is cooperative with myogenin, MEF2, and other myogenic cofactors and is muscle-lineage dependent; the reviewed FGF6-FGFR4 handoff and SCI activation are not established."),
    ("M22B-E000246", "MYOG", "Ckm", "mouse", "PMID:21797989", "Mouse skeletal-muscle differentiation models with myogenin occupancy at the muscle creatine kinase intronic enhancer, ChIP/ChIP-seq, and enhancer-activity assays; non-SCI comparator.", "Primary enhancer studies identified myogenin occupancy at the Ckm intronic enhancer and showed enhancer activity during myogenic differentiation, supporting myogenin-associated activation of Ckm.", "The enhancer response is cooperative with MyoD, MEF2, and other myogenic cofactors and is muscle-lineage dependent; the reviewed FGF6-FGFR4 handoff and SCI activation are not established."),
]


def next_id(rows: list[dict[str, str]], field: str) -> int:
    return max([int(m.group(1)) for row in rows if (m := re.search(r"(\d+)$", row[field]))] or [0]) + 1


def main() -> int:
    edges, evidence = read_tsv(EDGE_PATH), read_tsv(EVIDENCE_PATH)
    existing = {(r.get("species_context", "").casefold(), r.get("source_entity", "").casefold(), r.get("target_entity", "").casefold()) for r in edges if r.get("pathway_name") == "target_gene"}
    edge_number, evidence_number = next_id(edges, "b_edge_id"), next_id(evidence, "b_evidence_id")
    audit = []
    for i, (holds, tf, target, species, locator, context, summary, limitations) in enumerate(UPDATES, start=42):
        pair = (species.casefold(), tf.casefold(), target.casefold())
        if pair in existing:
            raise SystemExit(f"target pair already exists: {pair}")
        edge_id, evidence_id = f"M22B-E{edge_number:06d}", f"M22B-EVID-{evidence_number:06d}"
        edge_number += 1
        evidence_number += 1
        edges.append({"b_edge_id": edge_id, "source_entity": tf, "relation_type": f"{tf} activates the {target} target gene in primary-study evidence", "target_entity": target, "pathway_name": "target_gene", "evidence_layer": "ligand_receptor_or_direct_molecular", "source_a_edge_id": f"M22B-TARGET-SEARCH-{i:04d}", "edge_status": "reviewed_direct_target", "context_scope": context, "cell_type_context": context, "compartment_context": "unspecified", "species_context": species, "injury_context": "not_assessed", "confidence_tier": "high", "export_priority": "medium", "exportable": "true", "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing {holds}; upstream handoff remains separate and unupgraded."})
        evidence.append({"b_evidence_id": evidence_id, "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-{i:04d}", "b_edge_ids": edge_id, "source_kind": "reviewed_direct_target", "source_locator": locator, "support_kind": "primary_experiment", "species_support": species, "source_scope": "direct_edge", "confidence_tier": "high", "citation_note": f"Primary-study target-gene evidence identified while reviewing hold rows {holds}; standalone general TF-regulon claim.", "evidence_summary": summary, "limitations": limitations, "evidence_layer": "ligand_receptor_or_direct_molecular", "exportable": "true", "consolidation_note": f"{BATCH_ID}: primary-study target-gene evidence; upstream handoff remains separate and unupgraded."})
        audit.append({"batch_id": BATCH_ID, "hold_edges_reviewed": holds, "tf": tf, "target": target, "species": species, "b_edge_id": edge_id, "b_evidence_id": evidence_id, "source_locator": locator, "upstream_handoff_upgraded": "false", "standalone_target_gene_edge": "true", "decision_basis": summary})
        existing.add(pair)
    fields = ["batch_id", "hold_edges_reviewed", "tf", "target", "species", "b_edge_id", "b_evidence_id", "source_locator", "upstream_handoff_upgraded", "standalone_target_gene_edge", "decision_basis"]
    write_tsv(AUDIT_PATH, audit, fields)
    write_tsv(EDGE_PATH, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    summary = {"batch_id": BATCH_ID, "standalone_target_gene_edges_added": len(audit), "upstream_handoff_edges_upgraded": 0, "high_edges_after": sum(r["confidence_tier"] == "high" for r in edges), "exportable_edges_after": sum(r["exportable"] == "true" for r in edges), "target_gene_edges_after": sum(r["pathway_name"] == "target_gene" for r in edges), "upstream_activation_inferred": False, "audit": str(AUDIT_PATH)}
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
