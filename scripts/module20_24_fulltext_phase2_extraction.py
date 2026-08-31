#!/usr/bin/env python3
"""Build, fetch, and conservatively screen Module 20B–24B full-text queues.

This script is a Phase-2 preparation and candidate-extraction tool. It never
promotes a snippet to a validated Observation or AuthorClaim and never writes
canonical database tables. Human/full-text validation remains required before
the phase-2 integration gate.

Examples:

  python3 scripts/module20_24_fulltext_phase2_extraction.py build-queue
  python3 scripts/module20_24_fulltext_phase2_extraction.py fetch --lane C_23B
  python3 scripts/module20_24_fulltext_phase2_extraction.py extract --lane C_23B
  python3 scripts/module20_24_fulltext_phase2_extraction.py extract --all
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
import time
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode, urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
REVIEW_ROOT = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review"
QUEUE_ROOT = REVIEW_ROOT / "phase2_queues"
CACHE_ROOT = ROOT / "data" / "raw" / "evidence" / "module20_24_phase2_fulltext"
PHASE1 = REVIEW_ROOT / "module20_24_integrated_canonical_evidence_review.tsv"

LANES = {
    "A_20B": {"M20B"},
    "B_21B_22B": {"M21B", "M22B"},
    "C_23B": {"M23B"},
    "D_24B": {"M24B"},
}

QUEUE_FIELDS = [
    "queue_id", "module", "b_edge_id", "b_evidence_id", "evidence_layer",
    "canonical_paper_key", "anchor_type", "anchor_locator", "paper_status",
    "observation_status", "claim_status", "species", "cell_type_or_model",
    "assay_or_perturbation", "relation_type", "pathway_or_branch",
    "context_and_limitations", "source_locator", "search_boundary",
]

EXTRACTION_FIELDS = [
    "extraction_id", "module", "b_edge_id", "b_evidence_id", "evidence_layer",
    "canonical_paper_key", "paper_status", "observation_status",
    "observation_id_or_action", "observation_value_or_blocker",
    "observation_source_section", "observation_figure_or_table",
    "observation_species", "observation_cell_or_model", "observation_assay",
    "observation_perturbation", "claim_status", "claim_id_or_action",
    "claim_text_or_blocker", "claim_source_section", "confidence",
    "context_and_limitations", "source_locator", "search_boundary",
    "reviewer_notes", "fulltext_path", "fulltext_access_status",
    "candidate_observation_snippet", "candidate_claim_snippet",
]

TOKEN_RE = re.compile(
    r"(?P<pmid>PMID:\s*\d+)|(?P<pmcid>PMCID:\s*PMC\d+)|"
    r"(?P<doi>DOI:\s*10\.[^;\s]+)|(?P<url>https?://[^;\s]+)",
    re.IGNORECASE,
)


class VisibleTextParser(HTMLParser):
    """Extract visible text while skipping script/style/navigation noise."""

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
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def split_tokens(value: str) -> list[tuple[str, str]]:
    result: list[tuple[str, str]] = []
    for match in TOKEN_RE.finditer(value or ""):
        kind = match.lastgroup or "url"
        locator = match.group(0).strip().rstrip(".,)")
        if kind == "pmid":
            locator = "PMID:" + re.sub(r"\D", "", locator)
        elif kind == "pmcid":
            locator = "PMCID:" + re.sub(r"\s+", "", locator).upper().replace("PMCID:", "")
        elif kind == "doi":
            locator = "DOI:" + re.sub(r"^DOI:\s*", "", locator, flags=re.I).lower()
        token = (kind, locator)
        if token not in result:
            result.append(token)
    return result


def lane_for(module: str) -> str:
    module = module.upper()
    if not module.startswith("M"):
        module = "M" + module
    for lane, modules in LANES.items():
        if module in modules:
            return lane
    raise ValueError(f"unsupported module: {module}")


def build_queue(args: argparse.Namespace) -> None:
    if not PHASE1.exists():
        raise SystemExit(f"missing Phase-1 ledger: {PHASE1}")
    source_rows = read_tsv(PHASE1)
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    seen: set[tuple[str, str, str]] = set()
    for row in source_rows:
        module = row["module"].strip().upper()
        if not module.startswith("M"):
            module = "M" + module
        lane = lane_for(module)
        key = (row["b_evidence_id"], row["canonical_paper_key"], row["paper_anchor_locator"])
        if key in seen:
            continue
        seen.add(key)
        queue_id = f"M20_24-P2-{len(seen):06d}"
        anchor_type = row["paper_anchor_type"]
        anchor_locator = row["paper_anchor_locator"]
        canonical = row["canonical_paper_key"]
        for prefix, normalized_type in (("PMID:", "pmid"), ("PMCID:", "pmcid"), ("DOI:", "doi")):
            if canonical.upper().startswith(prefix):
                anchor_type = normalized_type
                anchor_locator = canonical
                break
        grouped[lane].append({
            "queue_id": queue_id,
            "module": module,
            "b_edge_id": row["b_edge_id"],
            "b_evidence_id": row["b_evidence_id"],
            "evidence_layer": row["evidence_layer"],
            "canonical_paper_key": canonical,
            "anchor_type": anchor_type,
            "anchor_locator": anchor_locator,
            "paper_status": row["paper_resolution_status"],
            "observation_status": row["observation_status"],
            "claim_status": row["claim_status"],
            "species": row["species"],
            "cell_type_or_model": row["cell_type_or_model"],
            "assay_or_perturbation": row["assay_or_perturbation"],
            "relation_type": row["relation_type"],
            "pathway_or_branch": row["pathway_or_branch"],
            "context_and_limitations": row["context_and_limitations"],
            "source_locator": row["paper_anchor_locator"] or row.get("source_locator", ""),
            "search_boundary": row["search_boundary"],
        })

    for lane, lane_rows in grouped.items():
        lane_rows.sort(key=lambda row: (row["module"], row["b_evidence_id"], row["anchor_locator"]))
        write_tsv(QUEUE_ROOT / f"phase2_{lane}.tsv", QUEUE_FIELDS, lane_rows)
        batch_size = args.batch_size
        for start in range(0, len(lane_rows), batch_size):
            batch = lane_rows[start : start + batch_size]
            batch_number = start // batch_size + 1
            write_tsv(QUEUE_ROOT / f"phase2_{lane}_batch{batch_number:03d}.tsv", QUEUE_FIELDS, batch)
        report = QUEUE_ROOT / f"phase2_{lane}.md"
        report.write_text(
            f"# Phase-2 Full-Text Queue: {lane}\n\n"
            f"- Queue rows: {len(lane_rows):,}\n"
            f"- Batch size: {batch_size:,}\n"
            f"- Stable paper anchors: {sum(bool(row['canonical_paper_key']) for row in lane_rows):,}\n"
            f"- Manifest/local unresolved anchors: {sum(not row['canonical_paper_key'] for row in lane_rows):,}\n\n"
            "Rows are candidates for full-text extraction only. A source snippet "
            "must be validated against the primary paper before Observation or "
            "AuthorClaim creation.\n"
        )
    print(f"built_queue_rows={len(seen)} lanes={len(grouped)} output={QUEUE_ROOT}")


def cache_stem(kind: str, value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_")
    return f"{kind}_{cleaned}"


def http_get(url: str, timeout: int) -> tuple[bytes, str]:
    request = Request(url, headers={"User-Agent": "mSCIdblit-module20-24-phase2/1.0"})
    with urlopen(request, timeout=timeout) as response:
        return response.read(), response.headers.get_content_type()


def fetch_one(row: dict[str, str], timeout: int) -> dict[str, str]:
    CACHE_ROOT.mkdir(parents=True, exist_ok=True)
    anchor_type = row["anchor_type"].lower()
    locator = row["anchor_locator"]
    if anchor_type == "pmcid":
        pmcid = re.sub(r"^PMCID:", "", locator, flags=re.I)
        stem = cache_stem("pmc", pmcid)
        path = CACHE_ROOT / f"{stem}.json"
        url = f"https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/{pmcid}/unicode"
        kind = "pmc_fulltext_bioc"
    elif anchor_type == "pmid":
        pmid = re.sub(r"^PMID:", "", locator, flags=re.I)
        stem = cache_stem("pubmed", pmid)
        path = CACHE_ROOT / f"{stem}.xml"
        params = urlencode({"db": "pubmed", "id": pmid, "rettype": "abstract", "retmode": "xml"})
        url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?{params}"
        kind = "pubmed_abstract_xml"
    else:
        return {"fulltext_path": "", "fulltext_access_status": "not_fetchable_stable_publisher_or_doi"}
    if path.exists() and path.stat().st_size:
        return {"fulltext_path": str(path), "fulltext_access_status": f"cached_{kind}"}
    try:
        body, content_type = http_get(url, timeout)
    except (HTTPError, URLError, TimeoutError) as error:
        return {"fulltext_path": "", "fulltext_access_status": f"fetch_failed:{type(error).__name__}"}
    path.write_bytes(body)
    (path.with_suffix(path.suffix + ".meta.json")).write_text(json.dumps({"url": url, "content_type": content_type, "kind": kind}, indent=2))
    return {"fulltext_path": str(path), "fulltext_access_status": f"fetched_{kind}"}


def fetch_queue(args: argparse.Namespace) -> None:
    lanes = selected_lanes(args)
    rows = [row for lane in lanes for row in read_tsv(QUEUE_ROOT / f"phase2_{lane}.tsv")]
    seen: set[tuple[str, str]] = set()
    results: list[dict[str, str]] = []
    for row in rows:
        key = (row["anchor_type"], row["anchor_locator"])
        if not row["anchor_locator"] or key in seen:
            continue
        seen.add(key)
        result = fetch_one(row, args.timeout)
        results.append({**row, **result})
        time.sleep(args.sleep)
    write_tsv(QUEUE_ROOT / "phase2_fetch_manifest.tsv", QUEUE_FIELDS + ["fulltext_path", "fulltext_access_status"], results)
    print(f"fetch_manifest_rows={len(results)}")


def load_text(path: Path) -> str:
    raw = path.read_bytes()
    suffix = path.suffix.lower()
    if suffix in {".html", ".htm"}:
        parser = VisibleTextParser()
        parser.feed(raw.decode("utf-8", errors="replace"))
        return "\n".join(parser.parts)
    if suffix == ".json":
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            return raw.decode("utf-8", errors="replace")
        strings: list[str] = []
        def collect(value: object) -> None:
            if isinstance(value, str):
                strings.append(value)
            elif isinstance(value, list):
                for item in value:
                    collect(item)
            elif isinstance(value, dict):
                for item in value.values():
                    collect(item)
        collect(data)
        return "\n".join(strings)
    return html.unescape(raw.decode("utf-8", errors="replace"))


def compact(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def terms(row: dict[str, str]) -> list[str]:
    source = " ".join(row.get(key, "") for key in ("relation_type", "pathway_or_branch", "assay_or_perturbation", "context_and_limitations"))
    raw = re.findall(r"[A-Za-z][A-Za-z0-9α-β_/-]{2,}", source)
    stop = {"the", "and", "with", "from", "evidence", "primary", "layer", "context", "not", "only", "this", "that", "were", "was"}
    result: list[str] = []
    for item in raw:
        key = item.casefold()
        if key not in stop and key not in {term.casefold() for term in result}:
            result.append(item)
    return result[:24]


def snippets(text: str, row: dict[str, str]) -> tuple[str, str, str, str]:
    lines = [compact(line) for line in text.splitlines() if compact(line)]
    key_terms = terms(row)
    key_lower = [term.casefold() for term in key_terms if len(term) >= 4]
    experimental = re.compile(r"assay|stimulat|treat|knockout|knockdown|inhibit|phosph|reporter|binding|immunoblot|migration|expression|transfect|perturb|deplet|block", re.I)
    claim_words = re.compile(r"we show|we demonstrate|these results|our findings|suggest|indicate|conclude|support", re.I)
    observation_candidates: list[tuple[int, str]] = []
    claim_candidates: list[tuple[int, str]] = []
    section = "unknown"
    for line in lines:
        heading = re.match(r"^(abstract|introduction|methods?|results?|discussion|conclusions?|figure|table)\b", line, re.I)
        if heading:
            section = heading.group(1).lower()
        lower = line.casefold()
        hits = sum(term in lower for term in key_lower)
        if hits and experimental.search(line):
            observation_candidates.append((hits, f"[{section}] {line[:700]}"))
        if claim_words.search(line) and section in {"abstract", "results", "discussion", "conclusion", "conclusions"}:
            claim_candidates.append((1, f"[{section}] {line[:700]}"))
    observation = max(observation_candidates, default=(0, ""), key=lambda item: item[0])[1]
    claim = max(claim_candidates, default=(0, ""), key=lambda item: item[0])[1]
    return observation, claim, section, ";".join(key_terms[:12])


def extract_row(row: dict[str, str], fetch_map: dict[tuple[str, str], dict[str, str]]) -> dict[str, str]:
    module = row["module"].strip().upper()
    evidence_id = row["b_evidence_id"]
    extraction_id = f"P2-{evidence_id}-{hashlib.sha1((row['canonical_paper_key'] + row['anchor_locator']).encode()).hexdigest()[:8]}"
    fetched = fetch_map.get((row["anchor_type"], row["anchor_locator"]), {})
    fulltext_path = fetched.get("fulltext_path", "")
    access = fetched.get("fulltext_access_status", "not_cached")
    observation = claim = ""
    section = ""
    keywords = ""
    if fulltext_path and Path(fulltext_path).exists():
        observation, claim, section, keywords = snippets(load_text(Path(fulltext_path)), row)
    if not row["canonical_paper_key"]:
        observation_status = "unresolved_manifest_source"
        observation_action = "RESOLVE_UNDERLYING_PRIMARY_PAPER_REQUIRED before Observation creation."
        observation_blocker = "Frozen Module 20A manifest/local audit anchor has no paper-level full text."
        claim_status = "unresolved_manifest_source"
        claim_action = "RESOLVE_UNDERLYING_PRIMARY_PAPER_REQUIRED before AuthorClaim creation."
        claim_blocker = "No paper-level author claim can be created from the manifest."
    elif not fulltext_path:
        observation_status = "needs_primary_fulltext"
        observation_action = "VALIDATE_OBSERVATION_FROM_PRIMARY_FULLTEXT"
        observation_blocker = "No cached full text; abstract/metadata is insufficient for atomic extraction."
        claim_status = "needs_primary_fulltext"
        claim_action = "VALIDATE_AUTHORCLAIM_FROM_PRIMARY_FULLTEXT"
        claim_blocker = "No cached full text for explicit author interpretation."
    else:
        observation_status = "candidate_requires_curator_validation" if observation else "no_experiment_match"
        observation_action = "VALIDATE_CANDIDATE_SNIPPET_AGAINST_PRIMARY_SOURCE" if observation else "NO_ATOMIC_EXPERIMENT_MATCH; inspect full text manually"
        observation_blocker = observation or "No candidate snippet found by conservative keyword screen."
        claim_status = "candidate_requires_curator_validation" if claim else "no_explicit_claim_match"
        claim_action = "VALIDATE_CANDIDATE_CLAIM_SNIPPET_AGAINST_PRIMARY_SOURCE" if claim else "NO_EXPLICIT_AUTHOR_CLAIM_MATCH; inspect Discussion/Conclusion manually"
        claim_blocker = claim or "No candidate author-claim snippet found by conservative keyword screen."
    return {
        "extraction_id": extraction_id,
        "module": module,
        "b_edge_id": row["b_edge_id"],
        "b_evidence_id": evidence_id,
        "evidence_layer": row["evidence_layer"],
        "canonical_paper_key": row["canonical_paper_key"],
        "paper_status": row["paper_status"],
        "observation_status": observation_status,
        "observation_id_or_action": observation_action,
        "observation_value_or_blocker": observation_blocker,
        "observation_source_section": section or "not located",
        "observation_figure_or_table": "not inferred; curator must locate exact figure/table",
        "observation_species": row["species"],
        "observation_cell_or_model": row["cell_type_or_model"],
        "observation_assay": row["assay_or_perturbation"],
        "observation_perturbation": row["assay_or_perturbation"],
        "claim_status": claim_status,
        "claim_id_or_action": claim_action,
        "claim_text_or_blocker": claim_blocker,
        "claim_source_section": section or "not located",
        "confidence": "uncertain_candidate" if observation or claim else "uncertain",
        "context_and_limitations": row["context_and_limitations"],
        "source_locator": row["source_locator"],
        "search_boundary": row["search_boundary"],
        "reviewer_notes": f"Conservative full-text screen only; keywords={keywords}; no automatic promotion. access={access}",
        "fulltext_path": fulltext_path,
        "fulltext_access_status": access,
        "candidate_observation_snippet": observation,
        "candidate_claim_snippet": claim,
    }


def selected_lanes(args: argparse.Namespace) -> list[str]:
    if args.all:
        return sorted(LANES)
    if args.lane:
        if args.lane not in LANES:
            raise SystemExit(f"unknown lane {args.lane}; choose from {', '.join(sorted(LANES))}")
        return [args.lane]
    raise SystemExit("provide --lane NAME or --all")


def extract_queue(args: argparse.Namespace) -> None:
    lanes = selected_lanes(args)
    fetch_manifest = QUEUE_ROOT / "phase2_fetch_manifest.tsv"
    fetch_map: dict[tuple[str, str], dict[str, str]] = {}
    if fetch_manifest.exists():
        for row in read_tsv(fetch_manifest):
            fetch_map[(row["anchor_type"], row["anchor_locator"])] = row
    for lane in lanes:
        queue = read_tsv(QUEUE_ROOT / f"phase2_{lane}.tsv")
        extracted = [extract_row(row, fetch_map) for row in queue]
        write_tsv(QUEUE_ROOT / f"phase2_{lane}_extractions.tsv", EXTRACTION_FIELDS, extracted)
        counts = Counter(row["observation_status"] for row in extracted)
        (QUEUE_ROOT / f"phase2_{lane}_extractions.md").write_text(
            f"# Phase-2 extraction screen: {lane}\n\n"
            f"- Queue rows screened: {len(extracted):,}\n"
            f"- Observation statuses: {dict(sorted(counts.items()))}\n\n"
            "All candidate snippets require primary-source curator validation; "
            "this output does not create canonical Observation or AuthorClaim rows.\n"
        )
        print(f"lane={lane} extracted={len(extracted)} statuses={dict(sorted(counts.items()))}")


def parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    queue = sub.add_parser("build-queue")
    queue.add_argument("--batch-size", type=int, default=50)
    fetch = sub.add_parser("fetch")
    fetch.add_argument("--lane")
    fetch.add_argument("--all", action="store_true")
    fetch.add_argument("--timeout", type=int, default=30)
    fetch.add_argument("--sleep", type=float, default=0.35)
    extract = sub.add_parser("extract")
    extract.add_argument("--lane")
    extract.add_argument("--all", action="store_true")
    return parser


def main() -> None:
    args = parser().parse_args()
    if args.command == "build-queue":
        build_queue(args)
    elif args.command == "fetch":
        fetch_queue(args)
    elif args.command == "extract":
        extract_queue(args)


if __name__ == "__main__":
    main()
