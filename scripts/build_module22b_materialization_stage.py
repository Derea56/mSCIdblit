#!/usr/bin/env python3
"""Build the deterministic, evidence-backed Module 22B write set.

The repository contains several public-TF review lanes produced at different
stages.  This script combines only rows explicitly promoted to 22B, removes
overlapping pair rows, preserves source provenance, and writes one canonical
materialization input.  It does not touch PostgreSQL.

The resulting canonical confidence is intentionally ``medium``: these are
pair-level primary-literature promotions, but some lanes are abstract-level
or context-limited and should not be represented as universal direct-binding
claims.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "work/module22b_consolidation/materialization_round_2026_08_26"

INPUTS = (
    (
        "new_tf_evidence_all_remaining",
        ROOT / "data/processed/public_tf_union_v1/module_curation/new_tf_evidence_materialized/all_remaining/priority_tf_agent_promoted.tsv",
        "agent",
    ),
    (
        "priority_tf_agent",
        ROOT / "data/processed/public_tf_union_v1/module_curation/agent_materialized/priority_tf_agent_promoted.tsv",
        "agent",
    ),
    (
        "new_tf_agent",
        ROOT / "data/processed/public_tf_union_v1/module_curation/new_tf_materialized/priority_tf_agent_promoted.tsv",
        "agent",
    ),
    (
        "new_tf_batch_agent",
        ROOT / "data/processed/public_tf_union_v1/module_curation/new_tf_batch_materialized/round_001/priority_tf_agent_promoted.tsv",
        "agent",
    ),
    (
        "priority_batch001",
        ROOT / "data/processed/public_tf_union_v1/module_curation/batch001/priority_curation_batch001_promoted_22B.tsv",
        "batch",
    ),
)

OUTPUT_FIELDS = [
    "materialization_id",
    "module",
    "species",
    "tf_symbol",
    "target_symbol",
    "relation_type",
    "effect_polarity",
    "canonical_confidence_tier",
    "membership_basis",
    "membership_status",
    "export_priority",
    "evidence_status",
    "support_kind",
    "primary_pmids",
    "corroborating_pmids",
    "external_record_keys",
    "source_registries",
    "tf_entity_ids",
    "target_entity_ids",
    "tf_frozen_match_status",
    "target_frozen_match_status",
    "tf_role_present",
    "target_role_present",
    "cell_type_context",
    "stimulus_context",
    "limitations",
    "notes",
    "source_artifacts",
]

PMID_RE = re.compile(r"(?<!\d)(?:PMID\s*[:]?\s*)?(\d{7,9})(?!\d)", re.I)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def values(value: str | None) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for match in PMID_RE.finditer(value or ""):
        token = match.group(1)
        if token not in seen:
            seen.add(token)
            result.append(token)
    if result:
        return result
    for token in re.split(r"[;,]", value or ""):
        token = token.strip()
        if token and token not in {"\\N", "NA", "null"} and token not in seen:
            seen.add(token)
            result.append(token)
    return result


def join_unique(items: list[str]) -> str:
    result: list[str] = []
    seen: set[str] = set()
    for item in items:
        for token in re.split(r"[;,]", item or ""):
            token = token.strip()
            if not token or token in {"\\N", "NA", "null"} or token in seen:
                continue
            seen.add(token)
            result.append(token)
    return ";".join(result)


def normalize_effect(*raw_values: str) -> str:
    text = ";".join(raw_values).casefold()
    activating = any(token in text for token in ("activating_target", "positive", "induc", "activat"))
    repressing = any(token in text for token in ("repressing_target", "negative", "repress", "inhib"))
    contextual = "context_dependent" in text or "context dependent" in text
    if contextual or (activating and repressing):
        return "context_dependent"
    if activating:
        return "activating_target"
    if repressing:
        return "repressing_target"
    return "unknown"


def normalized_row(row: dict[str, str], artifact: str, kind: str) -> dict[str, str]:
    is_batch = kind == "batch"
    species = (row.get("species") or "").strip().casefold()
    tf = (row.get("tf_symbol") or "").strip()
    target = (row.get("target_symbol") or "").strip()
    primary = row.get("source_pmids", "") if is_batch else row.get("primary_pmids", "")
    corroborating = row.get("corroborating_pmids", "")
    effect = normalize_effect(row.get("effect_polarity", ""), row.get("public_effect_polarities", ""))
    evidence_status = row.get("evidence_status", "") or (
        "primary_reference_verified" if row.get("public_verification_statuses") == "primary_reference_verified" else "staged_pair_review"
    )
    notes = row.get("notes", "") or row.get("curation_note", "")
    if kind == "batch":
        notes = join_unique([notes, f"Original batch confidence tier: {row.get('confidence_tier', '') or 'unspecified'}."])
    return {
        "module": "22B",
        "species": species,
        "tf_symbol": tf,
        "target_symbol": target,
        "effect_polarity": effect,
        "evidence_status": evidence_status,
        "support_kind": "primary_experiment_plus_independent_corroboration" if values(corroborating) else "primary_experiment",
        "primary_pmids": join_unique([*values(primary)]),
        "corroborating_pmids": join_unique([*values(corroborating)]),
        "external_record_keys": join_unique([row.get("external_record_keys", "")]),
        "source_registries": join_unique([row.get("source_registries", "")]),
        "tf_entity_ids": join_unique([row.get("tf_entity_ids", "")]),
        "target_entity_ids": join_unique([row.get("target_entity_ids", "")]),
        "tf_frozen_match_status": row.get("tf_frozen_match_status", ""),
        "target_frozen_match_status": row.get("target_frozen_match_status", ""),
        "tf_role_present": row.get("tf_role_present", ""),
        "target_role_present": row.get("target_role_present", ""),
        "cell_type_context": row.get("cell_type_context", ""),
        "stimulus_context": row.get("stimulus_context", ""),
        "limitations": row.get("limitations", ""),
        "notes": notes,
        "source_artifacts": artifact,
    }


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    args = parse_args()
    by_key: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    source_counts: Counter[str] = Counter()
    input_counts: dict[str, int] = {}
    errors: list[str] = []

    for artifact, path, kind in INPUTS:
        if not path.is_file():
            errors.append(f"missing input: {path}")
            continue
        rows = read_rows(path)
        input_counts[artifact] = len(rows)
        for row in rows:
            decision = row.get("decision", "") or row.get("promotion_decision", "")
            if not decision.startswith("promote_to_22B"):
                errors.append(f"{artifact}: non-promotion row encountered: {decision}")
                continue
            normalized = normalized_row(row, artifact, kind)
            key = (normalized["species"], normalized["tf_symbol"].casefold(), normalized["target_symbol"].casefold())
            if not all(key):
                errors.append(f"{artifact}: incomplete pair: {key}")
                continue
            if not values(normalized["primary_pmids"]):
                errors.append(f"{artifact}: missing primary PMID for {key}")
                continue
            by_key[key].append(normalized)
            source_counts[artifact] += 1

    output_rows: list[dict[str, str]] = []
    duplicate_count = 0
    conflicting_effect_count = 0
    for index, key in enumerate(sorted(by_key), start=1):
        variants = by_key[key]
        if len(variants) > 1:
            duplicate_count += len(variants) - 1
        effects = {item["effect_polarity"] for item in variants}
        if len(effects) > 1:
            conflicting_effect_count += 1
        primary = join_unique([item["primary_pmids"] for item in variants])
        corroborating = join_unique([item["corroborating_pmids"] for item in variants])
        source_artifacts = join_unique([item["source_artifacts"] for item in variants])
        notes = join_unique([item["notes"] for item in variants])
        if len(effects) > 1:
            notes = join_unique([notes, "Conflicting staged polarity labels were retained as context_dependent."])
        selected = variants[0]
        row = dict(selected)
        row.update(
            {
                "materialization_id": f"M22B-PTF-{index:06d}",
                "module": "22B",
                "relation_type": "regulates_target_gene",
                "effect_polarity": "context_dependent" if len(effects) > 1 else selected["effect_polarity"],
                "canonical_confidence_tier": "medium",
                "membership_basis": "inferred_regulatory",
                "membership_status": "supported",
                "export_priority": "medium",
                "primary_pmids": primary,
                "corroborating_pmids": corroborating,
                "external_record_keys": join_unique([item["external_record_keys"] for item in variants]),
                "source_registries": join_unique([item["source_registries"] for item in variants]),
                "tf_entity_ids": join_unique([item["tf_entity_ids"] for item in variants]),
                "target_entity_ids": join_unique([item["target_entity_ids"] for item in variants]),
                "notes": notes,
                "source_artifacts": source_artifacts,
            }
        )
        output_rows.append({field: row.get(field, "") for field in OUTPUT_FIELDS})

    manifest = {
        "status": "pass" if not errors else "fail",
        "canonical_database_writes": False,
        "frozen_release_modified": False,
        "input_rows": input_counts,
        "accepted_input_rows": dict(source_counts),
        "unique_promoted_pairs": len(output_rows),
        "duplicate_rows_removed": duplicate_count,
        "pairs_with_conflicting_staged_polarity": conflicting_effect_count,
        "human_pairs": sum(row["species"] == "human" for row in output_rows),
        "mouse_pairs": sum(row["species"] == "mouse" for row in output_rows),
        "tf_species_keys": len({(row["species"], row["tf_symbol"].casefold()) for row in output_rows}),
        "tf_symbol_keys": len({row["tf_symbol"].casefold() for row in output_rows}),
        "target_species_keys": len({(row["species"], row["target_symbol"].casefold()) for row in output_rows}),
        "errors": errors,
        "policy": {
            "canonical_confidence": "medium",
            "membership_basis": "inferred_regulatory",
            "primary_evidence_required": True,
            "independent_corroboration": "preserved where available; primary-only rows remain explicitly limited",
            "upstream_activation": "not inferred",
        },
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "module22b_materialization_manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    if not errors:
        write_tsv(args.output_dir / "module22b_promoted_pairs.tsv", output_rows)
    print(json.dumps(manifest, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
