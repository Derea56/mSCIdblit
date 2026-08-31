#!/usr/bin/env python3
"""Normalize CellChatDB.mouse into Module 20A seed tables."""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
from collections import Counter
from pathlib import Path


OUTPUT_HEADERS = [
    "source_record_id",
    "source_database",
    "source_package_version",
    "source_checked_date",
    "cellchat_row_version",
    "interaction_name",
    "interaction_name_2",
    "annotation",
    "pathway_name",
    "ligand",
    "receptor",
    "ligand_symbol",
    "receptor_symbol",
    "agonist",
    "antagonist",
    "co_a_receptor",
    "co_i_receptor",
    "ligand_location",
    "receptor_location",
    "ligand_keyword",
    "receptor_keyword",
    "evidence",
    "pair_label",
    "matched_families",
    "directness_note",
]

PRIORITY_ANNOTATIONS = (
    "Secreted Signaling",
    "ECM-Receptor",
    "Cell-Cell Contact",
    "Non-protein Signaling",
)


def parse_args() -> argparse.Namespace:
    root = Path(__file__).resolve().parents[1]
    base_dir = root / "work" / "module20_db_seed"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--cellchat-repo",
        type=Path,
        default=Path("/private/tmp/CellChat_jinworks"),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=base_dir / "cellchatdb_module20_priority_seeds",
    )
    parser.add_argument(
        "--checked-date",
        default="2026-08-04",
    )
    return parser.parse_args()


def normalize_text(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text).strip().lower()


def family_matches(text: str) -> list[str]:
    checks = [
        ("chemokine_family", ("chemokine", " ccl", " cxcl", " cx3cl", " xcl", " ccr", " cxcr", " ackr")),
        ("il_family", ("interleukin", " il-", " il ", " il1r", " il6r", " il10r", " il17r", " il20r", " il22r")),
        ("interferon_family", ("interferon", " ifn", " ifnar", "ifngr", "ifnlr")),
        ("tnf_family", ("tumor necrosis factor", " tnf", "tnfr", "fasl", "fas ligand", "rankl", "cd40")),
        (
            "tgfb_bmp_family",
            ("transforming growth factor", "tgfb", "tgf-beta", " bmp", "bone morphogenetic", "activin", "inhibin", "gdf"),
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
                "egf",
                "fgf",
                "vegf",
                "pdgf",
                "hgf",
                "ngf",
                "bdnf",
                "gdnf",
                "csf",
            ),
        ),
        ("wnt_notch_family", (" wnt", "frizzled", " notch", " jagged", " delta-like", " dll", "lrp5", "lrp6")),
        ("complement_family", ("complement", " c1q", " c3", " c3a", " c5", " c5a", "cr1", "cr2", "c3ar", "c5ar")),
        (
            "damp_purinergic_tlr_family",
            (
                "toll-like",
                " tlr",
                "purinergic",
                "p2rx",
                "p2ry",
                "adenosine receptor",
                "atp",
                "adp",
                "hmgb1",
                "rage",
                "ager",
                "s100",
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
                "ecm",
            ),
        ),
    ]
    padded = f" {text} "
    return sorted({family for family, terms in checks if any(term in padded for term in terms)})


def directness_note(row: dict[str, str]) -> str:
    annotation = row.get("annotation", "")
    has_modifiers = any(row.get(field, "").strip() for field in ("agonist", "antagonist", "co_A_receptor", "co_I_receptor"))
    receptor_symbol = row.get("receptor.symbol", "")
    receptor_complex = "," in receptor_symbol

    if annotation == "Secreted Signaling" and not has_modifiers and not receptor_complex:
        return "seed_candidate_simple"
    if annotation == "Non-protein Signaling":
        return "seed_candidate_nonprotein_or_mediator_context"
    if annotation == "ECM-Receptor":
        return "seed_candidate_ecm_or_adhesion_context"
    if annotation == "Cell-Cell Contact":
        return "seed_candidate_contact_context"
    if has_modifiers or receptor_complex:
        return "seed_candidate_complex_or_cofactor_context"
    return "seed_candidate_needs_review"


