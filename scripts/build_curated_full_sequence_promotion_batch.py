#!/usr/bin/env python3
"""Reconcile the next all-ligand full-sequence promotion tranche.

The broad promotion generators identify exact ligand/receptor/intermediate/TF/
target signatures, but a legacy downstream queue can point at an evidence
record from an adjacent queue row.  This wrapper keeps only source-queue and
source-record pairs whose foreign-key relationship is internally consistent,
then rewrites the route summary as an explicit component composition.  It
does not assert a causal handoff or assign confidence.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path


LOCATOR_RE = re.compile(
    r"(?:PMID:[^;\s]+|PMCID:[^;\s]+|DOI:[^;\s]+|https?://[^;\s]+)",
    re.IGNORECASE,
)
ROUTE_ID_RE = re.compile(r"(?:LITEXP|GRAPHROUTE):\d{6}")


def read_tsv(path: Path) -> list[dict[str, str]]:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def split_values(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()]


def join_unique(*values: str) -> str:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        for item in split_values(value):
            if item and item not in seen:
                seen.add(item)
                result.append(item)
    return "; ".join(result)


def route_ids_from_chain(value: str) -> list[str]:
    return list(dict.fromkeys(ROUTE_ID_RE.findall(value or "")))


def route_component_rows(
    row: dict[str, str],
    routes_by_id: dict[str, dict[str, str]],
    routes: list[dict[str, str]],
) -> list[dict[str, str]]:
    selected: list[dict[str, str]] = []
    for route_id in route_ids_from_chain(row.get("source_chain_id", "")):
        route = routes_by_id.get(route_id)
        if route and route not in selected:
            selected.append(route)
    if selected:
        return selected

    # Target-promotion rows often retain a FULLSEQ candidate rather than the
    # route IDs used to build it.  Recover a bounded, exact-pair component set
    # without joining across other ligand/receptor identities.
    pair = (row.get("ligand_node_id", ""), row.get("receptor_node_id", ""))
    candidates = [
        route
        for route in routes
        if (route.get("ligand_node_id", ""), route.get("receptor_node_id", "")) == pair
        and route.get("source_queue_id", "") == row.get("source_queue_id", "")
        and any(
            route.get(field, "")
            and route.get(field, "") == row.get(field, "")
            for field in (
                "intracellular_continuation_node_id",
                "transcription_factor_node_id",
                "target_gene_node_id",
            )
        )
    ]
    return sorted(candidates, key=lambda route: route.get("route_evidence_id", ""))[:6]


def reconcile_rows(bundle: Path, rows: list[dict[str, str]]) -> tuple[list[dict[str, str]], dict[str, int]]:
    records = {row["record_id"]: row for row in read_tsv(bundle / "mechanism_downstream_evidence_records.tsv")}
    routes = read_tsv(bundle / "mechanism_signaling_route_evidence.tsv.gz")
    routes_by_id = {row["route_evidence_id"]: row for row in routes}
    output: list[dict[str, str]] = []
    skipped = {"source_record_queue_mismatch": 0, "missing_primary_locator": 0}

    for row in rows:
        record = records.get(row.get("source_evidence_record_id", ""), {})
        if (
            row.get("source_queue_id")
            and row.get("source_evidence_record_id")
            and record.get("source_queue_id") != row.get("source_queue_id")
        ):
            skipped["source_record_queue_mismatch"] += 1
            continue
        if not LOCATOR_RE.search(row.get("primary_locator", "")):
            skipped["missing_primary_locator"] += 1
            continue

        components = route_component_rows(row, routes_by_id, routes)
        component_ids = [component.get("route_evidence_id", "") for component in components if component.get("route_evidence_id")]
        component_records = [
            records[component["source_evidence_record_id"]]
            for component in components
            if component.get("source_evidence_record_id") in records
        ]
        component_locators = [
            locator
            for component in components
            for locator in LOCATOR_RE.findall(component.get("evidence_ids", ""))
        ]
        component_locators.extend(
            locator
            for component_record in component_records
            for locator in LOCATOR_RE.findall(component_record.get("source_locator", ""))
        )
        row["primary_locator"] = join_unique(row.get("primary_locator", ""), "; ".join(component_locators))
        record_ids = join_unique(
            row.get("source_evidence_record_id", ""),
            "; ".join(component.get("source_evidence_record_id", "") for component in components),
        )
        row["evidence_ids"] = join_unique(row.get("evidence_ids", ""), "; ".join(component_ids), record_ids)

        component_context = " | ".join(
            dict.fromkeys(
                record.get("evidence_summary", "").strip()
                for record in component_records
                if record.get("evidence_summary", "").strip()
            )
        )
        route_label = " > ".join(
            value
            for value in (
                row.get("ligand_label", ""),
                row.get("receptor_label", ""),
                row.get("intracellular_continuation_label", ""),
                row.get("transcription_factor_label", ""),
                row.get("target_gene_label", ""),
            )
            if value
        )
        row["evidence_summary"] = (
            f"Primary-locator-backed composed evidence route: {route_label}. "
            "The ligand/receptor, intracellular, transcription-factor, and target-gene layers are retained "
            "from exact ligand/receptor component records; no single source is asserted to demonstrate every "
            "handoff."
            + (f" Component source context: {component_context}" if component_context else "")
        )
        row["limitations"] = join_unique(
            row.get("limitations", ""),
            "Component studies may use different cell types, receptor-shared branches, or complementary assays; this row is plausibility evidence rather than an end-to-end primary experiment.",
            "Direct intracellular-to-TF and TF-to-target handoffs remain unasserted unless separately represented as graph evidence.",
        )
        row["citation_note"] = join_unique(
            row.get("citation_note", ""),
            f"Reconciled component route records: {', '.join(component_ids) if component_ids else 'exact-pair route records'}; source evidence records: {record_ids}.",
        )
        row["route_linkage_status"] = join_unique(
            row.get("route_linkage_status", ""),
            "curation:source_record_queue_consistent",
            "curation:component_evidence_summary_reconciled",
        )
        row["source_scope"] = join_unique(row.get("source_scope", ""), "strict_component_provenance_reconciled")
        output.append(row)

    return output, skipped


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    bundle = args.bundle.resolve()
    with tempfile.TemporaryDirectory(prefix="mSCIdblit_next_full_sequence_") as temp_name:
        candidate_path = Path(temp_name) / "promotion.json"
        subprocess.run(
            [
                sys.executable,
                str(Path(__file__).with_name("build_all_ligand_full_sequence_promotion_batch.py")),
                "--bundle",
                str(bundle),
                "--output",
                str(candidate_path),
            ],
            check=True,
        )
        candidates = json.loads(candidate_path.read_text(encoding="utf-8"))

    rows, skipped = reconcile_rows(bundle, candidates)
    args.output.resolve().write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output.resolve()), "input_rows": len(candidates), "rows": len(rows), "ligands": len({row.get('ligand_node_id', '') for row in rows}), "skipped": skipped}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
