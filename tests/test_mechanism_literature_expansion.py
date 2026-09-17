from pathlib import Path

from scripts.build_mechanism_literature_expansion import read_input, validate_rows


def test_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch001.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_evidence_contract"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert sum(row["route_tier"] == "explicit_ligand_receptor_intracellular_tf_target" for row in rows) == 4
    assert sum(row["route_tier"] == "ligand_receptor_output_annotation_missing_intracellular_and_tf" for row in rows) == 1
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_second_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch002.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion001"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert sum(row["route_tier"] == "explicit_ligand_receptor_intracellular_tf_target" for row in rows) == 3
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_output_missing_tf" for row in rows) == 2
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_third_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch003.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion002"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_intracellular_output_missing_tf"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_fourth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch004.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion003"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_tf_output_missing_target_gene" for row in rows) == 1
    assert sum(row["route_tier"] == "ligand_receptor_output_annotation_missing_intracellular_and_tf" for row in rows) == 2
    assert all(row["causal_status"] == "not_asserted" for row in rows)
