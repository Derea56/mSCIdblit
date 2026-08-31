#!/usr/bin/env python3
"""Build an evidence-to-source-anchor registry for Modules 20B-24B.

The registry is a preparation layer for canonical materialization. It resolves
stable citation tokens and local audit locators, but does not invent Paper,
Observation, or AuthorClaim rows and does not modify canonical tables.
"""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
B_ROOT = ROOT / "work" / "module_b_consolidation"
M20_STARTER = ROOT / "work" / "module20_db_seed" / "evidence_escalation_starter"
OUT_TSV = ROOT / "data" / "processed" / "module20_24_source_anchor_registry.tsv"
OUT_MD = ROOT / "docs" / "MODULE20_24_SOURCE_ANCHOR_AUDIT.md"

TOKEN_RE = re.compile(
    r"(?P<pmid>PMID:\s*\d+)|(?P<pmcid>PMCID:\s*PMC\d+)|"
    r"(?P<doi>DOI:\s*10\.\S+)|(?P<url>https?://[^\s;]+)|"
    r"(?P<url_label>URL:\s*https?://[^\s;]+)",
    re.IGNORECASE,
)
EVIDENCE_ID_RE = re.compile(r"\b[A-Z0-9]+(?:-[A-Z0-9]+)+-EVID-\d+\b", re.IGNORECASE)

