#!/usr/bin/env python3
"""Build the compact, release-owned route connector table.

The release already contains the evidence-layer route records. This command
does not infer missing biology or promote evidence to a causal graph edge. It
materializes a compact gzip-compressed table for L>O, L>R>O, L>R>S>TF>O, and
partial routes while retaining topology, layer status, and provenance.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
from pathlib import Path
from typing import Mapping


SCHEMA_VERSION = "mscs_route_connectors_v1"
TABLE_NAME = "route_connectors.tsv.gz"
REQUIRED_COLUMNS = (
    "route_evidence_id", "route_status", "route_tier", "path_expression",
    "known_layers", "missing_layers", "route_class", "ligand_node_id",
    "ligand_receptor_edge_id", "receptor_node_id", "receptor_intracellular_edge_id",
    "intracellular_continuation_node_id", "intracellular_tf_edge_id",
    "transcription_factor_node_id", "tf_target_edge_id", "target_gene_node_id",
    "output_node_id", "bridge_id", "evidence_ids", "source_chain_id", "effect_polarity",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _text(value: object) -> str:
    return "" if value is None else str(value).strip()


def _open_table(path: Path):
    return gzip.open(path, "rt", encoding="utf-8", newline="") if path.suffix == ".gz" else path.open("r", encoding="utf-8", newline="")


def _route_class(row: Mapping[str, str]) -> str:
    ligand = _text(row.get("ligand_node_id"))
    receptor = _text(row.get("receptor_node_id"))
    signal = _text(row.get("intracellular_continuation_node_id"))
    tf = _text(row.get("transcription_factor_node_id"))
    output = _text(row.get("output_node_id")) or _text(row.get("target_gene_node_id"))
    if ligand and receptor and signal and tf and output:
        return "l_r_s_tf_o"
    if ligand and receptor and signal and tf:
        return "l_r_s_tf"
    if ligand and receptor and signal and output:
        return "l_r_s_o"
    if ligand and receptor and tf and output:
        return "l_r_tf_o"
    if ligand and receptor and output:
        return "l_r_o"
    if ligand and output:
        return "l_o"
    if ligand and receptor:
        return "l_r"
    return "evidence_only"


def _source_route_path(release: Path) -> Path:
    graph = release / "mechanism_graph"
    for name in ("mechanism_signaling_route_evidence.tsv.gz", "mechanism_signaling_route_evidence.tsv"):
        path = graph / name
        if path.is_file():
            return path
    raise FileNotFoundError("release lacks mechanism_graph/mechanism_signaling_route_evidence.tsv[.gz]")


def _release_manifest(release: Path) -> tuple[Path, dict[str, object]]:
    path = release / "release_manifest.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or not _text(payload.get("release_id")):
        raise ValueError("release_manifest.json must contain a release_id")
    return path, payload


def build_route_connectors(release_directory: Path | str, output_directory: Path | str, *, register_in_release: bool = False) -> dict[str, object]:
    release = Path(release_directory).expanduser().resolve(strict=True)
    output = Path(output_directory).expanduser().resolve()
    if output.exists():
        raise FileExistsError(f"refusing to overwrite existing connector directory: {output}")
    output.mkdir(parents=True)
    release_manifest_path, release_manifest = _release_manifest(release)
    source = _source_route_path(release)
    table_path = output / TABLE_NAME
    counts_by_class: dict[str, int] = {}
    counts_by_status: dict[str, int] = {}
    row_count = 0
    seen: set[str] = set()
    with _open_table(source) as source_handle, gzip.open(table_path, "wt", encoding="utf-8", newline="") as table_handle:
        reader = csv.DictReader(source_handle, delimiter="\t")
        missing = set(REQUIRED_COLUMNS) - set(reader.fieldnames or ()) - {"route_class"}
        if missing:
            raise ValueError(f"route evidence is missing columns: {sorted(missing)}")
        writer = csv.DictWriter(table_handle, fieldnames=REQUIRED_COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in reader:
            route_id = _text(row.get("route_evidence_id"))
            if not route_id or route_id in seen:
                raise ValueError(f"route evidence IDs must be non-empty and unique: {route_id!r}")
            seen.add(route_id)
            route_class = _route_class(row)
            writer.writerow({column: route_class if column == "route_class" else _text(row.get(column)) for column in REQUIRED_COLUMNS})
            counts_by_class[route_class] = counts_by_class.get(route_class, 0) + 1
            status = _text(row.get("route_status"))
            counts_by_status[status] = counts_by_status.get(status, 0) + 1
            row_count += 1

    registered = output.is_relative_to(release)
    if register_in_release and not registered:
        raise ValueError("--register-in-release requires output inside the release directory")
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "runtime": "python_stdlib_gzip_tsv",
        "semantics": {
            "response_dependence": "response_independent_evidence",
            "causal_assertions_created": False,
            "missing_layers_preserved": True,
            "labels_resolved_from_release_graph": True,
            "route_classes": list(sorted(counts_by_class)),
        },
        "source_release": {
            "release_id": _text(release_manifest["release_id"]),
            "release_manifest_path": str(release_manifest_path.relative_to(release)),
            "route_evidence_path": str(source.relative_to(release)),
            "route_evidence_sha256": sha256(source),
        },
        "connector_table": {
            "relative_path": table_path.name,
            "sha256": sha256(table_path),
            "bytes": table_path.stat().st_size,
            "format": "gzip_tsv",
            "table": TABLE_NAME,
            "columns": list(REQUIRED_COLUMNS),
        },
        "counts": {
            "route_connectors": row_count,
            "by_route_class": dict(sorted(counts_by_class.items())),
            "by_route_status": dict(sorted(counts_by_status.items())),
        },
    }
    if not registered:
        manifest["source_release"]["release_manifest_sha256"] = sha256(release_manifest_path)
    manifest_path = output / "route_connectors_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if register_in_release:
        release_manifest["route_connector_manifest_path"] = str(manifest_path.relative_to(release))
        release_manifest["route_connector_table_path"] = str(table_path.relative_to(release))
        release_manifest.pop("route_connector_database_path", None)
        release_manifest["route_connector_contract"] = {
            "schema_version": SCHEMA_VERSION,
            "causal_assertions_created": False,
            "missing_layers_preserved": True,
            "storage": "gzip_tsv",
        }
        registered_files = dict(release_manifest.get("files", {}))
        output_prefix = str(output.relative_to(release)) + "/"
        for stale in [key for key in registered_files if key.startswith(output_prefix)]:
            registered_files.pop(stale, None)
        for path in (table_path, manifest_path):
            registered_files[str(path.relative_to(release))] = {"bytes": path.stat().st_size, "sha256": sha256(path)}
        release_manifest["files"] = registered_files
        release_manifest_path.write_text(json.dumps(release_manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release-directory", type=Path, required=True)
    parser.add_argument("--output-directory", type=Path, required=True)
    parser.add_argument("--register-in-release", action="store_true", help="register the connector table and manifest in the release manifest")
    args = parser.parse_args()
    manifest = build_route_connectors(args.release_directory, args.output_directory, register_in_release=args.register_in_release)
    print(json.dumps({"status": "complete", "output_directory": str(args.output_directory.resolve()), "counts": manifest["counts"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
