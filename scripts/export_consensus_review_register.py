#!/usr/bin/env python3
"""Export a cross-module consensus review register.

The B trackers remain the source of truth for observations, claims, evidence
links, boundaries, and consensus drafts. This script creates a review layer for
walking consensus statements module-by-module without losing tracker IDs.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from export_tracker_evidence_bundle import MODULES, build_bundle, referenced_ids, validate_bundle


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "processed" / "consensus_review_register.json"
DEFAULT_MD = ROOT / "docs" / "CONSENSUS_REVIEW_REGISTER.md"


MODULE_REVIEW_NOTES = {
    "1b": {
        "review_status": "COMPLETE FIRST-PASS MATERIALIZATION",
        "module_action": "Use as the reference standard for later module consensus passes.",
        "priority": "promote with normal manuscript-style editing",
    },
    "2b": {
        "review_status": "CONSENSUS-READY FIRST PASS",
        "module_action": "Tighten scaffold statements against Module 1 lesion-anatomy boundaries before promotion.",
        "priority": "rewrite for attribution and lesion-context precision",
    },
    "3b": {
        "review_status": "CONSENSUS-READY FIRST PASS",
        "module_action": "Preserve timing, cell-population, and pathway boundaries; avoid global anti-inflammatory claims.",
        "priority": "rewrite for mechanism specificity",
    },
    "4b": {
        "review_status": "CONSENSUS-READY FIRST PASS",
        "module_action": "Separate graft survival, differentiation, integration, and functional-recovery claims.",
        "priority": "rewrite for cell-source and endpoint precision",
    },
    "5b": {
        "review_status": "CONSENSUS-READY FIRST PASS",
        "module_action": "Keep regeneration, sprouting, remyelination, relay, and activity-dependent plasticity as separate consensus families.",
        "priority": "rewrite for tract and endpoint precision",
    },
    "6b": {
        "review_status": "CONSENSUS-READY FIRST PASS",
        "module_action": "Use as the human-translation boundary layer; keep pathology, imaging, and clinical-readiness claims separated.",
        "priority": "promote after human-specific wording pass",
    },
    "7b": {
        "review_status": "CONSENSUS-READY FIRST PASS",
        "module_action": "Keep host-conditioning evidence directness explicit across implant, flap, islet, organ, wound, and SCI analogs.",
        "priority": "rewrite for cross-field translation boundaries",
    },
    "8b": {
        "review_status": "CONSENSUS-READY FIRST PASS",
        "module_action": "Treat as model-ontology consensus; rewrite generic first-pass statements into operational model-selection rules.",
        "priority": "needs statement rewrite before promotion",
    },
    "9b": {
        "review_status": "CONSENSUS-READY FIRST PASS",
        "module_action": "Treat as in vitro/ex vivo model-ontology consensus; rewrite into validation-use rules.",
        "priority": "needs statement rewrite before promotion",
    },
    "10b": {
        "review_status": "CONSENSUS-READY FIRST PASS",
        "module_action": "Treat as clinical-trial map consensus; keep registry status separate from efficacy evidence.",
        "priority": "needs trial-result linkage before strength claims",
    },
    "11b": {
        "review_status": "CONSENSUS-READY FIRST PASS",
        "module_action": "Rewrite perioperative ischemia-protection statements so they are not just topic labels plus caveats.",
        "priority": "needs statement rewrite before promotion",
    },
    "12b": {
        "review_status": "CONSENSUS-READY FIRST PASS",
        "module_action": "Keep innate immune conditioning broad; treat endotoxin/LPS as one discovery platform and route translational claims through safer host-conditioning analogs.",
        "priority": "promote after full-text confidence upgrade of direct innate-conditioning anchors",
    },
}


def module_sort_key(key: str) -> int:
    return int(key.removesuffix("b"))


def markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "|" + "|".join(["---"] * len(headers)) + "|",
    ]
    for row in rows:
        cells = [str(cell).replace("\n", " ").replace("|", "/") for cell in row]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def consensus_statement(draft: dict[str, str]) -> str:
    return draft.get("consensus_statement") or draft.get("draft_statement") or draft.get("draft_consensus_statement") or ""


def tracker_id(draft: dict[str, str]) -> str:
    return draft.get("tracker_id") or draft.get("consensus_draft_id") or draft.get("consensus_id") or "UNKNOWN"


def evidence_text(draft: dict[str, str]) -> str:
    return " ".join(str(value) for value in draft.values())


def linked_ids(draft: dict[str, str], prefix: str) -> list[str]:
    return referenced_ids(evidence_text(draft), prefix)


def confidence_profile(rows: list[dict[str, str]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        confidence = row.get("extraction_confidence") or row.get("confidence_level") or "unknown"
        counts[confidence] = counts.get(confidence, 0) + 1
    return dict(sorted(counts.items()))


def review_action(module_key: str, statement: str) -> str:
    text = statement.lower()
    if module_key == "1b":
        return "promote after prose polish"
    if "is consensus-ready as a first-pass" in text:
        return "rewrite generic placeholder into final consensus language"
    if "requires full-text" in text or "full-text" in text:
        return "hold strength claims until confidence upgrade"
    if "boundary" in text or "must distinguish" in text or "should remain" in text:
        return "promote as boundary consensus after wording pass"
    return "review for final consensus wording"


def build_register() -> dict[str, Any]:
    module_rows: list[dict[str, Any]] = []
    consensus_rows: list[dict[str, Any]] = []
    for module_key in sorted(MODULES, key=module_sort_key):
        config = MODULES[module_key]
        bundle = build_bundle(config)
        errors = validate_bundle(bundle, config)
        if errors:
            raise ValueError(f"{config.label} failed validation: {errors}")

        note = MODULE_REVIEW_NOTES[module_key]
        module_rows.append(
            {
                "module_key": module_key,
                "module": config.label,
                "source_tracker": bundle["source_tracker"],
                "review_status": note["review_status"],
                "observations": len(bundle["observations"]),
                "author_claims": len(bundle["author_claims"]),
                "evidence_links": len(bundle["evidence_links"]),
                "boundary_records": len(bundle["boundary_records"]),
                "consensus_drafts": len(bundle["consensus_drafts"]),
                "module_action": note["module_action"],
                "priority": note["priority"],
            }
        )

        observation_by_id = {row["tracker_id"]: row for row in bundle["observations"]}
        claim_by_id = {row["tracker_id"]: row for row in bundle["author_claims"]}
        boundary_by_id = {row["tracker_id"]: row for row in bundle["boundary_records"]}

        for draft in bundle["consensus_drafts"]:
            obs_ids = linked_ids(draft, f"{config.id_prefix}-O")
            claim_ids = linked_ids(draft, f"{config.id_prefix}-C")
            boundary_ids = linked_ids(draft, config.boundary_prefix)
            statement = consensus_statement(draft)
            consensus_rows.append(
                {
                    "module_key": module_key,
                    "module": config.label,
                    "consensus_id": tracker_id(draft),
                    "topic_id": draft.get("topic_id"),
                    "statement": statement,
                    "status": draft.get("status") or draft.get("readiness_status") or draft.get("sql_materialization_status") or draft.get("evidence_status"),
                    "supporting_observations": obs_ids,
                    "supporting_claims": claim_ids,
                    "boundary_records": boundary_ids,
                    "observation_count": len(obs_ids),
                    "claim_count": len(claim_ids),
                    "boundary_count": len(boundary_ids),
                    "observation_confidence": confidence_profile([observation_by_id[item] for item in obs_ids if item in observation_by_id]),
                    "claim_confidence": confidence_profile([claim_by_id[item] for item in claim_ids if item in claim_by_id]),
                    "boundary_confidence": "all boundary records" if re.search(r"all boundary records", evidence_text(draft), re.I) else f"{len([item for item in boundary_ids if item in boundary_by_id])} linked",
                    "review_action": review_action(module_key, statement),
                }
            )

    return {
        "status": "cross-module consensus review register",
        "generated_from": "validated B-tracker evidence bundles",
        "module_count": len(module_rows),
        "consensus_count": len(consensus_rows),
        "module_rows": module_rows,
        "consensus_rows": consensus_rows,
    }


def render_markdown(register: dict[str, Any]) -> str:
    module_rows = register["module_rows"]
    consensus_rows = register["consensus_rows"]
    lines = [
        "# Consensus Review Register",
        "",
        "This register is the working layer for going through consensus in each module. The B trackers remain the source of truth; this file summarizes which consensus statements are ready to promote, which need wording cleanup, and which require confidence upgrades before stronger claims.",
        "",
        f"**Coverage**: {register['module_count']} modules, {register['consensus_count']} consensus statements.",
        "",
        "## Module Pass Order",
        "",
        markdown_table(
            ["Module", "Status", "Counts", "Consensus Action", "Priority"],
            [
                [
                    row["module"],
                    row["review_status"],
                    f"{row['observations']} obs / {row['author_claims']} claims / {row['evidence_links']} links / {row['boundary_records']} boundaries / {row['consensus_drafts']} drafts",
                    row["module_action"],
                    row["priority"],
                ]
                for row in module_rows
            ],
        ),
        "",
        "## Recommended Review Sequence",
        "",
        markdown_table(
            ["Step", "Modules", "Reason"],
            [
                ["1", "Module 1B", "Use as the completed reference style for final consensus wording and materialized evidence."],
                ["2", "Modules 2B-7B", "These are closest to biological/reconstructive synthesis and should be polished into final consensus statements first."],
                ["3", "Modules 8B-10B", "These are model-system and clinical-trial ontology layers; rewrite generic boundary drafts into operational rules."],
                ["4", "Modules 11B-12B", "These support conditioning logic; refine perioperative ischemia and innate-conditioning discovery-platform boundaries before grant-facing use."],
            ],
        ),
        "",
        "## Consensus Statement Register",
        "",
    ]
    for module in module_rows:
        rows = [row for row in consensus_rows if row["module_key"] == module["module_key"]]
        lines.extend(
            [
                f"### {module['module']}",
                "",
                markdown_table(
                    ["Consensus", "Topic", "Evidence", "Review Action", "Statement"],
                    [
                        [
                            row["consensus_id"],
                            row["topic_id"],
                            f"{row['observation_count']} obs / {row['claim_count']} claims / {row['boundary_count']} boundaries",
                            row["review_action"],
                            row["statement"],
                        ]
                        for row in rows
                    ],
                ),
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json-output", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-output", type=Path, default=DEFAULT_MD)
    parser.add_argument("--check", action="store_true", help="Validate and summarize without writing files.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    register = build_register()
    if args.check:
        print(
            f"PASS consensus register: {register['module_count']} modules, "
            f"{register['consensus_count']} consensus statements"
        )
        return 0
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.md_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(json.dumps(register, indent=2) + "\n")
    args.md_output.write_text(render_markdown(register))
    print(f"Wrote {args.json_output.relative_to(ROOT)}")
    print(f"Wrote {args.md_output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
