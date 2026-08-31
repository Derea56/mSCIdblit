#!/usr/bin/env python3
"""Prepare the bounded repository-local Module 20B/21B review lane."""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_ROOT = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review"
OUT_TSV = OUT_ROOT / "lane_A_20B_21B.tsv"
OUT_MD = OUT_ROOT / "lane_A_20B_21B.md"

FIELDS = [
    "review_id", "module", "b_edge_id", "b_evidence_id", "evidence_layer",
    "support_kind", "canonical_paper_key", "paper_anchor_type",
    "paper_anchor_locator", "paper_resolution_status", "observation_status",
    "observation_key_or_action", "claim_status", "claim_key_or_action",
    "species", "cell_type_or_model", "assay_or_perturbation", "relation_type",
    "pathway_or_branch", "confidence", "source_scope",
    "context_and_limitations", "search_boundary", "reviewer_notes",
]


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def tokens(value: str) -> list[tuple[str, str]]:
    pattern = re.compile(r"PMID:\s*\d+|PMCID:\s*PMC\d+|DOI:\s*10\.[^;\s]+", re.I)
    result: list[tuple[str, str]] = []
    for token in pattern.findall(value or ""):
        token = token.strip()
        if token.upper().startswith("PMID:"):
            kind = "pmid"
            locator = "PMID:" + re.sub(r"\D", "", token)
        elif token.upper().startswith("PMCID:"):
            kind = "pmcid"
            locator = "PMCID:" + re.sub(r"\s+", "", token).upper().replace("PMCID:", "")
        else:
            kind = "doi"
            locator = "DOI:" + re.sub(r"^DOI:\s*", "", token, flags=re.I).lower()
        if (kind, locator) not in result:
            result.append((kind, locator))
    return result


def stable_key(kind: str, locator: str) -> str:
    return locator


