#!/usr/bin/env python3
"""Extract explicit paper identifiers used by the Module 22 work.

This is a provenance extraction, not a bibliographic resolver.  It accepts
only identifiers or stable article URLs explicitly present in Module 22
source-locator fields.  Search URLs, database records, and unkeyed links are
written to a separate locator audit rather than being promoted to papers.
Local metadata from the existing Module 20--24 identity ledgers is joined
when an exact identifier match is available; no metadata is invented or
fetched by this script.
"""

from __future__ import annotations

import csv
import glob
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import quote, urlparse


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "work" / "module22_paper_extraction"
PAPERS_OUT = OUT_DIR / "module22_paper_identifiers.tsv"
LOCATORS_OUT = OUT_DIR / "module22_nonpaper_source_locators.tsv"
REPORT_OUT = ROOT / "docs" / "MODULE22_PAPER_EXTRACTION_2026-09-05.md"

PAPER_FIELDS = [
    "paper_identifier", "identifier_type", "identifier_value", "canonical_url",
    "metadata_status", "title", "authors", "publication_year", "journal",
    "source_lanes", "source_registers", "source_record_count",
    "source_record_ids", "source_edge_ids", "source_evidence_ids",
    "source_handoff_ids", "confidence_tiers", "evidence_layers",
    "sci_context_phrase_present", "notes",
]

LOCATOR_FIELDS = [
    "source_lane", "source_register", "source_record_id", "locator_component",
    "locator_class", "reason",
]

ID_PATTERNS = {
    "PMID": re.compile(r"(?i)\bPMID\s*:\s*(\d+)\b"),
    "PMCID": re.compile(r"(?i)\bPMCID\s*:\s*(PMC\d+)\b"),
    "DOI": re.compile(r"(?i)\bDOI\s*:\s*(10\.\S+?)(?=;|\s|$)"),
}
URL_RE = re.compile(r"https?://[^;\s]+", re.IGNORECASE)
SCI_RE = re.compile(r"(?i)\b(?:SCI|spinal cord|spinal injury)\b")

INPUTS = [
    {
        "lane": "module22b_evidence_register",
        "path": ROOT / "work" / "module_b_consolidation" / "module22b" / "module22b_evidence_register.tsv",
        "locator_field": "source_locator",
        "record_field": "b_evidence_id",
        "edge_field": "b_edge_ids",
        "evidence_field": "b_evidence_id",
        "handoff_field": "",
        "context_fields": ("evidence_summary", "limitations", "consolidation_note"),
    },
    {
        "lane": "module22a_new_primary_extractions",
        "path": ROOT / "work" / "module22a_22b_promotion_audit" / "module22a_new_primary_extractions.tsv",
        "locator_field": "source_locator",
        "record_field": "extraction_id",
        "edge_field": "b_edge_id",
        "evidence_field": "b_evidence_id",
        "handoff_field": "",
        "context_fields": ("observation_value_or_blocker", "context_and_limitations", "reviewer_notes"),
    },
    {
        "lane": "module22a_pending_candidate_dispositions",
        "path": ROOT / "work" / "module22a_22b_promotion_audit" / "module22a_pending_candidate_dispositions.tsv",
        "locator_field": "source_locators",
        "record_field": "module22a_handoff_id",
        "edge_field": "",
        "evidence_field": "module21a_evidence_ids",
        "handoff_field": "module22a_handoff_id",
        "context_fields": ("source_evidence_summary", "source_limitations", "limitations"),
    },
    {
        "lane": "module22a_22b_high_confidence_promotions",
        "path": ROOT / "work" / "module22a_22b_promotion_audit" / "module22a_22b_high_confidence_promotions.tsv",
        "locator_field": "evidence_source_locator",
        "record_field": "link_id",
        "edge_field": "edge_id",
        "evidence_field": "evidence_id",
        "handoff_field": "handoff_id",
        "context_fields": ("decision_basis", "handoff_limitations", "edge_limitations", "evidence_limitations"),
    },
    {
        "lane": "module22a_handoff_source_evidence",
        "path": ROOT / "work" / "module21_relay" / "module21a_pair_relay_evidence_detail.tsv",
        "locator_field": "source_locators",
        "record_field": "evidence_id",
        "edge_field": "",
        "evidence_field": "evidence_id",
        "handoff_field": "__handoff_ids",
        "context_fields": ("evidence_summary", "limitations"),
        "only_referenced_by_module22a": True,
    },
]

