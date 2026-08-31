#!/usr/bin/env python3
"""Build a conservative, paper-linked A-E/U and L0-L4 grading ledger.

The ledger is staging/audit output only. It never writes canonical database
rows. Rule-based grades are emitted only where the existing register explicitly
identifies the source class; all other cases remain review_required rather than
being guessed from a confidence tier.
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTER_ROOT = ROOT / "work" / "module_b_consolidation"
PHASE2 = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review" / "module20_24_integrated_phase2_extractions.tsv"
OUT = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review" / "module20_24_evidence_grade_ledger.tsv"
REPORT = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review" / "module20_24_evidence_grade_ledger_report.md"
MODULES = ("20B", "21B", "22B", "23B", "24B")

FIELDS = [
    "module", "b_edge_id", "b_evidence_id", "source_kind", "support_kind",
    "source_scope", "source_locator", "species_support", "evidence_layer",
    "exportable", "confidence_tier", "citation_note", "evidence_grade", "context_level",
    "grading_status", "grading_basis", "paper_keys", "paper_row_count",
    "observation_statuses", "claim_statuses", "context_basis", "limitations",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def register(module: str) -> list[dict[str, str]]:
    lower = module.lower()
    return read_tsv(REGISTER_ROOT / f"module{lower}" / f"module{lower}_evidence_register.tsv")


def stable_papers(value: str) -> list[str]:
    return sorted(set(re.findall(r"(?:PMID|PMCID|DOI):\S+", value or "", flags=re.I)))


def grade_rule(row: dict[str, str]) -> tuple[str, str, str]:
    source = " ".join(row.get(k, "") for k in ("source_kind", "support_kind", "source_scope")).lower()
    locator = row.get("source_locator", "")
    if any(token in source for token in ("negative_evidence", "search_boundary", "no_evidence_boundary", "no_exact_primary")):
        return "E", "rule_based_provisional", "Reviewed negative/bounded or no-exact-primary evidence; non-promotable by the rubric."
    if "unresolved" in source or not locator.strip():
        return "U", "rule_based_provisional", "Source is explicitly unresolved or lacks a source locator; no grade inferred."
    if "primary_experiment_plus_independent_corroboration" in source:
        return "A", "rule_based_provisional", "Register explicitly records primary experiment plus independent corroboration."
    if "primary_experiment" in source or "primary_research" in source or "primary_" in source:
        if stable_papers(locator):
            return "B", "rule_based_provisional", "Register identifies a traceable primary source; independent corroboration was not explicitly recorded on this row."
    if "database_curated" in source or "profile" in source or "membership" in source or "catalog" in source:
        return "D", "rule_based_provisional", "Register identifies database/profile/membership-only support."
    return "", "review_required", "Existing fields do not safely distinguish A-E/U without paper-level adjudication."


def phase2_primary_grade(linked: list[dict[str, str]]) -> tuple[str, str, str]:
    """Use an exact validated Phase-2 paper route when the register label is blank."""
    blocked = ("abstract", "metadata", "unresolved", "boundary", "not_required", "no_pair", "unknown")
    for item in linked:
        observation_status = item.get("observation_status", "").lower()
        claim_status = item.get("claim_status", "").lower()
        observation_text = item.get("observation_value_or_blocker", "").strip()
        claim_text = item.get("claim_text_or_blocker", "").strip()
        if not observation_status.startswith("validated") or not claim_status.startswith("validated"):
            continue
        if any(token in observation_status or token in claim_status for token in blocked):
            continue
        if len(observation_text) < 40 or len(claim_text) < 40:
            continue
        if "do_not_create" in observation_text.lower() or "do_not_create" in claim_text.lower():
            continue
        paper_anchor = stable_papers(item.get("canonical_paper_key", ""))
        if not paper_anchor:
            paper_anchor = stable_papers(item.get("source_locator", ""))
        if paper_anchor:
            return (
                "B",
                "phase2_primary_route",
                "The exact Phase-2 row has a stable primary paper anchor plus validated observation and claim text; independent corroboration is not recorded on this row.",
            )
    return "", "review_required", "Existing register labels and linked Phase-2 rows do not safely support a final A-E/U grade."


def context_rule(row: dict[str, str]) -> tuple[str, str, str]:
    # Limitations frequently say "no SCI model". They are retained in the
    # ledger but are not positive context evidence, so do not use them to
    # assign L2-L4.
    text = " ".join(row.get(k, "") for k in ("species_support", "source_scope", "evidence_summary", "citation_note")).lower()
    # A limitation such as "no SCI model" must not become positive L4
    # evidence merely because the string SCI appears in the record.
    negative_context = re.compile(
        r"\b(?:no|not|without|rather than|instead of|lacks?|lack(?:ing)?|does not|did not)\b"
        r"[^.;]{0,100}\b(?:sci|spinal[- ]cord(?: tissue| injury)?)\b",
    )
    positive_text = " ".join(
        sentence for sentence in re.split(r"[.;]", text)
        if not negative_context.search(sentence)
    )
    boundary = " ".join(row.get(k, "") for k in ("source_kind", "support_kind", "source_scope", "evidence_layer")).lower()
    if any(token in boundary for token in ("negative_evidence", "search_boundary", "no_evidence_boundary", "no_exact_primary", "boundary")):
        return "L0", "rule_based_provisional", "The record is a negative/bounded or boundary record and therefore does not establish context for the exact asserted relationship."
    if any(token in positive_text for token in ("spinal cord injury", "spinal-cord injury", "sci model", "after sci", "post-injury")):
        return "L4", "rule_based_provisional", "Register text explicitly identifies spinal-cord injury context."
    if any(token in positive_text for token in ("spinal cord tissue", "spinal-cord tissue", "spinal cord", "spinal-cord")):
        return "L3", "rule_based_provisional", "Register text explicitly identifies spinal-cord tissue context without an explicit injury claim."
    if any(token in positive_text for token in ("cns", "brain", "cortical", "cerebral", "neural", "neuron", "retina")):
        return "L2", "rule_based_provisional", "Register text identifies a CNS system but not spinal-cord tissue or SCI."
    primary_or_review = any(token in boundary for token in ("primary", "review", "experiment", "research", "pubmed", "pmcid"))
    if primary_or_review and (row.get("source_locator", "").strip() or row.get("species_support", "").strip()):
        return "L1", "rule_based_provisional", "A source or species context is present, but no CNS, spinal-cord, or SCI context is explicitly established."
    return "L0", "rule_based_provisional", "No qualifying context is present in the register fields."


def main() -> None:
    phase2 = read_tsv(PHASE2) if PHASE2.exists() else []
    phase_index: dict[str, list[dict[str, str]]] = {}
    for row in phase2:
        phase_index.setdefault((row["module"], row["b_evidence_id"]), []).append(row)

    output: list[dict[str, str]] = []
    grade_counts = Counter()
    context_counts = Counter()
    status_counts = Counter()
    for module in MODULES:
        for row in register(module):
            key = (module, row["b_evidence_id"])
            linked = phase_index.get(key, [])
            grade, grade_status, grade_basis = grade_rule(row)
            if not grade:
                grade, grade_status, grade_basis = phase2_primary_grade(linked)
            context, context_status, context_basis = context_rule(row)
            status = "review_required" if grade_status == "review_required" or context_status == "review_required" else "rule_based_provisional"
            papers = sorted({paper for item in linked for paper in stable_papers(item.get("canonical_paper_key", ""))})
            observations = sorted({item.get("observation_status", "") for item in linked if item.get("observation_status", "")})
            claims = sorted({item.get("claim_status", "") for item in linked if item.get("claim_status", "")})
            record = {field: "" for field in FIELDS}
            record.update({
                "module": module,
                "b_edge_id": row.get("b_edge_ids", ""),
                "b_evidence_id": row["b_evidence_id"],
                "source_kind": row.get("source_kind", ""),
                "support_kind": row.get("support_kind", ""),
                "source_scope": row.get("source_scope", ""),
                "source_locator": row.get("source_locator", ""),
                "species_support": row.get("species_support", ""),
                "evidence_layer": row.get("evidence_layer", ""),
                "exportable": row.get("exportable", ""),
                "confidence_tier": row.get("confidence_tier", ""),
                "citation_note": row.get("citation_note", ""),
                "evidence_grade": grade,
                "context_level": context,
                "grading_status": status,
                "grading_basis": grade_basis,
                "paper_keys": "; ".join(papers),
                "paper_row_count": str(len(linked)),
                "observation_statuses": "; ".join(observations),
                "claim_statuses": "; ".join(claims),
                "context_basis": context_basis,
                "limitations": row.get("limitations", ""),
            })
            output.append(record)
            grade_counts[(module, grade or "UNASSIGNED")] += 1
            context_counts[(module, context)] += 1
            status_counts[(module, status)] += 1

    with OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(output)

    lines = [
        "# Module 20B–24B evidence grade ledger",
        "",
        "This is staging/audit output. It does not write canonical database rows.",
        "Rule-based provisional values are derived from explicit register labels",
        "or an exact validated Phase-2 primary-paper route; remaining unassigned",
        "grades require paper-level adjudication.",
        "",
        f"- Evidence records: {len(output):,}",
        f"- Phase-2 linked rows available: {len(phase2):,}",
        "",
        "## Grade counts",
        "",
        "| Module | A | B | C | D | E | U | Unassigned |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for module in MODULES:
        values = [grade_counts[(module, grade)] for grade in ("A", "B", "C", "D", "E", "U", "UNASSIGNED")]
        lines.append(f"| {module} | " + " | ".join(f"{value:,}" for value in values) + " |")
    lines.extend([
        "",
        "## Context counts",
        "",
        "| Module | L0 | L1 | L2 | L3 | L4 |",
        "|---|---:|---:|---:|---:|---:|",
    ])
    for module in MODULES:
        values = [context_counts[(module, level)] for level in ("L0", "L1", "L2", "L3", "L4")]
        lines.append(f"| {module} | " + " | ".join(f"{value:,}" for value in values) + " |")
    lines.extend([
        "",
        "## Use",
        "",
        "- `evidence_grade` and `context_level` are independent and must be retained together with the written bases.",
        "- `grading_status=review_required` means the register fields do not safely support a final grade.",
        "- A stable paper anchor, experiment-level source locator, exact claim/observation, and scope match remain required before canonical materialization.",
        "",
    ])
    REPORT.write_text("\n".join(lines))
    print(f"ledger_rows={len(output)} phase2_rows={len(phase2)} report={REPORT}")


if __name__ == "__main__":
    main()
