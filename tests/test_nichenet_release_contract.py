import json
from pathlib import Path

import pytest

from scripts.nichenet_release_contract import (
    CONTRACT_RELATIVE,
    build_contract,
    validate_contract,
)


def _write(path: Path, text: str | bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(text, bytes):
        path.write_bytes(text)
    else:
        path.write_text(text, encoding="utf-8")


def _fixture(tmp_path: Path) -> tuple[Path, Path, Path]:
    method = tmp_path / "method"
    bundle = tmp_path / "bundle"
    companion = tmp_path / "companion"
    neutral_dir = method / "method_native/nichenet_neutral_v1"
    release_neutral_dir = bundle / "method_resources/method_native/nichenet_neutral_v1"
    artifact_dir = companion / "nichenet_neutral_v1"
    matrix = bytes(range(48))
    _write(artifact_dir / "ligand_target_matrix.f64le.bin", matrix)
    axes = {
        "target_genes.tsv": "target_id\nt1\nt2\n",
        "ligands.tsv": "ligand_id\nl1\nl2\nl3\n",
    }
    for name, content in axes.items():
        _write(neutral_dir / name, content)
        _write(release_neutral_dir / name, content)
    _write(neutral_dir / "lr_network.tsv", "from\tto\ndb\tr1\n")
    _write(bundle / "method_resources/method_native/nichenet_neutral_v1/lr_network.tsv", "from\tto\ndb\tr1\n")
    neutral = {
        "source_model": "NicheNet v2 mouse",
        "matrix_sha256": __import__("hashlib").sha256(matrix).hexdigest(),
        "matrix_shape": [2, 3],
        "matrix_dtype": "float64",
        "matrix_endianness": "little",
        "matrix_layout": "column_major",
        "lr_network_row_count": 1,
    }
    _write(neutral_dir / "neutral_model_manifest.json", json.dumps(neutral))
    _write(release_neutral_dir / "neutral_model_manifest.json", json.dumps(neutral))
    _write(
        method / "method_resource_numeric_artifacts.tsv",
        "resource_key\tartifact_key\tartifact_kind\tstorage_path\tstorage_status\tartifact_sha256\tbyte_size\tdtype\tendianness\tlayout\tshape_json\taxis_artifacts_json\tsource_model_version\trelease_contract_status\trelease_relative_path\tnotes\n"
        "resource\tnichenet_neutral_v1_ligand_target_matrix\tligand_target_prior_matrix\tref\tsource_reference_only\t"
        + neutral["matrix_sha256"]
        + "\t48\tfloat64\tlittle\tcolumn_major\t[2,3]\t[]\tNicheNet v2 mouse\tcompanion_required\tpath\tnotes\n",
    )
    _write(
        bundle / "mechanism_graph/mechanism_output_bridges_validated.tsv",
        "bridge_id\tsource_label\toutput_label\toutput_product_labels\tvalidation_status\tcausal_status\ttraversal_status\n"
        "b1\tL1\tO1\tO1\tvalidated_primary_output\tbounded_output_only\tconditional_product_continuation\n",
    )
    return method, bundle, companion


def _write_contract(bundle: Path, payload: dict) -> None:
    path = bundle / CONTRACT_RELATIVE
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")


def test_nichenet_contract_round_trip_is_complete_and_companion_pinned(tmp_path):
    method, bundle, companion = _fixture(tmp_path)
    payload = build_contract(method_dir=method, bundle=bundle, companion_artifact_root=companion)
    _write_contract(bundle, payload)
    summary = validate_contract(bundle=bundle, companion_artifact_root=companion)
    assert summary["matrix_shape"] == [2, 3]
    assert summary["output_projection_rows"] == 1
    assert payload["matrix"]["selection"] == "complete_matrix"


def test_nichenet_contract_fails_closed_without_companion(tmp_path):
    method, bundle, companion = _fixture(tmp_path)
    payload = build_contract(method_dir=method, bundle=bundle, companion_artifact_root=companion)
    _write_contract(bundle, payload)
    with pytest.raises(ValueError, match="companion_artifact_root is required"):
        validate_contract(bundle=bundle, companion_artifact_root=None)


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda p: p["matrix"].update({"sha256": "0" * 64}), "checksum mismatch"),
        (lambda p: p["matrix"].update({"shape": [3, 3]}), "shape/byte-size"),
        (lambda p: p["matrix"].update({"layout": "row_major"}), "layout"),
        (lambda p: p["axes"].pop("target"), "target and ligand axes"),
        (lambda p: p["output_projection"].pop("release_path"), "output_projection"),
    ],
)
def test_nichenet_contract_rejects_incomplete_or_mismatched_references(tmp_path, mutation, message):
    method, bundle, companion = _fixture(tmp_path)
    payload = build_contract(method_dir=method, bundle=bundle, companion_artifact_root=companion)
    mutation(payload)
    _write_contract(bundle, payload)
    with pytest.raises(ValueError, match=message):
        validate_contract(bundle=bundle, companion_artifact_root=companion)


def test_nichenet_contract_rejects_missing_matrix_during_build(tmp_path):
    method, bundle, companion = _fixture(tmp_path)
    (companion / "nichenet_neutral_v1/ligand_target_matrix.f64le.bin").unlink()
    with pytest.raises(ValueError, match="missing NicheNet companion matrix"):
        build_contract(method_dir=method, bundle=bundle, companion_artifact_root=companion)
