#!/usr/bin/env python3
"""Stage conservative evidence findings for all 100 Batch 011 pairs."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/"
    "current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_011/"
    "public_tf_evidence_collection_batch_011.tsv"
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
# model, assay, observation
REGULATORS = {
    "zbtb1": ("ZBTB1", "https://pubmed.ncbi.nlm.nih.gov/21706167/", "https://pubmed.ncbi.nlm.nih.gov/22753936/", "primary_literature_regulator_level", "human and mouse lymphocyte models", "reporter repression and loss-of-function", "ZBTB1 has transcriptional repression and lymphocyte-development evidence, but none of the four queued targets was directly validated."),
    "znf165": ("ZNF165", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4660212/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7302877/", "primary_literature_regulator_level", "human TNBC models", "ChIP-seq, depletion, and chromatin co-occupancy", "ZNF165 has evidence for TGF-beta transcriptional programs and SMAD3 co-occupancy, but none of the four queued targets was directly established."),
    "znf791": ("ZNF791", "https://pubmed.ncbi.nlm.nih.gov/33326746/", "https://pubmed.ncbi.nlm.nih.gov/35989482/", "primary_literature_regulator_level", "human KRAB-domain and cardiomyocyte models", "KRAB recruitment and miRNA-axis perturbation", "ZNF791 has limited regulator-level repression/perturbation evidence, without queued target attribution."),
    "znf418": ("ZNF418", "https://pubmed.ncbi.nlm.nih.gov/18084723/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6643133/", "primary_literature_regulator_level", "human reporter, MAPK/AP-1, and cardiac-remodeling models", "reporter repression and perturbation", "ZNF418 has repression and MAPK/AP-1 evidence at nonqueued contexts, but none of the four queued targets was directly established."),
    "znf581": ("ZNF581", "https://www.uniprot.org/uniprotkb/Q9P0T4/entry", "", "authoritative_binding_dataset_only", "human annotation and TFLink/GTRD candidate set", "protein annotation and database membership", "ZNF581 has cautious annotation-level transcriptional-regulation support, but no direct regulator-level functional study was verified in this pass."),
    "znf236": ("ZNF236", TF_LINK_URL, "", "authoritative_binding_dataset_only", "human TFLink/GTRD candidate set", "species-matched target-set membership", "No qualifying regulator-level functional or perturbation evidence was located in this bounded pass beyond the database-derived candidate set."),
    "mlxip": ("MLXIP", TF_LINK_URL, "", "authoritative_binding_dataset_only", "human TFLink/GTRD candidate set", "species-matched target-set membership", "No qualifying regulator-level evidence was located for the queued targets in this bounded pass."),
    "ybx3": ("YBX3", TF_LINK_URL, "", "authoritative_binding_dataset_only", "human TFLink/GTRD candidate set", "species-matched target-set membership", "No qualifying regulator-level evidence was located for the queued targets in this bounded pass."),
    "hoxd11": ("HOXD11", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5805373/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12189421/", "primary_literature_regulator_level", "human and mouse HOXD11 developmental studies", "developmental expression and DNA-binding/target studies", "HOXD11 has regulator-level developmental evidence at nonqueued targets, but none of the four queued targets was directly validated."),
    "znf669": ("ZNF669", TF_LINK_URL, "", "authoritative_binding_dataset_only", "human TFLink/GTRD candidate set", "species-matched target-set membership", "No qualifying regulator-level functional or perturbation evidence was located in this bounded pass beyond the database-derived candidate set."),
    "znf529": ("ZNF529", TF_LINK_URL, "", "authoritative_binding_dataset_only", "human TFLink/GTRD candidate set", "species-matched target-set membership", "No qualifying regulator-level functional or perturbation evidence was located in this bounded pass beyond the database-derived candidate set."),
    "znf707": ("ZNF707", TF_LINK_URL, "", "authoritative_binding_dataset_only", "human TFLink/GTRD candidate set", "species-matched target-set membership", "No qualifying regulator-level functional or perturbation evidence was located in this bounded pass beyond the database-derived candidate set."),
    "dlx6": ("DLX6", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9846190/", "https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM6522566", "primary_literature_regulator_level", "human glioma and trophoblast ChIP/knockdown studies", "ChIP, knockdown, and target-expression analysis", "DLX6 has human regulator-level ChIP/knockdown evidence at ATG7 and independent occupancy resources, but none of the four queued targets was directly validated."),
    "znf530": ("ZNF530", TF_LINK_URL, "", "authoritative_binding_dataset_only", "human TFLink/GTRD candidate set", "species-matched target-set membership", "No qualifying regulator-level functional or perturbation evidence was located in this bounded pass beyond the database-derived candidate set."),
    "hivep1": ("HIVEP1", TF_LINK_URL, "", "authoritative_binding_dataset_only", "human TFLink/GTRD candidate set", "species-matched target-set membership", "No qualifying regulator-level functional or perturbation evidence was located in this bounded pass beyond the database-derived candidate set."),
    "znf667": ("ZNF667", TF_LINK_URL, "", "authoritative_binding_dataset_only", "human TFLink/GTRD candidate set", "species-matched target-set membership", "No qualifying regulator-level functional or perturbation evidence was located in this bounded pass beyond the database-derived candidate set."),
    "znf708": ("ZNF708", TF_LINK_URL, "", "authoritative_binding_dataset_only", "human TFLink/GTRD candidate set", "species-matched target-set membership", "No qualifying regulator-level functional or perturbation evidence was located in this bounded pass beyond the database-derived candidate set."),
    "znf785": ("ZNF785", TF_LINK_URL, "", "authoritative_binding_dataset_only", "human TFLink/GTRD candidate set", "species-matched target-set membership", "No qualifying regulator-level functional or perturbation evidence was located in this bounded pass beyond the database-derived candidate set."),
    "zscan5b": ("ZSCAN5B", TF_LINK_URL, "", "authoritative_binding_dataset_only", "human TFLink/GTRD candidate set", "species-matched target-set membership", "No qualifying regulator-level functional or perturbation evidence was located in this bounded pass beyond the database-derived candidate set."),
    "znf582": ("ZNF582", TF_LINK_URL, "", "authoritative_binding_dataset_only", "human TFLink/GTRD candidate set", "species-matched target-set membership", "No qualifying regulator-level functional or perturbation evidence was located in this bounded pass beyond the database-derived candidate set."),
    "znf433": ("ZNF433", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6362961/", "", "primary_literature_regulator_level", "human prostate-cancer models", "overexpression/knockdown and beta-catenin/TCF pathway analysis", "ZNF433 has tumor-growth and beta-catenin/TCF pathway evidence at nonqueued markers, but none of the four assigned targets was directly established."),
    "zscan18": ("ZSCAN18", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9847086/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10300323/", "primary_literature_regulator_level", "human gastric-cancer, glioblastoma, and breast-cancer models", "loss-of-function and transcript/pathway analysis", "ZSCAN18 has tumor-suppressive evidence and nonqueued downstream relationships, but none of the four assigned targets was directly validated."),
    "znf586": ("ZNF586", "https://www.ncbi.nlm.nih.gov/gene/54807", "", "authoritative_binding_dataset_only", "human gene annotation and TFLink/GTRD candidate set", "gene annotation and database membership", "ZNF586 is annotated as a predicted DNA-binding TF, but no regulator-level functional study or queued target mechanism was established."),
    "nkx2-8": ("NKX2-8", "https://www.ncbi.nlm.nih.gov/gene/26257", "https://aacrjournals.org/cancerres/article/73/12/3638/584231/Nkx2-8-Downregulation-Promotes-Angiogenesis-and", "primary_literature_regulator_level", "human cancer and promoter models", "promoter activation and tumor phenotype studies", "NKX2-8 has regulator-level promoter and tumor-effect evidence at nonqueued targets, but none of the four assigned targets was directly established."),
    "znf488": ("ZNF488", "https://pubmed.ncbi.nlm.nih.gov/25779368/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10658979/", "primary_literature_regulator_level", "human NPC and pancreatic-cancer models", "overexpression/knockdown and target-expression studies", "ZNF488 has functional evidence at nonqueued targets including SCD1, but none of the four assigned targets was directly validated."),
}

SET_URL = {
    "zbtb1": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZBTB1_TARGET_GENES.html", "znf165": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF165_TARGET_GENES.html", "znf791": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF791_TARGET_GENES.html", "znf418": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF418_TARGET_GENES.html", "znf581": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF581_TARGET_GENES.html", "hoxd11": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/HOXD11_TARGET_GENES.html", "znf433": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF433_TARGET_GENES.html", "zscan18": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZSCAN18_TARGET_GENES.html", "znf586": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF586_TARGET_GENES.html", "nkx2-8": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/NKX2_8_TARGET_GENES.html", "znf488": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF488_TARGET_GENES.html",
}

DATABASE_ONLY = {
    ("mlxip", target) for target in ("adam23", "fst", "hes1", "abcb7")
} | {
    ("ybx3", target) for target in ("gdf11", "lamp1", "abt1")
} | {
    ("znf669", target) for target in ("atp6ap2", "sema6a", "stat3", "adap2")
} | {("znf667", "taz"), ("znf708", "cntn1")}


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
        symbol, primary, corr, kind, model, assay, observation = REGULATORS[key]
        target_key = row["target_symbol"].lower()
        candidate = key == "msgn1" and target_key == "dll3"
        database_only = (key, target_key) in DATABASE_ONLY
        status = "functional_direct_binding_promotion_candidate" if candidate else ("database_membership_only_not_promotable" if database_only else "binding_dataset_only_not_promotable")
        set_url = SET_URL.get(key, TF_LINK_URL)
        if candidate:
            pair_primary = "https://pmc.ncbi.nlm.nih.gov/articles/PMC3622708/"
            pair_corr = "https://reactome.org/content/detail/R-MMU-9824184"
            cell = "present_in_mouse_presomitic_mesoderm_not_SCI_target_cell"
            binding = "direct_upstream_binding_and_regulatory_element_validation"
            downstream = "Msgn1_loss_lowered_Dll3_and_inducible_Msgn1_increased_Dll3"
            disposition = "promotion_candidate_pending_SCI_target_cell_context"
            notes = "Msgn1 binds upstream of Dll3; Msgn1 loss lowers Dll3, inducible Msgn1 increases Dll3, and a Dll3 regulatory element is transactivated in reporter assays. This is a strong exact pair, but the evidence is from mouse presomitic mesoderm rather than the SCI target cell; stage for review, do not materialize."
        elif database_only:
            pair_primary = TF_LINK_URL
            pair_corr = ""
            cell = "not_established_for_exact_pair"
            binding = "TFLink_snapshot_membership_only"
            downstream = "not_found_for_exact_pair"
            disposition = "retain_database_candidate_as_search_lead_only"
            notes = "The species-matched TFLink membership is retained as a database search lead, but the exact pair was not independently confirmed in the checked GTRD/MSigDB target set and no direct functional or perturbation validation was located; do not promote."
        else:
            pair_primary = set_url
            pair_corr = ""
            cell = "not_established_for_exact_pair"
            binding = "authoritative_database_membership_lead"
            downstream = "not_found_for_exact_pair"
            disposition = "retain_database_candidate_as_search_lead_only"
            notes = "Species-matched TFLink/GTRD-derived target-set membership is retained as a database/binding search lead; no direct target-specific functional or perturbation validation was located in this bounded pass."
        pairs.append({"review_id": f"public_tf_evidence_batch011_pair_{int(row['batch_rank']):02d}_{row['target_rank']}", "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key, "regulator_symbol": symbol, "species_scope": row["species_scope"], "source_registry": row["source_registry"], "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"], "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"], "exact_pair_search_url": search_url(symbol, row["target_symbol"], row["species_scope"]), "exact_pair_status": status, "regulator_general_evidence_status": "supported_general_regulator_evidence", "target_cell_presence_status": cell, "binding_or_association_status": binding, "downstream_expression_or_perturbation_status": downstream, "downstream_activation_status": "not_established_for_SCI_target_cell", "upstream_relay_status": "not_tested_for_exact_pair", "disposition": disposition, "primary_citation": pair_primary, "corroborating_citation": pair_corr, "near_match_exclusions": "Regulator-level evidence at nonqueued targets, orthologs, reverse-direction relationships, and lineage-driver use was not transferred to queued edges.", "review_notes": notes + " " + observation, "exportable": "false", "canonical_write_performed": "false"})
        if key not in seen:
            evidence.append({"evidence_id": f"public_tf_evidence_batch011_regulator_{key}", "regulator_key": key, "regulator_symbol": symbol, "species_scope": row["species_scope"], "evidence_layer": "regulator_identity_and_regulatory_capacity", "support_kind": kind, "cell_or_model": model, "assay_or_perturbation": assay, "observation": observation, "effect_direction": "queued-pair direction not established except staged Msgn1-Dll3 candidate", "primary_citation": primary, "corroborating_citation": corr, "route_or_module_relevance": "regulator-level evidence only", "target_pair_scope": "not evidence for unrelated queued exact pairs; no upstream relay inferred", "exportable": "false", "canonical_write_performed": "false", "limitations": "Regulator-level evidence does not establish SCI target-cell presence, exact queued-target direction, downstream activation, or upstream relay. The Msgn1-Dll3 pair is retained separately as a promotion candidate pending SCI-cell context."})
        seen.add(key)
    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch011_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch011_regulator_register.tsv"
    summary_path = args.output_dir / "batch_011_evidence_review_summary.json"
    report_path = args.output_dir / "EVIDENCE_REVIEW_BATCH011.md"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    status_counts: dict[str, int] = {}
    for row in pairs:
        status_counts[row["exact_pair_status"]] = status_counts.get(row["exact_pair_status"], 0) + 1
    pair_keys = {(row["regulator_key"], row["target_symbol"], row["species_scope"], row["source_record_id"]) for row in pairs}
    summary = {"status": "staging_only", "batch_id": "public_tf_evidence_batch_011", "source_set_ranks_reviewed": list(range(1, 26)), "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen), "unique_provenance_aware_pairs": len(pair_keys), "exact_pair_status_counts": status_counts, "regulator_register_rows": len(evidence), "exact_pair_support_rows": status_counts.get("functional_direct_binding_promotion_candidate", 0), "promotion_candidate_rows": status_counts.get("functional_direct_binding_promotion_candidate", 0), "partial_or_near_match_rows": 0, "binding_dataset_only_not_promotable_rows": status_counts.get("binding_dataset_only_not_promotable", 0), "database_membership_only_not_promotable_rows": status_counts.get("database_membership_only_not_promotable", 0), "bounded_negative_rows": 0, "exportable_pair_rows": 0, "canonical_writes_performed": False, "module22b_promotions_performed": False, "provenance_preserved": True, "limitations": ["TFLink/GTRD/MSigDB membership is database/binding evidence, not causal regulation.", "Some TFLink-only rows are retained separately from independently corroborated GTRD/MSigDB promoter occupancy.", "Target-cell presence, downstream activation, and upstream relay remain unestablished for all queued pairs.", "No canonical or Module 22B write was performed."], "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))]}
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    report_path.write_text("# Evidence review: public TF batch 011\n\nReviewed all 25 selected TFLink source sets and 100 exact regulator-target-species pairs.\n\n" + f"- **{len(pairs)} / 100** pairs were reviewed.\n- **{summary['exact_pair_support_rows']}** exact pairs met the promotion-candidate threshold.\n- **{summary['binding_dataset_only_not_promotable_rows']}** pairs had independently corroborated GTRD/MSigDB promoter-occupancy leads.\n- **{summary['database_membership_only_not_promotable_rows']}** pairs remained TFLink-snapshot-only database leads.\n- **0** rows are exportable; no canonical or Module 22B writes were performed.\n\nNo queued pair had matched target-level functional validation in this bounded pass.\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
