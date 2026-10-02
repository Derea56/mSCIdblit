import csv
import gzip
import json
from pathlib import Path

import pytest

from scripts.build_gene_identifier_crosswalk import parse_gene_info
from scripts.validate_mscs_gene_identifier_release import validate_gene_crosswalk_artifact


ROOT = Path(__file__).resolve().parents[1]
CROSSWALK = ROOT / "data/processed/gene_identifier_crosswalk_ncbi_2026_10_02_v2"


def _gene_info_row(tax_id, gene_id, symbol, synonyms, dbxrefs):
    return [
        tax_id, gene_id, symbol, synonyms, dbxrefs, "1", "", "description", "protein-coding",
        symbol, symbol, "", "", "20261002",
    ]


def test_gene_info_parser_preserves_exact_casefolded_aliases(tmp_path):
    path = tmp_path / "Mus_musculus.gene_info.gz"
    fields = [
        "tax_id", "GeneID", "Symbol", "Synonyms", "dbXrefs", "chromosome", "map_location",
        "description", "type_of_gene", "Symbol_from_nomenclature_authority",
        "Full_name_from_nomenclature_authority", "Nomenclature_status", "Other_designations",
        "Modification_date",
    ]
    with gzip.open(path, "wt", newline="", encoding="utf-8") as handle:
        handle.write("#" + "\t".join(fields) + "\n")
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(_gene_info_row("10090", "1", "Tnf", "TNF|tumor necrosis factor", "Ensembl:ENSMUSG00000000001"))
        writer.writerow(_gene_info_row("10090", "2", "Other", "Shared", ""))
        writer.writerow(_gene_info_row("10090", "3", "Third", "Shared", ""))

    rows, lookup = parse_gene_info(path, "mouse")
    assert rows[0]["canonical_symbol"] == "Tnf"
    assert lookup["tnf"][0]["entrez_gene_id"] == "1"
    assert {row["entrez_gene_id"] for row in lookup["shared"]} == {"2", "3"}
    assert rows[0]["ensembl_gene_id"] == "ENSMUSG00000000001"


def test_real_ncbi_crosswalk_validates_and_keeps_species_explicit():
    summary = validate_gene_crosswalk_artifact(CROSSWALK)
    assert summary == {
        "mouse_catalog_records": 112258,
        "human_catalog_records": 193873,
        "crosswalk_rows": 48693,
        "crosswalk_resolved_rows": 24733,
        "crosswalk_ambiguous_rows": 2800,
        "crosswalk_unresolved_rows": 1821,
        "crosswalk_orthology_rows": 19339,
        "orthology_rows": 17095,
    }
    with (CROSSWALK / "gene_crosswalk.tsv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    tnf = [row for row in rows if row["query_symbol"] == "Tnf" and row["query_species_scope"] == "mouse"]
    assert {(row["species"], row["mapping_status"], row["canonical_symbol"]) for row in tnf} >= {
        ("mouse", "resolved_source_canonical", "Tnf"),
    }
    unscoped_tnf = [row for row in rows if row["query_symbol"] == "TNF" and row["query_species_scope"] == "unscoped"]
    assert {row["species"] for row in unscoped_tnf} == {"mouse", "human"}
    with (CROSSWALK / "gene_label_coverage_audit.tsv").open(newline="", encoding="utf-8") as handle:
        audit = list(csv.DictReader(handle, delimiter="\t"))
    for label in ("AQP4", "BDNF", "CXCL2"):
        rows_for_label = [row for row in audit if row["label"] == label and row["label_kind"] == "validated_output_product_label"]
        assert rows_for_label
        assert all(row["mouse_mapping_status"] == "uniquely_mapped_source_gene" for row in rows_for_label)
    assert any(row["label_kind"] == "validated_output_product_label" and row["mouse_mapping_status"] == "unresolved_source_symbol" for row in audit)


def test_crosswalk_validator_rejects_checksum_drift(tmp_path):
    for name in ("gene_catalog.tsv", "gene_crosswalk.tsv", "gene_orthology.tsv", "gene_label_coverage_audit.tsv"):
        source = CROSSWALK / name
        target = tmp_path / name
        target.write_bytes(source.read_bytes())
    manifest = json.loads((CROSSWALK / "gene_identifier_crosswalk_manifest.json").read_text(encoding="utf-8"))
    (tmp_path / "gene_identifier_crosswalk_manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    (tmp_path / "gene_crosswalk.tsv").write_text(
        (tmp_path / "gene_crosswalk.tsv").read_text(encoding="utf-8") + "\n", encoding="utf-8"
    )
    with pytest.raises(ValueError, match="checksum/size mismatch"):
        validate_gene_crosswalk_artifact(tmp_path)
