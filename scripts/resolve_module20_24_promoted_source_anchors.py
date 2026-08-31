#!/usr/bin/env python3
"""Resolve source anchors used by promoted Module 20B-24B linkage rows.

This is an audit-layer preparation step. It creates stable paper-key and
evidence-anchor ledgers but does not insert Paper, Observation, AuthorClaim,
SignalingEdge, or SignalingEdgeSource rows.
"""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
B_ROOT = ROOT / "work" / "module_b_consolidation"
LINKAGE_ROOT = ROOT / "work" / "cross_module_synthesis" / "path_linkage_batches"
OUT_ROOT = ROOT / "work" / "cross_module_synthesis"
ANCHOR_TSV = OUT_ROOT / "module20_24_promoted_source_anchor_resolution.tsv"
PAPER_TSV = OUT_ROOT / "module20_24_canonical_paper_anchor_map.tsv"
REPORT_MD = OUT_ROOT / "module20_24_promoted_source_anchor_resolution.md"

EVIDENCE_FIELDS = [
    "evidence_id", "module", "linkage_edge_ids", "b_edge_ids",
    "source_a_evidence_id", "evidence_layer", "support_kind", "source_scope",
    "anchor_type", "anchor_locator", "canonical_paper_key",
    "anchor_resolution_status", "metadata_status", "species_support",
]
PAPER_FIELDS = [
    "canonical_paper_key", "primary_anchor_type", "primary_anchor_locator",
    "alternate_anchor_types", "evidence_ids", "modules", "evidence_layers",
    "anchor_resolution_status", "metadata_status",
]

