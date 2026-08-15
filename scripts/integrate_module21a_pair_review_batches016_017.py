#!/usr/bin/env python3
"""Integrate priority-6 low ECM batches 016-017."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELAY = ROOT / "work" / "module21_relay"
PAIR = RELAY / "module21a_all_pair_relay_coverage.tsv"
TF = RELAY / "module22a_ligand_tf_handoff.tsv"
REUSE = RELAY / "module21a_pathway_reuse_registry.tsv"
DETAIL = RELAY / "module21a_pair_relay_evidence_detail.tsv"
REVIEW = RELAY / "module21a_pair_relay_review_batches016_017.tsv"
AGENT017 = RELAY / "module21a_batch017_review.tsv"


def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def spec(review_id, locators, species, model, assay, relation, layer, branch, status, note):
    return {"review_id": review_id, "source_locators": locators, "species": species,
            "cell_type_model": model, "assay_or_perturbation": assay,
            "relation_type": relation, "evidence_layer": layer,
            "pathway_branch": branch, "confidence_tier": "low",
            "terminal_tf_entities": "", "review_status": status,
            "curator_note": note}


def main() -> None:
    pair_rows = read(PAIR)
    tf_rows = read(TF)
    reuse_rows = read(REUSE)
    detail_rows = read(DETAIL)
    old_review = read(REVIEW) if REVIEW.exists() else []
    old_by_review = {r.get("review_id", ""): r for r in old_review if r.get("review_id")}
    old_reuse_keys = {r.get("pathway_reuse_key", "") for r in old_review if r.get("pathway_reuse_key")}
    old_evidence_ids = {r.get("evidence_id", "") for r in old_review if r.get("evidence_id")}

    P = "https://pubmed.ncbi.nlm.nih.gov/"
    batch016 = [
        spec("M20A-EXT-0227", P+"9699516/; "+P+"11572855/", "human", "human/recombinant alpha2beta1 and collagen-IV fragments", "adhesion and I-domain assays", "collagen-IV-family-alpha2beta1 binding", "ligand_receptor_binding_or_activation", "alpha2beta1 collagen-IV adhesion", "reviewed_binding_only", "Native collagen-IV/fragments were not resolved to COL4A5; no downstream relay."),
        spec("M20A-EXT-0228", P+"10229657/; https://pmc.ncbi.nlm.nih.gov/articles/PMC2390958/", "human", "PC-3 cells and podocytes on collagen-IV matrices", "adhesion, blockade and immunoprecipitation", "collagen-IV matrix-alpha3beta1 adhesion", "ligand_receptor_binding_or_activation", "alpha3beta1 collagen-IV adhesion", "reviewed_binding_only", "Native network or alpha3-chain domains, not isolated COL4A5; no relay."),
        spec("M20A-EXT-0229", P+"11572855/; "+P+"7493650/", "human/bovine", "collagen-receptor comparisons", "affinity and subtype-binding assays", "no exact COL4A5-alpha9beta1 interaction recovered", "ligand_receptor_binding_or_activation", "alpha9beta1 ECM adhesion candidate", "reviewed_unresolved", "No chain-resolved COL4A5 or collagen-IV alpha9beta1 evidence."),
        spec("M20A-EXT-0230", P+"27033701/; https://pmc.ncbi.nlm.nih.gov/articles/PMC7328133/", "human", "recombinant alphaVbeta8 and latent-TGFbeta assays", "ligand-specificity and latent-TGFbeta activation", "alphaVbeta8-latent-TGFbeta activation, not COL4A5 binding", "ligand_receptor_binding_or_activation", "alphaVbeta8 latent-TGFbeta branch", "reviewed_unresolved", "No collagen-IV or COL4A5 interaction demonstrated."),
        spec("M20A-EXT-0231", P+"7949658/; https://doi.org/10.1093/glycob/4.3.327", "human/mouse", "human collagen-IV preparations; murine SDC1", "affinity co-electrophoresis", "native collagen-IV-family-SDC1 association", "ligand_receptor_binding_or_activation", "SDC1 collagen-IV matrix association", "reviewed_unresolved", "Binding was to collagen-IV material, not isolated COL4A5; no relay."),
        spec("M20A-EXT-0232", P+"32236637/; https://pmc.ncbi.nlm.nih.gov/articles/PMC4788096/", "human/mouse", "CD44 studies with HA/BMP or collagen-family context", "exact-pair search; no qualifying assay", "no exact COL4A6-CD44 interaction recovered", "ligand_receptor_binding_or_activation", "CD44 matrix-adhesion candidate", "reviewed_unresolved", "CD44 signaling evidence concerns HA or other matrix ligands."),
        spec("M20A-EXT-0233", P+"18231936/; https://pmc.ncbi.nlm.nih.gov/articles/PMC3890855/", "human/mouse", "platelet GPVI assays with fibrillar collagen I/II and collagen-IV-family preparations", "platelet adhesion and receptor-blocking assays", "no chain-resolved COL4A6-GPVI activation", "ligand_receptor_binding_or_activation", "GPVI-FcRgamma-Syk-PLCgamma2 platelet branch", "reviewed_unresolved", "GPVI evidence is mainly fibrillar collagen I/II; collagen-IV binding is disputed and not COL4A6-specific."),
        spec("M20A-EXT-0234", P+"11572855/; https://pmc.ncbi.nlm.nih.gov/articles/PMC5380659/", "human", "recombinant alpha10beta1 domains; collagen-IV/VI toolkit", "collagen-family binding assays", "collagen-IV-family-alpha10beta1 binding", "ligand_receptor_binding_or_activation", "alpha10beta1 basement-membrane collagen adhesion", "reviewed_binding_only", "Native collagen-IV or fragments were not chain-resolved; no relay."),
        spec("M20A-EXT-0235", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10404678/; https://pmc.ncbi.nlm.nih.gov/articles/PMC5380659/", "human", "recombinant alpha11beta1 and collagen-IV assemblies", "purified integrin binding", "collagen-IV-family-alpha11beta1 association", "ligand_receptor_binding_or_activation", "alpha11beta1 collagen-ECM adhesion", "reviewed_binding_only", "Multichain assemblies were used; isolated COL4A6 and signaling were not tested."),
        spec("M20A-EXT-0236", P+"9699516/; "+P+"9139675/", "human", "recombinant alpha1beta1 and collagen-IV fragments", "adhesion and I-domain assays", "collagen-IV-family-alpha1beta1 binding", "ligand_receptor_binding_or_activation", "alpha1beta1 collagen-IV adhesion", "reviewed_binding_only", "Fragment/network binding was not assigned to COL4A6."),
        spec("M20A-EXT-0237", P+"9699516/; "+P+"8344274/", "human", "collagen-IV fragments and purified alpha2beta1", "solid-phase and inhibition assays", "collagen-IV-family-alpha2beta1 binding", "ligand_receptor_binding_or_activation", "alpha2beta1 collagen-IV adhesion", "reviewed_binding_only", "Binding sites were not uniquely mapped to COL4A6."),
        spec("M20A-EXT-0238", P+"10229657/; https://pmc.ncbi.nlm.nih.gov/articles/PMC2390958/", "human", "PC-3 cells and podocytes on collagen-IV matrices", "adhesion and integrin blockade", "collagen-IV matrix-alpha3beta1 adhesion", "ligand_receptor_binding_or_activation", "alpha3beta1 collagen-IV adhesion", "reviewed_binding_only", "Native network or other collagen-IV domains were tested, not isolated COL4A6."),
        spec("M20A-EXT-0239", P+"11572855/; "+P+"7493650/", "human/bovine", "collagen-receptor comparisons", "affinity and subtype-binding assays", "no exact COL4A6-alpha9beta1 interaction recovered", "ligand_receptor_binding_or_activation", "alpha9beta1 collagen adhesion candidate", "reviewed_unresolved", "No convincing collagen-IV alpha9beta1 or COL4A6-specific evidence."),
        spec("M20A-EXT-0240", P+"27033701/; https://pmc.ncbi.nlm.nih.gov/articles/PMC7328133/", "human", "recombinant alphaVbeta8 and latent-TGFbeta systems", "ligand-specificity and latent-TGFbeta activation", "alphaVbeta8-latent-TGFbeta activation, not COL4A6 binding", "ligand_receptor_binding_or_activation", "alphaVbeta8 latent-TGFbeta branch", "reviewed_unresolved", "No exact collagen-IV/alphaVbeta8 interaction demonstrated."),
        spec("M20A-EXT-0241", P+"7949658/; https://doi.org/10.1093/glycob/4.3.327", "human/mouse", "human collagen-IV preparations; murine SDC1", "affinity co-electrophoresis", "native collagen-IV-family-SDC1 association", "ligand_receptor_binding_or_activation", "SDC1 collagen-IV matrix organization", "reviewed_unresolved", "No isolated COL4A6 or receptor-proximal relay evidence."),
        spec("M20A-EXT-0242", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4121998/; "+P+"2924798/", "human/mouse", "collagen-VI and CD44/HA literature", "cell-attachment and matrix studies", "no exact COL6A1-CD44 molecular interaction established", "ligand_receptor_binding_or_activation", "collagen-VI/CD44 matrix-adhesion candidate", "reviewed_unresolved", "CD44 evidence primarily concerns hyaluronan; collagen-VI studies do not resolve COL6A1-CD44."),
        spec("M20A-EXT-0243", "https://pmc.ncbi.nlm.nih.gov/articles/PMC1218415/; "+P+"25051961/", "human", "platelets and collagen-VI preparations", "platelet adhesion and receptor-blocking assays", "collagen-VI platelet interaction via GPIa/IIa, not GPVI", "ligand_receptor_binding_or_activation", "platelet collagen adhesion", "reviewed_unresolved", "No COL6A1-specific GPVI binding or activation was shown."),
        spec("M20A-EXT-0244", P+"11572855/; https://pmc.ncbi.nlm.nih.gov/articles/PMC5380659/", "human", "recombinant alpha10beta1 and collagen-VI/IV toolkit assays", "collagen-family binding assays", "collagen-VI-family-alpha10beta1 binding", "ligand_receptor_binding_or_activation", "alpha10beta1 collagen-VI adhesion", "reviewed_binding_only", "Native collagen-VI or non-chain-resolved material; no intracellular relay."),
        spec("M20A-EXT-0245", P+"11572855/; https://pmc.ncbi.nlm.nih.gov/articles/PMC5380659/", "human", "recombinant collagen-binding integrins", "collagen subtype comparisons", "no qualifying COL6A1-alpha11beta1 evidence recovered", "ligand_receptor_binding_or_activation", "alpha11beta1 collagen adhesion candidate", "reviewed_unresolved", "Alpha11beta1 evidence is strongest for fibrillar collagens; exact collagen-VI chain evidence was not established."),
        spec("M20A-EXT-0248", P+"37645762/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10462164/", "human", "VSMCs; collagen-VI-containing matrix/vesicles", "integrin proximity, adhesion and invasion assays", "collagen-VI-family-alpha3beta1 adhesion with functional motility output", "ligand_receptor_binding_or_activation", "alpha3beta1 collagen-VI adhesion/focal-adhesion branch", "reviewed_binding_only", "Collagen-VI assemblies/sEV presentation, not isolated COL6A1; relay was not chain-resolved."),
        spec("M20A-EXT-0249", P+"11572855/; https://pmc.ncbi.nlm.nih.gov/articles/PMC5380659/", "human", "recombinant integrin domains and collagen subtype comparisons", "collagen subtype-binding studies", "no exact COL6A1-alpha9beta1 interaction recovered", "ligand_receptor_binding_or_activation", "alpha9beta1 collagen adhesion candidate", "reviewed_unresolved", "Alpha9beta1 is not established here as a collagen-VI receptor."),
        spec("M20A-EXT-0250", P+"27033701/; https://pmc.ncbi.nlm.nih.gov/articles/PMC7328133/", "human", "recombinant alphaVbeta8 and latent-TGFbeta assays", "ligand-specificity and latent-TGFbeta activation", "alphaVbeta8-latent-TGFbeta activation, not COL6A1 binding", "ligand_receptor_binding_or_activation", "alphaVbeta8 latent-TGFbeta branch", "reviewed_unresolved", "No exact collagen-VI/alphaVbeta8 evidence identified."),
        spec("M20A-EXT-0251", P+"2924798/; https://pmc.ncbi.nlm.nih.gov/articles/PMC4121998/", "human/mouse", "collagen-VI cell-attachment and proteoglycan literature", "exact SDC1 search and matrix studies", "no exact COL6A1-SDC1 interaction established", "ligand_receptor_binding_or_activation", "collagen-VI proteoglycan/matrix association", "reviewed_unresolved", "Reported collagen-VI adhesion does not identify SDC1 or isolate COL6A1."),
        spec("M20A-EXT-0252", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4121998/; "+P+"2924798/", "human/mouse", "collagen-VI/CD44/HA literature", "collagen-VI chain attachment and CD44/HA studies", "no exact COL6A2-CD44 interaction established", "ligand_receptor_binding_or_activation", "collagen-VI/CD44 matrix-adhesion candidate", "reviewed_unresolved", "CD44 evidence primarily concerns HA; chain and receptor attribution are unresolved."),
        spec("M20A-EXT-0253", "https://pmc.ncbi.nlm.nih.gov/articles/PMC1218415/; "+P+"25051961/", "human", "platelets and collagen-VI preparations", "platelet adhesion and receptor-blocking assays", "collagen-VI platelet interaction via GPIa/IIa, not demonstrated GPVI signaling", "ligand_receptor_binding_or_activation", "platelet collagen adhesion", "reviewed_unresolved", "No COL6A2-specific GPVI binding or activation was established."),
    ]

    # Batch017 was written by the research agent with the full per-row audit fields.
    batch017_raw = read(AGENT017)
    batch017 = []
    for r in batch017_raw:
        batch017.append({"review_id": r["review_id"], "source_locators": r["stable_citations"],
                         "species": r["species"], "cell_type_model": r["cell_type_model"],
                         "assay_or_perturbation": r["assay_perturbation"], "relation_type": r["relation_type"],
                         "evidence_layer": r["primary_evidence_layer"], "pathway_branch": r["pathway_branch"],
                         "confidence_tier": "low", "terminal_tf_entities": r.get("terminal_TF", ""),
                         "review_status": r["status"], "curator_note": r["limitations"]})
    source_rows = batch016 + batch017
    if len(source_rows) != 50 or len({r["review_id"] for r in source_rows}) != 50:
        raise SystemExit("batches016_017 must contain 50 unique exact rows")

    pair_by_review = {r["module20a_review_id"]: r for r in pair_rows}
    tf_by_pair = {r["pair_key"]: r for r in tf_rows}
    assigned = {r["review_id"] for r in source_rows}
    if not assigned.issubset(pair_by_review):
        raise SystemExit(f"review IDs absent from scaffold: {sorted(assigned - set(pair_by_review))}")
    for rid in assigned:
        row = pair_by_review[rid]
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
    review_fields = ["review_id", "pair_key", "pair_label_canonical", "pathway_reuse_key", "evidence_id",
                     "source_locators", "species", "cell_type_model", "assay_or_perturbation", "relation_type",
                     "evidence_layer", "pathway_branch", "confidence_tier", "terminal_tf_entities", "review_status", "curator_note"]
    final_review = []
    new_reuse = []
    for s in source_rows:
        old = old_by_review.get(s["review_id"], {})
        has_reuse = s["review_status"] in {"reviewed_relay_candidate", "reviewed_function_only", "reviewed_scavenging_only"}
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
        existing_reuse.add(reuse_key); existing_evidence.add(evidence_id)
        pair = pair_by_review[s["review_id"]]
        pair["pathway_reuse_keys"] = reuse_key
        pair["module21a_edge_ids"] = "PENDING_M21A_EDGE_MATERIALIZATION" if has_reuse else ""
        pair["module21a_evidence_ids"] = evidence_id
        pair["terminal_tf_entities"] = s["terminal_tf_entities"]
        pair["module21a_status"] = s["review_status"]
        pair["module22a_status"] = "candidate_tf_handoff_pending_validation" if s["terminal_tf_entities"] else "no_terminal_tf_evidence"
        pair["search_boundary"] = "primary_review_batches016_017; exact chain-resolution boundary search"
        pair["curator_notes"] = s["curator_note"]
        tfrow = tf_by_pair[pair["pair_key"]]
        tfrow["pathway_reuse_keys"] = reuse_key
        tfrow["terminal_tf_entities"] = s["terminal_tf_entities"]
        tfrow["module21a_evidence_ids"] = evidence_id
        tfrow["handoff_status"] = "pending_tf_program_review" if s["terminal_tf_entities"] else "no_terminal_tf_assigned"
        tfrow["terminal_tf_status"] = "candidate_or_supported_activation" if s["terminal_tf_entities"] else "none_found"
        tfrow["search_boundary"] = "Primary downstream review batches016-017; exact chain-resolution search boundary."
        tfrow["limitations"] = s["curator_note"]
        if has_reuse:
            new_reuse.append({"pathway_reuse_key": reuse_key, "source_entity": s["pathway_branch"].split("-", 1)[0],
                              "pathway_name": s["pathway_branch"], "edge_ids": "", "evidence_ids": evidence_id,
                              "target_entities": "", "ligand_pair_count": "1", "ligand_pair_keys": pair["pair_key"],
                              "terminal_tf_entities": s["terminal_tf_entities"],
                              "validation_status": "reviewed_batches016_017_candidate",
                              "reuse_rule": "Reuse only when exact ligand/receptor complex, isoform/chain/cofactor, species, cell/model, assay and evidence scope match.",
                              "limitations": s["curator_note"]})
        detail_rows.append({"evidence_id": evidence_id, "pathway_reuse_key": reuse_key,
                            "source_locators": s["source_locators"], "species": s["species"],
                            "cell_type_model": s["cell_type_model"], "assay_or_perturbation": s["assay_or_perturbation"],
                            "relation_type": s["relation_type"], "evidence_layer": s["evidence_layer"],
                            "pathway_branch": s["pathway_branch"], "confidence_tier": s["confidence_tier"],
                            "evidence_summary": s["pathway_branch"], "limitations": s["curator_note"]})
        final_review.append({"review_id": s["review_id"], "pair_key": pair["pair_key"],
                             "pair_label_canonical": pair["pair_label_canonical"], "pathway_reuse_key": reuse_key,
                             "evidence_id": evidence_id, "source_locators": s["source_locators"], "species": s["species"],
                             "cell_type_model": s["cell_type_model"], "assay_or_perturbation": s["assay_or_perturbation"],
                             "relation_type": s["relation_type"], "evidence_layer": s["evidence_layer"],
                             "pathway_branch": s["pathway_branch"], "confidence_tier": s["confidence_tier"],
                             "terminal_tf_entities": s["terminal_tf_entities"], "review_status": s["review_status"],
                             "curator_note": s["curator_note"]})

    write(PAIR, list(pair_rows[0]), pair_rows)
    write(TF, list(tf_rows[0]), tf_rows)
    write(REUSE, list(reuse_rows[0]), reuse_rows + new_reuse)
    write(DETAIL, detail_fields, detail_rows)
    write(REVIEW, review_fields, final_review)
    print(f"integrated {len(final_review)} pair outcomes, {len(new_reuse)} reusable pathway candidates, and {len(final_review)} evidence records")


if __name__ == "__main__":
    main()
