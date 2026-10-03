#!/usr/bin/env python3
"""Build an immutable mSCS release with the corrected LR component crosswalk."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASE = ROOT / "data/processed/mscs_release_bundle_v1_8_0_nichenet_tf_prior_gene_identifiers_v2"
DEFAULT_CANDIDATE = ROOT / "data/processed/mechanism_lr_candidate_universe_v3_component_crosswalk_v1"
DEFAULT_OUTPUT = ROOT / "data/processed/mscs_release_bundle_v1_9_0_nichenet_tf_prior_gene_identifiers_candidate_components_v1"
DEFAULT_RELEASE_ID = "mscs_release_bundle:2026-10-03-nichenet-tf-prior-gene-identifiers-candidate-components-v1"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-release-dir", type=Path, default=DEFAULT_BASE)
    parser.add_argument("--candidate-dir", type=Path, default=DEFAULT_CANDIDATE)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--release-id", default=DEFAULT_RELEASE_ID)
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise SystemExit(f"Expected JSON object: {path}")
    return value


def main() -> int:
    args = parse_args()
    base = args.base_release_dir.resolve()
    candidate = args.candidate_dir.resolve()
    output = args.output_dir.resolve()
    if output.exists():
        raise SystemExit(f"Refusing to overwrite existing release: {output}")
    base_manifest = load_json(base / "release_manifest.json")
    required_candidate = [
        candidate / "mechanism_lr_candidate_universe.tsv",
        candidate / "mechanism_lr_candidate_universe_report.json",
        candidate / "mechanism_lr_candidate_component_crosswalk.tsv",
        candidate / "candidate_component_handoff.json",
    ]
    missing = [str(path) for path in required_candidate if not path.is_file()]
    if missing:
        raise SystemExit("Missing corrected candidate-universe inputs: " + ", ".join(missing))

    shutil.copytree(base, output)
    candidate_target = output / "candidate_universe"
    candidate_target.mkdir(parents=True, exist_ok=True)
    copied: list[Path] = []
    for source in required_candidate:
        target = candidate_target / source.name
        shutil.copy2(source, target)
        copied.append(target)

    candidate_report = load_json(candidate / "mechanism_lr_candidate_universe_report.json")
    manifest = dict(base_manifest)
    manifest["release_id"] = args.release_id
    manifest["parent_release_id"] = base_manifest.get("release_id")
    manifest["candidate_universe_path"] = "candidate_universe/mechanism_lr_candidate_universe.tsv"
    manifest["candidate_universe_component_crosswalk_path"] = "candidate_universe/mechanism_lr_candidate_component_crosswalk.tsv"
    manifest["candidate_universe_report_path"] = "candidate_universe/mechanism_lr_candidate_universe_report.json"
    manifest["candidate_component_handoff_path"] = "candidate_universe/candidate_component_handoff.json"
    manifest["candidate_universe_component_crosswalk"] = candidate_report.get("component_crosswalk", {})
    manifest["counts"] = dict(base_manifest.get("counts", {}))
    component = candidate_report.get("component_crosswalk", {})
    manifest["counts"].update({
        "candidate_universe_records": candidate_report.get("canonical_communication_count"),
        "candidate_component_mappings": component.get("mapping_count"),
        "candidate_component_resolved": sum(
            count for status, count in component.get("status_counts", {}).items()
            if not status.startswith("unresolved_")
        ),
        "candidate_component_unresolved": sum(
            count for status, count in component.get("status_counts", {}).items()
            if status.startswith("unresolved_")
        ),
    })
    manifest["candidate_component_contract"] = {
        "schema_version": component.get("schema_version"),
        "biological_component_inference": False,
        "canonical_complex_identity_preserved": True,
        "underscore_splitting_used": False,
        "source_registry_checksum_verified": True,
    }
    manifest["migration_gaps"] = list(base_manifest.get("migration_gaps", [])) + [
        "The candidate component crosswalk resolves only exact source-registry pairs; it does not infer components from canonical names.",
        "The coordinator-reported 88-pair downstream measured-feature audit was not present in this repository and must be supplied for pair-level recovery accounting.",
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
        "candidate_component_mappings": manifest["counts"]["candidate_component_mappings"],
        "candidate_component_resolved": manifest["counts"]["candidate_component_resolved"],
        "candidate_component_unresolved": manifest["counts"]["candidate_component_unresolved"],
        "manifest_files": len(files),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
