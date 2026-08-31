#!/usr/bin/env python3
"""Build a conservative entity/pathway alias audit for promoted linkages."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LINKAGE_ROOT = ROOT / "work" / "cross_module_synthesis" / "path_linkage_batches"
OUT = ROOT / "work" / "cross_module_synthesis" / "module20_24_entity_pathway_dedup_audit.tsv"
REPORT = ROOT / "work" / "cross_module_synthesis" / "module20_24_entity_pathway_dedup_audit.md"

FIELDS = ["raw_label", "normalized_key", "label_type", "layer", "linkage_edge_ids", "source_rows", "dedup_status", "complex_preservation_note"]


def split(value: str) -> list[str]:
    return [item.strip() for item in (value or "").split(";") if item.strip()]


def normalize(value: str) -> str:
    value = value.casefold().replace("α", "alpha").replace("β", "beta")
    return re.sub(r"[^a-z0-9]+", "", value)


def add_label(store: dict[tuple[str, str], dict], raw: str, label_type: str, layer: str, edge_id: str) -> None:
    if not raw or raw.startswith("No exact"):
        return
    value = raw.strip()
    if value.startswith("Module 23B relay: "):
        value = value.removeprefix("Module 23B relay: ")
    elif value.startswith("Module 24B relay: "):
        value = value.removeprefix("Module 24B relay: ")
    elif value.startswith("Module M23B output: "):
        value = value.removeprefix("Module M23B output: ")
    elif value.startswith("Module M22B contextual program: "):
        value = value.removeprefix("Module M22B contextual program: ")
    key = normalize(value)
    if not key:
        return
    record = store.setdefault((value, key), {"raw_label": value, "normalized_key": key, "label_type": label_type, "layers": set(), "edges": set(), "rows": 0})
    record["layers"].add(layer)
    record["edges"].add(edge_id)
    record["rows"] += 1


def main() -> None:
    store: dict[tuple[str, str], dict] = {}
    linkage_rows = 0
    promoted_rows = 0
    for path in sorted(LINKAGE_ROOT.glob("module20_24_path_linkage_block*.tsv")):
        with path.open(newline="") as handle:
            for row in csv.DictReader(handle, delimiter="\t"):
                linkage_rows += 1
                if row.get("linkage_status") == "direct_lr_only_bounded_no_exact_relay_or_downstream":
                    continue
                promoted_rows += 1
                edge_id = row["lr_edge_ids"]
                add_label(store, row.get("ligand", ""), "ligand", "M20B", edge_id)
                add_label(store, row.get("receptor_complex", ""), "receptor_complex", "M20B", edge_id)
                for item in split(row.get("relay_or_pathway", "")):
                    add_label(store, item, "relay_or_pathway", "M23B_or_M24B", edge_id)
                for item in split(row.get("terminal_tf_or_output", "")):
                    add_label(store, item, "downstream_or_output", "M22B_or_M23B", edge_id)

    by_key: dict[str, list[dict]] = defaultdict(list)
    for record in store.values():
        by_key[record["normalized_key"]].append(record)

    rows = []
    for record in sorted(store.values(), key=lambda item: (item["normalized_key"], item["label_type"], item["raw_label"])):
        aliases = by_key[record["normalized_key"]]
        status = "candidate_alias_group" if len(aliases) > 1 else "unique_label"
        complex_note = (
            "Preserve receptor-complex/subunit or processed-domain topology; alias candidate only, no automatic merge."
            if any(token in record["raw_label"] for token in (":", "/", "_", "complex", "domain", "alpha", "beta"))
            else "No complex/domain marker in label; retain exact source spelling."
        )
        rows.append({
            "raw_label": record["raw_label"],
            "normalized_key": record["normalized_key"],
            "label_type": record["label_type"],
            "layer": ";".join(sorted(record["layers"])),
            "linkage_edge_ids": ";".join(sorted(record["edges"])),
            "source_rows": str(record["rows"]),
            "dedup_status": status,
            "complex_preservation_note": complex_note,
        })

    with OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)

    alias_groups = sum(1 for values in by_key.values() if len(values) > 1)
    cross_layer_groups = sum(1 for values in by_key.values() if len({value["label_type"] for value in values}) > 1)
    complex_rows = sum("complex/domain" in row["complex_preservation_note"] for row in rows)
    report = [
        "# Module 20B–24B Entity/Pathway Deduplication Audit",
        "",
        f"- Linkage rows scanned: {linkage_rows:,}",
        f"- Promoted linkage rows scanned: {promoted_rows:,}",
        f"- Distinct raw labels: {len(rows):,}",
        f"- Normalized alias groups requiring review: {alias_groups:,}",
        f"- Alias groups crossing evidence layers: {cross_layer_groups:,}",
        f"- Labels with complex/domain preservation markers: {complex_rows:,}",
        "",
        "## Rules",
        "",
        "Normalized keys are candidate alias groups only. Receptor complexes, subunits, processed domains, reciprocal adhesion labels, and pathway/program outputs are not automatically collapsed.",
        "Direct, receptor-proximal/pathway, and downstream/function labels remain separate even when their normalized names overlap.",
        "",
        "## Materialization gate",
        "",
        "The TSV must be reviewed for alias groups before canonical SignalingEntity, SignalingPathway, and SignalingEdge rows are generated.",
        "",
    ]
    REPORT.write_text("\n".join(report))
    print(f"linkage_rows={linkage_rows} promoted_rows={promoted_rows} labels={len(rows)} alias_groups={alias_groups} cross_layer_groups={cross_layer_groups}")


if __name__ == "__main__":
    main()
