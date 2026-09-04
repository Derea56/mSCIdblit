#!/usr/bin/env python3
"""Add direct, reusable TF-to-target lanes found in holds 0389-0396."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch066.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch066_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch066-2026-09-04"

UPDATES = [
    {
        "holds": "M22B-HOLD-AUDIT-0389",
        "tf": "MYC",
        "target": "ITGA1",
        "species": "human",
        "locator": "PMID:26096932; PMCID:PMC4820680; DOI:10.1038/onc.2015.231",
        "context": "Human colorectal-cell studies showed MYC occupancy at the proximal ITGA1 promoter, MYC-dependent promoter-reporter activation, response-element disruption effects, and reduced ITGA1 after MYC inhibition or knockdown. Non-SCI intestinal-cancer comparator.",
        "summary": "MYC promoter ChIP, response-element disruption, promoter-reporter activation, and MYC loss-of-function support direct MYC activation of human ITGA1.",
        "limitations": "The study concerns colorectal cancer and does not establish COL1A1-ITGA1 signaling to MYC or SCI activity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0392",
        "tf": "SP1",
        "target": "ITGA9",
        "species": "human",
        "locator": "PMID:25746835; DOI:10.1016/j.exer.2015.03.001",
        "context": "Human corneal epithelial and ocular-cell studies showed Sp1 binding at the ITGA9 promoter by footprinting/ChIP and reduced alpha9 expression after Sp1 RNAi. Non-SCI wound-repair comparator.",
        "summary": "Sp1 promoter binding and Sp1 loss-of-function support direct SP1 activation of human ITGA9.",
        "limitations": "The study concerns ocular epithelial and melanoma models and does not establish COL1A1-ITGA9 signaling to SP1 or SCI activity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0393",
        "tf": "SP1",
        "target": "Itgav",
        "species": "mouse",
        "locator": "PMID:10899572; DOI:10.1016/S0167-4781(00)00121-4",
        "context": "Mouse melanoma-cell studies identified a functional Sp1 site in the Itgav promoter; binding interference and mutation/deletion reduced promoter activity. Non-SCI melanoma comparator.",
        "summary": "Sp1 binding-site evidence and mutation/deletion effects support direct SP1 activation of mouse Itgav.",
        "limitations": "The study concerns mouse integrin-alphaV promoter regulation in melanoma and does not establish COL1A1-ITGAV/ITGB8 signaling to SP1 or SCI activity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0393",
        "tf": "ETS1",
        "target": "Itgav",
        "species": "mouse",
        "locator": "PMID:10899572; DOI:10.1016/S0167-4781(00)00121-4",
        "context": "Mouse melanoma-cell studies identified two functional Ets sites in the Itgav promoter; mutation/deletion reduced activity and Ets-1 plus Sp1 cotransfection increased promoter activity. Non-SCI melanoma comparator.",
        "summary": "Ets-site mutation/deletion and Ets-1 cotransactivation support direct ETS1 activation of mouse Itgav.",
        "limitations": "The study concerns mouse integrin-alphaV promoter regulation in melanoma and does not establish COL1A1-ITGAV/ITGB8 signaling to ETS1 or SCI activity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0394",
        "tf": "HIF1A",
        "target": "SDC4",
        "species": "human",
        "locator": "PMID:24558194; PMCID:PMC4021441; DOI:10.1096/fj.13-243741",
        "context": "Human nucleus-pulposus-cell studies showed hypoxic SDC4 induction, HRE-dependent SDC4 promoter activity, increased SDC4 after HIF-1alpha overexpression, and reduced expression after HIF-1alpha or HIF-1beta suppression. Non-SCI intervertebral-disc comparator.",
        "summary": "HRE-dependent promoter activity and HIF1A gain- and loss-of-function support direct HIF1A activation of human SDC4 under hypoxia.",
        "limitations": "The study concerns SDC4 in intervertebral-disc cells, not the candidate SDC1 pair; it does not establish COL1A1-SDC1 signaling to HIF1A or SCI activity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0395",
        "tf": "SMAD3",
        "target": "SDC4",
        "species": "human",
        "locator": "PMID:37935976; PMCID:PMC10766520; DOI:10.1038/s41388-023-02880-7",
        "context": "Human osteosarcoma-cell studies identified SMAD3 binding at SDC4 promoter SBE sites by ChIP and reduced TGF-beta-induced promoter activity after SBE deletion. Non-SCI osteosarcoma comparator.",
        "summary": "SMAD3 ChIP and SBE deletion effects support direct SMAD3 activation of human SDC4 in a TGF-beta-responsive system.",
        "limitations": "The study concerns osteosarcoma TGF-beta feedback and does not establish COL1A1-SDC4 signaling to SMAD3 or SCI activity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0395",
        "tf": "KLF5",
        "target": "SDC4",
        "species": "human",
        "locator": "PMID:41747442; DOI:10.1016/j.bbrc.2026.153515",
        "context": "Human colorectal-cell studies showed KLF5 binding at SDC4 promoter regions by ChIP-qPCR, promoter-region dependence in reporter assays, and reduced SDC4 after KLF5 knockdown. Non-SCI colorectal-cancer comparator.",
        "summary": "KLF5 promoter ChIP, promoter deletion analysis, reporter activity, and knockdown effects support direct KLF5 activation of human SDC4.",
        "limitations": "The study concerns colorectal cancer and does not establish COL1A1-SDC4 signaling to KLF5 or SCI activity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0395",
        "tf": "RELA",
        "target": "SDC4",
        "species": "human",
        "locator": "PMID:40341546; DOI:10.1038/s41598-025-00793-x",
        "context": "Human tumor-cell studies showed TNF-alpha-induced NF-kappaB/RelA binding at the SDC4 promoter by ChIP-qPCR and reduced SDC4 induction after NF-kappaB inhibition. Non-SCI tumor comparator.",
        "summary": "TNF-alpha-dependent RelA promoter occupancy and NF-kappaB inhibitor effects support direct RELA-associated activation of human SDC4.",
        "limitations": "The study concerns TNF-alpha-treated tumor cells and does not establish COL1A1-SDC4 signaling to RELA or SCI activity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0394",
        "tf": "ZEB1",
        "target": "SDC1",
        "species": "human",
        "locator": "PMID:30065348; PMCID:PMC6068163; DOI:10.1038/s41598-018-29829-1",
        "context": "Human prostate-epithelial studies showed ZEB1 binding at the SDC1 promoter by ChIP, reduced promoter activity after ZEB1 expression, and increased SDC1 after ZEB1 knockdown. Non-SCI prostate-cancer comparator.",
        "summary": "ZEB1 promoter ChIP, promoter repression, and knockdown effects support direct ZEB1 repression of human SDC1.",
        "limitations": "The study concerns prostate epithelial cancer and does not establish COL1A1-SDC1 signaling to ZEB1 or SCI activity.",
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
            "source_a_edge_id": f"M22B-TARGET-SEARCH-0389-{index:02d}",
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
            "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-0389-{index:02d}",
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
            "consolidation_note": f"{BATCH_ID}: primary-study target-gene evidence; upstream handoff remains separate and unupgraded.",
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
