#!/usr/bin/env python3
"""Integrate Phase-2 Paper/Observation/AuthorClaim extraction batches."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW_ROOT = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review"
OUT_TSV = REVIEW_ROOT / "module20_24_integrated_phase2_extractions.tsv"
OUT_MD = REVIEW_ROOT / "module20_24_integrated_phase2_extractions.md"

INPUTS = {
    "phase2_A_20B_observation_claim.tsv": {"20B"},
    "phase2_B_21B_22B_observation_claim.tsv": {"21B", "22B"},
    "phase2_C_23B_observation_claim.tsv": {"23B"},
    "phase2_D_24B_observation_claim.tsv": {"24B"},
}

# Source-unit adjudication is kept as a small, explicit overlay so the large
# pre-existing Phase-2 lane remains intact. Overlay rows replace matching
# extraction IDs; they never add a second row for the same extraction.
OVERLAYS = {
    "phase2_E_21B_source_unit_overlay.tsv": {"21B"},
    "phase2_F_23B_source_unit_overlay.tsv": {"23B"},
    "phase2_G_24B_source_unit_overlay.tsv": {"24B"},
    "phase2_H_22B_even_tf_program_overlay.tsv": {"22B"},
    "phase2_I_22B_odd_tf_program_overlay.tsv": {"22B"},
    "phase2_J_20B_source_unit_overlay.tsv": {"20B"},
}

FIELDS = [
    "extraction_id", "module", "b_edge_id", "b_evidence_id", "evidence_layer",
    "canonical_paper_key", "paper_status", "observation_status",
    "observation_id_or_action", "observation_value_or_blocker",
    "observation_source_section", "observation_figure_or_table",
    "observation_species", "observation_cell_or_model", "observation_assay",
    "observation_perturbation", "claim_status", "claim_id_or_action",
    "claim_text_or_blocker", "claim_source_section", "confidence",
    "context_and_limitations", "source_locator", "search_boundary",
    "reviewer_notes",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def register(module: str, kind: str) -> dict[str, dict[str, str]]:
    module_dir = f"module{module.lower()}"
    path = ROOT / "work" / "module_b_consolidation" / module_dir / f"{module_dir}_{kind}_register.tsv"
    return {row[f"b_{kind}_id"]: row for row in read_tsv(path)}


def expected_evidence() -> dict[str, set[str]]:
    result: dict[str, set[str]] = defaultdict(set)
    for module in ("20B", "21B", "22B", "23B", "24B"):
        for row in register(module, "evidence").values():
            if row.get("exportable") == "true":
                result[module].add(row["b_evidence_id"])
    return result


def main() -> None:
    errors: list[str] = []
    rows: list[dict[str, str]] = []
    seen_extractions: set[str] = set()
    seen_composites: set[tuple[str, str, str, str]] = set()
    overlays: dict[str, dict[str, str]] = {}
    used_overlays: set[str] = set()
    edges: dict[str, dict[str, dict[str, str]]] = {}
    evidence: dict[str, dict[str, dict[str, str]]] = {}

    for filename, modules in OVERLAYS.items():
        path = REVIEW_ROOT / filename
        if not path.exists():
            errors.append(f"missing Phase-2 overlay file: {filename}")
            continue
        batch = read_tsv(path)
        if not batch:
            errors.append(f"empty Phase-2 overlay file: {filename}")
            continue
        missing = sorted(set(FIELDS) - set(batch[0]))
        if missing:
            errors.append(f"{filename} missing fields: {', '.join(missing)}")
            continue
        for row in batch:
            module = row["module"].strip().upper()
            module_key = module[1:] if module.startswith("M") else module
            if module_key not in modules:
                errors.append(f"{filename} out-of-scope module {module}")
            extraction_id = row["extraction_id"].strip()
            if not extraction_id or extraction_id in overlays:
                errors.append(f"duplicate or empty overlay extraction_id: {extraction_id!r}")
            overlays[extraction_id] = row

    for filename, modules in INPUTS.items():
        path = REVIEW_ROOT / filename
        if not path.exists():
            errors.append(f"missing Phase-2 file: {filename}")
            continue
        batch = read_tsv(path)
        if not batch:
            errors.append(f"empty Phase-2 file: {filename}")
            continue
        missing = sorted(set(FIELDS) - set(batch[0]))
        if missing:
            errors.append(f"{filename} missing fields: {', '.join(missing)}")
            continue
        for row in batch:
            base_extraction_id = row["extraction_id"].strip()
            if base_extraction_id in overlays:
                row = overlays[base_extraction_id]
                used_overlays.add(base_extraction_id)
            module = row["module"].strip().upper()
            module_key = module[1:] if module.startswith("M") else module
            if module_key not in modules:
                errors.append(f"{filename} out-of-scope module {module}")
            extraction_id = row["extraction_id"].strip()
            if not extraction_id or extraction_id in seen_extractions:
                errors.append(f"duplicate or empty extraction_id: {extraction_id!r}")
            seen_extractions.add(extraction_id)
            if module_key not in edges:
                edges[module_key] = register(module_key, "edge")
                evidence[module_key] = register(module_key, "evidence")
            evidence_id = row["b_evidence_id"].strip()
            if evidence_id not in evidence[module_key]:
                errors.append(f"{extraction_id} unknown evidence {evidence_id}")
            else:
                source = evidence[module_key][evidence_id]
                if source.get("exportable") != "true":
                    errors.append(f"{extraction_id} targets non-exportable evidence {evidence_id}")
                if source.get("evidence_layer") != row["evidence_layer"]:
                    errors.append(f"{extraction_id} evidence-layer drift for {evidence_id}")
            for edge_id in [item for item in row["b_edge_id"].split(";") if item]:
                if edge_id not in edges[module_key]:
                    errors.append(f"{extraction_id} unknown edge {edge_id}")
            composite = (
                evidence_id, row["canonical_paper_key"],
                row["observation_id_or_action"], row["claim_id_or_action"],
            )
            if composite in seen_composites:
                errors.append(f"duplicate extraction composite: {composite}")
            seen_composites.add(composite)
            rows.append(row)

    for extraction_id in sorted(set(overlays) - used_overlays):
        errors.append(f"overlay extraction_id not found in base inputs: {extraction_id}")

    if errors:
        for error in errors:
            print(f"FAIL {error}")
        raise SystemExit(1)

    with OUT_TSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    expected = expected_evidence()
    observed: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        module = row["module"].strip().upper()
        module_key = module[1:] if module.startswith("M") else module
        observed[module_key].add(row["b_evidence_id"])
    lines = [
        "# Module 20B–24B Integrated Phase-2 Extractions",
        "",
        "This is an audit-layer integration of paper/Observation/AuthorClaim",
        "extraction batches. It does not insert canonical database rows.",
        "",
        f"- Extraction rows: {len(rows):,}",
        f"- Unique extraction IDs: {len(seen_extractions):,}",
        f"- Unique extraction composites: {len(seen_composites):,}",
        "",
        "## Exportable-evidence coverage",
        "",
        "| Module | Expected exportable evidence | Covered | Uncovered |",
        "|---|---:|---:|---:|",
    ]
    for module in sorted(expected):
        missing = expected[module] - observed[module]
        lines.append(f"| {module} | {len(expected[module]):,} | {len(observed[module] & expected[module]):,} | {len(missing):,} |")
    lines.extend([
        "",
        "## Status",
        "",
        "| Paper | Observation | AuthorClaim | Rows |",
        "|---|---|---|---:|",
    ])
    status_counts = Counter((row["paper_status"], row["observation_status"], row["claim_status"]) for row in rows)
    for (paper, observation, claim), count in sorted(status_counts.items()):
        lines.append(f"| {paper} | {observation} | {claim} | {count:,} |")
    lines.extend([
        "",
        "Canonical materialization remains blocked until all import-ready rows",
        "have stable Paper plus validated atomic Observation/AuthorClaim support,",
        "and unresolved cases are explicitly approved or excluded from import.",
        "",
    ])
    OUT_MD.write_text("\n".join(lines))
    print(f"phase2_rows={len(rows)} unique_extractions={len(seen_extractions)}")


if __name__ == "__main__":
    main()
