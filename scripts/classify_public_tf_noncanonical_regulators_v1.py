#!/usr/bin/env python3
"""Stage likely noncanonical transcriptional regulators from the public TF union.

This is a conservative, source-preserving role screen. It does not assert that
every matched protein regulates a particular gene and it does not promote a
canonical TF role or a Module 22B edge. The curated symbols/prefixes below are
only a first-pass screen for proteins whose primary biology is chromatin
modification, chromatin architecture, transcriptional co-regulation, or
transcriptional complex activity.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/tf_expansion_triage.tsv"
DEFAULT_OUTPUT = ROOT / "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1"


# Exact symbols are used for families with mixed canonical-TF membership. Broad
# prefixes are restricted to families whose members are predominantly chromatin
# or transcriptional-complex proteins in this staging screen.
EXACT_BY_CATEGORY = {
    "chromatin_modifier_or_reader": {
        "ATAD2", "ATF7IP", "ATRX", "BAP1", "BAZ2A", "BAZ2B", "CENPA", "CXXC1",
        "DAXX", "DNMT1", "DNMT3A", "DNMT3B", "DNMT3L", "DPF2", "DPY30", "EHMT1", "EHMT2",
        "EMSY", "EP400", "EP300", "EZH1", "EZH2", "GATAD1", "GATAD2A", "GATAD2B", "H2AZ1",
        "HDAC1", "HDAC2",
        "HDAC3", "HDAC4", "HDAC5", "HDAC6", "HDAC7", "HDAC8", "HDAC9",
        "HDAC10", "HDAC11", "MBD2", "MBD3", "MBD4", "MBD5", "MBD6",
        "KANSL1", "KANSL3", "L3MBTL2", "L3MBTL3", "L3MBTL4", "MECP2", "MORC2", "MYSM1", "PBRM1", "PCGF1", "PCGF6", "PHF5A", "PHF6", "PRMT1", "PRMT5", "RBBP4", "RBBP5", "RBBP7",
        "SETD1A", "SETD1B", "SETD2", "SETD5", "SETD6", "SETD7", "SETD8",
        "SMYD2", "SMYD3", "SMYD4", "SMYD5", "SUV39H1", "SUV39H2", "SUZ12",
        "SIRT6", "SP110", "SP140L", "TET1", "TET2", "TET3", "TRIM28", "TRIM33", "UBN1", "UHRF1", "USP7", "USP16", "WDR5", "WIZ", "YEATS4", "ZZZ3",
    },
    "chromatin_remodeler_or_architecture": {
        "ANP32E", "ARID1A", "ARID1B", "ARID2", "ARID4A", "ARID4B", "ARID5A", "ARID5B",
        "ASH2L", "BAZ1A", "BAZ1B", "BCL7A", "BCL7B", "BCL7C", "BRPF1", "BRPF2", "BRWD1",
        "CBX1", "CBX2", "CBX3", "CBX4", "CBX5", "CBX6", "CBX7", "CBX8",
        "BRPF3", "CHD1", "CHD2", "CHD3", "CHD4", "CHD5", "CHD6", "CHD7",
        "CHD8", "CHD9", "HELLS", "INO80", "JARID2", "NIPBL", "NCAPD2",
        "NCAPD3", "NCAPH", "NCAPH2", "NCAPG", "PBRM1", "RAD21", "SMARCA2",
        "SMARCA4", "SMARCAD1", "SMARCB1", "SMARCC1", "SMARCC2", "SMARCD1",
        "SMARCD2", "SMARCD3", "SMARCE1", "SMC1A", "SMC3", "SMCHD1", "STAG1",
        "STAG2", "SRCAP", "SSRP1", "SFMBT1", "SCML2", "RYBP", "RING1",
    },
    "transcriptional_coregulator_or_complex": {
        "AATF", "ADNP", "ADNP2", "AFF1", "AFF2", "AFF3", "AFF4", "ANKRD11",
        "ASXL2", "ATN1", "AUTS2", "BAHD1", "BANP", "BAP18", "BCOR", "BCLAF1", "BICRA", "CBFA2T2", "CARM1", "CCAR2", "CDC73", "CITED1", "CITED2", "CITED4", "CNOT1",
        "CNOT2", "CRTC1", "CRTC2", "CRTC3", "CTBP1", "CTBP2", "DACH1",
        "DACH2", "DIP2A", "DIP2B", "DIP2C", "DR1", "DRAP1", "EAF1", "EAF2",
        "CDYL", "CHAF1A", "CHAF1B", "CXXC4", "DIDO1", "DPPA2", "DPPA3", "DPPA4", "ELL1", "ELL2", "ELL3", "EPOP", "GPS2", "GSE1", "HCFC1", "HMG20A", "HMG20B", "HMGXB4", "INTS3", "JMJD6", "LCOR",
        "LDB1", "LDB2", "LEO1", "MED1", "MED4", "MED6", "MED7", "MED8",
        "MED9", "MED10", "MED11", "MED12", "MED13", "MED14", "MED15", "MED16",
        "MED17", "MED18", "MED19", "MED20", "MED22", "MED23", "MED24", "MNAT1",
        "LMO1", "LMO2", "LMO3", "LMO4", "MIER3", "NCOA1", "NCOA2", "NCOA3", "NCOA4", "NCOA6", "NCOA7", "NCOR1", "NCOR2",
        "PAF1", "PPARGC1A", "PPARGC1B", "RCOR1", "RCOR2", "RCOR3", "RERE",
        "SAP130", "SAP30", "SIN3A", "SIN3B", "SKIL", "SPEN", "SS18", "SUPT5H", "TBL1XR1", "TLE1",
        "TLE2", "TLE3", "TLE4", "TLE5", "TLE6", "TRRAP", "WWTR1", "YAP1",
        "ZMIZ1", "ZMYM2", "ZMYM3", "ZMYM4", "ZNF532", "ZNF592", "ZNF687", "ZNF827",
    },
    "transcriptional_modifier_or_elongation_factor": {
        "CDK7", "CDK8", "CDK9", "CDK12", "CDK13", "CCNT2", "INTS11", "INTS12", "INTS13", "KAT2A", "KAT2B", "KAT5",
        "KAT6A", "KAT6B", "KAT7", "KAT8", "PAF1", "SUPT4H1", "SUPT5H",
        "SUPT6H", "TAF1", "TAF2", "TAF3", "TAF4", "TAF5", "TAF6", "TAF7", "TAF9", "TAF10",
        "TAF11", "TAF12", "TAF15", "LARP7", "MLLT1", "NELFA", "NELFE", "PCF11", "SSU72",
    },
}

PREFIX_BY_CATEGORY = {
    "chromatin_modifier_or_reader": ("BRD", "EHMT", "HDAC", "KAT", "KDM", "KMT", "NSD", "SETD", "SUV"),
    "chromatin_remodeler_or_architecture": ("BAZ", "BRPF", "CBX", "CHD", "PCGF", "SMAR", "SMC", "STAG"),
    "transcriptional_coregulator_or_complex": ("MED", "NCOA", "NCOR", "RCOR", "TLE", "ZMYM"),
}

FIELDS = [
    "regulator_key", "display_symbols", "species_scopes", "source_registries",
    "source_versions", "identity_catalogs", "triage_bucket", "identity_source_count",
    "catalog_profile_count", "tflink_target_count", "matched_role_signals",
    "role_category", "classification_confidence", "classification_status", "module_route", "module22b_eligibility",
    "evidence_readiness", "provenance_note",
]

PROVISIONAL_SYMBOLS = {
    "ANP32E", "ASXL2", "AUTS2", "BAHD1", "BANP", "BAP18", "BRWD1", "CARM1",
    "CBFA2T2", "CCAR2", "CDC73", "CDYL", "CHAF1A", "CXXC4", "DIDO1", "DPPA2",
    "DPPA3", "DPPA4", "KANSL1", "KANSL3", "UBN1", "WIZ", "ZNF532", "ZNF592",
    "ZNF687", "ZNF827", "ZZZ3",
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def split_symbols(value: str) -> list[str]:
    return [item.strip().upper() for item in (value or "").split(";") if item.strip()]


def numeric(value: str) -> int:
    try:
        return int(value or 0)
    except ValueError:
        return 0


def classify(symbols: list[str]) -> tuple[list[str], list[str]]:
    matches: list[tuple[str, str]] = []
    for category, names in EXACT_BY_CATEGORY.items():
        for symbol in symbols:
            if symbol in names:
                matches.append((symbol, category))
    for category, prefixes in PREFIX_BY_CATEGORY.items():
        for symbol in symbols:
            if any(symbol.startswith(prefix) for prefix in prefixes):
                matches.append((symbol, category))
    signals = sorted({f"{symbol}:{category}" for symbol, category in matches})
    categories = sorted({category for _, category in matches})
    return signals, categories


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    rows = read_tsv(args.input)
    staged: list[dict[str, str]] = []
    for row in rows:
        symbols = split_symbols(row.get("display_symbols", ""))
        signals, categories = classify(symbols)
        if not signals:
            continue
        tflink = numeric(row.get("tflink_target_count", ""))
        catalog = numeric(row.get("catalog_profile_count", ""))
        if tflink and row.get("identity_catalogs"):
            readiness = "identity_plus_aggregated_target_lead"
        elif tflink:
            readiness = "aggregated_target_lead_only"
        elif catalog:
            readiness = "identity_plus_profile_only"
        else:
            readiness = "identity_catalog_only"
        staged.append({
            "regulator_key": row["tf_key"],
            "display_symbols": row.get("display_symbols", ""),
            "species_scopes": row.get("species_scopes", ""),
            "source_registries": row.get("source_registries", ""),
            "source_versions": row.get("source_versions", ""),
            "identity_catalogs": row.get("identity_catalogs", ""),
            "triage_bucket": row.get("triage_bucket", ""),
            "identity_source_count": row.get("identity_source_count", ""),
            "catalog_profile_count": row.get("catalog_profile_count", ""),
            "tflink_target_count": row.get("tflink_target_count", ""),
            "matched_role_signals": ";".join(signals),
            "role_category": ";".join(categories),
            "classification_confidence": (
                "provisional_screen" if any(symbol in PROVISIONAL_SYMBOLS for symbol in symbols)
                else "high_signal_screen"
            ),
            "classification_status": "staged_noncanonical_regulator_candidate",
            "module_route": "separate_noncanonical_regulator_queue",
            "module22b_eligibility": "not_strict_tf_pending_role_and_pair_review",
            "evidence_readiness": readiness,
            "provenance_note": (
                "Candidate selected by the conservative family/symbol screen; source registries, "
                "source versions, species scope, and parent raw identity records remain authoritative. "
                "This row is a role-review candidate, not a biological assertion or evidence promotion."
            ),
        })

    staged.sort(key=lambda row: (row["role_category"], row["regulator_key"]))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output = args.output_dir / "noncanonical_regulator_staging.tsv"
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(staged)

    counts = Counter(row["role_category"] for row in staged)
    bucket_counts = Counter(row["triage_bucket"] for row in staged)
    readiness_counts = Counter(row["evidence_readiness"] for row in staged)
    confidence_counts = Counter(row["classification_confidence"] for row in staged)
    source_counts = Counter(
        source
        for row in staged
        for source in row["source_registries"].split(";")
        if source
    )
    keys = [row["regulator_key"] for row in staged]
    summary_path = args.output_dir / "noncanonical_regulator_staging_summary.json"
    summary = {
        "status": "staging_only",
        "input_rows": len(rows),
        "staged_rows": len(staged),
        "duplicate_regulator_keys": len(keys) - len(set(keys)),
        "role_category_counts": dict(sorted(counts.items())),
        "triage_bucket_counts": dict(sorted(bucket_counts.items())),
        "evidence_readiness_counts": dict(sorted(readiness_counts.items())),
        "classification_confidence_counts": dict(sorted(confidence_counts.items())),
        "source_registry_presence_counts": dict(sorted(source_counts.items())),
        "canonical_writes_performed": False,
        "module22b_promotions_performed": False,
        "policy": {
            "screen": "conservative exact-symbol and family-prefix role screen",
            "species": "human/mouse evidence remains separate during later review",
            "module22b": "role staging does not create strict TF identity or TF-target evidence",
            "provenance": "source registries and parent identity records remain authoritative",
        },
        "outputs": [
            str(output.relative_to(ROOT)),
            str(summary_path.relative_to(ROOT)),
        ],
    }
    summary_path.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
