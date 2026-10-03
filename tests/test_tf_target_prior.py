from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts.tf_target_prior_contract import (
    DIRECT_GRAPH_TIER,
    PRIOR_MANIFEST,
    PRIOR_TABLE,
    SOURCE_RECORDS,
    SOURCE_REGISTRY,
    TARGET_AXIS,
    TF_AXIS,
    TFTargetPriorError,
    aggregate_pairs,
    sha256,
    validate_prior_manifest,
    write_tsv,
)
from scripts.validate_mscs_tf_target_release import validate_release_identity


def _source_row(record_id: str, effect: str, *, tf: str = "Trp53", target: str = "Cdkn1a") -> dict[str, str]:
    return {
        "source_registry": "TRRUST",
        "species_scope": "mouse",
        "source_version": "TRRUST_v2_test",
        "source_record_id": record_id,
        "normalized_tf_symbol": tf,
        "normalized_target_symbol": target,
        "effect_polarity": effect,
        "relationship_class": "transcriptional_regulation",
        "evidence_basis": "manual_curation",
        "reference_pmids": "12345678",
        "source_locator": "https://example.org/trrust.mouse.tsv#" + record_id,
        "raw_record_sha256": record_id * 64,
    }


def test_unsigned_and_signed_source_effects_are_preserved_without_inference():
    unsigned = aggregate_pairs([_source_row("u", "unknown", tf="Stat3", target="Socs3")])[0]
    signed = aggregate_pairs([_source_row("s1", "activating_target"), _source_row("s2", "unknown")])[0]
    assert unsigned["effect_polarity"] == "unknown"
    assert unsigned["effect_resolution"] == "unknown_only"
    assert signed["effect_polarity"] == "activating_target"
    assert signed["effect_resolution"] == "consistent_signed_sources_with_unknowns"


def test_duplicate_pairs_and_conflicting_signs_resolve_deterministically():
    rows = aggregate_pairs([
        _source_row("a", "activating_target"),
        _source_row("b", "repressing_target"),
    ])
    assert len(rows) == 1
    assert rows[0]["source_record_count"] == "2"
    assert rows[0]["effect_polarity"] == "unknown"
    assert rows[0]["effect_resolution"] == "conflicting_signed_sources"


def _minimal_release(tmp_path: Path) -> Path:
    root = tmp_path / "release"
    rows = aggregate_pairs([_source_row("a", "activating_target")])
    source_rows = [_source_row("a", "activating_target")]
    write_tsv(root / SOURCE_RECORDS, list(source_rows[0]), source_rows)
    write_tsv(root / PRIOR_TABLE, list(rows[0]), rows)
    write_tsv(root / TF_AXIS, ["tf_id", "tf_symbol", "species", "identifier_namespace"], [{
        "tf_id": rows[0]["tf_id"], "tf_symbol": "Trp53", "species": "mouse", "identifier_namespace": "mouse_gene_symbol"
    }])
    write_tsv(root / TARGET_AXIS, ["target_id", "target_symbol", "species", "identifier_namespace"], [{
        "target_id": rows[0]["target_id"], "target_symbol": "Cdkn1a", "species": "mouse", "identifier_namespace": "mouse_gene_symbol"
    }])
    write_tsv(root / DIRECT_GRAPH_TIER, ["tier", "edge_id"], [{"tier": "direct_graph_evidence", "edge_id": "edge-1"}])
    write_tsv(root / SOURCE_REGISTRY, ["source_registry", "license_name"], [{
        "source_registry": "TRRUST", "license_name": "CC BY-SA 4.0"
    }])
    files = {}
    for relative in (SOURCE_RECORDS, PRIOR_TABLE, TF_AXIS, TARGET_AXIS, DIRECT_GRAPH_TIER, SOURCE_REGISTRY):
        path = root / relative
        files[relative.as_posix()] = {"sha256": sha256(path), "bytes": path.stat().st_size}
    manifest = {
        "schema_version": "tf_target_prior_v1",
        "species": "mouse",
        "response_selection": "none",
        "weights": {"status": "not_supplied"},
        "ranks": {"status": "not_supplied"},
        "source": {"license_name": "CC BY-SA 4.0"},
        "counts": {"source_record_count": 1, "pair_count": 1, "tf_count": 1, "target_count": 1, "direct_graph_edge_count": 1},
        "files": files,
    }
    (root / PRIOR_MANIFEST).write_text(json.dumps(manifest), encoding="utf-8")
    return root


def test_prior_validator_rejects_corrupt_hash_axis_and_numeric_weight(tmp_path):
    root = _minimal_release(tmp_path)
    assert validate_prior_manifest(root)["pair_count"] == 1

    manifest_path = root / PRIOR_MANIFEST
    manifest = json.loads(manifest_path.read_text())
    manifest["files"][PRIOR_TABLE.as_posix()]["sha256"] = "0" * 64
    manifest_path.write_text(json.dumps(manifest))
    with pytest.raises(TFTargetPriorError, match="checksum/size mismatch"):
        validate_prior_manifest(root)

    root = _minimal_release(tmp_path / "axis")
    (root / TARGET_AXIS).write_text((root / TARGET_AXIS).read_text() + "mouse_gene_symbol:Cdkn1a\tCdkn1a\tmouse\tmouse_gene_symbol\n")
    manifest = json.loads((root / PRIOR_MANIFEST).read_text())
    manifest["files"][TARGET_AXIS.as_posix()] = {
        "sha256": sha256(root / TARGET_AXIS), "bytes": (root / TARGET_AXIS).stat().st_size
    }
    manifest["counts"]["target_count"] = 2
    (root / PRIOR_MANIFEST).write_text(json.dumps(manifest))
    with pytest.raises(TFTargetPriorError, match="target axis contains empty or duplicate IDs"):
        validate_prior_manifest(root)

    root = _minimal_release(tmp_path / "weight")
    lines = (root / PRIOR_TABLE).read_text().splitlines()
    header = lines[0].split("\t")
    values = lines[1].split("\t")
    values[header.index("association_weight")] = "nan"
    (root / PRIOR_TABLE).write_text("\n".join([lines[0], "\t".join(values)]) + "\n")
    manifest = json.loads((root / PRIOR_MANIFEST).read_text())
    manifest["files"][PRIOR_TABLE.as_posix()] = {
        "sha256": sha256(root / PRIOR_TABLE), "bytes": (root / PRIOR_TABLE).stat().st_size
    }
    (root / PRIOR_MANIFEST).write_text(json.dumps(manifest))
    with pytest.raises(TFTargetPriorError, match="invented numeric values"):
        validate_prior_manifest(root)


def test_additive_release_identity_requires_distinct_parent_and_preservation():
    manifest = {
        "schema_version": "mscs_release_bundle_v1",
        "nichenet_ligand_target_prior_manifest": "method_resources/nichenet_ligand_target_prior_manifest.json",
        "tf_target_prior_manifest": "tf_target_prior/tf_target_prior_manifest.json",
        "candidate_universe_component_crosswalk_path": "candidate_universe/mechanism_lr_candidate_component_crosswalk.tsv",
        "candidate_component_handoff_path": "candidate_universe/candidate_component_handoff.json",
        "release_id": "child",
        "parent_release_id": "parent",
        "original_mscs_resources_preserved": True,
    }
    validate_release_identity(manifest)
    manifest["parent_release_id"] = "child"
    with pytest.raises(SystemExit, match="distinct parent release"):
        validate_release_identity(manifest)
