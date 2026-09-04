#!/usr/bin/env python3
"""Add primary-study desmosomal and odontoblast TF-target lanes for holds 0661-0668."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch078.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch078_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch078-2026-09-04"

UPDATES = [
    {
        "hold": "M22B-HOLD-AUDIT-0663;M22B-HOLD-AUDIT-0664;M22B-HOLD-AUDIT-0665;M22B-HOLD-AUDIT-0666;M22B-HOLD-AUDIT-0667", "tf": "TP63", "target": "DSG1", "species": "human", "relation": "regulates", "status": "reviewed_direct_target", "scope": "direct_edge",
        "locator": "PMID:24594668; PMCID:PMC4102640; DOI:10.1038/jid.2014.124",
        "context": "Human epidermal keratinocyte and organotypic epidermis experiments detected p63 binding at a DSG1 enhancer; UVB-associated loss of p63 binding tracked reduced DSG1 expression. Non-SCI epithelial comparator.",
        "summary": "p63 occupancy at a human DSG1 enhancer in epidermal cells, together with linked DSG1 expression changes, supports DSG1 as a TP63-regulated target.",
        "limitations": "The study emphasizes UVB-associated loss of occupancy rather than a complete TP63 gain-of-function promoter series; it does not establish the submitted desmosomal protein handoffs or SCI activity.",
    },
    {
        "hold": "M22B-HOLD-AUDIT-0667", "tf": "TP53", "target": "DSC3", "species": "human", "relation": "regulates", "status": "reviewed_regulatory_support", "scope": "functional_edge",
        "locator": "PMID:22941060; DOI:10.1093/carcin/bgs273",
        "context": "Human lung-cancer cell experiments reported p53 overexpression-associated restoration of DSC3 expression in an unmethylated line and after demethylation in a methylated line. Non-SCI epithelial cancer comparator.",
        "summary": "Primary human-cell perturbation linked p53 expression to DSC3 re-expression, supporting a functional TP53–DSC3 target relationship.",
        "limitations": "The source does not establish direct TP53 binding at the DSC3 promoter and methylation state limits the perturbation response; it does not establish the submitted Dsg1c-Dsc3 handoff or SCI activity.",
    },
    {
        "hold": "M22B-HOLD-AUDIT-0668", "tf": "Dlx5", "target": "Dspp", "species": "mouse", "relation": "activates", "status": "reviewed_direct_target", "scope": "direct_edge",
        "locator": "PMID:20843790; PMCID:PMC2978565",
        "context": "Mouse pre-odontoblast and C2C12 experiments showed Dlx5-dependent Dspp expression and activation of Dspp promoter reporters; promoter deletion analysis localized a Dlx5-responsive H1 region and EMSA detected Dlx5 binding to a Dspp probe. Non-SCI odontoblast comparator.",
        "summary": "Dlx5 perturbation, Dspp promoter activation, response-element mapping, and DNA-binding assays support mouse Dspp as a Dlx5 target.",
        "limitations": "The study is an odontoblast/BMP comparator and does not establish the submitted DSPP-integrin handoff or SCI activity.",
    },
    {
        "hold": "M22B-HOLD-AUDIT-0668", "tf": "Msx2", "target": "Dspp", "species": "mouse", "relation": "represses", "status": "reviewed_regulatory_support", "scope": "functional_edge",
        "locator": "PMID:20843790; PMCID:PMC2978565",
        "context": "Mouse pre-odontoblast and C2C12 experiments showed Msx2 suppression of Dspp expression and Dspp promoter activity, with the effect localized to the H2 promoter region and linked to antagonism of Dlx5 binding. Non-SCI odontoblast comparator.",
        "summary": "Msx2 perturbation and H2-dependent Dspp promoter repression support mouse Dspp as an Msx2-regulated target.",
        "limitations": "The source supports repression/antagonism rather than activation and does not establish the submitted DSPP-integrin handoff or SCI activity.",
    },
    {
        "hold": "M22B-HOLD-AUDIT-0668", "tf": "Runx2", "target": "Dspp", "species": "mouse", "relation": "activates", "status": "reviewed_regulatory_support", "scope": "functional_edge",
        "locator": "PMID:20843790; PMCID:PMC2978565",
        "context": "Mouse pre-odontoblast experiments showed that Runx2 overexpression stimulated Dspp mRNA and Runx2 knockdown reduced BMP-2-induced Dspp expression. Non-SCI odontoblast comparator.",
        "summary": "Runx2 gain- and loss-of-function effects on mouse Dspp expression support a functional Runx2–Dspp target relationship.",
        "limitations": "The source does not establish direct Runx2 occupancy at the Dspp promoter in the reported experiments; it does not establish the submitted DSPP-integrin handoff or SCI activity.",
    },
    {
        "hold": "M22B-HOLD-AUDIT-0668", "tf": "Sp7", "target": "Dspp", "species": "mouse", "relation": "activates", "status": "reviewed_direct_target", "scope": "direct_edge",
        "locator": "PMID:29405385; PMCID:PMC6002875",
        "context": "Mouse odontoblast/ameloblast experiments showed loss of Dspp in Sp7-deficient teeth and strong activation of a mouse Dspp promoter reporter by Sp7; the source describes conserved Sp motifs and direct promoter control. Non-SCI odontoblast comparator.",
        "summary": "Sp7 loss-of-function and mouse Dspp promoter-reporter activation establish Dspp as an Sp7 target.",
        "limitations": "The study uses tooth-development and heterologous reporter contexts and does not establish the submitted DSPP-integrin handoff or SCI activity.",
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
            "source_a_edge_id": f"M22B-TARGET-SEARCH-0663-{index:02d}", "edge_status": update["status"],
            "context_scope": update["context"], "cell_type_context": update["context"], "compartment_context": "unspecified", "species_context": update["species"], "injury_context": "not_assessed",
            "confidence_tier": "high", "export_priority": "medium", "exportable": "true", "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing {update['hold']}; upstream handoff remains separate and unupgraded.",
        })
        evidence.append({
            "b_evidence_id": evidence_id, "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-0663-{index:02d}", "b_edge_ids": edge_id, "source_kind": "reviewed_direct_target" if update["scope"] == "direct_edge" else "reviewed_functional_target",
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
