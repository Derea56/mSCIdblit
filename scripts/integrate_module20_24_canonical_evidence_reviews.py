#!/usr/bin/env python3
"""Integrate disjoint Module 20B–24B provenance-review lane outputs.

The script is deliberately an audit-layer gate. It validates references and
evidence-layer preservation, then writes an integrated review ledger and
summary. It does not insert canonical Paper, Observation, AuthorClaim,
SignalingEdge, or SignalingEdgeSource rows.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW_ROOT = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review"
OUT_TSV = REVIEW_ROOT / "module20_24_integrated_canonical_evidence_review.tsv"
OUT_MD = REVIEW_ROOT / "module20_24_integrated_canonical_evidence_review.md"

LANES = {
    "lane_A_20B_21B": {"20B", "21B"},
    "lane_B_22B": {"22B"},
    "lane_C_23B": {"23B"},
    "lane_D_24B": {"24B"},
}

FIELDS = [
    "review_id", "module", "b_edge_id", "b_evidence_id", "evidence_layer",
    "support_kind", "canonical_paper_key", "paper_anchor_type",
    "paper_anchor_locator", "paper_resolution_status", "observation_status",
    "observation_key_or_action", "claim_status", "claim_key_or_action",
    "species", "cell_type_or_model", "assay_or_perturbation", "relation_type",
    "pathway_or_branch", "confidence", "source_scope",
    "context_and_limitations", "search_boundary", "reviewer_notes",
]
ALLOWED_LAYERS = {
    "boundary",
    "ligand_receptor_binding_or_activation",
    "ligand_receptor_or_direct_molecular",
    "receptor_proximal_or_pathway",
    "mixed_receptor_proximal_and_downstream",
    "downstream_or_functional",
    "contextual_or_unresolved",
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def register_rows(module: str, kind: str) -> dict[str, dict[str, str]]:
    module_key = module[1:] if module.startswith("M") else module
    module_dir = f"module{module_key.lower()}"
    path = ROOT / "work" / "module_b_consolidation" / module_dir / f"{module_dir}_{kind}_register.tsv"
    return {row[f"b_{kind}_id"]: row for row in read_tsv(path)}


def main() -> None:
    errors: list[str] = []
    rows: list[dict[str, str]] = []
    duplicate_rows = 0
    seen_review_ids: set[str] = set()
    seen_composites: set[tuple[str, str, str, str]] = set()
    edge_cache: dict[str, dict[str, dict[str, str]]] = {}
    evidence_cache: dict[str, dict[str, dict[str, str]]] = {}

    for lane, modules in LANES.items():
        path = REVIEW_ROOT / f"{lane}.tsv"
        if not path.exists():
            errors.append(f"missing lane output: {path.name}")
            continue
        lane_rows = read_tsv(path)
        if not lane_rows:
            errors.append(f"empty lane output: {path.name}")
            continue
        missing = sorted(set(FIELDS) - set(lane_rows[0]))
        if missing:
            errors.append(f"{path.name} missing fields: {', '.join(missing)}")
            continue
        for row in lane_rows:
            module = row["module"].strip().upper()
            module_key = module[1:] if module.startswith("M") else module
            if module_key not in modules:
                errors.append(f"{path.name} has out-of-scope module {module}")
            review_id = row["review_id"].strip()
            if not review_id or review_id in seen_review_ids:
                errors.append(f"duplicate or empty review_id: {review_id!r}")
            seen_review_ids.add(review_id)
            if row["evidence_layer"] not in ALLOWED_LAYERS:
                errors.append(f"{review_id} invalid evidence layer {row['evidence_layer']!r}")
            if not row["canonical_paper_key"] and row["paper_resolution_status"] == "paper_ready":
                errors.append(f"{review_id} is paper_ready without canonical_paper_key")
            composite = (
                row["b_evidence_id"], row["canonical_paper_key"],
                row["observation_key_or_action"], row["claim_key_or_action"],
            )
            if composite in seen_composites:
                prior = next(item for item in rows if (
                    item["b_evidence_id"], item["canonical_paper_key"],
                    item["observation_key_or_action"], item["claim_key_or_action"],
                ) == composite)
                comparable_fields = [field for field in FIELDS if field not in {"review_id", "reviewer_notes"}]
                if any(prior[field] != row[field] for field in comparable_fields):
                    errors.append(f"conflicting duplicate provenance composite: {composite}")
                else:
                    duplicate_rows += 1
                    if row["reviewer_notes"] and row["reviewer_notes"] not in prior["reviewer_notes"]:
                        prior["reviewer_notes"] += " | duplicate-lane note: " + row["reviewer_notes"]
                    continue
            seen_composites.add(composite)
            if module_key not in edge_cache:
                edge_cache[module_key] = register_rows(module, "edge")
                evidence_cache[module_key] = register_rows(module, "evidence")
            edge_ids = set(row["b_edge_id"].split(";") if row["b_edge_id"] else [])
            evidence_ids = set(row["b_evidence_id"].split(";") if row["b_evidence_id"] else [])
            for edge_id in edge_ids:
                if edge_id not in edge_cache[module_key]:
                    errors.append(f"{review_id} unknown edge {edge_id}")
            for evidence_id in evidence_ids:
                if evidence_id not in evidence_cache[module_key]:
                    errors.append(f"{review_id} unknown evidence {evidence_id}")
                elif evidence_cache[module_key][evidence_id].get("evidence_layer") != row["evidence_layer"]:
                    errors.append(f"{review_id} evidence-layer drift for {evidence_id}")
            rows.append(row)

    if errors:
        for error in errors:
            print(f"FAIL {error}")
        raise SystemExit(1)

    with OUT_TSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    paper_status = Counter(row["paper_resolution_status"] for row in rows)
    observation_status = Counter(row["observation_status"] for row in rows)
    claim_status = Counter(row["claim_status"] for row in rows)
    lines = [
        "# Module 20B–24B Integrated Canonical-Evidence Review",
        "",
        "Audit-layer integration of the four disjoint provenance-review lanes.",
        "No canonical Paper, Observation, AuthorClaim, SignalingEdge, or",
        "SignalingEdgeSource rows are inserted by this report.",
        "",
        f"- Review rows: {len(rows):,}",
        f"- Unique review IDs after deduplication: {len({row['review_id'] for row in rows}):,}",
        f"- Unique provenance composites: {len(seen_composites):,}",
        f"- Exact duplicate lane rows collapsed: {duplicate_rows:,}",
        "",
        "## Paper resolution status",
        "",
        "| Status | Rows |",
        "|---|---:|",
    ]
    lines.extend(f"| {key} | {value:,} |" for key, value in sorted(paper_status.items()))
    lines.extend(["", "## Observation status", "", "| Status | Rows |", "|---|---:|"])
    lines.extend(f"| {key} | {value:,} |" for key, value in sorted(observation_status.items()))
    lines.extend(["", "## Author-claim status", "", "| Status | Rows |", "|---|---:|"])
    lines.extend(f"| {key} | {value:,} |" for key, value in sorted(claim_status.items()))
    lines.extend([
        "",
        "## Materialization boundary",
        "",
        "This ledger is ready for schema review only. Canonical insertion remains",
        "blocked until all import-ready source rows have a stable Paper plus an",
        "existing or explicitly approved Observation/AuthorClaim route, and the",
        "isolated SQL and referential-integrity gates pass.",
        "",
    ])
    OUT_MD.write_text("\n".join(lines))
    print(f"integrated_rows={len(rows)} unique_review_ids={len({row['review_id'] for row in rows})}")


if __name__ == "__main__":
    main()
