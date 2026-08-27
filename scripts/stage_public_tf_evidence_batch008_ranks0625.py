#!/usr/bin/env python3
"""Stage conservative evidence findings for public-TF batch 008 ranks 6-25."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/"
    "current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_008/"
    "public_tf_evidence_collection_batch_008.tsv"
)
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


# These records preserve regulator-level evidence separately from queued edges.
# Exact target-set members below are binding/occupancy-only and cannot promote an edge.
REGULATORS = {
    "znf660": {
        "symbol": "ZNF660", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF660_TARGET_GENES.html", "corr": "",
        "model": "human GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization",
        "observation": "The GTRD-derived ZNF660 target set contains queued C5AR1, CTNNB1, EFNA3, and FGF21; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Target-set membership is occupancy-only; no exact functional pair was promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "rfx6": {
        "symbol": "RFX6", "species": "mouse", "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC2896718/", "corr": "https://pmc.ncbi.nlm.nih.gov/articles/PMC2799156/",
        "model": "mouse pancreatic endocrine development and islet models", "assay": "developmental loss-of-function, expression, ChIP-seq/ChIP-qPCR, and transcript analysis",
        "observation": "RFX6 has strong regulator-level evidence in mouse pancreatic endocrine development and adult islet function, including direct targets such as Neurod1, Hnf1a, Nkx6-1, St18, Eif2ak1, Upf1, and Eif5; none of the queued Adm, Crhr2, Cx3cl1, or Cxcr4 edges was validated.",
        "exclusions": "Nonqueued RFX6 targets and tissue-specific pancreatic evidence were not transferred to queued genes.", "kind": "primary_literature_regulator_level",
    },
    "znf610": {
        "symbol": "ZNF610", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF610_TARGET_GENES", "corr": "",
        "model": "human GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization",
        "observation": "The GTRD-derived ZNF610 target set contains queued BMPR1A, CTNNB1, DLL1, and EDN1; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Target-set membership is occupancy-only; no exact functional pair was promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "znf260": {
        "symbol": "ZNF260", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF260_TARGET_GENES.html", "corr": "",
        "model": "human GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization",
        "observation": "The GTRD-derived ZNF260 target set contains queued ADAM22, ADGRE5, ADIPOR2, and ANXA2; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Target-set membership is occupancy-only; no exact functional pair was promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "znf329": {
        "symbol": "ZNF329", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF329_TARGET_GENES.html", "corr": "",
        "model": "human GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization",
        "observation": "The GTRD-derived ZNF329 target set contains queued ADGRB3, ADGRL1, AVPR1B, and BDKRB2; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Target-set membership is occupancy-only; no exact functional pair was promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "znf816": {
        "symbol": "ZNF816", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF816_TARGET_GENES.html", "corr": "",
        "model": "human GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization",
        "observation": "The GTRD-derived ZNF816 target set contains queued BDKRB2, BMP7, CD81, and FGFR1; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Target-set membership is occupancy-only; no exact functional pair was promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "znf561": {
        "symbol": "ZNF561", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF561_TARGET_GENES.html", "corr": "",
        "model": "human GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization",
        "observation": "The GTRD-derived ZNF561 target set contains queued C1QL4, COL4A1, COL4A2, and FZD5; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Target-set membership is occupancy-only; no exact functional pair was promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "znf563": {
        "symbol": "ZNF563", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF563_TARGET_GENES.html", "corr": "https://www.ncbi.nlm.nih.gov/gene/147837/",
        "model": "human regulator annotation and GTRD-derived occupancy resource", "assay": "gene annotation and GTRD ChIP-seq harmonization",
        "observation": "ZNF563 is annotated as a predicted sequence-specific transcription factor and its GTRD-derived target set contains queued AVPR1A, BMPR1A, COL14A1, and COL8A2; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Predicted regulator annotation and occupancy-only target membership were not promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "zscan21": {
        "symbol": "ZSCAN21", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZSCAN21_TARGET_GENES.html", "corr": "",
        "model": "human GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization",
        "observation": "The GTRD-derived ZSCAN21 target set contains queued ADAM22, ANXA2, CD8A, and HMGB1; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Target-set membership is occupancy-only; no exact functional pair was promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "znf623": {
        "symbol": "ZNF623", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF623_TARGET_GENES.html", "corr": "",
        "model": "human GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization",
        "observation": "The GTRD-derived ZNF623 target set contains queued ADA, C3, COL1A1, and EFNA2; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Target-set membership is occupancy-only; no exact functional pair was promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "zscan31": {
        "symbol": "ZSCAN31", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZSCAN31_TARGET_GENES.html", "corr": "",
        "model": "human GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization",
        "observation": "The GTRD-derived ZSCAN31 target set contains queued ADAM17, CADM1, CMKLR1, and FGF9; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Target-set membership is occupancy-only; no exact functional pair was promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "zkscan1": {
        "symbol": "ZKSCAN1", "species": "mouse", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/mouse/geneset/ZKSCAN1_TARGET_GENES.html", "corr": "",
        "model": "mouse GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization",
        "observation": "The mouse GTRD-derived ZKSCAN1 target set contains queued Adam22, Adgrl2, Ado, and Ccl22; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Target-set membership is occupancy-only; no exact functional pair was promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "hand1": {
        "symbol": "HAND1", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/HAND1_TARGET_GENES.html", "corr": "",
        "model": "human GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization",
        "observation": "The human GTRD-derived HAND1 target set contains queued ADAM22, APLP2, CDH11, and EPOR; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Target-set membership is occupancy-only; no exact functional pair was promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "znf213": {
        "symbol": "ZNF213", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF213_TARGET_GENES.html", "corr": "",
        "model": "human GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization",
        "observation": "The GTRD-derived ZNF213 target set contains queued ADA, ADO, APP, and CXCL16; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Target-set membership is occupancy-only; no exact functional pair was promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "znf512b": {
        "symbol": "ZNF512B", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF512B_TARGET_GENES.html", "corr": "https://academic.oup.com/nar/article/54/15/gkag802/8758778",
        "model": "human transcriptional/chromatin studies and GTRD occupancy resource", "assay": "NuRD/chromatin interaction, DNA-binding characterization, and GTRD ChIP-seq harmonization",
        "observation": "ZNF512B has regulator-level chromatin/transcription evidence and its GTRD-derived target set contains queued COL6A3, FGF13, FST, and GDF11; no matched perturbation or orthogonal target-expression validation was located for these edges.",
        "exclusions": "Regulator-level chromatin evidence and occupancy-only target membership were not promoted to queued functional edges.", "kind": "primary_literature_regulator_level",
    },
    "znf197": {
        "symbol": "ZNF197", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF197_TARGET_GENES.html", "corr": "https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2023.1189570/pdf",
        "model": "human GTRD-derived occupancy and regulator-network resources", "assay": "GTRD ChIP-seq harmonization and regulator-network analysis",
        "observation": "The GTRD-derived ZNF197 target set contains queued ADAM9, ADGRB3, and ALB; ADCYAP1 was not present in the fetched set. No matched functional queued edge was validated.",
        "exclusions": "Occupancy-only membership and nonqueued regulator-network evidence were not promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "znf362": {
        "symbol": "ZNF362", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF362_TARGET_GENES.html", "corr": "https://www.genecards.org/card/ZNF362",
        "model": "human GTRD-derived promoter occupancy and gene-regulation annotations", "assay": "GTRD ChIP-seq harmonization and regulatory annotation",
        "observation": "The GTRD-derived ZNF362 target set contains queued ADGRL1, AMBN, APLP2, and FBN1; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "General regulatory annotation and occupancy-only target membership were not promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "znf547": {
        "symbol": "ZNF547", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF547_TARGET_GENES.html", "corr": "",
        "model": "human GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization",
        "observation": "The GTRD-derived ZNF547 target set contains queued ATP1A3, CCL2, FBN1, and HMGB1; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Target-set membership is occupancy-only; no exact functional pair was promoted.", "kind": "authoritative_binding_dataset_only",
    },
    "barhl1": {
        "symbol": "BARHL1", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/BARHL1_TARGET_GENES.html", "corr": "https://pmc.ncbi.nlm.nih.gov/articles/PMC2268402/",
        "model": "human GTRD-derived target set with vertebrate Barhl1 promoter-binding literature", "assay": "GTRD ChIP-seq harmonization; promoter ChIP and reporter assays in Barhl1 models",
        "observation": "The human GTRD-derived BARHL1 target set contains queued ANXA2, CISH, DIP2A, and DKK1. Vertebrate Barhl1 has direct promoter-binding evidence at its own nonqueued promoter, but no queued target was validated by matched perturbation and target expression.",
        "exclusions": "Self-promoter and nonqueued developmental evidence were not transferred to queued edges.", "kind": "primary_literature_regulator_level",
    },
    "znf577": {
        "symbol": "ZNF577", "species": "human", "primary": "https://www.gsea-msigdb.org/gsea/msigdb/human/geneset/ZNF577_TARGET_GENES.html", "corr": "",
        "model": "human GTRD-derived promoter occupancy resource", "assay": "GTRD ChIP-seq harmonization",
        "observation": "The GTRD-derived ZNF577 target set contains queued ADA, APLP1, CDON, and DLL3; no matched perturbation or orthogonal target-expression validation was located.",
        "exclusions": "Target-set membership is occupancy-only; no exact functional pair was promoted.", "kind": "authoritative_binding_dataset_only",
    },
}

EXACT_OCCUPANCY_ONLY = {}


def add_targets(key: str, targets: list[str]) -> None:
    for target in targets:
        EXACT_OCCUPANCY_ONLY[(key, target)] = REGULATORS[key]["primary"]


add_targets("znf660", ["C5AR1", "CTNNB1", "EFNA3", "FGF21"])
add_targets("znf610", ["BMPR1A", "CTNNB1", "DLL1", "EDN1"])
add_targets("znf260", ["ADAM22", "ADGRE5", "ADIPOR2", "ANXA2"])
add_targets("znf329", ["ADGRB3", "ADGRL1", "AVPR1B", "BDKRB2"])
add_targets("znf816", ["BDKRB2", "BMP7", "CD81", "FGFR1"])
add_targets("znf561", ["C1QL4", "COL4A1", "COL4A2", "FZD5"])
add_targets("znf563", ["AVPR1A", "BMPR1A", "COL14A1", "COL8A2"])
add_targets("zscan21", ["ADAM22", "ANXA2", "CD8A", "HMGB1"])
add_targets("znf623", ["ADA", "C3", "COL1A1", "EFNA2"])
add_targets("zscan31", ["ADAM17", "CADM1", "CMKLR1", "FGF9"])
add_targets("zkscan1", ["Adam22", "Adgrl2", "Ado", "Ccl22"])
add_targets("hand1", ["ADAM22", "APLP2", "CDH11", "EPOR"])
add_targets("znf213", ["ADA", "ADO", "APP", "CXCL16"])
add_targets("znf512b", ["COL6A3", "FGF13", "FST", "GDF11"])
add_targets("znf197", ["ADAM9", "ADGRB3", "ALB"])
add_targets("znf362", ["ADGRL1", "AMBN", "APLP2", "FBN1"])
add_targets("znf547", ["ATP1A3", "CCL2", "FBN1", "HMGB1"])
add_targets("barhl1", ["ANXA2", "CISH", "DIP2A", "DKK1"])
add_targets("znf577", ["ADA", "APLP1", "CDON", "DLL3"])


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
    rows = [row for row in read_tsv(args.batch) if 6 <= int(row["batch_rank"]) <= 25]
    if len(rows) != 80:
        raise SystemExit(f"expected 80 rows for ranks 6-25, found {len(rows)}")

    pairs: list[dict[str, str]] = []
    evidence: list[dict[str, str]] = []
    seen_keys: set[str] = set()
    for i, row in enumerate(rows, 1):
        key = row["regulator_key"]
        if key not in REGULATORS:
            raise SystemExit(f"missing evidence map for {key}")
        info = REGULATORS[key]
        exact_lead = EXACT_OCCUPANCY_ONLY.get((key, row["target_symbol"]))
        if exact_lead:
            exact_status = "binding_dataset_only_not_promotable"
            binding_status = "authoritative_occupancy_dataset_lead"
            expression_status = "not_found_for_exact_pair"
            pair_primary = exact_lead
            pair_notes = "An authoritative binding/target-set record indicates regulator association at this exact gene, but no matched perturbation or orthogonal validation was located; do not promote."
        else:
            exact_status = "no_exact_pair_support_found_in_bounded_search"
            binding_status = "not_found_for_exact_pair"
            expression_status = "not_found_for_exact_pair"
            pair_primary = ""
            pair_notes = "No qualifying exact regulator-target assay was located in the bounded search."
        general_status = "supported_authoritative_binding_dataset_only" if info["kind"] == "authoritative_binding_dataset_only" else "supported_general_regulator_evidence"
        pairs.append({
            "review_id": f"public_tf_evidence_batch008_pair_{int(row['batch_rank']):02d}_{i:02d}",
            "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key,
            "regulator_symbol": info["symbol"], "species_scope": row["species_scope"], "source_registry": row["source_registry"],
            "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"],
            "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": search_url(info["symbol"], row["target_symbol"], row["species_scope"]), "exact_pair_status": exact_status,
            "regulator_general_evidence_status": general_status, "target_cell_presence_status": "not_established_for_exact_pair",
            "binding_or_association_status": binding_status, "downstream_expression_or_perturbation_status": expression_status,
            "downstream_activation_status": "not_assessed", "upstream_relay_status": "not_tested_for_exact_pair",
            "disposition": "retain_database_candidate_as_search_lead_only", "primary_citation": pair_primary,
            "corroborating_citation": "", "near_match_exclusions": info["exclusions"],
            "review_notes": pair_notes + " Regulator-level references are stored separately and are not evidence for this exact queued pair. " + info["observation"],
            "exportable": "false", "canonical_write_performed": "false",
        })
        if key not in seen_keys:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch008_regulator_{key}", "regulator_key": key,
                "regulator_symbol": info["symbol"], "species_scope": info["species"], "evidence_layer": "regulator_identity_and_regulatory_capacity",
                "support_kind": info["kind"], "cell_or_model": info["model"], "assay_or_perturbation": info["assay"],
                "observation": info["observation"], "effect_direction": "queued-pair direction not established", "primary_citation": info["primary"],
                "corroborating_citation": info["corr"], "route_or_module_relevance": "regulator-level evidence only",
                "target_pair_scope": "not evidence for queued exact pairs; no Module 22B edge or upstream relay inferred",
                "exportable": "false", "canonical_write_performed": "false",
                "limitations": "Regulator-level evidence does not establish the queued target relationship, target-cell presence in SCI, downstream activation, or upstream relay.",
            })
        seen_keys.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch008_ranks0625_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch008_ranks0625_regulator_register.tsv"
    summary_path = args.output_dir / "batch_008_ranks0625_evidence_review_summary.json"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    occupancy_rows = sum(row["exact_pair_status"] == "binding_dataset_only_not_promotable" for row in pairs)
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_008", "source_set_ranks_reviewed": list(range(6, 26)),
        "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen_keys), "exact_pair_support_rows": 0,
        "binding_dataset_only_not_promotable_rows": occupancy_rows, "partial_or_near_match_rows": 0,
        "general_regulator_evidence_rows": len(evidence), "exportable_pair_rows": 0,
        "canonical_writes_performed": False, "module22b_promotions_performed": False, "provenance_preserved": True,
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
        "decision": "Retain all 80 pairs as database-attributed search leads; exact binding-only leads remain non-promotable without matched perturbation or orthogonal validation.",
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
