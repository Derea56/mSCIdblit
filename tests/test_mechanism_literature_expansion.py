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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
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
        if prior_path != input_path
        for prior_row in json.loads(prior_path.read_text())
    }
    assert not ({row["source_queue_id"] for row in rows} & prior_queue_ids)

    route_rows = list(csv.DictReader((bundle / "mechanism_signaling_route_evidence.tsv").open(), delimiter="\t"))
    assert len(route_rows) == 16590
    assert sum(row["route_evidence_id"].startswith("LITEXP:") for row in route_rows) == 543
    assert {row["source_chain_id"] for row in route_rows[-10:]} == {row["expansion_id"] for row in rows}
