#!/usr/bin/env python3
"""Build a provenance-preserving expansion of the public TF candidate union.

This produces a staging/discovery artifact only.  It does not write to
PostgreSQL or promote any TF-target assertion into the canonical graph.

The artifact keeps three provenance levels separate:

* primary snapshot records (TRRUST and the existing OmniPath/DoRothEA export),
* reported contributor labels embedded in the OmniPath/DoRothEA records, and
* identity/profile catalogs (Lambert human TFs, AnimalTFDB3 fallback lists,
  JASPAR CORE profiles, and TFLink gateway summaries).

TFLink's GMT files are intentionally summarized at the TF level here.  GMT
does not retain the detailed source database, assay, and PMID columns that are
required for pair-level evidence review.  Its raw files remain registered and
its TF/target counts are used for candidate discovery, but the summary rows
are not treated as pair-level corroboration.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable, Mapping


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EXISTING = ROOT / "data/processed/public_tf_union_v1"
DEFAULT_IDENTITY = ROOT / "data/raw/public_database_snapshots/tf_identity_intake_v1"
DEFAULT_EXPANSION = ROOT / "data/raw/public_database_snapshots/tf_union_expansion_v1"
DEFAULT_OUTPUT = ROOT / "data/processed/public_tf_union_expansion_v1"

REGISTRY_FIELDS = [
    "source_registry", "source_version", "species_scope", "retrieval_date",
    "source_url", "snapshot_path", "snapshot_sha256", "resource_class",
    "provenance_role", "independence_status", "upstream_version", "notes",
]

CONTRIBUTOR_FIELDS = [
    "contributor_key", "raw_source_label", "source_family", "aggregation_layer",
    "source_url", "provenance_status", "independent_snapshot", "reported_by",
    "reported_record_count", "reported_tf_species_count", "reported_pair_count",
    "notes",
]

IDENTITY_FIELDS = [
    "identity_record_key", "species_scope", "source_registry", "source_version",
    "source_record_id", "raw_symbol", "normalized_symbol", "normalized_symbol_key",
    "identity_decision", "candidate_class", "evidence_kind", "source_locator",
    "raw_record_sha256", "raw_payload", "provenance_status", "notes",
]

TF_LINK_SUMMARY_FIELDS = [
    "species_scope", "source_registry", "source_version", "source_record_id",
    "raw_tf_symbol", "normalized_tf_symbol", "normalized_tf_symbol_key",
    "tf_uniprot_id", "target_count", "source_locator", "raw_record_sha256",
    "provenance_status", "notes",
]

PAIR_FIELDS = [
    "pair_record_key", "source_registry", "source_version", "species_scope",
    "source_record_id", "raw_record_id", "raw_record_sha256", "raw_tf_symbol",
    "raw_target_symbol", "normalized_tf_symbol", "normalized_tf_symbol_key",
    "normalized_target_symbol", "normalized_target_symbol_key", "effect_polarity",
    "relationship_class", "evidence_basis", "reference_pmids", "source_locator",
    "provenance_status", "independence_status", "limitations",
]

CANDIDATE_FIELDS = [
    "candidate_key", "species_scope", "tf_symbol", "tf_key", "source_registries",
    "source_versions", "reported_contributor_labels", "identity_source_count",
    "regulon_record_count", "records_with_reference", "unique_reference_pmids",
    "catalog_profile_count", "tflink_target_count", "evidence_kinds",
    "independence_statuses", "candidate_class", "review_status", "notes",
]

PMID_RE = re.compile(r"(?<!\d)(\d{5,9})(?!\d)")
SIMPLE_SYMBOL_RE = re.compile(r"^[A-Za-z][A-Za-z0-9._-]*$")

CONTRIBUTOR_URLS = {
    "TRRUST": "https://www.grnpedia.org/trrust/",
    "DoRothEA": "https://saezlab.github.io/dorothea/",
    "JASPAR": "https://jaspar2026.elixir.no/",
    "ReMap": "https://remap.univ-amu.fr/",
    "RegNetwork": "https://regnetworkweb.org/",
    "TRED": "https://rulai.cshl.edu/TRED/",
    "HTRIdb": "https://htriadb.ugent.be/",
    "ORegAnno": "https://www.oreganno.org/",
    "SIGNOR": "https://signor.uniroma2.it/",
    "IntAct": "https://www.ebi.ac.uk/intact/",
    "ENCODE": "https://www.encodeproject.org/",
    "PAZAR": "https://pazar.info/",
    "HOCOMOCO": "https://hocomoco11.autosome.org/",
    "TFactS": "https://www.tfacts.org/",
    "FANTOM4": "https://fantom.gsc.riken.jp/4/",
    "KEGG-MEDICUS": "https://www.kegg.jp/kegg/medicus/",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: Iterable[Mapping[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def normalize_symbol(value: str | None) -> tuple[str, str, str, str]:
    raw = (value or "").strip()
    if not raw or raw in {r"\N", "NULL", "null"}:
        return "", "", "empty_unresolved", "Empty symbol."
    if not SIMPLE_SYMBOL_RE.fullmatch(raw) or any(token in raw for token in ("::", "/", "|", ";", "+", ",")):
        return "", "", "composite_unresolved", "Composite or non-simple label retained without splitting."
    return raw, raw.casefold(), "normalized_exact", "Trimmed simple symbol; no alias expansion applied."


def pmids(value: str | None) -> set[str]:
    return set(PMID_RE.findall(value or ""))


def null_text(value: str | None) -> str:
    text = (value or "").strip()
    return "" if text in {r"\N", "NULL", "null"} else text


def contributor_parts(raw_label: str) -> tuple[str, str]:
    label = raw_label.strip()
    for suffix in ("_DoRothEA-A", "_DoRothEA", "_CollecTRI2", "_CollecTRI"):
        if label.endswith(suffix):
            return label[: -len(suffix)], suffix[1:]
    return label, "direct_or_unqualified"


def source_registry_row(
    source_registry: str,
    source_version: str,
    species_scope: str,
    retrieval_date: str,
    source_url: str,
    snapshot_path: Path,
    resource_class: str,
    provenance_role: str,
    independence_status: str,
    upstream_version: str,
    notes: str,
) -> dict[str, object]:
    return {
        "source_registry": source_registry,
        "source_version": source_version,
        "species_scope": species_scope,
        "retrieval_date": retrieval_date,
        "source_url": source_url,
        "snapshot_path": str(snapshot_path),
        "snapshot_sha256": sha256_file(snapshot_path),
        "resource_class": resource_class,
        "provenance_role": provenance_role,
        "independence_status": independence_status,
        "upstream_version": upstream_version,
        "notes": notes,
    }


def existing_registry_rows(existing_dir: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for row in read_tsv(existing_dir / "source_registry.tsv"):
        rows.append({
            "source_registry": row["source_registry"],
            "source_version": row["source_version"],
            "species_scope": row["species_context"],
            "retrieval_date": row["retrieval_date"],
            "source_url": row["source_url"],
            "snapshot_path": row["snapshot_path"],
            "snapshot_sha256": row["snapshot_sha256"],
            "resource_class": row["resource_class"],
            "provenance_role": "primary_snapshot" if row["source_registry"] == "TRRUST" else "aggregated_snapshot",
            "independence_status": "repository_snapshot" if row["source_registry"] == "TRRUST" else "integrated_aggregator_snapshot",
            "upstream_version": row.get("upstream_version", ""),
            "notes": row.get("notes", ""),
        })
    return rows


def add_identity(
    store: dict[str, dict[str, object]],
    *,
    species_scope: str,
    source_registry: str,
    source_version: str,
    source_record_id: str,
    raw_symbol: str,
    candidate_class: str,
    evidence_kind: str,
    source_locator: str,
    raw_record_sha256: str,
    raw_payload: object,
    provenance_status: str,
    notes: str,
) -> None:
    display, key, decision, reason = normalize_symbol(raw_symbol)
    identity_record_key = "|".join((source_registry, source_version, species_scope, source_record_id, raw_symbol))
    store[identity_record_key] = {
        "identity_record_key": identity_record_key,
        "species_scope": species_scope,
        "source_registry": source_registry,
        "source_version": source_version,
        "source_record_id": source_record_id,
        "raw_symbol": raw_symbol,
        "normalized_symbol": display,
        "normalized_symbol_key": key,
        "identity_decision": decision,
        "candidate_class": candidate_class,
        "evidence_kind": evidence_kind,
        "source_locator": source_locator,
        "raw_record_sha256": raw_record_sha256,
        "raw_payload": json.dumps(raw_payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")),
        "provenance_status": provenance_status,
        "notes": f"{reason} {notes}".strip(),
    }


def existing_pairs_and_identities(
    existing_dir: Path,
    identity_rows: dict[str, dict[str, object]],
    pair_rows: list[dict[str, object]],
    contributor_links: list[dict[str, object]],
    contributor_counts: Counter,
) -> None:
    records = read_tsv(existing_dir / "source_records.tsv")
    for record in records:
        species = record["species_context"]
        registry = record["source_registry"]
        version = record["source_version"]
        source_id = record["external_record_id"]
        tf = record["source_tf_symbol"]
        target = record["source_target_symbol"]
        add_identity(
            identity_rows,
            species_scope=species,
            source_registry=registry,
            source_version=version,
            source_record_id=source_id,
            raw_symbol=tf,
            candidate_class="regulon_tf",
            evidence_kind="tf_regulon_record",
            source_locator=record["source_locator"],
            raw_record_sha256=record["raw_record_sha256"],
            raw_payload={"tf": tf, "target": target},
            provenance_status="source_record",
            notes="TF identity observed in an imported source-specific TF-target assertion.",
        )
        contributor_labels = [x.strip() for x in (record.get("external_sources") or "").split(";") if x.strip()]
        for label in contributor_labels:
            family, layer = contributor_parts(label)
            contributor_key = f"{family}|{layer}"
            contributor_links.append({
                "contributor_key": contributor_key,
                "external_record_key": record["external_record_key"],
                "source_registry": registry,
                "source_version": version,
                "species_scope": species,
                "raw_source_label": label,
                "source_family": family,
                "aggregation_layer": layer,
                "source_locator": record["source_locator"],
                "provenance_status": "reported_by_aggregator",
                "independent_snapshot": "false",
                "reference_pmids": ";".join(sorted(pmids(record.get("reference_text")))),
                "notes": "Contributor label is preserved from the OmniPath/DoRothEA raw row; it is not an independent snapshot in this intake.",
            })
            contributor_counts[contributor_key] += 1
        pair_rows.append({
            "pair_record_key": record["external_record_key"],
            "source_registry": registry,
            "source_version": version,
            "species_scope": species,
            "source_record_id": source_id,
            "raw_record_id": record["raw_record_id"],
            "raw_record_sha256": record["raw_record_sha256"],
            "raw_tf_symbol": tf,
            "raw_target_symbol": target,
            "normalized_tf_symbol": null_text(record.get("tf_normalized_symbol", "")),
            "normalized_tf_symbol_key": null_text(record.get("tf_normalized_symbol_key", "")),
            "normalized_target_symbol": null_text(record.get("target_normalized_symbol", "")),
            "normalized_target_symbol_key": null_text(record.get("target_normalized_symbol_key", "")),
            "effect_polarity": record.get("effect_polarity", "unknown"),
            "relationship_class": record.get("relationship_class", "unresolved"),
            "evidence_basis": record.get("evidence_basis", "database_curated"),
            "reference_pmids": record.get("reference_pmids", ""),
            "source_locator": record.get("source_locator", ""),
            "provenance_status": "source_record",
            "independence_status": "repository_snapshot" if registry == "TRRUST" else "integrated_aggregator_snapshot",
            "limitations": "Existing public TF-union assertion; database membership remains a review lead until exact-pair literature evidence is checked.",
        })


def parse_lambert(path: Path, identity_rows: dict[str, dict[str, object]]) -> int:
    count = 0
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        symbol = line.strip()
        if not symbol:
            continue
        add_identity(
            identity_rows,
            species_scope="human",
            source_registry="Lambert_HumanTFs",
            source_version="Lambert_v1.01",
            source_record_id=f"line:{line_number}",
            raw_symbol=symbol,
            candidate_class="tf_catalog",
            evidence_kind="expert_curated_tf_identity",
            source_locator="https://humantfs.ccbr.utoronto.ca/download/v_1.01/TF_names_v_1.01.txt",
            raw_record_sha256=sha256_text(symbol),
            raw_payload={"tf_name": symbol},
            provenance_status="primary_identity_catalog",
            notes="Lambert et al. human TF list; identity/catalog evidence only, not a TF-target assertion.",
        )
        count += 1
    return count


def parse_animaltfdb(path: Path, species_scope: str, identity_rows: dict[str, dict[str, object]]) -> int:
    count = 0
    source_url = {
        "human": "https://raw.githubusercontent.com/GuoBioinfoLab/AnimalTFDB3/master/AnimalTFDB3/static/AnimalTFDB3/download/Homo_sapiens_TF",
        "mouse": "https://raw.githubusercontent.com/GuoBioinfoLab/AnimalTFDB3/master/AnimalTFDB3/static/AnimalTFDB3/download/Mus_musculus_TF",
    }[species_scope]
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for line_number, row in enumerate(reader, start=2):
            symbol = (row.get("Symbol") or "").strip()
            if not symbol:
                continue
            raw_text = "\t".join(row.get(field, "") for field in reader.fieldnames or [])
            add_identity(
                identity_rows,
                species_scope=species_scope,
                source_registry="AnimalTFDB3",
                source_version="AnimalTFDB3_git_snapshot",
                source_record_id=f"line:{line_number}",
                raw_symbol=symbol,
                candidate_class="tf_catalog",
                evidence_kind="domain_curated_tf_identity",
                source_locator=source_url,
                raw_record_sha256=sha256_text(raw_text),
                raw_payload=row,
                provenance_status="primary_identity_catalog_fallback",
                notes="AnimalTFDB3 fallback snapshot used because the AnimalTFDB4 endpoint was unavailable; identity/catalog evidence only.",
            )
            count += 1
    return count


def parse_jaspar(path: Path, identity_rows: dict[str, dict[str, object]]) -> int:
    count = 0
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.startswith(">"):
            continue
        fields = line[1:].split("\t", 1)
        matrix_id = fields[0].strip()
        name = fields[1].strip() if len(fields) > 1 else ""
        if not name:
            continue
        add_identity(
            identity_rows,
            species_scope="vertebrates",
            source_registry="JASPAR_CORE",
            source_version="JASPAR2026_CORE_vertebrates_nonredundant",
            source_record_id=matrix_id,
            raw_symbol=name,
            candidate_class="binding_profile",
            evidence_kind="experimentally_derived_binding_profile",
            source_locator="https://jaspar2026.elixir.no/download/data/2026/CORE/JASPAR2026_CORE_vertebrates_non-redundant_pfms_jaspar.txt#" + matrix_id,
            raw_record_sha256=sha256_text(line),
            raw_payload={"matrix_id": matrix_id, "name": name, "header_line": line_number},
            provenance_status="primary_binding_profile_catalog",
            notes="JASPAR profile scope is vertebrates; profile presence does not establish occupancy, regulatory direction, or species-specific target regulation.",
        )
        count += 1
    return count


def parse_tflink(path: Path, species_scope: str, summary_rows: list[dict[str, object]], identity_rows: dict[str, dict[str, object]]) -> int:
    count = 0
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            fields = line.rstrip("\n").split("\t")
            if len(fields) < 2:
                continue
            raw_tf = fields[0].strip()
            tf_uniprot = fields[1].strip()
            targets = [target.strip() for target in fields[2:] if target.strip()]
            if not raw_tf:
                continue
            row_hash = sha256_text(line.rstrip("\n"))
            source_record_id = f"tflink:{species_scope}:{line_number:06d}:{row_hash[:12]}"
            display, key, _, _ = normalize_symbol(raw_tf)
            source_locator = "https://tflink.net/download/#interaction-gmt"
            summary_rows.append({
                "species_scope": species_scope,
                "source_registry": "TFLink",
                "source_version": "TFLink_v1.0_snapshot",
                "source_record_id": source_record_id,
                "raw_tf_symbol": raw_tf,
                "normalized_tf_symbol": display,
                "normalized_tf_symbol_key": key,
                "tf_uniprot_id": tf_uniprot,
                "target_count": len(targets),
                "source_locator": source_locator,
                "raw_record_sha256": row_hash,
                "provenance_status": "aggregated_gateway_record",
                "notes": "GMT preserves TF identifiers and target membership counts but not the detailed source database, assay, or PMID per target; not pair-level corroboration.",
            })
            add_identity(
                identity_rows,
                species_scope=species_scope,
                source_registry="TFLink",
                source_version="TFLink_v1.0_snapshot",
                source_record_id=source_record_id,
                raw_symbol=raw_tf,
                candidate_class="regulon_tf",
                evidence_kind="aggregated_tf_gateway_identity",
                source_locator=source_locator,
                raw_record_sha256=row_hash,
                raw_payload={"tf": raw_tf, "uniprot": tf_uniprot, "target_count": len(targets)},
                provenance_status="aggregated_gateway_record",
                notes="TFLink gateway summary only; detailed target-level provenance must be acquired from the TSV interaction table before evidence promotion.",
            )
            count += 1
    return count


def make_contributor_registry(
    contributor_counts: Counter,
    contributor_links: list[dict[str, object]],
) -> list[dict[str, object]]:
    tf_counts: Counter = Counter()
    pair_counts: Counter = Counter()
    seen_tf: defaultdict[str, set[tuple[str, str]]] = defaultdict(set)
    seen_pair: defaultdict[str, set[tuple[str, str, str]]] = defaultdict(set)
    for row in contributor_links:
        key = row["contributor_key"]
        record = row["external_record_key"]
        species = row["species_scope"]
        tf = record.split("|")[-1] if "|" in record else record
        # The source record key does not expose the normalized TF reliably;
        # record and pair counts remain exact while TF counts are populated by
        # the candidate aggregation below when possible.
        pair_counts[key] += 1
        seen_pair[key].add((species, record, row["raw_source_label"]))
    rows: list[dict[str, object]] = []
    for key in sorted(contributor_counts):
        family, layer = key.split("|", 1)
        rows.append({
            "contributor_key": key,
            "raw_source_label": next(row["raw_source_label"] for row in contributor_links if row["contributor_key"] == key),
            "source_family": family,
            "aggregation_layer": layer,
            "source_url": CONTRIBUTOR_URLS.get(family, "https://omnipathdb.org/"),
            "provenance_status": "reported_by_aggregator",
            "independent_snapshot": "false",
            "reported_by": "OmniPath_DoRothEA",
            "reported_record_count": len(seen_pair[key]),
            "reported_tf_species_count": "",
            "reported_pair_count": len(seen_pair[key]),
            "notes": "This is a contributor label reported inside an OmniPath/DoRothEA record; it is not an independently retrieved snapshot in this expansion.",
        })
    return rows


def aggregate_candidates(
    identity_rows: list[dict[str, object]],
    pair_rows: list[dict[str, object]],
    tflink_rows: list[dict[str, object]],
    contributor_links: list[dict[str, object]],
) -> list[dict[str, object]]:
    groups: dict[tuple[str, str], dict[str, object]] = {}

    def group_for(species: str, key: str, symbol: str) -> dict[str, object]:
        group_key = (species, key)
        if group_key not in groups:
            groups[group_key] = {
                "candidate_key": f"{species}|{key}",
                "species_scope": species,
                "tf_symbol": symbol,
                "tf_key": key,
                "source_registries": set(),
                "source_versions": set(),
                "reported_contributor_labels": set(),
                "identity_sources": set(),
                "regulon_record_count": 0,
                "records_with_reference": 0,
                "unique_reference_pmids": set(),
                "catalog_profile_count": 0,
                "tflink_target_count": 0,
                "evidence_kinds": set(),
                "independence_statuses": set(),
                "candidate_class": set(),
                "notes": set(),
            }
        return groups[group_key]

    for row in identity_rows:
        key = str(row.get("normalized_symbol_key", ""))
        symbol = str(row.get("normalized_symbol", ""))
        if not key or not symbol:
            continue
        group = group_for(str(row["species_scope"]), key, symbol)
        group["source_registries"].add(str(row["source_registry"]))
        group["source_versions"].add(str(row["source_version"]))
        group["identity_sources"].add(str(row["source_registry"]))
        group["evidence_kinds"].add(str(row["evidence_kind"]))
        group["candidate_class"].add(str(row["candidate_class"]))
        if row["candidate_class"] == "binding_profile":
            group["catalog_profile_count"] += 1
        group["independence_statuses"].add(
            "integrated_aggregator_snapshot" if row["source_registry"] in {"OmniPath_DoRothEA", "TFLink"} else
            "primary_binding_profile_catalog" if row["source_registry"] == "JASPAR_CORE" else
            "primary_identity_catalog"
        )

    pair_tf_by_record: dict[str, tuple[str, str]] = {}
    for row in pair_rows:
        key = str(row.get("normalized_tf_symbol_key", ""))
        symbol = str(row.get("normalized_tf_symbol", ""))
        if not key or not symbol:
            continue
        pair_tf_by_record[str(row["pair_record_key"])] = (str(row["species_scope"]), key)
        group = group_for(str(row["species_scope"]), key, symbol)
        group["source_registries"].add(str(row["source_registry"]))
        group["source_versions"].add(str(row["source_version"]))
        group["regulon_record_count"] += 1
        reference_pmids = pmids(str(row.get("reference_pmids", "")))
        if reference_pmids:
            group["records_with_reference"] += 1
            group["unique_reference_pmids"].update(reference_pmids)
        group["evidence_kinds"].add("tf_regulon_record")
        group["candidate_class"].add("regulon_tf")
        group["independence_statuses"].add(str(row["independence_status"]))

    for row in contributor_links:
        pair_info = pair_tf_by_record.get(str(row["external_record_key"]))
        if not pair_info:
            continue
        species, key = pair_info
        group = groups[(species, key)]
        group["reported_contributor_labels"].add(str(row["raw_source_label"]))

    for row in tflink_rows:
        key = str(row.get("normalized_tf_symbol_key", ""))
        symbol = str(row.get("normalized_tf_symbol", ""))
        if not key or not symbol:
            continue
        group = group_for(str(row["species_scope"]), key, symbol)
        group["source_registries"].add("TFLink")
        group["source_versions"].add("TFLink_v1.0_snapshot")
        group["tflink_target_count"] += int(row["target_count"])
        group["evidence_kinds"].add("aggregated_tf_gateway_identity")
        group["candidate_class"].add("regulon_tf")
        group["independence_statuses"].add("integrated_aggregator_snapshot")
        group["notes"].add("TFLink target count is from GMT summary; target-level source/assay/PMID provenance is not available in this file.")

    output: list[dict[str, object]] = []
    for group in groups.values():
        classes = group["candidate_class"]
        candidate_class = "tf_identity_and_regulon" if {"tf_catalog", "regulon_tf"} <= classes else next(iter(classes))
        output.append({
            "candidate_key": group["candidate_key"],
            "species_scope": group["species_scope"],
            "tf_symbol": group["tf_symbol"],
            "tf_key": group["tf_key"],
            "source_registries": ";".join(sorted(group["source_registries"])),
            "source_versions": ";".join(sorted(group["source_versions"])),
            "reported_contributor_labels": ";".join(sorted(group["reported_contributor_labels"])),
            "identity_source_count": len(group["identity_sources"]),
            "regulon_record_count": group["regulon_record_count"],
            "records_with_reference": group["records_with_reference"],
            "unique_reference_pmids": len(group["unique_reference_pmids"]),
            "catalog_profile_count": group["catalog_profile_count"],
            "tflink_target_count": group["tflink_target_count"],
            "evidence_kinds": ";".join(sorted(group["evidence_kinds"])),
            "independence_statuses": ";".join(sorted(group["independence_statuses"])),
            "candidate_class": candidate_class,
            "review_status": "new_candidate",
            "notes": "; ".join(sorted(group["notes"])),
        })
    return sorted(output, key=lambda row: (row["species_scope"], row["tf_key"]))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--existing-dir", type=Path, default=DEFAULT_EXISTING)
    parser.add_argument("--identity-dir", type=Path, default=DEFAULT_IDENTITY)
    parser.add_argument("--expansion-dir", type=Path, default=DEFAULT_EXPANSION)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--retrieval-date", default="2026-08-26")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    registry_rows = existing_registry_rows(args.existing_dir)
    identity_rows: dict[str, dict[str, object]] = {}
    pair_rows: list[dict[str, object]] = []
    contributor_links: list[dict[str, object]] = []
    contributor_counts: Counter = Counter()
    tflink_rows: list[dict[str, object]] = []

    existing_pairs_and_identities(args.existing_dir, identity_rows, pair_rows, contributor_links, contributor_counts)

    lambert = args.identity_dir / "human_tfs_lambert_v1.01.txt"
    jaspar = args.identity_dir / "jaspar2026_core_vertebrates_nonredundant_pfms.jaspar"
    animal_human = args.expansion_dir / "animaltfdb3_human_tf.tsv"
    animal_mouse = args.expansion_dir / "animaltfdb3_mouse_tf.tsv"
    tflink_human = args.expansion_dir / "tflink_human_v1.0.gmt"
    tflink_mouse = args.expansion_dir / "tflink_mouse_v1.0.gmt"
    required = [lambert, jaspar, animal_human, animal_mouse, tflink_human, tflink_mouse]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        raise SystemExit("missing required snapshot(s): " + ", ".join(missing))

    registry_rows.extend([
        source_registry_row(
            "Lambert_HumanTFs", "Lambert_v1.01", "human", args.retrieval_date,
            "https://humantfs.ccbr.utoronto.ca/download/v_1.01/TF_names_v_1.01.txt", lambert,
            "tf_identity_catalog", "primary_identity_catalog", "repository_catalog",
            "Lambert et al. 2018, PMID 29425488", "Expert-curated human TF identity list; no target assertions.",
        ),
        source_registry_row(
            "AnimalTFDB3", "AnimalTFDB3_git_snapshot", "human", args.retrieval_date,
            "https://raw.githubusercontent.com/GuoBioinfoLab/AnimalTFDB3/master/AnimalTFDB3/static/AnimalTFDB3/download/Homo_sapiens_TF", animal_human,
            "tf_identity_catalog", "primary_identity_catalog_fallback", "repository_catalog",
            "AnimalTFDB3", "Fallback identity catalog; AnimalTFDB4 endpoint was unavailable during acquisition.",
        ),
        source_registry_row(
            "AnimalTFDB3", "AnimalTFDB3_git_snapshot", "mouse", args.retrieval_date,
            "https://raw.githubusercontent.com/GuoBioinfoLab/AnimalTFDB3/master/AnimalTFDB3/static/AnimalTFDB3/download/Mus_musculus_TF", animal_mouse,
            "tf_identity_catalog", "primary_identity_catalog_fallback", "repository_catalog",
            "AnimalTFDB3", "Fallback identity catalog; AnimalTFDB4 endpoint was unavailable during acquisition.",
        ),
        source_registry_row(
            "JASPAR_CORE", "JASPAR2026_CORE_vertebrates_nonredundant", "vertebrates", args.retrieval_date,
            "https://jaspar2026.elixir.no/download/data/2026/CORE/JASPAR2026_CORE_vertebrates_non-redundant_pfms_jaspar.txt", jaspar,
            "tf_binding_profile", "primary_binding_profile_catalog", "repository_catalog",
            "JASPAR 2026 release 11", "Vertebrate PFM profiles; not species-specific and not direct TF-target evidence.",
        ),
        source_registry_row(
            "TFLink", "TFLink_v1.0_snapshot", "human", args.retrieval_date,
            "https://tflink.net/download/", tflink_human,
            "tf_regulon", "aggregated_gateway_snapshot", "integrated_aggregator_snapshot",
            "TFLink downloadable gateway snapshot v1.0", "GMT summary used for TF discovery; detailed pair provenance is not retained in this file.",
        ),
        source_registry_row(
            "TFLink", "TFLink_v1.0_snapshot", "mouse", args.retrieval_date,
            "https://tflink.net/download/", tflink_mouse,
            "tf_regulon", "aggregated_gateway_snapshot", "integrated_aggregator_snapshot",
            "TFLink downloadable gateway snapshot v1.0", "GMT summary used for TF discovery; detailed pair provenance is not retained in this file.",
        ),
    ])

    counts = {
        "lambert_identity_rows": parse_lambert(lambert, identity_rows),
        "animal_tfdb3_human_identity_rows": parse_animaltfdb(animal_human, "human", identity_rows),
        "animal_tfdb3_mouse_identity_rows": parse_animaltfdb(animal_mouse, "mouse", identity_rows),
        "jaspar_profile_identity_rows": parse_jaspar(jaspar, identity_rows),
        "tflink_human_tf_summary_rows": parse_tflink(tflink_human, "human", tflink_rows, identity_rows),
        "tflink_mouse_tf_summary_rows": parse_tflink(tflink_mouse, "mouse", tflink_rows, identity_rows),
    }

    contributors = make_contributor_registry(contributor_counts, contributor_links)
    candidates = aggregate_candidates(list(identity_rows.values()), pair_rows, tflink_rows, contributor_links)

    write_tsv(args.output_dir / "source_registry.tsv", REGISTRY_FIELDS, sorted(registry_rows, key=lambda row: (row["source_registry"], row["species_scope"])))
    write_tsv(args.output_dir / "reported_contributor_registry.tsv", CONTRIBUTOR_FIELDS, contributors)
    write_tsv(args.output_dir / "reported_contributor_links.tsv", [
        "contributor_key", "external_record_key", "source_registry", "source_version", "species_scope",
        "raw_source_label", "source_family", "aggregation_layer", "source_locator", "provenance_status",
        "independent_snapshot", "reference_pmids", "notes",
    ], sorted(contributor_links, key=lambda row: (row["contributor_key"], row["external_record_key"])))
    write_tsv(args.output_dir / "tf_identity_records.tsv", IDENTITY_FIELDS, sorted(identity_rows.values(), key=lambda row: row["identity_record_key"]))
    write_tsv(args.output_dir / "tflink_tf_summary.tsv", TF_LINK_SUMMARY_FIELDS, sorted(tflink_rows, key=lambda row: (row["species_scope"], row["normalized_tf_symbol_key"])))
    write_tsv(args.output_dir / "tf_pair_records.tsv", PAIR_FIELDS, sorted(pair_rows, key=lambda row: row["pair_record_key"]))
    write_tsv(args.output_dir / "tf_candidate_union.tsv", CANDIDATE_FIELDS, candidates)

    manifest = {
        "integration_name": "public_tf_union_expansion_v1",
        "integration_status": "staging_discovery_only",
        "retrieval_date": args.retrieval_date,
        "scope": ["human", "mouse", "vertebrate_profile_scope"],
        "source_policy": {
            "primary_snapshot": "TRRUST and existing OmniPath/DoRothEA records remain source-specific and are copied with their original record keys.",
            "reported_contributors": "OmniPath/DoRothEA external_sources labels are decomposed into a link table, but remain marked reported_by_aggregator and independent_snapshot=false.",
            "identity_catalogs": "Lambert and AnimalTFDB expand the TF identity universe; JASPAR expands binding-profile coverage without creating TF-target edges.",
            "tflink": "TFLink GMT is retained as an aggregated gateway summary. Pair-level evidence is not created from GMT because its detailed source, assay, and PMID columns are absent.",
        },
        "counts": {
            **counts,
            "source_registry_rows": len(registry_rows),
            "reported_contributor_registry_rows": len(contributors),
            "reported_contributor_links": len(contributor_links),
            "tf_identity_records": len(identity_rows),
            "tf_pair_records": len(pair_rows),
            "tf_candidate_union_rows": len(candidates),
            "human_candidate_rows": sum(row["species_scope"] == "human" for row in candidates),
            "mouse_candidate_rows": sum(row["species_scope"] == "mouse" for row in candidates),
            "vertebrate_profile_candidate_rows": sum(row["species_scope"] == "vertebrates" for row in candidates),
        },
        "raw_snapshots": [
            {"path": str(path), "sha256": sha256_file(path)} for path in required
        ],
        "not_promoted": True,
        "notes": "This expansion does not change SignalingEntity, SignalingEdge, Regulon, or any canonical evidence table.",
    }
    (args.output_dir / "expansion_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (args.output_dir / "README.md").write_text(
        "# Public TF union expansion v1\n\n"
        "This is a staging/discovery artifact. It expands TF identity and source provenance without promoting any new canonical TF-target evidence.\n\n"
        "`tf_candidate_union.tsv` is the review inventory. `tf_identity_records.tsv` records where each TF identity/profile came from. `tf_pair_records.tsv` copies the existing source-specific pair assertions. `reported_contributor_links.tsv` preserves contributor labels reported inside OmniPath/DoRothEA records and explicitly marks them as non-independent. `tflink_tf_summary.tsv` records TFLink GMT TF-level counts only; it is not pair-level evidence.\n\n"
        "The release is intentionally separate from the frozen mechanism graph and must be reviewed before any promotion.\n",
        encoding="utf-8",
    )
    print(json.dumps(manifest["counts"], sort_keys=True))


if __name__ == "__main__":
    main()