TOKEN_RE = re.compile(
    r"(?P<pmid>PMID:\s*\d+)|(?P<pmcid>PMCID:\s*PMC\d+)|"
    r"(?P<doi>DOI:\s*10\.[^;\s]+)|(?P<url_label>URL:\s*https?://[^;\s]+)|"
    r"(?P<url>https?://[^;\s]+)",
    re.IGNORECASE,
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def citation_tokens(value: str) -> list[tuple[str, str]]:
    tokens = []
    for match in TOKEN_RE.finditer(value or ""):
        kind = match.lastgroup or "url"
        locator = match.group(0).strip().rstrip(".,)")
        if kind == "url_label":
            kind = "url"
        tokens.append((kind, locator))
    return tokens


def split_ids(value: str) -> list[str]:
    return [item.strip() for item in (value or "").split(";") if item.strip()]


def module_from_evidence_id(evidence_id: str) -> str:
    return evidence_id.split("-", 1)[0]


def canonical_key(anchor_type: str, locator: str) -> str:
    value = locator.strip()
    if anchor_type == "pmid":
        return "PMID:" + re.sub(r"\D", "", value)
    if anchor_type == "pmcid":
        return "PMCID:" + re.sub(r"\s+", "", value).upper().replace("PMCID:", "")
    if anchor_type == "doi":
        doi = re.sub(r"^DOI:\s*", "", value, flags=re.IGNORECASE).rstrip(".,)").lower()
        return "DOI:" + doi
    return "URL:" + value.rstrip(".,)")


def main() -> None:
    linkage_rows: list[dict[str, str]] = []
    evidence_to_edges: dict[str, set[str]] = defaultdict(set)
    for path in sorted(LINKAGE_ROOT.glob("module20_24_path_linkage_block*.tsv")):
        for row in read_tsv(path):
            if row.get("linkage_status") == "direct_lr_only_bounded_no_exact_relay_or_downstream":
                continue
            linkage_rows.append(row)
            for column in ("relay_evidence_ids", "downstream_evidence_ids"):
                for evidence_id in split_ids(row.get(column, "")):
                    evidence_to_edges[evidence_id].add(row["lr_edge_ids"])

    evidence_records: dict[str, dict[str, str]] = {}
    for module in ("22", "23", "24"):
        path = B_ROOT / f"module{module}b" / f"module{module}b_evidence_register.tsv"
        for record in read_tsv(path):
            evidence_records[record["b_evidence_id"]] = record

    assert evidence_to_edges
    assert set(evidence_to_edges).issubset(evidence_records)

    anchor_rows: list[dict[str, str]] = []
    paper_anchors: dict[str, dict[str, set[str] | str]] = {}
    for evidence_id in sorted(evidence_to_edges):
        record = evidence_records[evidence_id]
        module = module_from_evidence_id(evidence_id)
        tokens = citation_tokens(record.get("source_locator", ""))
        assert tokens, evidence_id
        for anchor_type, locator in tokens:
            key = canonical_key(anchor_type, locator)
            metadata_status = (
                "metadata_lookup_required"
                if anchor_type in {"pmid", "pmcid", "doi"}
                else "url_semantics_review_required"
            )
            anchor_rows.append({
                "evidence_id": evidence_id,
                "module": module,
                "linkage_edge_ids": ";".join(sorted(evidence_to_edges[evidence_id])),
                "b_edge_ids": record.get("b_edge_ids", ""),
                "source_a_evidence_id": record.get("source_a_evidence_id", ""),
                "evidence_layer": record.get("evidence_layer", ""),
                "support_kind": record.get("support_kind", ""),
                "source_scope": record.get("source_scope", ""),
                "anchor_type": anchor_type,
                "anchor_locator": locator,
                "canonical_paper_key": key,
                "anchor_resolution_status": "stable_identifier_anchor" if anchor_type in {"pmid", "pmcid", "doi"} else "stable_url_anchor",
                "metadata_status": metadata_status,
                "species_support": record.get("species_support", ""),
            })
            aggregate = paper_anchors.setdefault(key, {
                "primary_anchor_type": anchor_type,
                "primary_anchor_locator": locator,
                "alternate_anchor_types": set(),
                "evidence_ids": set(),
                "modules": set(),
                "evidence_layers": set(),
                "anchor_resolution_status": "stable_identifier_anchor" if anchor_type in {"pmid", "pmcid", "doi"} else "stable_url_anchor",
                "metadata_status": metadata_status,
            })
            if anchor_type in {"pmid", "pmcid", "doi"} and aggregate["primary_anchor_type"] == "url":
                aggregate["primary_anchor_type"] = anchor_type
                aggregate["primary_anchor_locator"] = locator
                aggregate["anchor_resolution_status"] = "stable_identifier_anchor"
                aggregate["metadata_status"] = metadata_status
            aggregate["alternate_anchor_types"].add(anchor_type)
            aggregate["evidence_ids"].add(evidence_id)
            aggregate["modules"].add(module)
            aggregate["evidence_layers"].add(record.get("evidence_layer", ""))

    with ANCHOR_TSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=EVIDENCE_FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(anchor_rows)

    paper_rows = []
    for key in sorted(paper_anchors):
        aggregate = paper_anchors[key]
        paper_rows.append({
            "canonical_paper_key": key,
            "primary_anchor_type": aggregate["primary_anchor_type"],
            "primary_anchor_locator": aggregate["primary_anchor_locator"],
            "alternate_anchor_types": ";".join(sorted(aggregate["alternate_anchor_types"])),
            "evidence_ids": ";".join(sorted(aggregate["evidence_ids"])),
            "modules": ";".join(sorted(aggregate["modules"])),
            "evidence_layers": ";".join(sorted(aggregate["evidence_layers"])),
            "anchor_resolution_status": aggregate["anchor_resolution_status"],
            "metadata_status": aggregate["metadata_status"],
        })
    with PAPER_TSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=PAPER_FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(paper_rows)

    anchor_status = Counter(row["anchor_resolution_status"] for row in anchor_rows)
    metadata_status = Counter(row["metadata_status"] for row in anchor_rows)
    by_module = Counter(row["module"] for row in anchor_rows)
    by_layer = Counter(row["evidence_layer"] for row in anchor_rows)
    report = [
        "# Module 20B–24B Promoted Source-Anchor Resolution",
        "",
        "This is an audit-layer source-anchor pass for the completed systematic linkage blocks.",
        "It does not insert canonical Paper, Observation, AuthorClaim, SignalingEdge, or SignalingEdgeSource rows.",
        "M20B LR discovery-only manifest provenance is intentionally excluded from canonical paper resolution.",
        "",
        "## Coverage",
        "",
        f"- Promoted linkage rows audited: {len(linkage_rows):,}",
        f"- Unique M22B/M23B/M24B evidence records: {len(evidence_to_edges):,}",
        f"- Evidence-anchor rows: {len(anchor_rows):,}",
        f"- Deduplicated canonical paper keys: {len(paper_rows):,}",
        "",
        "## Anchor status",
        "",
        "| Status | Rows |",
        "|---|---:|",
    ]
    report.extend(f"| {key} | {value:,} |" for key, value in sorted(anchor_status.items()))
    report.extend([
        "",
        "## Metadata gate",
        "",
        "| Status | Rows |",
        "|---|---:|",
    ])
    report.extend(f"| {key} | {value:,} |" for key, value in sorted(metadata_status.items()))
    report.extend([
        "",
        "## Module and layer coverage",
        "",
        "| Module | Anchor rows |",
        "|---|---:|",
    ])
    report.extend(f"| {key} | {value:,} |" for key, value in sorted(by_module.items()))
    report.extend([
        "",
        "| Evidence layer | Anchor rows |",
        "|---|---:|",
    ])
    report.extend(f"| {key} | {value:,} |" for key, value in sorted(by_layer.items()))
    report.extend([
        "",
        "## Interpretation",
        "",
        "Stable PMID, PMCID, and DOI tokens now have deduplicated canonical paper keys, but bibliographic metadata still requires a controlled PubMed/PMC/DOI metadata import.",
        "URL-only anchors require semantic review before they can become Paper rows.",
        "No pathway or functional evidence was promoted to direct molecular evidence during this pass.",
        "",
    ])
    REPORT_MD.write_text("\n".join(report))
    print(f"promoted_rows={len(linkage_rows)} evidence_records={len(evidence_to_edges)} anchor_rows={len(anchor_rows)} paper_keys={len(paper_rows)}")
    print(dict(sorted(anchor_status.items())))


if __name__ == "__main__":
    main()
