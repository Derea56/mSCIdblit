#!/usr/bin/env python3
"""Create the controlled Module 21A extraction queue from explicit seed gaps."""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELAY = ROOT / "work" / "module21_relay"
MATRIX = RELAY / "module21a_saturation_matrix.tsv"
QUEUE = RELAY / "module21a_extraction_queue.tsv"
HANDOFF = RELAY / "module21a_lr_handoff.md"
MANIFEST = ROOT / "work" / "module20_db_seed" / "evidence_escalation_router" / "module20a_lr_release_manifest.json"


def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    matrix = read(MATRIX)
    rows = []
    for index, row in enumerate(matrix, 1):
        gap = row["next_gap"]
        priority = "high" if "SCI" in row["SCI_relevance_posture"] or "specific" in gap.lower() else "medium"
        rows.append({"queue_id": f"M21A-Q{index:03d}", "family_id": row["family_id"], "family_name": row["family_name"], "current_relay_coverage": row["canonical_relay_coverage"], "alternate_branch_coverage": row["alternate_branch_coverage"], "species_posture": row["species_posture"], "sci_relevance_posture": row["SCI_relevance_posture"], "current_status": row["status"], "extraction_priority": priority, "next_gap": gap, "evidence_layer": "intracellular_relay", "status": "queued"})
    fields = list(rows[0])
    write(QUEUE, fields, rows)
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    HANDOFF.write_text(
        f"""# Module 21A LR handoff and extraction scope

Generated from frozen LR manifest `{manifest['manifest_version']}` at
`{manifest['generated_utc']}`.

## Frozen Module 20A boundary

- Comparison universe: **{manifest['pair_universe']['comparison_total']}** rows
- Source-backed LR union: **{manifest['pair_universe']['source_union_total']}** unique pairs
- Comparison-only rows excluded from LR release: **{manifest['pair_universe']['comparison_only_total']}**
- CellChat-full pairs: **{manifest['pair_universe']['cellchat_full_total']}**
- LIANA-consensus pairs: **{manifest['pair_universe']['liana_consensus_total']}**
- Source commit: `{manifest.get('source_git_commit')}`

The frozen LR release is an input boundary for Module 21A. It does not imply
that a ligand–receptor pair activates every downstream relay edge. Module 21A
must separately extract intracellular evidence and preserve assay, species,
cell-model, branch, and perturbation context.

## Existing seed

The first-pass Module 21A packet contains 57 relay edges, 14 grouped evidence
records, and 17 perturbation records across nine priority families. It remains
an audit-layer seed until node identity and branch semantics are reconciled.

## Extraction order

1. Reconcile receptor-complex names in the Module 20A release with Module 21A
   receptor entry nodes.
2. Extract primary evidence for the explicit family gaps in
   `module21a_extraction_queue.tsv`.
3. Keep direct molecular edges separate from pathway-complex and functional
   output edges.
4. Record negative or boundary evidence explicitly; do not fill gaps by
   pathway analogy.
5. Materialize SQL only after the evidence and node-identity audit passes.

The queue is intentionally family-level for this pass. Each extracted edge
should retain a stable evidence ID and link back to the LR snapshot only as
its upstream receptor/ligand context.
""",
        encoding="utf-8",
    )
    print(f"wrote {QUEUE} and {HANDOFF} for {len(rows)} family gaps")


if __name__ == "__main__":
    main()