# These audit ledgers are part of the Module 22 paper-generation trail even
# when a citation has not yet been copied into the canonical evidence table.
# They are discovered by their fixed Module 22 directories so new numbered
# batches are included on the next run without manually editing this list.
for _path in sorted(glob.glob(str(ROOT / "work" / "module22b_low_confidence_upgrade_audit" / "*.tsv"))):
    INPUTS.append({
        "lane": Path(_path).stem,
        "path": Path(_path),
        "locator_field": "source_locator",
        "record_field": "b_evidence_id",
        "edge_field": "b_edge_id",
        "evidence_field": "b_evidence_id",
        "handoff_field": "",
        "context_fields": ("decision_basis",),
    })
for _path in sorted(glob.glob(str(ROOT / "work" / "module22b_tf_regulon_promotion_audit" / "*.tsv"))):
    _name = Path(_path).name
    if _name == "module22b_general_tf_regulon_promotion_batch001.tsv":
        INPUTS.append({
            "lane": Path(_path).stem,
            "path": Path(_path),
            "locator_fields": ("primary_pmids", "corroborating_pmids"),
            "record_field": "curation_id",
            "edge_field": "b_edge_id",
            "evidence_field": "b_evidence_id",
            "handoff_field": "",
            "context_fields": ("cell_type_context", "upstream_sci_activation_claim"),
        })
    else:
        INPUTS.append({
            "lane": Path(_path).stem,
            "path": Path(_path),
            "locator_field": "source_locator",
            "record_field": "b_evidence_id" if "repair" not in _name else "row_id",
            "edge_field": "b_edge_id",
            "evidence_field": "b_evidence_id" if "repair" not in _name else "evidence_id",
            "handoff_field": "",
            "context_fields": ("decision_basis", "upstream_sci_activation_claim"),
        })
INPUTS.append({
    "lane": "module22b_individual_hold_search_log",
    "path": ROOT / "docs" / "MODULE22B_INDIVIDUAL_HOLD_SEARCH_LOG_2026-09-03.tsv",
    "locator_field": "source_locator",
    "record_field": "search_id",
    "edge_field": "b_edge_id",
    "evidence_field": "",
    "handoff_field": "",
    "context_fields": ("relation_text", "evidence_basis", "decision", "sci_context_note"),
})

