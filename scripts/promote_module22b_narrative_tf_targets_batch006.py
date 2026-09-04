#!/usr/bin/env python3
"""Stage uncovered named/composite TF target edges from primary studies."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch006.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch006_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch006-2026-09-03"

UPDATES = [
    ("M22B-E000005;M22B-E000006", "AP-1", "CXCL8", "human", "PMID:12209633", "Human arterial endothelial cells with AP-1-dependent IL-8/CXCL8 promoter activation and AP-1-site mutagenesis; non-SCI comparator.", "Primary promoter studies showed that AP-1 induction increased human IL-8/CXCL8 transcription and that mutation of the AP-1 site abolished the promoter response.", "The family-level edge is stimulus-dependent and does not assign a unique JUN/FOS paralog; this does not establish the reviewed 2-AG-CB1/CB2 handoff or SCI activation."),
    ("M22B-E000005;M22B-E000006", "AP-1", "MMP1", "human", "PMID:16707434", "Human gastric epithelial/cancer samples and cells with c-Fos/c-Jun AP-1 occupancy at the MMP1 promoter during H. pylori stimulation; non-SCI comparator.", "Primary binding and promoter studies showed c-Fos and c-Jun occupancy at AP-1 sites in the human MMP1 promoter during stimulation and linked AP-1-site activity to MMP1 induction.", "The family-level edge represents cooperative c-Fos/c-Jun activity and infection-dependent regulation; this does not establish the reviewed 2-AG-CB1/CB2 handoff or SCI activation."),
    ("M22B-E000200", "HHEX", "CDKN1A", "human", "PMID:34595169; PMCID:PMC8476888", "Human HCT116 tumor-cell and HEK293T promoter assays with HHEX ChIP and CDKN1A promoter reporter activation; non-SCI comparator.", "Primary experiments showed HHEX binding to the human CDKN1A promoter and activation of an 898-bp CDKN1A promoter reporter, consistent with increased CDKN1A transcription after HHEX expression.", "HHEX also represses other targets, and this activation is cancer/differentiation-context dependent; it does not establish the reviewed PTPN14 handoff or SCI activation."),
    ("M22B-E000281", "NFATC3", "CCL5", "human", "PMID:31903118", "Human rheumatoid-arthritis synovial fibroblasts with NFATc3 ChIP-qPCR, promoter reporter, and knockdown assays; inflammatory non-SCI comparator.", "Primary experiments showed NFATc3 binding to the human CCL5/RANTES promoter and NFATc3-dependent promoter activity and CCL5 expression.", "The response is calcium/ionomycin and inflammatory-cell-context dependent; this does not establish the reviewed ASIC1A handoff or SCI activation."),
    ("M22B-E000301", "RARA;RXRA", "RARB", "mouse", "PMID:11839811", "Mouse P19 embryonal-carcinoma cells with RAR/RXR ligand-dependent mRARbeta2 promoter reporter and chromatin-promoter assays; non-SCI comparator.", "Primary promoter experiments showed cooperative RAR/RXR activation of the mouse Rarb beta2 promoter in response to retinoid ligands.", "The evidence supports the cooperative RAR/RXR complex rather than a single RAR or RXR paralog and is embryonal-retinoid-context dependent; it does not establish the reviewed CRABP2-RARA/RXRA handoff or SCI activation."),
    ("M22B-E000482", "THRB", "LDLR", "human", "PMID:24558356; PMCID:PMC3928038", "Human HepG2 cells expressing TRbeta with T3-dependent expression and TRbeta occupancy assays; hepatic non-SCI comparator.", "Primary BioChIP/ChIP and expression experiments identified LDLR as a direct human TRbeta-associated T3-induced target, with increased LDLR transcript and protein in TRbeta-expressing cells.", "The response is T3/TRbeta/RXRA-context dependent and hepatic; it does not establish the reviewed THRB handoff or SCI activation."),
    ("M22B-E000482", "THRB", "BCL3", "human", "PMID:24558356; PMCID:PMC3928038", "Human HepG2 cells expressing TRbeta with T3-dependent expression and TRbeta occupancy assays; hepatic non-SCI comparator.", "Primary BioChIP/ChIP and expression experiments identified BCL3 as a direct human TRbeta-associated T3-induced target.", "The response is T3/TRbeta/RXRA-context dependent and hepatic; it does not establish the reviewed THRB handoff or SCI activation."),
    ("M22B-E000482", "THRB", "NCOR2", "human", "PMID:24558356; PMCID:PMC3928038", "Human HepG2 cells expressing TRbeta with T3-dependent expression and TRbeta occupancy assays; hepatic non-SCI comparator.", "Primary BioChIP/ChIP and expression experiments identified NCOR2 as a TRbeta-bound locus associated with T3-induced transcription.", "The response is T3/TRbeta/RXRA-context dependent and hepatic; it does not establish the reviewed THRB handoff or SCI activation."),
    ("M22B-E000482", "THRB", "ADSSL1", "human", "PMID:24558356; PMCID:PMC3928038", "Human HepG2 cells expressing TRbeta with T3-dependent expression and TRbeta occupancy assays; hepatic non-SCI comparator.", "Primary BioChIP/ChIP and expression experiments identified ADSSL1 as a TRbeta-bound locus associated with T3-induced transcription.", "The response is T3/TRbeta/RXRA-context dependent and hepatic; it does not establish the reviewed THRB handoff or SCI activation."),
    ("M22B-E000482", "THRB", "SOX7", "human", "PMID:24558356; PMCID:PMC3928038", "Human HepG2 cells expressing TRbeta with T3-dependent expression and TRbeta occupancy assays; hepatic non-SCI comparator.", "Primary BioChIP/ChIP and expression experiments identified SOX7 as a TRbeta-bound locus associated with T3-induced transcription.", "The response is T3/TRbeta/RXRA-context dependent and hepatic; it does not establish the reviewed THRB handoff or SCI activation."),
    ("M22B-E000482", "THRB", "ADM", "human", "PMID:24558356; PMCID:PMC3928038", "Human HepG2 cells expressing TRbeta with TRbeta ChIP, T3-dependent expression, EMSA, and ADM promoter reporter assays; hepatic non-SCI comparator.", "Primary experiments showed TRbeta binding to the human ADM promoter, T3-dependent ADM transcription, and ADM promoter elements that conferred TRbeta/T3 responsiveness in reporter assays.", "The response is T3/TRbeta/RXRA-context dependent and hepatic; it does not establish the reviewed THRB handoff or SCI activation."),
]


def next_id(rows: list[dict[str, str]], field: str) -> int:
    return max([int(m.group(1)) for row in rows if (m := re.search(r"(\d+)$", row[field]))] or [0]) + 1


def main() -> int:
    edges, evidence = read_tsv(EDGE_PATH), read_tsv(EVIDENCE_PATH)
    existing = {(r.get("species_context", "").casefold(), r.get("source_entity", "").casefold(), r.get("target_entity", "").casefold()) for r in edges if r.get("pathway_name") == "target_gene"}
    edge_number, evidence_number = next_id(edges, "b_edge_id"), next_id(evidence, "b_evidence_id")
    audit = []
    for i, (holds, tf, target, species, locator, context, summary, limitations) in enumerate(UPDATES, start=51):
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
