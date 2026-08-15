#!/usr/bin/env python3
"""Integrate the two-agent priority-7 high/medium review batches."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELAY = ROOT / "work" / "module21_relay"
PAIR = RELAY / "module21a_all_pair_relay_coverage.tsv"
TF = RELAY / "module22a_ligand_tf_handoff.tsv"
REUSE = RELAY / "module21a_pathway_reuse_registry.tsv"
DETAIL = RELAY / "module21a_pair_relay_evidence_detail.tsv"
REVIEW = RELAY / "module21a_pair_relay_review_batches012_013.tsv"


def read(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def add(rows, key, review_id, locators, species, model, assay, relation, layer,
        branch, confidence, status, note, tf=""):
    rows.append({"key": key, "review_id": review_id, "locators": locators,
                 "species": species, "model": model, "assay": assay,
                 "relation": relation, "layer": layer, "branch": branch,
                 "confidence": confidence, "status": status, "note": note,
                 "tf": tf})


def main() -> None:
    pair_rows = read(PAIR)
    tf_rows = read(TF)
    reuse_rows = read(REUSE)
    detail_rows = read(DETAIL)
    old_review = read(REVIEW)
    old_by_review = {r.get("review_id", ""): r for r in old_review if r.get("review_id")}
    old_reuse_keys = {r.get("pathway_reuse_key", "") for r in old_review if r.get("pathway_reuse_key")}
    old_evidence_ids = {r.get("evidence_id", "") for r in old_review if r.get("evidence_id")}

    specs = []
    P = "https://pubmed.ncbi.nlm.nih.gov/"
    add(specs, "c1ql1_adgrb3", "M20A-EXT-0516", P+"21262840/; "+P+"37488606/", "mouse", "neurons and Purkinje cells", "recombinant binding, C1QL1/BAI3 loss-of-function, synapse counts and electrophysiology", "direct binding; receptor-dependent synaptic function", "downstream_pathway_function", "C1QL1-BAI3 synapse-organization branch", "high", "reviewed_function_only", "Direct binding and receptor-dependent synaptic function are established, but intracellular relay intermediates were not resolved.")
    add(specs, "c1ql2_adgrb3", "M20A-EXT-0517", P+"21262840/", "mouse", "recombinant domains and cell-surface binding systems", "SPR and cell-surface binding of C1QL2/BAI3 domains", "direct ligand-receptor binding only", "ligand_receptor_binding_or_activation", "C1QL2-BAI3 adhesion-GPCR branch", "high", "reviewed_binding_only", "C1QL2 functional studies primarily implicate NRXN3/kainate receptors, not exact BAI3-dependent signaling.")
    add(specs, "c1ql3_adgrb3", "M20A-EXT-0518", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6254345/; "+P+"21262840/", "mouse and human", "islets and INS1(832/13) cells", "C1QL3 treatment, BAI3 knockdown, soluble BAI3 blockade and insulin secretion", "receptor-dependent function", "downstream_pathway_function", "C1QL3-BAI3-cAMP/insulin-secretion branch", "high", "reviewed_function_only", "Functional output is receptor-dependent, but the intracellular relay was not directly mapped.")
    add(specs, "c1ql4_adgrb3", "M20A-EXT-0519", P+"21262840/; "+P+"30608882/; https://pmc.ncbi.nlm.nih.gov/articles/PMC6203814/", "mouse", "Leydig cells, seminiferous tubules and myoblasts", "recombinant C1QL4, BAI3 knockdown, ERK/cAMP assays, steroidogenesis and fusion assays", "receptor-dependent function; partial relay", "downstream_pathway_function", "C1QL4-BAI3 steroidogenic/myoblast branch", "medium", "reviewed_function_only", "BAI3 mediates only part of the Leydig-cell response and an additional receptor is implicated; CREB readout is not assigned as a pair-specific terminal TF.")
    add(specs, "cholesterol_dhcr24_rora_unresolved", "M20A-EXT-0520", "https://doi.org/10.1016/S0969-2126(02)00912-7; https://pmc.ncbi.nlm.nih.gov/articles/PMC2836105/", "human", "RORalpha ligand-binding domain structural/reporter systems", "RORalpha LBD structural/reporter assays, cholesterol manipulation and ligand-pocket mutation", "direct cholesterol-RORA binding/transcriptional modulation; composite pair unresolved", "ligand_receptor_binding_or_activation", "cholesterol-RORA nuclear-receptor branch; DHCR24 composite unresolved", "low", "reviewed_unresolved", "DHCR24 was not part of the demonstrated ligand-receptor assay. Retain the exact frozen composite as unresolved; do not transfer direct RORA activity to cholesterol-DHCR24.")
    add(specs, "col1a1_sdc4_no_downstream", "M20A-EXT-0522", P+"9712917/; "+P+"31907416/; "+P+"37991018/", "rat and mouse", "syndecan-transfectant collagen-I adhesion, MEFs on collagen-I and computational communication", "native collagen-I adhesion/mechanotransduction and computational COL1A1-SDC4 communication", "matrix-level/family context only", "ligand_receptor_binding_or_activation", "no defensible exact COL1A1-SDC4 intracellular branch", "low", "reviewed_no_downstream_evidence", "Evidence is for native type-I collagen or computational communication, not purified COL1A1 chain-specific binding or exact-pair perturbation.")
    add(specs, "col9a1_sdc4", "M20A-EXT-0547", "https://pubmed.ncbi.nlm.nih.gov/41999506/; https://doi.org/10.1007/s00535-026-02416-2", "human", "gastric-cancer CAFs and metastasis-initiating cells", "spatial/single-cell profiling, co-culture, COL9A1/SDC4 perturbation and migration/invasion assays", "receptor-dependent cellular function", "downstream_pathway_function", "COL9A1-SDC4 metastatic-niche branch", "medium", "reviewed_function_only", "Single study; downstream SDC4 effectors were not defined and no direct biochemical binding assay was reported.")
    add(specs, "dspp_itgav_itgb1", "M20A-EXT-0551", P+"22134916/; https://pmc.ncbi.nlm.nih.gov/articles/PMC3285302/; https://reactome.org/content/detail/R-HSA-4086132", "mouse", "C3H10T1/2 mesenchymal and dental-pulp cells", "DPP substrate, alphaV/beta1 blockade, beta1 knockdown, pFAK/paxillin/pERK/pELK1 and odontogenic differentiation", "direct processed-DPP binding; receptor-proximal relay; function", "downstream_pathway_function", "DSPP/DPP-alphaVbeta1-FAK/paxillin-ERK-ELK1 odontogenic branch", "high", "reviewed_relay_candidate", "Evidence is for the cleaved DPP region of DSPP rather than necessarily full-length precursor. ELK1 phosphorylation was directly measured and is handed to Module22A.", "ELK1")
    add(specs, "fn1_sdc4", "M20A-EXT-0553", P+"17485492/; "+P+"16787950/; "+P+"9079625/", "mouse and rat", "Sdc4-null MEFs and rat embryo fibroblasts", "fibronectin substrates, SDC4 mutants/knockdown and PKCalpha/RhoA/Rac1/FAK assays", "direct FN-SDC4 engagement; receptor-proximal relay; function", "downstream_pathway_function", "FN1-SDC4-PIP2-PKCalpha-RhoA/Rac1-FAK focal-adhesion branch", "high", "reviewed_relay_candidate", "Relay is established across matrix-adhesion studies rather than one complete ligand-to-output experiment; no terminal TF was directly measured.")
    add(specs, "lama1_itga1_itgb1", "M20A-EXT-0554", P+"9688542/; https://reactome.org/content/detail/R-HSA-215953", "human", "recombinant laminin-alpha1 fragments and purified alpha1beta1 systems", "purified alpha1beta1 binding and adhesion-domain assays", "direct fragment-integrin binding only", "ligand_receptor_binding_or_activation", "laminin-alpha1 LN-domain/alpha1beta1 adhesion branch", "high", "reviewed_binding_only", "Evidence is for alpha1-chain fragments and laminin-domain recognition; no pair-specific intracellular kinase or functional-output relay was measured.")
    add(specs, "lama2_itga1_itgb1", "M20A-EXT-0558", P+"9361014/; https://doi.org/10.1074/jbc.272.46.29330", "human", "recombinant laminin-alpha2 short-arm/domain-VI fragments and adhesion/neurite systems", "alpha1beta1-specific recognition, cell adhesion and neurite assays", "direct fragment-integrin binding only", "ligand_receptor_binding_or_activation", "laminin-2 alpha1beta1 adhesion branch", "high", "reviewed_binding_only", "Interaction was mapped to the laminin-alpha2 short arm/domain VI; downstream kinase relay was not established and intact laminin-211 context remains important.")
    add(specs, "lama5_itga1_itgb1", "M20A-EXT-0570", P+"18635166/", "human", "HCC cells and alpha5-containing laminin adhesion systems", "adhesion/recognition assays with alpha5-containing laminin", "direct alpha5-laminin-alpha1beta1 recognition only", "ligand_receptor_binding_or_activation", "laminin-alpha5/alpha1beta1 ECM adhesion branch", "medium", "reviewed_binding_only", "Exact alpha5-containing trimer and intracellular relay were not resolved.")
    add(specs, "lama5_sv2a_unresolved", "M20A-EXT-0571", "https://doi.org/10.1074/jbc.275.1.451", "electric ray", "electric-ray synaptosomes and purified SV2", "complex isolation and binding assay", "SV2-family/alpha5-laminin complex; exact isoform unresolved", "ligand_receptor_binding_or_activation", "presynaptic matrix adhesion branch; SV2A assignment unresolved", "low", "reviewed_unresolved", "Study used SV2-family protein, not isoform-resolved SV2A; no intracellular relay was measured.")
    add(specs, "mmp2_mmp14_itgav_itgb3", "M20A-EXT-0598", P+"11161720/; "+P+"10861447/", "human", "MCF7 and BLM melanoma models", "co-expression, immunoprecipitation, zymography, microscopy and invasion/migration assays", "MMP2 docking/maturation through MT1-MMP-alphaVbeta3 complex; receptor-proximal function", "downstream_pathway_function", "MT1-MMP/TIMP2-dependent MMP2 activation and alphaVbeta3 invasion branch", "high", "reviewed_relay_candidate", "Composite receptor context; no single linear intracellular pathway or TF endpoint was established.")
    add(specs, "ncam1_l1cam", "M20A-EXT-0599", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2115980/; https://doi.org/10.1016/S0014-5793(99)01671-3", "mouse and rat", "N2A/ESb-MP cells, cerebellar neurons and PC12-E2", "purified-protein, bead-aggregation and neurite assays", "NCAM-containing cis-complex enhances L1-dependent adhesion; function", "downstream_pathway_function", "L1/NCAM adhesion and neurite-outgrowth branch", "medium", "reviewed_function_only", "Evidence supports an NCAM-modulated L1 complex, not necessarily an isolated direct NCAM-L1 interface; exact downstream relay was not measured.")
    add(specs, "ncam1_ncam1", "M20A-EXT-0600", P+"7961669/; "+P+"10704499/", "mouse and rat", "NCAM-expressing cells, PC12-E2 and hippocampal neurons", "homophilic binding, coculture, inhibitors and kinase-pathway perturbations", "homophilic adhesion; receptor-proximal relay; function", "downstream_pathway_function", "NCAM-Fyn/FAK-PLCgamma-PKC-Ras/MEK-ERK neurite branch", "high", "reviewed_relay_candidate", "Neuronal and context-dependent pathway; ERK is a pathway readout, not a terminal TF activation record.")
    add(specs, "npnt_complex1_itga8_itgb1", "M20A-EXT-0602", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2757411/; "+P+"19342381/; https://pmc.ncbi.nlm.nih.gov/articles/PMC8916771/", "mouse and chick", "kidney development and periocular neural-crest models", "recombinant binding, knockout/knockdown and FAK/ROCK inhibition", "direct nephronectin-alpha8beta1 binding; receptor activation; function", "downstream_pathway_function", "NPNT-alpha8beta1-FAK-Rho/ROCK migration and GDNF/RET-linked kidney branch", "high", "reviewed_relay_candidate", "Complex 1 is not independently molecularly resolved from the second NPNT row; GDNF is a functional output, not a TF endpoint.")
    add(specs, "npnt_complex2_itga8_itgb1", "M20A-EXT-0603", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2757411/; "+P+"19342381/; https://pmc.ncbi.nlm.nih.gov/articles/PMC8916771/", "mouse and chick", "kidney development and periocular neural-crest models", "same exact NPNT-alpha8beta1 binding, knockout/knockdown and FAK/ROCK evidence", "direct nephronectin-alpha8beta1 binding; receptor activation; function", "downstream_pathway_function", "NPNT-alpha8beta1-FAK-Rho/ROCK migration and GDNF/RET-linked kidney branch", "high", "reviewed_relay_candidate", "Evidence is shared with complex 1; do not interpret the two queue rows as two independently proven receptor complexes.")
    add(specs, "ntn4_unc5b", "M20A-EXT-0605", P+"18719102/; https://pmc.ncbi.nlm.nih.gov/articles/PMC2902137/; https://pmc.ncbi.nlm.nih.gov/articles/PMC3909532/", "human and mouse", "endothelial/VSMC and angiogenesis models", "Fc-receptor binding, co-IP, siRNA, migration and tube assays", "UNC5B recruitment into a neogenin-NTN4 receptor complex; receptor-proximal function", "downstream_pathway_function", "neogenin-UNC5B guidance/angiogenesis-Src/FAK-PI3K-AKT-ERK/S6 branch", "medium", "reviewed_relay_candidate", "Primary evidence supports NTN4 binding to neogenin with UNC5B recruitment, not isolated NTN4-UNC5B binding; receptor-independent NTN4 outputs occur in some contexts.")
    add(specs, "ntn4_unc5d", "M20A-EXT-0606", P+"21216843/; https://doi.org/10.1093/cercor/bhq265", "mouse", "developing sensory cortex", "cell-surface binding and exogenous NTN4 survival assay", "exact ligand-receptor binding; receptor-associated function", "downstream_pathway_function", "NTN4-UNC5D layer-4 cortical cell-survival branch", "medium", "reviewed_function_only", "No intracellular relay or kinase pathway was directly measured; UNC5D was insufficient in deep-layer cells.")
    add(specs, "thbs2_sdc4", "M20A-EXT-0607", P+"40973793/; https://doi.org/10.1038/s41388-025-03569-9", "human and mouse", "lung adenocarcinoma CAF/tumor models", "spatial/single-cell analyses, binding and THBS2/SDC4 functional perturbations", "direct/contextual THBS2-SDC4 association; cellular function", "downstream_pathway_function", "THBS2-SDC4 EMT and tumor-progression branch", "medium", "reviewed_function_only", "Direct affinity was not quantified and SDC4 intracellular signaling was not mapped; EMT-associated TF readouts were not promoted.")
    add(specs, "vwf_gp_complex", "M20A-EXT-0616", P+"7523416/; https://doi.org/10.1182/blood-2002-03-0806; https://pmc.ncbi.nlm.nih.gov/articles/PMC1895591/", "human and mouse", "platelets and thrombosis models", "VWF/botrocetin or shear stimulation, kinase inhibition, immunoprecipitation and aggregation assays", "direct VWF binding to GPIb-IX-V; receptor-complex activation; function", "downstream_pathway_function", "VWF-GPIb-IX-V-Src/Lyn-Syk-SLP76-PI3K-Btk-PLCgamma2/PKC and alphaIIbbeta3 activation branch", "high", "reviewed_relay_candidate", "The receptor is a multimeric GP Ib-IX-V complex; individual-subunit attribution and terminal TF involvement are not established.")

    if len(specs) != 22 or len({s["review_id"] for s in specs}) != 22:
        raise SystemExit("batches012_013 must contain 22 unique exact-pair outcomes")
    pair_by_review = {r["module20a_review_id"]: r for r in pair_rows}
    tf_by_pair = {r["pair_key"]: r for r in tf_rows}
    assigned = {s["review_id"] for s in specs}
    if not assigned.issubset(pair_by_review):
        raise SystemExit(f"review IDs absent from scaffold: {sorted(assigned - set(pair_by_review))}")

    for review_id in assigned:
        row = pair_by_review[review_id]
        for field in ("pathway_reuse_keys", "module21a_edge_ids", "module21a_evidence_ids", "terminal_tf_entities",
                      "module21a_status", "module22a_status", "search_boundary", "curator_notes"):
            row[field] = ""
        tfrow = tf_by_pair[row["pair_key"]]
        for field in ("pathway_reuse_keys", "terminal_tf_entities", "module21a_evidence_ids", "handoff_status",
                      "terminal_tf_status", "search_boundary", "limitations"):
            tfrow[field] = ""
    reuse_rows = [r for r in reuse_rows if r.get("pathway_reuse_key", "") not in old_reuse_keys]
    detail_rows = [r for r in detail_rows if r.get("evidence_id", "") not in old_evidence_ids]
    existing_reuse = {r.get("pathway_reuse_key", "") for r in reuse_rows}
    next_reuse = max((int(k.rsplit("-", 1)[1]) for k in existing_reuse if k.startswith("M21A-REUSE-")), default=0) + 1
    existing_evidence = {r.get("evidence_id", "") for r in detail_rows}
    next_evidence = max((int(k.rsplit("-", 1)[1]) for k in existing_evidence if k.startswith("M21A-PAIR-EVID-")), default=0) + 1
    detail_fields = ["evidence_id", "pathway_reuse_key", "source_locators", "species", "cell_type_model",
                     "assay_or_perturbation", "relation_type", "evidence_layer", "pathway_branch",
                     "confidence_tier", "evidence_summary", "limitations"]
    review_rows = []
    new_reuse = []
    for s in specs:
        old = old_by_review.get(s["review_id"], {})
        has_reuse = s["status"] in {"reviewed_relay_candidate", "reviewed_function_only", "reviewed_scavenging_only"}
        reuse_key = old.get("pathway_reuse_key", "") if has_reuse else ""
        if has_reuse and not reuse_key:
            while f"M21A-REUSE-{next_reuse:04d}" in existing_reuse:
                next_reuse += 1
            reuse_key = f"M21A-REUSE-{next_reuse:04d}"
            next_reuse += 1
        evidence_id = old.get("evidence_id", "")
        if not evidence_id:
            while f"M21A-PAIR-EVID-{next_evidence:03d}" in existing_evidence:
                next_evidence += 1
            evidence_id = f"M21A-PAIR-EVID-{next_evidence:03d}"
            next_evidence += 1
        existing_reuse.add(reuse_key)
        existing_evidence.add(evidence_id)
        pair = pair_by_review[s["review_id"]]
        pair["pathway_reuse_keys"] = reuse_key
        pair["module21a_edge_ids"] = "PENDING_M21A_EDGE_MATERIALIZATION" if has_reuse else ""
        pair["module21a_evidence_ids"] = evidence_id
        pair["terminal_tf_entities"] = s["tf"]
        pair["module21a_status"] = s["status"]
        pair["module22a_status"] = "candidate_tf_handoff_pending_validation" if s["tf"] else "no_terminal_tf_evidence"
        pair["search_boundary"] = "primary_review_batches012_013"
        pair["curator_notes"] = s["note"]
        tfrow = tf_by_pair[pair["pair_key"]]
        tfrow["pathway_reuse_keys"] = reuse_key
        tfrow["terminal_tf_entities"] = s["tf"]
        tfrow["module21a_evidence_ids"] = evidence_id
        tfrow["handoff_status"] = "pending_tf_program_review" if s["tf"] else "no_terminal_tf_assigned"
        tfrow["terminal_tf_status"] = "candidate_or_supported_activation" if s["tf"] else "none_found"
        tfrow["search_boundary"] = "Primary downstream review batches012_013; TF target-program search remains separate."
        tfrow["limitations"] = s["note"]
        if has_reuse:
            new_reuse.append({
                "pathway_reuse_key": reuse_key,
                "source_entity": s["branch"].split("-", 1)[0],
                "pathway_name": s["branch"],
                "edge_ids": "",
                "evidence_ids": evidence_id,
                "target_entities": "",
                "ligand_pair_count": "1",
                "ligand_pair_keys": pair["pair_key"],
                "terminal_tf_entities": s["tf"],
                "validation_status": "reviewed_batches012_013_candidate",
                "reuse_rule": "Reuse only when exact ligand/receptor complex, isoform/chain/cofactor, species, cell/model, assay and evidence scope match.",
                "limitations": s["note"],
            })
        detail_rows.append({"evidence_id": evidence_id, "pathway_reuse_key": reuse_key,
                            "source_locators": s["locators"], "species": s["species"],
                            "cell_type_model": s["model"], "assay_or_perturbation": s["assay"],
                            "relation_type": s["relation"], "evidence_layer": s["layer"],
                            "pathway_branch": s["branch"], "confidence_tier": s["confidence"],
                            "evidence_summary": s["branch"], "limitations": s["note"]})
        review_rows.append({"review_id": s["review_id"], "pair_key": pair["pair_key"],
                            "pair_label_canonical": pair["pair_label_canonical"],
                            "pathway_reuse_key": reuse_key, "evidence_id": evidence_id,
                            "source_locators": s["locators"], "species": s["species"],
                            "cell_type_model": s["model"], "assay_or_perturbation": s["assay"],
                            "relation_type": s["relation"], "evidence_layer": s["layer"],
                            "pathway_branch": s["branch"], "confidence_tier": s["confidence"],
                            "terminal_tf_entities": s["tf"], "review_status": s["status"],
                            "curator_note": s["note"]})

    write(PAIR, list(pair_rows[0]), pair_rows)
    write(TF, list(tf_rows[0]), tf_rows)
    write(REUSE, list(reuse_rows[0]), reuse_rows + new_reuse)
    write(DETAIL, detail_fields, detail_rows)
    write(REVIEW, list(review_rows[0]), review_rows)
    print(f"integrated {len(review_rows)} pair outcomes, {len(new_reuse)} reusable pathway candidates, and {len(review_rows)} evidence records")


if __name__ == "__main__":
    main()
