#!/usr/bin/env python3
"""Build the current Module 22B materialization stage from the registers.

Only exportable ``target_gene`` rows with an explicit human or mouse species
context are staged.  Program, phenotype, unresolved, no-evidence-boundary,
and blank-species rows remain in the registers and are reported as excluded.
The stage preserves database-curated provenance through external record keys;
it does not infer upstream TF activation or perform a database write.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
DEFAULT_OUTPUT = ROOT / "work/module22b_consolidation/materialization_round_register_2026_09_03"

OUTPUT_FIELDS = [
    "materialization_id", "module", "species", "tf_symbol", "target_symbol",
    "relation_type", "effect_polarity", "canonical_confidence_tier",
    "membership_basis", "membership_status", "export_priority", "evidence_status",
    "support_kind", "primary_pmids", "corroborating_pmids", "external_record_keys",
    "source_registries", "tf_entity_ids", "target_entity_ids",
    "tf_frozen_match_status", "target_frozen_match_status", "tf_role_present",
    "target_role_present", "cell_type_context", "stimulus_context", "limitations",
    "notes", "source_artifacts",
]

PMID_RE = re.compile(r"(?:\bPMID\s*[: ]\s*|pubmed\.ncbi\.nlm\.nih\.gov/)(\d{7,9})\b", re.I)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--edge-register", type=Path, default=EDGE_PATH)
    parser.add_argument("--evidence-register", type=Path, default=EVIDENCE_PATH)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def unique_tokens(values: list[str]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        for token in re.split(r"[;,]", value or ""):
            token = token.strip()
            if token and token not in {"NA", "null", "\\N", "none"} and token not in seen:
                seen.add(token)
                result.append(token)
    return result


def join_unique(values: list[str]) -> str:
    return ";".join(unique_tokens(values))


def pmids(evidence_rows: list[dict[str, str]]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for evidence in evidence_rows:
        text = " ".join(evidence.get(field, "") for field in ("source_locator", "citation_note", "evidence_summary"))
        matches = list(PMID_RE.finditer(text))
        explicit = re.search(r"public_reference_pmids=([0-9; ]+)", text, re.I)
        if explicit:
            matches.extend(re.finditer(r"(?<!\d)(\d{7,9})(?!\d)", explicit.group(1)))
        if not matches and all(token.strip().isdigit() for token in re.split(r"[;,]", text) if token.strip()):
            matches = list(re.finditer(r"(?<!\d)(\d{7,9})(?!\d)", text))
        for match in matches:
            if match.group(1) not in seen:
                seen.add(match.group(1))
                result.append(match.group(1))
    return result


def field_from_notes(evidence_rows: list[dict[str, str]], name: str) -> list[str]:
    result: list[str] = []
    for evidence in evidence_rows:
        for note in (evidence.get("citation_note", ""), evidence.get("evidence_summary", "")):
            if name == "external_record_keys":
                match = re.search(
                    r"(?:external_record_keys|external_records)=([^;]+(?:;[^;]+)*?)(?:;\s*(?:reference_count|public_reference_pmids)=|$)",
                    note,
                    re.I,
                )
            elif name == "source_registries":
                match = re.search(
                    r"(?:source_registries|registries)=([^;]+(?:;[^;]+)*?)(?:;\s*(?:external_record_keys|external_records|dorothea_levels)=|$)",
                    note,
                    re.I,
                )
            else:
                match = re.search(rf"{re.escape(name)}=([^;]+)", note)
            if match:
                result.extend(unique_tokens([match.group(1)]))
    return result


def normalize_effect(edge: dict[str, str], evidence_rows: list[dict[str, str]]) -> str:
    text = " ".join(
        [edge.get("relation_type", ""), edge.get("consolidation_note", "")]
        + [evidence.get("evidence_summary", "") for evidence in evidence_rows]
        + [evidence.get("citation_note", "") for evidence in evidence_rows]
    ).casefold()
    activating = any(token in text for token in ("activat", "induces", "induction", "positive"))
    repressing = any(token in text for token in ("repress", "inhibit", "negative"))
    if activating and repressing:
        return "context_dependent"
    if activating:
        return "activating_target"
    if repressing:
        return "repressing_target"
    return "unknown"


def main() -> int:
    args = parse_args()
    edges = read_tsv(args.edge_register)
    evidence = read_tsv(args.evidence_register)
    evidence_by_edge: dict[str, list[dict[str, str]]] = defaultdict(list)
    for evidence_row in evidence:
        for edge_id in evidence_row.get("b_edge_ids", "").split(";"):
            if edge_id.strip():
                evidence_by_edge[edge_id.strip()].append(evidence_row)

    target_gene = [
        edge for edge in edges
        if edge.get("pathway_name") == "target_gene" and edge.get("exportable") == "true"
    ]
    included = [edge for edge in target_gene if edge.get("species_context") in {"human", "mouse"}]
    if not included:
        raise SystemExit("no human or mouse exportable target-gene rows found")

    rows: list[dict[str, str]] = []
    for index, edge in enumerate(
        sorted(included, key=lambda row: (row["species_context"], row["source_entity"].casefold(), row["target_entity"].casefold(), row["b_edge_id"])),
        start=1,
    ):
        linked = evidence_by_edge.get(edge["b_edge_id"], [])
        if not linked:
            raise SystemExit(f"{edge['b_edge_id']}: exportable target-gene edge has no evidence")
        primary_pmids = pmids(linked)
        external_keys = field_from_notes(linked, "external_record_keys")
        source_registries = field_from_notes(linked, "source_registries")
        database_only = any(evidence.get("source_kind") == "database_curated" for evidence in linked)
        support_kinds = unique_tokens([evidence.get("support_kind", "") for evidence in linked])
        support_kind = "database_curated" if database_only and not primary_pmids else (
            "primary_experiment" if "primary_experiment" in support_kinds else (support_kinds[0] if support_kinds else "review_statement")
        )
        source_confidences = unique_tokens([evidence.get("confidence_tier", "") for evidence in linked] + [edge.get("confidence_tier", "")])
        limitations = join_unique([edge.get("context_scope", "")] + [evidence.get("limitations", "") for evidence in linked])
        evidence_ids = join_unique([evidence.get("b_evidence_id", "") for evidence in linked])
        source_kind_text = join_unique([evidence.get("source_kind", "") for evidence in linked])
        notes = (
            f"Register edge {edge['b_edge_id']}; register evidence {evidence_ids}; "
            f"source kinds={source_kind_text}; source confidence tiers={';'.join(source_confidences) or 'unspecified'}. "
            "Canonical materializer confidence is normalized to medium; source-register confidence and limitations remain in this stage. "
            "TF-target membership does not imply upstream ligand activation."
        )
        if database_only:
            notes += " Database-curated support is retained as inferred regulatory evidence and does not prove direct DNA binding."
        rows.append({
            "materialization_id": f"M22B-PROM-{index:06d}",
            "module": "22B",
            "species": edge["species_context"],
            "tf_symbol": edge["source_entity"],
            "target_symbol": edge["target_entity"],
            "relation_type": "regulates_target_gene",
            "effect_polarity": normalize_effect(edge, linked),
            "canonical_confidence_tier": "medium",
            "membership_basis": "inferred_regulatory",
            "membership_status": "supported",
            "export_priority": "medium",
            "evidence_status": "register_promoted",
            "support_kind": support_kind,
            "primary_pmids": ";".join(primary_pmids),
            "corroborating_pmids": "",
            "external_record_keys": ";".join(external_keys),
            "source_registries": ";".join(source_registries),
            "tf_entity_ids": "",
            "target_entity_ids": "",
            "tf_frozen_match_status": "",
            "target_frozen_match_status": "",
            "tf_role_present": "",
            "target_role_present": "",
            "cell_type_context": edge.get("cell_type_context", ""),
            "stimulus_context": edge.get("context_scope", ""),
            "limitations": limitations,
            "notes": notes,
            "source_artifacts": "work/module_b_consolidation/module22b/module22b_edge_register.tsv;work/module_b_consolidation/module22b/module22b_evidence_register.tsv",
        })

    keys = [(row["species"], row["tf_symbol"].casefold(), row["target_symbol"].casefold()) for row in rows]
    if len(keys) != len(set(keys)):
        raise SystemExit("duplicate species/TF/target key in materialization stage")
    if any(not row["primary_pmids"] and not row["external_record_keys"] for row in rows):
        raise SystemExit("materialization row has neither primary PMID nor external record key")
    if any(not row["tf_symbol"] or not row["target_symbol"] or row["tf_symbol"].casefold() == row["target_symbol"].casefold() for row in rows):
        raise SystemExit("invalid target-gene endpoint in materialization stage")

    stage_path = args.output_dir / "module22b_promoted_pairs.tsv"
    manifest_path = args.output_dir / "module22b_materialization_manifest.json"
    write_tsv(stage_path, rows)
    manifest = {
        "materialization_version": "module22b-register-materialization-2026-09-03",
        "module": "22B",
        "edge_register": str(args.edge_register),
        "evidence_register": str(args.evidence_register),
        "input_edge_rows": len(edges),
        "input_evidence_rows": len(evidence),
        "exportable_target_gene_rows": len(target_gene),
        "included_rows": len(rows),
        "unique_promoted_pairs": len(rows),
        "excluded_blank_species_target_gene_rows": sum(1 for edge in target_gene if not edge.get("species_context")),
        "excluded_non_target_gene_rows": len(edges) - len(target_gene),
        "included_by_species": dict(sorted(Counter(row["species"] for row in rows).items())),
        "included_by_source_confidence": dict(sorted(Counter(edge.get("confidence_tier", "") for edge in included).items())),
        "included_by_support_kind": dict(sorted(Counter(row["support_kind"] for row in rows).items())),
        "rows_with_primary_pmids": sum(bool(row["primary_pmids"]) for row in rows),
        "rows_with_external_record_keys": sum(bool(row["external_record_keys"]) for row in rows),
        "canonical_database_write_performed": False,
        "upstream_tf_activation_inferred": False,
        "notes": (
            "This stage consumes the current Module 22B working registers. "
            "Blank-species target-gene rows remain register evidence but are not "
            "materialized because the canonical write requires an explicit species."
        ),
    }
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
