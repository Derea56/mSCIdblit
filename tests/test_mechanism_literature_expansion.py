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
