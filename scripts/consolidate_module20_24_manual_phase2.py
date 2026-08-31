#!/usr/bin/env python3
"""Consolidate supervised Phase-2 batch records into four audit-layer lanes.

This is deliberately conservative. Existing manual/recovery records are
retained when they reference exportable B-layer evidence. Missing evidence IDs
are represented by explicit unresolved fallback rows derived from the lane
review ledger; no observation, claim, or direct molecular relation is
fabricated. The script never writes canonical SQL tables.
"""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW_ROOT = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review"
BATCH_ROOT = ROOT / "work" / "cross_module_synthesis" / "manual_phase2_batches"
LEGACY_BATCH_ROOT = ROOT / "work" / "cross_module_synthesis"

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

MODULES = ("20B", "21B", "22B", "23B", "24B")
LANE_FILES = {
    "20B": "lane_A_20B_21B.tsv",
    "21B": "lane_A_20B_21B.tsv",
    "22B": "lane_B_22B.tsv",
    "23B": "lane_C_23B.tsv",
    "24B": "lane_D_24B.tsv",
}
OUTPUTS = {
    "20B": REVIEW_ROOT / "phase2_A_20B_observation_claim.tsv",
    "21B": REVIEW_ROOT / "phase2_B_21B_22B_observation_claim.tsv",
    "22B": REVIEW_ROOT / "phase2_B_21B_22B_observation_claim.tsv",
    "23B": REVIEW_ROOT / "phase2_C_23B_observation_claim.tsv",
    "24B": REVIEW_ROOT / "phase2_D_24B_observation_claim.tsv",
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def module_key(value: str) -> str:
    value = value.strip().upper()
    return value[1:] if value.startswith("M") else value


def register(module: str, kind: str) -> dict[str, dict[str, str]]:
    key = module.lower()
    path = ROOT / "work" / "module_b_consolidation" / f"module{key}" / f"module{key}_{kind}_register.tsv"
    rows = read_tsv(path)
    return {row[f"b_{kind}_id"]: row for row in rows}


def batch_files() -> list[Path]:
    paths = set(BATCH_ROOT.glob("*.tsv"))
    paths.update(LEGACY_BATCH_ROOT.glob("manual_batch_*.tsv"))
    return sorted(paths)


def load_manual_rows() -> tuple[list[dict[str, str]], list[str]]:
    rows: list[dict[str, str]] = []
    ignored: list[str] = []
    for path in batch_files():
        with path.open(newline="") as handle:
            reader = csv.DictReader(handle, delimiter="\t")
            if not reader.fieldnames or set(FIELDS) - set(reader.fieldnames):
                ignored.append(str(path))
                continue
            for row in reader:
                if module_key(row.get("module", "")) in MODULES:
                    row["_source_file"] = str(path)
                    rows.append(row)
    return rows, ignored


def load_lane_rows() -> dict[str, dict[str, list[dict[str, str]]]]:
    result: dict[str, dict[str, list[dict[str, str]]]] = {}
    for module, filename in LANE_FILES.items():
        grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in read_tsv(REVIEW_ROOT / filename):
            if module_key(row.get("module", "")) == module:
                grouped[row["b_evidence_id"]].append(row)
        result[module] = grouped
    return result


def fallback_row(module: str, evidence: dict[str, str], lane_row: dict[str, str] | None) -> dict[str, str]:
    evidence_id = evidence["b_evidence_id"]
    edge_id = evidence.get("b_edge_id", "")
    layer = evidence.get("evidence_layer", "")
    if module == "20B":
        paper_key = ""
        paper_status = "unresolved_manifest_source"
        source_locator = evidence.get("source_locator", "") or "work/module20_db_seed/evidence_escalation_router/module20a_lr_release_manifest.json"
        boundary = (
            "Frozen Module 20A manifest/local audit anchor only; no underlying "
            "paper-level source was attached to this Module 20B row. Search "
            "boundary: repository Module 20A source ledgers and exact-pair "
            "history; do not treat the frozen manifest as a Paper or Observation."
        )
        species = evidence.get("species", "") or "registered LR context; not an atomic paper model"
        model = evidence.get("cell_type_or_model", "") or "not verified"
        assay = "not available from frozen manifest"
        perturbation = "not available from frozen manifest"
        confidence = "uncertain"
        context = "Module 20B LR provenance remains separate from intracellular/pathway evidence. No paper-level Observation or AuthorClaim is created."
        notes = "Explicit unresolved manifest-source fallback; no directness, family substitution, pathway-to-edge, or terminal-TF inference."
    else:
        lane_row = lane_row or {}
        paper_key = lane_row.get("canonical_paper_key", "")
        paper_status = lane_row.get("paper_resolution_status", "unresolved_identifier")
        source_locator = lane_row.get("paper_anchor_locator", "") or evidence.get("source_locator", "")
        boundary = lane_row.get("search_boundary", "") or "Lane review did not retain an atomic primary-paper passage; retrieve the exact cited primary paper and Results/Methods/figure/table locus before import."
        species = lane_row.get("species", "") or "not verified"
        model = lane_row.get("cell_type_or_model", "") or "not verified"
        assay = lane_row.get("assay_or_perturbation", "") or "not verified"
        perturbation = lane_row.get("assay_or_perturbation", "") or "not verified"
        confidence = lane_row.get("confidence", "") or "uncertain"
        context = lane_row.get("context_and_limitations", "") or "No atomic Observation or separate AuthorClaim was retained in the supervised batch pass."
        notes = "Fallback generated from lane review only; not import-ready and not a promotion."
    obs_status = "unresolved_manifest_source" if module == "20B" else "unresolved"
    claim_status = "unresolved_manifest_source" if module == "20B" else "unresolved"
    return {
        "extraction_id": f"P2FALLBACK-{module}-{evidence_id}",
        "module": module,
        "b_edge_id": edge_id,
        "b_evidence_id": evidence_id,
        "evidence_layer": layer,
        "canonical_paper_key": paper_key,
        "paper_status": paper_status,
        "observation_status": obs_status,
        "observation_id_or_action": "DO_NOT_CREATE_OBSERVATION:unresolved_primary_support",
        "observation_value_or_blocker": "Unresolved: no validated atomic primary-paper observation was retained for this evidence record; do not import.",
        "observation_source_section": "not located",
        "observation_figure_or_table": "not located",
        "observation_species": species,
        "observation_cell_or_model": model,
        "observation_assay": assay,
        "observation_perturbation": perturbation,
        "claim_status": claim_status,
        "claim_id_or_action": "DO_NOT_CREATE_AUTHOR_CLAIM:unresolved_primary_support",
        "claim_text_or_blocker": "Unresolved: no separate explicit author interpretation was retained from a primary-paper section or figure legend; do not convert the B-layer summary into an AuthorClaim.",
        "claim_source_section": "not located",
        "confidence": confidence,
        "context_and_limitations": context,
        "source_locator": source_locator,
        "search_boundary": boundary,
        "reviewer_notes": notes,
    }


def main() -> None:
    registers = {module: {kind: register(module, kind) for kind in ("edge", "evidence")} for module in MODULES}
    manual_rows, ignored = load_manual_rows()
    lane_rows = load_lane_rows()

    by_extraction: dict[str, dict[str, str]] = {}
    conflicts: list[str] = []
    for row in manual_rows:
        row = {key: value for key, value in row.items() if not key.startswith("_")}
        extraction_id = row["extraction_id"]
        if extraction_id in by_extraction:
            prior = by_extraction[extraction_id]
            if any(prior[field] != row[field] for field in FIELDS):
                conflicts.append(f"conflicting extraction_id: {extraction_id}")
            continue
        by_extraction[extraction_id] = row

    rows_by_module: dict[str, list[dict[str, str]]] = defaultdict(list)
    layer_drift: list[str] = []
    for row in by_extraction.values():
        module = module_key(row["module"])
        if module in MODULES and row["b_evidence_id"] in registers[module]["evidence"]:
            if registers[module]["evidence"][row["b_evidence_id"]].get("exportable") == "true":
                row["module"] = module
                expected_layer = registers[module]["evidence"][row["b_evidence_id"]].get("evidence_layer", "")
                if row.get("evidence_layer", "") != expected_layer:
                    layer_drift.append(
                        f"{row['extraction_id']} {row['b_evidence_id']}: "
                        f"batch={row.get('evidence_layer', '')!r} register={expected_layer!r}"
                    )
                    continue
                rows_by_module[module].append(row)

    fallback_count: dict[str, int] = {}
    for module in MODULES:
        expected = {
            evidence_id
            for evidence_id, evidence in registers[module]["evidence"].items()
            if evidence.get("exportable") == "true"
        }
        observed = {row["b_evidence_id"] for row in rows_by_module[module]}
        missing = sorted(expected - observed)
        fallback_count[module] = len(missing)
        for evidence_id in missing:
            evidence = registers[module]["evidence"][evidence_id]
            candidates = lane_rows[module].get(evidence_id, [])
            lane_row = sorted(candidates, key=lambda row: row.get("review_id", ""))[0] if candidates else None
            rows_by_module[module].append(fallback_row(module, evidence, lane_row))

    output_rows: dict[Path, list[dict[str, str]]] = defaultdict(list)
    for module in MODULES:
        rows = sorted(rows_by_module[module], key=lambda row: (row["b_evidence_id"], row["extraction_id"]))
        output_rows[OUTPUTS[module]].extend(rows)

    for output, rows in output_rows.items():
        seen_composites: set[tuple[str, str, str, str]] = set()
        deduped: list[dict[str, str]] = []
        for row in sorted(rows, key=lambda row: (row["module"], row["b_evidence_id"], row["extraction_id"])):
            composite = (row["b_evidence_id"], row["canonical_paper_key"], row["observation_id_or_action"], row["claim_id_or_action"])
            if composite in seen_composites:
                continue
            seen_composites.add(composite)
            deduped.append(row)
        with output.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t")
            writer.writeheader()
            writer.writerows(deduped)
        print(f"{output.name}: rows={len(deduped)} modules={sorted({row['module'] for row in deduped})}")

    audit = REVIEW_ROOT / "module20_24_manual_phase2_consolidation_audit.md"
    lines = [
        "# Module 20B–24B manual Phase-2 consolidation audit",
        "",
        "This audit-layer consolidation retains supervised/recovery records and adds only explicit unresolved fallback rows for exportable evidence IDs not represented in those records. It does not modify canonical SQL or the frozen Module 20A LR layer.",
        "",
        f"- Manual/recovery source rows read: {len(manual_rows):,}",
        f"- Duplicate exact extraction IDs collapsed: {len(manual_rows) - len(by_extraction):,}",
        f"- Conflicting extraction IDs: {len(conflicts):,}",
        f"- Manual rows excluded for evidence-layer drift: {len(layer_drift):,}",
        f"- Batch files with non-Phase-2 schemas ignored: {len(ignored):,}",
        "",
        "| Module | Exportable evidence | Consolidated evidence | Explicit unresolved fallbacks |",
        "|---|---:|---:|---:|",
    ]
    for module in MODULES:
        expected = sum(row.get("exportable") == "true" for row in registers[module]["evidence"].values())
        output_rows_for_module = [row for row in read_tsv(OUTPUTS[module]) if module_key(row.get("module", "")) == module]
        lines.append(f"| {module} | {expected:,} | {len({row['b_evidence_id'] for row in output_rows_for_module}):,} | {fallback_count[module]:,} |")
    if conflicts:
        lines.extend(["", "## Conflicts", "", *[f"- {item}" for item in conflicts]])
    if layer_drift:
        lines.extend(["", "## Evidence-layer drift excluded from integration", "", *[f"- {item}" for item in layer_drift]])
    lines.extend([
        "",
        "Fallback rows are intentionally excluded from import-ready promotion. They carry a stable search boundary when available and require primary-paper validation before any Observation or AuthorClaim can be created.",
        "",
    ])
    audit.write_text("\n".join(lines))
    if conflicts:
        raise SystemExit("conflicting extraction IDs found")


if __name__ == "__main__":
    main()
