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
