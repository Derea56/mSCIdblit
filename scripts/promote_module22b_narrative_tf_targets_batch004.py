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
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch004.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch004_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch004-2026-09-03"

UPDATES = [
    ("M22B-E000185", "FOXO1", "G6PC", "human", "PMID:23995837", "Human hepatic cells with TRbeta-dependent FoxO1 promoter occupancy and transcription assays; non-SCI comparator.", "Primary experiments showed FoxO1 recruitment to the G6PC promoter and FoxO1-dependent thyroid-hormone activation of G6PC transcription.", "The effect is cooperative with TRbeta and SIRT1 and is hepatic/hormone-context dependent; the reviewed FGF15-FGFR4 handoff and SCI activation are not established."),
    ("M22B-E000185", "FOXO1", "PCK1", "human", "PMID:23995837", "Human hepatic cells with TRbeta-dependent FoxO1 promoter occupancy and transcription assays; non-SCI comparator.", "Primary experiments showed FoxO1 recruitment to the PCK1 promoter and FoxO1-dependent thyroid-hormone activation of PCK1 transcription.", "The effect is cooperative with TRbeta and SIRT1 and is hepatic/hormone-context dependent; the reviewed FGF15-FGFR4 handoff and SCI activation are not established."),
    ("M22B-E000323;M22B-E000324;M22B-E000325;M22B-E000326;M22B-E000327;M22B-E000328", "RELA", "IL6", "human", "PMID:8234276; PMCID:PMC47740", "Human inflammatory-cell promoter-reporter experiments identifying RelA/p65 activity at the IL6 promoter; non-SCI comparator.", "Primary promoter-mutagenesis and cotransfection experiments showed the NF-kappaB p65/RelA subunit cooperates at the human IL6 promoter and is required for strong promoter activation with NF-IL6.", "Activation is cooperative with NF-IL6 and stimulus-dependent; it does not establish any reviewed ECM/TLR/AXL handoff or SCI-specific RelA activation."),
    ("M22B-E000342", "RUNX2", "ATF6", "mouse", "PMID:22102412; PMCID:PMC3256879", "Mouse osteoblast BMP2/Runx2 promoter and ChIP experiments; non-SCI comparator.", "Primary osteoblast experiments showed BMP2-enhanced Runx2 binding to an OSE2 motif in the Atf6 promoter and Runx2-dependent Atf6 transcription.", "The bone/BMP2 model is lineage-specific and stimulus-dependent; it does not establish the reviewed EDIL3-ITGB3 handoff or SCI-specific Runx2 activation."),
    ("M22B-E000191;M22B-E000192", "GLI1", "PTCH1", "human", "PMID:16229683", "Human HEK293 promoter-reporter experiments with GLI1 activation of a Patched-family promoter; non-SCI comparator.", "Primary reporter experiments showed GLI1 activates a PTCH-family promoter through GLI response elements, with PTCH1 modulating the response.", "The assay uses a PTCH2 promoter reporter and GLI consensus elements rather than the reviewed SCUBE2/HHIP handoffs; exact receptor activation and SCI transfer are not established."),
    ("M22B-E000278", "NFATC1", "Il2", "mouse", "PMID:28894104; PMCID:PMC5593830", "Mouse activated CD8 T cells with NFATc1 ChIP-seq, transcriptome, and loss-of-function assays; non-SCI comparator.", "Primary CD8 T-cell experiments identified Il2 as a direct NFATc1-associated target with promoter-proximal occupancy and reduced expression after Nfatc1 loss.", "NFATc1 overlaps with NFATc2 and the response is T-cell activation dependent; this does not establish the reviewed SEMA6A-PLXNA2 handoff or SCI activation."),
    ("M22B-E000249", "NANOG", "ZFP42", "mouse", "PMID:16714766", "Mouse embryonic-stem-cell and P19 pluripotency models with Nanog promoter-reporter and knockdown assays; non-SCI comparator.", "Nanog directly transactivated the Rex-1/Zfp42 promoter, and Nanog knockdown reduced endogenous Rex-1 expression; Sox2 augmented the response.", "The pluripotency model is cooperative with Sox2/Oct4 and does not establish the reviewed EFNA4-EPHA10 handoff or SCI activation."),
    ("M22B-E000401", "SOX2", "ZFP42", "mouse", "PMID:16714766", "Mouse embryonic-stem-cell and P19 pluripotency models with Sox2/Nanog promoter-reporter assays; non-SCI comparator.", "Sox2 transactivated the Rex-1/Zfp42 promoter and cooperated with Nanog in the primary promoter assays.", "The effect is cooperative with Nanog and Oct4 and does not establish the reviewed ECM1-ITGB4 handoff or SCI activation."),
    ("M22B-E000401", "SOX2", "NANOG", "human", "PMID:15860457", "Human and mouse embryonic-stem-cell promoter, binding, and knockdown experiments; non-SCI comparator.", "Primary experiments identified a conserved Sox2/Oct4 composite element in the NANOG promoter, confirmed Sox2 occupancy by ChIP, and linked Sox2 depletion to reduced NANOG expression.", "The direct activation is a Sox2-Oct4 cooperative mechanism and does not establish the reviewed ECM1-ITGB4 handoff or SCI activation."),
    ("M22B-E000467", "TBX21", "Ifng", "mouse", "PMID:28623086", "Mouse CD4 T-cell Th1 differentiation with T-bet ChIP-seq and genotype-dependent expression; non-SCI comparator.", "Primary Th1 experiments identified Ifng as a T-bet/TBX21-activated direct target with T-bet binding and reduced expression in Tbx21-deficient cells.", "The target is T-cell and cytokine-context dependent and does not establish the reviewed SEMA4A-PLXND1 handoff or SCI activation."),
    ("M22B-E000485", "YAP", "CTGF", "human", "PMID:18579750", "Human MCF10A epithelial cells with endogenous YAP ChIP, CTGF promoter reporter, and TEAD perturbation; non-SCI comparator.", "Primary genome-wide occupancy and promoter assays identified CTGF as a direct YAP target, with YAP and TEAD1 binding the CTGF promoter and TEAD required for YAP-dependent activation.", "YAP activation is TEAD/cofactor dependent and cell-context specific; it does not establish the reviewed SEMA3G-NRP2/PLXNA1 handoff or SCI activation."),
    ("M22B-E000464;M22B-E000485", "TEAD", "CTGF", "human", "PMID:18579750", "Human MCF10A epithelial cells with TEAD1 ChIP and CTGF promoter reporter/perturbation assays; non-SCI comparator.", "Primary assays showed TEAD1 occupancy at the CTGF promoter and TEAD-dependent activation of the YAP-responsive CTGF promoter.", "TEAD acts with YAP and the response is cell-context dependent; this does not establish the reviewed LAMA5/TAZ or SEMA3G/YAP handoffs or SCI activation."),
    ("M22B-E004148;M22B-E000478;M22B-E000479;M22B-E000480", "TCF4", "GLI1", "human", "PMID:30186446", "Human fibroblast Wnt3a stimulation with TCF4 promoter occupancy and reporter assays; TCF4 denotes the TCF7L2 alias; non-SCI comparator.", "Primary experiments showed a beta-catenin/TCF4 complex binds the human GLI1 promoter and activates GLI1 transcription after Wnt3a stimulation.", "The edge is TCF7L2/TCF4-alias and beta-catenin dependent; it does not establish the reviewed Wnt1-CD36 or RSPO/SOST handoffs or SCI activation."),
    ("M22B-E004148;M22B-E000478;M22B-E000479;M22B-E000480", "TCF4", "SMO", "human", "PMID:30186446", "Human fibroblast Wnt3a stimulation with TCF4 promoter occupancy and reporter assays; TCF4 denotes the TCF7L2 alias; non-SCI comparator.", "Primary experiments showed a beta-catenin/TCF4 complex binds the human SMO promoter and activates SMO transcription after Wnt3a stimulation.", "The edge is TCF7L2/TCF4-alias and beta-catenin dependent; it does not establish the reviewed Wnt1-CD36 or RSPO/SOST handoffs or SCI activation."),
    ("M22B-E000127;M22B-E000128;M22B-E000129;M22B-E000274", "NFAT", "IL2", "human", "PMID:7565783; PMCID:PMC230882", "Human T-cell promoter studies with NFAT/AP-1 footprinting, binding, and reporter assays; family-level non-SCI comparator.", "Primary promoter studies identified multiple NFAT sites required for full T-cell-receptor-induced IL2 promoter activity, with NFAT/AP-1 composite elements demonstrated by footprinting and reporter assays.", "This is a family-level NFAT/AP-1 promoter claim rather than a single NFAT paralog assignment; it does not establish the reviewed FGF/GABA handoffs or SCI activation."),
    ("M22B-E000114;M22B-E000115;M22B-E000116;M22B-E000117;M22B-E000118;M22B-E000119;M22B-E000120;M22B-E000121", "CREB", "BDNF", "human", "PMID:31915257", "Primary rat cortical-neuron CREB/CBP and conserved human BDNF-promoter reporter experiments; CREB-family comparator, not SCI-specific.", "Primary neuronal experiments showed CREB binds BDNF promoter IV and activates its transcription through CBP; complementary reporter assays indicated conservation of the regulatory response in the human BDNF promoter.", "The direct occupancy experiment is in rat cortical neurons and CREB-family activity is cofactor/stimulus dependent; the reviewed receptor handoffs and SCI activation are not established."),
]


