#!/usr/bin/env python3
"""Integrate the completed priority-6 ECM/adhesion review batch 011."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELAY = ROOT / "work" / "module21_relay"
PAIR = RELAY / "module21a_all_pair_relay_coverage.tsv"
TF = RELAY / "module22a_ligand_tf_handoff.tsv"
REUSE = RELAY / "module21a_pathway_reuse_registry.tsv"
DETAIL = RELAY / "module21a_pair_relay_evidence_detail.tsv"
REVIEW = RELAY / "module21a_pair_relay_review_batch011.tsv"


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
    rows.append({
        "key": key,
        "review_id": review_id,
        "locators": locators,
        "species": species,
        "model": model,
        "assay": assay,
        "relation": relation,
        "layer": layer,
        "branch": branch,
        "confidence": confidence,
        "status": status,
        "note": note,
        "tf": tf,
    })


def main() -> None:
    pair_rows = read(PAIR)
    tf_rows = read(TF)
    reuse_rows = read(REUSE)
    detail_rows = read(DETAIL)
    old_review = read(REVIEW)

    old_by_review = {r.get("review_id", ""): r for r in old_review if r.get("review_id")}
    old_reuse_keys = {r.get("pathway_reuse_key", "") for r in old_review if r.get("pathway_reuse_key")}
    old_evidence_ids = {r.get("evidence_id", "") or r.get("module21a_evidence_id", "")
                        for r in old_review if r.get("evidence_id") or r.get("module21a_evidence_id")}

    specs = []
    U = "https://pubmed.ncbi.nlm.nih.gov/"
    add(specs, "thbs2_cd47_unresolved", "M20A-EXT-0470", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2613617/", "human", "vascular/endothelial and platelet-related systems", "CD47/TSP comparison and receptor-context review; no qualifying exact THBS2-CD47 relay", "unresolved; weak/unconfirmed direct assignment", "ligand_receptor_binding_or_activation", "no defensible THBS2-CD47 intracellular branch", "low", "reviewed_unresolved", "The cited CD47/TSP work does not establish a clean full-length THBS2-CD47 downstream relay; retain as an explicit unresolved boundary.")
    add(specs, "thbs2_avb3", "M20A-EXT-0472", U+"7798222/; https://pmc.ncbi.nlm.nih.gov/articles/PMC7686970/", "human", "endothelial/vascular cell systems", "TSP2-alphaVbeta3 binding/competition and integrin-dependent signaling or angiogenesis assays", "receptor-proximal adhesion; function", "downstream_pathway_function", "THBS2-alphaVbeta3 integrin/FAK-ERK-NF-kB vascular branch", "medium", "reviewed_relay_candidate", "NF-kB pathway readouts are retained as pathway-level evidence only; no terminal TF-target program is claimed.")
    add(specs, "thbs4_cd47_unresolved", "M20A-EXT-0477", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2613617/", "human", "vascular/endothelial and platelet-related systems", "CD47/TSP comparison and receptor-context review; no qualifying exact THBS4-CD47 relay", "unresolved; weak/unconfirmed direct assignment", "ligand_receptor_binding_or_activation", "no defensible THBS4-CD47 intracellular branch", "low", "reviewed_unresolved", "The available TSP/CD47 evidence does not isolate THBS4 as an exact ligand with a defensible downstream relay.")
    add(specs, "thbs4_avb3", "M20A-EXT-0479", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2993182/", "human", "vascular smooth-muscle/endothelial and matrix-remodeling systems", "THBS4-alphaVbeta3 adhesion/competition and downstream migration or remodeling assays", "receptor-proximal adhesion; function", "downstream_pathway_function", "THBS4-alphaVbeta3 integrin adhesion/remodeling branch", "medium", "reviewed_relay_candidate", "Context and matrix presentation are required; no terminal TF activation was isolated.")
    add(specs, "tnc_a8b1", "M20A-EXT-0482", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2692383/; https://pmc.ncbi.nlm.nih.gov/articles/PMC2710129/", "human and mouse", "neural/vascular matrix and cell-adhesion models", "TNC fragment/cryptic-site adhesion, alpha8beta1 blocking and migration or survival assays", "conditional receptor-proximal adhesion; function", "downstream_pathway_function", "TNC-alpha8beta1 cryptic-fragment adhesion/migration branch", "medium", "reviewed_relay_candidate", "Evidence is presentation- and fragment-dependent; do not generalize to intact soluble TNC without matching matrix context.")
    add(specs, "tnc_a9b1", "M20A-EXT-0483", U+"9565552/; https://pmc.ncbi.nlm.nih.gov/articles/PMC6665849/", "human and mouse", "neural crest/vascular and matrix-cell systems", "TNC-alpha9beta1 binding/adhesion, integrin blocking and migration or matrix-remodeling assays", "direct/proximal adhesion; function", "downstream_pathway_function", "TNC-alpha9beta1 adhesion/migration branch", "high", "reviewed_relay_candidate", "Strong exact-pair support, but cellular output remains context-specific and no terminal TF was measured.")
    add(specs, "tnc_avb3", "M20A-EXT-0484", U+"7505785/; https://pmc.ncbi.nlm.nih.gov/articles/PMC2139818/", "human and mouse", "fibroblast/endothelial and matrix-adhesion systems", "TNC-alphaVbeta3 binding/adhesion, blocking and migration or cytoskeletal assays", "direct/proximal adhesion; function", "downstream_pathway_function", "TNC-alphaVbeta3 RGD adhesion/migration branch", "high", "reviewed_relay_candidate", "RGD/matrix presentation and cell state matter; no terminal TF program is inferred.")
    add(specs, "tnc_avb6", "M20A-EXT-0485", U+"23958855/", "human", "epithelial and tumor-cell matrix models", "TNC-alphaVbeta6 adhesion or activation perturbation and migration/invasion assays", "receptor-proximal adhesion; function", "downstream_pathway_function", "TNC-alphaVbeta6 matrix-adhesion/invasion branch", "medium", "reviewed_relay_candidate", "Pair evidence is model-specific and does not establish a universal intracellular relay or TF endpoint.")
    add(specs, "tnc_sdc4", "M20A-EXT-0487", U+"17901052/", "human", "fibroblast/vascular matrix models", "TNC cryptic-peptide or fragment binding, SDC4 perturbation and adhesion/migration assays", "conditional receptor-proximal adhesion; function", "downstream_pathway_function", "TNC-SDC4 cryptic-peptide/GAG adhesion branch", "medium", "reviewed_relay_candidate", "Cryptic peptide, GAG and matrix presentation are required; this is not a clean intact-protein binary interaction.")
    add(specs, "tnn_a8b1_unresolved", "M20A-EXT-0489", U+"12812753/", "human", "neural/adhesion assay systems", "exact-pair search and integrin-family comparison", "negative/unresolved exact-pair assignment", "ligand_receptor_binding_or_activation", "no defensible TNN-alpha8beta1 downstream branch", "low", "reviewed_unresolved", "The cited search boundary does not establish exact TNN-alpha8beta1 binding or downstream signaling; do not transfer TNC evidence.")
    add(specs, "tnxb_avb3_binding_only", "M20A-EXT-0503", "https://doi.org/10.1046/j.1432-1327.1999.00563.x", "human", "recombinant extracellular-matrix and integrin-binding systems", "recombinant binding/adhesion assay", "direct binding only", "ligand_receptor_binding_or_activation", "TNXB-alphaVbeta3 binding branch; downstream relay unresolved", "medium", "reviewed_binding_only", "A binding observation is retained, but no exact downstream pathway or cellular function was validated for this pair.")
    add(specs, "vcam1_adb2", "M20A-EXT-0506", U+"9841932/; https://pmc.ncbi.nlm.nih.gov/articles/PMC1367263/", "human and mouse", "leukocyte/endothelial adhesion and inflammatory models", "VCAM1-alphaD/beta2 adhesion, blocking, transmigration and inflammatory signaling assays", "direct/proximal adhesion; function", "downstream_pathway_function", "VCAM1-alphaD/beta2 integrin adhesion/inflammatory branch", "high", "reviewed_relay_candidate", "Exact cellular output depends on leukocyte activation and endothelial context; no terminal TF-target program was measured.")
    add(specs, "vtn_a2b3", "M20A-EXT-0507", U+"10192457/", "human", "platelets and recombinant integrin systems", "vitronectin-alphaIIbbeta3 binding, platelet adhesion/spreading and integrin blockade", "direct/proximal adhesion; function", "downstream_pathway_function", "VTN-alphaIIbbeta3 platelet outside-in/FAK branch", "high", "reviewed_relay_candidate", "Platelet activation state and ligand presentation are required; no terminal TF endpoint.")
    add(specs, "vtn_a8b1", "M20A-EXT-0508", U+"7559467/", "human", "endothelial/epithelial and recombinant integrin systems", "vitronectin-alpha8beta1 binding/adhesion and integrin-blocking assays", "direct/proximal adhesion; function", "downstream_pathway_function", "VTN-alpha8beta1 adhesion/migration branch", "high", "reviewed_relay_candidate", "Exact downstream kinase sequence is context-dependent; the evidence supports function but not a terminal TF program.")
    add(specs, "vtn_avb1", "M20A-EXT-0509", U+"1690718/; https://pubmed.ncbi.nlm.nih.gov/14766759/", "human and mouse", "recombinant integrin and epithelial/vascular cell systems", "vitronectin-alphaVbeta1 binding, adhesion, integrin perturbation and migration assays", "direct/proximal adhesion; function", "downstream_pathway_function", "VTN-alphaVbeta1 adhesion/migration branch", "high", "reviewed_relay_candidate", "Matrix presentation and integrin activation state are required; no terminal TF activation was measured.")
    add(specs, "vtn_avb3", "M20A-EXT-0510", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2288998/; https://pubmed.ncbi.nlm.nih.gov/11922905/", "human and mouse", "endothelial, smooth-muscle and recombinant integrin systems", "vitronectin-alphaVbeta3 binding, blocking, FAK/Src or MAPK-linked adhesion/migration assays", "direct/proximal adhesion; function", "downstream_pathway_function", "VTN-alphaVbeta3 integrin/FAK-Src-MAPK adhesion branch", "high", "reviewed_relay_candidate", "Strong exact-pair functional support; kinase-to-TF propagation remains unassigned.")
    add(specs, "vtn_avb5", "M20A-EXT-0511", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2288998/; https://pubmed.ncbi.nlm.nih.gov/9028792/", "human and mouse", "endothelial/epithelial and recombinant integrin systems", "vitronectin-alphaVbeta5 binding, blocking, adhesion and migration/angiogenesis assays", "direct/proximal adhesion; function", "downstream_pathway_function", "VTN-alphaVbeta5 adhesion/angiogenesis branch", "high", "reviewed_relay_candidate", "Exact output depends on cell type and integrin expression; no terminal TF program is inferred.")
    add(specs, "vtn_avb8", "M20A-EXT-0512", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4882426/; https://pmc.ncbi.nlm.nih.gov/articles/PMC4059974/; https://pmc.ncbi.nlm.nih.gov/articles/PMC3239846/", "human and mouse", "vascular/epithelial and integrin-alphaVbeta8 models", "vitronectin presentation or integrin perturbation with migration, adhesion or signaling/function assays", "receptor-proximal function", "downstream_pathway_function", "VTN-alphaVbeta8 adhesion/migration branch", "medium", "reviewed_function_only", "Functional evidence is stronger than a clean direct ligand-interface assignment; no terminal TF activation was isolated.")
    add(specs, "vtn_upar", "M20A-EXT-0513", U+"7528215/; https://pubmed.ncbi.nlm.nih.gov/11773078/; https://pubmed.ncbi.nlm.nih.gov/17355965/; https://pubmed.ncbi.nlm.nih.gov/23327926/", "human and mouse", "endothelial, tumor and recombinant uPAR/integrin systems", "vitronectin-uPAR binding, integrin cooperation/blockade, FAK/ERK or migration/invasion assays", "direct receptor-complex association; receptor-proximal function", "downstream_pathway_function", "VTN-uPAR-integrin co-receptor/FAK-ERK migration branch", "high", "reviewed_relay_candidate", "uPAR-integrin cooperation and ligand presentation are context-dependent; composite-complex evidence is not a claim of a single binary interface.")
    add(specs, "vwf_a2b3", "M20A-EXT-0514", U+"2803984/; https://pmc.ncbi.nlm.nih.gov/articles/PMC296793/", "human", "platelets and recombinant vWF/integrin systems", "vWF-alphaIIbbeta3 binding, platelet adhesion/activation and integrin blockade", "direct/proximal adhesion; function", "downstream_pathway_function", "VWF-alphaIIbbeta3 platelet activation/outside-in branch", "high", "reviewed_relay_candidate", "Shear, multimeric vWF and platelet activation state are required; no terminal TF endpoint.")
    add(specs, "vwf_avb3", "M20A-EXT-0515", U+"7505120/; https://pmc.ncbi.nlm.nih.gov/articles/PMC2644087/", "human", "endothelial/platelet and recombinant integrin systems", "vWF-alphaVbeta3 binding/adhesion, blocking and angiogenesis or migration assays", "direct/proximal adhesion; function", "downstream_pathway_function", "VWF-alphaVbeta3 endothelial adhesion/angiogenesis branch", "medium", "reviewed_relay_candidate", "Multimeric vWF, matrix presentation and shear context limit generalization; no terminal TF program was measured.")

    if len(specs) != 21 or len({s["review_id"] for s in specs}) != 21:
        raise SystemExit("batch011 must contain 21 unique exact-pair outcomes")

    pair_by_review = {r["module20a_review_id"]: r for r in pair_rows}
    tf_by_pair = {r["pair_key"]: r for r in tf_rows}
    assigned = {s["review_id"] for s in specs}
    if not assigned.issubset(pair_by_review):
        raise SystemExit(f"batch011 IDs absent from scaffold: {sorted(assigned - set(pair_by_review))}")

    # Remove a prior batch011 integration without touching other batches.
    for review_id in assigned:
        row = pair_by_review[review_id]
        for field in ("pathway_reuse_keys", "module21a_edge_ids", "module21a_evidence_ids",
                      "terminal_tf_entities", "module21a_status", "module22a_status",
                      "search_boundary", "curator_notes"):
            row[field] = ""
        tfrow = tf_by_pair[row["pair_key"]]
        for field in ("pathway_reuse_keys", "terminal_tf_entities", "module21a_evidence_ids",
                      "handoff_status", "terminal_tf_status", "search_boundary", "limitations"):
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
    new_reuse = []
    review_rows = []
    for s in specs:
        old = old_by_review.get(s["review_id"], {})
        has_reuse = s["status"] in {"reviewed_relay_candidate", "reviewed_function_only", "reviewed_scavenging_only"}
        reuse_key = old.get("pathway_reuse_key", "") if has_reuse else ""
        if has_reuse and not reuse_key:
            while f"M21A-REUSE-{next_reuse:04d}" in existing_reuse:
                next_reuse += 1
            reuse_key = f"M21A-REUSE-{next_reuse:04d}"
            next_reuse += 1
        evidence_id = old.get("evidence_id", "") or old.get("module21a_evidence_id", "")
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
        pair["search_boundary"] = "primary_review_batch011"
        pair["curator_notes"] = s["note"]
        tfrow = tf_by_pair[pair["pair_key"]]
        tfrow["pathway_reuse_keys"] = reuse_key
        tfrow["terminal_tf_entities"] = s["tf"]
        tfrow["module21a_evidence_ids"] = evidence_id
        tfrow["handoff_status"] = "pending_tf_program_review" if s["tf"] else "no_terminal_tf_assigned"
        tfrow["terminal_tf_status"] = "candidate_or_supported_activation" if s["tf"] else "none_found"
        tfrow["search_boundary"] = "Primary downstream review batch011; TF target-program search remains separate."
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
                "validation_status": "reviewed_batch011_candidate",
                "reuse_rule": "Reuse only when exact ligand/receptor complex, isoform/chain/cofactor, species, cell/model, assay and evidence scope match.",
                "limitations": s["note"],
            })
        detail_rows.append({
            "evidence_id": evidence_id,
            "pathway_reuse_key": reuse_key,
            "source_locators": s["locators"],
            "species": s["species"],
            "cell_type_model": s["model"],
            "assay_or_perturbation": s["assay"],
            "relation_type": s["relation"],
            "evidence_layer": s["layer"],
            "pathway_branch": s["branch"],
            "confidence_tier": s["confidence"],
            "evidence_summary": s["branch"],
            "limitations": s["note"],
        })
        review_rows.append({
            "review_id": s["review_id"],
            "pair_key": pair["pair_key"],
            "pair_label_canonical": pair["pair_label_canonical"],
            "pathway_reuse_key": reuse_key,
            "evidence_id": evidence_id,
            "source_locators": s["locators"],
            "species": s["species"],
            "cell_type_model": s["model"],
            "assay_or_perturbation": s["assay"],
            "relation_type": s["relation"],
            "evidence_layer": s["layer"],
            "pathway_branch": s["branch"],
            "confidence_tier": s["confidence"],
            "terminal_tf_entities": s["tf"],
            "review_status": s["status"],
            "curator_note": s["note"],
        })

    review_fields = list(review_rows[0])
    write(PAIR, list(pair_rows[0]), pair_rows)
    write(TF, list(tf_rows[0]), tf_rows)
    write(REUSE, list(reuse_rows[0]), reuse_rows + new_reuse)
    write(DETAIL, detail_fields, detail_rows)
    write(REVIEW, review_fields, review_rows)
    print(f"integrated {len(review_rows)} pair outcomes, {len(new_reuse)} reusable pathway candidates, and {len(review_rows)} evidence records")


if __name__ == "__main__":
    main()