def main() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    output: list[dict[str, str]] = []
    for module in (20, 21):
        root = ROOT / "work" / "module_b_consolidation" / f"module{module}b"
        edges = {row["b_edge_id"]: row for row in rows(root / f"module{module}b_edge_register.tsv")}
        evidence = rows(root / f"module{module}b_evidence_register.tsv")
        for record in evidence:
            if record.get("exportable") != "true":
                continue
            edge_ids = [item for item in record.get("b_edge_ids", "").split(";") if item]
            edge_rows = [edges[item] for item in edge_ids if item in edges]
            relation_types = sorted({row.get("relation_type", "") for row in edge_rows if row.get("relation_type")})
            pathways = sorted({row.get("pathway_name", "") for row in edge_rows if row.get("pathway_name")})
            cells = sorted({row.get("cell_type_context", "") for row in edge_rows if row.get("cell_type_context")})
            locators = tokens(record.get("source_locator", "")) if module == 21 else []
            if not locators:
                locators = [("", "")]
            for index, (anchor_type, anchor_locator) in enumerate(locators, start=1):
                if module == 20:
                    paper_status = "unresolved_identifier"
                    paper_key = ""
                    observation_status = "not_applicable_lr_release"
                    observation_action = "DO_NOT_CREATE: frozen Module 20A LR release is a source manifest anchor, not an atomic experiment record; retain the existing LR evidence layer."
                    claim_status = "not_applicable_lr_release"
                    claim_action = "DO_NOT_CREATE: no paper-level author claim is attached to the frozen LR manifest row."
                    boundary = "Repository-local boundary 2026-08-19: Module 20B source_locator is the frozen Module 20A LR manifest; no paper/figure/experiment locator is present in this B-layer row. Resolve the underlying Module 20A source before canonical Paper/Observation/Claim import."
                    notes = "20B LR provenance remains separate from 21B intracellular/pathway evidence; no Module 20A ledger or manifest was modified."
                else:
                    paper_status = "paper_ready"
                    paper_key = stable_key(anchor_type, anchor_locator)
                    observation_status = "required_bounded_creation"
                    observation_action = "CREATE_OBSERVATION_REQUIRED: extract one atomic measured/tested receptor-proximal or pathway result from the cited primary paper's Results/Methods/figure/table before insertion; do not infer the source locus from the B-layer summary."
                    claim_status = "required_bounded_creation"
                    claim_action = "CREATE_AUTHORCLAIM_REQUIRED: transcribe the explicit author interpretation from the cited primary paper after full-text verification; keep it separate from the observation."
                    boundary = "Repository-local anchor pass 2026-08-19: stable PMID/PMCID/DOI retained from the M21B evidence register; exact experiment/figure/claim extraction remains required before import."
                    notes = "21B receptor-proximal/pathway evidence is not ligand occupancy evidence; preserve receptor-complex, branch, species, model, and assay limitations."
                row = {
                    "review_id": f"M{module}B-CER-{record['b_evidence_id'].split('-')[-1]}-{index:02d}",
                    "module": f"M{module}B",
                    "b_edge_id": ";".join(edge_ids),
                    "b_evidence_id": record["b_evidence_id"],
                    "evidence_layer": record.get("evidence_layer", ""),
                    "support_kind": record.get("support_kind", ""),
                    "canonical_paper_key": paper_key,
                    "paper_anchor_type": anchor_type or "local_audit",
                    "paper_anchor_locator": anchor_locator or record.get("source_locator", ""),
                    "paper_resolution_status": paper_status,
                    "observation_status": observation_status,
                    "observation_key_or_action": observation_action,
                    "claim_status": claim_status,
                    "claim_key_or_action": claim_action,
                    "species": record.get("species_support", ""),
                    "cell_type_or_model": "; ".join(cells) or "not specified in B-layer register",
                    "assay_or_perturbation": "not specified at atomic experiment level in B-layer register; full-text extraction required",
                    "relation_type": "; ".join(relation_types),
                    "pathway_or_branch": "; ".join(pathways),
                    "confidence": record.get("confidence_tier", ""),
                    "source_scope": record.get("source_scope", ""),
                    "context_and_limitations": f"{record.get('evidence_summary', '')} | limitations: {record.get('limitations', '')}",
                    "search_boundary": boundary,
                    "reviewer_notes": f"{record.get('citation_note', '')} | {notes} | {record.get('consolidation_note', '')}",
                }
                output.append(row)

    with OUT_TSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(output)

    by_module = Counter(row["module"] for row in output)
    paper = Counter(row["paper_resolution_status"] for row in output)
    lines = [
        "# Lane A — Module 20B/21B canonical-evidence readiness",
        "",
        "This lane was prepared from repository-local B-layer registers only.",
        "It does not modify Module 20A ledgers, classifications, or the frozen",
        "manifest, and it does not create canonical rows.",
        "",
        f"- Provenance rows: {len(output):,}",
        f"- Module 20B rows: {by_module['M20B']:,}",
        f"- Module 21B rows: {by_module['M21B']:,}",
        "",
        "## Paper-resolution status",
        "",
        "| Status | Rows |",
        "|---|---:|",
    ]
    lines.extend(f"| {key} | {value:,} |" for key, value in sorted(paper.items()))
    lines.extend([
        "",
        "## Readiness boundary",
        "",
        "20B exportable LR rows retain the frozen Module 20A manifest as a local",
        "audit anchor but are not paper-ready until their underlying source",
        "records are attached. 21B rows have stable citation tokens but require",
        "atomic full-text Observation and AuthorClaim extraction before import.",
        "Receptor-proximal/pathway evidence remains distinct from LR binding or",
        "activation evidence.",
        "",
    ])
    OUT_MD.write_text("\n".join(lines))
    print(f"lane_A_rows={len(output)} module20b={by_module['M20B']} module21b={by_module['M21B']}")


if __name__ == "__main__":
    main()
