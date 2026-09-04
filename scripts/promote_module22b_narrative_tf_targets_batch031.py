#!/usr/bin/env python3
"""Add target lanes recovered while reviewing Module 22B holds 0029-0032."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch031.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch031_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch031-2026-09-03"

UPDATES = [
    (
        "M22B-HOLD-AUDIT-0030",
        "ESR2",
        "HSD17B1",
        "mouse",
        "PMID:38031019; PMCID:PMC10688478",
        "Primary mouse ovarian ERβ/ESR2 cistrome-transcriptome study with ERβ ChIP-seq and wild-type/ERβ-knockout RNA-seq; non-SCI comparator.",
        "Integrated ERβ occupancy and expression analysis identified Hsd17b1 as an ERβ-bound, ERβ-dependent ovarian target gene.",
        "This standalone ESR2 target lane is supported by integrated cistrome/transcriptome evidence rather than a single promoter-causality assay; it does not establish the submitted HSD17B1 handoff or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0030",
        "ESR2",
        "KCNMB1",
        "human",
        "PMID:37948436; PMCID:PMC10637685",
        "Primary human colonic smooth-muscle study with ERβ/ESR2 promoter binding, reporter, deletion/mutagenesis, and chromatin assays; rat physiology comparator; non-SCI.",
        "ERβ/ESR2 directly bound and activated the human KCNMB1 promoter in colonic smooth-muscle cells.",
        "This is a standalone ESR2 target-gene edge from a non-SCI smooth-muscle model; it does not establish the submitted HSD17B1 handoff or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0031",
        "ETV4",
        "CCND1",
        "human",
        "PMCID:PMC5805611",
        "Primary human pancreatic-cell study with ETV4 promoter occupancy, perturbation, and site-specific CCND1 promoter reporter/mutation assays; non-SCI comparator.",
        "ETV4 bound and transcriptionally regulated the human CCND1 promoter in pancreatic cells.",
        "This standalone ETV4 target lane does not establish the submitted FGF18-FGFR2/FGFR4-to-ETV4/ETV5 handoff or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0031",
        "ETV5",
        "MMP2",
        "human",
        "PMID:17638886",
        "Primary human endometrial-cancer study with ETV5 perturbation, MMP2 expression/activity assays, and ETV5 occupancy at the MMP2 promoter; mouse orthotopic validation; non-SCI comparator.",
        "ETV5 bound the human MMP2 promoter and promoted MMP2 expression and matrix-metalloproteinase activity.",
        "This standalone ETV5 target lane does not establish the submitted FGF18-FGFR2/FGFR4-to-ETV4/ETV5 handoff or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0031",
        "ETV4;ETV5",
        "SHH",
        "mouse",
        "PMID:26555052; PMCID:PMC4763945",
        "Primary mouse lung-branching study with FGF-regulated Etv4/Etv5 occupancy and perturbation of the Shh enhancer; developmental, non-SCI comparator.",
        "FGF-regulated Etv4 and Etv5 collectively occupied and activated a Shh enhancer in mouse lung branching.",
        "This composite lane records the reported Etv4/Etv5 regulatory module and should not be interpreted as either factor alone being sufficient; it does not establish the submitted FGF18-receptor handoff or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0032",
        "FOXO1",
        "CYP7A1",
        "mouse",
        "PMID:19237543; PMCID:PMC2670116",
        "Primary mouse liver/hepatocyte study with FOXO1 chromatin occupancy, CYP7A1 promoter binding/mutation, perturbation, and FGF15/FGFR4 pathway experiments; non-SCI metabolic comparator.",
        "FOXO1 directly bound and activated the mouse Cyp7a1 promoter, while FGF15/FGFR4 signaling suppressed this FOXO1-dependent bile-acid metabolic program.",
        "This standalone FOXO1 target lane does not establish the submitted FGF15-FGFR4-specific handoff or SCI specificity.",
    ),
]


def next_id(rows: list[dict[str, str]], field: str) -> int:
    return max([int(match.group(1)) for row in rows if (match := re.search(r"(\d+)$", row[field]))] or [0]) + 1


def main() -> int:
    edges, evidence = read_tsv(EDGE_PATH), read_tsv(EVIDENCE_PATH)
    existing = {(r.get("species_context", "").casefold(), r.get("source_entity", "").casefold(), r.get("target_entity", "").casefold()) for r in edges if r.get("pathway_name") == "target_gene"}
    edge_number, evidence_number = next_id(edges, "b_edge_id"), next_id(evidence, "b_evidence_id")
    audit = []
    for index, (holds, tf, target, species, locator, context, summary, limitations) in enumerate(UPDATES, start=141):
        pair = (species.casefold(), tf.casefold(), target.casefold())
        if pair in existing:
            raise SystemExit(f"target pair already exists: {pair}")
        edge_id, evidence_id = f"M22B-E{edge_number:06d}", f"M22B-EVID-{evidence_number:06d}"
        edge_number += 1
        evidence_number += 1
        edges.append({"b_edge_id": edge_id, "source_entity": tf, "relation_type": f"{tf} activates the {target} target gene in primary-study evidence", "target_entity": target, "pathway_name": "target_gene", "evidence_layer": "ligand_receptor_or_direct_molecular", "source_a_edge_id": f"M22B-TARGET-SEARCH-{index:04d}", "edge_status": "reviewed_direct_target", "context_scope": context, "cell_type_context": context, "compartment_context": "unspecified", "species_context": species, "injury_context": "not_assessed", "confidence_tier": "high", "export_priority": "medium", "exportable": "true", "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing {holds}; upstream handoff remains separate and unupgraded."})
        evidence.append({"b_evidence_id": evidence_id, "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-{index:04d}", "b_edge_ids": edge_id, "source_kind": "reviewed_direct_target", "source_locator": locator, "support_kind": "primary_experiment", "species_support": species, "source_scope": "direct_edge", "confidence_tier": "high", "citation_note": f"Primary-study target-gene evidence identified while reviewing hold row {holds}; standalone general TF-regulon claim.", "evidence_summary": summary, "limitations": limitations, "evidence_layer": "ligand_receptor_or_direct_molecular", "exportable": "true", "consolidation_note": f"{BATCH_ID}: primary-study target-gene evidence; upstream handoff remains separate and unupgraded."})
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
