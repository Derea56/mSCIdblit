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
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULES = ("20", "21", "22", "23", "24")
ROLE_NAMES = ("ligand", "receptor", "transcription_factor", "target_gene", "signaling_cascade")
PRIMARY_ROLE_ORDER = ("ligand", "receptor", "transcription_factor", "target_gene")

# These are deliberately narrow role hints for labels whose role is explicit
# in the Module 20B–24B evidence handoff. Composite labels remain composite;
# the role table records them as a TF or receptor complex without splitting
# them into unsupported entities.
CURATED_ROLE_HINTS = {
    "smad2": ("transcription_factor", "Module 21B TGF-beta-SMAD receptor-proximal relay and nuclear transcriptional relay."),
    "smad3": ("transcription_factor", "Module 21B TGF-beta-SMAD receptor-proximal relay and nuclear transcriptional relay."),
    "smad4": ("transcription_factor", "Module 21B TGF-beta-SMAD SMAD2/3-SMAD4 complex and nuclear relay."),
    "smad2-smad3": ("transcription_factor", "Module 21B TGF-beta-SMAD SMAD2/3 complex."),
    "smad2/3": ("transcription_factor", "Module 22B SMAD2/3 transcriptional signaling program."),
    "smad2/3;smad4": ("transcription_factor", "Module 22B SMAD2/3-SMAD4 transcriptional signaling program."),
    "smad2;smad3": ("transcription_factor", "Module 22B SMAD2/3 transcriptional signaling program."),
    "smad3;smad4": ("transcription_factor", "Module 22B SMAD3-SMAD4 transcriptional signaling program."),
    "smad1/5/8": ("transcription_factor", "Module 22B SMAD1/5/8 transcriptional signaling program."),
    "smad1/5/8;smad4": ("transcription_factor", "Module 22B SMAD1/5/8-SMAD4 transcriptional signaling program."),
    "smad1/5;smad4": ("transcription_factor", "Module 22B SMAD1/5-SMAD4 transcriptional signaling program."),
    "smad1;smad4": ("transcription_factor", "Module 22B SMAD1-SMAD4 transcriptional signaling program."),
    "tgfbr1-tgfbr2 receptor complex": ("receptor", "Module 21B TGF-beta-SMAD receptor-proximal relay."),
}


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


def is_self_loop(edge: dict[str, str]) -> bool:
    return node_key(edge.get("source_entity", "")) == node_key(edge.get("target_entity", ""))


def add_role(
    role_map: dict[str, dict[str, dict[str, set[str]]]],
    node_id: str,
    role: str,
    role_source: str,
    role_evidence: str,
) -> None:
    if role not in ROLE_NAMES:
        raise ValueError(f"Unsupported mechanism node role: {role}")
    entry = role_map.setdefault(node_id, {}).setdefault(
        role,
        {"sources": set(), "evidence": set()},
    )
    entry["sources"].add(role_source)
    entry["evidence"].add(role_evidence)


def primary_node_type(roles: set[str]) -> str:
    for role in PRIMARY_ROLE_ORDER:
        if role in roles:
            return role
    # mSCS uses node_type for legacy feature typing. Keep the many-to-many
    # signaling_cascade role in mechanism_node_roles.tsv, but use the
    # recognized legacy fallback for generic relay/complex/program nodes.
    return "signaling_effector"


def safe_gene_symbol(label: str, roles: set[str]) -> str:
    """Keep only simple role-bearing labels as gene symbols.

    Composite labels, pathway names, and phenotype/program labels remain
    addressable through canonical_name but are not silently converted into a
    gene symbol.
    """
    if not roles.intersection({"ligand", "receptor", "transcription_factor", "target_gene"}):
        return ""
    normalized = label.strip()
    if re.fullmatch(r"[A-Za-z][A-Za-z0-9-]{1,31}", normalized):
        return normalized
    return ""


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


def effect_polarity(value: str) -> str:
    """Normalize register prose without inventing a sign for mixed relations."""
    lowered = value.casefold()
    negative = any(token in lowered for token in ("inhibit", "suppress", "repress", "decrease", "negative"))
    positive = any(token in lowered for token in ("activat", "promot", "induc", "increase", "positive"))
    if negative and positive:
        return "unknown"
    if negative:
        return "inhibitory"
    if positive:
        return "activating"
    return "unknown"


