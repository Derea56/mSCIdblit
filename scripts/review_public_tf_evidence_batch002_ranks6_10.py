#!/usr/bin/env python3
"""Stage the bounded literature review for batch 002 ranks 6--10.

The TFLink rows are candidate search leads only.  This script records exact
pair review outcomes and a separate regulator-level evidence register.  It
does not write canonical TF, regulon, signaling, or Module 22B records.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import quote_plus


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH = ROOT / (
    "data/processed/public_tf_union_expansion_v1/"
    "current_set_crosswalk_v1/candidate_triage_v1/evidence_batches/batch_002/"
    "public_tf_evidence_collection_batch_002.tsv"
)
DEFAULT_OUTPUT = DEFAULT_BATCH.parent

PAIR_FIELDS = [
    "review_id", "batch_id", "batch_rank", "regulator_key", "regulator_symbol",
    "species_scope", "source_registry", "source_record_id", "raw_tf_symbol",
    "target_symbol", "target_graph_modules", "candidate_membership_status",
    "exact_pair_search_url", "exact_pair_status", "regulator_general_evidence_status",
    "target_cell_presence_status", "binding_or_association_status",
    "downstream_expression_or_perturbation_status", "downstream_activation_status",
    "upstream_relay_status", "disposition", "primary_citation",
    "corroborating_citation", "regulator_general_primary_citation",
    "regulator_general_corroborating_citation", "near_match_exclusions",
    "review_notes", "exportable", "canonical_write_performed",
]

REGISTER_FIELDS = [
    "evidence_id", "regulator_key", "regulator_symbol", "species_scope",
    "evidence_layer", "support_kind", "cell_or_model", "assay_or_perturbation",
    "observation", "effect_direction", "primary_citation", "corroborating_citation",
    "route_or_module_relevance", "target_pair_scope", "exportable",
    "canonical_write_performed", "limitations",
]


REGULATOR_GENERAL = {
    "mxd3": {
        "symbol": "MXD3",
        "species": "human",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3393725/",
        "corroborating": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4387021/",
        "model": "human DAOY medulloblastoma and Reh precursor-B-ALL cells",
        "assay": "MXD3 ChIP-chip with expression profiling; independent shRNA knockdown/rescue",
        "observation": "MXD3 is supported as a nuclear transcriptional regulator with validated targets in other programs, including ZNF577, RUNX1T1, MYCL1, and C10orf120 in DAOY cells; the queued ABCA1/ACKR2/ACVR1/ACVR1C pairs were not established.",
        "direction": "context-dependent regulatory effects; queued-pair direction not established",
        "near": "ABCA1 promoter work identifies SP1/SP3, E-box, and AP1 elements but not MXD3 (https://pmc.ncbi.nlm.nih.gov/articles/PMC16657/); ACVR1/ACVR1C receptor studies and ACKR2 studies without MXD3 were excluded.",
    },
    "fezf1": {
        "symbol": "FEZF1",
        "species": "human",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6218770/",
        "corroborating": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8616448/",
        "model": "human HeLa and Ewing-sarcoma cell models; developmental mouse work used only as regulator background",
        "assay": "FEZF1 ChIP/ChIP-seq with perturbation and expression profiling",
        "observation": "FEZF1 is supported as a sequence-specific transcriptional regulator with occupancy and perturbation evidence for neural/Wnt-related programs in other contexts; the queued ACKR2/ACTR2/ACVR1/ACVR1C pairs were not established.",
        "direction": "context-dependent activating/repressive effects; queued-pair direction not established",
        "near": "FEZF1 developmental and Wnt-target studies did not report the queued targets; ACVR1 promoter studies naming other factors and ACKR2/ACTR2/ACVR1C studies without FEZF1 were excluded.",
    },
    "scrt1": {
        "symbol": "SCRT1",
        "species": "human",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12633387/",
        "corroborating": "https://pmc.ncbi.nlm.nih.gov/articles/PMC2818459/",
        "model": "human HEK293T enhancer/TF perturbation model and neuronal P19 context",
        "assay": "CRISPR knockout with STARR-seq/RNA-seq; promoter/regulator-context experiments",
        "observation": "SCRT1 is supported as a transcriptional regulator/repressor in experimental human and neuronal contexts; the queued ABCA1/ACVR1/ADAM9/ADGRB3 pairs were not established.",
        "direction": "repressive or enhancer-dependent effects are context-specific; queued-pair direction not established",
        "near": "RIN1/SCRT1 co-expression and general neuronal repression context did not establish the queued pairs; ABCA1, ACVR1, ADAM9, and ADGRB3 studies without SCRT1 were excluded.",
    },
    "myt1l": {
        "symbol": "MYT1L",
        "species": "mouse",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11348803/",
        "corroborating": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8668036/",
        "model": "mouse fetal neurons, MEFs, neural stem cells, and primary hippocampal neurons",
        "assay": "MYT1L ChIP-seq with RNA-seq and shRNA/overexpression perturbation",
        "observation": "MYT1L is strongly supported as a direct transcriptional repressor of neuronal/non-neuronal identity programs, including direct Notch/HES1-related regulation; the queued Abca1/Ackr3/Actr2/Adam10 pairs were not established.",
        "direction": "predominantly repressive in the cited neuronal reprogramming context; queued-pair direction not established",
        "near": "Notch/HES1 and ADAM10 studies were treated as pathway or target-only context, not MYT1L-to-Adam10 evidence; Abca1, Ackr3, and Actr2 studies without MYT1L were excluded.",
    },
    "znf554": {
        "symbol": "ZNF554",
        "species": "human",
        "primary": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6092567/",
        "corroborating": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7461028/",
        "model": "human BeWo/HTR8/SVneo trophoblasts and U87 glioblastoma cells",
        "assay": "ZNF554 siRNA/overexpression with microarray or transcriptome profiling and functional assays",
        "observation": "ZNF554 is supported as a human KRAB-zinc-finger transcriptional regulator with perturbation-linked gene programs, including FSTL3 and trophoblast invasion/cancer signatures; the queued ACVR1/ADAM10/ADAM22/ADAM9 pairs were not established.",
        "direction": "context-dependent regulatory effects; queued-pair direction not established",
        "near": "ZNF554 perturbation papers report broad expression programs but no queued exact target edge; ACVR1, ADAM10, ADAM22, and ADAM9 studies without ZNF554 were excluded.",
    },
}


def exact_search_url(regulator: str, target: str, species: str) -> str:
    term = f'"{regulator}" AND "{target}" AND {species}'
    return "https://pubmed.ncbi.nlm.nih.gov/?term=" + quote_plus(term)


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    selected = [row for row in rows if 6 <= int(row["batch_rank"]) <= 10]
    if len(selected) != 20:
        raise ValueError(f"expected 20 rows for ranks 6-10, found {len(selected)}")
    return selected


def build_pair_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    output: list[dict[str, str]] = []
    for number, row in enumerate(rows, start=1):
        key = row["regulator_key"]
        general = REGULATOR_GENERAL[key]
        output.append({
            "review_id": f"public_tf_evidence_batch002_r6_10_pair_{number:03d}",
            "batch_id": row["batch_id"],
            "batch_rank": row["batch_rank"],
            "regulator_key": key,
            "regulator_symbol": row["raw_tf_symbol"],
            "species_scope": row["species_scope"],
            "source_registry": row["source_registry"],
            "source_record_id": row["source_record_id"],
            "raw_tf_symbol": row["raw_tf_symbol"],
            "target_symbol": row["target_symbol"],
            "target_graph_modules": row["target_graph_modules"],
            "candidate_membership_status": row["candidate_membership_status"],
            "exact_pair_search_url": exact_search_url(row["raw_tf_symbol"], row["target_symbol"], row["species_scope"]),
            "exact_pair_status": "no_exact_pair_support_found_in_bounded_search",
            "regulator_general_evidence_status": "supported_general_regulator_evidence",
            "target_cell_presence_status": "not_established_for_exact_pair",
            "binding_or_association_status": "not_found_for_exact_pair",
            "downstream_expression_or_perturbation_status": "not_found_for_exact_pair",
            "downstream_activation_status": "not_assessed",
            "upstream_relay_status": "not_tested_for_exact_pair",
            "disposition": "retain_database_candidate_as_search_lead_only",
            "primary_citation": "none located",
            "corroborating_citation": "none located",
            "regulator_general_primary_citation": general["primary"],
            "regulator_general_corroborating_citation": general["corroborating"],
            "near_match_exclusions": general["near"],
            "review_notes": "Regulator-level literature is not evidence for this exact regulator-target-species pair. Database membership, motif-only evidence, co-expression, pathway inference, and cross-species matches were not used for promotion.",
            "exportable": "false",
            "canonical_write_performed": "false",
        })
    return output


def build_register_rows() -> list[dict[str, str]]:
    output = []
    for key, general in REGULATOR_GENERAL.items():
        output.append({
            "evidence_id": f"public_tf_evidence_batch002_regulator_{key}",
            "regulator_key": key,
            "regulator_symbol": general["symbol"],
            "species_scope": general["species"],
            "evidence_layer": "regulator_identity_and_regulatory_capacity",
            "support_kind": "primary_literature_regulator_level",
            "cell_or_model": general["model"],
            "assay_or_perturbation": general["assay"],
            "observation": general["observation"],
            "effect_direction": general["direction"],
            "primary_citation": general["primary"],
            "corroborating_citation": general["corroborating"],
            "route_or_module_relevance": "regulator-level identity/capacity only; no Module 20-24 route or relay inferred",
            "target_pair_scope": "not evidence for any queued batch 002 ranks 6-10 exact pair",
            "exportable": "false",
            "canonical_write_performed": "false",
            "limitations": "These citations establish that the regulator can act in the cited model. They do not establish presence in the target SCI cell, a queued target edge, downstream activation, or an upstream signaling relay.",
        })
    return output


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_summary(output: Path, pair_rows: list[dict[str, str]]) -> None:
    summary = {
        "status": "staging_only",
        "review_scope": "batch_002 ranks 6-10",
        "pair_rows": len(pair_rows),
        "unique_regulators": len({row["regulator_key"] for row in pair_rows}),
        "exact_pair_support_rows": 0,
        "no_exact_pair_support_rows": len(pair_rows),
        "regulator_general_evidence_rows": len(REGULATOR_GENERAL),
        "exportable_rows": 0,
        "canonical_writes_performed": False,
        "module22b_promotions_performed": False,
        "evidence_policy": "Exact regulator-target-species evidence is required for promotion. General regulator evidence is retained in a separate register and is not attached to target pairs.",
    }
    (output / "batch002_ranks6_10_evidence_review_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n"
    )

    lines = [
        "# Evidence review: public TF batch 002 ranks 6-10",
        "",
        "This is a bounded PubMed/PMC primary-literature review of 20 exact TFLink search leads.",
        "No exact regulator-target-species pair was promoted. Regulator-level evidence is stored separately.",
        "",
        "## Result",
        "",
        f"- Exact pair rows reviewed: {len(pair_rows)}",
        "- Exact pair support: 0",
        "- Regulator-level registers: 5",
        "- Target-cell presence established for an exact pair: 0",
        "- Direct exact binding/association found: 0",
        "- Exact downstream direction found: 0",
        "- Directly tested upstream relay: 0",
        "- Canonical/module writes: 0",
        "",
        "## Interpretation",
        "",
        "The regulator papers establish activity of MXD3, FEZF1, SCRT1, MYT1L, or ZNF554 in other models, but do not establish the queued target edges. Database membership, co-expression, motif-only evidence, pathway-only evidence, and cross-species matches were excluded.",
        "",
        "All rows remain database-attributed candidate search leads only.",
    ]
    (output / "EVIDENCE_REVIEW_BATCH002_RANKS6_10.md").write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    pair_rows = build_pair_rows(read_rows(args.batch))
    register_rows = build_register_rows()
    write_tsv(args.output / "public_tf_evidence_review_batch002_ranks6_10.tsv", PAIR_FIELDS, pair_rows)
    write_tsv(args.output / "public_tf_evidence_review_batch002_ranks6_10_regulator_register.tsv", REGISTER_FIELDS, register_rows)
    write_summary(args.output, pair_rows)
    print(f"wrote {len(pair_rows)} pair rows and {len(register_rows)} regulator rows")


if __name__ == "__main__":
    main()
