#!/usr/bin/env python3
"""Sort the expanded public-TF inventory into role-review categories.

The output is a staging overlay over the original TF triage ledger. Categories
are mutually exclusive at the primary-role level, while the original source
registries, species scopes, and evidence topology remain attached to every
row. This script does not promote canonical TF roles, create Module 22B edges,
or delete candidates from any source inventory.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/tf_expansion_triage.tsv"
DEFAULT_NONCANONICAL = ROOT / "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/noncanonical_regulator_staging.tsv"
DEFAULT_OUTPUT = ROOT / "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1"


EXACT_RNA = {
    "AGO1", "AGO2", "DCP1A", "DROSHA", "FIP1L1", "HNRNPL", "HNRNPLL", "HNRNPU",
    "PCBP1", "RBFOX2", "ZC3H8", "XRN2", "ELAVL1", "ELAVL2", "ELAVL3",
    "ELAVL4", "FUS", "PUM1", "PUM2", "SFPQ", "NONO", "TIA1", "TARDBP",
}
RNA_PREFIXES = ("AGO", "DCP", "DROSHA", "ELAVL", "HNRN", "PCBP", "RBFOX", "RBM", "SRSF", "XRN")

EXACT_DNA_REPAIR = {
    "ATM", "ATR", "DMC1", "ERCC3", "ERCC6", "FANCD2", "MCM7", "NBN",
    "OGG1", "ORC2", "RAG1", "RAG2", "TOP1", "XRCC3", "XRCC4", "BRCA1",
    "BRCA2", "RAD50", "RAD51", "RECQL", "PARP1", "PARP2",
}
DNA_REPAIR_PREFIXES = ("ERCC", "FAN", "MCM", "ORC", "PARP", "RAD", "RECQL", "XRCC")

EXACT_SIGNALING = {
    "ACVR1", "ANPEP", "ARRB1", "BMPR1A", "CAT", "CCND2", "CCNY", "CDK6",
    "CSNK2A1", "DAND5", "EGLN2", "FGFR1", "GPIHBP1", "KCNH2", "MBL2",
    "ME1", "ME3", "MTOR", "MUC22", "OCA2", "PADI2", "PEX2", "PMEPA1",
    "PTEN", "SLC30A9", "SRC",
}
SIGNALING_PREFIXES = ("ACVR", "BMPR", "CCN", "CDK", "FGFR", "GPIHBP", "KCN", "MAPK", "SLC")

EXACT_NUCLEAR_STRUCTURE = {
    "LMNA", "LMNB1", "NUP98", "TERF2IP", "SUMO2",
}
NUCLEAR_STRUCTURE_PREFIXES = ("LMNB", "NUP")

EXACT_PROVISIONAL_NUCLEAR = {"ATMIN", "CARF", "FIZ1"}

EXACT_DUAL_ROLE = {
    "FOXP4", "MGA", "PRDM12", "PRDM4", "PRDM6", "PRDM9", "ZBTB7C",
    "ZHX1", "ZNF516", "ZNF521", "ZNF541", "ZNF711", "ZFP57", "ZGPAT",
}

EXACT_NUCLEAR_MACHINERY = {
    "CENPS", "CENPT", "CENPX", "SON", "TERF1", "TERF2", "TERB1", "THYN1",
}

EXACT_ALIAS_OR_ARTIFACT = {"NA", "P65"}

FIELDS = [
    "regulator_key", "display_symbols", "species_scopes", "source_registries",
    "source_versions", "identity_catalogs", "original_triage_bucket",
    "identity_source_count", "catalog_profile_count", "tflink_target_count",
    "identifier_flags", "primary_role_category", "role_subcategory",
    "role_screen_basis", "classification_status", "module_route",
    "module22b_eligibility", "evidence_readiness", "sort_priority",
    "provenance_note",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def symbols(row: dict[str, str]) -> list[str]:
    return [item.strip().upper() for item in (row.get("display_symbols", "") or "").split(";") if item.strip()]


def numeric(value: str) -> int:
    try:
        return int(value or 0)
    except ValueError:
        return 0


def matches(values: list[str], exact: set[str], prefixes: tuple[str, ...]) -> list[str]:
    found = [value for value in values if value in exact or any(value.startswith(prefix) for prefix in prefixes)]
    return sorted(set(found))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--noncanonical", type=Path, default=DEFAULT_NONCANONICAL)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    triage = read_tsv(args.input)
    noncanonical = {row["regulator_key"]: row for row in read_tsv(args.noncanonical)}
    output: list[dict[str, str]] = []

    for row in triage:
        key = row["tf_key"]
        syms = symbols(row)
        if key in noncanonical:
            nc = noncanonical[key]
            primary = "noncanonical_transcriptional_regulator"
            subcategory = nc["role_category"]
            basis = "Conservative chromatin/co-regulator family screen; retain for separate functional evidence review."
            priority = 20
        elif row.get("triage_bucket") == "exclude_unresolved_identifier":
            primary = "unresolved_identifier"
            subcategory = "protein_accession_mapping_required"
            basis = "Protein accession is not yet a stable gene-symbol identity."
            priority = 80
        elif row.get("triage_bucket") == "exclude_from_automatic_module_promotion_profile_only":
            primary = "binding_profile_only"
            subcategory = "motif_profile_without_pair_evidence"
            basis = "JASPAR profile support without exact TF-target evidence."
            priority = 70
        elif any(value in EXACT_ALIAS_OR_ARTIFACT for value in syms):
            primary = "alias_or_ingestion_artifact_review"
            subcategory = "noncanonical_or_missing_value_symbol"
            basis = "Symbol requires alias resolution or may represent an ingestion placeholder."
            priority = 75
        elif (found := [value for value in syms if value in EXACT_PROVISIONAL_NUCLEAR]):
            primary = "provisional_nuclear_transcriptional_regulator"
            subcategory = "nuclear_scaffold_or_damage_signal_co_regulator"
            basis = "Literature-linked nuclear transcriptional effect, but insufficient evidence for the stronger chromatin-regulator category: " + ";".join(found) + "."
            priority = 25
        elif (found := [value for value in syms if value in EXACT_DUAL_ROLE]):
            primary = "dual_role_tf_chromatin_candidate"
            subcategory = "sequence_specific_tf_with_chromatin_coregulator_function"
            basis = "Retain as a TF candidate because of DNA-binding/TF evidence while flagging chromatin-coregulator activity: " + ";".join(found) + "."
            priority = 15
        elif (found := [value for value in syms if value in EXACT_NUCLEAR_MACHINERY]):
            primary = "nuclear_machinery_or_structural_not_regulatory"
            subcategory = "centromere_telomere_or_nuclear_processing"
            basis = "Nuclear/chromosome-associated protein without a sufficient locus-directed transcriptional-regulator basis: " + ";".join(found) + "."
            priority = 52
        elif (found := matches(syms, EXACT_RNA, RNA_PREFIXES)):
            primary = "rna_binding_or_post_transcriptional"
            subcategory = "rna_processing_or_binding"
            basis = "Symbol matches a conservative RNA-binding/RNA-processing family screen: " + ";".join(found) + "."
            priority = 40
        elif (found := matches(syms, EXACT_DNA_REPAIR, DNA_REPAIR_PREFIXES)):
            primary = "dna_repair_or_genome_maintenance"
            subcategory = "repair_replication_or_recombination"
            basis = "Symbol matches a conservative DNA-repair, replication, or genome-maintenance family screen: " + ";".join(found) + "."
            priority = 45
        elif (found := matches(syms, EXACT_NUCLEAR_STRUCTURE, NUCLEAR_STRUCTURE_PREFIXES)):
            primary = "nuclear_structure_or_transport"
            subcategory = "lamina_pore_or_genome_organization"
            basis = "Symbol matches a nuclear-structure/transport screen: " + ";".join(found) + "."
            priority = 50
        elif (found := matches(syms, EXACT_SIGNALING, SIGNALING_PREFIXES)):
            primary = "signaling_metabolic_membrane_or_cell_cycle"
            subcategory = "enzyme_receptor_transporter_or_cell_cycle"
            basis = "Symbol matches a conservative signaling, metabolic, membrane, or cell-cycle screen: " + ";".join(found) + "."
            priority = 55
        elif row.get("triage_bucket") == "promote_identity_staging":
            primary = "catalog_concordant_tf_candidate"
            subcategory = "identity_supported_pair_unverified"
            basis = "Independent Lambert and AnimalTFDB3 identity catalogs agree; canonical TF role and exact pair evidence remain to be reviewed."
            priority = 10
        elif row.get("triage_bucket") == "prioritize_target_evidence_search":
            primary = "regulon_lead_unclassified"
            subcategory = "aggregated_tf_link_target_lead"
            basis = "TFLink target-membership lead without enough retained metadata for a biological role assignment."
            priority = 30
        else:
            primary = "identity_review_unclassified"
            subcategory = "single_source_or_profile_identity"
            basis = "Candidate requires identity, domain, and functional-role review before routing."
            priority = 60

        if row.get("triage_bucket") == "exclude_unresolved_identifier":
            readiness = "not_reviewable_as_gene_symbol"
        elif row.get("triage_bucket") == "exclude_from_automatic_module_promotion_profile_only":
            readiness = "motif_profile_only"
        elif numeric(row.get("tflink_target_count", "")) and row.get("identity_catalogs"):
            readiness = "identity_plus_aggregated_target_lead"
        elif numeric(row.get("tflink_target_count", "")):
            readiness = "aggregated_target_lead_only"
        elif numeric(row.get("catalog_profile_count", "")):
            readiness = "identity_plus_profile_only"
        else:
            readiness = "identity_catalog_only_or_unverified"

        if primary == "noncanonical_transcriptional_regulator":
            route = "separate_noncanonical_regulator_queue"
            eligibility = "not_strict_tf_pending_role_and_pair_review"
        elif primary == "catalog_concordant_tf_candidate":
            route = "22B_after_exact_pair_evidence"
            eligibility = "strict_tf_candidate_pending_exact_pair_review"
        elif primary == "regulon_lead_unclassified":
            route = "22B_target_search_after_role_review"
            eligibility = "not_ready_pending_role_and_pair_review"
        elif primary in {"rna_binding_or_post_transcriptional", "dna_repair_or_genome_maintenance", "nuclear_structure_or_transport", "nuclear_machinery_or_structural_not_regulatory", "signaling_metabolic_membrane_or_cell_cycle"}:
            route = "role_specific_review_outside_strict_tf_default"
            eligibility = "not_strict_tf_pending_functional_review"
        elif primary == "provisional_nuclear_transcriptional_regulator":
            route = "separate_nuclear_regulator_review_queue"
            eligibility = "not_strict_tf_pending_functional_review"
        elif primary == "dual_role_tf_chromatin_candidate":
            route = "22B_after_tf_and_chromatin_role_review"
            eligibility = "strict_tf_candidate_pending_exact_pair_review"
        elif primary == "binding_profile_only":
            route = "profile_validation"
            eligibility = "not_ready_profile_only"
        elif primary == "unresolved_identifier":
            route = "identifier_mapping_required"
            eligibility = "not_ready_identifier_unresolved"
        elif primary == "alias_or_ingestion_artifact_review":
            route = "identifier_or_ingestion_audit"
            eligibility = "not_ready_alias_or_artifact_review"
        else:
            route = "identity_and_role_review"
            eligibility = "not_ready_pending_identity_and_pair_review"

        output.append({
            "regulator_key": key,
            "display_symbols": row.get("display_symbols", ""),
            "species_scopes": row.get("species_scopes", ""),
            "source_registries": row.get("source_registries", ""),
            "source_versions": row.get("source_versions", ""),
            "identity_catalogs": row.get("identity_catalogs", ""),
            "original_triage_bucket": row.get("triage_bucket", ""),
            "identity_source_count": row.get("identity_source_count", ""),
            "catalog_profile_count": row.get("catalog_profile_count", ""),
            "tflink_target_count": row.get("tflink_target_count", ""),
            "identifier_flags": row.get("identifier_flags", ""),
            "primary_role_category": primary,
            "role_subcategory": subcategory,
            "role_screen_basis": basis,
            "classification_status": "role_triage_staging",
            "module_route": route,
            "module22b_eligibility": eligibility,
            "evidence_readiness": readiness,
            "sort_priority": str(priority),
            "provenance_note": (
                "This is a role-triage overlay. Source registries, source versions, species scope, and "
                "source-specific parent identity records remain authoritative; no canonical role or evidence "
                "promotion is created by this row."
            ),
        })

    output.sort(key=lambda row: (int(row["sort_priority"]), row["primary_role_category"], row["regulator_key"]))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_path = args.output_dir / "public_tf_role_triage.tsv"
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(output)

    summary_path = args.output_dir / "public_tf_role_triage_summary.json"
    summary = {
        "status": "staging_only",
        "input_rows": len(triage),
        "output_rows": len(output),
        "duplicate_regulator_keys": len(output) - len({row["regulator_key"] for row in output}),
        "primary_role_category_counts": dict(sorted(Counter(row["primary_role_category"] for row in output).items())),
        "original_triage_bucket_counts": dict(sorted(Counter(row["original_triage_bucket"] for row in output).items())),
        "module22b_eligibility_counts": dict(sorted(Counter(row["module22b_eligibility"] for row in output).items())),
        "canonical_writes_performed": False,
        "module22b_promotions_performed": False,
        "policy": {
            "primary_role": "mutually exclusive conservative staging category",
            "provenance": "source registries and parent identity records are retained",
            "species": "human and mouse remain separate during evidence review",
            "evidence": "role classification does not establish exact TF-target evidence",
        },
        "outputs": [str(output_path.relative_to(ROOT)), str(summary_path.relative_to(ROOT))],
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
