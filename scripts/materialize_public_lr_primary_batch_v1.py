#!/usr/bin/env python3
"""Materialize a selected public-LR primary-evidence batch into Module 21B.

This is an evidence-layer materialization step. It does not assign mSCS route
confidence and it does not infer intracellular, TF, or target-gene links that
are absent from the reviewed primary evidence.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SUPPLEMENT = ROOT / "data/processed/public_database_comparison_v2/candidate_triage_v1/review_resolution_ledger.tsv"
DEFAULT_NORMALIZATION = ROOT / "data/processed/public_database_comparison_v2/candidate_triage_v1/candidate_normalization.tsv"
DEFAULT_MODULE = ROOT / "work/module_b_consolidation/module21b"
DEFAULT_AUDIT = DEFAULT_MODULE / "module21b_public_lr_materialization_batch002.tsv"

EDGE_FIELDS = [
    "b_edge_id", "source_entity", "relation_type", "target_entity", "pathway_name",
    "evidence_layer", "source_a_edge_id", "edge_status", "context_scope",
    "cell_type_context", "compartment_context", "species_context", "injury_context",
    "confidence_tier", "export_priority", "exportable", "consolidation_note",
]
EVIDENCE_FIELDS = [
    "b_evidence_id", "source_a_evidence_id", "b_edge_ids", "source_kind",
    "source_locator", "support_kind", "species_support", "source_scope",
    "confidence_tier", "citation_note", "evidence_summary", "limitations",
    "evidence_layer", "exportable", "consolidation_note",
]
AUDIT_FIELDS = [
    "candidate_unit_id", "b_edge_id", "b_evidence_id", "primary_locator",
    "previous_register_match", "materialization_status", "limitations",
]

BATCH_002 = {
    "LR:PTN>SDC2",
    "LR:EFNA3>EPHA5",
    "LR:EFNA5>EPHA8",
    "LR:JAG1>NOTCH4",
    "LR:SEMA5B>PLXNA3",
    "LR:BDNF>NGFR",
    "LR:CCL5>CCR4",
    "LR:CXCL13>CXCR3",
    "LR:GCG>GCGR",
    "LR:PRSS2>F2R",
    "LR:PRSS2>F2RL1",
}

# These rows are evidence-layer promotions only. Composite receptor labels are
# retained when the reviewed primary evidence is explicitly composite; the
# register does not expand them into unreported binary sub-edges.
BATCH_003 = {
    "LR:APOB>LRP2",
    "LR:APP>GPC1",
    "LR:APP>NGFR",
    "LR:COL4A1>ITGA3+ITGB1",
    "LR:COL4A3>ITGA2+ITGB1",
    "LR:CXCL2>ACKR1",
    "LR:EFNA4>EPHA1",
    "LR:EFNA4>EPHA3",
    "LR:EFNA4>EPHA5",
    "LR:EFNA4>EPHA6",
    "LR:EFNA5>EPHA1",
    "LR:EFNA5>EPHA5",
    "LR:EFNA5>EPHA6",
    "LR:FGF17>FGFR1",
    "LR:FGF17>FGFR2",
    "LR:FGF20>FGFR1",
    "LR:FGF20>FGFR2",
    "LR:FGF3>FGFR1",
    "LR:FGF3>FGFR2",
    "LR:FGF8>FGFR1",
    "LR:VIP>SCTR",
    "LR:CXCL1>CXCR1",
    "LR:CXCL5>CXCR1",
    "LR:FGF1>NRP1",
    "LR:IL16>CD9",
    "LR:KLK5>F2RL1",
    "LR:MSTN>ACVR1B+ACVR2A",
    "LR:MSTN>ACVR1B+ACVR2B",
    "LR:MSTN>ACVR2A+TGFBR1",
    "LR:MSTN>ACVR2B+TGFBR1",
    "LR:CTSG>FPR1",
    "LR:RAET1A>KLRK1",
    "LR:ALKAL1>ALK",
    "LR:CCL8>CCR8",
    "LR:CORT>MRGPRB2",
    "LR:L1CAM>ALCAM",
    "LR:PDGFB>PDGFRA+PDGFRB",
}

BATCH_004 = {
    "LR:TSHB>TSHR",
    "LR:PPY>NPY5R",
    "LR:CCL21A>CCR7",
}

BATCH_005 = {"LR:APOE>LRP2"}

BATCH_006 = {"LR:LAMC3>DAG1"}
BATCH_007 = {"LR:BMP15>BMPR1A"}
BATCH_008 = {"LR:COL1A2>CD44", "LR:COL2A1>SDC1", "LR:TRY4>F2RL1"}
BATCH_009 = {
    "LR:FGF2>SDC4",
    "LR:FGF2>CD44",
    "LR:COL4A1>SDC1",
    "LR:COL6A1>SDC1",
}
BATCH_010 = {"LR:CXCL10>SDC4"}

BATCHES = {"002": BATCH_002, "003": BATCH_003, "004": BATCH_004, "005": BATCH_005, "006": BATCH_006, "007": BATCH_007, "008": BATCH_008, "009": BATCH_009, "010": BATCH_010}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def next_id(rows: list[dict[str, str]], field: str, pattern: str) -> int:
    values = []
    for row in rows:
        match = re.fullmatch(pattern, row.get(field, "").strip())
        if match:
            values.append(int(match.group(1)))
    return max(values, default=0) + 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--review-ledger", dest="supplement", type=Path, default=DEFAULT_SUPPLEMENT,
                        help="Consolidated review ledger containing final primary-evidence dispositions")
    parser.add_argument("--batch", choices=sorted(BATCHES), default="002",
                        help="Materialization batch to run (default: 002)")
    parser.add_argument("--normalization", type=Path, default=DEFAULT_NORMALIZATION)
    parser.add_argument("--module-dir", type=Path, default=DEFAULT_MODULE)
    parser.add_argument("--audit-output", type=Path, default=DEFAULT_AUDIT)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    selected = BATCHES[args.batch]
    if args.audit_output == DEFAULT_AUDIT and args.batch != "002":
        args.audit_output = DEFAULT_MODULE / f"module21b_public_lr_materialization_batch{args.batch}.tsv"
    supplement = {row["candidate_unit_id"]: row for row in read_tsv(args.supplement)}
    normalization = {row["candidate_unit_id"]: row for row in read_tsv(args.normalization)}
    missing = sorted(selected - (set(supplement) & set(normalization)))
    if missing:
        raise SystemExit(f"selected candidates missing from review artifacts: {missing}")

    edge_path = args.module_dir / "module21b_edge_register.tsv"
    evidence_path = args.module_dir / "module21b_evidence_register.tsv"
    edges = read_tsv(edge_path)
    evidence = read_tsv(evidence_path)
    triples = {(row["source_entity"].upper(), row["target_entity"].upper()) for row in edges}
    existing_candidate_notes = " ".join(row.get("consolidation_note", "") for row in edges)
    if "candidate=LR:" in existing_candidate_notes:
        existing_candidate_ids = {
            token.split("=", 1)[1].rstrip(";,." )
            for token in re.findall(r"candidate=LR:[^;,.\s]+", existing_candidate_notes)
        }
    else:
        existing_candidate_ids = set()

    edge_start = next_id(edges, "b_edge_id", r"M21B-E(\d+)")
    evidence_start = next_id(evidence, "b_evidence_id", r"M21B-EVID-(\d+)")
    new_edges: list[dict[str, str]] = []
    new_evidence: list[dict[str, str]] = []
    audit: list[dict[str, str]] = []

    for offset, candidate_id in enumerate(sorted(selected)):
        res = supplement.get(candidate_id)
        norm = normalization.get(candidate_id)
        if res is None or norm is None:
            raise SystemExit(f"candidate {candidate_id} must be present in both supplement and normalization")
        if res["disposition"] != "new_primary_supported_edge_candidate":
            raise SystemExit(f"candidate {candidate_id} is not primary-supported: {res['disposition']}")
        if norm.get("matched_graph_edge_ids", ""):
            raise SystemExit(f"candidate {candidate_id} already maps to graph edge(s): {norm['matched_graph_edge_ids']}")
        if candidate_id in existing_candidate_ids:
            raise SystemExit(f"candidate {candidate_id} already has a materialization note")

        edge_id = f"M21B-E{edge_start + offset:06d}"
        evidence_id = f"M21B-EVID-{evidence_start + offset:06d}"
        source = norm["normalized_ligand_key"]
        target = norm["normalized_receptor_key"]
        relation = "binds/activates"
        if res["evidence_layer"] == "ligand_receptor_binding_or_activation":
            relation = "binds"
        pathway = f"{source}-{target}-primary-evidence"
        layer = res["evidence_layer"]
        locator = res["supporting_primary_locators"]
        species = res["species_support"] or "as stated in primary model/assay"
        note = (
            f"Primary-only materialization; candidate={candidate_id}; "
            f"review={res['review_status']}; primary={locator}. "
            "Evidence layer only; no mSCS route confidence or unreported downstream links inferred."
        )
        new_edges.append({
            "b_edge_id": edge_id,
            "source_entity": source,
            "relation_type": relation,
            "target_entity": target,
            "pathway_name": pathway,
            "evidence_layer": layer,
            "source_a_edge_id": "",
            "edge_status": "validated_primary_exact_layer",
            "context_scope": "Review-guided primary evidence; exact pair and reported layer bounded",
            "cell_type_context": "Primary model/assay described in the linked evidence record",
            "compartment_context": "extracellular ligand to plasma-membrane receptor or receptor complex",
            "species_context": species,
            "injury_context": res["limitations"],
            "confidence_tier": "medium-high",
            "export_priority": "medium",
            "exportable": "true",
            "consolidation_note": note,
        })
        new_evidence.append({
            "b_evidence_id": evidence_id,
            "source_a_evidence_id": "",
            "b_edge_ids": edge_id,
            "source_kind": "primary_research_paper",
            "source_locator": locator,
            "support_kind": "primary_experiment",
            "species_support": species,
            "source_scope": layer,
            "confidence_tier": "medium-high",
            "citation_note": f"Primary evidence harvested in public LR review {res['review_status']}; candidate={candidate_id}.",
            "evidence_summary": res["evidence_summary"],
            "limitations": res["limitations"],
            "evidence_layer": layer,
            "exportable": "true",
            "consolidation_note": note,
        })
        audit.append({
            "candidate_unit_id": candidate_id,
            "b_edge_id": edge_id,
            "b_evidence_id": evidence_id,
            "primary_locator": locator,
            "previous_register_match": "none",
            "materialization_status": "materialized_reviewed_primary",
            "limitations": res["limitations"],
        })

    if args.dry_run:
        print(f"would_materialize={len(new_edges)} first_edge={new_edges[0]['b_edge_id']} last_edge={new_edges[-1]['b_edge_id']}")
        return 0

    write_tsv(edge_path, edges + new_edges, EDGE_FIELDS)
    write_tsv(evidence_path, evidence + new_evidence, EVIDENCE_FIELDS)
    write_tsv(args.audit_output, audit, AUDIT_FIELDS)
    print(f"materialized={len(new_edges)} first_edge={new_edges[0]['b_edge_id']} last_edge={new_edges[-1]['b_edge_id']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
