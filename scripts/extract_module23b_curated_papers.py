#!/usr/bin/env python3
"""Build a conservative paper-extraction batch for curated Module 23B rows.

The output is an audit-layer extraction packet. It links each selected B-layer
record to the local source artifact and retains a short, deterministic text
excerpt when one is available. It does not create canonical database rows or
upgrade evidence status; curator validation remains required.
"""

from __future__ import annotations

import argparse
import csv
import html
import re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTER = ROOT / "work/module_b_consolidation/module23b/module23b_evidence_register.tsv"
DEFAULT_MANIFEST = ROOT / "work/module23a/module23a_second_pass_source_manifest.tsv"
DEFAULT_OUTPUT = ROOT / "work/module_b_consolidation/module23b/module23b_paper_extraction_batch_2026-09-05.tsv"
DEFAULT_REPORT = ROOT / "work/module_b_consolidation/module23b/module23b_paper_extraction_batch_2026-09-05.md"

SOURCE_IDS = {
    "EXPAND23A-REV-067",
    "EXPAND23A-REV-068",
    "EXPAND23A-REV-069",
    "EXPAND23A-REV-070",
    "EXPAND23A-REV-071",
    "EXPAND23A-REV-072",
    "EXPAND23A-REV-073",
}

FIELDS = [
    "extraction_id", "source_review_id", "b_evidence_id", "b_edge_ids",
    "source_a_evidence_id", "primary_locator", "local_source_path",
    "source_format", "source_artifact_status", "evidence_layer",
    "source_scope", "confidence_tier", "registered_evidence_summary",
    "source_excerpt", "excerpt_sentence_index", "excerpt_match_terms",
    "extraction_method", "paper_extraction_status", "human_validation_status",
    "promotion_status", "limitations", "consolidation_note",
]


