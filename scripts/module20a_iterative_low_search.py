#!/usr/bin/env python3
"""Manage resumable, auditable literature-search passes over Module 20A lows.

This tool only manages search accounting and worker packets. It never promotes
a row, edits the canonical queue, or creates a SignalingEdge. A curator must
review worker flags and write the normal evidence/decision registers.
"""

from __future__ import annotations

import argparse
import csv
from datetime import UTC, datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue.tsv"
OUT = ROOT / "work/module20_db_seed/evidence_search_agents/iterative"
LEDGER = OUT / "low_search_ledger.tsv"

LEDGER_HEADERS = [
    "review_id",
    "pair_key",
    "pair_label_canonical",
    "review_priority",
    "review_priority_rationale",
    "queue_confidence",
    "search_status",
    "attempt_count",
    "last_iteration",
    "packet_id",
    "worker_verdict",
    "source_locators",
    "species_support",
    "support_kind",
    "evidence_summary",
    "limitations",
    "curator_disposition",
    "last_updated_utc",
]

ACTIVE_STATUSES = {"unsearched", "retry"}
VERDICTS = {"promote_candidate", "needs_manual_review", "hold_low", "reject_pair"}


def now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, headers: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def queue_rows() -> list[dict[str, str]]:
    rows = read_tsv(QUEUE)
    return [row for row in rows if row.get("confidence_decision") == "low"]


def init_ledger() -> list[dict[str, str]]:
    existing = {row["review_id"]: row for row in read_tsv(LEDGER)} if LEDGER.exists() else {}
    # Preserve completed/promoted rows as well as currently low queue rows.
    # Otherwise a later ledger refresh would silently drop rows after their
    # confidence decision changed in the canonical queue.
    merged: dict[str, dict[str, str]] = dict(existing)
    for row in queue_rows():
        review_id = row["review_id"]
        if review_id in existing:
            merged[review_id] = existing[review_id]
            continue
        merged[review_id] = {
            "review_id": review_id,
            "pair_key": row.get("pair_key", ""),
            "pair_label_canonical": row.get("pair_label_canonical", ""),
            "review_priority": row.get("review_priority", ""),
            "review_priority_rationale": row.get("review_priority_rationale", ""),
            "queue_confidence": row.get("confidence_decision", "low"),
            "search_status": "unsearched",
            "attempt_count": "0",
            "last_iteration": "",
            "packet_id": "",
            "worker_verdict": "",
            "source_locators": "",
            "species_support": "",
            "support_kind": "",
            "evidence_summary": "",
            "limitations": "",
            "curator_disposition": "",
            "last_updated_utc": now(),
        }
    rows = sorted(merged.values(), key=lambda row: (int(row["review_priority"] or 99), row["review_id"]))
    write_tsv(LEDGER, LEDGER_HEADERS, rows)
    return rows


def next_iteration() -> int:
    values = []
    for path in OUT.glob("iteration_*"):
        try:
            values.append(int(path.name.split("_", 1)[1]))
        except (IndexError, ValueError):
            pass
    return max(values, default=0) + 1