def canonical_relation_type(edge: dict[str, str], target_gene_edge: bool) -> str:
    """Emit the exact relation names used by mSCS while preserving the register relation."""
    relation = edge["relation_type"].casefold()
    layer = edge["evidence_layer"].casefold()
    if layer == "ligand_receptor_or_direct_molecular" and edge["module"] != "22B" and not target_gene_edge:
        return "binds_receptor"
    if target_gene_edge:
        if any(token in relation for token in ("repress", "inhibit", "suppress", "decrease")):
            return "represses_target_gene"
        if any(token in relation for token in ("induc", "activat", "promot", "increase")):
            return "induces_target_gene"
        return "regulates_target_gene"
    return edge["relation_type"]


def normalize_species_support(value: str) -> str:
    lowered = value.casefold()
    has_mouse = "mouse" in lowered or "murine" in lowered
    has_human = "human" in lowered
    if has_mouse and has_human:
        return "both"
    if has_mouse:
        return "mouse"
    if has_human:
        return "human"
    if lowered.strip():
        return "mixed"
    return "not_applicable"


def normalize_confidence(value: str) -> str:
    lowered = value.casefold().strip()
    if lowered.startswith("high"):
        return "high"
    if lowered.startswith("medium"):
        return "medium"
    if lowered.startswith("low"):
        return "low"
    return "uncertain"


def normalize_export_priority(value: str) -> str:
    lowered = value.casefold().strip()
    return {
        "p1": "high",
        "p2": "medium",
        "p3": "low",
        "high": "high",
        "medium": "medium",
        "low": "low",
        "exclude": "exclude",
        "": "",
    }.get(lowered, "")


def normalize_support_kind(source_kind: str, support_kind: str) -> str:
    value = f"{source_kind} {support_kind}".casefold()
    if "primary" in value or "validated" in value:
        return "primary_experiment"
    if "review" in value:
        return "review_statement"
    if "database" in value or "frozen_" in value:
        return "database_curated"
    if "consensus" in value:
        return "consensus_summary"
    return "manual_background"


