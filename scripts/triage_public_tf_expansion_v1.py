#!/usr/bin/env python3
"""Run a conservative first-pass triage of novel public TF inventory keys.

This is a staging artifact. It does not promote canonical TF roles, create
Module 22B regulons, or write to PostgreSQL. The only automatic promotion
allowed here is identity-level staging when both AnimalTFDB3 and the Lambert
human TF catalog support the normalized symbol. TFLink GMT membership is
treated as a target-search lead, not as pair-level evidence.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1"
DEFAULT_EXPANSION = ROOT / "data/processed/public_tf_union_expansion_v1"
DEFAULT_OUTPUT = DEFAULT_INPUT / "candidate_triage_v1"

IDENTITY_CATALOGS = {"AnimalTFDB3", "Lambert_HumanTFs", "JASPAR_CORE"}
DIRECT_IDENTITY_CATALOGS = {"AnimalTFDB3", "Lambert_HumanTFs"}
PROTEIN_ACCESSION_RE = re.compile(
    r"^(?:[OPQ][0-9][A-Z0-9]{4,7}|A0A[0-9A-Z]{6,})$", re.IGNORECASE
)
MOUSE_PREDICTED_RE = re.compile(r"^Gm[0-9]+$", re.IGNORECASE)
TRANSCRIPT_LIKE_RE = re.compile(
    r"^(?:AC|AL|AP|CT|DQ|GL|KB|LR|NG|NR|NT|NW|XR|BC|BX|CR|DR|FP|HQ|JH|KI|KN|LINC|RP(?:11)?-)[A-Z0-9_.-]+$",
    re.IGNORECASE,
)

FIELDS = [
    "tf_key", "display_symbols", "species_scopes", "source_registries",
    "source_versions", "identity_catalogs", "identity_source_count",
    "catalog_profile_count", "tflink_target_count", "unique_reference_pmids",
    "current_status", "identifier_flags", "triage_bucket", "promotion_scope",
    "module_route", "evidence_readiness", "triage_reason", "provenance_note",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def split_values(value: str) -> set[str]:
    return {item.strip() for item in (value or "").split(";") if item.strip()}


def numeric(value: str) -> int:
    try:
        return int(value or 0)
    except ValueError:
        return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--expansion-dir", type=Path, default=DEFAULT_EXPANSION)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    collapsed = [
        row for row in read_tsv(args.input_dir / "tf_cross_species_collapsed.tsv")
        if row.get("dedupe_status") == "new_candidate"
    ]
    crosswalk = read_tsv(args.input_dir / "tf_candidate_crosswalk.tsv")
    by_key: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in crosswalk:
        if row.get("tf_key"):
            by_key[row["tf_key"]].append(row)

    triage: list[dict[str, str]] = []
    for row in collapsed:
        key = row["tf_key"]
        source_registries = split_values(row.get("source_registries", ""))
        related = by_key.get(key, [])
        source_versions = {
            version
            for item in related
            for version in split_values(item.get("source_versions", ""))
        }
        identity_source_count = sum(numeric(item.get("identity_source_count", "")) for item in related)
        catalog_profile_count = sum(numeric(item.get("catalog_profile_count", "")) for item in related)
        tflink_target_count = sum(numeric(item.get("tflink_target_count", "")) for item in related)
        unique_reference_pmids = sum(numeric(item.get("unique_reference_pmids", "")) for item in related)
        symbol = (row.get("display_symbols", "") or key).split(";")[0].strip()
        identifier_flags: list[str] = []
        if PROTEIN_ACCESSION_RE.fullmatch(symbol):
            identifier_flags.append("unresolved_protein_accession")
        if MOUSE_PREDICTED_RE.fullmatch(symbol):
            identifier_flags.append("predicted_mouse_symbol")
        if TRANSCRIPT_LIKE_RE.fullmatch(symbol):
            identifier_flags.append("transcript_like_identifier")

        has_both_direct_catalogs = DIRECT_IDENTITY_CATALOGS <= source_registries
        only_jaspar = source_registries == {"JASPAR_CORE"}
        has_tflink_lead = "TFLink" in source_registries and tflink_target_count > 0

        if "unresolved_protein_accession" in identifier_flags:
            bucket = "exclude_unresolved_identifier"
            promotion_scope = "none"
            module_route = "identifier_mapping_required"
            evidence_readiness = "not_reviewable_as_gene_symbol"
            reason = "Protein accession is not a stable gene-symbol TF identity; map to a gene symbol before review."
        elif only_jaspar:
            bucket = "exclude_from_automatic_module_promotion_profile_only"
            promotion_scope = "none"
            module_route = "profile_validation"
            evidence_readiness = "motif_profile_only"
            reason = "JASPAR profile support identifies a DNA-binding profile but supplies no exact TF-target pair evidence."
        elif has_both_direct_catalogs:
            bucket = "promote_identity_staging"
            promotion_scope = "identity_only"
            module_route = "22B_after_exact_pair_evidence"
            evidence_readiness = "identity_supported_pair_unverified"
            reason = "Independent Lambert and AnimalTFDB3 identity catalogs agree; this supports TF identity staging only."
        elif has_tflink_lead:
            bucket = "prioritize_target_evidence_search"
            promotion_scope = "none"
            module_route = "22B_target_search"
            evidence_readiness = "aggregated_target_lead_pair_unverified"
            reason = "TFLink supplies target-membership counts, but its GMT snapshot lacks target-level assay and PMID provenance."
        else:
            bucket = "manual_identity_review"
            promotion_scope = "none"
            module_route = "unassigned_until_identity_and_pair_review"
            evidence_readiness = "single_identity_source_pair_unverified"
            reason = "Only one identity/profile lane is present and no exact-pair primary evidence is available in the expansion."

        if has_tflink_lead and bucket == "promote_identity_staging":
            reason += " TFLink target membership is retained as a separate search lead."
        if identifier_flags and bucket not in {"exclude_unresolved_identifier"}:
            reason += " Identifier flag is retained for manual review: " + ", ".join(identifier_flags) + "."

        triage.append({
            "tf_key": key,
            "display_symbols": row.get("display_symbols", ""),
            "species_scopes": row.get("species_scopes", ""),
            "source_registries": row.get("source_registries", ""),
            "source_versions": ";".join(sorted(source_versions)),
            "identity_catalogs": ";".join(sorted(source_registries & IDENTITY_CATALOGS)),
            "identity_source_count": str(identity_source_count),
            "catalog_profile_count": str(catalog_profile_count),
            "tflink_target_count": str(tflink_target_count),
            "unique_reference_pmids": str(unique_reference_pmids),
            "current_status": row.get("dedupe_status", ""),
            "identifier_flags": ";".join(identifier_flags),
            "triage_bucket": bucket,
            "promotion_scope": promotion_scope,
            "module_route": module_route,
            "evidence_readiness": evidence_readiness,
            "triage_reason": reason,
            "provenance_note": (
                "Source registries retained from tf_cross_species_collapsed.tsv and source versions "
                "rejoined from tf_candidate_crosswalk.tsv; "
                "source-specific identity records remain in the parent expansion artifact."
            ),
        })

    triage.sort(key=lambda item: (item["triage_bucket"], item["tf_key"]))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_path = args.output_dir / "tf_expansion_triage.tsv"
    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(triage)

    bucket_outputs: list[str] = []
    for bucket in sorted({row["triage_bucket"] for row in triage}):
        bucket_path = args.output_dir / f"{bucket}.tsv"
        with bucket_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(row for row in triage if row["triage_bucket"] == bucket)
        bucket_outputs.append(str(bucket_path.relative_to(ROOT)))

    counts = Counter(row["triage_bucket"] for row in triage)
    input_keys = {row["tf_key"] for row in collapsed}
    output_keys = {row["tf_key"] for row in triage}
    validation_checks = {
        "duplicate_triage_keys": len(triage) - len(output_keys),
        "input_keys_missing_from_triage": len(input_keys - output_keys),
        "triage_keys_not_in_input": len(output_keys - input_keys),
        "triage_rows_without_source_registries": sum(not row["source_registries"] for row in triage),
        "triage_rows_without_source_versions": sum(not row["source_versions"] for row in triage),
        "unexpected_module_evidence_promotions": sum(
            row["promotion_scope"] not in {"none", "identity_only"} for row in triage
        ),
        "bucket_total_mismatch": len(triage) - sum(counts.values()),
    }
    summary = {
        "status": "staging_triage_only" if all(value == 0 for value in validation_checks.values()) else "validation_failed",
        "input_new_inventory_unique_tf_keys": len(collapsed),
        "triage_rows": len(triage),
        "triage_bucket_counts": dict(sorted(counts.items())),
        "validation_checks": validation_checks,
        "canonical_write_performed": False,
        "module_evidence_promotions_performed": False,
        "policy": {
            "identity_promotion": "only both Lambert_HumanTFs and AnimalTFDB3; identity layer only",
            "tflink": "target-search lead only; GMT is not pair-level evidence",
            "jaspar_only": "excluded from automatic Module 22B promotion, not deleted from inventory",
            "unresolved_protein_accession": "excluded from gene-symbol review queue pending mapping",
            "human_mouse": "species-specific evidence remains separate; collapse is inventory-only",
        },
        "outputs": [
            str(output_path.relative_to(ROOT)),
            *bucket_outputs,
            str((args.output_dir / "triage_validation.json").relative_to(ROOT)),
        ],
    }
    (args.output_dir / "triage_manifest.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (args.output_dir / "triage_validation.json").write_text(
        json.dumps({"status": summary["status"], "checks": validation_checks}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (args.output_dir / "README.md").write_text(
        "# Public TF expansion triage v1\n\n"
        "This is a conservative staging triage of the 2,051 normalized symbols absent from the current sets in every scope. It does not write canonical TF roles, Module 22B regulons, or evidence promotions.\n\n"
        "`promote_identity_staging` means only that Lambert and AnimalTFDB3 independently support the TF identity. It is not a Module 22B evidence promotion. TFLink membership is a target-search lead because the retained GMT snapshot lacks target-level assays and PMIDs. JASPAR-only profiles and unresolved protein accessions are kept in the provenance inventory but excluded from automatic module promotion or gene-symbol review, respectively.\n\n"
        "The bucket-specific TSV files are review queues generated from the full `tf_expansion_triage.tsv` ledger. Human, mouse, and vertebrate-profile evidence must remain separate during later evidence review. See `triage_validation.json` for key/provenance invariants.\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
