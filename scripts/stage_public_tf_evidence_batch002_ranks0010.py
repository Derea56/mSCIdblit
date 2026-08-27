#!/usr/bin/env python3
"""Stage completed evidence reviews for batch 002 source ranks 1-10.

The lane reports no exact promoted pairs. Regulator-level references remain
separate from exact target evidence, and all outputs are non-exportable.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/"
    "current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_002/"
    "public_tf_evidence_collection_batch_002.tsv"
)

PAIR_FIELDS = [
    "review_id", "batch_id", "batch_rank", "regulator_key", "regulator_symbol",
    "species_scope", "source_registry", "source_record_id", "raw_tf_symbol",
    "target_symbol", "target_graph_modules", "candidate_membership_status",
    "exact_pair_search_url", "exact_pair_status", "regulator_general_evidence_status",
    "target_cell_presence_status", "binding_or_association_status",
    "downstream_expression_or_perturbation_status", "downstream_activation_status",
    "upstream_relay_status", "disposition", "primary_citation",
    "corroborating_citation", "near_match_exclusions", "review_notes", "exportable",
    "canonical_write_performed",
]

EVIDENCE_FIELDS = [
    "evidence_id", "regulator_key", "regulator_symbol", "species_scope", "evidence_layer",
    "support_kind", "cell_or_model", "assay_or_perturbation", "observation",
    "effect_direction", "primary_citation", "corroborating_citation",
    "route_or_module_relevance", "target_pair_scope", "exportable",
    "canonical_write_performed", "limitations",
]

REGULATORS = {
    "znf48": ("ZNF48", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC13017510/", "", "human promoter-element assay; no queued target relationship", "promoter-element assay", "Regulator-level DNA/promoter evidence only; no queued A2M/ACVR1/ACVR1C/ADA edge was found.", "NFAT5-to-A2M and ACVR1 studies naming other TFs were excluded."),
    "znf83": ("ZNF83", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC2978345/", "", "human manipulation/expression study", "ZNF83 manipulation and expression analysis", "ZNF83 has experimental expression/manipulation evidence, but no queued ACTR2/ACVR1/ACVR1C/ADA target relationship was found.", "Broad expression, methylation, and annotation lists were excluded."),
    "ikzf5": ("IKZF5", "human", "https://pubmed.ncbi.nlm.nih.gov/10978333/", "https://pubmed.ncbi.nlm.nih.gov/31217188/", "human hematopoietic/megakaryocytic models", "DNA binding, reporter repression, chromatin/perturbation studies", "IKZF5 has sequence-specific DNA-binding and chromatin/regulatory evidence, but no queued A2M/ACKR2/ACTR2/ACVR1 edge was found.", "Platelet gene lists, predicted networks, and target-specific studies without IKZF5 were excluded."),
    "homez": ("HOMEZ", "human", "https://pubmed.ncbi.nlm.nih.gov/12925734/", "https://pubmed.ncbi.nlm.nih.gov/22001922/", "human developmental and knockout models", "DNA-binding, expression, and knockout studies", "HOMEZ has DNA-binding and developmental regulatory evidence, but no queued A2M/ACKR2/ACVR1/ADAM10 edge was found.", "Mouse Homez/A2m co-expression and pathway studies without HOMEZ were excluded."),
    "patz1": ("PATZ1", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4405645/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3877567/", "human tumor and promoter-regulatory models", "transcriptional perturbation, ChIP/promoter, and target-gene studies", "PATZ1 has direct regulatory evidence at other genes, but no queued ACVR1/ADAM10/ADAM17/ADAM22 edge was found.", "PATZ1-ADAM17 differential co-expression is explicitly a non-mechanistic near match: https://pmc.ncbi.nlm.nih.gov/articles/PMC4434877/."),
    "mxd3": ("MXD3", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5766270/", "https://pubmed.ncbi.nlm.nih.gov/42146011/", "human neuroblastoma and regulatory models", "MXD3 knockdown and promoter-occupancy studies", "MXD3 has regulator-level evidence at other genes, but no queued ABCA1/ACKR2/ACVR1/ACVR1C edge was found.", "OxLDL/ABCA1 co-occurrence and ACVR1/ACKR2 studies without MXD3 were excluded."),
    "fezf1": ("FEZF1", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8616448/", "https://pubmed.ncbi.nlm.nih.gov/20431123/", "human Ewing-sarcoma and mouse forebrain models", "FEZF1 knockdown/RNA-seq and developmental repression studies", "FEZF1 has regulator-level neural/developmental evidence, but no queued ACKR2/ACTR2/ACVR1/ACVR1C edge was found.", "Fezf1/Acvr1c co-expression and receptor studies without FEZF1 were excluded."),
    "scrt1": ("SCRT1", "human", "https://pubmed.ncbi.nlm.nih.gov/33309639/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8062533/", "human and rodent beta-cell/islet models", "ChIP/knockdown and chromatin-accessibility studies", "SCRT1 has regulator-level beta-cell chromatin evidence, but no queued ABCA1/ACVR1/ADAM9/ADGRB3 edge was found.", "ABCA1, ACVR1, ADAM9, and ADGRB3 studies without SCRT1 were excluded."),
    "myt1l": ("MYT1L", "mouse", "https://pmc.ncbi.nlm.nih.gov/articles/PMC11348803/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC10575775/", "mouse brain and human-neuron models", "ChIP-seq, repression, deficiency, and neuronal differentiation studies", "MYT1L has neuronal regulator-level evidence, but no queued Abca1/Ackr3/Actr2/Adam10 edge was found.", "MYT1L/Abca1 co-list results and receptor/cytoskeletal studies without MYT1L were excluded."),
    "znf554": ("ZNF554", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6092567/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7461028/", "human trophoblast and glioma models", "knockdown/overexpression transcriptomics", "ZNF554 has regulator-level expression/perturbation evidence, but no queued ACVR1/ADAM10/ADAM22/ADAM9 edge was found.", "Lipid-GWAS and ADAM gene co-occurrence were excluded."),
    "znf574": ("ZNF574", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12603413/", "", "human promoter-regulatory model", "promoter regulation and transcriptional assays", "ZNF574 has regulator-level evidence at TRPM4, but no queued ACVR1/ACVR1C/ADAM22/ADGRE5 edge was found.", "ACVR1/ACVR1C, ADAM22/LGI1, and ADGRE5/CD97 studies without ZNF574 were excluded."),
    "mynn": ("MYNN", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9194458/", "", "human SMAD/BMP regulatory models", "MYNN transcriptional and SMAD/BMP pathway studies", "MYNN has regulator-level SMAD/BMP pathway evidence, but no queued ACKR1/ACTR2/ACVR1/ACVRL1 edge was found.", "ACKR1/DARC, ACTR2/ARP2, ACVR1, and ACVRL1 studies without MYNN were excluded."),
    "zbtb42": ("ZBTB42", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3057000/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4240208/", "human muscle-development and loss-of-function models", "expression characterization and loss-of-function studies", "ZBTB42 has regulator-level muscle evidence, but no queued ACVR1/ADAM23/ADGRB3/ADGRE5 edge was found.", "ACVR1, ADAM23, ADGRB3, and ADGRE5 studies without ZBTB42 were excluded."),
    "fezf2": ("FEZF2", "mouse", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3099680/", "", "mouse cortical projection-neuron models", "DNA binding, electroporation/perturbation, and neural target studies", "FEZF2 has direct neural regulator evidence at other targets, but no queued A2M/Ackr3/Actr2/Acvr1 edge was found.", "FEZF2 target studies naming other neural genes and co-expression markers were excluded."),
    "znf207": ("ZNF207", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6197280/", "", "human embryonic-stem-cell models", "ZNF207 perturbation and regulatory profiling", "ZNF207 has hESC regulator-level evidence, but no queued ABCA1/ACTR2/ADAM10/ADAM17 edge was found.", "LXR/miR-33-to-ABCA1, ARP2, ADAM10/Notch, and ADAM17 studies without ZNF207 were excluded."),
    "znf574": ("ZNF574", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12603413/", "", "human promoter-regulatory model", "promoter regulation and transcriptional assays", "ZNF574 has regulator-level evidence at TRPM4, but no queued ACVR1/ACVR1C/ADAM22/ADGRE5 edge was found.", "ACVR1/ACVR1C, ADAM22/LGI1, and ADGRE5/CD97 studies without ZNF574 were excluded."),
    "mynn": ("MYNN", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9194458/", "", "human SMAD/BMP regulatory models", "MYNN transcriptional and SMAD/BMP pathway studies", "MYNN has regulator-level SMAD/BMP pathway evidence, but no queued ACKR1/ACTR2/ACVR1/ACVRL1 edge was found.", "ACKR1/DARC, ACTR2/ARP2, ACVR1, and ACVRL1 studies without MYNN were excluded."),
    "zbtb42": ("ZBTB42", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3057000/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4240208/", "human muscle-development and loss-of-function models", "expression characterization and loss-of-function studies", "ZBTB42 has regulator-level muscle evidence, but no queued ACVR1/ADAM23/ADGRB3/ADGRE5 edge was found.", "ACVR1, ADAM23, ADGRB3, and ADGRE5 studies without ZBTB42 were excluded."),
    "fezf2": ("FEZF2", "mouse", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3099680/", "", "mouse cortical projection-neuron models", "DNA binding, electroporation/perturbation, and neural target studies", "FEZF2 has direct neural regulator evidence at other targets, but no queued A2M/Ackr3/Actr2/Acvr1 edge was found.", "FEZF2 target studies naming other neural genes and co-expression markers were excluded."),
    "znf207": ("ZNF207", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6197280/", "", "human embryonic-stem-cell models", "ZNF207 perturbation and regulatory profiling", "ZNF207 has hESC regulator-level evidence, but no queued ABCA1/ACTR2/ADAM10/ADAM17 edge was found.", "LXR/miR-33-to-ABCA1, ARP2, ADAM10/Notch, and ADAM17 studies without ZNF207 were excluded."),
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_BATCH.parent)
    args = parser.parse_args()
    rows = [row for row in read_tsv(args.batch) if int(row["batch_rank"]) <= 15]
    if len(rows) != 60:
        raise SystemExit(f"expected 60 rows for ranks 1-15, found {len(rows)}")

    pairs = []
    for i, row in enumerate(rows, 1):
        key = row["regulator_key"]
        if key not in REGULATORS:
            raise SystemExit(f"missing evidence map for {key}")
        symbol, species, primary, corr, model, assay, observation, near = REGULATORS[key]
        near_status = "coexpression_only_near_match_not_promotable" if (key, row["target_symbol"].casefold()) == ("patz1", "adam17") else "no_exact_pair_support_found_in_bounded_search"
        pairs.append({
            "review_id": f"public_tf_evidence_batch002_pair_{i:03d}", "batch_id": row["batch_id"], "batch_rank": row["batch_rank"],
            "regulator_key": key, "regulator_symbol": symbol, "species_scope": row["species_scope"], "source_registry": row["source_registry"],
            "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"],
            "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": search_url(symbol, row["target_symbol"], row["species_scope"]), "exact_pair_status": near_status,
            "regulator_general_evidence_status": "supported_general_regulator_evidence" if primary else "not_found_in_bounded_search",
            "target_cell_presence_status": "not_established_for_exact_pair", "binding_or_association_status": "not_found_for_exact_pair",
            "downstream_expression_or_perturbation_status": "not_found_for_exact_pair", "downstream_activation_status": "not_assessed",
            "upstream_relay_status": "not_tested_for_exact_pair", "disposition": "retain_database_candidate_as_search_lead_only",
            "primary_citation": "", "corroborating_citation": "", "near_match_exclusions": near,
            "review_notes": "Regulator-level references are stored separately; they are not evidence for this exact queued pair. " + observation,
            "exportable": "false", "canonical_write_performed": "false",
        })

    evidence = []
    for key, (symbol, species, primary, corr, model, assay, observation, near) in REGULATORS.items():
        if not primary:
            continue
        evidence.append({
            "evidence_id": f"public_tf_evidence_batch002_regulator_{key}", "regulator_key": key, "regulator_symbol": symbol,
            "species_scope": species, "evidence_layer": "regulator_identity_and_regulatory_capacity",
            "support_kind": "primary_literature_regulator_level", "cell_or_model": model, "assay_or_perturbation": assay,
            "observation": observation, "effect_direction": "queued-pair direction not established", "primary_citation": primary,
            "corroborating_citation": corr, "route_or_module_relevance": "regulator-level evidence only",
            "target_pair_scope": "not evidence for queued exact pairs; no Module 22B edge or upstream relay inferred",
            "exportable": "false", "canonical_write_performed": "false",
            "limitations": "Regulator-level evidence does not establish the queued target relationship, target-cell presence in SCI, downstream activation, or upstream relay.",
        })

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch002_ranks0015_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch002_ranks0015_regulator_register.tsv"
    summary_path = args.output_dir / "batch_002_ranks0015_evidence_review_summary.json"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_002", "source_set_ranks_reviewed": list(range(1, 16)),
        "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len({r["regulator_key"] for r in pairs}),
        "exact_pair_support_rows": 0, "partial_or_near_match_rows": sum(r["exact_pair_status"] != "no_exact_pair_support_found_in_bounded_search" for r in pairs),
        "general_regulator_evidence_rows": len(evidence), "exportable_pair_rows": 0, "canonical_writes_performed": False,
        "module22b_promotions_performed": False, "provenance_preserved": True,
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
        "decision": "Keep all 60 pairs as database-attributed search leads. PATZ1-to-ADAM17 is a co-expression-only near match and remains non-promotable.",
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (args.output_dir / "EVIDENCE_REVIEW_BATCH002_RANKS0010.md").write_text(
        "# Evidence review: public TF batch 002 ranks 1-10\n\n"
        "Sixty exact regulator-target pairs were bounded-reviewed. No exact pair met the promotion threshold. "
        "Regulator-level literature is retained in a separate register; it is not applied to queued target pairs. "
        "PATZ1-to-ADAM17 is explicitly recorded as a co-expression-only near match. No canonical or Module 22B writes were performed.\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
