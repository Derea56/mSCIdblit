import csv
import json
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


def test_fifth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch005.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion004"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert sum(row["route_tier"] == "explicit_ligand_receptor_intracellular_tf_target" for row in rows) == 1
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_tf_output_missing_target_gene" for row in rows) == 3
    assert sum(row["route_tier"] == "ligand_receptor_tf_output_annotation_missing_intracellular" for row in rows) == 1
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_sixth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch006.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion005"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_tf_output_missing_target_gene" for row in rows) == 1
    assert sum(row["route_tier"] == "ligand_receptor_tf_output_annotation_missing_intracellular" for row in rows) == 4
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_seventh_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch007.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion006"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_tf_output_missing_target_gene" for row in rows) == 2
    assert sum(row["route_tier"] == "ligand_receptor_tf_output_annotation_missing_intracellular" for row in rows) == 2
    assert sum(row["route_tier"] == "ligand_receptor_output_annotation_missing_intracellular_and_tf" for row in rows) == 1
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_eighth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch008.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion007"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert sum(row["route_tier"] == "explicit_ligand_receptor_intracellular_tf_target" for row in rows) == 2
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_output_missing_tf" for row in rows) == 2
    assert sum(row["route_tier"] == "ligand_receptor_output_annotation_missing_intracellular_and_tf" for row in rows) == 1
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_ninth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch009.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion008"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_tf_output_annotation_missing_intracellular"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_tenth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch010.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion009"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_tf_output_missing_target_gene" for row in rows) == 2
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_output_missing_tf" for row in rows) == 3
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_eleventh_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch011.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion010"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_intracellular_tf_output_missing_target_gene"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_twelfth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch012.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion011"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert sum(row["route_tier"] == "ligand_receptor_output_annotation_missing_intracellular_and_tf" for row in rows) == 4
    assert sum(row["route_tier"] == "ligand_receptor_tf_output_annotation_missing_intracellular" for row in rows) == 1
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_thirteenth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch013.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion012"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_output_missing_tf" for row in rows) == 4
    assert sum(row["route_tier"] == "ligand_receptor_output_annotation_missing_intracellular_and_tf" for row in rows) == 1
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_fourteenth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch014.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion013"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_intracellular_output_missing_tf"}
    assert all(row["intracellular_status"] == "source_supported" for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_fifteenth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch015.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion014"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_tf_output_annotation_missing_intracellular"}
    assert all(row["intracellular_status"] == "not_assayed" for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_sixteenth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch016.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion015"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_tf_output_annotation_missing_intracellular"}
    assert all(row["intracellular_status"] == "not_assayed" for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_seventeenth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch017.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion016"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_output_missing_tf" for row in rows) == 3
    assert sum(row["route_tier"] == "ligand_receptor_output_annotation_missing_intracellular_and_tf" for row in rows) == 2
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_eighteenth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch018.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion017"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_output_missing_tf" for row in rows) == 1
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_tf_output_missing_target_gene" for row in rows) == 1
    assert sum(row["route_tier"] == "ligand_receptor_tf_output_annotation_missing_intracellular" for row in rows) == 3
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_nineteenth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch019.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion018"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_output_missing_tf" for row in rows) == 2
    assert sum(row["route_tier"] == "ligand_receptor_output_annotation_missing_intracellular_and_tf" for row in rows) == 2
    assert sum(row["route_tier"] == "ligand_receptor_tf_output_annotation_missing_intracellular" for row in rows) == 1
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_twentieth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch020.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion019"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_tf_output_annotation_missing_intracellular"}
    assert all(row["intracellular_status"] == "not_assayed" for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_twenty_first_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch021.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion020"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_tf_output_annotation_missing_intracellular"}
    assert {row["source_scope"] for row in rows} == {"direct_edge"}
    assert all(row["intracellular_status"] == "not_assayed" for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_twenty_second_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch022.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion021"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_intracellular_output_missing_tf"}
    assert all(row["intracellular_status"] == "source_supported" for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_twenty_third_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch023.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion022"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_tf_output_missing_target_gene" for row in rows) == 3
    assert sum(row["route_tier"] == "ligand_receptor_tf_output_annotation_missing_intracellular" for row in rows) == 2
    assert sum(row["intracellular_status"] == "source_supported" for row in rows) == 3
    assert sum(row["intracellular_status"] == "not_assayed" for row in rows) == 2
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_twenty_fourth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch024.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion023"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_tf_output_annotation_missing_intracellular"}
    assert all(row["intracellular_status"] == "not_assayed" for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_twenty_fifth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch025.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion024"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert all(row["intracellular_status"] == "not_assayed" for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_twenty_sixth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch026.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion025"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 5
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_tf_output_missing_target_gene" for row in rows) == 1
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_output_missing_tf" for row in rows) == 4
    assert all(row["intracellular_status"] == "source_supported" for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_twenty_seventh_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch027.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion026"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 10
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert sum(row["route_tier"] == "explicit_ligand_receptor_intracellular_tf_target" for row in rows) == 5
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_tf_output_missing_target_gene" for row in rows) == 3
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_output_missing_tf" for row in rows) == 2
    assert all(row["intracellular_status"] == "source_supported" for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)


def test_twenty_eighth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch028.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion027"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_intracellular_output_missing_tf"}
    assert all(row["intracellular_status"] == "source_supported" for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)


def test_twenty_ninth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch029.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion028"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_intracellular_output_missing_tf"}
    assert all(row["intracellular_status"] == "source_supported" for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)


def test_thirtieth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch030.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion029"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_tf_output_annotation_missing_intracellular"}
    assert all(row["intracellular_status"] == "not_assayed" for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)


def test_thirty_first_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch031.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion030"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_intracellular_output_missing_tf"}
    assert all(row["intracellular_status"] == "source_supported" for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)


def test_thirty_second_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch032.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion031"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_intracellular_output_missing_tf"}
    assert all(row["intracellular_status"] == "source_supported" for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)


def test_thirty_third_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch033.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion032"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_intracellular_output_missing_tf"}
    assert all(row["intracellular_status"] == "source_supported" for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)


def test_thirty_fourth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch034.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion033"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_output_missing_tf" for row in rows) == 6
    assert sum(row["route_tier"] == "ligand_receptor_output_annotation_missing_intracellular_and_tf" for row in rows) == 2
    assert sum(row["intracellular_status"] == "source_supported" for row in rows) == 6
    assert sum(row["intracellular_status"] == "not_assayed" for row in rows) == 2
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)


def test_thirty_fifth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch035.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion034"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)


def test_thirty_sixth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch036.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion035"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)


def test_thirty_seventh_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch037.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion036"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)


def test_thirty_eighth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch038.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion037"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)


def test_thirty_ninth_primary_literature_expansion_batch_is_bounded_and_validated():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch039.json"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion038"
    rows = read_input(input_path)
    validate_rows(rows, bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)


def test_fortieth_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch040.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion039"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion040"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16291
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 244
    assert {row["source_chain_id"] for row in route_rows[-8:]} == {row["expansion_id"] for row in rows}


def test_forty_first_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch041.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion040"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion041"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16299
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 252
    assert {row["source_chain_id"] for row in route_rows[-8:]} == {row["expansion_id"] for row in rows}


def test_forty_second_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch042.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion041"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion042"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16307
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 260
    assert {row["source_chain_id"] for row in route_rows[-8:]} == {row["expansion_id"] for row in rows}


def test_forty_third_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch043.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion042"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion043"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16315
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 268
    assert {row["source_chain_id"] for row in route_rows[-8:]} == {row["expansion_id"] for row in rows}


def test_forty_fourth_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch044.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion043"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion044"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16323
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 276
    assert {row["source_chain_id"] for row in route_rows[-8:]} == {row["expansion_id"] for row in rows}


def test_forty_fifth_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch045.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion044"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion045"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16331
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 284
    assert {row["source_chain_id"] for row in route_rows[-8:]} == {row["expansion_id"] for row in rows}


def test_forty_sixth_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch046.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion045"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion046"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16339
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 292
    assert {row["source_chain_id"] for row in route_rows[-8:]} == {row["expansion_id"] for row in rows}


def test_forty_seventh_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch047.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion046"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion047"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16347
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 300
    assert {row["source_chain_id"] for row in route_rows[-8:]} == {row["expansion_id"] for row in rows}


def test_forty_eighth_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch048.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion047"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion048"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16355
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 308
    assert {row["source_chain_id"] for row in route_rows[-8:]} == {row["expansion_id"] for row in rows}


def test_forty_ninth_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch049.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion048"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion049"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16363
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 316
    assert {row["source_chain_id"] for row in route_rows[-8:]} == {row["expansion_id"] for row in rows}


def test_fiftieth_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch050.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion049"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion050"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16371
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 324
    assert {row["source_chain_id"] for row in route_rows[-8:]} == {row["expansion_id"] for row in rows}


def test_fifty_first_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch051.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion050"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion051"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16379
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 332
    assert {row["source_chain_id"] for row in route_rows[-8:]} == {row["expansion_id"] for row in rows}


def test_fifty_second_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch052.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion051"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion052"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 8
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16387
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 340
    assert {row["source_chain_id"] for row in route_rows[-8:]} == {row["expansion_id"] for row in rows}


def test_fifty_third_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch053.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion052"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion053"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 2
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16389
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 342
    assert {row["source_chain_id"] for row in route_rows[-2:]} == {row["expansion_id"] for row in rows}


def test_fifty_fourth_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch054.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion053"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion054"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16399
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 352
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_fifty_fifth_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch055.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion054"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion055"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 7
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16406
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 359
    assert {row["source_chain_id"] for row in route_rows[-7:]} == {row["expansion_id"] for row in rows}


