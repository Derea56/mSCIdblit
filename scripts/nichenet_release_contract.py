#!/usr/bin/env python3
"""Build and validate the release-owned NicheNet prior contract."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
from typing import Any


CONTRACT_RELATIVE = Path("method_resources/nichenet_ligand_target_prior_manifest.json")
COMPANION_RELATIVE = Path("nichenet_neutral_v1/ligand_target_matrix.f64le.bin")
TARGET_AXIS_RELATIVE = Path("method_resources/method_native/nichenet_neutral_v1/target_genes.tsv")
LIGAND_AXIS_RELATIVE = Path("method_resources/method_native/nichenet_neutral_v1/ligands.tsv")
LR_NETWORK_RELATIVE = Path("method_resources/method_native/nichenet_neutral_v1/lr_network.tsv")
OUTPUT_PROJECTION_RELATIVE = Path("mechanism_graph/mechanism_output_bridges_validated.tsv")


class NicheNetContractError(ValueError):
    """Raised when a release-owned NicheNet contract is invalid."""


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise NicheNetContractError(f"missing tabular release input: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def _relative_path(value: Any, field: str) -> Path:
    if not isinstance(value, str) or not value or Path(value).is_absolute():
        raise NicheNetContractError(f"{field} must be a non-empty relative path")
    path = Path(value)
    if ".." in path.parts:
        raise NicheNetContractError(f"{field} must not escape its root: {value}")
    return path


def _axis_contract(bundle: Path, path: Path, role: str, expected_count: int) -> dict[str, Any]:
    rows = _read_tsv(bundle / path)
    if len(rows) != expected_count:
        raise NicheNetContractError(f"{role} axis row count mismatch: {len(rows)} != {expected_count}")
    if not rows or len(rows[0]) != 1:
        raise NicheNetContractError(f"{role} axis must have exactly one column: {path}")
    column = next(iter(rows[0]))
    values = [row.get(column, "") for row in rows]
    if len(set(values)) != len(values) or any(not value for value in values):
        raise NicheNetContractError(f"{role} axis contains empty or duplicate identifiers: {path}")
    return {
        "release_path": path.as_posix(),
        "sha256": sha256(bundle / path),
        "row_count": len(rows),
        "column": column,
    }


def _numeric_row(method_dir: Path) -> dict[str, str]:
    rows = _read_tsv(method_dir / "method_resource_numeric_artifacts.tsv")
    matches = [row for row in rows if row.get("artifact_key") == "nichenet_neutral_v1_ligand_target_matrix"]
    if len(matches) != 1:
        raise NicheNetContractError("method migration must contain exactly one neutral NicheNet matrix row")
    return matches[0]


def build_contract(*, method_dir: Path, bundle: Path, companion_artifact_root: Path,
                   output_projection: Path = OUTPUT_PROJECTION_RELATIVE) -> dict[str, Any]:
    """Verify inputs and return the immutable release contract payload."""
    neutral_path = method_dir / "method_native/nichenet_neutral_v1/neutral_model_manifest.json"
    if not neutral_path.is_file():
        raise NicheNetContractError(f"missing neutral model manifest: {neutral_path}")
    neutral = json.loads(neutral_path.read_text(encoding="utf-8"))
    numeric = _numeric_row(method_dir)
    shape = neutral.get("matrix_shape")
    if not isinstance(shape, list) or len(shape) != 2:
        raise NicheNetContractError("neutral manifest matrix_shape must contain two dimensions")
    target_count, ligand_count = int(shape[0]), int(shape[1])
    matrix = companion_artifact_root / COMPANION_RELATIVE
    if not matrix.is_file():
        raise NicheNetContractError(f"missing NicheNet companion matrix: {matrix}")
    expected_hash = str(neutral.get("matrix_sha256") or numeric.get("artifact_sha256") or "")
    if sha256(matrix) != expected_hash or numeric.get("artifact_sha256") != expected_hash:
        raise NicheNetContractError(f"NicheNet matrix checksum mismatch: {sha256(matrix)} != {expected_hash}")
    expected_bytes = target_count * ligand_count * 8
    if matrix.stat().st_size != expected_bytes or int(numeric.get("byte_size", -1)) != expected_bytes:
        raise NicheNetContractError(f"NicheNet matrix byte size mismatch: {matrix.stat().st_size} != {expected_bytes}")
    if numeric.get("dtype") != "float64" or numeric.get("endianness") != "little" or numeric.get("layout") != "column_major":
        raise NicheNetContractError("numeric artifact dtype, endianness, or layout is not the pinned contract")

    target_axis = _axis_contract(bundle, TARGET_AXIS_RELATIVE, "target", target_count)
    ligand_axis = _axis_contract(bundle, LIGAND_AXIS_RELATIVE, "ligand", ligand_count)
    lr_path = bundle / LR_NETWORK_RELATIVE
    lr_rows = _read_tsv(lr_path)
    expected_lr = int(neutral.get("lr_network_row_count", 0))
    if len(lr_rows) != expected_lr:
        raise NicheNetContractError(f"LR network row count mismatch: {len(lr_rows)} != {expected_lr}")
    projection_path = bundle / output_projection
    projection_rows = _read_tsv(projection_path)
    required_columns = {"bridge_id", "source_label", "output_label", "output_product_labels",
                        "validation_status", "causal_status", "traversal_status"}
    if not projection_rows or not required_columns.issubset(projection_rows[0]):
        raise NicheNetContractError("output projection is missing required bridge columns")

    return {
        "schema_version": "nichenet_release_resource_v1",
        "artifact_key": numeric["artifact_key"],
        "resource_key": numeric["resource_key"],
        "source_model": neutral["source_model"],
        "species": "mouse",
        "matrix": {
            "companion_relative_path": COMPANION_RELATIVE.as_posix(),
            "sha256": expected_hash,
            "byte_size": expected_bytes,
            "dtype": "float64",
            "endianness": "little",
            "layout": "column_major",
            "shape": [target_count, ligand_count],
            "selection": "complete_matrix",
            "response_dependence": "response_independent_prior",
        },
        "axes": {"target": target_axis, "ligand": ligand_axis},
        "lr_network": {
            "release_path": LR_NETWORK_RELATIVE.as_posix(),
            "sha256": sha256(lr_path),
            "row_count": len(lr_rows),
        },
        "output_projection": {
            "release_path": output_projection.as_posix(),
            "sha256": sha256(projection_path),
            "row_count": len(projection_rows),
            "role": "broad_response_independent_ligand_to_output_mapping",
            "selection": "all_validated_output_bridges",
            "receiver_compatible_lr_join_required": True,
            "causal_assertions_created": False,
            "graph_edges_created": False,
        },
        "storage": {
            "mode": "companion_required",
            "companion_artifact_root_config_key": "nichenet_companion_artifact_root",
            "release_owned_contract": True,
            "working_tree_dependency": False,
        },
        "limitations": [
            "The dense prior is not expanded into relational rows or top-k mappings.",
            "The output projection is evidence-layer metadata and does not create causal graph edges or route confidence.",
            "The companion artifact root must be supplied by the downstream consumer and is verified fail-closed.",
        ],
    }


def validate_contract(*, bundle: Path, companion_artifact_root: Path | None) -> dict[str, Any]:
    """Validate a release contract and its companion artifact."""
    contract_path = bundle / CONTRACT_RELATIVE
    if not contract_path.is_file():
        raise NicheNetContractError(f"missing NicheNet release contract: {contract_path}")
    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    if contract.get("schema_version") != "nichenet_release_resource_v1":
        raise NicheNetContractError("unsupported NicheNet release contract schema")
    matrix = contract.get("matrix")
    if not isinstance(matrix, dict):
        raise NicheNetContractError("NicheNet contract has no matrix block")
    shape = matrix.get("shape")
    if not isinstance(shape, list) or len(shape) != 2 or any(int(value) <= 0 for value in shape):
        raise NicheNetContractError("NicheNet contract matrix shape is incomplete")
    if matrix.get("dtype") != "float64" or matrix.get("endianness") != "little" or matrix.get("layout") != "column_major":
        raise NicheNetContractError("NicheNet contract matrix layout is unsupported")
    if matrix.get("selection") != "complete_matrix" or matrix.get("response_dependence") != "response_independent_prior":
        raise NicheNetContractError("NicheNet prior completeness/response contract is invalid")
    if companion_artifact_root is None:
        raise NicheNetContractError("nichenet_companion_artifact_root is required; refusing to validate an unavailable prior")
    companion = companion_artifact_root / _relative_path(matrix.get("companion_relative_path"), "matrix.companion_relative_path")
    if not companion.is_file():
        raise NicheNetContractError(f"missing NicheNet companion matrix: {companion}")
    expected_bytes = int(shape[0]) * int(shape[1]) * 8
    if companion.stat().st_size != expected_bytes or companion.stat().st_size != int(matrix.get("byte_size", -1)):
        raise NicheNetContractError("NicheNet matrix shape/byte-size contract mismatch")
    actual_hash = sha256(companion)
    if actual_hash != matrix.get("sha256"):
        raise NicheNetContractError(f"NicheNet matrix checksum mismatch: {actual_hash}")

    axes = contract.get("axes")
    if not isinstance(axes, dict) or set(axes) != {"target", "ligand"}:
        raise NicheNetContractError("NicheNet contract must contain target and ligand axes")
    for role, expected_count in (("target", int(shape[0])), ("ligand", int(shape[1]))):
        axis = axes[role]
        if not isinstance(axis, dict):
            raise NicheNetContractError(f"{role} axis contract is incomplete")
        axis_path = _relative_path(axis.get("release_path"), f"axes.{role}.release_path")
        axis_info = _axis_contract(bundle, axis_path, role, expected_count)
        if axis_info["sha256"] != axis.get("sha256"):
            raise NicheNetContractError(f"{role} axis checksum mismatch")
        if axis_info["row_count"] != int(axis.get("row_count", -1)):
            raise NicheNetContractError(f"{role} axis row-count contract mismatch")

    for key in ("lr_network", "output_projection"):
        block = contract.get(key)
        if not isinstance(block, dict):
            raise NicheNetContractError(f"NicheNet contract missing {key} block")
        path = _relative_path(block.get("release_path"), f"{key}.release_path")
        full_path = bundle / path
        if not full_path.is_file() or sha256(full_path) != block.get("sha256"):
            raise NicheNetContractError(f"{key} path or checksum is invalid: {path}")
        rows = _read_tsv(full_path)
        if len(rows) != int(block.get("row_count", -1)):
            raise NicheNetContractError(f"{key} row-count contract mismatch")
    storage = contract.get("storage")
    if not isinstance(storage, dict) or storage.get("mode") != "companion_required" or storage.get("working_tree_dependency") is not False:
        raise NicheNetContractError("NicheNet storage contract is incomplete")
    return {
        "artifact_key": contract.get("artifact_key"),
        "matrix_sha256": actual_hash,
        "matrix_shape": shape,
        "target_axis_sha256": axes["target"].get("sha256"),
        "ligand_axis_sha256": axes["ligand"].get("sha256"),
        "output_projection_rows": contract["output_projection"].get("row_count"),
    }
