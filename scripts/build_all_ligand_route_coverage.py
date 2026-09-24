#!/usr/bin/env python3
"""Build a semantic, all-ligand route-coverage catalog.

The graph and literature-expansion tables retain the detailed evidence rows.
This derived table gives mSCS one compact row per ligand node so it can choose
the deepest available route layer without treating coverage as confidence.
Only node roles already exported by mSCIdblit are used for semantic counts;
no route, edge, causal assertion, or score is created here.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


LOCATOR_RE = re.compile(r"(?:PMID:[^;\s]+|PMCID:[^;\s]+|DOI:[^;\s]+|https?://[^;\s]+)", re.IGNORECASE)

OUTPUT_FIELDS = (
    "ligand_node_id",
    "ligand_label",
    "ligand_aliases",
    "ligand_role_status",
    "receptor_pair_count",
    "route_evidence_row_count",
    "literature_expansion_row_count",
    "primary_locator_route_count",
    "ligand_receptor_route_count",
    "intracellular_route_count",
    "transcription_factor_route_count",
    "functional_output_route_count",
    "target_gene_route_count",
    "full_target_gene_route_count",
    "full_functional_output_route_count",
    "unique_receptor_count",
    "unique_intracellular_count",
    "unique_transcription_factor_count",
    "unique_target_gene_count",
    "unique_output_count",
    "route_tiers",
    "coverage_status",
    "evidence_layer_note",
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv_gz(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in OUTPUT_FIELDS} for row in rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--summary-output", type=Path)
    return parser.parse_args()


def split_values(value: str) -> set[str]:
    return {part.strip() for part in value.split(";") if part.strip()}


def role_map(bundle: Path) -> dict[str, set[str]]:
    roles: dict[str, set[str]] = defaultdict(set)
    for row in read_tsv(bundle / "mechanism_node_roles.tsv"):
        roles[row["node_id"]].add(row["role"])
    return roles


def has_primary_locator(row: dict[str, str]) -> bool:
    return bool(LOCATOR_RE.search(row.get("primary_locator", "")))


def valid_ligand(node_id: str, roles: dict[str, set[str]]) -> bool:
    node_roles = roles.get(node_id, set())
    return "ligand" in node_roles and not ({"receptor", "transcription_factor", "target_gene"} & node_roles)


def valid_receptor(node_id: str, roles: dict[str, set[str]]) -> bool:
    node_roles = roles.get(node_id, set())
    return "receptor" in node_roles and "transcription_factor" not in node_roles


def valid_tf(node_id: str, roles: dict[str, set[str]]) -> bool:
    return "transcription_factor" in roles.get(node_id, set())


def valid_target(node_id: str, roles: dict[str, set[str]]) -> bool:
    return "target_gene" in roles.get(node_id, set())


def add_route_counts(
    row: dict[str, str],
    stats: dict[str, object],
    roles: dict[str, set[str]],
) -> None:
    receptor_id = row.get("receptor_node_id", "")
    relay_id = row.get("intracellular_continuation_node_id", "")
    tf_id = row.get("transcription_factor_node_id", "")
    target_id = row.get("target_gene_node_id", "")
    output_id = row.get("output_node_id", "") or row.get("output_label", "")
    if not valid_ligand(row.get("ligand_node_id", ""), roles):
        return
    if not valid_receptor(receptor_id, roles):
        return

    stats["receptors"].add(receptor_id)
    stats["route_rows"] += 1
    if has_primary_locator(row):
        stats["primary_locator_rows"] += 1
    stats["tiers"].update(split_values(row.get("route_tier", "")))
    stats["ligand_receptor_rows"] += 1
    if relay_id:
        stats["relays"].add(relay_id)
        stats["intracellular_rows"] += 1
    if tf_id and valid_tf(tf_id, roles):
        stats["tfs"].add(tf_id)
        stats["tf_rows"] += 1
    if output_id:
        stats["outputs"].add(output_id)
        stats["output_rows"] += 1
    if target_id and valid_target(target_id, roles):
        stats["targets"].add(target_id)
        stats["target_rows"] += 1
    if relay_id and tf_id and valid_tf(tf_id, roles) and target_id and valid_target(target_id, roles):
        stats["full_target_rows"] += 1
    if relay_id and tf_id and valid_tf(tf_id, roles) and output_id:
        stats["full_output_rows"] += 1


def status(stats: dict[str, object]) -> str:
    if stats["full_target_rows"]:
        return "full_target_gene_route"
    if stats["full_output_rows"]:
        return "full_functional_output_route"
    if stats["intracellular_rows"] or stats["tf_rows"] or stats["target_rows"] or stats["output_rows"]:
        return "partial_downstream_route"
    return "ligand_receptor_only"


def build(bundle: Path) -> tuple[list[dict[str, str]], dict[str, object]]:
    roles = role_map(bundle)
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    route_rows = read_tsv(bundle / "mechanism_signaling_route_evidence.tsv.gz")
    expansion_rows = read_tsv(bundle / "mechanism_literature_expansion.tsv")

    by_ligand: dict[str, dict[str, object]] = {}

    def stats_for(node_id: str) -> dict[str, object]:
        return by_ligand.setdefault(
            node_id,
            {
                "labels": set(),
                "receptors": set(),
                "relays": set(),
                "tfs": set(),
                "targets": set(),
                "outputs": set(),
                "tiers": set(),
                "route_rows": 0,
                "expansion_rows": 0,
                "primary_locator_rows": 0,
                "ligand_receptor_rows": 0,
                "intracellular_rows": 0,
                "tf_rows": 0,
                "output_rows": 0,
                "target_rows": 0,
                "full_target_rows": 0,
                "full_output_rows": 0,
            },
        )

    for row in route_rows:
        node_id = row.get("ligand_node_id", "")
        if node_id and valid_ligand(node_id, roles):
            stats = stats_for(node_id)
            stats["labels"].add(row.get("ligand_label", ""))
            add_route_counts(row, stats, roles)

    for row in expansion_rows:
        node_id = row.get("ligand_node_id", "")
        if node_id and valid_ligand(node_id, roles):
            stats = stats_for(node_id)
            stats["labels"].add(row.get("ligand_label", ""))
            stats["expansion_rows"] += 1

    output: list[dict[str, str]] = []
    for node_id in sorted(by_ligand):
        stats = by_ligand[node_id]
        node = nodes.get(node_id, {})
        labels = sorted(label for label in stats["labels"] if label)
        canonical = node.get("canonical_label", "") or (labels[0] if labels else "")
        output.append(
            {
                "ligand_node_id": node_id,
                "ligand_label": canonical,
                "ligand_aliases": ";".join(labels),
                "ligand_role_status": "exported_ligand_role_only",
                "receptor_pair_count": str(len(stats["receptors"])),
                "route_evidence_row_count": str(stats["route_rows"]),
                "literature_expansion_row_count": str(stats["expansion_rows"]),
                "primary_locator_route_count": str(stats["primary_locator_rows"]),
                "ligand_receptor_route_count": str(stats["ligand_receptor_rows"]),
                "intracellular_route_count": str(stats["intracellular_rows"]),
                "transcription_factor_route_count": str(stats["tf_rows"]),
                "functional_output_route_count": str(stats["output_rows"]),
                "target_gene_route_count": str(stats["target_rows"]),
                "full_target_gene_route_count": str(stats["full_target_rows"]),
                "full_functional_output_route_count": str(stats["full_output_rows"]),
                "unique_receptor_count": str(len(stats["receptors"])),
                "unique_intracellular_count": str(len(stats["relays"])),
                "unique_transcription_factor_count": str(len(stats["tfs"])),
                "unique_target_gene_count": str(len(stats["targets"])),
                "unique_output_count": str(len(stats["outputs"])),
                "route_tiers": ";".join(sorted(stats["tiers"])),
                "coverage_status": status(stats),
                "evidence_layer_note": (
                    "Derived coverage summary from exported route evidence and literature expansion; "
                    "not a confidence score, causal assertion, or graph traversal permission."
                ),
            }
        )

    summary = {
        "coverage_rows": len(output),
        "coverage_status_counts": dict(Counter(row["coverage_status"] for row in output)),
        "rows_with_full_target_gene_route": sum(row["coverage_status"] == "full_target_gene_route" for row in output),
        "rows_with_full_functional_output_route": sum(row["coverage_status"] == "full_functional_output_route" for row in output),
        "rows_with_partial_downstream_route": sum(row["coverage_status"] == "partial_downstream_route" for row in output),
        "rows_with_ligand_receptor_only": sum(row["coverage_status"] == "ligand_receptor_only" for row in output),
        "source_route_evidence_rows": len(route_rows),
        "source_literature_expansion_rows": len(expansion_rows),
        "semantic_role_filter": "ligand role required; receptor/TF/target-gene role overlap excluded from ligand input",
        "confidence_or_causal_fields_created": False,
    }
    return output, summary


def main() -> int:
    args = parse_args()
    rows, summary = build(args.bundle_dir.resolve())
    write_tsv_gz(args.output.resolve(), rows)
    if args.summary_output:
        args.summary_output.resolve().write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output.resolve()), **summary}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