def test_fifty_sixth_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch056.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion055"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion056"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 7
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16413
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 366
    assert {row["source_chain_id"] for row in route_rows[-7:]} == {row["expansion_id"] for row in rows}


def test_fifty_seventh_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch057.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion056"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion057"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 7
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16420
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 373
    assert {row["source_chain_id"] for row in route_rows[-7:]} == {row["expansion_id"] for row in rows}


def test_fifty_eighth_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch058.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion057"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion058"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 7
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16427
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 380
    assert {row["source_chain_id"] for row in route_rows[-7:]} == {row["expansion_id"] for row in rows}


def test_fifty_ninth_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch059.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion058"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion059"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 7
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16434
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 387
    assert {row["source_chain_id"] for row in route_rows[-7:]} == {row["expansion_id"] for row in rows}


def test_sixtieth_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch060.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion059"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion060"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 7
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16441
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 394
    assert {row["source_chain_id"] for row in route_rows[-7:]} == {row["expansion_id"] for row in rows}


def test_sixty_first_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch061.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion060"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion061"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 6
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16447
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 400
    assert {row["source_chain_id"] for row in route_rows[-6:]} == {row["expansion_id"] for row in rows}


def test_sixty_second_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch062.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion061"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion062"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 3
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16450
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 403
    assert {row["source_chain_id"] for row in route_rows[-3:]} == {row["expansion_id"] for row in rows}


def test_sixty_third_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch063.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion062"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion063"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 6
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16456
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 409
    assert {row["source_chain_id"] for row in route_rows[-6:]} == {row["expansion_id"] for row in rows}