def next_id(rows: list[dict[str, str]], field: str) -> int:
    return max([int(m.group(1)) for row in rows if (m := re.search(r"(\d+)$", row[field]))] or [0]) + 1


def main() -> int:
    edges, evidence = read_tsv(EDGE_PATH), read_tsv(EVIDENCE_PATH)
    existing = {(r.get("species_context", "").casefold(), r.get("source_entity", "").casefold(), r.get("target_entity", "").casefold()) for r in edges if r.get("pathway_name") == "target_gene"}
    edge_number, evidence_number = next_id(edges, "b_edge_id"), next_id(evidence, "b_evidence_id")
    audit = []
    for i, (holds, tf, target, species, locator, context, summary, limitations) in enumerate(UPDATES, start=26):
        pair = (species.casefold(), tf.casefold(), target.casefold())
        if pair in existing:
            raise SystemExit(f"target pair already exists: {pair}")
        edge_id, evidence_id = f"M22B-E{edge_number:06d}", f"M22B-EVID-{evidence_number:06d}"
        edge_number += 1; evidence_number += 1
        edges.append({"b_edge_id": edge_id, "source_entity": tf, "relation_type": f"{tf} activates the {target} target gene in primary-study evidence", "target_entity": target, "pathway_name": "target_gene", "evidence_layer": "ligand_receptor_or_direct_molecular", "source_a_edge_id": f"M22B-TARGET-SEARCH-{i:04d}", "edge_status": "reviewed_direct_target", "context_scope": context, "cell_type_context": context, "compartment_context": "unspecified", "species_context": species, "injury_context": "not_assessed", "confidence_tier": "high", "export_priority": "medium", "exportable": "true", "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing {holds}; upstream handoff remains separate and unupgraded."})
        evidence.append({"b_evidence_id": evidence_id, "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-{i:04d}", "b_edge_ids": edge_id, "source_kind": "reviewed_direct_target", "source_locator": locator, "support_kind": "primary_experiment", "species_support": species, "source_scope": "direct_edge", "confidence_tier": "high", "citation_note": f"Primary-study target-gene evidence identified while reviewing hold rows {holds}; standalone general TF-regulon claim.", "evidence_summary": summary, "limitations": limitations, "evidence_layer": "ligand_receptor_or_direct_molecular", "exportable": "true", "consolidation_note": f"{BATCH_ID}: primary-study target-gene evidence; upstream handoff remains separate and unupgraded."})
        audit.append({"batch_id": BATCH_ID, "hold_edges_reviewed": holds, "tf": tf, "target": target, "species": species, "b_edge_id": edge_id, "b_evidence_id": evidence_id, "source_locator": locator, "upstream_handoff_upgraded": "false", "standalone_target_gene_edge": "true", "decision_basis": summary})
        existing.add(pair)
    fields = ["batch_id", "hold_edges_reviewed", "tf", "target", "species", "b_edge_id", "b_evidence_id", "source_locator", "upstream_handoff_upgraded", "standalone_target_gene_edge", "decision_basis"]
    write_tsv(AUDIT_PATH, audit, fields); write_tsv(EDGE_PATH, edges, EDGE_FIELDS); write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    summary = {"batch_id": BATCH_ID, "standalone_target_gene_edges_added": len(audit), "upstream_handoff_edges_upgraded": 0, "high_edges_after": sum(r["confidence_tier"] == "high" for r in edges), "exportable_edges_after": sum(r["exportable"] == "true" for r in edges), "target_gene_edges_after": sum(r["pathway_name"] == "target_gene" for r in edges), "upstream_activation_inferred": False, "audit": str(AUDIT_PATH)}
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True); SUMMARY_PATH.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8"); print(json.dumps(summary, indent=2)); return 0


if __name__ == "__main__":
    raise SystemExit(main())
