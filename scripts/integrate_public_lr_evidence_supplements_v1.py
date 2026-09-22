#!/usr/bin/env python3
"""Attach reviewed public-LR primary evidence to existing graph edges.

This is an evidence-source overlay only. It never creates graph edges, never
assigns biological confidence, and never promotes a public-only candidate that
does not already resolve to a current graph edge.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BUNDLE = ROOT / "data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion262"
DEFAULT_LEDGER = ROOT / "data/processed/public_database_comparison_v2/candidate_triage_v1/review_resolution_ledger.tsv"

EDGE_SOURCE_FIELDS = [
    "edge_source_id", "edge_id", "paper_id", "observation_id", "claim_id", "support_kind",
    "species_support", "source_scope", "confidence_tier", "citation_note", "notes",
    "module", "evidence_id", "source_kind", "source_locator", "source_locator_status",
    "evidence_summary", "limitations", "evidence_layer", "evidence_exportable",
    "consolidation_note",
]
SUPPLEMENT_FIELDS = [
    "supplement_id", "candidate_unit_id", "review_batch", "disposition", "edge_id",
    "normalized_ligand_key", "normalized_receptor_key", "supporting_primary_locators",
    "evidence_layer", "species_support", "evidence_summary", "limitations", "integration_status",
]
INTEGRATED_DISPOSITIONS = {
    "already_present_exact_or_alias",
    "hold_contextual_or_complex_boundary",
    "already_present_reverse_orientation",
}
LOCATOR_RE = re.compile(r"(?:PMID|PMCID|DOI):[^;\s]+|https?://[^;\s]+|PDB:[^;\s]+", re.IGNORECASE)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8", errors="replace") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: str(row.get(field, "")) for field in fields} for row in rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    return parser.parse_args()


def normalized_species(value: str) -> str:
    tokens = {token.strip().casefold() for token in re.split(r"[;,]", value) if token.strip()}
    if tokens == {"human"}:
        return "human"
    if tokens == {"mouse"}:
        return "mouse"
    if not tokens:
        return ""
    return "mixed"


def first_paper_id(locators: list[str]) -> str:
    for locator in locators:
        if locator.upper().startswith(("PMID:", "PMCID:", "DOI:")):
            return locator
    return locators[0] if locators else ""


def main() -> int:
    args = parse_args()
    bundle = args.bundle_dir.resolve()
    ledger = args.ledger.resolve()
    edge_path = bundle / "mechanism_edges.tsv"
    source_path = bundle / "mechanism_edge_sources.tsv"
    pathway_path = bundle / "mechanism_pathways.tsv"
    metadata_path = bundle / "bundle_metadata.json"
    edges = read_tsv(edge_path)
    sources = read_tsv(source_path)
    pathways = read_tsv(pathway_path)
    ledger_rows = read_tsv(ledger)
    edge_ids = {row["edge_id"] for row in edges}
    existing_source_ids = {row["edge_source_id"] for row in sources}

    attachments: list[tuple[dict[str, str], str, list[str]]] = []
    skipped_unmatched = 0
    skipped_unresolved = 0
    for row in ledger_rows:
        locators = [token.strip() for token in LOCATOR_RE.findall(row.get("supporting_primary_locators", ""))]
        if row.get("disposition") not in INTEGRATED_DISPOSITIONS or not locators:
            if row.get("disposition") in INTEGRATED_DISPOSITIONS and not locators:
                skipped_unresolved += 1
            continue
        matched = [edge_id for edge_id in row.get("matched_graph_edge_ids", "").split(";") if edge_id]
        valid = [edge_id for edge_id in matched if edge_id in edge_ids]
        if not valid:
            skipped_unmatched += 1
            continue
        for edge_id in valid:
            attachments.append((row, edge_id, locators))

    # A candidate review row is unique evidence, even when it points to a
    # composite edge. Re-running the overlay is therefore safe and deterministic.
    new_sources: list[dict[str, str]] = []
    supplement_rows: list[dict[str, str]] = []
    edge_added_sources: Counter[str] = Counter()
    edge_added_locators: Counter[str] = Counter()
    start = 1
    for row, edge_id, locators in attachments:
        supplement_id = f"PUBLIC-LR-SUPP:{start:06d}"
        source_id = f"PUBLR-SRC{start:06d}"
        evidence_id = supplement_id
        if source_id in existing_source_ids:
            raise SystemExit(f"source ID collision: {source_id}")
        locator_text = "; ".join(locators)
        disposition = row["disposition"]
        scope = "direct_edge" if disposition == "already_present_exact_or_alias" else "contextual_support"
        note = (
            f"public_lr_candidate={row['candidate_unit_id']}; disposition={disposition}; "
            "primary review supplements an existing graph edge; no new edge or causal route asserted."
        )
        source = {
            "edge_source_id": source_id,
            "edge_id": edge_id,
            "paper_id": first_paper_id(locators),
            "observation_id": supplement_id,
            "claim_id": "",
            "support_kind": "primary_experiment",
            "species_support": normalized_species(row.get("species_support", "")),
            "source_scope": scope,
            "confidence_tier": "",
            "citation_note": locator_text,
            "notes": note,
            "module": "public_lr_review",
            "evidence_id": evidence_id,
            "source_kind": "public_lr_primary_review",
            "source_locator": locator_text,
            "source_locator_status": "stable",
            "evidence_summary": row.get("evidence_summary", ""),
            "limitations": row.get("limitations", ""),
            "evidence_layer": row.get("evidence_layer", "ligand_receptor_binding_or_activation"),
            "evidence_exportable": "true",
            "consolidation_note": "Public-LR primary-evidence supplement; evidence-only overlay; mSCS determines route plausibility.",
        }
        new_sources.append(source)
        supplement_rows.append({
            "supplement_id": supplement_id,
            "candidate_unit_id": row["candidate_unit_id"],
            "review_batch": row.get("review_batch", ""),
            "disposition": disposition,
            "edge_id": edge_id,
            "normalized_ligand_key": row.get("normalized_ligand_key", ""),
            "normalized_receptor_key": row.get("normalized_receptor_key", ""),
            "supporting_primary_locators": locator_text,
            "evidence_layer": row.get("evidence_layer", ""),
            "species_support": row.get("species_support", ""),
            "evidence_summary": row.get("evidence_summary", ""),
            "limitations": row.get("limitations", ""),
            "integration_status": "attached_to_existing_graph_edge",
        })
        edge_added_sources[edge_id] += 1
        edge_added_locators[edge_id] += 1
        start += 1

    sources.extend(new_sources)
    write_tsv(source_path, EDGE_SOURCE_FIELDS, sources)
    write_tsv(bundle / "mechanism_public_lr_evidence_supplement.tsv", SUPPLEMENT_FIELDS, supplement_rows)

    for edge in edges:
        edge_id = edge["edge_id"]
        if not edge_added_sources[edge_id]:
            continue
        edge["evidence_count"] = str(int(edge.get("evidence_count", "0") or 0) + edge_added_sources[edge_id])
        edge["source_locator_count"] = str(int(edge.get("source_locator_count", "0") or 0) + edge_added_locators[edge_id])
        existing_evidence = [item for item in edge.get("evidence_ids", "").split(";") if item]
        existing_evidence.extend(row["evidence_id"] for row in new_sources if row["edge_id"] == edge_id)
        edge["evidence_ids"] = ";".join(dict.fromkeys(existing_evidence))
    write_tsv(edge_path, list(edges[0]), edges)

    # Pathway summaries cache evidence counts, so keep them consistent with
    # the edge-source overlay while preserving their edge/node counts.
    sources_by_edge: defaultdict[str, list[dict[str, str]]] = defaultdict(list)
    for source in sources:
        sources_by_edge[source["edge_id"]].append(source)
    for pathway in pathways:
        pathway_evidence = {
            source["evidence_id"]
            for edge in edges
            if edge["module"] == pathway["module"]
            and edge["pathway_name"] == pathway["pathway_name"]
            for source in sources_by_edge.get(edge["edge_id"], [])
        }
        pathway["evidence_count"] = str(len(pathway_evidence))
    write_tsv(pathway_path, list(pathways[0]), pathways)

    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    metadata.setdefault("files", {})["public_lr_evidence_supplement"] = "mechanism_public_lr_evidence_supplement.tsv"
    metadata.setdefault("counts", {})["edge_sources"] = len(sources)
    metadata.setdefault("counts", {})["public_lr_evidence_supplements"] = len(supplement_rows)
    metadata.setdefault("graph_policy", {})["public_lr_review_sources_are_evidence_only"] = True
    metadata.setdefault("graph_policy", {})["public_lr_review_sources_create_no_edges"] = True
    statement = (
        "Public-LR primary-evidence supplements are attached only to existing graph edges; "
        "new-edge candidates remain review-only and no biological confidence score is assigned."
    )
    if statement not in metadata.setdefault("accuracy_contract", []):
        metadata["accuracy_contract"].append(statement)
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

    summary = {
        "ledger": str(ledger),
        "bundle": str(bundle),
        "ledger_rows": len(ledger_rows),
        "integrated_supplement_rows": len(supplement_rows),
        "integrated_source_rows": len(new_sources),
        "affected_graph_edges": len(edge_added_sources),
        "skipped_integrated_disposition_without_primary_locator": skipped_unresolved,
        "skipped_primary_rows_without_current_graph_match": skipped_unmatched,
        "new_graph_edges": 0,
        "confidence_scores_created": False,
        "causal_routes_created": False,
    }
    (bundle / "public_lr_evidence_integration_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