def test_sixty_fourth_primary_literature_expansion_batch_preserves_overlay_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch064.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion063"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion064"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 6
    assert {row["curation_status"] for row in rows} == {"curated_primary_route"}
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_output_annotation_missing_intracellular_and_tf"}
    assert {row["intracellular_status"] for row in rows} == {"not_assayed"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert len({row["source_queue_id"] for row in rows}) == len(rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16462
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 415
    assert {row["source_chain_id"] for row in route_rows[-6:]} == {row["expansion_id"] for row in rows}


def test_sixty_fifth_primary_literature_expansion_batch_preserves_tf_output_route_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch065.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion064"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion065"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 1
    row = rows[0]
    assert row["source_queue_id"] == "M21B-DOWNSTREAM:02133"
    assert row["route_tier"] == "ligand_receptor_tf_output_annotation_missing_intracellular"
    assert row["known_layers"] == "ligand|receptor|transcription_factor|cellular_functional_readout"
    assert row["missing_layers"] == "intracellular_continuation|target_gene_expression"
    assert row["ligand_receptor_edge_id"] == "M21B-E007015"
    assert row["transcription_factor_node_id"] == "NODE10409"
    assert row["transcription_factor_label"] == "SMAD1/5/8"
    assert row["intracellular_status"] == "not_assayed"
    assert row["causal_status"] == "not_asserted"
    assert row["curation_status"] == "curated_primary_route"
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert row["source_queue_id"] not in prior_queue_ids

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16463
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 416
    assert {row["source_chain_id"] for row in route_rows[-1:]} == {row["expansion_id"] for row in rows}


def test_sixty_sixth_primary_literature_expansion_batch_preserves_selectin_dr3_tf_output_route_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch066.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion065"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion066"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 1
    row = rows[0]
    assert row["source_queue_id"] == "M21B-DOWNSTREAM:00093"
    assert row["route_tier"] == "ligand_receptor_tf_output_annotation_missing_intracellular"
    assert row["known_layers"] == "ligand|receptor|transcription_factor|cellular_functional_readout"
    assert row["missing_layers"] == "intracellular_continuation|target_gene_expression"
    assert row["ligand_receptor_edge_id"] == "M21B-E000310"
    assert row["transcription_factor_node_id"] == "NODE07961"
    assert row["transcription_factor_label"] == "NF-kB"
    assert row["intracellular_status"] == "not_assayed"
    assert row["causal_status"] == "not_asserted"
    assert row["curation_status"] == "curated_primary_route"
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert row["source_queue_id"] not in prior_queue_ids

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16464
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 417
    assert {row["source_chain_id"] for row in route_rows[-1:]} == {row["expansion_id"] for row in rows}


def test_sixty_seventh_primary_literature_expansion_batch_preserves_chemokine_intracellular_routes_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch067.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion067"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion067"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 3
    assert {row["route_tier"] for row in rows} == {"ligand_receptor_intracellular_output_missing_tf"}
    assert {row["intracellular_status"] for row in rows} == {"source_supported"}
    assert {row["receptor_intracellular_edge_id"] for row in rows} == {"M21B-E003375", "M21B-E004414"}
    assert {row["intracellular_continuation_node_id"] for row in rows} == {"NODE04271", "NODE04284"}
    assert all(row["missing_layers"] == "transcription_factor|target_gene_expression" for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16467
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 420
    assert {row["source_chain_id"] for row in route_rows[-3:]} == {row["expansion_id"] for row in rows}


def test_sixty_eighth_primary_literature_expansion_batch_preserves_selective_ligand_receptor_intracellular_routes_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch068.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion067"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion068"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 3
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00553",
        "M21B-DOWNSTREAM:00567",
        "M21B-DOWNSTREAM:01761",
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows} == {
        "M21B-E003343",
        "M21B-E003315",
        "M21B-E004451",
    }
    assert {row["intracellular_continuation_node_id"] for row in rows} == {"NODE04271", "NODE04282"}
    assert all(row["route_tier"] == "ligand_receptor_intracellular_output_missing_tf" for row in rows)
    assert all(row["intracellular_status"] == "source_supported" for row in rows)
    assert all(row["missing_layers"] == "transcription_factor|target_gene_expression" for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    assert any("20-HETE" in row["limitations"] for row in rows if row["source_queue_id"] == "M21B-DOWNSTREAM:01761")
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16470
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 423
    assert {row["source_chain_id"] for row in route_rows[-3:]} == {row["expansion_id"] for row in rows}


def test_sixty_ninth_primary_literature_expansion_batch_preserves_selective_ligand_receptor_tf_routes_and_is_bounded():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch069.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion068"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion069"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 4
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00824",
        "M21B-DOWNSTREAM:00107",
        "M21B-DOWNSTREAM:00175",
        "M21B-DOWNSTREAM:00820",
    }
    assert {row["intracellular_tf_edge_id"] for row in rows} == {
        "M21B-E011529",
        "M21B-E001779",
        "M21B-E000551",
        "M21B-E000058",
    }
    assert {row["transcription_factor_node_id"] for row in rows} == {"NODE10693", "NODE10719"}
    assert all(row["route_tier"] == "ligand_receptor_tf_output_annotation_missing_intracellular" for row in rows)
    assert all(row["intracellular_status"] == "not_assayed" for row in rows)
    assert all(row["missing_layers"] == "intracellular_continuation|target_gene_expression" for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    assert all(row["source_scope"] == "composite_primary_evidence" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16474
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 427
    assert {row["source_chain_id"] for row in route_rows[-4:]} == {row["expansion_id"] for row in rows}


def test_seventieth_primary_literature_expansion_batch_preserves_partial_output_and_src_routes():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch070.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion069"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion070"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 6
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00038",
        "M21B-DOWNSTREAM:00039",
        "M21B-DOWNSTREAM:00047",
        "M21B-DOWNSTREAM:02090",
        "M21B-DOWNSTREAM:01662",
        "M21B-DOWNSTREAM:00385",
    }
    assert sum(row["route_tier"] == "ligand_receptor_output_annotation_missing_intracellular_and_tf" for row in rows) == 5
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_output_missing_tf" for row in rows) == 1
    assert {row["receptor_intracellular_edge_id"] for row in rows if row["receptor_intracellular_edge_id"]} == {"M21B-E002277"}
    assert {row["intracellular_continuation_node_id"] for row in rows if row["intracellular_continuation_node_id"]} == {"NODE10616"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16480
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 433
    assert {row["source_chain_id"] for row in route_rows[-6:]} == {row["expansion_id"] for row in rows}


def test_seventy_first_primary_literature_expansion_batch_preserves_receptor_proximal_and_tf_routes():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch071.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion070"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion071"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00053",
        "M21B-DOWNSTREAM:00556",
        "M21B-DOWNSTREAM:00560",
        "M21B-DOWNSTREAM:00565",
        "M21B-DOWNSTREAM:00649",
        "M21B-DOWNSTREAM:00809",
        "M21B-DOWNSTREAM:00812",
        "M21B-DOWNSTREAM:00822",
        "M21B-DOWNSTREAM:00312",
    }
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_output_missing_tf" for row in rows) == 8
    assert sum(row["route_tier"] == "ligand_receptor_tf_output_annotation_missing_intracellular" for row in rows) == 2
    assert {row["receptor_intracellular_edge_id"] for row in rows if row["receptor_intracellular_edge_id"]} == {
        "M21B-E000023",
        "M21B-E001484",
        "M21B-E001743",
        "M21B-E001809",
        "M21B-E001819",
        "M21B-E001843",
        "M21B-E001847",
        "M21B-E003376",
    }
    assert {row["intracellular_tf_edge_id"] for row in rows if row["intracellular_tf_edge_id"]} == {
        "M21B-E011536",
        "M21B-E011537",
    }
    assert {row["transcription_factor_node_id"] for row in rows if row["transcription_factor_node_id"]} == {
        "NODE10672",
        "NODE10692",
    }
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16490
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 443
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_seventy_second_primary_literature_expansion_batch_preserves_partial_routes():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch072.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion071"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion072"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00069",
        "M21B-DOWNSTREAM:00140",
        "M21B-DOWNSTREAM:00141",
        "M21B-DOWNSTREAM:00157",
        "M21B-DOWNSTREAM:00161",
        "M21B-DOWNSTREAM:00162",
        "M21B-DOWNSTREAM:00202",
        "M21B-DOWNSTREAM:00376",
        "M21B-DOWNSTREAM:02112",
        "M21B-DOWNSTREAM:02181",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf"
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows if row["receptor_intracellular_edge_id"]} == {
        "M21B-E001335",
        "M21B-E001791",
        "M21B-E001804",
        "M21B-E003315",
        "M21B-E003353",
        "M21B-E003375",
        "M21B-E003462",
        "M21B-E004414",
        "M21B-E004471",
    }
    assert not {row["intracellular_tf_edge_id"] for row in rows if row["intracellular_tf_edge_id"]}
    assert not {row["transcription_factor_node_id"] for row in rows if row["transcription_factor_node_id"]}
    assert {row["effect_polarity"] for row in rows if row["source_queue_id"] in {
        "M21B-DOWNSTREAM:00140",
        "M21B-DOWNSTREAM:00141",
    }} == {"inhibitory"}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16500
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 453
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_seventy_third_primary_literature_expansion_batch_preserves_receptor_proximal_routes():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch073.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion072"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion073"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00156",
        "M21B-DOWNSTREAM:00163",
        "M21B-DOWNSTREAM:00164",
        "M21B-DOWNSTREAM:00322",
        "M21B-DOWNSTREAM:00370",
        "M21B-DOWNSTREAM:00375",
        "M21B-DOWNSTREAM:00377",
        "M21B-DOWNSTREAM:00576",
        "M21B-DOWNSTREAM:00577",
        "M21B-DOWNSTREAM:00582",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf"
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows} == {
        "M21B-E001335",
        "M21B-E001746",
        "M21B-E001799",
        "M21B-E001855",
        "M21B-E002037",
        "M21B-E002040",
        "M21B-E002049",
        "M21B-E003816",
        "M21B-E004414",
        "M21B-E004471",
    }
    assert not {row["intracellular_tf_edge_id"] for row in rows if row["intracellular_tf_edge_id"]}
    assert not {row["transcription_factor_node_id"] for row in rows if row["transcription_factor_node_id"]}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16510
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 463
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_seventy_fourth_primary_literature_expansion_batch_preserves_gpcr_output_routes():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch074.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion073"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion074"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00571",
        "M21B-DOWNSTREAM:00575",
        "M21B-DOWNSTREAM:00589",
        "M21B-DOWNSTREAM:00591",
        "M21B-DOWNSTREAM:00607",
        "M21B-DOWNSTREAM:00635",
        "M21B-DOWNSTREAM:00636",
        "M21B-DOWNSTREAM:00640",
        "M21B-DOWNSTREAM:00701",
        "M21B-DOWNSTREAM:00709",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf"
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows} == {
        "M21B-E001816",
        "M21B-E001828",
        "M21B-E001829",
        "M21B-E001840",
        "M21B-E002039",
        "M21B-E002048",
        "M21B-E002051",
        "M21B-E003305",
        "M21B-E003353",
        "M21B-E004372",
    }
    assert not {row["intracellular_tf_edge_id"] for row in rows if row["intracellular_tf_edge_id"]}
    assert not {row["transcription_factor_node_id"] for row in rows if row["transcription_factor_node_id"]}
    assert {row["output_class"] for row in rows} == {
        "cellular_functional_readout",
        "second_messenger_readout",
    }
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16520
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 473
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_seventy_fifth_primary_literature_expansion_batch_preserves_endocrine_and_metabolite_gpcr_routes():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch075.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion074"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion075"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00599",
        "M21B-DOWNSTREAM:00600",
        "M21B-DOWNSTREAM:00601",
        "M21B-DOWNSTREAM:00602",
        "M21B-DOWNSTREAM:00604",
        "M21B-DOWNSTREAM:00626",
        "M21B-DOWNSTREAM:00628",
        "M21B-DOWNSTREAM:00653",
        "M21B-DOWNSTREAM:00655",
        "M21B-DOWNSTREAM:00661",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf"
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows} == {
        "M21B-E001831",
        "M21B-E001836",
        "M21B-E001888",
        "M21B-E001890",
        "M21B-E001891",
        "M21B-E001893",
        "M21B-E002042",
        "M21B-E003311",
        "M21B-E003350",
        "M21B-E003352",
    }
    assert not {row["intracellular_tf_edge_id"] for row in rows if row["intracellular_tf_edge_id"]}
    assert not {row["transcription_factor_node_id"] for row in rows if row["transcription_factor_node_id"]}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16530
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 483
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_seventy_sixth_primary_literature_expansion_batch_preserves_neuroendocrine_gpcr_routes():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch076.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion075"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion076"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00596",
        "M21B-DOWNSTREAM:00598",
        "M21B-DOWNSTREAM:00603",
        "M21B-DOWNSTREAM:00608",
        "M21B-DOWNSTREAM:00609",
        "M21B-DOWNSTREAM:00610",
        "M21B-DOWNSTREAM:00611",
        "M21B-DOWNSTREAM:00612",
        "M21B-DOWNSTREAM:00620",
        "M21B-DOWNSTREAM:00623",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf"
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows} == {
        "M21B-E001879",
        "M21B-E001881",
        "M21B-E004394",
        "M21B-E003339",
        "M21B-E003347",
        "M21B-E003348",
        "M21B-E003359",
        "M21B-E003341",
        "M21B-E001886",
        "M21B-E001887",
    }
    assert not {row["intracellular_tf_edge_id"] for row in rows if row["intracellular_tf_edge_id"]}
    assert not {row["transcription_factor_node_id"] for row in rows if row["transcription_factor_node_id"]}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16540
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 493
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_seventy_seventh_primary_literature_expansion_batch_preserves_non_gpcr_receptor_adaptor_routes():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch077.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion076"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion077"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00193",
        "M21B-DOWNSTREAM:00217",
        "M21B-DOWNSTREAM:00218",
        "M21B-DOWNSTREAM:00291",
        "M21B-DOWNSTREAM:00305",
        "M21B-DOWNSTREAM:00310",
        "M21B-DOWNSTREAM:00373",
        "M21B-DOWNSTREAM:01132",
        "M21B-DOWNSTREAM:01158",
        "M21B-DOWNSTREAM:01233",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf"
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows} == {
        "M21B-E001126",
        "M21B-E001224",
        "M21B-E001375",
        "M21B-E001377",
        "M21B-E001789",
        "M21B-E001796",
        "M21B-E002647",
        "M21B-E003843",
        "M21B-E011548",
    }
    assert {row["output_class"] for row in rows} == {
        "cellular_functional_readout",
        "phagocytosis_or_engulfment",
        "phosphorylation_or_activation_readout",
        "reporter_readout",
        "secreted_protein_or_release",
    }
    assert not {row["intracellular_tf_edge_id"] for row in rows if row["intracellular_tf_edge_id"]}
    assert not {row["transcription_factor_node_id"] for row in rows if row["transcription_factor_node_id"]}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16550
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 503
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_seventy_eighth_primary_literature_expansion_batch_preserves_receptor_proximal_output_routes():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch078.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion077"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion078"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00618",
        "M21B-DOWNSTREAM:00619",
        "M21B-DOWNSTREAM:00810",
        "M21B-DOWNSTREAM:00821",
        "M21B-DOWNSTREAM:00827",
        "M21B-DOWNSTREAM:01656",
        "M21B-DOWNSTREAM:01677",
        "M21B-DOWNSTREAM:01872",
        "M21B-DOWNSTREAM:01883",
        "M21B-DOWNSTREAM:01990",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf"
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows} == {
        "M21B-E000065",
        "M21B-E001335",
        "M21B-E001490",
        "M21B-E001746",
        "M21B-E002060",
        "M21B-E002061",
        "M21B-E007911",
        "M21B-E011350",
    }
    assert {row["output_class"] for row in rows} == {
        "cellular_functional_readout",
        "gene_expression_or_transcription",
        "phosphorylation_or_activation_readout",
        "reporter_readout",
    }
    assert not {row["intracellular_tf_edge_id"] for row in rows if row["intracellular_tf_edge_id"]}
    assert not {row["transcription_factor_node_id"] for row in rows if row["transcription_factor_node_id"]}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16560
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 513
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_seventy_ninth_primary_literature_expansion_batch_preserves_gpcr_second_messenger_routes():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch079.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion078"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion079"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00557",
        "M21B-DOWNSTREAM:00561",
        "M21B-DOWNSTREAM:00590",
        "M21B-DOWNSTREAM:00592",
        "M21B-DOWNSTREAM:00593",
        "M21B-DOWNSTREAM:00597",
        "M21B-DOWNSTREAM:00605",
        "M21B-DOWNSTREAM:00606",
        "M21B-DOWNSTREAM:00629",
        "M21B-DOWNSTREAM:00643",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf"
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows} == {
        "M21B-E001844",
        "M21B-E001845",
        "M21B-E001849",
        "M21B-E001880",
        "M21B-E001889",
        "M21B-E001894",
        "M21B-E002043",
        "M21B-E003325",
        "M21B-E003327",
        "M21B-E003329",
    }
    assert {row["output_class"] for row in rows} == {"second_messenger_readout"}
    assert not {row["intracellular_tf_edge_id"] for row in rows if row["intracellular_tf_edge_id"]}
    assert not {row["transcription_factor_node_id"] for row in rows if row["transcription_factor_node_id"]}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16570
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 523
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_eightieth_primary_literature_expansion_batch_preserves_gpcr_second_messenger_routes():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch080.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion079"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion080"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00530",
        "M21B-DOWNSTREAM:00531",
        "M21B-DOWNSTREAM:00532",
        "M21B-DOWNSTREAM:00533",
        "M21B-DOWNSTREAM:00536",
        "M21B-DOWNSTREAM:00539",
        "M21B-DOWNSTREAM:00558",
        "M21B-DOWNSTREAM:00564",
        "M21B-DOWNSTREAM:00572",
        "M21B-DOWNSTREAM:00573",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf"
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows} == {
        "M21B-E001811",
        "M21B-E001814",
        "M21B-E001853",
        "M21B-E001854",
        "M21B-E001895",
        "M21B-E001896",
        "M21B-E001897",
        "M21B-E001901",
        "M21B-E002050",
        "M21B-E002052",
    }
    assert {row["output_class"] for row in rows} == {"second_messenger_readout"}
    assert not {row["intracellular_tf_edge_id"] for row in rows if row["intracellular_tf_edge_id"]}
    assert not {row["transcription_factor_node_id"] for row in rows if row["transcription_factor_node_id"]}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16580
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 533
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_eighty_first_primary_literature_expansion_batch_preserves_gpcr_second_messenger_routes():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch081.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion080"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion081"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00538",
        "M21B-DOWNSTREAM:00545",
        "M21B-DOWNSTREAM:00547",
        "M21B-DOWNSTREAM:00554",
        "M21B-DOWNSTREAM:00559",
        "M21B-DOWNSTREAM:00563",
        "M21B-DOWNSTREAM:00566",
        "M21B-DOWNSTREAM:00644",
        "M21B-DOWNSTREAM:00652",
        "M21B-DOWNSTREAM:00664",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf"
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows} == {
        "M21B-E001818",
        "M21B-E001846",
        "M21B-E001899",
        "M21B-E002053",
        "M21B-E003312",
        "M21B-E003345",
        "M21B-E003360",
        "M21B-E003364",
        "M21B-E003371",
        "M21B-E003963",
    }
    assert {row["output_class"] for row in rows} == {"second_messenger_readout"}
    assert {row["effect_polarity"] for row in rows} == {"activating", "inhibitory"}
    assert not {row["intracellular_tf_edge_id"] for row in rows if row["intracellular_tf_edge_id"]}
    assert not {row["transcription_factor_node_id"] for row in rows if row["transcription_factor_node_id"]}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16590
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 543
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_eighty_second_primary_literature_expansion_batch_preserves_gpcr_second_messenger_routes():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch082.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion081"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion082"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 11
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00673",
        "M21B-DOWNSTREAM:00681",
        "M21B-DOWNSTREAM:00682",
        "M21B-DOWNSTREAM:00683",
        "M21B-DOWNSTREAM:00684",
        "M21B-DOWNSTREAM:00697",
        "M21B-DOWNSTREAM:00704",
        "M21B-DOWNSTREAM:00711",
        "M21B-DOWNSTREAM:00712",
        "M21B-DOWNSTREAM:00785",
        "M21B-DOWNSTREAM:00786",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf"
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows} == {
        "M21B-E001812",
        "M21B-E001826",
        "M21B-E001875",
        "M21B-E001876",
        "M21B-E001900",
        "M21B-E003321",
        "M21B-E003330",
        "M21B-E003356",
        "M21B-E003367",
        "M21B-E003370",
        "M21B-E003945",
    }
    assert {row["output_class"] for row in rows} == {"second_messenger_readout"}
    assert {row["effect_polarity"] for row in rows} == {"activating", "inhibitory"}
    assert not {row["intracellular_tf_edge_id"] for row in rows if row["intracellular_tf_edge_id"]}
    assert not {row["transcription_factor_node_id"] for row in rows if row["transcription_factor_node_id"]}
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16601
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 554
    assert {row["source_chain_id"] for row in route_rows[-11:]} == {row["expansion_id"] for row in rows}


