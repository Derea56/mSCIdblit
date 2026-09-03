#!/usr/bin/env python3
"""Materialize signed public TF-target assertions for Module 22B.

This batch uses exact simple-symbol pairs from the public TF review queue.  It
requires a non-conflicting signed effect and OmniPath/DoRothEA level A or B
support.  The resulting edges describe general inferred regulatory capacity;
they do not assert direct binding, SCI activity, or ligand-to-TF causality.
"""

from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
QUEUE_PATH = ROOT / "data/processed/public_tf_union_v1/module_curation/module_22_priority_tf_review_queue.tsv"
AUDIT_PATH = ROOT / (
    "work/module22b_tf_regulon_promotion_audit/"
    "module22b_signed_public_tf_promotion_batch002.tsv"
)
SUMMARY_PATH = ROOT / (
    "work/module22b_tf_regulon_promotion_audit/"
    "module22b_signed_public_tf_promotion_batch002_summary.json"
)
BATCH_ID = "module22b-signed-public-tf-promotion-batch002-2026-09-03"
SIMPLE_SYMBOL = re.compile(r"[A-Za-z][A-Za-z0-9-]{1,31}\Z")

EDGE_FIELDS = [
    "b_edge_id", "source_entity", "relation_type", "target_entity",
    "pathway_name", "evidence_layer", "source_a_edge_id", "edge_status",
    "context_scope", "cell_type_context", "compartment_context",
    "species_context", "injury_context", "confidence_tier", "export_priority",
    "exportable", "consolidation_note",
]
EVIDENCE_FIELDS = [
    "b_evidence_id", "source_a_evidence_id", "b_edge_ids", "source_kind",
    "source_locator", "support_kind", "species_support", "source_scope",
    "confidence_tier", "citation_note", "evidence_summary", "limitations",
    "evidence_layer", "exportable", "consolidation_note",
]
AUDIT_FIELDS = [
    "batch_id", "queue_key", "species", "tf_symbol", "target_symbol",
    "b_edge_id", "b_evidence_id", "confidence_tier", "effect_polarity",
    "dorothea_levels", "source_registries", "external_record_keys",
    "reference_count", "source_locator", "module22b_register_changed",
    "general_tf_target_claim", "direct_binding_claim", "upstream_sci_activation_claim",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fields,
            delimiter="\t",
            lineterminator="\r\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def split_values(value: str) -> list[str]:
    return [item.strip() for item in (value or "").split(";") if item.strip() and item.strip() != r"\N"]


def unique(values: list[str]) -> list[str]:
    return list(dict.fromkeys(value for value in values if value))


def next_numeric_id(rows: list[dict[str, str]], field: str) -> int:
    values = []
    for row in rows:
        match = re.search(r"(\d+)\Z", row[field])
        if match:
            values.append(int(match.group(1)))
    return max(values, default=0) + 1


def main() -> int:
    edges = read_tsv(EDGE_PATH)
    evidence = read_tsv(EVIDENCE_PATH)
    queue = read_tsv(QUEUE_PATH)
    if any(row["source_a_edge_id"].startswith("PUBTF-DB-") for row in edges):
        raise SystemExit("batch002 appears to be already materialized")

    grouped: dict[tuple[str, str, str], list[dict[str, str]]] = defaultdict(list)
    for row in queue:
        tf = row["tf_symbol"]
        target = row["target_symbol"]
        if not SIMPLE_SYMBOL.fullmatch(tf) or not SIMPLE_SYMBOL.fullmatch(target):
            continue
        if tf.casefold() == target.casefold():
            continue
        grouped[(row["species_context"], tf.casefold(), target.casefold())].append(row)

    existing_pairs = {
        (row["source_entity"].casefold(), row["target_entity"].casefold())
        for row in edges
        if row["pathway_name"] == "target_gene"
    }
    edge_number = next_numeric_id(edges, "b_edge_id")
    evidence_number = next_numeric_id(evidence, "b_evidence_id")
    audit: list[dict[str, str]] = []

    for queue_key, rows in sorted(grouped.items()):
        species, _, _ = queue_key
        tf = rows[0]["tf_symbol"]
        target = rows[0]["target_symbol"]
        effects = {row["effect_polarity"] for row in rows if row["effect_polarity"] not in {"", "unknown"}}
        levels = unique([level for row in rows for level in split_values(row.get("dorothea_level", ""))])
        if effects not in ({"activating_target"}, {"repressing_target"}):
            continue
        if not any(level.startswith(("A", "B")) for level in levels):
            continue
        if (tf.casefold(), target.casefold()) in existing_pairs:
            continue

        tier = "high" if any(level.startswith("A") for level in levels) else "medium-high"
        effect = next(iter(effects))
        verb = "activates" if effect == "activating_target" else "represses"
        edge_id = f"M22B-E{edge_number:06d}"
        evidence_id = f"M22B-EVID-{evidence_number:06d}"
        source_id = f"PUBTF-DB-{len(audit) + 1:06d}"
        edge_number += 1
        evidence_number += 1

        registries = unique([row["source_registry"] for row in rows])
        record_keys = unique([row["external_record_key"] for row in rows])
        references = unique([ref for row in rows for ref in split_values(row.get("reference_pmids", ""))])
        locator_refs = "; ".join(f"PMID:{ref}" for ref in references[:10])
        source_locator = locator_refs or "public TF union source record"
        reference_count = str(len(references))
        level_text = ";".join(levels) or "not_recorded"
        registry_text = ";".join(registries)
        record_text = ";".join(record_keys)
        effect_text = "activating" if effect == "activating_target" else "repressing"

        edges.append({
            "b_edge_id": edge_id,
            "source_entity": tf,
            "relation_type": (
                f"{tf} {verb} the {target} target gene according to signed "
                "public TF regulatory evidence; inferred regulatory relationship"
            ),
            "target_entity": target,
            "pathway_name": "target_gene",
            "evidence_layer": "downstream_or_functional",
            "source_a_edge_id": source_id,
            "edge_status": "reviewed_regulatory_support",
            "context_scope": (
                f"General {effect_text} TF-target assertion in {species}; source-specific "
                "cell/model context is not required for this layer and was not used "
                "to infer SCI activity."
            ),
            "cell_type_context": "not specified by public TF union",
            "compartment_context": "unspecified",
            "species_context": species,
            "injury_context": "not_assessed",
            "confidence_tier": tier,
            "export_priority": "medium",
            "exportable": "true",
            "consolidation_note": (
                f"{BATCH_ID}: {tier} for general signed TF-target regulatory capacity "
                "from level A/B public evidence; not direct-binding proof and no "
                "upstream ligand/receptor-to-TF activation inferred."
            ),
        })
        evidence.append({
            "b_evidence_id": evidence_id,
            "source_a_evidence_id": source_id,
            "b_edge_ids": edge_id,
            "source_kind": "database_curated",
            "source_locator": source_locator,
            "support_kind": "database_curated",
            "species_support": species,
            "source_scope": "inferred_regulatory",
            "confidence_tier": tier,
            "citation_note": (
                f"Module 22 public TF queue; source_registries={registry_text}; "
                f"dorothea_levels={level_text}; external_record_keys={record_text}; "
                f"reference_count={reference_count}; reference_pmids={';'.join(references) or 'none'}"
            ),
            "evidence_summary": (
                f"Signed public TF resources support that {tf} {verb} {target} in "
                f"{species}-scoped inferred regulatory evidence."
            ),
            "limitations": (
                "DoRothEA levels summarize aggregated evidence and do not prove direct "
                "DNA binding. This relationship is not evidence that a particular "
                "ligand/receptor route activates the TF, and no SCI or spinal-cord "
                "activation claim is inferred."
            ),
            "evidence_layer": "downstream_or_functional",
            "exportable": "true",
            "consolidation_note": (
                f"{BATCH_ID}: signed public database evidence retained as inferred "
                "regulatory support with source record provenance."
            ),
        })
        audit.append({
            "batch_id": BATCH_ID,
            "queue_key": f"{species}|{tf.casefold()}|{target.casefold()}",
            "species": species,
            "tf_symbol": tf,
            "target_symbol": target,
            "b_edge_id": edge_id,
            "b_evidence_id": evidence_id,
            "confidence_tier": tier,
            "effect_polarity": effect,
            "dorothea_levels": level_text,
            "source_registries": registry_text,
            "external_record_keys": record_text,
            "reference_count": reference_count,
            "source_locator": source_locator,
            "module22b_register_changed": "true",
            "general_tf_target_claim": "true",
            "direct_binding_claim": "false",
            "upstream_sci_activation_claim": "false",
        })

    write_tsv(EDGE_PATH, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    write_tsv(AUDIT_PATH, audit, AUDIT_FIELDS)
    counts = {
        "batch_id": BATCH_ID,
        "signed_public_tf_edges_added": len(audit),
        "high_edges_added": sum(row["confidence_tier"] == "high" for row in audit),
        "medium_high_edges_added": sum(row["confidence_tier"] == "medium-high" for row in audit),
        "high_edges_after": sum(row["confidence_tier"] == "high" for row in edges),
        "medium_high_edges_after": sum(row["confidence_tier"] == "medium-high" for row in edges),
        "target_gene_edges_after": sum(row["pathway_name"] == "target_gene" for row in edges),
        "exportable_edges_after": sum(row["exportable"] == "true" for row in edges),
        "module22b_register_changed": True,
        "direct_binding_inferred": False,
        "upstream_sci_activation_inferred": False,
        "audit": str(AUDIT_PATH),
    }
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(json.dumps(counts, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(counts, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
