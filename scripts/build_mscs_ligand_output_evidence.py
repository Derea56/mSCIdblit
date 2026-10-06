#!/usr/bin/env python3
"""Materialize the release-owned ligand-to-output evidence database.

The source matrix is a response-independent ranked prior.  This command turns
its ligand and target axes into one indexed SQLite table owned by the
mSCIdblit release.  The source method remains provenance for each relationship;
the table is the canonical L>O evidence interface for downstream consumers.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import mmap
import os
from pathlib import Path
import shutil
import sqlite3
import struct
from typing import Iterable


SCHEMA_VERSION = "mscs_ligand_output_evidence_v1"
DATABASE_NAME = "ligand_output_evidence.sqlite"
TABLE_NAME = "ligand_output_prior"
AXIS_COLUMNS = {
    "ligands": "ligand_id",
    "targets": "target_id",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _text(value: object) -> str:
    return "" if value is None else str(value).strip()


def _read_axis(path: Path, column: str) -> list[str]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if tuple(reader.fieldnames or ()) != (column,):
            raise ValueError(f"{path.name} must contain exactly one {column} column")
        values = [_text(row.get(column)) for row in reader]
    if any(not value for value in values):
        raise ValueError(f"{path} contains a blank {column}")
    if len(set(values)) != len(values):
        raise ValueError(f"{path} contains duplicate {column} identifiers")
    return values


def _release_manifest(release: Path) -> tuple[Path, dict[str, object]]:
    path = release / "release_manifest.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or not _text(payload.get("release_id")):
        raise ValueError("release_manifest.json must contain a release_id")
    return path, payload


def _write_metadata(connection: sqlite3.Connection, metadata: dict[str, str]) -> None:
    connection.executemany(
        "INSERT INTO metadata(key, value) VALUES (?, ?)",
        sorted(metadata.items()),
    )


def build_ligand_output_evidence(
    release_directory: Path | str,
    matrix_path: Path | str,
    output_directory: Path | str,
    *,
    register_in_release: bool = False,
) -> dict[str, object]:
    release = Path(release_directory).expanduser().resolve(strict=True)
    matrix = Path(matrix_path).expanduser().resolve(strict=True)
    output = Path(output_directory).expanduser().resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite existing output: {output}")
    registered = output.is_relative_to(release)
    if register_in_release and not registered:
        raise ValueError("--register-in-release requires output inside the release")

    release_manifest_path, release_manifest = _release_manifest(release)
    neutral = release / "method_resources/method_native/nichenet_neutral_v1"
    ligand_path = neutral / "ligands.tsv"
    target_path = neutral / "target_genes.tsv"
    neutral_manifest_path = neutral / "neutral_model_manifest.json"
    for path in (ligand_path, target_path, neutral_manifest_path):
        if not path.is_file():
            raise FileNotFoundError(f"release is missing required axis file: {path}")
    neutral_manifest = json.loads(neutral_manifest_path.read_text(encoding="utf-8"))
    shape = neutral_manifest.get("matrix_shape")
    if not isinstance(shape, list) or len(shape) != 2:
        raise ValueError("neutral model manifest has no two-dimensional matrix_shape")
    target_count, ligand_count = (int(shape[0]), int(shape[1]))
    ligands = _read_axis(ligand_path, AXIS_COLUMNS["ligands"])
    targets = _read_axis(target_path, AXIS_COLUMNS["targets"])
    if len(ligands) != ligand_count or len(targets) != target_count:
        raise ValueError("matrix shape disagrees with release axes")
    expected_bytes = target_count * ligand_count * 8
    if matrix.stat().st_size != expected_bytes:
        raise ValueError(
            f"matrix byte count disagrees: {matrix.stat().st_size} != {expected_bytes}"
        )
    expected_matrix_sha256 = neutral_manifest.get("matrix_sha256")
    if expected_matrix_sha256 and sha256(matrix) != expected_matrix_sha256:
        raise ValueError("matrix checksum disagrees with the release neutral manifest")

    output.mkdir(parents=True)
    database_path = output / DATABASE_NAME
    temporary_database = output / f".{DATABASE_NAME}.tmp"
    if temporary_database.exists():
        temporary_database.unlink()
    try:
        connection = sqlite3.connect(temporary_database)
        try:
            connection.executescript(
                """
                PRAGMA journal_mode=OFF;
                PRAGMA synchronous=OFF;
                CREATE TABLE metadata (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL
                );
                CREATE TABLE ligands (
                    ligand_idx INTEGER PRIMARY KEY,
                    ligand_id TEXT NOT NULL UNIQUE
                );
                CREATE TABLE targets (
                    target_idx INTEGER PRIMARY KEY,
                    target_id TEXT NOT NULL UNIQUE
                );
                CREATE TABLE ligand_output_prior (
                    ligand_idx INTEGER NOT NULL,
                    target_idx INTEGER NOT NULL,
                    target_rank_within_ligand INTEGER NOT NULL,
                    regulatory_potential REAL NOT NULL,
                    PRIMARY KEY (ligand_idx, target_rank_within_ligand),
                    UNIQUE (ligand_idx, target_idx),
                    FOREIGN KEY (ligand_idx) REFERENCES ligands(ligand_idx),
                    FOREIGN KEY (target_idx) REFERENCES targets(target_idx)
                ) WITHOUT ROWID;
                """
            )
            connection.executemany(
                "INSERT INTO ligands(ligand_idx, ligand_id) VALUES (?, ?)",
                enumerate(ligands),
            )
            connection.executemany(
                "INSERT INTO targets(target_idx, target_id) VALUES (?, ?)",
                enumerate(targets),
            )
            metadata = {
                "schema_version": SCHEMA_VERSION,
                "release_id": _text(release_manifest["release_id"]),
                "source_model": _text(neutral_manifest.get("source_model")) or "unknown",
                "species": _text(neutral_manifest.get("species")) or "unknown",
                "interpretation": "ranked_ligand_output_prior_not_probability_or_causal_edge",
                "matrix_layout": _text(neutral_manifest.get("matrix_layout")) or "column_major",
                "matrix_dtype": _text(neutral_manifest.get("matrix_dtype")) or "float64",
                "matrix_sha256": sha256(matrix),
                "ligand_axis_sha256": sha256(ligand_path),
                "target_axis_sha256": sha256(target_path),
            }
            _write_metadata(connection, metadata)

            row_count = 0
            with matrix.open("rb") as handle:
                mapped = mmap.mmap(handle.fileno(), 0, access=mmap.ACCESS_READ)
                try:
                    for ligand_idx, ligand_id in enumerate(ligands):
                        offset = ligand_idx * target_count * 8
                        scores = struct.unpack_from(f"<{target_count}d", mapped, offset)
                        ranked = sorted(
                            zip(scores, targets, range(target_count)),
                            key=lambda item: (-item[0], item[1]),
                        )
                        connection.executemany(
                            """
                            INSERT INTO ligand_output_prior(
                                ligand_idx, target_idx,
                                target_rank_within_ligand, regulatory_potential
                            ) VALUES (?, ?, ?, ?)
                            """,
                            (
                                (ligand_idx, target_idx, rank, float(score))
                                for rank, (score, _target_id, target_idx) in enumerate(ranked, start=1)
                            ),
                        )
                        row_count += target_count
                        if ligand_idx % 16 == 0:
                            connection.commit()
                finally:
                    mapped.close()
            connection.execute(
                "CREATE INDEX ligand_output_prior_target_idx ON ligand_output_prior(target_idx, ligand_idx)"
            )
            connection.commit()
        finally:
            connection.close()
        os.replace(temporary_database, database_path)
    except BaseException:
        if temporary_database.exists():
            temporary_database.unlink()
        shutil.rmtree(output, ignore_errors=True)
        raise

    manifest = {
        "schema_version": SCHEMA_VERSION,
        "runtime": "python_stdlib_sqlite",
        "semantics": {
            "response_dependence": "response_independent_prior",
            "interpretation": "ranked_ligand_output_prior_not_probability_or_causal_edge",
            "direction_assigned": False,
            "source_method_is_provenance_only": True,
        },
        "source_release": {
            "release_id": _text(release_manifest["release_id"]),
            "release_manifest_path": str(release_manifest_path.relative_to(release)),
            "neutral_model_manifest_path": str(neutral_manifest_path.relative_to(release)),
            "matrix_sha256": sha256(matrix),
            "matrix_reference": "method_resources/nichenet_ligand_target_prior_manifest.json",
        },
        "database": {
            "relative_path": database_path.name,
            "sha256": sha256(database_path),
            "bytes": database_path.stat().st_size,
            "table": TABLE_NAME,
            "columns": [
                "ligand_idx",
                "target_idx",
                "target_rank_within_ligand",
                "regulatory_potential",
            ],
        },
        "counts": {
            "ligands": ligand_count,
            "outputs": target_count,
            "relationships": row_count,
            "maximum_target_rank": target_count,
        },
    }
    manifest_path = output / "ligand_output_evidence_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if register_in_release:
        release_manifest["ligand_output_evidence_manifest_path"] = str(manifest_path.relative_to(release))
        release_manifest["ligand_output_evidence_database_path"] = str(database_path.relative_to(release))
        release_manifest["ligand_output_evidence_contract"] = {
            "schema_version": SCHEMA_VERSION,
            "storage": "sqlite",
            "source_method_is_provenance_only": True,
        }
        registered_files = dict(release_manifest.get("files", {}))
        prefix = str(output.relative_to(release)) + "/"
        for stale in [key for key in registered_files if key.startswith(prefix)]:
            registered_files.pop(stale, None)
        for path in (database_path, manifest_path):
            registered_files[str(path.relative_to(release))] = {
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
        release_manifest["files"] = registered_files
        release_manifest_path.write_text(
            json.dumps(release_manifest, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release-directory", type=Path, required=True)
    parser.add_argument("--matrix-path", type=Path, required=True)
    parser.add_argument("--output-directory", type=Path, required=True)
    parser.add_argument(
        "--register-in-release",
        action="store_true",
        help="register the database and manifest in release_manifest.json",
    )
    args = parser.parse_args()
    manifest = build_ligand_output_evidence(
        args.release_directory,
        args.matrix_path,
        args.output_directory,
        register_in_release=args.register_in_release,
    )
    print(json.dumps({"status": "complete", "counts": manifest["counts"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