def test_eighty_third_primary_literature_expansion_batch_preserves_unique_gpcr_output_routes():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch083.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion082"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion083"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00670",
        "M21B-DOWNSTREAM:00672",
        "M21B-DOWNSTREAM:00674",
        "M21B-DOWNSTREAM:00675",
        "M21B-DOWNSTREAM:00680",
        "M21B-DOWNSTREAM:00695",
        "M21B-DOWNSTREAM:00696",
        "M21B-DOWNSTREAM:00698",
        "M21B-DOWNSTREAM:00699",
        "M21B-DOWNSTREAM:00700",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf",
        "ligand_receptor_output_annotation_missing_intracellular_and_tf",
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows if row["receptor_intracellular_edge_id"]} == {
        "M21B-E002051",
        "M21B-E001895",
        "M21B-E001896",
        "M21B-E003320",
        "M21B-E003328",
        "M21B-E003997",
    }
    assert {row["output_class"] for row in rows} == {"reporter_readout", "second_messenger_readout"}
    assert {row["effect_polarity"] for row in rows} == {"activating"}
    assert all(not row["intracellular_tf_edge_id"] for row in rows)
    assert all(not row["transcription_factor_node_id"] for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16611
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 564
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_eighty_fourth_primary_literature_expansion_batch_preserves_unique_gpcr_output_routes():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch084.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion083"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion084"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00702",
        "M21B-DOWNSTREAM:00703",
        "M21B-DOWNSTREAM:00705",
        "M21B-DOWNSTREAM:00706",
        "M21B-DOWNSTREAM:00707",
        "M21B-DOWNSTREAM:00708",
        "M21B-DOWNSTREAM:00710",
        "M21B-DOWNSTREAM:00713",
        "M21B-DOWNSTREAM:00714",
        "M21B-DOWNSTREAM:00715",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf",
        "ligand_receptor_output_annotation_missing_intracellular_and_tf",
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows if row["receptor_intracellular_edge_id"]} == {
        "M21B-E003333",
        "M21B-E003334",
        "M21B-E003362",
        "M21B-E003365",
        "M21B-E003921",
        "M21B-E003964",
        "M21B-E003982",
    }
    assert {row["output_class"] for row in rows} == {
        "phagocytosis_or_engulfment",
        "phosphorylation_or_activation_readout",
        "reporter_readout",
        "second_messenger_readout",
    }
    assert all(row["effect_polarity"] == "activating" for row in rows)
    assert all(not row["intracellular_tf_edge_id"] for row in rows)
    assert all(not row["transcription_factor_node_id"] for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16621
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 574
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_eighty_fifth_primary_literature_expansion_batch_preserves_unique_gpcr_output_routes():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch085.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion084"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion085"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00716",
        "M21B-DOWNSTREAM:00717",
        "M21B-DOWNSTREAM:00718",
        "M21B-DOWNSTREAM:00719",
        "M21B-DOWNSTREAM:00741",
        "M21B-DOWNSTREAM:00742",
        "M21B-DOWNSTREAM:00756",
        "M21B-DOWNSTREAM:00784",
        "M21B-DOWNSTREAM:00787",
        "M21B-DOWNSTREAM:00788",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf",
        "ligand_receptor_output_annotation_missing_intracellular_and_tf",
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows if row["receptor_intracellular_edge_id"]} == {
        "M21B-E001824",
        "M21B-E001838",
        "M21B-E001847",
        "M21B-E001857",
        "M21B-E003359",
        "M21B-E003373",
        "M21B-E003976",
    }
    assert {row["output_class"] for row in rows} == {
        "phosphorylation_or_activation_readout",
        "reporter_readout",
        "secreted_protein_or_release",
        "second_messenger_readout",
    }
    assert {row["effect_polarity"] for row in rows} == {"activating", "inhibitory"}
    assert all(not row["intracellular_tf_edge_id"] for row in rows)
    assert all(not row["transcription_factor_node_id"] for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16631
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 584
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_eighty_sixth_primary_literature_expansion_batch_preserves_unique_peptide_receptor_output_routes():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch086.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion085"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion086"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00789",
        "M21B-DOWNSTREAM:00790",
        "M21B-DOWNSTREAM:00791",
        "M21B-DOWNSTREAM:00792",
        "M21B-DOWNSTREAM:00793",
        "M21B-DOWNSTREAM:00794",
        "M21B-DOWNSTREAM:00800",
        "M21B-DOWNSTREAM:00801",
        "M21B-DOWNSTREAM:00804",
        "M21B-DOWNSTREAM:00805",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf",
        "ligand_receptor_output_annotation_missing_intracellular_and_tf",
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows if row["receptor_intracellular_edge_id"]} == {
        "M21B-E001820",
        "M21B-E003322",
        "M21B-E003359",
    }
    assert {row["output_class"] for row in rows} == {
        "phosphorylation_or_activation_readout",
        "second_messenger_readout",
    }
    assert {row["effect_polarity"] for row in rows} == {"activating"}
    assert all(not row["intracellular_tf_edge_id"] for row in rows)
    assert all(not row["transcription_factor_node_id"] for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16641
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 594
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_eighty_seventh_primary_literature_expansion_batch_preserves_intracellular_and_tf_routes():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch087.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion086"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion087"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00173",
        "M21B-DOWNSTREAM:00180",
        "M21B-DOWNSTREAM:00537",
        "M21B-DOWNSTREAM:00546",
        "M21B-DOWNSTREAM:00654",
        "M21B-DOWNSTREAM:00657",
        "M21B-DOWNSTREAM:00663",
        "M21B-DOWNSTREAM:02291",
        "M21B-DOWNSTREAM:02370",
        "M21B-DOWNSTREAM:02548",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf",
        "ligand_receptor_output_annotation_missing_intracellular_and_tf",
        "ligand_receptor_tf_output_annotation_missing_intracellular",
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows if row["receptor_intracellular_edge_id"]} == {
        "M21B-E001810",
        "M21B-E002053",
        "M21B-E003317",
        "M21B-E003349",
        "M21B-E003351",
    }
    assert {row["intracellular_tf_edge_id"] for row in rows if row["intracellular_tf_edge_id"]} == {
        "M21B-E001717",
        "M21B-E001781",
        "M21B-E011519",
    }
    assert all(not row["receptor_intracellular_edge_id"] for row in rows if row["route_tier"] == "ligand_receptor_tf_output_annotation_missing_intracellular")
    assert all(row["intracellular_status"] == "source_supported" for row in rows if row["route_tier"] == "ligand_receptor_intracellular_output_missing_tf")
    assert all(row["intracellular_status"] == "not_assayed" for row in rows if row["route_tier"] == "ligand_receptor_tf_output_annotation_missing_intracellular")
    assert {row["output_class"] for row in rows} == {
        "phosphorylation_or_activation_readout",
        "second_messenger_readout",
        "unknown",
    }
    assert {row["effect_polarity"] for row in rows} == {"activating"}
    assert all(not row["tf_target_edge_id"] for row in rows)
    assert all(not row["target_gene_node_id"] for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16651
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 604
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_eighty_eighth_primary_literature_expansion_batch_preserves_receptor_output_routes():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch088.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion087"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion088"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:02157",
        "M21B-DOWNSTREAM:02158",
        "M21B-DOWNSTREAM:02173",
        "M21B-DOWNSTREAM:02174",
        "M21B-DOWNSTREAM:02175",
        "M21B-DOWNSTREAM:02176",
        "M21B-DOWNSTREAM:02177",
        "M21B-DOWNSTREAM:02242",
        "M21B-DOWNSTREAM:02262",
        "M21B-DOWNSTREAM:02263",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf",
        "ligand_receptor_output_annotation_missing_intracellular_and_tf",
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows if row["receptor_intracellular_edge_id"]} == {
        "M21B-E004391",
        "M21B-E004409",
    }
    assert {row["output_class"] for row in rows} == {
        "cellular_functional_readout",
        "phosphorylation_or_activation_readout",
        "second_messenger_readout",
    }
    assert all(row["effect_polarity"] == "activating" for row in rows)
    assert all(not row["intracellular_tf_edge_id"] for row in rows)
    assert all(not row["transcription_factor_node_id"] for row in rows)
    assert all(not row["tf_target_edge_id"] for row in rows)
    assert all(not row["target_gene_node_id"] for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16661
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 614
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_eighty_ninth_primary_literature_expansion_batch_preserves_chemokine_and_guidance_outputs():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch089.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion088"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion089"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00045",
        "M21B-DOWNSTREAM:00058",
        "M21B-DOWNSTREAM:00059",
        "M21B-DOWNSTREAM:00060",
        "M21B-DOWNSTREAM:00061",
        "M21B-DOWNSTREAM:00062",
        "M21B-DOWNSTREAM:00065",
        "M21B-DOWNSTREAM:00158",
        "M21B-DOWNSTREAM:00168",
        "M21B-DOWNSTREAM:00170",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_output_annotation_missing_intracellular_and_tf",
    }
    assert {row["output_class"] for row in rows} == {
        "cellular_functional_readout",
        "phosphorylation_or_activation_readout",
        "second_messenger_readout",
    }
    assert {row["effect_polarity"] for row in rows} == {"activating", "inhibitory"}
    assert all(not row["receptor_intracellular_edge_id"] for row in rows)
    assert all(not row["intracellular_tf_edge_id"] for row in rows)
    assert all(not row["transcription_factor_node_id"] for row in rows)
    assert all(not row["tf_target_edge_id"] for row in rows)
    assert all(not row["target_gene_node_id"] for row in rows)
    assert all(row["intracellular_status"] == "not_assayed" for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16671
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 624
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_ninetieth_primary_literature_expansion_batch_preserves_bounded_receptor_outputs():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch090.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion089"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion090"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00046",
        "M21B-DOWNSTREAM:00063",
        "M21B-DOWNSTREAM:00066",
        "M21B-DOWNSTREAM:00172",
        "M21B-DOWNSTREAM:00174",
        "M21B-DOWNSTREAM:00184",
        "M21B-DOWNSTREAM:00185",
        "M21B-DOWNSTREAM:00207",
        "M21B-DOWNSTREAM:00216",
        "M21B-DOWNSTREAM:02103",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_output_annotation_missing_intracellular_and_tf",
    }
    assert {row["output_class"] for row in rows} == {
        "cellular_functional_readout",
        "phosphorylation_or_activation_readout",
        "second_messenger_readout",
        "cleavage_or_processing_readout",
    }
    assert {row["effect_polarity"] for row in rows} == {"activating", "inhibitory", "unknown"}
    assert all(not row["receptor_intracellular_edge_id"] for row in rows)
    assert all(not row["intracellular_tf_edge_id"] for row in rows)
    assert all(not row["transcription_factor_node_id"] for row in rows)
    assert all(not row["tf_target_edge_id"] for row in rows)
    assert all(not row["target_gene_node_id"] for row in rows)
    assert all(row["intracellular_status"] == "not_assayed" for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16681
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 634
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_ninety_first_primary_literature_expansion_batch_preserves_pathway_outputs():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch091.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion090"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion091"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:02108",
        "M21B-DOWNSTREAM:02111",
        "M21B-DOWNSTREAM:02113",
        "M21B-DOWNSTREAM:02114",
        "M21B-DOWNSTREAM:02115",
        "M21B-DOWNSTREAM:02116",
        "M21B-DOWNSTREAM:02125",
        "M21B-DOWNSTREAM:02130",
        "M21B-DOWNSTREAM:02152",
        "M21B-DOWNSTREAM:02156",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf",
        "ligand_receptor_output_annotation_missing_intracellular_and_tf",
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows if row["receptor_intracellular_edge_id"]} == {
        "M21B-E000137",
    }
    assert {row["output_class"] for row in rows} == {
        "cellular_functional_readout",
        "phosphorylation_or_activation_readout",
        "reporter_readout",
    }
    assert {row["effect_polarity"] for row in rows} == {"activating", "inhibitory", "unknown"}
    assert all(not row["intracellular_tf_edge_id"] for row in rows)
    assert all(not row["transcription_factor_node_id"] for row in rows)
    assert all(not row["tf_target_edge_id"] for row in rows)
    assert all(not row["target_gene_node_id"] for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16691
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 644
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_ninety_second_primary_literature_expansion_batch_preserves_gpcr_and_notch_outputs():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch092.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion091"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion092"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:02183",
        "M21B-DOWNSTREAM:02184",
        "M21B-DOWNSTREAM:02195",
        "M21B-DOWNSTREAM:02197",
        "M21B-DOWNSTREAM:02198",
        "M21B-DOWNSTREAM:02199",
        "M21B-DOWNSTREAM:02202",
        "M21B-DOWNSTREAM:02203",
        "M21B-DOWNSTREAM:02222",
        "M21B-DOWNSTREAM:02223",
    }
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_output_missing_tf" for row in rows) == 3
    assert sum(row["route_tier"] == "ligand_receptor_output_annotation_missing_intracellular_and_tf" for row in rows) == 7
    assert {row["receptor_intracellular_edge_id"] for row in rows if row["receptor_intracellular_edge_id"]} == {
        "M21B-E004256",
        "M21B-E004473",
        "M21B-E004481",
    }
    assert {row["output_class"] for row in rows} == {
        "reporter_readout",
        "second_messenger_readout",
    }
    assert {row["effect_polarity"] for row in rows} == {"activating"}
    assert all(not row["intracellular_tf_edge_id"] for row in rows)
    assert all(not row["transcription_factor_node_id"] for row in rows)
    assert all(not row["tf_target_edge_id"] for row in rows)
    assert all(not row["target_gene_node_id"] for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16701
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 654
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_ninety_third_primary_literature_expansion_batch_preserves_receptor_diversity_outputs():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch093.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion092"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion093"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:02160",
        "M21B-DOWNSTREAM:02161",
        "M21B-DOWNSTREAM:02163",
        "M21B-DOWNSTREAM:02165",
        "M21B-DOWNSTREAM:02171",
        "M21B-DOWNSTREAM:02172",
        "M21B-DOWNSTREAM:02178",
        "M21B-DOWNSTREAM:02182",
        "M21B-DOWNSTREAM:02216",
        "M21B-DOWNSTREAM:02224",
    }
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_output_missing_tf" for row in rows) == 1
    assert sum(row["route_tier"] == "ligand_receptor_output_annotation_missing_intracellular_and_tf" for row in rows) == 9
    assert {row["receptor_intracellular_edge_id"] for row in rows if row["receptor_intracellular_edge_id"]} == {
        "M21B-E006779",
    }
    assert {row["output_class"] for row in rows} == {
        "cellular_functional_readout",
        "phosphorylation_or_activation_readout",
        "second_messenger_readout",
        "secreted_protein_or_release",
    }
    assert {row["effect_polarity"] for row in rows} == {"activating", "unknown"}
    assert all(not row["intracellular_tf_edge_id"] for row in rows)
    assert all(not row["transcription_factor_node_id"] for row in rows)
    assert all(not row["tf_target_edge_id"] for row in rows)
    assert all(not row["target_gene_node_id"] for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16711
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 664
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_ninety_fourth_primary_literature_expansion_batch_preserves_gpcr_coupling_outputs():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch094.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion093"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion094"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00574",
        "M21B-DOWNSTREAM:00621",
        "M21B-DOWNSTREAM:00624",
        "M21B-DOWNSTREAM:00647",
        "M21B-DOWNSTREAM:00656",
        "M21B-DOWNSTREAM:00658",
        "M21B-DOWNSTREAM:00659",
        "M21B-DOWNSTREAM:00660",
        "M21B-DOWNSTREAM:00666",
        "M21B-DOWNSTREAM:00667",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf",
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows} == {
        "M21B-E001817",
        "M21B-E003339",
        "M21B-E003341",
        "M21B-E003346",
        "M21B-E003373",
        "M21B-E003309",
        "M21B-E003307",
        "M21B-E003318",
        "M21B-E003335",
        "M21B-E003337",
    }
    assert {row["output_class"] for row in rows} == {
        "phosphorylation_or_activation_readout",
        "second_messenger_readout",
    }
    assert {row["effect_polarity"] for row in rows} == {"activating"}
    assert {row["source_scope"] for row in rows} == {"composite_primary_evidence"}
    assert {row["evidence_directness"] for row in rows} == {"composite_source_claim"}
    assert all(row["intracellular_status"] == "source_supported" for row in rows)
    assert all(not row["intracellular_tf_edge_id"] for row in rows)
    assert all(not row["transcription_factor_node_id"] for row in rows)
    assert all(not row["tf_target_edge_id"] for row in rows)
    assert all(not row["target_gene_node_id"] for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)
    covered_queue_ids = prior_queue_ids | {row["source_queue_id"] for row in rows}
    queue_rows = list(csv.DictReader((source_bundle / "mechanism_downstream_curation_queue.tsv").open(), delimiter="\t"))
    all_queue_ids = {row["queue_id"] for row in queue_rows}
    p1_queue_ids = {row["queue_id"] for row in queue_rows if row["curation_priority"] == "P1"}
    assert len(covered_queue_ids) == 658
    assert len(all_queue_ids - covered_queue_ids) == 2673
    assert len(p1_queue_ids - covered_queue_ids) == 1611

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16721
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 674
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_ninety_fifth_primary_literature_expansion_batch_preserves_immune_and_neuropeptide_gpcr_outputs():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch095.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion094"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion095"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:01654",
        "M21B-DOWNSTREAM:01655",
        "M21B-DOWNSTREAM:01660",
        "M21B-DOWNSTREAM:01666",
        "M21B-DOWNSTREAM:01813",
        "M21B-DOWNSTREAM:01832",
        "M21B-DOWNSTREAM:01922",
        "M21B-DOWNSTREAM:02055",
        "M21B-DOWNSTREAM:02065",
        "M21B-DOWNSTREAM:02074",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf",
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows} == {
        "M21B-E001812",
        "M21B-E001809",
        "M21B-E003375",
        "M21B-E001810",
        "M21B-E003893",
        "M21B-E003376",
        "M21B-E001891",
        "M21B-E003462",
    }
    assert {row["output_class"] for row in rows} == {
        "cellular_functional_readout",
        "phosphorylation_or_activation_readout",
        "second_messenger_readout",
        "translocation_or_localization_readout",
    }
    assert {row["effect_polarity"] for row in rows} == {"activating"}
    assert {row["source_scope"] for row in rows} == {"composite_primary_evidence"}
    assert {row["evidence_directness"] for row in rows} == {"composite_source_claim"}
    assert all(row["intracellular_status"] == "source_supported" for row in rows)
    assert all(not row["intracellular_tf_edge_id"] for row in rows)
    assert all(not row["transcription_factor_node_id"] for row in rows)
    assert all(not row["tf_target_edge_id"] for row in rows)
    assert all(not row["target_gene_node_id"] for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)
    covered_queue_ids = prior_queue_ids | {row["source_queue_id"] for row in rows}
    queue_rows = list(csv.DictReader((source_bundle / "mechanism_downstream_curation_queue.tsv").open(), delimiter="\t"))
    all_queue_ids = {row["queue_id"] for row in queue_rows}
    p1_queue_ids = {row["queue_id"] for row in queue_rows if row["curation_priority"] == "P1"}
    assert len(covered_queue_ids) == 668
    assert len(all_queue_ids - covered_queue_ids) == 2663
    assert len(p1_queue_ids - covered_queue_ids) == 1601

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16731
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 684
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_ninety_sixth_primary_literature_expansion_batch_preserves_immune_resolution_and_gpcr_outputs():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch096.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion095"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion096"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00915",
        "M21B-DOWNSTREAM:00916",
        "M21B-DOWNSTREAM:00918",
        "M21B-DOWNSTREAM:01356",
        "M21B-DOWNSTREAM:01536",
        "M21B-DOWNSTREAM:01537",
        "M21B-DOWNSTREAM:01538",
        "M21B-DOWNSTREAM:01752",
        "M21B-DOWNSTREAM:01818",
        "M21B-DOWNSTREAM:02030",
    }
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_output_missing_tf" for row in rows) == 9
    assert sum(row["route_tier"] == "ligand_receptor_output_annotation_missing_intracellular_and_tf" for row in rows) == 1
    assert {row["receptor_intracellular_edge_id"] for row in rows if row["receptor_intracellular_edge_id"]} == {
        "M21B-E003369",
        "M21B-E003462",
        "M21B-E001809",
        "M21B-E004386",
        "M21B-E004020",
        "M21B-E004278",
        "M21B-E004410",
        "M21B-E001819",
    }
    assert {row["output_class"] for row in rows} == {
        "second_messenger_readout",
        "phosphorylation_or_activation_readout",
        "phagocytosis_or_engulfment",
    }
    assert {row["effect_polarity"] for row in rows} == {"activating", "unknown"}
    assert {row["source_scope"] for row in rows} == {"composite_primary_evidence", "direct_edge"}
    assert {row["evidence_directness"] for row in rows} == {"composite_source_claim", "source_claim"}
    assert sum(row["intracellular_status"] == "source_supported" for row in rows) == 9
    assert sum(row["intracellular_status"] == "not_assayed" for row in rows) == 1
    assert all(not row["transcription_factor_node_id"] for row in rows)
    assert all(not row["intracellular_tf_edge_id"] for row in rows)
    assert all(not row["tf_target_edge_id"] for row in rows)
    assert all(not row["target_gene_node_id"] for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    direct_rows = [row for row in rows if row["source_queue_id"] == "M21B-DOWNSTREAM:01752"]
    assert len(direct_rows) == 1
    assert not direct_rows[0]["receptor_intracellular_edge_id"]
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)
    covered_queue_ids = prior_queue_ids | {row["source_queue_id"] for row in rows}
    queue_rows = list(csv.DictReader((source_bundle / "mechanism_downstream_curation_queue.tsv").open(), delimiter="\t"))
    all_queue_ids = {row["queue_id"] for row in queue_rows}
    p1_queue_ids = {row["queue_id"] for row in queue_rows if row["curation_priority"] == "P1"}
    assert len(covered_queue_ids) == 678
    assert len(all_queue_ids - covered_queue_ids) == 2653
    assert len(p1_queue_ids - covered_queue_ids) == 1591

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16741
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 694
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_ninety_seventh_primary_literature_expansion_batch_preserves_gpcr_second_messenger_outputs():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch097.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion096"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion097"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00583",
        "M21B-DOWNSTREAM:00584",
        "M21B-DOWNSTREAM:00648",
        "M21B-DOWNSTREAM:00668",
        "M21B-DOWNSTREAM:00919",
        "M21B-DOWNSTREAM:01355",
        "M21B-DOWNSTREAM:01667",
        "M21B-DOWNSTREAM:01668",
        "M21B-DOWNSTREAM:01669",
        "M21B-DOWNSTREAM:01670",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf",
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows} == {
        "M21B-E001883",
        "M21B-E001884",
        "M21B-E002056",
        "M21B-E003372",
        "M21B-E003369",
        "M21B-E003304",
        "M21B-E003339",
        "M21B-E003341",
    }
    assert {row["output_class"] for row in rows} == {
        "second_messenger_readout",
        "phosphorylation_or_activation_readout",
    }
    assert {row["effect_polarity"] for row in rows} == {"activating"}
    assert {row["source_scope"] for row in rows} == {"composite_primary_evidence"}
    assert {row["evidence_directness"] for row in rows} == {"composite_source_claim"}
    assert all(row["intracellular_status"] == "source_supported" for row in rows)
    assert all(not row["transcription_factor_node_id"] for row in rows)
    assert all(not row["intracellular_tf_edge_id"] for row in rows)
    assert all(not row["tf_target_edge_id"] for row in rows)
    assert all(not row["target_gene_node_id"] for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)
    covered_queue_ids = prior_queue_ids | {row["source_queue_id"] for row in rows}
    queue_rows = list(csv.DictReader((source_bundle / "mechanism_downstream_curation_queue.tsv").open(), delimiter="\t"))
    all_queue_ids = {row["queue_id"] for row in queue_rows}
    p1_queue_ids = {row["queue_id"] for row in queue_rows if row["curation_priority"] == "P1"}
    assert len(covered_queue_ids) == 688
    assert len(all_queue_ids - covered_queue_ids) == 2643
    assert len(p1_queue_ids - covered_queue_ids) == 1581

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16751
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 704
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_ninety_eighth_primary_literature_expansion_batch_preserves_immune_gpcr_outputs():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch098.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion097"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion098"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:01367",
        "M21B-DOWNSTREAM:01776",
        "M21B-DOWNSTREAM:01918",
        "M21B-DOWNSTREAM:01919",
        "M21B-DOWNSTREAM:01920",
        "M21B-DOWNSTREAM:01923",
        "M21B-DOWNSTREAM:01924",
        "M21B-DOWNSTREAM:01925",
        "M21B-DOWNSTREAM:01926",
        "M21B-DOWNSTREAM:01928",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf",
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows} == {
        "M21B-E003898",
        "M21B-E003375",
        "M21B-E003369",
        "M21B-E003893",
    }
    assert {row["output_class"] for row in rows} == {
        "second_messenger_readout",
        "phosphorylation_or_activation_readout",
        "cellular_functional_readout",
    }
    assert {row["effect_polarity"] for row in rows} == {"activating", "unknown"}
    assert {row["source_scope"] for row in rows} == {"composite_primary_evidence"}
    assert {row["evidence_directness"] for row in rows} == {"composite_source_claim"}
    assert all(row["intracellular_status"] == "source_supported" for row in rows)
    assert all(not row["transcription_factor_node_id"] for row in rows)
    assert all(not row["intracellular_tf_edge_id"] for row in rows)
    assert all(not row["tf_target_edge_id"] for row in rows)
    assert all(not row["target_gene_node_id"] for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)
    covered_queue_ids = prior_queue_ids | {row["source_queue_id"] for row in rows}
    queue_rows = list(csv.DictReader((source_bundle / "mechanism_downstream_curation_queue.tsv").open(), delimiter="\t"))
    all_queue_ids = {row["queue_id"] for row in queue_rows}
    p1_queue_ids = {row["queue_id"] for row in queue_rows if row["curation_priority"] == "P1"}
    assert len(covered_queue_ids) == 698
    assert len(all_queue_ids - covered_queue_ids) == 2633
    assert len(p1_queue_ids - covered_queue_ids) == 1571

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16761
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 714
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_ninety_ninth_primary_literature_expansion_batch_preserves_endocrine_and_neuropeptide_gpcr_outputs():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch099.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion098"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion099"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00622",
        "M21B-DOWNSTREAM:00625",
        "M21B-DOWNSTREAM:01675",
        "M21B-DOWNSTREAM:01688",
        "M21B-DOWNSTREAM:01690",
        "M21B-DOWNSTREAM:01810",
        "M21B-DOWNSTREAM:01815",
        "M21B-DOWNSTREAM:01816",
        "M21B-DOWNSTREAM:01826",
        "M21B-DOWNSTREAM:01921",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf",
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows} == {
        "M21B-E003339",
        "M21B-E003341",
        "M21B-E003346",
        "M21B-E001831",
        "M21B-E001826",
        "M21B-E004452",
        "M21B-E004269",
        "M21B-E003991",
        "M21B-E003370",
        "M21B-E003893",
    }
    assert {row["output_class"] for row in rows} == {
        "second_messenger_readout",
        "gene_expression_or_transcription",
    }
    assert {row["effect_polarity"] for row in rows} == {"activating", "inhibitory"}
    assert {row["source_scope"] for row in rows} == {"composite_primary_evidence"}
    assert {row["evidence_directness"] for row in rows} == {"composite_source_claim"}
    assert all(row["intracellular_status"] == "source_supported" for row in rows)
    assert all(not row["transcription_factor_node_id"] for row in rows)
    assert all(not row["intracellular_tf_edge_id"] for row in rows)
    assert all(not row["tf_target_edge_id"] for row in rows)
    assert all(not row["target_gene_node_id"] for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)
    covered_queue_ids = prior_queue_ids | {row["source_queue_id"] for row in rows}
    queue_rows = list(csv.DictReader((source_bundle / "mechanism_downstream_curation_queue.tsv").open(), delimiter="\t"))
    all_queue_ids = {row["queue_id"] for row in queue_rows}
    p1_queue_ids = {row["queue_id"] for row in queue_rows if row["curation_priority"] == "P1"}
    assert len(covered_queue_ids) == 708
    assert len(all_queue_ids - covered_queue_ids) == 2623
    assert len(p1_queue_ids - covered_queue_ids) == 1561

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16771
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 724
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_one_hundredth_primary_literature_expansion_batch_preserves_innate_and_neuroimmune_outputs():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch100.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion099"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion100"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:01875",
        "M21B-DOWNSTREAM:01929",
        "M21B-DOWNSTREAM:01931",
        "M21B-DOWNSTREAM:01933",
        "M21B-DOWNSTREAM:01934",
        "M21B-DOWNSTREAM:01935",
        "M21B-DOWNSTREAM:01936",
        "M21B-DOWNSTREAM:01945",
        "M21B-DOWNSTREAM:01967",
        "M21B-DOWNSTREAM:01975",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf",
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows} == {
        "M21B-E001335",
        "M21B-E003893",
        "M21B-E001812",
        "M21B-E004465",
    }
    assert {row["output_class"] for row in rows} == {
        "phosphorylation_or_activation_readout",
        "second_messenger_readout",
        "phagocytosis_or_engulfment",
        "gene_expression_or_transcription",
    }
    assert {row["effect_polarity"] for row in rows} == {"activating"}
    assert {row["source_scope"] for row in rows} == {"composite_primary_evidence"}
    assert {row["evidence_directness"] for row in rows} == {"composite_source_claim"}
    assert all(row["intracellular_status"] == "source_supported" for row in rows)
    assert all(not row["transcription_factor_node_id"] for row in rows)
    assert all(not row["intracellular_tf_edge_id"] for row in rows)
    assert all(not row["tf_target_edge_id"] for row in rows)
    assert all(not row["target_gene_node_id"] for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)
    covered_queue_ids = prior_queue_ids | {row["source_queue_id"] for row in rows}
    queue_rows = list(csv.DictReader((source_bundle / "mechanism_downstream_curation_queue.tsv").open(), delimiter="\t"))
    all_queue_ids = {row["queue_id"] for row in queue_rows}
    p1_queue_ids = {row["queue_id"] for row in queue_rows if row["curation_priority"] == "P1"}
    assert len(covered_queue_ids) == 718
    assert len(all_queue_ids - covered_queue_ids) == 2613
    assert len(p1_queue_ids - covered_queue_ids) == 1551

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16781
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 734
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_one_hundred_first_primary_literature_expansion_batch_preserves_shared_receptor_and_innate_routes():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch101.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion100"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion101"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00342",
        "M21B-DOWNSTREAM:00343",
        "M21B-DOWNSTREAM:00344",
        "M21B-DOWNSTREAM:00378",
        "M21B-DOWNSTREAM:03057",
        "M21B-DOWNSTREAM:03062",
        "M21B-DOWNSTREAM:03110",
        "M21B-DOWNSTREAM:03112",
        "M21B-DOWNSTREAM:03128",
        "M21B-DOWNSTREAM:03275",
    }
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_output_missing_tf" for row in rows) == 8
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_tf_output_missing_target_gene" for row in rows) == 1
    assert sum(row["route_tier"] == "ligand_receptor_tf_output_annotation_missing_intracellular" for row in rows) == 1
    assert {row["receptor_intracellular_edge_id"] for row in rows if row["receptor_intracellular_edge_id"]} == {
        "M21B-E006779",
        "M21B-E004471",
        "M21B-E001809",
        "M21B-E004410",
        "M21B-E001335",
        "M21B-E001333",
    }
    assert {row["transcription_factor_node_id"] for row in rows if row["transcription_factor_node_id"]} == {
        "NODE10672",
        "NODE07961",
    }
    assert {row["output_class"] for row in rows} == {
        "cellular_functional_readout",
        "second_messenger_readout",
        "phosphorylation_or_activation_readout",
        "secreted_protein_or_release",
        "gene_expression_or_transcription",
        "reporter_readout",
    }
    assert {row["effect_polarity"] for row in rows} == {"activating"}
    assert {row["source_scope"] for row in rows} == {"composite_primary_evidence"}
    assert {row["evidence_directness"] for row in rows} == {"composite_source_claim"}
    assert sum(row["intracellular_status"] == "source_supported" for row in rows) == 9
    assert sum(row["intracellular_status"] == "not_assayed" for row in rows) == 1
    assert all(not row["tf_target_edge_id"] for row in rows)
    assert all(not row["target_gene_node_id"] for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)
    covered_queue_ids = prior_queue_ids | {row["source_queue_id"] for row in rows}
    queue_rows = list(csv.DictReader((source_bundle / "mechanism_downstream_curation_queue.tsv").open(), delimiter="\t"))
    all_queue_ids = {row["queue_id"] for row in queue_rows}
    p1_queue_ids = {row["queue_id"] for row in queue_rows if row["curation_priority"] == "P1"}
    assert len(covered_queue_ids) == 728
    assert len(all_queue_ids - covered_queue_ids) == 2603
    assert len(p1_queue_ids - covered_queue_ids) == 1547

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16791
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 744
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_one_hundred_second_primary_literature_expansion_batch_preserves_receptor_and_innate_outputs():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch102.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion101"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion102"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00396",
        "M21B-DOWNSTREAM:00397",
        "M21B-DOWNSTREAM:02820",
        "M21B-DOWNSTREAM:02818",
        "M21B-DOWNSTREAM:02752",
        "M21B-DOWNSTREAM:02753",
        "M21B-DOWNSTREAM:03031",
        "M21B-DOWNSTREAM:02819",
        "M21B-DOWNSTREAM:03274",
        "M21B-DOWNSTREAM:03277",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf",
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows} == {
        "M21B-E002037",
        "M21B-E001809",
        "M21B-E003343",
        "M21B-E003831",
        "M21B-E003335",
        "M21B-E003302",
        "M21B-E001332",
        "M21B-E001476",
    }
    assert {row["output_class"] for row in rows} == {
        "cellular_functional_readout",
        "second_messenger_readout",
        "phosphorylation_or_activation_readout",
    }
    assert {row["effect_polarity"] for row in rows} == {"activating", "inhibitory", "unknown"}
    assert {row["source_scope"] for row in rows} == {"composite_primary_evidence"}
    assert {row["evidence_directness"] for row in rows} == {"composite_source_claim"}
    assert all(row["intracellular_status"] == "source_supported" for row in rows)
    assert all(not row["transcription_factor_node_id"] for row in rows)
    assert all(not row["intracellular_tf_edge_id"] for row in rows)
    assert all(not row["tf_target_edge_id"] for row in rows)
    assert all(not row["target_gene_node_id"] for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)
    covered_queue_ids = prior_queue_ids | {row["source_queue_id"] for row in rows}
    queue_rows = list(csv.DictReader((source_bundle / "mechanism_downstream_curation_queue.tsv").open(), delimiter="\t"))
    all_queue_ids = {row["queue_id"] for row in queue_rows}
    p1_queue_ids = {row["queue_id"] for row in queue_rows if row["curation_priority"] == "P1"}
    assert len(covered_queue_ids) == 738
    assert len(all_queue_ids - covered_queue_ids) == 2593
    assert len(p1_queue_ids - covered_queue_ids) == 1545

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16801
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 754
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_one_hundred_third_primary_literature_expansion_batch_preserves_cytokine_chemokine_and_purinergic_routes():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch103.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion102"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion103"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:02551",
        "M21B-DOWNSTREAM:02547",
        "M21B-DOWNSTREAM:02548",
        "M21B-DOWNSTREAM:02550",
        "M21B-DOWNSTREAM:00025",
        "M21B-DOWNSTREAM:00105",
        "M21B-DOWNSTREAM:00112",
        "M21B-DOWNSTREAM:00017",
        "M21B-DOWNSTREAM:00064",
        "M21B-DOWNSTREAM:00556",
    }
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_output_missing_tf" for row in rows) == 7
    assert sum(row["route_tier"] == "ligand_receptor_intracellular_tf_output_missing_target_gene" for row in rows) == 3
    assert {row["receptor_intracellular_edge_id"] for row in rows} == {
        "M21B-E000023",
        "M21B-E001727",
        "M21B-E001716",
        "M21B-E000014",
        "M21B-E001776",
        "M21B-E011504",
        "M21B-E000034",
        "M21B-E003377",
        "M21B-E003378",
        "M21B-E001847",
    }
    assert {row["transcription_factor_node_id"] for row in rows if row["transcription_factor_node_id"]} == {
        "NODE10693",
        "NODE10719",
    }
    assert {row["output_class"] for row in rows} == {
        "phosphorylation_or_activation_readout",
        "second_messenger_readout",
        "gene_expression_or_transcription",
    }
    assert {row["effect_polarity"] for row in rows} == {"activating"}
    assert {row["source_scope"] for row in rows} == {"composite_primary_evidence"}
    assert {row["evidence_directness"] for row in rows} == {"composite_source_claim"}
    assert all(row["intracellular_status"] == "source_supported" for row in rows)
    assert sum(bool(row["transcription_factor_node_id"]) for row in rows) == 3
    assert all(not row["tf_target_edge_id"] for row in rows)
    assert all(not row["target_gene_node_id"] for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)
    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    current_queue_ids = {row["source_queue_id"] for row in rows}
    assert len(current_queue_ids & prior_queue_ids) == 7
    assert len(current_queue_ids - prior_queue_ids) == 3
    covered_queue_ids = prior_queue_ids | current_queue_ids
    queue_rows = list(csv.DictReader((source_bundle / "mechanism_downstream_curation_queue.tsv").open(), delimiter="\t"))
    all_queue_ids = {row["queue_id"] for row in queue_rows}
    p1_queue_ids = {row["queue_id"] for row in queue_rows if row["curation_priority"] == "P1"}
    assert len(covered_queue_ids) == 741
    assert len(all_queue_ids - covered_queue_ids) == 2590
    assert len(p1_queue_ids - covered_queue_ids) == 1545

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16811
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 764
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_one_hundred_fourth_primary_literature_expansion_batch_preserves_receptor_proximal_adaptor_routes():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch104.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion103"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion104"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00001",
        "M21B-DOWNSTREAM:00920",
        "M21B-DOWNSTREAM:01213",
        "M21B-DOWNSTREAM:01218",
        "M21B-DOWNSTREAM:01219",
        "M21B-DOWNSTREAM:01627",
        "M21B-DOWNSTREAM:01927",
        "M21B-DOWNSTREAM:02221",
        "M21B-DOWNSTREAM:00381",
        "M21B-DOWNSTREAM:00394",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf",
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows} == {
        "M21B-E000112",
        "M21B-E003369",
        "M21B-E003833",
        "M21B-E003828",
        "M21B-E001794",
        "M21B-E003893",
        "M21B-E003371",
        "M21B-E004461",
    }
    assert {row["intracellular_continuation_label"] for row in rows} == {
        "PI3K p85/p110",
        "GNAI/O/Z",
        "CD247/CD3ζ",
        "DAP10/HCST",
        "TRAF1",
        "GNAQ/GNA11",
        "GNAS",
    }
    assert {row["output_class"] for row in rows} == {
        "cellular_functional_readout",
        "generic_functional_readout",
        "gene_expression_or_transcription",
        "phosphorylation_or_activation_readout",
    }
    assert {row["effect_polarity"] for row in rows} == {"activating", "inhibitory", "unknown"}
    assert {row["source_scope"] for row in rows} == {"composite_primary_evidence"}
    assert {row["evidence_directness"] for row in rows} == {"composite_source_claim"}
    assert all(row["intracellular_status"] == "source_supported" for row in rows)
    assert all(not row["transcription_factor_node_id"] for row in rows)
    assert all(not row["intracellular_tf_edge_id"] for row in rows)
    assert all(not row["tf_target_edge_id"] for row in rows)
    assert all(not row["target_gene_node_id"] for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)

    edges = {
        row["edge_id"]: (row["source_node_id"], row["target_node_id"])
        for row in csv.DictReader((source_bundle / "mechanism_edges.tsv").open(), delimiter="\t")
    }
    for row in rows:
        assert edges[row["ligand_receptor_edge_id"]] == (row["ligand_node_id"], row["receptor_node_id"])
        assert edges[row["receptor_intracellular_edge_id"]] == (
            row["receptor_node_id"],
            row["intracellular_continuation_node_id"],
        )

    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    current_queue_ids = {row["source_queue_id"] for row in rows}
    assert current_queue_ids & prior_queue_ids == {"M21B-DOWNSTREAM:00001"}
    assert len(current_queue_ids - prior_queue_ids) == 9
    covered_queue_ids = prior_queue_ids | current_queue_ids
    queue_rows = list(csv.DictReader((source_bundle / "mechanism_downstream_curation_queue.tsv").open(), delimiter="\t"))
    all_queue_ids = {row["queue_id"] for row in queue_rows}
    p1_queue_ids = {row["queue_id"] for row in queue_rows if row["curation_priority"] == "P1"}
    assert len(covered_queue_ids) == 750
    assert len(all_queue_ids - covered_queue_ids) == 2581
    assert len(p1_queue_ids - covered_queue_ids) == 1536

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16821
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 774
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}


