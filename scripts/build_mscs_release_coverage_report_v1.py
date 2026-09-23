#!/usr/bin/env python3
"""Build route-coverage and intracellular/TF gap reports for an mSCS release."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BUNDLE = ROOT / "data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion262"
DEFAULT_LEDGER = ROOT / "data/processed/public_database_comparison_v2/candidate_triage_v1/review_resolution_ledger.tsv"


def read_tsv(path: Path) -> list[dict[str, str]]:
    if path.suffix == ".gz":
        handle = gzip.open(path, "rt", newline="", encoding="utf-8", errors="replace")
    else:
        handle = path.open(newline="", encoding="utf-8", errors="replace")
    with handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def route_path(bundle: Path) -> Path:
    path = bundle / "mechanism_signaling_route_evidence.tsv"
    return path if path.exists() else path.with_suffix(path.suffix + ".gz")


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: str(row.get(field, "")) for field in fields} for row in rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    return parser.parse_args()


def tokens(value: str) -> set[str]:
    return {token.strip() for token in value.split("|") if token.strip()}


def route_class(row: dict[str, str]) -> str:
    layers = tokens(row.get("known_layers", ""))
    has_lr = (
        "ligand_receptor_pair" in layers
        or {"ligand", "receptor"}.issubset(layers)
    )
    has_i = "intracellular_continuation" in layers
    has_tf = "transcription_factor" in layers
    has_output = bool(
        {
            "target_gene_expression_or_output",
            "target_gene_expression",
            "target_gene",
            "output",
        }
        & layers
    ) or bool(row.get("output_label") or row.get("target_gene_label"))
    if has_lr and has_i and has_tf and has_output:
        return "L_R_intracellular_TF_output"
    if has_lr and has_tf and has_output:
        return "L_R_TF_output"
    if has_lr and has_i and has_output:
        return "L_R_intracellular_output"
    if has_lr and has_output:
        return "L_R_output"
    if has_lr:
        return "L_R_entry_only"
    return "other"


def missing_layers(row: dict[str, str]) -> set[str]:
    return {token.strip() for token in row.get("missing_layers", "").split("|") if token.strip()}


def build_gap_rows(routes: list[dict[str, str]]) -> list[dict[str, object]]:
    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in routes:
        ligand = row.get("ligand_label", "").strip()
        receptor = row.get("receptor_label", "").strip()
        if ligand and receptor and missing_layers(row) & {"intracellular_continuation", "transcription_factor"}:
            grouped[(ligand, receptor)].append(row)

    output: list[dict[str, object]] = []
    for (ligand, receptor), rows in grouped.items():
        missing = Counter(layer for row in rows for layer in missing_layers(row))
        evidence_ids = {item for row in rows for item in row.get("evidence_ids", "").split(";") if item}
        route_tiers = Counter(row.get("route_tier", "") for row in rows)
        output_rows = sum(bool(row.get("output_label") or row.get("target_gene_label")) for row in rows)
        tf_rows = sum(bool(row.get("transcription_factor_label")) for row in rows)
        intracellular_rows = sum(bool(row.get("intracellular_continuation_label")) for row in rows)
        # This is a curation-workflow priority heuristic, not a biological
        # confidence score. It favors repeated source-backed gaps with an
        # existing output, TF, or intracellular annotation to anchor review.
        score = len(rows) * 10 + len(evidence_ids) * 2 + output_rows * 4 + tf_rows * 3 + intracellular_rows * 2
        output.append({
            "review_priority_rank": 0,
            "review_priority_score": score,
            "ligand_label": ligand,
            "receptor_label": receptor,
            "route_record_count": len(rows),
            "unique_evidence_id_count": len(evidence_ids),
            "output_annotated_route_count": output_rows,
            "tf_annotated_route_count": tf_rows,
            "intracellular_annotated_route_count": intracellular_rows,
            "missing_intracellular_count": missing["intracellular_continuation"],
            "missing_tf_count": missing["transcription_factor"],
            "route_tiers": ";".join(f"{key}:{value}" for key, value in sorted(route_tiers.items())),
            "selection_note": "Workflow prioritization only; mSCS determines route plausibility and confidence.",
        })
    output.sort(key=lambda row: (-int(row["review_priority_score"]), str(row["ligand_label"]), str(row["receptor_label"])))
    for index, row in enumerate(output, start=1):
        row["review_priority_rank"] = index
    return output


def main() -> int:
    args = parse_args()
    bundle = args.bundle_dir.resolve()
    ledger = args.ledger.resolve()
    metadata = json.loads((bundle / "bundle_metadata.json").read_text(encoding="utf-8"))
    route_file = route_path(bundle)
    routes = read_tsv(route_file)
    ledger_rows = read_tsv(ledger)
    edges = read_tsv(bundle / "mechanism_edges.tsv")
    sources = read_tsv(bundle / "mechanism_edge_sources.tsv")
    chains_path = bundle / "full_signaling_chain_audit.json"
    chains = json.loads(chains_path.read_text(encoding="utf-8")) if chains_path.exists() else {}
    route_classes = Counter(route_class(row) for row in routes)
    route_tiers = Counter(row.get("route_tier", "") for row in routes)
    gap_rows = build_gap_rows(routes)
    gap_fields = [
        "review_priority_rank", "review_priority_score", "ligand_label", "receptor_label",
        "route_record_count", "unique_evidence_id_count", "output_annotated_route_count",
        "tf_annotated_route_count", "intracellular_annotated_route_count",
        "missing_intracellular_count", "missing_tf_count", "route_tiers", "selection_note",
    ]
    write_tsv(bundle / "mechanism_route_gap_priorities.tsv", gap_fields, gap_rows)

    candidate_dispositions = Counter(row.get("disposition", "") for row in ledger_rows)
    candidate_primary = sum(bool(row.get("supporting_primary_locators")) for row in ledger_rows)
    candidate_matched_primary = sum(
        bool(row.get("supporting_primary_locators")) and bool(row.get("matched_graph_edge_ids"))
        for row in ledger_rows
    )
    categories = {
        "L_R_output": route_classes["L_R_output"],
        "L_R_TF_output": route_classes["L_R_TF_output"],
        "L_R_intracellular_output": route_classes["L_R_intracellular_output"],
        "L_R_intracellular_TF_output": route_classes["L_R_intracellular_TF_output"],
        "L_R_entry_only": route_classes["L_R_entry_only"],
    }
    report = {
        "release_id": metadata.get("release_id", "unknown"),
        "bundle_dir": str(bundle),
        "graph_counts": metadata.get("counts", {}),
        "route_evidence": {
            "record_count": len(routes),
            "tier_counts": dict(sorted(route_tiers.items())),
            "category_counts": categories,
            "unique_ligands": len({row["ligand_label"] for row in routes if row.get("ligand_label")}),
            "unique_receptors": len({row["receptor_label"] for row in routes if row.get("receptor_label")}),
            "unique_transcription_factors": len({row["transcription_factor_label"] for row in routes if row.get("transcription_factor_label")}),
            "unique_outputs": len({row.get("output_label") or row.get("target_gene_label") for row in routes if row.get("output_label") or row.get("target_gene_label")}),
        },
        "full_chain_audit": chains.get("full_chain_counts", {}),
        "candidate_audit": {
            "candidate_units": len(ledger_rows),
            "disposition_counts": dict(sorted(candidate_dispositions.items())),
            "rows_with_primary_locators": candidate_primary,
            "rows_with_primary_locators_and_current_graph_match": candidate_matched_primary,
        },
        "primary_evidence_integration": json.loads(
            (bundle / "public_lr_evidence_integration_summary.json").read_text(encoding="utf-8")
        ) if (bundle / "public_lr_evidence_integration_summary.json").exists() else {},
        "gap_prioritization": {
            "prioritized_pair_count": len(gap_rows),
            "top_pairs_emitted": min(100, len(gap_rows)),
            "priority_is_not_biological_confidence": True,
            "priority_table": "mechanism_route_gap_priorities.tsv",
        },
        "integrity_inputs": {
            "edge_count_observed": len(edges),
            "edge_source_count_observed": len(sources),
            "route_evidence_sha256": sha256(route_file),
        },
    }
    (bundle / "release_coverage_report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    lines = [
        f"# mSCS release coverage report",
        "",
        f"Release: `{report['release_id']}`",
        "",
        "This report separates route-evidence coverage from biological confidence. The route layer is evidence-only and non-causal; mSCS applies route plausibility and confidence logic.",
        "",
        "## Route categories",
        "",
        "| Category | Records |",
        "|---|---:|",
    ]
    for key, value in categories.items():
        lines.append(f"| {key.replace('_', '→')} | {value:,} |")
    lines.extend([
        "",
        "## Audit and public-LR coverage",
        "",
        f"- Route-evidence records: {len(routes):,}",
        f"- Graph edges: {len(edges):,}",
        f"- Graph evidence-source rows: {len(sources):,}",
        f"- Public-LR candidates covered: {len(ledger_rows):,}",
        f"- Public-LR rows with primary locators and graph matches: {candidate_matched_primary:,}",
        f"- Intracellular/TF gap pairs prioritized: {len(gap_rows):,}",
        "",
        "The prioritized gap table is a workflow queue for evidence harvesting. It does not assign biological confidence or promote causal edges.",
    ])
    (bundle / "release_coverage_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"release_id": report["release_id"], "route_categories": categories, "gap_pairs": len(gap_rows)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
