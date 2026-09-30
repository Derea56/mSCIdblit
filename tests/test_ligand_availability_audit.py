from __future__ import annotations

import csv
import json
from pathlib import Path

from scripts.audit_ligand_availability import build


ROOT = Path(__file__).parents[1]
RELEASE = ROOT / "data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion627"
LEDGER = ROOT / "work/cross_module_synthesis/canonical_evidence_review/module20_24_integrated_phase2_extractions.tsv"
PACK = ROOT / "context_packs/spinal_cord_injury"


def test_ligand_availability_audit_is_source_preserving(tmp_path):
    summary = build(RELEASE, LEDGER, PACK, tmp_path)

    assert summary["audit_version"] == "ligand_availability_audit_v1"
    assert summary["mechanism_release_id"] == "module20_24_mechanism_graph:2026-09-25-literature-expansion-627"
    assert summary["release_ligand_node_count"] > 0
    assert summary["ligand_evidence_associations"] > 0
    assert summary["counts_by"]["availability_evidence_state"]["not_reported_in_source_record"] > 0
    assert (tmp_path / "ligand_availability_audit.tsv").is_file()
    assert (tmp_path / "ligand_availability_audit.json").is_file()

    rows = list(csv.DictReader((tmp_path / "ligand_availability_audit.tsv").open(), delimiter="\t"))
    slit2 = next(row for row in rows if row["b_evidence_id"] == "M20B-EVID-001792")
    assert slit2["mechanism_node_id"] == "NODE10400"
    assert slit2["dependency_group"] == "M20B-EVID-001792|NODE10400"
    assert slit2["availability_class_candidate"] == "soluble"
    assert slit2["promotion_state"] == "audit_only_not_promoted"

    ada = next(row for row in rows if row["b_evidence_id"] == "M20B-EVID-002407")
    assert ada["availability_evidence_state"] != "source_reported_candidate"

    adam10 = next(row for row in rows if row["b_evidence_id"] == "M23B-EVID-000636")
    assert adam10["availability_evidence_state"] != "source_reported_candidate"


def test_ligand_availability_audit_records_exact_inputs(tmp_path):
    build(RELEASE, LEDGER, PACK, tmp_path)
    report = json.loads((tmp_path / "ligand_availability_audit.json").read_text())
    assert [item["path"] for item in report["input_artifacts"]] == [
        "data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion627/bundle_metadata.json",
        "data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion627/mechanism_nodes.tsv",
        "data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion627/mechanism_edges.tsv",
        "work/cross_module_synthesis/canonical_evidence_review/module20_24_integrated_phase2_extractions.tsv",
        "context_packs/spinal_cord_injury/observations.tsv",
    ]