class VisibleTextParser(HTMLParser):
    """Extract visible HTML text without script/style payloads."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.skip_depth = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() in {"script", "style", "noscript", "svg"}:
            self.skip_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in {"script", "style", "noscript", "svg"} and self.skip_depth:
            self.skip_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self.skip_depth and data.strip():
            self.parts.append(data.strip())


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def source_id(row: dict[str, str]) -> str:
    match = re.search(r"EXPAND23A-REV-\d+", row.get("citation_note", ""))
    return match.group(0) if match else ""


def local_paths(locator: str) -> list[Path]:
    paths: list[Path] = []
    for token in locator.split(";"):
        token = token.strip()
        labeled = re.search(r"local(?:\s+full\s+text)?\s*[:=]\s*(data/\S+|work/\S+)", token, flags=re.I)
        if labeled:
            token = labeled.group(1)
        elif token.lower().startswith("local:"):
            token = token.removeprefix("local:")
        if token.startswith("data/") or token.startswith("work/"):
            path = ROOT / token
            if path not in paths:
                paths.append(path)
    return paths


def plain_text(path: Path) -> str:
    raw = path.read_bytes().decode("utf-8", errors="replace")
    if path.suffix.lower() in {".html", ".htm"}:
        parser = VisibleTextParser()
        parser.feed(raw)
        raw = "\n".join(parser.parts)
    else:
        raw = re.sub(r"<[^>]+>", " ", raw)
    raw = html.unescape(raw)
    raw = raw.replace("\r", "\n")
    return re.sub(r"\s+", " ", raw).strip()


def sentences(text: str) -> list[str]:
    # Figure citations commonly contain a period followed by a numeral; do
    # not split a candidate excerpt in the middle of "Fig. 2" or "Fig. 3f".
    normalized = re.sub(r"\b(Fig(?:ure)?|Figs?|No|Dr|et al)\.", r"\1", text, flags=re.I)
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+", normalized) if part.strip()]


def match_excerpt(text: str, summary: str, scope: str) -> tuple[str, int, str]:
    terms = []
    for token in re.findall(r"[A-Za-z][A-Za-z0-9-]{3,}", f"{summary} {scope}"):
        key = token.casefold()
        if key not in {"primary", "study", "source", "supports", "supporting", "reported", "context", "assay", "function", "layer"} and key not in terms:
            terms.append(key)
    candidates: list[tuple[int, int, str]] = []
    for index, sentence in enumerate(sentences(text), start=1):
        lower = sentence.casefold()
        hits = sum(term in lower for term in terms)
        if hits:
            candidates.append((hits, index, sentence))
    if not candidates:
        return "", 0, ";".join(terms[:12])
    _, index, excerpt = max(candidates, key=lambda item: (item[0], -item[1]))
    return excerpt[:900], index, ";".join(terms[:12])


def choose_artifact(paths: list[Path]) -> tuple[Path | None, str, str]:
    existing = [path for path in paths if path.is_file()]
    if not existing:
        return None, "missing", "no_local_artifact"
    full_text = sorted(
        [path for path in existing if (
            "fulltext" in path.name.lower()
            or path.suffix.lower() == ".pdf"
            or "_full." in path.name.lower()
            or "_bioc." in path.name.lower()
            or (path.suffix.lower() in {".html", ".htm"} and ("pmc" in path.name.lower() or "article" in path.name.lower()))
        )],
        key=lambda path: (
            path.suffix.lower() == ".pdf",
            path.suffix.lower() not in {".html", ".htm", ".xml", ".json"},
        ),
    )
    path = full_text[0] if full_text else existing[0]
    suffix = path.suffix.lower()
    full_text_artifact = (
        suffix == ".pdf"
        or "fulltext" in path.name.lower()
        or "_full." in path.name.lower()
        or "_bioc." in path.name.lower()
        or (suffix in {".html", ".htm"} and ("pmc" in path.name.lower() or "article" in path.name.lower()))
    )
    if suffix == ".pdf":
        source_format = "pdf_full_text"
    elif suffix in {".html", ".htm"}:
        source_format = "html_full_text" if full_text_artifact else "html_or_metadata"
    elif suffix == ".json" and full_text_artifact:
        source_format = "bioc_full_text"
    elif suffix == ".xml" and full_text_artifact:
        source_format = "xml_full_text"
    else:
        source_format = "xml_or_metadata"
    if full_text_artifact:
        status = "local_full_text_artifact"
    else:
        status = "local_abstract_or_metadata_artifact"
    return path, source_format, status


def build(register_path: Path, manifest_path: Path, output: Path, report: Path) -> None:
    register_rows = read_tsv(register_path)
    manifest = {row["source_id"]: row for row in read_tsv(manifest_path)}
    selected = [
        row for row in register_rows
        if row["b_evidence_id"].startswith("M23B-EVID-EXPAND23A-")
        and source_id(row) in SOURCE_IDS
    ]
    if not selected:
        raise SystemExit("no selected Module 23B curated rows found")

    output_rows: list[dict[str, str]] = []
    for index, row in enumerate(selected, start=1):
        review_id = source_id(row)
        manifest_row = manifest.get(review_id, {})
        paths = local_paths(manifest_row.get("local_path", ""))
        artifact, source_format, artifact_status = choose_artifact(paths)
        excerpt = ""
        sentence_index = 0
        match_terms = ""
        if artifact is not None:
            excerpt, sentence_index, match_terms = match_excerpt(
                plain_text(artifact), row["evidence_summary"], row["source_scope"]
            )
        has_full_text = artifact_status == "local_full_text_artifact"
        output_rows.append({
            "extraction_id": f"M23B-X-20260905-{index:03d}",
            "source_review_id": review_id,
            "b_evidence_id": row["b_evidence_id"],
            "b_edge_ids": row["b_edge_ids"],
            "source_a_evidence_id": row["source_a_evidence_id"],
            "primary_locator": row["source_locator"].split("; local:", 1)[0],
            "local_source_path": str(artifact.relative_to(ROOT)) if artifact else "; ".join(str(path.relative_to(ROOT)) for path in paths),
            "source_format": source_format,
            "source_artifact_status": artifact_status,
            "evidence_layer": row["evidence_layer"],
            "source_scope": row["source_scope"],
            "confidence_tier": row["confidence_tier"],
            "registered_evidence_summary": row["evidence_summary"],
            "source_excerpt": excerpt,
            "excerpt_sentence_index": str(sentence_index),
            "excerpt_match_terms": match_terms,
            "extraction_method": "deterministic_sentence_match_against_local_artifact",
            "paper_extraction_status": (
                "candidate_extracted_from_full_text" if has_full_text and excerpt
                else "candidate_extracted_from_abstract_or_metadata" if excerpt
                else "awaiting_source_acquisition" if artifact is None
                else "artifact_present_excerpt_not_matched"
            ),
            "human_validation_status": "required",
            "promotion_status": "not_promoted",
            "limitations": row["limitations"],
            "consolidation_note": row["consolidation_note"],
        })

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)

    counts = Counter(row["paper_extraction_status"] for row in output_rows)
    source_counts = Counter(row["source_review_id"] for row in output_rows)
    lines = [
        "# Module 23B curated paper extraction batch (2026-09-05)",
        "",
        "This is an audit-layer extraction packet for the newest curated Module",
        "23B source-review batches. It links B-layer evidence to local artifacts",
        "and records deterministic candidate excerpts. It does not create or",
        "promote canonical database rows; human source validation remains required.",
        "",
        f"- Evidence rows extracted: {len(output_rows):,}",
        f"- Source-review batches: {len(source_counts):,}",
        f"- Full-text candidate rows: {sum(value for key, value in counts.items() if key == 'candidate_extracted_from_full_text'):,}",
        f"- Abstract/metadata candidate rows: {sum(value for key, value in counts.items() if key == 'candidate_extracted_from_abstract_or_metadata'):,}",
        f"- Unmatched local-artifact rows: {sum(value for key, value in counts.items() if key == 'artifact_present_excerpt_not_matched'):,}",
        f"- Awaiting source acquisition: {sum(value for key, value in counts.items() if key == 'awaiting_source_acquisition'):,}",
        "",
        "## Included source-review batches",
        "",
        "| Source review | Evidence rows |",
        "|---|---:|",
    ]
    lines.extend(f"| {key} | {value:,} |" for key, value in sorted(source_counts.items()))
    lines.extend([
        "",
        "## Boundary",
        "",
        "The registered evidence summary is retained alongside the local source",
        "excerpt so the provenance chain is explicit. Excerpts are candidate text",
        "matches, not adjudicated atomic observations or AuthorClaims. Abstract-only",
        "sources remain abstract-bounded, and every row remains unpromoted.",
        "",
    ])
    report.write_text("\n".join(lines), encoding="utf-8")
    print(f"extraction_rows={len(output_rows)} source_reviews={len(source_counts)} output={output}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--register", type=Path, default=DEFAULT_REGISTER)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()
    build(args.register, args.manifest, args.output, args.report)


if __name__ == "__main__":
    main()
