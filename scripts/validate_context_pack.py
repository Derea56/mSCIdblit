#!/usr/bin/env python3
"""Validate a file-based mSCIdblit context evidence pack."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


TABLES = {
    "contexts": "contexts.tsv",
    "observations": "observations.tsv",
    "mechanism_links": "mechanism_links.tsv",
}


def _read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames is None:
            raise ValueError(f"missing header: {path}")
        rows = list(reader)
        if any(None in row for row in rows):
            raise ValueError(f"row has more fields than header: {path}")
        return rows


def _require_nonempty(rows: list[dict[str, str]], field: str, path: Path) -> None:
    for number, row in enumerate(rows, start=2):
        if not row.get(field, "").strip():
            raise ValueError(f"{path}:{number}: {field} is required")


def _unique(rows: list[dict[str, str]], field: str, path: Path) -> None:
    values = [row.get(field, "") for row in rows]
    duplicates = sorted({value for value in values if value and values.count(value) > 1})
    if duplicates:
        raise ValueError(f"{path}: duplicate {field}: {', '.join(duplicates)}")


def validate_pack(pack: Path) -> dict[str, Any]:
    manifest_path = pack / "context_manifest.json"
    if not manifest_path.exists():
        raise ValueError(f"missing manifest: {manifest_path}")
    manifest = json.loads(manifest_path.read_text())

    if manifest.get("pack_type") != "disease_injury_evidence_overlay":
        raise ValueError("manifest pack_type must be disease_injury_evidence_overlay")
    if manifest.get("evidence_policy", {}).get("route_confidence_stored") is not False:
        raise ValueError("context packs must not store route confidence")
    if manifest.get("evidence_policy", {}).get("numeric_modality_weights_stored") is not False:
        raise ValueError("context packs must not store numeric modality weights")

    rows: dict[str, list[dict[str, str]]] = {}
    for key, filename in TABLES.items():
        path = pack / filename
        if not path.exists():
            raise ValueError(f"missing artifact: {path}")
        rows[key] = _read_tsv(path)

    contexts = rows["contexts"]
    observations = rows["observations"]
    links = rows["mechanism_links"]
    for field in ("context_id", "context_name", "context_kind", "context_status", "provenance_note"):
        _require_nonempty(contexts, field, pack / TABLES["contexts"])
    _unique(contexts, "context_id", pack / TABLES["contexts"])
    context_ids = {row["context_id"] for row in contexts}

    for field in ("observation_id", "context_id", "modality", "measurement_kind", "evidence_role", "dependency_group", "provenance_note"):
        _require_nonempty(observations, field, pack / TABLES["observations"])
    _unique(observations, "observation_id", pack / TABLES["observations"])
    observation_ids = {row["observation_id"] for row in observations}
    unknown_contexts = sorted({row["context_id"] for row in observations} - context_ids)
    if unknown_contexts:
        raise ValueError(f"observations reference unknown contexts: {', '.join(unknown_contexts)}")

    for field in ("link_id", "observation_id", "mechanism_release_id", "mechanism_target_kind", "mechanism_target_key", "route_stage", "link_role", "link_basis"):
        _require_nonempty(links, field, pack / TABLES["mechanism_links"])
    _unique(links, "link_id", pack / TABLES["mechanism_links"])
    unknown_observations = sorted({row["observation_id"] for row in links} - observation_ids)
    if unknown_observations:
        raise ValueError(f"links reference unknown observations: {', '.join(unknown_observations)}")

    expected_counts = manifest.get("counts", {})
    actual_counts = {
        "context_profiles": len(contexts),
        "observations": len(observations),
        "mechanism_links": len(links),
        "included_mechanism_links": sum(
            row.get("release_status") == "included" for row in links
        ),
    }
    if expected_counts != actual_counts:
        raise ValueError(f"manifest counts {expected_counts} do not match artifacts {actual_counts}")

    return {
        "pack_id": manifest["context_pack_id"],
        "pack_version": manifest["context_pack_version"],
        "status": manifest["status"],
        "counts": actual_counts,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pack", type=Path, help="context pack directory")
    args = parser.parse_args()
    try:
        summary = validate_pack(args.pack)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
