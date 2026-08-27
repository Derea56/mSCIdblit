#!/usr/bin/env python3
"""Record a bounded, staging-only review of batch 002 ranks 11--15.

The input is the database-attributed TFLink search queue.  This script does
not change canonical TF, regulon, or Module 22B files.  Exact-pair evidence is
kept separate from regulator-level evidence so a paper about a different
target cannot promote a database membership edge.
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BATCH_DIR = (
    ROOT
    / "data/processed/public_tf_union_expansion_v1/current_set_crosswalk_v1"
    / "candidate_triage_v1/evidence_batches/batch_002"
)
INPUT = BATCH_DIR / "public_tf_evidence_collection_batch_002.tsv"
OUTPUT = BATCH_DIR / "public_tf_evidence_review_batch002_ranks11_15.tsv"
SUMMARY = BATCH_DIR / "ranks11_15_evidence_review_summary.json"
REPORT = BATCH_DIR / "EVIDENCE_REVIEW_RANKS11_15.md"


GENERAL = {
    "znf574": {
        "status": "supported_general_regulator_evidence_not_exact_target",
        "citations": (
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC12603413/ "
            "(ZNF574 promoter binding/repression of TRPM4; not a queued target); "
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC12101526/ "
            "(ribosome-surveillance function; transcriptional role remains open)"
        ),
        "model": "Human cancer-cell and ribosome-surveillance studies; no queued target pair tested.",
    },
    "mynn": {
        "status": "supported_general_regulator_evidence_not_exact_target",
        "citations": (
            "https://pubmed.ncbi.nlm.nih.gov/10873615/ "
            "(human/mouse myoneurin expression and BTB/POZ-zinc-finger identity); "
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC9194458/ "
            "(MYNN interaction with SMAD/Ppm1a and BMP signaling; not ACVR1 regulation)"
        ),
        "model": "Human/mouse expression plus zebrafish and mammalian BMP/SMAD studies; no queued target pair tested.",
    },
    "zbtb42": {
        "status": "supported_identity_and_regulator_context_not_exact_target",
        "citations": (
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC3057000/ "
            "(human/mouse transcript, protein, nuclear localization, and zinc-finger domains); "
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC4240208/ "
            "(zebrafish loss-of-function/rescue muscle phenotype; no queued target)"
        ),
        "model": "Human skeletal muscle, mouse myotubes/tissues, and zebrafish muscle development; no queued target pair tested.",
    },
    "fezf2": {
        "status": "supported_general_regulator_evidence_not_exact_target",
        "citations": (
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC3099680/ "
            "(direct Fezf2 DNA binding and reporter activity; eomesa/tbr2 and lhx2b targets, not queued); "
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC7529949/ "
            "(mouse Fezf2 perturbation and ChIP-seq target-program work, not queued targets)"
        ),
        "model": "Zebrafish forebrain and mouse neural progenitor/cortical studies; no queued target pair tested.",
    },
    "znf207": {
        "status": "supported_general_regulator_evidence_not_exact_target",
        "citations": (
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC6197280/ "
            "(human hESC ChIP/functional target-program evidence, including non-queued genes); "
            "https://pubmed.ncbi.nlm.nih.gov/24462186/ "
            "(BuGZ/ZNF207-BUB3 mitotic function, not transcriptional target evidence); "
            "https://pubmed.ncbi.nlm.nih.gov/35246476/ "
            "(human HCC ZNF207→IDO1 mechanism, not a queued target)"
        ),
        "model": "Human hESC, cancer-cell, and mitotic studies; no queued target pair tested.",
    },
}


NEAR_MATCHES = {
    ("znf574", "ACVR1"): "ACVR1 developmental/receptor papers and ZNF574 non-queued TRPM4 papers; no ZNF574-ACVR1 assay.",
    ("znf574", "ACVR1C"): "ACVR1C receptor/metabolic papers and ZNF574 non-queued TRPM4 papers; no ZNF574-ACVR1C assay.",
    ("znf574", "ADAM22"): "ADAM22/LGI1 neuronal receptor studies and ZNF574 non-queued studies; no ZNF574-ADAM22 assay.",
    ("znf574", "ADGRE5"): "ADGRE5/CD97 receptor-signaling studies and ZNF574 non-queued studies; no ZNF574-ADGRE5 assay.",
    ("mynn", "ACKR1"): "ACKR1/DARC expression and knockout studies; no MYNN binding or perturbation of ACKR1.",
    ("mynn", "ACTR2"): "ACTR2/ARP2 cytoskeletal and platelet studies; no MYNN binding or perturbation of ACTR2.",
    ("mynn", "ACVR1"): "MYNN-BMP/SMAD signaling is pathway-level and does not show ACVR1 transcriptional regulation; ACVR1 studies naming other regulators excluded.",
    ("mynn", "ACVRL1"): "ACVRL1/ALK1 promoter and vascular studies; no MYNN binding or perturbation of ACVRL1.",
    ("zbtb42", "ACVR1"): "ACVR1 developmental studies and ZBTB42 muscle studies are separate; no ZBTB42-ACVR1 assay.",
    ("zbtb42", "ADAM23"): "ADAM23/LGI neuronal receptor studies; no ZBTB42 binding or perturbation of ADAM23.",
    ("zbtb42", "ADGRB3"): "ADGRB3/BAI3 synapse studies; no ZBTB42 binding or perturbation of ADGRB3.",
    ("zbtb42", "ADGRE5"): "ADGRE5/CD97 receptor-signaling studies; no ZBTB42 binding or perturbation of ADGRE5.",
    ("fezf2", "A2m"): "FEZF2 target studies identify non-queued neural targets; A2M expression studies do not test FEZF2.",
    ("fezf2", "Ackr3"): "FEZF2 and ACKR3/CXCR7 appear in neuronal expression or marker studies, but no direct regulatory edge was tested.",
    ("fezf2", "Actr2"): "ACTR2/ARP2 studies; no FEZF2 binding or perturbation of Actr2.",
    ("fezf2", "Acvr1"): "FEZF2/ACVR1 co-expression or developmental brain studies do not establish binding or downstream regulation.",
    ("znf207", "ABCA1"): "ABCA1 regulation by LXR/miR-33 and other factors; no ZNF207 binding or perturbation of ABCA1.",
    ("znf207", "ACTR2"): "ACTR2/ARP2 studies; no ZNF207 binding or perturbation of ACTR2.",
    ("znf207", "ADAM10"): "ADAM10 sheddase/Notch studies; no ZNF207 binding or perturbation of ADAM10.",
    ("znf207", "ADAM17"): "ADAM17 sheddase/EGFR-cytokine studies; no ZNF207 binding or perturbation of ADAM17.",
}


def exact_search_url(regulator: str, target: str, species: str) -> str:
    return (
        "https://pubmed.ncbi.nlm.nih.gov/?term="
        f"%22{regulator}%22+AND+%22{target}%22+AND+{species}"
    )


def main() -> None:
    with INPUT.open(newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    rows = [row for row in rows if 11 <= int(row["batch_rank"]) <= 15]
    if len(rows) != 20:
        raise SystemExit(f"expected 20 rows for ranks 11-15, found {len(rows)}")

    fieldnames = [
        "review_id",
        "batch_id",
        "batch_rank",
        "regulator_key",
        "regulator_symbol",
        "species_scope",
        "source_registry",
        "source_record_id",
        "raw_tf_symbol",
        "target_symbol",
        "target_graph_modules",
        "candidate_membership_status",
        "exact_pair_search_url",
        "exact_pair_status",
        "regulator_general_evidence_status",
        "regulator_level_citations",
        "cell_or_model_context",
        "target_cell_presence_status",
        "binding_or_association_status",
        "downstream_expression_or_perturbation_status",
        "downstream_activation_status",
        "upstream_relay_status",
        "disposition",
        "primary_citation",
        "corroborating_citation",
        "near_match_exclusions",
        "review_notes",
        "exportable",
        "canonical_write_performed",
    ]

    out_rows = []
    for index, row in enumerate(rows, start=1):
        key = row["regulator_key"]
        target = row["target_symbol"]
        general = GENERAL[key]
        out_rows.append(
            {
                "review_id": f"public_tf_evidence_batch002_pair_{index:03d}",
                "batch_id": row["batch_id"],
                "batch_rank": row["batch_rank"],
                "regulator_key": key,
                "regulator_symbol": row["display_symbols"],
                "species_scope": row["species_scope"],
                "source_registry": row["source_registry"],
                "source_record_id": row["source_record_id"],
                "raw_tf_symbol": row["raw_tf_symbol"],
                "target_symbol": target,
                "target_graph_modules": row["target_graph_modules"],
                "candidate_membership_status": row["candidate_membership_status"],
                "exact_pair_search_url": exact_search_url(
                    row["raw_tf_symbol"], target, row["species_scope"]
                ),
                "exact_pair_status": "no_exact_pair_support_found_in_bounded_search",
                "regulator_general_evidence_status": general["status"],
                "regulator_level_citations": general["citations"],
                "cell_or_model_context": general["model"],
                "target_cell_presence_status": "not_established_for_exact_pair",
                "binding_or_association_status": "not_found_for_exact_pair",
                "downstream_expression_or_perturbation_status": "not_found_for_exact_pair",
                "downstream_activation_status": "not_assessed",
                "upstream_relay_status": "not_tested_for_exact_pair",
                "disposition": "retain_database_candidate_as_search_lead_only",
                "primary_citation": "",
                "corroborating_citation": "",
                "near_match_exclusions": NEAR_MATCHES[(key, target)],
                "review_notes": (
                    "No exact regulator-target-species evidence was located in the bounded PubMed/PMC review. "
                    "Regulator-level citations are retained separately and are not evidence for this pair. "
                    "Database membership, co-expression, motif-only, pathway-only, and cross-species observations "
                    "were not used for promotion."
                ),
                "exportable": "false",
                "canonical_write_performed": "false",
            }
        )

    with OUTPUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(out_rows)

    summary = {
        "batch_id": "public_tf_evidence_batch_002",
        "review_scope": "batch ranks 11-15",
        "input": str(INPUT.relative_to(ROOT)),
        "output": str(OUTPUT.relative_to(ROOT)),
        "rows_reviewed": len(out_rows),
        "unique_regulators": len({row["regulator_key"] for row in out_rows}),
        "unique_exact_pairs": len({(row["regulator_key"], row["target_symbol"], row["species_scope"]) for row in out_rows}),
        "exact_pair_status_counts": dict(Counter(row["exact_pair_status"] for row in out_rows)),
        "regulator_general_evidence_status_counts": dict(Counter(row["regulator_general_evidence_status"] for row in out_rows)),
        "exact_primary_citations": 0,
        "exact_corroborating_citations": 0,
        "exportable_rows": 0,
        "canonical_writes": 0,
        "promotion_decision": "none",
        "limitations": [
            "No-exact-support is bounded to the PubMed/PMC primary-literature searches recorded per row; it is not a global absence claim.",
            "Regulator-level evidence for a different target is not attached to any queued pair.",
            "Target-cell presence, downstream activation, and upstream relay remain unassessed for the exact pairs.",
        ],
    }
    SUMMARY.write_text(json.dumps(summary, indent=2) + "\n")

    report_lines = [
        "# Evidence review: public TF batch 002 ranks 11-15",
        "",
        "This staging-only review covers 20 exact TFLink regulator-target-species search leads for ZNF574, MYNN, ZBTB42, FEZF2, and ZNF207.",
        "",
        "## Result",
        "",
        "- 20 exact pairs reviewed; 0 had qualifying exact pair support.",
        "- 5 regulators had literature-level context, but those papers concerned identity, pathway behavior, or non-queued targets and were not attached to the queued pairs.",
        "- 0 records are exportable, 0 canonical writes were performed, and 0 Module 22B entries were changed.",
        "- Target-cell presence, direct binding/association, downstream direction, and upstream relay remain unestablished for every exact pair in this slice.",
        "",
        "## Regulator-level evidence kept separate",
        "",
        "- ZNF574: direct promoter/regulatory evidence exists for TRPM4, not ACVR1, ACVR1C, ADAM22, or ADGRE5; separate ribosome-surveillance work cautions that its broader transcriptional role remains unresolved.",
        "- MYNN: MYNN has expression/identity evidence and a MYNN-SMAD/Ppm1a mechanism affecting BMP signaling, but this does not demonstrate regulation of ACVR1 or ACVRL1.",
        "- ZBTB42: human/mouse expression and nuclear localization plus zebrafish muscle loss-of-function/rescue evidence exist, without a queued target gene.",
        "- FEZF2: direct DNA-binding and non-queued target-program evidence exists in neural models; none of the four queued targets was validated as a FEZF2 target.",
        "- ZNF207: hESC/cancer regulatory evidence and a distinct BuGZ mitotic role exist; none of ABCA1, ACTR2, ADAM10, or ADAM17 was validated as a ZNF207 target.",
        "",
        "The TSV contains the row-level PubMed query URL and the excluded near-match rationale. Database membership remains a search lead only.",
    ]
    REPORT.write_text("\n".join(report_lines) + "\n")


if __name__ == "__main__":
    main()
