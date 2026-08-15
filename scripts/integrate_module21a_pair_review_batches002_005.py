#!/usr/bin/env python3
"""Integrate the next four read-only Module 21A pair-review batches.

This updates only the all-pair audit scaffolds. It preserves Module 20A and
does not materialize the main SQL-ready Module 21A ledgers.
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELAY = ROOT / "work" / "module21_relay"
PAIR = RELAY / "module21a_all_pair_relay_coverage.tsv"
TF = RELAY / "module22a_ligand_tf_handoff.tsv"
REUSE = RELAY / "module21a_pathway_reuse_registry.tsv"
DETAIL = RELAY / "module21a_pair_relay_evidence_detail.tsv"
REVIEW = RELAY / "module21a_pair_relay_review_batches002_005.tsv"


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


def spec(key: str, ids: list[str], locators: str, species: str, model: str, assay: str,
         relation: str, layer: str, branch: str, confidence: str, tf: str,
         status: str, note: str) -> dict[str, str | list[str]]:
    return {"key": key, "ids": ids, "locators": locators, "species": species,
            "model": model, "assay": assay, "relation": relation, "layer": layer,
            "branch": branch, "confidence": confidence, "tf": tf,
            "status": status, "note": note}


def main() -> None:
    pair_rows = read(PAIR)
    tf_rows = read(TF)
    reuse_rows = [r for r in read(REUSE) if r.get("validation_status") != "reviewed_batch002_005_candidate"]
    pair_by_review = {r["module20a_review_id"]: r for r in pair_rows}
    tf_by_pair = {r["pair_key"]: r for r in tf_rows}

    # One reusable record is created only for a matched ligand/receptor,
    # receptor-complex, species/model and assay context. Activation-screen
    # groups remain distinct from cellular functional groups.
    specs: list[dict[str, str | list[str]]] = [
        spec("cxcl3_cxcr2", [cell(398)], "https://pubmed.ncbi.nlm.nih.gov/38233929/", "human", "HEK293A-CXCR2", "CXCL8-competition binding, NanoBRET G-protein, beta-arrestin and internalization", "direct binding; receptor activation", "receptor_proximal_relay", "CXCR2-Gi/o/Galpha15 chemokine GPCR branch", "high", "", "reviewed_relay_candidate", "Human exact-pair evidence; mouse transfer is conditional and no terminal TF was measured."),
        spec("gdf11_acvr2b_alk5", [cell(726)], "https://pubmed.ncbi.nlm.nih.gov/31315975/; https://pmc.ncbi.nlm.nih.gov/articles/PMC3820543/", "human and mouse", "HEK293/R1B-L17 and mouse Cor-1 neural stem cells", "ternary structure, mutagenesis, receptor assembly, CAGA12 reporter, pSMAD2/3 and proliferation", "direct receptor-complex assembly; receptor-proximal activation; function", "receptor_proximal_relay", "GDF11-ACVR2B-ALK5-SMAD2/3 branch", "high", "SMAD2/3 candidate", "reviewed_relay_candidate", "Exact ternary complex is strong; the neural-stem-cell functional context is not an SCI-cell proxy."),
        spec("gdf5_bmpr1b_acvr2a", [cell(731)], "https://pubmed.ncbi.nlm.nih.gov/8702914/; https://pmc.ncbi.nlm.nih.gov/articles/PMC2670865/; https://pmc.ncbi.nlm.nih.gov/articles/PMC4755026/", "rat and mouse", "ROB-C26/COS-1 receptor reconstitution and mouse sympathetic neurons", "receptor reconstitution, structural binding, receptor perturbation and neurite-growth assays", "direct ligand-receptor binding; receptor-complex activation; function", "receptor_proximal_relay", "GDF5-BMPR1B/ACVR2A-BMP-SMAD branch", "medium", "SMAD1/5/8 candidate", "reviewed_relay_candidate", "BMPR1B binding and receptor use are supported; pSMAD1/5/8 was not isolated in the exact ACVR2A reconstitution."),
        spec("ccl21f_ackr4", [ext(73)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC8092586/; https://pubmed.ncbi.nlm.nih.gov/35108538/", "mouse and human family-level", "ACKR4-expressing cells, lymphatic/endothelial and dendritic-cell models", "labeled-chemokine uptake/scavenging, ACKR4 loss-of-function and trafficking assays", "scavenging/internalization; functional gradient control", "downstream_pathway_function", "ACKR4-CCL21-family chemokine-gradient branch", "low", "", "reviewed_scavenging_only", "Ccl21f was not isolated from Ccl21a/b paralogs; no canonical GPCR-to-TF relay."),
        spec("ccl26_ackr2", [ext(74)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC12017343/; https://doi.org/10.4049/jimmunol.1401096", "human; mouse exact pair unresolved", "HEK293T ACKR2 assays and earlier trophoblast assay", "NanoBRET competition, beta-arrestin, binding, uptake and negative comparison", "direct binding; atypical scavenging/partial agonism", "ligand_receptor_binding_or_activation", "ACKR2 scavenging/beta-arrestin branch", "low", "", "reviewed_unresolved", "Human results are low-potency and conflict with an earlier negative assay; mouse Ccl26-specific evidence was not recovered."),
        spec("ccl27a_ccr10", [ext(75)], "https://pubmed.ncbi.nlm.nih.gov/10725697/; https://pmc.ncbi.nlm.nih.gov/articles/PMC9157018/", "human and mouse", "human CCR10 transfectants and mouse CCL27-family skin/lymphocyte models", "binding, calcium flux, chemotaxis, knockout and migration assays", "direct ligand-receptor activation; function", "receptor_proximal_relay", "CCR10-Gi/Ca2+/chemotaxis and lymphocyte-localization branch", "medium", "", "reviewed_relay_candidate", "Human pair is strong; mouse Ccl27a-specific loss is confounded by total Ccl27-family targeting."),
        spec("ccl3_ackr2", [ext(77)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC12017343/; https://pmc.ncbi.nlm.nih.gov/articles/PMC11811810/", "mouse", "ACKR2-expressing HEK293T and mouse T-cell/fibroblast cancer-associated models", "NanoBRET binding/uptake and chemokine-availability/chemoattraction assays", "direct binding; scavenging/internalization; function", "downstream_pathway_function", "ACKR2-CCL3 scavenging and extracellular-availability branch", "medium", "", "reviewed_scavenging_only", "This is not canonical G-protein chemotaxis and does not establish a TF endpoint."),
        spec("ccl3_ccr1", [ext(78)], "https://pubmed.ncbi.nlm.nih.gov/10766793/; https://pubmed.ncbi.nlm.nih.gov/12181451/; https://pmc.ncbi.nlm.nih.gov/articles/PMC3145066/", "human and mouse", "human CCR1 transfectants and mouse radiation-fibrosis model", "calcium flux, chemotaxis, photo-crosslinking, loss-of-function and inhibitor assays", "direct ligand-receptor contact; GPCR activation; function", "receptor_proximal_relay", "CCR1-Gi/Ca2+ inflammatory chemotaxis branch", "medium", "", "reviewed_relay_candidate", "Human direct contact and signaling are strongest; mouse functional genetics do not isolate direct binding in the same assay."),
        spec("csf2_gmcsfr", [ext(79)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC49068/; https://pubmed.ncbi.nlm.nih.gov/9211889/; https://pubmed.ncbi.nlm.nih.gov/18945591/", "mouse with human comparator", "COS-7 receptor reconstitution, FDC-P1 and mouse myeloid cells", "radioligand binding, alpha/beta co-expression, receptor perturbation, phospho-STAT5 and growth assays", "direct receptor-complex assembly; receptor-proximal relay; function", "receptor_proximal_relay", "GM-CSF-CSF2RA/CSF2RB-JAK2/SHC/ERK/STAT5 branch", "medium", "STAT5 candidate", "reviewed_relay_candidate", "Exact alpha/beta complex is strong; downstream STAT5 evidence is from related myeloid context, not the same reconstitution."),
        spec("egf_egfr_erbb2", [ext(80)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC3438943/; https://pmc.ncbi.nlm.nih.gov/articles/PMC43187/; https://pmc.ncbi.nlm.nih.gov/articles/PMC4176247/", "human", "CHO EGFR/ERBB2 and engineered epithelial receptor systems", "125I-EGF binding, dimerization luciferase, autophosphorylation and transphosphorylation", "direct EGF-EGFR binding; receptor-complex activation", "receptor_proximal_relay", "EGFR-ERBB2 heterodimer receptor-phosphorylation branch", "medium", "", "reviewed_relay_candidate", "ERBB2 is a co-receptor; direct EGF-ERBB2 binding was not established and no terminal TF was measured."),
        spec("ereg_egfr_erbb2", [ext(81)], "https://pubmed.ncbi.nlm.nih.gov/9419975/; https://doi.org/10.1038/s41388-021-01734-4", "human", "human breast-carcinoma and EGFR-mutant NSCLC cells", "radioligand crosslinking, receptor phosphorylation, EREG perturbation, dimer imaging and AKT assays", "direct EREG-EGFR binding; receptor-complex activation; function", "receptor_proximal_relay", "EGFR-ERBB2-AKT/ERK branch", "medium", "", "reviewed_relay_candidate", "EREG-ERBB2 direct binding was not shown; ERBB2 is a heterodimer partner."),
        spec("ereg_erbb2_erbb4", [ext(82)], "https://pubmed.ncbi.nlm.nih.gov/9419975/; https://pubmed.ncbi.nlm.nih.gov/9553109/; https://pmc.ncbi.nlm.nih.gov/articles/PMC5650921/", "human", "engineered ErbB lines, Ba/F3 and MCF-7", "crosslinking, receptor phosphorylation and ligand-dependent dimer-kinetic assays", "direct EREG-ERBB4 binding; receptor-complex activation", "receptor_proximal_relay", "ERBB2-ERBB4-ERK/AKT mitogenic branch", "medium", "", "reviewed_relay_candidate", "EREG contacts ERBB4; no direct EREG-ERBB2 binding and no terminal TF assay."),

        spec("fgf1_fgfr2", [ext(83)], "https://pubmed.ncbi.nlm.nih.gov/8663044/; https://pubmed.ncbi.nlm.nih.gov/11069186/; https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/", "human and mouse engineered systems", "FGFR2 ectodomain and BaF3-FGFR2 cells", "crystal structure, receptor activation and mitogenic screen", "direct ligand-receptor binding; receptor activation", "ligand_receptor_binding_or_activation", "FGFR2-FRS2/RAS-ERK, PI3K/AKT and PLCgamma family branches", "high", "", "reviewed_relay_candidate", "Exact complex/activation is supported; pair-specific physiological downstream function was not isolated."),
        spec("fgf1_fgfr3", [ext(84)], "https://pubmed.ncbi.nlm.nih.gov/14732692/; https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/", "human and mouse engineered systems", "FGFR3c ectodomain and BaF3-FGFR3 cells", "crystal/SPR and receptor-activation screen", "direct ligand-receptor binding; receptor activation", "ligand_receptor_binding_or_activation", "FGFR3-FRS2/RAS-ERK family branch", "high", "", "reviewed_relay_candidate", "Queue gene-level label does not resolve FGFR3b/c; no pair-specific physiological function."),
        spec("fgf10_fgfr1", [ext(85)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/", "mouse engineered system", "BaF3-FGFR1b/FGFR isoform panel", "mitogenic receptor-activation screen", "receptor activation", "ligand_receptor_binding_or_activation", "FGFR1b activation-screen branch", "low", "", "reviewed_binding_only", "Weak FGFR1b activation only; no direct binding or physiological FGFR1 function."),
        spec("fgf10_fgfr2b", [ext(86)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC151329/; https://pubmed.ncbi.nlm.nih.gov/11062007/; https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/", "human and mouse", "FGFR2b ectodomain, BaF3 and mouse embryonic lung", "crystal structure, receptor activation and FGFR2b blockade", "direct binding; receptor activation; function", "receptor_proximal_relay", "FGFR2b-FRS2/ERK epithelial developmental branch", "high", "ETV4/ETV5 candidates", "reviewed_relay_candidate", "Reuse is limited to mouse embryonic lung/FGFR2b; ETV4/5 are reporter/transcript readouts, not occupancy."),
        spec("fgf15_fgfr1", [ext(87)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/", "mouse engineered system", "BaF3-FGFR1c", "high-concentration/heparin receptor-activation screen", "receptor activation", "ligand_receptor_binding_or_activation", "FGFR1c endocrine-family activation screen", "low", "", "reviewed_binding_only", "Supraphysiologic activation; FGF15/FGF19 and beta-Klotho contexts are not interchangeable."),
        spec("fgf15_fgfr2", [ext(88)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/", "mouse engineered system", "BaF3-FGFR2c", "high-concentration/heparin receptor-activation screen", "receptor activation", "ligand_receptor_binding_or_activation", "FGFR2c endocrine-family activation screen", "low", "", "reviewed_binding_only", "No physiological downstream function established."),
        spec("fgf15_fgfr3", [ext(89)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/", "mouse engineered system", "BaF3-FGFR3c", "high-concentration/heparin receptor-activation screen", "receptor activation", "ligand_receptor_binding_or_activation", "FGFR3c endocrine-family activation screen", "low", "", "reviewed_binding_only", "No physiological downstream function established."),
        spec("fgf15_fgfr4_liver", [ext(90)], "https://pubmed.ncbi.nlm.nih.gov/22467244/; https://pmc.ncbi.nlm.nih.gov/articles/PMC3390456/; https://pmc.ncbi.nlm.nih.gov/articles/PMC4768716/", "mouse", "hepatocytes and mouse liver", "FGF15 administration, FGFR4/KLB and FRS2alpha perturbation, phospho-kinase and Cyp7a1 assays", "receptor-complex activation; function", "downstream_pathway_function", "FGF15-FGFR4/KLB-FRS2alpha-ERK/AKT/JNK-FOXO1 hepatic branch", "high", "FOXO1 candidate", "reviewed_relay_candidate", "Reuse is restricted to mouse liver/hepatocyte KLB context; Cyp7a1 is a target gene, not a TF."),
        spec("fgf16_fgfr1", [ext(91)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/", "mouse", "BaF3-FGFR1c and neonatal cardiac myocytes", "receptor activation screen and FGF16 cardiac response without receptor-specific perturbation", "receptor activation; functional attribution unresolved", "ligand_receptor_binding_or_activation", "FGFR1c activation/PKC cardiac-growth candidate branch", "medium", "", "reviewed_binding_only", "Cardiac function was not receptor-specific; no terminal TF."),
        spec("fgf16_fgfr2", [ext(92)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/", "mouse engineered system", "BaF3-FGFR2c", "receptor-activation screen", "receptor activation", "ligand_receptor_binding_or_activation", "FGFR2c activation screen", "medium", "", "reviewed_binding_only", "No exact pair-specific downstream/function assay."),
        spec("fgf16_fgfr3", [ext(93)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/", "mouse engineered system", "BaF3-FGFR3b/c", "receptor-activation screen", "receptor activation", "ligand_receptor_binding_or_activation", "FGFR3 activation screen", "medium", "", "reviewed_binding_only", "Isoform unresolved; no exact downstream function."),
        spec("fgf16_fgfr4", [ext(94)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/", "mouse engineered system", "BaF3-FGFR4", "receptor-activation screen", "receptor activation", "ligand_receptor_binding_or_activation", "FGFR4 activation screen", "medium", "", "reviewed_binding_only", "No exact downstream function."),
        spec("fgf17_fgfr3_ol", [ext(95)], "https://pubmed.ncbi.nlm.nih.gov/16384934/; https://pubmed.ncbi.nlm.nih.gov/16093398/; https://pmc.ncbi.nlm.nih.gov/articles/PMC6725305/", "human and rat", "FGFR3 binding assays and rat oligodendrocyte progenitors", "SPR, FGFR3 blocking antibody and differentiation assays", "direct binding; receptor-dependent function", "downstream_pathway_function", "FGF17-FGFR3 oligodendrocyte differentiation branch", "high", "", "reviewed_relay_candidate", "Reuse is limited to rat OL-progenitor/blocking-antibody context; no terminal TF was directly measured."),
        spec("fgf17_fgfr4", [ext(96)], "https://pubmed.ncbi.nlm.nih.gov/16384934/; https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/", "human and mouse engineered systems", "FGFR4 binding/SPR and BaF3-FGFR4", "SPR and receptor-activation screen", "direct binding; receptor activation", "ligand_receptor_binding_or_activation", "FGFR4 activation branch", "medium", "", "reviewed_binding_only", "No matched downstream/function evidence."),
        spec("fgf18_fgfr1", [ext(97)], "https://pubmed.ncbi.nlm.nih.gov/16384934/; https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/", "human and mouse engineered systems", "FGFR1c binding and BaF3-FGFR1", "SPR and receptor-activation screen", "direct binding; receptor activation", "ligand_receptor_binding_or_activation", "FGFR1c activation branch", "medium", "", "reviewed_binding_only", "No receptor-specific physiological function."),
        spec("fgf18_fgfr2_hflf", [ext(98)], "https://pubmed.ncbi.nlm.nih.gov/37701781/; https://pubmed.ncbi.nlm.nih.gov/16384934/", "human", "stage-defined human fetal lung fibroblasts", "FGF18 plus FGFR2 siRNA, SPR/BaF3 and proliferation/migration assays", "direct binding; receptor activation; function", "downstream_pathway_function", "FGF18-FGFR2-ERK fetal-lung fibroblast branch", "high", "ETV4/ETV5 candidates", "reviewed_relay_candidate", "Reuse only in the matching fetal-lung stage/cell context; receptor-specific TF causality is unresolved."),
        spec("fgf18_fgfr4_hflf", [ext(99)], "https://pubmed.ncbi.nlm.nih.gov/37701781/; https://pubmed.ncbi.nlm.nih.gov/16384934/", "human", "stage-defined human fetal lung fibroblasts", "FGF18 plus FGFR4 siRNA, SPR/BaF3 and proliferation/migration assays", "direct binding; receptor activation; function", "downstream_pathway_function", "FGF18-FGFR4-ERK fetal-lung fibroblast branch", "high", "ETV4/ETV5 candidates", "reviewed_relay_candidate", "Reuse only in the matching fetal-lung stage/cell context; receptor-specific TF causality is unresolved."),
        spec("fgf2_fgfr1_ol", [ext(100)], "https://pubmed.ncbi.nlm.nih.gov/11030354/; https://pmc.ncbi.nlm.nih.gov/articles/PMC6725305/", "human and rat", "FGFR1c structure and rat oligodendrocyte progenitors", "heparin structure, FGFR1 blockade and proliferation/differentiation assays", "direct binding; receptor activation; function", "downstream_pathway_function", "FGF2-FGFR1-FRS2/ERK oligodendrocyte branch", "high", "", "reviewed_relay_candidate", "Reuse only in rat OL-progenitor context; no direct terminal TF assay."),
        spec("fgf2_fgfr2_ol", [ext(101)], "https://pubmed.ncbi.nlm.nih.gov/11030354/; https://pmc.ncbi.nlm.nih.gov/articles/PMC6725305/", "human and rat", "FGFR2 structure and differentiated rat oligodendrocytes", "structural binding, FGFR2 blockade and process-elongation assays", "direct binding; receptor activation; function", "downstream_pathway_function", "FGF2-FGFR2-ERK/MAPK oligodendrocyte branch", "high", "", "reviewed_relay_candidate", "Reuse only in differentiated OL context; splice isoform is unresolved."),
        spec("fgf2_fgfr3", [ext(102)], "https://pubmed.ncbi.nlm.nih.gov/8663044/; https://pmc.ncbi.nlm.nih.gov/articles/PMC6725305/", "mouse engineered system", "BaF3-FGFR3 and receptor phosphorylation assays", "receptor-activation and phosphorylation assays", "receptor activation", "ligand_receptor_binding_or_activation", "FGFR3 activation branch", "medium", "", "reviewed_binding_only", "No matched ligand-specific functional assay."),
        spec("fgf2_fgfr4", [ext(103)], "https://pubmed.ncbi.nlm.nih.gov/7680645/; https://pubmed.ncbi.nlm.nih.gov/8663044/", "human and mouse engineered systems", "FGFR4 binding and engineered activation", "binding and receptor autophosphorylation", "direct binding; receptor activation", "ligand_receptor_binding_or_activation", "FGFR4 activation branch", "high", "", "reviewed_binding_only", "No matched downstream functional branch."),
        spec("fgf20_fgfr3", [ext(104)], "https://pubmed.ncbi.nlm.nih.gov/29698669/; https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/", "mouse and rat", "BaF3-FGFR3 and rat dopaminergic-neuron model", "receptor activation and nonspecific FGFR inhibitor response", "receptor activation; function unresolved", "ligand_receptor_binding_or_activation", "FGFR3 activation/neuroprotection candidate branch", "low", "", "reviewed_binding_only", "Neuroprotective effect cannot be assigned specifically to FGFR3."),
        spec("fgf20_fgfr4", [ext(105)], "https://pubmed.ncbi.nlm.nih.gov/29698669/; https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/", "mouse and rat", "BaF3-FGFR4 and rat dopaminergic-neuron model", "receptor activation and nonspecific FGFR inhibitor response", "receptor activation; function unresolved", "ligand_receptor_binding_or_activation", "FGFR4 activation/neuroprotection candidate branch", "low", "", "reviewed_binding_only", "Neuroprotective effect cannot be assigned specifically to FGFR4."),
        spec("fgf21_fgfr1_klb", [ext(106)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC5419549/; https://pmc.ncbi.nlm.nih.gov/articles/PMC3138239/; https://pubmed.ncbi.nlm.nih.gov/22442730/", "mouse and human", "KLB-positive 3T3-L1/adipocytes, WAT/liver and BaF3 reconstitution", "quantitative binding, FRS2/ERK, glucose uptake and in-vivo expression assays", "direct binding; receptor-complex activation; function", "downstream_pathway_function", "FGF21-KLB-FGFR1c-FRS2alpha-ERK/AKT metabolic branch", "high", "EGR1; c-FOS candidates", "reviewed_relay_candidate", "Reuse only in KLB-positive adipocyte/WAT context; TF expression is not DNA occupancy."),
        spec("fgf21_fgfr3_klb", [ext(107)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC5419549/", "mouse engineered system", "BaF3 KLB-FGFR3c reconstitution", "receptor activation assay", "receptor activation", "ligand_receptor_binding_or_activation", "FGF21-KLB-FGFR3c activation branch", "high", "", "reviewed_binding_only", "Artificial receptor activation lacks matched physiological FGFR3c function."),

        spec("fgf22_fgfr2b", [ext(108)], "https://pubmed.ncbi.nlm.nih.gov/25926357/; https://pmc.ncbi.nlm.nih.gov/articles/PMC4440923/", "mouse", "hippocampal neurons and Fgfr2b loss/kinase perturbation", "receptor/kinase/FRS2/PI3K perturbation and synaptic differentiation assays", "receptor activation; function", "downstream_pathway_function", "FGF22-FGFR2b-FRS2-PI3K excitatory presynaptic branch", "high", "", "reviewed_relay_candidate", "Reuse only in hippocampal FGFR2b context; no terminal TF assay."),
        spec("fgf23_fgfr1_klotho", [ext(109)], "https://pubmed.ncbi.nlm.nih.gov/17086194/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10284700/", "mouse and human", "renal cells, DCT and alphaKlotho-FGFR1c complexes", "structural/biochemical complex, receptor activation and renal pERK", "direct receptor-complex assembly; receptor activation; function", "receptor_proximal_relay", "FGF23-alphaKlotho-FGFR1c-FRS2-ERK renal branch", "high", "EGR1 candidate", "reviewed_relay_candidate", "AlphaKlotho is required; no transfer to Klotho-negative contexts."),
        spec("fgf23_fgfr4_cardiac", [ext(110)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC9329240/; https://pubmed.ncbi.nlm.nih.gov/21985788/", "mouse", "cardiac models with heparin/FGFR4 context", "binding/activation and cardiac perturbation assays", "receptor-complex activation; function", "downstream_pathway_function", "FGF23-FGFR4-PLCgamma-calcineurin-NFAT cardiac branch", "high", "NFAT candidate", "reviewed_relay_candidate", "Heparin/cofactor and tissue dependence are essential; no generalized FGFR4 reuse."),
        spec("fgf4_fgfr1", [ext(111)], "https://pubmed.ncbi.nlm.nih.gov/11486033/; https://doi.org/10.1006/bbrc.1999.1434", "human engineered system", "FGFR1c/RCS engineered cells", "binding/mutagenesis, pFGFR1, FRS2 and PLCgamma assays", "direct binding; receptor activation; function", "receptor_proximal_relay", "FGF4-FGFR1c-FRS2/ERK/PLCgamma branch", "high", "", "reviewed_relay_candidate", "Engineered receptor system; no broad native-context reuse."),
        spec("fgf4_fgfr2", [ext(112)], "https://pubmed.ncbi.nlm.nih.gov/11486033/; https://doi.org/10.1006/bbrc.1999.1434", "human engineered system", "FGFR2-expressing CHO and receptor panel", "binding/competition and activation screen", "direct binding; receptor activation", "ligand_receptor_binding_or_activation", "FGFR2 activation branch", "medium", "", "reviewed_binding_only", "No independent pair-specific relay/function."),
        spec("fgf4_fgfr3", [ext(113)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/", "mouse engineered system", "BaF3-FGFR3c", "mitogenic activation screen", "receptor activation", "ligand_receptor_binding_or_activation", "FGFR3c activation branch", "low", "", "reviewed_binding_only", "Activation-screen evidence only."),
        spec("fgf4_fgfr4", [ext(114)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/; https://doi.org/10.1016/j.celrep.2020.108164", "mouse", "classic receptor screen and mouse hepatic model", "receptor screen, FGFR4 perturbation, CaMKKbeta-AMPK-caspase assays", "receptor activation; functional receptor dependence", "downstream_pathway_function", "FGF4-FGFR4 hepatic CaMKKbeta-AMPK branch", "medium", "", "reviewed_relay_candidate", "Functional FGFR4 dependence conflicts with weak classic activation; reuse is hepatic-model only."),
        spec("fgf5_fgfr1", [ext(115)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/; https://pmc.ncbi.nlm.nih.gov/articles/PMC6343348/", "mouse", "BaF3-FGFR1c and spermatogonial cells", "receptor screen, FGF5 stimulation, ERK/AKT, pCREB/c-Fos/STAT3 and proliferation assays", "receptor activation; function with unresolved receptor causality", "downstream_pathway_function", "FGF5-ERK/AKT spermatogonial branch", "medium", "CREB; c-FOS; STAT3 candidates", "reviewed_function_only", "Ligand response is measured but FGFR1 causality is not isolated."),
        spec("fgf5_fgfr2", [ext(116)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/; https://pmc.ncbi.nlm.nih.gov/articles/PMC6343348/", "mouse", "BaF3-FGFR2 and spermatogonial cells", "weak receptor-screen activation and ligand response without receptor perturbation", "receptor activation; function unresolved", "ligand_receptor_binding_or_activation", "FGFR2 activation candidate branch", "low", "", "reviewed_binding_only", "No exact receptor-specific relay/function."),
        spec("fgf5_fgfr3", [ext(117)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/", "mouse engineered system", "BaF3-FGFR3", "weak receptor-activation screen", "receptor activation", "ligand_receptor_binding_or_activation", "FGFR3 activation screen", "low", "", "reviewed_binding_only", "No exact downstream evidence."),
        spec("fgf5_fgfr4_none", [ext(118)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/", "mouse engineered system", "BaF3-FGFR4", "classic receptor screen", "negative/no qualifying receptor activation", "ligand_receptor_binding_or_activation", "no defensible FGFR4 branch", "low", "", "reviewed_no_downstream_evidence", "No meaningful support or independent relay/function."),
        spec("fgf6_fgfr1_myoblast", [ext(119)], "https://pubmed.ncbi.nlm.nih.gov/32105707/", "rat and mouse", "C2C12/primary myoblasts and injury model", "FGFR1 perturbation, FGF6 dose response, ERK-linked cyclin D1, viability and migration", "receptor activation; function", "downstream_pathway_function", "FGF6-FGFR1-ERK myoblast branch", "high", "", "reviewed_relay_candidate", "Reuse only in high-dose myoblast context; no direct TF activity assay."),
        spec("fgf6_fgfr2", [ext(120)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/", "mouse engineered system", "BaF3-FGFR2", "weak receptor-activation screen", "receptor activation", "ligand_receptor_binding_or_activation", "FGFR2 activation screen", "low", "", "reviewed_binding_only", "No receptor-specific downstream function."),
        spec("fgf6_fgfr3", [ext(121)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/", "mouse engineered system", "BaF3-FGFR3", "weak receptor-activation screen", "receptor activation", "ligand_receptor_binding_or_activation", "FGFR3 activation screen", "low", "", "reviewed_binding_only", "No exact downstream evidence."),
        spec("fgf6_fgfr4_myoblast", [ext(122)], "https://pubmed.ncbi.nlm.nih.gov/32105707/", "rat and mouse", "C2C12/primary myoblasts", "FGFR4 perturbation, differentiation, ERK1/2, MyHC, MyoD and myogenin assays", "receptor activation; function", "downstream_pathway_function", "FGF6-FGFR4-ERK myoblast differentiation branch", "high", "MyoD; myogenin candidates", "reviewed_relay_candidate", "Reuse only in matching myoblast differentiation context; expression is not TF occupancy."),
        spec("fgf7_fgfr1", [ext(123)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/; https://doi.org/10.1016/j.ymthe.2011.01.011", "mouse", "BaF3-FGFR1b and salivary gland", "activation screen and FGFR1b expression/perturbation", "receptor activation; function unresolved", "ligand_receptor_binding_or_activation", "FGFR1b activation candidate branch", "low", "", "reviewed_binding_only", "FGFR1b expression did not establish functional necessity."),
        spec("fgf7_fgfr2b", [ext(124)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC3074487/; https://pubmed.ncbi.nlm.nih.gov/15716343/", "mouse", "epithelial and salivary-gland models", "FGFR2b perturbation, branching, migration, ERK/Src/p38/PI3K and EGFR transactivation", "receptor activation; function", "downstream_pathway_function", "FGF7-FGFR2b-ADAM17-HB-EGF-EGFR branch", "high", "", "reviewed_relay_candidate", "Reuse only in FGFR2b epithelial/gland contexts; no terminal TF assay."),
        spec("fgf8_fgfr2", [ext(125)], "https://pubmed.ncbi.nlm.nih.gov/16384934/; https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/", "human and mouse", "FGFR2c structure/SPR, SC-3 and developmental explants", "crystal/SPR, receptor activation and FRS2/ERK assays", "direct binding; receptor activation; function", "receptor_proximal_relay", "FGF8-FGFR2c-FRS2/ERK developmental branch", "medium", "", "reviewed_relay_candidate", "Molecular evidence is strong; native downstream receptor assignment is not fully isolated."),
        spec("fgf8_fgfr3_cortex", [ext(126)], "https://pubmed.ncbi.nlm.nih.gov/20843859/; https://pmc.ncbi.nlm.nih.gov/articles/PMC2947756/", "mouse", "neocortex with FGFR3c dominant-negative perturbation", "binding/SPR, pERK and patterning perturbation", "direct binding; receptor activation; function", "downstream_pathway_function", "FGF8-FGFR3c-ERK cortical-patterning branch", "high", "", "reviewed_relay_candidate", "Nr2f1 is a target gene readout, not a direct TF-activation assay."),
        spec("fgf8_fgfr4", [ext(127)], "https://pubmed.ncbi.nlm.nih.gov/16384934/; https://pubmed.ncbi.nlm.nih.gov/18213631/", "human and mouse", "FGFR4 SPR and SC-3/LNCaP", "SPR and FRS2/ERK cell assays with receptor identity unresolved", "direct binding; receptor activation; function unresolved", "ligand_receptor_binding_or_activation", "FGFR4 activation candidate branch", "low", "", "reviewed_binding_only", "Downstream SC-3 assays cannot assign FGFR4 specifically."),
        spec("fgf9_fgfr1_engineered", [ext(128)], "https://pubmed.ncbi.nlm.nih.gov/28757146/; https://pmc.ncbi.nlm.nih.gov/articles/PMC5587394/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10990489/", "human engineered system", "engineered FGF9/FGFR1c P252R RCS cells", "engineered ligand/receptor activation, pERK/pFRS2/PLCgamma and growth assays", "conditional receptor activation; function", "receptor_proximal_relay", "engineered FGF9-FGFR1c-ERK/FRS2/PLCgamma branch", "medium", "", "reviewed_relay_candidate", "Native WT FGF9-FGFR1 activation is weak/conditional; reuse only in engineered context."),
        spec("fgf9_fgfr4_none", [ext(129)], "https://pubmed.ncbi.nlm.nih.gov/8619928/; https://pmc.ncbi.nlm.nih.gov/articles/PMC2080618/", "mouse/human receptor screens", "FGFR4 receptor-activation panels", "heparin-dependent receptor-specificity screen", "negative/no qualifying receptor activation", "ligand_receptor_binding_or_activation", "no defensible FGFR4 branch", "low", "", "reviewed_no_downstream_evidence", "No meaningful binding/activation or independent downstream evidence."),

        spec("gdnf_gfra1_ret", [ext(130)], "https://pubmed.ncbi.nlm.nih.gov/14514671/; https://pubmed.ncbi.nlm.nih.gov/10545102/; https://pmc.ncbi.nlm.nih.gov/articles/PMC2905627/", "human, rat and mouse", "recombinant receptors and mouse spermatogonial stem-cell line", "receptor binding, phospho-RET, Ras/ERK/PI3K assays and inhibitor/function studies", "direct receptor-complex assembly; receptor activation; function", "downstream_pathway_function", "GDNF-GFRA1-RET-Shc/Grb2-Ras-ERK and PI3K/AKT branch", "high", "CREB1; ATF1; CREM1 candidates", "reviewed_relay_candidate", "Reuse only for matched GDNF-GFRA1-RET context; TF phosphorylation is relay-level, not a target program."),
        spec("ifna9_ifnar_family", [ext(131)], "https://pubmed.ncbi.nlm.nih.gov/9322767/; https://pubmed.ncbi.nlm.nih.gov/10704203/; https://www.ncbi.nlm.nih.gov/gene/15972", "mouse family-level", "type-I IFN receptor structural/reconstitution studies; no exact Ifna9 cell assay", "family receptor architecture and JAK/STAT comparator; exact-pair search boundary", "family-level receptor assignment; no exact downstream evidence", "receptor_proximal_relay", "IFNAR1/2-JAK1/TYK2-STAT1/2-IRF9 family branch", "low", "STAT1/2; IRF9 candidates", "reviewed_unresolved", "No exact Ifna9 binding or receptor-dependence study recovered; do not promote family evidence to exact pair."),
        spec("ifnab_ifnar_family", [ext(132)], "https://pubmed.ncbi.nlm.nih.gov/9322767/; https://pubmed.ncbi.nlm.nih.gov/10704203/; https://www.ncbi.nlm.nih.gov/gene/15974", "mouse family-level", "type-I IFN receptor structural/reconstitution studies; no exact Ifnab cell assay", "family receptor architecture and JAK/STAT comparator; exact-pair search boundary", "family-level receptor assignment; no exact downstream evidence", "receptor_proximal_relay", "IFNAR1/2-JAK1/TYK2-STAT1/2-IRF9 family branch", "low", "STAT1/2; IRF9 candidates", "reviewed_unresolved", "No exact Ifnab binding or receptor-dependence study recovered."),
        spec("ifnb1_ifnar", [ext(133)], "https://pubmed.ncbi.nlm.nih.gov/9322767/; https://pubmed.ncbi.nlm.nih.gov/10704203/; https://pubmed.ncbi.nlm.nih.gov/34813358/", "human and mouse", "Daudi and reconstituted IFNAR cells", "receptor-contact/mutational mapping, ternary activation and antiviral/antiproliferative assays", "direct receptor-complex assembly; receptor activation; function", "downstream_pathway_function", "IFNbeta-IFNAR1/2-JAK1/TYK2-STAT1/2-IRF9 branch", "high", "STAT1/2; IRF9 candidates", "reviewed_relay_candidate", "Exact IFNbeta-IFNAR branch is strong; target programs remain Module22A."),
        spec("ifne_ifnar", [ext(134)], "https://pubmed.ncbi.nlm.nih.gov/23449591/; https://pmc.ncbi.nlm.nih.gov/articles/PMC3617553/", "mouse", "female reproductive tract epithelial infection models", "recombinant IFNepsilon, IFNAR dependence, HSV-2/Chlamydia protection and ISG assays", "receptor activation; function", "downstream_pathway_function", "IFNepsilon-IFNAR-JAK/STAT-ISG branch", "medium", "STAT/ISGF3 candidates", "reviewed_relay_candidate", "Exact terminal TF was not isolated; reuse only in mouse reproductive-tract epithelial context."),
        spec("ifng_ifngr", [ext(135)], "https://pubmed.ncbi.nlm.nih.gov/7777519/; https://www.rcsb.org/structure/1FG9; https://pubmed.ncbi.nlm.nih.gov/7673114/", "human and mouse", "reconstituted IFNGR cells and receptor structural systems", "ternary/hexameric structure, receptor-chain dependence, pSTAT1 and nuclear translocation", "direct receptor-complex assembly; receptor activation; function", "downstream_pathway_function", "IFNgamma-IFNGR1/2-JAK1/JAK2-STAT1 GAF branch", "high", "STAT1 candidate", "reviewed_relay_candidate", "Exact pSTAT1/nuclear translocation supports relay; target program remains Module22A."),
        spec("ifnk_ifnar", [ext(136)], "https://pubmed.ncbi.nlm.nih.gov/11514542/; https://pmc.ncbi.nlm.nih.gov/articles/PMC6185784/", "human", "human keratinocytes", "recombinant IFNkappa, IFNAR/TYK2 perturbation, ISRE/ISG and antiviral assays", "receptor activation; function", "downstream_pathway_function", "IFNkappa-IFNAR-JAK1/TYK2-STAT/ISGF3 branch", "medium", "STAT/ISGF3 candidates", "reviewed_relay_candidate", "Exact terminal TF activation was not isolated; mouse exact-pair resolution is low."),
        spec("mif_cd74_cxcr2", [ext(137)], "https://pubmed.ncbi.nlm.nih.gov/17435771/; https://pmc.ncbi.nlm.nih.gov/articles/PMC2566990/", "human and mouse", "HEK293, monocytes and vascular/atherosclerosis models", "ligand binding, co-complex, Galpha-i/integrin arrest, chemotaxis, calcium and blockade assays", "direct component binding; receptor-complex activation; function", "downstream_pathway_function", "MIF-CD74/CXCR2-Gi/integrin/Ca2+ branch", "high", "", "reviewed_relay_candidate", "MIF binds CXCR2 and CD74 separately; direct binding to the composite trimer is not claimed and no TF was measured."),
        spec("mif_cd74_cxcr4", [ext(138)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC2193907/; https://pmc.ncbi.nlm.nih.gov/articles/PMC2911026/", "human", "HEK293, Jurkat, monocytes and CLL cells", "MIF-CD74 binding, CD74/CXCR4 co-complex, AKT, AMD3100/antibody blockade and migration assays", "direct component binding; receptor-complex activation; function", "downstream_pathway_function", "MIF-CD74/CXCR4-PI3K/AKT branch", "high", "", "reviewed_relay_candidate", "Composite-trimer direct binding is unresolved; no terminal TF was measured."),
        spec("slitrk1_ptprd", [ext(139)], "https://pubmed.ncbi.nlm.nih.gov/25394468/; https://pubmed.ncbi.nlm.nih.gov/25989451/", "mouse and rat", "recombinant proteins, cell-binding and neuronal/cell-aggregation assays", "binding, structural/contact and synaptic adhesion assays", "direct adhesion; functional attribution unresolved", "ligand_receptor_binding_or_activation", "SLITRK1-PTPRD trans-synaptic adhesion branch", "medium", "", "reviewed_binding_only", "PTPRS is stronger for some SLITRK1 functional contexts; PTPRD-specific functional branch remains unresolved."),
        spec("slitrk2_ptprd", [ext(140)], "https://www.nature.com/articles/ncomms6423; https://pubmed.ncbi.nlm.nih.gov/25989451/", "mouse and rat", "PTPRD MeB/splice and neuronal co-culture", "structure, SPR, mutagenesis and synaptogenic rescue/perturbation", "direct adhesion; function", "downstream_pathway_function", "SLITRK2-PTPRD splice-dependent synaptic-assembly branch", "medium", "", "reviewed_relay_candidate", "Reuse only with matching PTPRD splice/contact and synaptic context; no TF."),
        spec("slitrk3_ptprd", [ext(141)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC3288805/", "mouse and rat", "COS-cell binding, rat hippocampal cultures and Slitrk3-null mice", "binding, PTPRD dependence, knockout and inhibitory-synapse assays", "direct adhesion; receptor-dependent function", "downstream_pathway_function", "SLITRK3-PTPRD inhibitory synaptic-adhesion branch", "high", "", "reviewed_relay_candidate", "Reuse only in matched inhibitory synapse/PTPRD splice context; no TF."),
        spec("slitrk4_ptprs", [ext(142)], "https://pubmed.ncbi.nlm.nih.gov/23345436/; https://pmc.ncbi.nlm.nih.gov/articles/PMC3593915/", "rat", "rat neuronal cultures and artificial-synapse assays", "cell binding, PTPRS knockdown and synaptogenesis", "direct adhesion; receptor-dependent function", "downstream_pathway_function", "SLITRK4-PTPRS excitatory synaptic-adhesion branch", "medium", "", "reviewed_relay_candidate", "Reuse only in matching excitatory synapse/PTPRS splice context; no TF."),
        spec("slitrk5_ptprs", [ext(143)], "https://pubmed.ncbi.nlm.nih.gov/23345436/; https://pmc.ncbi.nlm.nih.gov/articles/PMC3593915/", "rat", "rat neuronal cultures and artificial-synapse assays", "cell binding, PTPRS knockdown and synaptogenesis", "direct adhesion; receptor-dependent function", "downstream_pathway_function", "SLITRK5-PTPRS excitatory synaptic-adhesion branch", "medium", "", "reviewed_relay_candidate", "Reuse only in matching excitatory synapse/PTPRS splice context; no TF."),
        spec("wnt5a_fzd10_none", [ext(144)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC2881539/; https://pmc.ncbi.nlm.nih.gov/articles/PMC12153800/", "human assay systems", "FZD10 CRD and low-receptor NanoBRET assays", "purified binding and NanoBRET association", "negative/unresolved direct binding", "ligand_receptor_binding_or_activation", "no defensible WNT5A-FZD10 branch", "low", "", "reviewed_unresolved", "No qualifying exact-pair activation/function; retain as unresolved rather than transfer FZD3/FZD6 evidence."),
        spec("wnt5a_fzd3", [ext(145)], "https://pubmed.ncbi.nlm.nih.gov/17804197/", "human", "primary human dermal fibroblasts and FZD3 assays", "binding, FZD3-CRD blockade, PI3K/AKT and adhesion assays", "direct binding; receptor-proximal activation; function", "downstream_pathway_function", "WNT5A-FZD3-PI3K/AKT adhesion branch", "high", "", "reviewed_relay_candidate", "Reuse only in matched human fibroblast/FZD3 context; no TF endpoint."),
        spec("wnt5a_fzd6", [ext(146)], "https://pmc.ncbi.nlm.nih.gov/articles/PMC5992127/; https://pubmed.ncbi.nlm.nih.gov/34769487/", "human", "liver tumor-initiating cells and PC-3 cells", "GST pulldown, FZD6 attachment/proximity, beta-catenin nuclear accumulation and PCP assays", "direct/contextual receptor association; receptor-proximal activation; function", "downstream_pathway_function", "WNT5A-FZD6 context-dependent beta-catenin or ROR1-PCP branches", "medium", "beta-catenin candidate", "reviewed_relay_candidate", "Two non-interchangeable contexts are retained in one pair record; no target-program inference."),
    ]

    assigned = {rid for s in specs for rid in s["ids"]}
    if len(assigned) != 76:
        raise SystemExit(f"expected 76 assigned outcomes, got {len(assigned)}")
    if not assigned.issubset(pair_by_review):
        raise SystemExit(f"assigned IDs absent from scaffold: {sorted(assigned - set(pair_by_review))}")

    existing_keys = {r["pathway_reuse_key"] for r in reuse_rows}
    max_reuse = max((int(k.rsplit("-", 1)[1]) for k in existing_keys if k.startswith("M21A-REUSE-")), default=0)
    max_evidence = 0
    for row in read(RELAY / "module21a_pair_relay_evidence_register.tsv"):
        value = row.get("evidence_id", "")
        if value.startswith("M21A-PAIR-EVID-"):
            max_evidence = max(max_evidence, int(value.rsplit("-", 1)[1]))

    detail_fields = ["evidence_id", "pathway_reuse_key", "source_locators", "species", "cell_type_model", "assay_or_perturbation", "relation_type", "evidence_layer", "pathway_branch", "confidence_tier", "evidence_summary", "limitations"]
    detail_rows = read(DETAIL) if DETAIL.exists() else []
    if detail_rows and "evidence_id" not in detail_rows[0]:
        detail_rows = []
    detail_rows = [
        r for r in detail_rows
        if not (r.get("evidence_id", "").startswith("M21A-PAIR-EVID-")
                and int(r["evidence_id"].rsplit("-", 1)[1]) >= 31)
    ]
    detail_ids = {r["evidence_id"] for r in detail_rows}
    if not detail_rows:
        for row in read(RELAY / "module21a_pair_relay_evidence_register.tsv"):
            detail_rows.append({
                "evidence_id": row.get("evidence_id", ""), "pathway_reuse_key": row.get("pathway_reuse_key", ""),
                "source_locators": row.get("source_locators", ""), "species": row.get("species_support", ""),
                "cell_type_model": row.get("source_species_detail", ""), "assay_or_perturbation": "See Module21A batch001 summary and cited primary sources.",
                "relation_type": "pathway_or_functional_evidence", "evidence_layer": row.get("evidence_layer", ""),
                "pathway_branch": row.get("evidence_summary", ""), "confidence_tier": row.get("confidence_tier", ""),
                "evidence_summary": row.get("evidence_summary", ""), "limitations": row.get("limitations", ""),
            })
            detail_ids.add(row.get("evidence_id", ""))

    new_reuse = []
    review_rows = []
    for s in specs:
        max_evidence += 1
        has_relay_or_function = s["status"] in {"reviewed_relay_candidate", "reviewed_function_only", "reviewed_scavenging_only"}
        if has_relay_or_function:
            max_reuse += 1
            reuse_key = f"M21A-REUSE-{max_reuse:04d}"
        else:
            reuse_key = ""
        evidence_id = f"M21A-PAIR-EVID-{max_evidence:03d}"
        s["reuse_key"] = reuse_key
        s["evidence_id"] = evidence_id
        ids = s["ids"]
        if has_relay_or_function:
            new_reuse.append({
                "pathway_reuse_key": reuse_key,
                "source_entity": str(s["branch"]).split("-")[0],
                "pathway_name": s["branch"],
                "edge_ids": "",
                "evidence_ids": evidence_id,
                "target_entities": "",
                "ligand_pair_count": str(len(ids)),
                "ligand_pair_keys": ";".join(sorted(pair_by_review[x]["pair_key"] for x in ids)),
                "terminal_tf_entities": str(s["tf"]),
                "validation_status": "reviewed_batch002_005_candidate",
                "reuse_rule": "Reuse only when exact ligand/receptor complex, isoform/cofactor, species, cell/model, assay and evidence scope match.",
                "limitations": s["note"],
            })
        detail_rows.append({
            "evidence_id": evidence_id, "pathway_reuse_key": reuse_key, "source_locators": s["locators"],
            "species": s["species"], "cell_type_model": s["model"], "assay_or_perturbation": s["assay"],
            "relation_type": s["relation"], "evidence_layer": s["layer"], "pathway_branch": s["branch"],
            "confidence_tier": s["confidence"], "evidence_summary": s["branch"], "limitations": s["note"],
        })
        for rid in ids:
            pair = pair_by_review[rid]
            pair["pathway_reuse_keys"] = reuse_key
            pair["module21a_edge_ids"] = "PENDING_M21A_EDGE_MATERIALIZATION" if has_relay_or_function else ""
            pair["module21a_evidence_ids"] = evidence_id
            pair["terminal_tf_entities"] = s["tf"]
            pair["module21a_status"] = s["status"]
            pair["module22a_status"] = "candidate_tf_handoff_pending_validation" if s["tf"] else "no_terminal_tf_evidence"
            pair["search_boundary"] = "primary_review_batches002_005"
            pair["curator_notes"] = s["note"]
            tfrow = tf_by_pair[pair["pair_key"]]
            tfrow["pathway_reuse_keys"] = reuse_key
            tfrow["terminal_tf_entities"] = s["tf"]
            tfrow["module21a_evidence_ids"] = evidence_id
            tfrow["handoff_status"] = "pending_tf_program_review" if s["tf"] else "no_terminal_tf_assigned"
            tfrow["terminal_tf_status"] = "candidate_or_supported_activation" if s["tf"] else "none_found"
            tfrow["search_boundary"] = "Primary downstream review batches002_005; TF target-program search remains separate."
            tfrow["limitations"] = s["note"]
            review_rows.append({
                "review_id": rid, "pair_key": pair["pair_key"], "pair_label_canonical": pair["pair_label_canonical"],
                "pathway_reuse_key": reuse_key, "evidence_id": evidence_id, "source_locators": s["locators"],
                "species": s["species"], "cell_type_model": s["model"], "assay_or_perturbation": s["assay"],
                "relation_type": s["relation"], "evidence_layer": s["layer"], "pathway_branch": s["branch"],
                "confidence_tier": s["confidence"], "terminal_tf_entities": s["tf"], "review_status": s["status"],
                "curator_note": s["note"],
            })

    # One review row per exact Module20A pair; the reusable pathway/evidence
    # record is shared only where the evidence scope actually matches.
    write(PAIR, list(pair_rows[0]), pair_rows)
    write(TF, list(tf_rows[0]), tf_rows)
    write(REUSE, list(reuse_rows[0]), reuse_rows + new_reuse)
    write(DETAIL, detail_fields, detail_rows)
    write(REVIEW, list(review_rows[0]), review_rows)
    print(f"integrated {len(review_rows)} pair outcomes, {len(new_reuse)} reusable pathway candidates, and {len(new_reuse)} detailed evidence records")


if __name__ == "__main__":
    main()
