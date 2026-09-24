#!/usr/bin/env python3
"""Build an evidence-only prolactin-PRLR-JAK2-STAT5-Csn2 route."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def unique_join(*values: str) -> str:
    output: list[str] = []
    seen: set[str] = set()
    for value in values:
        for item in value.split(";"):
            item = item.strip()
            if item and item not in seen:
                seen.add(item)
                output.append(item)
    return "; ".join(output)


def make_rows(bundle: Path) -> list[dict[str, str]]:
    expansions = read_tsv(bundle / "mechanism_literature_expansion.tsv")
    nodes = {row["node_id"]: row for row in read_tsv(bundle / "mechanism_nodes.tsv")}
    template = next(
        row
        for row in expansions
        if row["expansion_id"] == "M21B-LITEXP-FULLSEQ-0165"
    )
    target = nodes["NODE02548"]
    row = dict(template)
    row.update(
        {
            "expansion_id": "M21B-LITEXP-PROLactin-JAK2-STAT5-CSN2-001",
            "path_expression": "ligand>receptor>intracellular>TF>target_gene_expression",
            "route_tier": "ligand_receptor_intracellular_tf_target_missing_direct_tf_edges",
            "known_layers": "ligand|receptor|intracellular_continuation|transcription_factor|target_gene_expression",
            "missing_layers": "intracellular_to_tf_edge|tf_to_target_edge",
            "target_gene_node_id": target["node_id"],
            "target_gene_label": target["canonical_label"],
            "output_node_id": target["node_id"],
            "output_label": "Csn2 (beta-casein) expression",
            "pathway_name": "Prolactin-PRLR-JAK2-STAT5-Csn2",
            "route_linkage_status": unique_join(
                template["route_linkage_status"],
                "target_gene_output_supported",
                "intracellular_to_tf_edge_not_asserted",
                "tf_to_target_edge_not_asserted",
            ),
            "primary_locator": unique_join(template["primary_locator"], "PMID:7925280"),
            "evidence_ids": unique_join(template["evidence_ids"], "M22B-EVID-000072"),
            "citation_note": (
                "Primary prolactin/PRLR studies support JAK2-dependent STAT5 activation and a beta-casein "
                "promoter reporter response. Csn2 is retained as the target-gene output, while the exact "
                "STAT5-to-Csn2 handoff is not asserted as a new graph edge."
            ),
            "evidence_summary": (
                "Primary evidence supports prolactin engagement of PRLR, JAK2-dependent STAT5 activation, "
                "and prolactin-associated beta-casein reporter output. The route composes these source-linked "
                "layers and keeps the intracellular-to-STAT5 and STAT5-to-Csn2 handoffs explicit as unresolved "
                "evidence-layer links where the graph does not assert them."
            ),
            "limitations": (
                "The receptor, kinase/STAT5, and beta-casein reporter observations are source-linked layers "
                "from mammary/cytokine-receptor systems rather than one end-to-end experiment. Preserve long-"
                "form PRLR dependence, species and assay context, beta-casein reporter versus endogenous Csn2 "
                "distinction, and the non-causal route status; no SCI transfer or database confidence score is inferred."
            ),
            "output_class": "target_gene_expression",
            "curation_status": "curated_primary_route",
        }
    )
    return [row]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = make_rows(args.bundle.resolve())
    args.output.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "output": str(args.output)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