def export_batch(args: argparse.Namespace) -> None:
    rows = init_ledger()
    iteration = args.iteration or next_iteration()
    candidates = [row for row in rows if row["search_status"] in ACTIVE_STATUSES]
    candidates.sort(key=lambda row: (int(row["review_priority"] or 99), row["review_id"]))
    selected = candidates[: args.batch_size]
    if not selected:
        print("no unsearched low-confidence rows remain")
        return

    iteration_dir = OUT / f"iteration_{iteration:03d}"
    packet_rows: list[dict[str, str]] = []
    for row in selected:
        queue_row = next(item for item in queue_rows() if item["review_id"] == row["review_id"])
        packet_rows.append(
            {
                "review_id": row["review_id"],
                "pair_key": row["pair_key"],
                "pair_label_canonical": row["pair_label_canonical"],
                "review_priority": row["review_priority"],
                "review_priority_rationale": row["review_priority_rationale"],
                "seed_annotations": queue_row.get("cellchat_priority_annotations", "UNKNOWN"),
                "seed_pathways": queue_row.get("cellchat_priority_pathways", "UNKNOWN"),
                "seed_directness": queue_row.get("cellchat_priority_directness", "UNKNOWN"),
                "complex_receptor_coverage": queue_row.get("complex_receptor_coverage", "UNKNOWN"),
                "existing_evidence_register_ids": queue_row.get("evidence_register_ids", "UNKNOWN"),
                "curator_notes": queue_row.get("curator_notes", "UNKNOWN"),
            }
        )

    packet_headers = list(packet_rows[0])
    write_tsv(iteration_dir / "source_rows.tsv", packet_headers, packet_rows)
    manifest: list[dict[str, str]] = []
    packet_size = args.packet_size
    for start in range(0, len(packet_rows), packet_size):
        chunk = packet_rows[start : start + packet_size]
        packet_id = f"M20A-ITER{iteration:03d}-{start // packet_size + 1:02d}"
        packet_path = iteration_dir / f"{packet_id}.tsv"
        write_tsv(packet_path, packet_headers, chunk)
        manifest.append(
            {
                "iteration": str(iteration),
                "packet_id": packet_id,
                "row_count": str(len(chunk)),
                "first_review_id": chunk[0]["review_id"],
                "last_review_id": chunk[-1]["review_id"],
                "packet_path": str(packet_path.relative_to(ROOT)),
                "worker_status": "queued",
            }
        )
        selected_ids = {selected_row["review_id"] for selected_row in chunk}
        for ledger_row in rows:
            if ledger_row["review_id"] not in selected_ids:
                continue
            ledger_row["search_status"] = "queued"
            ledger_row["attempt_count"] = str(int(ledger_row["attempt_count"] or 0) + 1)
            ledger_row["last_iteration"] = str(iteration)
            ledger_row["packet_id"] = packet_id
            ledger_row["last_updated_utc"] = now()

    write_tsv(iteration_dir / "packet_manifest.tsv", list(manifest[0]), manifest)
    write_tsv(LEDGER, LEDGER_HEADERS, rows)
    (iteration_dir / "worker_contract.md").write_text(
        """# Worker contract

Read only your assigned TSV packet. Return one tab-separated row per
candidate, with the exact columns below, plus a short count summary.
Do not edit the canonical queue, tracker, evidence registers, or
SignalingEdge tables. A worker verdict is only a curator-review flag.

`review_id\tpair_key\tverdict\tsource_locators\tspecies_support\tsupport_kind\tevidence_summary\tlimitations`

Allowed verdicts: `promote_candidate`, `needs_manual_review`,
`hold_low`, `reject_pair`. Use exact PMIDs/DOIs/URLs, do not infer
species, complexes, directness, SCI relevance, or downstream mechanism.
Prefer mouse primary evidence. Database records, expression, pathway
membership, and review cartoons are leads, not promotion evidence.
""",
        encoding="utf-8",
    )
    print(f"iteration={iteration} selected={len(selected)} packets={len(manifest)} remaining_unsearched={len(candidates)-len(selected)}")
    print(iteration_dir)


def record_report(args: argparse.Namespace) -> None:
    """Record a worker report after checking identity and allowed vocabulary."""
    rows = init_ledger()
    report = read_tsv(args.report)
    required = [
        "review_id",
        "pair_key",
        "verdict",
        "source_locators",
        "species_support",
        "support_kind",
        "evidence_summary",
        "limitations",
    ]
    if not report or list(report[0]) != required:
        raise SystemExit(f"report must have exact columns: {required}")
    by_id = {row["review_id"]: row for row in rows}
    seen: set[str] = set()
    for item in report:
        review_id = item["review_id"]
        if review_id in seen:
            raise SystemExit(f"duplicate review_id in report: {review_id}")
        seen.add(review_id)
        ledger_row = by_id.get(review_id)
        if ledger_row is None:
            raise SystemExit(f"review_id is not a low row in the ledger: {review_id}")
        if ledger_row["packet_id"] != args.packet_id:
            raise SystemExit(f"{review_id} belongs to {ledger_row['packet_id']}, not {args.packet_id}")
        if item["pair_key"] != ledger_row["pair_key"]:
            raise SystemExit(f"pair_key mismatch for {review_id}")
        if item["verdict"] not in VERDICTS:
            raise SystemExit(f"invalid verdict for {review_id}: {item['verdict']}")
        if not item["evidence_summary"].strip() or not item["limitations"].strip():
            raise SystemExit(f"summary and limitations are required for {review_id}")
        ledger_row.update(
            {
                "search_status": "flagged",
                "worker_verdict": item["verdict"],
                "source_locators": item["source_locators"] or "UNKNOWN",
                "species_support": item["species_support"] or "UNKNOWN",
                "support_kind": item["support_kind"] or "UNKNOWN",
                "evidence_summary": item["evidence_summary"],
                "limitations": item["limitations"],
                "last_updated_utc": now(),
            }
        )
    write_tsv(LEDGER, LEDGER_HEADERS, rows)
    print(f"recorded {len(report)} worker flags for {args.packet_id}; no confidence decisions changed")


