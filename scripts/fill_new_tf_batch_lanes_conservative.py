#!/usr/bin/env python3
"""Fill missing remaining-TF batch lanes with conservative database-only rows.

This is a completion fallback for lanes whose bounded literature worker did not
finish. It records the best existing TRRUST/DoRothEA source lead but never
promotes a pair and never writes the canonical graph or database.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


FIELDS = [
    "species", "tf_symbol", "target_symbol", "external_record_keys", "decision",
    "module_assignment", "evidence_status", "support_kind", "effect_polarity",
    "primary_pmids", "corroborating_pmids", "shared_paper_status",
    "cross_module_status", "cell_type_context", "stimulus_context", "limitations", "notes",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def pmids(value: str) -> list[str]:
    return sorted({token.strip() for token in (value or "").replace(",", ";").split(";")
                   if token.strip().isdigit()}, key=int)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-manifest", type=Path, required=True)
    parser.add_argument("--source-records", type=Path, required=True)
    parser.add_argument("--lane-dir", type=Path, required=True)
    parser.add_argument("--batch-id", action="append", dest="batch_ids")
    args = parser.parse_args()

    manifest = json.loads(args.batch_manifest.read_text(encoding="utf-8"))
    records = read_tsv(args.source_records)
    by_tf: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in records:
        key = (row.get("tf_normalized_symbol_key") or "").strip().casefold()
        target = (row.get("target_normalized_symbol") or row.get("source_target_symbol") or "").strip()
        if key and target and target not in {"\\N", "NA", "null"}:
            row = dict(row)
            row["_target"] = target
            row["_pmids"] = pmids(row.get("reference_pmids", ""))
            by_tf[key].append(row)

    batches = manifest["batches"]
    selected = set(args.batch_ids or [batch["batch_id"] for batch in batches])
    args.lane_dir.mkdir(parents=True, exist_ok=True)
    generated: dict[str, int] = {}
    for batch in batches:
        batch_id = batch["batch_id"]
        if batch_id not in selected:
            continue
        out = args.lane_dir / f"{batch_id}.tsv"
        if out.exists():
            continue
        rows: list[dict[str, str]] = []
        for key in batch["tf_keys"]:
            candidates = by_tf.get(key.casefold(), [])
            if not candidates:
                rows.append({
                    "species": "human", "tf_symbol": key.upper(), "target_symbol": "UNKNOWN",
                    "external_record_keys": "", "decision": "database_only_unverified",
                    "module_assignment": "22B", "evidence_status": "database_curated_unverified",
                    "support_kind": "database_assertion", "effect_polarity": "unknown",
                    "primary_pmids": "", "corroborating_pmids": "",
                    "shared_paper_status": "none_identified", "cross_module_status": "none_claimed",
                    "cell_type_context": "not verified", "stimulus_context": "not verified",
                    "limitations": "No source record was available for a bounded exact-pair review.",
                    "notes": "Conservative completion row; no promotion asserted.",
                })
                continue
            best = max(candidates, key=lambda row: (len(row["_pmids"]),
                                                       row.get("source_registry", ""),
                                                       row.get("external_record_key", "")))
            ref_head = ";".join(best["_pmids"][:5])
            species = (best.get("species_context") or "human").strip().casefold()
            if species not in {"human", "mouse"}:
                species = "human"
            tf_symbol = (best.get("source_tf_symbol") or best.get("tf_normalized_symbol") or key).strip()
            target_symbol = best["_target"]
            rows.append({
                "species": species,
                "tf_symbol": tf_symbol,
                "target_symbol": target_symbol,
                "external_record_keys": best.get("external_record_key", ""),
                "decision": "database_only_unverified",
                "module_assignment": "22B",
                "evidence_status": "database_curated_unverified",
                "support_kind": "database_assertion",
                "effect_polarity": "unknown",
                "primary_pmids": "",
                "corroborating_pmids": "",
                "shared_paper_status": "none_identified",
                "cross_module_status": "none_claimed",
                "cell_type_context": "not verified; source database only",
                "stimulus_context": "not verified",
                "limitations": "Database presence and linked PMIDs do not establish exact-pair direct binding or perturbation, effect direction, or species/context scope.",
                "notes": f"Conservative source lead only; source_registry={best.get('source_registry','')}; database_ref_count={len(best['_pmids'])}; ref_head={ref_head}; no promotion asserted.",
            })
        with out.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        generated[batch_id] = len(rows)

    print(json.dumps({"generated": generated, "lane_dir": str(args.lane_dir)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
