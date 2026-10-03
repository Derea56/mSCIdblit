from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import pytest

from scripts.build_mechanism_lr_candidate_universe import (
    component_index,
    load_master_component_registry,
    validate_registry_component_row,
)
from scripts.validate_mscs_tf_target_release import validate_component_crosswalk


def registry_row(**updates: str) -> dict[str, str]:
    row = {
        "registry_id": "LRREG_TEST",
        "ligand": "Il6",
        "receptor": "Il6st_Lifr",
        "ligand_entity_type": "gene",
        "receptor_entity_type": "complex",
        "ligand_components": "Il6",
        "receptor_components": "Il6st|Lifr",
        "source_methods": "liana",
        "source_resources": "mouseconsensus",
        "source_record_ids": "row:1",
        "source_databases": "",
        "evidence_notes": "",
    }
    row.update(updates)
    return row


def test_explicit_complex_and_single_gene_mappings_are_distinguished():
    assert validate_registry_component_row(registry_row()) == (
        "explicit_source_complex", "Il6", "Il6st|Lifr"
    )
    single = registry_row(
        receptor="Il6ra",
        receptor_entity_type="gene",
        receptor_components="Il6ra",
    )
    assert validate_registry_component_row(single) == (
        "single_gene_identity", "Il6", "Il6ra"
    )


@pytest.mark.parametrize(
    "updates, expected",
    [
        ({"receptor_components": "Il6st|Il6st"}, "unresolved_duplicate_source_components"),
        ({"receptor_entity_type": "gene"}, "unresolved_entity_type_component_mismatch"),
        ({"receptor_components": ""}, "unresolved_missing_or_invalid_source_components"),
    ],
)
def test_malformed_source_mappings_remain_unresolved(updates, expected):
    status, ligand, receptor = validate_registry_component_row(registry_row(**updates))
    assert status == expected
    assert ligand == ""
    assert receptor == ""


def test_duplicate_component_rows_are_deduplicated_for_candidate_fields():
    indexed = component_index([
        {"canonical_communication_id": "PAIR1", "side": "receptor", "component_name": "Lifr", "component_ordinal": "2"},
        {"canonical_communication_id": "PAIR1", "side": "receptor", "component_name": "Il6st", "component_ordinal": "1"},
        {"canonical_communication_id": "PAIR1", "side": "receptor", "component_name": "Lifr", "component_ordinal": "2"},
    ])
    assert indexed["PAIR1"]["receptor"] == [(1, "Il6st"), (2, "Lifr")]


def test_ambiguous_registry_pair_fails_closed(tmp_path: Path):
    path = tmp_path / "master.tsv"
    fields = list(registry_row())
    rows = [registry_row(), registry_row(registry_id="LRREG_TEST_2", receptor_components="Lifr|Il6st")]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    with pytest.raises(ValueError, match="ambiguous duplicate pair"):
        load_master_component_registry(path)


def test_crosswalk_release_validation_checks_manifest_source_checksum(tmp_path: Path):
    (tmp_path / "candidate_universe").mkdir(parents=True)
    (tmp_path / "method_resources/method_native").mkdir(parents=True)
    source = tmp_path / "method_resources/method_native/master_lr_registry.tsv"
    source.write_text("ligand\treceptor\nIl6\tIl6st_Lifr\n", encoding="utf-8")
    source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    candidate = tmp_path / "candidate_universe/mechanism_lr_candidate_universe.tsv"
    candidate.write_text(
        "candidate_pair_id\tcomponent_mapping_id\tcomponent_mapping_status\tligand_components\treceptor_components\n"
        "P1\tCOMPONENTMAP:P1\texplicit_source_complex\tIl6\tIl6st|Lifr\n",
        encoding="utf-8",
    )
    crosswalk = tmp_path / "candidate_universe/mechanism_lr_candidate_component_crosswalk.tsv"
    crosswalk.write_text(
        "component_mapping_id\tcandidate_pair_id\tcomponent_mapping_status\tligand_components\treceptor_components\tsource_registry_sha256\n"
        f"COMPONENTMAP:P1\tP1\texplicit_source_complex\tIl6\tIl6st|Lifr\t{source_hash}\n",
        encoding="utf-8",
    )
    manifest = {
        "candidate_universe_path": "candidate_universe/mechanism_lr_candidate_universe.tsv",
        "candidate_universe_component_crosswalk_path": "candidate_universe/mechanism_lr_candidate_component_crosswalk.tsv",
    }
    assert validate_component_crosswalk(tmp_path, manifest) == {
        "candidate_count": 1, "crosswalk_count": 1, "resolved_count": 1, "unresolved_count": 0
    }
    source.write_text(source.read_text(encoding="utf-8") + "changed\n", encoding="utf-8")
    with pytest.raises(SystemExit, match="source-registry checksum"):
        validate_component_crosswalk(tmp_path, manifest)
