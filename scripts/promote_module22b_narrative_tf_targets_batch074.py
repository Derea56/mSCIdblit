#!/usr/bin/env python3
"""Add primary-study TF-target lanes found while reviewing holds 0629-0636."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch074.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch074_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch074-2026-09-04"

UPDATES = [
    {
        "hold": "M22B-HOLD-AUDIT-0629", "tf": "NR1H3", "target": "SULT2A1", "species": "human",
        "locator": "PMID:25028566; DOI:10.1124/dmd.114.058479",
        "context": "Human primary-hepatocyte and HepG2 studies showed LXR-alpha/NR1H3 binding to the SULT2A1 promoter by ChIP, promoter-reporter transactivation, and LXR-alpha knockdown. Non-SCI hepatic steroid-metabolism comparator.",
        "summary": "LXR-alpha/NR1H3 promoter binding, reporter transactivation, and knockdown evidence establish human SULT2A1 as an NR1H3 target gene.",
        "limitations": "The study concerns human hepatic steroid and xenobiotic metabolism and does not establish DHEAS signaling to NR1H3 or SCI activity.",
        "relation": "activates",
    },
    {
        "hold": "M22B-HOLD-AUDIT-0630;M22B-HOLD-AUDIT-0631;M22B-HOLD-AUDIT-0632", "tf": "SP1", "target": "SULT2B1", "species": "human",
        "locator": "PMID:15953604; DOI:10.1016/j.febslet.2005.05.041",
        "context": "Immortalized human keratinocyte experiments mapped regulatory GC-rich elements in the SULT2B1b promoter; Sp1/Sp2 supershift analysis and reporter assays showed Sp1-associated induction. Non-SCI skin/steroid-metabolism comparator.",
        "summary": "Mapped SULT2B1b promoter GC elements, Sp1 supershift evidence, and reporter induction support direct SP1 regulation of human SULT2B1.",
        "limitations": "The study concerns human keratinocytes and SULT2B1b promoter regulation, not DHEAS-specific PPAR signaling or SCI activity.",
        "relation": "activates",
    },
    {
        "hold": "M22B-HOLD-AUDIT-0630;M22B-HOLD-AUDIT-0631;M22B-HOLD-AUDIT-0632", "tf": "VDR", "target": "SULT2B1", "species": "human",
        "locator": "PMID:23579488; PMCID:PMC3656233; DOI:10.1210/me.2012-1369",
        "context": "Human prostate-cell studies mapped a vitamin-D-responsive DR7 element in the SULT2B1 promoter; VDR/RXR-alpha occupancy was shown by footprinting, EMSA, and ChIP, and the element was required for promoter induction. Non-SCI prostate/steroid-metabolism comparator.",
        "summary": "VDR/RXR-alpha occupancy at the SULT2B1 DR7 element and mutation-sensitive promoter induction support direct VDR regulation of human SULT2B1.",
        "limitations": "The study concerns human prostate tissue and cancer-cell models under vitamin-D stimulation and does not establish DHEAS signaling or SCI activity.",
        "relation": "activates",
    },
    {
        "hold": "M22B-HOLD-AUDIT-0634", "tf": "Srebf2", "target": "Srd5a2", "species": "mouse",
        "locator": "PMID:19500568; PMCID:PMC3124118; DOI:10.1016/j.yexcr.2009.05.025",
        "context": "Mouse liver and prostate studies showed SREBP-2/Srebf2 binding to the Srd5a2 promoter by ChIP-chip/ChIP, a responsive promoter region by reporter assays, in-vitro DNA binding by EMSA, and induction after SREBP-2 expression. Non-SCI steroid/lipid-metabolism comparator.",
        "summary": "SREBP-2/Srebf2 promoter occupancy, EMSA binding, responsive reporter activity, and expression induction establish mouse Srd5a2 as a direct Srebf2 target gene.",
        "limitations": "The study concerns mouse liver, prostate, and cultured-cell sterol regulation and does not establish DHT signaling to Srebf2 or SCI activity.",
        "relation": "activates",
    },
    {
        "hold": "M22B-HOLD-AUDIT-0635", "tf": "AR", "target": "SRD5A3", "species": "human",
        "locator": "PMID:22194926; DOI:10.1210/en.2011-1672",
        "context": "Human prostate-cell studies showed androgen-dependent AR recruitment to a negative androgen-response element in the SRD5A3 promoter by ChIP and in-vitro binding, with promoter deletion/mutation assays supporting functional regulation. Non-SCI prostate/androgen comparator.",
        "summary": "AR occupancy and in-vitro binding at the SRD5A3 promoter plus mutation-sensitive reporter effects establish direct AR regulation of human SRD5A3.",
        "limitations": "The study concerns human prostate cancer and androgen feedback; it does not establish the exact DHT-SRD5A3 upstream route or SCI activity.",
        "relation": "regulates",
    },
    {
        "hold": "M22B-HOLD-AUDIT-0636", "tf": "NR3C2", "target": "SCNN1A", "species": "human",
        "locator": "PMID:24062694",
        "context": "Human renal collecting-duct-cell studies used site-directed promoter mutation, DNA pull-down, and ChIP to show aldosterone-dependent MR/NR3C2 interaction with the alpha-ENaC/SCNN1A promoter. Non-SCI renal electrolyte-homeostasis comparator.",
        "summary": "MR/NR3C2 promoter interaction by DNA pull-down and ChIP, together with mutation-sensitive aldosterone promoter activity, supports direct NR3C2 regulation of human SCNN1A.",
        "limitations": "The study concerns human renal collecting-duct cells and aldosterone response; it does not establish DOC-CYP21A2 signaling to NR3C2 or SCI activity.",
        "relation": "activates",
    },
    {
        "hold": "M22B-HOLD-AUDIT-0636", "tf": "NR4A1", "target": "Cyp21a1", "species": "mouse",
        "locator": "PMID:8380897; PMCID:PMC358969; DOI:10.1128/mcb.13.2.861-868.1993",
        "context": "Mouse Y1 adrenocortical-cell studies showed NGFI-B/NR4A1 binding to the Cyp21a1/21-OHase promoter element by gel shift and footprinting; NR4A1 expression activated the intact promoter, while mutation of the element reduced activation. Non-SCI adrenal steroidogenesis comparator.",
        "summary": "NR4A1/NGFI-B binding, promoter activation, and loss of activation after response-element mutation establish mouse Cyp21a1 as a direct NR4A1 target gene.",
        "limitations": "The study concerns mouse adrenocortical Y1 cells and ACTH-responsive steroidogenesis and does not establish DOC-CYP21A2 signaling or SCI activity.",
        "relation": "activates",
    },
    {
        "hold": "M22B-HOLD-AUDIT-0636", "tf": "NR5A1", "target": "CYP21A2", "species": "human",
        "locator": "PMID:10608879; DOI:10.1074/jbc.274.53.38097",
        "context": "Human CYP21A2 regulatory-region studies in adrenal NCI-H295A cells identified an upstream enhancer; DNA-protein assays and SF-1/NR5A1 supershift/co-transfection experiments supported NR5A1 binding to two elements that contributed to CYP21 promoter activity. Non-SCI adrenal steroidogenesis comparator.",
        "summary": "NR5A1/SF-1 binding and functional enhancer/promoter evidence support direct NR5A1 regulation of human CYP21A2.",
        "limitations": "The study concerns human adrenal steroidogenic regulation and does not establish DOC signaling to NR3C2 or SCI activity.",
        "relation": "regulates",
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
            "source_a_edge_id": f"M22B-TARGET-SEARCH-0629-{index:02d}", "edge_status": "reviewed_direct_target", "context_scope": update["context"],
            "cell_type_context": update["context"], "compartment_context": "unspecified", "species_context": update["species"], "injury_context": "not_assessed",
            "confidence_tier": "high", "export_priority": "medium", "exportable": "true",
            "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing {update['hold']}; upstream handoff remains separate and unupgraded.",
        })
        evidence.append({
            "b_evidence_id": evidence_id, "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-0629-{index:02d}", "b_edge_ids": edge_id,
            "source_kind": "reviewed_direct_target", "source_locator": update["locator"], "support_kind": "primary_experiment", "species_support": update["species"],
            "source_scope": "direct_edge", "confidence_tier": "high", "citation_note": f"Primary-study target-gene evidence identified while reviewing hold row {update['hold']}; standalone general TF-regulon claim.",
            "evidence_summary": update["summary"], "limitations": update["limitations"], "evidence_layer": "ligand_receptor_or_direct_molecular", "exportable": "true",
            "consolidation_note": f"{BATCH_ID}: primary-study target-gene evidence; upstream handoff remains separate and unupgraded.",
        })
        audit_rows.append({
            "batch_id": BATCH_ID, "hold_edges_reviewed": update["hold"], "tf": update["tf"], "target": update["target"], "species": update["species"],
            "b_edge_id": edge_id, "b_evidence_id": evidence_id, "source_locator": update["locator"], "upstream_handoff_upgraded": "false",
            "standalone_target_gene_edge": "true", "decision_basis": update["summary"],
        })
        existing.add(pair); edge_num += 1; evidence_num += 1
    fields = ["batch_id", "hold_edges_reviewed", "tf", "target", "species", "b_edge_id", "b_evidence_id", "source_locator", "upstream_handoff_upgraded", "standalone_target_gene_edge", "decision_basis"]
    write_tsv(AUDIT_PATH, audit_rows, fields)
    write_tsv(EDGE_PATH, edges, EDGE_FIELDS); write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    summary = {
        "batch_id": BATCH_ID, "standalone_target_gene_edges_added": len(UPDATES), "upstream_handoff_edges_upgraded": 0,
        "high_edges_after": sum(r["confidence_tier"] == "high" for r in edges), "medium_high_edges_after": sum(r["confidence_tier"] == "medium-high" for r in edges),
        "exportable_edges_after": sum(r["exportable"] == "true" for r in edges), "target_gene_edges_after": sum(r["pathway_name"] == "target_gene" for r in edges),
        "upstream_activation_inferred": False, "audit": str(AUDIT_PATH),
    }
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True); SUMMARY_PATH.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2)); return 0


if __name__ == "__main__":
    raise SystemExit(main())
