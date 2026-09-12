import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "audit_mechanism_output_bridges.py"
SPEC = importlib.util.spec_from_file_location("audit_mechanism_output_bridges", SCRIPT)
assert SPEC and SPEC.loader
audit_bridges = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit_bridges)


def test_product_form_resolution_skips_small_molecules_and_keeps_unique_proteins():
    forms = {
        "bdnf": [{"entity_form_id": "PROTEIN:NODE00767", "form_type": "protein_ligand"}],
        "atp": [{"entity_form_id": "PROTEIN:NODE00665", "form_type": "protein_ligand"}],
    }

    result = audit_bridges.product_form_ids_for_labels("Bdnf;Atp", forms)

    assert result == "PROTEIN:NODE00767"


def test_transition_gate_requires_gene_level_output_evidence():
    transitions = {
        "GENE:NODE00767": [
            {
                "transition_id": "TRN:00010",
                "target_label": "Bdnf",
            }
        ]
    }
    protein_only = {
        "output_product_labels": "Bdnf",
        "assay_or_perturbation": "BDNF ELISA and secretion assay",
        "transition_ids": "TRN:00010",
    }
    gene_and_protein = {
        "output_product_labels": "Bdnf",
        "assay_or_perturbation": "Bdnf promoter-IV and BDNF secretion assays",
        "transition_ids": "TRN:00010",
    }

    audit_bridges.filter_output_transition_ids(protein_only, transitions)
    audit_bridges.filter_output_transition_ids(gene_and_protein, transitions)

    assert protein_only["transition_ids"] == ""
    assert gene_and_protein["transition_ids"] == "TRN:00010"


def test_explicit_microglial_il6_release_resolves_target_gene_product_form():
    forms = {
        "il6": [
            {"entity_form_id": "PROTEIN:NODE03873", "form_type": "protein_ligand"},
            {"entity_form_id": "PROTEIN:NODE04051", "form_type": "protein_ligand"},
            {"entity_form_id": "OUTPUT_PROTEIN:NODE03873", "form_type": "protein_output"},
            {"entity_form_id": "OUTPUT_PROTEIN:NODE04051", "form_type": "protein_output"},
        ]
    }
    row = {
        "output_product_labels": "Il6",
        "output_label": "microglial IL-6 release",
        "assay_or_perturbation": "IL-6 release and inflammatory readouts",
        "output_observation": "Microglial IL-6 release followed neuronal HMGB1 exposure.",
        "product_form_ids": "",
    }

    audit_bridges.enrich_validated_product_forms(row, forms)

    assert row["product_form_ids"] == "OUTPUT_PROTEIN:NODE04051"


def test_generic_il6_production_remains_untyped_when_label_is_ambiguous():
    forms = {
        "il6": [
            {"entity_form_id": "PROTEIN:NODE03873", "form_type": "protein_ligand"},
            {"entity_form_id": "PROTEIN:NODE04051", "form_type": "protein_ligand"},
            {"entity_form_id": "OUTPUT_PROTEIN:NODE03873", "form_type": "protein_output"},
            {"entity_form_id": "OUTPUT_PROTEIN:NODE04051", "form_type": "protein_output"},
        ]
    }
    row = {
        "output_product_labels": "Il6",
        "output_label": "IL6 production",
        "assay_or_perturbation": "IL-6 production and mRNA readouts",
        "output_observation": "P2Y12 stimulation altered Il6 production.",
        "product_form_ids": "",
    }

    audit_bridges.enrich_validated_product_forms(row, forms)

    assert row["product_form_ids"] == ""


def test_context_specific_aqp4_protein_outputs_do_not_collapse_context_nodes():
    row = {
        "output_product_labels": "Aqp4",
        "output_label": "Microglia-derived IL-6-associated astrocytic AQP4 expression",
        "assay_or_perturbation": "Astrocytic AQP4 mRNA/protein; edema readouts",
        "output_observation": "Microglial IL-6 context altered astrocytic AQP4.",
        "product_form_ids": "",
    }

    audit_bridges.enrich_validated_product_forms(row, {})

    assert row["product_form_ids"] == "OUTPUT_PROTEIN:NODE00612"
