#!/usr/bin/env python3
"""Build a ranked, module-routed inventory of non-priority public TFs.

The inventory is a planning artifact.  It does not promote records or edit
the canonical graph/database.  TF-target assertions default to Module 22B;
existing overlap with Modules 20B, 21B, 23B, or 24B is recorded as a review
flag rather than treated as evidence for that module.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data/processed/public_tf_union_v1"
DEFAULT_OUTPUT = DEFAULT_INPUT / "module_curation/new_tf_inventory.tsv"

PRIORITY_TFS = {
    "tp53", "trp53", "jun", "fos", "myc", "stat1", "hif1a", "sp1",
    "ets1", "runx1", "gata3", "cebpb", "irf1", "atf2", "egr1", "klf4", "nfkb2",
}
MODULE_NAMES = {"20B", "21B", "23B", "24B"}
PMID_RE = re.compile(r"(?<!\d)(?:PMID\s*[:]?\s*)?(\d{7,9})(?!\d)", re.I)
UNIPROT_RE = re.compile(r"^(?:[OPQ][0-9][A-Z0-9]{4,7}|A0A[0-9A-Z]{6,})$", re.I)

FIELDS = [
    "species", "tf_symbol", "tf_key", "source_labels", "source_record_count",
    "records_with_reference", "unique_reference_pmids", "source_registries",
    "mapping_decision", "frozen_entity_match_status", "frozen_entity_ids",
    "explicit_tf_role_present", "default_module", "existing_module_overlap_flags",
    "both_species_present", "priority_rank", "review_status", "notes",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in FIELDS} for row in rows)


def pmids(value: str) -> set[str]:
    return set(PMID_RE.findall(value or ""))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    source_rows = read_tsv(args.input_dir / "source_records.tsv")
    mapping_rows = read_tsv(args.input_dir / "frozen_entity_mapping.tsv")

    mapping_by_pair: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    labels_by_pair: dict[tuple[str, str], set[str]] = defaultdict(set)
    for mapping in mapping_rows:
        if mapping.get("identity_role") != "tf":
            continue
        symbol = mapping.get("normalized_symbol", "").strip()
        if not symbol or symbol == r"\N":
            continue
        pair = (mapping["species_context"].casefold(), mapping["normalized_symbol_key"].casefold())
        mapping_by_pair[pair].append(mapping)
        labels_by_pair[pair].add(mapping.get("source_symbol", ""))

    source_by_pair: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for source in source_rows:
        symbol = source.get("tf_normalized_symbol", "").strip()
        key = source.get("tf_normalized_symbol_key", "").strip()
        if not symbol or symbol == r"\N" or not key or key == r"\N":
            continue
        source_by_pair[(source["species_context"].casefold(), key.casefold())].append(source)

    module_overlap: dict[tuple[str, str], set[str]] = defaultdict(set)
    queue_dir = args.input_dir / "module_curation"
    for queue_path in sorted(queue_dir.glob("module_*_corroboration_queue.tsv")):
        for row in read_tsv(queue_path):
            species = row.get("species_context", row.get("species", "")).strip().casefold()
            tf = row.get("tf_symbol", "").strip().casefold()
            modules = {
                token.strip()
                for token in row.get("existing_modules", row.get("module", "")).replace(",", ";").split(";")
                if token.strip()
            }
            if species and tf:
                module_overlap[(species, tf)].update(modules & MODULE_NAMES)

    species_by_key: dict[str, set[str]] = defaultdict(set)
    for species, key in mapping_by_pair:
        symbol = mapping_by_pair[(species, key)][0]["normalized_symbol"].strip()
        if key not in PRIORITY_TFS and not UNIPROT_RE.fullmatch(symbol):
            species_by_key[key].add(species)

    rows: list[dict[str, object]] = []
    for (species, key), mappings in sorted(mapping_by_pair.items()):
        mapping = mappings[0]
        symbol = mapping["normalized_symbol"].strip()
        if key in PRIORITY_TFS or UNIPROT_RE.fullmatch(symbol):
            continue
        records = source_by_pair.get((species, key), [])
        reference_ids = set().union(*(pmids(row.get("reference_pmids", "")) for row in records))
        records_with_reference = sum(bool(pmids(row.get("reference_pmids", ""))) for row in records)
        registries = sorted({row.get("source_registry", "") for row in records if row.get("source_registry")})
        entity_ids = sorted({row.get("mscidblit_entity_id", "") for row in mappings if row.get("mscidblit_entity_id") not in {"", r"\N"}})
        match_status = sorted({row.get("frozen_entity_match_status", "") for row in mappings if row.get("frozen_entity_match_status")})
        overlap = sorted(module_overlap.get((species, key), set()))
        both_species = len(species_by_key.get(key, set())) == 2
        rank_score = (
            (1000 if both_species else 0)
            + min(len(reference_ids), 250)
            + min(len(records), 250) // 4
            + (50 if "mapped_unique" in match_status else 0)
            + 25 * len(overlap)
        )
        notes = []
        if not records:
            notes.append("identity mapping has no matching source record")
        if not reference_ids:
            notes.append("no PMID parsed from imported source records")
        if overlap:
            notes.append("module overlap is a routing flag, not cross-module evidence")
        rows.append({
            "species": species,
            "tf_symbol": symbol,
            "tf_key": key,
            "source_labels": ";".join(sorted(labels_by_pair[(species, key)])),
            "source_record_count": len(records),
            "records_with_reference": records_with_reference,
            "unique_reference_pmids": len(reference_ids),
            "source_registries": ";".join(registries),
            "mapping_decision": mapping.get("identity_decision", ""),
            "frozen_entity_match_status": ";".join(match_status),
            "frozen_entity_ids": ";".join(entity_ids),
            "explicit_tf_role_present": "true" if any(row.get("frozen_tf_role_present") == "t" for row in mappings) else "false",
            "default_module": "22B",
            "existing_module_overlap_flags": ";".join(overlap),
            "both_species_present": "true" if both_species else "false",
            "priority_rank": rank_score,
            "review_status": "new_candidate",
            "notes": "; ".join(notes),
        })

    rows.sort(key=lambda row: (-int(row["priority_rank"]), row["tf_key"], row["species"]))
    write_tsv(args.output, rows)
    print({
        "rows": len(rows),
        "species_tf_pairs": len({(row["species"], row["tf_key"]) for row in rows}),
        "tf_keys": len({row["tf_key"] for row in rows}),
        "both_species_rows": sum(row["both_species_present"] == "true" for row in rows),
        "default_module": "22B",
        "output": str(args.output),
    })


if __name__ == "__main__":
    main()
