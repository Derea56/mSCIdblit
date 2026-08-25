#!/usr/bin/env python3
"""Export a conservative Module 20B–24B mechanism graph release.

The local Module 20B–24B registers are the source for this release artifact.
Only edge-register rows marked ``exportable=true`` become graph edges. Every
node label is preserved as curated; composite labels are not silently split or
aliased. Evidence rows for exported edges remain attached as source records,
including non-exportable boundary evidence so the graph stays auditable.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import unicodedata
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULES = ("20", "21", "22", "23", "24")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "data" / "processed" / "mechanism_graph_module20_24_v2026_08_25",
        help="Directory for the release bundle.",
    )
    parser.add_argument(
        "--source-root",
        type=Path,
        default=ROOT / "work" / "module_b_consolidation",
        help="Directory containing module20b–module24b register directories.",
    )
    return parser.parse_args()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fieldnames,
            delimiter="\t",
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def split_ids(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()]


def node_key(label: str) -> str:
    normalized = unicodedata.normalize("NFKC", label).strip()
    return " ".join(normalized.split()).casefold()


def source_files(source_root: Path, module: str) -> tuple[Path, Path]:
    directory = source_root / f"module{module}b"
    return (
        directory / f"module{module}b_edge_register.tsv",
        directory / f"module{module}b_evidence_register.tsv",
    )


def public_locator(value: str) -> tuple[str, str]:
    """Keep stable public locators and classify local-only provenance."""
    stable: list[str] = []
    local_or_unstable = False
    for token in value.split(";"):
        token = token.strip()
        if not token:
            continue
        if token.startswith(("PMID:", "PMCID:", "DOI:", "http://", "https://")):
            stable.append(token)
        else:
            local_or_unstable = True
    if stable and local_or_unstable:
        return "; ".join(dict.fromkeys(stable)), "stable_plus_local"
    if stable:
        return "; ".join(dict.fromkeys(stable)), "stable"
    if local_or_unstable:
        return "", "local_only_or_unresolved"
    return "", "missing"


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_release(source_root: Path) -> dict[str, object]:
    all_edges: list[dict[str, str]] = []
    exportable_edges: list[dict[str, str]] = []
    evidence_rows: list[dict[str, str]] = []
    module_stats: list[dict[str, object]] = []

    for module in MODULES:
        edge_path, evidence_path = source_files(source_root, module)
        edges = read_tsv(edge_path)
        evidence = read_tsv(evidence_path)
        for row in edges:
            row = dict(row)
            row["module"] = f"{module}B"
            all_edges.append(row)
            if row.get("exportable") == "true":
                exportable_edges.append(row)
        for row in evidence:
            row = dict(row)
            row["module"] = f"{module}B"
            evidence_rows.append(row)
        module_stats.append(
            {
                "module": f"{module}B",
                "edge_count": len(edges),
                "exportable_edge_count": sum(row.get("exportable") == "true" for row in edges),
                "evidence_count": len(evidence),
                "pathway_count": len({row.get("pathway_name", "") for row in edges}),
                "nonexportable_edge_count": sum(row.get("exportable") != "true" for row in edges),
            }
        )

    exportable_ids = {row["b_edge_id"] for row in exportable_edges}
    evidence_by_edge: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in evidence_rows:
        for edge_id in split_ids(row.get("b_edge_ids", "")):
            if edge_id in exportable_ids:
                evidence_by_edge[edge_id].append(row)

    node_records: dict[str, dict[str, object]] = {}
    for row in exportable_edges:
        for side in ("source_entity", "target_entity"):
            label = row.get(side, "").strip()
            key = node_key(label)
            if not key:
                continue
            record = node_records.setdefault(
                key,
                {
                    "label": label,
                    "labels": set(),
                    "modules": set(),
                    "pathways": set(),
                    "edge_ids": set(),
                    "exportable_edge_count": 0,
                },
            )
            record["labels"].add(label)
            record["modules"].add(row["module"])
            record["pathways"].add(row.get("pathway_name", ""))
            record["edge_ids"].add(row["b_edge_id"])
            record["exportable_edge_count"] += 1

    node_id_by_key = {
        key: f"NODE{index:05d}"
        for index, key in enumerate(sorted(node_records), start=1)
    }
    node_rows: list[dict[str, object]] = []
    for key in sorted(node_records):
        record = node_records[key]
        node_rows.append(
            {
                "node_id": node_id_by_key[key],
                "canonical_label": record["label"],
                "label_variants": "; ".join(sorted(record["labels"])),
                "modules": ";".join(sorted(record["modules"])),
                "pathways": ";".join(sorted(filter(None, record["pathways"]))),
                "exportable_edge_count": len(record["edge_ids"]),
            }
        )

    edge_rows: list[dict[str, object]] = []
    source_rows: list[dict[str, object]] = []
    pathway_edges: dict[tuple[str, str], set[str]] = defaultdict(set)
    pathway_nodes: dict[tuple[str, str], set[str]] = defaultdict(set)
    pathway_evidence: dict[tuple[str, str], set[str]] = defaultdict(set)

    for edge in sorted(exportable_edges, key=lambda row: (row["module"], row["b_edge_id"])):
        source_key = node_key(edge["source_entity"])
        target_key = node_key(edge["target_entity"])
        edge_id = edge["b_edge_id"]
        pathway = edge.get("pathway_name", "")
        pathway_key = (edge["module"], pathway)
        linked_evidence = evidence_by_edge.get(edge_id, [])
        evidence_ids = sorted({row["b_evidence_id"] for row in linked_evidence})
        locator_count = sum(bool(public_locator(row.get("source_locator", ""))[0]) for row in linked_evidence)
        edge_rows.append(
            {
                "edge_id": edge_id,
                "module": edge["module"],
                "source_node_id": node_id_by_key[source_key],
                "target_node_id": node_id_by_key[target_key],
                "source_label": edge["source_entity"],
                "relation_type": edge["relation_type"],
                "target_label": edge["target_entity"],
                "pathway_name": pathway,
                "evidence_layer": edge["evidence_layer"],
                "edge_status": edge["edge_status"],
                "context_scope": edge["context_scope"],
                "cell_type_context": edge["cell_type_context"],
                "compartment_context": edge["compartment_context"],
                "species_context": edge["species_context"],
                "injury_context": edge["injury_context"],
                "confidence_tier": edge["confidence_tier"],
                "export_priority": edge["export_priority"],
                "evidence_ids": ";".join(evidence_ids),
                "evidence_count": len(evidence_ids),
                "source_locator_count": locator_count,
                "exportable": "true",
                "consolidation_note": edge["consolidation_note"],
            }
        )
        pathway_edges[pathway_key].add(edge_id)
        pathway_nodes[pathway_key].update((node_id_by_key[source_key], node_id_by_key[target_key]))
        pathway_evidence[pathway_key].update(evidence_ids)

        for evidence in sorted(linked_evidence, key=lambda row: row["b_evidence_id"]):
            locator, locator_status = public_locator(evidence["source_locator"])
            source_rows.append(
                {
                    "source_id": f"SRC{len(source_rows) + 1:06d}",
                    "edge_id": edge_id,
                    "module": edge["module"],
                    "evidence_id": evidence["b_evidence_id"],
                    "source_kind": evidence["source_kind"],
                    "source_locator": locator,
                    "source_locator_status": locator_status,
                    "support_kind": evidence["support_kind"],
                    "species_support": evidence["species_support"],
                    "source_scope": evidence["source_scope"],
                    "confidence_tier": evidence["confidence_tier"],
                    "citation_note": evidence["citation_note"],
                    "evidence_summary": evidence["evidence_summary"],
                    "limitations": evidence["limitations"],
                    "evidence_layer": evidence["evidence_layer"],
                    "evidence_exportable": evidence["exportable"],
                    "consolidation_note": evidence["consolidation_note"],
                }
            )

    pathway_rows = [
        {
            "module": module,
            "pathway_name": pathway,
            "edge_count": len(pathway_edges[(module, pathway)]),
            "node_count": len(pathway_nodes[(module, pathway)]),
            "evidence_count": len(pathway_evidence[(module, pathway)]),
        }
        for module, pathway in sorted(pathway_edges)
    ]

    boundary_counter: Counter[tuple[str, str, str, str, str]] = Counter()
    for edge in all_edges:
        if edge.get("exportable") == "true":
            continue
        key = (
            edge["module"],
            edge.get("pathway_name", ""),
            edge.get("evidence_layer", ""),
            edge.get("edge_status", ""),
            edge.get("export_priority", ""),
        )
        boundary_counter[key] += 1
    boundary_rows = [
        {
            "module": key[0],
            "pathway_name": key[1],
            "evidence_layer": key[2],
            "edge_status": key[3],
            "export_priority": key[4],
            "nonexportable_edge_count": count,
        }
        for key, count in sorted(boundary_counter.items())
    ]

    input_registers = []
    for module in MODULES:
        edge_path, evidence_path = source_files(source_root, module)
        input_registers.extend(
            {
                "module": f"{module}B",
                "file": path.name,
                "sha256": file_sha256(path),
            }
            for path in (edge_path, evidence_path)
        )

    metadata = {
        "release_name": "mSCIdblit Module 20B-24B mechanism graph",
        "release_id": f"module20_24_mechanism_graph:{date.today().isoformat()}",
        "release_status": "conservative_register_backed_snapshot",
        "source_repo": "mSCIdblit",
        "source_scope": "validated Module 20B-24B edge and evidence registers",
        "generated_at": date.today().isoformat(),
        "canonical_database_materialization": False,
        "input_registers": input_registers,
        "graph_policy": {
            "exportable_edges_only": True,
            "composite_labels_preserved": True,
            "unresolved_and_nonexportable_edges_excluded_from_graph": True,
            "evidence_rows_retained_for_exported_edges": True,
        },
        "counts": {
            "nodes": len(node_rows),
            "edges": len(edge_rows),
            "edge_sources": len(source_rows),
            "pathways": len(pathway_rows),
            "boundary_groups": len(boundary_rows),
            "nonexportable_edges": sum(row["nonexportable_edge_count"] for row in boundary_rows),
        },
        "source_locator_status_counts": dict(
            Counter(row["source_locator_status"] for row in source_rows)
        ),
        "module_counts": module_stats,
        "files": {
            "nodes": "mechanism_nodes.tsv",
            "edges": "mechanism_edges.tsv",
            "edge_sources": "mechanism_edge_sources.tsv",
            "pathways": "mechanism_pathways.tsv",
            "boundaries": "mechanism_boundary_summary.tsv",
            "validation": "validation_report.json",
        },
        "accuracy_contract": [
            "Every exported edge must reference existing source and target nodes.",
            "Every exported edge must retain at least one evidence-register source row.",
            "Every exported edge must belong to a pathway row.",
            "Non-exportable edges remain summarized as boundaries and are not traversable graph edges.",
            "Stable PMID/PMCID/DOI/URL locators are retained in edge-source rows where available; local paths are not released.",
        ],
    }

    return {
        "metadata": metadata,
        "nodes": node_rows,
        "edges": edge_rows,
        "sources": source_rows,
        "pathways": pathway_rows,
        "boundaries": boundary_rows,
    }


def main() -> None:
    args = parse_args()
    release = build_release(args.source_root.resolve())
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    write_tsv(
        output_dir / "mechanism_nodes.tsv",
        ["node_id", "canonical_label", "label_variants", "modules", "pathways", "exportable_edge_count"],
        release["nodes"],
    )
    write_tsv(
        output_dir / "mechanism_edges.tsv",
        [
            "edge_id", "module", "source_node_id", "target_node_id", "source_label",
            "relation_type", "target_label", "pathway_name", "evidence_layer", "edge_status",
            "context_scope", "cell_type_context", "compartment_context", "species_context",
            "injury_context", "confidence_tier", "export_priority", "evidence_ids",
            "evidence_count", "source_locator_count", "exportable", "consolidation_note",
        ],
        release["edges"],
    )
    write_tsv(
        output_dir / "mechanism_edge_sources.tsv",
        [
            "source_id", "edge_id", "module", "evidence_id", "source_kind", "source_locator",
            "source_locator_status", "support_kind", "species_support", "source_scope", "confidence_tier", "citation_note",
            "evidence_summary", "limitations", "evidence_layer", "evidence_exportable",
            "consolidation_note",
        ],
        release["sources"],
    )
    write_tsv(
        output_dir / "mechanism_pathways.tsv",
        ["module", "pathway_name", "edge_count", "node_count", "evidence_count"],
        release["pathways"],
    )
    write_tsv(
        output_dir / "mechanism_boundary_summary.tsv",
        [
            "module", "pathway_name", "evidence_layer", "edge_status", "export_priority",
            "nonexportable_edge_count",
        ],
        release["boundaries"],
    )
    (output_dir / "bundle_metadata.json").write_text(json.dumps(release["metadata"], indent=2) + "\n")
    print(json.dumps(release["metadata"]["counts"], sort_keys=True))


if __name__ == "__main__":
    main()
