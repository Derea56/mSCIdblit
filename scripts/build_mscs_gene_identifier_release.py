#!/usr/bin/env python3
"""Build an immutable mSCS release carrying the source-bound gene crosswalk."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASE = ROOT / "data/processed/mscs_release_bundle_v1_7_0_nichenet_tf_prior_v1"
DEFAULT_CROSSWALK = ROOT / "data/processed/gene_identifier_crosswalk_ncbi_2026_10_02_v1"
DEFAULT_OUTPUT = ROOT / "data/processed/mscs_release_bundle_v1_8_0_nichenet_tf_prior_gene_identifiers_v1"
DEFAULT_RELEASE_ID = "mscs_release_bundle:2026-10-02-nichenet-tf-prior-gene-identifiers-v1"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise SystemExit(f"Expected JSON object: {path}")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-release-dir", type=Path, default=DEFAULT_BASE)
    parser.add_argument("--crosswalk-dir", type=Path, default=DEFAULT_CROSSWALK)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--release-id", default=DEFAULT_RELEASE_ID)
    args = parser.parse_args()
    base = args.base_release_dir.resolve()
    crosswalk = args.crosswalk_dir.resolve()
    output = args.output_dir.resolve()
    if output.exists():
        raise SystemExit(f"Refusing to overwrite gene-identifier release: {output}")
    base_manifest = load_json(base / "release_manifest.json")
    crosswalk_manifest = load_json(crosswalk / "gene_identifier_crosswalk_manifest.json")
    source_files = [crosswalk / name for name in ("gene_catalog.tsv", "gene_crosswalk.tsv", "gene_orthology.tsv", "gene_identifier_crosswalk_manifest.json")]
    missing = [str(path) for path in source_files if not path.is_file()]
    if missing:
        raise SystemExit("Missing gene crosswalk files: " + ", ".join(missing))

    shutil.copytree(base, output)
    target_dir = output / "gene_identifier_crosswalk"
    target_dir.mkdir(parents=True, exist_ok=True)
    copied = []
    for source in source_files:
        target = target_dir / source.name
        shutil.copy2(source, target)
        copied.append(target)

    manifest = dict(base_manifest)
    manifest["release_id"] = args.release_id
    manifest["parent_release_id"] = base_manifest.get("release_id")
    manifest["gene_identifier_crosswalk_manifest"] = "gene_identifier_crosswalk/gene_identifier_crosswalk_manifest.json"
    manifest["gene_identifier_crosswalk"] = crosswalk_manifest
    manifest["gene_identifier_contract"] = {
        "schema_version": crosswalk_manifest.get("schema_version"),
        "species_explicit": True,
        "case_normalized_lookup_supported": True,
        "ambiguous_mappings_preserved": True,
        "unresolved_mappings_preserved": True,
        "orthology_inference": False,
    }
    counts = dict(base_manifest.get("counts", {}))
    counts.update({
        "gene_crosswalk_rows": crosswalk_manifest["counts"]["crosswalk_rows"],
        "gene_crosswalk_resolved_rows": crosswalk_manifest["counts"]["crosswalk_resolved_rows"],
        "gene_crosswalk_ambiguous_rows": crosswalk_manifest["counts"]["crosswalk_ambiguous_rows"],
        "gene_crosswalk_unresolved_rows": crosswalk_manifest["counts"]["crosswalk_unresolved_rows"],
        "gene_orthology_rows": crosswalk_manifest["counts"]["orthology_rows"],
    })
    manifest["counts"] = counts
    manifest["migration_gaps"] = list(base_manifest.get("migration_gaps", [])) + [
        "The NCBI GeneInfo and gene_orthologs raw snapshots are checksum-pinned references and are not copied into the Git release.",
        "Ambiguous and unresolved gene identifier mappings remain in the crosswalk and require downstream policy rather than automatic selection.",
    ]
    files = dict(base_manifest.get("files", {}))
    for path in copied:
        files[str(path.relative_to(output))] = {"sha256": sha256(path), "bytes": path.stat().st_size}
    manifest["files"] = files
    (output / "release_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "output_dir": str(output),
        "release_id": args.release_id,
        "parent_release_id": base_manifest.get("release_id"),
        "gene_crosswalk_rows": counts["gene_crosswalk_rows"],
        "gene_orthology_rows": counts["gene_orthology_rows"],
        "manifest_files": len(files),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
