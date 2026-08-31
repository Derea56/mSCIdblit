#!/usr/bin/env python3
"""Extract and adjudicate retained Module 20B-24B source artifacts.

This is the bridge between the lossless artifact register and the existing
paper/Observation/AuthorClaim review ledger. It gives every artifact an
explicit use status, links exact identifier matches to reviewed extraction
rows when available, and leaves unsupported or unresolved artifacts visible.

The script never infers a paper from a search result, database membership, or
an article's reference list. It also never creates a new biological claim.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "data/processed/module20_24_evidence_artifact_provenance_v1/artifact_manifest.tsv"
DEFAULT_CROSSWALK = ROOT / "data/processed/module20_24_evidence_artifact_provenance_v1/register_crosswalk_candidates.tsv"
DEFAULT_PHASE2 = ROOT / "work/cross_module_synthesis/canonical_evidence_review/module20_24_integrated_phase2_extractions.tsv"
DEFAULT_IDENTITY = ROOT / "work/cross_module_synthesis/canonical_evidence_review/module20_24_phase2_paper_identity_resolution.tsv"
DEFAULT_LEDGER = ROOT / "work/cross_module_synthesis/canonical_evidence_review/module20_24_evidence_grade_ledger.tsv"
DEFAULT_OUTPUT = ROOT / "data/processed/module20_24_evidence_artifact_provenance_v1/artifact_adjudication.tsv"
DEFAULT_SQL = ROOT / "data/processed/module20_24_evidence_artifact_provenance_v1/artifact_adjudication_materialization.sql"
DEFAULT_REPORT = ROOT / "data/processed/module20_24_evidence_artifact_provenance_v1/artifact_adjudication_report.md"

MODULES = {"20B", "21B", "22B", "23B", "24B"}
ID_RE = re.compile(
    r"(?i)\bPMID\s*[:_-]?\s*(\d{4,9})\b|"
    r"\b(PMC\d{3,10})\b|"
    r"\b(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)\b"
)
URL_ID_RE = re.compile(
    r"(?i)pubmed\.ncbi\.nlm\.nih\.gov/(\d+)|"
    r"pmc\.ncbi\.nlm\.nih\.gov/articles/(PMC\d+)|"
    r"doi\.org/(10\.\d{4,9}/[^\s<>\"']+)"
)

FIELDS = [
    "artifact_path", "artifact_sha256", "artifact_byte_size", "artifact_role",
    "artifact_identifier_tokens", "module", "register_edge_id",
    "register_evidence_id", "extraction_id", "canonical_paper_key",
    "resolved_pmid", "paper_match_status", "artifact_support_status",
    "evidence_grade", "context_level", "observation_status", "claim_status",
    "source_locator", "candidate_observation_snippet", "candidate_claim_snippet",
    "adjudication_basis",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def normalize_identifier(kind: str, value: str) -> tuple[str, str]:
    value = value.strip().rstrip(".,;:)]}'\"")
    if kind == "PMID":
        return kind, value
    if kind == "PMCID":
        return kind, value.upper()
    return "DOI", value.lower().removeprefix("doi:")


def identifier_tokens(value: str) -> set[tuple[str, str]]:
    found: set[tuple[str, str]] = set()
    for match in ID_RE.finditer(value or ""):
        if match.group(1):
            found.add(normalize_identifier("PMID", match.group(1)))
        elif match.group(2):
            found.add(normalize_identifier("PMCID", match.group(2)))
        elif match.group(3):
            found.add(normalize_identifier("DOI", match.group(3)))
    for match in URL_ID_RE.finditer(value or ""):
        if match.group(1):
            found.add(normalize_identifier("PMID", match.group(1)))
        elif match.group(2):
            found.add(normalize_identifier("PMCID", match.group(2)))
        elif match.group(3):
            found.add(normalize_identifier("DOI", match.group(3)))
    return found


def xml_self_identifiers(path: Path) -> set[tuple[str, str]]:
    found: set[tuple[str, str]] = set()
    try:
        root = ET.parse(path).getroot()
    except (ET.ParseError, OSError):
        return found
    for node in root.iter():
        tag = node.tag.rsplit("}", 1)[-1].lower()
        text = "".join(node.itertext()).strip()
        if not text:
            continue
        if tag == "pmid":
            found.add(normalize_identifier("PMID", text))
        elif tag == "article-id":
            kind = (node.attrib.get("IdType") or node.attrib.get("pub-id-type") or "").lower()
            if kind in {"pmc", "pmcid"} and re.fullmatch(r"PMC\d+", text, re.I):
                found.add(normalize_identifier("PMCID", text))
            elif kind == "doi" and text.startswith("10."):
                found.add(normalize_identifier("DOI", text))
    return found


def keyed_json_identifiers(value: object) -> set[tuple[str, str]]:
    found: set[tuple[str, str]] = set()
    if isinstance(value, dict):
        for key, item in value.items():
            key_lower = str(key).lower()
            if isinstance(item, str) and key_lower in {"pmid", "pmcid", "doi", "id", "document_id", "article_id"}:
                found.update(identifier_tokens(item))
            elif isinstance(item, (dict, list)):
                found.update(keyed_json_identifiers(item))
    elif isinstance(value, list):
        for item in value:
            found.update(keyed_json_identifiers(item))
    return found


def content_self_identifiers(path: Path, role: str) -> set[tuple[str, str]]:
    """Return only identifiers in source-record metadata, not references."""
    suffix = path.suffix.lower()
    if role in {"literature_xml", "full_text_xml"}:
        return xml_self_identifiers(path)
    if role == "full_text_or_bioc_json":
        try:
            return keyed_json_identifiers(json.loads(path.read_text(encoding="utf-8", errors="replace")))
        except (json.JSONDecodeError, OSError):
            return set()
    if role in {"full_text_html", "metadata_or_search_html"}:
        try:
            raw = path.read_text(encoding="utf-8", errors="replace")[:100_000]
        except OSError:
            return set()
        head = html.unescape(raw)
        # Restrict HTML identity extraction to citation/meta tags and stable
        # PubMed/PMC/DOI URLs; ordinary visible text may contain references.
        metadata = " ".join(
            part for part in re.findall(r"<meta\b[^>]+>", head, flags=re.I)
            if any(token in part.lower() for token in ("citation_", "dc.identifier", "doi.org", "pubmed", "pmc"))
        )
        return identifier_tokens(metadata)
    return set()


def stable_paper_tokens(value: str) -> set[tuple[str, str]]:
    return identifier_tokens(value)


def sql(value: str | None) -> str:
    if value is None:
        return "NULL"
    return "'" + value.replace("'", "''") + "'"


def nullable_sql(value: str) -> str:
    return sql(value) if value else "NULL"


def is_validated_status(value: str) -> bool:
    lowered = (value or "").lower()
    if not lowered.startswith("validated"):
        return False
    return not any(token in lowered for token in ("abstract", "metadata", "unresolved", "boundary", "no_pair", "not_required"))


def classify_match(artifact_role: str, phase_row: dict[str, str], identity: dict[str, str]) -> tuple[str, str]:
    observation = phase_row.get("observation_status", "")
    claim = phase_row.get("claim_status", "")
    lowered = f"{observation} {claim}".lower()
    if any(token in lowered for token in ("boundary", "no_pair", "no_exact", "negative", "do_not_create")):
        return "negative_or_boundary_evaluated", "The linked Phase-2 adjudication explicitly bounds or rejects support for the requested exact relationship."
    if is_validated_status(observation) and is_validated_status(claim):
        if not identity.get("resolved_pmid"):
            return "candidate_requires_review", "The observation and claim are validated, but the Phase-2 paper identity resolver did not establish one PMID for this artifact/extraction pair."
        if artifact_role in {"full_text_xml", "full_text_html", "full_text_or_bioc_json", "full_text_pdf", "figure_image", "literature_xml"}:
            return "supporting_validated_claim", "The artifact has an exact identifier match to a Phase-2 row with validated observation and validated claim statuses."
    if phase_row.get("paper_status", "").startswith("validated") or phase_row.get("paper_status", "") in {"paper_ready", "primary_recovery_validated"}:
        return "candidate_requires_review", "The artifact is linked to a resolved paper-level review row, but the observation and claim gates are not both satisfied."
    return "linked_unresolved", "The artifact is linked to a Phase-2 evidence row, but the paper, observation, or claim remains unresolved."


def build(args: argparse.Namespace) -> dict[str, object]:
    manifest = read_tsv(args.manifest)
    crosswalk = read_tsv(args.crosswalk)
    phase2 = read_tsv(args.phase2)
    identities = {row.get("extraction_id", ""): row for row in read_tsv(args.identity) if row.get("extraction_id")}
    ledger = {row.get("b_evidence_id", ""): row for row in read_tsv(args.ledger) if row.get("b_evidence_id")}
    phase_by_evidence: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in phase2:
        phase_by_evidence[row.get("b_evidence_id", "")].append(row)
    cross_by_path: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in crosswalk:
        cross_by_path[row.get("relative_path", "")].append(row)

    output: list[dict[str, str]] = []
    for artifact in manifest:
        path_string = artifact["relative_path"]
        path = ROOT / path_string
        filename_ids = {
            (row["identifier_type"], row["identifier_value"])
            for row in read_tsv(args.identifiers)
            if row.get("relative_path") == path_string
        }
        self_ids = filename_ids | content_self_identifiers(path, artifact.get("artifact_role", ""))
        self_id_text = ";".join(f"{kind}:{value}" for kind, value in sorted(self_ids))
        links = cross_by_path.get(path_string, [])
        if not links:
            role = artifact.get("artifact_role", "")
            status = "metadata_or_search_only" if role in {"metadata_or_search_json", "metadata_or_search_html", "search_or_manifest", "search_output"} else "unmapped_source_artifact"
            basis = "No conservative register crosswalk exists for this artifact."
            if status == "metadata_or_search_only":
                basis += " Its role is metadata/search/manifest output and it is not treated as direct biological evidence."
            output.append({
                "artifact_path": path_string, "artifact_sha256": artifact["sha256"], "artifact_byte_size": artifact["byte_size"],
                "artifact_role": role, "artifact_identifier_tokens": self_id_text, "module": "", "register_edge_id": "",
                "register_evidence_id": "", "extraction_id": "", "canonical_paper_key": "", "resolved_pmid": "",
                "paper_match_status": "not_attempted", "artifact_support_status": status, "evidence_grade": "",
                "context_level": "", "observation_status": "", "claim_status": "", "source_locator": "",
                "candidate_observation_snippet": "", "candidate_claim_snippet": "", "adjudication_basis": basis,
            })
            continue

        for link in links:
            module = link.get("module", "").upper()
            evidence_id = link.get("register_evidence_id", "")
            phase_candidates = phase_by_evidence.get(evidence_id, [])
            matched = []
            for phase_row in phase_candidates:
                paper_ids = stable_paper_tokens(phase_row.get("canonical_paper_key", "")) | stable_paper_tokens(phase_row.get("source_locator", ""))
                overlap = self_ids & paper_ids
                if overlap:
                    matched.append((phase_row, overlap))
            if not matched:
                grade_row = ledger.get(evidence_id, {})
                output.append({
                    "artifact_path": path_string, "artifact_sha256": artifact["sha256"], "artifact_byte_size": artifact["byte_size"],
                    "artifact_role": artifact.get("artifact_role", ""), "artifact_identifier_tokens": self_id_text, "module": module,
                    "register_edge_id": link.get("register_edge_id", ""), "register_evidence_id": evidence_id,
                    "extraction_id": "", "canonical_paper_key": "", "resolved_pmid": "", "paper_match_status": "no_exact_phase2_paper_match",
                    "artifact_support_status": "linked_unresolved", "evidence_grade": grade_row.get("evidence_grade", ""),
                    "context_level": grade_row.get("context_level", ""), "observation_status": "", "claim_status": "",
                    "source_locator": "", "candidate_observation_snippet": "", "candidate_claim_snippet": "",
                    "adjudication_basis": "Conservative filename/register crosswalk exists, but no exact source-identifier match to a Phase-2 paper row was found; no claim is inferred.",
                })
                continue
            for phase_row, overlap in matched:
                identity = identities.get(phase_row.get("extraction_id", ""), {})
                grade_row = ledger.get(evidence_id, {})
                status, basis = classify_match(artifact.get("artifact_role", ""), phase_row, identity)
                output.append({
                    "artifact_path": path_string, "artifact_sha256": artifact["sha256"], "artifact_byte_size": artifact["byte_size"],
                    "artifact_role": artifact.get("artifact_role", ""), "artifact_identifier_tokens": self_id_text, "module": module,
                    "register_edge_id": link.get("register_edge_id", ""), "register_evidence_id": evidence_id,
                    "extraction_id": phase_row.get("extraction_id", ""), "canonical_paper_key": phase_row.get("canonical_paper_key", ""),
                    "resolved_pmid": identity.get("resolved_pmid", ""), "paper_match_status": "exact_identifier_match:" + ";".join(f"{k}:{v}" for k, v in sorted(overlap)),
                    "artifact_support_status": status, "evidence_grade": grade_row.get("evidence_grade", ""),
                    "context_level": grade_row.get("context_level", ""), "observation_status": phase_row.get("observation_status", ""),
                    "claim_status": phase_row.get("claim_status", ""), "source_locator": phase_row.get("source_locator", ""),
                    "candidate_observation_snippet": phase_row.get("observation_value_or_blocker", ""),
                    "candidate_claim_snippet": phase_row.get("claim_text_or_blocker", ""),
                    "adjudication_basis": basis + " Matched identifiers are recorded for audit; filename tokens and database links alone are not treated as claim support.",
                })

    output.sort(key=lambda row: (row["artifact_path"], row["module"], row["register_evidence_id"], row["extraction_id"]))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(output)

    sql_lines = [
        "-- Generated by scripts/build_module20_24_artifact_adjudication.py.",
        "-- Artifact adjudication is an audit/review bridge; it does not promote edges.",
        "BEGIN;",
        "-- This is a complete regenerated snapshot; replace only this additive review table.",
        "DELETE FROM EvidenceArtifactAdjudication;",
        "",
    ]
    for row in output:
        sql_lines.append(
            "INSERT INTO EvidenceArtifactAdjudication (artifact_id, module, register_edge_id, register_evidence_id, extraction_id, canonical_paper_key, resolved_pmid, artifact_role, paper_match_status, artifact_support_status, evidence_grade, context_level, observation_status, claim_status, source_locator, candidate_observation_snippet, candidate_claim_snippet, adjudication_basis) "
            "SELECT artifact_id, "
            + ", ".join(
                nullable_sql(row[field]) if field in {"resolved_pmid", "evidence_grade", "context_level"} else sql(row[field])
                for field in ("module", "register_edge_id", "register_evidence_id", "extraction_id", "canonical_paper_key", "resolved_pmid", "artifact_role", "paper_match_status", "artifact_support_status", "evidence_grade", "context_level", "observation_status", "claim_status", "source_locator", "candidate_observation_snippet", "candidate_claim_snippet", "adjudication_basis")
            )
            + " FROM EvidenceArtifact WHERE relative_path=" + sql(row["artifact_path"]) + " AND NOT EXISTS (SELECT 1 FROM EvidenceArtifactAdjudication x WHERE x.artifact_id=EvidenceArtifact.artifact_id AND x.module=" + sql(row["module"]) + " AND x.register_evidence_id=" + sql(row["register_evidence_id"]) + " AND x.extraction_id=" + sql(row["extraction_id"]) + ");"
        )
    sql_lines.extend(["", "COMMIT;", ""])
    args.sql.write_text("\n".join(sql_lines), encoding="utf-8")

    status_counts = Counter(row["artifact_support_status"] for row in output)
    module_counts = Counter(row["module"] or "UNMAPPED" for row in output)
    artifact_paths = {row["artifact_path"] for row in output}
    report_lines = [
        "# Module 20B-24B artifact extraction and adjudication",
        "",
        "This report is the artifact-to-review bridge. It does not infer new",
        "biological claims and does not independently promote mechanism edges.",
        "Every manifest artifact receives at least one explicit status row.",
        "",
        f"- Manifest artifacts: {len(manifest):,}",
        f"- Adjudication rows: {len(output):,}",
        f"- Artifacts represented: {len(artifact_paths):,}",
        f"- Artifacts without a conservative register crosswalk: {sum(not cross_by_path.get(row['relative_path']) for row in manifest):,}",
        "",
        "## Status counts",
        "",
        "| Status | Rows |",
        "|---|---:|",
    ]
    report_lines.extend(f"| `{key}` | {value:,} |" for key, value in sorted(status_counts.items()))
    report_lines.extend(["", "## Module routing", "", "| Module | Rows |", "|---|---:|"])
    report_lines.extend(f"| `{key}` | {value:,} |" for key, value in sorted(module_counts.items()))
    report_lines.extend([
        "",
        "## Interpretation",
        "",
        "- `supporting_validated_claim` is the only status that may feed a later canonical evidence-source update, subject to the existing materialization validators.",
        "- `candidate_requires_review` and `linked_unresolved` are usable review inputs but are not canonical support.",
        "- `negative_or_boundary_evaluated` preserves evaluated non-support and must remain available for screening.",
        "- Metadata/search/manifest artifacts are retained for provenance and search reproducibility, not treated as direct evidence.",
        "- Exact identifiers are limited to filename/source-record metadata; article reference-list mentions are not used as paper identity.",
        "",
    ])
    args.report.write_text("\n".join(report_lines), encoding="utf-8")
    return {
        "manifest_artifacts": len(manifest),
        "adjudication_rows": len(output),
        "artifact_paths": len(artifact_paths),
        "status_counts": dict(sorted(status_counts.items())),
        "module_counts": dict(sorted(module_counts.items())),
        "output": str(args.output),
        "sql": str(args.sql),
        "report": str(args.report),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--identifiers", type=Path, default=DEFAULT_MANIFEST.with_name("artifact_identifiers.tsv"))
    parser.add_argument("--crosswalk", type=Path, default=DEFAULT_CROSSWALK)
    parser.add_argument("--phase2", type=Path, default=DEFAULT_PHASE2)
    parser.add_argument("--identity", type=Path, default=DEFAULT_IDENTITY)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--sql", type=Path, default=DEFAULT_SQL)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()
    summary = build(args)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
