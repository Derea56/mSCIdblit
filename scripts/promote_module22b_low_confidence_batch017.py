#!/usr/bin/env python3
"""Promote exact receptor-function boundaries to bounded program records."""
import csv, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
EDGE_PATH=ROOT/"work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH=ROOT/"work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH=ROOT/"work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch017.tsv"
SUMMARY_PATH=ROOT/"work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch017_summary.json"
BATCH_ID="module22b-low-confidence-upgrade-batch017-2026-09-03"

U={
"M22B-E005646":("M22B-EVID-004902","SEMA4D","SEMA4D engages CD72 and releases CD72-associated inhibitory SHP-1 to tune immune receptor signaling; no terminal TF-target regulation is assigned","SEMA4D-CD72 -> inhibitory immune-signaling program","PMID:16113236; PMID:17244710","mouse; human comparator","Primary immune studies support SEMA4D engagement of CD72 and relief of CD72-associated inhibitory phosphatase signaling with receptor-dependent immune outputs. This recovers an exact receptor-proximal program, but not a terminal TF.","CD72 phosphorylation, BCR or platelet activation context, and immune-cell state constrain the relay; no terminal TF occupancy or SCI receiver program was measured."),
"M22B-E005647":("M22B-EVID-004931","SERPINF1","PEDF binds PLXDC1, alters receptor oligomerization, and supports PLXDC1-dependent cell responses; no terminal TF-target regulation is assigned","SERPINF1/PEDF-PLXDC1 -> atypical receptor response program","PMID:25535841; PMCID:PMC4303762; DOI:10.7554/eLife.05401","mouse; human cell systems","Primary binding and cell-based studies support PEDF engagement of PLXDC1, receptor oligomerization changes, and PLXDC1-dependent cellular responses. This recovers an exact atypical-receptor function program, but not a universal kinase or terminal TF.","PLXDC1 is an atypical receptor with cell-type-specific outputs and no established canonical kinase; no terminal TF occupancy or SCI receiver program was measured."),
"M22B-E005663":("M22B-EVID-005060","TGFB1","TGFB1 engages the canonical TGFBR1/TGFBR2 receptor complex and initiates receptor-proximal signaling; no terminal TF-target regulation is assigned","TGFB1-TGFBR1/TGFBR2 -> canonical TGF-beta signaling program","PMID:7693660; PMID:1700790; PMID:40011426","mouse; human","Primary biochemical and receptor studies support TGFB1 engagement of the canonical TGFBR1/TGFBR2 heteromeric complex and receptor-proximal signaling. This recovers an exact ligand-receptor program, but not a terminal TF target locus.","Receptor stoichiometry and betaglycan/endoglin contributions vary by cell and assay; no SCI-specific terminal TF endpoint was measured."),
"M22B-E005664":("M22B-EVID-005066","TGFB2","TGFB2 engages the TGFBR1/TGFBR2 receptor complex, with betaglycan often contributing to ligand capture; no terminal TF-target regulation is assigned","TGFB2-TGFBR1/TGFBR2 -> canonical TGF-beta signaling program","PMID:7693660; PMID:1700790; PMID:40011426","mouse; human","Primary receptor studies support TGFB2 signaling through the TGFBR1/TGFBR2 complex and identify accessory betaglycan contributions to ligand capture. This recovers an exact ligand-receptor program, but not a terminal TF target locus.","TGFB2 affinity, TGFBR3 dependence, receptor stoichiometry, and cellular potency are context dependent; no SCI-specific terminal TF endpoint was measured."),
"M22B-E005665":("M22B-EVID-005076","TGFB3","TGFB3 engages the canonical TGFBR1/TGFBR2 signaling complex; no terminal TF-target regulation is assigned","TGFB3-TGFBR1/TGFBR2 -> canonical TGF-beta signaling program","PMID:1700790; PMID:7693660; PMID:40011426","mouse; human","Primary ligand-receptor studies support TGFB3 engagement of the canonical TGFBR1/TGFBR2 signaling complex. This recovers an exact ligand-receptor program, but not a terminal TF target locus.","Isoform affinity and receptor stoichiometry vary by cell context; no SCI-specific terminal TF endpoint was measured."),
}
EF=["b_edge_id","source_entity","relation_type","target_entity","pathway_name","evidence_layer","source_a_edge_id","edge_status","context_scope","cell_type_context","compartment_context","species_context","injury_context","confidence_tier","export_priority","exportable","consolidation_note"]
VF=["b_evidence_id","source_a_evidence_id","b_edge_ids","source_kind","source_locator","support_kind","species_support","source_scope","confidence_tier","citation_note","evidence_summary","limitations","evidence_layer","exportable","consolidation_note"]
AF=["batch_id","b_edge_id","b_evidence_id","old_edge_confidence","new_edge_confidence","old_evidence_confidence","new_evidence_confidence","old_target","new_target","old_edge_status","new_edge_status","decision_basis","source_locator","module22b_register_changed","canonical_sql_materialization"]
def rd(p):
    with p.open(newline="",encoding="utf-8") as h:return list(csv.DictReader(h,delimiter="\t"))
