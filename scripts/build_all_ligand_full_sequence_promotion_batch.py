#!/usr/bin/env python3
"""Combine the conservative all-ligand full-sequence promotion passes.

The component generators already enforce primary locators and retain missing
handoffs.  This wrapper runs them against one immutable source bundle, removes
duplicate route signatures, merges auditable evidence fields when the same
signature is supported by more than one pass, and assigns collision-free
expansion identifiers before materialization.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path


SIGNATURE_FIELDS = (
    "ligand_node_id",
    "receptor_node_id",
    "intracellular_continuation_node_id",
    "transcription_factor_node_id",
    "target_gene_node_id",
    "output_label",
)
MERGE_FIELDS = (
    "evidence_ids",
    "primary_locator",
    "route_linkage_status",
    "limitations",
    "citation_note",
    "source_chain_id",
)
NO_ROWS_MARKERS = (
    "No eligible full-intermediate queue records found",
    "No source-linked full-sequence compositions found",
    "No eligible source-linked target routes found",
    "No eligible route candidates found",
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
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
    return ";".join(result)


def signature(row: dict[str, str]) -> tuple[str, ...]:
    return tuple(row.get(field, "") for field in SIGNATURE_FIELDS)


def prefix_and_number(expansion_id: str) -> tuple[str, int] | None:
    match = re.match(r"^(.*-)(\d+)$", expansion_id)
    if not match:
        return None
    return match.group(1), int(match.group(2))


def run_generator(script: Path, bundle: Path, temp_dir: Path) -> list[dict[str, str]]:
    output = temp_dir / f"{script.stem}.json"
    if script.name in {"build_full_sequence_target_gene_promotion_batch.py", "build_source_linked_component_promotion_batch.py", "build_source_linked_target_gene_promotion_batch.py"}:
        command = [sys.executable, str(script), "--bundle", str(bundle), "--output", str(output)]
    else:
        command = [sys.executable, str(script), "--bundle-dir", str(bundle), "--output", str(output)]
    completed = subprocess.run(command, text=True, capture_output=True, check=False)
    if completed.returncode:
        combined = f"{completed.stdout}\n{completed.stderr}"
        if any(marker in combined for marker in NO_ROWS_MARKERS):
            return []
        raise RuntimeError(f"{script.name} failed:\n{combined}")
    return json.loads(output.read_text(encoding="utf-8"))


def renumber(rows: list[dict[str, str]], existing_ids: set[str]) -> None:
    maxima: defaultdict[str, int] = defaultdict(int)
    for expansion_id in existing_ids:
        parsed = prefix_and_number(expansion_id)
        if parsed:
            prefix, number = parsed
            maxima[prefix] = max(maxima[prefix], number)
    for row in rows:
        parsed = prefix_and_number(row.get("expansion_id", ""))
        if not parsed:
            raise ValueError(f"expansion row has an unparseable ID: {row.get('expansion_id', '')}")
        prefix, _ = parsed
        maxima[prefix] += 1
        row["expansion_id"] = f"{prefix}{maxima[prefix]:04d}"
        existing_ids.add(row["expansion_id"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    bundle = args.bundle.resolve()

    existing = read_tsv(bundle / "mechanism_literature_expansion.tsv")
    existing_ids = {row["expansion_id"] for row in existing}
    seen_signatures = {signature(row) for row in existing}

    generator_names = (
        "build_full_sequence_target_gene_promotion_batch.py",
        "build_source_linked_component_promotion_batch.py",
        "build_source_linked_target_gene_promotion_batch.py",
        "generate_missing_intermediate_literature_batch_from_queue.py",
        "generate_full_sequence_literature_batch_from_queue.py",
    )
    generated: list[dict[str, str]] = []
    generator_counts: dict[str, int] = {}
    with tempfile.TemporaryDirectory(prefix="mSCIdblit_full_sequence_") as temp_name:
        temp_dir = Path(temp_name)
        for name in generator_names:
            rows = run_generator(Path(__file__).with_name(name), bundle, temp_dir)
            generator_counts[name] = len(rows)
            for row in rows:
                key = signature(row)
                if key in seen_signatures:
                    existing_match = next((item for item in generated if signature(item) == key), None)
                    if existing_match is not None:
                        for field in MERGE_FIELDS:
                            existing_match[field] = join_unique(existing_match.get(field, ""), row.get(field, ""))
                    continue
                seen_signatures.add(key)
                generated.append(row)

    renumber(generated, existing_ids)
    args.output.resolve().write_text(json.dumps(generated, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(args.output.resolve()),
        "rows": len(generated),
        "ligands": len({row.get("ligand_label", "") for row in generated}),
        "generator_counts": generator_counts,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
