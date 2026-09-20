#!/usr/bin/env python3
"""Compare the current mSCIdblit evidence release with frozen public LR resources.

The comparison is intentionally an inventory audit, not a biological truth
score. It reports both conservative label-level overlap and component-aware
overlap for ligand/receptor complexes. Public-only rows are emitted as review
candidates and are never promoted to mSCIdblit graph edges.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable


DEFAULT_BUNDLE = Path(
    "data/processed/"
    "mechanism_graph_module20_24_v2026_09_19_literature_expansion242"
)
DEFAULT_SNAPSHOT = Path("data/raw/method_resources/mscs_phase2_external_snapshot_2026-08-05")

PAIR_SEPARATORS = re.compile(r"[|_:;,/+\s]+")
NON_ALNUM = re.compile(r"[^A-Z0-9]")
NON_ENTITY_WORDS = {"COMPLEX", "RECEPTOR", "PROTEIN", "FAMILY", "CHAIN"}
PRIMARY_LOCATOR = re.compile(r"\b(?:PMID|PMCID)\s*:\s*[A-Z0-9]+|\bdoi\s*:\s*10\.\d{4,9}/\S+", re.IGNORECASE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument("--snapshot-dir", type=Path, default=DEFAULT_SNAPSHOT)
    parser.add_argument(
        "--output-dir", type=Path, default=Path("data/processed/public_database_comparison_v2")
    )
    return parser.parse_args()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_token(value: str) -> str:
    return NON_ALNUM.sub("", value.strip().upper())


def components(value: str) -> tuple[str, ...]:
    """Return conservative component tokens from a gene/protein/complex label."""

    tokens: list[str] = []
    for raw in PAIR_SEPARATORS.split(value or ""):
        token = normalize_token(raw)
        if token and token not in NON_ENTITY_WORDS and len(token) > 1:
            tokens.append(token)
    return tuple(sorted(set(tokens)))


def label_key(ligand: str, receptor: str) -> tuple[str, str] | None:
    ligand_key = normalize_token(ligand)
    receptor_key = normalize_token(receptor)
    if not ligand_key or not receptor_key:
        return None
    return ligand_key, receptor_key


def component_key(
    ligand: str,
    receptor: str,
    *,
    ligand_components: str = "",
    receptor_components: str = "",
) -> tuple[tuple[str, ...], tuple[str, ...]] | None:
    ligand_parts = components(ligand_components) or components(ligand)
    receptor_parts = components(receptor_components) or components(receptor)
    if not ligand_parts or not receptor_parts:
        return None
    return ligand_parts, receptor_parts


def metrics(ours: set, public: set) -> dict[str, int | float]:
    overlap = ours & public
    union = ours | public
    return {
        "mSCIdblit": len(ours),
        "public": len(public),
        "overlap": len(overlap),
        "mSCIdblit_only": len(ours - public),
        "public_only": len(public - ours),
        "jaccard": round(len(overlap) / len(union), 6) if union else 0.0,
        "mSCIdblit_coverage_of_public": round(len(overlap) / len(public), 6)
        if public
        else 0.0,
        "public_coverage_of_mSCIdblit": round(len(overlap) / len(ours), 6)
        if ours
        else 0.0,
    }


def pair_sets_from_mscidblit(rows: Iterable[dict[str, str]]) -> tuple[set, set, dict]:
    label_pairs: set[tuple[str, str]] = set()
    component_pairs: set[tuple[tuple[str, ...], tuple[str, ...]]] = set()
    records: dict[tuple[tuple[str, ...], tuple[str, ...]], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        if row.get("relation_type") != "binds_receptor":
            continue
        ligand = row.get("source_label", "")
        receptor = row.get("target_label", "")
        label = label_key(ligand, receptor)
        component = component_key(ligand, receptor)
        if label:
            label_pairs.add(label)
        if component:
            component_pairs.add(component)
            records[component].append(
                {
                    "edge_id": row.get("edge_id", ""),
                    "ligand": ligand,
                    "receptor": receptor,
                    "pathway": row.get("pathway_name", ""),
                    "evidence_ids": row.get("evidence_ids", ""),
                }
            )
    return label_pairs, component_pairs, records


def pair_sets_from_public(
    rows: Iterable[dict[str, str]],
    *,
    ligand_field: str,
    receptor_field: str,
    ligand_components_field: str = "",
    receptor_components_field: str = "",
) -> tuple[set, set, dict]:
    label_pairs: set[tuple[str, str]] = set()
    component_pairs: set[tuple[tuple[str, ...], tuple[str, ...]]] = set()
    records: dict[tuple[tuple[str, ...], tuple[str, ...]], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        ligand = row.get(ligand_field, "")
        receptor = row.get(receptor_field, "")
        label = label_key(ligand, receptor)
        component = component_key(
            ligand,
            receptor,
            ligand_components=row.get(ligand_components_field, "") if ligand_components_field else "",
            receptor_components=row.get(receptor_components_field, "") if receptor_components_field else "",
        )
        if label:
            label_pairs.add(label)
        if component:
            component_pairs.add(component)
            records[component].append(dict(row))
    return label_pairs, component_pairs, records


def format_pair(pair: tuple[tuple[str, ...], tuple[str, ...]]) -> tuple[str, str]:
    ligand, receptor = pair
    return "+".join(ligand), "+".join(receptor)


def load_sources(snapshot: Path) -> dict[str, dict]:
    sources = {
        "CellChatDB.mouse": {
            "path": snapshot / "cellchat_mouse.tsv",
            "rows": read_tsv(snapshot / "cellchat_mouse.tsv"),
            "ligand_field": "ligand",
            "receptor_field": "receptor",
            "ligand_components_field": "ligand_components",
            "receptor_components_field": "receptor_components",
        },
        "NicheNet.neutral_v1": {
            "path": snapshot / "nichenet_neutral_v1" / "lr_network.tsv",
            "rows": read_tsv(snapshot / "nichenet_neutral_v1" / "lr_network.tsv"),
            "ligand_field": "from",
            "receptor_field": "to",
        },
        "LIANA.mouseconsensus": {
            "path": snapshot / "liana_mouseconsensus.tsv",
            "rows": read_tsv(snapshot / "liana_mouseconsensus.tsv"),
            "ligand_field": "ligand",
            "receptor_field": "receptor",
        },
        "master_LR_union": {
            "path": snapshot / "master_lr_registry.tsv",
            "rows": read_tsv(snapshot / "master_lr_registry.tsv"),
            "ligand_field": "ligand",
            "receptor_field": "receptor",
            "ligand_components_field": "ligand_components",
            "receptor_components_field": "receptor_components",
        },
    }
    return sources


def nonempty_count(rows: Iterable[dict[str, str]], field: str) -> int:
    return sum(bool(row.get(field, "").strip()) for row in rows)


def evidence_gate(row: dict[str, str]) -> str:
    text = " ".join(
        row.get(field, "")
        for field in ("evidence", "annotation", "citation_note", "source_record_id")
    )
    if PRIMARY_LOCATOR.search(text):
        return "primary_locator_present_unverified"
    return "no_primary_locator_in_public_snapshot"


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    edge_path = args.bundle_dir / "mechanism_edges.tsv"
    route_path = args.bundle_dir / "mechanism_signaling_route_evidence.tsv"
    metadata_path = args.bundle_dir / "bundle_metadata.json"
    edges = read_tsv(edge_path)
    routes = read_tsv(route_path)
    bundle_metadata = json.loads(metadata_path.read_text(encoding="utf-8"))

    our_label_pairs, our_component_pairs, our_records = pair_sets_from_mscidblit(edges)
    route_tiers = Counter(row.get("route_tier", "") for row in routes)
    output_classes = Counter(
        row.get("output_class", "") or "unknown"
        for row in routes
        if "literature_expansion" in row.get("route_linkage_status", "")
    )
    queue_ids = {row.get("source_queue_id", "") for row in routes if row.get("source_queue_id")}
    literature_queue_ids = {
        row.get("source_queue_id", "")
        for row in routes
        if row.get("source_queue_id") and "literature_expansion" in row.get("route_linkage_status", "")
    }
    route_detail = {
        "distinct_ligands": len({row.get("ligand_label", "") for row in routes if row.get("ligand_label")}),
        "distinct_receptors": len({row.get("receptor_label", "") for row in routes if row.get("receptor_label")}),
        "distinct_intracellular_continuations": len(
            {
                row.get("intracellular_continuation_label", "")
                for row in routes
                if row.get("intracellular_continuation_label")
            }
        ),
        "distinct_transcription_factors": len(
            {
                row.get("transcription_factor_label", "")
                for row in routes
                if row.get("transcription_factor_label")
            }
        ),
        "distinct_target_genes": len(
            {row.get("target_gene_label", "") for row in routes if row.get("target_gene_label")}
        ),
        "distinct_outputs": len({row.get("output_label", "") for row in routes if row.get("output_label")}),
        "contextualized_records": sum(
            bool(
                row.get("species_context", "")
                or row.get("cell_type_context", "")
                or row.get("compartment_context", "")
            )
            for row in routes
        ),
    }

    public_sources = load_sources(args.snapshot_dir)
    comparison: dict[str, dict] = {}
    public_only_rows: list[dict[str, str]] = []
    for name, source in public_sources.items():
        public_label_pairs, public_component_pairs, public_records = pair_sets_from_public(
            source["rows"],
            ligand_field=source["ligand_field"],
            receptor_field=source["receptor_field"],
            ligand_components_field=source.get("ligand_components_field", ""),
            receptor_components_field=source.get("receptor_components_field", ""),
        )
        component_only = public_component_pairs - our_component_pairs
        comparison[name] = {
            "path": str(source["path"]),
            "sha256": sha256(source["path"]),
            "raw_rows": len(source["rows"]),
            "label_pairs": len(public_label_pairs),
            "component_pairs": len(public_component_pairs),
            "label_overlap": metrics(our_label_pairs, public_label_pairs),
            "component_overlap": metrics(our_component_pairs, public_component_pairs),
            "public_only_component_pairs": len(component_only),
            "schema": {
                "fields": list(source["rows"][0].keys()) if source["rows"] else [],
                "nonempty_fields": {
                    field: nonempty_count(source["rows"], field)
                    for field in (
                        "ligand_components",
                        "receptor_components",
                        "annotation",
                        "evidence",
                        "cofactor_annotations",
                        "database",
                        "source",
                    )
                    if source["rows"] and field in source["rows"][0]
                },
            },
        }
        for pair in sorted(component_only):
            ligand, receptor = format_pair(pair)
            for record in public_records.get(pair, [{}]):
                public_only_rows.append(
                    {
                        "source_database": name,
                        "ligand_components": ligand,
                        "receptor_components": receptor,
                        "source_ligand": record.get(source["ligand_field"], ""),
                        "source_receptor": record.get(source["receptor_field"], ""),
                        "source_record_id": record.get("source_record_id", ""),
                        "pathway": record.get("pathway_name", "") or record.get("pathway", ""),
                        "annotation": record.get("annotation", ""),
                        "evidence": record.get("evidence", ""),
                        "primary_evidence_gate": evidence_gate(record),
                        "review_status": "candidate_public_only_not_graph_edge",
                        "reason": "no_component_normalized_match_in_mSCIdblit",
                    }
                )

    unique_public_candidates: dict[tuple[str, str], dict[str, str]] = {}
    for row in public_only_rows:
        key = (row["ligand_components"], row["receptor_components"])
        current = unique_public_candidates.setdefault(
            key,
            {
                **row,
                "source_databases": row["source_database"],
                "source_record_ids": row["source_record_id"],
                "pathways": row["pathway"],
                "annotations": row["annotation"],
                "evidence_notes": row["evidence"],
            },
        )
        if current is not row:
            for field, output_field in (
                ("source_database", "source_databases"),
                ("source_record_id", "source_record_ids"),
                ("pathway", "pathways"),
                ("annotation", "annotations"),
                ("evidence", "evidence_notes"),
            ):
                values = [value for value in (current.get(output_field, "").split(";") + [row.get(field, "")]) if value]
                current[output_field] = ";".join(sorted(set(values)))
            if row.get("primary_evidence_gate") == "primary_locator_present_unverified":
                current["primary_evidence_gate"] = "primary_locator_present_unverified"
    gate_counts = Counter(row["primary_evidence_gate"] for row in unique_public_candidates.values())
    primary_review_rows = [
        {**row, "review_status": "requires_primary_paper_verification"}
        for row in unique_public_candidates.values()
        if row["primary_evidence_gate"] == "primary_locator_present_unverified"
    ]
    manifest = {
        "comparison_id": "mSCIdblit:literature-expansion242:public-databases-v2",
        "bundle_dir": str(args.bundle_dir),
        "bundle_release_id": bundle_metadata.get("release_id"),
        "snapshot_dir": str(args.snapshot_dir),
        "snapshot_manifest": str(args.snapshot_dir / "resource_manifest.json"),
        "inputs": {
            "edges": {"path": str(edge_path), "sha256": sha256(edge_path), "rows": len(edges)},
            "route_evidence": {"path": str(route_path), "sha256": sha256(route_path), "rows": len(routes)},
        },
        "sources": comparison,
        "route_evidence": {
            "rows": len(routes),
            "route_tiers": dict(sorted(route_tiers.items())),
            "literature_expansion_output_classes": dict(sorted(output_classes.items())),
            "unique_queue_ids_with_route_evidence": len(queue_ids),
            "unique_queue_ids_with_literature_expansion": len(literature_queue_ids),
            "detail": route_detail,
        },
        "mSCIdblit": {
            "lr_edge_rows": sum(row.get("relation_type") == "binds_receptor" for row in edges),
            "unique_label_pairs": len(our_label_pairs),
            "unique_component_pairs": len(our_component_pairs),
            "bundle_counts": bundle_metadata.get("counts", {}),
        },
        "candidate_queue": {
            "rows": len(unique_public_candidates),
            "primary_evidence_gate_counts": dict(sorted(gate_counts.items())),
            "primary_evidence_review_queue_rows": len(primary_review_rows),
            "policy": "public-only candidates remain review evidence and are not causal graph edges",
        },
    }
    (args.output_dir / "comparison_summary.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    candidate_fields = [
        "source_databases",
        "ligand_components",
        "receptor_components",
        "source_ligand",
        "source_receptor",
        "source_record_ids",
        "pathways",
        "annotations",
        "evidence_notes",
        "primary_evidence_gate",
        "review_status",
        "reason",
    ]
    with (args.output_dir / "public_only_lr_candidates.tsv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=candidate_fields,
            delimiter="\t",
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(sorted(unique_public_candidates.values(), key=lambda row: (row["ligand_components"], row["receptor_components"])))
    with (args.output_dir / "primary_evidence_review_queue.tsv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=candidate_fields,
            delimiter="\t",
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(sorted(primary_review_rows, key=lambda row: (row["ligand_components"], row["receptor_components"])))

    def pct(value: float) -> str:
        return f"{value * 100:.1f}%"

    report = [
        "# mSCIdblit public signaling-database comparison v2",
        "",
        f"This report compares `{manifest['bundle_release_id']}` with the frozen public-resource snapshot `{args.snapshot_dir.name}`. It is an inventory audit, not a biological completeness score. Complexes are compared first as component sets; public-only rows remain candidates and are not added as graph edges.",
        "",
        "## Executive summary",
        "",
        f"- mSCIdblit contains {manifest['mSCIdblit']['lr_edge_rows']:,} ligand–receptor edge rows, {manifest['mSCIdblit']['unique_label_pairs']:,} unique label pairs, and {manifest['mSCIdblit']['unique_component_pairs']:,} component-normalized pairs.",
        f"- The route-evidence layer contains {len(routes):,} records and covers {len(literature_queue_ids):,} of {len(queue_ids):,} queue IDs with literature-linked evidence.",
        f"- The comparison emits {len(unique_public_candidates):,} unique public-only LR candidates for review; these are not causal graph additions.",
        f"- Primary-evidence gate: {gate_counts.get('primary_locator_present_unverified', 0):,} candidates have a locator-like public note requiring verification, and {gate_counts.get('no_primary_locator_in_public_snapshot', 0):,} have no primary locator in the frozen public snapshot. None is automatically verified.",
        "- Exact label overlap is intentionally conservative. Component-normalized overlap is the preferred ligand–receptor comparison, especially for heteromeric receptors.",
        "",
        "## Ligand–receptor comparison",
        "",
        "| Source | Raw rows | mSCIdblit pairs | Public pairs | Component overlap | mSCIdblit coverage of public | Public coverage of mSCIdblit | Public-only component pairs |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for name, data in comparison.items():
        metric = data["component_overlap"]
        report.append(
            f"| {name} | {data['raw_rows']:,} | {metric['mSCIdblit']:,} | {metric['public']:,} | {metric['overlap']:,} | {pct(metric['mSCIdblit_coverage_of_public'])} | {pct(metric['public_coverage_of_mSCIdblit'])} | {data['public_only_component_pairs']:,} |"
        )
    report.extend(
        [
            "",
            "## Representational depth",
            "",
            "| Resource/layer | LR pairs/rows | Intracellular continuation | TF layer | Target/output layer | Context/evidence fields |",
            "|---|---:|---:|---:|---:|---|",
            f"| mSCIdblit route evidence | {len(routes):,} | {route_detail['distinct_intracellular_continuations']:,} distinct intermediates | {route_detail['distinct_transcription_factors']:,} distinct TFs | {route_detail['distinct_target_genes']:,} target genes; {route_detail['distinct_outputs']:,} outputs | {route_detail['contextualized_records']:,} contextualized records |",
            f"| CellChatDB.mouse | {comparison['CellChatDB.mouse']['component_pairs']:,} | not represented as route layer | not represented as route layer | not represented as route layer | cofactors: {comparison['CellChatDB.mouse']['schema']['nonempty_fields'].get('cofactor_annotations', 0):,}; evidence: {comparison['CellChatDB.mouse']['schema']['nonempty_fields'].get('evidence', 0):,} rows |",
            f"| NicheNet.neutral_v1 | {comparison['NicheNet.neutral_v1']['component_pairs']:,} | target-prior network, not explicit relay chain | not explicit in LR table | target-gene matrix available in snapshot | source/database fields in LR table |",
            f"| LIANA.mouseconsensus | {comparison['LIANA.mouseconsensus']['component_pairs']:,} | not represented | not represented | not represented | pair inventory fields only |",
            "",
            "This is the key distinction: mSCIdblit carries an evidence-bearing route layer beyond the public LR inventories. NicheNet contributes downstream ligand–target priors, while Reactome, OmniPath, and TF resources are needed for the next intracellular and TF edge comparison.",
            "",
            "## mSCIdblit route detail",
            "",
            "| Route tier | Records |",
            "|---|---:|",
        ]
    )
    for tier, count in sorted(route_tiers.items(), key=lambda item: (-item[1], item[0])):
        report.append(f"| `{tier}` | {count:,} |")
    report.extend(
        [
            "",
            "### Literature-linked output classes",
            "",
            "| Output class | Records |",
            "|---|---:|",
        ]
    )
    for output_class, count in sorted(output_classes.items(), key=lambda item: (-item[1], item[0])):
        report.append(f"| `{output_class}` | {count:,} |")
    report.extend(
        [
            "",
            "## Interpretation",
            "",
            "- Public-only pairs are candidates for evidence review, not proof that mSCIdblit is incomplete. Differences can arise from species scope, complex representation, source inclusion, evidence thresholds, and inferred versus directly curated interactions.",
            "- mSCIdblit adds information that LR-only resources do not represent in the same row: receptor-proximal continuation, TF and target-gene annotations, output classes, context, assay/perturbation, source locators, and explicit non-causal traversal status.",
            "- A fair next comparison is therefore not only pair overlap. It should compare how many public LR pairs can be connected to intracellular, TF, and output evidence in mSCIdblit, and how many mSCIdblit routes are absent from each public resource because that resource stops at a different layer.",
            "",
            "## Reproduction",
            "",
            "```bash",
            "python3 scripts/compare_release_public_databases_v2.py",
            "```",
            "",
            "The JSON summary contains input hashes, counts, denominators, and route-tier details. `public_only_lr_candidates.tsv` is a review queue only; `primary_evidence_review_queue.tsv` contains only locator-bearing candidates that still require manual primary-paper verification.",
            "",
        ]
    )
    (args.output_dir / "PUBLIC_DATABASE_COMPARISON_V2.md").write_text("\n".join(report), encoding="utf-8")


if __name__ == "__main__":
    main()
