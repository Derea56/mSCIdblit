#!/usr/bin/env python3
"""Stage conservative evidence findings for all Batch 017 pairs.

Batch 017 is a noncanonical-regulator slice.  Exact KMT2D->Abca1 and
GPS2->Abca1 observations are retained as chromatin/coregulator candidates,
not strict sequence-specific TF edges.  No canonical or Module 22B write is
performed.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_017/"
    "public_tf_evidence_collection_batch_017.tsv"
)
TF_LINK_URL = "https://tflink.net/download/#interaction-gmt"
PAIR_FIELDS = [
    "review_id", "batch_id", "batch_rank", "regulator_key", "regulator_symbol", "species_scope",
    "source_registry", "source_record_id", "raw_tf_symbol", "target_symbol", "target_graph_modules",
    "candidate_membership_status", "exact_pair_search_url", "exact_pair_status", "regulator_general_evidence_status",
    "target_cell_presence_status", "binding_or_association_status", "downstream_expression_or_perturbation_status",
    "downstream_activation_status", "upstream_relay_status", "disposition", "primary_citation",
    "corroborating_citation", "near_match_exclusions", "review_notes", "exportable", "canonical_write_performed",
]
EVIDENCE_FIELDS = [
    "evidence_id", "regulator_key", "regulator_symbol", "species_scope", "evidence_layer", "support_kind",
    "cell_or_model", "assay_or_perturbation", "observation", "effect_direction", "primary_citation",
    "corroborating_citation", "route_or_module_relevance", "target_pair_scope", "exportable",
    "canonical_write_performed", "limitations",
]


# symbol, primary regulator-level citation, corroborating citation, support kind,
# model, assay, observation, role relevance
REGULATORS = {
    "kdm4a": ("KDM4A/JMJD2A", "https://pubmed.ncbi.nlm.nih.gov/29383092/", "", "primary_literature_regulator_level", "human and mouse macrophage models", "oxLDL-induced macrophage polarization and KDM4A perturbation", "KDM4A is a chromatin modifier linked to inflammatory macrophage programs, not the queued targets.", "noncanonical chromatin regulator capacity only"),
    "rcor1": ("RCOR1/CoREST", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7108912/", "", "primary_literature_regulator_level", "mouse Treg and chromatin-corepressor models", "CoREST/LSD1/HDAC recruitment and Rcor1 loss", "RCOR1 corepressor evidence concerns Il2, Ifng, and Tbx1, not the queued targets.", "noncanonical transcriptional coregulator capacity only"),
    "gatad2a": ("GATAD2A/p66alpha", "https://pubmed.ncbi.nlm.nih.gov/21490301/", "https://www.encodeproject.org/experiments/ENCSR925BFV/", "primary_literature_regulator_level", "human NuRD/globin and ENCODE models", "MBD2-NuRD recruitment and ChIP-seq resource", "GATAD2A is a NuRD corepressor/scaffold; no queued-locus evidence was established.", "noncanonical chromatin coregulator capacity only"),
    "kmt2d": ("KMT2D/MLL4", "https://pubmed.ncbi.nlm.nih.gov/24368734/", "https://pubmed.ncbi.nlm.nih.gov/18372346/", "primary_literature_regulator_level", "mouse enhancer and chromatin models", "enhancer binding, H3K4 methylation, H3K27ac, Mediator/Pol II recruitment", "KMT2D/MLL4 has enhancer-regulator evidence; the exact Abca1 relationship is recorded separately as a noncanonical candidate.", "noncanonical chromatin coactivator capacity; exact Abca1 edge kept separate"),
    "smc1a": ("SMC1A", "https://pubmed.ncbi.nlm.nih.gov/26581180/", "https://pubmed.ncbi.nlm.nih.gov/23704192/", "primary_literature_regulator_level", "human and mouse cohesin/ChIA-PET models", "cohesin architecture, ChIA-PET, and Pol II/gene-expression studies", "SMC1A has chromatin-architecture evidence, not the queued target edges.", "noncanonical chromatin architecture capacity only"),
    "brd9": ("BRD9", "https://pubmed.ncbi.nlm.nih.gov/38102116/", "https://pubmed.ncbi.nlm.nih.gov/36332631/", "primary_literature_regulator_level", "human and mouse BRD9 chromatin models", "BRD9 loss, ChIP/ATAC, and 3D-chromatin analyses", "BRD9 perturbation changes chromatin accessibility and cell fate at other loci, not the queued targets.", "noncanonical chromatin regulator capacity only"),
    "dpf2": ("DPF2", "https://pubmed.ncbi.nlm.nih.gov/37200093/", "", "primary_literature_regulator_level", "human AML/BAF chromatin model", "DPF2 depletion and BAF/NRF2 occupancy", "DPF2 chromatin-cofactor evidence concerns NRF2-associated programs, not ABCA1 or ACKR regulation.", "noncanonical chromatin coregulator capacity only"),
    "ss18": ("SS18", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3307773/", "https://pubmed.ncbi.nlm.nih.gov/34215745/", "primary_literature_regulator_level", "human BAF-complex models", "TAP-MS/co-IP, CRISPR/rescue, and BAF ChIP-seq", "SS18 is a BAF-complex subunit with chromatin-regulatory activity at other loci, not the queued targets.", "noncanonical chromatin coregulator capacity only"),
    "cdk8": ("CDK8", "https://pubmed.ncbi.nlm.nih.gov/28855340/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2863696/", "primary_literature_regulator_level", "human CDK8/19 Mediator-kinase models", "inhibition/knockdown, Pol II elongation, and promoter co-recruitment", "CDK8 regulates transcriptional responses at IL8/CXCL and Dio1, not the queued targets.", "noncanonical transcriptional modifier capacity only"),
    "arid2": ("ARID2/BAF200", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9013128/", "https://pubmed.ncbi.nlm.nih.gov/32071245/", "primary_literature_regulator_level", "human PBAF and HCC models", "chromatin occupancy, perturbation, and DNMT1/Snail promoter repression", "ARID2 is a PBAF specificity subunit with regulator activity at other loci, not the queued targets.", "noncanonical chromatin-remodeler capacity only"),
    "aff4": ("AFF4", "https://pubmed.ncbi.nlm.nih.gov/22528490/", "https://pubmed.ncbi.nlm.nih.gov/40790766/", "primary_literature_regulator_level", "human SEC/transcription-elongation models", "SEC scaffold, AMPKalpha2 promoter activation, and PTEN promoter regulation", "AFF4 is a transcription-elongation scaffold; these nonqueued promoter findings do not transfer to the queued targets.", "noncanonical transcriptional coregulator capacity only"),
    "brd2": ("BRD2", "https://pubmed.ncbi.nlm.nih.gov/26349765/", "https://pubmed.ncbi.nlm.nih.gov/15548137/", "primary_literature_regulator_level", "human and mouse BET chromatin-reader models", "BRD2 binding and regulation at Pai-1/cyclin A plus mouse ChIP-seq resource", "BRD2 is a chromatin reader/cofactor; no queued target edge was independently verified.", "noncanonical chromatin-reader capacity only"),
    "med12": ("MED12", "https://pubmed.ncbi.nlm.nih.gov/27570068/", "https://pubmed.ncbi.nlm.nih.gov/27188461/", "primary_literature_regulator_level", "mouse Mediator/HSC and neural stem-cell models", "MED12 deletion, enhancer, Wnt, and neural-program studies", "MED12 is a Mediator kinase-module subunit; general coactivator evidence does not establish the queued targets.", "noncanonical transcriptional coregulator capacity only"),
    "ring1": ("RING1/RING1A", "https://pubmed.ncbi.nlm.nih.gov/9858531/", "https://pubmed.ncbi.nlm.nih.gov/9312051/", "primary_literature_regulator_level", "human and mouse Polycomb/PRC1 models", "Polycomb occupancy, repression, and developmental-locus studies", "RING1 is a Polycomb chromatin repressor; nonqueued developmental targets do not support the queued edges.", "noncanonical chromatin architecture/repressor capacity only"),
    "gatad2b": ("GATAD2B/p66beta", "https://pubmed.ncbi.nlm.nih.gov/28576827/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10796954/", "primary_literature_regulator_level", "human myometrial and NuRD models", "promoter recruitment with progesterone receptor and NuRD/GAND studies", "GATAD2B is a NuRD corepressor/scaffold with nonqueued promoter evidence.", "noncanonical transcriptional coregulator capacity only"),
    "dppa4": ("DPPA4", "https://pubmed.ncbi.nlm.nih.gov/30031967/", "https://pubmed.ncbi.nlm.nih.gov/20298437/", "primary_literature_regulator_level", "mouse ESC/embryonal and fibroblast models", "genome-wide ChIP-seq and pluripotency-associated chromatin studies", "DPPA4 has chromatin-associated occupancy at other loci, not the queued targets.", "noncanonical chromatin regulator capacity only"),
    "tet2": ("TET2/Tet2", "https://pubmed.ncbi.nlm.nih.gov/26287468/", "https://pubmed.ncbi.nlm.nih.gov/28826859/", "primary_literature_regulator_level", "mouse macrophage and inflammatory epigenetic models", "DNA-modification, HDAC2 recruitment, and inflammatory-program perturbation", "TET2 has inflammatory chromatin-regulator evidence, but the queued Abca1 perturbation result is non-supportive.", "noncanonical chromatin regulator capacity only; negative exact result retained"),
    "kdm2b": ("KDM2B", "https://pubmed.ncbi.nlm.nih.gov/31197256/", "https://pubmed.ncbi.nlm.nih.gov/23256043/", "primary_literature_regulator_level", "mouse and human Polycomb/CpG-island models", "Il6 promoter/chromatin regulation and Polycomb/CpG-island studies", "KDM2B has chromatin-regulator evidence at other targets, not the queued mouse genes.", "noncanonical chromatin regulator capacity only"),
    "smarcad1": ("SMARCAD1", "https://pubmed.ncbi.nlm.nih.gov/32160911/", "https://pubmed.ncbi.nlm.nih.gov/30902974/", "primary_literature_regulator_level", "mouse intestinal and embryonic-stem-cell models", "chromatin remodeling, heterochromatin, and gene-expression studies", "SMARCAD1 has chromatin-remodeling activity at other loci, not the queued targets.", "noncanonical chromatin-remodeler capacity only"),
    "gps2": ("GPS2", "https://pubmed.ncbi.nlm.nih.gov/30153049/", "https://pubmed.ncbi.nlm.nih.gov/19481530/", "primary_literature_regulator_level", "mouse macrophage and coregulator models", "coregulator/chromatin occupancy and inflammatory lipid-efflux studies", "GPS2 is a transcriptional coregulator with an exact Abca1 macrophage relationship recorded separately.", "noncanonical transcriptional coregulator; exact Abca1 edge kept separate"),
    "nelfa": ("NELFA/WHSC2", "https://pubmed.ncbi.nlm.nih.gov/12612062/", "https://pubmed.ncbi.nlm.nih.gov/21623364/", "primary_literature_regulator_level", "rat neuronal and biochemical NELF models", "NELF reconstitution, promoter occupancy, and depletion", "NELFA is a Pol II pausing complex subunit; nonqueued neuronal promoters do not support the queued mouse genes.", "noncanonical transcriptional modifier capacity only"),
    "h2az1": ("H2AZ1/H2AFZ", "https://pubmed.ncbi.nlm.nih.gov/33953180/", "", "primary_literature_regulator_level", "human H2A.Z chromatin models", "nucleosome architecture and depletion/accessibility studies", "H2A.Z regulates chromatin state but is not a sequence-specific TF for the queued genes.", "noncanonical chromatin-state regulator capacity only"),
    "supt5h": ("SUPT5H/SPT5", "https://pubmed.ncbi.nlm.nih.gov/9450929/", "https://pubmed.ncbi.nlm.nih.gov/36206739/", "primary_literature_regulator_level", "human DSIF/Pol II models", "processivity, pausing, and elongation studies", "SUPT5H is a DSIF transcription-elongation factor; no queued target edge was established.", "noncanonical transcriptional modifier capacity only"),
    "chd2": ("CHD2", "https://pubmed.ncbi.nlm.nih.gov/25621013/", "https://pubmed.ncbi.nlm.nih.gov/36115870/", "primary_literature_regulator_level", "human and mouse CHD2 chromatin models", "active-chromatin occupancy and nucleosome/H3.3 organization", "CHD2 affects chromatin organization at other loci, not the queued targets.", "noncanonical chromatin-remodeler capacity only"),
    "pcgf6": ("PCGF6", "https://pubmed.ncbi.nlm.nih.gov/28304275/", "", "primary_literature_regulator_level", "mouse ESC PRC1.6 model", "PRC1.6 repression and germ-cell-promoter de-repression", "PCGF6 has noncanonical PRC1.6 repression evidence, not evidence for the queued genes.", "noncanonical chromatin-repressor capacity only"),
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


def search_url(regulator: str, target: str, species: str) -> str:
    return "https://pubmed.ncbi.nlm.nih.gov/?term=" + quote_plus(f'"{regulator}" AND "{target}" AND {species}')


def classify(row: dict[str, str]) -> dict[str, str]:
    key = row["regulator_key"]
    target = row["target_symbol"].lower()
    info = REGULATORS[key]
    symbol, general_primary, general_corr, kind, model, assay, observation, relevance = info
    status = "database_membership_only_not_promotable"
    primary = TF_LINK_URL
    corr = ""
    cell = "not_established_for_exact_pair"
    binding = "TFLink_or_curated_database_membership_only"
    downstream = "not_found_for_exact_pair"
    disposition = "retain_as_staging_search_lead_only"
    exclusions = "Regulator-level evidence at nonqueued loci, orthologs, paralogs, reverse directions, co-models, and broad chromatin programs was not transferred to this exact pair."
    notes = "TFLink membership is a search lead only; it does not establish causal direction, target-cell presence, downstream activation, or upstream relay."

    if key == "kmt2d" and target == "abca1":
        status = "functional_chromatin_coregulator_promotion_candidate_not_strict_tf"
        primary = "https://pubmed.ncbi.nlm.nih.gov/18372346/"
        corr = "https://pmc.ncbi.nlm.nih.gov/articles/PMC2422828/"
        cell = "mouse_E9_5_MEF_model_not_SCI_target_cell"
        binding = "ASC2_MLL4_occupancy_at_Abca1_LXRE_and_H3K4me3"
        downstream = "LXR_ligand_increased_Abca1_and_MLL4_dependent_reporter_or_expression_response"
        disposition = "retain_noncanonical_chromatin_coactivator_candidate_pending_SCI_context"
        exclusions = "MLL3 and MLL4 are redundant and ASC-2 loss disrupts the complex; the study did not selectively test KMT2D alone in an SCI model."
        notes = "Mouse LXR/ASC-2/MLL4 assays support Abca1 chromatin activation, but this is a chromatin coactivator relationship rather than a strict sequence-specific TF edge."
    elif key == "gps2" and target == "abca1":
        status = "functional_noncanonical_coregulator_promotion_candidate_not_strict_tf"
        primary = "https://pubmed.ncbi.nlm.nih.gov/30153049/"
        binding = "GPS2_and_NFkB_p65_cooccupancy_at_Abca1_promoter_or_enhancers"
        downstream = "GPS2_loss_reduced_LPS_induced_Abca1_and_cholesterol_efflux"
        disposition = "retain_noncanonical_coregulator_candidate_pending_SCI_context"
        cell = "mouse_RAW_BMDM_and_peritoneal_macrophage_models_not_SCI_target_cell"
        exclusions = "GPS2 is a transcriptional coregulator rather than a sequence-specific DNA-binding TF; no SCI target-cell validation or independent second exact paper was found."
        notes = "GPS2 loss, Abca1 promoter/enhancer co-occupancy with NF-kB p65, and reduced lipid efflux support an exact module-relevant coregulator relationship, not a canonical TF promotion."
    elif key == "tet2" and target == "abca1":
        status = "exact_perturbation_non_supportive_not_promotable"
        primary = "https://pubmed.ncbi.nlm.nih.gov/28104796/"
        corr = "https://pubmed.ncbi.nlm.nih.gov/32160545/"
        cell = "mouse_macrophage_atherosclerosis_and_hematopoietic_co_model_not_SCI_target_cell"
        binding = "no_TET2_Abca1_locus_binding_established"
        downstream = "Tet2_deficiency_showed_no_significant_Abca1_change_in_reported_cholesterol_trafficking_panel"
        disposition = "retain_negative_exact_perturbation_result_separately"
        notes = "The exact mouse perturbation was non-supportive for Abca1; a separate Abca1/Tet2 co-model does not establish Tet2 regulation of Abca1."
    elif key == "h2az1" and target == "actr2":
        status = "network_cooccurrence_only_not_promotable"
        primary = "https://pubmed.ncbi.nlm.nih.gov/35116276/"
        binding = "no_H2AZ1_ACTR2_binding_or_promoter_assay_established"
        downstream = "PPI_or_hub_gene_cooccurrence_only"
        disposition = "retain_network_cooccurrence_separately"
        notes = "H2AFZ and ACTR2 co-occur in a network analysis, but no regulatory assay, direction, or causal relationship was shown."
    elif key in {"kmt2d", "gps2"}:
        status = "database_membership_only_not_promotable"
        notes = "The exact module-relevant relationship was found only for the separately recorded Abca1 row; other queued targets remain TFLink leads."
    elif key in {"tet2", "h2az1"}:
        status = "chromatin_regulator_database_only_not_tf_promotable"
        disposition = "retain_noncanonical_chromatin_regulator_candidate_separately"
        binding = "chromatin_regulator_database_membership_only"
        notes = "General chromatin evidence is retained for the noncanonical category; it does not establish this exact queued target edge."
    else:
        status = "chromatin_or_transcriptional_machinery_database_only_not_promotable"
        disposition = "retain_noncanonical_regulator_candidate_separately"
        binding = "chromatin_or_transcriptional_machinery_database_membership_only"
        notes = "This candidate is retained in the noncanonical chromatin/cofactor/machinery category; database membership and regulator-level literature do not establish this exact target edge."

    return {
        "symbol": symbol, "general_primary": general_primary, "general_corr": general_corr, "kind": kind,
        "model": model, "assay": assay, "observation": observation, "relevance": relevance,
        "status": status, "primary": primary, "corr": corr, "cell": cell, "binding": binding,
        "downstream": downstream, "disposition": disposition, "exclusions": exclusions, "notes": notes,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_BATCH.parent)
    args = parser.parse_args()
    rows = read_tsv(args.batch)
    if len(rows) != 100:
        raise SystemExit(f"expected 100 rows, found {len(rows)}")

    pairs: list[dict[str, str]] = []
    evidence: list[dict[str, str]] = []
    seen: set[str] = set()
    for row in rows:
        key = row["regulator_key"]
        if key not in REGULATORS:
            raise SystemExit(f"missing evidence map for {key}")
        info = classify(row)
        pairs.append({
            "review_id": f"public_tf_evidence_batch017_pair_{int(row['batch_rank']):02d}_{row['target_rank']}",
            "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key,
            "regulator_symbol": info["symbol"], "species_scope": row["species_scope"],
            "source_registry": row["source_registry"], "source_record_id": row["source_record_id"],
            "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"],
            "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": search_url(row["raw_tf_symbol"], row["target_symbol"], row["species_scope"]),
            "exact_pair_status": info["status"], "regulator_general_evidence_status": "supported_general_or_authoritative_regulator_evidence",
            "target_cell_presence_status": info["cell"], "binding_or_association_status": info["binding"],
            "downstream_expression_or_perturbation_status": info["downstream"], "downstream_activation_status": "not_established_for_SCI_target_cell",
            "upstream_relay_status": "not_tested_for_exact_pair", "disposition": info["disposition"],
            "primary_citation": info["primary"], "corroborating_citation": info["corr"], "near_match_exclusions": info["exclusions"],
            "review_notes": info["notes"] + " " + info["observation"], "exportable": "false", "canonical_write_performed": "false",
        })
        if key not in seen:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch017_regulator_{key}", "regulator_key": key,
                "regulator_symbol": info["symbol"], "species_scope": row["species_scope"],
                "evidence_layer": "regulator_identity_and_regulatory_capacity", "support_kind": info["kind"],
                "cell_or_model": info["model"], "assay_or_perturbation": info["assay"], "observation": info["observation"],
                "effect_direction": "queued-pair direction not established except explicitly recorded exact noncanonical or negative findings",
                "primary_citation": info["general_primary"], "corroborating_citation": info["general_corr"],
                "route_or_module_relevance": info["relevance"], "target_pair_scope": "not evidence for unrelated queued exact pairs; no upstream relay inferred",
                "exportable": "false", "canonical_write_performed": "false",
                "limitations": "Regulator-level evidence does not establish SCI target-cell presence, exact queued-target direction, downstream activation, or upstream relay. Chromatin-associated and transcriptional-machinery evidence is retained separately from canonical promoter-TF evidence.",
            })
            seen.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch017_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch017_regulator_register.tsv"
    summary_path = args.output_dir / "batch_017_evidence_review_summary.json"
    report_path = args.output_dir / "EVIDENCE_REVIEW_BATCH017.md"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    status_counts: dict[str, int] = {}
    for item in pairs:
        status_counts[item["exact_pair_status"]] = status_counts.get(item["exact_pair_status"], 0) + 1
    pair_keys = {(item["regulator_key"], item["target_symbol"], item["species_scope"], item["source_record_id"]) for item in pairs}
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_017", "source_set_ranks_reviewed": list(range(1, 26)),
        "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen), "unique_provenance_aware_pairs": len(pair_keys),
        "exact_pair_status_counts": status_counts, "regulator_register_rows": len(evidence),
        "strict_tf_promotion_candidate_rows": 0, "noncanonical_exact_candidate_rows": status_counts.get("functional_chromatin_coregulator_promotion_candidate_not_strict_tf", 0) + status_counts.get("functional_noncanonical_coregulator_promotion_candidate_not_strict_tf", 0),
        "exportable_pair_rows": 0, "canonical_writes_performed": False, "module22b_promotions_performed": False, "provenance_preserved": True,
        "limitations": ["TFLink membership is a search lead, not causal regulation.", "Exact pair negatives are bounded-search results, not global absence.", "KMT2D and GPS2 Abca1 findings are noncanonical chromatin/coregulator evidence and are not strict TF promotions.", "TET2 Abca1 was explicitly non-supportive and was not promoted.", "No canonical or Module 22B write was performed."],
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path.write_text("\n".join([
        "# Evidence review: public TF batch 017", "", "Reviewed 100 exact regulator-target-species pairs across 25 selected source-set ranks.", "",
        f"- **{len(pairs)}** pairs were reviewed across **{len(seen)}** regulators.",
        f"- **{summary['noncanonical_exact_candidate_rows']}** exact noncanonical chromatin/coregulator candidates were staged: KMT2D-to-Abca1 and GPS2-to-Abca1.",
        f"- **{status_counts.get('exact_perturbation_non_supportive_not_promotable', 0)}** exact perturbation result was non-supportive (TET2-to-Abca1).",
        f"- **{status_counts.get('network_cooccurrence_only_not_promotable', 0)}** network co-occurrence row was kept separate.",
        f"- **{status_counts.get('chromatin_or_transcriptional_machinery_database_only_not_promotable', 0) + status_counts.get('chromatin_regulator_database_only_not_tf_promotable', 0)}** chromatin/cofactor/machinery rows remained noncanonical database leads.",
        "- **0** strict TF promotion candidates, exportable rows, canonical writes, or Module 22B writes.", "",
        "All rows retain the original TFLink source record, raw symbol, species, target, graph-module mapping, and local source snapshot. General chromatin and cofactor literature is recorded separately from exact pair evidence.", "",
    ]) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
