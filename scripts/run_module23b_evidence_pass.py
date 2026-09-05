#!/usr/bin/env python3
"""Run the Module 23B A-E/U and L0-L5 evidence pass.

This is a staging/audit output only.  It does not modify the Module 23B
registers or canonical database tables.  A-E/U grading reuses the repository's
existing conservative grade rules.  The repository's existing context rubric
ends at L4, so this module-specific pass defines L5 explicitly as an
audit-only extension: the row names both an injury model and an SCI receiver
cell or lesion compartment for the asserted evidence unit.
"""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "work/module_b_consolidation/module23b/module23b_evidence_register.tsv"
OUT = ROOT / "work/module_b_consolidation/module23b/module23b_evidence_grade_context_pass_2026-09-05.tsv"
REPORT = ROOT / "work/module_b_consolidation/module23b/module23b_evidence_grade_context_pass_2026-09-05.md"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_module20_24_evidence_grade_ledger import grade_rule, stable_papers  # noqa: E402


FIELDS = [
    "module", "b_edge_ids", "b_evidence_id", "source_kind", "support_kind",
    "source_scope", "source_locator", "species_support", "evidence_layer",
    "exportable", "confidence_tier", "citation_note", "evidence_grade",
    "context_level", "grading_status", "grading_basis", "paper_keys",
    "context_basis", "limitations", "pass_disposition",
]

NEGATIVE_CONTEXT = re.compile(
    r"\b(?:no|not|without|rather than|instead of|lacks?|lack(?:ing)?|does not|did not)\b"
    r"[^.;]{0,100}\b(?:sci|spinal[- ]cord(?: tissue| injury)?|injur(?:y|ed|ies))\b",
    flags=re.I,
)

