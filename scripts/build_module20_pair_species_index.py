#!/usr/bin/env python3
"""Build the one-row-per-pair Module 20A species/confidence index."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work" / "module20_db_seed"
ROUTER = WORK / "evidence_escalation_router"
OUTPUT = WORK / "evidence_escalation_router" / "module20a_pair_species_confidence_index.tsv"
EXTERNAL_QUEUE = ROUTER / "module20a_external_review_queue.tsv"
EXTERNAL_DECISION_DIR = WORK / "evidence_escalation_starter"
AUDITED_SUPPLEMENT = ROUTER / "module20a_audited_pair_confidence_supplement.tsv"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def pair_key(label: str) -> str:
    return " ".join(label.split()).casefold()


def canonical_symbol(symbol: str) -> str:
    symbol = symbol.strip()
    if not symbol:
        return ""
    return symbol[:1].upper() + symbol[1:].lower()


def canonical_label(label: str) -> str:
    tokens = [canonical_symbol(token) for token in label.split()]
    return " ".join(token for token in tokens if token)


def max_confidence(rows: list[dict[str, str]], tier_field: str, rank_field: str) -> tuple[str, str]:
    ranked = []
    for row in rows:
        tier = row.get(tier_field, "").strip() or "uncertain"
        try:
            rank = int(row.get(rank_field, "0") or 0)
        except ValueError:
            rank = 0
        ranked.append((rank, tier))
    if not ranked:
        return "not_assessed", "0"
    rank, tier = max(ranked)
    return tier, str(rank)


def main() -> None:
    lane_rows = read_tsv(ROUTER / "module20a_all_lane_overview.tsv")
    rollup_rows = read_tsv(ROUTER / "module20a_evidence_effort_pair_rollup.tsv")
    connectome_rows = read_tsv(
        WORK / "connectomedb_mouse_priority_direct_chunks" / "connectomedb_mouse_priority_direct_master.tsv"
    )
    gtop_rows = read_tsv(WORK / "gtopdb_module20_priority_seeds" / "gtopdb_endogenous_module20_priority.tsv")

    # Audited external rows are added as a controlled supplement.  Unreviewed
    # discovery rows remain in the external queue and do not enter this index.
    external_rows = []
    external_decision_files = sorted(EXTERNAL_DECISION_DIR.glob("module20a_external*_decision_register.tsv"))
    iterative_promotion = EXTERNAL_DECISION_DIR / "module20a_iterative_promotion_2026-08-10_decision_register.tsv"
    if iterative_promotion.exists():
        external_decision_files.append(iterative_promotion)
    focused_pilot_001 = EXTERNAL_DECISION_DIR / "module20a_focused_pilot_001_decision_register.tsv"
    if focused_pilot_001.exists():
        external_decision_files.append(focused_pilot_001)
    batch002_final = EXTERNAL_DECISION_DIR / "module20a_batch002_final_decision_register.tsv"
    if batch002_final.exists():
        external_decision_files.append(batch002_final)
    boundary_batch003_final = EXTERNAL_DECISION_DIR / "module20a_boundary_second_pass_final_decision_register.tsv"
    if boundary_batch003_final.exists():
        external_decision_files.append(boundary_batch003_final)
    remaining_boundary_batch004_final = EXTERNAL_DECISION_DIR / "module20a_remaining_boundary_final_decision_register.tsv"
    if remaining_boundary_batch004_final.exists():
        external_decision_files.append(remaining_boundary_batch004_final)
    manual_boundary_batch005_final = EXTERNAL_DECISION_DIR / "module20a_manual_boundary_continuation_final_decision_register.tsv"
    if manual_boundary_batch005_final.exists():
        external_decision_files.append(manual_boundary_batch005_final)
    literature_batch006_final = EXTERNAL_DECISION_DIR / "module20a_literature_continuation_final_decision_register.tsv"
    if literature_batch006_final.exists():
        external_decision_files.append(literature_batch006_final)
    literature_batch007_final = EXTERNAL_DECISION_DIR / "module20a_literature_continuation045_final_decision_register.tsv"
    if literature_batch007_final.exists():
        external_decision_files.append(literature_batch007_final)
    literature_batch008_final = EXTERNAL_DECISION_DIR / "module20a_literature_continuation046_final_decision_register.tsv"
    if literature_batch008_final.exists():
        external_decision_files.append(literature_batch008_final)
    literature_batch009_final = EXTERNAL_DECISION_DIR / "module20a_literature_continuation047_final_decision_register.tsv"
    if literature_batch009_final.exists():
        external_decision_files.append(literature_batch009_final)
    literature_batch010_final = EXTERNAL_DECISION_DIR / "module20a_literature_continuation048_final_decision_register.tsv"
    if literature_batch010_final.exists():
        external_decision_files.append(literature_batch010_final)
    literature_batch011_final = EXTERNAL_DECISION_DIR / "module20a_literature_continuation049_final_decision_register.tsv"
    if literature_batch011_final.exists():
        external_decision_files.append(literature_batch011_final)
    literature_batch012_final = EXTERNAL_DECISION_DIR / "module20a_literature_continuation050_final_decision_register.tsv"
    if literature_batch012_final.exists():
        external_decision_files.append(literature_batch012_final)
    literature_batch013_final = EXTERNAL_DECISION_DIR / "module20a_literature_continuation051_final_decision_register.tsv"
    if literature_batch013_final.exists():
        external_decision_files.append(literature_batch013_final)
    literature_batch014_final = EXTERNAL_DECISION_DIR / "module20a_literature_continuation052_final_decision_register.tsv"
    if literature_batch014_final.exists():
        external_decision_files.append(literature_batch014_final)
    literature_batch015_final = EXTERNAL_DECISION_DIR / "module20a_literature_continuation053_final_decision_register.tsv"
    if literature_batch015_final.exists():
        external_decision_files.append(literature_batch015_final)
    literature_batch016_final = EXTERNAL_DECISION_DIR / "module20a_literature_continuation054_final_decision_register.tsv"
    if literature_batch016_final.exists():
        external_decision_files.append(literature_batch016_final)
    literature_batch017_final = EXTERNAL_DECISION_DIR / "module20a_literature_continuation055_final_decision_register.tsv"
    if literature_batch017_final.exists():
        external_decision_files.append(literature_batch017_final)
    literature_batch018_final = EXTERNAL_DECISION_DIR / "module20a_literature_continuation056_final_decision_register.tsv"
    if literature_batch018_final.exists():
        external_decision_files.append(literature_batch018_final)
    literature_batch019_final = EXTERNAL_DECISION_DIR / "module20a_literature_continuation057_final_decision_register.tsv"
    if literature_batch019_final.exists():
        external_decision_files.append(literature_batch019_final)
    literature_batch020_final = EXTERNAL_DECISION_DIR / "module20a_literature_continuation058_final_decision_register.tsv"
    if literature_batch020_final.exists():
        external_decision_files.append(literature_batch020_final)
    literature_batch021_final = EXTERNAL_DECISION_DIR / "module20a_literature_continuation059_final_decision_register.tsv"
    if literature_batch021_final.exists():
        external_decision_files.append(literature_batch021_final)
    literature_batch022_final = EXTERNAL_DECISION_DIR / "module20a_literature_continuation060_final_decision_register.tsv"
    if literature_batch022_final.exists():
        external_decision_files.append(literature_batch022_final)
    review_reference_backtrace001_final = EXTERNAL_DECISION_DIR / "module20a_review_reference_backtrace001_final_decision_register.tsv"
    if review_reference_backtrace001_final.exists():
        external_decision_files.append(review_reference_backtrace001_final)
    if EXTERNAL_QUEUE.exists() and external_decision_files:
        external_queue = {row["review_id"]: row for row in read_tsv(EXTERNAL_QUEUE)}
        for decision_path in external_decision_files:
            for decision in read_tsv(decision_path):
                queue_row = external_queue.get(decision["review_id"], {})
                source_flags = []
                if queue_row.get("in_cellchat_priority") == "yes":
                    source_flags.append(("CellChat", f"CellChat:{queue_row.get('pair_label_canonical', decision['pair_label_canonical']).upper().replace(' ', '_')}"))
                if queue_row.get("in_liana_consensus") == "yes":
                    source_flags.append(("LIANA", f"LIANA:{decision['pair_key']}"))
                for source_database, source_record_id in source_flags:
                    external_rows.append(
                        {
                            "pair_label": decision["pair_label_canonical"],
                            "source_record_id": source_record_id,
                            "source_database": source_database,
                            "routing_tier": "external_review",
                            "audit_status": "audited_packet_logged",
                            "reusable_packet_status": "external_batch_review",
                            "reusable_family_packets": "",
                            "best_mouse_confidence_tier": decision["mouse_confidence"],
                            "best_mouse_confidence_rank": decision["mouse_confidence_rank"],
                            "best_human_confidence_tier": decision["human_confidence"],
                            "best_human_confidence_rank": decision["human_confidence_rank"],
                            "confidence_origin": "external_batch_review",
                            "high_confidence_flag": "yes" if decision["confidence_decision"] == "high" else "no",
                            "targeted_followup_bucket": "external_batch_reviewed",
                            "followup_rationale": decision["decision_basis"],
                        }
                    )
                if decision.get("human_evidence_present") == "yes":
                    external_rows.append(
                        {
                            "pair_label": decision["pair_label_canonical"],
                            "source_record_id": f"ExternalHumanEvidence:{decision['review_id']}",
                            "source_database": "ExternalHumanEvidence",
                            "routing_tier": "external_review",
                            "audit_status": "audited_packet_logged",
                            "reusable_packet_status": "external_batch_review",
                            "reusable_family_packets": "",
                            "best_mouse_confidence_tier": decision["mouse_confidence"],
                            "best_mouse_confidence_rank": decision["mouse_confidence_rank"],
                            "best_human_confidence_tier": decision["human_confidence"],
                            "best_human_confidence_rank": decision["human_confidence_rank"],
                            "confidence_origin": "external_batch_review",
                            "high_confidence_flag": "yes" if decision["confidence_decision"] == "high" else "no",
                            "targeted_followup_bucket": "external_batch_reviewed",
                            "followup_rationale": decision["decision_basis"],
                        }
                    )
    lane_rows.extend(external_rows)

    # Audited pair-level packets that are not external-queue decisions are
    # added as a controlled supplement.  This preserves the source/database
    # seed rows while allowing pair-specific evidence escalation to raise or
    # lower species confidence reproducibly.  The supplement must retain
    # source_record_id and source_database provenance for every row.
    if AUDITED_SUPPLEMENT.exists():
        lane_rows.extend(read_tsv(AUDITED_SUPPLEMENT))

    by_key: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in lane_rows:
        by_key[pair_key(row["pair_label"])].append(row)

    rollup_by_key: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rollup_rows:
        rollup_by_key[pair_key(row["pair_label"])].append(row)

    connectome_by_record = {row["interaction_id"]: row for row in connectome_rows}
    gtop_human_by_key: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in gtop_rows:
        if row["source_record_id"].rsplit(":", 1)[-1].casefold() == "human":
            gtop_human_by_key[pair_key(row["pair_label"])].append(row)
    output_rows = []
    for key in sorted(by_key):
        rows = by_key[key]
        rollups = rollup_by_key.get(key, [])
        display_label = canonical_label(sorted(row["pair_label"] for row in rows)[0])
        databases = sorted({row["source_database"] for row in rows})
        records = sorted({row["source_record_id"] for row in rows})

        mouse_sources = set()
        human_sources = set()
        human_ortholog_mapping = False
        for row in rows:
            source = row["source_database"]
            record = row["source_record_id"]
            if source in {"CellChat", "ConnectomeDB2025", "LIANA"}:
                mouse_sources.add(source)
            elif source == "GuideToPharmacology":
                species = record.rsplit(":", 1)[-1].casefold()
                if species == "mouse":
                    mouse_sources.add(source)
                elif species == "human":
                    human_sources.add(source)
            elif source == "ExternalHumanEvidence":
                human_sources.add(source)
            if source == "ConnectomeDB2025":
                cdb = connectome_by_record.get(record)
                if cdb and cdb.get("human_ligand_symbols", "").strip() and cdb.get("human_receptor_symbols", "").strip():
                    human_ortholog_mapping = True
        human_source_rows = gtop_human_by_key.get(key, [])
        if human_source_rows:
            human_sources.add("GuideToPharmacology")

        mouse_present = bool(mouse_sources)
        human_present = bool(human_sources)
        if mouse_present and human_present:
            conservation_status = "present_in_both_species_sources"
            conservation_call = "yes"
        elif mouse_present and human_ortholog_mapping:
            conservation_status = "mouse_source_plus_human_ortholog_mapping_only"
            conservation_call = "not_established"
        elif mouse_present:
            conservation_status = "mouse_source_only_in_current_sources"
            conservation_call = "not_established"
        elif human_present:
            conservation_status = "human_source_only_in_current_sources"
            conservation_call = "not_established"
        else:
            conservation_status = "species_not_resolved_from_current_sources"
            conservation_call = "not_established"

        mouse_conf, mouse_rank = max_confidence(rows, "best_mouse_confidence_tier", "best_mouse_confidence_rank")
        human_conf, human_rank = max_confidence(rows, "best_human_confidence_tier", "best_human_confidence_rank")
        confident_species = []
        if mouse_conf == "high":
            confident_species.append("mouse")
        if human_conf == "high":
            confident_species.append("human")
        if mouse_conf == "high" or human_conf == "high":
            either_status = "high_in_at_least_one_species"
        elif mouse_conf == "medium" or human_conf == "medium":
            either_status = "medium_or_lower_only"
        else:
            either_status = "uncertain_or_unassessed"

        audited = any(row["audit_status"] == "audited_packet_logged" for row in rows)
        output_rows.append(
            {
                "pair_key": key,
                "pair_label_canonical": display_label,
                "source_record_count": str(len(records)),
                "source_databases": ";".join(databases),
                "human_pair_source_record_count": str(len(human_source_rows)),
                "human_pair_source_record_ids": ";".join(sorted(row["source_record_id"] for row in human_source_rows)),
                "mouse_confidence": mouse_conf,
                "mouse_confidence_rank": mouse_rank,
                "human_confidence": human_conf,
                "human_confidence_rank": human_rank,
                "high_confidence_species": ";".join(confident_species),
                "confidence_extractability": either_status,
                "has_audited_packet": "yes" if audited else "no",
                "pair_present_in_mouse_sources": "yes" if mouse_present else "no",
                "pair_present_in_human_sources": "yes" if human_present else "no",
                "human_ortholog_mapping_present": "yes" if human_ortholog_mapping else "no",
                "conserved_between_mouse_and_human": conservation_call,
                "conservation_status": conservation_status,
                "absence_is_non_evidence": "yes",
                "source_record_ids": ";".join(records),
            }
        )

    fields = list(output_rows[0]) if output_rows else []
    with OUTPUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)
    print(f"wrote {len(output_rows)} unique pair rows to {OUTPUT}")


if __name__ == "__main__":
    main()
