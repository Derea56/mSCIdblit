#!/usr/bin/env python3
"""Route abstract-level evidence decisions for Module 20–24 literature leads.

This produces staging decisions and evidence excerpts. It is intentionally
conservative: no row is canonical evidence and no row is promoted solely from
database membership or keyword matching.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data/processed/module20_24_database_intake_v1/database_literature_review_queue.tsv"
DEFAULT_OUTPUT = ROOT / "data/processed/module20_24_database_intake_v1"

DECISION_FIELDS = [
    "candidate_key", "module_primary", "module_consolidation", "database_ids", "pmid",
    "entity_a", "entity_b", "title", "species", "triage_score", "disposition",
    "evidence_layer", "pair_support", "primary_experiment", "module_fit", "routed_modules",
    "corroboration_required", "direct_terms_found", "module_terms_found", "sci_terms_found",
    "evidence_excerpt", "source_record_ids", "source_locators", "limitations", "decision_basis",
]

ROUTE_TERMS = {
    "20A": ("ligand", "receptor", "binding", "agonist", "antagonist", "complex"),
    "21A": ("jak", "stat", "mapk", "smad", "phosphorylat", "adaptor", "kinase", "cytokine", "chemokine", "relay"),
    "22A": ("transcription factor", "target gene", "promoter", "enhancer", "chip-seq", "binding site", "transcriptional"),
    "23A": ("integrin", "adhesion", "matrix", "collagen", "laminin", "fibronectin", "mechanotransduction", "focal adhesion", "cadherin"),
    "24A": ("complement", "coagulation", "lipid", "protease", "cleavage", "thrombin", "kinin", "eicosanoid", "purinergic", "c1q", "c3", "c5"),
}
DIRECT_TERMS = ("bind", "binding", "ligand", "receptor", "agonist", "antagonist", "activate", "phosphorylat", "cleavage", "blockade", "neutraliz", "knockdown", "knockout", "required", "inhibit")
PRIMARY_TYPES = ("journal article", "research support", "clinical trial", "case reports", "comparative study")
REVIEW_WORDS = ("review", "systematic review", "meta-analysis")


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def norm(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value or "")
    return re.sub(r"\s+", " ", value).strip().casefold()


def terms(text: str, candidates: tuple[str, ...]) -> list[str]:
    lowered = norm(text)
    return [term for term in candidates if term in lowered]


def match_entity(entity: str, text: str) -> bool:
    entity_norm = norm(entity)
    text_norm = norm(text)
    if not entity_norm or not text_norm:
        return False
    if entity_norm in text_norm:
        return True
    tokens = [token for token in re.split(r"[^a-z0-9]+", entity_norm) if len(token) >= 3]
    return any(re.search(rf"\b{re.escape(token)}\b", text_norm) for token in tokens)


def excerpt(text: str, entity_a: str, entity_b: str) -> str:
    sentences = re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text or "").strip())
    for sentence in sentences:
        if match_entity(entity_a, sentence) and match_entity(entity_b, sentence):
            return sentence[:900]
    for sentence in sentences:
        if any(term in norm(sentence) for term in DIRECT_TERMS):
            return sentence[:900]
    return (sentences[0] if sentences else "")[:900]


def classify(row: dict[str, str], reused_pmids: set[str]) -> dict[str, str]:
    text = " ".join(row.get(field, "") or "" for field in ("title", "abstract"))
    a_match = match_entity(row.get("entity_a", ""), text)
    b_match = match_entity(row.get("entity_b", ""), text)
    exact = a_match and b_match
    direct = terms(text, DIRECT_TERMS)
    module_terms = terms(text, ROUTE_TERMS.get(row.get("module_primary", ""), ()))
    sci = terms(text, ("spinal cord", "spinal injury", "sci", "lesion", "contusion", "hemisection", "transection", "astrocyte", "microglia", "macrophage", "neuron"))
    publication = norm(row.get("publication_types", ""))
    review = any(word in publication for word in REVIEW_WORDS)
    try:
        score = int(row.get("triage_score", "0"))
    except ValueError:
        score = 0
    database_ids = set(filter(None, (row.get("database_ids", "") or "").split(";")))
    database_only = all(db.startswith(("omnipath", "reactome")) for db in database_ids) if database_ids else False
    if exact and row.get("abstract_available") == "true" and score >= 8 and not review and not database_only:
        disposition = "abstract_supported_candidate"
    elif exact and row.get("abstract_available") == "true":
        disposition = "hold_for_fulltext"
    elif a_match or b_match or module_terms:
        disposition = "context_only"
    else:
        disposition = "no_exact_support"

    routed: list[str] = [row.get("module_primary", "")]
    lowered = norm(text)
    # A route is a follow-up review candidate only when the paper contains
    # module-specific mechanism terms; generic words such as receptor do not
    # automatically add Module 21.
    downstream = ("phosphorylat", "jak", "stat", "smad", "mapk", "akt", "nf-kb", "kinase", "transcription factor", "target gene")
    if row.get("module_primary") == "20A" and any(term in lowered for term in downstream):
        routed.append("21A")
    if row.get("module_primary") != "23A" and any(term in lowered for term in ROUTE_TERMS["23A"]):
        if a_match or b_match:
            routed.append("23A")
    if row.get("module_primary") != "24A" and any(term in lowered for term in ROUTE_TERMS["24A"]):
        if a_match or b_match:
            routed.append("24A")
    if row.get("module_primary") == "21A" and any(term in lowered for term in ROUTE_TERMS["22A"]):
        routed.append("22A")
    routed = list(dict.fromkeys(routed))
    corr = row.get("pmid", "") in reused_pmids or int(row.get("database_count", "1") or "1") >= 2
    if database_only:
        layer = "integrated_pathway_or_causal_context"
    elif row.get("module_primary") == "20A":
        layer = "ligand_receptor_or_pharmacology"
    elif row.get("module_primary") == "21A":
        layer = "receptor_proximal_or_downstream_relay"
    elif row.get("module_primary") == "23A":
        layer = "ecm_adhesion_or_mechanotransduction"
    else:
        layer = "complement_coagulation_lipid_or_protease_boundary"
    primary = not review and any(word in publication for word in PRIMARY_TYPES)
    limitations = ["abstract-level decision; full text required"]
    if database_only:
        limitations.append("integrated/pathway database source cannot establish direct mechanism")
    if not row.get("abstract"):
        limitations.append("abstract unavailable")
    if len(routed) > 1:
        limitations.append("each routed module requires separate exact-fit review")
    return {
        "candidate_key": row.get("candidate_key", ""), "module_primary": row.get("module_primary", ""),
        "module_consolidation": row.get("module_consolidation", ""), "database_ids": row.get("database_ids", ""),
        "pmid": row.get("pmid", ""), "entity_a": row.get("entity_a", ""), "entity_b": row.get("entity_b", ""),
        "title": row.get("title", ""), "species": row.get("species", ""), "triage_score": str(score),
        "disposition": disposition, "evidence_layer": layer,
        "pair_support": "exact_text_match" if exact else "partial_or_no_text_match",
        "primary_experiment": "likely_primary" if primary else "review_or_uncertain",
        "module_fit": "primary_module_fit" if row.get("module_primary") in routed else "context_only",
        "routed_modules": ";".join(routed), "corroboration_required": str(corr).lower(),
        "direct_terms_found": ";".join(direct), "module_terms_found": ";".join(module_terms),
        "sci_terms_found": ";".join(sci), "evidence_excerpt": excerpt(text, row.get("entity_a", ""), row.get("entity_b", "")),
        "source_record_ids": row.get("source_record_ids", ""), "source_locators": row.get("source_locators", ""),
        "limitations": "; ".join(limitations),
        "decision_basis": "; ".join(row.get("notes", "").split("; ")[:3]) + "; conservative abstract-level routing; no canonical promotion",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    rows = read_tsv(args.input)
    cross_path = args.output_dir / "cross_module_paper_corroboration_queue.tsv"
    reused_pmids = {row.get("pmid", "") for row in read_tsv(cross_path)} if cross_path.exists() else set()
    decisions = [classify(row, reused_pmids) for row in rows]
    decisions.sort(key=lambda row: (-int(row["triage_score"]), row["module_primary"], row["pmid"], row["entity_a"], row["entity_b"]))
    all_path = args.output_dir / "database_evidence_decisions.tsv"
    with all_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=DECISION_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(decisions)
    by_module = {module: [row for row in decisions if row["module_primary"] == module] for module in ("20A", "21A", "23A", "24A")}
    for module, module_rows in by_module.items():
        with (args.output_dir / f"module_{module}_evidence_decisions.tsv").open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=DECISION_FIELDS, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(module_rows)
    routed = [row for row in decisions if ";" in row["routed_modules"]]
    with (args.output_dir / "cross_module_routing_candidates.tsv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=DECISION_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(routed)
    cross_fields = [
        "handoff_id", "candidate_key", "pmid", "source_module", "target_module", "module_consolidation",
        "database_ids", "species", "entity_a", "entity_b", "disposition", "evidence_layer",
        "evidence_excerpt", "corroboration_required", "target_module_review_status", "notes",
    ]
    cross_rows = []
    for row in routed:
        targets = [module for module in row["routed_modules"].split(";") if module and module != row["module_primary"]]
        for index, target in enumerate(targets, start=1):
            cross_rows.append({
                "handoff_id": f"DBINT-XMOD-{len(cross_rows)+1:06d}",
                "candidate_key": row["candidate_key"], "pmid": row["pmid"],
                "source_module": row["module_primary"], "target_module": target,
                "module_consolidation": target.replace("A", "B") if target.endswith("A") else "",
                "database_ids": row["database_ids"], "species": row["species"],
                "entity_a": row["entity_a"], "entity_b": row["entity_b"],
                "disposition": row["disposition"], "evidence_layer": row["evidence_layer"],
                "evidence_excerpt": row["evidence_excerpt"], "corroboration_required": "true",
                "target_module_review_status": "needs_target_module_review",
                "notes": "Keyword-supported upstream/downstream handoff candidate; target module must independently confirm the claim and source scope.",
            })
    with (args.output_dir / "cross_module_evidence_handoff_queue.tsv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=cross_fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(cross_rows)
    manifest = {
        "input_rows": len(rows), "decision_rows": len(decisions),
        "by_module": {module: len(module_rows) for module, module_rows in by_module.items()},
        "by_disposition": dict(sorted(Counter(row["disposition"] for row in decisions).items())),
        "cross_module_routing_candidates": len(routed),
        "cross_module_handoff_rows": len(cross_rows),
        "corroboration_required": sum(row["corroboration_required"] == "true" for row in decisions),
        "abstract_level_only": True, "canonical_write_performed": False,
    }
    (args.output_dir / "database_evidence_decision_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
