#!/usr/bin/env python3
"""Summarize assay/readout modalities captured in tracker observations.

This report is intentionally conservative: it distinguishes explicit assay
terms from inferred endpoint families so pathway targets such as NF-kB or Nrf2
do not get mistaken for a known measurement method.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON = ROOT / "data" / "processed" / "assay_modality_report.json"
DEFAULT_MD = ROOT / "docs" / "ASSAY_MODALITY_REPORT.md"


@dataclass(frozen=True)
class AssayRule:
    label: str
    pattern: str
    status: str


ASSAY_RULES: tuple[AssayRule, ...] = (
    AssayRule("Western blot / immunoblot", r"\bwestern blot\b|\bimmunoblot\b", "explicit"),
    AssayRule("ELISA / cytokine protein assay", r"\bELISA\b|\bcytokine\b|\bchemokine\b|\bIL-6\b|\bIL-10\b|\bTNF\b|\bCXCL\b|\bCCL\b|\bRANTES\b", "mixed"),
    AssayRule("qPCR / RT-PCR / mRNA assay", r"\bqPCR\b|\bRT-PCR\b|\breal-time PCR\b|\bmRNA\b|\btranscriptional\b", "mixed"),
    AssayRule("Flow cytometry / FACS", r"\bflow cytometry\b|\bFACS\b|\bcell sorting\b", "explicit"),
    AssayRule("Single-cell RNA-seq / cell-state atlas", r"\bscRNA-seq\b|\bsingle-cell\b|\bsingle cell\b|\bsingle-nucleus\b|\bsingle nucleus\b|\bcell-state\b|\bcell state\b", "mixed"),
    AssayRule("Spatial transcriptomics / spatial atlas", r"\bspatial transcriptomic\b|\bspatial atlas\b", "mixed"),
    AssayRule("Bulk transcriptomics / GEO dataset", r"\bRNA-seq\b|\btranscriptomic\b|\bGEO\b", "mixed"),
    AssayRule("Immunostaining / histology / pathology", r"\bimmunohistochemistry\b|\bimmunofluorescence\b|\bIHC\b|\bIF\b|\bhistology\b|\bhistologic\b|\bhistopathology\b|\bneuropathology\b|\bpathology\b|\bstaining\b", "mixed"),
    AssayRule("Barrier / permeability / endothelial assay", r"\bbarrier\b|\bpermeability\b|\btight junction\b|\bBSCB\b|\bBBB\b|\bendothelial\b|\bMMP-2\b|\bMMP-9\b", "inferred"),
    AssayRule("Pathway activity / phospho-signaling assay", r"\bNF-kB activity\b|\bcaspase-?3 activity\b|\bphospho\b|\bphosphorylation\b|\bp38\b|\bAkt\b|\bGSK\b|\bSTAT\b|\bNrf2\b|\bIRF3\b", "inferred"),
    AssayRule("Genetic perturbation / knockdown assay", r"\bknockout\b|\bdeficien\w*\b|\bsiRNA\b|\bsiMyD88\b|\bsiTRIF\b|\bCRISPR\b|\bguide RNA\b", "mixed"),
    AssayRule("MRI / imaging assay", r"\bMRI\b|\bimaging\b", "mixed"),
    AssayRule("Behavioral / functional recovery assay", r"\blocomo\w*\b|\bbehavior\w*\b|\bfunctional recovery\b|\bneurologic score\b|\brecovery\b", "inferred"),
)

INNATE_MODULES = (3, 12, 13)
ADDENDUM_TRACKERS = (
    ROOT / "modules" / "Module_5A_TRACKER.md",
    ROOT / "modules" / "Module_5B_TRACKER.md",
    ROOT / "modules" / "Module_12A_TRACKER.md",
    ROOT / "modules" / "Module_12B_TRACKER.md",
    ROOT / "modules" / "Module_13A_TRACKER.md",
    ROOT / "modules" / "Module_13B_TRACKER.md",
)


def observation_text(row: dict[str, Any]) -> str:
    keys = (
        "figure_ref",
        "evidence_type",
        "outcome_type",
        "observation_value",
        "normalized_value",
        "statistics_reported",
        "source_section",
        "notes",
    )
    return " ".join(str(row.get(key, "")) for key in keys)


def module_bundle(module_num: int) -> dict[str, Any]:
    return json.loads((ROOT / "data" / "processed" / f"module{module_num}_evidence_bundle.json").read_text())


def matched_rules(text: str) -> list[str]:
    return [rule.label for rule in ASSAY_RULES if re.search(rule.pattern, text, flags=re.IGNORECASE)]


def build_report() -> dict[str, Any]:
    module_rows: list[dict[str, Any]] = []
    assay_rows: list[dict[str, Any]] = []
    unmatched_rows: list[dict[str, Any]] = []

    for module_num in INNATE_MODULES:
        bundle = module_bundle(module_num)
        observations = bundle["observations"]
        counts = {rule.label: 0 for rule in ASSAY_RULES}
        matched_count = 0
        for row in observations:
            text = observation_text(row)
            labels = matched_rules(text)
            if labels:
                matched_count += 1
                for label in labels:
                    counts[label] += 1
            else:
                unmatched_rows.append(
                    {
                        "module": f"Module {module_num}",
                        "observation_id": row["tracker_id"],
                        "outcome_type": row.get("outcome_type", ""),
                        "note": "No assay family inferred from tracker text.",
                    }
                )
        module_rows.append(
            {
                "module": f"Module {module_num}",
                "observation_count": len(observations),
                "observations_with_assay_family": matched_count,
                "observations_without_assay_family": len(observations) - matched_count,
            }
        )
        for rule in ASSAY_RULES:
            if counts[rule.label]:
                assay_rows.append(
                    {
                        "module": f"Module {module_num}",
                        "assay_family": rule.label,
                        "evidence_status": rule.status,
                        "mention_count": counts[rule.label],
                    }
                )

    addendum_text = "\n".join(path.read_text() for path in ADDENDUM_TRACKERS if path.exists())
    addendum_counts = [
        {
            "assay_family": rule.label,
            "evidence_status": rule.status,
            "mention_count": len(re.findall(rule.pattern, addendum_text, flags=re.IGNORECASE)),
        }
        for rule in ASSAY_RULES
        if re.search(rule.pattern, addendum_text, flags=re.IGNORECASE)
    ]

    return {
        "scope": "Innate-signaling-related modules 3, 12, and 13 plus targeted grant addenda in modules 5, 12, and 13.",
        "interpretation_note": "Counts are tracker-text mentions, not source-level assay re-extractions. Mixed/inferred labels require full-text confirmation before gold assay claims.",
        "module_summary": module_rows,
        "module_assay_counts": assay_rows,
        "targeted_addendum_assay_mentions": addendum_counts,
        "unmatched_observations": unmatched_rows,
    }


def markdown_table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "|" + "|".join(["---"] * len(headers)) + "|",
    ]
    for row in rows:
        cells = [str(cell).replace("\n", " ").replace("|", "/") for cell in row]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def write_markdown(report: dict[str, Any], path: Path) -> None:
    lines = [
        "# Assay Modality Report",
        "",
        f"Scope: {report['scope']}",
        "",
        f"Interpretation note: {report['interpretation_note']}",
        "",
        "## Module Coverage",
        "",
        markdown_table(
            ["Module", "Observations", "With Assay Family", "Without Assay Family"],
            [
                [
                    row["module"],
                    row["observation_count"],
                    row["observations_with_assay_family"],
                    row["observations_without_assay_family"],
                ]
                for row in report["module_summary"]
            ],
        ),
        "",
        "## Assay Family Counts",
        "",
        markdown_table(
            ["Module", "Assay Family", "Evidence Status", "Mention Count"],
            [
                [row["module"], row["assay_family"], row["evidence_status"], row["mention_count"]]
                for row in report["module_assay_counts"]
            ],
        ),
        "",
        "## Targeted Grant Addendum Mentions",
        "",
        markdown_table(
            ["Assay Family", "Evidence Status", "Mention Count"],
            [
                [row["assay_family"], row["evidence_status"], row["mention_count"]]
                for row in report["targeted_addendum_assay_mentions"]
            ],
        ),
        "",
        "## Unmatched Observations",
        "",
        markdown_table(
            ["Module", "Observation ID", "Outcome Type", "Note"],
            [
                [row["module"], row["observation_id"], row["outcome_type"], row["note"]]
                for row in report["unmatched_observations"]
            ],
        ),
        "",
    ]
    path.write_text("\n".join(lines))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    report = build_report()
    if args.check:
        if not report["module_assay_counts"]:
            raise SystemExit("No assay modality counts generated")
        print(
            "PASS assay modality report: "
            f"{len(report['module_assay_counts'])} module assay rows, "
            f"{len(report['targeted_addendum_assay_mentions'])} addendum assay rows"
        )
        return 0
    DEFAULT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    write_markdown(report, DEFAULT_MD)
    print(f"Wrote {DEFAULT_JSON.relative_to(ROOT)}")
    print(f"Wrote {DEFAULT_MD.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
