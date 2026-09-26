from __future__ import annotations

import csv
import json
from pathlib import Path

from scripts.validate_context_pack import validate_pack


ROOT = Path(__file__).parents[1]
PACK = ROOT / "context_packs" / "spinal_cord_injury"


def _header(path: Path) -> list[str]:
    with path.open(newline="") as handle:
        return next(csv.reader(handle, delimiter="\t"))


def test_sci_context_manifest_pins_neutral_mechanism_release():
    manifest = json.loads((PACK / "context_manifest.json").read_text())

    assert manifest["context_pack_id"] == "spinal_cord_injury"
    assert manifest["status"] == "scaffold"
    assert manifest["mechanism_dependency"]["generic_graph_is_unchanged"] is True
    assert manifest["mechanism_dependency"]["context_links_are_not_graph_edges"] is True
    assert manifest["evidence_policy"]["route_confidence_stored"] is False
    assert manifest["evidence_policy"]["numeric_modality_weights_stored"] is False
    bundle_path = PACK / manifest["mechanism_dependency"]["bundle_metadata"]
    assert bundle_path.resolve().is_file()
    assert manifest["counts"] == {
        "context_profiles": 1,
        "observations": 0,
        "mechanism_links": 0,
        "included_mechanism_links": 0,
    }


def test_sci_context_tables_have_stable_contract_headers():
    contexts = _header(PACK / "contexts.tsv")
    observations = _header(PACK / "observations.tsv")
    links = _header(PACK / "mechanism_links.tsv")

    assert contexts[:4] == [
        "context_id",
        "context_name",
        "context_kind",
        "disease_context",
    ]
    assert observations[:8] == [
        "observation_id",
        "context_id",
        "source_system",
        "source_database",
        "source_record_type",
        "source_record_key",
        "source_version",
        "modality",
    ]
    assert links[:8] == [
        "link_id",
        "observation_id",
        "mechanism_release_id",
        "mechanism_target_kind",
        "mechanism_target_key",
        "mechanism_route_id",
        "route_stage",
        "link_role",
    ]


def test_sci_context_scope_is_not_a_study_observation():
    rows = list(csv.DictReader((PACK / "contexts.tsv").open(), delimiter="\t"))

    assert len(rows) == 1
    assert rows[0]["context_kind"] == "ontology_scope"
    assert rows[0]["context_status"] == "defined"
    assert rows[0]["sample_id"] == ""


def test_sci_context_pack_validator_accepts_scaffold():
    summary = validate_pack(PACK)

    assert summary["pack_id"] == "spinal_cord_injury"
    assert summary["counts"]["observations"] == 0
    assert summary["counts"]["mechanism_links"] == 0