HEADERLESS_LOW_CONFIDENCE_FIELDS = [
    "batch_id", "b_edge_id", "b_evidence_id", "old_edge_confidence",
    "new_edge_confidence", "old_evidence_confidence", "new_evidence_confidence",
    "old_target", "new_target", "old_edge_status", "new_edge_status",
    "decision_basis", "source_locator", "module22b_register_changed",
    "canonical_sql_materialization",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    if path.name == "module22b_low_confidence_upgrade_batch015.tsv":
        with path.open(newline="") as handle:
            rows = list(csv.reader(handle, delimiter="\t"))
        return [dict(zip(HEADERLESS_LOW_CONFIDENCE_FIELDS, row)) for row in rows if row]
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def clean_doi(value: str) -> str:
    return value.strip().removeprefix("DOI:").rstrip(".,)\"]").lower()


def identifier_tokens(value: str) -> set[tuple[str, str]]:
    tokens: set[tuple[str, str]] = set()
    for kind, pattern in ID_PATTERNS.items():
        for match in pattern.finditer(value or ""):
            raw = match.group(1).rstrip('.,)\"]')
            tokens.add((kind, clean_doi(raw) if kind == "DOI" else raw.upper() if kind == "PMCID" else raw))
    for match in URL_RE.finditer(value or ""):
        parsed = urlparse(match.group(0).rstrip('.,)\"]'))
        host = parsed.netloc.lower().split(":", 1)[0]
        path = parsed.path.strip("/")
        if host == "pubmed.ncbi.nlm.nih.gov" and re.fullmatch(r"\d+", path):
            tokens.add(("PMID", path))
        elif host == "pmc.ncbi.nlm.nih.gov" and path.lower().startswith("articles/"):
            pmcid = path.split("/", 1)[1].split("/", 1)[0]
            if re.fullmatch(r"PMC\d+", pmcid, flags=re.IGNORECASE):
                tokens.add(("PMCID", pmcid.upper()))
        elif host == "doi.org" and path.startswith("10."):
            tokens.add(("DOI", clean_doi(path)))
    return tokens


def canonical_url(kind: str, value: str) -> str:
    if kind == "PMID":
        return f"https://pubmed.ncbi.nlm.nih.gov/{value}/"
    if kind == "PMCID":
        return f"https://pmc.ncbi.nlm.nih.gov/articles/{value}/"
    # Preserve the observed DOI in ``identifier_value`` while making the
    # convenience URL safe for legacy DOI strings containing angle brackets.
    return "https://doi.org/" + quote(value, safe=";/?:@&=+$,-_.!~*'()")


def split_components(value: str) -> list[str]:
    return [part.strip() for part in (value or "").split(";") if part.strip()]


def locator_value(spec: dict[str, object], row: dict[str, str]) -> str:
    if spec.get("locator_fields"):
        parts: list[str] = []
        for field in spec["locator_fields"]:
            value = row.get(str(field), "") or ""
            if str(field).endswith("_pmids"):
                parts.extend(f"PMID:{item}" for item in re.split(r"[;,\s]+", value) if item.isdigit())
            elif value:
                parts.append(value)
        return "; ".join(parts)
    return row.get(str(spec["locator_field"]), "") or ""


def classify_nonpaper(component: str) -> tuple[str, str]:
    lowered = component.lower()
    if "?term=" in lowered or "?query=" in lowered or "/search" in lowered:
        return "search_query", "URL contains a query/search locator, not an exact paper identifier"
    if any(token in lowered for token in ("ncbi", "reactome", "bioproject", "geo:", "gse", "prjna", "public tf union", "local=")):
        return "database_or_local_record", "database, accession, or local source record without an exact paper identifier"
    if lowered.startswith(("http://", "https://", "url:")):
        return "paper_url_without_explicit_id", "article-like URL retained as a lead because no exact PMID, PMCID, or DOI was present"
    return "unresolved_source_label", "source label has no explicit bibliographic identifier"


def metadata_index() -> dict[tuple[str, str], dict[str, str]]:
    paths = [
        ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review" / "module20_24_phase2_paper_identity_resolution.tsv",
        ROOT / "work" / "cross_module_synthesis" / "module20_24_canonical_paper_metadata.tsv",
    ]
    output: dict[tuple[str, str], dict[str, str]] = {}
    for path in paths:
        if not path.exists():
            continue
        for row in read_tsv(path):
            title = row.get("source_metadata_title") or row.get("title") or ""
            if not title:
                continue
            ids: set[tuple[str, str]] = set()
            for field in ("canonical_paper_key", "canonical_merge_key", "resolved_canonical_paper_key", "resolved_pmid", "resolved_pmcid", "resolved_doi", "pmid", "pmcid", "doi"):
                value = row.get(field, "")
                if field in {"resolved_pmid", "pmid"} and value.isdigit():
                    ids.add(("PMID", value))
                elif field in {"resolved_pmcid", "pmcid"} and value.upper().startswith("PMC"):
                    ids.add(("PMCID", value.upper()))
                elif field in {"resolved_doi", "doi"} and value:
                    ids.add(("DOI", clean_doi(value)))
                else:
                    ids |= identifier_tokens(value)
            record = {
                "title": title,
                "authors": row.get("source_metadata_authors") or row.get("authors") or "",
                "publication_year": row.get("source_metadata_year") or row.get("publication_year") or "",
                "journal": row.get("source_metadata_journal") or row.get("journal") or "",
            }
            for identifier in ids:
                if identifier not in output or not output[identifier]["title"]:
                    output[identifier] = record
    return output


def add_ids(value: str, prefix: str, bucket: set[str]) -> None:
    for item in (value or "").split(";"):
        item = item.strip()
        if item:
            bucket.add(prefix + item)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    metadata = metadata_index()
    records: dict[tuple[str, str], dict[str, object]] = {}
    nonpaper: dict[tuple[str, str, str], dict[str, str]] = {}
    input_counts: Counter[str] = Counter()
    module22a_handoff_refs: dict[str, set[str]] = defaultdict(set)
    handoff_path = ROOT / "work" / "module21_relay" / "module22a_ligand_tf_handoff.tsv"
    handoff_rows = read_tsv(handoff_path)
    for handoff in handoff_rows:
        handoff_id = handoff.get("module22a_handoff_id", "")
        for evidence_id in (handoff.get("module21a_evidence_ids", "") or "").split(";"):
            if evidence_id.strip() and handoff_id:
                module22a_handoff_refs[evidence_id.strip()].add(handoff_id)

    for spec in INPUTS:
        rows = read_tsv(spec["path"])
        if spec.get("only_referenced_by_module22a"):
            rows = [row for row in rows if row.get(spec["record_field"], "") in module22a_handoff_refs]
        input_counts[spec["lane"]] = len(rows)
        for row in rows:
            locator = locator_value(spec, row)
            record_id = row.get(spec["record_field"], "") or ""
            record_key = f"{spec['lane']}:{record_id}"
            if spec.get("only_referenced_by_module22a"):
                row = dict(row)
                row["__handoff_ids"] = ";".join(sorted(module22a_handoff_refs[record_id]))
            ids = identifier_tokens(locator)
            context = " ".join(row.get(field, "") or "" for field in spec["context_fields"])
            for kind, value in ids:
                key = (kind, value)
                entry = records.setdefault(key, {
                    "source_lanes": set(), "source_registers": set(), "source_record_ids": set(),
                    "source_edge_ids": set(), "source_evidence_ids": set(), "source_handoff_ids": set(),
                    "confidence_tiers": set(), "evidence_layers": set(), "sci": False,
                })
                entry["source_lanes"].add(spec["lane"])
                entry["source_registers"].add(str(spec["path"].relative_to(ROOT)))
                entry["source_record_ids"].add(record_key)
                add_ids(row.get(spec["edge_field"], "") if spec["edge_field"] else "", "", entry["source_edge_ids"])
                add_ids(row.get(spec["evidence_field"], "") if spec["evidence_field"] else "", "", entry["source_evidence_ids"])
                add_ids(row.get(spec["handoff_field"], "") if spec["handoff_field"] else "", "", entry["source_handoff_ids"])
                for field in ("confidence_tier", "source_confidence_tier", "evidence_confidence_tier", "promotion_confidence_tier", "confidence"):
                    if row.get(field):
                        entry["confidence_tiers"].add(row[field])
                for field in ("evidence_layer", "source_evidence_layer"):
                    if row.get(field):
                        entry["evidence_layers"].add(row[field])
                entry["sci"] = bool(entry["sci"] or SCI_RE.search(context))
            components_with_ids = set()
            for component in split_components(locator):
                component_ids = identifier_tokens(component)
                components_with_ids |= component_ids
                if not component_ids:
                    klass, reason = classify_nonpaper(component)
                    nonpaper[(spec["lane"], record_key, component)] = {
                        "source_lane": spec["lane"],
                        "source_register": str(spec["path"].relative_to(ROOT)),
                        "source_record_id": record_key,
                        "locator_component": component,
                        "locator_class": klass,
                        "reason": reason,
                    }
            if not ids and not split_components(locator):
                nonpaper[(spec["lane"], record_key, "")] = {
                    "source_lane": spec["lane"],
                    "source_register": str(spec["path"].relative_to(ROOT)),
                    "source_record_id": record_key,
                    "locator_component": "",
                    "locator_class": "missing_locator",
                    "reason": "source record contains no source locator",
                }

    with PAPERS_OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=PAPER_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for (kind, value), entry in sorted(records.items()):
            meta = metadata.get((kind, value), {})
            writer.writerow({
                "paper_identifier": f"{kind}:{value}",
                "identifier_type": kind,
                "identifier_value": value,
                "canonical_url": canonical_url(kind, value),
                "metadata_status": "matched_existing_local_metadata" if meta.get("title") else "identifier_only_no_local_metadata",
                "title": meta.get("title", ""),
                "authors": meta.get("authors", ""),
                "publication_year": meta.get("publication_year", ""),
                "journal": meta.get("journal", ""),
                "source_lanes": ";".join(sorted(entry["source_lanes"])),
                "source_registers": ";".join(sorted(entry["source_registers"])),
                "source_record_count": len(entry["source_record_ids"]),
                "source_record_ids": ";".join(sorted(entry["source_record_ids"])),
                "source_edge_ids": ";".join(sorted(entry["source_edge_ids"])),
                "source_evidence_ids": ";".join(sorted(entry["source_evidence_ids"])),
                "source_handoff_ids": ";".join(sorted(entry["source_handoff_ids"])),
                "confidence_tiers": ";".join(sorted(entry["confidence_tiers"])),
                "evidence_layers": ";".join(sorted(entry["evidence_layers"])),
                "sci_context_phrase_present": "true" if entry["sci"] else "false",
                "notes": "SCI flag means the associated Module 22 record text mentions SCI/spinal cord/spinal injury; it is not a paper-level SCI validation.",
            })

    with LOCATORS_OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=LOCATOR_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for key in sorted(nonpaper):
            writer.writerow(nonpaper[key])

    paper_counts = Counter(kind for kind, _ in records)
    metadata_count = sum(bool(metadata.get(key, {}).get("title")) for key in records)
    sci_count = sum(bool(entry["sci"]) for entry in records.values())
    locator_classes = Counter(row["locator_class"] for row in nonpaper.values())
    handoff_reference_values = [
        handoff.get("module21a_evidence_ids", "")
        for handoff in handoff_rows
        if handoff.get("module21a_evidence_ids", "")
    ]
    handoff_reference_ids = {
        item.strip()
        for value in handoff_reference_values
        for item in value.split(";")
        if item.strip()
    }
    detail_ids = {
        row.get("evidence_id", "")
        for row in read_tsv(ROOT / "work" / "module21_relay" / "module21a_pair_relay_evidence_detail.tsv")
        if row.get("evidence_id", "")
    }
    report = [
        "# Module 22 Paper Extraction",
        "",
        "Generated 2026-09-05 from explicit paper locators in the Module 22 source lanes below, including all discovered numbered audit batches.",
        "",
        "## Result",
        "",
        f"- Unique explicit identifiers: **{len(records)}** ({paper_counts['PMID']} PMID, {paper_counts['PMCID']} PMCID, {paper_counts['DOI']} DOI).",
        f"- Identifiers matched to an existing local title/metadata record: **{metadata_count}**.",
        f"- Identifiers whose associated Module 22 text mentions SCI/spinal cord/spinal injury: **{sci_count}**; this is a text-presence flag, not paper-level SCI validation.",
        f"- Non-paper or unresolved locator components retained separately: **{len(nonpaper)}**.",
        f"- Module 22A handoff coverage: **{len(handoff_rows)}** handoffs inspected; {len(handoff_reference_values)} had evidence references, covering {len(handoff_reference_ids)} unique detail packets; missing detail IDs: {len(handoff_reference_ids - detail_ids)}.",
        "",
        "The main TSV is identifier-level. A paper with PMID, PMCID, and DOI can therefore occur as three identifiers until a validated cross-identifier mapping is available; this avoids falsely merging multiple papers cited in one source record.",
        "",
        "## Source lanes",
        "",
    ]
    for lane, count in input_counts.items():
        report.append(f"- `{lane}`: {count} source records")
    report += [
        "",
        "## Non-paper locator classes",
        "",
    ]
    for klass, count in sorted(locator_classes.items()):
        report.append(f"- `{klass}`: {count}")
    report += [
        "",
        "## Files",
        "",
        f"- Identifier manifest: [`{PAPERS_OUT.relative_to(ROOT)}`]({PAPERS_OUT.relative_to(ROOT)})",
        f"- Non-paper locator audit: [`{LOCATORS_OUT.relative_to(ROOT)}`]({LOCATORS_OUT.relative_to(ROOT)})",
        "- Reproducible extractor: [`scripts/extract_module22_papers.py`](../scripts/extract_module22_papers.py)",
        "",
        "No titles, authors, years, or journal fields were invented. Blank metadata means that an exact local metadata match was unavailable to this extraction.",
    ]
    REPORT_OUT.write_text("\n".join(report) + "\n")
    print(f"wrote {PAPERS_OUT} ({len(records)} rows)")
    print(f"wrote {LOCATORS_OUT} ({len(nonpaper)} rows)")
    print(f"wrote {REPORT_OUT}")


if __name__ == "__main__":
    main()
