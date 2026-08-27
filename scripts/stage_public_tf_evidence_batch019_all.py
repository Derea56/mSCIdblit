#!/usr/bin/env python3
"""Stage conservative evidence findings for all Batch 019 pairs."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_019/"
    "public_tf_evidence_collection_batch_019.tsv"
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
    "prmt1": ("PRMT1", "https://pubmed.ncbi.nlm.nih.gov/18413343/", "", "primary_literature_regulator_level", "human chromatin/coactivator models", "PRMT1/CARM1 ChIP, reporter, and cytokine-responsive promoter studies", "PRMT1 has chromatin/coactivator evidence at nonqueued loci; a nonspecific PRMT inhibitor affected ABCA1 separately.", "noncanonical chromatin enzyme capacity only"),
    "phf5a": ("PHF5A", "https://pubmed.ncbi.nlm.nih.gov/18758164/", "https://pubmed.ncbi.nlm.nih.gov/12054543/", "primary_literature_regulator_level", "mouse spliceosomal/nuclear models", "U2AF1/SFRS5/EP400/DDX1 interaction and spliceosomal studies", "PHF5A is a nuclear spliceosomal/bridge protein, not a sequence-specific TF for the queued targets.", "noncanonical nuclear machinery capacity only"),
    "larp7": ("LARP7", "https://pubmed.ncbi.nlm.nih.gov/18281698/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2367717/", "primary_literature_regulator_level", "human 7SK/P-TEFb models", "7SK snRNP, P-TEFb availability, and Pol II elongation studies", "LARP7 controls 7SK/P-TEFb dynamics; no queued target edge was established.", "noncanonical transcriptional elongation capacity only"),
    "smyd3": ("SMYD3", "https://pubmed.ncbi.nlm.nih.gov/23752591/", "https://pubmed.ncbi.nlm.nih.gov/25669152/", "primary_literature_regulator_level", "mouse C2C12 and T-cell chromatin models", "recruitment, H3K4 methylation, Pol II/cofactor engagement, and expression studies", "SMYD3 has chromatin-regulator evidence at myostatin, c-Met, and Foxp3, not the queued targets.", "noncanonical chromatin methyltransferase capacity only"),
    "cdk7": ("CDK7", "https://pubmed.ncbi.nlm.nih.gov/19667075/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5564226/", "primary_literature_regulator_level", "human transcription-initiation/elongation models", "analog-sensitive CDK7, Pol II CTD phosphorylation, pausing, and termination", "CDK7 is transcriptional machinery/kinase evidence at nonqueued genes, not a sequence-specific TF.", "noncanonical transcriptional machinery capacity only"),
    "baz1b": ("BAZ1B/WSTF", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2695106/", "https://pubmed.ncbi.nlm.nih.gov/26755828/", "primary_literature_regulator_level", "mouse and human WINAC/WICH chromatin models", "Gja5 promoter regulation, chromatin remodeling, and ChIP-seq", "BAZ1B has chromatin-remodeler evidence at nonqueued loci, not the queued targets.", "noncanonical chromatin-remodeler capacity only"),
    "ints13": ("INTS13", "https://pubmed.ncbi.nlm.nih.gov/32647223/", "", "primary_literature_regulator_level", "human Integrator model", "Integrator-module assembly, nucleic-acid binding, and RNA-processing/termination", "INTS13 is transcriptional machinery, not a sequence-specific TF for the queued genes.", "noncanonical transcriptional machinery capacity only"),
    "dpy30": ("DPY30", "https://pubmed.ncbi.nlm.nih.gov/21335234/", "https://pubmed.ncbi.nlm.nih.gov/27647347/", "primary_literature_regulator_level", "mouse ESC and HSC chromatin models", "H3K4 methylation, ChIP-seq, and knockout lineage-expression studies", "DPY30 has chromatin-modifier evidence at other loci, not the queued targets.", "noncanonical chromatin-complex capacity only"),
    "trim33": ("TRIM33/TIF1gamma", "https://pubmed.ncbi.nlm.nih.gov/29930104/", "", "primary_literature_regulator_level", "mouse Th17 chromatin model", "ChIP-seq, Smad2/RORgamma recruitment, chromatin marks, and Il17a/Il10 expression", "TRIM33 has target-specific chromatin/cofactor evidence at Il17a and Il10, not the queued targets.", "noncanonical chromatin coregulator capacity only"),
    "tbl1xr1": ("TBL1XR1/TBLR1", "https://pubmed.ncbi.nlm.nih.gov/19481530/", "https://reactome.org/content/detail/R-HSA-9024326", "primary_literature_regulator_level", "human HepG2 nuclear-receptor model", "LXR/NCoR/GPS2/HDAC3 corepressor complex and ABCA1 promoter study", "TBL1XR1/TBLR1 is a nuclear-receptor coregulator; the exact ABCA1 edge is recorded separately.", "noncanonical transcriptional coregulator; exact ABCA1 edge kept separate"),
    "arid4b": ("ARID4B", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4552441/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5743547/", "primary_literature_regulator_level", "mouse Sertoli and chromatin-coregulator models", "Rhox5 promoter occupancy, androgen-receptor cooperation, and network studies", "ARID4B has promoter/coregulator evidence at nonqueued loci, not the queued targets.", "noncanonical chromatin coregulator capacity only"),
    "usp7": ("USP7/HAUSP", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8096222/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3545798/", "primary_literature_regulator_level", "human melanoma and NF-kB activation models", "PRC2 ChIP-seq, deubiquitinase perturbation, and NF-kB promoter recruitment", "USP7 is a deubiquitinase/chromatin-transcriptional regulator with nonqueued targets.", "noncanonical chromatin/transcriptional regulator capacity only"),
    "nelfa": ("NELFA/WHSC2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6817524/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7402197/", "primary_literature_regulator_level", "human and mouse promoter-pausing models", "NELF ChIP-seq/PRO-seq, promoter occupancy, and pause-release studies", "NELFA controls promoter-proximal Pol II pausing, not sequence-specific queued target regulation.", "noncanonical transcriptional elongation capacity only"),
    "nelfe": ("NELFE/WHSC2", "https://pubmed.ncbi.nlm.nih.gov/12612062/", "https://pubmed.ncbi.nlm.nih.gov/29523821/", "primary_literature_regulator_level", "human and mouse promoter-pausing models", "NELF reconstitution, promoter occupancy, and pause-release studies", "NELFE controls promoter-proximal Pol II pausing, not sequence-specific queued target regulation.", "noncanonical transcriptional elongation capacity only"),
    "ncaph2": ("NCAPH2/CAP-H2", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12148035/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5479651/", "primary_literature_regulator_level", "mouse erythroid and ESC condensin-II models", "CUT&RUN/RNA-seq, condensin occupancy, and 4C-seq architecture", "NCAPH2 is a chromosome-architecture factor with nonqueued locus evidence.", "noncanonical chromosome-architecture capacity only"),
    "taf3": ("TAF3", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3588593/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3490149/", "primary_literature_regulator_level", "human HCT116 and hESC TFIID models", "ChIP-seq/ChIP-chip, promoter occupancy, and depletion studies", "TAF3 is a general TFIID initiation factor; broad promoter occupancy is not a queued target edge.", "noncanonical transcriptional machinery capacity only"),
    "cenpa": ("CENPA", "https://pubmed.ncbi.nlm.nih.gov/25788983/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4363203/", "primary_literature_regulator_level", "human cancer chromatin models", "ectopic CENP-A nucleosome and accessible-promoter studies", "CENPA is a centromeric histone variant; no queued promoter edge was established.", "noncanonical chromatin-state capacity only"),
    "hmgxb4": ("HMGXB4/HMG2L1", "https://pubmed.ncbi.nlm.nih.gov/20511232/", "https://www.encodeproject.org/experiments/ENCSR713KVZ/", "primary_literature_regulator_level", "human smooth-muscle and ENCODE models", "myocardin/SRF promoter coregulation and ChIP-seq resource", "HMGXB4 is a transcriptional coregulator with nonqueued promoter evidence.", "noncanonical transcriptional coregulator capacity only"),
    "med26": ("MED26", "https://pubmed.ncbi.nlm.nih.gov/25575120/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3145325/", "primary_literature_regulator_level", "human Mediator models", "initiation/elongation complex docking and transcriptional perturbation", "MED26 is Mediator machinery; no queued target edge was established.", "noncanonical transcriptional machinery capacity only"),
    "pcgf1": ("PCGF1", "https://pubmed.ncbi.nlm.nih.gov/37266576/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10287155/", "primary_literature_regulator_level", "mouse PRC1.1/HSPC and ESC models", "H2AK119ub1/H3K27me3 regulation, ChIP, and loss-of-function derepression", "PCGF1 has noncanonical PRC1 chromatin-repressor evidence at other loci.", "noncanonical chromatin-repressor capacity only"),
    "stag1": ("STAG1/SA1", "https://pubmed.ncbi.nlm.nih.gov/25735743/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4381060/", "primary_literature_regulator_level", "mouse cohesin/4C and ChIP models", "cohesin occupancy, RNA-seq, and locus architecture at nonqueued genes", "STAG1 is a cohesin/chromatin-architecture component, not a sequence-specific TF.", "noncanonical chromatin-architecture capacity only"),
    "ep400": ("EP400", "https://pubmed.ncbi.nlm.nih.gov/26669263/", "https://pubmed.ncbi.nlm.nih.gov/31142747/", "primary_literature_regulator_level", "human and mouse H2A.Z/H3.3 chromatin models", "promoter/enhancer histone deposition and conditional deletion", "EP400 affects chromatin state and transcription at nonqueued loci.", "noncanonical chromatin-remodeler capacity only"),
    "rybp": ("RYBP", "https://pubmed.ncbi.nlm.nih.gov/27705745/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8837790/", "primary_literature_regulator_level", "mouse ESC and neural PRC1 models", "PRC1 reconstitution, ChIP-seq, depletion, and Pax6 promoter repression", "RYBP is a PRC1 chromatin regulator with nonqueued target evidence.", "noncanonical chromatin-repressor capacity only"),
    "ino80": ("INO80", "https://pubmed.ncbi.nlm.nih.gov/34139016/", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE49137", "primary_literature_regulator_level", "mouse ESC chromatin models", "bivalent-promoter ChIP-seq, conditional deletion, and H2A.Z deposition", "INO80 has chromatin-remodeling/resource evidence, not queued target regulation.", "noncanonical chromatin-remodeler capacity only"),
    "tet2": ("TET2", "https://pubmed.ncbi.nlm.nih.gov/35931086/", "https://pubmed.ncbi.nlm.nih.gov/30417100/", "primary_literature_regulator_level", "human macrophage and enhancer models", "TET2-dependent TFAM/IFN and enhancer occupancy/demethylation studies", "TET2 is an epigenetic regulator with nonqueued target evidence; queued human edges remain unverified.", "noncanonical chromatin regulator capacity only"),
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
    status = "chromatin_or_transcriptional_machinery_database_only_not_promotable"
    primary = TF_LINK_URL
    corr = ""
    cell = "not_established_for_exact_pair"
    binding = "TFLink_or_curated_database_membership_only"
    downstream = "not_found_for_exact_pair"
    disposition = "retain_noncanonical_regulator_candidate_separately"
    exclusions = "General regulator-level evidence at nonqueued loci, orthologs, reverse directions, co-models, and broad chromatin programs was not transferred to this exact pair."
    notes = "TFLink membership is a search lead only; it does not establish causal direction, target-cell presence, downstream activation, or upstream relay."

    if key == "tbl1xr1" and target == "abca1":
        status = "functional_noncanonical_coregulator_promotion_candidate_not_strict_tf"
        primary = "https://pubmed.ncbi.nlm.nih.gov/19481530/"
        corr = "https://reactome.org/content/detail/R-HSA-9024326"
        cell = "human_HepG2_model_not_SCI_target_cell"
        binding = "TBLR1_TBL1XR1_ChIP_at_ABCA1_promoter"
        downstream = "siTBLR1_reduced_ligand_induced_ABCA1_expression"
        disposition = "retain_noncanonical_coregulator_candidate_pending_SCI_context"
        exclusions = "TBL1XR1/TBLR1 is a nuclear-receptor coregulator rather than a sequence-specific TF; no SCI target-cell validation or independent second exact paper was found."
        notes = "Human HepG2 ChIP and siRNA support a TBL1XR1/TBLR1-dependent LXR-ABCA1 relationship, but this is noncanonical coregulator evidence rather than strict TF promotion."
    elif key == "prmt1" and target == "abca1":
        status = "perturbation_association_without_regulator_specific_causality_not_promotable"
        primary = "https://pubmed.ncbi.nlm.nih.gov/41545753/"
        cell = "human_MDA_MB_231_and_Hs578T_models_not_SCI_target_cell"
        binding = "no_PRMT1_ABCA1_locus_binding_established"
        downstream = "type_I_PRMT_inhibitor_increased_ABCA1_ABCG1_and_cholesterol_efflux"
        disposition = "retain_indirect_perturbation_association_separately"
        exclusions = "The inhibitor affected PRMT1/6/8 together; PRMT1-specific causality, direct locus binding, and SCI-cell context were not established."
        notes = "The target-expression response is a nonspecific type-I PRMT perturbation association, not a direct PRMT1-to-ABCA1 edge."
    elif key == "stag1" and target == "a2m":
        status = "chromatin_or_transcriptional_machinery_database_only_not_promotable"
        notes = "Mouse STAG1/SA1 chromatin and 4C evidence concerns other loci; the queued A2m row remains a TFLink lead only."
    elif key == "ep400" and target == "abca1":
        status = "chromatin_resource_without_target_call_not_promotable"
        primary = "https://dbarchive.biosciencedbc.jp/kyushu-u/hg38/target/EP400.10.html"
        binding = "EP400_ChIP_Atlas_resource_without_retrieved_ABCA1_call"
        disposition = "retain_chromatin_resource_lead_separately"
        notes = "A human EP400 target resource was checked, but no queued ABCA1 locus call was retrieved."
    elif key == "nelfe" and row["species_scope"] == "mouse" and target == "abca1":
        status = "chromatin_resource_without_target_call_not_promotable"
        primary = "https://dbarchive.biosciencedbc.jp/kyushu-u/mm10/target/Nelfe.10.html"
        binding = "mouse_Nelfe_ChIP_Atlas_resource_without_retrieved_Abca1_call"
        disposition = "retain_chromatin_resource_lead_separately"
        notes = "A mouse NELFE target resource was checked, but no queued Abca1 locus call was retrieved."
    elif key in {"prmt1", "tbl1xr1"}:
        status = "database_membership_only_not_promotable"
        notes = "Only the separately recorded ABCA1 relationship has target-specific evidence; other queued rows remain TFLink leads."

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
            "review_id": f"public_tf_evidence_batch019_pair_{int(row['batch_rank']):02d}_{row['target_rank']}",
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
                "evidence_id": f"public_tf_evidence_batch019_regulator_{key}", "regulator_key": key,
                "regulator_symbol": info["symbol"], "species_scope": row["species_scope"],
                "evidence_layer": "regulator_identity_and_regulatory_capacity", "support_kind": info["kind"],
                "cell_or_model": info["model"], "assay_or_perturbation": info["assay"], "observation": info["observation"],
                "effect_direction": "queued-pair direction not established except explicitly recorded limited associations",
                "primary_citation": info["general_primary"], "corroborating_citation": info["general_corr"],
                "route_or_module_relevance": info["relevance"], "target_pair_scope": "not evidence for unrelated queued exact pairs; no upstream relay inferred",
                "exportable": "false", "canonical_write_performed": "false",
                "limitations": "Regulator-level evidence does not establish SCI target-cell presence, exact queued-target direction, downstream activation, or upstream relay. Chromatin-associated, cofactor, and indirect perturbation evidence is retained separately from canonical promoter-TF evidence.",
            })
            seen.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch019_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch019_regulator_register.tsv"
    summary_path = args.output_dir / "batch_019_evidence_review_summary.json"
    report_path = args.output_dir / "EVIDENCE_REVIEW_BATCH019.md"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    status_counts: dict[str, int] = {}
    for item in pairs:
        status_counts[item["exact_pair_status"]] = status_counts.get(item["exact_pair_status"], 0) + 1
    pair_keys = {(item["regulator_key"], item["target_symbol"], item["species_scope"], item["source_record_id"]) for item in pairs}
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_019", "source_set_ranks_reviewed": list(range(1, 26)),
        "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen), "unique_provenance_aware_pairs": len(pair_keys),
        "exact_pair_status_counts": status_counts, "regulator_register_rows": len(evidence), "strict_tf_promotion_candidate_rows": 0,
        "noncanonical_exact_candidate_rows": status_counts.get("functional_noncanonical_coregulator_promotion_candidate_not_strict_tf", 0),
        "exportable_pair_rows": 0, "canonical_writes_performed": False, "module22b_promotions_performed": False, "provenance_preserved": True,
        "limitations": ["TFLink membership is a search lead, not causal regulation.", "Exact pair negatives are bounded-search results, not global absence.", "TBL1XR1/TBLR1 is a coregulator, not a strict TF.", "PRMT1-ABCA1 is a nonspecific inhibitor association without PRMT1-specific causality.", "No canonical or Module 22B write was performed."],
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path.write_text("\n".join([
        "# Evidence review: public TF batch 019", "", "Reviewed 100 exact regulator-target-species pairs across 25 selected source-set ranks.", "",
        f"- **{len(pairs)}** pairs were reviewed across **{len(seen)}** regulators.",
        f"- **{summary['noncanonical_exact_candidate_rows']}** exact noncanonical coregulator candidate was staged: human TBL1XR1/TBLR1-to-ABCA1.",
        f"- **{status_counts.get('perturbation_association_without_regulator_specific_causality_not_promotable', 0)}** indirect PRMT1 inhibitor association was retained without regulator-specific causality.",
        f"- **{status_counts.get('ortholog_species_near_match_not_promotable', 0)}** cross-species chromatin near-match, plus resource/co-occurrence leads, were not transferred to exact queued edges.",
        "- **0** strict TF promotion candidates, exportable rows, canonical writes, or Module 22B writes.", "",
        "All rows retain the original TFLink source record, raw symbol, species, target, graph-module mapping, and local source snapshot. General chromatin, cofactor, and indirect perturbation evidence is recorded separately from exact canonical TF evidence.", "",
    ]) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