def normalize_source_scope(source_scope: str, source_kind: str, support_kind: str) -> str:
    scope = source_scope.casefold().strip()
    kind = source_kind.casefold().strip()
    support = support_kind.casefold().strip()
    boundary_kind = (
        kind.startswith("search")
        or kind.endswith("_boundary")
        or kind in {"no_evidence_boundary", "unresolved"}
    )
    boundary_scope = (
        scope.startswith("search")
        or "_search" in scope
        or any(token in scope for token in ("negative", "boundary", "unresolved", "no_evidence"))
    )
    if (
        boundary_kind
        or boundary_scope
        or support in {"negative_evidence", "no_exact_primary_packet"}
        or "no exact" in support
    ):
        return "negative_evidence"
    if "direct" in scope:
        return "direct_edge"
    if "pathway" in scope:
        return "pathway_membership"
    return "contextual_support"


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
            if row.get("exportable") == "true" and not is_self_loop(row):
                exportable_edges.append(row)
        for row in evidence:
            row = dict(row)
            row["module"] = f"{module}B"
            evidence_rows.append(row)
        module_stats.append(
            {
                "module": f"{module}B",
                "edge_count": len(edges),
                "exportable_edge_count": sum(
                    row.get("exportable") == "true" and not is_self_loop(row) for row in edges
                ),
                "evidence_count": len(evidence),
                "pathway_count": len({row.get("pathway_name", "") for row in edges}),
                "nonexportable_edge_count": sum(
                    row.get("exportable") != "true" or is_self_loop(row) for row in edges
                ),
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
    role_map: dict[str, dict[str, dict[str, set[str]]]] = {}
    for key, node_id in node_id_by_key.items():
        add_role(
            role_map,
            node_id,
            "signaling_cascade",
            "module20_24_export",
            "Node participates in at least one evidence-gated exported mechanism edge.",
        )
        if key in CURATED_ROLE_HINTS:
            hint_role, hint = CURATED_ROLE_HINTS[key]
            add_role(role_map, node_id, hint_role, "curated_role_hint", hint)

    node_rows: list[dict[str, object]] = []
    for key in sorted(node_records):
        record = node_records[key]
        label_variants = "; ".join(sorted(record["labels"]))
        modules = ";".join(sorted(record["modules"]))
        pathways = ";".join(sorted(filter(None, record["pathways"])))
        node_id = node_id_by_key[key]
        roles = set(role_map[node_id])
        node_rows.append(
            {
                "node_id": node_id,
                # Required mSCS contract fields. The source registers contain
                # curated labels, not a safe gene-symbol/entity-type mapping.
                "canonical_name": record["label"],
                "node_type": primary_node_type(roles),
                "node_subtype": "",
                "gene_symbol": safe_gene_symbol(record["label"], roles),
                "organism_scope": "",
                "compartment": "",
                "notes": (
                    f"modules={modules}; pathways={pathways}; "
                    f"label_variants={label_variants}; "
                    f"exportable_edge_count={len(record['edge_ids'])}"
                ),
                # Extra audit fields retained for the mSCIdblit release.
                "canonical_label": record["label"],
                "label_variants": label_variants,
                "modules": modules,
                "pathways": pathways,
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
        role_evidence = f"edge={edge_id}; evidence={';'.join(evidence_ids) or 'none'}"
        pathway_lower = pathway.casefold()
        layer_lower = edge["evidence_layer"].casefold()
        target_gene_edge = "target_gene" in pathway_lower or layer_lower == "target_gene"
        if target_gene_edge:
            add_role(
                role_map,
                node_id_by_key[source_key],
                "transcription_factor",
                "register_target_gene_layer",
                role_evidence,
            )
            add_role(
                role_map,
                node_id_by_key[target_key],
                "target_gene",
                "register_target_gene_layer",
                role_evidence,
            )
        elif layer_lower == "ligand_receptor_or_direct_molecular" and edge["module"] != "22B":
            # Modules 20B, 21B, 23B, and 24B use this layer for their
            # receptor-facing molecular handoffs. Module 22B also uses the
            # layer for TF-target rows, so those are handled above instead of
            # being mislabeled as ligand/receptor pairs.
            add_role(
                role_map,
                node_id_by_key[source_key],
                "ligand",
                "register_ligand_receptor_layer",
                role_evidence,
            )
            add_role(
                role_map,
                node_id_by_key[target_key],
                "receptor",
                "register_ligand_receptor_layer",
                role_evidence,
            )
        edge_rows.append(
            {
                "edge_id": edge_id,
                "module": edge["module"],
                "source_node_id": node_id_by_key[source_key],
                "target_node_id": node_id_by_key[target_key],
                "pathway_label": pathway,
                "effect_polarity": effect_polarity(edge["relation_type"]),
                "evidence_status": edge["edge_status"],
                "notes": edge["consolidation_note"],
                "source_label": edge["source_entity"],
                "relation_type": canonical_relation_type(edge, target_gene_edge),
                "register_relation_type": edge["relation_type"],
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
                "export_priority": normalize_export_priority(edge["export_priority"]),
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
                    "edge_source_id": f"SRC{len(source_rows) + 1:06d}",
                    "edge_id": edge_id,
                    # The register evidence ID is an explicit external
                    # observation token, not a fabricated database integer.
                    "paper_id": "",
                    "observation_id": f"REGISTER:{evidence['b_evidence_id']}",
                    "claim_id": "",
                    "support_kind": normalize_support_kind(
                        evidence["source_kind"], evidence["support_kind"]
                    ),
                    "species_support": normalize_species_support(evidence["species_support"]),
                    "source_scope": normalize_source_scope(
                        evidence["source_scope"], evidence["source_kind"], evidence["support_kind"]
                    ),
                    "confidence_tier": normalize_confidence(evidence["confidence_tier"]),
                    "citation_note": evidence["citation_note"],
                    "notes": (
                        f"register_evidence_id={evidence['b_evidence_id']}; "
                        f"original_source_kind={evidence['source_kind']}; "
                        f"original_support_kind={evidence['support_kind']}; "
                        f"source_locator_status={locator_status}"
                    ),
                    "module": edge["module"],
                    "evidence_id": evidence["b_evidence_id"],
                    "source_kind": evidence["source_kind"],
                    "source_locator": locator,
                    "source_locator_status": locator_status,
                    "evidence_summary": evidence["evidence_summary"],
                    "limitations": evidence["limitations"],
                    "evidence_layer": evidence["evidence_layer"],
                    "evidence_exportable": evidence["exportable"],
                    "consolidation_note": evidence["consolidation_note"],
                }
            )

    role_rows: list[dict[str, object]] = []
    node_rows_by_id = {str(row["node_id"]): row for row in node_rows}
    for node_id in sorted(role_map):
        roles = set(role_map[node_id])
        node_row = node_rows_by_id[node_id]
        node_row["node_type"] = primary_node_type(roles)
        node_row["gene_symbol"] = safe_gene_symbol(str(node_row["canonical_name"]), roles)
        for role in sorted(roles):
            assignment = role_map[node_id][role]
            role_rows.append(
                {
                    "node_id": node_id,
                    "role": role,
                    "role_source": ";".join(sorted(assignment["sources"])),
                    "role_evidence": " || ".join(sorted(assignment["evidence"])),
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
        if edge.get("exportable") == "true" and not is_self_loop(edge):
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
        "bundle_name": "module20_24_mechanism_graph",
        "release_id": f"module20_24_mechanism_graph:{date.today().isoformat()}",
        "release_status": "conservative_register_backed_snapshot",
        "source_repo": "mSCIdblit",
        "target_repo": "mSCS",
        "source_scope": "validated Module 20B-24B edge and evidence registers",
        "generated_at": date.today().isoformat(),
        "canonical_database_materialization": False,
        "authoritative_pathway_snapshot": True,
        "replacement_policy": (
            "Importing this bundle replaces the selected active mechanism release in mSCS; "
            "it does not alter atlas-derived tables."
        ),
        "input_registers": input_registers,
        "graph_policy": {
            "exportable_edges_only": True,
            "composite_labels_preserved": True,
            "unresolved_and_nonexportable_edges_excluded_from_graph": True,
            "evidence_rows_retained_for_exported_edges": True,
            "self_loops_excluded_from_traversable_graph": True,
        },
        "counts": {
            "nodes": len(node_rows),
            "edges": len(edge_rows),
            "edge_sources": len(source_rows),
            "node_roles": len(role_rows),
            "nodes_with_ligand_role": sum("ligand" in role_map[node_id] for node_id in role_map),
            "nodes_with_receptor_role": sum("receptor" in role_map[node_id] for node_id in role_map),
            "nodes_with_transcription_factor_role": sum(
                "transcription_factor" in role_map[node_id] for node_id in role_map
            ),
            "nodes_with_target_gene_role": sum("target_gene" in role_map[node_id] for node_id in role_map),
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
            "node_roles": "mechanism_node_roles.tsv",
            "edges": "mechanism_edges.tsv",
            "edge_sources": "mechanism_edge_sources.tsv",
            "pathways": "mechanism_pathways.tsv",
            "boundaries": "mechanism_boundary_summary.tsv",
            "validation": "validation_report.json",
        },
        "accuracy_contract": [
            "Every exported edge must reference existing source and target nodes.",
            "Every exported node must have a signaling_cascade role; specialized roles are only added from explicit register layers or curated role hints.",
            "Every exported edge must retain at least one evidence-register source row.",
            "Every exported edge must belong to a pathway row.",
            "Role-aware edges use canonical binds_receptor or target-gene relation types with matching endpoint roles; original register relations remain audit fields.",
            "Self-loop register rows are retained as boundaries and are not inserted into the normalized graph.",
            "Non-exportable edges remain summarized as boundaries and are not traversable graph edges.",
            "Stable PMID/PMCID/DOI/URL locators are retained in edge-source rows where available; local paths are not released.",
        ],
    }

    return {
        "metadata": metadata,
        "nodes": node_rows,
        "node_roles": role_rows,
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
        [
            "node_id", "canonical_name", "node_type", "node_subtype", "gene_symbol",
            "organism_scope", "compartment", "notes", "canonical_label", "label_variants",
            "modules", "pathways", "exportable_edge_count",
        ],
        release["nodes"],
    )
    write_tsv(
        output_dir / "mechanism_node_roles.tsv",
        ["node_id", "role", "role_source", "role_evidence"],
        release["node_roles"],
    )
    write_tsv(
        output_dir / "mechanism_edges.tsv",
        [
            "edge_id", "source_node_id", "target_node_id", "pathway_label", "relation_type",
            "effect_polarity", "species_context", "cell_type_context", "compartment_context",
            "injury_context", "evidence_status", "context_scope", "export_priority", "notes",
            "module", "source_label", "target_label", "register_relation_type", "pathway_name", "evidence_layer", "edge_status",
            "confidence_tier", "evidence_ids",
            "evidence_count", "source_locator_count", "exportable", "consolidation_note",
        ],
        release["edges"],
    )
    write_tsv(
        output_dir / "mechanism_edge_sources.tsv",
        [
            "edge_source_id", "edge_id", "paper_id", "observation_id", "claim_id", "support_kind",
            "species_support", "source_scope", "confidence_tier", "citation_note", "notes",
            "module", "evidence_id", "source_kind", "source_locator", "source_locator_status",
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
