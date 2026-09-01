#!/usr/bin/env python3
"""Assign conservative Module 20B receptor-family groupings.

This is a review layer, not a mechanism promotion. It preserves the source
edge register unchanged and assigns a broad family label only when the
registered endpoint nomenclature and the existing direct-molecular evidence
layer support that grouping. The labels describe receptor-family organization;
they do not assert an unobserved downstream cascade.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "work/module_b_consolidation/module20b/module20b_edge_register.tsv"
DEFAULT_OUTPUT_DIR = ROOT / "data/processed/module20b_pathway_family_layer_v1"

OUTPUT_FIELDS = [
    "b_edge_id",
    "source_entity",
    "target_entity",
    "relation_type",
    "confidence_tier",
    "evidence_layer",
    "edge_status",
    "exportable",
    "register_pathway_name",
    "pathway_family",
    "family_label",
    "assignment_status",
    "assignment_basis",
    "pathway_claim_boundary",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def compact(value: str) -> str:
    return re.sub(r"[^A-Z0-9]", "", value.upper())


def classify_target(target: str) -> tuple[str, str] | None:
    """Return (stable family key, human label) from explicit receptor naming."""
    token = compact(target)

    # Complexes are checked before single-subunit prefixes.
    if any(x in token for x in ("TGFBR", "BMPR", "ACVR", "AMHR")):
        return "tgfb_bmp_receptor_family", "TGF-beta/BMP receptor family"
    if any(x in token for x in ("IFNAR", "IFNGR", "IL1R", "IL6ST", "CSF2R", "IL20R", "IL22R")):
        return "cytokine_receptor_family", "Cytokine receptor family"
    if "NOTCH" in token:
        return "notch_receptor_family", "Notch receptor family"
    if any(x in token for x in ("PTCH", "CDON", "BOC", "GAS1", "SMO")):
        return "hedgehog_receptor_family", "Hedgehog receptor family"
    if any(x in token for x in ("FZD", "LRP5", "LRP6", "LGR", "RNF43", "ZNRF3", "KREMEN")):
        return "wnt_frizzled_receptor_family", "WNT/Frizzled receptor family"
    if any(x in token for x in ("TLR", "IL1RAP", "CD74")):
        return "innate_immune_receptor_family", "Innate-immune receptor family"
    if any(x in token for x in ("FGFR", "EGFR", "ERBB", "IGF1R", "INSR", "KDR", "TEK", "NTRK", "MET")):
        return "rtk_growth_factor_receptor_family", "RTK growth-factor receptor family"
    if any(x in token for x in ("CCR", "CXCR", "ACKR", "GPR", "NPY2R", "NPBWR", "NPFFR", "VIPR", "CRHR", "RXFP", "PTH1R", "PTH2R", "F2R")):
        return "gpcr_receptor_family", "GPCR receptor family"
    if any(x in token for x in ("ITGA", "ITGB", "ITGAM", "DAG1", "SDC", "CD44", "CD36", "MCAM")):
        return "ecm_integrin_adhesion_family", "ECM/integrin adhesion receptor family"
    if any(x in token for x in ("EPHA", "EPHB", "ROBO", "UNC5", "DCC", "NRP", "PLXN", "RTN4R", "ADGR", "NEO1")):
        return "axon_guidance_adhesion_family", "Axon-guidance/adhesion receptor family"
    if any(x in token for x in ("NRXN", "NLGN", "CNTN", "PTPR", "ADAM23")):
        return "synaptic_cell_adhesion_family", "Synaptic/cell-adhesion receptor family"
    if any(x in token for x in ("LRP1", "LRP2", "LRP4", "SORT1", "MERTK", "LDLR", "CD47")):
        return "scavenger_uptake_receptor_family", "Scavenger/uptake-associated receptor family"
    if any(x in token for x in ("NPTR", "NPTX", "P2RX", "P2RY")):
        return "purinergic_neuroreceptor_family", "Purinergic/neuroreceptor family"
    return None


def classify(row: dict[str, str]) -> dict[str, str]:
    direct = row.get("evidence_layer") == "ligand_receptor_or_direct_molecular"
    supported_tier = row.get("confidence_tier") in {"high", "medium"}
    family = classify_target(row.get("target_entity", "")) if direct and supported_tier else None
    if family:
        key, label = family
        status = "family_group_assigned"
        basis = "explicit target receptor-family nomenclature plus direct molecular evidence layer"
    else:
        key = "pathway_not_established"
        label = "Pathway not established"
        status = "not_established"
        if not direct:
            basis = "boundary or non-direct layer; no pathway-family assignment made"
        elif not supported_tier:
            basis = "direct molecular candidate lacks medium/high confidence tier"
        else:
            basis = "target nomenclature did not support a conservative family assignment"
    return {
        **{field: row.get(field, "") for field in OUTPUT_FIELDS[:8]},
        "register_pathway_name": row.get("pathway_name", ""),
        "pathway_family": key,
        "family_label": label,
        "assignment_status": status,
        "assignment_basis": basis,
        "pathway_claim_boundary": "Family grouping only; downstream pathway, relay, TF/program, and SCI context remain unasserted.",
    }


def main() -> int:
    args = parse_args()
    rows = read_tsv(args.input.resolve())
    stratified = [classify(row) for row in rows]
    output_dir = args.output_dir.resolve()
    write_tsv(output_dir / "module20b_pathway_family_layer.tsv", stratified)
    summary = {
        "input": str(args.input.resolve()),
        "row_count": len(stratified),
        "family_counts": dict(sorted(Counter(row["pathway_family"] for row in stratified).items())),
        "assignment_status_counts": dict(sorted(Counter(row["assignment_status"] for row in stratified).items())),
        "exportable_family_counts": dict(sorted(Counter(
            row["pathway_family"] for row in stratified if row["exportable"] == "true"
        ).items())),
        "policy": {
            "register_unchanged": True,
            "family_labels_are_not_downstream_pathway_claims": True,
            "direct_medium_or_high_required_for_family_assignment": True,
            "unassigned_rows_use_pathway_not_established": True,
        },
    }
    (output_dir / "module20b_pathway_family_layer_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
