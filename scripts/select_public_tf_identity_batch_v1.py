#!/usr/bin/env python3
"""Select a deterministic 100-TF identity-staging evidence pilot.

The pilot is ranked by independent identity support followed by TFLink target
network size. TFLink GMT targets are search leads only; their order is not an
evidence or confidence ranking. No canonical or evidence tables are changed.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TRIAGE = ROOT / "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/candidate_triage_v1/promote_identity_staging.tsv"
DEFAULT_RAW = ROOT / "data/raw/public_database_snapshots/tf_union_expansion_v1"
DEFAULT_OUTPUT = ROOT / "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1/identity_batches/batch_001"

BATCH_FIELDS = [
    "batch_rank", "tf_key", "display_symbols", "species_scopes", "source_registries",
    "source_versions", "identity_catalogs", "identity_source_count", "tflink_target_count",
    "identifier_flags", "selection_reason", "evidence_readiness",
]
PAIR_FIELDS = [
    "batch_rank", "tf_key", "tf_symbol", "species", "target_symbol", "tflink_uniprot_id",
    "tflink_target_count", "lead_rank_within_tf", "source_registry", "source_version",
    "source_snapshot", "lead_status", "limitations",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def norm(value: str) -> str:
    return (value or "").strip().casefold()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_gmt(path: Path) -> dict[str, tuple[str, str, list[str]]]:
    output: dict[str, tuple[str, str, list[str]]] = {}
    with path.open(encoding="utf-8", errors="replace") as handle:
        for line in handle:
            fields = line.rstrip("\n").split("\t")
            if len(fields) < 3:
                continue
            tf_symbol, uniprot, *targets = fields
            output[norm(tf_symbol)] = (tf_symbol, uniprot, list(dict.fromkeys(targets)))
    return output


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--triage", type=Path, default=DEFAULT_TRIAGE)
    parser.add_argument("--raw-dir", type=Path, default=DEFAULT_RAW)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--size", type=int, default=100)
    parser.add_argument("--targets-per-species", type=int, default=4)
    args = parser.parse_args()

    candidates = [
        row for row in read_tsv(args.triage)
        if not row.get("identifier_flags")
    ]
    candidates.sort(
        key=lambda row: (
            -int(row.get("tflink_target_count", "0") or 0),
            -int(row.get("identity_source_count", "0") or 0),
            row.get("tf_key", ""),
        )
    )
    selected = candidates[:args.size]
    human_gmt = args.raw_dir / "tflink_human_v1.0.gmt"
    mouse_gmt = args.raw_dir / "tflink_mouse_v1.0.gmt"
    gmt = {"human": read_gmt(human_gmt), "mouse": read_gmt(mouse_gmt)}
    gmt_paths = {"human": human_gmt, "mouse": mouse_gmt}

    batch_rows: list[dict[str, str]] = []
    pair_rows: list[dict[str, str]] = []
    no_lead_species: list[str] = []
    for batch_rank, row in enumerate(selected, start=1):
        batch_rows.append({
            "batch_rank": str(batch_rank),
            "tf_key": row["tf_key"],
            "display_symbols": row.get("display_symbols", ""),
            "species_scopes": row.get("species_scopes", ""),
            "source_registries": row.get("source_registries", ""),
            "source_versions": row.get("source_versions", ""),
            "identity_catalogs": row.get("identity_catalogs", ""),
            "identity_source_count": row.get("identity_source_count", ""),
            "tflink_target_count": row.get("tflink_target_count", ""),
            "identifier_flags": row.get("identifier_flags", ""),
            "selection_reason": "Top TFLink target-count rank among clean dual-catalog identity candidates; identity support is independent of target evidence.",
            "evidence_readiness": row.get("evidence_readiness", ""),
        })
        scopes = set(row.get("species_scopes", "").split(";")) & {"human", "mouse"}
        for species in sorted(scopes):
            raw_tf_symbol, uniprot, targets = gmt[species].get(row["tf_key"], ("", "", []))
            if not targets:
                no_lead_species.append(f"{row['tf_key']}|{species}")
                continue
            for lead_rank, target in enumerate(targets[: args.targets_per_species], start=1):
                pair_rows.append({
                    "batch_rank": str(batch_rank),
                    "tf_key": row["tf_key"],
                    "tf_symbol": raw_tf_symbol,
                    "species": species,
                    "target_symbol": target,
                    "tflink_uniprot_id": uniprot,
                    "tflink_target_count": row.get("tflink_target_count", ""),
                    "lead_rank_within_tf": str(lead_rank),
                    "source_registry": "TFLink",
                    "source_version": "TFLink_v1.0_snapshot",
                    "source_snapshot": str(gmt_paths[species].relative_to(ROOT)),
                    "lead_status": "target_search_lead_only",
                    "limitations": "GMT membership has no target-level assay, source database, or PMID; exact-pair literature review required.",
                })

    args.output_dir.mkdir(parents=True, exist_ok=True)
    batch_path = args.output_dir / "identity_staging_batch_001.tsv"
    pair_path = args.output_dir / "tflink_pair_search_leads.tsv"
    write_tsv(batch_path, BATCH_FIELDS, batch_rows)
    write_tsv(pair_path, PAIR_FIELDS, pair_rows)
    manifest = {
        "status": "staging_pilot_only",
        "selection_size_requested": args.size,
        "selected_identity_candidates": len(batch_rows),
        "clean_identity_candidates_available": len(candidates),
        "ranking": "descending TFLink target-count, identity-source-count, normalized TF key",
        "targets_per_species": args.targets_per_species,
        "pair_search_lead_rows": len(pair_rows),
        "tf_species_without_tflink_leads": no_lead_species,
        "canonical_write_performed": False,
        "module_evidence_promotions_performed": False,
        "limitations": [
            "Identity staging is not Module 22B evidence promotion.",
            "TFLink GMT targets are search leads, not independently verified TF-target assertions.",
            "Human and mouse leads remain separate.",
        ],
        "inputs": {
            "triage": str(args.triage.relative_to(ROOT)),
            "human_gmt": {"path": str(human_gmt.relative_to(ROOT)), "sha256": sha256(human_gmt)},
            "mouse_gmt": {"path": str(mouse_gmt.relative_to(ROOT)), "sha256": sha256(mouse_gmt)},
        },
        "outputs": [str(batch_path.relative_to(ROOT)), str(pair_path.relative_to(ROOT))],
    }
    (args.output_dir / "batch_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (args.output_dir / "README.md").write_text(
        "# Identity-staging evidence pilot batch 001\n\n"
        "This batch contains the top 100 clean dual-catalog identity candidates ranked by TFLink target-count signal. It is a bounded evidence-search pilot. Identity support does not promote a TF-target edge.\n\n"
        "`tflink_pair_search_leads.tsv` contains up to four TFLink GMT target leads per species and TF. These are discovery leads only; exact-pair primary literature and independent corroboration are required before any Module 22B promotion.\n",
        encoding="utf-8",
    )
    print(json.dumps(manifest, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
