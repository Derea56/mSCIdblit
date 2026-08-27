#!/usr/bin/env python3
"""Stage conservative evidence findings for all Batch 016 pairs.

This batch is intentionally non-exportable.  It is dominated by TFLink leads,
chromatin regulators, and indirect perturbation associations.  None of those
are written as canonical Module 22B TF edges here.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_016/"
    "public_tf_evidence_collection_batch_016.tsv"
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
    "zgpat": (
        "ZGPAT", "https://pubmed.ncbi.nlm.nih.gov/19644445/", "https://doi.org/10.1038/emboj.2009.211",
        "primary_literature_regulator_level", "human promoter/chromatin-corepressor model",
        "DNA binding, EGFR promoter luciferase, ChIP/re-ChIP, NuRD recruitment",
        "ZGPAT has sequence-specific promoter and corepressor evidence at EGFR, not at the queued targets.",
        "dual-role TF/chromatin capacity only; no queued target edge",
    ),
    "prdm6": (
        "PRDM6", "https://pubmed.ncbi.nlm.nih.gov/16537907/", "https://doi.org/10.1128/MCB.26.7.2626-2636.2006",
        "primary_literature_regulator_level", "human PRDM6 repression/chromatin model",
        "GAL4 reporter repression, HDAC/G9a interaction, SMC perturbation",
        "PRDM6 has regulator-level repression and chromatin evidence, not evidence for the queued targets.",
        "dual-role TF/chromatin capacity only; no queued target edge",
    ),
    "mga": (
        "MGA", "https://pubmed.ncbi.nlm.nih.gov/10601024/", "https://pubmed.ncbi.nlm.nih.gov/34236315/",
        "primary_literature_regulator_level", "human and mouse E-box/ncPRC1.6 models",
        "E-box/T-box DNA binding, reporter regulation, promoter co-occupancy, CRISPR loss",
        "MGA has DNA-binding and ncPRC1.6 transcriptional-regulator evidence, not evidence for ABCA1, ACTR2, ADAM17, or ADIPOR2.",
        "dual-role TF/chromatin capacity only; no queued target edge",
    ),
    "prdm4": (
        "PRDM4", "https://pubmed.ncbi.nlm.nih.gov/33846573/", "https://pubmed.ncbi.nlm.nih.gov/23048031/",
        "primary_literature_regulator_level", "human promoter and epigenetic PRDM4 models",
        "PTEN dual-luciferase/qChIP; PRMT5/H4R3 methylation studies",
        "PRDM4 has promoter and epigenetic regulator evidence at nonqueued targets, not at the queued targets.",
        "dual-role TF/chromatin capacity only; no queued target edge",
    ),
    "prdm9": (
        "PRDM9", "https://pubmed.ncbi.nlm.nih.gov/22028627/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5705219/",
        "primary_literature_regulator_level", "mouse and human meiotic chromatin models",
        "sequence-specific hotspot binding and H3K4me3 enrichment",
        "PRDM9 evidence is centered on meiotic recombination hotspots, not canonical regulation of the queued targets.",
        "chromatin-associated regulator capacity only; no queued target edge",
    ),
    "znf711": (
        "ZNF711", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2989439/", "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF711_TARGET_GENES.html",
        "authoritative_binding_dataset_only", "human SH-SY5Y and GTRD-derived target-set models",
        "ChIP-seq occupancy and promoter target-set membership",
        "ZNF711 has broad regulator-level occupancy evidence; the four queued rows are aggregate occupancy leads without target-specific functional validation.",
        "strict TF occupancy lead only; no queued causal edge",
    ),
    "prdm12": (
        "PRDM12", "https://pubmed.ncbi.nlm.nih.gov/35464160/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4631751/",
        "authoritative_binding_dataset_only", "mouse P19 and Xenopus developmental models",
        "developmental perturbation, ChIP-seq occupancy, and target-gene expression studies",
        "PRDM12 has developmental regulator and occupancy evidence at other targets; the queued rows remain aggregate target-set leads.",
        "strict TF occupancy lead only; no queued causal edge",
    ),
    "brd4": (
        "BRD4", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10435483/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7310347/",
        "primary_literature_regulator_level", "human and mouse BET/chromatin perturbation models",
        "BRD4 ChIP-Rx, acute degradation, stimulus-responsive ChIP-seq, and BET inhibition",
        "BRD4 has broad enhancer/chromatin occupancy and transcriptional-control evidence; the queued target associations are indirect or database-derived.",
        "chromatin-associated regulator capacity; indirect target associations kept separate",
    ),
    "rad21": (
        "RAD21/Rad21", "https://pubmed.ncbi.nlm.nih.gov/25030696/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5961189/",
        "primary_literature_regulator_level", "human and mouse cohesin/chromatin-architecture models",
        "RAD21 ChIP, 3C, enhancer-promoter architecture, and functional enhancer validation at nonqueued genes",
        "RAD21 has cohesin architecture and gene-regulation evidence, but no queued A2M/ABCA1/ACKR edge was established.",
        "chromatin architecture capacity only; no queued target edge",
    ),
    "stag1": (
        "STAG1/SA1", "https://pubmed.ncbi.nlm.nih.gov/29867216/", "",
        "primary_literature_regulator_level", "human cohesin-SA1 model",
        "cohesin architecture and gene-regulatory studies",
        "STAG1/SA1 is a cohesin component; general chromatin regulation does not establish the queued target edges.",
        "chromatin architecture capacity only; no queued target edge",
    ),
    "smc3": (
        "SMC3", "https://pubmed.ncbi.nlm.nih.gov/32253279/", "",
        "primary_literature_regulator_level", "human cohesin model",
        "cohesin chromatin-architecture studies",
        "SMC3 has chromatin-architecture evidence, not target-specific regulation of the queued genes.",
        "chromatin architecture capacity only; no queued target edge",
    ),
    "smc1a": (
        "SMC1A/Smc1a", "https://pubmed.ncbi.nlm.nih.gov/23704192/", "",
        "primary_literature_regulator_level", "mouse limb cohesin/ChIA-PET model",
        "ChIA-PET-associated regulatory interactions",
        "SMC1A-associated chromatin interactions were reported at other loci; no queued target direction was established.",
        "chromatin architecture capacity only; no queued target edge",
    ),
    "mbd4": (
        "MBD4", "https://pubmed.ncbi.nlm.nih.gov/23316048/", "",
        "primary_literature_regulator_level", "human DNA-repair/methyl-CpG model",
        "methyl-CpG recognition and DNA-glycosylase studies",
        "MBD4 DNA-repair and methyl-CpG biology does not establish regulation of the queued targets.",
        "DNA-repair/chromatin-associated capacity only; no queued target edge",
    ),
    "cdk9": (
        "CDK9", "https://pubmed.ncbi.nlm.nih.gov/9857195/", "",
        "primary_literature_regulator_level", "human P-TEFb transcription-elongation model",
        "CDK9/P-TEFb transcriptional elongation studies",
        "Global transcription-elongation activity does not establish A2M, ABCA1, ACKR2, or ACKR3 target regulation.",
        "transcriptional machinery capacity only; no queued target edge",
    ),
    "kdm1a": (
        "KDM1A/LSD1", "https://pubmed.ncbi.nlm.nih.gov/38152966/", "https://pubmed.ncbi.nlm.nih.gov/33811891/",
        "primary_literature_regulator_level", "human neural-stem-cell and mouse atherosclerosis models",
        "KDM1A ChIP-seq/inhibition and pathway perturbation studies",
        "KDM1A has epigenetic and pathway-regulator evidence; only the separately recorded Abca1/Ackr3 associations are indirect.",
        "chromatin-associated regulator capacity; indirect target associations kept separate",
    ),
    "ints11": (
        "INTS11", "https://pubmed.ncbi.nlm.nih.gov/32697989/", "",
        "primary_literature_regulator_level", "human Integrator/PRO-seq model",
        "depletion and PRO-seq studies of pause release, elongation, and eRNA termination",
        "INTS11 is an RNA-processing/transcriptional-termination factor; no queued target edge was established.",
        "transcriptional/RNA-processing machinery capacity only; no queued target edge",
    ),
    "tet1": (
        "TET1/Tet1", "https://pubmed.ncbi.nlm.nih.gov/24050401/", "https://pubmed.ncbi.nlm.nih.gov/27916660/",
        "primary_literature_regulator_level", "mouse neuronal and developmental epigenetic models",
        "knockout/isoform studies of DNA demethylation, imprint erasure, and gene expression",
        "TET1 has epigenetic regulator evidence at developmental targets, not at the queued target genes.",
        "chromatin-associated regulator capacity only; no queued target edge",
    ),
    "kmt2b": (
        "KMT2B/MLL2", "https://pubmed.ncbi.nlm.nih.gov/23426673/", "https://pubmed.ncbi.nlm.nih.gov/30504434/",
        "primary_literature_regulator_level", "human and mouse H3K4-methyltransferase models",
        "conditional deletion and chromatin-dependent transcriptional-program studies",
        "KMT2B has chromatin-dependent transcriptional regulation evidence at nonqueued programs, not at the queued targets.",
        "chromatin-associated regulator capacity only; no queued target edge",
    ),
    "kdm2b": (
        "KDM2B", "https://pubmed.ncbi.nlm.nih.gov/26808549/", "https://maayanlab.cloud/Harmonizome/gene_set/KDM2B-26808549-CHIP-SEQ-SUP-B15-HUMAN/ChEA%2BTranscription%2BFactor%2BTargets%2B2022",
        "authoritative_binding_dataset_only", "human KDM2B ChIP-seq target-set model",
        "processed ChIP-seq target-set occupancy",
        "KDM2B occupancy has a queued ACKR2 target-set lead; no direction, perturbation, reporter, or endogenous validation was found.",
        "chromatin-modifier occupancy only; not a sequence-specific TF edge",
    ),
    "rbbp5": (
        "RBBP5", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6821195/", "",
        "chromatin_regulator_context_only", "human SET1/MLL H3K4-methyltransferase-complex model",
        "chromatin-complex scaffold and histone-methyltransferase studies",
        "RBBP5 is a chromatin-complex scaffold; database membership does not establish promoter binding or target regulation.",
        "noncanonical chromatin regulator category; not Module 22B promoter-TF evidence",
    ),
    "brd2": (
        "BRD2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3826993/", "",
        "chromatin_regulator_context_only", "human BET chromatin-reader model",
        "BET bromodomain/chromatin-reader and promoter-regulation studies",
        "BRD2 is a chromatin reader/cofactor; general BET evidence does not validate the queued target edges.",
        "noncanonical chromatin regulator category; not Module 22B promoter-TF evidence",
    ),
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
    symbol, general_primary, general_corr, kind, model, assay, observation, relevance = REGULATORS[key]

    status = "database_membership_only_not_promotable"
    primary = TF_LINK_URL
    corr = ""
    binding = "TFLink_or_curated_database_membership_only"
    downstream = "not_found_for_exact_pair"
    disposition = "retain_as_staging_search_lead_only"
    cell = "not_established_for_exact_pair"
    exclusions = "Regulator-level evidence at nonqueued targets, orthologs, paralogs, reverse directions, and broad chromatin programs was not transferred to this exact pair."
    notes = "TFLink membership is a search lead only; it does not establish causal direction, target-cell presence, downstream activation, or upstream relay."

    if key in {"znf711", "prdm12"}:
        status = "binding_dataset_only_not_promotable"
        primary = "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/" + ("ZNF711_TARGET_GENES.html" if key == "znf711" else "PRDM12_TARGET_GENES.html")
        corr = "https://pubmed.ncbi.nlm.nih.gov/27924024/"
        binding = "species_matched_aggregate_promoter_occupancy_target_set_lead"
        notes = "The source target set is derived from aggregate ChIP-seq promoter occupancy; it does not establish target-specific direction, perturbation, or causal function."
    elif key == "kdm2b" and target == "ackr2":
        status = "chromatin_occupancy_only_not_tf_promotable"
        primary = "https://pubmed.ncbi.nlm.nih.gov/26808549/"
        corr = "https://maayanlab.cloud/Harmonizome/gene_set/KDM2B-26808549-CHIP-SEQ-SUP-B15-HUMAN/ChEA%2BTranscription%2BFactor%2BTargets%2B2022"
        binding = "KDM2B_ChIP_target_set_occupancy_only"
        downstream = "not_found_for_exact_pair"
        disposition = "retain_noncanonical_chromatin_regulator_candidate_separately"
        notes = "KDM2B-ACKR2 is a processed ChIP-seq occupancy lead without direction, perturbation, reporter, or endogenous target validation; it is not a sequence-specific TF edge."
    elif key == "brd4" and target == "abca1":
        status = "perturbation_association_without_direct_binding_not_promotable"
        primary = "https://pubmed.ncbi.nlm.nih.gov/39990894/"
        corr = "https://pmc.ncbi.nlm.nih.gov/articles/PMC11843129/"
        binding = "no_BRD4_Abca1_locus_binding_established"
        downstream = "pan_BET_or_BRD4_perturbation_associated_Abca1_increase_in_mouse_renal_model"
        disposition = "retain_indirect_perturbation_association_separately"
        cell = "mouse_db_db_renal_model_not_SCI_target_cell"
        notes = "Apabetalone or BRD4 perturbation was associated with increased Abca1, alongside PPAR-gamma/LXR changes, but no locus occupancy or Abca1-specific causal rescue was shown."
    elif key == "brd4" and target == "a2m":
        status = "perturbation_association_without_direct_binding_not_promotable"
        primary = "https://pubmed.ncbi.nlm.nih.gov/32821285/"
        corr = "https://pmc.ncbi.nlm.nih.gov/articles/PMC7416228/"
        binding = "no_BRD4_A2m_locus_binding_established"
        downstream = "pan_BET_perturbation_associated_A2m_suppression_in_mouse_liver_LPS_model"
        disposition = "retain_indirect_perturbation_association_separately"
        cell = "mouse_LPS_liver_model_not_SCI_target_cell"
        notes = "Apabetalone suppressed A2m in a mouse LPS model, but the study did not establish A2m-locus BRD4 binding or BRD4-selective target causality."
    elif key == "kdm1a" and target == "abca1":
        status = "indirect_pathway_association_without_direct_binding_not_promotable"
        primary = "https://pubmed.ncbi.nlm.nih.gov/33811891/"
        binding = "no_KDM1A_Abca1_locus_binding_established"
        downstream = "KDM1A_pathway_perturbation_associated_with_PPARgamma_LXR_ABCA1_changes"
        disposition = "retain_indirect_pathway_association_separately"
        cell = "mouse_atherosclerosis_and_RAW264_7_models_not_SCI_target_cell"
        notes = "KDM1A perturbation was associated with the PPAR-gamma/LXR/ABCA1 pathway, but no Abca1-locus binding, promoter assay, or direct rescue was shown."
    elif key == "kdm1a" and target == "ackr3":
        status = "perturbation_association_without_direct_binding_not_promotable"
        primary = "https://maayanlab.cloud/Harmonizome/gene_set/Perturb_13560_OE_Kdm1a_SRP105108/PerturbAtlas%2BSignatures%2Bof%2BDifferentially%2BExpressed%2BGenes%2Bfor%2BMouse%2BGene%2BPerturbations"
        binding = "no_KDM1A_Ackr3_locus_binding_established"
        downstream = "Kdm1a_overexpression_associated_with_reduced_Ackr3_in_mouse_C2C12_signature"
        disposition = "retain_indirect_perturbation_association_separately"
        cell = "mouse_C2C12_signature_not_SCI_target_cell"
        notes = "A perturbation signature associates Kdm1a overexpression with Ackr3 reduction, but no occupancy, promoter assay, rescue, or SCI-relevant model was established."
    elif key in {"rbbp5", "brd2"}:
        status = "chromatin_regulator_database_only_not_tf_promotable"
        disposition = "retain_noncanonical_chromatin_regulator_candidate_separately"
        binding = "chromatin_regulator_or_reader_database_membership_only"
        notes = "This candidate is retained for the separate chromatin/regulatory-capacity category; database membership and general chromatin biology are not promoter-TF evidence for this pair."
    elif key in {"stag1", "smc3", "smc1a", "mbd4", "cdk9", "ints11", "tet1", "kmt2b", "kdm1a"}:
        status = "chromatin_or_transcriptional_machinery_database_only_not_promotable"
        disposition = "retain_noncanonical_chromatin_regulator_candidate_separately"
        binding = "chromatin_or_transcriptional_machinery_database_membership_only"
        notes = "General chromatin/transcriptional-machinery evidence supports regulator capacity only; it does not establish this exact regulator-target edge."
    elif key in {"zgpat", "prdm6", "mga", "prdm4", "prdm9"}:
        status = "database_membership_only_not_promotable"
        notes = "The regulator has literature-level DNA-binding/chromatin evidence at other loci, but TFLink membership alone does not establish this queued exact target edge."

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
            "review_id": f"public_tf_evidence_batch016_pair_{int(row['batch_rank']):02d}_{row['target_rank']}",
            "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key,
            "regulator_symbol": info["symbol"], "species_scope": row["species_scope"],
            "source_registry": row["source_registry"], "source_record_id": row["source_record_id"],
            "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"],
            "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": search_url(row["raw_tf_symbol"], row["target_symbol"], row["species_scope"]),
            "exact_pair_status": info["status"],
            "regulator_general_evidence_status": "supported_general_or_authoritative_regulator_evidence",
            "target_cell_presence_status": info["cell"], "binding_or_association_status": info["binding"],
            "downstream_expression_or_perturbation_status": info["downstream"],
            "downstream_activation_status": "not_established_for_SCI_target_cell",
            "upstream_relay_status": "not_tested_for_exact_pair", "disposition": info["disposition"],
            "primary_citation": info["primary"], "corroborating_citation": info["corr"],
            "near_match_exclusions": info["exclusions"], "review_notes": info["notes"] + " " + info["observation"],
            "exportable": "false", "canonical_write_performed": "false",
        })
        if key not in seen:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch016_regulator_{key}", "regulator_key": key,
                "regulator_symbol": info["symbol"], "species_scope": row["species_scope"],
                "evidence_layer": "regulator_identity_and_regulatory_capacity", "support_kind": info["kind"],
                "cell_or_model": info["model"], "assay_or_perturbation": info["assay"],
                "observation": info["observation"],
                "effect_direction": "queued-pair direction not established except explicitly recorded indirect associations",
                "primary_citation": info["general_primary"], "corroborating_citation": info["general_corr"],
                "route_or_module_relevance": info["relevance"],
                "target_pair_scope": "not evidence for unrelated queued exact pairs; no upstream relay inferred",
                "exportable": "false", "canonical_write_performed": "false",
                "limitations": "Regulator-level evidence does not establish SCI target-cell presence, exact queued-target direction, downstream activation, or upstream relay. Chromatin-associated and transcriptional-machinery evidence is retained separately from canonical promoter-TF evidence.",
            })
            seen.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch016_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch016_regulator_register.tsv"
    summary_path = args.output_dir / "batch_016_evidence_review_summary.json"
    report_path = args.output_dir / "EVIDENCE_REVIEW_BATCH016.md"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)

    status_counts: dict[str, int] = {}
    for item in pairs:
        status_counts[item["exact_pair_status"]] = status_counts.get(item["exact_pair_status"], 0) + 1
    pair_keys = {(item["regulator_key"], item["target_symbol"], item["species_scope"], item["source_record_id"]) for item in pairs}
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_016",
        "source_set_ranks_reviewed": list(range(1, 26)), "pair_rows_reviewed": len(pairs),
        "unique_regulators_reviewed": len(seen), "unique_provenance_aware_pairs": len(pair_keys),
        "exact_pair_status_counts": status_counts, "regulator_register_rows": len(evidence),
        "exact_pair_support_rows": 0, "promotion_candidate_rows": 0,
        "partial_or_near_match_rows": sum(v for k, v in status_counts.items() if "near_match" in k or "association" in k or "occupancy" in k),
        "binding_dataset_only_not_promotable_rows": status_counts.get("binding_dataset_only_not_promotable", 0),
        "database_membership_only_not_promotable_rows": status_counts.get("database_membership_only_not_promotable", 0),
        "chromatin_or_machinery_rows": sum(v for k, v in status_counts.items() if "chromatin" in k or "machinery" in k),
        "exportable_pair_rows": 0, "canonical_writes_performed": False, "module22b_promotions_performed": False,
        "provenance_preserved": True,
        "limitations": [
            "TFLink/GTRD/HTRI membership or aggregate occupancy is not causal regulation.",
            "Indirect pan-BET or pathway perturbation associations are not direct regulator-target edges.",
            "Chromatin architecture, readers, writers, DNA repair, and transcriptional machinery are retained separately from strict promoter-TF evidence.",
            "Exact pair negatives are bounded-search results, not global absence.",
            "No canonical or Module 22B write was performed.",
        ],
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path.write_text("\n".join([
        "# Evidence review: public TF batch 016", "",
        "Reviewed 100 exact regulator-target-species pairs across 25 selected source-set ranks.", "",
        f"- **{len(pairs)}** pairs were reviewed across **{len(seen)}** regulators.",
        f"- **{status_counts.get('binding_dataset_only_not_promotable', 0)}** rows were aggregate binding/occupancy leads only.",
        f"- **{status_counts.get('database_membership_only_not_promotable', 0)}** rows were TFLink/database membership leads only.",
        f"- **{summary['chromatin_or_machinery_rows']}** rows were chromatin-associated or transcriptional-machinery candidates and remain outside strict Module 22B TF evidence.",
        f"- **{summary['partial_or_near_match_rows']}** rows had limited indirect perturbation or occupancy-only associations; none met the direct TF promotion threshold.",
        "- **0** rows are exportable; no canonical or Module 22B writes were performed.", "",
        "The useful findings in this batch are regulator-level or indirect: ZNF711/PRDM12 aggregate promoter occupancy, BRD4-associated A2m/Abca1 expression responses, KDM2B-ACKR2 processed occupancy, and general chromatin/transcriptional-machinery evidence. None establishes exact target-cell presence, direct causal direction, downstream activation, or upstream relay in the SCI mechanism graph.", "",
    ]) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