def wr(p,rows,fields):
    with p.open("w",newline="",encoding="utf-8") as h:
        w=csv.DictWriter(h,fieldnames=fields,delimiter="\t",lineterminator="\n");w.writeheader();w.writerows(rows)
def once(v,x):return v if x in v else (f"{v}; {x}" if v else x)
def main():
    edges,evidence=rd(EDGE_PATH),rd(EVIDENCE_PATH); eb={r["b_edge_id"]:r for r in edges}; vb={r["b_evidence_id"]:r for r in evidence}; audit=[]
    for eid,c in U.items():
        vid,src,rel,tgt,loc,species,basis,scope=c; e,v=eb.get(eid),vb.get(vid)
        if e is None or v is None:raise SystemExit(f"missing batch017 row for {eid}")
        if e["confidence_tier"]!="low" or e["edge_status"]!="no_evidence_boundary":raise SystemExit(f"{eid}: expected low boundary")
        if v["source_kind"]!="no_evidence_boundary" or v["support_kind"]!="negative_evidence":raise SystemExit(f"{eid}: expected boundary evidence")
        oldt,olds,olde,oldv=e["target_entity"],e["edge_status"],e["confidence_tier"],v["confidence_tier"]
        e.update({"source_entity":src,"relation_type":rel,"target_entity":tgt,"pathway_name":"cell_state_program","edge_status":"reviewed_program_association","context_scope":scope,"confidence_tier":"medium","exportable":"true"})
        e["consolidation_note"]=once(e["consolidation_note"],f"Low-confidence recovery batch017: medium after exact primary receptor/function re-review for {src}.")
        v.update({"source_kind":"reviewed_program_association","source_locator":loc,"support_kind":"primary_experiment","species_support":species,"source_scope":"contextual_support","confidence_tier":"high","evidence_summary":basis,"limitations":scope,"evidence_layer":"downstream_or_functional","exportable":"true"})
        v["consolidation_note"]=once(v["consolidation_note"],"Low-confidence recovery batch017: exact primary receptor-complex/function evidence recovered; terminal TF claim remains excluded.")
        audit.append({"batch_id":BATCH_ID,"b_edge_id":eid,"b_evidence_id":vid,"old_edge_confidence":olde,"new_edge_confidence":e["confidence_tier"],"old_evidence_confidence":oldv,"new_evidence_confidence":v["confidence_tier"],"old_target":oldt,"new_target":tgt,"old_edge_status":olds,"new_edge_status":e["edge_status"],"decision_basis":basis,"source_locator":loc,"module22b_register_changed":"true","canonical_sql_materialization":"false"})
    wr(EDGE_PATH,edges,EF);wr(EVIDENCE_PATH,evidence,VF);AUDIT_PATH.parent.mkdir(parents=True,exist_ok=True);wr(AUDIT_PATH,audit,AF)
    counts={"batch_id":BATCH_ID,"records_upgraded":len(audit),"medium_edge_upgrades":len(audit),"recovered_boundary_edges":len(audit),"low_edges_after":sum(r["confidence_tier"]=="low" for r in edges),"low_medium_edges_after":sum(r["confidence_tier"]=="low-medium" for r in edges),"medium_edges_after":sum(r["confidence_tier"]=="medium" for r in edges),"medium_high_edges_after":sum(r["confidence_tier"]=="medium-high" for r in edges),"high_edges_after":sum(r["confidence_tier"]=="high" for r in edges),"exportable_edges_after":sum(r["exportable"]=="true" for r in edges),"canonical_sql_materialization":False,"audit":str(AUDIT_PATH)}
    SUMMARY_PATH.write_text(json.dumps(counts,indent=2)+"\n",encoding="utf-8");print(json.dumps(counts,indent=2))
if __name__=="__main__":main()