INJURY_CONTEXT = (
    "spinal cord injury", "spinal-cord injury", "sci model", "after sci",
    "post-injury", "contusion", "crush lesion", "dorsal-column crush",
    "transection", "hemisection", "lesion",
)
SCI_TOKEN = re.compile(r"\bsci\b", flags=re.I)
RECEIVER_CONTEXT = (
    "astrocyte", "microglia", "macrophage", "monocyte", "fibroblast",
    "neuron", "neuronal", "axon", "oligodendrocyte", "progenitor",
    "glial", "ependymal", "immune cell", "lesion core", "perivascular",
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def positive_context(row: dict[str, str]) -> str:
    # Limitations are intentionally excluded from positive context scoring.
    text = " ".join(
        row.get(field, "")
        for field in ("species_support", "source_scope", "evidence_summary", "citation_note")
    ).lower()
    return " ".join(
        sentence for sentence in re.split(r"[.;]", text)
        if not NEGATIVE_CONTEXT.search(sentence)
    )


def context_rule_l5(row: dict[str, str]) -> tuple[str, str]:
    text = positive_context(row)
    boundary = " ".join(
        row.get(field, "")
        for field in ("source_kind", "support_kind", "source_scope", "evidence_layer")
    ).lower()
    if any(token in boundary for token in ("negative_evidence", "search_boundary", "no_evidence_boundary", "boundary")):
        return "L0", "The row is a negative/bounded record and does not establish positive context for the asserted relationship."

    has_injury = any(token in text for token in INJURY_CONTEXT) or bool(SCI_TOKEN.search(text))
    has_receiver = any(token in text for token in RECEIVER_CONTEXT)
    if has_injury and has_receiver:
        return "L5", "The register explicitly names an injury model or lesion and an SCI receiver cell or lesion compartment."
    if has_injury:
        return "L4", "The register explicitly identifies spinal-cord injury or an injury model, but not an explicit receiver-cell/lesion-compartment match."
    if "spinal cord tissue" in text or "spinal-cord tissue" in text or "spinal cord" in text or "spinal-cord" in text:
        return "L3", "The register explicitly identifies spinal-cord tissue without an explicit injury-model claim."
    if any(token in text for token in ("cns", "brain", "cortical", "cerebral", "neural", "neuron", "retina")):
        return "L2", "The register identifies a CNS or neural system but not spinal-cord tissue or SCI."
    primary_or_review = any(token in boundary for token in ("primary", "review", "experiment", "pubmed", "pmcid"))
    if primary_or_review and (row.get("source_locator", "").strip() or row.get("species_support", "").strip()):
        return "L1", "A traceable source or species context is present, but no CNS, spinal-cord, or SCI context is established."
    return "L0", "No qualifying context is present in the register fields."


def main() -> None:
    rows = read_tsv(REGISTER)
    output: list[dict[str, str]] = []
    grade_counts: Counter[str] = Counter()
    context_counts: Counter[str] = Counter()
    disposition_counts: Counter[str] = Counter()

    for row in rows:
        grade, grade_status, grade_basis = grade_rule(row)
        if not grade:
            grade = "U"
        context, context_basis = context_rule_l5(row)
        status = "review_required" if grade_status == "review_required" else "rule_based_provisional"
        if grade == "U":
            status = "review_required"
        disposition = (
            "boundary_or_nonpromotable" if context == "L0" or grade == "E"
            else "review_required" if grade == "U"
            else "retain_for_adjudication"
        )
        record = {field: "" for field in FIELDS}
        record.update({
            "module": "23B",
            "b_edge_ids": row.get("b_edge_ids", ""),
            "b_evidence_id": row.get("b_evidence_id", ""),
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
            "paper_keys": "; ".join(
                sorted({
                    match.rstrip(";,. )")
                    for match in stable_papers(row.get("source_locator", ""))
                })
            ),
            "context_basis": context_basis,
            "limitations": row.get("limitations", "") or "Not separately recorded in source register.",
            "pass_disposition": disposition,
        })
        output.append(record)
        grade_counts[grade] += 1
        context_counts[context] += 1
        disposition_counts[disposition] += 1

    with OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(output)

    lines = [
        "# Module 23B A–E/U and L0–L5 evidence pass",
        "",
        "This is a staging/audit output. It does not modify the Module 23B",
        "registers, promote edges, or write canonical database tables.",
        "",
        "The A–E/U grade axis reuses the repository's existing conservative",
        "register-based rules. U means the current register fields do not safely",
        "support an A–E call. The existing repository rubric defines L0–L4; this",
        "pass adds L5 as an audit-only extension for explicit injury-model context",
        "plus an explicitly named SCI receiver cell or lesion compartment.",
        "",
        f"- Evidence records reviewed: {len(output):,}",
        f"- Output: `{OUT.relative_to(ROOT)}`",
        "",
        "## Evidence grade counts",
        "",
        "| Grade | Count |",
        "|---|---:|",
    ]
    lines.extend(f"| {grade} | {grade_counts[grade]:,} |" for grade in ("A", "B", "C", "D", "E", "U"))
    lines.extend([
        "",
        "## Context level counts",
        "",
        "| Level | Operational meaning | Count |",
        "|---|---|---:|",
        "| L0 | No positive context or negative/bounded record | " + f"{context_counts['L0']:,} |",
        "| L1 | Traceable source/species context; no CNS context | " + f"{context_counts['L1']:,} |",
        "| L2 | CNS/neural system | " + f"{context_counts['L2']:,} |",
        "| L3 | Spinal-cord tissue without explicit injury model | " + f"{context_counts['L3']:,} |",
        "| L4 | Explicit SCI/injury-model context without receiver-cell match | " + f"{context_counts['L4']:,} |",
        "| L5 | Explicit injury model plus SCI receiver cell/lesion compartment | " + f"{context_counts['L5']:,} |",
        "",
        "## Pass disposition",
        "",
        "| Disposition | Count |",
        "|---|---:|",
    ])
    lines.extend(f"| {name} | {disposition_counts[name]:,} |" for name in ("retain_for_adjudication", "review_required", "boundary_or_nonpromotable"))
    lines.extend([
        "",
        "No edge promotion or canonical materialization was performed. Grade and",
        "context remain independent axes; the written basis and limitations must",
        "travel with any later promotion review.",
        "",
    ])
    REPORT.write_text("\n".join(lines))
    print(f"module23b_rows={len(output)} report={REPORT}")


if __name__ == "__main__":
    main()
