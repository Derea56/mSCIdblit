#!/usr/bin/env python3
"""Compare the frozen mSCIdblit v1.0 graph with public pathway resources.

This is deliberately a conservative comparison.  It reports exact normalized
gene-symbol and pair overlap, while keeping complex/composite identifiers that
cannot be mapped one-to-one in an unresolved bucket.  Public resources have
different scopes and evidence policies, so the output is an inventory audit,
not a biological truth score.

The public input files are intentionally supplied by path rather than fetched
by this script.  That keeps the analysis reproducible and avoids embedding
third-party database snapshots in the repository.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import Iterable


DEFAULT_PSQL = "/Users/derea/Homebrew/bin/psql"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--database",
        default="postgresql:///mscidblit_local?host=/private/tmp/mscidblit_pg_socket&port=55432",
        help="PostgreSQL connection string accepted by psql.",
    )
    parser.add_argument("--psql", default=DEFAULT_PSQL)
    parser.add_argument("--cellchat-human", type=Path, required=True)
    parser.add_argument("--cellchat-mouse", type=Path, required=True)
    parser.add_argument("--trrust-human", type=Path, required=True)
    parser.add_argument("--trrust-mouse", type=Path, required=True)
    parser.add_argument("--dorothea-human", type=Path, required=True)
    parser.add_argument("--dorothea-mouse", type=Path, required=True)
    parser.add_argument("--omnipath-causal-human", type=Path, required=True)
    parser.add_argument("--omnipath-causal-mouse", type=Path, required=True)
    parser.add_argument("--reactome-gmt", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args()


def run_psql(psql: str, database: str, query: str) -> list[dict[str, str]]:
    result = subprocess.run(
        [psql, "-X", "--csv", "-v", "ON_ERROR_STOP=1", "-d", database, "-c", query],
        check=True,
        capture_output=True,
        text=True,
    )
    return list(csv.DictReader(io.StringIO(result.stdout)))


def read_tsv(path: Path, *, header: bool = True) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        if header:
            return list(csv.DictReader(handle, delimiter="\t"))
        reader = csv.reader(handle, delimiter="\t")
        return [
            {"tf": row[0], "target": row[1], "effect": row[2], "pmid": row[3]}
            for row in reader
            if len(row) >= 4 and any(cell.strip() for cell in row)
        ]


def normalize_symbol(value: str) -> str:
    """Normalize a single simple gene symbol for case-insensitive comparison."""

    return re.sub(r"[^A-Z0-9]", "", value.strip().upper())


def one_symbol(value: str | None) -> str:
    """Return a symbol only when a field is a one-to-one identifier."""

    if not value:
        return ""
    value = value.strip()
    if not value or re.search(r"[,;+|/\\\s]", value):
        return ""
    symbol = normalize_symbol(value)
    if not re.fullmatch(r"[A-Z][A-Z0-9]{1,15}", symbol):
        return ""
    return symbol


def split_symbols(value: str | None) -> set[str]:
    """Split a public complex field into conservative component symbols."""

    if not value:
        return set()
    symbols: set[str] = set()
    for token in re.split(r"[,;+|/\\\s]+", value):
        symbol = one_symbol(token)
        if symbol:
            symbols.add(symbol)
    return symbols


def overlap_metrics(ours: set, public: set) -> dict[str, int | float]:
    intersection = ours & public
    return {
        "ours": len(ours),
        "public": len(public),
        "overlap": len(intersection),
        "ours_only": len(ours - public),
        "public_only": len(public - ours),
        "jaccard": round(len(intersection) / len(ours | public), 6) if ours | public else 0.0,
        "ours_coverage_of_public": round(len(intersection) / len(public), 6) if public else 0.0,
        "public_coverage_of_ours": round(len(intersection) / len(ours), 6) if ours else 0.0,
    }


def read_cellchat(path: Path) -> tuple[set[str], set[str], set[tuple[str, str]], int, int]:
    ligands: set[str] = set()
    receptors: set[str] = set()
    pairs: set[tuple[str, str]] = set()
    rows = 0
    rows_with_pair = 0
    for row in read_tsv(path):
        rows += 1
        ligand_symbols = split_symbols(row.get("ligand.symbol", ""))
        receptor_symbols = split_symbols(row.get("receptor.symbol", ""))
        ligands.update(ligand_symbols)
        receptors.update(receptor_symbols)
        expanded = {(ligand, receptor) for ligand in ligand_symbols for receptor in receptor_symbols}
        if expanded:
            rows_with_pair += 1
            pairs.update(expanded)
    return ligands, receptors, pairs, rows, rows_with_pair


def read_tf_targets(path: Path, *, source: str) -> tuple[set[str], set[str], set[tuple[str, str]], int]:
    tf_symbols: set[str] = set()
    target_symbols: set[str] = set()
    pairs: set[tuple[str, str]] = set()
    raw_rows = 0
    if source == "trrust":
        rows = read_tsv(path, header=False)
        for row in rows:
            raw_rows += 1
            tf = one_symbol(row.get("tf"))
            target = one_symbol(row.get("target"))
            if tf:
                tf_symbols.add(tf)
            if target:
                target_symbols.add(target)
            if tf and target:
                pairs.add((tf, target))
    else:
        for row in read_tsv(path):
            raw_rows += 1
            tf = one_symbol(row.get("source_genesymbol"))
            target = one_symbol(row.get("target_genesymbol"))
            if tf:
                tf_symbols.add(tf)
            if target:
                target_symbols.add(target)
            if tf and target:
                pairs.add((tf, target))
    return tf_symbols, target_symbols, pairs, raw_rows


def read_causal_edges(path: Path) -> tuple[set[tuple[str, str]], set[tuple[str, str]], int, int]:
    """Read OmniPath causal rows as all symbolized and directed pair sets."""

    all_pairs: set[tuple[str, str]] = set()
    directed_pairs: set[tuple[str, str]] = set()
    raw_rows = 0
    directed_rows = 0
    for row in read_tsv(path):
        raw_rows += 1
        source = one_symbol(row.get("source_genesymbol"))
        target = one_symbol(row.get("target_genesymbol"))
        if not (source and target):
            continue
        pair = (source, target)
        all_pairs.add(pair)
        if row.get("is_directed", "").strip().lower() == "true":
            directed_rows += 1
            directed_pairs.add(pair)
    return all_pairs, directed_pairs, raw_rows, directed_rows


def read_reactome(path: Path) -> tuple[dict[str, set[str]], set[str]]:
    pathways: dict[str, set[str]] = {}
    genes: set[str] = set()
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            fields = line.rstrip("\n").split("\t")
            if len(fields) < 3:
                continue
            name = fields[0]
            pathway_genes = {symbol for value in fields[2:] for symbol in split_symbols(value)}
            pathways[name] = pathway_genes
            genes.update(pathway_genes)
    return pathways, genes


def pair_metrics(ours: set[tuple[str, str]], public: set[tuple[str, str]], our_tfs: set[str], public_tfs: set[str]) -> dict:
    base = overlap_metrics(ours, public)
    public_for_our_tfs = {pair for pair in public if pair[0] in our_tfs}
    ours_for_public_tfs = {pair for pair in ours if pair[0] in public_tfs}
    base.update(
        {
            "public_pairs_for_our_tfs": len(public_for_our_tfs),
            "public_pairs_for_our_tfs_not_in_ours": len(public_for_our_tfs - ours),
            "ours_pairs_for_public_tfs": len(ours_for_public_tfs),
            "ours_pairs_for_public_tfs_not_in_public": len(ours_for_public_tfs - public),
        }
    )
    return base


def pathway_label(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    roles = run_psql(
        args.psql,
        args.database,
        """
        SELECT e.entity_id::text AS entity_id,
               e.canonical_name,
               COALESCE(e.entity_type, '') AS entity_type,
               COALESCE(e.gene_symbol, '') AS gene_symbol,
               COALESCE(e.organism_scope, '') AS organism_scope,
               r.role
        FROM signalingentity e
        JOIN signalingentityrole r ON r.entity_id = e.entity_id
        WHERE r.export_priority <> 'exclude'
          AND r.role IN ('ligand', 'receptor', 'signaling_cascade', 'transcription_factor', 'target_gene')
        ORDER BY e.entity_id, r.role
        """,
    )
    edges = run_psql(
        args.psql,
        args.database,
        """
        SELECT se.edge_id::text AS edge_id,
               COALESCE(src.gene_symbol, '') AS source_gene_symbol,
               COALESCE(tgt.gene_symbol, '') AS target_gene_symbol,
               se.relation_type,
               COALESCE(sp.pathway_name, '') AS pathway_name
        FROM signalingedge se
        JOIN signalingentity src ON src.entity_id = se.source_entity_id
        JOIN signalingentity tgt ON tgt.entity_id = se.target_entity_id
        LEFT JOIN signalingpathway sp ON sp.pathway_id = se.pathway_id
        WHERE se.export_priority <> 'exclude'
        ORDER BY se.edge_id
        """,
    )
    regulon_members = run_psql(
        args.psql,
        args.database,
        """
        SELECT COALESCE(tf.gene_symbol, '') AS tf_gene_symbol,
               tf.canonical_name AS tf_name,
               COALESCE(target.gene_symbol, '') AS target_gene_symbol,
               target.canonical_name AS target_name,
               COALESCE(rm.membership_status, '') AS membership_status,
               COALESCE(rm.export_priority, '') AS export_priority
        FROM regulonmember rm
        JOIN regulon r ON r.regulon_id = rm.regulon_id
        JOIN signalingentity tf ON tf.entity_id = r.tf_entity_id
        JOIN signalingentity target ON target.entity_id = rm.target_entity_id
        WHERE r.source_registry = 'mSCIdblit_signaling_edges'
          AND r.source_version = '2026-08-25'
          AND rm.export_priority <> 'exclude'
        ORDER BY tf.canonical_name, target.canonical_name
        """,
    )

    role_symbols: defaultdict[str, set[str]] = defaultdict(set)
    role_unresolved: defaultdict[str, int] = defaultdict(int)
    for row in roles:
        symbol = one_symbol(row.get("gene_symbol"))
        role = row["role"]
        if symbol:
            role_symbols[role].add(symbol)
        else:
            role_unresolved[role] += 1

    our_lr_pairs: set[tuple[str, str]] = set()
    our_cascade_edge_pairs: set[tuple[str, str]] = set()
    for row in edges:
        source = one_symbol(row.get("source_gene_symbol"))
        target = one_symbol(row.get("target_gene_symbol"))
        if not (source and target):
            continue
        if row["relation_type"] == "binds_receptor":
            our_lr_pairs.add((source, target))
        else:
            our_cascade_edge_pairs.add((source, target))

    our_regulon_pairs: set[tuple[str, str]] = set()
    regulon_unresolved = 0
    for row in regulon_members:
        tf = one_symbol(row.get("tf_gene_symbol"))
        target = one_symbol(row.get("target_gene_symbol"))
        if tf and target:
            our_regulon_pairs.add((tf, target))
        else:
            regulon_unresolved += 1
    our_regulon_tfs = {tf for tf, _ in our_regulon_pairs}
    our_tf_symbols = role_symbols["transcription_factor"]
    our_cascade_symbols = role_symbols["signaling_cascade"]

    our_pathway_genes: defaultdict[str, set[str]] = defaultdict(set)
    for row in edges:
        pathway = row.get("pathway_name", "").strip()
        if not pathway:
            continue
        for field in ("source_gene_symbol", "target_gene_symbol"):
            symbol = one_symbol(row.get(field))
            if symbol:
                our_pathway_genes[pathway].add(symbol)

    cellchat: dict[str, dict] = {}
    for species, path in (("human", args.cellchat_human), ("mouse", args.cellchat_mouse)):
        ligands, receptors, pairs, rows, rows_with_pair = read_cellchat(path)
        cellchat[species] = {
            "ligands": ligands,
            "receptors": receptors,
            "pairs": pairs,
            "rows": rows,
            "rows_with_pair": rows_with_pair,
        }

    trrust: dict[str, dict] = {}
    dorothea: dict[str, dict] = {}
    for species, path in (("human", args.trrust_human), ("mouse", args.trrust_mouse)):
        tf, targets, pairs, rows = read_tf_targets(path, source="trrust")
        trrust[species] = {"tfs": tf, "targets": targets, "pairs": pairs, "rows": rows}
    for species, path in (("human", args.dorothea_human), ("mouse", args.dorothea_mouse)):
        tf, targets, pairs, rows = read_tf_targets(path, source="dorothea")
        dorothea[species] = {"tfs": tf, "targets": targets, "pairs": pairs, "rows": rows}

    causal: dict[str, dict] = {}
    for species, path in (("human", args.omnipath_causal_human), ("mouse", args.omnipath_causal_mouse)):
        all_pairs, directed_pairs, rows, directed_rows = read_causal_edges(path)
        causal[species] = {
            "pairs": all_pairs,
            "directed_pairs": directed_pairs,
            "rows": rows,
            "directed_rows": directed_rows,
        }

    reactome_pathways, reactome_genes = read_reactome(args.reactome_gmt)
    reactome_label_set = {pathway_label(name) for name in reactome_pathways}
    mscidblit_label_set = {pathway_label(name) for name in our_pathway_genes}

    role_comparison: dict[str, dict] = {}
    for role, public_key in (("ligand", "ligands"), ("receptor", "receptors")):
        for species in ("human", "mouse"):
            role_comparison[f"{role}_symbols_{species}"] = overlap_metrics(
                role_symbols[role], cellchat[species][public_key]
            )

    lr_comparison = {
        species: overlap_metrics(our_lr_pairs, cellchat[species]["pairs"])
        for species in ("human", "mouse")
    }

    tf_comparison: dict[str, dict] = {}
    regulon_comparison: dict[str, dict] = {}
    for source_name, source_data in (("trrust", trrust), ("dorothea", dorothea)):
        for species in ("human", "mouse"):
            tf_comparison[f"{source_name}_{species}"] = overlap_metrics(our_tf_symbols, source_data[species]["tfs"])
            regulon_comparison[f"{source_name}_{species}"] = pair_metrics(
                our_regulon_pairs,
                source_data[species]["pairs"],
                our_regulon_tfs or our_tf_symbols,
                source_data[species]["tfs"],
            )

    pathway_overlap_count = 0
    pathway_overlap_2plus = 0
    pathway_best_overlap: dict[str, int] = {}
    for pathway, genes in our_pathway_genes.items():
        best = max((len(genes & reference_genes) for reference_genes in reactome_pathways.values()), default=0)
        pathway_best_overlap[pathway] = best
        if best >= 1:
            pathway_overlap_count += 1
        if best >= 2:
            pathway_overlap_2plus += 1

    summary = {
        "analysis": {
            "graph_version": "1.0.0",
            "release_id": "module20_24_database_graph:v1.0.0",
            "retrieved_on": "2026-08-25",
            "comparison_unit": "case-insensitive normalized HGNC-style gene symbols and ordered source-target pairs",
            "unresolved_role_rows": dict(role_unresolved),
            "unresolved_regulon_member_rows": regulon_unresolved,
        },
        "frozen_graph": {
            "role_rows": len(roles),
            "role_symbols": {role: len(values) for role, values in sorted(role_symbols.items())},
            "binds_receptor_pairs_with_simple_symbols": len(our_lr_pairs),
            "non_ligand_receptor_edge_pairs_with_simple_symbols": len(our_cascade_edge_pairs),
            "generic_regulon_member_rows": len(regulon_members),
            "generic_regulon_pairs_with_simple_symbols": len(our_regulon_pairs),
            "generic_regulon_tfs_with_simple_symbols": len(our_regulon_tfs),
            "pathways_with_symbolized_edges": len(our_pathway_genes),
            "signaling_cascade_symbols": len(our_cascade_symbols),
        },
        "cellchat": {
            species: {
                "interaction_rows": cellchat[species]["rows"],
                "rows_with_symbolized_pair": cellchat[species]["rows_with_pair"],
                "ligand_symbols": len(cellchat[species]["ligands"]),
                "receptor_symbols": len(cellchat[species]["receptors"]),
                "pair_symbols": len(cellchat[species]["pairs"]),
                "role_comparison": {
                    "ligand": role_comparison[f"ligand_symbols_{species}"],
                    "receptor": role_comparison[f"receptor_symbols_{species}"],
                },
                "lr_pair_comparison": lr_comparison[species],
            }
            for species in ("human", "mouse")
        },
        "tf_sources": {
            "trrust": {
                species: {
                    "raw_rows": trrust[species]["rows"],
                    "tf_symbols": len(trrust[species]["tfs"]),
                    "target_symbols": len(trrust[species]["targets"]),
                    "pairs": len(trrust[species]["pairs"]),
                    "tf_node_comparison": tf_comparison[f"trrust_{species}"],
                    "pair_comparison": regulon_comparison[f"trrust_{species}"],
                }
                for species in ("human", "mouse")
            },
            "dorothea_omnipath": {
                species: {
                    "raw_rows": dorothea[species]["rows"],
                    "tf_symbols": len(dorothea[species]["tfs"]),
                    "target_symbols": len(dorothea[species]["targets"]),
                    "pairs": len(dorothea[species]["pairs"]),
                    "tf_node_comparison": tf_comparison[f"dorothea_{species}"],
                    "pair_comparison": regulon_comparison[f"dorothea_{species}"],
                }
                for species in ("human", "mouse")
            },
        },
        "signaling_cascade_edges": {
            species: {
                "raw_rows": causal[species]["rows"],
                "directed_rows": causal[species]["directed_rows"],
                "public_symbolized_pairs": len(causal[species]["pairs"]),
                "public_directed_symbolized_pairs": len(causal[species]["directed_pairs"]),
                "all_pair_comparison": overlap_metrics(our_cascade_edge_pairs, causal[species]["pairs"]),
                "directed_pair_comparison": overlap_metrics(our_cascade_edge_pairs, causal[species]["directed_pairs"]),
            }
            for species in ("human", "mouse")
        },
        "reactome": {
            "pathways": len(reactome_pathways),
            "gene_symbols": len(reactome_genes),
            "cascade_gene_comparison": overlap_metrics(our_cascade_symbols, reactome_genes),
            "mSCIdblit_pathways_with_symbolized_edges": len(our_pathway_genes),
            "mSCIdblit_pathways_with_one_or_more_shared_reactome_genes": pathway_overlap_count,
            "mSCIdblit_pathways_with_two_or_more_shared_reactome_genes": pathway_overlap_2plus,
            "exact_normalized_pathway_label_overlap": len(mscidblit_label_set & reactome_label_set),
        },
        "sources": {
            "cellchat": {
                "human": "https://raw.githubusercontent.com/jinworks/CellChat/main/data/CellChatDB.human.rda",
                "mouse": "https://raw.githubusercontent.com/jinworks/CellChat/main/data/CellChatDB.mouse.rda",
            },
            "trrust": {
                "human": "https://www.grnpedia.org/trrust/data/trrust_rawdata.human.tsv",
                "mouse": "https://www.grnpedia.org/trrust/data/trrust_rawdata.mouse.tsv",
            },
            "dorothea_omnipath": {
                "human": "https://omnipathdb.org/interactions?genesymbols=yes&datasets=dorothea&organisms=9606&fields=sources,references,curation_effort,dorothea_level",
                "mouse": "https://omnipathdb.org/interactions?genesymbols=yes&datasets=dorothea&organisms=10090&fields=sources,references,curation_effort,dorothea_level",
            },
            "omnipath_causal": {
                "human": "https://omnipathdb.org/interactions?genesymbols=yes&datasets=omnipath&organisms=9606&fields=sources,references,curation_effort",
                "mouse": "https://omnipathdb.org/interactions?genesymbols=yes&datasets=omnipath&organisms=10090&fields=sources,references,curation_effort",
            },
            "reactome": "https://reactome.org/download/current/ReactomePathways.gmt.zip",
        },
    }

    (args.output_dir / "comparison_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    def pct(value: float) -> str:
        return f"{value * 100:.1f}%"

    report_lines = [
        "# mSCIdblit v1.0 public-database comparison",
        "",
        "This audit compares the frozen `mSCIdblit-v1.0.0` / `mechanism-graph-v1.0.0` release with public snapshots retrieved on 2026-08-25. Exact overlap means case-insensitive normalized one-to-one gene symbols or ordered source-target pairs. Complexes and composite identifiers that cannot be reduced to one symbol are counted as unresolved rather than forced into a match.",
        "",
        "## Executive summary",
        "",
        f"- The frozen graph contains {len(roles):,} exported role rows, {len(our_lr_pairs):,} ligand-to-receptor pairs with simple symbols, and {len(our_regulon_pairs):,} generic TF-to-target pairs with simple symbols.",
            f"- CellChatDB provides the closest public ligand/receptor comparison. The result is reported separately for human and mouse because the source is species-specific and its receptor fields often represent complexes.",
            f"- TRRUST and OmniPath/DoRothEA provide independent TF-target comparisons. Public-only pairs are not automatically missing from mSCIdblit biologically; they are candidates for future curation under the current release scope.",
            f"- OmniPath’s curated causal interaction export is used as a directional edge-level proxy for signaling-cascade comparison, while Reactome is retained as a pathway-membership check.",
            f"- Reactome is compared at gene participation and pathway-label levels. Exact pathway-label overlap is {summary['reactome']['exact_normalized_pathway_label_overlap']}, which reflects different naming/modeling granularity and is not evidence that the signaling biology is absent.",
            "- A companion complex-level harmonized ligand/receptor audit preserves receptor component sets and maps unambiguous canonical tokens; see `HARMONIZED_LR_COMPARISON_V1.md` in this output directory.",
        "",
        "## Frozen graph inventory",
        "",
        "| Layer | Count | Unresolved role rows |",
        "|---|---:|---:|",
    ]
    for role in ("ligand", "receptor", "signaling_cascade", "transcription_factor", "target_gene"):
        report_lines.append(f"| `{role}` symbols | {len(role_symbols[role]):,} | {role_unresolved[role]:,} |")
    report_lines.extend(
        [
            f"| `binds_receptor` pairs with simple symbols | {len(our_lr_pairs):,} | — |",
            f"| generic regulon member rows | {len(regulon_members):,} | {regulon_unresolved:,} |",
            f"| generic regulon pairs with simple symbols | {len(our_regulon_pairs):,} | — |",
            "",
            "## Ligand/receptor comparison with CellChatDB",
            "",
            "Percentages below are overlap divided by the named denominator. `mSCIdblit-only` and `CellChat-only` are inventory differences, not validated biological omissions.",
            "",
            "| Species | Layer | mSCIdblit | CellChatDB | Exact overlap | mSCIdblit-only | CellChatDB-only | Fraction of mSCIdblit found in CellChatDB | Fraction of CellChatDB found in mSCIdblit |",
            "|---|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for species in ("human", "mouse"):
        for layer, key in (("ligand symbols", "ligand"), ("receptor symbols", "receptor"), ("LR component pairs", "pairs")):
            metric = lr_comparison[species] if key == "pairs" else role_comparison[f"{key}_symbols_{species}"]
            report_lines.append(
                f"| {species} | {layer} | {metric['ours']:,} | {metric['public']:,} | {metric['overlap']:,} | {metric['ours_only']:,} | {metric['public_only']:,} | {pct(metric['public_coverage_of_ours'])} | {pct(metric['ours_coverage_of_public'])} |"
            )
    report_lines.extend(
        [
            "",
            "## TF and regulon comparison",
            "",
            f"The pair comparison uses only mSCIdblit regulon memberships where both the TF and target have a simple symbol. It therefore covers {len(our_regulon_tfs):,} mSCIdblit TF symbols with at least one symbol-resolved regulon pair; the separate TF-node comparison covers all {len(our_tf_symbols):,} simple-symbol TF nodes. The `public pairs for mSCIdblit regulon TFs not in ours` column is the most useful estimate of additional public coverage within that 15-TF pair universe.",
            "",
            f"| Source | Species | Exact TF overlap | mSCIdblit pairs | Public pairs | Pair overlap | Public pairs for {len(our_regulon_tfs):,} mSCIdblit regulon TFs not in ours | mSCIdblit pairs for public TFs not in source |",
            "|---|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for source_name, label in (("trrust", "TRRUST"), ("dorothea_omnipath", "OmniPath/DoRothEA")):
        for species in ("human", "mouse"):
            data = summary["tf_sources"][source_name][species]
            tf_metric = data["tf_node_comparison"]
            pair_metric = data["pair_comparison"]
            report_lines.append(
                f"| {label} | {species} | {tf_metric['overlap']:,} | {pair_metric['ours']:,} | {pair_metric['public']:,} | {pair_metric['overlap']:,} | {pair_metric['public_pairs_for_our_tfs_not_in_ours']:,} | {pair_metric['ours_pairs_for_public_tfs_not_in_public']:,} |"
            )
    report_lines.extend(
        [
            "",
            "## Pathway and signaling-cascade comparison with Reactome",
            "",
            f"Reactome GMT contains {len(reactome_pathways):,} pathways and {len(reactome_genes):,} unique human gene symbols in the retrieved snapshot. mSCIdblit contributes {len(our_cascade_symbols):,} signaling-cascade symbols. {pathway_overlap_count:,} of {len(our_pathway_genes):,} mSCIdblit pathways with symbolized edges share at least one gene with at least one Reactome pathway, and {pathway_overlap_2plus:,} share at least two. These are participation checks, not direct pathway-equivalence calls.",
            "",
            "| Comparison | mSCIdblit | Reactome | Exact overlap | mSCIdblit-only | Reactome-only |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )
    cascade_metric = summary["reactome"]["cascade_gene_comparison"]
    report_lines.append(
        f"| signaling-cascade gene symbols | {cascade_metric['ours']:,} | {cascade_metric['public']:,} | {cascade_metric['overlap']:,} | {cascade_metric['ours_only']:,} | {cascade_metric['public_only']:,} |"
    )
    report_lines.extend(
        [
            "| normalized pathway labels | — | — | "
            f"{summary['reactome']['exact_normalized_pathway_label_overlap']:,} | — | — |",
            "",
            "## Directional signaling-edge comparison with OmniPath",
            "",
            "The cascade edge comparison excludes mSCIdblit `binds_receptor` edges and compares the remaining exported source-target pairs with simple symbols against OmniPath rows marked directed. Because mSCIdblit relation labels include both mechanistic and program-level evidence, this is an edge inventory screen, not a claim that every pair has identical semantics.",
            "",
            "| Species | mSCIdblit non-LR edge pairs | OmniPath directed pairs | Exact overlap | mSCIdblit-only | OmniPath-only | Fraction of mSCIdblit found in OmniPath | Fraction of OmniPath found in mSCIdblit |",
            "|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for species in ("human", "mouse"):
        metric = summary["signaling_cascade_edges"][species]["directed_pair_comparison"]
        report_lines.append(
            f"| {species} | {metric['ours']:,} | {metric['public']:,} | {metric['overlap']:,} | {metric['ours_only']:,} | {metric['public_only']:,} | {pct(metric['public_coverage_of_ours'])} | {pct(metric['ours_coverage_of_public'])} |"
        )
    report_lines.extend(
        [
            "",
            "## Interpretation and limits",
            "",
            "- Public-only content indicates a candidate gap relative to that source snapshot, but not necessarily an error: sources differ in species, evidence thresholds, complex modeling, directness, pathway scope, and whether they include context-specific or inferred edges.",
            "- mSCIdblit-only content is useful for review and provenance checking, but should not be treated as unsupported merely because another database lacks it.",
            "- Exact pair overlap is intentionally conservative. A receptor complex or TF alias can be biologically equivalent while failing a one-to-one symbol match; those cases belong in a separate mapping layer.",
            "- Reactome is a human pathway knowledgebase, so its gene-participation comparison should not be interpreted as a mouse completeness score.",
            "- The harmonized ligand/receptor companion report is the preferred completeness view for multimeric complexes; this original report retains the expanded component-pair view for compatibility with earlier results.",
            "- The JSON file beside this report contains the full counts, denominators, and source URLs for reruns.",
            "",
            "## Reproduction",
            "",
            "```bash",
            "python3 scripts/compare_public_databases_v1.py \\",
            "  --cellchat-human /private/tmp/cellchat_human_lr.tsv \\",
            "  --cellchat-mouse /private/tmp/cellchat_mouse_lr.tsv \\",
            "  --trrust-human /private/tmp/trrust_human.tsv \\",
            "  --trrust-mouse /private/tmp/trrust_mouse.tsv \\",
            "  --dorothea-human /private/tmp/omnipath_dorothea_human.tsv \\",
            "  --dorothea-mouse /private/tmp/omnipath_dorothea_mouse.tsv \\",
            "  --omnipath-causal-human /private/tmp/omnipath_causal_human.tsv \\",
            "  --omnipath-causal-mouse /private/tmp/omnipath_causal_mouse.tsv \\",
            "  --reactome-gmt /private/tmp/reactome_v97/ReactomePathways.gmt \\",
            "  --output-dir data/processed/public_database_comparison_v1",
            "```",
            "",
        ]
    )
    (args.output_dir / "PUBLIC_DATABASE_COMPARISON_V1.md").write_text(
        "\n".join(report_lines), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