def finalize_packet(args: argparse.Namespace) -> None:
    """Move a completed worker packet out of the export pool without curating it."""
    rows = init_ledger()
    matched = [row for row in rows if row["packet_id"] == args.packet_id]
    if not matched:
        raise SystemExit(f"packet not found in ledger: {args.packet_id}")
    for row in matched:
        row["search_status"] = args.status
        if args.note:
            row["curator_disposition"] = args.note
        row["last_updated_utc"] = now()
    write_tsv(LEDGER, LEDGER_HEADERS, rows)
    print(f"updated {len(matched)} rows for {args.packet_id} to {args.status}")


def reset_queued_range(args: argparse.Namespace) -> None:
    """Return an explicitly orphaned queued range to the export pool."""
    rows = init_ledger()
    matched = [
        row
        for row in rows
        if args.first_review_id <= row["review_id"] <= args.last_review_id
        and row["search_status"] == "queued"
    ]
    if not matched:
        raise SystemExit("no queued rows matched the requested orphan range")
    for row in matched:
        row["search_status"] = "unsearched"
        row["last_iteration"] = ""
        row["packet_id"] = ""
        row["last_updated_utc"] = now()
    write_tsv(LEDGER, LEDGER_HEADERS, rows)
    print(f"reset {len(matched)} orphaned queued rows to unsearched")


def restore_manifest(args: argparse.Namespace) -> None:
    """Restore ledger packet ownership from an existing immutable manifest."""
    rows = init_ledger()
    manifest_path = OUT / f"iteration_{args.iteration:03d}" / "packet_manifest.tsv"
    manifest = read_tsv(manifest_path)
    by_id = {row["review_id"]: row for row in rows}
    restored = 0
    for packet in manifest:
        packet_rows = read_tsv(ROOT / packet["packet_path"])
        for item in packet_rows:
            ledger_row = by_id.get(item["review_id"])
            if ledger_row is None or ledger_row["pair_key"] != item["pair_key"]:
                raise SystemExit(f"manifest row mismatch: {item['review_id']}")
            ledger_row.update(
                {
                    "search_status": "queued",
                    "attempt_count": str(max(1, int(ledger_row["attempt_count"] or 0))),
                    "last_iteration": str(args.iteration),
                    "packet_id": packet["packet_id"],
                    "worker_verdict": "",
                    "source_locators": "",
                    "species_support": "",
                    "support_kind": "",
                    "evidence_summary": "",
                    "limitations": "",
                    "curator_disposition": "",
                    "last_updated_utc": now(),
                }
            )
            restored += 1
    write_tsv(LEDGER, LEDGER_HEADERS, rows)
    print(f"restored {restored} ledger rows from iteration {args.iteration:03d} manifest")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("init", help="create or refresh the persistent low-search ledger")
    export = sub.add_parser("export", help="claim and export the next disjoint search batch")
    export.add_argument("--batch-size", type=int, default=300)
    export.add_argument("--packet-size", type=int, default=50)
    export.add_argument("--iteration", type=int)
    record = sub.add_parser("record", help="validate and record one worker TSV report")
    record.add_argument("--packet-id", required=True)
    record.add_argument("--report", type=Path, required=True)
    finalize = sub.add_parser("finalize-packet", help="close a worker packet for curator review")
    finalize.add_argument("--packet-id", required=True)
    finalize.add_argument("--status", choices=["retry", "searched_pending_curator"], required=True)
    finalize.add_argument("--note", default="")
    reset = sub.add_parser("reset-queued-range", help="recover an explicitly orphaned queued range")
    reset.add_argument("--first-review-id", required=True)
    reset.add_argument("--last-review-id", required=True)
    restore = sub.add_parser("restore-manifest", help="restore packet ownership from a saved manifest")
    restore.add_argument("--iteration", type=int, required=True)
    args = parser.parse_args()
    if args.command == "init":
        print(f"initialized {len(init_ledger())} low-confidence rows at {LEDGER}")
    elif args.command == "export":
        export_batch(args)
    elif args.command == "record":
        record_report(args)
    elif args.command == "finalize-packet":
        finalize_packet(args)
    elif args.command == "restore-manifest":
        restore_manifest(args)
    else:
        reset_queued_range(args)


if __name__ == "__main__":
    main()
