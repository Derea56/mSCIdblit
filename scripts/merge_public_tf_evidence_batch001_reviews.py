#!/usr/bin/env python3
"""Merge completed bounded evidence lanes for public TF batch 001.

The merge is intentionally staging-only.  It normalizes the external lane
for ranks 16-20 into the local schema, preserves the TFLink source record
IDs, and keeps regulator-level citations out of the exact-pair citation
fields.  No canonical model or Module 22B artifact is changed.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIR = ROOT / (
    "data/processed/public_tf_union_expansion_v1/"
    "current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_001"
)

PAIR_FIELDS = [
    "review_id", "batch_id", "batch_rank", "regulator_key", "regulator_symbol",
    "species_scope", "source_registry", "source_record_id", "raw_tf_symbol",
    "target_symbol", "target_graph_modules", "candidate_membership_status",
    "exact_pair_search_url", "exact_pair_status", "regulator_general_evidence_status",
    "target_cell_presence_status", "binding_or_association_status",
    "downstream_expression_or_perturbation_status", "downstream_activation_status",
    "upstream_relay_status", "disposition", "primary_citation",
    "corroborating_citation", "near_match_exclusions", "review_notes", "exportable",
    "canonical_write_performed",
]

EVIDENCE_FIELDS = [
    "evidence_id", "regulator_key", "regulator_symbol", "species_scope", "evidence_layer",
    "support_kind", "cell_or_model", "assay_or_perturbation", "observation",
    "effect_direction", "primary_citation", "corroborating_citation",
    "route_or_module_relevance", "target_pair_scope", "exportable",
    "canonical_write_performed", "limitations",
]

RANKS_16_20 = {
    "zscan22": {
        "symbol": "ZSCAN22", "species": "human",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5131825/", "corroborating": "",
        "model": "human HEK293 functional-screen models",
        "assay": "C2H2 zinc-finger functional/regulatory screen",
        "observation": "ZSCAN22 has regulator-level functional evidence, but the queued ACKR3/ACTR2/ACVR1/ACVR1C targets were not directly tested.",
        "direction": "queued-pair direction not established",
        "near": "ACKR3-only, ARP2/3, and ACVR1/ACVR1C studies without ZSCAN22 were excluded",
    },
    "purb": {
        "symbol": "PURB", "species": "mouse",
        "primary": "https://pubmed.ncbi.nlm.nih.gov/12874279/", "corroborating": "https://pubmed.ncbi.nlm.nih.gov/23724822/",
        "model": "mouse transcriptional and smooth-muscle models",
        "assay": "PURB promoter/transcriptional studies with independent Acta2 validation",
        "observation": "PURB has regulator-level evidence including Acta2-related transcriptional regulation; the queued Actr2/Acvr1/Acvr1c/Acvrl1 targets were not directly tested.",
        "direction": "queued-pair direction not established",
        "near": "PURB-to-Acta2 is a different target from queued Actr2; ACVR1/ACVR1C/ACVRL1 studies naming other factors were excluded",
    },
    "zfhx2": {
        "symbol": "ZFHX2", "species": "human",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5837393/", "corroborating": "",
        "model": "human sensory-neuron/Marsili syndrome models",
        "assay": "human ZFHX2 genetic and transcriptional regulatory studies",
        "observation": "ZFHX2 has human regulator-level evidence in sensory-neuron biology; the queued A2M/ACKR3/ACTR2/ACVR1 targets were not directly tested.",
        "direction": "queued-pair direction not established",
        "near": "ZHX2, ACKR3-only, ARP2/3, and LHX2-to-ACVR1 studies were excluded as different genes or regulators",
    },
    "neurod2": {
        "symbol": "NEUROD2", "species": "mouse",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5343279/", "corroborating": "https://pubmed.ncbi.nlm.nih.gov/27146976/",
        "model": "mouse neuronal models",
        "assay": "NEUROD2 perturbation, chromatin/target studies, and independent neuronal target validation",
        "observation": "NEUROD2 has regulator-level neuronal evidence with targets such as Stim1 and other neuronal genes; the queued Actr2/Acvr1/Acvr1c/Adam10 targets were not directly tested.",
        "direction": "queued-pair direction not established",
        "near": "Stim1, Reln, Dlg4/Cntn2, LHX2-to-Acvr1, YAP-to-Acvr1c, and Adam10 expression studies were excluded as different targets or regulators",
    },
    "prdm10": {
        "symbol": "PRDM10", "species": "human",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6525587/", "corroborating": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7368010/",
        "model": "human and mouse PRDM10 cellular models",
        "assay": "PRDM10 perturbation and target-gene transcriptional studies",
        "observation": "PRDM10 has regulator-level evidence including BCL2/EIF3B-related transcriptional targets; the queued ACKR1/ACKR2/ACTR2/ACVR1 targets were not directly tested.",
        "direction": "queued-pair direction not established",
        "near": "PRDM10-to-BCL2/EIF3B, GATA1-to-ACKR2, ARP2/3, and EGR1/HEY1/ZBTB7A/SP1-to-ACVR1 studies were excluded as different pairs",
    },
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


def normalize_external(row: dict[str, str]) -> dict[str, str]:
    result = {field: row.get(field, "") for field in PAIR_FIELDS}
    regulator = RANKS_16_20[row["regulator_key"]]
    # The external lane used this field for a regulator-level citation. Keep
    # exact-pair citation columns empty to prevent accidental evidence reuse.
    general_citation = row.get("primary_citation", "")
    result["primary_citation"] = ""
    result["corroborating_citation"] = ""
    result["near_match_exclusions"] = row.get("excluded_near_matches", "")
    result["review_notes"] = (
        row.get("review_notes", "")
        + (" General regulator-level citation retained separately: " + general_citation if general_citation else "")
    )
    result["regulator_symbol"] = regulator["symbol"]
    result["downstream_activation_status"] = "not_assessed"
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=Path, default=DEFAULT_DIR)
    args = parser.parse_args()

    local_path = args.directory / "public_tf_evidence_review_batch001_pairs.tsv"
    external_path = args.directory / "public_tf_evidence_review_batch001_ranks16_20.tsv"
    register_path = args.directory / "public_tf_evidence_review_batch001_regulator_register.tsv"
    local_rows = read_tsv(local_path)
    external_rows = read_tsv(external_path)
    if len(local_rows) != 100:
        raise SystemExit(f"expected 100 local rows for ranks 1-25, found {len(local_rows)}")
    if len(external_rows) != 20:
        raise SystemExit(f"expected 20 external rows for ranks 16-20, found {len(external_rows)}")
    if any(row["regulator_key"] not in RANKS_16_20 for row in external_rows):
        raise SystemExit("external rows contain an unexpected regulator key")

    # Replace the generic stage rows for ranks 16-20 with the completed
    # evidence lane, while retaining ranks 1-15 and 21-25 from the local
    # stage. This keeps the final batch at exactly 100 unique pairs.
    retained_local_rows = [row for row in local_rows if not 16 <= int(row["batch_rank"]) <= 20]
    merged_pairs = retained_local_rows + [normalize_external(row) for row in external_rows]
    merged_pairs.sort(key=lambda row: (int(row["batch_rank"]), row["target_symbol"].casefold()))
    write_tsv(local_path, PAIR_FIELDS, merged_pairs)

    register_rows = read_tsv(register_path)
    existing_keys = {row["regulator_key"] for row in register_rows}
    for key, evidence in RANKS_16_20.items():
        if key in existing_keys:
            continue
        register_rows.append({
            "evidence_id": f"public_tf_evidence_batch001_regulator_{key}",
            "regulator_key": key,
            "regulator_symbol": evidence["symbol"],
            "species_scope": evidence["species"],
            "evidence_layer": "regulator_identity_and_regulatory_capacity",
            "support_kind": "primary_literature_regulator_level",
            "cell_or_model": evidence["model"],
            "assay_or_perturbation": evidence["assay"],
            "observation": evidence["observation"],
            "effect_direction": evidence["direction"],
            "primary_citation": evidence["primary"],
            "corroborating_citation": evidence["corroborating"],
            "route_or_module_relevance": "regulator-level identity and regulatory-capacity evidence only",
            "target_pair_scope": "not evidence for the queued exact pairs; no Module 22B edge or upstream relay inferred",
            "exportable": "false",
            "canonical_write_performed": "false",
            "limitations": "Regulator-level evidence does not establish presence in the target SCI cell, regulation of a queued target, downstream activation, or an upstream relay.",
        })
    register_rows.sort(key=lambda row: row["regulator_key"])
    write_tsv(register_path, EVIDENCE_FIELDS, register_rows)

    summary = {
        "status": "staging_only",
        "batch_id": "public_tf_evidence_batch_001",
        "source_set_ranks_reviewed": list(range(1, 26)),
        "pair_rows_reviewed": len(merged_pairs),
        "unique_regulators_reviewed": len({row["regulator_key"] for row in merged_pairs}),
        "exact_pair_support_rows": 0,
        "partial_functional_pair_rows": sum(row["exact_pair_status"].startswith("partial_") for row in merged_pairs),
        "evidence_register_rows": len(register_rows),
        "general_regulator_evidence_rows": sum(row["evidence_layer"] == "regulator_identity_and_regulatory_capacity" for row in register_rows),
        "target_cell_presence_rows_promoted": 0,
        "binding_or_association_rows_promoted": 0,
        "downstream_expression_or_perturbation_rows_promoted": 0,
        "upstream_relay_rows_promoted": 0,
        "exportable_pair_rows": 0,
        "canonical_writes_performed": False,
        "module22b_promotions_performed": False,
        "provenance_preserved": True,
        "remaining_batch_source_set_ranks": [],
        "outputs": [str(local_path.relative_to(ROOT)), str(register_path.relative_to(ROOT))],
        "decision": "Keep all 100 reviewed database-attributed memberships as search leads. Retain ZNF580-to-ABCA1 as partial functional staging evidence only; keep regulator-level literature separate from target-pair evidence and do not promote any pair.",
    }
    (args.directory / "batch_001_evidence_review_summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (args.directory / "EVIDENCE_REVIEW_BATCH001.md").write_text(
        "# Evidence review: public TF batch 001\n\n"
        "This bounded pass reviewed all source-set ranks 1-25 (100 exact regulator-target pairs). "
        "ZNF580-to-ABCA1 has partial functional support in human THP-1 oxLDL foam cells, but lacks direct binding and independent corroboration and remains staging-only. "
        "The other exact pairs had no defensible exact regulator-target-species result in these bounded lanes. "
        "Regulator-level literature is kept in a separate register and cannot promote a queued target pair. No canonical or Module 22B writes were performed.\n\n"
        "Near matches are recorded as exclusions so that evidence for another regulator, target, species, or pathway cannot silently migrate onto a queued pair.\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
