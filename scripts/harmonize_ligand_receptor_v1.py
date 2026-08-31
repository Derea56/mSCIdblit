#!/usr/bin/env python3
"""Harmonize mSCIdblit and CellChat ligand/receptor interactions.

The first public-database audit compared expanded component pairs.  This audit
keeps each ligand and receptor complex as a set of components, while mapping
unambiguous symbols found in mSCIdblit canonical names.  It is intentionally
read-only with respect to the frozen database and does not infer a complex from
free prose unless the component token is an already-known gene symbol.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from compare_public_databases_v1 import (
    DEFAULT_PSQL,
    normalize_symbol,
    one_symbol,
    read_tsv,
    run_psql,
    split_symbols,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--database",
        default="postgresql:///mscidblit_local?host=/private/tmp/mscidblit_pg_socket&port=55432",
    )
    parser.add_argument("--psql", default=DEFAULT_PSQL)
    parser.add_argument("--cellchat-human", type=Path, required=True)
    parser.add_argument("--cellchat-mouse", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def token_symbols(value: str | None, known_symbols: set[str]) -> set[str]:
    """Extract only whole tokens already present in the known symbol universe."""

    if not value:
        return set()
    symbols: set[str] = set()
    for token in re.findall(r"[A-Za-z][A-Za-z0-9]*", value):
        symbol = normalize_symbol(token)
        if symbol in known_symbols:
            symbols.add(symbol)
    return symbols


def map_entity(row: dict[str, str], known_symbols: set[str]) -> tuple[frozenset[str], str]:
    direct = one_symbol(row.get("gene_symbol"))
    if direct:
        return frozenset({direct}), "gene_symbol"

    canonical_symbols = token_symbols(row.get("canonical_name"), known_symbols)
    alias_symbols = token_symbols(row.get("aliases"), known_symbols)
    combined = canonical_symbols | alias_symbols
    if len(combined) >= 2:
        return frozenset(combined), "canonical_or_alias_complex_tokens"
    if combined:
        return frozenset(combined), "canonical_or_alias_single_token"
    return frozenset(), "unresolved"


def read_cellchat_rows(path: Path) -> tuple[list[dict[str, str]], set[str]]:
    rows = read_tsv(path)
    symbols = set()
    for row in rows:
        symbols.update(split_symbols(row.get("ligand.symbol", "")))
        symbols.update(split_symbols(row.get("receptor.symbol", "")))
    return rows, symbols


def public_signatures(rows: list[dict[str, str]]) -> tuple[set[tuple[frozenset[str], frozenset[str]]], Counter]:
    signatures: set[tuple[frozenset[str], frozenset[str]]] = set()
    rows_by_signature: Counter = Counter()
    for row in rows:
        ligand = frozenset(split_symbols(row.get("ligand.symbol", "")))
        receptor = frozenset(split_symbols(row.get("receptor.symbol", "")))
        if not ligand or not receptor:
            continue
        signature = (ligand, receptor)
        signatures.add(signature)
        rows_by_signature[signature] += 1
    return signatures, rows_by_signature


def compatible(ours: tuple[frozenset[str], frozenset[str]], public: tuple[frozenset[str], frozenset[str]]) -> bool:
    """Allow an optional complex component on one side, but not both sides."""

    our_ligand, our_receptor = ours
    public_ligand, public_receptor = public
    same_ligand = our_ligand == public_ligand and (our_receptor <= public_receptor or public_receptor <= our_receptor)
    same_receptor = our_receptor == public_receptor and (our_ligand <= public_ligand or public_ligand <= our_ligand)
    return same_ligand or same_receptor


def compare_signature_sets(
    ours: set[tuple[frozenset[str], frozenset[str]]],
    public: set[tuple[frozenset[str], frozenset[str]]],
    public_rows_by_signature: Counter,
) -> dict:
    exact = ours & public
    compatible_ours = {signature for signature in ours if any(compatible(signature, candidate) for candidate in public)}
    compatible_public = {signature for signature in public if any(compatible(candidate, signature) for candidate in ours)}
    exact_rows = sum(public_rows_by_signature[signature] for signature in exact)
    compatible_rows = sum(public_rows_by_signature[signature] for signature in compatible_public)
    return {
        "ours_unique_complex_signatures": len(ours),
        "public_unique_complex_signatures": len(public),
        "exact_signature_overlap": len(exact),
        "exact_ours_only": len(ours - public),
        "exact_public_only": len(public - ours),
        "compatible_ours_signatures": len(compatible_ours),
        "compatible_public_signatures": len(compatible_public),
        "compatible_ours_only": len(ours - compatible_ours),
        "compatible_public_only": len(public - compatible_public),
        "public_rows_with_exact_signature": exact_rows,
        "public_rows_with_compatible_signature": compatible_rows,
        "public_rows_total_with_components": sum(public_rows_by_signature.values()),
    }


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    entity_rows = run_psql(
        args.psql,
        args.database,
        """
        SELECT entity_id::text AS entity_id,
               canonical_name,
               COALESCE(gene_symbol, '') AS gene_symbol,
               COALESCE(aliases, '') AS aliases,
               entity_type
        FROM signalingentity
        ORDER BY entity_id
        """,
    )
    edge_rows = run_psql(
        args.psql,
        args.database,
        """
        SELECT se.edge_id::text AS edge_id,
               src.entity_id::text AS source_entity_id,
               src.canonical_name AS source_name,
               COALESCE(src.gene_symbol, '') AS source_gene_symbol,
               COALESCE(src.aliases, '') AS source_aliases,
               tgt.entity_id::text AS target_entity_id,
               tgt.canonical_name AS target_name,
               COALESCE(tgt.gene_symbol, '') AS target_gene_symbol,
               COALESCE(tgt.aliases, '') AS target_aliases
        FROM signalingedge se
        JOIN signalingentity src ON src.entity_id = se.source_entity_id
        JOIN signalingentity tgt ON tgt.entity_id = se.target_entity_id
        WHERE se.relation_type = 'binds_receptor'
          AND se.export_priority <> 'exclude'
        ORDER BY se.edge_id
        """,
    )
    cellchat_rows: dict[str, list[dict[str, str]]] = {}
    public_symbols: set[str] = set()
    for species, path in (("human", args.cellchat_human), ("mouse", args.cellchat_mouse)):
        rows, symbols = read_cellchat_rows(path)
        cellchat_rows[species] = rows
        public_symbols.update(symbols)

    mscidblit_symbols = {symbol for row in entity_rows if (symbol := one_symbol(row.get("gene_symbol")))}
    known_symbols = mscidblit_symbols | public_symbols

    our_signatures: set[tuple[frozenset[str], frozenset[str]]] = set()
    mapping_method_counts: Counter = Counter()
    unresolved_edge_rows = 0
    mapped_edge_rows = 0
    mapped_edge_examples: list[dict] = []
    for row in edge_rows:
        source_entity = {
            "canonical_name": row["source_name"],
            "gene_symbol": row["source_gene_symbol"],
            "aliases": row["source_aliases"],
        }
        target_entity = {
            "canonical_name": row["target_name"],
            "gene_symbol": row["target_gene_symbol"],
            "aliases": row["target_aliases"],
        }
        source_components, source_method = map_entity(source_entity, known_symbols)
        target_components, target_method = map_entity(target_entity, known_symbols)
        mapping_method_counts[f"source:{source_method}"] += 1
        mapping_method_counts[f"target:{target_method}"] += 1
        if not source_components or not target_components:
            unresolved_edge_rows += 1
            continue
        mapped_edge_rows += 1
        signature = (source_components, target_components)
        our_signatures.add(signature)
        if len(mapped_edge_examples) < 25 and (source_method != "gene_symbol" or target_method != "gene_symbol"):
            mapped_edge_examples.append(
                {
                    "edge_id": row["edge_id"],
                    "source_name": row["source_name"],
                    "source_components": sorted(source_components),
                    "source_method": source_method,
                    "target_name": row["target_name"],
                    "target_components": sorted(target_components),
                    "target_method": target_method,
                }
            )

    summary = {
        "analysis": {
            "graph_version": "1.0.0",
            "release_id": "module20_24_database_graph:v1.0.0",
            "retrieved_on": "2026-08-25",
            "harmonization_unit": "ordered ligand-component-set to receptor-component-set signature",
            "mapping_rule": "direct gene_symbol, otherwise only whole canonical/alias tokens already present in the mSCIdblit or CellChat symbol universe",
            "no_external_alias_table_applied": True,
        },
        "mSCIdblit": {
            "binding_edge_rows": len(edge_rows),
            "mapped_binding_edge_rows": mapped_edge_rows,
            "unresolved_binding_edge_rows": unresolved_edge_rows,
            "unique_complex_signatures": len(our_signatures),
            "entity_rows_with_alias_text": sum(bool(row.get("aliases", "").strip()) for row in entity_rows),
            "mapping_method_counts": dict(sorted(mapping_method_counts.items())),
            "mapped_complex_examples": mapped_edge_examples,
        },
        "cellchat": {},
        "sources": {
            "cellchat_human": "https://raw.githubusercontent.com/jinworks/CellChat/main/data/CellChatDB.human.rda",
            "cellchat_mouse": "https://raw.githubusercontent.com/jinworks/CellChat/main/data/CellChatDB.mouse.rda",
        },
    }
    for species in ("human", "mouse"):
        public, rows_by_signature = public_signatures(cellchat_rows[species])
        summary["cellchat"][species] = {
            "interaction_rows": len(cellchat_rows[species]),
            "unique_signatures": len(public),
            "signature_size_distribution": {
                "ligand_components_1": sum(len(signature[0]) == 1 for signature in public),
                "ligand_components_2_plus": sum(len(signature[0]) >= 2 for signature in public),
                "receptor_components_1": sum(len(signature[1]) == 1 for signature in public),
                "receptor_components_2_plus": sum(len(signature[1]) >= 2 for signature in public),
            },
            "comparison": compare_signature_sets(our_signatures, public, rows_by_signature),
        }

    (args.output_dir / "harmonized_lr_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    lines = [
        "# Harmonized mSCIdblit v1.0 ligand/receptor comparison",
        "",
        "This audit keeps a ligand/receptor complex as an ordered signature of component sets instead of expanding every receptor complex into separate component pairs. mSCIdblit canonical names are mapped only when their whole tokens match symbols already present in the mSCIdblit or CellChat symbol universe. No external alias table or speculative text matching is applied.",
        "",
        "## Why this changes the comparison",
        "",
        f"The frozen graph contains {len(edge_rows):,} exported `binds_receptor` rows. The harmonizer maps {mapped_edge_rows:,} rows to a component signature and leaves {unresolved_edge_rows:,} unresolved. Those mapped rows collapse to {len(our_signatures):,} unique complex signatures. CellChatDB is similarly collapsed from interaction rows to unique component-set signatures before comparison.",
        "",
        "## Harmonized results",
        "",
        "`Exact overlap` requires the ligand component set and receptor component set to be identical. `Compatible` allows an extra component on one side only, which is useful for optional co-receptor differences but should remain a review category rather than an automatic merge.",
        "",
        "| Species | mSCIdblit signatures | CellChat signatures | Exact overlap | Exact mSCIdblit-only | Exact CellChat-only | Compatible mSCIdblit-only | Compatible CellChat-only | CellChat rows with exact match | CellChat rows with compatible match |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for species in ("human", "mouse"):
        comparison = summary["cellchat"][species]["comparison"]
        lines.append(
            f"| {species} | {comparison['ours_unique_complex_signatures']:,} | {comparison['public_unique_complex_signatures']:,} | {comparison['exact_signature_overlap']:,} | {comparison['exact_ours_only']:,} | {comparison['exact_public_only']:,} | {comparison['compatible_ours_only']:,} | {comparison['compatible_public_only']:,} | {comparison['public_rows_with_exact_signature']:,} | {comparison['public_rows_with_compatible_signature']:,} |"
        )
    lines.extend(
        [
            "",
            "## Complex representation in CellChatDB",
            "",
            "| Species | Unique signatures | Ligand complexes (2+ components) | Receptor complexes (2+ components) |",
            "|---|---:|---:|---:|",
        ]
    )
    for species in ("human", "mouse"):
        data = summary["cellchat"][species]
        lines.append(
            f"| {species} | {data['unique_signatures']:,} | {data['signature_size_distribution']['ligand_components_2_plus']:,} | {data['signature_size_distribution']['receptor_components_2_plus']:,} |"
        )
    lines.extend(
        [
            "",
            "## Mapping limits",
            "",
            "- mSCIdblit’s `aliases` column is populated for only "
            f"{summary['mSCIdblit']['entity_rows_with_alias_text']:,} entities in this snapshot, so most harmonization comes from explicit gene symbols and canonical complex tokens.",
            "- A compatible match is not proof that the two resources describe the same biochemical complex; it identifies a candidate for manual review.",
            "- Species are reported separately, but symbol normalization is case-insensitive because the frozen graph is mouse-scoped while CellChat provides separate human and mouse tables.",
            "- The original expanded component-pair comparison remains useful for downstream queries. This harmonized view is the better completeness audit for complexes.",
            "",
            "## Reproduction",
            "",
            "```bash",
            "python3 scripts/harmonize_ligand_receptor_v1.py \\",
            "  --cellchat-human /private/tmp/cellchat_human_lr.tsv \\",
            "  --cellchat-mouse /private/tmp/cellchat_mouse_lr.tsv \\",
            "  --output-dir data/processed/public_database_comparison_v1",
            "```",
            "",
        ]
    )
    (args.output_dir / "HARMONIZED_LR_COMPARISON_V1.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
