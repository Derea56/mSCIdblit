#!/usr/bin/env python3
"""Validate and merge the disjoint priority-TF agent review lanes.

The merge is intentionally evidence-ledger only.  It rejects duplicate
species/TF/target rows, missing terminal decisions, and unsupported module
routing.  It does not write canonical SignalingEdge or Regulon rows.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LANE_DIR = ROOT / "work/public_tf_curation/agent_lanes"
DEFAULT_OUTPUT = ROOT / "data/processed/public_tf_union_v1/module_curation/agent_merged"

LANES = {
    "lane_A_tp53_jun_fos_myc.tsv": {"TP53", "JUN", "FOS", "MYC"},
    "lane_B_stat1_hif1a_ets1.tsv": {"STAT1", "HIF1A", "ETS1"},
    "lane_C_sp1_runx1_gata3_cebpb.tsv": {"SP1", "RUNX1", "GATA3", "CEBPB"},
    "lane_D_irf1_atf2_egr1_klf4.tsv": {"IRF1", "ATF2", "EGR1", "KLF4"},
    "lane_E_nfkb2_boundary.tsv": {"NFKB2"},
}

FIELDS = [
    "species", "tf_symbol", "target_symbol", "external_record_keys", "decision",
    "module_assignment", "evidence_status", "support_kind", "effect_polarity",
    "primary_pmids", "corroborating_pmids", "shared_paper_status",
    "cross_module_status", "cell_type_context", "stimulus_context", "limitations",
    "notes",
]
ALLOWED_DECISIONS = {
    "promote_to_22B",
    "promote_to_20B",
    "promote_to_21B",
    "promote_to_23B",
    "promote_to_24B",
    "hold_exact_pair",
    "hold_direction_conflict",
    "database_only_unverified",
}
ALLOWED_SPECIES = {"human", "mouse"}
MODULES = {"20A", "20B", "21A", "21B", "22A", "22B", "23A", "23B", "24A", "24B"}
TF_ALIASES = {"TRP53": "TP53"}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in FIELDS} for row in rows)


def module_tokens(value: str) -> set[str]:
    tokens = {token.strip() for token in value.replace(",", ";").replace("/", ";").split(";") if token.strip()}
    return {token.removesuffix("_candidate") for token in tokens}


def has_actual_cross_module_status(value: str) -> bool:
    normalized = (value or "").strip().lower()
    return bool(normalized) and normalized not in {
        "not_applicable",
        "no_overlap_with_modules_20_21_23_24",
        "no_modules_20_21_23_24_overlap",
        "no_verified_cross_module_claim",
        "not_claimed",
        "none",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lane-dir", type=Path, default=DEFAULT_LANE_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    errors: list[str] = []
    merged: list[dict[str, str]] = []
    boundary_audit: list[dict[str, str]] = []
    seen_pairs: set[tuple[str, str, str]] = set()
    lane_counts: Counter[str] = Counter()
    tf_seen: dict[str, set[str]] = {tf: set() for tfs in LANES.values() for tf in tfs}

    for filename, expected_tfs in LANES.items():
        path = args.lane_dir / filename
        if not path.is_file():
            errors.append(f"missing lane file: {path}")
            continue
        rows = read_tsv(path)
        if not rows:
            errors.append(f"empty lane file: {path}")
            continue
        missing = sorted(set(FIELDS) - set(rows[0]))
        if missing:
            errors.append(f"{filename} missing fields: {', '.join(missing)}")
            continue
        for line_number, row in enumerate(rows, start=2):
            raw_tf = row["tf_symbol"].strip().upper()
            tf = TF_ALIASES.get(raw_tf, raw_tf)
            species = row["species"].strip().lower()
            target = row["target_symbol"].strip()
            pair = (species, tf, target.casefold())
            boundary_audit_row = filename == "lane_E_nfkb2_boundary.tsv" and has_actual_cross_module_status(row["cross_module_status"])
            if tf not in expected_tfs and not boundary_audit_row:
                errors.append(f"{filename}:{line_number}: TF {tf} is outside this lane")
            if species not in ALLOWED_SPECIES:
                errors.append(f"{filename}:{line_number}: invalid species {species}")
            if (not target or target in {"\\N", "NA", "null"}) and not boundary_audit_row:
                errors.append(f"{filename}:{line_number}: missing target symbol")
            if row["decision"] not in ALLOWED_DECISIONS:
                errors.append(f"{filename}:{line_number}: invalid decision {row['decision']}")
            if pair in seen_pairs and not boundary_audit_row:
                errors.append(f"duplicate species/TF/target pair: {pair}")
            if not boundary_audit_row:
                seen_pairs.add(pair)
            if not boundary_audit_row:
                tf_seen.setdefault(tf, set()).add(species)
            tokens = module_tokens(row["module_assignment"])
            if not tokens or not tokens.issubset(MODULES):
                errors.append(f"{filename}:{line_number}: invalid module assignment {row['module_assignment']}")
            if row["decision"].startswith("promote_to_"):
                expected_module = row["decision"].removeprefix("promote_to_")
                if expected_module not in tokens:
                    errors.append(f"{filename}:{line_number}: promotion/module mismatch")
                if not row["primary_pmids"].strip():
                    errors.append(f"{filename}:{line_number}: promotion lacks primary PMID")
            if row["decision"] == "database_only_unverified" and not boundary_audit_row and row["evidence_status"].strip() not in {"", "database_curated", "database_curated_unverified", "database_only_unverified", "unverified_public_record"}:
                errors.append(f"{filename}:{line_number}: database-only row has non-database evidence status")
            if boundary_audit_row and row["decision"].startswith("promote_to_"):
                errors.append(f"{filename}:{line_number}: boundary-audit row cannot be a promotion")
            if has_actual_cross_module_status(row["cross_module_status"]) and row["decision"].startswith("promote_to_"):
                if not row["corroborating_pmids"].strip():
                    errors.append(f"{filename}:{line_number}: cross-module promotion lacks corroborating PMID")
            if boundary_audit_row:
                boundary_audit.append(row)
            else:
                merged.append(row)
            lane_counts[filename] += 1

    missing_tfs = sorted(tf for tf, species in tf_seen.items() if not species)
    if missing_tfs:
        errors.append("TFs with no agent rows: " + ", ".join(missing_tfs))

    status = "pass" if not errors else "fail"
    args.output_dir.mkdir(parents=True, exist_ok=True)
    if not errors:
        write_tsv(args.output_dir / "priority_tf_agent_merged.tsv", merged)
        write_tsv(args.output_dir / "priority_tf_agent_boundary_audit.tsv", boundary_audit)
    manifest = {
        "status": status,
        "lane_counts": dict(lane_counts),
        "merged_rows": len(merged),
        "boundary_audit_rows": len(boundary_audit),
        "tf_species_coverage": {tf: sorted(species) for tf, species in sorted(tf_seen.items())},
        "decision_counts": dict(Counter(row["decision"] for row in merged)),
        "errors": errors,
        "canonical_database_writes": False,
        "frozen_release_modified": False,
    }
    (args.output_dir / "priority_tf_agent_merge_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
