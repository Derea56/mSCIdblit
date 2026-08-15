#!/usr/bin/env python3
"""Integrate the first four read-only Module 20A pair reviews into audit scaffolds.

This writes only pair-level audit inventories and a reusable-evidence register.
It deliberately does not materialize new main Module 21A graph edges.
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELAY = ROOT / "work" / "module21_relay"
PAIR = RELAY / "module21a_all_pair_relay_coverage.tsv"
TF = RELAY / "module22a_ligand_tf_handoff.tsv"
REUSE = RELAY / "module21a_pathway_reuse_registry.tsv"
EVIDENCE = RELAY / "module21a_pair_relay_evidence_register.tsv"
REVIEW = RELAY / "module21a_pair_relay_review_batch001.tsv"


def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def ext(n: int) -> str:
    return f"M20A-EXT-{n:04d}"


def cell(n: int) -> str:
    return f"M20A-CELLCHAT-REMAINING-{n:04d}"


def main() -> None:
    pair_rows = read(PAIR)
    tf_rows = read(TF)
    reuse_rows = read(REUSE)
    pair_by_review = {r["module20a_review_id"]: r for r in pair_rows}
    tf_by_review = {r["pair_key"]: r for r in tf_rows}

    specs = {
        "bdnf_sort1": ("BDNF/proBDNF-p75NTR-SORT1 apoptotic branch", "PMID:15930396; PMID:31223654", "rat sympathetic neurons; mouse neuropathic-pain model", "downstream_pathway_function", "medium", "ProBDNF versus mature BDNF and p75NTR scope require explicit separation.", "no terminal TF endpoint"),
        "ackr2_scavenging": ("ACKR2 chemokine internalization/scavenging", "PMID:39903605; PMCID:PMC12017343; PMID:24890717", "human and mouse ACKR2-expressing HEK293T and mouse leukocyte uptake systems", "downstream_pathway_function", "medium", "Scavenging/availability control is not canonical G-protein signaling and does not establish a TF endpoint.", "no terminal TF endpoint"),
        "ccr2_gi_pi3k_erk": ("CCL2-CCR2-Gi/PI3K/ERK chemotaxis branch", "PMID:24890717; PMID:19906300", "mouse leukocytes and mouse EAE monocyte-trafficking model", "receptor_proximal_relay", "high", "No pair-specific TF-target program or SCI receiver relay was established.", "no terminal TF endpoint"),
        "ackr4_scavenging": ("ACKR4 chemokine scavenging/internalization branch", "PMID:23341447; PMID:32289156; PMID:26976955; PMID:33875601; PMCID:PMC7188906", "human receptor assays and mouse ACKR4 loss-of-function/barrier-tissue models", "receptor_proximal_relay", "medium", "GRK3/beta-arrestin trafficking and chemokine-gradient control do not establish canonical Gi signaling or a TF endpoint.", "no terminal TF endpoint"),
        "ccr10_gi": ("CCL27-CCR10-Gi/Ca2+/chemotaxis branch", "PMID:10725697; PMID:14581607; PMID:35663027", "human CCR10 transfectants and mouse melanoma/skin models", "receptor_proximal_relay", "medium", "Mouse Ccl27b paralog was not isolated and no terminal TF program was demonstrated.", "no terminal TF endpoint"),
        "slit_robo_guidance": ("Slit-Robo-CC0-srGAP-Rac/Rho actin-guidance branch", "PMID:10433822; PMID:10102268; PMID:17360927; PMID:18417704", "mouse developmental binding, genetics, and repulsion assays", "receptor_proximal_relay", "high", "Canonical guidance relay is supported, but no terminal TF endpoint or SCI receiver weighting was established.", "no terminal TF endpoint"),
        "slitrk_ptprs": ("SLITRK-PTPRS synaptogenic adhesion/scaffold branch", "PMID:23345436; PMCID:PMC3593915; PMID:29934346; PMCID:PMC6705959", "rat neurons and heterologous synapse assays", "downstream_pathway_function", "medium", "Synapse assembly is a functional/scaffold output; no terminal TF endpoint.", "no terminal TF endpoint"),
        "wnt5a_mcam_jnk": ("WNT5A-MCAM/CD146-DVL2-JNK branch", "PMID:24335906; PMID:33462195", "human cells, zebrafish embryos, and mouse/human renal models", "receptor_proximal_relay", "high", "JUN/AP-1 is a candidate only; target-program evidence remains deferred to Module22A.", "candidate TF only"),
        "activin_alk4": ("Activin-ACVR2A/B-ALK4-SMAD2/3-SMAD4 branch", "PMID:26001835; PMID:15475360; PMID:8622651", "human granulosa cells and heterologous/cell-free receptor systems", "receptor_proximal_relay", "medium", "Exact ligand plus four-part receptor complex was not isolated in one assay.", "candidate TF only"),
        "activin_alk7": ("Activin-ACVR2A/B-ALK7-SMAD2/3-SMAD4 branch", "PMID:18951876; PMID:32235336; PMID:15475360", "human beta-cell, myeloma/HepG2, and cell-free receptor systems", "receptor_proximal_relay", "medium", "ACVR2A/B partner identity is not uniquely resolved in the ALK7 assays; PDX1 is model-specific.", "candidate TF only"),
        "amh_bmpr1b": ("AMH-AMHR2/BMPR1B-SMAD1/5 branch", "PMID:10854429; PMCID:PMC6620045", "mouse receptor co-IP, reporter, pSMAD, and neuronal migration assays", "receptor_proximal_relay", "high", "No target-program claim and no SCI receiver weighting.", "candidate TF only"),
        "areg_egfr": ("AREG-EGFR-ERK/MAPK branch", "PMID:10085134; PMID:41085543", "human EGFR-engineered fibroblasts and human/mouse bile-duct organoids/injury model", "receptor_proximal_relay", "medium", "Relay and functional models differ; ELK1 is a candidate, not an exact organoid endpoint.", "candidate TF only"),
        "areg_erbb2": ("AREG-EGFR-mediated ERBB2 transphosphorylation branch", "PMID:10085134", "human epithelial cells and EGFR-engineered fibroblasts", "receptor_proximal_relay", "medium", "EGFR mediates the ligand response; direct AREG-ERBB2 binding and TF endpoint are not established.", "candidate TF only"),
        "artn_gfra3_ret": ("ARTN-GFRA3-RET-ERK/PI3K-AKT branch", "PMID:9883723; PMID:25635057; DOI:10.1038/nchembio823", "mouse neuronal cultures and receptor-complex assays", "receptor_proximal_relay", "medium", "No exact terminal TF assay; ELK1/AP-1 are generic candidates only.", "candidate TF only"),
        "bdnf_trkb": ("BDNF-TrkB-Shc/RAS/ERK, PI3K/AKT, PLCgamma-CREB branch", "PMID:9312147; PMCID:PMC3230766; PMID:16034442", "mouse cortical neurons and rat amygdala with receptor inhibition and pERK/pCREB assays", "receptor_proximal_relay", "high", "Mature versus proBDNF and TrkB isoform scope remain limitations; CREB phosphorylation is a terminal TF activation signal, not a target program.", "supported TF activation"),
        "bmp10_acvr2a": ("BMP10-ACVRL1/ALK1-SMAD1/5/9 branch with ACVR2A binding", "PMID:22718755", "human recombinant receptor ectodomain SPR/thermodynamics", "ligand_receptor_binding_or_activation", "low", "ACVR2A binding is shown but exact ternary cellular signaling is not established.", "candidate TF only"),
        "bmp10_bmpr2": ("BMP10-ACVRL1/ALK1-BMPR2-SMAD1/5/9 branch", "PMID:35504921; PMCID:PMC9064986", "human recombinant structural system and separate zebrafish endothelial ALK1 signaling", "receptor_proximal_relay", "medium", "Structural ternary evidence and family relay are not a matched cell-level TF assay.", "candidate TF only"),
        "bmp15_bmpr1b": ("BMP15-BMPR2/BMPR1B-SMAD1/5/8-SMAD4 branch", "PMID:22294741", "human granulosa-luteal/COV434 and COS receptor-complex/pSMAD assays", "receptor_proximal_relay", "high", "Inhibin-B downstream program belongs to Module22A and is not included here.", "candidate TF only"),
        "bmp2_bmpr1a_acvr2a": ("BMP2-ACVR2A-BMPR1A/ALK3-SMAD1/5/8 branch", "PMCID:PMC8855587", "human U2OS/COS7 receptor competition, FRAP, siRNA, and pSMAD assays", "receptor_proximal_relay", "medium", "Not SCI-specific and no target-program endpoint.", "candidate TF only"),
        "bmp2_bmpr1a_bmpr2": ("BMP2-BMPR2/BMPR1A/ALK3-SMAD1/5 branch", "PMID:19211807; PMID:17989347", "mouse LbetaT2 and human vascular cells with receptor perturbation/pSMAD assays", "receptor_proximal_relay", "medium", "Fshb and other target programs belong to Module22A.", "candidate TF only"),
        "bmp2_bmpr1b_bmpr2": ("BMP2-BMPR2/BMPR1B-SMAD1/5 branch", "PMID:21471205; PMID:19211807", "COS7 live-cell FRAP/pSMAD and mouse LbetaT2 functional assays", "receptor_proximal_relay", "medium", "Target-program endpoints remain deferred.", "candidate TF only"),
        "bmp4_bmpr1a_bmpr2": ("BMP4-BMPR2/BMPR1A-SMAD1/5 branch", "PMID:17989347", "human pulmonary vascular cells with receptor siRNA and pSMAD assays", "receptor_proximal_relay", "medium", "Model-specific; no terminal TF target program.", "candidate TF only"),
        "bmp5_ligand_smad": ("BMP5 ligand-level SMAD1/5/8 and p38 branch", "PMID:17541940; PMID:28925352", "rat primary chondrocytes and chicken spinal cord", "downstream_pathway_function", "low", "No receptor-complex perturbation; exact queued receptor pair is unresolved.", "candidate TF only"),
        "bmp6_bmpr": ("BMP6 receptor-utilization-SMAD1/5/8 branch", "PMID:18436533; PMCID:PMC3258927", "human bone-marrow MSC receptor RNAi/co-expression and differentiation assays", "receptor_proximal_relay", "medium", "BMPR1B and ACVR2B were weak/not significant in the matched model; no SCI context.", "candidate TF only"),
        "bmp7_bmpr": ("BMP7 receptor-utilization-SMAD1/5/8 branch", "PMID:18436533; PMCID:PMC3258927; PMID:7790373; PMCID:PMC2120513", "human MSC and receptor binding/reporter systems", "receptor_proximal_relay", "medium", "Exact pair support varies by receptor combination; binding-only rows remain unpromoted.", "candidate TF only"),
        "bmp8a_bmpr": ("BMP8A receptor-reconstituted-SMAD1/5/8 branch", "PMID:28465413; DOI:10.1126/scisignal.aal1910", "HEK293T receptor reconstitution/BRE-CAGA reporters and mouse spermatogonia", "receptor_proximal_relay", "medium", "Exact reporter support is stronger for ACVR2A/BMPR2 combinations; SMAD2/3 branch uses ALK5 and is not transferred.", "candidate TF only"),
        "bmp8b_ligand_smad": ("BMP8B ligand-level SMAD1/5/9 and SMAD2/3 branches", "PMID:32694734; PMCID:PMC7617436; PMCID:PMC10780770; PMCID:PMC9234707", "mouse hepatic stellate/3T3-L1/BAT systems and human NASH microtissues", "downstream_pathway_function", "low", "Exact ACVR/BMPR receptor complex is unresolved; do not transfer BMP8A receptor-complex evidence.", "candidate TF only"),
        "btc_egfr": ("BTC-EGFR/ERBB4 receptor activation with ERK/PI3K candidates", "PMID:8570211; DOI:10.1152/ajpcell.00436.2003", "mouse receptor-defined Ba/F3 and rat vascular smooth-muscle systems", "receptor_proximal_relay", "medium", "Pair-specific receptor activation, but no pair-specific TF assay; AP-1/ELK1 are generic candidates only.", "candidate TF only"),
        "btc_erbb4_structural": ("BTC-HER2/HER4 structural complex", "PMID:38498590; PMCID:PMC10948148", "human HER2/HER4 ectodomains, cryo-EM", "ligand_receptor_binding_or_activation", "low", "Structural receptor evidence only; intracellular relay and TF endpoint not measured.", "no terminal TF endpoint"),
        "btc_egfr_erbb2": ("BTC-EGFR/ERBB2 heterodimer ERK/AKT/p38 branch", "DOI:10.1152/ajpcell.00436.2003", "rat vascular smooth-muscle cells with receptor association/phosphorylation and kinase inhibitors", "receptor_proximal_relay", "medium", "TF-target evidence absent and branch is model-specific.", "candidate TF only"),
    }

    spec_key_to_id: dict[str, str] = {}
    next_reuse = 1 + max([int(r["pathway_reuse_key"].split("-")[-1]) for r in reuse_rows] or [0])
    for key in specs:
        spec_key_to_id[key] = f"M21A-REUSE-{next_reuse:04d}"
        next_reuse += 1

    outcomes: dict[str, tuple[str | None, str, str, str]] = {}

    def set_out(ids: list[str], spec: str | None, tf: str, status: str, note: str) -> None:
        evidence_id = f"M21A-PAIR-EVID-{list(specs).index(spec)+1:03d}" if spec else ""
        for review_id in ids:
            outcomes[review_id] = (spec, tf, status, note)

    set_out([ext(1)], "bdnf_sort1", "", "reviewed_relay_candidate", "Pair/form-specific proBDNF-p75NTR-SORT1 evidence; no TF endpoint.")
    set_out([ext(n) for n in [2, 9, 12]], None, "", "reviewed_no_downstream_evidence", "No qualifying exact-pair downstream evidence found.")
    set_out([ext(n) for n in [3, 4, 5, 8, 13]], "ackr2_scavenging", "", "reviewed_scavenging_only", "ACKR2 scavenging/internalization; no canonical intracellular relay or TF.")
    set_out([ext(6)], "ccr2_gi_pi3k_erk", "", "reviewed_relay_candidate", "Pair-specific canonical CCR2 pathway; no terminal TF evidence.")
    set_out([ext(n) for n in [7, 10]], "ackr4_scavenging", "", "reviewed_scavenging_only", "ACKR4 scavenging/internalization; exact paralog context is limited.")
    set_out([ext(11)], "ccr10_gi", "", "reviewed_relay_candidate", "CCR10 receptor relay; exact mouse Ccl27b and TF endpoint unresolved.")
    set_out([ext(14)], None, "", "reviewed_unresolved", "GDF15-TGFBR2 assignment is contested; do not use GDF15-GFRAL/RET evidence as a substitute.")
    set_out([ext(n) for n in [15, 16, 17]], "slit_robo_guidance", "", "reviewed_relay_candidate", "Slit-Robo guidance relay; no terminal TF evidence.")
    set_out([ext(n) for n in [18, 19, 20]], "slitrk_ptprs", "", "reviewed_function_only", "Synaptogenic adhesion/scaffold output; no terminal TF evidence.")
    set_out([ext(21)], "wnt5a_mcam_jnk", "JUN/AP-1 candidate", "reviewed_relay_candidate", "Pair-specific WNT5A-MCAM-DVL2-JNK branch; JUN/AP-1 remains a candidate only.")
    set_out([cell(n) for n in [138, 139]], "activin_alk4", "SMAD2/3;SMAD4 candidate", "reviewed_relay_candidate", "Activin-ALK4 family branch; exact four-part pair not isolated in one assay.")
    set_out([cell(n) for n in [140, 141]], "activin_alk7", "SMAD2/3;SMAD4 candidate", "reviewed_relay_candidate", "Activin-ALK7 family branch; exact type-II partner and PDX1 scope are limited.")
    set_out([ext(22)], None, "", "reviewed_no_downstream_evidence", "AMH-AMHR2-BMPR1A association was not detected in the primary comparison assay.")
    set_out([ext(23)], "amh_bmpr1b", "SMAD1/5/9;SMAD4 candidate", "reviewed_relay_candidate", "AMH-AMHR2-BMPR1B-SMAD1/5 branch; no target program.")
    set_out([cell(204)], "areg_egfr", "ELK1 candidate", "reviewed_relay_candidate", "AREG-EGFR relay partly reused across organoid and fibroblast models.")
    set_out([ext(24)], "areg_erbb2", "ELK1;AP-1 candidates", "reviewed_relay_candidate", "EGFR-mediated ERBB2 transphosphorylation; no direct AREG-ERBB2 binding.")
    set_out([ext(25)], None, "", "reviewed_unresolved", "ARTN-GFRA1-RET downstream signaling is weak/contested.")
    set_out([ext(26)], "artn_gfra3_ret", "ELK1/AP-1 candidates", "reviewed_relay_candidate", "ARTN-GFRA3-RET-ERK/PI3K-AKT relay; no terminal TF assay.")
    set_out([ext(27)], "bdnf_trkb", "CREB", "reviewed_relay_candidate", "Pair-specific TrkB pathway with measured pCREB; Module22A target program still pending.")
    set_out([ext(28)], "bmp10_acvr2a", "SMAD1/5/9;SMAD4 candidates", "reviewed_binding_only", "ACVR2A binding/structural compatibility without exact ternary cellular relay.")
    set_out([ext(29)], "bmp10_bmpr2", "SMAD1/5/9;SMAD4 candidates", "reviewed_relay_candidate", "BMP10-ALK1-BMPR2 structural/family relay; no matched TF endpoint.")
    set_out([ext(30)], "bmp15_bmpr1b", "SMAD1/5/8;SMAD4 candidates", "reviewed_relay_candidate", "Pair-specific BMP15 receptor/pSMAD branch; downstream inhibin-B program deferred.")
    set_out([ext(31)], "bmp2_bmpr1a_acvr2a", "SMAD1/5/8;SMAD4 candidates", "reviewed_relay_candidate", "Pair-specific BMP2 receptor/pSMAD branch, non-SCI model.")
    set_out([ext(32)], None, "", "reviewed_binding_only", "Exact receptor-component binding only; no downstream cellular relay.")
    set_out([ext(33)], "bmp2_bmpr1a_bmpr2", "SMAD1/5/8;SMAD4 candidates", "reviewed_relay_candidate", "Pair-containing BMP2 receptor/pSMAD branch; target program deferred.")
    set_out([ext(34), ext(35)], None, "", "reviewed_binding_only", "Exact receptor-component binding only; no matched cellular relay.")
    set_out([ext(36)], "bmp2_bmpr1b_bmpr2", "SMAD1/5/8;SMAD4 candidates", "reviewed_relay_candidate", "Pair-containing BMP2 BMPR2/BMPR1B pSMAD branch.")
    set_out([ext(37), ext(38)], None, "", "reviewed_binding_only", "Exact receptor-component binding only; no matched cellular relay.")
    set_out([ext(39)], "bmp4_bmpr1a_bmpr2", "SMAD1/5/8;SMAD4 candidates", "reviewed_relay_candidate", "Pair-containing BMP4 BMPR2/BMPR1A pSMAD branch.")
    set_out([ext(40), ext(41), ext(42), ext(43), ext(44), ext(45)], None, "", "reviewed_no_downstream_evidence", "No qualifying exact-pair downstream relay found; binding/family pointers were not promoted.")
    set_out([ext(n) for n in range(46, 52)], "bmp5_ligand_smad", "SMAD1/5/8;SMAD4 candidates", "reviewed_relay_candidate", "BMP5 ligand-level family relay only; exact receptor pair unresolved.")
    set_out([ext(52)], "bmp6_bmpr", "SMAD1/5/8;SMAD4 candidates", "reviewed_relay_candidate", "BMP6 ACVR1/ACVR2A receptor-use branch.")
    set_out([ext(53), ext(56), ext(58), ext(59)], None, "", "reviewed_no_downstream_evidence", "Matched model did not support the exact receptor combination.")
    set_out([ext(54)], "bmp6_bmpr", "SMAD1/5/8;SMAD4 candidates", "reviewed_relay_candidate", "BMP6 ACVR1/BMPR2 receptor-use branch.")
    set_out([ext(55), ext(57)], "bmp6_bmpr", "SMAD1/5/8;SMAD4 candidates", "reviewed_relay_candidate", "BMP6 BMPR1A receptor-use branch.")
    set_out([cell(n) for n in [209]], "bmp7_bmpr", "SMAD1/5/8;SMAD4 candidates", "reviewed_relay_candidate", "BMP7 BMPR1A/ACVR2A receptor-use branch.")
    set_out([cell(210), cell(212)], None, "", "reviewed_binding_only", "Binding-family evidence without matched downstream relay.")
    set_out([cell(211)], "bmp7_bmpr", "SMAD1/5/8;SMAD4 candidates", "reviewed_relay_candidate", "BMP7 BMPR1B/ACVR2A reporter branch; TF identity unresolved.")
    set_out([cell(213)], "bmp8a_bmpr", "SMAD1/5/8;SMAD4 candidates", "reviewed_relay_candidate", "BMP8A BMPR1A/ACVR2A receptor-reconstituted canonical branch.")
    set_out([cell(214), cell(216)], None, "", "reviewed_no_downstream_evidence", "No matching canonical receptor-complex relay for the queued pair.")
    set_out([cell(215)], "bmp8a_bmpr", "SMAD1/5/8;SMAD4 candidates", "reviewed_relay_candidate", "BMP8A BMPR1B/ACVR2A reporter branch.")
    set_out([cell(n) for n in [217, 219, 220, 221, 222, 223, 224, 225]], "bmp8b_ligand_smad", "SMAD1/5/8;SMAD2/3 candidates", "reviewed_relay_candidate", "BMP8B ligand-level family relay only; exact receptor complex unresolved.")
    set_out([cell(227), cell(228)], "btc_egfr", "AP-1;ELK1 candidates", "reviewed_relay_candidate", "BTC receptor activation with ERK/PI3K candidates; no pair-specific TF assay.")
    set_out([ext(60)], "btc_egfr_erbb2", "AP-1;ELK1 candidates", "reviewed_relay_candidate", "BTC-EGFR/ERBB2 receptor and kinase branch; no TF-target evidence.")
    set_out([ext(61)], "btc_erbb4_structural", "", "reviewed_binding_only", "Structural BTC-HER2/HER4 complex only; intracellular relay not measured.")
    set_out([ext(62), ext(63)], None, "", "reviewed_binding_only", "Processed iC3b-CR3/CR4 binding evidence; intact C3 downstream kinase/TF relay not established.")
    set_out([ext(64), ext(65), ext(66), ext(68)], None, "", "reviewed_scavenging_only", "ACKR1 binding/transport/reservoir context; no canonical intracellular relay or TF.")
    set_out([ext(67), ext(69), ext(70), ext(71), ext(72)], "ackr4_scavenging", "", "reviewed_scavenging_only", "ACKR4 scavenging/gradient control; no terminal TF.")

    missing = sorted(set(pair_by_review) & set(outcomes) ^ set(outcomes))
    expected = set(outcomes)
    if len(expected) != 95:
        raise SystemExit(f"expected 95 reviewed pair outcomes, got {len(expected)}")
    if not expected.issubset(pair_by_review):
        raise SystemExit(f"outcomes not found in scaffold: {sorted(expected-set(pair_by_review))}")

    existing_keys = {r["pathway_reuse_key"] for r in reuse_rows}
    evidence_rows = []
    new_reuse_rows = []
    spec_to_evidence: dict[str, str] = {}
    for spec, (name, locators, species, layer, confidence, limitations, tf_status) in specs.items():
        reuse_key = spec_key_to_id[spec]
        evidence_id = f"M21A-PAIR-EVID-{list(specs).index(spec)+1:03d}"
        spec_to_evidence[spec] = evidence_id
        new_reuse_rows.append({
            "pathway_reuse_key": reuse_key,
            "source_entity": name.split("-")[0],
            "pathway_name": name,
            "edge_ids": "",
            "evidence_ids": evidence_id,
            "target_entities": "",
            "ligand_pair_count": "0",
            "ligand_pair_keys": "",
            "terminal_tf_entities": "",
            "validation_status": "reviewed_batch001_candidate",
            "reuse_rule": "Reuse only when receptor complex, branch, species, cell/model, assay, and evidence scope match.",
            "limitations": limitations,
        })
        evidence_rows.append({
            "evidence_id": evidence_id,
            "pathway_reuse_key": reuse_key,
            "source_locators": locators,
            "support_kind": "primary_experiment_or_structural_primary",
            "species_support": species,
            "source_species_detail": species,
            "evidence_layer": layer,
            "confidence_tier": confidence,
            "evidence_summary": name,
            "limitations": limitations,
        })

    # Fill pair-level linkage while retaining one reusable pathway record.
    review_rows = []
    pair_count_by_spec: dict[str, int] = {}
    pair_keys_by_spec: dict[str, list[str]] = {}
    for review_id, (spec, tf_entity, status, note) in outcomes.items():
        row = pair_by_review[review_id]
        reuse_key = spec_key_to_id.get(spec, "") if spec else ""
        evidence_id = spec_to_evidence.get(spec, "") if spec else ""
        if spec:
            pair_count_by_spec[spec] = pair_count_by_spec.get(spec, 0) + 1
            pair_keys_by_spec.setdefault(spec, []).append(row["pair_key"])
        row["pathway_reuse_keys"] = reuse_key
        row["module21a_edge_ids"] = "PENDING_M21A_EDGE_MATERIALIZATION" if spec else ""
        row["module21a_evidence_ids"] = evidence_id
        row["terminal_tf_entities"] = tf_entity
        row["module21a_status"] = status
        row["module22a_status"] = "candidate_tf_handoff_pending_validation" if tf_entity else "no_terminal_tf_evidence"
        row["search_boundary"] = "primary_review_batch001"
        row["curator_notes"] = note

        tfrow = tf_by_review[row["pair_key"]]
        tfrow["pathway_reuse_keys"] = reuse_key
        tfrow["terminal_tf_entities"] = tf_entity
        tfrow["module21a_evidence_ids"] = evidence_id
        tfrow["handoff_status"] = "pending_tf_program_review" if tf_entity else "no_terminal_tf_assigned"
        tfrow["terminal_tf_status"] = "candidate_or_supported_activation" if tf_entity else "none_found"
        tfrow["search_boundary"] = "Primary downstream review batch001; TF target-program search remains separate."
        tfrow["limitations"] = note

        review_rows.append({
            "review_id": review_id,
            "pair_key": row["pair_key"],
            "pair_label_canonical": row["pair_label_canonical"],
            "pathway_reuse_key": reuse_key,
            "module21a_evidence_id": evidence_id,
            "terminal_tf_entities": tf_entity,
            "review_status": status,
            "confidence_tier": "reviewed",
            "evidence_layer": spec and specs[spec][3] or "none",
            "curator_note": note,
        })

    for reuse in new_reuse_rows:
        spec = next(k for k, v in spec_key_to_id.items() if v == reuse["pathway_reuse_key"])
        reuse["ligand_pair_count"] = str(pair_count_by_spec.get(spec, 0))
        reuse["ligand_pair_keys"] = ";".join(sorted(pair_keys_by_spec.get(spec, [])))
        reuse["terminal_tf_entities"] = ";".join(sorted({r["terminal_tf_entities"] for r in review_rows if r["pathway_reuse_key"] == reuse["pathway_reuse_key"] and r["terminal_tf_entities"]}))

    write(PAIR, list(pair_rows[0]), list(pair_rows))
    write(TF, list(tf_rows[0]), list(tf_rows))
    write(REUSE, list(reuse_rows[0]), reuse_rows + new_reuse_rows)
    write(EVIDENCE, list(evidence_rows[0]), evidence_rows)
    write(REVIEW, list(review_rows[0]), review_rows)
    print(f"integrated {len(review_rows)} pair outcomes, {len(new_reuse_rows)} reusable pathway candidates, and {len(evidence_rows)} evidence records")


if __name__ == "__main__":
    main()