def test_one_hundred_fifth_primary_literature_expansion_batch_preserves_dap12_linked_routes():
    root = Path(__file__).parents[1]
    input_path = root / "work/module_b_consolidation/module21b/module21b_literature_expansion_batch105.json"
    source_bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion104"
    bundle = root / "data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion105"
    rows = read_input(input_path)
    validate_rows(rows, source_bundle)
    assert len(rows) == 10
    assert {row["expansion_id"] for row in rows} == {
        f"M21B-LITEXP-{number:04d}" for number in range(775, 785)
    }
    assert {row["source_queue_id"] for row in rows} == {
        "M21B-DOWNSTREAM:00462",
        "M21B-DOWNSTREAM:00831",
        "M21B-DOWNSTREAM:00834",
        "M21B-DOWNSTREAM:00839",
    }
    assert {row["route_tier"] for row in rows} == {
        "ligand_receptor_intracellular_output_missing_tf",
    }
    assert {row["receptor_intracellular_edge_id"] for row in rows} == {
        "M21B-E001120",
        "M21B-E001924",
        "M21B-E001927",
        "M21B-E001933",
    }
    assert {row["intracellular_continuation_label"] for row in rows} == {"DAP12/TYROBP"}
    assert {row["output_class"] for row in rows} == {
        "gene_expression_or_transcription",
        "phagocytosis_or_engulfment",
        "phosphorylation_or_activation_readout",
    }
    assert {row["effect_polarity"] for row in rows} == {"activating", "inhibitory", "unknown"}
    assert {row["source_scope"] for row in rows} == {"composite_primary_evidence"}
    assert {row["evidence_directness"] for row in rows} == {"composite_source_claim"}
    assert all(row["intracellular_status"] == "source_supported" for row in rows)
    assert all(not row["transcription_factor_node_id"] for row in rows)
    assert all(not row["intracellular_tf_edge_id"] for row in rows)
    assert all(not row["tf_target_edge_id"] for row in rows)
    assert all(not row["target_gene_node_id"] for row in rows)
    assert all(row["causal_status"] == "not_asserted" for row in rows)
    assert all(row["traversal_status"] == "evidence_route_not_causal" for row in rows)
    assert all(row["curation_status"] == "curated_primary_route" for row in rows)

    edges = {
        row["edge_id"]: (row["source_node_id"], row["target_node_id"])
        for row in csv.DictReader((source_bundle / "mechanism_edges.tsv").open(), delimiter="\t")
    }
    for row in rows:
        assert edges[row["ligand_receptor_edge_id"]] == (
            row["ligand_node_id"],
            row["receptor_node_id"],
        )
        assert edges[row["receptor_intracellular_edge_id"]] == (
            row["receptor_node_id"],
            row["intracellular_continuation_node_id"],
        )

    prior_queue_ids = {
        prior_row["source_queue_id"]
        for prior_path in input_path.parent.glob("module21b_literature_expansion_batch*.json")
        if prior_path != input_path and int(prior_path.stem[-3:]) < int(input_path.stem[-3:])
        for prior_row in json.loads(prior_path.read_text())
    }
    covered_queue_ids = prior_queue_ids
    current_queue_ids = {row["source_queue_id"] for row in rows}
    assert not current_queue_ids & covered_queue_ids
    queue_rows = list(csv.DictReader(
        (source_bundle / "mechanism_downstream_curation_queue.tsv").open(), delimiter="\t"
    ))
    all_queue_ids = {row["queue_id"] for row in queue_rows}
    p1_queue_ids = {row["queue_id"] for row in queue_rows if row["curation_priority"] == "P1"}
    covered_after = covered_queue_ids | current_queue_ids
    assert len(covered_after) == 754
    assert len(all_queue_ids - covered_after) == 2577
    assert len(p1_queue_ids - covered_after) == 1532

    route_rows = list(csv.DictReader(
        (bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"
    ))
    assert len(route_rows) == 16831
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 784
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}