def export_cellchat_interaction(repo_dir: Path, output_path: Path) -> str:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    description_path = repo_dir / "DESCRIPTION"
    package_version = ""
    for line in description_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("Version:"):
            package_version = line.split(":", 1)[1].strip()
            break
    if not package_version:
        raise SystemExit(f"Could not find package version in {description_path}")

    rda_path = repo_dir / "data" / "CellChatDB.mouse.rda"
    if not rda_path.exists():
        raise SystemExit(f"Missing {rda_path}")

    cmd = [
        "Rscript",
        "-e",
        (
            "load(commandArgs(TRUE)[1]); "
            "utils::write.table(CellChatDB.mouse$interaction, file=commandArgs(TRUE)[2], "
            "sep='\\t', row.names=FALSE, col.names=TRUE, quote=TRUE)"
        ),
        str(rda_path),
        str(output_path),
    ]
    subprocess.run(cmd, check=True)
    return package_version


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


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
    output_dir = args.output_dir
    raw_export = output_dir / "cellchatdb_mouse_interaction_raw.tsv"
    package_version = export_cellchat_interaction(args.cellchat_repo, raw_export)
    rows = read_rows(raw_export)

    normalized_rows: list[dict[str, str]] = []
    priority_rows: list[dict[str, str]] = []

    for row in rows:
        text = normalize_text(
            " ".join(
                [
                    row.get("interaction_name", ""),
                    row.get("interaction_name_2", ""),
                    row.get("pathway_name", ""),
                    row.get("ligand", ""),
                    row.get("receptor", ""),
                    row.get("ligand.symbol", ""),
                    row.get("receptor.symbol", ""),
                    row.get("annotation", ""),
                ]
            )
        )
        matched = ";".join(family_matches(text))
        out_row = {
            "source_record_id": f"CellChat:{row.get('interaction_name', '')}",
            "source_database": "CellChatDB.mouse",
            "source_package_version": package_version,
            "source_checked_date": args.checked_date,
            "cellchat_row_version": row.get("version", ""),
            "interaction_name": row.get("interaction_name", ""),
            "interaction_name_2": row.get("interaction_name_2", ""),
            "annotation": row.get("annotation", ""),
            "pathway_name": row.get("pathway_name", ""),
            "ligand": row.get("ligand", ""),
            "receptor": row.get("receptor", ""),
            "ligand_symbol": row.get("ligand.symbol", ""),
            "receptor_symbol": row.get("receptor.symbol", ""),
            "agonist": row.get("agonist", ""),
            "antagonist": row.get("antagonist", ""),
            "co_a_receptor": row.get("co_A_receptor", ""),
            "co_i_receptor": row.get("co_I_receptor", ""),
            "ligand_location": row.get("ligand.location", ""),
            "receptor_location": row.get("receptor.location", ""),
            "ligand_keyword": row.get("ligand.keyword", ""),
            "receptor_keyword": row.get("receptor.keyword", ""),
            "evidence": row.get("evidence", ""),
            "pair_label": f"{row.get('ligand', '')} {row.get('receptor', '')}",
            "matched_families": matched,
            "directness_note": directness_note(row),
        }
        normalized_rows.append(out_row)
        if matched and row.get("annotation", "") in PRIORITY_ANNOTATIONS:
            priority_rows.append(out_row)

    normalized_rows.sort(key=lambda r: (r["annotation"], r["matched_families"], r["interaction_name"]))
    priority_rows.sort(key=lambda r: (r["annotation"], r["matched_families"], r["interaction_name"]))

    write_tsv(output_dir / "cellchatdb_mouse_module20_all.tsv", normalized_rows)
    write_tsv(output_dir / "cellchatdb_mouse_module20_priority.tsv", priority_rows)
    for annotation in PRIORITY_ANNOTATIONS:
        safe = annotation.lower().replace(" ", "_").replace("-", "_")
        write_tsv(
            output_dir / f"cellchatdb_mouse_module20_priority_{safe}.tsv",
            [row for row in priority_rows if row["annotation"] == annotation],
        )

    annotation_counts = Counter(row["annotation"] for row in priority_rows)
    family_counts = Counter()
    directness_counts = Counter(row["directness_note"] for row in priority_rows)
    version_counts = Counter(row["cellchat_row_version"] for row in priority_rows)
    for row in priority_rows:
        for family in row["matched_families"].split(";"):
            if family:
                family_counts[family] += 1

    summary = {
        "source_database": "CellChatDB.mouse",
        "source_package_version": package_version,
        "source_checked_date": args.checked_date,
        "all_rows": len(normalized_rows),
        "priority_rows": len(priority_rows),
        "priority_annotation_counts": dict(sorted(annotation_counts.items())),
        "priority_family_counts": dict(family_counts.most_common()),
        "priority_directness_counts": dict(sorted(directness_counts.items())),
        "priority_row_version_counts": dict(sorted(version_counts.items())),
    }
    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    write_summary(
        output_dir / "summary.md",
        [
            "# CellChatDB.mouse Module 20A Priority Seed Summary",
            "",
            f"- Source database: `CellChatDB.mouse`",
            f"- Source package version: `{package_version}`",
            f"- Checked date: `{args.checked_date}`",
            f"- Mouse interaction rows exported: `{len(normalized_rows)}`",
            f"- Priority-family rows retained: `{len(priority_rows)}`",
            "",
            "## Priority Annotation Counts",
            "",
            *[f"- `{key}`: `{value}`" for key, value in sorted(annotation_counts.items())],
            "",
            "## Priority Family Counts",
            "",
            *[f"- `{key}`: `{value}`" for key, value in family_counts.most_common()],
            "",
            "## Priority Directness Notes",
            "",
            *[f"- `{key}`: `{value}`" for key, value in sorted(directness_counts.items())],
            "",
            "## Priority Row Version Counts",
            "",
            *[f"- `{key}`: `{value}`" for key, value in sorted(version_counts.items())],
        ],
    )


if __name__ == "__main__":
    main()
