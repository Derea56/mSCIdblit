#!/usr/bin/env python3
"""Build a deduplicated all-ligand queue for full-route literature curation.

The route-evidence table intentionally contains many repeated compositions from
different source chains. This helper collapses those records by their ordered
ligand/receptor/intermediate/TF/output signature, while retaining the complete
set of route IDs, source chains, evidence IDs, pathway names, and stable
locators that support each signature.

The result is a curation worklist, not a confidence layer and not a graph
materialization. Missing links remain explicit and no new biological edge is
created by this script.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import shutil
import re
from collections import Counter, defaultdict
from pathlib import Path


ROUTE_FIELDS = (
    "route_evidence_id",
    "route_tier",
    "path_expression",
    "known_layers",
    "missing_layers",
    "ligand_node_id",
    "ligand_label",
    "ligand_receptor_edge_id",
    "receptor_node_id",
    "receptor_label",
    "receptor_intracellular_edge_id",
    "intracellular_continuation_node_id",
    "intracellular_continuation_label",
    "intracellular_tf_edge_id",
    "transcription_factor_node_id",
    "transcription_factor_label",
    "tf_target_edge_id",
    "target_gene_node_id",
    "target_gene_label",
    "output_label",
    "output_node_id",
    "pathway_name",
    "evidence_ids",
    "source_chain_id",
    "source_scope",
    "route_linkage_status",
)

OUTPUT_FIELDS = (
    "curation_candidate_id",
    "review_priority",
    "ligand_node_id",
    "ligand_label",
    "receptor_node_id",
    "receptor_label",
    "intracellular_continuation_node_id",
    "intracellular_continuation_label",
    "transcription_factor_node_id",
    "transcription_factor_label",
    "target_gene_node_id",
    "target_gene_label",
    "target_gene_node_ids",
    "target_gene_labels",
    "output_node_id",
    "output_label",
    "output_node_ids",
    "output_labels",
    "known_layers",
    "missing_layers",
    "route_tiers",
    "path_expressions",
    "route_count",
    "route_evidence_ids",
    "source_chain_ids",
    "ligand_receptor_edge_ids",
    "receptor_intracellular_edge_ids",
    "intracellular_tf_edge_ids",
    "tf_target_edge_ids",
    "pathway_names",
    "route_linkage_statuses",
    "evidence_ids",
    "stable_primary_locators",
    "source_scopes",
)

LOCATOR_RE = re.compile(r"(?:PMID:\S+|PMCID:\S+|DOI:\S+|https?://\S+)")


def read_tsv(path: Path) -> list[dict[str, str]]:
    opener = gzip.open if path.suffix == ".gz" else open
    kwargs = {"newline": "", "encoding": "utf-8", "errors": "replace"}
    if path.suffix == ".gz":
        with opener(path, "rt", **kwargs) as handle:
            return list(csv.DictReader(handle, delimiter="\t"))
    with opener(path, **kwargs) as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv_gz(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in OUTPUT_FIELDS} for row in rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--summary-output", type=Path)
    parser.add_argument("--output-bundle", type=Path)
    parser.add_argument("--release-id", default="")
    return parser.parse_args()


def tokens(value: str) -> set[str]:
    return {token for token in value.split("|") if token}


def split_values(*values: str) -> set[str]:
    output: set[str] = set()
    for value in values:
        output.update(token.strip() for token in value.split(";") if token.strip())
    return output


def candidate_signature(row: dict[str, str]) -> tuple[str, ...]:
    return tuple(row.get(field, "") for field in (
        "ligand_node_id",
        "receptor_node_id",
        "intracellular_continuation_node_id",
        "transcription_factor_node_id",
    ))


def review_priority(known_layers: set[str]) -> str:
    downstream = bool(known_layers & {"target_gene", "output"})
    if "intracellular_continuation" in known_layers and "transcription_factor" in known_layers and downstream:
        return "P1"
    if "intracellular_continuation" in known_layers and downstream:
        return "P2"
    if "transcription_factor" in known_layers and downstream:
        return "P2"
    return "P3"


def build_queue(routes: list[dict[str, str]], edge_sources: list[dict[str, str]]) -> tuple[list[dict[str, str]], dict[str, object]]:
    source_locators: dict[str, set[str]] = defaultdict(set)
    for source in edge_sources:
        locator = source.get("source_locator", "").strip()
        if not locator or source.get("source_locator_status") not in {"stable", "stable_plus_local"}:
            continue
        keys = {source.get("evidence_id", ""), source.get("edge_id", "")}
        keys.update(token for token in source.get("paper_id", "").split(";") if token)
        for key in keys:
            if key:
                source_locators[key].add(locator)

    grouped: dict[tuple[str, ...], list[dict[str, str]]] = defaultdict(list)
    excluded = Counter()
    for route in routes:
        layers = tokens(route.get("known_layers", ""))
        if not route.get("ligand_node_id") or not route.get("receptor_node_id"):
            excluded["missing_ligand_or_receptor"] += 1
            continue
        if not (layers & {"intracellular_continuation", "transcription_factor", "target_gene", "output"}):
            excluded["ligand_receptor_entry_only"] += 1
            continue
        grouped[candidate_signature(route)].append(route)

    output: list[dict[str, str]] = []
    for index, signature in enumerate(sorted(grouped), start=1):
        members = grouped[signature]
        representative = sorted(
            members,
            key=lambda row: (-len(tokens(row.get("known_layers", ""))), row.get("route_evidence_id", "")),
        )[0]
        known = set().union(*(tokens(row.get("known_layers", "")) for row in members))
        missing = set().union(*(tokens(row.get("missing_layers", "")) for row in members))
        route_tiers = split_values(*(row.get("route_tier", "") for row in members))
        path_expressions = split_values(*(row.get("path_expression", "") for row in members))
        route_ids = split_values(*(row.get("route_evidence_id", "") for row in members))
        source_chains = split_values(*(row.get("source_chain_id", "") for row in members))
        lr_edges = split_values(*(row.get("ligand_receptor_edge_id", "") for row in members))
        receptor_intracellular_edges = split_values(*(row.get("receptor_intracellular_edge_id", "") for row in members))
        intracellular_tf_edges = split_values(*(row.get("intracellular_tf_edge_id", "") for row in members))
        tf_target_edges = split_values(*(row.get("tf_target_edge_id", "") for row in members))
        pathways = split_values(*(row.get("pathway_name", "") for row in members))
        linkage_statuses = split_values(*(row.get("route_linkage_status", "") for row in members))
        evidence_ids = split_values(*(row.get("evidence_ids", "") for row in members))
        source_scopes = split_values(*(row.get("source_scope", "") for row in members))
        target_gene_pairs = sorted(
            {
                (row.get("target_gene_node_id", ""), row.get("target_gene_label", ""))
                for row in members
                if row.get("target_gene_node_id") or row.get("target_gene_label")
            }
        )
        output_pairs = sorted(
            {
                (row.get("output_node_id", ""), row.get("output_label", ""))
                for row in members
                if row.get("output_node_id") or row.get("output_label")
            }
        )
        locators: set[str] = set()
        for evidence_id in evidence_ids | lr_edges | receptor_intracellular_edges | intracellular_tf_edges | tf_target_edges:
            locators.update(source_locators.get(evidence_id, set()))
        for row in members:
            locators.update(LOCATOR_RE.findall(row.get("evidence_ids", "")))
        output.append(
            {
                "curation_candidate_id": f"FULLSEQ:{index:06d}",
                "review_priority": review_priority(known),
                "ligand_node_id": representative.get("ligand_node_id", ""),
                "ligand_label": representative.get("ligand_label", ""),
                "receptor_node_id": representative.get("receptor_node_id", ""),
                "receptor_label": representative.get("receptor_label", ""),
                "intracellular_continuation_node_id": representative.get("intracellular_continuation_node_id", ""),
                "intracellular_continuation_label": representative.get("intracellular_continuation_label", ""),
                "transcription_factor_node_id": representative.get("transcription_factor_node_id", ""),
                "transcription_factor_label": representative.get("transcription_factor_label", ""),
                "target_gene_node_id": representative.get("target_gene_node_id", ""),
                "target_gene_label": representative.get("target_gene_label", ""),
                "target_gene_node_ids": ";".join(node_id for node_id, _ in target_gene_pairs if node_id),
                "target_gene_labels": ";".join(label for _, label in target_gene_pairs if label),
                "output_node_id": representative.get("output_node_id", ""),
                "output_label": representative.get("output_label", ""),
                "output_node_ids": ";".join(node_id for node_id, _ in output_pairs if node_id),
                "output_labels": ";".join(label for _, label in output_pairs if label),
                "known_layers": "|".join(sorted(known)),
                "missing_layers": "|".join(sorted(missing)),
                "route_tiers": ";".join(sorted(route_tiers)),
                "path_expressions": ";".join(sorted(path_expressions)),
                "route_count": str(len(members)),
                "route_evidence_ids": ";".join(sorted(route_ids)),
                "source_chain_ids": ";".join(sorted(source_chains)),
                "ligand_receptor_edge_ids": ";".join(sorted(lr_edges)),
                "receptor_intracellular_edge_ids": ";".join(sorted(receptor_intracellular_edges)),
                "intracellular_tf_edge_ids": ";".join(sorted(intracellular_tf_edges)),
                "tf_target_edge_ids": ";".join(sorted(tf_target_edges)),
                "pathway_names": ";".join(sorted(pathways)),
                "route_linkage_statuses": ";".join(sorted(linkage_statuses)),
                "evidence_ids": ";".join(sorted(evidence_ids)),
                "stable_primary_locators": ";".join(sorted(locators)),
                "source_scopes": ";".join(sorted(source_scopes)),
            }
        )

    output.sort(key=lambda row: (row["review_priority"], row["ligand_label"].casefold(), row["curation_candidate_id"]))
    for index, row in enumerate(output, start=1):
        row["curation_candidate_id"] = f"FULLSEQ:{index:06d}"
    summary = {
        "route_records_seen": len(routes),
        "route_records_excluded": dict(sorted(excluded.items())),
        "curation_candidate_count": len(output),
        "unique_ligands": len({row["ligand_node_id"] for row in output}),
        "unique_receptors": len({row["receptor_node_id"] for row in output}),
        "review_priority_counts": dict(sorted(Counter(row["review_priority"] for row in output).items())),
        "known_layer_counts": dict(sorted(Counter(layer for row in output for layer in row["known_layers"].split("|") if layer).items())),
        "route_tier_counts": dict(sorted(Counter(tier for row in output for tier in row["route_tiers"].split(";") if tier).items())),
        "policy": (
            "Deduplicated evidence-route signatures for all ligands; source chains and stable locators are retained. "
            "This is a primary-literature curation queue only: no confidence score, causal edge, or missing-link assertion is created."
        ),
    }
    return output, summary


def main() -> int:
    args = parse_args()
    bundle = args.bundle_dir.resolve()
    if args.output_bundle and not args.release_id:
        raise ValueError("--release-id is required with --output-bundle")
    if not args.output_bundle and (not args.output or not args.summary_output):
        raise ValueError("--output and --summary-output are required unless --output-bundle is used")
    route_path = bundle / "mechanism_signaling_route_evidence.tsv.gz"
    if not route_path.exists():
        route_path = bundle / "mechanism_signaling_route_evidence.tsv"
    routes = read_tsv(route_path)
    edge_sources = read_tsv(bundle / "mechanism_edge_sources.tsv")
    rows, summary = build_queue(routes, edge_sources)
    if args.output_bundle:
        output_bundle = args.output_bundle.resolve()
        if output_bundle.exists():
            raise FileExistsError(f"Output bundle already exists: {output_bundle}")
        shutil.copytree(bundle, output_bundle)
        output = output_bundle / "mechanism_full_sequence_curation_queue.tsv.gz"
        summary_output = output_bundle / "full_sequence_curation_queue_summary.json"
        metadata_path = output_bundle / "bundle_metadata.json"
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        metadata["release_id"] = args.release_id
        metadata.setdefault("counts", {})["full_sequence_curation_queue"] = len(rows)
        metadata.setdefault("files", {})["full_sequence_curation_queue"] = "mechanism_full_sequence_curation_queue.tsv.gz"
        metadata.setdefault("graph_policy", {})["full_sequence_curation_queue_is_evidence_only"] = True
        statement = (
            "The all-ligand full-sequence curation queue aggregates route evidence for primary-literature review; "
            "it creates no confidence score, causal graph edge, or assertion for a missing link."
        )
        if statement not in metadata.setdefault("accuracy_contract", []):
            metadata["accuracy_contract"].append(statement)
        metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    else:
        output = args.output.resolve()
        summary_output = args.summary_output.resolve()
    write_tsv_gz(output, rows)
    summary_output.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(output), "summary_output": str(summary_output), **summary}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
