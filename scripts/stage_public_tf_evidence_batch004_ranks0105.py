#!/usr/bin/env python3
"""Stage conservative evidence findings for public-TF batch 004 ranks 1-5."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/"
    "current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_004/"
    "public_tf_evidence_collection_batch_004.tsv"
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

# symbol, species, primary, corroboration, model, assay, observation, exclusions,
# support kind
REGULATORS = {
    "gmeb2": (
        "GMEB2", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9776391/", "https://pubmed.ncbi.nlm.nih.gov/9651376/",
        "human transcriptional and cancer-cell models", "ChIP-qPCR, knockdown, promoter-reporter, and DNA/protein interaction assays",
        "GMEB2 has regulator-level evidence at non-queued genes including ADRM1 and at glucocorticoid-modulated regulatory elements, but no queued ACKR2/ADAM17/ADAM22/ADGRB3 relationship was found.",
        "The ADRM1 and GME/TAT regulatory results were not transferred to queued edges.", "primary_literature_regulator_level",
    ),
    "znf316": (
        "ZNF316", "human", "https://remap.univ-amu.fr/target_page/ZNF316%3A9606", "",
        "human K-562 cells", "ReMap ChIP-seq occupancy resource",
        "An authoritative ReMap occupancy record exists for ZNF316 in K-562 cells, but no validated target-level perturbation or queued ACVR1/ADAM12/ADAM9/ADGRL1 relationship was established.",
        "Occupancy-only dataset evidence lacks queued-locus verification and perturbation; it is a follow-up lead, not a functional edge.", "authoritative_binding_dataset_only",
    ),
    "hes5": (
        "HES5", "mouse", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4920244/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC1618116/",
        "mouse neural developmental and myelinating models", "HES5 perturbation, ChIP/occupancy, and target-expression assays",
        "HES5 has direct regulator-level evidence at non-queued genes including Sox9 and Mbp, but no queued Actr2/Acvr1/Acvr1c/Adam22 relationship was found.",
        "Neural developmental targets and co-mentions were not transferred to queued edges.", "primary_literature_regulator_level",
    ),
    "myrf": (
        "MYRF", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3742440/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8600034/",
        "vertebrate oligodendrocyte/myelinating models", "MYRF ChIP-seq, enhancer/reporter, knockout, and myelin-gene expression assays",
        "MYRF has direct regulator-level evidence at non-queued myelin genes including Mbp, Plp1, Mag, Cntn2, and Trf, but no queued ACKR2/ADAM10/ADAM17/ADAM22 relationship was found.",
        "Myelin-gene occupancy and expression effects were not transferred to queued edges; the human queue entry does not establish SCI-cell activity.", "primary_literature_regulator_level",
    ),
    "tgif2": (
        "TGIF2", "human", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5649440/", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6908606/",
        "human cancer and pluripotency models", "promoter/target-expression perturbation and transcriptional assays",
        "TGIF2 has regulator-level evidence at non-queued genes including FUT8 and OCT4, but no queued A2M/ABCA1/ACKR2/ACTR2 relationship was found.",
        "The ABCA1 near match is TGIF1, not TGIF2; paralog evidence was explicitly excluded. TGIF2 evidence at FUT8/OCT4/FCMR was not transferred to queued edges.", "primary_literature_regulator_level",
    ),
}
TGIF1_ABCA1_URL = "https://pmc.ncbi.nlm.nih.gov/articles/PMC2939915/"


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
    rows = [row for row in read_tsv(args.batch) if 1 <= int(row["batch_rank"]) <= 5]
    if len(rows) != 20:
        raise SystemExit(f"expected 20 rows for ranks 1-5, found {len(rows)}")

    pairs: list[dict[str, str]] = []
    evidence: list[dict[str, str]] = []
    seen_keys: set[str] = set()
    for i, row in enumerate(rows, 1):
        key = row["regulator_key"]
        if key not in REGULATORS:
            raise SystemExit(f"missing evidence map for {key}")
        symbol, species, primary, corr, model, assay, observation, exclusions, support_kind = REGULATORS[key]
        is_near_match = key == "tgif2" and row["target_symbol"].lower() == "abca1"
        pair_exclusions = exclusions
        if is_near_match:
            pair_exclusions = f"{TGIF1_ABCA1_URL} — direct ABCA1 evidence is for TGIF1, not TGIF2; paralog evidence excluded."
        pairs.append({
            "review_id": f"public_tf_evidence_batch004_pair_{int(row['batch_rank']):02d}_{i:02d}",
            "batch_id": row["batch_id"], "batch_rank": row["batch_rank"], "regulator_key": key,
            "regulator_symbol": symbol, "species_scope": row["species_scope"], "source_registry": row["source_registry"],
            "source_record_id": row["source_record_id"], "raw_tf_symbol": row["raw_tf_symbol"], "target_symbol": row["target_symbol"],
            "target_graph_modules": row["target_graph_modules"], "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": search_url(symbol, row["target_symbol"], row["species_scope"]),
            "exact_pair_status": "paralog_near_match_not_promotable" if is_near_match else "no_exact_pair_support_found_in_bounded_search",
            "regulator_general_evidence_status": "supported_authoritative_binding_dataset_only" if support_kind == "authoritative_binding_dataset_only" else ("supported_general_regulator_evidence" if primary else "not_found_in_bounded_search"),
            "target_cell_presence_status": "not_established_for_exact_pair", "binding_or_association_status": "not_found_for_exact_pair",
            "downstream_expression_or_perturbation_status": "not_found_for_exact_pair", "downstream_activation_status": "not_assessed",
            "upstream_relay_status": "not_tested_for_exact_pair", "disposition": "retain_database_candidate_as_search_lead_only",
            "primary_citation": "", "corroborating_citation": "", "near_match_exclusions": pair_exclusions,
            "review_notes": "Regulator-level references are stored separately; they are not evidence for this exact queued pair. " + observation,
            "exportable": "false", "canonical_write_performed": "false",
        })
        if key not in seen_keys:
            evidence.append({
                "evidence_id": f"public_tf_evidence_batch004_regulator_{key}", "regulator_key": key,
                "regulator_symbol": symbol, "species_scope": species, "evidence_layer": "regulator_identity_and_regulatory_capacity",
                "support_kind": support_kind, "cell_or_model": model, "assay_or_perturbation": assay,
                "observation": observation, "effect_direction": "queued-pair direction not established", "primary_citation": primary,
                "corroborating_citation": corr, "route_or_module_relevance": "regulator-level evidence only" if primary else "regulator-level evidence not established",
                "target_pair_scope": "not evidence for queued exact pairs; no Module 22B edge or upstream relay inferred",
                "exportable": "false", "canonical_write_performed": "false",
                "limitations": "Regulator-level evidence does not establish the queued target relationship, target-cell presence in SCI, downstream activation, or upstream relay.",
            })
        seen_keys.add(key)

    args.output_dir = args.output_dir.resolve()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    pair_path = args.output_dir / "public_tf_evidence_review_batch004_ranks0105_pairs.tsv"
    register_path = args.output_dir / "public_tf_evidence_review_batch004_ranks0105_regulator_register.tsv"
    summary_path = args.output_dir / "batch_004_ranks0105_evidence_review_summary.json"
    write_tsv(pair_path, PAIR_FIELDS, pairs)
    write_tsv(register_path, EVIDENCE_FIELDS, evidence)
    summary = {
        "status": "staging_only", "batch_id": "public_tf_evidence_batch_004", "source_set_ranks_reviewed": list(range(1, 6)),
        "pair_rows_reviewed": len(pairs), "unique_regulators_reviewed": len(seen_keys), "exact_pair_support_rows": 0,
        "partial_or_near_match_rows": sum(row["exact_pair_status"] != "no_exact_pair_support_found_in_bounded_search" for row in pairs),
        "general_regulator_evidence_rows": len(evidence), "exportable_pair_rows": 0,
        "canonical_writes_performed": False, "module22b_promotions_performed": False, "provenance_preserved": True,
        "outputs": [str(pair_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
        "decision": "Retain all 20 pairs as database-attributed search leads; TGIF2/ABCA1 is a TGIF1 paralog near match and no exact pair met the promotion threshold.",
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
