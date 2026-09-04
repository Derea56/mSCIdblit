import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from public_tf_curation import (  # noqa: E402
    build_ledger_rows,
    classify_row,
    duplicate_metadata,
    eligible_for_mode,
    source_locator_status,
    traversal_flags,
    validate_promotable_overlay_row,
)


def candidate(**overrides):
    row = {
        "layer_record_id": "PTF-1",
        "layer_membership": "evidence_candidate",
        "traversal_status": "not_traversable",
        "regulator_symbol": "MSGN1",
        "raw_tf_symbol": "Msgn1",
        "target_symbol": "Dll3",
        "module": "20B",
        "species_scope": "mouse",
        "evidence_confidence_tier": "C_tflink_source_table_only",
        "mechanism_evidence_type": "expression_or_perturbation_association",
        "effect_polarity": "",
        "context_level_exact_pair": "L0_no_context_evidence",
        "primary_citation": "",
        "source_record_id": "tflink:mouse:1",
        "source_record_ids": "",
    }
    row.update(overrides)
    return row


def validated(**overrides):
    row = candidate(
        layer_membership="validated_mechanism_edge",
        traversal_status="validated_edge_candidate",
        evidence_confidence_tier="A_independent_literature_corroborated",
        mechanism_evidence_type="direct_sequence_specific_tf_binding",
        exact_pair_status="functional_direct_binding_promotion_candidate",
        primary_citation="https://example.org/primary",
        validation_basis="Primary mouse occupancy and perturbation evidence",
        validated_effect_polarity="activating",
        context_level_exact_pair="L1_non_CNS_context",
        promotion_confidence="strong_exact_pair_evidence_context_limited",
    )
    row.update(overrides)
    return row


class PublicTFCurationTests(unittest.TestCase):
    def test_unsupported_promotion_is_rejected(self):
        row = validated(layer_membership="evidence_candidate")
        with self.assertRaisesRegex(ValueError, "layer_membership"):
            validate_promotable_overlay_row(row)

    def test_candidate_rows_are_not_traversable(self):
        row = candidate()
        status = classify_row(row, {})
        flags = traversal_flags(status, row)
        self.assertEqual(status, "candidate_only")
        self.assertEqual(flags["traversal_eligibility"], "not_traversable")
        self.assertFalse(eligible_for_mode({**row, **flags}, "general_mouse"))

    def test_context_gated_promotion(self):
        neural = validated(context_level_exact_pair="L2_CNS_context")
        flags = traversal_flags("neural_context_validated", neural)
        self.assertTrue(flags["traversable_general_mouse"])
        self.assertTrue(flags["traversable_neural"])
        self.assertFalse(flags["traversable_sci"])

        sci = validated(context_level_exact_pair="L4_SCI_context")
        flags = traversal_flags("sci_context_validated", sci)
        self.assertTrue(flags["traversable_sci"])

    def test_duplicate_and_module_handling(self):
        rows = [candidate(), candidate(layer_record_id="PTF-2", module="23B")]
        duplicates = duplicate_metadata(rows)
        key = ("msgn1", "dll3")
        self.assertEqual(duplicates["row_counts"][key], 2)
        self.assertEqual(duplicates["module_counts"][key], 2)

    def test_provenance_and_unknown_values_are_retained(self):
        source = candidate(
            evidence_confidence_tier="A_independent_literature_corroborated",
            primary_citation="https://example.org/source",
            source_record_id="source-42",
            tflink_source_url="https://example.org/tflink",
        )
        ledger = build_ledger_rows([source], [], active_node_symbols={})
        row = ledger[0]
        self.assertEqual(row["curation_status"], "unresolved")
        self.assertEqual(row["effect_direction"], "unknown")
        self.assertEqual(row["tissue_cell_context"], "unknown_not_structured_in_candidate_layer")
        self.assertIn("https://example.org/source", row["citation_provenance"])
        self.assertEqual(row["source_record_id"], "source-42")
        self.assertEqual(source_locator_status(source), "citation_and_source_record")
        self.assertEqual(row["traversal_eligibility"], "not_traversable")


if __name__ == "__main__":
    unittest.main()
