#!/usr/bin/env python3
"""Build a checksummed database-backed provenance layer for Module 20-24 files.

This script does not create Paper, Experiment, Observation, AuthorClaim, or
SignalingEdgeSource rows. It records retained artifacts and conservative
filename-token crosswalk candidates so raw evidence can be reviewed and later
promoted without losing provenance.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE_ROOT = ROOT / "data" / "raw" / "evidence" / "module20_24_supervised_cli_phase2"
DEFAULT_OUTPUT_ROOT = ROOT / "data" / "processed" / "module20_24_evidence_artifact_provenance_v1"
SCAN_VERSION = "module20_24_artifact_scan_v1"
MODULES = ("20B", "21B", "22B", "23B", "24B")

IDENTIFIER_PATTERNS = (
    ("PMID", re.compile(r"(?i)(?:PMID|pubmed)[_:-]?([0-9]{4,9})")),
    ("PMCID", re.compile(r"(?i)(PMC[0-9]{3,10})")),
    ("DOI", re.compile(r"(?i)(10\.[0-9]{4,9}/[-._;()/:A-Za-z0-9]+)")),
    ("GEO", re.compile(r"(?i)\b(GSE[0-9]{3,10}|GPL[0-9]{3,10})\b")),
    ("SRA", re.compile(r"(?i)\b((?:SRP|SRR|SRX|SRS)[0-9]{3,12})\b")),
    ("BIOPROJECT", re.compile(r"(?i)\b(PRJNA[0-9]{3,12})\b")),
    ("BIOSAMPLE", re.compile(r"(?i)\b(SAMN[0-9]{3,12})\b")),
    ("ARRAYEXPRESS", re.compile(r"(?i)\b(E-[A-Z]{4}-[0-9]{3,8})\b")),
    ("PROTEOMEXCHANGE", re.compile(r"(?i)\b(PXD[0-9]{3,10})\b")),
)

LOCATOR_PATTERNS = (
    ("PMID", re.compile(r"(?i)\bPMID[:_ -]?([0-9]{4,9})\b")),
    ("PMCID", re.compile(r"(?i)\b(PMC[0-9]{3,10})\b")),
    ("DOI", re.compile(r"(?i)\b(10\.[0-9]{4,9}/[-._;()/:A-Za-z0-9]+)")),
)


def sql_literal(value: str | None) -> str:
    if value is None:
        return "NULL"
    return "'" + value.replace("'", "''") + "'"


def normalize_identifier(kind: str, value: str) -> str:
    value = value.strip().rstrip(".,;:)]}'\"")
    if kind == "PMID":
        return value
    if kind == "PMCID":
        return value.upper()
    if kind == "DOI":
        return value.lower().replace("_", "/")
    return value.upper()


def filename_identifiers(name: str) -> list[tuple[str, str]]:
    found: set[tuple[str, str]] = set()
    for kind, pattern in IDENTIFIER_PATTERNS:
        for match in pattern.finditer(name):
            value = normalize_identifier(kind, match.group(1))
            found.add((kind, value))
    return sorted(found)


def locator_identifiers(value: str) -> set[tuple[str, str]]:
    found: set[tuple[str, str]] = set()
    for kind, pattern in LOCATOR_PATTERNS:
        for match in pattern.finditer(value or ""):
            found.add((kind, normalize_identifier(kind, match.group(1))))
    return found


def role(path: Path) -> str:
    name = path.name.lower()
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return "full_text_pdf"
    if suffix == ".jpg" or suffix == ".jpeg":
        return "figure_image"
    if suffix == ".tsv":
        return "search_or_manifest"
    if suffix == ".txt":
        return "search_output"
    if suffix == ".xml":
        if any(token in name for token in ("pubmed", "efetch", "europepmc", "primary_records")):
            return "literature_xml"
        return "full_text_xml"
    if suffix == ".json":
        if "search" in name or "crossref" in name or "idconv" in name:
            return "metadata_or_search_json"
        return "full_text_or_bioc_json"
    if suffix in {".html", ".htm"}:
        if "search" in name or "landing" in name:
            return "metadata_or_search_html"
        return "full_text_html"
    return "other_artifact"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_registers() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for module in MODULES:
        module_key = module.lower()
        path = ROOT / "work" / "module_b_consolidation" / f"module{module_key}" / f"module{module_key}_evidence_register.tsv"
        with path.open(newline="") as handle:
            for row in csv.DictReader(handle, delimiter="\t"):
                row["module"] = module
                rows.append(row)
    return rows


def build(root: Path, output: Path) -> dict[str, int]:
    root = root.resolve()
    if not root.is_dir():
        raise SystemExit(f"evidence root does not exist: {root}")
    try:
        repository_relative_root = root.relative_to(ROOT).as_posix()
    except ValueError as exc:
        raise SystemExit("evidence root must be inside the repository") from exc

    artifacts: list[dict[str, object]] = []
    identifiers: list[dict[str, str]] = []
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        relative_path = path.relative_to(ROOT).as_posix()
        artifacts.append({
            "repository_root": repository_relative_root,
            "relative_path": relative_path,
            "sha256": sha256(path),
            "byte_size": path.stat().st_size,
            "file_extension": path.suffix.lower().lstrip(".") or None,
            "artifact_role": role(path),
            "scan_version": SCAN_VERSION,
        })
        for kind, value in filename_identifiers(path.name):
            identifiers.append({
                "repository_root": repository_relative_root,
                "relative_path": relative_path,
                "identifier_type": kind,
                "identifier_value": value,
                "match_scope": "filename",
            })

    by_path = {(row["repository_root"], row["relative_path"]): row for row in identifiers}
    artifact_identifier_sets: dict[str, set[tuple[str, str]]] = {}
    for row in identifiers:
        artifact_identifier_sets.setdefault(row["relative_path"], set()).add((row["identifier_type"], row["identifier_value"]))

    crosswalks: list[dict[str, str]] = []
    for register in read_registers():
        locator_ids = locator_identifiers(register.get("source_locator", ""))
        if not locator_ids:
            continue
        for artifact in artifacts:
            path = str(artifact["relative_path"])
            matches = sorted(locator_ids & artifact_identifier_sets.get(path, set()))
            for kind, value in matches:
                crosswalks.append({
                    "repository_root": str(artifact["repository_root"]),
                    "relative_path": path,
                    "module": register["module"],
                    "register_edge_id": register["b_edge_ids"],
                    "register_evidence_id": register["b_evidence_id"],
                    "matched_identifier_type": kind,
                    "matched_identifier_value": value,
                    "match_method": "filename_locator_token",
                    "crosswalk_status": "filename_token_candidate",
                    "notes": "Conservative candidate link only; filename token does not by itself validate or promote biological evidence.",
                })

    output.mkdir(parents=True, exist_ok=True)
    artifact_fields = ["repository_root", "relative_path", "sha256", "byte_size", "file_extension", "artifact_role", "scan_version"]
    identifier_fields = ["repository_root", "relative_path", "identifier_type", "identifier_value", "match_scope"]
    crosswalk_fields = ["repository_root", "relative_path", "module", "register_edge_id", "register_evidence_id", "matched_identifier_type", "matched_identifier_value", "match_method", "crosswalk_status", "notes"]
    for filename, fields, rows in (
        ("artifact_manifest.tsv", artifact_fields, artifacts),
        ("artifact_identifiers.tsv", identifier_fields, identifiers),
        ("register_crosswalk_candidates.tsv", crosswalk_fields, crosswalks),
    ):
        with (output / filename).open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)

    sql_lines = [
        "-- Generated by scripts/materialize_module20_24_evidence_artifacts.py.",
        "-- Artifact presence and filename-token links are provenance only.",
        "BEGIN;",
        "",
    ]
    for row in artifacts:
        values = [sql_literal(str(row["repository_root"])), sql_literal(str(row["relative_path"])), sql_literal(str(row["sha256"])), str(row["byte_size"]), sql_literal(row["file_extension"]), sql_literal(str(row["artifact_role"])), sql_literal(str(row["scan_version"]))]
        sql_lines.append(
            "INSERT INTO EvidenceArtifact (repository_root, relative_path, sha256, byte_size, file_extension, artifact_role, scan_version) VALUES ("
            + ", ".join(values)
            + ") ON CONFLICT (repository_root, relative_path) DO UPDATE SET sha256=EXCLUDED.sha256, byte_size=EXCLUDED.byte_size, file_extension=EXCLUDED.file_extension, artifact_role=EXCLUDED.artifact_role, scan_version=EXCLUDED.scan_version, scanned_at=CURRENT_TIMESTAMP;"
        )
    for row in identifiers:
        sql_lines.append(
            "INSERT INTO EvidenceArtifactIdentifier (artifact_id, identifier_type, identifier_value, match_scope) SELECT artifact_id, "
            + ", ".join(sql_literal(row[k]) for k in ("identifier_type", "identifier_value", "match_scope"))
            + " FROM EvidenceArtifact WHERE repository_root=" + sql_literal(row["repository_root"])
            + " AND relative_path=" + sql_literal(row["relative_path"])
            + " ON CONFLICT (artifact_id, identifier_type, identifier_value, match_scope) DO NOTHING;"
        )
    for row in crosswalks:
        sql_lines.append(
            "INSERT INTO EvidenceArtifactRegisterCrosswalk (artifact_id, register_source_id, module, register_edge_id, register_evidence_id, matched_identifier_type, matched_identifier_value, match_method, crosswalk_status, notes) SELECT a.artifact_id, s.register_source_id, s.module, s.register_edge_id, s.register_evidence_id, "
            + ", ".join(sql_literal(row[k]) for k in ("matched_identifier_type", "matched_identifier_value", "match_method", "crosswalk_status", "notes"))
            + " FROM EvidenceArtifact a JOIN SignalingEdgeRegisterSource s ON s.module=" + sql_literal(row["module"])
            + " AND s.register_evidence_id=" + sql_literal(row["register_evidence_id"])
            + " WHERE a.repository_root=" + sql_literal(row["repository_root"])
            + " AND a.relative_path=" + sql_literal(row["relative_path"])
            + " ON CONFLICT (artifact_id, register_source_id, matched_identifier_type, matched_identifier_value, match_method) DO NOTHING;"
        )
    sql_lines.extend(["", "COMMIT;", ""])
    (output / "module20_24_evidence_artifacts_materialization.sql").write_text("\n".join(sql_lines))

    summary = {
        "scan_version": SCAN_VERSION,
        "repository_root": repository_relative_root,
        "artifact_count": len(artifacts),
        "identifier_count": len(identifiers),
        "crosswalk_candidate_count": len(crosswalks),
        "unique_sha256_count": len({str(row["sha256"]) for row in artifacts}),
        "scope_note": "Filename identifiers and crosswalks are conservative provenance candidates; no canonical biological evidence is created by this layer.",
    }
    (output / "bundle_metadata.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    return {key: int(value) for key, value in summary.items() if isinstance(value, int)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence-root", type=Path, default=DEFAULT_EVIDENCE_ROOT)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    args = parser.parse_args()
    counts = build(args.evidence_root, args.output_root)
    print(" ".join(f"{key}={value}" for key, value in counts.items()))


if __name__ == "__main__":
    main()
