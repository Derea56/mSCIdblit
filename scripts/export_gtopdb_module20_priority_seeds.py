#!/usr/bin/env python3
"""Normalize GtoPdb endogenous ligand pairings into Module 20A seed tables."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


SOURCE_VERSION = "2026.2"
SOURCE_DATE = "2026-06-15"

OUTPUT_HEADERS = [
    "source_record_id",
    "source_database",
    "source_version",
    "source_date",
    "ligand_id",
    "ligand_display",
    "ligand_type",
    "ligand_species",
    "target_id",
    "target_display",
    "target_name_exact",
    "target_species",
    "species_note",
    "target_family_name",
    "target_type",
    "pair_label",
    "matched_families",
    "rank_potency_pmids",
    "interaction_pmids",
    "interaction_species_seen",
    "list_comment",
]


def parse_args() -> argparse.Namespace:
    root = Path(__file__).resolve().parents[1]
    base_dir = root / "work" / "module20_db_seed"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--pairings",
        type=Path,
        default=base_dir / "GtoPdb_endogenous_ligand_pairings_all_2026_2.tsv",
    )
    parser.add_argument(
        "--detailed",
        type=Path,
        default=base_dir / "GtoPdb_endogenous_ligand_detailed_2026_2.tsv",
    )
    parser.add_argument(
        "--targets",
        type=Path,
        default=base_dir / "GtoPdb_targets_and_families_2026_2.tsv",
    )
    parser.add_argument(
        "--ligands",
        type=Path,
        default=base_dir / "GtoPdb_ligands_2026_2.tsv",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=base_dir / "gtopdb_module20_priority_seeds",
    )
    return parser.parse_args()


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return value[1:-1]
    return value


def iter_dict_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        filtered = (
            line
            for line in handle
            if not strip_quotes(line).startswith("#")
        )
        reader = csv.DictReader(filtered, delimiter="\t", quotechar='"')
        rows: list[dict[str, str]] = []
        for row in reader:
            cleaned = {strip_quotes(key): strip_quotes(value or "") for key, value in row.items() if key is not None}
            rows.append(cleaned)
        return rows


def join_nonempty(values: list[str]) -> str:
    return "|".join(value for value in values if value)


def collect_pmids(raw: str) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for token in raw.split("|"):
        token = token.strip()
        if not token or token in seen:
            continue
        seen.add(token)
        ordered.append(token)
    return ordered


def normalize_text(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text).strip().lower()


def family_matches(text: str) -> list[str]:
    checks = [
        (
            "chemokine_family",
            (
                "chemokine",
                " ccl",
                " cxcl",
                " cx3cl",
                " xcl",
                " ccr",
                " cxcr",
                " ackr",
            ),
        ),
        (
            "il_family",
            (
                "interleukin",
                " il-",
                " il ",
                "il1r",
                "il6r",
                "il10r",
                "il17r",
                "il20r",
                "il22r",
                "il1 receptor",
                "interleukin receptor",
            ),
        ),
        (
            "interferon_family",
            ("interferon", " ifn", "ifnar", "ifngr", "ifnlr"),
        ),
        (
            "tnf_family",
            ("tumor necrosis factor", " tnf", "tnfr", "tweak", "fas ligand", "rankl", "traf?"),
        ),
        (
            "tgfb_bmp_family",
            (
                "transforming growth factor",
                "tgf-beta",
                "tgfb",
                "bone morphogenetic",
                " bmp",
                "activin",
                "inhibin",
                "gdf",
                "amhr",
            ),
        ),
        (
            "growth_factor_family",
            (
                "growth factor",
                "epidermal growth factor",
                "fibroblast growth factor",
                "vascular endothelial growth factor",
                "platelet-derived growth factor",
                "hepatocyte growth factor",
                "neurotrophin",
                "insulin-like growth factor",
                "colony-stimulating factor",
                "egfr",
                "fgfr",
                "vegfr",
                "pdgfr",
                "csf1r",
                "csf2ra",
                "csf2rb",
                "kit receptor",
                "met receptor",
                "trk",
            ),
        ),
        (
            "wnt_notch_family",
            ("wnt", "frizzled", " notch", " jagged", " delta-like", " dll", " lrp5", " lrp6"),
        ),
        (
            "complement_family",
            ("complement", " c3a", " c5a", " c5ar", " c3ar", "cr1", "cr2", "cr3"),
        ),
        (
            "damp_purinergic_tlr_family",
            (
                "toll-like",
                " tlr",
                "purinergic",
                "p2rx",
                "p2ry",
                "adenosine receptor",
                "atp ",
                " adp",
                "adenosine triphosphate",
                "adenosine diphosphate",
                "hmgb1",
                "rage",
                "ager",
            ),
        ),
        (
            "guidance_ecm_family",
            (
                "integrin",
                "collagen",
                "laminin",
                "fibronectin",
                "vitronectin",
                "tenascin",
                "thrombospondin",
                "syndecan",
                "semaphorin",
                "plexin",
                "netrin",
                "dcc",
                "ephrin",
                "eph receptor",
                "slit",
                "robo",
                "cadherin",
                "agrin",
                "reelin",
                "ncam",
            ),
        ),
    ]

    padded = f" {text} "
    hits = [family for family, terms in checks if any(term in padded for term in terms)]
    return sorted(set(hits))


def ligand_display(row: dict[str, str], ligand_lookup: dict[str, dict[str, str]]) -> str:
    subunit = row.get("Ligand Subunit Name", "").strip()
    if subunit:
        return subunit
    ligand_id = row["Ligand ID"]
    ligand_row = ligand_lookup.get(ligand_id, {})
    name = ligand_row.get("Name", "").strip()
    if name:
        return name
    return row.get("Ligand Name", "").strip()


def target_display(target_row: dict[str, str], target_species: str, target_name_exact: str) -> str:
    if target_species == "Mouse":
        symbol = target_row.get("MGI symbol", "").strip()
        if symbol:
            return symbol
    if target_species == "Human":
        symbol = target_row.get("HGNC symbol", "").strip()
        if symbol:
            return symbol
    return target_name_exact


def build_detailed_index(rows: list[dict[str, str]]) -> dict[tuple[str, str, str], dict[str, str]]:
    index: dict[tuple[str, str, str], dict[str, str]] = {}
    for row in rows:
        key = (row["Ligand ID"], row["Target ID"], row["Target Species"])
        entry = index.setdefault(
            key,
            {
                "interaction_pmids": "",
                "interaction_species_seen": "",
            },
        )
        pmids = collect_pmids(entry["interaction_pmids"])
        pmids.extend(collect_pmids(row.get("Interaction PubMed IDs", "")))
        species_seen = [value for value in entry["interaction_species_seen"].split("|") if value]
        interaction_species = row.get("Interaction Species", "").strip()
        if interaction_species and interaction_species not in species_seen:
            species_seen.append(interaction_species)
        entry["interaction_pmids"] = join_nonempty(collect_pmids("|".join(pmids)))
        entry["interaction_species_seen"] = join_nonempty(species_seen)
    return index


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_HEADERS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def write_summary(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    pairings = iter_dict_rows(args.pairings)
    detailed = iter_dict_rows(args.detailed)
    targets = iter_dict_rows(args.targets)
    ligands = iter_dict_rows(args.ligands)

    target_lookup = {row["Target id"]: row for row in targets if row.get("Target id")}
    ligand_lookup = {row["Ligand ID"]: row for row in ligands if row.get("Ligand ID")}
    detailed_index = build_detailed_index(detailed)

    species_by_pair: dict[tuple[str, str], set[str]] = defaultdict(set)
    for row in pairings:
        species_by_pair[(row["Ligand ID"], row["Target ID"])].add(row["Target Species"])

    all_rows: list[dict[str, str]] = []
    priority_rows: list[dict[str, str]] = []

    for row in pairings:
        target_species = row.get("Target Species", "").strip()
        if target_species not in {"Mouse", "Human"}:
            continue

        target_row = target_lookup.get(row["Target ID"], {})
        target_name_exact = row.get("Target Name", "").strip()
        ligand_value = ligand_display(row, ligand_lookup)
        target_value = target_display(target_row, target_species, target_name_exact)
        pair_species = species_by_pair[(row["Ligand ID"], row["Target ID"])]
        if target_species == "Mouse" and "Human" in pair_species:
            species_note = "mouse_target_with_human_comparator"
        elif target_species == "Mouse":
            species_note = "mouse_target_only_in_gtopdb"
        elif "Mouse" in pair_species:
            species_note = "human_target_with_mouse_comparator"
        else:
            species_note = "human_target_only_in_gtopdb"

        search_blob = normalize_text(
            " ".join(
                [
                    ligand_value,
                    row.get("Ligand Name", ""),
                    target_value,
                    target_name_exact,
                    target_row.get("Family name", ""),
                    target_row.get("Target name", ""),
                    row.get("List Comment", ""),
                ]
            )
        )
        matched_families = ";".join(family_matches(search_blob))
        detailed_row = detailed_index.get((row["Ligand ID"], row["Target ID"], target_species), {})

        out_row = {
            "source_record_id": f"GtoPdb:{row['Ligand ID']}:{row['Target ID']}:{target_species.lower()}",
            "source_database": "GuideToPharmacology",
            "source_version": SOURCE_VERSION,
            "source_date": SOURCE_DATE,
            "ligand_id": row["Ligand ID"],
            "ligand_display": ligand_value,
            "ligand_type": row.get("Ligand Type", ""),
            "ligand_species": row.get("Ligand Species", ""),
            "target_id": row["Target ID"],
            "target_display": target_value,
            "target_name_exact": target_name_exact,
            "target_species": target_species,
            "species_note": species_note,
            "target_family_name": target_row.get("Family name", ""),
            "target_type": target_row.get("Type", ""),
            "pair_label": f"{ligand_value} {target_value}",
            "matched_families": matched_families,
            "rank_potency_pmids": join_nonempty(collect_pmids(row.get("Rank Potency Refs(PMIDs)", ""))),
            "interaction_pmids": detailed_row.get("interaction_pmids", ""),
            "interaction_species_seen": detailed_row.get("interaction_species_seen", ""),
            "list_comment": row.get("List Comment", ""),
        }
        all_rows.append(out_row)
        if matched_families:
            priority_rows.append(out_row)

    output_dir = args.output_dir
    all_rows = sorted(all_rows, key=lambda row: (row["matched_families"], row["target_species"], row["pair_label"], row["source_record_id"]))
    priority_rows = sorted(priority_rows, key=lambda row: (row["matched_families"], row["target_species"], row["pair_label"], row["source_record_id"]))
    write_tsv(output_dir / "gtopdb_endogenous_module20_all.tsv", all_rows)
    write_tsv(output_dir / "gtopdb_endogenous_module20_priority.tsv", priority_rows)
    write_tsv(
        output_dir / "gtopdb_endogenous_module20_priority_mouse.tsv",
        [row for row in priority_rows if row["target_species"] == "Mouse"],
    )
    write_tsv(
        output_dir / "gtopdb_endogenous_module20_priority_human.tsv",
        [row for row in priority_rows if row["target_species"] == "Human"],
    )

    species_counts = Counter(row["target_species"] for row in priority_rows)
    family_counts = Counter()
    for row in priority_rows:
        for family in row["matched_families"].split(";"):
            if family:
                family_counts[family] += 1

    summary = {
        "source_database": "GuideToPharmacology",
        "source_version": SOURCE_VERSION,
        "source_date": SOURCE_DATE,
        "all_rows": len(all_rows),
        "priority_rows": len(priority_rows),
        "priority_species_counts": dict(sorted(species_counts.items())),
        "priority_family_counts": dict(family_counts.most_common()),
    }
    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    write_summary(
        output_dir / "summary.md",
        [
            "# GtoPdb Module 20A Priority Seed Summary",
            "",
            f"- Source database: `GuideToPharmacology`",
            f"- Version: `{SOURCE_VERSION}`",
            f"- Source date: `{SOURCE_DATE}`",
            f"- Mouse/Human endogenous rows retained in all-table export: `{len(all_rows)}`",
            f"- Priority-family rows retained: `{len(priority_rows)}`",
            "",
            "## Priority Species Counts",
            "",
            *[f"- `{key}`: `{value}`" for key, value in sorted(species_counts.items())],
            "",
            "## Priority Family Counts",
            "",
            *[f"- `{key}`: `{value}`" for key, value in family_counts.most_common()],
        ],
    )


if __name__ == "__main__":
    main()
