#!/usr/bin/env python3
"""Reconcile historical full-route curation rows to the current graph IDs.

Historical curation batches retain primary evidence and human-readable labels,
but node IDs were reindexed during later graph builds.  This utility resolves
those rows against the current edge labels, rejects ambiguous mappings, and
emits only evidence-layer route annotations that can be validated by the
literature-expansion builder.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import re
from collections import defaultdict
from pathlib import Path


FULL_PATH = "ligand>receptor>intracellular>TF>target_gene_expression"

RECEPTOR_SOURCE_ALIASES = {
    frozenset({"mpl", "mpltporeceptor"}),
    frozenset({"tlr2", "tlr2tirdomain"}),
    frozenset({"tlr4", "tlr4tirdomain"}),
    frozenset({"epor", "eporeporeceptor"}),
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def normalize(value: str) -> str:
    value = value.casefold().replace("κ", "k").replace("β", "b").replace("α", "a")
    return re.sub(r"[^a-z0-9]+", "", value)


def relaxed(value: str) -> str:
    value = normalize(value)
    for token in ("gene", "target", "promoter", "enhancer", "expression"):
        value = value.replace(token, "")
    return value


def label_match(left: str, right: str) -> bool:
    exact = normalize(left) == normalize(right)
    if exact:
        return True
    left_relaxed, right_relaxed = relaxed(left), relaxed(right)
    if left_relaxed and left_relaxed == right_relaxed:
        return True
    return bool(left_relaxed and right_relaxed and (left_relaxed in right_relaxed or right_relaxed in left_relaxed) and min(len(left_relaxed), len(right_relaxed)) >= 5)


def label_parts(value: str) -> list[str]:
    """Return the independently named components of a composite label."""

    return [part.strip() for part in re.split(r"[/;,]", value) if part.strip()]


def intermediate_label_match(edge_label: str, historical_label: str) -> bool:
    if label_match(edge_label, historical_label):
        return True
    return any(label_match(edge_label, part) for part in label_parts(historical_label))


def receptor_source_match(edge_label: str, historical_label: str) -> bool:
    if label_match(edge_label, historical_label):
        return True
    pair = frozenset({normalize(edge_label), normalize(historical_label)})
    return pair in RECEPTOR_SOURCE_ALIASES


def join_unique(values: list[str]) -> str:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        for item in value.split(";"):
            item = item.strip()
            if item and item not in seen:
                seen.add(item)
                result.append(item)
    return "; ".join(result)


def resolve_edge(
    row: dict[str, str],
    edges: dict[str, dict[str, str]],
    source_label: str,
    target_label: str,
    edge_field: str,
) -> tuple[dict[str, str] | None, str]:
    old_id = row.get(edge_field, "")
    old = edges.get(old_id)
    if old and label_match(old["source_label"], source_label) and label_match(old["target_label"], target_label):
        return old, "historical_edge_id"
    candidates = [
        edge for edge in edges.values()
        if label_match(edge["source_label"], source_label) and label_match(edge["target_label"], target_label)
    ]
    if len(candidates) == 1:
        return candidates[0], "current_label_match"
    return None, f"ambiguous_or_missing:{len(candidates)}"


def resolve_receptor_edges(
    row: dict[str, str],
    edges: dict[str, dict[str, str]],
    receptor_node_id: str,
    receptor_label: str,
) -> tuple[list[dict[str, str]], str]:
    """Resolve receptor-proximal edges, including explicit composite intermediates.

    Historical rows sometimes report a receptor-associated pair such as
    ``JAK1/JAK3`` while the current graph stores one edge per kinase.  When
    the current receptor node is exact, each matching component is retained as
    its own evidence route.  A label-based fallback is limited to a historical
    edge ID whose current source label still matches, preserving known receptor
    aliases without guessing a new receptor identity.
    """

    historical_edge_id = row.get("receptor_intracellular_edge_id", "")
    historical_edge = edges.get(historical_edge_id)
    intermediate_label = row.get("intracellular_continuation_label", "")
    parts = label_parts(intermediate_label)
    if historical_edge and intermediate_label_match(historical_edge["target_label"], intermediate_label) and len(parts) <= 1:
        if historical_edge["source_node_id"] == receptor_node_id or receptor_source_match(historical_edge["source_label"], receptor_label):
            return [historical_edge], "historical_edge_id"

    exact_candidates = [
        edge
        for edge in edges.values()
        if edge["source_node_id"] == receptor_node_id
        and intermediate_label_match(edge["target_label"], intermediate_label)
    ]
    if exact_candidates:
        return exact_candidates, "current_receptor_match"
    alias_candidates = [
        edge
        for edge in edges.values()
        if receptor_source_match(edge["source_label"], receptor_label)
        and intermediate_label_match(edge["target_label"], intermediate_label)
    ]
    return alias_candidates, "receptor_source_alias" if alias_candidates else "ambiguous_or_missing:0"


def historical_rows(root: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    seen: set[str] = set()
    for path in sorted((root / "work/module_b_consolidation/module21b").glob("module21b_literature_expansion_batch*.json")):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        for row in payload:
            expansion_id = str(row.get("expansion_id", ""))
            if row.get("path_expression") != FULL_PATH or not expansion_id or expansion_id in seen:
                continue
            seen.add(expansion_id)
            rows.append({str(key): "" if value is None else str(value) for key, value in row.items()})
    return rows


def reconcile(root: Path, bundle: Path) -> tuple[list[dict[str, str]], dict[str, object]]:
    edges_list = read_tsv(bundle / "mechanism_edges.tsv")
    edges = {row["edge_id"]: row for row in edges_list}
    queue_ids = {row["queue_id"] for row in read_tsv(bundle / "mechanism_downstream_curation_queue.tsv")}
    evidence_ids = {row["record_id"] for row in read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")}
    with gzip.open(bundle / "mechanism_signaling_route_evidence.tsv.gz", "rt", encoding="utf-8", newline="") as handle:
        existing_chains = {row["source_chain_id"] for row in csv.DictReader(handle, delimiter="\t") if row["route_evidence_id"].startswith("LITEXP:")}
    sources_by_edge: dict[str, list[dict[str, str]]] = defaultdict(list)
    for source in read_tsv(bundle / "mechanism_edge_sources.tsv"):
        sources_by_edge[source["edge_id"]].append(source)

    output: list[dict[str, str]] = []
    skipped: list[dict[str, str]] = []
    source_rows = historical_rows(root)
    for row in source_rows:
        expansion_id = row["expansion_id"]
        if expansion_id in existing_chains:
            skipped.append({"expansion_id": expansion_id, "reason": "already_materialized"})
            continue
        if row.get("source_queue_id") not in queue_ids:
            skipped.append({"expansion_id": expansion_id, "reason": "missing_source_queue"})
            continue
        if row.get("source_evidence_record_id") not in evidence_ids:
            skipped.append({"expansion_id": expansion_id, "reason": "missing_source_evidence_record"})
            continue

        lr_edge, lr_resolution = resolve_edge(row, edges, row["ligand_label"], row["receptor_label"], "ligand_receptor_edge_id")
        tf_edge, tf_resolution = resolve_edge(row, edges, row["transcription_factor_label"], row["target_gene_label"], "tf_target_edge_id")
        if not lr_edge or not tf_edge:
            skipped.append({"expansion_id": expansion_id, "reason": f"lr={lr_resolution};tf={tf_resolution}"})
            continue

        receptor_node_id = lr_edge["target_node_id"]
        ligand_node_id = lr_edge["source_node_id"]
        tf_node_id = tf_edge["source_node_id"]
        target_node_id = tf_edge["target_node_id"]
        receptor_edges, receptor_resolution = resolve_receptor_edges(
            row,
            edges,
            receptor_node_id,
            lr_edge["target_label"],
        )

        if not receptor_edges:
            skipped.append({"expansion_id": expansion_id, "reason": "missing_or_ambiguous_receptor_intracellular_edge"})
            continue

        for branch_index, receptor_edge in enumerate(receptor_edges, start=1):
            intermediate_id = receptor_edge["target_node_id"]
            intermediate_label = receptor_edge["target_label"]
            intracellular_tf_edge = edges.get(row.get("intracellular_tf_edge_id", ""))
            if not intracellular_tf_edge or intracellular_tf_edge["source_node_id"] != intermediate_id or intracellular_tf_edge["target_node_id"] != tf_node_id:
                intracellular_tf_edge = None

            branch_id = expansion_id
            linkage_parts = [
                "historical_primary_route_reconciled",
                "primary_layer_linked",
            ]
            if len(receptor_edges) > 1:
                branch_id = f"{expansion_id}-via-{normalize(intermediate_label)}"
                linkage_parts.append(f"composite_intermediate_split:{row.get('intracellular_continuation_label', '')}")
            if receptor_edge["source_node_id"] != receptor_node_id or not label_match(receptor_edge["source_label"], lr_edge["target_label"]):
                linkage_parts.append(f"receptor_identity_alias:{receptor_edge['source_label']}")
            if len(label_parts(row.get("intracellular_continuation_label", ""))) > 1 and not label_match(
                intermediate_label,
                row.get("intracellular_continuation_label", ""),
            ):
                linkage_parts.append(f"composite_relay_reconciled:{row.get('intracellular_continuation_label', '')}")
            if not intracellular_tf_edge:
                linkage_parts.append("intracellular_to_tf_edge_not_asserted")
            linkage_parts.append("evidence_route_only")

            reconciled = dict(row)
            reconciled.update(
                {
                    "expansion_id": branch_id,
                    "ligand_node_id": ligand_node_id,
                    "ligand_label": lr_edge["source_label"],
                    "ligand_receptor_edge_id": lr_edge["edge_id"],
                    "receptor_node_id": receptor_node_id,
                    "receptor_label": lr_edge["target_label"],
                    "receptor_intracellular_edge_id": receptor_edge["edge_id"],
                    "intracellular_continuation_node_id": intermediate_id,
                    "intracellular_continuation_label": intermediate_label,
                    "intracellular_tf_edge_id": intracellular_tf_edge["edge_id"] if intracellular_tf_edge else "",
                    "transcription_factor_node_id": tf_node_id,
                    "transcription_factor_label": tf_edge["source_label"],
                    "tf_target_edge_id": tf_edge["edge_id"],
                    "target_gene_node_id": target_node_id,
                    "target_gene_label": tf_edge["target_label"],
                    "output_node_id": target_node_id,
                    "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
                    "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
                    "intracellular_status": "source_supported",
                    "route_linkage_status": ";".join(linkage_parts),
                    "causal_status": "not_asserted",
                    "traversal_status": "evidence_route_not_causal",
                    "source_chain_id": branch_id,
                    "route_status": "retained_evidence_route",
                    "evidence_ids": join_unique(
                        [
                            row.get("evidence_ids", ""),
                            lr_edge["edge_id"],
                            tf_edge["edge_id"],
                            receptor_edge["edge_id"],
                            intracellular_tf_edge["edge_id"] if intracellular_tf_edge else "",
                            *[source.get("source_locator", "") for source in sources_by_edge[lr_edge["edge_id"]]],
                            *[source.get("source_locator", "") for source in sources_by_edge[tf_edge["edge_id"]]],
                        ]
                    ),
                    "missing_layers": "" if intracellular_tf_edge else "intracellular_to_tf_edge",
                }
            )
            output.append(reconciled)

    audit = {
        "historical_unique_full_routes": len(source_rows),
        "existing_materialized_routes": sum(item["reason"] == "already_materialized" for item in skipped),
        "rows_emitted": len(output),
        "rows_skipped": len(skipped),
        "skipped": skipped,
        "ligands_emitted": len({row["ligand_label"] for row in output}),
    }
    return output, audit


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    args = parser.parse_args()
    rows, audit = reconcile(args.root.resolve(), args.bundle.resolve())
    args.output.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    args.audit.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: audit[key] for key in ("historical_unique_full_routes", "existing_materialized_routes", "rows_emitted", "rows_skipped", "ligands_emitted")}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