FIELDS = [
    "module", "b_evidence_id", "source_a_evidence_id", "exportable",
    "support_kind", "anchor_type", "anchor_locator", "anchor_status",
    "resolution_basis",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def normalize_token(kind: str, value: str) -> str:
    value = value.strip()
    if kind in {"pmid", "pmcid", "doi", "url_label"}:
        return re.sub(r"\s+", "", value)
    return value.rstrip(".,)")


def citation_tokens(value: str) -> list[tuple[str, str]]:
    tokens: list[tuple[str, str]] = []
    for match in TOKEN_RE.finditer(value or ""):
        kind = match.lastgroup or "url"
        tokens.append(("url" if kind == "url_label" else kind, normalize_token(kind, match.group(0))))
    return tokens


def build_a_evidence_index() -> dict[str, set[str]]:
    index: dict[str, set[str]] = defaultdict(set)
    for path in sorted(M20_STARTER.glob("*_evidence_register.tsv")):
        for row in read_tsv(path):
            evidence_id = row.get("evidence_id", "") or row.get("evidence_item_id", "")
            if not evidence_id:
                continue
            for field in ("source_locator", "stable_citations", "citation_note", "citation", "source_url"):
                for _, token in citation_tokens(row.get(field, "")):
                    index[evidence_id].add(token)
    return index


def build_rows() -> tuple[list[dict[str, str]], dict[str, int]]:
    a_evidence_index = build_a_evidence_index()
    m20_queue = {
        row.get("review_id", ""): row
        for row in read_tsv(ROOT / "work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue.tsv")
    }
    rows: list[dict[str, str]] = []
    stats = Counter()
    for module in ("20", "21", "22", "23", "24"):
        path = B_ROOT / f"module{module}b" / f"module{module}b_evidence_register.tsv"
        for evidence in read_tsv(path):
            b_id = evidence["b_evidence_id"]
            module_label = f"{module}B"
            direct_tokens = citation_tokens(evidence.get("source_locator", ""))
            referenced_ids = EVIDENCE_ID_RE.findall(evidence.get("citation_note", ""))
            if module == "20":
                referenced_ids.extend(
                    EVIDENCE_ID_RE.findall(m20_queue.get(evidence.get("source_a_evidence_id", ""), {}).get("evidence_register_ids", ""))
                )
            inherited_tokens = sorted({token for ref in referenced_ids for token in a_evidence_index.get(ref, set())})
            tokens = direct_tokens + [
                ("pmid" if token.upper().startswith("PMID:") else
                 "pmcid" if token.upper().startswith("PMCID:") else
                 "doi" if token.upper().startswith("DOI:") else "url", token)
                for token in inherited_tokens
            ]
            if not tokens:
                local = evidence.get("source_locator", "")
                if not local and evidence.get("exportable") != "true" and evidence.get("source_a_evidence_id"):
                    a_register = ROOT / f"work/module{module}a/module{module}a_evidence_register.tsv"
                    if a_register.exists():
                        local = f"local:{a_register.relative_to(ROOT)}#{evidence['source_a_evidence_id']}"
                if local:
                    rows.append({
                        "module": module_label, "b_evidence_id": b_id,
                        "source_a_evidence_id": evidence.get("source_a_evidence_id", ""),
                        "exportable": evidence.get("exportable", "false"),
                        "support_kind": evidence.get("support_kind", ""),
                        "anchor_type": "local", "anchor_locator": local,
                        "anchor_status": "local_audit_anchor",
                        "resolution_basis": (
                            "B evidence source_locator"
                            if evidence.get("source_locator")
                            else "A-layer no-evidence boundary record; no external paper anchor asserted"
                        ),
                    })
                    stats["local_audit_anchor"] += 1
                else:
                    rows.append({
                        "module": module_label, "b_evidence_id": b_id,
                        "source_a_evidence_id": evidence.get("source_a_evidence_id", ""),
                        "exportable": evidence.get("exportable", "false"),
                        "support_kind": evidence.get("support_kind", ""),
                        "anchor_type": "unresolved", "anchor_locator": "",
                        "anchor_status": "unresolved",
                        "resolution_basis": "No stable external or local locator in B evidence",
                    })
                    stats["unresolved"] += 1
                continue
            seen: set[tuple[str, str]] = set()
            for anchor_type, locator in tokens:
                key = (anchor_type, locator)
                if key in seen:
                    continue
                seen.add(key)
                rows.append({
                    "module": module_label, "b_evidence_id": b_id,
                    "source_a_evidence_id": evidence.get("source_a_evidence_id", ""),
                    "exportable": evidence.get("exportable", "false"),
                    "support_kind": evidence.get("support_kind", ""),
                    "anchor_type": anchor_type, "anchor_locator": locator,
                    "anchor_status": "candidate_external_anchor",
                    "resolution_basis": "B source_locator" if (anchor_type, locator) in direct_tokens else "Module 20A evidence-register citation referenced by B row",
                })
                stats["candidate_external_anchor"] += 1
    return rows, stats


def write_outputs(rows: list[dict[str, str]], stats: Counter) -> None:
    OUT_TSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_TSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    by_module = Counter(row["module"] for row in rows)
    by_module_status = Counter((row["module"], row["anchor_status"], row["exportable"]) for row in rows)
    lines = [
        "# Module 20B–24B Source-Anchor Audit",
        "",
        "This registry prepares canonical materialization. It does not create",
        "Paper, Observation, or AuthorClaim rows and does not modify canonical SQL.",
        "",
        "## Anchor status",
        "",
        "| Status | Rows |",
        "|---|---:|",
    ]
    for status, count in sorted(stats.items()):
        lines.append(f"| {status} | {count:,} |")
    lines.extend([
        "",
        "## Registry coverage",
        "",
        "| Module | Evidence-anchor rows |",
        "|---|---:|",
    ])
    for module in ("20B", "21B", "22B", "23B", "24B"):
        lines.append(f"| {module} | {by_module[module]:,} |")
    lines.extend([
        "",
        "## Exportable-evidence anchor posture",
        "",
        "| Module | External candidate anchors | Local-only anchors | Unresolved anchors |",
        "|---|---:|---:|---:|",
    ])
    for module in ("20B", "21B", "22B", "23B", "24B"):
        external = by_module_status[(module, "candidate_external_anchor", "true")]
        local = by_module_status[(module, "local_audit_anchor", "true")]
        unresolved = by_module_status[(module, "unresolved", "true")]
        lines.append(f"| {module} | {external:,} | {local:,} | {unresolved:,} |")
    lines.extend([
        "",
        "External PMID/PMCID/DOI/URL tokens are candidate anchors only. They must",
        "be resolved to canonical Paper rows and then linked to an observation or",
        "author claim before SignalingEdgeSource materialization.",
        "",
    ])
    OUT_MD.write_text("\n".join(lines))


def main() -> None:
    rows, stats = build_rows()
    write_outputs(rows, stats)
    print(f"wrote {OUT_TSV} rows={len(rows)}")
    print(f"wrote {OUT_MD}")
    print(dict(sorted(stats.items())))


if __name__ == "__main__":
    main()
