#!/usr/bin/env python3
"""Build a species-aware, source-bound mouse/human gene identifier crosswalk."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RELEASE = ROOT / "data/processed/mscs_release_bundle_v1_7_0_nichenet_tf_prior_v1"
DEFAULT_MOUSE_GENE_INFO = Path("/private/tmp/Mus_musculus.gene_info.gz")
DEFAULT_HUMAN_GENE_INFO = Path("/private/tmp/Homo_sapiens.gene_info.gz")
DEFAULT_ORTHOLOGS = Path("/private/tmp/gene_orthologs.gz")
DEFAULT_OUTPUT = ROOT / "data/processed/gene_identifier_crosswalk_ncbi_2026_10_02_v2"

SPECIES = {
    "mouse": {"tax_id": "10090", "prefix": "ENSMUSG"},
    "human": {"tax_id": "9606", "prefix": "ENSG"},
}

CATALOG_FIELDS = [
    "species", "tax_id", "entrez_gene_id", "canonical_symbol", "ensembl_gene_id",
    "aliases_json", "dbxrefs_json", "gene_type", "description", "source_record_id",
    "source_path", "source_sha256",
]
CROSSWALK_FIELDS = [
    "crosswalk_id", "query_symbol", "lookup_key", "query_species_scope", "species",
    "mapping_status", "mapping_kind", "canonical_symbol", "entrez_gene_id",
    "ensembl_gene_id", "aliases_json", "source_record_id", "source_registry_path",
    "source_registry_sha256", "query_sources_json", "orthology_record_id",
    "orthology_status", "notes",
]
ORTHOLOGY_FIELDS = [
    "orthology_record_id", "mouse_entrez_gene_id", "mouse_symbol", "human_entrez_gene_id",
    "human_symbol", "relationship", "mapping_cardinality", "source_path", "source_sha256",
]
LABEL_AUDIT_FIELDS = [
    "label_audit_id", "label", "label_kind", "query_species_scope", "source_records_json",
    "mouse_mapping_status", "mouse_entrez_gene_ids", "mouse_symbols", "mouse_ensembl_gene_ids",
    "human_mapping_status", "human_entrez_gene_ids", "human_symbols", "human_ensembl_gene_ids",
    "unresolved_mapping_reason",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    csv.field_size_limit(max(csv.field_size_limit(), 10_000_000))
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


def parse_dbxrefs(value: str) -> dict[str, list[str]]:
    result: dict[str, list[str]] = defaultdict(list)
    for token in value.split("|"):
        if ":" not in token:
            continue
        prefix, identifier = token.split(":", 1)
        if prefix and identifier:
            result[prefix].append(identifier)
    return {key: sorted(set(values)) for key, values in sorted(result.items())}


def aliases_for(row: dict[str, str]) -> list[str]:
    values = [row.get("Symbol", "").strip()]
    values.extend(token.strip() for token in row.get("Synonyms", "").split("|") if token.strip() and token.strip() != "-")
    return sorted(set(values))


def query_token(query_symbol: str, query_species_scope: str) -> str:
    """Return a stable collision-resistant token for the exact query namespace."""
    value = f"{query_species_scope}\0{query_symbol}"
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:20]


def parse_gene_info(path: Path, species: str) -> tuple[list[dict[str, str]], dict[str, list[dict[str, str]]]]:
    if not path.is_file():
        raise SystemExit(f"Missing NCBI GeneInfo source: {path}")
    source_hash = sha256(path)
    rows: list[dict[str, str]] = []
    by_lookup: dict[str, list[dict[str, str]]] = defaultdict(list)
    expected_tax = SPECIES[species]["tax_id"]
    with gzip.open(path, "rt", newline="", encoding="utf-8") as handle:
        header_line = handle.readline().rstrip("\n")
        fieldnames = header_line.lstrip("#").split("\t")
        reader = csv.DictReader(handle, fieldnames=fieldnames, delimiter="\t")
        required = {"tax_id", "GeneID", "Symbol", "Synonyms", "dbXrefs", "type_of_gene", "description"}
        if not required.issubset(reader.fieldnames or []):
            raise SystemExit(f"NCBI GeneInfo source is missing required fields: {path}")
        for row in reader:
            if row.get("tax_id") != expected_tax or not row.get("GeneID") or not row.get("Symbol"):
                continue
            dbxrefs = parse_dbxrefs(row.get("dbXrefs", ""))
            ensembl = dbxrefs.get("Ensembl", [])
            record = {
                "species": species,
                "tax_id": expected_tax,
                "entrez_gene_id": row["GeneID"],
                "canonical_symbol": row["Symbol"],
                "ensembl_gene_id": "|".join(ensembl),
                "aliases_json": json.dumps(aliases_for(row), separators=(",", ":")),
                "dbxrefs_json": json.dumps(dbxrefs, separators=(",", ":")),
                "gene_type": row.get("type_of_gene", ""),
                "description": row.get("description", ""),
                "source_record_id": f"NCBI GeneID:{row['GeneID']}",
                "source_path": str(path),
                "source_sha256": source_hash,
                "_aliases": aliases_for(row),
            }
            rows.append(record)
            for alias in record["_aliases"]:
                by_lookup[alias.casefold()].append(record)
    return rows, by_lookup


def load_query_symbols(release: Path) -> list[dict[str, Any]]:
    queries: dict[tuple[str, str], dict[str, Any]] = {}

    def add(symbol: str, scope: str, source: str, source_path: str, source_id: str) -> None:
        symbol = symbol.strip()
        if not symbol or symbol in {"-", "NA", "None"}:
            return
        key = (symbol, scope)
        item = queries.setdefault(key, {"query_symbol": symbol, "query_species_scope": scope, "sources": []})
        item["sources"].append({"source": source, "source_path": source_path, "source_id": source_id})

    prior = release / "tf_target_prior"
    for filename, field, id_field in (("tf_axis.tsv", "tf_symbol", "tf_id"), ("target_axis.tsv", "target_symbol", "target_id")):
        path = prior / filename
        for row in read_tsv(path):
            add(row[field], "mouse", "tf_target_prior_axis", str(path), row[id_field])
    for filename, field, source in (("target_genes.tsv", "target_id", "nichenet_target_axis"), ("ligands.tsv", "ligand_id", "nichenet_ligand_axis")):
        path = release / "method_resources/method_native/nichenet_neutral_v1" / filename
        for row in read_tsv(path):
            add(row[field], "mouse", source, str(path), row[field])
    graph_path = release / "mechanism_graph/mechanism_nodes.tsv"
    for row in read_tsv(graph_path):
        if row.get("gene_symbol", "").strip():
            add(row["gene_symbol"], "unscoped", "mechanism_graph_gene_symbol", str(graph_path), row.get("node_id", ""))
    candidate_path = release / "candidate_universe/mechanism_lr_candidate_universe.tsv"
    candidate_fields = (
        ("ligand_name", "candidate_universe_label"),
        ("receptor_name", "candidate_universe_label"),
        ("normalized_ligand_name", "candidate_universe_label"),
        ("normalized_receptor_name", "candidate_universe_label"),
    )
    for row in read_tsv(candidate_path):
        for field, source in candidate_fields:
            add(row.get(field, ""), "mouse", source, str(candidate_path), row.get("candidate_pair_id", ""))
        for field in ("ligand_components", "receptor_components"):
            for component in row.get(field, "").split("|"):
                add(component, "mouse", "candidate_component_label", str(candidate_path), row.get("candidate_pair_id", ""))
    bridge_path = release / "mechanism_graph/mechanism_output_bridges_validated.tsv"
    for row in read_tsv(bridge_path):
        for label in row.get("output_product_labels", "").split(";"):
            add(label, "unscoped", "validated_output_product_label", str(bridge_path), row.get("bridge_id", ""))
    return sorted(queries.values(), key=lambda item: (item["query_species_scope"], item["query_symbol"].casefold()))


def build_label_audit(queries: list[dict[str, Any]], crosswalk: list[dict[str, str]]) -> list[dict[str, str]]:
    """Summarize exact active-release candidate/output labels by source-backed species mapping."""
    relevant = {"candidate_universe_label", "candidate_component_label", "validated_output_product_label"}
    audit_rows: list[dict[str, str]] = []
    direct_statuses = {"resolved_source_canonical", "resolved_source_alias", "ambiguous_source_alias"}

    def mapped(rows: list[dict[str, str]], species: str) -> tuple[str, list[dict[str, str]]]:
        matches = [row for row in rows if row.get("species") == species and row.get("mapping_status") in direct_statuses]
        ids = {row.get("entrez_gene_id", "") for row in matches if row.get("entrez_gene_id")}
        if not matches:
            return "unresolved_source_symbol", []
        if any(row.get("mapping_status") == "ambiguous_source_alias" for row in matches):
            return "ambiguous_source_alias", matches
        if len(ids) == 1:
            return "uniquely_mapped_source_gene", matches
        return "multiple_source_mappings", matches

    for query in queries:
        source_kinds = sorted({item["source"] for item in query["sources"] if item["source"] in relevant})
        if not source_kinds:
            continue
        query_rows = [
            row for row in crosswalk
            if row.get("query_symbol") == query["query_symbol"]
            and row.get("query_species_scope") == query["query_species_scope"]
        ]
        token = query_token(query["query_symbol"], query["query_species_scope"])
        for source_kind in source_kinds:
            mouse_status, mouse_rows = mapped(query_rows, "mouse")
            human_status, human_rows = mapped(query_rows, "human")
            def values(rows: list[dict[str, str]], field: str) -> str:
                return "|".join(sorted({row.get(field, "") for row in rows if row.get(field, "")}))
            reason = ""
            if mouse_status == "unresolved_source_symbol" or human_status == "unresolved_source_symbol":
                reason = "No exact case-normalized source-backed mouse or human record for this active-release label."
            elif mouse_status in {"ambiguous_source_alias", "multiple_source_mappings"} or human_status in {"ambiguous_source_alias", "multiple_source_mappings"}:
                reason = "Multiple or ambiguous source-backed records retained without selecting one."
            audit_rows.append({
                "label_audit_id": f"GENE_LABEL_AUDIT:{source_kind}:{token}",
                "label": query["query_symbol"],
                "label_kind": source_kind,
                "query_species_scope": query["query_species_scope"],
                "source_records_json": json.dumps(query["sources"], sort_keys=True, separators=(",", ":")),
                "mouse_mapping_status": mouse_status,
                "mouse_entrez_gene_ids": values(mouse_rows, "entrez_gene_id"),
                "mouse_symbols": values(mouse_rows, "canonical_symbol"),
                "mouse_ensembl_gene_ids": values(mouse_rows, "ensembl_gene_id"),
                "human_mapping_status": human_status,
                "human_entrez_gene_ids": values(human_rows, "entrez_gene_id"),
                "human_symbols": values(human_rows, "canonical_symbol"),
                "human_ensembl_gene_ids": values(human_rows, "ensembl_gene_id"),
                "unresolved_mapping_reason": reason,
            })
    return sorted(audit_rows, key=lambda row: (row["label_kind"], row["label"].casefold(), row["query_species_scope"]))


def load_orthology(path: Path, catalogs: dict[str, dict[str, dict[str, str]]]) -> list[dict[str, str]]:
    source_hash = sha256(path)
    pairs: dict[tuple[str, str], dict[str, str]] = {}
    with gzip.open(path, "rt", newline="", encoding="utf-8") as handle:
        header_line = handle.readline().rstrip("\n")
        fieldnames = header_line.lstrip("#").split("\t")
        reader = csv.DictReader(handle, fieldnames=fieldnames, delimiter="\t")
        for row in reader:
            tax_a, tax_b = row.get("tax_id", ""), row.get("Other_tax_id", "")
            gene_a, gene_b = row.get("GeneID", ""), row.get("Other_GeneID", "")
            if {tax_a, tax_b} != {SPECIES["mouse"]["tax_id"], SPECIES["human"]["tax_id"]}:
                continue
            if tax_a == SPECIES["mouse"]["tax_id"]:
                mouse_id, human_id = gene_a, gene_b
            else:
                mouse_id, human_id = gene_b, gene_a
            if mouse_id not in catalogs["mouse"] or human_id not in catalogs["human"]:
                continue
            pairs[(mouse_id, human_id)] = {
                "mouse_entrez_gene_id": mouse_id,
                "mouse_symbol": catalogs["mouse"][mouse_id]["canonical_symbol"],
                "human_entrez_gene_id": human_id,
                "human_symbol": catalogs["human"][human_id]["canonical_symbol"],
                "relationship": row.get("relationship", ""),
                "source_path": str(path),
                "source_sha256": source_hash,
            }
    by_mouse: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in pairs.values():
        by_mouse[row["mouse_entrez_gene_id"]].append(row)
    output = []
    for row in sorted(pairs.values(), key=lambda value: (value["mouse_entrez_gene_id"], value["human_entrez_gene_id"])):
        cardinality = "one_to_many" if len(by_mouse[row["mouse_entrez_gene_id"]]) > 1 else "one_to_one"
        row = dict(row)
        row["mapping_cardinality"] = cardinality
        row["orthology_record_id"] = f"NCBI_ORTHOLOGY:{row['mouse_entrez_gene_id']}:{row['human_entrez_gene_id']}"
        output.append(row)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release-dir", type=Path, default=DEFAULT_RELEASE)
    parser.add_argument("--mouse-gene-info", type=Path, default=DEFAULT_MOUSE_GENE_INFO)
    parser.add_argument("--human-gene-info", type=Path, default=DEFAULT_HUMAN_GENE_INFO)
    parser.add_argument("--gene-orthologs", type=Path, default=DEFAULT_ORTHOLOGS)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    release = args.release_dir.resolve()
    output = args.output_dir.resolve()
    if output.exists():
        raise SystemExit(f"Refusing to overwrite crosswalk output: {output}")

    mouse_catalog_rows, mouse_lookup = parse_gene_info(args.mouse_gene_info.resolve(), "mouse")
    human_catalog_rows, human_lookup = parse_gene_info(args.human_gene_info.resolve(), "human")
    catalogs = {
        "mouse": {row["entrez_gene_id"]: row for row in mouse_catalog_rows},
        "human": {row["entrez_gene_id"]: row for row in human_catalog_rows},
    }
    queries = load_query_symbols(release)
    lookup_by_species = {"mouse": mouse_lookup, "human": human_lookup}
    crosswalk: list[dict[str, str]] = []
    resolved_mouse_ids: set[str] = set()
    for query in queries:
        scopes = ["mouse", "human"] if query["query_species_scope"] == "unscoped" else [query["query_species_scope"]]
        token = query_token(query["query_symbol"], query["query_species_scope"])
        for species in scopes:
            matches = list({match["entrez_gene_id"]: match for match in lookup_by_species[species].get(query["query_symbol"].casefold(), [])}.values())
            if not matches:
                crosswalk.append({
                    "crosswalk_id": f"GENE_XW:{species}:{token}:unresolved",
                    "query_symbol": query["query_symbol"],
                    "lookup_key": query["query_symbol"].casefold(),
                    "query_species_scope": query["query_species_scope"],
                    "species": species,
                    "mapping_status": "unresolved_source_symbol",
                    "mapping_kind": "none",
                    "query_sources_json": json.dumps(query["sources"], sort_keys=True, separators=(",", ":")),
                    "notes": "No exact case-normalized canonical symbol or alias in the NCBI GeneInfo snapshot.",
                })
                continue
            status = "resolved_source_canonical" if any(m["canonical_symbol"].casefold() == query["query_symbol"].casefold() for m in matches) else "resolved_source_alias"
            if len(matches) > 1:
                status = "ambiguous_source_alias"
            for match in sorted(matches, key=lambda row: row["entrez_gene_id"]):
                if species == "mouse":
                    resolved_mouse_ids.add(match["entrez_gene_id"])
                crosswalk.append({
                    "crosswalk_id": f"GENE_XW:{species}:{token}:{match['entrez_gene_id']}",
                    "query_symbol": query["query_symbol"],
                    "lookup_key": query["query_symbol"].casefold(),
                    "query_species_scope": query["query_species_scope"],
                    "species": species,
                    "mapping_status": status,
                    "mapping_kind": "canonical_symbol" if match["canonical_symbol"].casefold() == query["query_symbol"].casefold() else "alias",
                    "canonical_symbol": match["canonical_symbol"],
                    "entrez_gene_id": match["entrez_gene_id"],
                    "ensembl_gene_id": match["ensembl_gene_id"],
                    "aliases_json": match["aliases_json"],
                    "source_record_id": match["source_record_id"],
                    "source_registry_path": match["source_path"],
                    "source_registry_sha256": match["source_sha256"],
                    "query_sources_json": json.dumps(query["sources"], sort_keys=True, separators=(",", ":")),
                    "notes": "Casefolded lookup only; ambiguous source aliases are retained without choosing a record." if len(matches) > 1 else "Exact source-backed canonical symbol or alias match.",
                })

    orthology_rows = load_orthology(args.gene_orthologs.resolve(), catalogs)
    by_mouse_id: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in orthology_rows:
        by_mouse_id[row["mouse_entrez_gene_id"]].append(row)
    for row in crosswalk[:]:
        if row.get("species") != "mouse" or row.get("entrez_gene_id") not in resolved_mouse_ids:
            continue
        for orth in by_mouse_id.get(row["entrez_gene_id"], []):
            crosswalk.append({
                "crosswalk_id": f"GENE_XW:orthology:{row['crosswalk_id']}:{orth['human_entrez_gene_id']}",
                "query_symbol": row["query_symbol"],
                "lookup_key": row["lookup_key"],
                "query_species_scope": row["query_species_scope"],
                "species": "human",
                "mapping_status": "explicit_orthology_one_to_many" if orth["mapping_cardinality"] == "one_to_many" else "explicit_orthology_one_to_one",
                "mapping_kind": "explicit_orthology",
                "canonical_symbol": orth["human_symbol"],
                "entrez_gene_id": orth["human_entrez_gene_id"],
                "ensembl_gene_id": catalogs["human"][orth["human_entrez_gene_id"]]["ensembl_gene_id"],
                "aliases_json": catalogs["human"][orth["human_entrez_gene_id"]]["aliases_json"],
                "source_record_id": catalogs["human"][orth["human_entrez_gene_id"]]["source_record_id"],
                "source_registry_path": catalogs["human"][orth["human_entrez_gene_id"]]["source_path"],
                "source_registry_sha256": catalogs["human"][orth["human_entrez_gene_id"]]["source_sha256"],
                "query_sources_json": row["query_sources_json"],
                "orthology_record_id": orth["orthology_record_id"],
                "orthology_status": orth["mapping_cardinality"],
                "notes": "Explicit NCBI gene_orthologs relationship; no ortholog chosen when one-to-many.",
            })

    label_audit = build_label_audit(queries, crosswalk)
    direct_statuses = {"resolved_source_canonical", "resolved_source_alias", "ambiguous_source_alias"}
    nichenet_target_queries = [
        query for query in queries
        if any(source.get("source") == "nichenet_target_axis" for source in query["sources"])
    ]
    nichenet_target_statuses = []
    for query in nichenet_target_queries:
        rows = [
            row for row in crosswalk
            if row.get("query_symbol") == query["query_symbol"]
            and row.get("query_species_scope") == "mouse"
            and row.get("species") == "mouse"
            and row.get("mapping_status") in direct_statuses
        ]
        ids = {row.get("entrez_gene_id") for row in rows if row.get("entrez_gene_id")}
        nichenet_target_statuses.append(
            "ambiguous" if any(row.get("mapping_status") == "ambiguous_source_alias" for row in rows)
            else "unique" if len(ids) == 1 else "unresolved"
        )
    output.mkdir(parents=True)
    write_tsv(output / "gene_catalog.tsv", CATALOG_FIELDS, mouse_catalog_rows + human_catalog_rows)
    write_tsv(output / "gene_crosswalk.tsv", CROSSWALK_FIELDS, crosswalk)
    write_tsv(output / "gene_orthology.tsv", ORTHOLOGY_FIELDS, orthology_rows)
    write_tsv(output / "gene_label_coverage_audit.tsv", LABEL_AUDIT_FIELDS, label_audit)
    files = {}
    for path in (output / "gene_catalog.tsv", output / "gene_crosswalk.tsv", output / "gene_orthology.tsv", output / "gene_label_coverage_audit.tsv"):
        files[path.name] = {"sha256": sha256(path), "bytes": path.stat().st_size}
    source_inputs = []
    for name, path, url in (
        ("mouse_gene_info", args.mouse_gene_info.resolve(), "https://ftp.ncbi.nlm.nih.gov/gene/DATA/GENE_INFO/Mammalia/Mus_musculus.gene_info.gz"),
        ("human_gene_info", args.human_gene_info.resolve(), "https://ftp.ncbi.nlm.nih.gov/gene/DATA/GENE_INFO/Mammalia/Homo_sapiens.gene_info.gz"),
        ("gene_orthologs", args.gene_orthologs.resolve(), "https://ftp.ncbi.nlm.nih.gov/gene/DATA/gene_orthologs.gz"),
    ):
        source_inputs.append({"name": name, "url": url, "local_snapshot_path": str(path), "sha256": sha256(path), "bytes": path.stat().st_size})
    crosswalk_status_counts = dict(sorted(Counter(row["mapping_status"] for row in crosswalk).items()))
    crosswalk_species_counts = dict(sorted(Counter(row["species"] for row in crosswalk).items()))
    crosswalk_scope_counts = dict(sorted(Counter(row["query_species_scope"] for row in crosswalk).items()))
    orthology_cardinality_counts = dict(sorted(Counter(row["mapping_cardinality"] for row in orthology_rows).items()))
    manifest = {
        "schema_version": "gene_identifier_crosswalk_v1",
        "species": {name: {"tax_id": value["tax_id"]} for name, value in SPECIES.items()},
        "lookup_normalization": "Unicode-preserving casefold only; punctuation and aliases are not guessed or stripped.",
        "orthology_policy": "Retain explicit NCBI mouse-human orthology records; preserve one-to-many mappings without selecting arbitrarily.",
        "query_scope": "Committed mSCS TF-prior axes, neutral NicheNet mouse axes, mechanism graph gene symbols, active candidate-universe labels/components, and exact validated output-product labels.",
        "source_inputs": source_inputs,
        "counts": {
            "mouse_catalog_records": len(mouse_catalog_rows),
            "human_catalog_records": len(human_catalog_rows),
            "query_symbol_scope_records": len(queries),
            "crosswalk_rows": len(crosswalk),
            "crosswalk_resolved_rows": sum(row.get("mapping_status", "").startswith("resolved_") for row in crosswalk),
            "crosswalk_ambiguous_rows": sum(row.get("mapping_status", "").startswith("ambiguous_") for row in crosswalk),
            "crosswalk_unresolved_rows": sum(row.get("mapping_status", "").startswith("unresolved_") for row in crosswalk),
            "crosswalk_orthology_rows": sum(row.get("mapping_status", "").startswith("explicit_orthology_") for row in crosswalk),
            "orthology_rows": len(orthology_rows),
            "crosswalk_by_mapping_status": crosswalk_status_counts,
            "crosswalk_by_species": crosswalk_species_counts,
            "crosswalk_by_query_species_scope": crosswalk_scope_counts,
            "orthology_by_mapping_cardinality": orthology_cardinality_counts,
            "active_release_label_audit_rows": len(label_audit),
            "active_release_output_product_labels_total": sum(row["label_kind"] == "validated_output_product_label" for row in label_audit),
            "active_release_output_product_labels_mouse_unique": sum(row["label_kind"] == "validated_output_product_label" and row["mouse_mapping_status"] == "uniquely_mapped_source_gene" for row in label_audit),
            "active_release_output_product_labels_mouse_ambiguous": sum(row["label_kind"] == "validated_output_product_label" and row["mouse_mapping_status"] in {"ambiguous_source_alias", "multiple_source_mappings"} for row in label_audit),
            "active_release_output_product_labels_mouse_unresolved": sum(row["label_kind"] == "validated_output_product_label" and row["mouse_mapping_status"] == "unresolved_source_symbol" for row in label_audit),
            "active_release_candidate_labels_total": sum(row["label_kind"] == "candidate_universe_label" for row in label_audit),
            "active_release_candidate_components_total": sum(row["label_kind"] == "candidate_component_label" for row in label_audit),
            "nichenet_target_ids_total": len(nichenet_target_queries),
            "nichenet_target_ids_mouse_unique": nichenet_target_statuses.count("unique"),
            "nichenet_target_ids_mouse_ambiguous": nichenet_target_statuses.count("ambiguous"),
            "nichenet_target_ids_mouse_unresolved": nichenet_target_statuses.count("unresolved"),
        },
        "files": files,
        "release_input": {"release_path": str(release), "release_id": json.loads((release / "release_manifest.json").read_text())["release_id"]},
        "limitations": [
            "The crosswalk does not infer identity from capitalization, punctuation, substring matches, or symbol similarity.",
            "Unresolved and ambiguous aliases remain explicitly represented; downstream consumers must not choose among ambiguous rows.",
            "The raw NCBI snapshots are checksum-pinned references and are not copied into the Git release.",
        ],
    }
    (output / "gene_identifier_crosswalk_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output_dir": str(output), "counts": manifest["counts"], "files": files}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
