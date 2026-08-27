#!/usr/bin/env python3
"""Build bounded exact-pair literature packets from TRRUST/DoRothEA leads."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path


FIELDS = [
    "tf_key", "species", "tf_symbol", "target_symbol", "source_registry",
    "external_record_key", "reference_pmids", "reference_text", "source_locator",
    "raw_relationship_effect", "effect_polarity", "relationship_class", "evidence_basis",
    "confidence_tier", "dorothea_level", "limitations",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def pmid_count(value: str) -> int:
    return len({p.strip() for p in (value or "").replace(",", ";").split(";") if p.strip().isdigit()})


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-manifest", type=Path, required=True)
    parser.add_argument("--source-records", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    records = read_tsv(args.source_records)
    by_tf: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in records:
        key = (row.get("tf_normalized_symbol_key") or "").strip().casefold()
        target = (row.get("target_normalized_symbol") or row.get("source_target_symbol") or "").strip()
        if key and target and target not in {"\\N", "NA", "null"}:
            by_tf[key].append(row)

    manifest = json.loads(args.batch_manifest.read_text(encoding="utf-8"))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    packet_manifest: dict[str, dict[str, int]] = {}
    for batch in manifest["batches"]:
        rows: list[dict[str, str]] = []
        for key in batch["tf_keys"]:
            candidates = by_tf.get(key.casefold(), [])
            # Keep the strongest TRRUST/DoRothEA record per species/target, then
            # cap the packet so agents review bounded exact pairs rather than all
            # thousands of database edges.
            best: dict[tuple[str, str], dict[str, str]] = {}
            for row in candidates:
                species = (row.get("species_context") or "").strip().casefold()
                target = (row.get("target_normalized_symbol") or row.get("source_target_symbol") or "").strip()
                if species not in {"human", "mouse"} or not target:
                    continue
                reg = row.get("source_registry", "")
                score = (
                    1 if reg.casefold() == "trrust" else 0,
                    pmid_count(row.get("reference_pmids", "")),
                    int(row.get("curation_effort", "0") or 0) if (row.get("curation_effort", "0") or "0").isdigit() else 0,
                    row.get("dorothea_level", ""),
                )
                slot = (species, target.casefold())
                previous = best.get(slot)
                if previous is None or score > previous["_score"]:
                    copied = dict(row)
                    copied["_score"] = score
                    best[slot] = copied
            chosen = sorted(best.values(), key=lambda row: row["_score"], reverse=True)[:4]
            for row in chosen:
                rows.append({
                    "tf_key": key,
                    "species": row.get("species_context", ""),
                    "tf_symbol": row.get("source_tf_symbol") or row.get("tf_normalized_symbol", ""),
                    "target_symbol": row.get("target_normalized_symbol") or row.get("source_target_symbol", ""),
                    "source_registry": row.get("source_registry", ""),
                    "external_record_key": row.get("external_record_key", ""),
                    "reference_pmids": row.get("reference_pmids", ""),
                    "reference_text": row.get("reference_text", ""),
                    "source_locator": row.get("source_locator", ""),
                    "raw_relationship_effect": row.get("raw_relationship_effect", ""),
                    "effect_polarity": row.get("effect_polarity", ""),
                    "relationship_class": row.get("relationship_class", ""),
                    "evidence_basis": row.get("evidence_basis", ""),
                    "confidence_tier": row.get("confidence_tier", ""),
                    "dorothea_level": row.get("dorothea_level", ""),
                    "limitations": row.get("limitations", ""),
                })
        out = args.output_dir / f"{batch['batch_id']}.tsv"
        with out.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        packet_manifest[batch["batch_id"]] = {"tf_keys": len(batch["tf_keys"]), "candidate_rows": len(rows)}

    (args.output_dir / "packet_manifest.json").write_text(json.dumps(packet_manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"batches": len(packet_manifest), "packets": packet_manifest}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
