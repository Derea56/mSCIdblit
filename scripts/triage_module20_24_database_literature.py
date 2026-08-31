#!/usr/bin/env python3
"""Create conservative, abstract-level review queues for database literature leads.

The output is prioritization only. A high triage score is not a promotion
decision and does not substitute for full-text review of exact pair/complex,
species, assay, perturbation, and injury context.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data/processed/module20_24_database_intake_v1/database_literature_leads.tsv"
DEFAULT_CANDIDATES = ROOT / "data/processed/module20_24_database_intake_v1/database_candidate_leads.tsv"
DEFAULT_OUTPUT = ROOT / "data/processed/module20_24_database_intake_v1"

DIRECT_TERMS = ("bind", "binding", "ligand", "receptor", "agonist", "antagonist", "activate", "phosphorylat", "cleavage", "blockade", "neutraliz", "knockdown", "knockout", "required", "inhibit")
SCI_TERMS = ("spinal cord", "spinal injury", "sci", "lesion", "contusion", "hemisection", "transection", "traumatic", "astrocyte", "microglia", "macrophage", "oligodendrocyte", "neuron")
MODULE_TERMS = {
    "20A": ("ligand", "receptor", "complex", "co-receptor", "decoy", "binding"),
    "21A": ("jak", "stat", "mapk", "smad", "phosphorylat", "cytokine", "chemokine", "relay", "adaptor"),
    "23A": ("integrin", "adhesion", "matrix", "collagen", "laminin", "fibronectin", "mechanotransduction", "focal adhesion", "cadherin"),
    "24A": ("complement", "coagulation", "lipid", "protease", "cleavage", "thrombin", "kinin", "eicosanoid", "purinergic", "c1q", "c3", "c5"),
}


FIELDS = [
    "candidate_key", "module_primary", "module_consolidation", "database_ids", "database_count",
    "source_record_ids", "species", "entity_a", "entity_b", "pathway_or_family", "relationship",
    "effect", "pmid", "title", "abstract", "journal", "year", "publication_types",
    "entity_a_match", "entity_b_match", "exact_pair_text_match", "direct_terms_found",
    "module_terms_found", "sci_terms_found", "review_publication", "abstract_available",
    "triage_score", "suggested_action", "corroboration_flag", "source_locators", "notes",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def normalize(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value or "")
    return re.sub(r"\s+", " ", value).strip().casefold()


def entity_match(entity: str, text: str) -> bool:
    entity_norm = normalize(entity)
    text_norm = normalize(text)
    if not entity_norm or not text_norm:
        return False
    if entity_norm in text_norm:
        return True
    # For aliases/complex strings, require at least one meaningful token. Do
    # not let two-character connector words drive an exact-pair match.
    tokens = [token for token in re.split(r"[^a-z0-9]+", entity_norm) if len(token) >= 3]
    return any(re.search(rf"\b{re.escape(token)}\b", text_norm) for token in tokens)


def found_terms(text: str, terms: tuple[str, ...]) -> list[str]:
    lowered = normalize(text)
    return [term for term in terms if term in lowered]


def row_score(row: dict[str, str]) -> tuple[int, list[str]]:
    text = " ".join((row.get(field, "") or "") for field in ("title", "abstract"))
    direct = found_terms(text, DIRECT_TERMS)
    module = found_terms(text, MODULE_TERMS[row["module_primary"]])
    sci = found_terms(text, SCI_TERMS)
    a_match = entity_match(row.get("entity_a", ""), text)
    b_match = entity_match(row.get("entity_b", ""), text)
    exact = a_match and b_match
    review = "review" in normalize(row.get("publication_types", ""))
    score = 0
    reasons: list[str] = []
    if exact:
        score += 6
        reasons.append("both entities text-matched")
    elif a_match or b_match:
        score += 2
        reasons.append("one entity text-matched")
    score += min(3, len(direct))
    if direct:
        reasons.append("direct/function terms")
    score += min(2, len(module))
    if module:
        reasons.append("module terms")
    if sci:
        score += 2
        reasons.append("SCI/context terms")
    if review:
        score -= 3
        reasons.append("review publication type")
    if not row.get("abstract"):
        score -= 2
        reasons.append("abstract unavailable")
    return score, reasons


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--candidate-input", type=Path, default=DEFAULT_CANDIDATES)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--packet-size", type=int, default=250)
    args = parser.parse_args()

    literature = read_tsv(args.input)
    candidates = read_tsv(args.candidate_input)
    grouped: dict[tuple[str, str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in literature:
        key = (
            row.get("module_primary", ""), normalize(row.get("entity_a", "")),
            normalize(row.get("entity_b", "")), row.get("pmid", ""),
        )
        grouped[key].append(row)

    queue: list[dict[str, str]] = []
    for key, rows in grouped.items():
        best = max(rows, key=lambda row: row_score(row)[0])
        score, reasons = row_score(best)
        text = " ".join((best.get(field, "") or "") for field in ("title", "abstract"))
        a_match = entity_match(best.get("entity_a", ""), text)
        b_match = entity_match(best.get("entity_b", ""), text)
        direct = found_terms(text, DIRECT_TERMS)
        module = found_terms(text, MODULE_TERMS[best["module_primary"]])
        sci = found_terms(text, SCI_TERMS)
        databases = sorted({row.get("database_id", "") for row in rows if row.get("database_id")})
        source_ids = sorted({row.get("source_record_id", "") for row in rows if row.get("source_record_id")})
        locators = sorted({row.get("source_locator", "") for row in rows if row.get("source_locator")})
        review = "review" in normalize(best.get("publication_types", ""))
        action = "review_high_priority" if score >= 8 and a_match and b_match else "review_context" if score >= 4 else "hold_for_fulltext_or_gap_search"
        queue.append({
            "candidate_key": "::".join(key),
            "module_primary": best.get("module_primary", ""),
            "module_consolidation": best.get("module_consolidation", ""),
            "database_ids": ";".join(databases),
            "database_count": str(len(databases)),
            "source_record_ids": ";".join(source_ids),
            "species": best.get("species", ""),
            "entity_a": best.get("entity_a", ""),
            "entity_b": best.get("entity_b", ""),
            "pathway_or_family": best.get("pathway_or_family", ""),
            "relationship": best.get("relationship", ""),
            "effect": best.get("effect", ""),
            "pmid": best.get("pmid", ""),
            "title": best.get("title", ""),
            "abstract": best.get("abstract", ""),
            "journal": best.get("journal", ""),
            "year": best.get("year", ""),
            "publication_types": best.get("publication_types", ""),
            "entity_a_match": str(a_match).lower(),
            "entity_b_match": str(b_match).lower(),
            "exact_pair_text_match": str(a_match and b_match).lower(),
            "direct_terms_found": ";".join(direct),
            "module_terms_found": ";".join(module),
            "sci_terms_found": ";".join(sci),
            "review_publication": str(review).lower(),
            "abstract_available": str(bool(best.get("abstract"))).lower(),
            "triage_score": str(score),
            "suggested_action": action,
            "corroboration_flag": "multi_database" if len(databases) >= 2 else "single_database",
            "source_locators": ";".join(locators),
            "notes": "; ".join(reasons) + "; abstract-level triage only; no promotion implied",
        })

    queue.sort(key=lambda row: (-int(row["triage_score"]), row["module_primary"], row["entity_a"], row["entity_b"], row["pmid"]))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    with (args.output_dir / "database_literature_review_queue.tsv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(queue)

    # Split complete review queues and bounded agent packets. Every module gets
    # a file even when a later source acquisition produces zero rows.
    by_module = defaultdict(list)
    for row in queue:
        by_module[row["module_primary"]].append(row)
    for module in ("20A", "21A", "23A", "24A"):
        rows = by_module[module]
        path = args.output_dir / f"module_{module}_database_literature_review_queue.tsv"
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        packet = args.output_dir / f"module_{module}_database_literature_priority_packet.tsv"
        with packet.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows[:args.packet_size])

    no_lit = [row for row in candidates if not row.get("linked_pmids")]
    no_lit_path = args.output_dir / "database_no_linked_literature_leads.tsv"
    if candidates:
        with no_lit_path.open("w", newline="", encoding="utf-8") as handle:
            fields = list(candidates[0])
            writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(no_lit)

    manifest = {
        "input_rows": len(literature),
        "unique_module_entity_pmid_candidates": len(queue),
        "queue_rows_by_module": dict(sorted(Counter(row["module_primary"] for row in queue).items())),
        "priority_packet_size": args.packet_size,
        "no_linked_literature_leads": len(no_lit),
        "high_priority_rows": sum(row["suggested_action"] == "review_high_priority" for row in queue),
        "multi_database_rows": sum(row["corroboration_flag"] == "multi_database" for row in queue),
        "abstract_level_only": True,
        "canonical_write_performed": False,
    }
    (args.output_dir / "database_literature_triage_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
