#!/usr/bin/env python3
"""Normalize and triage public ligand--receptor candidates.

This is an inventory-reduction step, not a biological confidence model.  It
collapses candidate rows by normalized component pair, compares them with the
current graph's direct ligand--receptor edges, and emits separate lanes for
resolved graph matches, alias-like matches requiring adjudication, and novel
literature-review candidates.

No candidate is promoted to a graph edge by this script.  Evidence provenance
remains in the candidate output for mSCIdblit; route confidence is left to
mSCS.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BUNDLE = ROOT / "data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion243"
DEFAULT_CANDIDATES = ROOT / "data/processed/public_database_comparison_v2/public_only_lr_candidates.tsv"
DEFAULT_PRIOR_AUDIT = ROOT / "data/processed/public_database_comparison_v2/primary_evidence_harvest_resolution.tsv"
DEFAULT_OUTPUT = ROOT / "data/processed/public_database_comparison_v2/candidate_triage_v1"

PAIR_SEPARATORS = re.compile(r"[|_:;,/+\s]+")
NON_ALNUM = re.compile(r"[^A-Z0-9]")
NON_ENTITY_WORDS = {"COMPLEX", "RECEPTOR", "PROTEIN", "FAMILY", "CHAIN"}
DIRECT_LR_RELATIONS = {"binds", "binds_receptor"}
PRIMARY_LOCATOR = re.compile(r"\b(?:PMID|PMCID)\s*:\s*[A-Z0-9]+|\bdoi\s*:\s*10\.\d{4,9}/\S+", re.IGNORECASE)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_token(value: str) -> str:
    return NON_ALNUM.sub("", (value or "").strip().upper())


def components(value: str) -> tuple[str, ...]:
    tokens = []
    for raw in PAIR_SEPARATORS.split(value or ""):
        token = normalize_token(raw)
        if token and token not in NON_ENTITY_WORDS and len(token) > 1:
            tokens.append(token)
    return tuple(sorted(set(tokens)))


def label_key(value: str) -> str:
    return normalize_token(value)


def component_key(value: str) -> tuple[str, ...]:
    return components(value) or ((normalize_token(value),) if normalize_token(value) else ())


def relation_is_direct_lr(row: dict[str, str]) -> bool:
    relation = (row.get("relation_type") or "").strip().lower()
    return relation in DIRECT_LR_RELATIONS


def edge_component_keys(edge: dict[str, str]) -> tuple[tuple[str, ...], tuple[str, ...]]:
    return component_key(edge.get("source_label", "")), component_key(edge.get("target_label", ""))


def subset_match(left: tuple[str, ...], right: tuple[str, ...]) -> bool:
    return bool(left and right and (set(left) <= set(right) or set(right) <= set(left)))


def classify_match(
    candidate: dict[str, str],
    exact_labels: dict[tuple[str, str], list[dict[str, str]]],
    exact_components: dict[tuple[tuple[str, ...], tuple[str, ...]], list[dict[str, str]]],
    edges_by_ligand_token: dict[str, set[int]],
    edges_by_receptor_token: dict[str, set[int]],
    edges: list[dict[str, str]],
) -> tuple[str, list[dict[str, str]]]:
    ligand = candidate.get("ligand_components", "")
    receptor = candidate.get("receptor_components", "")
    labels = (label_key(ligand), label_key(receptor))
    if labels in exact_labels:
        return "graph_match_exact_label", exact_labels[labels]

    key = (component_key(ligand), component_key(receptor))
    if key in exact_components:
        return "graph_match_exact_components", exact_components[key]

    candidate_ligand, candidate_receptor = key
    ligand_candidates = set().union(*(edges_by_ligand_token.get(token, set()) for token in candidate_ligand))
    receptor_candidates = set().union(*(edges_by_receptor_token.get(token, set()) for token in candidate_receptor))
    alias_matches = []
    for edge_index in sorted(ligand_candidates & receptor_candidates):
        edge = edges[edge_index]
        edge_ligand, edge_receptor = edge_component_keys(edge)
        if subset_match(candidate_ligand, edge_ligand) and subset_match(candidate_receptor, edge_receptor):
            alias_matches.append(edge)
    if alias_matches:
        return "graph_match_alias_adjudication", alias_matches
    return "novel_candidate", []


def source_count(row: dict[str, str]) -> int:
    raw = row.get("independent_public_source_count", "")
    try:
        return int(raw)
    except ValueError:
        return len([x for x in row.get("source_databases", "").split(";") if x])


def locator_count(row: dict[str, str]) -> int:
    try:
        value = row.get("primary_locator_count", "")
        if value:
            return int(value)
    except ValueError:
        pass
    text = " ".join(row.get(field, "") for field in ("evidence_notes", "annotations", "source_record_ids"))
    return len(PRIMARY_LOCATOR.findall(text))


def priority(row: dict[str, str], match_class: str) -> int:
    """Rank review effort; this is not a confidence score."""

    try:
        public_score = int(row.get("review_priority_score", "0"))
    except ValueError:
        public_score = 0
    return public_score + source_count(row) * 10 + min(locator_count(row), 5) * 5 + (
        20 if match_class == "graph_match_alias_adjudication" else 0
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument("--candidates", type=Path, default=DEFAULT_CANDIDATES)
    parser.add_argument("--prior-audit", type=Path, default=DEFAULT_PRIOR_AUDIT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--batch-size", type=int, default=100)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.batch_size < 1:
        raise SystemExit("--batch-size must be positive")

    candidate_rows = read_tsv(args.candidates)
    prior_audit_rows = read_tsv(args.prior_audit) if args.prior_audit.exists() else []
    prior_audit = {
        (row.get("ligand", "").strip().upper(), row.get("receptor", "").strip().upper()): row
        for row in prior_audit_rows
        if row.get("ligand") and row.get("receptor")
    }
    graph_edges = [row for row in read_tsv(args.bundle_dir / "mechanism_edges.tsv") if relation_is_direct_lr(row)]

    exact_labels: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    exact_components: dict[tuple[tuple[str, ...], tuple[str, ...]], list[dict[str, str]]] = defaultdict(list)
    edges_by_ligand_token: dict[str, set[int]] = defaultdict(set)
    edges_by_receptor_token: dict[str, set[int]] = defaultdict(set)
    for edge_index, edge in enumerate(graph_edges):
        exact_labels[(label_key(edge.get("source_label", "")), label_key(edge.get("target_label", "")))].append(edge)
        exact_components[edge_component_keys(edge)].append(edge)
        ligand_key, receptor_key = edge_component_keys(edge)
        for token in ligand_key:
            edges_by_ligand_token[token].add(edge_index)
        for token in receptor_key:
            edges_by_receptor_token[token].add(edge_index)

    # The comparison output is already source-collapsed, but this grouping is
    # retained so the report remains correct if future snapshots reintroduce
    # one row per public source.
    grouped: dict[tuple[tuple[str, ...], tuple[str, ...]], dict[str, str]] = {}
    source_fields = ("source_databases", "source_record_ids", "pathways", "annotations", "evidence_notes")
    for row in candidate_rows:
        key = (component_key(row.get("ligand_components", "")), component_key(row.get("receptor_components", "")))
        if not key[0] or not key[1]:
            continue
        current = grouped.get(key)
        if current is None:
            grouped[key] = dict(row)
            continue
        for field in source_fields:
            values = {value for value in current.get(field, "").split(";") if value}
            values.update(value for value in row.get(field, "").split(";") if value)
            current[field] = ";".join(sorted(values))
        current["primary_locator_count"] = str(max(locator_count(current), locator_count(row)))
        current["independent_public_source_count"] = str(max(source_count(current), source_count(row)))
        current["review_priority_score"] = str(max(int(current.get("review_priority_score", "0") or 0), int(row.get("review_priority_score", "0") or 0)))

    all_rows: list[dict[str, str]] = []
    for key, row in grouped.items():
        match_class, matches = classify_match(
            row,
            exact_labels,
            exact_components,
            edges_by_ligand_token,
            edges_by_receptor_token,
            graph_edges,
        )
        if match_class.startswith("graph_match_exact"):
            review_lane = "resolved_graph_match"
        elif match_class == "graph_match_alias_adjudication":
            review_lane = "alias_adjudication"
        else:
            review_lane = "primary_evidence_review" if locator_count(row) else "discovery_review"
        match_ids = sorted({edge.get("edge_id", "") for edge in matches if edge.get("edge_id")})
        match_labels = sorted({f"{edge.get('source_label', '')}>{edge.get('target_label', '')}" for edge in matches})
        row_out = dict(row)
        row_out.update(
            {
                "normalized_ligand_key": "+".join(key[0]),
                "normalized_receptor_key": "+".join(key[1]),
                "normalization_match": match_class,
                "review_lane": review_lane,
                "matched_graph_edge_ids": ";".join(match_ids),
                "matched_graph_edges": ";".join(match_labels),
                "review_priority_rank_value": str(priority(row, match_class)),
                "candidate_unit_id": f"LR:{'+'.join(key[0])}>{'+'.join(key[1])}",
                "independent_public_source_count": str(source_count(row)),
                "primary_locator_count": str(locator_count(row)),
                "prior_harvest_disposition": "",
                "prior_harvest_primary_locators": "",
            }
        )
        prior = prior_audit.get(
            (row.get("ligand_components", "").strip().upper(), row.get("receptor_components", "").strip().upper())
        )
        if prior:
            row_out["prior_harvest_disposition"] = prior.get("disposition", "")
            row_out["prior_harvest_primary_locators"] = prior.get("primary_locators", "")
            row_out["review_lane"] = "completed_prior_harvest"
        elif (
            match_class == "graph_match_alias_adjudication"
            and len(key[0]) == 1
            and len(key[1]) == 1
            and len(matches) == 1
        ):
            # A single public component on each side maps to one direct graph
            # edge. This resolves representation only; it does not infer new
            # biological evidence or promote an edge.
            row_out["review_lane"] = "represented_graph_alias"
        all_rows.append(row_out)

    all_rows.sort(key=lambda row: (-int(row["review_priority_rank_value"]), row["candidate_unit_id"]))
    review_rows = [
        row
        for row in all_rows
        if row["review_lane"] not in {
            "resolved_graph_match",
            "completed_prior_harvest",
            "represented_graph_alias",
        }
    ]
    for index, row in enumerate(review_rows):
        row["review_batch"] = f"batch_{index // args.batch_size + 1:03d}"
    for row in all_rows:
        row.setdefault("review_batch", "")

    fields = [
        "candidate_unit_id", "source_databases", "ligand_components", "receptor_components",
        "source_ligand", "source_receptor", "source_record_ids", "pathways", "annotations",
        "evidence_notes", "primary_evidence_gate", "independent_public_source_count",
        "independent_public_sources", "primary_locator_count", "review_priority_score",
        "normalized_ligand_key", "normalized_receptor_key", "normalization_match", "review_lane",
        "matched_graph_edge_ids", "matched_graph_edges", "review_priority_rank_value", "review_batch",
        "prior_harvest_disposition", "prior_harvest_primary_locators", "review_status", "reason",
    ]
    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_tsv(args.output_dir / "candidate_normalization.tsv", all_rows, fields)
    write_tsv(args.output_dir / "candidate_review_queue.tsv", review_rows, fields)

    match_counts = Counter(row["normalization_match"] for row in all_rows)
    lane_counts = Counter(row["review_lane"] for row in all_rows)
    review_batch_counts = Counter(row["review_batch"] for row in review_rows)
    summary = {
        "triage_id": "mSCIdblit:public-lr-candidate-triage-v1",
        "bundle_dir": str(args.bundle_dir),
        "bundle_release_id": json.loads((args.bundle_dir / "bundle_metadata.json").read_text(encoding="utf-8")).get("release_id"),
        "candidate_input": {"path": str(args.candidates), "sha256": sha256(args.candidates), "raw_rows": len(candidate_rows)},
        "prior_audit_input": {
            "path": str(args.prior_audit),
            "sha256": sha256(args.prior_audit) if args.prior_audit.exists() else "",
            "rows": len(prior_audit_rows),
        },
        "graph_input": {"path": str(args.bundle_dir / "mechanism_edges.tsv"), "sha256": sha256(args.bundle_dir / "mechanism_edges.tsv"), "direct_lr_edges": len(graph_edges)},
        "candidate_units": len(all_rows),
        "normalization_match_counts": dict(sorted(match_counts.items())),
        "review_lane_counts": dict(sorted(lane_counts.items())),
        "prior_harvest_rows": len(prior_audit_rows),
        "prior_harvest_matched_units": sum(row["review_lane"] == "completed_prior_harvest" for row in all_rows),
        "review_queue_rows": len(review_rows),
        "review_queue_with_primary_locators": sum(locator_count(row) > 0 for row in review_rows),
        "review_queue_without_primary_locators": sum(locator_count(row) == 0 for row in review_rows),
        "review_batch_size": args.batch_size,
        "review_batch_counts": dict(sorted(review_batch_counts.items())),
        "policy": "This triage does not promote edges or assign biological confidence; primary evidence and route plausibility remain separate downstream decisions.",
    }
    (args.output_dir / "candidate_triage_summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    report = [
        "# Public ligand--receptor candidate triage v1",
        "",
        f"This report reduces `{len(candidate_rows):,}` public-only rows to `{len(all_rows):,}` normalized candidate units against `{len(graph_edges):,}` direct ligand--receptor graph edges from `{summary['bundle_release_id']}`.",
        "",
        "## Results",
        "",
        "| Triage lane | Candidate units | Meaning |",
        "|---|---:|---|",
        f"| Resolved graph match | {lane_counts.get('resolved_graph_match', 0):,} | Exact label or exact component match; no new edge is implied. |",
        f"| Completed prior harvest | {lane_counts.get('completed_prior_harvest', 0):,} | Present in the existing primary-evidence harvest ledger; excluded from new review batches. |",
        f"| Represented graph alias | {lane_counts.get('represented_graph_alias', 0):,} | Conservative one-component/one-edge representation match; no new evidence or edge is inferred. |",
        f"| Alias adjudication | {lane_counts.get('alias_adjudication', 0):,} | Component overlap suggests an alias or composite representation; curator confirmation is required. |",
        f"| Primary-evidence review | {lane_counts.get('primary_evidence_review', 0):,} | No automatic graph match and a public primary-paper locator is present. |",
        f"| Discovery review | {lane_counts.get('discovery_review', 0):,} | No automatic graph match and no primary locator in the frozen public snapshot. |",
        "",
        f"The actionable review queue contains `{len(review_rows):,}` units, of which `{summary['review_queue_with_primary_locators']:,}` have a primary locator and `{summary['review_queue_without_primary_locators']:,}` require discovery or broader evidence search.",
        "",
        "## Review batches",
        "",
        f"Novel and alias-adjudication units are ranked using the existing public-source/locator priority fields and divided into batches of `{args.batch_size}`. This rank is an effort-ordering value, not a confidence score.",
        "",
        "## Reproduction",
        "",
        "```bash",
        "python3 scripts/triage_public_lr_candidates_v1.py",
        "```",
        "",
        "Outputs: `candidate_normalization.tsv` contains every normalized unit; `candidate_review_queue.tsv` excludes automatic graph matches; `candidate_triage_summary.json` contains input hashes and counts.",
        "",
    ]
    (args.output_dir / "PUBLIC_LR_CANDIDATE_TRIAGE_V1.md").write_text("\n".join(report), encoding="utf-8")

    print(
        f"raw_rows={len(candidate_rows)} candidate_units={len(all_rows)} "
        f"resolved={lane_counts.get('resolved_graph_match', 0)} "
        f"alias_adjudication={lane_counts.get('alias_adjudication', 0)} "
        f"primary_review={lane_counts.get('primary_evidence_review', 0)} "
        f"discovery_review={lane_counts.get('discovery_review', 0)} "
        f"review_queue={len(review_rows)}"
    )


if __name__ == "__main__":
    main()
