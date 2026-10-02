#!/usr/bin/env python3
"""Contract helpers for the additive mouse TF-target prior release."""

from __future__ import annotations

import csv
import hashlib
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable


PRIOR_DIR = Path("tf_target_prior")
PRIOR_MANIFEST = PRIOR_DIR / "tf_target_prior_manifest.json"
PRIOR_TABLE = PRIOR_DIR / "tf_target_prior.tsv"
SOURCE_RECORDS = PRIOR_DIR / "tf_target_prior_source_records.tsv"
TF_AXIS = PRIOR_DIR / "tf_axis.tsv"
TARGET_AXIS = PRIOR_DIR / "target_axis.tsv"
DIRECT_GRAPH_TIER = PRIOR_DIR / "tf_target_direct_graph_tier.tsv"
SOURCE_REGISTRY = PRIOR_DIR / "source_registry.tsv"
SCHEMA_VERSION = "tf_target_prior_v1"
ID_PREFIX = "mouse_gene_symbol:"
SIGNED_EFFECTS = {"activating_target", "repressing_target"}


class TFTargetPriorError(ValueError):
    """Raised when the TF-target prior cannot satisfy its release contract."""


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise TFTargetPriorError(f"missing TF-target prior input: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


def gene_id(symbol: str) -> str:
    symbol = symbol.strip()
    if not symbol:
        raise TFTargetPriorError("empty mouse gene symbol")
    return f"{ID_PREFIX}{symbol}"


def _json_list(values: Iterable[str]) -> str:
    return json.dumps(sorted({value for value in values if value}), separators=(",", ":"))


def resolve_effect(rows: list[dict[str, str]]) -> tuple[str, str]:
    effects = {row.get("effect_polarity", "unknown") or "unknown" for row in rows}
    signed = effects & SIGNED_EFFECTS
    if len(signed) > 1:
        return "unknown", "conflicting_signed_sources"
    if not signed:
        return "unknown", "unknown_only"
    if "unknown" in effects:
        return next(iter(signed)), "consistent_signed_sources_with_unknowns"
    return next(iter(signed)), "consistent_signed_sources"


def aggregate_pairs(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    """Collapse source records by exact namespace-qualified mouse symbol pair."""
    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        tf = row.get("normalized_tf_symbol", "").strip()
        target = row.get("normalized_target_symbol", "").strip()
        if not tf or not target:
            raise TFTargetPriorError("retained source row lacks normalized TF or target symbol")
        grouped[(tf, target)].append(row)
    output: list[dict[str, str]] = []
    for ordinal, ((tf, target), members) in enumerate(sorted(grouped.items()), start=1):
        effect, effect_resolution = resolve_effect(members)
        relationships = {row.get("relationship_class", "unresolved") or "unresolved" for row in members}
        bases = {row.get("evidence_basis", "unresolved") or "unresolved" for row in members}
        output.append({
            "prior_record_id": f"TRRUST_MOUSE_PAIR:{ordinal:05d}",
            "tf_id": gene_id(tf),
            "target_id": gene_id(target),
            "tf_symbol": tf,
            "target_symbol": target,
            "species": "mouse",
            "source_registry": "TRRUST",
            "source_version": members[0].get("source_version", ""),
            "source_record_count": str(len(members)),
            "source_record_ids": _json_list(row.get("source_record_id", "") for row in members),
            "raw_record_sha256s": _json_list(row.get("raw_record_sha256", "") for row in members),
            "effect_polarity": effect,
            "effect_resolution": effect_resolution,
            "relationship_class": ";".join(sorted(relationships)),
            "evidence_basis": ";".join(sorted(bases)),
            "reference_pmids": _json_list(
                pmid for row in members for pmid in (row.get("reference_pmids", "").split(";") if row.get("reference_pmids") else [])
            ),
            "source_locators": _json_list(row.get("source_locator", "") for row in members),
            "association_weight": "",
            "weight_status": "not_supplied",
            "association_rank": "",
            "rank_status": "not_supplied",
            "observed_response_used": "false",
            "prior_role": "broad_response_independent_prior",
        })
    return output


def validate_prior_manifest(release_dir: Path, manifest_path: Path | None = None) -> dict[str, Any]:
    """Fail-closed validation of the TF-target prior and its provenance files."""
    path = manifest_path or release_dir / PRIOR_MANIFEST
    if not path.is_file():
        raise TFTargetPriorError(f"missing TF-target prior manifest: {path}")
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if manifest.get("schema_version") != SCHEMA_VERSION:
        raise TFTargetPriorError("unsupported TF-target prior schema")
    if manifest.get("species") != "mouse" or manifest.get("response_selection") != "none":
        raise TFTargetPriorError("prior is not explicitly mouse-only and response-independent")
    if manifest.get("weights", {}).get("status") != "not_supplied" or manifest.get("ranks", {}).get("status") != "not_supplied":
        raise TFTargetPriorError("prior claims an unsupported weight or rank")
    files = manifest.get("files")
    if not isinstance(files, dict):
        raise TFTargetPriorError("TF-target prior manifest has no files block")
    for relative, metadata in files.items():
        file_path = release_dir / relative
        if not file_path.is_file():
            raise TFTargetPriorError(f"missing TF-target prior file: {relative}")
        if sha256(file_path) != metadata.get("sha256") or file_path.stat().st_size != int(metadata.get("bytes", -1)):
            raise TFTargetPriorError(f"TF-target prior checksum/size mismatch: {relative}")

    prior_rows = read_tsv(release_dir / PRIOR_TABLE)
    source_rows = read_tsv(release_dir / SOURCE_RECORDS)
    tf_rows = read_tsv(release_dir / TF_AXIS)
    target_rows = read_tsv(release_dir / TARGET_AXIS)
    if not tf_rows or len({row.get("tf_id") for row in tf_rows}) != len(tf_rows) or any(not row.get("tf_id") for row in tf_rows):
        raise TFTargetPriorError("TF axis contains empty or duplicate IDs")
    if not target_rows or len({row.get("target_id") for row in target_rows}) != len(target_rows) or any(not row.get("target_id") for row in target_rows):
        raise TFTargetPriorError("target axis contains empty or duplicate IDs")
    tf_ids, target_ids = {row["tf_id"] for row in tf_rows}, {row["target_id"] for row in target_rows}
    required = {"tf_id", "target_id", "effect_polarity", "association_weight", "association_rank", "observed_response_used"}
    if not prior_rows or not required.issubset(prior_rows[0]):
        raise TFTargetPriorError("TF-target prior is missing required association columns")
    pair_keys = {(row.get("tf_id"), row.get("target_id")) for row in prior_rows}
    if len(pair_keys) != len(prior_rows) or any(tf not in tf_ids or target not in target_ids for tf, target in pair_keys):
        raise TFTargetPriorError("prior rows do not match unique axis IDs")
    allowed_effects = SIGNED_EFFECTS | {"context_dependent", "unknown"}
    for row in prior_rows:
        if row.get("effect_polarity") not in allowed_effects:
            raise TFTargetPriorError("invalid effect polarity in TF-target prior")
        if row.get("observed_response_used") != "false" or row.get("association_weight") or row.get("association_rank"):
            raise TFTargetPriorError("TF-target prior contains response-selected or invented numeric values")
    if len(source_rows) != int(manifest.get("counts", {}).get("source_record_count", -1)):
        raise TFTargetPriorError("source-record count mismatch")
    source_ids = [row.get("source_record_id", "") for row in source_rows]
    if any(not value for value in source_ids) or len(set(source_ids)) != len(source_ids):
        raise TFTargetPriorError("source records contain empty or duplicate source_record_id values")
    direct_path = release_dir / DIRECT_GRAPH_TIER
    direct_rows = read_tsv(direct_path)
    expected_direct = int(manifest.get("counts", {}).get("direct_graph_edge_count", -1))
    if len(direct_rows) != expected_direct or any(row.get("tier") != "direct_graph_evidence" for row in direct_rows):
        raise TFTargetPriorError("direct graph evidence tier count or tier label mismatch")
    source_registry = read_tsv(release_dir / SOURCE_REGISTRY)
    if len(source_registry) != 1 or source_registry[0].get("license_name") != manifest.get("source", {}).get("license_name"):
        raise TFTargetPriorError("source registry license/provenance block is incomplete")
    if len(prior_rows) != int(manifest.get("counts", {}).get("pair_count", -1)):
        raise TFTargetPriorError("unique pair count mismatch")
    if len(tf_rows) != int(manifest.get("counts", {}).get("tf_count", -1)) or len(target_rows) != int(manifest.get("counts", {}).get("target_count", -1)):
        raise TFTargetPriorError("axis count mismatch")
    return {
        "status": "PASS TF-target prior validation",
        "pair_count": len(prior_rows),
        "source_record_count": len(source_rows),
        "tf_count": len(tf_rows),
        "target_count": len(target_rows),
        "direct_graph_edge_count": manifest.get("counts", {}).get("direct_graph_edge_count"),
    }
