import csv
import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "query_pathway.py"
SPEC = importlib.util.spec_from_file_location("query_pathway", SCRIPT)
assert SPEC and SPEC.loader
query_pathway = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(query_pathway)


def test_query_is_read_only_and_uses_parameterized_psql_variable():
    sql = query_pathway.QUERY_SQL.upper()
    assert query_pathway.QUERY_TERM_MARKER in query_pathway.QUERY_SQL
    for forbidden in ("INSERT ", "UPDATE ", "DELETE ", "ALTER ", "DROP "):
        assert forbidden not in sql
    assert "SIGNALINGEDGE" in sql
    assert "EVIDENCEOBSERVATIONDETAIL" in sql
    assert "NATIVE_FIELDS_JSON" in sql
    assert "METHODRESOURCERECORD" in sql


def test_query_term_sql_literal_escapes_quotes_without_wildcard_semantics():
    term = "IL'1B%"
    sql = query_pathway.QUERY_SQL.replace(
        query_pathway.QUERY_TERM_MARKER,
        "'" + term.replace("'", "''") + "'",
    )
    assert "'IL''1B%'" in sql
    assert query_pathway.QUERY_TERM_MARKER not in sql


def test_local_staging_scan_labels_rows_and_preserves_fields(tmp_path):
    path = tmp_path / "staging.tsv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["tf_symbol", "target_symbol", "decision"], delimiter="\t")
        writer.writeheader()
        writer.writerow({"tf_symbol": "SPI1", "target_symbol": "IL1B", "decision": "promote_to_22B"})
        writer.writerow({"tf_symbol": "RELA", "target_symbol": "TNF", "decision": "promote_to_22B"})

    result = query_pathway.scan_local_staging("il1b", 10, (path,))
    assert result["files"][0]["matched_rows"] == 1
    assert result["rows"][0]["staging_status"] == "staged_evidence_only"
    assert result["rows"][0]["canonical_mechanism_status"] == "not_materialized_by_this_query"
    assert result["rows"][0]["row"]["target_symbol"] == "IL1B"


def test_local_evidence_scan_is_separate_from_database_layers(tmp_path):
    path = tmp_path / "evidence.tsv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["reported_entity_name", "value"], delimiter="\t")
        writer.writeheader()
        writer.writerow({"reported_entity_name": "IL-1beta", "value": "increased"})

    result = query_pathway.scan_local_evidence("IL-1", 10, (path,))
    assert result["rows"][0]["source_layer"] == "local_import_snapshot"
    assert result["rows"][0]["row"]["reported_entity_name"] == "IL-1beta"


def test_local_staging_scan_reports_truncation(tmp_path):
    path = tmp_path / "staging.tsv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["target_symbol"], delimiter="\t")
        writer.writeheader()
        for _ in range(3):
            writer.writerow({"target_symbol": "IL1B"})

    result = query_pathway.scan_local_staging("IL1B", 2, (path,))
    assert len(result["rows"]) == 2
    assert result["files"][0]["matched_rows"] == 3
    assert result["files"][0]["truncated"] is True
